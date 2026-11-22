from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, RedirectResponse, Response
from starlette.middleware.gzip import GZipMiddleware
from openai import AsyncOpenAI
from urllib.parse import quote, urlencode, urlparse
import asyncio
import hashlib
import html
import httpx
import json
import logging
import os
import re
import secrets
import tempfile
import time
from datetime import datetime, timezone

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=500)

log = logging.getLogger("tripassembler")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(ROOT_DIR, "static")
LEGACY_DIR = os.path.join(ROOT_DIR, "legacy_pages")
STYLES_PATH = os.path.join(STATIC_DIR, "styles.css")
HOME_TEMPLATE = os.path.join(STATIC_DIR, "home.html")

PAGES_DIR = os.getenv("PAGES_DIR", "/opt/render/project/src/pages")
INDEX_FILE = os.getenv("INDEX_FILE", "/opt/render/project/src/index.json")
BASE_URL = os.getenv("BASE_URL", "https://tripassembler.onrender.com")
os.makedirs(PAGES_DIR, exist_ok=True)

# Async client: the request loop stays free while a trip is generated.
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY") or "missing", timeout=45.0)
MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")

# Maps Embed API allows up to 20 intermediate waypoints plus origin and destination.
MAX_WAYPOINTS = 20
MODEL = "gpt-4o-mini"
MAX_OUTPUT_TOKENS = 2400

# In-process jobs are enough for a single Render instance. A restart forgets them.
JOBS = {}
JOB_TTL_SECONDS = 60 * 60
JOB_TIMEOUT_SECONDS = 90
_background_tasks = set()

WIKI_UA = "TripAssembler/1.0 (https://www.tripassembler.com/; trip page images) httpx"
WIKI_API = "https://en.wikipedia.org/w/api.php"
WIKI_SUMMARY = "https://en.wikipedia.org/api/rest_v1/page/summary/"
_IMAGE_POSITIVE_TTL = 30 * 24 * 3600
_IMAGE_NEGATIVE_TTL = 6 * 3600
_image_cache = {}
_cache_loaded = False

# Served pages (legacy files and older generated HTML) get one pass that adds
# photos, related trips, and the current tagline. The marker makes that pass idempotent.
TAGLINE = "Assemble the perfect Trip"
ENHANCED_MARKER = "<!-- ta-enhanced -->"
ENHANCE_TIMEOUT = 6.0
RELATED_LIMIT = 6
_page_mem = {}
_page_locks = {}
_catalog = {"key": None, "items": []}
_popular_slugs = None
_OLD_TAGLINE_RE = re.compile(r"Assemble the perfect stay", re.I)

_TOKEN_RE = re.compile(r"%%[A-Z_]+%%")
_SLUG_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,180}")
_WHEN_RE = re.compile(
    r"\d|week|night|day|weekend|month|flexible|"
    r"jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec",
    re.I,
)
_STRENGTH_TIPS = {
    "where": "Add a destination so we know where to plan.",
    "when": "Add how many nights for a better day-by-day plan.",
    "who": "Say who\u2019s coming so the stays fit your group.",
    "budget": "Add a nightly budget so picks match what you want to spend.",
    "must": "Add one must-have \u2014 walkable, a kitchen, quiet, the beach.",
}
_STRENGTH_LABELS = [
    "Add a destination",
    "Just started",
    "Fill in a few more details",
    "Good shape",
    "Strong",
    "Ready to assemble",
]
_STRENGTH_DONE = "This is enough detail for a strong day-by-day plan."
EXAMPLE_FIELDS = {
    "where": "Reykjavik, Iceland",
    "budget": "$150\u2013300/night",
    "who": "Couple",
    "must": "Walkable, Kitchen, Great food scene",
    "when": "5 nights in June",
    "interests": "Relaxed pace, Food, Nature",
}

PROMPT = """You are an expert travel planner. Return ONLY JSON for the trip request below.

Schema:
{
  "title": "appealing title",
  "location": "City or region, Country",
  "wiki_title": "English Wikipedia article for the destination, or empty",
  "summary": "2-3 sentence overview",
  "constraints": ["constraint", "constraint", "constraint"],
  "hotels": [
    {"name": "", "why": "", "price_range": "$ per night", "area": "neighborhood", "url": "https://"}
  ],
  "itinerary": [
    {"day": 1, "title": "theme", "description": "2 sentences", "activities": ["specific", "specific", "specific"], "tips": "practical tip", "activity_urls": ["https://"], "wiki_title": "English Wikipedia article for the day's main sight, or empty"}
  ],
  "map_places": [
    {"name": "Place", "city": "City", "country": "Country", "wiki_title": "English Wikipedia article title, or empty"}
  ],
  "faqs": [{"question": "", "answer": ""}],
  "transport": "how to get around",
  "budget_notes": "realistic budget guidance"
}

Rules:
- Match the requested destination, length, budget, group, and must-haves.
- 2 or 3 real hotels or apartments with believable nightly prices and a booking or official URL.
- Itinerary length matches the request. Each day: short description, 3 specific activities, one tip.
- map_places: 4 to 6 on-the-ground stops in visit order, inside the destination only. No home airports or overseas connections.
- wiki_title fields are exact English Wikipedia article titles when you know them, otherwise "".
- 3 short practical FAQs.
- JSON only.

Trip request:
"""


def _styles_version():
    if not os.path.isfile(STYLES_PATH):
        return "0"
    digest = hashlib.sha256()
    with open(STYLES_PATH, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()[:10]


STYLES_VERSION = _styles_version()
STYLES_HREF = f"/styles.css?v={STYLES_VERSION}"


def _default_wiki_cache():
    env = os.getenv("WIKI_CACHE")
    if env:
        return env
    parent = os.path.dirname(PAGES_DIR)
    if parent and os.path.isdir(parent) and os.path.realpath(parent) != os.path.realpath(ROOT_DIR):
        return os.path.join(parent, "wiki_image_cache.json")
    return os.path.join(tempfile.gettempdir(), "tripassembler_wiki_cache.json")


WIKI_CACHE_PATH = _default_wiki_cache()


def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE) as f:
            return json.load(f)
    return []


def save_index(data):
    directory = os.path.dirname(INDEX_FILE)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(INDEX_FILE, "w") as f:
        json.dump(data, f, indent=2)


def esc(value):
    """HTML-escape user/LLM text and neutralize braces so str.format stays safe."""
    return html.escape(str(value or "")).replace("{", "&#123;").replace("}", "&#125;")


def safe_url(url):
    """Allow only absolute http(s) URLs; return an attribute-safe escaped string."""
    if not url:
        return ""
    url = str(url).strip()
    if url.startswith("https://") or url.startswith("http://"):
        return html.escape(url, quote=True)
    return ""


def slugify(text, max_len=70):
    text = (text or "").lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text[:max_len].strip("-") or "trip"


def clean_field(value, limit):
    return " ".join(str(value or "").split())[:limit].strip()


def opt_text(value, limit=160):
    if value is None:
        return ""
    text = " ".join(str(value).split())
    if text.lower() in {"none", "null", "n/a", "na", "-"}:
        return ""
    return text[:limit].strip()


def fields_from(where="", budget="", who="", must="", when="", interests=""):
    return {
        "where": clean_field(where, 180),
        "budget": clean_field(budget, 240),
        "who": clean_field(who, 240),
        "must": clean_field(must, 400),
        "when": clean_field(when, 240),
        "interests": clean_field(interests, 240),
    }


def compose_request(where="", budget="", who="", must="", when="", interests="", request=""):
    """Turn the home form into one structured planner request."""
    labeled = [
        ("Where", where),
        ("Budget", budget),
        ("Who's coming and space needed", who),
        ("Must-haves and vibe", must),
        ("Timing and other notes", when),
        ("Pace and interests", interests),
    ]
    lines = ["Plan a trip with these constraints:"]
    wrote = False
    for label, value in labeled:
        text = " ".join(str(value or "").split())
        if text:
            wrote = True
            lines.append(f"{label}: {text}")
    extra = " ".join(str(request or "").split())
    if extra:
        wrote = True
        lines.append(extra)
    if not wrote:
        return "Plan a trip with these constraints:\nWhere: a trip"
    return "\n".join(lines)


def trip_strength(where="", budget="", who="", must="", when="", interests=""):
    """Score the details that change plan quality. Order is the next tip to show."""
    have = {
        "where": len((where or "").strip()) > 1,
        "when": bool(_WHEN_RE.search(when or "")),
        "who": bool((who or "").strip()),
        "budget": bool((budget or "").strip()),
        "must": bool((must or "").strip() or (interests or "").strip()),
    }
    order = ["where", "when", "who", "budget", "must"]
    score = sum(1 for key in order if have[key])
    tip = _STRENGTH_DONE
    for key in order:
        if not have[key]:
            tip = _STRENGTH_TIPS[key]
            break
    return {"score": score, "tip": tip, "label": _STRENGTH_LABELS[score]}


def retry_query(fields):
    pairs = []
    for key in ("where", "budget", "who", "must", "when", "interests"):
        value = str((fields or {}).get(key) or "").strip()
        if value:
            pairs.append((key, value[:300]))
    return "/?" + urlencode(pairs) if pairs else "/"


def fill_template(doc, mapping):
    return _TOKEN_RE.sub(lambda match: mapping.get(match.group(0), match.group(0)), doc)


def _inside(path, directory):
    real = os.path.realpath(path)
    root = os.path.realpath(directory)
    return real == root or real.startswith(root + os.sep)


def legacy_slugs():
    if not os.path.isdir(LEGACY_DIR):
        return []
    slugs = []
    for name in os.listdir(LEGACY_DIR):
        if not name.endswith(".html"):
            continue
        slug = name[:-5]
        if _SLUG_RE.fullmatch(slug):
            slugs.append(slug)
    slugs.sort()
    return slugs


def resolve_page_file(raw):
    """Generated page on the persistent disk, then a legacy page, else nothing."""
    name = raw[:-5] if raw.endswith(".html") else raw
    if not _SLUG_RE.fullmatch(name):
        return None
    generated = os.path.join(PAGES_DIR, name + ".html")
    legacy = os.path.join(LEGACY_DIR, name + ".html")
    if os.path.isfile(generated) and _inside(generated, PAGES_DIR):
        return generated
    if os.path.isfile(legacy) and _inside(legacy, LEGACY_DIR):
        return legacy
    return None


def place_to_str(place):
    """Coerce a map_places item (string or dict) to a single label."""
    if isinstance(place, str):
        return " ".join(place.split()).strip(" ,")
    if isinstance(place, dict):
        parts = [
            place.get("name") or place.get("place") or place.get("title"),
            place.get("city") or place.get("area") or place.get("region"),
            place.get("country"),
        ]
        return ", ".join(str(p).strip() for p in parts if p and str(p).strip())
    return str(place or "").strip()


def _raw_items(raw_places):
    if not raw_places:
        return []
    if isinstance(raw_places, str):
        if "\n" in raw_places or " | " in raw_places or ";" in raw_places:
            return re.split(r"[\n;]| \| ", raw_places)
        return [raw_places]
    if isinstance(raw_places, (list, tuple)):
        return list(raw_places)
    return []


def _clean_records(raw_places, location=""):
    """Stops as labels plus an optional Wikipedia title. Same de-dupe rules as before."""
    location = " ".join(str(location or "").split()).strip()
    if location.lower() in {"see request", "travel"}:
        location = ""
    records = []
    seen = set()
    for item in _raw_items(raw_places):
        label = place_to_str(item)
        wiki = ""
        if isinstance(item, dict):
            wiki = opt_text(item.get("wiki_title") or item.get("image_hint"), 120)
        if not label:
            continue
        if location and location.lower() not in label.lower():
            label = f"{label}, {location}"
        key = re.sub(r"\s+", " ", label).casefold()
        if key in seen:
            continue
        seen.add(key)
        records.append({"label": label, "wiki_title": wiki})

    max_points = MAX_WAYPOINTS + 2
    if len(records) > max_points:
        middle = records[1:-1]
        keep = MAX_WAYPOINTS
        step = len(middle) / keep
        sampled = [middle[int(i * step)] for i in range(keep)]
        out = [records[0]]
        seen_mid = {records[0]["label"].casefold(), records[-1]["label"].casefold()}
        for item in sampled:
            if item["label"].casefold() not in seen_mid:
                out.append(item)
                seen_mid.add(item["label"].casefold())
        out.append(records[-1])
        records = out
    return records


def normalize_places(raw_places, location=""):
    """
    Turn LLM map_places into a clean, de-duplicated list of 'Name, City, Country' strings.
    A string (not a list) is a common JSON mistake; never treat it as a character sequence.
    """
    return [record["label"] for record in _clean_records(raw_places, location)]


def encode_place(place):
    # Docs use unescaped commas and '+' for spaces (e.g. City+Hall,New+York,NY).
    # Still encode '|', '&', '#' and other reserved characters.
    place = re.sub(r"\s*,\s*", ",", place)
    place = re.sub(r"\s+", " ", place).strip()
    return quote(place.replace(" ", "+"), safe=",+")


def build_map_urls(places, location=""):
    """Return (embed_url, open_in_maps_url). embed_url is empty when no API key."""
    context = (location or "").strip() or "travel"
    open_url = f"https://www.google.com/maps/search/?api=1&query={encode_place(places[0] if places else context)}"

    if len(places) >= 2:
        origin = encode_place(places[0])
        destination = encode_place(places[-1])
        waypoints = "|".join(encode_place(p) for p in places[1:-1])
        open_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&origin={origin}&destination={destination}"
        )
        if waypoints:
            open_url += f"&waypoints={waypoints}"
        if MAPS_KEY:
            embed = (
                f"https://www.google.com/maps/embed/v1/directions?key={MAPS_KEY}"
                f"&origin={origin}&destination={destination}"
            )
            if waypoints:
                embed += f"&waypoints={waypoints}"
            return embed, open_url

    query = encode_place(places[0] if places else context)
    if MAPS_KEY:
        embed = f"https://www.google.com/maps/embed/v1/place?key={MAPS_KEY}&q={query}"
        return embed, open_url
    return "", open_url


def _wiki_host(url):
    host = (urlparse(url).hostname or "").lower()
    return host == "wikipedia.org" or host.endswith(".wikipedia.org") or host.endswith(".wikimedia.org")


def _wiki_image(src, width, height, page, title):
    src = str(src or "").strip()
    if not src.startswith("https://") or not _wiki_host(src):
        return None
    try:
        w = int(width)
        h = int(height)
    except (TypeError, ValueError):
        return None
    if w < 80 or h < 80:
        return None
    w = min(w, 2000)
    h = min(h, 2000)
    page_url = str(page or "").strip()
    if not (page_url.startswith("https://") and _wiki_host(page_url)):
        page_url = ""
    return {
        "src": src,
        "width": w,
        "height": h,
        "page": page_url,
        "title": str(title or "").strip(),
    }


def _parse_query(data):
    if not isinstance(data, dict):
        return None
    pages = (data.get("query") or {}).get("pages") or {}
    if not isinstance(pages, dict):
        return None
    # generator=search includes an index. Page ids are not relevance order, and the
    # top hit often has no thumbnail (a list or a disambiguation).
    ordered = sorted(
        (page for page in pages.values() if isinstance(page, dict)),
        key=lambda page: page.get("index") if isinstance(page.get("index"), int) else 0,
    )
    for page in ordered:
        if not isinstance(page, dict) or "missing" in page:
            continue
        thumb = page.get("thumbnail") or {}
        image = _wiki_image(
            thumb.get("source"),
            thumb.get("width"),
            thumb.get("height"),
            page.get("fullurl"),
            page.get("title"),
        )
        if image:
            return image
    return None


def wiki_client():
    return httpx.AsyncClient(
        timeout=httpx.Timeout(3.0, connect=2.0),
        headers={
            "User-Agent": WIKI_UA,
            "Api-User-Agent": WIKI_UA,
            "Accept": "application/json",
        },
        follow_redirects=True,
    )


async def _get_json(http, url, params=None):
    try:
        response = await http.get(url, params=params)
    except httpx.HTTPError:
        return None
    if response.status_code != 200:
        return None
    try:
        return response.json()
    except ValueError:
        return None


async def fetch_by_title(http, title):
    """Exact article via the MediaWiki API, asking for a 640px thumbnail."""
    data = await _get_json(http, WIKI_API, {
        "action": "query",
        "titles": title,
        "prop": "pageimages|info",
        "inprop": "url",
        "pithumbsize": "640",
        "redirects": "1",
        "format": "json",
    })
    return _parse_query(data)


async def fetch_summary(http, title):
    """REST summary fallback. No API key; thumbnail is whatever Wikipedia serves."""
    url = WIKI_SUMMARY + quote(title.replace(" ", "_"), safe="")
    data = await _get_json(http, url)
    if not isinstance(data, dict) or data.get("type") == "disambiguation":
        return None
    thumb = data.get("thumbnail") or {}
    desktop = (data.get("content_urls") or {}).get("desktop") or {}
    return _wiki_image(
        thumb.get("source"),
        thumb.get("width"),
        thumb.get("height"),
        desktop.get("page"),
        data.get("title") or title,
    )


async def fetch_search(http, query):
    data = await _get_json(http, WIKI_API, {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": "5",
        "prop": "pageimages|info",
        "inprop": "url",
        "pithumbsize": "640",
        "format": "json",
    })
    return _parse_query(data)


async def lookup_image(http, wiki_title="", query=""):
    """One image for a stop or destination. Misses return None and never raise."""
    title = opt_text(wiki_title, 120)
    query = opt_text(query, 160)
    image = None
    if title:
        image = await fetch_by_title(http, title)
        if not image:
            image = await fetch_summary(http, title)
    if not image:
        search_for = query or title
        if search_for and (not title or search_for.casefold() != title.casefold()):
            image = await fetch_search(http, search_for)
    return image


def image_cache_key(wiki_title, query):
    title = opt_text(wiki_title, 120).casefold()
    if title:
        return "title:" + title
    text = opt_text(query, 160).casefold()
    return "search:" + text if text else ""


def _load_image_cache():
    global _cache_loaded
    if _cache_loaded:
        return
    _cache_loaded = True
    try:
        with open(WIKI_CACHE_PATH, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError):
        return
    if not isinstance(data, dict):
        return
    now = time.time()
    for key, item in data.items():
        if not isinstance(item, dict) or not item.get("image"):
            continue
        if now - float(item.get("at") or 0) > _IMAGE_POSITIVE_TTL:
            continue
        _image_cache[key] = item


def _save_image_cache():
    try:
        directory = os.path.dirname(WIKI_CACHE_PATH)
        if directory:
            os.makedirs(directory, exist_ok=True)
        positive = {key: value for key, value in _image_cache.items() if value.get("image")}
        temporary = WIKI_CACHE_PATH + ".tmp"
        with open(temporary, "w", encoding="utf-8") as handle:
            json.dump(positive, handle)
        os.replace(temporary, WIKI_CACHE_PATH)
    except OSError:
        log.warning("could not persist wikipedia image cache", exc_info=True)


def remember_image(image, slug="", *labels):
    """Keep a positive hit under a page slug and plain-text place names."""
    if not isinstance(image, dict) or not image.get("src"):
        return
    _load_image_cache()
    now = time.time()
    changed = False
    if slug and _SLUG_RE.fullmatch(slug):
        _image_cache["slug:" + slug.casefold()] = {"at": now, "image": image}
        changed = True
    for label in labels:
        key = image_cache_key("", label)
        if not key:
            continue
        existing = _image_cache.get(key)
        if isinstance(existing, dict) and existing.get("image"):
            continue
        _image_cache[key] = {"at": now, "image": image}
        changed = True
    if changed:
        _save_image_cache()


def cache_get(key):
    _load_image_cache()
    item = _image_cache.get(key)
    if not item:
        return None, False
    age = time.time() - float(item.get("at") or 0)
    ttl = _IMAGE_POSITIVE_TTL if item.get("image") else _IMAGE_NEGATIVE_TTL
    if age > ttl:
        _image_cache.pop(key, None)
        return None, False
    return item.get("image"), True


async def resolve_images(specs, timeout=8.0):
    """Look up many images at once. Each call is capped; the whole batch is capped too."""
    _load_image_cache()
    results = {}
    groups = {}
    order = []
    for key, wiki, query in specs:
        cache_key = image_cache_key(wiki, query)
        if not cache_key:
            continue
        groups.setdefault(cache_key, {"keys": [], "wiki": wiki, "query": query})
        groups[cache_key]["keys"].append(key)
        if cache_key not in order:
            order.append(cache_key)

    pending = []
    for cache_key in order:
        image, hit = cache_get(cache_key)
        if hit:
            if image:
                for key in groups[cache_key]["keys"]:
                    results[key] = image
            continue
        pending.append(cache_key)
    pending = pending[:12]
    if not pending:
        return results

    async def one(http, cache_key):
        group = groups[cache_key]
        try:
            image = await lookup_image(http, wiki_title=group["wiki"], query=group["query"])
        except asyncio.CancelledError:
            raise
        except Exception:
            log.info("wikipedia lookup failed for %s", cache_key, exc_info=True)
            image = None
        _image_cache[cache_key] = {"at": time.time(), "image": image}
        return cache_key, image

    try:
        async with wiki_client() as http:
            sem = asyncio.Semaphore(4)

            async def limited(cache_key):
                async with sem:
                    return await one(http, cache_key)

            tasks = [asyncio.create_task(limited(cache_key)) for cache_key in pending]
            done, not_done = await asyncio.wait(tasks, timeout=timeout)
            for task in not_done:
                task.cancel()
            for task in not_done:
                try:
                    await task
                except (asyncio.CancelledError, Exception):
                    pass
            for task in done:
                if task.cancelled():
                    continue
                exc = task.exception()
                if exc:
                    continue
                cache_key, image = task.result()
                if not image:
                    continue
                for key in groups[cache_key]["keys"]:
                    results[key] = image
    except Exception:
        log.warning("wikipedia image batch failed", exc_info=True)
    _save_image_cache()
    return results


async def attach_images(assembly, records):
    specs = []
    hero_wiki = opt_text(assembly.get("wiki_title"), 120)
    location = opt_text(assembly.get("location"), 160)
    if hero_wiki or location:
        specs.append(("hero", hero_wiki, hero_wiki or location))
    for index, record in enumerate(records[:8]):
        wiki = opt_text(record.get("wiki_title"), 120)
        label = record.get("label") or ""
        if wiki or label:
            specs.append((f"stop:{index}", wiki, label or wiki))
    itinerary = assembly.get("itinerary") if isinstance(assembly.get("itinerary"), list) else []
    for index, day in enumerate(itinerary):
        if not isinstance(day, dict):
            continue
        wiki = opt_text(day.get("wiki_title"), 120)
        if wiki:
            specs.append((f"day:{index}", wiki, wiki))
    try:
        found = await resolve_images(specs)
    except Exception:
        log.warning("image attachment failed", exc_info=True)
        found = {}
    if found.get("hero"):
        assembly["hero_image"] = found["hero"]
        remember_image(
            found["hero"],
            "",
            hero_wiki,
            location,
            hero_wiki or location,
        )
    for index, record in enumerate(records[:8]):
        image = found.get(f"stop:{index}")
        if image:
            record["image"] = image
    for index, day in enumerate(itinerary):
        if isinstance(day, dict) and found.get(f"day:{index}"):
            day["image"] = found[f"day:{index}"]


def photo_figure(image, alt, css_class):
    if css_class not in {"hero-photo", "day-photo"} or not isinstance(image, dict):
        return ""
    src = safe_url(image.get("src"))
    if not src:
        return ""
    try:
        width = int(image.get("width") or 640)
        height = int(image.get("height") or 480)
    except (TypeError, ValueError):
        width, height = 640, 480
    alt_text = str(image.get("title") or alt or "Trip photo")
    page = safe_url(image.get("page"))
    caption = ""
    if page:
        caption = (
            f'<figcaption><a href="{page}" target="_blank" rel="noopener noreferrer">'
            f'{esc(image.get("title") or alt_text)}</a> · Wikipedia</figcaption>'
        )
    return (
        f'<figure class="{css_class}">'
        f'<img src="{src}" width="{width}" height="{height}" alt="{esc(alt_text)}" '
        f'loading="lazy" decoding="async">'
        f"{caption}</figure>"
    )


def stop_li_html(label, image=None):
    """One route stop, with a Wikipedia thumbnail when we have one."""
    maps = "https://www.google.com/maps/search/?api=1&query=" + encode_place(label)
    thumb = ""
    attr = ""
    if isinstance(image, dict):
        src = safe_url(image.get("src"))
        if src:
            try:
                width = int(image.get("width") or 640)
                height = int(image.get("height") or 480)
            except (TypeError, ValueError):
                width, height = 640, 480
            thumb = (
                f'<img class="stop-thumb" src="{src}" width="{width}" height="{height}" '
                f'alt="{esc(image.get("title") or label)}" loading="lazy" decoding="async">'
            )
            page = safe_url(image.get("page"))
            if page:
                attr = (
                    f'<div class="wiki-attr-line"><a href="{page}" target="_blank" '
                    f'rel="noopener noreferrer">{esc(image.get("title") or label)}</a>'
                    f" · Wikipedia</div>"
                )
    return (
        f'<li class="stop">{thumb}<div class="stop-body">'
        f'<a href="{html.escape(maps, quote=True)}" target="_blank" rel="noopener noreferrer">{esc(label)}</a>'
        f"{attr}</div></li>"
    )


def map_block_html(records, location, map_url, open_url):
    items = []
    for record in records:
        if isinstance(record, dict):
            label = record.get("label") or ""
            image = record.get("image")
        else:
            label = str(record or "")
            image = None
        if not label:
            continue
        items.append(stop_li_html(label, image))
    stops_html = f'<ol class="stops">{"".join(items)}</ol>' if items else ""
    iframe = ""
    if map_url:
        iframe = (
            f'<div class="map-container">'
            f'<iframe src="{html.escape(map_url, quote=True)}" allowfullscreen loading="lazy" '
            f'referrerpolicy="strict-origin-when-cross-origin" title="Itinerary route map"></iframe>'
            f"</div>"
        )
    links = []
    if open_url:
        label = "Open route in Google Maps" if len(records) >= 2 else "Open in Google Maps"
        links.append(
            f'<a href="{html.escape(open_url, quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>'
        )
    link_html = f'<p class="map-links">{" · ".join(links)}</p>' if links else ""
    heading = "<h2>Route map</h2>" if (iframe or stops_html) else ""
    return heading + iframe + link_html + stops_html


def hotels_to_html(hotels):
    parts = []
    for h in hotels or []:
        if not isinstance(h, dict):
            continue
        url = safe_url(h.get("url"))
        link = f' <a href="{url}" target="_blank" rel="noopener noreferrer">Book / View</a>' if url else ""
        parts.append(
            "<p><strong>{}</strong> ({}) — {} ({}){}</p>".format(
                esc(h.get("name", "")),
                esc(h.get("area", "")),
                esc(h.get("why", "")),
                esc(h.get("price_range", "")),
                link,
            )
        )
    return "".join(parts)


def itinerary_to_html(itinerary):
    parts = []
    for d in itinerary or []:
        if not isinstance(d, dict):
            continue
        activities = d.get("activities") or []
        if isinstance(activities, str):
            activities = [activities]
        elif not isinstance(activities, list):
            activities = []
        urls = d.get("activity_urls") or []
        if not isinstance(urls, list):
            urls = []
        lis = []
        for i, activity in enumerate(activities):
            url = safe_url(urls[i] if i < len(urls) else "")
            text = esc(activity)
            if url:
                lis.append(
                    f'<li>{text} <a href="{url}" target="_blank" rel="noopener noreferrer">Info</a></li>'
                )
            else:
                lis.append(f"<li>{text}</li>")
        description = d.get("description") or ""
        desc_html = f"<p>{esc(description)}</p>" if description else ""
        tips = d.get("tips") or ""
        tips_html = f"<p><em>{esc(tips)}</em></p>" if tips else ""
        photo = photo_figure(d.get("image"), str(d.get("title") or "Itinerary day"), "day-photo")
        parts.append(
            f'<div class="day">{photo}<h3>Day {esc(d.get("day", "?"))}: {esc(d.get("title", ""))}</h3>'
            f"{desc_html}"
            f'<ul>{"".join(lis)}</ul>'
            f"{tips_html}</div>"
        )
    return "".join(parts)


def related_to_html(index, slug, location, limit=RELATED_LIMIT, title=""):
    """Related-trip cards. `index` is unused; the pool is legacy pages plus index.json."""
    return related_section_html(slug, title, location, limit=limit)


def build_json_ld(page_url, title, summary, location, itinerary, faqs, image_url=""):
    elements = []
    for i, d in enumerate(itinerary or [], start=1):
        if not isinstance(d, dict):
            continue
        name = f"Day {d.get('day', i)}: {d.get('title', '')}".strip()
        elements.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "description": d.get("description") or d.get("tips") or "",
        })
    trip = {
        "@type": "TouristTrip",
        "name": title,
        "description": summary,
        "touristType": "Leisure",
        "url": page_url,
        "itinerary": {
            "@type": "ItemList",
            "name": f"{title} itinerary",
            "itemListElement": elements,
        },
    }
    if image_url:
        trip["image"] = image_url
    graph = [
        trip,
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "TripAssembler", "item": BASE_URL + "/"},
                {"@type": "ListItem", "position": 2, "name": title, "item": page_url},
            ],
        },
    ]
    if location:
        graph[0]["touristDestination"] = {"@type": "Place", "name": location}
    clean_faqs = []
    for faq in faqs or []:
        if isinstance(faq, dict) and faq.get("question") and faq.get("answer"):
            clean_faqs.append({
                "@type": "Question",
                "name": str(faq["question"]),
                "acceptedAnswer": {"@type": "Answer", "text": str(faq["answer"])},
            })
    if clean_faqs:
        graph.append({"@type": "FAQPage", "mainEntity": clean_faqs})
    payload = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    return payload.replace("</", "<\\/")


def faqs_to_html(faqs):
    parts = []
    for faq in faqs or []:
        if not isinstance(faq, dict) or not faq.get("question") or not faq.get("answer"):
            continue
        parts.append(f"<h3>{esc(faq['question'])}</h3><p>{esc(faq['answer'])}</p>")
    if not parts:
        return ""
    return "<h2>Planning FAQs</h2>" + "".join(parts)


def meta_description(summary, max_len=155):
    text = " ".join(str(summary or "").split())
    if len(text) <= max_len:
        return text
    cut = text[: max_len - 1].rsplit(" ", 1)[0]
    return cut.rstrip(".,;:") + "…"


def render_home(error="", values=None):
    values = values or {}
    strength = trip_strength(
        values.get("where", ""),
        values.get("budget", ""),
        values.get("who", ""),
        values.get("must", ""),
        values.get("when", ""),
        values.get("interests", ""),
    )
    with open(HOME_TEMPLATE, encoding="utf-8") as handle:
        doc = handle.read()
    error_html = f'<div class="card error-card"><p>{esc(error)}</p></div>' if error else ""
    label = f"{strength['label']} \u00b7 {strength['score']}/5"
    return fill_template(doc, {
        "%%ERROR%%": error_html,
        "%%BASE_URL%%": html.escape(BASE_URL, quote=True),
        "%%STYLES%%": html.escape(STYLES_HREF, quote=True),
        "%%WHERE%%": html.escape(values.get("where", ""), quote=True),
        "%%BUDGET%%": html.escape(values.get("budget", ""), quote=True),
        "%%WHO%%": html.escape(values.get("who", ""), quote=True),
        "%%MUST%%": html.escape(values.get("must", "")),
        "%%WHEN%%": html.escape(values.get("when", ""), quote=True),
        "%%INTERESTS%%": html.escape(values.get("interests", ""), quote=True),
        "%%SCORE%%": str(strength["score"]),
        "%%SCORE_PCT%%": str(strength["score"] * 20),
        "%%STRENGTH_LABEL%%": esc(label),
        "%%STRENGTH_TIP%%": esc(strength["tip"]),
    })


BRAND_SVG = (
    '<svg class="logo-svg" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg">'
    '<rect width="36" height="36" rx="8" fill="#1e40af"/>'
    '<path d="M8 22 L18 10 L28 22" stroke="white" stroke-width="2.5" fill="none" '
    'stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="18" cy="24" r="2" fill="white"/>'
    "</svg>"
)
CRITICAL_CSS = (
    '<style>body{margin:0;background:#f8fafc;color:#0f172a;'
    'font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}</style>'
)
ICON_HTML = (
    '<div class="page-icon">'
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1e40af" stroke-width="2">'
    '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>'
    '<circle cx="12" cy="10" r="3"/></svg></div>'
)

PROGRESS_PANEL = """
<div class="card stage-card">
  <div class="route-wrap" aria-hidden="true">
    <svg class="route-svg" viewBox="0 0 420 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A route being drawn between stops">
      <path class="route-guide" d="M36 146C78 146 96 70 132 74C176 80 168 132 214 126C260 120 258 58 300 62C338 66 348 112 384 108"></path>
      <path class="route-line" pathLength="100" d="M36 146C78 146 96 70 132 74C176 80 168 132 214 126C260 120 258 58 300 62C338 66 348 112 384 108"></path>
      <g class="pin pin-1"><circle cx="36" cy="146" r="8"></circle><circle class="pin-core" cx="36" cy="146" r="3"></circle></g>
      <g class="pin pin-2"><circle cx="132" cy="74" r="8"></circle><circle class="pin-core" cx="132" cy="74" r="3"></circle></g>
      <g class="pin pin-3"><circle cx="214" cy="126" r="8"></circle><circle class="pin-core" cx="214" cy="126" r="3"></circle></g>
      <g class="pin pin-4"><circle cx="300" cy="62" r="8"></circle><circle class="pin-core" cx="300" cy="62" r="3"></circle></g>
      <g class="pin pin-5"><circle cx="384" cy="108" r="8"></circle><circle class="pin-core" cx="384" cy="108" r="3"></circle></g>
      <circle class="traveler" cx="0" cy="0" r="5"></circle>
    </svg>
  </div>
  <p class="stage-current" id="stageCurrent" aria-live="polite">Reading your constraints…</p>
  <ol class="stage-list" id="stageList">
    <li class="is-on">Reading your constraints…</li>
    <li>Picking the best area to stay…</li>
    <li>Finding stays that match…</li>
    <li>Mapping your stops…</li>
    <li>Writing your day-by-day plan…</li>
  </ol>
</div>
"""

PROGRESS_SCRIPT = """
<script>
(function () {
  var jobId = "__JOB_ID__";
  var stages = [
    "Reading your constraints…",
    "Picking the best area to stay…",
    "Finding stays that match…",
    "Mapping your stops…",
    "Writing your day-by-day plan…"
  ];
  var index = 0;
  var list = document.getElementById("stageList");
  var current = document.getElementById("stageCurrent");
  function paint() {
    if (list) {
      var items = list.querySelectorAll("li");
      for (var i = 0; i < items.length; i++) {
        items[i].classList.toggle("is-done", i < index);
        items[i].classList.toggle("is-on", i === index);
      }
    }
    if (current) current.textContent = stages[index];
  }
  paint();
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var stepMs = reduce ? 4000 : 2200;
  var timer = setInterval(function () {
    if (index < stages.length - 1) {
      index += 1;
      paint();
    } else {
      clearInterval(timer);
    }
  }, stepMs);
  if (!jobId) return;
  var fails = 0;
  function poll() {
    fetch("/api/jobs/" + jobId, {headers: {Accept: "application/json"}})
      .then(function (res) {
        if (res.status === 404) {
          window.location.reload();
          return null;
        }
        if (!res.ok) throw new Error("status");
        return res.json();
      })
      .then(function (data) {
        if (!data) return;
        fails = 0;
        if (data.status === "done" && typeof data.redirect === "string" && data.redirect.indexOf("/pages/") === 0) {
          window.location.href = data.redirect;
          return;
        }
        if (data.status === "error") {
          window.location.reload();
          return;
        }
        setTimeout(poll, 1500);
      })
      .catch(function () {
        fails += 1;
        if (fails > 8 && current) current.textContent = "Still working… this page will keep trying.";
        setTimeout(poll, 1500);
      });
  }
  poll();
})();
</script>
"""


def page_shell(title, body_html, head_extra="", script=""):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        "<title>" + esc(title) + "</title>\n"
        + CRITICAL_CSS
        + '\n<link rel="stylesheet" href="' + html.escape(STYLES_HREF, quote=True) + '">\n'
        + (head_extra or "")
        + "</head>\n<body>\n<header><a class=\"brand\" href=\"/\">"
        + BRAND_SVG
        + '<span class="brand-lockup"><h1>TripAssembler</h1>'
        + f'<p class="brand-tag">{TAGLINE}</p></span></a></header>\n'
        + body_html
        + '\n<footer>TripAssembler · Custom assemblies for real travel constraints · '
        + '<a href="/sitemap.xml">Sitemap</a></footer>\n'
        + (script or "")
        + "\n</body>\n</html>"
    )


def render_simple(title, message):
    body = (
        '<div class="container"><div class="hero"><h2>'
        + esc(title)
        + "</h2><p>"
        + esc(message)
        + '</p></div><a class="btn" href="/">Assemble a trip</a></div>'
    )
    return page_shell(title + " | TripAssembler", body)


def recap_html(fields):
    rows = [
        ("Where", "where"),
        ("Budget", "budget"),
        ("Who", "who"),
        ("Must-haves", "must"),
        ("When", "when"),
        ("Interests", "interests"),
    ]
    parts = []
    for label, key in rows:
        value = str((fields or {}).get(key) or "").strip()
        if not value:
            continue
        parts.append("<dt>" + esc(label) + "</dt><dd>" + esc(value) + "</dd>")
    if not parts:
        return ""
    return '<div class="card recap"><h2>What you asked for</h2><dl>' + "".join(parts) + "</dl></div>"


def render_assembling(job, job_id=""):
    if job is None:
        heading = "This assembly isn't available"
        intro = (
            "That progress page expired — the server may have restarted. "
            "Start again and, if this browser saved a draft, your details will be filled back in."
        )
        panel = ""
        recap = ""
        actions = '<p class="btn-row"><a class="btn" href="/">Assemble a trip</a></p>'
        script = ""
        head_extra = '<meta name="robots" content="noindex">'
        status = 404
        page_title = heading
    elif job.get("status") == "error":
        heading = "We couldn't finish that trip"
        intro = job.get("error") or (
            "Something went wrong while assembling your trip. Your details are still here — try again."
        )
        panel = ""
        recap = recap_html(job.get("fields") or {})
        retry = html.escape(job.get("retry") or "/", quote=True)
        actions = f'<p class="btn-row"><a class="btn" href="{retry}">Try again</a></p>'
        script = ""
        head_extra = '<meta name="robots" content="noindex">'
        status = 200
        page_title = heading
    else:
        heading = "Assembling your trip"
        intro = "Your page will open as soon as the plan is ready."
        panel = PROGRESS_PANEL
        recap = recap_html(job.get("fields") or {})
        actions = ""
        safe_id = job_id if re.fullmatch(r"[a-f0-9]{16}", job_id or "") else ""
        script = PROGRESS_SCRIPT.replace("__JOB_ID__", safe_id)
        head_extra = '<meta name="robots" content="noindex">\n<noscript><meta http-equiv="refresh" content="3"></noscript>'
        status = 200
        page_title = "Assembling your trip"
    body = (
        '<div class="container assemble"><div class="hero"><h2>'
        + esc(heading)
        + "</h2><p>"
        + esc(intro)
        + "</p></div>"
        + panel
        + recap
        + actions
        + "</div>"
    )
    return page_shell(page_title + " | TripAssembler", body, head_extra, script), status


PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | TripAssembler</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{page_url}">
<meta property="og:site_name" content="TripAssembler">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_desc}">
{social_extra}
<style>body{{margin:0;background:#f8fafc;color:#0f172a;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}}</style>
<link rel="stylesheet" href="{styles_href}">
<link rel="preconnect" href="https://www.google.com">
<link rel="preconnect" href="https://maps.gstatic.com" crossorigin>
<link rel="preconnect" href="https://thumb.wikimedia.org" crossorigin>
<script type="application/ld+json">{json_ld}</script>
</head>
<body>
<header>
  <a class='brand' href='/'>
    <svg class="logo-svg" viewBox="0 0 36 36" xmlns="http://www.w3.org/2000/svg">
  <rect width="36" height="36" rx="8" fill="#1e40af"/>
  <path d="M8 22 L18 10 L28 22" stroke="white" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="18" cy="24" r="2" fill="white"/>
</svg>
    <span class="brand-lockup"><h1>TripAssembler</h1><p class="brand-tag">Assemble the perfect Trip</p></span>
  </a>
</header>
<div class="container">
  {hero_html}
  {icon_html}
  <h2 style="margin:0 0 8px;">{title}</h2>
  <p style="color:var(--muted); margin-top:0;"><strong>Location:</strong> {location}</p>
  <div class="card">
    <h3 style="margin-top:0;">Key constraints</h3>
    <p>{constraints}</p>
    <p>{summary}</p>
  </div>
  <div class="card">
    {map_html}
  </div>
  <div class="card">
    <h2>Recommended Stays</h2>
    {hotels_html}
  </div>
  <div class="card">
    <h2>Suggested Itinerary</h2>
    {itinerary_html}
  </div>
  <div class="card">
    <h2>Getting Around</h2>
    <p>{transport}</p>
  </div>
  <div class="card">
    <h2>Budget Notes</h2>
    <p>{budget_notes}</p>
  </div>
  {faqs_html}
  {related_html}
  <div class="actions">
    <button type="button" onclick="window.print()">Print / Save PDF</button>
    <button type="button" onclick="navigator.clipboard.writeText(location.href);alert('Link copied')">Copy share link</button>
  </div>
  <div class="cta">
    <a class='btn' href='/' style='width:auto;'>Assemble another trip</a>
  </div>
</div>
<footer>TripAssembler · Custom assemblies for real travel constraints · <a href="/sitemap.xml">Sitemap</a></footer>
<!-- ta-enhanced -->
</body>
</html>
"""


def persist_assembly(assembly, records):
    created_at = datetime.now(timezone.utc)
    stamp = created_at.strftime("%Y%m%d%H%M")
    title = str(assembly.get("title") or "").strip() or "Your trip assembly"
    location = str(assembly.get("location") or "").strip()
    slug = f"{slugify(title)}-{stamp}-{secrets.token_hex(2)}"

    labels = [record["label"] for record in records]
    map_url, open_url = build_map_urls(labels, location)
    map_html = map_block_html(records, location, map_url, open_url)

    hotels = assembly.get("hotels") if isinstance(assembly.get("hotels"), list) else []
    itinerary = assembly.get("itinerary") if isinstance(assembly.get("itinerary"), list) else []
    faqs = assembly.get("faqs") if isinstance(assembly.get("faqs"), list) else []
    hotels_html = hotels_to_html(hotels)
    itinerary_html = itinerary_to_html(itinerary)
    faqs_html = faqs_to_html(faqs)
    if faqs_html:
        faqs_html = f'<div class="card">{faqs_html}</div>'

    index = load_index()
    related_html = related_to_html(index, slug, location, title=title)
    if isinstance(assembly.get("hero_image"), dict):
        remember_image(assembly.get("hero_image"), slug, location, title)

    page_url = f"{BASE_URL}/pages/{slug}.html"
    summary = assembly.get("summary", "")
    if not isinstance(summary, str):
        summary = str(summary or "")
    desc = meta_description(summary)
    hero = assembly.get("hero_image") if isinstance(assembly.get("hero_image"), dict) else None
    hero_html = photo_figure(hero, location or title, "hero-photo")
    icon_html = "" if hero_html else ICON_HTML
    image_url = ""
    if hero and isinstance(hero.get("src"), str) and hero["src"].startswith("https://") and _wiki_host(hero["src"]):
        image_url = hero["src"]
    json_ld = build_json_ld(
        page_url, title, summary, location, itinerary, faqs, image_url=image_url
    )
    if image_url:
        escaped = safe_url(image_url)
        social_extra = (
            f'<meta property="og:image" content="{escaped}">\n'
            f'<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:image" content="{escaped}">'
        )
    else:
        social_extra = '<meta name="twitter:card" content="summary">'

    raw_constraints = assembly.get("constraints") or []
    if isinstance(raw_constraints, str):
        raw_constraints = [raw_constraints]
    elif not isinstance(raw_constraints, list):
        raw_constraints = []
    constraints = ", ".join(str(item) for item in raw_constraints if str(item).strip())

    html_out = PAGE_TEMPLATE.format(
        title=esc(title),
        meta_desc=esc(desc),
        page_url=esc(page_url),
        json_ld=json_ld,
        styles_href=html.escape(STYLES_HREF, quote=True),
        social_extra=social_extra,
        hero_html=hero_html,
        icon_html=icon_html,
        location=esc(location),
        constraints=esc(constraints),
        summary=esc(summary),
        map_html=map_html,
        hotels_html=hotels_html,
        itinerary_html=itinerary_html,
        transport=esc(assembly.get("transport", "")),
        budget_notes=esc(assembly.get("budget_notes", "")),
        faqs_html=faqs_html,
        related_html=related_html,
    )
    os.makedirs(PAGES_DIR, exist_ok=True)
    with open(os.path.join(PAGES_DIR, f"{slug}.html"), "w", encoding="utf-8") as handle:
        handle.write(html_out)
    index.insert(0, {
        "slug": slug,
        "title": title,
        "location": location,
        "created_at": created_at.strftime("%Y-%m-%d"),
    })
    save_index(index)
    return f"/pages/{slug}.html"


async def generate_assembly(request_text):
    response = await client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": PROMPT + request_text[:2500]}],
        temperature=0.7,
        max_tokens=MAX_OUTPUT_TOKENS,
        response_format={"type": "json_object"},
        timeout=45,
    )
    content = response.choices[0].message.content or ""
    assembly = json.loads(content)
    if not isinstance(assembly, dict):
        raise ValueError("model returned unexpected JSON")
    return assembly


async def run_job(job_id, request_text):
    job = JOBS.get(job_id)
    if not job:
        return
    job["status"] = "working"
    await asyncio.sleep(0)
    try:
        assembly = await generate_assembly(request_text)
        records = _clean_records(assembly.get("map_places"), assembly.get("location") or "")
        await attach_images(assembly, records)
        job["redirect"] = persist_assembly(assembly, records)
        job["status"] = "done"
    except Exception:
        log.exception("assembly job %s failed", job_id)
        job["error"] = (
            "Something went wrong while assembling your trip. "
            "Your details are still here — try again."
        )
        job["status"] = "error"


def spawn(coro):
    task = asyncio.create_task(coro)
    _background_tasks.add(task)
    task.add_done_callback(_background_tasks.discard)
    return task


def prune_jobs():
    cutoff = time.time() - JOB_TTL_SECONDS
    for job_id, job in list(JOBS.items()):
        if job["created"] < cutoff:
            JOBS.pop(job_id, None)


def refresh_job(job):
    if job["status"] in {"queued", "working"} and time.time() - job["created"] > JOB_TIMEOUT_SECONDS:
        job["status"] = "error"
        job["error"] = "This one took too long and was stopped. Your details are still here — try again."


@app.middleware("http")
async def cache_headers(request, call_next):
    response = await call_next(request)
    if response.status_code != 200:
        return response
    path = request.url.path
    if path == "/styles.css" or (path.startswith("/pages/") and path not in {"/pages", "/pages/"}):
        # Slugs include a timestamp, so generated pages are effectively immutable.
        # Legacy pages and the stylesheet are static assets served the same way.
        # A versioned stylesheet sets a longer Cache-Control itself.
        response.headers.setdefault("Cache-Control", "public, max-age=86400")
    elif path in {"/sitemap.xml", "/robots.txt"}:
        response.headers.setdefault("Cache-Control", "public, max-age=3600")
    elif path == "/":
        response.headers.setdefault("Cache-Control", "public, max-age=60")
    return response


@app.get("/healthz")
async def healthz():
    """Cheap liveness check. Ping it to keep a free Render instance from sleeping."""
    return Response(content="ok", media_type="text/plain", headers={"Cache-Control": "no-store"})


@app.get("/", response_class=HTMLResponse)
async def home(
    example: str = "",
    where: str = "",
    budget: str = "",
    who: str = "",
    must: str = "",
    when: str = "",
    interests: str = "",
):
    fields = fields_from(where, budget, who, must, when, interests)
    if example == "1" and not any(fields.values()):
        fields = dict(EXAMPLE_FIELDS)
    return render_home(values=fields)


@app.post("/assemble")
async def assemble(
    where: str = Form(""),
    budget: str = Form(""),
    who: str = Form(""),
    must: str = Form(""),
    when: str = Form(""),
    interests: str = Form(""),
    captcha: str = Form(""),
    request: str = Form(""),
):
    fields = fields_from(where, budget, who, must, when, interests)
    if str(captcha or "").strip() != "7":
        return HTMLResponse(render_home("Please answer correctly.", fields), status_code=400)
    if not fields["where"]:
        return HTMLResponse(
            render_home("Add a destination so we know where to plan.", fields),
            status_code=400,
        )
    prune_jobs()
    job_id = secrets.token_hex(8)
    JOBS[job_id] = {
        "status": "queued",
        "redirect": "",
        "error": "",
        "retry": retry_query(fields),
        "fields": fields,
        "created": time.time(),
    }
    request_text = compose_request(
        where=fields["where"],
        budget=fields["budget"],
        who=fields["who"],
        must=fields["must"],
        when=fields["when"],
        interests=fields["interests"],
        request=clean_field(request, 400),
    )
    spawn(run_job(job_id, request_text))
    return RedirectResponse(f"/assembling/{job_id}", status_code=303)


@app.get("/assembling/{job_id}")
async def assembling(job_id: str):
    headers = {"Cache-Control": "no-store"}
    if not re.fullmatch(r"[a-f0-9]{16}", job_id):
        body, status = render_assembling(None)
        return HTMLResponse(body, status_code=status, headers=headers)
    job = JOBS.get(job_id)
    if not job:
        body, status = render_assembling(None)
        return HTMLResponse(body, status_code=status, headers=headers)
    refresh_job(job)
    redirect = str(job.get("redirect") or "")
    if job["status"] == "done" and redirect.startswith("/pages/"):
        return RedirectResponse(redirect, status_code=303)
    body, status = render_assembling(job, job_id)
    return HTMLResponse(body, status_code=status, headers=headers)


@app.get("/api/jobs/{job_id}")
async def job_status(job_id: str):
    job = JOBS.get(job_id)
    if not job or not re.fullmatch(r"[a-f0-9]{16}", job_id):
        return JSONResponse(
            {
                "status": "error",
                "redirect": "",
                "error": "This assembly is no longer available. The server may have restarted.",
            },
            status_code=404,
            headers={"Cache-Control": "no-store"},
        )
    refresh_job(job)
    return JSONResponse(
        {
            "status": job["status"],
            "redirect": job.get("redirect") or "",
            "error": job.get("error") or "",
        },
        headers={"Cache-Control": "no-store"},
    )


@app.get("/sitemap.xml")
async def sitemap():
    index = load_index()
    generated_lastmod = {}
    generated_order = []
    for item in index:
        slug = item.get("slug")
        if not slug or slug in generated_lastmod:
            continue
        generated_lastmod[slug] = item.get("created_at")
        generated_order.append(slug)

    urls = [{"loc": f"{BASE_URL}/", "lastmod": None}]
    seen = set()
    for slug in legacy_slugs():
        seen.add(slug)
        urls.append({
            "loc": f"{BASE_URL}/pages/{slug}.html",
            "lastmod": generated_lastmod.get(slug),
        })
    for slug in generated_order:
        if slug in seen:
            continue
        urls.append({
            "loc": f"{BASE_URL}/pages/{slug}.html",
            "lastmod": generated_lastmod.get(slug),
        })
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for item in urls:
        loc = html.escape(item["loc"], quote=True)
        lastmod = item.get("lastmod")
        if lastmod:
            parts.append(f"  <url><loc>{loc}</loc><lastmod>{html.escape(str(lastmod))}</lastmod></url>")
        else:
            parts.append(f"  <url><loc>{loc}</loc></url>")
    parts.append("</urlset>")
    return Response(content="\n".join(parts) + "\n", media_type="application/xml")


@app.get("/robots.txt")
async def robots():
    body = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /assembling/\n"
        "Disallow: /api/\n"
        f"Sitemap: {BASE_URL}/sitemap.xml\n"
    )
    return Response(content=body, media_type="text/plain")


@app.get("/styles.css")
async def styles_css(v: str = ""):
    if not os.path.isfile(STYLES_PATH):
        return HTMLResponse(render_simple("Page not found", "That file is not here."), status_code=404)
    if v:
        cache = "public, max-age=31536000, immutable"
    else:
        cache = "public, max-age=86400"
    return FileResponse(STYLES_PATH, media_type="text/css", headers={"Cache-Control": cache})


# City -> (country, region) for legacy slugs, whose titles name a place but not a country.
PLACE_META = {
    "amsterdam": ("Netherlands", "Europe"),
    "athens": ("Greece", "Europe"),
    "bali": ("Indonesia", "Asia"),
    "banff": ("Canada", "North America"),
    "bangkok": ("Thailand", "Asia"),
    "barcelona": ("Spain", "Europe"),
    "budapest": ("Hungary", "Europe"),
    "cancun": ("Mexico", "North America"),
    "cape town": ("South Africa", "Africa"),
    "dubai": ("United Arab Emirates", "Middle East"),
    "dubrovnik": ("Croatia", "Europe"),
    "iceland": ("Iceland", "Europe"),
    "reykjavik": ("Iceland", "Europe"),
    "kyoto": ("Japan", "Asia"),
    "lisbon": ("Portugal", "Europe"),
    "london": ("United Kingdom", "Europe"),
    "los angeles": ("United States", "North America"),
    "maldives": ("Maldives", "Asia"),
    "marrakech": ("Morocco", "Africa"),
    "maui": ("United States", "North America"),
    "miami": ("United States", "North America"),
    "mykonos": ("Greece", "Europe"),
    "new york": ("United States", "North America"),
    "oahu": ("United States", "North America"),
    "osaka": ("Japan", "Asia"),
    "paris": ("France", "Europe"),
    "phuket": ("Thailand", "Asia"),
    "prague": ("Czechia", "Europe"),
    "rome": ("Italy", "Europe"),
    "santorini": ("Greece", "Europe"),
    "singapore": ("Singapore", "Asia"),
    "split": ("Croatia", "Europe"),
    "sydney": ("Australia", "Oceania"),
    "tokyo": ("Japan", "Asia"),
    "tulum": ("Mexico", "North America"),
    "vienna": ("Austria", "Europe"),
}
_PLACE_KEYS = tuple(sorted(PLACE_META, key=len, reverse=True))
_THEMES = (
    ("pet-friendly", ("pet-friendly", "pet friendly", "pets")),
    ("family", ("family", "kids")),
    ("budget", ("budget", "under-200", "under $200", "under 200")),
    ("beach", ("beach",)),
    ("luxury", ("luxury", "ocean view", "ocean-view")),
    ("pool", ("pool",)),
    ("walkable", ("walkable", "city center", "city-center")),
    ("romantic", ("romantic", "quiet")),
    ("nature", ("mountain", "nature")),
    ("kitchen", ("kitchen",)),
)
_GENERIC_DAY = re.compile(
    r"^(theme|explore|exploring|free day|arrival|departure|travel day|rest day|rest|day\s+\d+)$",
    re.I,
)
_PAGE_ICON_RE = re.compile(r"\s*<div class=\"page-icon\">.*?</div>", re.S | re.I)
_TITLE_BLOCK_RE = re.compile(
    r"<h2\b[^>]*>.*?</h2>(\s*<p\b[^>]*>.*?</p>)?",
    re.S | re.I,
)
_OLD_RELATED_RE = re.compile(
    r"\s*(?:<div class=\"card\">\s*)?<h2>\s*More trip assemblies\s*</h2>\s*<ul>.*?</ul>\s*(?:</div>)?",
    re.I | re.S,
)
_BRAND_LOCKUP = (
    '<span class="brand-lockup"><h1>TripAssembler</h1>'
    f'<p class="brand-tag">{TAGLINE}</p></span>'
)


def plain_text(fragment):
    text = re.sub(r"<[^>]+>", " ", fragment or "")
    return " ".join(html.unescape(text).split())


def read_text(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def write_text_atomic(path, text):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    fd, temporary = tempfile.mkstemp(dir=directory or ".", prefix=".page-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def sidecar_path(slug):
    return os.path.join(PAGES_DIR, ".enhanced", slug + ".html")


def apply_tagline(document):
    """Swap the old site tagline, and add it to a header that does not show one."""
    document = _OLD_TAGLINE_RE.sub(TAGLINE, document)
    if 'class="brand-tag"' in document:
        return document
    if "<h1>TripAssembler</h1>" in document:
        return document.replace("<h1>TripAssembler</h1>", _BRAND_LOCKUP, 1)
    return document


def page_title_from_html(document):
    match = re.search(r"<h2\b[^>]*>(.*?)</h2>", document or "", re.S | re.I)
    if not match:
        match = re.search(r"<title>(.*?)</title>", document or "", re.S | re.I)
    if not match:
        return ""
    text = plain_text(match.group(1))
    return re.sub(r"\s*\|\s*TripAssembler\s*$", "", text).strip()


def location_from_html(document):
    match = re.search(r"<strong>\s*Location:\s*</strong>\s*([^<]+)", document or "", re.I)
    if match:
        return plain_text(match.group(1))
    block = re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        document or "",
        re.S | re.I,
    )
    if not block:
        return ""
    try:
        data = json.loads(block.group(1).strip().replace("<\\/", "</"))
    except ValueError:
        return ""
    nodes = data.get("@graph") if isinstance(data, dict) else None
    if not isinstance(nodes, list):
        nodes = [data] if isinstance(data, dict) else []
    for node in nodes:
        if not isinstance(node, dict):
            continue
        dest = node.get("touristDestination")
        if isinstance(dest, dict) and dest.get("name"):
            return str(dest["name"]).strip()
        if isinstance(dest, str) and dest.strip():
            return dest.strip()
    return ""


def city_from_title_or_slug(title, slug):
    match = re.search(r"\bin\s+(.+)$", title or "", re.I)
    if match:
        return match.group(1).strip(" .")
    spaced = (slug or "").replace("-", " ").casefold()
    for key in _PLACE_KEYS:
        if spaced == key or spaced.startswith(key + " "):
            return key.title()
    return ""


def popular_slugs():
    global _popular_slugs
    if _popular_slugs is None:
        try:
            text = read_text(HOME_TEMPLATE)
        except OSError:
            text = ""
        _popular_slugs = set(re.findall(r"""href=['\"]/pages/([A-Za-z0-9][A-Za-z0-9_-]{0,180})""", text))
    return _popular_slugs


def describe_trip(slug, title, location="", created_at=""):
    title = " ".join(str(title or "").split())
    location = " ".join(str(location or "").split())
    if location.lower() in {"see request", "travel"}:
        location = ""
    city = ""
    country = ""
    if location:
        bits = [bit.strip() for bit in location.split(",") if bit.strip()]
        if bits:
            city = bits[0]
        if len(bits) >= 2:
            country = bits[-1]
    if not city:
        city = city_from_title_or_slug(title, slug)
    meta = PLACE_META.get(city.casefold())
    region = ""
    if meta:
        if not country:
            country = meta[0]
        region = meta[1]
    blob = " ".join((slug.replace("-", " "), title, location, city)).casefold()
    themes = [name for name, words in _THEMES if any(word in blob for word in words)]
    if city and country and city.casefold() != country.casefold():
        query = f"{city}, {country}"
    elif location:
        query = location
    else:
        query = city or title
    return {
        "slug": slug,
        "title": title or (slug or "trip").replace("-", " ").title(),
        "location": location,
        "city": city,
        "country": country,
        "region": region.casefold(),
        "themes": themes,
        "created_at": created_at or "",
        "popular": slug in popular_slugs(),
        "query": query,
    }


def _date_rank(created_at):
    text = str(created_at or "")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return 0
    try:
        year, month, day = (int(part) for part in text.split("-"))
    except ValueError:
        return 0
    return year * 10000 + month * 100 + day


def _catalog_stamp():
    try:
        index_stat = os.stat(INDEX_FILE)
        index_key = (index_stat.st_mtime_ns, index_stat.st_size)
    except OSError:
        index_key = (0, 0)
    legacy_key = []
    for slug in legacy_slugs():
        path = os.path.join(LEGACY_DIR, slug + ".html")
        try:
            stat = os.stat(path)
        except OSError:
            continue
        legacy_key.append((slug, stat.st_mtime_ns, stat.st_size))
    return (LEGACY_DIR, index_key, tuple(legacy_key))


def trip_catalog():
    """Legacy pages plus index.json, parsed once until those files change."""
    key = _catalog_stamp()
    if _catalog.get("key") == key and _catalog.get("items") is not None:
        return _catalog["items"]
    items = {}
    for slug in legacy_slugs():
        path = os.path.join(LEGACY_DIR, slug + ".html")
        try:
            title = page_title_from_html(read_text(path))
        except OSError:
            continue
        items[slug] = describe_trip(slug, title or slug.replace("-", " "))
    try:
        index = load_index()
    except (OSError, ValueError):
        index = []
    if isinstance(index, list):
        for entry in index:
            if not isinstance(entry, dict):
                continue
            slug = str(entry.get("slug") or "")
            if not _SLUG_RE.fullmatch(slug) or not resolve_page_file(slug):
                continue
            title = str(entry.get("title") or "").strip()
            location = str(entry.get("location") or "").strip()
            created = str(entry.get("created_at") or "").strip()
            if not title:
                path = resolve_page_file(slug)
                try:
                    title = page_title_from_html(read_text(path)) if path else ""
                except OSError:
                    title = ""
            items[slug] = describe_trip(slug, title, location, created_at=created)
    _catalog["key"] = key
    _catalog["items"] = list(items.values())
    return _catalog["items"]


def rank_related(current, pool, limit=RELATED_LIMIT):
    """Same place, then country, then region, then shared themes, then recent and popular."""
    city = (current.get("city") or "").casefold()
    country = (current.get("country") or "").casefold()
    region = (current.get("region") or "").casefold()
    themes = set(current.get("themes") or [])
    ranked = []
    for item in pool:
        slug = item.get("slug") or ""
        if not slug or slug == current.get("slug"):
            continue
        item_city = (item.get("city") or "").casefold()
        item_country = (item.get("country") or "").casefold()
        item_region = (item.get("region") or "").casefold()
        shared = len(themes & set(item.get("themes") or []))
        ranked.append((
            0 if city and item_city and city == item_city else 1,
            0 if country and item_country and country == item_country else 1,
            0 if region and item_region and region == item_region else 1,
            -shared,
            -_date_rank(item.get("created_at")),
            0 if item.get("popular") else 1,
            slug,
            item,
        ))
    ranked.sort(key=lambda row: row[:-1])
    return [row[-1] for row in ranked[:limit]]


def cached_thumb(item):
    keys = []
    slug = item.get("slug") or ""
    if slug:
        keys.append("slug:" + slug.casefold())
    labels = [item.get("query"), item.get("location"), item.get("city")]
    city = item.get("city") or ""
    country = item.get("country") or ""
    if city and country and city.casefold() != country.casefold():
        labels.append(f"{city}, {country}")
    for label in labels:
        key = image_cache_key("", label)
        if key and key not in keys:
            keys.append(key)
    for key in keys:
        image, hit = cache_get(key)
        if hit and isinstance(image, dict) and image.get("src"):
            return image
    return None


def related_card_html(item):
    href = html.escape(f"/pages/{item['slug']}.html", quote=True)
    title = esc(item.get("title") or "Trip")
    meta = item.get("city") or item.get("location") or ""
    meta_html = f"<small>{esc(meta)}</small>" if meta else ""
    media = ""
    attr = ""
    image = cached_thumb(item)
    if image:
        src = safe_url(image.get("src"))
        if src:
            try:
                width = int(image.get("width") or 640)
                height = int(image.get("height") or 480)
            except (TypeError, ValueError):
                width, height = 640, 480
            alt = esc(image.get("title") or item.get("title") or "Trip photo")
            media = (
                f'<img class="related-thumb" src="{src}" width="{width}" height="{height}" '
                f'alt="{alt}" loading="lazy" decoding="async">'
            )
            page = safe_url(image.get("page"))
            if page:
                attr = (
                    f'<p class="wiki-attr-line"><a href="{page}" target="_blank" '
                    f'rel="noopener noreferrer">{esc(image.get("title") or "Wikipedia")}</a>'
                    f" · Wikipedia</p>"
                )
    return (
        '<article class="related-card">'
        f'<a class="related-link" href="{href}">{media}'
        f'<span class="related-title">{title}</span>{meta_html}</a>'
        f"{attr}</article>"
    )


def related_section_html(slug, title, location, limit=RELATED_LIMIT):
    pool = trip_catalog()
    current = next((item for item in pool if item.get("slug") == slug), None)
    described = describe_trip(
        slug,
        title or (current or {}).get("title", ""),
        location or (current or {}).get("location", ""),
        created_at=(current or {}).get("created_at", ""),
    )
    if current:
        described["popular"] = current.get("popular")
        if not title and not location:
            described = current
    picks = rank_related(described, pool, limit=limit)
    if not picks:
        return ""
    cards = "".join(related_card_html(item) for item in picks)
    section = (
        '<section class="related-trips" id="related-trips">'
        "<h2>Related trips</h2>"
        f'<div class="related-grid">{cards}</div>'
        "</section>"
    )
    # persist_assembly fills PAGE_TEMPLATE with str.format.
    return section.replace("{", "&#123;").replace("}", "&#125;")


def context_for(slug, document):
    title = ""
    location = ""
    created = ""
    try:
        index = load_index()
    except (OSError, ValueError):
        index = []
    if isinstance(index, list):
        for entry in index:
            if isinstance(entry, dict) and entry.get("slug") == slug:
                title = str(entry.get("title") or "").strip()
                location = str(entry.get("location") or "").strip()
                created = str(entry.get("created_at") or "").strip()
                break
    if not title:
        title = page_title_from_html(document)
    if not location:
        location = location_from_html(document)
    return describe_trip(slug, title, location, created_at=created)


def stops_from_html(document):
    match = re.search(r'<ol class="stops">(.*?)</ol>', document or "", re.S | re.I)
    if not match:
        return []
    labels = []
    for li in re.findall(r"<li\b[^>]*>(.*?)</li>", match.group(1), re.S | re.I):
        if "stop-thumb" in li:
            labels.append(None)
            continue
        link = re.search(r"<a\b[^>]*>(.*?)</a>", li, re.S | re.I)
        label = plain_text(link.group(1) if link else li)
        labels.append(label or None)
    return labels


def days_from_html(document):
    days = []
    for body in re.findall(r'<div class="day">(.*?)</div>', document or "", re.S | re.I):
        if "day-photo" in body:
            days.append(None)
            continue
        heading = re.search(r"<h3\b[^>]*>(.*?)</h3>", body, re.S | re.I)
        title = plain_text(heading.group(1) if heading else "")
        title = re.sub(r"^Day\s+\d+\s*:\s*", "", title, flags=re.I).strip()
        days.append(title or None)
    return days


def day_is_identifiable(title, city):
    text = " ".join(str(title or "").split())
    if len(text) < 6 or _GENERIC_DAY.match(text):
        return False
    if city and text.casefold() == city.casefold():
        return False
    return True


def needs_image_lookup(document):
    if ENHANCED_MARKER in document:
        return False
    markers = ('class="hero-photo"', 'class="stop-thumb"', 'class="day-photo"')
    return not any(marker in document for marker in markers)


def inject_hero(document, image, alt):
    figure = photo_figure(image, alt, "hero-photo")
    if not figure or 'class="hero-photo"' in document:
        return document
    document = _PAGE_ICON_RE.sub("\n", document, count=1)
    match = _TITLE_BLOCK_RE.search(document)
    if not match:
        needle = '<div class="container">'
        if needle in document:
            return document.replace(needle, needle + "\n" + figure, 1)
        return figure + document
    return document[:match.end()] + "\n" + figure + document[match.end():]


def inject_stop_images(document, labels, found):
    match = re.search(r'(<ol class="stops">)(.*?)(</ol>)', document, re.S | re.I)
    if not match:
        return document
    body = match.group(2)
    lis = list(re.finditer(r"<li\b[^>]*>.*?</li>", body, re.S | re.I))
    pieces = []
    cursor = 0
    for index, li in enumerate(lis):
        pieces.append(body[cursor:li.start()])
        image = found.get(f"stop:{index}")
        label = labels[index] if index < len(labels) else None
        if image and label and "stop-thumb" not in li.group(0):
            pieces.append(stop_li_html(label, image))
        else:
            pieces.append(li.group(0))
        cursor = li.end()
    pieces.append(body[cursor:])
    return document[:match.start(2)] + "".join(pieces) + document[match.end(2):]


def inject_day_images(document, titles, found):
    matches = list(re.finditer(r'<div class="day">.*?</div>', document, re.S | re.I))
    if not matches:
        return document
    pieces = []
    cursor = 0
    for index, match in enumerate(matches):
        pieces.append(document[cursor:match.start()])
        block = match.group(0)
        image = found.get(f"day:{index}")
        title = titles[index] if index < len(titles) else ""
        if image and title and "day-photo" not in block:
            figure = photo_figure(image, title, "day-photo")
            block = block.replace('<div class="day">', '<div class="day">' + figure, 1)
        pieces.append(block)
        cursor = match.end()
    pieces.append(document[cursor:])
    return "".join(pieces)


def with_json_ld_image(document, image_url):
    if not image_url:
        return document
    match = re.search(
        r'(<script type="application/ld\+json">)(.*?)(</script>)',
        document,
        re.S | re.I,
    )
    if not match:
        return document
    try:
        data = json.loads(match.group(2).strip().replace("<\\/", "</"))
    except ValueError:
        return document
    nodes = data.get("@graph") if isinstance(data, dict) else None
    if not isinstance(nodes, list):
        return document
    changed = False
    for node in nodes:
        if isinstance(node, dict) and node.get("@type") == "TouristTrip" and not node.get("image"):
            node["image"] = image_url
            changed = True
            break
    if not changed:
        return document
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return document[:match.start(2)] + payload + document[match.end(2):]


def inject_related(document, section):
    if not section or 'id="related-trips"' in document:
        return document
    document = _OLD_RELATED_RE.sub("\n", document, count=1)
    for needle in ('<div class="actions">', "<footer>", "<footer "):
        if needle in document:
            return document.replace(needle, section + "\n" + needle, 1)
    if "</body>" in document:
        return document.replace("</body>", section + "\n</body>", 1)
    return document + "\n" + section


async def inject_images(document, info):
    stops = stops_from_html(document)
    days = days_from_html(document)
    specs = []
    query = info.get("query") or info.get("title") or ""
    if query:
        specs.append(("hero", "", query))
    city = info.get("city") or ""
    for index, label in enumerate(stops):
        if label and sum(1 for key, _, _ in specs if key.startswith("stop:")) < 6:
            specs.append((f"stop:{index}", "", label))
    for index, title in enumerate(days):
        if not title or not day_is_identifiable(title, city):
            continue
        if sum(1 for key, _, _ in specs if key.startswith("day:")) >= 3:
            break
        if city and city.casefold() not in title.casefold():
            day_query = f"{title}, {city}"
        else:
            day_query = title
        specs.append((f"day:{index}", "", day_query))
    if not specs:
        return document
    found = await resolve_images(specs, timeout=ENHANCE_TIMEOUT)
    hero = found.get("hero")
    if hero:
        alt = info.get("city") or info.get("title") or "Destination"
        document = inject_hero(document, hero, alt)
        src = str(hero.get("src") or "")
        if src.startswith("https://") and _wiki_host(src):
            document = with_json_ld_image(document, src)
        remember_image(
            hero,
            info.get("slug") or "",
            query,
            info.get("city") or "",
            info.get("location") or "",
            info.get("country") or "",
        )
    if any(found.get(f"stop:{index}") for index in range(len(stops))):
        document = inject_stop_images(document, stops, found)
    if any(found.get(f"day:{index}") for index in range(len(days))):
        document = inject_day_images(document, days, found)
    if "wikimedia.org" in document and 'href="https://thumb.wikimedia.org"' not in document:
        if "</head>" in document:
            document = document.replace(
                "</head>",
                '<link rel="preconnect" href="https://thumb.wikimedia.org" crossorigin>\n</head>',
                1,
            )
    return document


async def enhance_document(slug, document):
    """Add photos, related trips, and the tagline. Raises if image lookup itself raises."""
    if ENHANCED_MARKER in document and 'id="related-trips"' in document:
        return apply_tagline(document)
    document = apply_tagline(document)
    info = context_for(slug, document)
    if needs_image_lookup(document):
        document = await inject_images(document, info)
    if 'id="related-trips"' not in document:
        section = related_section_html(
            slug,
            info.get("title") or "",
            info.get("location") or "",
        )
        document = inject_related(document, section)
    if ENHANCED_MARKER not in document:
        if "</body>" in document:
            document = document.replace("</body>", ENHANCED_MARKER + "\n</body>", 1)
        else:
            document += "\n" + ENHANCED_MARKER + "\n"
    return document


async def prepare_served_page(slug, path):
    lock = _page_locks.get(slug)
    if lock is None:
        lock = asyncio.Lock()
        _page_locks[slug] = lock
    async with lock:
        stat = os.stat(path)
        stamp = (stat.st_mtime_ns, stat.st_size)
        cached = _page_mem.get(slug)
        if cached and cached.get("stamp") == stamp:
            return cached["html"]
        document = read_text(path)
        if ENHANCED_MARKER in document and 'id="related-trips"' in document:
            document = apply_tagline(document)
            _page_mem[slug] = {"stamp": stamp, "html": document}
            return document
        side = sidecar_path(slug)
        on_disk = _inside(path, PAGES_DIR)
        if (
            not on_disk
            and os.path.isfile(side)
            and os.stat(side).st_mtime_ns >= stat.st_mtime_ns
        ):
            side_html = read_text(side)
            if ENHANCED_MARKER in side_html:
                side_html = apply_tagline(side_html)
                _page_mem[slug] = {"stamp": stamp, "html": side_html}
                return side_html
        try:
            updated = await enhance_document(slug, document)
        except Exception:
            log.warning("could not enhance %s", slug, exc_info=True)
            updated = apply_tagline(document)
            _page_mem[slug] = {"stamp": stamp, "html": updated}
            return updated
        if updated != document:
            try:
                if on_disk:
                    write_text_atomic(path, updated)
                    stat = os.stat(path)
                    stamp = (stat.st_mtime_ns, stat.st_size)
                else:
                    write_text_atomic(side, updated)
            except OSError:
                log.warning("could not store enhanced html for %s", slug, exc_info=True)
        _page_mem[slug] = {"stamp": stamp, "html": updated}
        return updated


@app.get("/pages/{slug}")
async def serve_page(slug: str):
    path = resolve_page_file(slug)
    if not path:
        return HTMLResponse(
            render_simple("Page not found", "That trip page is not here."),
            status_code=404,
        )
    name = slug[:-5] if slug.endswith(".html") else slug
    if not _SLUG_RE.fullmatch(name):
        return HTMLResponse(
            render_simple("Page not found", "That trip page is not here."),
            status_code=404,
        )
    try:
        html_out = await prepare_served_page(name, path)
    except Exception:
        log.exception("serve enhance failed for %s", name)
        try:
            html_out = apply_tagline(read_text(path))
        except OSError:
            return HTMLResponse(
                render_simple("Page not found", "That trip page is not here."),
                status_code=404,
            )
    return HTMLResponse(html_out, media_type="text/html")

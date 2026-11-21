from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from starlette.middleware.gzip import GZipMiddleware
import html
import json
import os
import re
from datetime import datetime, timezone
from urllib.parse import quote
from openai import OpenAI

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=500)

PAGES_DIR = "/opt/render/project/src/pages"
INDEX_FILE = "/opt/render/project/src/index.json"
BASE_URL = os.getenv("BASE_URL", "https://tripassembler.onrender.com")
os.makedirs(PAGES_DIR, exist_ok=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")

# Maps Embed API allows up to 20 intermediate waypoints plus origin and destination.
MAX_WAYPOINTS = 20


def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE) as f:
            return json.load(f)
    return []


def save_index(data):
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


def normalize_places(raw_places, location=""):
    """
    Turn LLM map_places into a clean, de-duplicated list of 'Name, City, Country' strings.
    A string (not a list) is a common JSON mistake; never treat it as a character sequence.
    """
    if not raw_places:
        places = []
    elif isinstance(raw_places, str):
        # Prefer splitting on typical list separators if the model returned one string.
        if "\n" in raw_places or " | " in raw_places or ";" in raw_places:
            bits = re.split(r"[\n;]| \| ", raw_places)
        else:
            bits = [raw_places]
        places = [place_to_str(b) for b in bits]
    elif isinstance(raw_places, (list, tuple)):
        places = [place_to_str(p) for p in raw_places]
    else:
        places = []

    location = " ".join(str(location or "").split()).strip()
    if location.lower() in {"see request", "travel"}:
        location = ""

    qualified = []
    seen = set()
    for place in places:
        if not place:
            continue
        if location and location.lower() not in place.lower():
            place = f"{place}, {location}"
        key = re.sub(r"\s+", " ", place).casefold()
        if key in seen:
            continue
        seen.add(key)
        qualified.append(place)

    # Cap at origin + 20 waypoints + destination. Keep start/end; sample the middle.
    max_points = MAX_WAYPOINTS + 2
    if len(qualified) > max_points:
        middle = qualified[1:-1]
        keep = MAX_WAYPOINTS
        step = len(middle) / keep
        sampled = [middle[int(i * step)] for i in range(keep)]
        # Preserve order and uniqueness after sampling
        out = [qualified[0]]
        seen_mid = {qualified[0].casefold(), qualified[-1].casefold()}
        for item in sampled:
            if item.casefold() not in seen_mid:
                out.append(item)
                seen_mid.add(item.casefold())
        out.append(qualified[-1])
        qualified = out

    return qualified


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

    # Single stop (or directions unavailable): pin the place, not a generic search.
    query = encode_place(places[0] if places else context)
    if MAPS_KEY:
        embed = f"https://www.google.com/maps/embed/v1/place?key={MAPS_KEY}&q={query}"
        return embed, open_url
    return "", open_url


def map_block_html(places, location, map_url, open_url):
    items = []
    for place in places:
        q = encode_place(place)
        items.append(
            f'<li><a href="https://www.google.com/maps/search/?api=1&query={q}" '
            f'target="_blank" rel="noopener noreferrer">{esc(place)}</a></li>'
        )
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
        label = "Open route in Google Maps" if len(places) >= 2 else "Open in Google Maps"
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
        urls = d.get("activity_urls") or []
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
        parts.append(
            f'<div class="day"><h3>Day {esc(d.get("day", "?"))}: {esc(d.get("title", ""))}</h3>'
            f"{desc_html}"
            f'<ul>{"".join(lis)}</ul>'
            f"{tips_html}</div>"
        )
    return "".join(parts)


def related_to_html(index, slug, location, limit=5):
    others = [item for item in index if item.get("slug") != slug]
    loc = (location or "").strip().casefold()
    if loc and loc not in {"see request", "travel"}:
        scored = []
        for item in others:
            item_loc = str(item.get("location", "")).casefold()
            title = str(item.get("title", "")).casefold()
            if loc in item_loc or loc in title or (item_loc and item_loc in loc):
                scored.append(item)
        others = scored or others
    others = others[:limit]
    if not others:
        return ""
    items = "".join(
        f'<li><a href="/pages/{esc(item["slug"])}.html">{esc(item.get("title", "Trip"))}</a></li>'
        for item in others
        if item.get("slug")
    )
    return f"<h2>More trip assemblies</h2><ul>{items}</ul>" if items else ""


def build_json_ld(page_url, title, summary, location, itinerary, faqs):
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
    graph = [
        {
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
        },
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


PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | TripAssembler</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{page_url}">
<meta property="og:site_name" content="TripAssembler">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{meta_desc}">
<link rel="preconnect" href="https://www.google.com">
<link rel="preconnect" href="https://maps.gstatic.com" crossorigin>
<style>
  body {{ font-family: system-ui, -apple-system, sans-serif; max-width: 820px; margin: 40px auto; line-height: 1.65; padding: 0 20px; color: #111; }}
  h1 {{ color: #004E89; font-size: 2rem; margin-bottom: 0.4em; }}
  .meta {{ color: #555; margin-bottom: 1em; }}
  .constraints {{ background: #f0f4f8; padding: 16px 18px; border-radius: 10px; margin: 1.2em 0; }}
  .map-container {{ margin: 1.5em 0 0.6em 0; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
  iframe {{ width: 100%; height: 420px; border: 0; }}
  .map-links {{ margin: 0.4em 0 0.6em 0; }}
  .stops {{ margin: 0 0 2em 1.2em; padding: 0; }}
  .day {{ background: #fff; border: 1px solid #e5e7eb; padding: 18px; margin: 16px 0; border-radius: 10px; }}
  .actions {{ margin: 2.5em 0; display: flex; gap: 10px; flex-wrap: wrap; }}
  .btn {{ padding: 10px 16px; border-radius: 8px; border: 1px solid #ddd; background: #fff; text-decoration: none; color: #333; font-size: 0.95em; }}
  .btn:hover {{ background: #f9fafb; }}
  @media print {{ .actions, .map-container {{ display: none; }} }}
</style>
<script type="application/ld+json">{json_ld}</script>
</head>
<body>
<article>
<header>
<h1>{title}</h1>
<div class="meta"><strong>Location:</strong> {location}</div>
</header>
<div class="constraints"><strong>Key constraints:</strong> {constraints}</div>
<p>{summary}</p>

{map_html}

<h2>Recommended Stays</h2>
{hotels_html}

<h2>Suggested Itinerary</h2>
{itinerary_html}

<h2>Getting Around</h2>
<p>{transport}</p>

<h2>Budget Notes</h2>
<p>{budget_notes}</p>

{faqs_html}

{related_html}
</article>
<div class="actions">
  <a class="btn" href="javascript:window.print()">Print / Save PDF</a>
  <a class="btn" href="javascript:navigator.clipboard.writeText(location.href);alert('Link copied')">Copy share link</a>
  <a class="btn" href="/">Assemble another trip</a>
</div>
</body>
</html>
"""


@app.middleware("http")
async def cache_headers(request, call_next):
    response = await call_next(request)
    path = request.url.path
    if path.startswith("/pages/") and path.endswith(".html"):
        # Slugs include a timestamp, so generated pages are effectively immutable.
        response.headers.setdefault("Cache-Control", "public, max-age=86400")
    elif path in {"/sitemap.xml", "/robots.txt"}:
        response.headers.setdefault("Cache-Control", "public, max-age=3600")
    elif path == "/":
        response.headers.setdefault("Cache-Control", "public, max-age=60")
    return response


@app.get("/", response_class=HTMLResponse)
async def home():
    index = load_index()
    links = "".join(
        f'<li><a href="/pages/{esc(item["slug"])}.html">{esc(item.get("title", "Trip"))}</a></li>'
        for item in index
        if item.get("slug")
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TripAssembler — Practical trip plans from your constraints</title>
<meta name="description" content="Describe your trip constraints and TripAssembler will assemble a practical itinerary, stays, and route map.">
<link rel="canonical" href="{BASE_URL}/">
<style>
  body {{ font-family: system-ui, -apple-system, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.65; color: #111; }}
  h1 {{ color: #004E89; }}
  button {{ padding: 12px 24px; background: #004E89; color: white; border: none; border-radius: 8px; font-size: 16px; }}
</style>
</head>
<body>
<h1>TripAssembler</h1>
<p>Describe your trip constraints and I’ll assemble a practical plan.</p>
<form id="tripForm" action="/assemble" method="post">
  <textarea name="request" rows="6" style="width:100%;font-size:16px;padding:12px;border-radius:8px;border:1px solid #ccc;" placeholder="Example: 7 nights in Iceland for 5 adults in December. Need either a 3BR apartment or 2 hotel rooms under $500/night total. Include must-see towns, scenic drives, hot springs, and short hikes."></textarea>
  <br><br>
  <button type="submit" id="submitBtn">Assemble my trip</button>
  <div id="loading" style="display:none;margin-top:16px;color:#004E89;">Assembling your trip… (usually 5–15 seconds)</div>
</form>
<script>
  document.getElementById('tripForm').onsubmit = function() {{
    document.getElementById('submitBtn').disabled = true;
    document.getElementById('submitBtn').textContent = 'Assembling…';
    document.getElementById('loading').style.display = 'block';
  }};
</script>
<h2>Recent Assemblies</h2>
<ul>{links or "<li>None yet</li>"}</ul>
</body></html>
"""


@app.post("/assemble")
async def assemble(request: str = Form(...)):
    request = request.strip() or "a trip"
    created_at = datetime.now(timezone.utc)
    stamp = created_at.strftime("%Y%m%d%H%M")

    prompt = f"""You are an expert travel planner. Create a realistic, useful trip assembly for this request:

"{request}"

Guidelines:
- Prefer real or highly realistic hotel/apartment names and neighborhoods
- Give believable price ranges
- Build a proper multi-day itinerary matching the requested length
- Include specific attractions, activities, food ideas, and practical tips
- For each itinerary day, include a 2–3 sentence "description" of the day
- Include a "map_places" array with 4–8 key on-the-ground stops in itinerary order (hotels, towns, attractions)
- map_places must stay inside the destination region only — do NOT include home-country airports or overseas connections that cannot be traveled as one continuous route
- Format each map_places item as an object: {{"name": "place or hotel name", "city": "city or town", "country": "country"}}
- For each hotel and each activity, include a realistic "url" field with a booking or info link when possible (Booking.com, official site, GetYourGuide, etc.)
- Include 3 short "faqs" that a traveler would actually ask about this trip
- Return ONLY valid JSON in this exact structure:

{{
  "title": "appealing title",
  "location": "main destination (City/Region, Country)",
  "summary": "2-4 sentence overview",
  "constraints": ["constraint 1", "constraint 2", "constraint 3"],
  "hotels": [
    {{"name": "place name", "why": "why it fits", "price_range": "$XXX-YYY per night", "area": "neighborhood", "url": "https://example.com"}}
  ],
  "itinerary": [
    {{"day": 1, "title": "theme", "description": "2-3 sentence overview of the day", "activities": ["specific thing 1", "specific thing 2"], "tips": "practical tip", "activity_urls": ["https://example.com", "https://example.com"]}}
  ],
  "map_places": [
    {{"name": "Place name", "city": "City", "country": "Country"}}
  ],
  "faqs": [
    {{"question": "short question", "answer": "concise practical answer"}}
  ],
  "transport": "how to get around + any notes",
  "budget_notes": "realistic budget guidance"
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"},
            timeout=45,
        )
        assembly = json.loads(response.choices[0].message.content)
    except Exception as e:
        assembly = {
            "title": f"Trip: {request[:70]}",
            "location": "See request",
            "summary": f"Generation failed: {str(e)}",
            "constraints": [request],
            "hotels": [{"name": "Error", "why": "AI call failed", "price_range": "—", "area": "—"}],
            "itinerary": [{"day": 1, "title": "Error", "activities": ["Try again"], "tips": ""}],
            "map_places": [],
            "faqs": [],
            "transport": "—",
            "budget_notes": "—",
        }

    title = assembly.get("title") or f"Trip: {request[:70]}"
    location = assembly.get("location") or ""
    slug = f"{slugify(title)}-{stamp}"
    assembly["slug"] = slug

    places = normalize_places(assembly.get("map_places", []), location)
    map_url, open_url = build_map_urls(places, location)
    map_html = map_block_html(places, location, map_url, open_url)

    hotels_html = hotels_to_html(assembly.get("hotels", []))
    itinerary_html = itinerary_to_html(assembly.get("itinerary", []))
    faqs_html = faqs_to_html(assembly.get("faqs", []))

    index = load_index()
    related_html = related_to_html(index, slug, location)

    page_url = f"{BASE_URL}/pages/{slug}.html"
    summary = assembly.get("summary", "")
    desc = meta_description(summary)
    json_ld = build_json_ld(
        page_url, title, summary, location, assembly.get("itinerary", []), assembly.get("faqs", [])
    )

    html_out = PAGE_TEMPLATE.format(
        title=esc(title),
        meta_desc=esc(desc),
        page_url=esc(page_url),
        json_ld=json_ld,
        location=esc(location),
        constraints=esc(", ".join(str(c) for c in assembly.get("constraints", []))),
        summary=esc(summary),
        map_html=map_html,
        hotels_html=hotels_html,
        itinerary_html=itinerary_html,
        transport=esc(assembly.get("transport", "")),
        budget_notes=esc(assembly.get("budget_notes", "")),
        faqs_html=faqs_html,
        related_html=related_html,
    )

    with open(os.path.join(PAGES_DIR, f"{slug}.html"), "w") as f:
        f.write(html_out)

    index.insert(0, {
        "slug": slug,
        "title": title,
        "location": location,
        "created_at": created_at.strftime("%Y-%m-%d"),
    })
    save_index(index)

    return RedirectResponse(f"/pages/{slug}.html", status_code=303)


@app.get("/sitemap.xml")
async def sitemap():
    index = load_index()
    urls = [{"loc": f"{BASE_URL}/", "lastmod": None}]
    for item in index:
        if not item.get("slug"):
            continue
        urls.append({
            "loc": f"{BASE_URL}/pages/{item['slug']}.html",
            "lastmod": item.get("created_at"),
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
    return Response(
        content=f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n",
        media_type="text/plain",
    )


app.mount("/pages", StaticFiles(directory=PAGES_DIR), name="pages")

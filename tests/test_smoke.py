"""Smoke tests with OpenAI and Wikipedia mocked. No network."""
import json
import os
import re
import shutil
import sys
import tempfile
import time
import unittest
from urllib.parse import unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = tempfile.mkdtemp(prefix="tripassembler-test-")
os.environ["PAGES_DIR"] = os.path.join(TMP, "pages")
os.environ["INDEX_FILE"] = os.path.join(TMP, "index.json")
os.environ["WIKI_CACHE"] = os.path.join(TMP, "wiki.json")
os.environ["OPENAI_API_KEY"] = "test-key"
os.environ["GOOGLE_MAPS_API_KEY"] = "test-maps-key"
os.environ["BASE_URL"] = "https://www.tripassembler.com"
sys.path.insert(0, ROOT)

import httpx
from fastapi.testclient import TestClient
from starlette.middleware.gzip import GZipMiddleware

import app

ASSEMBLY = {
    "title": "A long weekend in Reykjavik",
    "location": "Reykjavik, Iceland",
    "wiki_title": "Reykjavík",
    "summary": "A walkable long weekend built around the church, the harbor, and good food.",
    "constraints": ["Couple", "$150-300/night", "Walkable"],
    "hotels": [{
        "name": "Harbor House",
        "why": "Walk to Hallgrímskirkja",
        "price_range": "$180-260 per night",
        "area": "Midbaer",
        "url": "https://www.booking.com/hotel/is/harbor-house.html",
    }],
    "itinerary": [{
        "day": 1,
        "title": "Hallgrímskirkja and the harbor",
        "description": "Start at the church, then walk to the concert hall.",
        "activities": ["Climb Hallgrímskirkja", "See Harpa", "Dinner downtown"],
        "tips": "Book the tower early.",
        "activity_urls": ["https://www.hallgrimskirkja.is/"],
        "wiki_title": "Hallgrímskirkja",
    }],
    "map_places": [
        {
            "name": "Hallgrímskirkja",
            "city": "Reykjavik",
            "country": "Iceland",
            "wiki_title": "Hallgrímskirkja",
        },
        {
            "name": "Nowhere Special",
            "city": "Reykjavik",
            "country": "Iceland",
            "wiki_title": "MissingPlace",
        },
        {
            "name": "Harpa",
            "city": "Reykjavik",
            "country": "Iceland",
            "wiki_title": "Harpa (concert hall)",
        },
    ],
    "faqs": [{"question": "How many nights?", "answer": "Three nights is enough for a first visit."}],
    "transport": "Walk the center.",
    "budget_notes": "Meals are the flexible part.",
}


class _Msg:
    def __init__(self, content):
        self.content = content


class _Choice:
    def __init__(self, content):
        self.message = _Msg(content)


class _Resp:
    def __init__(self, content):
        self.choices = [_Choice(content)]


class FakeClient:
    def __init__(self, fn):
        self.calls = []

        class Completions:
            async def create(inner, **kwargs):
                self.calls.append(kwargs)
                return await fn(**kwargs)

        class Chat:
            completions = Completions()

        self.chat = Chat()


WIKI_CALLS = []
WIKI_MODE = {"empty": False}


def _photo_identity(url):
    if "Reykjav" in url:
        return "Reykjavik", "Reykjavík"
    if "Hallgr" in url:
        return "Hallgrimskirkja", "Hallgrímskirkja"
    if "Harpa" in url:
        return "Harpa", "Harpa (concert hall)"
    decoded = unquote(url)
    match = re.search(r"(?:gsrsearch|titles)=([^&]+)", decoded)
    raw = match.group(1) if match else "Place"
    token = re.sub(r"[^A-Za-z0-9]+", "", raw)[:48] or "Place"
    title = re.split(r"[, ]", raw.strip())[0] or token
    return token, title


def _place_hint(url):
    """Enough of a place name for the quality filter, including ambiguous cities."""
    low = unquote(url).casefold()
    if "lisbon" in low:
        return "Lisbon Portugal Belem"
    if "paris" in low:
        return "Paris France"
    if "amsterdam" in low:
        return "Amsterdam Netherlands canal"
    if "reykjav" in low or "iceland" in low or "hallgr" in low or "harpa" in low:
        return "Reykjavik Iceland"
    return ""


def wiki_handler(request):
    url = str(request.url)
    WIKI_CALLS.append(url)
    if WIKI_MODE["empty"]:
        return httpx.Response(503, text="unavailable")
    if "MissingPlace" in url or "Nowhere" in url:
        if "rest_v1" in url:
            return httpx.Response(404, json={"type": "not_found"})
        return httpx.Response(200, json={"query": {"pages": {"-1": {"missing": ""}}}})
    slug, title = _photo_identity(url)
    hint = _place_hint(url) or title
    file_name = f"{slug}.jpg"
    if "prop=imageinfo" in url or "iiurlwidth=" in url:
        return httpx.Response(200, json={"query": {"pages": {"1": {
            "title": f"File:{file_name}",
            "imageinfo": [{
                "thumburl": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8b/{file_name}/640px-{file_name}",
                "thumbwidth": 640,
                "thumbheight": 480,
                "width": 1600,
                "height": 1000,
                "mime": "image/jpeg",
                "descriptionurl": f"https://commons.wikimedia.org/wiki/File:{file_name}",
                "extmetadata": {
                    "DateTimeOriginal": {"value": "2018-06-01 12:00:00"},
                    "ObjectName": {"value": f"{title} {hint}"},
                    "ImageDescription": {"value": hint},
                    "Categories": {"value": f"{hint}|Quality images"},
                },
            }],
        }}}})
    if "prop=images" in url or "imlimit=" in url:
        return httpx.Response(200, json={"query": {"pages": {"1": {"title": "Place", "images": []}}}})
    if "rest_v1" in url:
        return httpx.Response(200, json={
            "type": "standard",
            "title": title,
            "thumbnail": {
                "source": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8b/{file_name}/330px-{file_name}",
                "width": 330,
                "height": 290,
            },
            "content_urls": {"desktop": {"page": f"https://en.wikipedia.org/wiki/{slug}"}},
        })
    return httpx.Response(200, json={"query": {"pages": {"1": {
        "title": title,
        "pageimage": file_name,
        "thumbnail": {
            "source": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8b/{file_name}/640px-{file_name}",
            "width": 640,
            "height": 480,
        },
        "fullurl": f"https://en.wikipedia.org/wiki/{slug}",
    }}}})


def fake_wiki_client(*args, **kwargs):
    return httpx.AsyncClient(transport=httpx.MockTransport(wiki_handler), timeout=3.0)


class SmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cm = TestClient(app.app)
        cls.client = cls._cm.__enter__()

    @classmethod
    def tearDownClass(cls):
        cls._cm.__exit__(None, None, None)

    def setUp(self):
        app.JOBS.clear()
        app._image_cache.clear()
        app._cache_loaded = True
        app._page_mem.clear()
        app._catalog["key"] = None
        app._catalog["items"] = []
        app.reset_assignments()
        WIKI_CALLS.clear()
        WIKI_MODE["empty"] = False
        cache = os.environ["WIKI_CACHE"]
        if os.path.exists(cache):
            os.remove(cache)
        pages = os.environ["PAGES_DIR"]
        if os.path.isdir(pages):
            for name in os.listdir(pages):
                target = os.path.join(pages, name)
                if os.path.isdir(target):
                    shutil.rmtree(target)
                else:
                    os.remove(target)
        index = os.environ["INDEX_FILE"]
        if os.path.exists(index):
            os.remove(index)
        app.wiki_client = fake_wiki_client

    def test_home_guided_form(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        text = response.text
        self.assertIn('name="where"', text)
        self.assertIn('name="budget"', text)
        self.assertIn('name="who"', text)
        self.assertIn('name="must"', text)
        self.assertIn('name="when"', text)
        self.assertIn('name="interests"', text)
        self.assertIn('name="captcha"', text)
        self.assertIn("Under $150/night", text)
        self.assertIn("$150–300/night", text)
        self.assertIn("Family with kids", text)
        self.assertIn("Pet-friendly", text)
        self.assertIn("This weekend", text)
        self.assertIn("Relaxed pace", text)
        self.assertIn("Try an example", text)
        self.assertIn('type="button"', text)
        self.assertIn('action="/assemble"', text)
        self.assertIn("role=\"meter\"", text)
        self.assertIn("Add a destination so we know where to plan.", text)
        self.assertIn("Assemble the perfect Trip", text)
        self.assertNotIn("perfect stay", text.lower())
        self.assertIn(f"/styles.css?v={app.STYLES_VERSION}", text)
        self.assertIn("Best pet-friendly in Bangkok", text)
        self.assertIn("logo-svg", text)
        self.assertIn("required", text)

    def test_example_and_strength_tip(self):
        example = self.client.get("/", params={"example": "1"})
        self.assertIn('value="Reykjavik, Iceland"', example.text)
        self.assertIn("Ready to assemble", example.text)
        self.assertIn('aria-valuenow="5"', example.text)
        partial = self.client.get("/", params={
            "where": "Lisbon, Portugal",
            "who": "Couple",
            "budget": "Under $150/night",
            "must": "Walkable",
        })
        self.assertIn("Add how many nights for a better day-by-day plan.", partial.text)
        self.assertIn('aria-valuenow="4"', partial.text)

    def test_home_escapes_query(self):
        response = self.client.get("/", params={"where": '<script>alert(1)</script>'})
        self.assertNotIn("<script>alert", response.text)
        self.assertIn("&lt;script&gt;", response.text)

    def test_compose_and_places(self):
        text = app.compose_request(
            where="Lisbon, Portugal",
            budget="Under $150/night",
            who="Solo",
            must="Walkable, Kitchen",
            when="5 nights",
            interests="Food, Museums",
        )
        self.assertTrue(text.startswith("Plan a trip with these constraints:"))
        self.assertIn("Where: Lisbon, Portugal", text)
        self.assertIn("Pace and interests: Food, Museums", text)
        places = app.normalize_places("Hallgrímskirkja, Reykjavik, Iceland", "Reykjavik, Iceland")
        self.assertEqual(len(places), 1)
        self.assertIn("Hallgrímskirkja", places[0])
        records = app._clean_records(
            [{"name": "Hallgrímskirkja", "city": "Reykjavik", "country": "Iceland", "wiki_title": "Hallgrímskirkja"}],
            "Reykjavik, Iceland",
        )
        self.assertEqual(records[0]["wiki_title"], "Hallgrímskirkja")

    def test_captcha_and_destination_keep_inputs(self):
        bad = self.client.post("/assemble", data={
            "where": "Oslo, Norway",
            "interests": "Food",
            "captcha": "no",
        })
        self.assertEqual(bad.status_code, 400)
        self.assertIn("Oslo, Norway", bad.text)
        self.assertIn("Please answer correctly.", bad.text)
        self.assertIn("Food", bad.text)
        self.assertEqual(app.JOBS, {})
        missing = self.client.post("/assemble", data={"captcha": "7"})
        self.assertEqual(missing.status_code, 400)
        self.assertIn("destination", missing.text.lower())

    def test_assemble_job_images_and_page(self):
        async def succeed(**kwargs):
            await __import__("asyncio").sleep(0.6)
            return _Resp(json.dumps(ASSEMBLY))

        app.client = FakeClient(succeed)
        started = time.perf_counter()
        response = self.client.post("/assemble", data={
            "where": "Reykjavik, Iceland",
            "budget": "$150-300/night",
            "who": "Couple",
            "must": "Walkable, Kitchen",
            "when": "5 nights in June",
            "interests": "Food, Nature",
            "captcha": "7",
        }, follow_redirects=False)
        elapsed = time.perf_counter() - started
        self.assertLess(elapsed, 0.45)
        self.assertEqual(response.status_code, 303)
        location = response.headers["location"]
        self.assertTrue(location.startswith("/assembling/"))
        job_id = location.rsplit("/", 1)[-1]
        self.assertRegex(job_id, r"^[a-f0-9]{16}$")

        progress = self.client.get(location, follow_redirects=False)
        self.assertEqual(progress.status_code, 200)
        self.assertIn("Reading your constraints", progress.text)
        self.assertIn("Reykjavik, Iceland", progress.text)
        self.assertIn("route-line", progress.text)
        self.assertIn("What you asked for", progress.text)
        self.assertIn('aria-live="polite"', progress.text)

        early = self.client.get(f"/api/jobs/{job_id}").json()
        self.assertIn(early["status"], ("queued", "working"))

        deadline = time.time() + 4
        body = early
        while time.time() < deadline:
            body = self.client.get(f"/api/jobs/{job_id}").json()
            if body["status"] in {"done", "error"}:
                break
            time.sleep(0.05)
        self.assertEqual(body["status"], "done", body)
        self.assertTrue(body["redirect"].startswith("/pages/"))
        self.assertEqual(app.client.calls[0]["model"], "gpt-4o-mini")
        self.assertEqual(app.client.calls[0]["max_tokens"], 2400)
        prompt = app.client.calls[0]["messages"][0]["content"]
        self.assertIn("wiki_title", prompt)
        self.assertIn("Reykjavik, Iceland", prompt)
        self.assertIn("Pace and interests: Food, Nature", prompt)

        page = self.client.get(body["redirect"])
        self.assertEqual(page.status_code, 200)
        self.assertEqual(page.text.count('class="hero-photo"'), 1)
        self.assertEqual(page.text.count('class="stop-thumb"'), 2)
        self.assertEqual(page.text.count('class="day-photo"'), 1)
        self.assertIn("loading=\"lazy\"", page.text)
        self.assertIn("decoding=\"async\"", page.text)
        self.assertIn('width="640"', page.text)
        self.assertIn("thumb.wikimedia.org", page.text)
        self.assertIn("wikipedia.org", page.text)
        self.assertIn("Wikipedia", page.text)
        self.assertIn("Hallgrímskirkja", page.text)
        self.assertIn("Nowhere Special", page.text)
        self.assertIn("Book / View", page.text)
        self.assertIn("maps/embed", page.text)
        self.assertIn('class="stops"', page.text)
        self.assertIn("Open route in Google Maps", page.text)
        self.assertIn("TouristTrip", page.text)
        self.assertIn("FAQPage", page.text)
        self.assertIn("Assemble the perfect Trip", page.text)
        self.assertNotIn("perfect stay", page.text.lower())
        self.assertEqual(page.text.count('id="related-trips"'), 1)
        related = page.text.split('id="related-trips"', 1)[1].split("</section>", 1)[0]
        related_links = re.findall(r'href="(/pages/[^"]+)"', related)
        self.assertGreaterEqual(len(related_links), 3)
        self.assertIn(f"/styles.css?v={app.STYLES_VERSION}", page.text)
        self.assertNotIn("MissingPlace", page.text.split("Nowhere Special")[1][:400])

        sitemap = self.client.get("/sitemap.xml")
        slug = body["redirect"].rsplit("/", 1)[-1]
        self.assertIn(slug, sitemap.text)
        self.assertIn("amsterdam-city-center-walkable", sitemap.text)

    def test_generation_error_keeps_inputs(self):
        async def explode(**kwargs):
            raise RuntimeError("boom-secret")

        app.client = FakeClient(explode)
        response = self.client.post("/assemble", data={
            "where": "Lisbon, Portugal",
            "budget": "Luxury",
            "captcha": "7",
        }, follow_redirects=False)
        self.assertEqual(response.status_code, 303)
        job_id = response.headers["location"].rsplit("/", 1)[-1]
        deadline = time.time() + 3
        body = {}
        while time.time() < deadline:
            body = self.client.get(f"/api/jobs/{job_id}").json()
            if body["status"] == "error":
                break
            time.sleep(0.05)
        self.assertEqual(body["status"], "error")
        self.assertNotIn("boom-secret", body["error"])
        page = self.client.get(f"/assembling/{job_id}")
        self.assertIn("Try again", page.text)
        self.assertIn("where=Lisbon", page.text)
        self.assertNotIn("boom-secret", page.text)
        self.assertNotIn("route-line", page.text)

    def test_unknown_job(self):
        missing = "ab" * 8
        page = self.client.get(f"/assembling/{missing}")
        self.assertEqual(page.status_code, 404)
        self.assertIn("restarted", page.text.lower())
        api = self.client.get(f"/api/jobs/{missing}")
        self.assertEqual(api.status_code, 404)
        self.assertEqual(api.json()["status"], "error")
        junk = self.client.get("/assembling/not-a-job")
        self.assertEqual(junk.status_code, 404)
        self.assertIn("restarted", junk.text.lower())
        self.assertIn("Assemble the perfect Trip", junk.text)
        self.assertNotIn("perfect stay", junk.text.lower())

    def test_legacy_sitemap_health_and_css(self):
        legacy = self.client.get("/pages/amsterdam-city-center-walkable")
        self.assertEqual(legacy.status_code, 200)
        self.assertIn("Amsterdam", legacy.text)
        self.assertIn("Assemble a new trip", legacy.text)
        self.assert_enhanced_page(legacy.text, require_stops=False)
        calls_after_first = len(WIKI_CALLS)
        again = self.client.get("/pages/amsterdam-city-center-walkable")
        self.assertEqual(again.status_code, 200)
        self.assertEqual(len(WIKI_CALLS), calls_after_first)
        self.assertEqual(again.text.count('id="related-trips"'), 1)
        robots = self.client.get("/robots.txt")
        self.assertIn("Sitemap:", robots.text)
        self.assertIn("/assembling/", robots.text)
        health = self.client.get("/healthz")
        self.assertEqual(health.status_code, 200)
        self.assertEqual(health.text, "ok")
        self.assertIn("no-store", health.headers["cache-control"])
        versioned = self.client.get("/styles.css", params={"v": app.STYLES_VERSION})
        self.assertEqual(versioned.status_code, 200)
        self.assertIn("immutable", versioned.headers["cache-control"])
        self.assertIn("--accent: #1e40af", versioned.text)
        self.assertIn("prefers-reduced-motion", versioned.text)
        plain = self.client.get("/styles.css")
        self.assertIn("max-age=86400", plain.headers["cache-control"])
        self.assertNotIn("immutable", plain.headers["cache-control"])
        self.assertTrue(any(getattr(m, "cls", None) is GZipMiddleware for m in app.app.user_middleware))

    def assert_enhanced_page(self, text, require_stops=False, slug=""):
        self.assertIn('class="hero-photo"', text)
        self.assertIn('loading="lazy"', text)
        self.assertIn('decoding="async"', text)
        self.assertRegex(text, r'width="\d+"')
        self.assertRegex(text, r'height="\d+"')
        self.assertRegex(text, r'alt="[^"]+"')
        self.assertIn("Wikipedia", text)
        self.assertIn("wikipedia.org", text)
        self.assertIn("Assemble the perfect Trip", text)
        self.assertNotIn("perfect stay", text.lower())
        self.assertEqual(text.count('id="related-trips"'), 1)
        self.assertNotIn("More trip assemblies", text)
        section = text.split('id="related-trips"', 1)[1].split("</section>", 1)[0]
        links = re.findall(r'href="(/pages/[^"]+\.html)"', section)
        self.assertGreaterEqual(len(links), 3)
        self.assertTrue(all(link.startswith("/pages/") for link in links))
        if slug:
            self.assertNotIn(f"/pages/{slug}.html", links)
        if require_stops:
            self.assertIn('class="stop-thumb"', text)
        # Photos that failed to resolve must not leave an empty image.
        self.assertNotIn('src=""', text)
        if "<h2" in text and 'class="hero-photo"' in text:
            self.assertLess(text.find("</h2>"), text.find('class="hero-photo"'))

    def _write_legacy(self, directory, slug, title, summary, stops=None):
        stop_html = ""
        if stops:
            items = "".join(
                f'<li><a href="https://www.google.com/maps/search/?api=1&query={label}">{label}</a></li>'
                for label in stops
            )
            stop_html = f'<ol class="stops">{items}</ol>'
        document = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>{title} | TripAssembler</title></head>
<body>
<header><a class="brand" href="/"><h1>TripAssembler</h1></a></header>
<div class="container">
  <div class="page-icon"><svg></svg></div>
  <h2 style="margin:0 0 8px;">{title}</h2>
  <p style="color:var(--muted); margin-top:0;">{summary}</p>
  <div class="card"><h3>Recommended options</h3>{stop_html}</div>
  <div class="actions"><button>Save</button></div>
</div>
<footer><a href="/">Home</a></footer>
</body></html>
"""
        with open(os.path.join(directory, slug + ".html"), "w", encoding="utf-8") as handle:
            handle.write(document)

    def test_serve_time_images_related_and_cache(self):
        legacy_dir = tempfile.mkdtemp(prefix="tripassembler-legacy-")
        original_legacy = app.LEGACY_DIR
        app.LEGACY_DIR = legacy_dir
        app._catalog["key"] = None
        try:
            self._write_legacy(
                legacy_dir,
                "lisbon-pet-friendly",
                "Best pet-friendly in Lisbon",
                "Assembled for pet-friendly in Lisbon.",
                stops=["Belem Tower, Lisbon, Portugal"],
            )
            self._write_legacy(
                legacy_dir,
                "lisbon-family-friendly-with-kitchen",
                "Best family-friendly with kitchen in Lisbon",
                "Assembled for family-friendly with kitchen in Lisbon.",
            )
            self._write_legacy(
                legacy_dir,
                "lisbon-budget-under-200night",
                "Best budget under $200/night in Lisbon",
                "Assembled for budget under $200/night in Lisbon.",
            )
            self._write_legacy(
                legacy_dir,
                "paris-pet-friendly",
                "Best pet-friendly in Paris",
                "Assembled for pet-friendly in Paris.",
            )
            disk = os.path.join(os.environ["PAGES_DIR"], "old-lisbon-weekend.html")
            disk_html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>Old Lisbon weekend | TripAssembler</title>
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"TouristTrip","name":"Old Lisbon weekend","description":"A walk along the river.","touristDestination":{"@type":"Place","name":"Lisbon, Portugal"}}]}</script>
</head><body>
<header><a class="brand" href="/"><h1>TripAssembler</h1></a></header>
<div class="container">
  <div class="page-icon"><svg></svg></div>
  <h2 style="margin:0 0 8px;">Old Lisbon weekend</h2>
  <p style="color:var(--muted); margin-top:0;"><strong>Location:</strong> Lisbon, Portugal</p>
  <p class="old-tag">Assemble the perfect stay</p>
  <div class="card">
    <h2>Route map</h2>
    <ol class="stops">
      <li><a href="https://www.google.com/maps/search/?api=1&query=Belem">Belem Tower, Lisbon, Portugal</a></li>
      <li><a href="https://www.google.com/maps/search/?api=1&query=Jeronimos">Jeronimos Monastery, Lisbon, Portugal</a></li>
    </ol>
  </div>
  <div class="card">
    <h2>Suggested Itinerary</h2>
    <div class="day"><h3>Day 1: Belem Tower and the river</h3><p>Walk the waterfront.</p></div>
  </div>
  <div class="card"><h2>More trip assemblies</h2><ul><li><a href="/pages/paris-pet-friendly.html">Paris</a></li></ul></div>
  <div class="actions"><button type="button">Print / Save PDF</button></div>
</div>
<footer>TripAssembler</footer>
</body></html>
"""
            with open(disk, "w", encoding="utf-8") as handle:
                handle.write(disk_html)
            with open(os.environ["INDEX_FILE"], "w", encoding="utf-8") as handle:
                json.dump([{
                    "slug": "old-lisbon-weekend",
                    "title": "Old Lisbon weekend",
                    "location": "Lisbon, Portugal",
                    "created_at": "2024-05-01",
                }], handle)

            legacy = self.client.get("/pages/lisbon-pet-friendly")
            self.assertEqual(legacy.status_code, 200)
            self.assert_enhanced_page(legacy.text, require_stops=True, slug="lisbon-pet-friendly")
            self.assertIn("Best pet-friendly in Lisbon", legacy.text)

            disk_response = self.client.get("/pages/old-lisbon-weekend")
            self.assertEqual(disk_response.status_code, 200)
            self.assert_enhanced_page(disk_response.text, require_stops=True, slug="old-lisbon-weekend")
            self.assertIn('class="day-photo"', disk_response.text)
            self.assertIn("Walk the waterfront.", disk_response.text)
            block = re.search(
                r'<script type="application/ld\+json">(.*?)</script>',
                disk_response.text,
                re.S,
            )
            self.assertIsNotNone(block)
            data = json.loads(block.group(1).replace("<\\/", "</"))
            self.assertEqual(data["@graph"][0]["@type"], "TouristTrip")
            self.assertTrue(str(data["@graph"][0].get("image", "")).startswith("https://"))
            with open(disk, encoding="utf-8") as handle:
                saved = handle.read()
            self.assertIn(app.ENHANCED_MARKER, saved)
            self.assertIn('class="hero-photo"', saved)

            calls_after = len(WIKI_CALLS)
            self.assertGreater(calls_after, 0)
            app._page_mem.clear()
            repeat_legacy = self.client.get("/pages/lisbon-pet-friendly")
            repeat_disk = self.client.get("/pages/old-lisbon-weekend.html")
            self.assertEqual(repeat_legacy.status_code, 200)
            self.assertEqual(repeat_disk.status_code, 200)
            self.assertEqual(len(WIKI_CALLS), calls_after)
            self.assertEqual(repeat_disk.text.count('id="related-trips"'), 1)
            self.assertIn("Assemble the perfect Trip", repeat_legacy.text)

            sitemap = self.client.get("/sitemap.xml")
            self.assertEqual(sitemap.status_code, 200)
            self.assertIn("lisbon-pet-friendly", sitemap.text)
            self.assertIn("old-lisbon-weekend", sitemap.text)
            section = disk_response.text.split('id="related-trips"', 1)[1]
            for link in re.findall(r'href="/pages/([^"]+)\.html"', section)[:3]:
                self.assertIn(link, sitemap.text)
            health = self.client.get("/healthz")
            self.assertEqual(health.status_code, 200)
            self.assertEqual(health.text, "ok")
        finally:
            app.LEGACY_DIR = original_legacy
            app._catalog["key"] = None
            app._catalog["items"] = []
            shutil.rmtree(legacy_dir, ignore_errors=True)

    def test_image_lookup_failure_serves_original(self):
        disk = os.path.join(os.environ["PAGES_DIR"], "old-porto-notes.html")
        original = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>Old Porto notes in Lisbon | TripAssembler</title></head>
<body>
<header><a class="brand" href="/"><h1>TripAssembler</h1></a></header>
<div class="container">
  <h2>Old Porto notes in Lisbon</h2>
  <p>Assemble the perfect stay</p>
  <p>The cellars are still in this page.</p>
  <div class="actions"><button>Print</button></div>
</div>
<footer>TripAssembler</footer>
</body></html>
"""
        with open(disk, "w", encoding="utf-8") as handle:
            handle.write(original)

        async def explode(*args, **kwargs):
            raise RuntimeError("wiki down")

        original_assign = app.assign_hero_image
        app.assign_hero_image = explode
        try:
            response = self.client.get("/pages/old-porto-notes")
        finally:
            app.assign_hero_image = original_assign
        self.assertEqual(response.status_code, 200)
        self.assertIn("Old Porto notes", response.text)
        self.assertIn("The cellars are still in this page.", response.text)
        self.assertIn("Assemble the perfect Trip", response.text)
        self.assertNotIn("perfect stay", response.text.lower())
        self.assertNotIn("hero-photo", response.text)
        self.assertNotIn("wiki down", response.text)
        self.assertNotIn("Traceback", response.text)
        with open(disk, encoding="utf-8") as handle:
            self.assertNotIn(app.ENHANCED_MARKER, handle.read())

        WIKI_MODE["empty"] = True
        WIKI_CALLS.clear()
        app._page_mem.clear()
        missed = self.client.get("/pages/old-porto-notes")
        self.assertEqual(missed.status_code, 200)
        self.assertIn("The cellars are still in this page.", missed.text)
        self.assertNotIn('class="hero-photo"', missed.text)
        self.assertNotIn('src=""', missed.text)
        self.assertIn('id="related-trips"', missed.text)
        self.assertIn("Assemble the perfect Trip", missed.text)
        calls_after = len(WIKI_CALLS)
        app._page_mem.clear()
        self.client.get("/pages/old-porto-notes")
        self.assertEqual(len(WIKI_CALLS), calls_after)

    def test_same_city_heroes_are_distinct(self):
        pool = []
        for index in range(4):
            pool.append({
                "file": f"photo-{index}.jpg",
                "src": f"https://upload.wikimedia.org/wikipedia/commons/photo-{index}.jpg",
                "width": 640,
                "height": 400,
                "page": f"https://en.wikipedia.org/wiki/Photo_{index}",
                "title": f"Photo {index}",
            })
        self.assertTrue(app.is_real_photo(pool[0]["src"], "Photo 0"))
        self.assertFalse(app.is_real_photo(
            "https://upload.wikimedia.org/wikipedia/commons/Flag_of_Amsterdam.svg",
            "Flag of Amsterdam.svg",
        ))
        self.assertFalse(app.is_real_photo(
            "https://upload.wikimedia.org/wikipedia/commons/Map_of_Amsterdam.png",
            "Map of Amsterdam.png",
        ))
        places = ["Amsterdam", "Netherlands"]
        good = {
            "file": "amsterdam_canal_2018.jpg",
            "title": "Amsterdam canal 2018",
            "full_width": 1600,
            "full_height": 900,
            "meta_blob": "Amsterdam Quality images 2018-06-01",
        }
        self.assertTrue(app.passes_quality(good, places, ()))
        self.assertFalse(app.passes_quality(
            dict(good, title="Banquet of the Amsterdam Civic Guard", file="banquet.jpg", meta_blob="oil on canvas 1648"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="Old Amsterdam 1891 street", file="old-amsterdam_1891-street-1.jpg", meta_blob="1891"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="Gercse osszel", file="gercse_osszel.jpg", meta_blob="Gercse Hungary autumn"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(dict(good, full_width=800, full_height=1200), places, ()))
        self.assertFalse(app.passes_quality(dict(good, full_width=600, full_height=400), places, ()))
        self.assertFalse(app.passes_quality(
            dict(good, title="HEADER", file="header.jpg", trusted=True, meta_blob="Paris skyline"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="Athens Georgia City Hall", file="athens_georgia_city_hall.jpg", meta_blob="Georgia"),
            ["Athens", "Greece"],
            ("georgia",),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="Iceland satellite", file="iceland_satellite.jpg", meta_blob="Iceland"),
            ["Iceland"],
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="A girl posing in a flower field", file="girl_posing.jpg"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, title="Breviceps gibbosus Cape Rain Frog", file="breviceps.jpg"),
            places,
            (),
        ))
        self.assertFalse(app.passes_quality(
            dict(good, page="https://en.wikipedia.org/wiki/London_Eye"),
            places,
            (),
        ))
        self.assertTrue(app.passes_quality(
            dict(good, page="https://commons.wikimedia.org/wiki/File:Amsterdam_canal_2018.jpg"),
            places,
            (),
        ))
        self.assertIsNone(app.choose_distinct("amsterdam-pet-friendly", pool, {image["file"] for image in pool}))
        taken = set()
        picked = []
        for slug in ("amsterdam-pet-friendly", "amsterdam-with-private-pool", "amsterdam-walkable"):
            image = app.choose_distinct(slug, pool, taken)
            self.assertIsNotNone(image)
            self.assertNotIn(image["file"], taken)
            taken.add(image["file"])
            picked.append(image["file"])
        again = app.choose_distinct("amsterdam-pet-friendly", pool, set())
        self.assertEqual(again["file"], picked[0])

        photos = [
            ("Amsterdam_canal_houses_2019.jpg", "Amsterdam canal houses 2019"),
            ("Amsterdam_rijksmuseum_2018.jpg", "Amsterdam rijksmuseum 2018"),
            ("Amsterdam_vondelpark_2016.jpg", "Amsterdam vondelpark 2016"),
            ("Amsterdam_jordaan_2014.jpg", "Amsterdam jordaan 2014"),
        ]

        def rich_handler(request):
            url = unquote(str(request.url))
            WIKI_CALLS.append(url)
            if "prop=imageinfo" in url or "iiurlwidth=" in url:
                pages = {}
                include_all = "filetype:bitmap" in url or "File:" in url
                for index, (name, label) in enumerate(photos, start=1):
                    if not include_all and name not in url and label not in url:
                        continue
                    pages[str(index)] = {
                        "title": f"File:{name}",
                        "imageinfo": [{
                            "thumburl": f"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a{index}/{name}/1280px-{name}",
                            "thumbwidth": 1280,
                            "thumbheight": 800,
                            "width": 1600,
                            "height": 1000,
                            "mime": "image/jpeg",
                            "descriptionurl": f"https://commons.wikimedia.org/wiki/File:{name}",
                            "extmetadata": {
                                "DateTimeOriginal": {"value": "2018-06-01 12:00:00"},
                                "ObjectName": {"value": label},
                                "Categories": {"value": "Amsterdam|Quality images"},
                            },
                        }],
                    }
                return httpx.Response(200, json={"query": {"pages": pages}})
            if "prop=images" in url or "imlimit=" in url:
                images = [{"title": f"File:{name}"} for name, _label in photos]
                images.append({"title": "File:Flag_of_Amsterdam.svg"})
                images.append({"title": "File:Map_of_Amsterdam.png"})
                return httpx.Response(200, json={"query": {"pages": {"12": {
                    "title": "Amsterdam",
                    "images": images,
                }}}})
            pages = {
                "50": {
                    "index": 0,
                    "title": "Map of Amsterdam",
                    "thumbnail": {
                        "source": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Map_of_Amsterdam.png/640px-Map_of_Amsterdam.png",
                        "width": 640,
                        "height": 480,
                    },
                    "fullurl": "https://en.wikipedia.org/wiki/Map_of_Amsterdam",
                },
            }
            for index, (name, label) in enumerate(photos, start=1):
                pages[str(index)] = {
                    "index": index,
                    "title": label,
                    "thumbnail": {
                        "source": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b{index}/{name}/640px-{name}",
                        "width": 640,
                        "height": 420,
                    },
                    "fullurl": f"https://en.wikipedia.org/wiki/{label.replace(' ', '_')}",
                }
            return httpx.Response(200, json={"query": {"pages": pages}})

        legacy_dir = tempfile.mkdtemp(prefix="tripassembler-distinct-")
        original_legacy = app.LEGACY_DIR
        original_client = app.wiki_client
        app.LEGACY_DIR = legacy_dir
        app._catalog["key"] = None
        app.wiki_client = lambda *args, **kwargs: httpx.AsyncClient(
            transport=httpx.MockTransport(rich_handler), timeout=3.0,
        )
        try:
            self._write_legacy(
                legacy_dir,
                "amsterdam-pet-friendly",
                "Best pet-friendly in Amsterdam",
                "Assembled for pet-friendly in Amsterdam.",
                stops=["Vondelpark, Amsterdam"],
            )
            self._write_legacy(
                legacy_dir,
                "amsterdam-with-private-pool",
                "Best with private pool in Amsterdam",
                "Assembled for a private pool in Amsterdam.",
                stops=["Vondelpark, Amsterdam"],
            )
            self._write_legacy(
                legacy_dir,
                "paris-pet-friendly",
                "Best pet-friendly in Paris",
                "Assembled for pet-friendly in Paris.",
            )
            first = self.client.get("/pages/amsterdam-pet-friendly")
            second = self.client.get("/pages/amsterdam-with-private-pool")
            self.assertEqual(first.status_code, 200)
            self.assertEqual(second.status_code, 200)
            hero_one = re.search(r'<figure class="hero-photo"><img src="([^"]+)"', first.text)
            hero_two = re.search(r'<figure class="hero-photo"><img src="([^"]+)"', second.text)
            self.assertIsNotNone(hero_one)
            self.assertIsNotNone(hero_two)
            self.assertNotEqual(hero_one.group(1), hero_two.group(1))
            self.assertNotIn("Map_of_Amsterdam", hero_one.group(1))
            self.assertNotIn("Flag_of_Amsterdam", hero_one.group(1))
            self.assertNotIn(".svg", hero_one.group(1).lower())
            self.assertIn("wikipedia.org", first.text.lower() + "wikimedia.org")
            self.assertRegex(first.text, r'class="hero-photo">.*href="https://[^"]+"', re.S)
            # The stop names the same park the pool may also contain. It must not repeat the hero.
            if 'class="stop-thumb"' in first.text:
                stop_src = re.search(r'class="stop-thumb" src="([^"]+)"', first.text).group(1)
                self.assertNotEqual(stop_src, hero_one.group(1))
            store = app.load_assignments()
            assigned = store["amsterdam|netherlands"]["assigned"]
            self.assertNotEqual(
                assigned["amsterdam-pet-friendly"]["file"],
                assigned["amsterdam-with-private-pool"]["file"],
            )
            section = app.related_section_html(
                "amsterdam-pet-friendly",
                "Best pet-friendly in Amsterdam",
                "",
            )
            self.assertIn(hero_two.group(1), section)
            self.assertNotIn(hero_one.group(1), section)
            calls_after = len(WIKI_CALLS)
            app._page_mem.clear()
            repeat = self.client.get("/pages/amsterdam-pet-friendly")
            self.assertEqual(repeat.status_code, 200)
            self.assertEqual(len(WIKI_CALLS), calls_after)
            self.assertIn(hero_one.group(1), repeat.text)
        finally:
            app.wiki_client = original_client
            app.LEGACY_DIR = original_legacy
            app._catalog["key"] = None
            app._catalog["items"] = []
            shutil.rmtree(legacy_dir, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()

"""Smoke tests with OpenAI and Wikipedia mocked. No network."""
import json
import os
import sys
import tempfile
import time
import unittest

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


def wiki_handler(request):
    url = str(request.url)
    if "MissingPlace" in url or "Nowhere" in url:
        if "rest_v1" in url:
            return httpx.Response(404, json={"type": "not_found"})
        return httpx.Response(200, json={"query": {"pages": {"-1": {"missing": ""}}}})
    title = "Reykjavík" if "Reykjav" in url else "Hallgrímskirkja"
    slug = "Reykjavik" if "Reykjav" in url else "Hallgrimskirkja"
    if "rest_v1" in url:
        return httpx.Response(200, json={
            "type": "standard",
            "title": title,
            "thumbnail": {
                "source": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8b/{slug}.jpg/330px-{slug}.jpg",
                "width": 330,
                "height": 290,
            },
            "content_urls": {"desktop": {"page": f"https://en.wikipedia.org/wiki/{slug}"}},
        })
    return httpx.Response(200, json={"query": {"pages": {"1": {
        "title": title,
        "thumbnail": {
            "source": f"https://thumb.wikimedia.org/wikipedia/commons/thumb/8/8b/{slug}.jpg/640px-{slug}.jpg",
            "width": 640,
            "height": 480,
        },
        "fullurl": f"https://en.wikipedia.org/wiki/{slug}",
    }}}})


def fake_wiki_client():
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
        cache = os.environ["WIKI_CACHE"]
        if os.path.exists(cache):
            os.remove(cache)
        pages = os.environ["PAGES_DIR"]
        if os.path.isdir(pages):
            for name in os.listdir(pages):
                os.remove(os.path.join(pages, name))
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

    def test_legacy_sitemap_health_and_css(self):
        legacy = self.client.get("/pages/amsterdam-city-center-walkable")
        self.assertEqual(legacy.status_code, 200)
        self.assertIn("Amsterdam", legacy.text)
        self.assertIn("Assemble a new trip", legacy.text)
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


if __name__ == "__main__":
    unittest.main()

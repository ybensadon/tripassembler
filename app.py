from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import json, os
from datetime import datetime
from openai import OpenAI

app = FastAPI()
PAGES_DIR = "/opt/render/project/src/pages"
INDEX_FILE = "/opt/render/project/src/index.json"
os.makedirs(PAGES_DIR, exist_ok=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MAPS_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")

def load_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE) as f:
            return json.load(f)
    return []

def save_index(data):
    with open(INDEX_FILE, "w") as f:
        json.dump(data, f, indent=2)

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | TripAssembler</title>
<meta name="description" content="{summary}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{summary}">
<meta property="og:type" content="article">
<style>
  body {{ font-family: system-ui, -apple-system, sans-serif; max-width: 820px; margin: 40px auto; line-height: 1.65; padding: 0 20px; color: #111; }}
  h1 {{ color: #004E89; font-size: 2rem; margin-bottom: 0.4em; }}
  .meta {{ color: #555; margin-bottom: 1em; }}
  .constraints {{ background: #f0f4f8; padding: 16px 18px; border-radius: 10px; margin: 1.2em 0; }}
  .map-container {{ margin: 1.5em 0 2em 0; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}
  iframe {{ width: 100%; height: 420px; border: 0; }}
  .day {{ background: #fff; border: 1px solid #e5e7eb; padding: 18px; margin: 16px 0; border-radius: 10px; }}
  .actions {{ margin: 2.5em 0; display: flex; gap: 10px; flex-wrap: wrap; }}
  .btn {{ padding: 10px 16px; border-radius: 8px; border: 1px solid #ddd; background: #fff; text-decoration: none; color: #333; font-size: 0.95em; }}
  .btn:hover {{ background: #f9fafb; }}
  @media print {{ .actions, .map-container {{ display: none; }} }}
</style>
</head>
<body>
<h1>{title}</h1>
<div class="meta"><strong>Location:</strong> {location}</div>
<div class="constraints"><strong>Key constraints:</strong> {constraints}</div>
<p>{summary}</p>

<div class="map-container">
  <iframe src="{map_url}" allowfullscreen loading="lazy"></iframe>
</div>

<h2>Recommended Stays</h2>
{hotels_html}

<h2>Suggested Itinerary</h2>
{itinerary_html}

<h2>Getting Around</h2>
<p>{transport}</p>

<h2>Budget Notes</h2>
<p>{budget_notes}</p>

<div class="actions">
  <a class="btn" href="javascript:window.print()">Print / Save PDF</a>
  <a class="btn" href="javascript:navigator.clipboard.writeText(location.href);alert('Link copied')">Copy share link</a>
  <a class="btn" href="/">Assemble another trip</a>
</div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    index = load_index()
    links = "".join(f'<li><a href="/pages/{item["slug"]}.html">{item["title"]}</a></li>' for item in index)
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>TripAssembler</title></head>
    <body style="font-family:system-ui;max-width:800px;margin:40px auto;padding:0 20px;">
    <h1>TripAssembler</h1>
    <p>Describe your trip constraints and I’ll assemble a practical plan.</p>
    <form id="tripForm" action="/assemble" method="post">
      <textarea name="request" rows="6" style="width:100%;font-size:16px;padding:12px;border-radius:8px;border:1px solid #ccc;" placeholder="Example: 7 nights in Iceland for 5 adults in December. Need either a 3BR apartment or 2 hotel rooms under $500/night total. Include must-see towns, scenic drives, hot springs, and short hikes."></textarea>
      <br><br>
      <button type="submit" id="submitBtn" style="padding:12px 24px;background:#004E89;color:white;border:none;border-radius:8px;font-size:16px;">Assemble my trip</button>
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

    slug_base = "-".join(request.lower().split()[:6])
    slug_base = "".join(c if c.isalnum() or c == "-" else "" for c in slug_base)
    slug = f"{slug_base}-{datetime.now().strftime('%Y%m%d%H%M')}"

    prompt = f"""You are an expert travel planner. Create a realistic, useful trip assembly for this request:

"{request}"

Guidelines:
- Prefer real or highly realistic hotel/apartment names and neighborhoods
- Give believable price ranges
- Build a proper multi-day itinerary matching the requested length
- Include specific attractions, activities, food ideas, and practical tips
- Include a "map_places" array with 4–8 key locations in itinerary order (hotels, towns, attractions), formatted as "Name, City or Region"
- Return ONLY valid JSON in this exact structure:

{{
  "title": "appealing title",
  "location": "main destination",
  "summary": "2-4 sentence overview",
  "constraints": ["constraint 1", "constraint 2", "constraint 3"],
  "hotels": [
    {{"name": "place name", "why": "why it fits", "price_range": "$XXX-YYY per night", "area": "neighborhood"}}
  ],
  "itinerary": [
    {{"day": 1, "title": "theme", "activities": ["specific thing 1", "specific thing 2"], "tips": "practical tip"}}
  ],
  "map_places": ["Place 1, Region", "Place 2, Region", "Place 3, Region"],
  "transport": "how to get around + any notes",
  "budget_notes": "realistic budget guidance"
}}"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        assembly = json.loads(response.choices[0].message.content)
        assembly["slug"] = slug
    except Exception as e:
        assembly = {
            "slug": slug,
            "title": f"Trip: {request[:70]}",
            "location": "See request",
            "summary": f"Generation failed: {str(e)}",
            "constraints": [request],
            "hotels": [{"name": "Error", "why": "AI call failed", "price_range": "—", "area": "—"}],
            "itinerary": [{"day": 1, "title": "Error", "activities": ["Try again"], "tips": ""}],
            "map_places": [],
            "transport": "—",
            "budget_notes": "—"
        }

    # Build Google Maps embed URL
places = assembly.get("map_places", [])
if MAPS_KEY and places and len(places) >= 2:
    from urllib.parse import quote
    origin = quote(places[0])
    destination = quote(places[-1])
    waypoints = "|".join(quote(p) for p in places[1:-1])
    map_url = f"https://www.google.com/maps/embed/v1/directions?key={MAPS_KEY}&origin={origin}&destination={destination}"
    if waypoints:
        map_url += f"&waypoints={waypoints}"
else:
    from urllib.parse import quote
    query = quote(assembly.get("location") or "travel")
    map_url = f"https://www.google.com/maps/embed/v1/search?key={MAPS_KEY}&q={query}" if MAPS_KEY else "about:blank"
    
        hotels_html = "".join(
            f"<p><strong>{h.get('name','')}</strong> ({h.get('area','')}) — {h.get('why','')} ({h.get('price_range','')})</p>"
            for h in assembly.get("hotels", [])
        )
        itinerary_html = "".join(
            f'<div class="day"><h3>Day {d.get("day","?")}: {d.get("title","")}</h3>'
            f'<ul>{"".join(f"<li>{a}</li>" for a in d.get("activities",[]))}</ul>'
            f'<p><em>{d.get("tips","")}</em></p></div>'
            for d in assembly.get("itinerary", [])
        )
    
        html = PAGE_TEMPLATE.format(
            title=assembly.get("title", "Trip"),
            location=assembly.get("location", ""),
            constraints=", ".join(assembly.get("constraints", [])),
            summary=assembly.get("summary", ""),
            map_url=map_url,
            hotels_html=hotels_html,
            itinerary_html=itinerary_html,
            transport=assembly.get("transport", ""),
            budget_notes=assembly.get("budget_notes", "")
        )
    
        with open(os.path.join(PAGES_DIR, f"{slug}.html"), "w") as f:
            f.write(html)
    
        index = load_index()
        index.insert(0, {"slug": slug, "title": assembly.get("title", "Trip")})
        save_index(index)
    
        return RedirectResponse(f"/pages/{slug}.html", status_code=303)

@app.get("/sitemap.xml")
async def sitemap():
    index = load_index()
    base = "https://tripassembler.onrender.com"
    urls = [f"{base}/"] + [f"{base}/pages/{item['slug']}.html" for item in index]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += f"  <url><loc>{url}</loc></url>\n"
    xml += "</urlset>"
    return HTMLResponse(content=xml, media_type="application/xml")

@app.get("/robots.txt")
async def robots():
    return HTMLResponse("User-agent: *\nAllow: /\nSitemap: https://tripassembler.onrender.com/sitemap.xml\n", media_type="text/plain")
    
app.mount("/pages", StaticFiles(directory=PAGES_DIR), name="pages")

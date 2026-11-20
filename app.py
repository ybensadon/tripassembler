from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import json, os
from datetime import datetime
from openai import OpenAI

app = FastAPI()
PAGES_DIR = "pages"
INDEX_FILE = "index.json"
os.makedirs(PAGES_DIR, exist_ok=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
<style>
  body {{ font-family: system-ui, -apple-system, sans-serif; max-width: 800px; margin: 40px auto; line-height: 1.6; padding: 0 20px; color: #1a1a1a; }}
  h1 {{ color: #004E89; margin-bottom: 0.3em; }}
  .meta {{ color: #555; font-size: 0.95em; margin-bottom: 1.5em; }}
  .constraints {{ background: #f0f4f8; padding: 16px; border-radius: 10px; margin: 1.5em 0; }}
  .day {{ background: #fff; border: 1px solid #e5e7eb; padding: 18px; margin: 16px 0; border-radius: 10px; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }}
  .actions {{ margin: 2em 0; display: flex; gap: 10px; flex-wrap: wrap; }}
  button, .btn {{ padding: 10px 16px; border-radius: 8px; border: 1px solid #ddd; background: #fff; cursor: pointer; font-size: 0.95em; text-decoration: none; color: #333; display: inline-block; }}
  button:hover, .btn:hover {{ background: #f9fafb; }}
  .primary {{ background: #004E89; color: white; border-color: #004E89; }}
  @media print {{
    .actions, .no-print {{ display: none !important; }}
    body {{ margin: 0; padding: 20px; }}
  }}
</style>
</head>
<body>
<h1>{title}</h1>
<div class="meta"><strong>Location:</strong> {location}</div>
<div class="constraints"><strong>Constraints:</strong> {constraints}</div>
<p>{summary}</p>

<h2>Recommended Stays</h2>
{hotels_html}

<h2>Suggested Itinerary</h2>
{itinerary_html}

<h2>Getting Around</h2>
<p>{transport}</p>

<h2>Budget Notes</h2>
<p>{budget_notes}</p>

<div class="actions no-print">
  <button onclick="window.print()">Print / Save as PDF</button>
  <button onclick="navigator.clipboard.writeText(window.location.href); alert('Link copied!')">Share link</button>
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
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
    <body style="font-family:system-ui;max-width:800px;margin:40px auto;padding:0 20px;">
    <h1>TripAssembler</h1>
    <p>Describe your trip constraints and I’ll assemble it.</p>
    <form id="tripForm" action="/assemble" method="post">
      <textarea name="request" rows="5" style="width:100%;font-size:16px;padding:10px;border-radius:8px;border:1px solid #ccc;" placeholder="Example: 5 days in Tokyo, family of 4, need a kitchen, under $250/night, near parks"></textarea>
      <br><br>
      <button type="submit" id="submitBtn" style="padding:12px 24px;background:#004E89;color:white;border:none;border-radius:8px;font-size:16px;cursor:pointer;">Assemble my trip</button>
      <div id="loading" style="display:none;margin-top:16px;color:#004E89;font-weight:500;">Assembling your trip… this usually takes 5–10 seconds.</div>
    </form>
    <script>
      document.getElementById('tripForm').addEventListener('submit', function() {{
        document.getElementById('submitBtn').disabled = true;
        document.getElementById('submitBtn').textContent = 'Assembling…';
        document.getElementById('loading').style.display = 'block';
      }});
    </script>
    <h2>Recent Assemblies</h2>
    <ul>{links or "<li>None yet</li>"}</ul>
    </body></html>
    """

@app.post("/assemble")
async def assemble(request: str = Form(...)):
    request = request.strip()
    if not request:
        request = "a trip"

    slug_base = "-".join(request.lower().split()[:6])
    slug_base = "".join(c if c.isalnum() or c == "-" else "" for c in slug_base)
    slug = f"{slug_base}-{datetime.now().strftime('%Y%m%d%H%M')}"

    prompt = f"""You are an expert travel planner. Create a practical, realistic trip assembly based on this request:

"{request}"

Rules:
- Use real or realistic hotel/apartment names and neighborhoods when possible
- Give approximate price ranges that make sense for the destination and group size
- Create a multi-day itinerary (match the number of days/nights in the request if given)
- Include specific attractions, food ideas, and practical tips
- Keep everything concise but useful
- Return ONLY valid JSON with this exact structure:

{{
  "title": "clear, appealing title",
  "location": "main city or region",
  "summary": "2-4 sentence overview of the trip",
  "constraints": ["key constraint 1", "key constraint 2", "key constraint 3"],
  "hotels": [
    {{
      "name": "realistic place name",
      "why": "why it fits the request",
      "price_range": "$XXX-YYY per night",
      "area": "neighborhood or area"
    }}
  ],
  "itinerary": [
    {{
      "day": 1,
      "title": "day theme",
      "activities": ["specific activity 1", "specific activity 2", "specific activity 3"],
      "tips": "one practical tip"
    }}
  ],
  "transport": "how to get around (with any important notes)",
  "budget_notes": "realistic budget guidance based on the request"
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
            "title": f"Trip assembly: {request[:80]}",
            "location": "Based on your request",
            "summary": f"Could not generate full assembly. Error: {str(e)}",
            "constraints": [request],
            "hotels": [{"name": "Generation failed", "why": "See summary", "price_range": "—", "area": "—"}],
            "itinerary": [{"day": 1, "title": "Try again", "activities": ["The AI call failed"], "tips": "Check your API key and logs"}],
            "transport": "—",
            "budget_notes": "—"
        }

    hotels_html = "".join(
        f"<p><strong>{h.get('name','')}</strong> ({h.get('area','')}) — {h.get('why','')} ({h.get('price_range','')})</p>"
        for h in assembly.get("hotels", [])
    )
    itinerary_html = "".join(
        f'<div class="day"><h3>Day {d.get("day", "?")}: {d.get("title", "")}</h3>'
        f'<ul>{"".join(f"<li>{a}</li>" for a in d.get("activities", []))}</ul>'
        f'<p><em>{d.get("tips", "")}</em></p></div>'
        for d in assembly.get("itinerary", [])
    )

    html = PAGE_TEMPLATE.format(
        title=assembly.get("title", "Trip"),
        location=assembly.get("location", ""),
        constraints=", ".join(assembly.get("constraints", [])),
        summary=assembly.get("summary", ""),
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

app.mount("/pages", StaticFiles(directory=PAGES_DIR), name="pages")

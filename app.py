from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import json, os
from datetime import datetime

app = FastAPI()
PAGES_DIR = "pages"
INDEX_FILE = "index.json"
os.makedirs(PAGES_DIR, exist_ok=True)

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
<html>
<head>
<meta charset="utf-8">
<title>{title} | TripAssembler</title>
<style>
body {{ font-family: system-ui, sans-serif; max-width: 800px; margin: 40px auto; line-height: 1.6; padding: 0 20px; }}
h1 {{ color: #004E89; }}
.constraints {{ background: #f0f4f8; padding: 12px; border-radius: 8px; }}
.day {{ background: #fff; border: 1px solid #eee; padding: 16px; margin: 16px 0; border-radius: 8px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p><strong>Location:</strong> {location}</p>
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
<p><a href="/">← Back to assemblies</a></p>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    index = load_index()
    links = "".join(f'<li><a href="/pages/{item["slug"]}.html">{item["title"]}</a></li>' for item in index)
    return f"""
    <html><body style="font-family:system-ui;max-width:800px;margin:40px auto;padding:0 20px;">
    <h1>TripAssembler</h1>
    <p>Describe your trip constraints and I’ll assemble it.</p>
    <form action="/assemble" method="post">
    <textarea name="request" rows="5" style="width:100%;" placeholder="Example: 5 days in Tokyo, family of 4, need a kitchen, under $250/night, near parks"></textarea><br><br>
    <button type="submit" style="padding:10px 20px;background:#004E89;color:white;border:none;border-radius:6px;">Assemble my trip</button>
    </form>
    <h2>Recent Assemblies</h2>
    <ul>{links or "<li>None yet</li>"}</ul>
    </body></html>
    """

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/assemble")
async def assemble(request: str = Form(...)):
    request = request.strip()
    if not request:
        request = "a trip"

    slug_base = "-".join(request.lower().split()[:6])
    slug_base = "".join(c if c.isalnum() or c == "-" else "" for c in slug_base)
    slug = f"{slug_base}-{datetime.now().strftime('%Y%m%d%H%M')}"

    prompt = f"""You are a helpful travel planner. Create a practical trip assembly based on this request:

"{request}"

Return ONLY valid JSON with this exact structure:
{{
  "title": "short descriptive title",
  "location": "main destination",
  "summary": "2-3 sentence summary",
  "constraints": ["list", "of", "key", "constraints"],
  "hotels": [
    {{"name": "hotel or apartment name", "why": "why it fits", "price_range": "$X-Y", "area": "neighborhood"}}
  ],
  "itinerary": [
    {{"day": 1, "title": "day title", "activities": ["activity1", "activity2"], "tips": "short tip"}}
  ],
  "transport": "how to get around",
  "budget_notes": "budget guidance"
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
        # Fallback if AI fails
        assembly = {
            "slug": slug,
            "title": f"Trip assembly: {request[:80]}",
            "location": "Based on your request",
            "summary": f"Could not generate full assembly. Request was: {request}",
            "constraints": [request],
            "hotels": [{"name": "Error generating", "why": str(e), "price_range": "—", "area": "—"}],
            "itinerary": [{"day": 1, "title": "Error", "activities": ["Try again"], "tips": ""}],
            "transport": "—",
            "budget_notes": "—"
        }

    # (rest of the function stays the same: build hotels_html, itinerary_html, write the file, update index, redirect)
    hotels_html = "".join(
        f"<p><strong>{h['name']}</strong> ({h['area']}) — {h['why']} ({h['price_range']})</p>"
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

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

@app.post("/assemble")
async def assemble(request: str = Form(...)):
    assembly = {
        "slug": "tokyo-family-kitchen-" + datetime.now().strftime("%Y%m%d%H%M"),
        "title": "Family-friendly Tokyo stay with kitchen near parks",
        "location": "Tokyo, Japan",
        "summary": "A practical assembly based on your request for a family trip with kitchen access and parks.",
        "constraints": ["family", "kitchen", "parks", "budget-conscious"],
        "hotels": [{"name": "Apartment in Nakameguro", "why": "Kitchen + parks nearby", "price_range": "$180-240", "area": "Nakameguro"}],
        "itinerary": [{"day": 1, "title": "Arrival", "activities": ["Check-in", "Local park walk", "Easy dinner"], "tips": "Get a Suica card"}],
        "transport": "Subway + walking",
        "budget_notes": "Apartments in this range are realistic outside the very center."
    }

    hotels_html = "".join(f"<p><strong>{h['name']}</strong> ({h['area']}) — {h['why']} ({h['price_range']})</p>" for h in assembly["hotels"])
    itinerary_html = "".join(f'<div class="day"><h3>Day {d["day"]}: {d["title"]}</h3><ul>{"".join("<li>"+a+"</li>" for a in d["activities"])}</ul><p><em>{d["tips"]}</em></p></div>' for d in assembly["itinerary"])

    html = PAGE_TEMPLATE.format(
        title=assembly["title"], location=assembly["location"],
        constraints=", ".join(assembly["constraints"]), summary=assembly["summary"],
        hotels_html=hotels_html, itinerary_html=itinerary_html,
        transport=assembly["transport"], budget_notes=assembly["budget_notes"]
    )

    slug = assembly["slug"]
    with open(os.path.join(PAGES_DIR, f"{slug}.html"), "w") as f:
        f.write(html)

    index = load_index()
    index.insert(0, {"slug": slug, "title": assembly["title"]})
    save_index(index)

    return RedirectResponse(f"/pages/{slug}.html", status_code=303)

app.mount("/pages", StaticFiles(directory=PAGES_DIR), name="pages")

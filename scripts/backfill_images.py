#!/usr/bin/env python3
"""Add Wikipedia images and related trips to existing TripAssembler pages.

Safe to re-run. A page that already has the enhanced marker, a related-trips
section, and a hero image is left unchanged. ``--force`` retries pages that
were enhanced but never received a hero image (for example Wikipedia was
down on the first pass).

From the app root on your machine, or in the Render shell:

    python scripts/backfill_images.py

That updates legacy pages in ``legacy_pages/`` and generated HTML in
``PAGES_DIR`` (on Render: ``/opt/render/project/src/pages``).
"""
import argparse
import asyncio
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import app


def targets(legacy, pages):
    found = []
    if legacy and os.path.isdir(app.LEGACY_DIR):
        for slug in app.legacy_slugs():
            path = os.path.join(app.LEGACY_DIR, slug + ".html")
            if os.path.isfile(path):
                found.append((path, slug))
    if pages and os.path.isdir(app.PAGES_DIR):
        for name in sorted(os.listdir(app.PAGES_DIR)):
            if not name.endswith(".html"):
                continue
            slug = name[:-5]
            if not app._SLUG_RE.fullmatch(slug):
                continue
            path = os.path.join(app.PAGES_DIR, name)
            if os.path.isfile(path) and app._inside(path, app.PAGES_DIR):
                found.append((path, slug))
    return found


def should_skip(document, force):
    done = (
        app.ENHANCED_MARKER in document
        and 'id="related-trips"' in document
        and 'class="brand-tag"' in document
    )
    if not done:
        return False
    if force and 'class="hero-photo"' not in document:
        return False
    return True


async def warm(queries):
    pending = []
    seen = set()
    for query in queries:
        text = app.opt_text(query, 160)
        if not text:
            continue
        key = text.casefold()
        if key in seen:
            continue
        seen.add(key)
        cache_key = app.image_cache_key("", text)
        image, hit = app.cache_get(cache_key)
        if hit and image:
            continue
        pending.append((key, "", text))
    for start in range(0, len(pending), 4):
        chunk = pending[start:start + 4]
        await app.resolve_images(chunk, timeout=20.0)
        print(f"looked up {min(start + len(chunk), len(pending))}/{len(pending)} destinations", flush=True)


async def assign_distinct(infos):
    """One shared photo pool per city, then a different photo for each slug."""
    groups = {}
    for info in infos:
        groups.setdefault(app.location_key(info) or info.get("slug") or "trip", []).append(info)
    store = app.load_assignments()
    for loc in list(groups):
        store.pop(loc, None)
    app.save_assignments()
    for loc, group in groups.items():
        group.sort(key=lambda item: item.get("slug") or "")
        extra = []
        for info in group:
            extra.extend(app.pool_queries(info))
        pool = await app.build_location_pool(
            group[0], extra_queries=extra, timeout=20.0, min_count=len(group),
        )
        bucket = {"pool": pool, "assigned": {}}
        taken = set()
        for info in group:
            image = app.choose_distinct(info.get("slug") or "", pool, taken)
            if not image:
                continue
            taken.add(image["file"])
            bucket["assigned"][info["slug"]] = image
            app.remember_image(image, info["slug"])
        store[loc] = bucket
        app.save_assignments()
        print(f"pool {loc}: {len(pool)} photos for {len(group)} pages", flush=True)
        await asyncio.sleep(0.35)


async def enhance_distinct(pairs):
    prepared = []
    infos = []
    for path, slug in pairs:
        original = app.read_text(path)
        document = app.strip_enhanced_media(original)
        info = app.context_for(slug, document)
        prepared.append((path, slug, original, document, info))
        infos.append(info)
    await assign_distinct(infos)
    wrote = 0
    failed = 0
    for path, slug, original, document, info in prepared:
        try:
            updated = await app.enhance_document(slug, document)
        except Exception as exc:
            failed += 1
            print(f"fail {slug}: {exc}", flush=True)
            continue
        if 'class="hero-photo"' not in updated:
            failed += 1
            print(f"no photo {slug}", flush=True)
        if updated != original:
            app.write_text_atomic(path, updated)
            wrote += 1
            print(f"updated {slug}", flush=True)
        else:
            print(f"unchanged {slug}", flush=True)
    return 0, wrote, failed


def hero_duplicate_report(directory):
    from collections import Counter, defaultdict
    groups = defaultdict(list)
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".html"):
            continue
        slug = name[:-5]
        text = app.read_text(os.path.join(directory, name))
        match = re.search(r'<figure class="hero-photo"><img src="([^"]+)"', text)
        src = ""
        if match:
            import html as html_mod
            src = html_mod.unescape(match.group(1))
        info = app.describe_trip(slug, app.page_title_from_html(text))
        loc = app.location_key(info) or slug
        groups[loc].append((slug, src, app.photo_file_key(src)))
    duplicate_locations = {}
    shared = 0
    for loc, rows in groups.items():
        if len(rows) < 2:
            continue
        shared += 1
        counts = Counter(key for _, _, key in rows if key)
        dups = {key: count for key, count in counts.items() if count > 1}
        if dups:
            duplicate_locations[loc] = {
                "pages": len(rows),
                "unique": len(counts),
                "duplicates": dups,
            }
    return {
        "pages": sum(len(rows) for rows in groups.values()),
        "locations": len(groups),
        "shared_locations": shared,
        "duplicate_locations": duplicate_locations,
    }


async def enhance_all(pairs, force):
    work = []
    skipped = 0
    for path, slug in pairs:
        document = app.read_text(path)
        if should_skip(document, force):
            skipped += 1
            continue
        if force and 'class="hero-photo"' not in document:
            document = document.replace(app.ENHANCED_MARKER, "")
        info = app.context_for(slug, document)
        work.append((path, slug, document, info))
    await warm(item[3].get("query") for item in work)
    wrote = 0
    failed = 0
    for path, slug, document, info in work:
        try:
            updated = await app.enhance_document(slug, document)
        except Exception as exc:
            failed += 1
            print(f"fail {slug}: {exc}", flush=True)
            continue
        if updated != app.read_text(path):
            app.write_text_atomic(path, updated)
            wrote += 1
            hero = "hero" if 'class="hero-photo"' in updated else "no-hero"
            print(f"updated {slug} ({hero})", flush=True)
        else:
            print(f"unchanged {slug}", flush=True)
    return skipped, wrote, failed


def main():
    parser = argparse.ArgumentParser(description="Pre-enhance trip pages with images and related trips.")
    parser.add_argument("--legacy-dir", default="", help="Override the legacy_pages directory.")
    parser.add_argument("--pages-dir", default="", help="Override PAGES_DIR for generated HTML.")
    parser.add_argument("--legacy-only", action="store_true", help="Only update legacy_pages.")
    parser.add_argument("--pages-only", action="store_true", help="Only update generated pages.")
    parser.add_argument("--force", action="store_true", help="Retry enhanced pages that still have no hero image.")
    parser.add_argument(
        "--distinct",
        action="store_true",
        help="Rebuild photos so pages for the same city do not share a hero.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Stop after this many pages (0 means all).")
    args = parser.parse_args()
    if args.legacy_dir:
        app.LEGACY_DIR = args.legacy_dir
    if args.pages_dir:
        app.PAGES_DIR = args.pages_dir
        os.makedirs(app.PAGES_DIR, exist_ok=True)
    pairs = targets(legacy=not args.pages_only, pages=not args.legacy_only)
    if args.limit:
        pairs = pairs[:args.limit]
    if not pairs:
        print("No pages to enhance.")
        return 0
    report = {"duplicate_locations": {}}
    if args.distinct:
        skipped, wrote, failed = asyncio.run(enhance_distinct(pairs))
    else:
        skipped, wrote, failed = asyncio.run(enhance_all(pairs, args.force))
    print(f"done: wrote {wrote}, skipped {skipped}, failed {failed}, seen {len(pairs)}")
    if args.legacy_only or not args.pages_only:
        report = hero_duplicate_report(app.LEGACY_DIR)
        print(
            "legacy heroes: {pages} pages, {locations} locations, "
            "{shared_locations} locations with more than one page, "
            "{dups} locations with a repeated hero".format(
                dups=len(report["duplicate_locations"]),
                **report,
            )
        )
        for loc, detail in sorted(report["duplicate_locations"].items()):
            print(f"  duplicate {loc}: {detail}")
    return 1 if failed or (args.distinct and report.get("duplicate_locations")) else 0


if __name__ == "__main__":
    raise SystemExit(main())

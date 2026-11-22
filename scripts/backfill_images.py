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
    skipped, wrote, failed = asyncio.run(enhance_all(pairs, args.force))
    print(f"done: wrote {wrote}, skipped {skipped}, failed {failed}, seen {len(pairs)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

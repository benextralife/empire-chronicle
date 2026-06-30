#!/usr/bin/env python3
"""Correct link scanner for empire-chronicle GitHub Pages.
Fixes the double-path bug by resolving absolute hrefs against the site root."""
import json, re, sys, urllib.request, urllib.parse

SITE = "https://benextralife.github.io/empire-chronicle"
SEEN = set()
BROKEN = []

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status, r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None, str(e)

def normalize(href, base):
    """Resolve href against base like a browser would."""
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        return "https://benextralife.github.io" + href
    return urllib.parse.urljoin(base, href)

# Start from root
status, html = fetch(SITE)
if status != 200:
    print("FAIL: root", SITE, status)
    sys.exit(1)

SEEN.add(SITE)

# Start with sitemap if present
status, sitemap = fetch(SITE + "/sitemap.xml")
if status == 200:
    for m in re.finditer(r"<loc>(.*?)</loc>", sitemap):
        url = m.group(1)
        if url not in SEEN:
            SEEN.add(url)
            # We'll fetch these below

# Extract all internal hrefs from collected pages
hrefs = set()
for url in list(SEEN):
    status, html = fetch(url)
    if status != 200:
        continue
    for m in re.finditer(r'href=["\'](.*?)["\']', html):
        href = m.group(1)
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("javascript:"):
            continue
        resolved = normalize(href, url)
        if "benextralife.github.io/empire-chronicle" in resolved:
            if resolved not in SEEN:
                hrefs.add(resolved)

# Fetch discovered pages
for url in sorted(hrefs):
    if url in SEEN:
        continue
    status, html = fetch(url)
    SEEN.add(url)
    if status == 404:
        BROKEN.append(url)

if BROKEN:
    print("Broken links found:")
    for u in BROKEN:
        print(" ", u)
else:
    print("All", len(SEEN), "pages OK.")

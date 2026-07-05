#!/usr/bin/env python3
"""Monitor Weng Hsiao-Ling news via web search."""
import os
import sys
import re
from datetime import datetime

# Add hermes_tools path
sys.path.insert(0, os.path.expanduser('~/AppData/Local/hermes'))

try:
    from hermes_tools import web_search
except ImportError:
    # Fallback: just mark that we ran
    results_file = os.path.join(os.path.dirname(__file__), 'last_run.txt')
    with open(results_file, 'w') as f:
        f.write(f"[{datetime.now()}] hermes_tools not available\n")
    print("hermes_tools not available, skipping")
    sys.exit(0)

QUERIES = [
    "翁曉玲 最新動態 2026",
    "翁曉玲 新聞 爭議",
    "翁曉玲 中國 廈門 台商",
    "翁曉玲 陳春生 財產",
    "翁曉玲 政府標案 關係企業",
    "翁曉玲 親屬 公司 商業",
]

results_file = os.path.join(os.path.dirname(__file__), 'search_results.txt')
existing_urls = set()
if os.path.exists(results_file):
    with open(results_file, 'r', encoding='utf-8') as f:
        existing_urls = set(re.findall(r'URL: (\S+)', f.read()))

new_items = []
for query in QUERIES:
    try:
        res = web_search(query=query, limit=5)
        items = res.get('data', {}).get('web', [])
        for it in items:
            url = it.get('url', '')
            title = it.get('title', '')
            if url and url not in existing_urls:
                new_items.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {title}\nURL: {url}\n")
                existing_urls.add(url)
    except Exception as e:
        new_items.append(f"[ERROR] {query}: {e}\n")

with open(results_file, 'a', encoding='utf-8') as f:
    if new_items:
        f.write('\n'.join(new_items) + '\n')
        print(f"Found {len(new_items)} new items")
    else:
        print("No new items")

# Print last 15 lines
with open(results_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("\n--- Recent ---")
    print('\n'.join(lines[-15:]))

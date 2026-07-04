"""Starweaver's Dream - Royal Road Batch Upload
Proven pattern from rr_upload.py (AI Garden's Dream).
Needs existing fiction_id.
"""
import time, re, sys, json, random
from playwright.sync_api import sync_playwright

FICTION_ID = "TBD"  # Replace after fiction creation

with open("Starweaver_Dream_RR.txt", encoding="utf-8") as f:
    raw = f.read()

sections = re.split(r'(?=Chapter\s+\d+)', raw)
chapters = []
for sec in sections:
    sec = sec.strip()
    if not sec:
        continue
    lines = sec.split('\n', 1)
    title = lines[0].strip()
    content = lines[1].strip() if len(lines) > 1 else ""
    chapters.append((title, content))

print(f"Loaded {len(chapters)} chapters")

def human_pause(base=5, variance=15):
    time.sleep(base + random.uniform(0, variance))

with sync_playwright() as p:
    ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = [pg for pg in ctx.contexts[0].pages if "royalroad" in pg.url][0]
    
    for i, (title, content) in enumerate(chapters):
        print(f"\n[{i+1}/{len(chapters)}] {title}")
        url = f"https://www.royalroad.com/author-dashboard/chapters/new/{FICTION_ID}"
        page.goto(url, wait_until="domcontentloaded")
        human_pause()
        
        # Fill title
        page.evaluate(f"""() => {{
            const el = document.querySelector('#Title');
            if (el) {{ el.value = {json.dumps(title)}; el.dispatchEvent(new Event('input', {{bubbles: true}})); }}
        }}""")
        human_pause(2, 4)
        
        # Fill content via textarea + execCommand fallback
        ta_len = page.evaluate(f"""() => {{
            const ta = document.querySelector('#contentEditor');
            if (ta) {{
                ta.value = {json.dumps(content)};
                ta.dispatchEvent(new Event('input', {{bubbles: true}}));
                return ta.value.length;
            }}
            return 0;
        }}""")
        human_pause(2, 5)
        
        if ta_len < 100:
            exec_ok = page.evaluate(f"""() => document.execCommand('insertText', false, {json.dumps(content)})""")
            print(f"  execCommand fallback: {exec_ok}")
        
        # Submit
        page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const btn = btns.find(b => /Save Draft|Publish/.test(b.innerText));
            if (btn) btn.click();
        }""")
        human_pause(8, 12)
        print(f"  -> Submitted ({len(content)} chars)")
    
    ctx.close()

print("\n=== ALL CHAPTERS PROCESSED ===")

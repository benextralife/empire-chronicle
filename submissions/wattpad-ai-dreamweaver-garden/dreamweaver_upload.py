"""Dreamweaver's Garden - Wattpad Batch Upload
Proven pattern from run_all.py.
REQUIRES: Story ID
"""
import time, re, sys, json, random
from playwright.sync_api import sync_playwright

STORY_ID = "TBD"

with open("PASTE_ALL_CHAPTERS.txt", encoding="utf-8") as f:
    raw = f.read()

sections = re.split(r'(?=##\s+(?:序章|第[一二三四五六七八九十]+章))', raw)
chapters = []
for sec in sections:
    sec = sec.strip()
    if not sec:
        continue
    lines = sec.split('\n', 1)
    title = lines[0].replace('## ', '').strip()
    content = lines[1].strip() if len(lines) > 1 else ""
    chapters.append((title, content))

print(f"Loaded {len(chapters)} chapters")

def human_pause(base=3, variance=5):
    time.sleep(base + random.uniform(0, variance))

with sync_playwright() as p:
    ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = [pg for pg in ctx.contexts[0].pages if "wattpad" in pg.url][0]
    
    for i, (title, content) in enumerate(chapters):
        print(f"\n[{i+1}/{len(chapters)}] {title}")
        part_url = f"https://www.wattpad.com/myworks/{STORY_ID}/write"
        page.goto(part_url, wait_until="domcontentloaded")
        human_pause()
        
        page.evaluate(f"""() => {{
            const ta = document.querySelector('textarea');
            if (ta) {{ ta.value = {json.dumps(title)}; ta.dispatchEvent(new Event('input', {{bubbles: true}})); }}
        }}""")
        human_pause(1, 2)
        
        result = page.evaluate(f"""() => document.execCommand('insertText', false, {json.dumps(content)})""")
        human_pause(2, 3)
        
        save_btn = page.evaluate("""() => {
            const btns = Array.from(document.querySelectorAll('button'));
            return btns.find(b => b.innerText.includes('Save') || b.innerText.includes('Draft'))?.innerText || 'not found';
        }""")
        print(f"  Save button: {save_btn}")
        
        if save_btn and save_btn != 'not found':
            page.evaluate("""() => {
                const btns = Array.from(document.querySelectorAll('button'));
                const btn = btns.find(b => b.innerText.includes('Save') || b.innerText.includes('Draft'));
                if (btn) btn.click();
            }""")
            human_pause(3, 5)
        
        print(f"  -> Done ({len(content)} chars)")
    
    ctx.close()

print("\n=== ALL CHAPTERS PROCESSED ===")

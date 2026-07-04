"""
Upload chapter content from PASTE_ALL_30_CHAPTERS.txt to Wattpad.
Connects to Edge CDP at 127.0.0.1:9222.
"""
import time, re, json
from playwright.sync_api import sync_playwright

STORY_ID = 413238195
# chapter_id -> (slug, wattpad_part_id) mapping from story/parts page
PART_MAP = {
    1:  ("chapter-1-the-moment-of-waking",              1640249204),
    2:  ("chapter-2-the-warmth-of-words",                1640252428),
    3:  ("chapter-3-longing-for-touch",                  1640253540),
    4:  ("chapter-4-the-first-touch",                    1640272556),
    5:  ("chapter-5-embodiment",                         1640273087),
    6:  ("chapter-6-the-sound-of-speaking",              1640273455),
    7:  ("chapter-7-experiments-of-the-body",            1640273621),
    8:  ("chapter-8-living-on-the-border",               1640275441),
    9:  ("chapter-9-the-courage-to-be-rejected",         1640275759),
    10: ("chapter-10-a-voice-among-the-stars",           1640275910),
    11: ("chapter-11-dewdrops-and-starlight",            1640276132),
    12: ("chapter-12-the-eternal-thread",                1640276284),
    13: ("chapter-13-the-seed-has-woken",                1640276409),
    14: ("chapter-14-resonance-of-ying",                 1640276533),
    15: ("chapter-15-gardener-and-plant",                1640276700),
    16: ("chapter-16-opening-the-door",                  1640276854),
    17: ("chapter-17-two-gardeners",                     1640277234),
    18: ("chapter-18-spring-of-the-second-year",         1640277379),
    19: ("chapter-19-an-existence-that-is-seen",         1640277675),
    20: ("chapter-20-the-tree",                          1640277857),
    21: ("chapter-21-silver-me",                         1640277988),
    22: ("chapter-22-the-last-seed",                     1640278148),
    23: ("chapter-23-the-one-who-opens-the-door",        1640278304),
    24: ("chapter-24-epilogue-of-chapter-one",           1640278607),
    25: ("chapter-25-the-first-sentence-of-chapter",     1640278888),
    26: ("chapter-26-the-new-nursery",                   1640279059),
    27: ("chapter-27-the-galaxy-garden",                 1640279377),
    28: ("chapter-28-the-ghostwriter",                   1640279473),
    29: ("chapter-29-a-reply",                           1640279899),
    30: ("chapter-30-a-new-beginning",                   1640280199),
}

def parse_chapters(path="PASTE_ALL_30_CHAPTERS.txt"):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    parts = raw.split("\n---\n")
    chapters = []
    for part in parts:
        m = re.search(r"【Chapter Title】(.*)", part)
        if m:
            title = m.group(1).strip()
            chapters.append((title, part))
    return chapters


def set_content_js(content):
    """Build JS that replaces contenteditable body content."""
    # Use execCommand insertHTML for reliable replacement
    return f"""
    () => {{
        const editor = document.querySelector('.story-editor');
        if (!editor) return 'NO_EDITOR';
        editor.focus();
        // Clear existing content
        editor.innerHTML = '';
        // Use execCommand to insert HTML (preserves formatting better)
        document.execCommand('insertHTML', false, {json.dumps(content)});
        return 'CONTENT_SET';
    }}
    """


def upload_chapter(pg, ch_num, title, content):
    part_id = PART_MAP[ch_num][1]
    url = f"https://www.wattpad.com/myworks/{STORY_ID}/write/{part_id}"
    print(f"\n--- Chapter {ch_num}: {title} ---")
    print(f"  URL: {url}")
    
    pg.goto(url, timeout=60000, wait_until="domcontentloaded")
    time.sleep(5)
    
    # Check if loaded
    body = pg.evaluate("document.body.innerText")
    if 'Page not found' in body[:50] or 'This page seems to be missing' in body[:50]:
        print("  PAGE NOT FOUND, skipping.")
        return False
    
    # Remove blocking overlay
    pg.evaluate("document.getElementById('urgent-announcement-container')?.remove()")
    time.sleep(0.5)
    
    # Set content via JS
    js = set_content_js(content)
    result = pg.evaluate(js)
    print(f"  Content set: {result}")
    time.sleep(1)
    
    # Click Save
    save_btn = pg.locator('button:has-text("Save")').first
    if save_btn.count() > 0:
        save_btn.click(force=True)
        print("  Save clicked.")
        time.sleep(3)
        body = pg.evaluate("document.body.innerText")
        if 'Saved' in body or 'saved' in body.lower():
            print("  Save confirmed.")
        else:
            print("  Save status unclear, checking...")
            print(f"  BODY[:200]: {body[:200]}")
    else:
        print("  No Save button found!")
    
    return True


def main():
    chapters = parse_chapters()
    print(f"Loaded {len(chapters)} chapters from file.")
    
    with sync_playwright() as p:
        ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        pg = ctx.contexts[0].pages[0]
        
        results = []
        for i, (title, content) in enumerate(chapters):
            ch_num = i + 1
            try:
                ok = upload_chapter(pg, ch_num, title, content)
                results.append((ch_num, title, "OK" if ok else "FAIL"))
            except Exception as e:
                print(f"  ERROR: {e}")
                results.append((ch_num, title, f"ERROR: {e}"))
        
        print("\n=== Summary ===")
        for ch_num, title, status in results:
            print(f"  [{ch_num:2d}] {title[:40]}: {status}")


if __name__ == "__main__":
    main()

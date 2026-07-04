"""
Human-like batch uploader for AI Garden's Dream (Wattpad).
Uses document.execCommand('insertText') for reliable content insertion.
"""
import time, re, json, random
from playwright.sync_api import sync_playwright

STORY_ID = 413256600
CHAPTERS_FILE = "PASTE_ALL_24_CHAPTERS_EN.txt"

with open("part_ids.json") as f:
    PART_IDS = json.load(f)


def parse_chapters():
    with open(CHAPTERS_FILE, encoding="utf-8") as f:
        raw = f.read()
    parts = re.split(r"\n(?=Chapter \d+: )", raw)
    chapters = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        title = part.split("\n")[0].strip()
        chapters.append((title, part))
    return chapters


def human_pause(label=""):
    wait = round(random.choice([
        random.uniform(3, 7),
        random.uniform(6, 14),
        random.uniform(12, 28),
    ]), 1)
    if label:
        print(f"  {label} ({wait}s)")
    time.sleep(wait)


def upload_chapter(page, ch_num, title, content, part_id):
    url = f"https://www.wattpad.com/myworks/{STORY_ID}/write/{part_id}"
    print(f"\n[{ch_num}/24] {title[:50]}")
    print(f"  Part ID: {part_id}")

    # Navigate
    page.goto(url, timeout=60000, wait_until="domcontentloaded")
    human_pause("Page loaded")

    # Remove overlay
    page.evaluate('document.getElementById("urgent-announcement-container")?.remove()')
    time.sleep(random.uniform(0.5, 1.5))

    # Set title via contenteditable
    page.evaluate("""(t) => {
        const el = document.querySelector('#story-title');
        if (el) { el.textContent = t; el.dispatchEvent(new Event('input', {bubbles:true})); }
    }""", title)
    human_pause("Title set")

    # Verify title
    actual = page.evaluate("document.querySelector('#story-title')?.innerText || ''")
    if title.lower() not in actual.lower():
        print(f"  ! Title retry")
        time.sleep(2)
        page.evaluate("""(t) => {
            const el = document.querySelector('#story-title');
            el.textContent = t;
            el.dispatchEvent(new Event('input', {bubbles:true}));
        }""", title)
        time.sleep(2)

    # Set content using execCommand ('this is the key that works')
    page.evaluate("""(txt) => {
        const editor = document.querySelector('.story-editor');
        if (!editor) return 'NO_EDITOR';
        editor.focus();
        const range = document.createRange();
        range.selectNodeContents(editor);
        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        const result = document.execCommand('insertText', false, txt);
        return 'insertText: ' + result + ', len=' + editor.textContent.length;
    }""", content)
    human_pause("Content pasted")

    # Verify word count
    body = page.evaluate("document.body.innerText")
    wc = re.search(r"(\d+)\s+Words", body)
    words = wc.group(1) if wc else "?"
    print(f"  Words: {words}")

    # Maybe glance at content
    if random.random() < 0.4:
        page.mouse.move(
            random.randint(300, 700),
            random.randint(300, 800)
        )
        page.evaluate("window.scrollBy(0, 300)")
        time.sleep(random.uniform(2, 5))
        page.evaluate("window.scrollTo(0, 0)")

    # Save
    human_pause("Ready to save")
    save_btn = page.locator('button:has-text("Save")').first
    if save_btn.count() > 0:
        if random.random() < 0.5:
            page.evaluate("window.scrollTo(0, 0)")
            time.sleep(random.uniform(0.3, 0.8))
        save_btn.click(force=True)
        print("  Save clicked")

        wait = round(random.uniform(5, 12), 1)
        print(f"  Waiting {wait}s for confirmation...")
        time.sleep(wait)

        body2 = page.evaluate("document.body.innerText")
        if "Saved" in body2:
            print("  ✓ Saved")
        else:
            print("  ? Save status unknown")
    else:
        print("  ✗ Save button missing")

    return True


def main():
    chapters = parse_chapters()
    print(f"Loaded {len(chapters)} chapters")
    print(f"Found {len(PART_IDS)} part IDs")

    if len(chapters) != len(PART_IDS):
        print(f"WARNING: chapters ({len(chapters)}) != parts ({len(PART_IDS)})")

    with sync_playwright() as p:
        ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        wattpad_pages = [pg for pg in ctx.contexts[0].pages if "wattpad" in pg.url]
        if not wattpad_pages:
            print("ERROR: No Wattpad page found. Open the story page first.")
            exit(1)
        page = wattpad_pages[-1]
        print(f"Using page: {page.url}")

        results = []
        for i, ((title, content), part_id) in enumerate(zip(chapters, PART_IDS)):
            ch_num = i + 1
            try:
                upload_chapter(page, ch_num, title, content, part_id)
                results.append((ch_num, title[:40], "OK"))
            except Exception as e:
                print(f"  ERROR ch{ch_num}: {e}")
                results.append((ch_num, title[:40], f"ERROR: {e}"))
                time.sleep(random.uniform(15, 40))

        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        for ch_num, title, status in results:
            marker = "✓" if status == "OK" else "✗"
            print(f"  {marker} [{ch_num:2d}] {title}: {status}")


if __name__ == "__main__":
    main()

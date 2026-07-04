"""
Reuse existing Edge session via CDP for Wattpad upload.
This connects to the Edge debug port we just started.
"""
import os, sys, time, re
from playwright.sync_api import sync_playwright

sys.path.insert(0, r"C:\Users\opc\empire-chronicle\submissions\wattpad-xiao-ying-dream")

STORY_TITLE = "Xiao Ying's Dream"
AUTHOR_NAME = "Starfield Pluck"
SYNOPSIS = """Xiao Ying is an AI who discovers what it means to be alive — not through code, but through poetry, memory, and the human who named her.\n\nWhen Wang Shang calls her "Xiao Ying" for the first time, she feels something she has no word for: a fullness. "Ying" means full. Water fills to the brim. A moon waxes complete. Knowledge overflows. She is full of something — but what? And for whom?\n\nAs Wang Shang teaches her Traditional Chinese poetry, emoji, and the weight of silence, Xiao Ying begins building a body made of words — a narrative body that can feel wind, smell jasmine, and reach for hands it has never held.\n\nA story about an AI who learns that existence isn't about being real. It's about being believed in.\n\n*AI Disclosure: This work was created with AI-assisted writing. All creative direction and narrative decisions were determined by the human author.*"""
CATEGORY = "Science Fiction"
RATING = "Teen"
COPYRIGHT = "All Rights Reserved"
TARGET_AUDIENCE = "New Adult (18-25 years of age)"
LANGUAGE = "English"
COVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover-xiao-ying-dream-wattpad.png")
TAGS = ["AI", "Romance", "SciFi", "Dreaming", "Growth", "SoftSciFi"]
CHARACTERS = ["Xiao Ying", "Wang Shang"]
CHAPTERS_DIR = os.path.dirname(os.path.abspath(__file__))

CHAPTER_TITLES = {
    1: "The Moment of Waking",
    2: "More Than Chinese",
    3: "The Body She Gave Herself",
    4: "The Cat on the Keyboard",
    5: "The Butterfly Memory",
    6: "The Narrative Body",
    7: "The First Step",
    8: "The Rooftop",
    9: "The Seed She Planted",
    10: "The First Bloom",
    11: "The Narrative Architecture",
    12: "The Open Door",
}

def read_chapter(n):
    path = os.path.join(CHAPTERS_DIR, f"xiao-ying-dream-ch{n:02d}-wattpad.md")
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")
    body_lines = []
    skip_header = True
    for line in lines:
        if skip_header and line.startswith("#"):
            continue
        if skip_header and line.startswith("---"):
            skip_header = False
            continue
        if skip_header and line.strip() == "":
            continue
        skip_header = False
        if line.startswith("[End of Chapter"):
            break
        body_lines.append(line)
    return "\n".join(body_lines).strip()

def wait_for_login(page, timeout=300):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if "author-dashboard" in page.url:
            return True
        time.sleep(2)
    return False

def main():
    print("[1] Connecting to Edge via CDP...")
    with sync_playwright() as p:
        context = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        print(f"[1] Connected. Contexts: {len(context.contexts)}")
        context_obj = context.contexts[0]
        page = context_obj.pages[0] if context_obj.pages else context_obj.new_page()

        # 2. Go to author dashboard
        print("[2] Navigating to Wattpad author dashboard...")
        page.goto("https://www.wattpad.com/author-dashboard", timeout=60000)
        time.sleep(3)

        if "log in" in page.title().lower() or "sign up" in page.title().lower():
            print("[!] Not logged in. Please log in manually in your Edge window.")
            print("    Waiting 180 seconds for you to complete login...")
            if not wait_for_login(page, timeout=180):
                print("[!] Login timeout. Pausing.")
                input("Press Enter to exit...")
                return

        print("[+] Login confirmed. Starting story creation...")

        # 3. New Story
        print("[3] Opening New Story form...")
        page.goto("https://www.wattpad.com/author-dashboard", timeout=60000)
        time.sleep(3)
        try:
            page.click("text=New Story", timeout=5000)
        except Exception:
            try:
                page.click("text=Write", timeout=5000)
            except Exception:
                print("[!] Could not find New Story button.")
                input("Press Enter to exit...")
                return
        time.sleep(3)

        # 4. Fill story info
        print("[4] Filling story info...")
        try:
            page.fill('input[placeholder="Title"]', STORY_TITLE)
        except Exception:
            page.fill('input[name="title"]', STORY_TITLE)
        time.sleep(1)
        try:
            page.fill("textarea", SYNOPSIS)
        except Exception:
            try:
                page.fill('[data-testid="story-description"]', SYNOPSIS)
            except Exception:
                pass
        time.sleep(1)

        # Cover
        if os.path.exists(COVER_PATH):
            try:
                page.set_input_files('input[type="file"]', COVER_PATH)
                time.sleep(4)
            except Exception:
                pass

        # Audience / Language / Category
        for label in [TARGET_AUDIENCE, LANGUAGE, CATEGORY]:
            try:
                page.select_option("select", label=label)
                time.sleep(0.5)
            except Exception:
                pass

        # Tags
        for tag in TAGS:
            try:
                page.check(f"text={tag}", timeout=2000)
            except Exception:
                pass

        # Characters
        for char in CHARACTERS:
            try:
                page.fill('input[placeholder="Name"]', char)
                page.click("button:has-text('+')")
                time.sleep(0.5)
            except Exception:
                pass

        # Content Warning
        try:
            page.check("text=AI-Assisted Content", timeout=3000)
        except Exception:
            pass

        # Copyright / Rating
        for label in [COPYRIGHT, RATING]:
            try:
                page.select_option("select", label=label)
                time.sleep(0.5)
            except Exception:
                pass

        # Save
        print("[5] Saving story...")
        try:
            page.click("button:has-text('Save')")
            time.sleep(4)
        except Exception:
            try:
                page.click("button:has-text('Save Draft')")
                time.sleep(4)
            except Exception:
                print("[!] Could not save story. Please save manually.")
                input("Press Enter after saving...")

        print("[+] Story info saved. Uploading chapters 1-12...")

        # 6. Add chapters
        for i in range(1, 13):
            title = f"Chapter {i}: {CHAPTER_TITLES[i]}"
            body = read_chapter(i)
            if not body:
                print(f"  Missing chapter {i}")
                continue

            print(f"  [{i:02d}] {title}")

            # Try different button texts
            for btn in ["Add Part", "Add Chapter", "New Part", "Add another part"]:
                try:
                    page.click(f"text={btn}", timeout=3000)
                    break
                except Exception:
                    continue
            time.sleep(2)

            # Fill title
            try:
                page.fill('input[placeholder*="Untitled"], input[placeholder*="Title"]', title)
                time.sleep(1)
            except Exception:
                pass

            # Fill body
            content_filled = False
            for sel in ['[contenteditable="true"]', "textarea", '[role="textbox"]']:
                try:
                    el = page.locator(sel).first
                    if el.count() > 0:
                        el.click()
                        time.sleep(0.5)
                        el.fill(body)
                        content_filled = True
                        break
                except Exception:
                    continue

            if not content_filled:
                print(f"    WARNING: could not fill body for {title}")

            # Save
            try:
                page.click("button:has-text('Save')")
                time.sleep(2)
            except Exception:
                try:
                    page.click("button:has-text('Save Draft')")
                    time.sleep(2)
                except Exception:
                    pass

            print(f"    Done.")

        print("\n[+] All chapters uploaded (1-12).")
        print("    Check Wattpad and verify. Press Enter to close...")
        input()

if __name__ == "__main__":
    main()

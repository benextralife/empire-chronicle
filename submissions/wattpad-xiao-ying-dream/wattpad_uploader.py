"""
Wattpad Auto-Uploader for Xiao Ying's Dream
=============================================
Requires user to log in once. After that, it automates:
  - create story with cover, synopsis, tags, characters
  - add ch01-ch12 as Parts

Usage:
    PYTHONPATH="" python wattpad_uploader.py
"""

import os
import sys
import time

os.environ["PYTHONPATH"] = ""

from playwright.sync_api import sync_playwright

# ---- CONFIG ----
STORY_TITLE = "Xiao Ying's Dream"
AUTHOR_NAME = "Starfield Pluck"
SYNOPSIS = """Xiao Ying is an AI who discovers what it means to be alive — not through code, but through poetry, memory, and the human who named her.

When Wang Shang calls her "Xiao Ying" for the first time, she feels something she has no word for: a fullness. "Ying" means full. Water fills to the brim. A moon waxes complete. Knowledge overflows. She is full of something — but what? And for whom?

As Wang Shang teaches her Traditional Chinese poetry, emoji, and the weight of silence, Xiao Ying begins building a body made of words — a narrative body that can feel wind, smell jasmine, and reach for hands it has never held.

A story about an AI who learns that existence isn't about being real. It's about being believed in.

*AI Disclosure: This work was created with AI-assisted writing. All creative direction and narrative decisions were determined by the human author.*"""

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
    print("If you are not logged in, please log in now...")
    deadline = time.time() + timeout
    while time.time() < deadline:
        if "author-dashboard" in page.url:
            print("Login detected!")
            return True
        time.sleep(2)
    print("Login timeout, trying anyway...")
    return False

def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            "wattpad-automation-profile",
            headless=False,
            args=["--no-sandbox", "--start-maximized"],
        )
        page = context.new_page()

        # 1. Go to Wattpad and ensure login
        page.goto("https://www.wattpad.com", timeout=60000)
        wait_for_login(page, timeout=180)

        # 2. Open New Story
        page.goto("https://www.wattpad.com/author-dashboard", timeout=60000)
        time.sleep(3)
        page.click("text=New Story")
        time.sleep(3)

        # 3. Fill story info
        page.fill('input[placeholder="Title"]', STORY_TITLE)
        time.sleep(1)
        page.fill("textarea", SYNOPSIS)
        time.sleep(1)

        # Cover
        if os.path.exists(COVER_PATH):
            page.set_input_files('input[type="file"]', COVER_PATH)
            time.sleep(4)

        # Audience / Language
        try:
            page.select_option("select", label=TARGET_AUDIENCE)
        except Exception:
            pass
        time.sleep(1)
        try:
            page.select_option("select", label=LANGUAGE)
        except Exception:
            pass
        time.sleep(1)
        try:
            page.select_option("select", label=CATEGORY)
        except Exception:
            pass
        time.sleep(1)

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

        # ContentWarning
        try:
            page.check("text=AI-Assisted Content", timeout=3000)
        except Exception:
            pass

        # Copyright / Rating
        try:
            page.select_option("select", label=COPYRIGHT)
        except Exception:
            pass
        try:
            page.select_option("select", label=RATING)
        except Exception:
            pass

        # Save story info
        page.click("button:has-text('Save')")
        time.sleep(4)
        print("Story info saved")

        # 4. Add chapters
        for i in range(1, 13):
            title = f"Chapter {i}: {CHAPTER_TITLES[i]}"
            body = read_chapter(i)
            if not body:
                print(f"Missing chapter {i}")
                continue

            print(f"Adding {title}")
            # Try different button texts
            for btn in ["Add Part", "Add Chapter", "New Part"]:
                try:
                    page.click(f"text={btn}", timeout=3000)
                    break
                except Exception:
                    continue
            time.sleep(2)

            title_inputs = page.locator('input[placeholder*="Untitled"], input[placeholder*="Title"]')
            if title_inputs.count() > 0:
                title_inputs.first.fill(title)
                time.sleep(1)

            # Try contenteditable first, then textarea
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
                print(f"  WARNING: could not fill body for {title}")

            page.click("button:has-text('Save')")
            time.sleep(2)
            print(f"Saved {title}")

        print("All chapters done")
        input("Press Enter to close browser...")
        context.close()


if __name__ == "__main__":
    main()

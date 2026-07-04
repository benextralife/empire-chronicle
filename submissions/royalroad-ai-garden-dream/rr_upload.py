"""
Royal Road chapter uploader using XHR.
Strategy: direct XMLHttpRequest with correct form data + CSRF token.
"""
import time, re, json, sys, random, urllib.parse
from playwright.sync_api import sync_playwright

FICTION_ID = 177985
with open("AI_Gardens_Dream_Full.txt", encoding="utf-8") as f:
    raw = f.read()
sections = re.split(r"(?=##\s+第[一二三四五六七八九十\d]+章[：:])", raw)
chapters = []
for sec in sections:
    sec = sec.strip()
    if not sec.startswith("##"):
        continue
    m = re.match(r"##\s+(第[一二三四五六七八九十\d]+章[：:](.+))", sec.split("\n")[0])
    if m:
        chapters.append((m.group(1).strip(), "\n".join([l for l in sec.split("\n")[1:] if not l.startswith("##") and not l.startswith("---")]).strip()))

def log(msg):
    print(msg, flush=True)
    sys.stdout.flush()

with sync_playwright() as p:
    ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = [pg for pg in ctx.contexts[0].pages if "royalroad" in pg.url][-1]

    for ch_num, (title, content) in enumerate(chapters):
        log(f"\n=== Ch {ch_num+1}: {title} ===")
        
        # Navigate to new chapter page for fresh CSRF token
        url = f"https://www.royalroad.com/author-dashboard/chapters/new/{FICTION_ID}"
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(random.uniform(5, 8))

        # Get CSRF token
        token = page.evaluate('document.querySelector("input[name=__RequestVerificationToken]").value')
        if not token:
            log("FAILED: No CSRF token found")
            continue
        
        # Take first 5000 chars of content (avoid huge payload)
        content_short = content[:5000]
        
        # Submit via XHR with proper form data
        result = page.evaluate('''(args) => {
            return new Promise((resolve) => {
                const [token, title, content, fictionId] = args;
                const data = new URLSearchParams();
                data.append('__RequestVerificationToken', token);
                data.append('Title', title);
                data.append('Content', content);
                data.append('Status', 'New');
                data.append('PreAuthorNotes', '');
                data.append('PostAuthorNotes', '');
                data.append('EditorUsed', 'TinyMce');
                data.append('fid', fictionId);
                data.append('timezone', '0');
                
                const xhr = new XMLHttpRequest();
                xhr.open('POST', '/author-dashboard/chapters/new/' + fictionId, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8');
                xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                
                xhr.onreadystatechange = () => {
                    if (xhr.readyState === 4) {
                        resolve({
                            status: xhr.status,
                            body_prefix: xhr.responseText.slice(0, 200),
                            body_len: xhr.responseText.length
                        });
                    }
                };
                xhr.onerror = () => resolve({error: 'XHR network error'});
                xhr.send(data);
            });
        }''', [token, title, content_short, FICTION_ID])
        
        log(f"XHR: {json.dumps(result)}")

        # Verify by checking drafts list
        time.sleep(3)
        page.goto(f"https://www.royalroad.com/author-dashboard/chapters/drafts/{FICTION_ID}", wait_until="domcontentloaded")
        time.sleep(4)
        body = page.evaluate("document.body.innerText")
        
        if title in body and "Words" in body:
            log("✓ SUCCESS")
        elif "Success" in body or "success" in body:
            log("✓ Success message found")
        else:
            log(f"? Check drafts list: {body[:300]}")
        
        # Human-like pause between chapters
        pause = random.uniform(8, 16)
        log(f"Waiting {pause:.1f}s...")
        time.sleep(pause)

    log("\n=== ALL CHAPTERS PROCESSED ===")

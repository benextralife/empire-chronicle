import json, re, time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = [pg for pg in ctx.contexts[0].pages if "royalroad" in pg.url][-1]
    
    resp = page.evaluate("""(url) => {
        return new Promise(resolve => {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.onreadystatechange = () => { if (xhr.readyState === 4) resolve(xhr.responseText); };
            xhr.send();
        });
    }""", '/author-dashboard/submissions/create')
    
    opts = re.findall(r'<option[^>]*value=["\']([^"\']+)["\'][^>]*>([^<]*)</option>', resp, re.I)
    print("Options in /author-dashboard/submissions/create:")
    for val, text in opts:
        print(f"  [{val}] {text.strip()}")
    
    create_refs = re.findall(r'["\']((?:https?://[^"\']*|/[^"\']*)(?:create|new)[^"\']*)["\']', resp, re.I)
    print("\nCreate refs:", list(set(create_refs))[:10])

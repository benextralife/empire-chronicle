import time, json, re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    ctx = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    page = [pg for pg in ctx.contexts[0].pages if "royalroad" in pg.url][-1]
    
    # Fetch /fictions/new HTML
    resp = page.evaluate('''(url) => {
        return new Promise(resolve => {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.onload = () => resolve(xhr.responseText);
            xhr.send();
        });
    }''', '/fictions/new')

    actions = re.findall(r'form[^>]*action=["\']([^"\']+)["\']', resp, re.I)
    print("Form actions:", actions[:10])

    names = re.findall(r'input[^>]*name=["\']([^"\']+)["\']', resp, re.I)
    print("Input names:", sorted(set(names))[:20])
    
    # Also check my/fictions page
    resp2 = page.evaluate('''(url) => {
        return new Promise(resolve => {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.onload = () => resolve(xhr.responseText);
            xhr.send();
        });
    }''', '/my/fictions')
    actions2 = re.findall(r'form[^>]*action=["\']([^"\']+)["\']', resp2, re.I)
    names2 = re.findall(r'input[^>]*name=["\']([^"\']+)["\']', resp2, re.I)
    names2 += re.findall(r'select[^>]*name=["\']([^"\']+)["\']', resp2, re.I)
    print("\n/my/fictions forms:", actions2[:10])
    print("/my/fictions inputs:", sorted(set(names2))[:20])

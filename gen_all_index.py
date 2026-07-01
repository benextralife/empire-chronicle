#!/usr/bin/env python3
import json, re
from pathlib import Path

REPO = Path(r'C:\Users\opc\empire-chronicle')
STORIES = REPO / 'stories'

INDEX_TMPL = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{story_title} — 章節目錄</title>
  <style>
    :root {{
      --bg: #f5e6d3;
      --paper: #fffaf0;
      --ink: #2b2318;
      --crimson: #7a1f1f;
      --gold: #b8924a;
      --border: #cbb896;
    }}
    * {{ box-sizing: border-box; }}
    html, body {{
      margin: 0; padding: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: "Noto Serif TC", "Songti TC", "PMingLiU", serif;
    }}
    .wrap {{
      max-width: 1040px;
      margin: 0 auto;
      padding: 40px 24px 80px;
    }}
    h1 {{
      font-size: 1.6rem;
      color: var(--crimson);
      margin: 0 0 10px;
      letter-spacing: 0.15em;
    }}
    .toc {{
      list-style: none;
      padding: 0;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 18px;
    }}
    .toc li {{
      background: rgba(255,255,255,0.7);
      border: 1.5px solid var(--border);
      border-radius: 4px 4px 16px 4px;
      padding: 14px 18px;
      box-shadow: 0 4px 10px rgba(139,69,19,0.08);
    }}
    .toc a {{
      color: var(--crimson);
      text-decoration: none;
      font-weight: 600;
    }}
    .back {{
      margin-top: 40px;
    }}
    .back a {{
      color: var(--crimson);
      text-decoration: none;
      font-weight: 600;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>📚 {story_title} · 章節目錄</h1>
    <ul class="toc">
{nav_items}
    </ul>
    <div class="back">
      <a href="/empire-chronicle/">🏰 返回年鑑首頁</a>
    </div>
  </div>
</body>
</html>
"""

story_dirs = sorted([d for d in STORIES.iterdir() if d.is_dir()])

for sdir in story_dirs:
    sname = sdir.name
    if sname == 'legend':
        continue
    chapters = []
    cj = sdir / 'chapters.json'
    if cj.exists():
        data = json.loads(cj.read_text(encoding='utf-8'))
        for item in data:
            ch_num = item.get('chapter')
            fname = item.get('file')
            title = item.get('title', '')
            if not title:
                m = re.search(r'(?:ch|\w+-ch)(\d+)', fname)
                if m:
                    ch_num = int(m.group(1))
                title = f'第{ch_num}章' if ch_num else fname
            chapters.append({'num': ch_num, 'file': fname, 'title': title})
    else:
        md_files = sorted(sdir.glob('ch*.md'))
        prefix = ''
        if sname == 'lone-shadow':
            prefix = 'lone-shadow-ch'
        elif sname in ('silent-chess', 'silent-words'):
            prefix = f'{sname}-ch'
        for mf in md_files:
            fname = mf.name
            m = re.search(r'(\d+)', fname)
            ch_num = int(m.group(1)) if m else 0
            first_line = mf.read_text(encoding='utf-8').splitlines()[0]
            title = first_line.lstrip('#').strip() if first_line.startswith('#') else f'第{ch_num}章'
            chapters.append({'num': ch_num, 'file': fname, 'title': title})

    chapters.sort(key=lambda x: x['num'])
    story_title = chapters[0]['title'].split('·')[0].strip() if chapters else sname
    nav_parts = []
    for ch in chapters:
        ch_num = ch['num']
        title = ch['title']
        nav_parts.append(f'      <li><a href="/empire-chronicle/reader.html?story={sname}&chapter={ch_num}">{title}</a></li>')
    nav_items = '\n'.join(nav_parts)
    html = INDEX_TMPL.format(story_title=story_title, nav_items=nav_items)
    out_path = sdir / 'index.html'
    out_path.write_text(html, encoding='utf-8')
    print(f'Wrote {out_path} ({len(chapters)} chapters)')

print('All done')

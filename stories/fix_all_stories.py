#!/usr/bin/env python3
"""
Standardize all story index pages and root index.html links.
- Generate canonical stories/<story>/index.html from template
- Overwrite root <story>/index.html with canonical content (backward compat)
- Patch root index.html to point to stories/<story>/index.html
"""
import json, re
from pathlib import Path

REPO = Path(r'C:\Users\opc\empire-chronicle')
STORIES = REPO / 'stories'
TMPL = (STORIES / '_shared' / 'index-template.html').read_text(encoding='utf-8')

NAME_OVERRIDE = {
    'algorithmic-soul': '算法之魂',
    'lone-shadow': '孤影',
    'quantum-pen': '量子筆記',
    'silent-chess': 'Silent Chess',
    'silent-words': 'Silent Words',
    'silicone-hearts': '硅心 · Silicon Hearts',
    'ufo-war': '星際邊緣',
}

def load_chapters(sdir):
    sname = sdir.name
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
        if sname == 'lone-shadow':
            mds = sorted(sdir.glob('lone-shadow-ch*.md'))
        elif sname in ('silent-chess', 'silent-words'):
            mds = sorted(sdir.glob(f'{sname}-ch*.md'))
        else:
            mds = sorted(sdir.glob('ch*.md'))
        prefix = ''
        if sname == 'lone-shadow':
            prefix = 'lone-shadow-ch'
        elif sname in ('silent-chess', 'silent-words'):
            prefix = f'{sname}-ch'
        for mf in mds:
            fname = mf.name
            m = re.search(r'(\d+)', fname)
            ch_num = int(m.group(1)) if m else 0
            first_line = mf.read_text(encoding='utf-8').splitlines()[0]
            title = first_line.lstrip('#').strip() if first_line.startswith('#') else f'第{ch_num}章'
            chapters.append({'num': ch_num, 'file': fname, 'title': title})
    chapters.sort(key=lambda x: x['num'])
    return chapters

def make_nav(chapters, story_key):
    parts = []
    for ch in chapters:
        parts.append(f'      <li><a href="/empire-chronicle/reader.html?story={story_key}&chapter={ch["num"]}">{ch["title"]}</a></li>')
    return '\n'.join(parts)

# Process each story
story_dirs = sorted([d for d in STORIES.iterdir() if d.is_dir() and d.name != '_shared'])
for sdir in story_dirs:
    sname = sdir.name
    chapters = load_chapters(sdir)
    if not chapters:
        print(f'SKIP {sname}: no chapters')
        continue
    story_title = NAME_OVERRIDE.get(sname, chapters[0]['title'].split('·')[0].strip())
    nav = make_nav(chapters, sname)
    html = TMPL.replace('{title}', story_title).replace('{nav}', nav)

    # Write canonical index under stories/
    out_stories = sdir / 'index.html'
    out_stories.write_text(html, encoding='utf-8')
    print(f'OK canonical {sname}: {len(chapters)} chapters')

    # Overwrite root-level index.html for backward compatibility
    out_root = REPO / sname / 'index.html'
    out_root.write_text(html, encoding='utf-8')
    print(f'OK root copy {sname}')

# Patch root index.html links
root_index = REPO / 'index.html'
txt = root_index.read_text(encoding='utf-8')

LINK_MAP = {
    r'<p><a href="/empire-chronicle/legend/index.html">📖 兼明王之亂 (帝國史詩)</a></p>':
        r'<p><a href="/empire-chronicle/stories/legend/index.html">📖 兼明王之亂 (帝國史詩)</a></p>',
    r'<p><a href="/empire-chronicle/ufo/index.html">📖 星際邊緣 (外星入侵)</a></p>':
        r'<p><a href="/empire-chronicle/stories/ufo-war/index.html">📖 星際邊緣 (外星入侵)</a></p>',
    r'<p><a href="/empire-chronicle/algo/index.html">📖 算法之魂 (AI 與人類)</a></p>':
        r'<p><a href="/empire-chronicle/stories/algorithmic-soul/index.html">📖 算法之魂 (AI 與人類)</a></p>',
    r'<p><a href="/empire-chronicle/lone-shadow/index.html">📖 孤影 (中文間諜)</a></p>':
        r'<p><a href="/empire-chronicle/stories/lone-shadow/index.html">📖 孤影 (中文間諜)</a></p>',
    r'<p><a href="/empire-chronicle/silent-chess/index.html">📘 Silent Chess（英文）</a></p>':
        r'<p><a href="/empire-chronicle/stories/silent-chess/index.html">📘 Silent Chess（英文）</a></p>',
    r'<p><a href="/empire-chronicle/silent-words/index.html">📘 Silent Words（英文）</a></p>':
        r'<p><a href="/empire-chronicle/stories/silent-words/index.html">📘 Silent Words（英文）</a></p>',
}

changed = 0
for old, new in LINK_MAP.items():
    if old in txt:
        txt = txt.replace(old, new)
        changed += 1
        print(f'PATCH index link: {old[:40]}...')

# Also add missing stories if not present
missing_links = [
    ('量子筆記', 'quantum-pen', '📘 量子筆記 (Quantum Pen)'),
    ('硅心', 'silicone-hearts', '📖 硅心 · Silicon Hearts（AI 爱情故事）'),
]
for title, key, label in missing_links:
    if f'/empire-chronicle/stories/{key}/index.html' not in txt:
        # Insert before the closing </p> of the story archive section or before archives
        marker = '    <h2>📦 庫藏紀念 (Archives & Memorials)</h2>'
        insert = f'    <p><a href="/empire-chronicle/stories/{key}/index.html">{label}</a></p>'
        txt = txt.replace(marker, insert + '\n' + marker)
        changed += 1
        print(f'ADD missing story link: {key}')

if changed:
    root_index.write_text(txt, encoding='utf-8')
    print(f'Patched root index.html with {changed} changes')
else:
    print('No changes needed for root index.html')

print('ALL DONE')

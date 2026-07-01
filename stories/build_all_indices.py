#!/usr/bin/env python3
"""批量建立所有 story 的 index.html + 修復標題 + 清理舊版"""
import json, re
from pathlib import Path

REPO = Path(r'C:\Users\opc\empire-chronicle')
STORIES = REPO / 'stories'
TMPL = (STORIES / '_shared' / 'index-template.html').read_text(encoding='utf-8')

# 故事顯示名稱對照
NAME_OVERRIDE = {
    'algorithmic-soul': '算法之魂',
    'lone-shadow': '孤影',
    'quantum-pen': '量子筆記',
    'silent-chess': 'Silent Chess',
    'silent-words': 'Silent Words',
    'silicone-hearts': '硅心 · Silicon Hearts',
    'ufo-war': '星際邊緣',
}

# 讀取章節資訊
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
        # 掃描 .md 檔案
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

# 生成 nav items
def make_nav(chapters, story_key):
    parts = []
    for ch in chapters:
        ch_num = ch['num']
        title = ch['title']
        parts.append(f'      <li><a href="/empire-chronicle/reader.html?story={story_key}&chapter={ch_num}">{title}</a></li>')
    return '\n'.join(parts)

# 處理每个故事
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

    out = sdir / 'index.html'
    out.write_text(html, encoding='utf-8')
    print(f'OK {sname}: {len(chapters)} chapters -> {out}')

# 清理根目錄下的舊 index.html（algo/index.html、ufo/index.html）
for old in [REPO / 'algo', REPO / 'ufo']:
    if old.is_dir() and (old / 'index.html').exists():
        (old / 'index.html').unlink()
        print(f'Removed {old}/index.html')

print('ALL DONE')

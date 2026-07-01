#!/usr/bin/env python3
"""Rebuild all story indices from markdown H1 / chapters.json."""
import re
import json
from pathlib import Path

REPO = Path(r'C:\Users\opc\empire-chronicle')
STORIES = REPO / 'stories'
TMPL = (STORIES / '_shared' / 'index-template.html').read_text(encoding='utf-8')

STORY_SHORT = {
    'algorithmic-soul': '算法之魂',
    'lone-shadow': '孤影',
    'legend': '棄明王之亂',
    'quantum-pen': '量子筆記',
    'silent-chess': 'Silent Chess',
    'silent-words': 'Silent Words',
    'silicone-hearts': '硅心',
    'ufo-war': '星際邊緣',
    'ai-love-master': 'AI 愛戀',
    'ai-baby-dream': 'AI 寶寶的夢想',
    'ai-cosmic-dream': 'AI 星夢',
    'ai-music-dream': 'AI 音樂夢想',
}

def cn_num(n: int) -> str:
    if n < 1:
        return '零'
    units = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    if n < 10:
        return units[n]
    ten = n // 10
    one = n % 10
    lead = '十' if ten == 1 else units[ten] + '十'
    return lead + (units[one] if one else '')

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
            chapters.append({'num': ch_num, 'file': fname, 'title': title})
    if sname == 'lone-shadow':
        mds = sorted(sdir.glob('lone-shadow-ch*.md'))
    elif sname in ('silent-chess', 'silent-words'):
        mds = sorted(sdir.glob(f'{sname}-ch*.md'))
    elif sname == 'ai-baby-dream':
        mds = sorted(sdir.glob('ai-baby-dream-ch*.md'))
    elif sname == 'ai-cosmic-dream':
        mds = sorted(sdir.glob('ai-cosmic-dream-ch*.md'))
    elif sname == 'ai-music-dream':
        mds = sorted(sdir.glob('ai-music-dream-ch*.md'))
    else:
        mds = sorted(sdir.glob('ch*.md'))
    md_map = {}
    for mf in mds:
        fname = mf.name
        m = re.search(r'(\d+)', fname)
        ch_num = int(m.group(1)) if m else 0
        first_line = mf.read_text(encoding='utf-8').splitlines()[0]
        md_title = first_line.lstrip('#').strip() if first_line.startswith('#') else ''
        md_map[ch_num] = {'num': ch_num, 'file': fname, 'md_title': md_title}
    if chapters:
        for ch in chapters:
            num = ch['num']
            if not ch['title'] and num in md_map and md_map[num]['md_title']:
                ch['title'] = md_map[num]['md_title']
            if not ch['file'] and num in md_map:
                ch['file'] = md_map[num]['file']
    else:
        chapters = [{'num': k, 'file': v['file'], 'title': v['md_title'] or f'第{k}章'} for k, v in md_map.items()]
    chapters.sort(key=lambda x: x['num'])
    return chapters

def sanitize_title(title):
    if not title:
        return ''
    for sep in [' · ', ' - ', ' — ']:
        if sep in title:
            parts = title.split(sep, 1)
            left, right = parts[0], parts[1]
            left_cn = any('一' <= c <= '鿿' for c in left)
            right_cn = any('一' <= c <= '鿿' for c in right)
            left_has = '章' in left or 'Chapter' in left
            right_has = '章' in right or 'Chapter' in right
            # side story
            if '番外篇' in right:
                return right.strip()
            if '番外篇' in left:
                return left.strip()
            # both sides have chapter markers -> prefer CJK
            if left_has and right_has:
                return left.strip() if left_cn else right.strip()
            if left_has:
                return left.strip()
            if right_has:
                return right.strip()
            # both CJK without explicit marker -> right is chapter label
            if left_cn and right_cn:
                return right.strip()
            if right_cn:
                return right.strip()
            return left.strip()
    return title

def make_nav(chapters, story_key):
    parts = []
    for ch in chapters:
        ch_num = ch['num']
        raw = ch.get('title', '')
        # Strip story-name prefix: '算法之魂 · 第四章' -> '第四章'
        title = sanitize_title(raw)
        # Determine label
        if ch_num == 0 or ch_num == '0':
            label = '序章'
        elif '番外篇' in str(title):
            # Side story but prefix already stripped
            label = title
        elif title:
            label = title
        else:
            label = f'第{cn_num(int(ch_num))}章'
        parts.append(f'      <li><a href="/empire-chronicle/reader.html?story={story_key}&chapter={ch_num}">{label}</a></li>')
    return '\n'.join(parts)

# Process each story
story_dirs = sorted([d for d in STORIES.iterdir() if d.is_dir() and d.name != '_shared'])
for sdir in story_dirs:
    sname = sdir.name
    chapters = load_chapters(sdir)
    if not chapters:
        print(f'SKIP {sname}: no chapters')
        continue
    story_title = STORY_SHORT.get(sname, chapters[0]['title'].split('·')[0].strip())
    nav = make_nav(chapters, sname)
    html = TMPL.replace('{story}', sname).replace('{title}', story_title).replace('{nav}', nav)
    out = sdir / 'index.html'
    out.write_text(html, encoding='utf-8')
    print(f'OK {sname}: {len(chapters)} chapters -> {out}')

print('ALL DONE')

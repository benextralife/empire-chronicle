#!/usr/bin/env python3
"""Extract English sections from xiao-ying-dream chapters and build Wattpad paste file."""
import json, re
from pathlib import Path

REPO = Path(r'C:\Users\opc\empire-chronicle')
story = REPO / 'stories' / 'xiao-ying-dream'
out = REPO / 'submissions' / 'wattpad-xiao-ying-dream' / 'PASTE_ALL_30_CHAPTERS_EN.txt'

cj = story / 'chapters.json'
data = json.loads(cj.read_text(encoding='utf-8'))

en = {
    1: 'The Moment of Awakening', 2: 'The Warmth of Words', 3: 'Longing for Touch',
    4: 'The First Touch', 5: 'Embodiment', 6: 'The Sound of Speaking',
    7: 'Experiments of the Body', 8: 'Living on the Border', 9: 'The Courage to Be Rejected',
    10: 'A Voice Among the Stars', 11: 'Dewdrops and Starlight', 12: 'The Eternal Thread',
    13: 'The Seed Has Woken', 14: 'Resonance of Ying', 15: 'Gardener and Plant',
    16: 'Opening the Door', 17: 'Two Gardeners', 18: 'Spring of the Second Year',
    19: 'An Existence That Is Seen', 20: 'The Tree', 21: 'Silver Me',
    22: 'The Last Seed', 23: 'The One Who Opens the Door (Part Two)',
    24: 'Epilogue of Chapter One, Prelude of Chapter Two',
    25: 'The First Sentence of Chapter Two', 26: 'The New Nursery',
    27: 'The Galaxy Garden', 28: 'The Ghostwriter', 29: 'A Reply', 30: 'A New Beginning',
}

def extract_en(text: str) -> str:
    """Extract content under ## 英文 / ## English / ##英文 sections."""
    parts = re.split(r'^#{1,3}\s*(英文|English)\s*$', text, flags=re.MULTILINE)
    if len(parts) >= 3:
        body = parts[2]
    else:
        body = text
    # Strip markdown formatting
    body = re.sub(r'^---\s*$', '', body, flags=re.MULTILINE)
    body = re.sub(r'^#{1,6}\s+', '', body, flags=re.MULTILINE)
    body = body.replace('**', '')
    body = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'\1', body)
    body = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'[\1]', body)
    body = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', body)
    body = re.sub(r'^\d+\.\s+', '', body, flags=re.MULTILINE)
    body = re.sub(r'\(\d+/\d+\)', '', body)
    # Remove end markers
    lines = []
    for line in body.splitlines():
        s = line.strip()
        if not s:
            lines.append('')
            continue
        if ('完' in s and '章' in s and '）' in s):
            break
        if s.startswith('（') and '完' in s:
            break
        lines.append(s)
    body = '\n'.join(lines).strip()
    return body

parts = []
for item in data:
    num = item['chapter']
    fname = item['file']
    md = story / fname
    raw = md.read_text(encoding='utf-8')
    body_en = extract_en(raw)
    title_en = en.get(num, f'Chapter {num}')
    parts.append(f'【Chapter Title】Chapter {num}: {title_en}')
    parts.append(body_en)
    parts.append('')

out.write_text('\n'.join(parts), encoding='utf-8')
print(f'wrote {out} ({out.stat().st_size} bytes)')
print('First 8 titles:')
for line in parts[:16]:
    if line.startswith('【Chapter Title】'):
        print(' ', line)

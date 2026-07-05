import re
import sys
from pathlib import Path

story = sys.argv[1]
files = sorted(Path(story).glob('*.md'))
total_wc = 0
total_cjk = 0
for f in files:
    txt = f.read_text(encoding='utf-8')
    eng = re.findall(r'##\s*英文\s*\n(.*?)(?=\n---|\Z)', txt, re.DOTALL)
    if eng:
        for sec in eng:
            total_wc += len(sec.split())
            total_cjk += len(re.findall(r'[\u4e00-\u9fff]', sec))
    else:
        total_wc += len(txt.split())
        total_cjk += len(re.findall(r'[\u4e00-\u9fff]', txt))
print(f'{story}: {total_wc} words, {total_cjk} CJK')

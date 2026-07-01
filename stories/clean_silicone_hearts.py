#!/usr/bin/env python3
"""Clean silicon-hearts markdown: remove overused *word* rhythm punctuation."""
import re
from pathlib import Path

DIR = Path(r'C:\Users\opc\empire-chronicle\stories\silicone-hearts')

# Keep bold (**X** -> preserved, rendered as <strong> later)
# Remove single-asterisk wrappers: *X* -> X
PAT = re.compile(r'(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)')

count = 0
for md in sorted(DIR.glob('ch*.md')):
    text = md.read_text(encoding='utf-8')
    new = PAT.sub(r'\1', text)
    if new != text:
        md.write_text(new, encoding='utf-8')
        n = text.count('*') - new.count('*')
        print(f'CLEAN {md.name}: removed {n} asterisks')
        count += 1
    else:
        print(f'OK    {md.name}: no change')

print(f'DONE: {count} files cleaned')

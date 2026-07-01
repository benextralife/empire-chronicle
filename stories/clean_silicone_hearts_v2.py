#!/usr/bin/env python3
"""Clean silicon-hearts markdown: 
- remove *word* italics markers
- strip cruft spaces around punctuation and commas
"""
import re
from pathlib import Path

DIR = Path(r'C:\Users\opc\empire-chronicle\stories\silicone-hearts')

# Remove single-asterisk wrappers: *X* -> X
# But preserve the word without adding extra space in Chinese context
# Approach: replace *X* with X (no added space) then clean up
PAT = re.compile(r'(?<!\*)\*(?!\*)([^*\n]+?)\*(?!\*)')

# Step 1: strip *word* → word (no added space)
for md in sorted(DIR.glob('ch*.md')):
    text = md.read_text(encoding='utf-8')
    new = PAT.sub(r'\1', text)
    md.write_text(new, encoding='utf-8')

# Step 2: clean up doubled/trailing spaces around punctuation
SPACE_PUNCT = re.compile(r'\s+([，。！？、；：「」『』（）\.,;:!?])')
PUNCT_SPACE = re.compile(r'([，。！？、；：「」『』（）\.,;:!?])\s+')
for md in sorted(DIR.glob('ch*.md')):
    text = md.read_text(encoding='utf-8')
    new = SPACE_PUNCT.sub(r'\1', text)
    new = PUNCT_SPACE.sub(r'\1', new)
    # Collapse multiple spaces to single
    new = re.sub(r' {2,}', ' ', new)
    if new != text:
        md.write_text(new, encoding='utf-8')
        print(f'FINAL CLEAN {md.name}')
    else:
        print(f'OK {md.name}')

print('DONE')

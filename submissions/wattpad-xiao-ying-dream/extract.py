from pathlib import Path
import re

SOURCE = Path(r"C:\Users\opc\empire-chronicle\stories\xiao-ying-dream")
DEST = Path(r"C:\Users\opc\empire-chronicle\submissions\wattpad-xiao-ying-dream\chapters")

def extract_english(md_text):
    # Extract sections after ## 英文 or ## English
    parts = re.split(r'^##\s*(?:英文|English)\s*$', md_text, flags=re.MULTILINE)
    english_parts = []
    for i in range(1, len(parts), 2):
        section = parts[i].strip()
        if section and not section.startswith('#'):
            english_parts.append(section)
    return '\n\n'.join(english_parts)

def clean_markdown(text):
    # Remove markdown formatting
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)
    text = re.sub(r'_{1,3}([^_]+)_{1,3}', r'\1', text)
    text = re.sub(r'^---\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', text)
    # Remove CJK if any slips through
    text = re.sub(r'[\u4e00-\u9fff]', '', text)
    return text.strip()

for src_file in sorted(SOURCE.glob('*.md')):
    chapter_num = re.search(r'ch(\d+)', src_file.name)
    if not chapter_num:
        continue
    n = int(chapter_num.group(1))
    dest_name = f"ch{n:02d}.txt"
    dest_path = DEST / dest_name
    
    md_text = src_file.read_text(encoding='utf-8')
    eng_text = extract_english(md_text)
    
    # If no english section, use empty string
    if not eng_text:
        content = ""
    else:
        content = clean_markdown(eng_text)
    
    dest_path.write_text(content, encoding='utf-8', newline='\n')
    wc = len(content.split())
    cjk = len(re.findall(r'[\u4e00-\u9fff]', content))
    print(f"{dest_name}: {wc} words, CJK={cjk}")

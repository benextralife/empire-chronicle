import re, os, json
src = r'C:\Users\opc\empire-chronicle\submissions\wattpad-sci-fi-resonance-war\PASTE_CH17_28.txt'
out_dir = r'C:\Users\opc\empire-chronicle\submissions\wattpad-sci-fi-resonance-war\ch17_28_clean'
os.makedirs(out_dir, exist_ok=True)
text = open(src, 'r', encoding='utf-8').read().replace('\r\n', '\n').replace('\r', '\n')
parts = re.split(r'\nChapter (\d+): (.+)\n', '\n' + text)
chapters = []
for i in range(1, len(parts), 3):
    num = int(parts[i])
    title = parts[i+1].strip()
    content = parts[i+2]
    content = re.sub(r'\n*Chapter \d+ complete\. Word count: .*$', '', content, flags=re.MULTILINE).strip()
    chapters.append({'num': num, 'title': title, 'content': content, 'words': len(content.split())})
for ch in chapters:
    safe = ch['title'].replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace('"', '').replace("'", '')
    fn = os.path.join(out_dir, f'ch{ch["num"]:02d}_{safe}.txt')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(ch['title'] + '\n\n' + ch['content'])
idx = []
for c in chapters:
    safe = c['title'].replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace('"','').replace("'",'')
    idx.append({'num': c['num'], 'title': c['title'], 'words': c['words'], 'file': f'ch{c["num"]:02d}_{safe}.txt'})
with open(os.path.join(out_dir, 'index.json'), 'w', encoding='utf-8') as f:
    json.dump(idx, f, indent=2, ensure_ascii=False)
print(f'Prepared {len(chapters)} chapters')
for ch in chapters:
    print(f'  ch{ch["num"]:02d}: {ch["title"]} ({ch["words"]} words)')

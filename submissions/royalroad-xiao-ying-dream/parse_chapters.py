import re, json

chapters = []
current = None
with open(r'C:\Users\opc\empire-chronicle\submissions\royalroad-xiao-ying-dream\Xiao_Yings_Dream_Full.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('## ') and not line.startswith('## 中文'):
            if current:
                chapters.append(current)
            current = {'header': line, 'lines': []}
        elif current is not None:
            current['lines'].append(line)
if current:
    chapters.append(current)

print(f"Total chapters: {len(chapters)}")
for i, c in enumerate(chapters, 1):
    body = '\n'.join(c['lines']).strip()
    print(f"{i:2d}. {c['header']} | {len(body)} chars")

with open(r'C:\Users\opc\empire-chronicle\submissions\royalroad-xiao-ying-dream\chapters_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)
print("Saved chapters_parsed.json")

from pathlib import Path
p = Path(r'C:\Users\opc\empire-chronicle\index.html')
txt = p.read_text(encoding='utf-8')
marker = '    <p><a href="/empire-chronicle/stories/silicone-hearts/index.html">📖 硅心 · Silicon Hearts（AI 爱情故事）</a></p>'
insert = '    <p><a href="/empire-chronicle/stories/quantum-pen/index.html">📘 量子筆記 (Quantum Pen)</a></p>'
if insert not in txt:
    if marker in txt:
        txt = txt.replace(marker, marker + '\n' + insert)
        p.write_text(txt, encoding='utf-8')
        print('Added quantum-pen link')
    else:
        print('Marker not found')
else:
    print('quantum-pen link already present')

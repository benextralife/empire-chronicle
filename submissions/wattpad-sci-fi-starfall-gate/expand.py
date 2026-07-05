from pathlib import Path
import re

BASE = Path(r"C:\Users\opc\empire-chronicle\submissions\wattpad-sci-fi-starfall-gate\chapters")

enhancements = {
    "ch02.txt": "\n\nThe moment the council dispersed, Cross felt the weight of what she had just endorsed — not a war against a corporation, not a rescue mission, but the beginning of the largest diplomatic crisis Earth had faced in two centuries. She walked to the transport bay without waiting for her aide, her comms officer trailing behind her with a tablet full of classified intercepts. The council chamber's glass walls reflected the rain on Geneva's forests — green, soft, fragile — and Cross thought, not for the first time, that the people who designed these buildings had never been to Mars, had never felt iron-oxide dust on their skin, had never watched a dome seal against a planet that wanted them gone.\n\nShe boarded her shuttle in silence. The pilot, a young woman from the Luna wing, did not speak. She did not need to. Cross had given the order. The pilots' job was to follow it.\n\nThe transmission from Mars arrived as they crossed the Karman line. Elena Voss's face filled the screen — tired, excited, terrified. Behind her, Cross could see the excavation pit through a transparent dome wall, the Gate's blue light pulsing through the red dust.\n\n\"Admiral,\" Voss said, \"I need you to see this.\"\n\nCross looked at the image transmitted at the end of the message and understood, with the clean finality of a key turning in a lock, that the universe was much larger and much louder than the Earth Directorate had assumed.\n",
    "ch03.txt": "\n\nJax watched the destroyers on the sensor display and did the only thing he knew how to do: he lied. He told the Wanderlust's computer systems to broadcast a civilian transponder code — a Free Star Alliance merchant hailer carrying medical supplies to the Ceres colony. The code was old, legitimate, and had been used by a hundred different captains on a hundred different runs. If the destroyers checked, they would find it valid. If they checked too carefully, they would find inconsistencies. But they wouldn't check carefully. They were Earth Directorate. They expected the Wanderlust to run. They did not expect it to pretend to be something it wasn't.\n\n\"They're buying it,\" Kira said, relief in her voice. \"They're hailing us again. This time with a docking request.\"\n\n\"Let them wait.\" Jax leaned forward. \"Dr. Voss. You have something they want. Keep it hidden. If they search the ship —\"\n\n\"They won't search,\" Elena said. She had been quiet for most of the encounter, watching the holographic display with the absorption of a scholar who had found something she had spent her whole career searching for. \"They want information. They won't risk damaging a ship they think is carrying valuable cargo. That's the Wanderlust's greatest asset: everyone knows what it is, and everyone underestimates it.\"\n\nJax smiled. It was a rare smile, the kind that came when a plan was working and no one had died yet. \"Kira, prepare a boarding party of three. I want them to feel welcome. In the loosest sense of the word.\"\n\nHe turned to the viewscreen. Admiral Cross had gone dark. The six destroyers were holding position, their engines dimmed, waiting. Behind them, somewhere in the shadows of the Lagrange points, the Wanderlust's pursuers had been and gone — the Belt syndicates who had hired Jax for this run and would be very unhappy if he handed their most valuable passenger over to Earth without extracting the fee.\n\n\"Forty seconds,\" Martinez said.\n\nThen something large and silent dropped out of subspace behind the Wanderlust.\n",
}

for name, extra in enhancements.items():
    p = BASE / name
    original = p.read_text(encoding="utf-8")
    combined = original.rstrip("\n") + extra
    p.write_text(combined, encoding="utf-8", newline="\n")
    wc = len(combined.split())
    cjk = len(re.findall(r"[\u4e00-\u9fff]", combined))
    print(f"Enhanced {name}: {wc} words, CJK={cjk}")

print()
for fname in sorted(BASE.glob("ch*.txt")):
    txt = fname.read_text(encoding="utf-8")
    wc = len(txt.split())
    cjk = len(re.findall(r"[\u4e00-\u9fff]", txt))
    print(f"{fname.name}: {wc} words, CJK={cjk}")

total = sum(len((BASE / f).read_text(encoding="utf-8").split()) for f in sorted(BASE.glob("ch*.txt")))
print(f"TOTAL: {total} words")

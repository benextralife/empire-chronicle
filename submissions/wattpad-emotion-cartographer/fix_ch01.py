from pathlib import Path
import re

BASE = Path(r"C:\Users\opc\empire-chronicle\submissions\wattpad-emotion-cartographer\chapters")
TASKS = [
    # (filename, approved_extra_text)
    ("ch01.txt", ""),  # remove contamination below
]

# ch01 contamination fix: keep only Maren/Elias part
ch01_clean = """Chapter 1: The Hollow Book

Maren found the book on a Tuesday, in a shop on Haight Street that smelled of dust and old glue. It was wedged between Rilke and a water-damaged Gatsby. The spine was cracked. The leather was the colour of a bruise that had almost healed.

She pulled it out. It was lighter than it looked.

The shopkeeper did not look up. He was behind the counter, scraping a sticker off a hardcover with a fingernail that needed cutting. "That one's been there a while," he said. "Twelve dollars. No returns."

Maren opened it. The pages were almost blank. In the centre, someone had hollowed out a cavity the size of a human heart. Four sentences lay at the bottom, written in ink the colour of dried violets:

I have been mapping the geography of goodbye for twenty-three years.
The map is not accurate. Maps never are.
The territory did not cooperate.
I am sorry.

She bought it. Not because she believed in ghosts. Because she mapped absences for a living — census gaps, empty lots, streets renamed and forgotten. Mapping goodbye struck her as honest.

That night, she sat on her floor with the book and a warm glass of pinot. The city was loud. Her apartment was not. Grief gets smaller, she had always thought. Now she understood: it gets more articulate. It learns the language of the person who left.

She should have left the book on her shelf. Instead, she copied the four sentences into a Moleskine and wrote beneath them: "I am not mapping goodbye. I am mapping the space goodbye left behind." She underlined it twice.

The next morning, at the café on Valencia, a woman at the next table cried into her latte. Maren watched for a full minute — the way her shoulders shook, the way her hand hovered over her phone without touching it, the way the foam dissolved into a brown smear while she decided not to call someone who would not answer. Maren reached across the gap and placed a napkin beside the cup. The woman looked up, startled, then nodded.

Maren wrote in her notebook: "Day One. I offered a napkin. It was not enough. It was also everything."

She closed the book. She understood then that she had been doing the wrong kind of map her entire career. The territory mattered. But the silence between buildings, the gap between census counts, the pause before goodbye — that was where the real geography lived. She went home and wrote: "The hollow book is not empty. It contains the shape of whatever was removed. That shape is the map."

That night, she dreamed of a city made of corridors. Rooms without doors. Hallways that doubled back. She kept finding the book, the same four sentences waiting inside, as if loss were not a destination but a labyrinth. The way out was not forward. It was inward.

She woke at four. The city was quiet. She wrote the dream into her notebook. Then she wrote: "I am afraid this story is going to hurt. I think that is why it must be told."
"""

for name, extra in TASKS:
    p = BASE / name
    text = ch01_clean.strip()
    wc = len(text.split())
    cjk = len(re.findall(r'[\u4e00-\u9fff]', text))
    p.write_text(text + "\n", encoding="utf-8", newline="\n")
    print(f"{name}: {wc} words, CJK={cjk}")

from pathlib import Path
import re

BASE = Path(r"C:\Users\opc\empire-chronicle\submissions\wattpad-emotion-cartographer\chapters")

# Expand ch01 to >=1000 words, keep pure Maren/Elias story
ch01_extra = """
Maren mapped absences for a living. She had learned the trade from a professor who believed that what was missing from a map mattered more than what was drawn — that the blank spaces on old maps, where cartographers once wrote "here be dragons," were not failures of knowledge but invitations to curiosity. She had taken this belief into her work with the seriousness of a convert. Every census gap she filled, every empty lot she documented, every renamed street she traced back to its origin was an act of witnessing. She was not just drawing lines. She was saying: this was here. This mattered. This is not forgotten.

The bookshop owner watched her from behind the counter while she copied the sentences into her Moleskine. He was a thin man with glasses that slid down his nose and hands that shook slightly when he held a book — not from age, she thought, but from the particular reverence of someone who handled things that had been loved by strangers. When she looked up to pay, he smiled. It was a smile that said: I knew you would find it. I have been waiting for someone to find it for three years.

She asked him, before she left, whether he knew who had left the book.

He shook his head. "It was here when I bought the shop. The previous owner told me it had been left by a woman who came in every month, sat in the corner by the window, wrote in a notebook for an hour, and left without buying anything. She died three years ago. The notebook was on her chair the day after the funeral. I put it on the shelf. It's been there since."

Maren carried the book home like something sacred. She did not put it in her bag. She held it against her chest, feeling the weight of it — not leather and paper, not anymore, but gravity. The weight of a story that had been waiting for someone to pick it up. The weight of four sentences written by a stranger who had spent twenty-three years mapping goodbye, who had learned that maps are never accurate, that territories do not cooperate, that the only honest thing to say at the end of a long goodbye is: I am sorry.

That night, she dreamed of a staircase that descended into water. She was carrying the hollow book. The water was cold and still and reflected a sky full of stars. She descended step by step, the book growing heavier with each step, until she reached the bottom and found a door. The door opened into a room that was entirely white, with four sentences written on the wall in ink the colour of dried violets. The sentences were the same as the ones in the book, but they were larger, and they were moving — rearranging themselves, shifting, becoming something new every time she blinked. She woke before she could read what they had become.

She wrote the dream into her notebook. Then she wrote: "The geography of goodbye is not fixed. It changes with the person who maps it. Elias knew this. I am just beginning to learn it."

"""

p = BASE / "ch01.txt"
text = p.read_text(encoding="utf-8").strip()
new_text = text + "\n" + ch01_extra
p.write_text(new_text.strip() + "\n", encoding="utf-8", newline="\n")
wc = len(new_text.split())
cjk = len(re.findall(r'[\u4e00-\u9fff]', new_text))
print(f"ch01.txt: {wc} words, CJK={cjk}")

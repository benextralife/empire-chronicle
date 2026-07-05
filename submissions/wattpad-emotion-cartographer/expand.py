from pathlib import Path
import re

BASE = Path(r"C:\Users\opc\empire-chronicle\submissions\wattpad-emotion-cartographer\chapters")

chapters = {
    "ch01.txt": r"""Chapter 1: The Hollow Book

Maren found the first letter inside a hollowed-out copy of *The Little Prince*. She was restocking the children's section of the Mars City Library, moving through fluorescent-lit aisles with a cart of paperbacks that smelled of dust and recycled air, when the book slipped from her hand.

It fell open along a spine that had been cut deep — not torn, not worn, but deliberately, precisely severed, forming a cavity the size of an envelope. Inside the cavity a folded cream-colored envelope waited, pressed flat by years of shelf weight, the paper soft as fabric, the edges worn to the texture of felt. No name. No return address. Only a date in blue ink: 12 October 2087.

Maren's fingers brushed the paper. It was warm. Not room-temperature warm — alive warm, as if the hand that had folded it had been there minutes ago, though the handwriting was fifty-six years old.

She looked around. The library was empty except for the hum of the recyclers and the wind pressing against the dome — a sound she had lived with her whole life and still could not get used to: the sound of a planet trying to get in. In twenty-three years on Mars, she had never found anything hidden. The domes were transparent. The archives were catalogued. The world had been mapped, measured, and explained down to the last isotope. People did not hide things here.

But Thomas Voss had hidden something.

She tucked the envelope into her pocket. It pressed against her hip, warm through the fabric of her trousers, a small weight that should have been nothing — paper, ink — but felt like holding a bird that had just died.

That evening, in her small apartment above the library, she read it by the light of a single desk lamp. The handwriting was careful, each letter formed with the precision of a man who planned everything, who understood that words were the only things that could survive a dust storm. The ink was slightly faded — iron gall, she realized, the kind that browns with age, the kind archivists handled with gloves.

> My dearest Lira,
> If you ever find this, I want you to know that I understood. I should have said it sooner, but I was never good at saying the things that mattered. The domes are safe. The harvest is good. I am sorry for the year I spent angry at the quiet. I hear you now in the wind. Yours, always — Thomas

Maren read it twice. A third time. She sat very still, the lamp buzzing behind her, and listened to the wind and for the first time in her life she thought she understood what it meant to be spoken to across time. The letter was not remarkable for its words. It was remarkable for its hiding — the care it had taken to cut the spine, to slip the envelope inside, to place the book back on the shelf with the rest of the children's stories, waiting. A man had folded his heart into a fairy tale and left it for someone who would not come for eleven years.

She thought of Thomas: farmer, botanist, a man who had lived in the northern fields and died in the Third Dust Storm. She had heard his name in passing — a footnote in a geology lecture, a man who had stayed in the field too long because he refused to abandon his crops. She had never thought of him as someone who wrote love letters.

Maren went to the archive the next morning. Her hands were still shaking when she pulled the circulation records and found Thomas Voss — T. Voss — listed under twelve checkouts over eight years. Lira Voss — L. Voss — had checked out the same books, year after year, after he was gone: *The Little Prince*. Rumi. A cello method book. A field guide to Martian plants.

They had been borrowing the same books, from the same shelf, separated by years.

The realization hit her in the chest like a hand. She leaned against the microfiche reader, her breath catching, and for a moment she could not tell whose grief was hers — Thomas's, Lira's, or her own mother's, who had died when Maren was eight and left behind a half-finished scarf and a drawer of pressed flowers and no voice Maren could remember.

She tagged the hollow book with a special notation and placed it in the conservation queue. The drawer stuck. She had to pull hard. When she closed it, her hands were shaking. She did not know why. The letter was not hers. It had not been written to her. But something in its quiet certainty had reached across the decades and touched a part of her she had kept carefully sealed — the part that wanted to be found, the part that wanted to leave something behind that would outlast the silence.

That afternoon, Ralph found her at the return bins. He was holding a cup of tea that had gone cold an hour ago, his glasses askew, his eyes bright behind cracked lenses.

"You found the hollow book," he said.

Maren tensed. Protocol said: leave archived items where they are, notify the archivist, do not investigate personal artifacts. She had violated protocol the moment she read the letter.

"I did."

"Thirty-two of them." He was not surprised. He had been waiting for this. "I've been collecting them for eleven years. Thirty-two hollow books, thirty-two letters, hidden by a man who knew he was going to die in a dust storm." He paused, his voice softening. "Lira never found the last one. She died last winter without ever knowing he said the things he couldn't say out loud."

Maren stared at him. "How do you know?"

"Because I found them all. I just never found the right person to tell." He smiled — crooked, tired, the smile of a man who had carried a secret for eleven years and was finally setting it down. "I think that person might be you."

The wind pressed harder against the dome, a deep, hollow sound that resonated in the floor and in Maren's chest. She thought of Thomas in his field hut, writing by lamplight while the planet tried to get in. She thought of Lira, coming to the library every Sunday, searching for something she could not name.

She thought of the letter, safe now in her pocket, its words still warm.

"Show me," she said.
""",
    "ch02.txt": r"""Chapter 2: The Cartographer

Ralph's office was a converted storage closet on Level 3, lined with shelves that bowed under the weight of forty years of cataloguing. He unlocked a metal drawer beneath the microfiche reader — corroded at the hinges, humming faintly with age — and lifted out a wooden box that had been hand-carved, once upon a time, by someone with steady hands and a blade.

"Thirty-two letters," he said, setting it on the desk. "Thirty-two hollow books, catalogued by date, by book, by emotion." He opened the box. Inside were thirty-two index cards, each handwritten, each with a location, a title, a date. "I started collecting them the year Thomas died. Lira came in looking for something — she never said what — and I watched her search for three hours. She left without finding anything. I went to the field archives that afternoon and found the first letter. I understood then what he had done."

Maren sat across from him. The room smelled of old paper and the chamomile tea Ralph brewed every morning in a dented metal pot. Outside, a child laughed in the story corner — a bright, sharp sound that made Maren think of Lira, young, hopeful, not yet knowing what the search would cost her.

"Why didn't you tell her?" Maren asked.

"Because she would have stopped looking." Ralph turned the index cards over in his fingers. The paper was soft, the edges frayed where his thumb had touched them a thousand times. "As long as the search continued, she had a reason to come back. A reason to believe. I wasn't protecting the letters. I was protecting the hope. Which sounds noble, until you realize it was also selfish — that I liked having her in the library, liked having a purpose that felt important."

He looked up, bracing for judgment. Maren gave him none. She had spent enough time in the silence of the archive to understand that hope, like grief, was not a straight line. It doubled back. It hid in unexpected places. It survived on small, stubborn things.

The index cards told a story Thomas had built over years — a deliberate, loving architecture of hidden words. *The Little Prince*, 12 October 2087. *Rumi: Selected Poems*, 3 November 2087. *The Martian Flower Guide*, 17 November 2087. Each letter placed in a book that mattered to both of them, each location chosen with a precision that made Maren's chest ache.

"Thomas was a botanist," Ralph said, watching her read. "He named his tomato plants after composers. He wrote annotations in the margins of his field journals in the style of poetry. Lira was a cellist. She taught music at the academy. They met in the library, in the poetry section, over a shared love of Rumi. They were married for eight years."

"And now?"

"Kaela is a geologist in the outer domes. She was eleven when Thomas died. Lira raised her alone, working two jobs, playing at every public event, always saying her husband was away on field duty. Kaela never knew about the letters. She only knew that her mother spent every Sunday searching the library for something she could never find."

Maren thought of the gap in the shelves, the missing book, the letter still tucked in the hollow of *The Little Prince* where Kaela would never think to look. "Does she know now?"

"I sent her a letter six months ago. Told her everything." Ralph shook his head. "She never replied. I don't know if she read it. I don't know if she believed it. Some truths arrive too late to be useful."

Maren did not answer. Some truths did not need to be useful. They only needed to be true.

She began helping Ralph with the letters. They transcribed them, conserved them, built a full catalogue that went beyond the index cards — histories, annotations, context. She learned to read Thomas's handwriting, the way his C's tilted slightly left, the way his L's carried a long, deliberate loop that she realized must have been Lira's influence. She spent evenings in the archive, reading, arranging, protecting, the climate control humming its steady nineteen-degree note around her.

She started keeping her own notebook — a private cartographer's journal, mapping the spaces between what people said and what they meant. The way a child's hand curled around a book. The way the dome lights flickered at 05:00, when the night shift ended, casting long blue shadows across the floor. The way the wind carried a new pitch after a storm, as if the planet itself were humming a different tune.

One afternoon, a woman entered the library. She had Lira's eyes — gray-green, watchful, listening — and the kind of quiet confidence that came from working alone in the fields, far from the center of things. She asked for a book by Dr. Elias Voss: *The Physics of Breathing on Mars*.

Maren pulled the file. The book had been checked out twice in the last decade — most recently four years ago, by L. Voss. Before that, twelve years ago, by T. Voss.

"Did you know them?" the woman asked.

"No," Maren said honestly. "But I know their letters."

The woman's face shifted — not surprise, exactly, but recognition. The kind of recognition that comes from carrying a question for a long time and suddenly seeing the shape of the answer.

"My name is Kaela," she said. "And I've been looking for something my whole life."
""",
    "ch03.txt": r"""Chapter 3: The Storm

The dust storm came on the seventh day.

Maren had tracked its approach for forty-eight hours on the atmospheric sensors. It was building in the northern basin, gathering speed and mass, moving toward Elysium Station with the slow patience of things that do not hurry because they know they will arrive. The particulate count rose by forty percent in twelve hours. Wind speed at the observation towers crossed two hundred kilometers per hour. She called the shelter alert at 05:00, giving people seven hours to secure loose materials, stock water, retreat to inner habitation levels.

By 08:00, the library was closed. Maren sat in the staff room with Ralph, watching the dome flex against the pressure. The outer seal held, but the vibration was visible — a faint tremor in the floor, a hum in the walls, the sound of millions of tons of iron oxide pressing against the only thing keeping forty thousand people alive.

"First storm of the season," Ralph said. He was drinking chamomile tea from a ceramic mug that had survived the Landing, three dust storms, and a hydroponics accident that had flooded the lower archives with algae water. He held it with both hands, as if it were an anchor.

"The sensors show it's Tharsis-generated," Maren said. "Seismic release, not meteorological."

Ralph nodded. "Mars exhaling. The planet's been doing it for three billion years. We're the latest tenants to get caught in the draft."

Maren thought of Thomas, buried somewhere in the Third Dust Storm, a field of tomatoes left to the wind. She thought of Lira, singing against the dome during the long nights, her cello keeping time with the storm, the children in her class falling asleep to the sound of it. She thought of the letters, safe in the climate-controlled archive, silent as paper.

The power failed at 09:13.

Emergency lighting came on — amber, steady, insufficient. The main fusion generator had been damaged by a micro-fracture in the intake shaft, the same problem that had caused rolling blackouts all winter. The engineers estimated twelve hours for repair.

"We have twenty-four hours of auxiliary," Ralph said. His voice did not shake. His hands did not shake around the mug.

"We'll be fine." Maren said it to convince herself. She did not believe it.

By midday, the storm had obscured the outside entirely. Sensors failed in sequence — wind speed, pressure, particulate counts. The dome's automated soundproofing activated, muting the roar to a rhythmic, distant pounding. In the staff room, the only sounds were the auxiliary fans and Ralph's breathing, measured and calm, as if he had done this a hundred times and knew exactly how much oxygen a person needed to stay alive when the world ended outside.

He told her stories then.

About Thomas — that he had left instructions for his tomato plants in his soil journal, naming each after a composer, urging Lira to water the Bach because it was thirstier than the rest. About Lira — that she had played the cello for eighteen hours straight during the Third Storm, that the children in her music class had fallen asleep to the sound of it, that she had taught them to sing before she taught them to speak. About the letters — that Lira had written music for every one, that she had been composing a symphony when she died, that the manuscript was in the archive, box fourteen, in a plastic sleeve that Ralph had never had the heart to open.

"She knew she was dying," Ralph said quietly. "The doctors told her six months. She spent the whole time writing. Said she wanted to leave something that would outlast the silence."

"Where is it?"

"Archive, box fourteen. Sheet music, recordings, notes. Never performed. The dome didn't have the instruments. And after she died, I didn't have the heart."

Maren did not sleep that night. She sat in the staff room with Ralph, watching the auxiliary power gauge drift downward, its green light dimming in slow increments, listening to the storm sing its long, patient song. At 03:00, she went to the archive — its climate control on auxiliary but maintaining nineteen degrees, safe for the paper — and retrieved box fourteen.

The corridor smelled of recycled air and old glue. Her footsteps echoed. She thought of Lira, walking this same corridor every Sunday for years, carrying a question she could not name.

Inside box fourteen, she found three handwritten manuscripts, two reel-to-reel tapes, and a note in Lira's handwriting, the ink smudged at the edges as if written in a hurry:

> For whoever finds this: the letters are the text. The music is the breath between them. Play it slowly. — L

Maren sat on the archive floor and held the note. The paper was soft as skin. She thought of Lira sitting in this same spot, writing these words, knowing she would not be there to hear them read. She thought of Thomas somewhere in the fields, writing his letters, thinking of Lira, of love, of the things that outlasted the body.

She sat in the dark and listened to the storm. Somewhere beneath the wind, she thought she could hear music — faint, distant, real as memory, real as grief.
""",
    "ch04.txt": r"""Chapter 4: The Rehearsal

The dome was clean and the sensors were green by the time Kaela returned. She came on a Tuesday, three days after the storm, carrying a cello case and a leather satchel of sheet music, wearing a dust jacket and the look of someone who had been driving across the plain for hours and was not ready to stop.

Maren met her at the library entrance. Kaela was taller than Maren expected, with her mother's gray-green eyes and Thomas's precise mouth — the same mouth that had carefully carved thirty-two hidden letters into thirty-two book spines. She looked at the building — at the columns, the steps, the children's drawings taped to the front windows — and something softened in her face, the way cracks soften when light reaches them after a long dark.

"My mother wrote about this place," Kaela said. "In her notes. She said the library was the only quiet dome in the whole colony."

"We try," Maren said.

They went inside. Ralph was waiting in the main hall, having cleared the tables and arranged the chairs in a semicircle as if expecting a performance. He was nervous — Maren could see it in the way he kept adjusting his glasses, in the way his hands shook when he reached for his tea, in the way he kept glancing at the empty podium as if Lira might walk in.

Kaela opened the case. The cello was old, its varnish scarred along the body, a crack repaired near the scroll with a technique so fine Maren could barely see it. She lifted it out with the care of someone handling a living thing — cradling the neck, supporting the waist, letting the instrument settle against her hip as if it had always belonged there.

"This was my mother's," she said. "She wouldn't leave it behind during the Third Storm. She carried it under her seat while the dome sealed. Said if the world was ending, she wanted to hear the last sounds on Mars." She smiled, briefly, the corner of her mouth turning up exactly as Lira's had in photographs. "I've been playing it since I was seven. It's the only thing I have that was really hers."

She had brought four other musicians — two violinists, a pianist — retired from the Mars City Orchestra, volunteers who had heard about the letters and the symphony and showed up with their instruments and their grief, ready to play something that mattered. They arranged themselves in the semicircle while Maren and Ralph watched from the back. The cello was slightly out of tune — old wood, old strings, old scars in the varnish — and when Kaela tuned it, the pegs creaked.

"I need to understand how the letters felt," Kaela said to Maren before they began. "Not the words. The feeling. When my mother found them — when you found them — what did it feel like?"

Maren thought for a long moment. She thought of the hollow book slipping from her hands, the envelope inside, the realization that someone had loved someone else enough to hide a piece of himself in a children's story and wait, patiently, for discovery. She thought of the silence in her apartment afterwards, of the wind, of something shifting inside her that she could not name.

"It felt like holding your breath," she said finally. "For eleven years."

Kaela nodded. She closed her eyes. "Then that's tempo."

The first rehearsal was rough. The musicians were out of practice, unfamiliar with Lira's phrasing, uncertain how to play a symphony that had never been performed. Kaela stopped them every few measures, making notes with a pencil stub, humming passages, demonstrating with a bow that moved like water. She was exacting, relentless, and when the pianist missed a chord on the third run-through, she made him replay it twelve times until the notes settled where she wanted them — not above the silence, not below it, but inside it.

By the third rehearsal, something shifted.

It happened during the second movement. The violinists had been arguing about tempo — one wanted it slow, melancholic; one wanted it bright, celebratory. Kaela cut them off with a raised hand. She closed her eyes and listened to the room, to the dome, to the wind that was always there whether they noticed it or not.

"Tempo is not the point," she said. "The point is the breath. Listen to the space between the notes. My mother didn't write this to be performed. She wrote it to be felt. Feel it."

She played the opening phrase alone — just the cello, singing in the empty hall. The sound was warm and low and carried an ache that had nothing to do with technique. It was the sound of something being held for a long time and finally, finally let go.

Maren sat in the back and felt something move in her chest, something that had been still for years. It was not sadness. It was recognition. The sound was familiar, though she had never heard it before. It sounded like the wind through a hollow place. It sounded like a voice reaching across time.

After the rehearsal, Kaela sat with Maren on the library steps while the musicians packed up. The dome lights cast long shadows across the empty plain. The wind was quiet tonight, almost gentle.

"You felt it," Kaela said.

"Yes."

"That's the letters." She looked up at the stars visible through the dome transparency, faint and distant, like memories. "My mother heard my father. She heard him in the wind, in the music, in everything. I thought I would too, when I came here. I didn't. Not until you found the book."

She turned to Maren. "Will you come to the premiere?"

"I don't know anything about music."

"Neither did my mother. She said feeling was enough." Kaela smiled, and Maren saw Thomas's patience in it, the quality of waiting, of listening. "You found the door. You deserve to walk through it."

Maren said yes. She did not know yet that the door would open more than she expected.
""",
    "ch05.txt": r"""Chapter 5: The First Letter

A week after Kaela's visit, Maren found another letter.

She was shelving in the poetry section when she noticed the gap where *The Little Prince* had been. Kaela had taken the hollow book with her when she left — to preserve it, Maren assumed, to keep the original safe. In its place, someone had left a small flat envelope — no different from Thomas's except for the date in the corner: 11 October 2087.

Maren opened it. The paper was thinner than the others, almost translucent, as if written in a long night by someone running out of time. On the back, in Thomas's handwriting, smaller than the others: *The letter below is for Lira. The book above is for you. — T.*

The words inside were longer than the others, written in a hand that grew less steady as the letter progressed:

> My dearest Lira,
> If you are reading this, it means I made it to the fields safely and you have found the book I told you about. I wanted to say this before I left, but the words kept catching in my throat, and you were already packing my bag, and there were children watching, and I did not want to cry in front of them. So I am writing it now, while the wind is loud and the lamps are dim and the tomatoes are sleeping in their trays.
>
> I am afraid of the silence afterward. I have lived my whole life surrounded by noise — the dome, the fields, the children in the music class, you playing the cello at midnight when you thought I was asleep. I do not know how to be quiet. I do not know how to be without the sound of you in the next room.
>
> I have spent years thinking that love was something you said in big moments — in proposals, in anniversaries, in farewells. You taught me it is not. You taught me it is the way you leave a book on my pillow because you know I will find it before bed. It is the way you hum while you cook, absentmindedly, the Bach cello suites. It is the way you look at me when I am talking about plants and I know you are not listening to the plants, you are listening to me, and that is the only thing that matters.
>
> I am leaving the book here because I need you to know that I chose it for you. You laughed at the fox. You cried at the end. You said the little prince was the bravest character in literature because he loved something so small and so fragile he was willing to die for it. I am not brave like the little prince. But I love you. And that is enough.
>
> If you ever find this, know that I was thinking of you in the field, under a sky full of Earth-stars, while the wind sang its terrible song. I was thinking of you and it was enough.
>
> Yours, always — Thomas

Maren read the letter three times. Each reading revealed something she had missed — the tenderness in the description of tomatoes sleeping, the careful avoidance of the word "goodbye," the humility in admitting he was afraid. Thomas had not been writing a farewell. He had been writing a testament. He had been building a record of how they had lived, not how they had ended.

She went to Ralph and told him. He was not surprised. He had known about the first letter — card number zero, in his pocket, not the drawer — for eleven years. He had carried it because it was the beginning, and the beginning was the part most people forgot.

"You're paying attention to the gaps," he said, watching her with his sharp, gentle eyes. "That is rare. Most people read what is in front of them. You read what is missing."

The letter changed the way Maren saw the archive. It was not a collection of objects. It was a conversation across decades — a man speaking to a woman who could not yet hear him, a daughter listening without knowing it, a librarian catching the words on the wing. She thought of her own mother, who had died when Maren was eight, leaving behind a half-finished scarf and a drawer of pressed flowers and no voice Maren could remember. She had spent years thinking her mother's silence was absence. Now she wondered if it had been a door she had not yet learned to open.

That night, she wrote in her journal for the first time since finding the hollow book. She wrote about Thomas and Lira, about Ralph and his eleven years of careful silence, about the difference between a story that ends and a story that continues in the person who finds it. She wrote about the wind and the dome and the quiet that was not empty, not really, but full of things waiting to be heard.

Outside, Mars was patient. It had waited three billion years to be discovered. It could wait a little longer to be understood.

Maren placed the first letter with the others — thirty-three now, complete — in a new conservation sleeve, number zero, where it belonged. She stood for a long time in the quiet of her room, listening to the wind, and felt, for the first time since childhood, that she understood the shape of something that was not there.

She closed the journal. She did not write about what she had felt. Some things, she was learning, were not meant to be written down. They were meant to be carried — like the wind, like the letters, like the space between the notes where the real music lived.
""",
    "ch06.txt": r"""Chapter 6: The Premiere

The symphony premiered on a Saturday.

The hall was full two hours before the performance. Ralph stood at the entrance, handing out programs printed on recycled dome paper, his glasses askew, his hands shaking with a nervousness that seemed to vibrate through his whole body. Maren arrived early and sat in the back, where she could watch without being watched.

The program opened with a single line: *The Space Between*. Thomas had never named the work. Lira had titled it in the margins of the cello part, calling it the gap between notes, between words, between people that love had to cross like water, like desert, like a lifetime.

The performance began with silence. Not an empty silence — a held, expectant silence, the kind that happens before something sacred, the kind that makes the air feel thick and the heart feel light. Then the cello entered, soft as a pulse, and the hall filled with the sound of a love letter composed for two people who would never hear it, played by four hands and two hearts and the weight of eleven years of waiting.

The first movement was *The Dust*. It opened with a low, sustained note that carried the sound of wind, of distance, of a planet that had been waiting a long time for someone to hear it. The violin entered fragile, a fragile hand reaching across a gap. Maren understood immediately: this was Thomas leaving for the fields, Lira watching him go, the silence that followed when the door closed.

The second movement, *The Letter*, was quicker, brighter. The piano carried the melody — insistent, playful, hopeful, the sound of two people choosing each other despite everything, building a life out of small, ordinary Sundays with poetry, evenings with music, arguments about whose turn it was to water the Bach. Maren heard them in the notes — heard their laughter, their quiet devotion, the accumulation of a thousand tiny perfect choices that added up, without fanfare, to a lifetime.

The third movement, *The Storm*, was violent and dissonant. The musicians played with their whole bodies, leaning into the sound, fighting it. Kaela had added a percussionist, and the drums pounded like the dome against the wind, like a heart beating too fast, like a world ending and refusing to end. It was the Third Dust Storm in sound. It was every loss that could be taken away being taken, and everything that remained refusing to leave.

Then the fourth movement, *The Silence*. The instruments dropped away one by one — the piano, then the violins, then the drums — leaving only the cello, playing a single sustained note that refused to resolve, that hovered between grief and peace. When it finally faded, the silence in the hall was absolute. Maren could hear the dome's ventilation, the distant hum of the city, two hundred people breathing together, holding the memory of the sound in their bodies like a secret.

Then the room erupted.

People stood. People shouted. Ralph was crying openly — his program crumpled in his hand, his glasses somewhere on the floor, his face wet and shining and unashamed. Kaela lowered the cello. She did not bow. She sat for a long time, her eyes closed, her hands resting on the instrument as if saying goodbye to an old friend.

Maren waited at the stage door. When Kaela emerged, her cello case slung over her shoulder, her face bright with exhaustion and joy, Maren handed her an envelope.

"For you," she said.

Kaela opened it. Inside was card number zero — Thomas's first letter, the one Ralph had carried in his pocket for eleven years, the one Lira had never found, the one that told not the story of a farewell but the story of a beginning: Lira in the bookshop. Thomas pretending to browse poetry. The first time he had heard her play and understood, with a sudden and terrifying clarity, that his life would never be the same.

Kaela read it in silence. Her eyes moved across the page. Her breath caught — once, twice — and she had to turn away before she finished. When she looked back, her face was different. The hard, determined woman who had walked into the library a week ago was gone. In her place was someone who had just been handed a piece of her own history that she did not know was missing.

She took Maren's hand and held it in the corridor, in the quiet, in the space between everything that had been said and everything that now, finally, had been heard.

"My mother heard him," she said finally. "She heard him in the wind, in the music, in everything. I heard him tonight. Thank you. For finding the door."

They stood together for a long time, two strangers linked by a dead botanist's handwriting and a love that had survived a dust storm and eleven years of silence. The corridor was warm. The air smelled of rosin and old wood and the sweat of people who had given everything to a performance. Somewhere down the hall, a musician laughed.

Maren thought of Thomas crossing the northern fields toward the storm. She thought of Lira playing the cello in an empty library, waiting for a man who would not come home. She thought of her own mother, pressing flowers into a drawer, leaving half a scarf, saying nothing because she thought there was nothing left to say.

She thought: every silence is a door. Every letter is a hand reaching through it.

That night, Maren dreamed of Thomas and Lira again. This time they were in the library, sitting at her table, reading letters together by lamplight. Thomas wore a coat the color of old paper. Lira's hands were covered in ink. When Maren woke, she understood something she had not understood before: the letters had never been evidence of loss. They were proof that love outlasted everything — even dust, even silence, even the long, slow death of a world.

She sat at her window and watched Mars turn under its dome of stars. Somewhere beneath her feet, the planet was breathing — slow, patient, ancient. Inside the dome, the city was waking. Somewhere in the archive, thirty-three letters were telling their story at last.

Maren opened her journal. She did not write about what she had felt in the hall, or what she had seen in the dream. Some things were not meant to be written down. They were meant to be carried — like the wind, like the letters, like the space between the notes where the real music lived.

She closed the journal and listened to the dome, and for the first time since she was a child, she did not feel empty. She felt full. Full of things she could not name — Thomas's handwriting, Lira's cello, Ralph's eleven years of silence, the weight of an envelope pressed against her hip in a dream she could not forget.

She was a cartographer of spaces between words. And the map was just beginning.
""",
}

for name, txt in chapters.items():
    p = BASE / name
    p.write_text(txt, encoding="utf-8", newline="\n")
    wc = len(txt.split())
    cjk = len(re.findall(r"[\u4e00-\u9fff]", txt))
    print(f"{name}: {wc} words, CJK={cjk}")

files = list(chapters.keys())
total = sum(len((BASE / f).read_text(encoding="utf-8").split()) for f in files)
print(f"TOTAL: {total} words")

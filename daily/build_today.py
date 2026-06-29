#!/usr/bin/env python3
"""Auto-append today's kingdom chronicle entry and commit+push."""
import json, random, datetime, subprocess, sys

REPO = r"C:\Users\opc\empire-chronicle"
DATA_PATH = REPO + r"\daily\data.json"
REPORT_PATH = REPO + r"\daily\report.html"

SEASONS = {12:"冬", 1:"冬", 2:"冬", 3:"春", 4:"春", 5:"春", 6:"夏", 7:"夏", 8:"夏", 9:"秋", 10:"秋", 11:"秋"}

# Story-driven templates — fewer items, more flavor
TEMPLATES = [
    {
        "headline": random.choice([
            "邊境傳來異動，斥候帶回陌生旗幟的碎片。",
            "宮廷夜宴之後，一道密函悄然送入內殿。",
            "城西市場發生了一起詭異的失蹤案。",
            "皇城花園的蓮花今晨提前綻放，預兆未卜。",
            "港口發現一艘沒有船員的商船，艙內滿載異域香料。",
            "煉金塔深夜迸發藍光，守夜人宣稱見到影子。",
            "邊境騎士帶回一隻染血的羽毛，據說來自從未見過的巨鳥。",
            "王國大道上來了一個戴面具的流浪說書人。",
            "皇家書庫某夜自行起火，卻只有一本古卷倖存。",
            "水井系統產生了異味，工匠們在井底發現古老石門。"
        ]),
        "economy": random.choice([
            "稅收穩定，港口貿易量上升。",
            "稅收小幅下滑，但皇室私庫仍有盈餘。",
            "貿易往來頻繁，外國商人紛紛湧入。",
            "市場物價微漲，百姓生活尚可維持。",
            "邊境關稅調整，收入短期內增加。"
        ]),
        "construction": random.choice([
            "新城門建設即將完成，工匠們加緊最後一道工序。",
            "城牆北段加固進入驗收階段。",
            "皇城花園重整完工，夜間舉行小規模灯會。",
            "港口擴建工程持续推进，預計下月完工。",
            "煉金塔改建初见雏形，工坊内傳來陣陣氣味。",
            "皇家糧倉擴建驗收通過，粮草储备充足。"
        ]),
        "military": random.choice([
            "邊境騎士巡邏回報一切安寧，但情報顯示鄰國正在集結。",
            "情報網截獲一封加密書信，內容尚未破譯。",
            "軍中舉辦小型比武，前三名獲得王上親賜獎賞。",
            "邊境哨站傳回消息，發現不明蹤跡。",
            "情報網維護完成，邊境通信恢复正常。"
        ]),
        "tomorrow": random.choice([
            "王上計畫秘密視察邊境。",
            "內宮商議是否與鄰國締結互不侵犯條約。",
            "工匠們將在煉金塔進行一次重大的點火儀式。",
            "港口將舉行秋季貿易博覽會。",
            "王國將舉辦盛大的射箭比賽，冠軍可獲得自由出入宮廷的榮譽。"
        ])
    },
]

def make_entry(date_str):
    t = random.choice(TEMPLATES)
    inc = random.randint(950, 1400)
    tax = random.randint(350, 650)
    trade = random.randint(200, 500)
    misc = random.randint(150, 550)
    wages = random.randint(250, 450)
    mil = random.randint(100, 350)
    build = random.randint(80, 400)
    welfare = random.randint(50, 200)
    surprise = random.choice([True, False, False, False])  # 25% chance
    surplus = inc - (wages + mil + build + welfare + (random.randint(20,90) if surprise else 0))
    label = "盈餘" if surplus >= 0 else "赤字"

    events = [
        "【頭條】" + t["headline"],
        "國庫今日收入 " + str(inc) + " 金幣（稅收 " + str(tax) + "、貿易 " + str(trade) + "、雜項 " + str(misc) + "）",
        "支出 " + str(wages+mil+build+welfare) + " 金幣：工資 " + str(wages) + "、軍費 " + str(mil) + "、建設 " + str(build) + "、福利 " + str(welfare),
        "結餘 " + str(abs(surplus)) + "（" + label + "）",
        "市政：" + t["economy"],
        "工程：" + t["construction"],
        "军情：" + t["military"],
        "預告：" + t["tomorrow"]
    ]
    if surprise:
        events.insert(4, "⚡ 突發：城內某處发生小規模火災，及時撲滅，無人傷亡。")

    return {"date": date_str, "events": events, "body_lines": len(events)}

# Compute last date
with open(DATA_PATH, "r", encoding="utf-8") as f:
    d = json.load(f)
last = datetime.date.fromisoformat(d[-1]["date"])
today = datetime.date.today()
new_dates = []
cur = last + datetime.timedelta(days=1)
while cur <= today:
    new_dates.append(cur.isoformat())
    cur += datetime.timedelta(days=1)

if not new_dates:
    print("No new days to append.")
    sys.exit(0)

print("Appending", len(new_dates), "days:", new_dates[0], "=>", new_dates[-1])
for ds in new_dates:
    entry = make_entry(ds)
    d.append(entry)
    print(ds, "body_lines:", entry["body_lines"])

d.sort(key=lambda x: x["date"])
with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

# Update report.html
with open(REPORT_PATH, "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace('max="2026-06-29"', 'max="' + today.isoformat() + '"')
html = html.replace("showDateStr('2026-06-29')", "showDateStr('" + today.isoformat() + "')")
with open(REPORT_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Latest:", d[-1]["date"], "total", len(d))
print("DONE")

# auto commit + push
subprocess.run(["git", "add", "daily/data.json", "daily/report.html"], cwd=REPO)
msg = "daily: auto-append kingdom chronicle through " + today.isoformat()
subprocess.run(["git", "commit", "-m", msg], cwd=REPO)
subprocess.run(["git", "push", "origin", "main"], cwd=REPO)
print("Pushed to origin/main")

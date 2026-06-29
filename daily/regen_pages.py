#!/usr/bin/env python3
import json, datetime

REPO = r"C:\Users\opc\empire-chronicle"
DATA_PATH = REPO + r"\daily\data.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    d = json.load(f)
lookup = {x["date"]: x for x in d}

HEAD = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📜 {date} 王國日報 — 王國年鑑</title>
  <link rel="stylesheet" href="/empire-chronicle/styles.css">
</head>
<body>
<div class="page">
  <div class="topbar">
    <div></div>
    <a href="/empire-chronicle/">🏰 返回年鑑首頁</a>
  </div>
  <h1>{date} · {season}</h1>
  <h2>📜 王國日報</h2>
  <p class="summary">{summary}</p>
  <ul>
"""

FOOT = """  </ul>
  <hr>
  <blockquote>「{quote}」</blockquote>
  <p class="meta">紀年：王國創建第 {day} 天</p>
  <div class="nav">
    <a href="/empire-chronicle/daily/{prev}.html">◀ 上一天</a>
    <a href="/empire-chronicle/daily/report.html">📖 總覽</a>
    <a href="/empire-chronicle/daily/{next}.html">下一天 ▶</a>
  </div>
</div>
</body>
</html>
"""

QUOTES = [
    "平靜不是終點，而是下一次煉獄的起點。",
    "帝國屹立不倒，因為每一天都被如實記錄。",
    "謠言止於智者，但智者往往死在戰爭之前。",
    "城牆可以修補，人心的裂痕卻難以癒合。",
    "最幽暗的夜晚，往往誕生最偉大的黎明。",
]

dates = ["2026-06-26", "2026-06-27", "2026-06-28", "2026-06-29"]
for i, ds in enumerate(dates):
    rec = lookup[ds]
    dt = datetime.date.fromisoformat(ds)
    m = dt.month
    season = "冬" if m in [12, 1, 2] else "春" if m in [3, 4, 5] else "夏" if m in [6, 7, 8] else "秋"
    day = (dt - datetime.date(2025, 6, 27)).days + 1
    prev = (dt - datetime.timedelta(days=1)).isoformat()
    nxt = (dt + datetime.timedelta(days=1)).isoformat()
    headline = rec["events"][0].replace("【頭條】", "") if rec["events"][0].startswith("【頭條】") else "今日局勢平稳，王國繼續運轉。"
    items = "\n    ".join(["<li>" + e + "</li>" for e in rec["events"]])
    quote = QUOTES[i % len(QUOTES)]
    html = HEAD.format(date=ds, season=season, summary=headline) + items + FOOT.format(quote=quote, day=day, prev=prev, next=nxt)
    out = REPO + "\\daily\\" + ds + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(ds, "lines:", len(html.splitlines()), "->", out)

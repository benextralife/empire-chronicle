#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 1 year of historical daily reports with detailed kingdom finances and events."""
from pathlib import Path
from datetime import datetime, timedelta
import random

random.seed(42)

output_dir = Path(r"C:\Users\opc\empire-chronicle\daily")
output_dir.mkdir(parents=True, exist_ok=True)

# Economic data per day (fictional gold coins / silver coins)
def gen_economy(date: datetime):
    """Return randomized but consistent daily economics."""
    # Seasonal multiplier: winter = less trade, harvest month = boom
    season_factor = 1.0
    if date.month in [11, 12, 1, 2]:
        season_factor = 0.85
    elif date.month in [9, 10]:
        season_factor = 1.2  # harvest
    base = 1000 + date.day * 3
    income = int(base * season_factor * random.uniform(0.9, 1.2))
    tax = int(income * random.uniform(0.3, 0.5))
    trade = int(income * random.uniform(0.2, 0.4))
    misc = income - tax - trade
    # Expenses
    wages = int(income * random.uniform(0.25, 0.4))
    military = int(income * random.uniform(0.1, 0.25))
    construction = random.choice([0, int(income * random.uniform(0.05, 0.15)), int(income * random.uniform(0.15, 0.3))])
    welfare = int(income * random.uniform(0.05, 0.12))
    events = random.choice([0, int(income * random.uniform(0.02, 0.08))])
    total_expense = wages + military + construction + welfare + events
    balance = income - total_expense
    return {
        "income": income,
        "tax": tax,
        "trade": trade,
        "misc": misc,
        "wages": wages,
        "military": military,
        "construction": construction,
        "welfare": welfare,
        "events": events,
        "total_expense": total_expense,
        "balance": balance,
    }

# Project tracker
projects = [
    "城牆北段加固",
    "新城門建設",
    "灌溉渠道修復",
    "王國大道鋪設",
    "港口擴建",
    "皇城花園重整",
    "邊境哨站設立",
    "河道疏浚",
    "王國學校興建",
    "煉金塔改建",
    "皇家糧倉擴建",
    "水井系統更新",
    "城西市場重建",
    "燈火系統改造",
    "皇家書庫整修",
]


def gen_project_status(date: datetime):
    p = random.choice(projects)
    states = [
        "籌備中",
        "已發包",
        "動工",
        "進行中",
        "完成 30%",
        "完成 60%",
        "完成 90%",
        "驗收中",
    ]
    return p, random.choice(states)


def gen_military(date: datetime):
    """Random military note, not always present."""
    if random.random() < 0.25:
        cost = random.randint(80, 500)
        ops = random.choice([
            "邊境巡邏物資更新",
            "士兵薪資加發",
            "盔甲兵器補給",
            "戰馬購置",
            "砲彈庫存補強",
            "情報網維護",
            " fortification 修繕",
        ])
        return ops, cost
    return None, 0


def fmt_num(n: int) -> str:
    return f"{n:,}"


cash_prefix = "💰"


def write_day(date: datetime, idx: int):
    month_names = ["","正月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","十二月"]
    chinese_date = f"{date.year}年{month_names[date.month]}{date.day}日"
    eco = gen_economy(date)
    proj_name, proj_status = gen_project_status(date)
    mil_ops, mil_cost = gen_military(date)

    # Build dynamic events list based on random decisions
    day_events = []
    
    # Always include basic economic summary
    day_events.append(f"收入：{fmt_num(eco['income'])} 金幣")
    day_events.append(f"稅收：{fmt_num(eco['tax'])}，貿易：{fmt_num(eco['trade'])}，雜項：{fmt_num(eco['misc'])}")
    
    # Expense breakdown
    day_events.append(f"支出：{fmt_num(eco['total_expense'])} 金幣")
    day_events.append(f"- 工資：{fmt_num(eco['wages'])}")
    day_events.append(f"- 軍費：{fmt_num(eco['military'])}")
    if eco['construction'] > 0:
        day_events.append(f"- 建設：{fmt_num(eco['construction'])}")
    day_events.append(f"- 福利：{fmt_num(eco['welfare'])}")
    if eco['events'] > 0:
        day_events.append(f"- 突發事件：{fmt_num(eco['events'])}")
    
    # Balance
    balance_str = f"{fmt_num(eco['balance'])}（{'盈餘' if eco['balance'] >= 0 else '赤字'}）"
    day_events.append(f"結餘：{balance_str}")
    
    # Project
    day_events.append(f"建設：{proj_name} — {proj_status}")
    
    # Military
    if mil_ops:
        day_events.append(f"軍事：{mil_ops}，花費 {fmt_num(mil_cost)} 金幣")
    
    # Random story line
    story = random.choice([
        "今日王國風調雨順，百姓安居樂業。",
        "城內市場熱鬧非凡，商旅絡繹不絕。",
        "學堂傳來讀書聲，王國下一代正茁壯成長。",
        "港口船隻進出頻繁，海上貿易興隆。",
        "農夫們正忙於田間耕作，期待豐收。",
        "工匠們在工坊中敲敲打打，技藝日益精湛。",
        "宮廷夜宴燈火通明，貴族們觥籌交錯。",
        "边境騎士們巡邏回報，一切安寧。",
        "今日宮廷舉行詩會，文人墨客齊聚一堂。",
        "王上頒布新詔，鼓勵農耕與工商並重。",
    ])
    day_events.append(story)

    # Tomorrow plan
    plan = random.choice([
        "明日計畫：繼續推動農業振興方案。",
        "明日計畫：審核新城門藍圖。",
        "明日計畫：接見外邦使節。",
        "明日計畫：視察邊境哨站。",
        "明日計畫：舉辦全國技藝大會。",
        "明日計畫：研究煉金術新發現。",
        "明日計畫：籌備豐收祭典。",
        "明日計畫：更新王國法律條文。",
    ])
    day_events.append(plan)

    day_of_year = date.timetuple().tm_yday
    season = ""
    if date.month in [12, 1, 2]:
        season = "冬"
    elif date.month in [3, 4, 5]:
        season = "春"
    elif date.month in [6, 7, 8]:
        season = "夏"
    else:
        season = "秋"

    content = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📜 {date.strftime('%Y-%m-%d')} 王國日報</title>
  <link rel="stylesheet" href="/empire-chronicle/styles.css">
</head>
<body>
  <div class="page">
    <div class="topbar">
      <div></div>
      <a href="/empire-chronicle/">🏰 返回年鑑首頁</a>
    </div>
    <h1>{date.strftime('%Y-%m-%d')} · {season}季</h1>
    <h2>📜 王國日報</h2>
    <ul>
"""
    for ev in day_events:
        content += f"      <li>{ev}</li>\n"

    content += """    </ul>
    <hr>
    <p class="meta">第 """ + str(day_of_year) + """ 天</p>
    <blockquote>「國之強弱，在於每日積累。」</blockquote>
  </div>
</body>
</html>
"""
    return content


start = datetime(2025, 6, 27)
end = datetime(2026, 6, 25)
cur = start
idx = 0
while cur <= end:
    fname = cur.strftime('%Y-%m-%d') + '.html'
    (output_dir / fname).write_text(write_day(cur, idx), encoding='utf-8')
    cur += timedelta(days=1)
    idx += 1

print(f"✅ Generated {idx} daily reports with finances + projects")

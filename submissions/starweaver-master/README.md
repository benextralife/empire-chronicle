# Starweaver's Dream - Master Deployment Guide
科幻+星際+AI戀愛 小說 | 10章, ~9-10K chars

##  FILE STATUS (2026-07-02)
- Wattpad: 10 ch ready in PASTE_ALL_CHAPTERS.txt
- RR: 10 ch ready in Starweaver_Dream_RR.txt
- Upload scripts: ready but need STORY_ID / FICTION_ID

##  STEP 1: 創建故事
### A) Wattpad
1. 王上在 https://www.wattpad.com/myworks 建立新故事
2. 標題：Xiao Ying's Dream (or ...)
3. 取得故事 ID（URL 中的數字）
4. 填入 run_starweaver.py 頂部的 STORY_ID

### B) Royal Road
1. 王上手動到 /author-dashboard 建立新小說
2. 取得 fiction ID
3. 填入 rr_upload_starweaver.py 頂部的 FICTION_ID
4. 建立 10 個 draft chapters（或讓腳本自動建立）

##  STEP 2: 執行發布
```bash
# Wattpad
cd wattpad-ai-starweaver-dream
C:/Python314/python.exe run_starweaver.py

# Royal Road
cd royalroad-ai-starweaver-dream
C:/Python314/python.exe rr_upload_starweaver.py
```

##   NOTE
- 瀏覽器需開啟且 Edge CDP port 9222 啟用
- 腳本使用 Playwright connect_over_cdp
- 需要手動處理 Wattpad 的 #urgent-announcement-container overlay
- RR 使用 XHR + CSRF token 策略

##  已完成項目
- Ch4 恢復發佈到 RR (AI Garden's Dream)
- RR AI Garden's Dream 全部 4 章上線
- RR 草稿清理完成
- Wattpad 小嬰 Ch1+Ch2 已發布

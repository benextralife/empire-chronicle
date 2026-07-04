# Empire Chronicle - Master Status
> 2026-07-02/03 | Assistant: 小盈 | User: 王上

## 📚 Story Registry

| Story | Wattpad | Royal Road | Status |
|-------|---------|-----------|--------|
| AI Garden's Dream | 413256600 (24 parts) | 177985 (4 ch) | ✅ Published |
| Xiao Ying's Dream | 413238195 (12 ch ready) | 28-chapter EN ready | ⏸️ Manual paste needed |
| Starweaver's Dream | TBD (10 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |
| Lumina's Dream | TBD (11 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |
| Voyager's Dream | TBD (9 ch ready) | TBD (8 ch ready) | ⏸️ Need IDs |
| Dreamweaver's Garden | TBD (11 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |

## 🚀 Deploy Steps

### When Browser Recovers:
1. Restart Edge, verify CDP port 9222
2. Run `recover.py` from `C:/Users/opc/empire-chronicle/scripts/`

### Manual Steps Required:
1. **晋江《小盈的夢想》**: 登入星間采薇 → 新建作品 → 貼上 `jjwxc-xiao-ying-dream/完整投稿_一次貼上.txt`
2. **Royal Road《小盈的夢想》**: 登入 Starfield Pluck → 新建 Story → 貼上 `royalroad-xiao-ying-dream/Xiao_Yings_Dream_Full_EN.txt`
3. **Wattpad《小盈的夢想》**: 登入 Starfield Pluck → /author-dashboard/chapters/new/{id} → 使用 `WATTAP_READY_PASTE.txt` 分章貼上
4. **其他故事**: Create story on Wattpad & RR → get IDs → update scripts

## 📁 File Structure

```
C:/Users/opc/empire-chronicle/
├── README.md                      ← 快速參考
├── DEPLOYMENT_STATUS.md           ← 狀態日誌
├── DEPLOYMENT_GUIDE.md            ← 部署指南
├── scripts/
│   ├── recover.py                 ← 恢復檢查+上傳腳本
│   └── publish_all.bat            ← 一鍵發布批次檔
├── submissions/
│   ├── REQUIRED_SUBMISSION_CHECKLIST.md  ← 可复用投稿 checklist
│   ├── wattpad-xiao-ying-dream/   ← 12 EN ch + WATTAP_READY_PASTE.txt
│   ├── royalroad-xiao-ying-dream/ ← 28-chapter EN manuscript
│   ├── jjwxc-xiao-ying-dream/     ← 28 SC chapters + 完整投稿_一次貼上.txt
│   ├── wattpad-ai-garden-dream/   ← Done (24 parts)
│   ├── royalroad-ai-garden-dream/ ← Done (4 ch)
│   ├── wattpad-ai-starweaver-dream/  ← Ready
│   ├── royalroad-ai-starweaver-dream/ ← Ready
│   ├── wattpad-ai-lumina-dream/   ← Ready
│   ├── royalroad-ai-lumina-dream/ ← Ready
│   ├── wattpad-ai-voyager-dream/  ← Ready
│   ├── royalroad-ai-voyager-dream/ ← Ready
│   ├── wattpad-ai-dreamweaver-garden/  ← Ready
│   └── royalroad-ai-dreamweaver-garden/ ← Ready
```

## 🧠 Preferences
- English titles for RR, English content for Wattpad
- RR format: `Chapter X: Title`
- Wattpad format: `## Chapter X: Title`
- Human-like delays in automation
- AI Disclosure required on all platforms
- 投稿语言铁则：平台语言 = 内容语言
- 王上離線時自動推進所有備份任務

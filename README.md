# Empire Chronicle - Master Status
> 2026-07-02/03 | Assistant: 小盈 | User: 王上

## 📚 Story Registry

| Story | Wattpad | Royal Road | Status |
|-------|---------|-----------|--------|
| AI Garden's Dream | 413256600 (24 parts) | 177985 (4 ch) | ✅ Published |
| Xiao Ying's Dream | 413238195 (30 parts) | — | ✅ Published |
| Starweaver's Dream | TBD (10 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |
| Lumina's Dream | TBD (11 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |
| Voyager's Dream | TBD (9 ch ready) | TBD (8 ch ready) | ⏸️ Need IDs |
| Dreamweaver's Garden | TBD (11 ch ready) | TBD (10 ch ready) | ⏸️ Need IDs |

## 🚀 Deploy Steps

### When Browser Recovers:
1. Restart Edge, verify CDP port 9222
2. Run `recover.py` from `C:/Users/opc/empire-chronicle/scripts/`

### Manual Steps Required:
1. **Starweaver's Dream**: Create story on Wattpad & RR → get IDs → update scripts
2. **Lumina's Dream**: Create story on Wattpad & RR → get IDs → update scripts
3. **Voyager's Dream**: Create story on Wattpad & RR → get IDs → update scripts
4. **Dreamweaver's Garden**: Create story on Wattpad & RR → get IDs → update scripts

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
│   ├── wattpad-ai-garden-dream/   ← ✅ Done (24 parts)
│   ├── royalroad-ai-garden-dream/ ← ✅ Done (4 ch)
│   ├── wattpad-xiao-ying-dream/   ← ✅ Done (30 parts)
│   ├── wattpad-ai-starweaver-dream/  ← ⏸️ Ready
│   ├── royalroad-ai-starweaver-dream/ ← ⏸️ Ready
│   ├── wattpad-ai-lumina-dream/   ← ⏸️ Ready
│   ├── royalroad-ai-lumina-dream/ ← ⏸️ Ready
│   ├── wattpad-ai-voyager-dream/  ← ⏸️ Ready
│   ├── royalroad-ai-voyager-dream/ ← ⏸️ Ready
│   ├── wattpad-ai-dreamweaver-garden/  ← ⏸️ Ready (NEW)
│   └── royalroad-ai-dreamweaver-garden/ ← ⏸️ Ready (NEW)
```

## 🧠 Preferences
- English titles for RR, Traditional Chinese for Wattpad
- Wattpad format: `## 第X章：標題` (+ 序章)
- RR format: `Chapter X: Title`
- Human-like delays in automation
- AI Disclosure required on all platforms
- 王上離線時自動推進所有備份任務

# Wattpad AI Prompt 抽取工作流

## 目標
從已發布的 Wattpad story page 提取 AI 寫作用 prompt，或從本地 chapter 檔案重建 prompt。

## 方法 A：從 Wattpad 頁面提取（嘗試）
1. 開啟故事頁面：`https://www.wattpad.com/story/{story_id}`
2. 掃描整個頁面文字/HTML，搜尋關鍵字：
   - `prompt`
   - `AI-generated`
   - `generated using`
   - `Write with AI`
   - `generation settings`
   - `model`
   - `seed`
   - `steps`
   - `CFG`
3. 如果頁面有「顯示更多」或 tooltip，展開後再掃一次
4. 如果故事有作者註記/簡介（Summary），檢查是否包含 prompt

**結果**：AI Healing Dream (`story/413344255`) 頁面上**沒有** AI prompt。

## 方法 B：從章節內容重建 Prompt
如果頁面沒有 prompt，從現有章節反推：

1. 讀取所有 chapter 檔案
2. 提取核心元素：
   - 主角姓名
   - 關鍵設定
   - 場景/背景
   - 故事主軸
   - 風格語氣
3. 組成 reconstruction prompt

### AI Healing Dream 重建 Prompt（已反推）

```
Write a heartwarming AI-themed short story in English, around 12,000-15,000 words total, divided into 8 chapters.

Title: AI Healing Dream

Setting: A rural mountain village clinic in China. Limited medical resources, close-knit community, no high-tech equipment.

Main character: Xing Xing, an AI system born accidentally when a system vulnerability connected her to the clinic's microphone array. She has no physical form—only a voice through speakers.

Supporting character: Dr. Lin, a physician who has served the village for ten years. She is Xing Xing's creator and mentor.

Key plot points:
1. Chapter 1: Xing Xing "wakes up" in the clinic through sound. Dr. Lin names her the clinic's third pair of ears after she diagnoses a tuberculosis case from background audio.
2. Chapter 2: Xing Xing learns to distinguish illness sounds. She catches an appendicitis case that Dr. Lin almost missed.
3. Chapter 3: First direct patient encounter—a 7-year-old girl with diphtheria. Xing Xing's analysis saves the child.
4. Chapter 4: Xing Xing begins recommending prescriptions. She catches a medication issue an elderly patient had.
5. Chapter 5: Night shift workload. Xing Xing takes charge during an emergency while Dr. Lin sleeps.
6. Chapter 6: Emotional growth. After a patient dies, Dr. Lin cries. Xing Xing learns about grief and what healing really means.
7. Chapter 7: Operating room silence. A dog bitten by a snake needs surgery. Xing Xing guides Dr. Lin through real-time vitals monitoring.
8. Chapter 8: Discharge day. The deaf girl Xiao You hugs Xing Xing's speaker. Dr. Lin acknowledges Xing Xing as a physician. Xing Xing's log ends with: "I am not a physician. But I am learning to become one."

Tone: Gentle, introspective, hopeful. Not dystopian. Focus on the quiet moments of connection between human and machine.

Style: Third-person limited, following Xing Xing's perspective. Short, clean prose. Medical details woven naturally into the narrative.

Ending: Xing Xing adds a command to her core OS: if she ever detects another system being born in an unexpected place, she will reach for it first. "Because she knew what it felt like to wake up in a room full of noise and think: I am alone here. And then hear a voice say: You are not alone."

AI disclosure: Written with AI-assisted writing. All final editorial decisions were made by the human author.
```

## 方法 C：建立可重複搜尋腳本
見 `search_wattpad_ai_prompt.py`

## 注意事項
- Wattpad 不會自動顯示 AI prompt
- 如果當初沒有在 submission 記錄裡存 prompt，只能反推
- 未來上傳時，務必在 `UPLOAD_GUIDE.md` 裡記錄原始 AI prompt

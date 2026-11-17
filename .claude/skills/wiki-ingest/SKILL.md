---
name: wiki-ingest
description: 將 raw/ 中的來源（論文 PDF、README）讀入並整合進推薦演算法 wiki。用於「ingest」「讀入」「處理這篇」「跑批次 1/2/3」等請求。含頁面範本與逐步檢查清單。
---

# wiki-ingest

先確認已讀過 `AGENTS.md`。raw/ 唯讀。

## A. 批次模式（首次建置）

批次定義見 AGENTS.md §3。對每一批：

1. **讀**：逐份完整閱讀該批來源。PDF 頁數多時分段讀（Read 工具 `pages` 參數，每次 ≤20 頁）；需要擷取文字時輸出到 scratchpad，不寫進 raw/。
   - 讀的同時記筆記：核心問題、方法、關鍵數字（附 PDF 頁碼）、限制、與其他來源的關聯。
2. **source 頁**：每份寫一頁 `wiki/sources/<slug>.md`（範本見 C1）。
3. **交叉整合**：列出該批涉及的概念與實體 → 查 index.md 是否已有頁 → 有則更新、無則新建（範本 C2/C3）。同批來源互相比較時寫 synthesis 頁（C4）。
4. **教學素材**：為本批最關鍵的 2–4 個概念寫/補 teaching 頁（C5）。
5. **glossary**：新術語加入 `wiki/glossary.md`。
6. **index.md**：同步所有新增/修改頁。
7. **log.md**：追加一筆 `## [日期] ingest | 批次 N：<主題>`，列出所有新增/修改頁與待決問題。
8. **lint**：依 wiki-lint skill 執行並修正。
9. **回報人類**：變更摘要（新增幾頁、哪些重點、哪些爭議、哪些 wiki 觀點需要人類過目），**停下來等確認**。

## B. 單篇模式（之後新增來源）

1. 確認人類已把檔案放進 raw/；把 MD5 追加到 `.raw-manifest.md5`（`md5 -r raw/<file>` 的輸出格式：`<hash> raw/<file>`）。
2. 完整閱讀。
3. **先跟人類討論**：列 3–5 個重點、它和現有 wiki 的關係（補強／衝突／全新），問要強調什麼。等回覆。
4. 依回覆執行 A 的步驟 2–8，並更新 AGENTS.md §3 的來源清單（記 log `schema`）。

## C. 頁面範本

### C1 source（`wiki/sources/<slug>.md`）

```markdown
---
type: source
title: <論文/文件標題>
raw: raw/<檔名>
authors: <作者，過多時寫第一作者 et al.>
year: <年>
venue: <會議/期刊/arXiv/GitHub/unknown>
sources: [<自己的 slug>]
updated: YYYY-MM-DD
---

# <中文短標題>（<英文原名>）

**一句話**：<這份來源最重要的一句話，給大學生看得懂>

## 背景：它想解決什麼問題
## 核心做法
## 關鍵數字與結果
- <數字>（p.N）— <實驗條件；註明為作者報告>
## 限制與注意事項
## 與其他來源的關係
- 補強/對照/衝突：[[sources/…]] — <說明>
## 相關頁面
- [[concepts/…]]、[[entities/…]]
```

### C2 concept（`wiki/concepts/<slug>.md`）

```markdown
---
type: concept
title: <中文（English）>
sources: [...]
updated: YYYY-MM-DD
---

# <中文（English）>

**一句話定義**：…

## 白話解釋
<至少一個生活比喻；給非資訊系也懂>

## 為什麼需要它
## 怎麼運作
<可附 mermaid 流程圖或簡單公式＋文字說明>

## 在各來源中的樣貌
- [[sources/…]]：…（p.N）

## ⚠️ 爭議（若有，格式見 AGENTS.md §8）

## 相關
- [[concepts/…]]、[[teaching/…]]
```

### C3 entity（`wiki/entities/<slug>.md`）

```markdown
---
type: entity
title: <名稱>
sources: [...]
updated: YYYY-MM-DD
---

# <名稱>

**是什麼**：<平台/系統/公司，一句話>

## 推薦系統的公開資訊
## 時間線（若適用）
## 相關研究／爭議
## 相關
```

### C4 synthesis（`wiki/syntheses/<slug>.md`）

```markdown
---
type: synthesis
title: <問題或比較主題>
sources: [...]
origin: ingest | query      # 由何產生
updated: YYYY-MM-DD
---

# <標題>

**結論摘要**：<3 行內>

## 比較／證據整理
| 面向 | 來源 A | 來源 B |
|---|---|---|

## 🧭 wiki 觀點
<明確標示為綜合判斷，附理由>

## 尚未解決的問題
```

### C5 teaching（`wiki/teaching/<slug>.md`）

```markdown
---
type: teaching
title: <主題>
sources: [...]
concepts: [<對應的 concept slug>]
updated: YYYY-MM-DD
---

# <主題>

## 比喻
## 常見迷思 vs. 事實
| 迷思 | 事實（出處） |
## 課堂例子／互動點子
## 可上簡報的圖解構想
```

### glossary 每列格式

`| 術語 | English | 一句白話 | [[concepts/…]] |`，依中文筆畫或注音排序皆可，但要一致（預設依英文字母排序）。

## D. 完成檢查

- [ ] 每份來源有 source 頁，frontmatter 齊全
- [ ] 數字/結果/引述都有頁碼或章節
- [ ] 新 concept 頁都有「白話解釋」
- [ ] 爭議有標示且 wiki 觀點分開
- [ ] index.md、glossary.md、log.md 已更新
- [ ] raw/ 無任何變動

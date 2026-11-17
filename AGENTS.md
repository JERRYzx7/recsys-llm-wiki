# AGENTS.md — 推薦演算法 LLM Wiki 規則

主題：**推薦演算法：短影音與社群平台如何決定你看什麼**。
本檔是 wiki 的 schema（規則總綱）。細部流程拆在 `.claude/skills/`，執行對應操作前**必須先讀該 skill**。

## 1. 角色分工

- **人類**：挑選來源、決定重點、提問、確認每批成果。
- **LLM**：閱讀來源、撰寫與維護 wiki 所有頁面、交叉連結、標註出處與爭議、記錄 log、跑 lint、產出簡報。
- 人類原則上不手寫 wiki；若人類手改了頁面，LLM 視為正確並據以同步其他頁面。

## 2. 三層架構與目錄

```
my-wiki/
├── AGENTS.md / CLAUDE.md     ← schema（CLAUDE.md 只有 @AGENTS.md）
├── .claude/skills/           ← wiki-ingest / wiki-lint / wiki-slides
├── raw/                      ← 原始來源（唯讀！）
├── .raw-manifest.md5         ← raw/ 的 MD5 清單，lint 用
├── wiki/                     ← LLM 維護的知識庫
│   ├── index.md  log.md  glossary.md
│   ├── sources/  concepts/  entities/  syntheses/  teaching/
└── output/                   ← 產出物（簡報），不屬於 wiki
```

### 🚫 raw/ 鐵則

- `raw/` **只能讀，絕對不能新增、修改、刪除、移動、重新命名**其中任何檔案。
- 需要轉檔或擷取文字時，輸出到暫存目錄（scratchpad），不要寫進 `raw/`。
- 新來源由**人類**放進 `raw/`；放入後 LLM 才可把它的 MD5 加進 `.raw-manifest.md5`（只能新增，不能改已存在的行）。

## 3. 來源清單（目前 10 份）

| 檔案 | 來源頁 | 批次 |
|---|---|---|
| 01-tiktok-foryou.pdf | sources/tiktok-foryou | 1 工業界技術 |
| 02-youtube-dnn-2016.pdf | sources/youtube-dnn-2016 | 1 |
| 03-monolith.pdf | sources/monolith | 1 |
| 06-x-algorithm.md | sources/x-algorithm | 1 |
| 04-hstu.pdf | sources/hstu | 2 生成式推薦 |
| 05-onerec.pdf | sources/onerec | 2 |
| 07-milli-2025.pdf | sources/milli-2025 | 3 社會影響 |
| 08-guess-2023.pdf | sources/guess-2023 | 3 |
| 09-haroon-2023.pdf | sources/haroon-2023 | 3 |
| 10-tiktok-transparency.pdf | sources/tiktok-transparency | 單篇（2026-11-17 新增） |

## 4. 讀者與深度

- 最終讀者：**完全不熟推薦系統的大學生**。
- **wiki 深度**：假設讀者是「修過程式、沒學過 ML 的資訊/理工系學生」。ML 術語首次出現必須解釋；可用流程圖與少量概念性公式，但公式旁一定要有文字說明。
- **簡報深度**：再降一級，給非資訊系也聽得懂；以比喻為主，盡量不出現公式。
- 內容需同時涵蓋 **技術面**（系統怎麼運作）與 **社會影響面**（極化、過濾泡泡、使用者福祉、平台誘因等）。

## 5. 語言與命名

- 內文：**繁體中文**（台灣用語）。專有名詞首次出現附英文，如「召回（retrieval）」、「嵌入向量（embedding）」。
- 檔名／資料夾：**英文 kebab-case**，如 `concepts/two-tower-model.md`。
- 連結：Obsidian wikilink，**一律寫從 wiki/ 起算的路徑、不含 .md**：`[[concepts/retrieval]]`、`[[concepts/retrieval|召回]]`、`[[sources/hstu#實驗結果]]`。
- 一頁只講一個主題；同一概念不得出現兩個頁面（先查 index.md）。

## 6. 頁面類型

| type | 位置 | 用途 |
|---|---|---|
| source | `wiki/sources/` | 每份 raw 一頁：書目資訊、一句話重點、核心貢獻、方法、關鍵數字、限制、與其他來源的關係 |
| concept | `wiki/concepts/` | 概念：定義、白話解釋/比喻、運作方式、在各來源中的樣貌、爭議 |
| entity | `wiki/entities/` | 平台／系統／公司（TikTok、YouTube、X、Meta、快手、字節…） |
| synthesis | `wiki/syntheses/` | 跨來源比較、爭議專頁、值得保存的 query 答案 |
| teaching | `wiki/teaching/` | 教學素材：比喻、常見迷思、課堂例子、可上簡報的圖解構想 |
| glossary | `wiki/glossary.md` | 單頁詞彙表：術語｜英文｜一句白話｜連結 |

### 必要 frontmatter（每個 wiki 頁面，index.md / log.md 除外）

```yaml
---
type: concept            # source | concept | entity | synthesis | teaching | glossary
title: 召回（Retrieval）
sources: [youtube-dnn-2016, x-algorithm]   # 引用到的來源頁 slug；無則 []
updated: 2026-11-17
---
```

source 頁另加：`raw: raw/04-hstu.pdf`、`authors`、`year`、`venue`（未知寫 unknown）。
各類頁面的完整範本在 `.claude/skills/wiki-ingest/SKILL.md`。

## 7. 出處規則

- **數字、實驗結果、直接引述**：必須標到頁碼或章節：`（[[sources/hstu]], §3.2）`、`（[[sources/guess-2023]], p.5）`。
- 一般背景敘述：標到來源即可：`（[[sources/monolith]]）`。
- Markdown 來源（如 X README）用章節標題：`（[[sources/x-algorithm]], #Ranking）`。
- PDF 頁碼以 **PDF 檔案頁碼** 為準；若與論文印刷頁碼不同，在 source 頁註明。
- 直接引述保留英文原文，後附中文翻譯。
- 不確定出處的說法不得寫入；LLM 自身背景知識若必要，須標 `（背景知識，非本 wiki 來源）`，且不得用於數字。

## 8. 矛盾與觀點

來源說法不一致時：

1. 在相關 concept/entity 頁加入區塊：

   ```markdown
   > [!warning] ⚠️ 爭議：<一句話描述>
   > - 說法 A：…（[[sources/x]], p.N）— 條件：平台/時間/樣本/方法
   > - 說法 B：…（[[sources/y]], §N）— 條件：…
   >
   > **🧭 wiki 觀點**：目前證據較支持…，理由…（此為 wiki 綜合判斷，非來源主張）
   ```

2. 重大爭議另開 `wiki/syntheses/<topic>.md` 專頁，並從相關頁連結過去。
3. **來源主張與 wiki 觀點必須明確分開**；wiki 觀點一律以「🧭 wiki 觀點」標示。
4. 不同研究條件（平台、年份、國家、實驗 vs. 觀察）造成的差異要明說，不要假裝是直接矛盾。
5. 新來源推翻舊說法時，舊說法不刪除，改標「已被 [[sources/…]] 修正」並說明。

## 9. 操作流程

### Ingest（讀 `.claude/skills/wiki-ingest/SKILL.md`）

- **首次建置分三批**：批次 1（01, 02, 03, 06）→ 批次 2（04, 05）→ 批次 3（07, 08, 09）。
  每批完成後：跑 lint → 向人類回報變更摘要與待決問題 → **等人類確認再進下一批**。
- **之後新增單篇**：先讀完 → 與人類討論 3–5 個重點、問要強調什麼 → 再寫入。
- 每次 ingest 必做：寫/更新 source 頁 → 更新或新建相關 concept/entity/synthesis/teaching 頁 → 更新 glossary → 更新 index.md → 追加 log.md。

### Query

1. 先讀 `wiki/index.md` 找相關頁，再讀頁面；wiki 不足時才回 raw/ 查，並考慮把查到的補進 wiki。
2. 回答需附 wikilink 出處。
3. 若答案有保存價值（比較、分析、新連結），**自行存成 `wiki/syntheses/` 新頁**，更新 index、記 log，並告訴人類存了哪頁。

### Lint（讀 `.claude/skills/wiki-lint/SKILL.md`）

- 時機：**每批 ingest 完**、**產簡報前**、人類要求時。
- 結構檢查跑 `python3 .claude/skills/wiki-lint/scripts/lint.py`；內容檢查由 LLM 判讀。
- 結果與修正記入 log.md。

### 產出簡報（讀 `.claude/skills/wiki-slides/SKILL.md`）

- 產出到 `output/`，單一自足 HTML（內嵌 CSS/JS、不依賴網路），含可切換的講者備忘。
- **只從 wiki 取材**，不直接讀 raw；發現 wiki 缺內容時先補 wiki 再做簡報。
- 產前先跑 lint。

## 10. index.md 與 log.md

- **index.md**：內容目錄，依類型分節（Sources / Concepts / Entities / Syntheses / Teaching / Glossary）。每行：`- [[path]] — 一句話摘要（來源數 N）`。每次新增/刪除/改名頁面都要同步。
- **log.md**：**只能往後追加**，不改舊紀錄。每筆格式：

  ```markdown
  ## [YYYY-MM-DD] <ingest|query|lint|slides|schema> | <標題>
  - 變更：新增/修改了哪些頁
  - 備註：待決問題、爭議、下一步
  ```

  可用 `grep "^## \[" wiki/log.md | tail -5` 看最近紀錄。

## 11. 寫作品質

- 每個 concept 頁必須有「白話解釋」小節（含至少一個比喻），供簡報降級使用。
- 先講「為什麼需要」再講「怎麼做」；避免照抄論文摘要。
- 相關頁要互相連結；新頁至少要有一個非 index 的頁面連進來（避免孤兒頁）。
- 不誇大：論文自述的成效（如「提升 X%」）要寫明是「論文作者報告」及其實驗條件。

## 12. Git

- `my-wiki/` 是獨立 git repo。**未經人類同意不 commit、不 push。**
- 建議每批 ingest 確認後由人類決定 commit。

## 13. 修改本 schema

- 人類與 LLM 可共同調整本檔；修改後在 log.md 記一筆 `schema`。
- 本檔需維持在 12,000 字元以內；細節寫進 skills。

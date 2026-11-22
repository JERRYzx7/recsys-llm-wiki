---
title: 執行紀錄｜一次完整執行
description: 2026-11-17 從空白到 49 頁 wiki 與 28 頁簡報的完整執行與檢查紀錄。
---

# 執行紀錄

以下整理自 [[log|wiki/log.md]]。log 只能往後追加，不能改舊紀錄，所以這份紀錄就是當時實際發生的事。

## 一眼看完

| 項目 | 結果 |
|---|---|
| 執行日期 | 2026-11-17（建 wiki 與簡報）；2026-11-22（重跑檢查、建網站） |
| 來源 | 10 份：9 份 PDF、1 份 GitHub README |
| ingest | 4 輪：批次 1 → 單篇 10 → 批次 2 → 批次 3 |
| wiki 頁數 | 29 → 32 → 41 → **49 頁**（10 sources、20 concepts、6 entities、4 syntheses、6 teaching、glossary、index、log） |
| lint | 6 次；內容檢查總共補了 **23 處缺漏的頁碼** |
| 簡報 | **28 頁**，每頁都有講者備忘與出處 |
| 簡報對 wiki 的追溯 | 簡報上 32 個數字，**32 個都能在 wiki 找到**（2026-11-22 檢查） |

## 時間線

| # | 節點 | 做了什麼 | 結果 |
|---|---|---|---|
| 1 | 0 規則 | 建立 `AGENTS.md`、3 個 skill、`lint.py`；登記 9 份 raw 的 MD5 | 決定分三批 |
| 2 | 1–6 批次 1 | YouTube 2016、Monolith、TikTok 2020、X README | 新增 26 頁：4 sources、13 concepts、4 entities、2 syntheses、3 teaching；術語 27 個 |
| 3 | 7–8 lint | 結構 5 項 OK（29 頁）；內容抓到問題 | 補 7 處頁碼、「追蹤」爭議改成標準格式、補 3 處 🧭 標記、修 3 個表格內的別名連結 |
| 4 | 2 單篇 10 | **先跟人類討論 5 個重點** | 人類指示：要有趣一點、新增 user-controls 頁、raw 檔改名 |
| 5 | 3–6 單篇 10 | TikTok 官方說明頁 | 新增 3 頁，更新 13 頁；修正迷思 #1 |
| 6 | 7 lint | 第 5 項不通過：raw 檔還沒改名，MD5 未登記 | **檢查不過 → 停下等人類** |
| 7 | 7 lint | 人類改名後補登記 MD5 | 5 項 OK（32 頁） |
| 8 | 1–6 批次 2 | HSTU、OneRec（PDF 超過 20 頁，抽文字分段讀） | 新增 9 頁；處理批次 1 留下的待辦（Transformer 建頁） |
| 9 | 7–8 lint | 結構 OK（41 頁） | 補 7 處頁碼 |
| 10 | 9 確認 | 人類決定：「漏斗 vs. 端到端」在簡報只用一頁 | 寫回 [[syntheses/cascade-vs-end-to-end]] |
| 11 | 1–6 批次 3 | Guess 2023、Milli、Haroon 2023 | 新增 8 頁，含核心整合頁 [[syntheses/do-algorithms-polarize]] |
| 12 | 7–8 lint | 結構 OK（49 頁） | 補 9 處頁碼、新增 2 個 ⚠️ 爭議區塊 |
| 13 | 10 簡報前 lint | 結構 OK | 沒有新頁面，內容沿用上次結果 |
| 14 | 11–13 簡報 | 人類要求「不要太 AI 美感」→ 改成「老師批改考卷」風格 | 28 頁 HTML |
| 15 | 14 驗證 | headless Chrome 截圖 28 頁 × 深色、淺色、600px 寬 | 抓到 3 個問題並修正（見下） |

## 檢查紀錄

### lint（節點 7、8、10）

| 時機 | 頁數 | 結構檢查（腳本） | 內容檢查（LLM） |
|---|---|---|---|
| 批次 1 後 | 29 | <span class="badge ok">5/5 OK</span> | 缺頁碼 **7**、爭議格式 1、缺 🧭 標記 3、表格別名連結 3；缺頁概念 3 個（Transformer 留到批次 2） |
| 單篇 10 後 | 32 | <span class="badge warn">4/5</span> raw 完整性 1 個問題 | — |
| raw 改名後 | 32 | <span class="badge ok">5/5 OK</span> | — |
| 批次 2 後 | 41 | <span class="badge ok">5/5 OK</span> | 缺頁碼 **7**；白話解釋、🧭、表格連結都沒問題 |
| 批次 3 後 | 49 | <span class="badge ok">5/5 OK</span> | 缺頁碼 **9**；新增 2 個爭議區塊 |
| 簡報前 | 49 | <span class="badge ok">5/5 OK</span> | 沒有新頁，沿用 |
| 2026-11-22 重跑 | 49 | <span class="badge ok">5/5 OK</span> | — |

2026-11-22 重跑的實際輸出：

```text
$ python3 .claude/skills/wiki-lint/scripts/lint.py
wiki 頁面數：49
[1 斷鏈] OK
[2 孤兒頁] OK
[3 index 不一致] OK
[4 frontmatter] OK
[5 raw 完整性] OK

總計問題：0
```

### 簡報驗證（節點 14）

| 檢查 | 發現 | 處理 |
|---|---|---|
| 截圖 28 頁 × 深色／淺色／600px 寬 | CSS 權重衝突，出處和頁碼的字被放大 | 修正選擇器 |
| 同上 | 圖表標籤重疊 | 調整位置 |
| 同上 | 參考資料頁文字溢出 | 調整版面 |
| 模擬按鍵：翻頁、逐步揭曉、備忘、主題切換 | 沒有 JS 錯誤 | — |
| 講者備忘 | 28 頁都有 | — |

### 簡報 ↔ wiki 追溯檢查（2026-11-22 補做）

用腳本把簡報每一頁的數字（百分比、小數、「數百萬」「十億」等）抓出來，在 `wiki/` 全文搜尋：**32 個數字，0 個找不到**。例如第 21 頁的「不可信來源多 68.8%」出現在 [[sources/guess-2023]]、[[syntheses/do-algorithms-polarize]]、[[teaching/myths-and-facts]]。

## 簡報每一頁取材自哪些 wiki 頁

| 頁 | 內容 | 主要取材 |
|---|---|---|
| 1–2 | 封面、今天的三個問題 | [[index]] |
| 3 | 東西太多了 | [[sources/youtube-dnn-2016]]、[[sources/tiktok-transparency]] |
| 5 | 像選秀節目：一關一關淘汰 | [[teaching/funnel-analogy]]、[[concepts/recommendation-funnel]] |
| 6 | TikTok 官方的五個步驟 | [[sources/tiktok-transparency]]、[[concepts/recommendation-funnel]] |
| 7 | 你的每個動作都是一張選票 | [[teaching/what-the-feed-learns-from-you]]、[[concepts/implicit-feedback]] |
| 8 | 猜猜看 TikTok 會預測什麼 | [[teaching/guess-the-signal]] |
| 9 | 「第三支影片」 | [[concepts/collaborative-filtering]] |
| 10 | 把預測加起來就是分數 | [[concepts/optimization-objective]]、[[sources/x-algorithm]]、[[teaching/myths-and-facts]] |
| 11 | 它想衝高的數字一直在變 | [[concepts/optimization-objective]]、[[sources/youtube-dnn-2016]] |
| 12 | 刻意加進來的多樣性 | [[concepts/diversity-and-exploration]] |
| 13 | 不是什麼都能被推薦 | [[concepts/visibility-filtering]] |
| 14 | 它學得有多快 | [[concepts/online-training]]、[[sources/monolith]]、[[entities/bytedance]] |
| 15 | 從選擇題變成申論題 | [[concepts/generative-recommendation]]、[[syntheses/cascade-vs-end-to-end]]、[[teaching/autocomplete-analogy]] |
| 17 | 它量不到你開不開心 | [[concepts/optimization-objective]]、[[sources/onerec]] |
| 18 | 你會點的不等於你想要的 | [[concepts/engagement-vs-stated-preference]]、[[sources/milli-2025]] |
| 19 | Twitter：演算法放大了憤怒 | [[sources/milli-2025]]、[[concepts/polarization]] |
| 20–21 | Facebook 改回時間序 | [[sources/guess-2023]] |
| 22 | YouTube 假帳號稽核 | [[sources/haroon-2023]]、[[concepts/algorithmic-audit]]、[[concepts/filter-bubble]] |
| 23 | 三篇研究怎麼拼在一起 | [[syntheses/do-algorithms-polarize]] |
| 24 | 五分鐘辯論 | [[teaching/chronological-feed-debate]] |
| 25 | 迷思與事實 | [[teaching/myths-and-facts]] |
| 26 | 你可以怎麼做 | [[concepts/user-controls]] |
| 27–28 | 帶走三句話、參考資料 | [[syntheses/do-algorithms-polarize]]、全部 10 個 source 頁 |

（第 4、16 頁是章節分隔頁。）

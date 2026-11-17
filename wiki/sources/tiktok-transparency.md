---
type: source
title: Introduction to the TikTok recommendation system（Policies & engagement）
raw: raw/10-tiktok-transparency.pdf
authors: TikTok（官方，未具名）
year: 2025
venue: TikTok 官方網站 Policies & engagement 頁（頁尾 © 2025，無更新日期；PDF 為 2026-11-17 網頁列印）
sources: [tiktok-transparency]
updated: 2026-11-17
---

# TikTok 官方：推薦系統介紹（Introduction to the TikTok recommendation system）

**一句話**：TikTok 官方對 For You 的「第二版說明」。它第一次把推薦流程拆成五個步驟，也列出系統會預測的十多種行為。整體來說，TikTok 的做法和 YouTube、X 的推薦漏斗是同一套邏輯。

> 頁碼說明：PDF 共 14 頁。p.1–2 是標題與導覽列；正文在 p.2–13；p.12 有一張流程圖；p.14 是頁尾。
> 網址：`tiktok.com/safety/en/policies-and-engagement/recommendation-system`（p.1 頁尾）。

## 背景：它想解決什麼問題

- 說明推薦系統怎麼運作，以及安全措施和使用者能用的工具。
- TikTok 自稱每月有**超過十億人**使用（p.2）。

**五個設計原則**（p.3）：
1. 給廣大受眾（特別是青少年）安全的體驗。
2. 尊重在地脈絡與文化規範。
3. **內容中立**：推薦系統對所有社群包容，對推薦的內容保持中立。
4. 鼓勵原創與創意表達。
5. 推廣多元內容和主題，讓使用者探索新內容。

## 核心做法：五個步驟（p.6–8）

1. **挑選影片（Selecting videos）**：從「已通過初步審核、符合推薦資格」的影片中撈出大量候選（p.7）。
2. **預測（Predicting）**：估計你對每支影片做出各種反應的機率，例如按讚、分享、留言、略過，再**合成一個總分**（p.7）。
3. **排序（Ranking）**：依總分由高到低排列（p.7）。
4. **相似度檢查（Similarity check）**：
   - 如果排在前面的影片彼此太像，例如**用同一段配樂**，就換掉一些，增加多樣性（p.8）。
   - 目的是降低看到重複主題的機會，幫你探索不同類型的內容（p.8）。
5. **推薦規則（Recommendation rules）**：在各個步驟套用額外的規則（p.8），例如：
   - 推薦頁一定會包含**同地區創作者**的內容。
   - **未滿 16 歲帳號**做的內容不會被推薦。

**p.12 的流程圖**：所有上傳的影片 → 審核（移除違規影片、移除較舊的影片）→ 符合資格的影片池（**數百萬**支）→ 挑選後剩**數千**支 → 依預測分數排序 → 套用推薦規則、檢查相似度與多樣性 → For You 頁。

## 訊號與預測（附錄，p.12–13）

**你的訊號**（p.12–13）：
- 地區（用來對齊當地標準與文化規範）
- 裝置語言、作業系統
- 最近互動過的影片：看了、**看完**、按讚、**略過**
- **你在 TikTok 上的追蹤關係**

**系統會預測你做出這些行為的機率**（p.13）：
- 按讚、分享、留言、標記「不感興趣」
- 追蹤作者、和作者的個人頁互動
- 看完、略過、收藏
- **觀看達到一定時間**
- **點擊影片的配樂**

**影片的訊號**（p.13）：發布時間、發布地區、作者的語言設定、配樂、影片長度、hashtag。

**別人的行為也有影響**（p.5）：
> "if another user has engaged with two of the same videos that you have interacted with, the system may predict that you are likely to also engage with a third video that this user has interacted with."
> （如果另一位使用者和你互動過同樣兩支影片，系統可能預測你也會和他互動過的第三支影片互動。）

這就是[[concepts/collaborative-filtering|協同過濾]]的白話版本。

## 安全與青少年保護（p.9–10）

- **新上傳的影片都要先審核**：機器學習加上人工審核，違反社群守則的影片會被刪除，「不適合廣大受眾」的影片則**不符合推薦資格**（p.9）。
- **13–17 歲帳號**在 TikTok 任何地方都看不到明顯的成人內容（p.10）。
- **未滿 16 歲帳號**做的內容不會被推上 For You（p.10；p.8 也有提到）。

## 使用者控制（p.11）

- **不感興趣**：長按影片，系統會減少推薦這類內容。
- **影片關鍵字過濾**：把特定字詞或 hashtag 從 For You 濾掉。
- **重設 For You（For You refresh）**：讓你探索「全新的 TikTok」。

## 關鍵數字與結果

- 每月使用者「超過十億」（p.2，平台自述）。
- 流程圖上的規模：符合資格的影片「數百萬」支 → 挑選後「數千」支（p.12）。
- 年齡門檻：未滿 16 歲的內容不推薦；13–17 歲看不到明顯成人內容（p.10）。
- **沒有公開權重、模型架構，也沒有成效數據。**

## 限制與注意事項

- **平台自述**，沒有外部驗證。頁面沒有更新日期，只有 © 2025。
- **沒有說明各種預測怎麼合成總分**，也就是權重。這點不如 X 公開得多（[[sources/x-algorithm]], #Scoring and Ranking）。
- 「內容中立」是平台自己宣稱的原則，是否做到需要獨立研究檢驗，待批次 3 補充。
- 這份文件的網址在 `/safety/` 底下，性質偏向政策說明，不是技術文件。

## 與其他來源的關係

- **更新** [[sources/tiktok-foryou]]（2020）：
  - 兩份都有：「不感興趣」、不連續推同一段配樂、安全上不符推薦資格的內容。
  - 新版多了五步驟流程、預測行為清單、未滿 16 歲規則、同地區規則、關鍵字過濾、重設 For You。
  - 新版**沒有再提**「追蹤數不是直接因素」，而是把「你的追蹤關係」列為訊號（p.13）。見 [[syntheses/platform-pipeline-comparison]] 的爭議區塊。
- **和 X 高度相似** [[sources/x-algorithm]]：同樣是「預測多種行為 → 合成分數 → 排序 → 多樣性調整 → 規則過濾」。差別在 X 公開了權重和程式碼。
- **漏斗規模和 YouTube 一致** [[sources/youtube-dnn-2016]]：都是從數百萬縮小（p.2）。

## 相關頁面

- [[entities/tiktok]]、[[concepts/recommendation-funnel]]、[[concepts/optimization-objective]]、[[concepts/diversity-and-exploration]]、[[concepts/visibility-filtering]]、[[concepts/user-controls]]、[[teaching/guess-the-signal]]

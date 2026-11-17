---
type: teaching
title: 推薦演算法的常見迷思與事實
sources: [tiktok-foryou, youtube-dnn-2016, monolith, x-algorithm, tiktok-transparency, hstu, onerec, guess-2023, milli-2025]
concepts: [optimization-objective, filter-bubble, diversity-and-exploration, visibility-filtering]
updated: 2026-11-17
---

# 推薦演算法的常見迷思與事實

> 這一頁會隨著每批 ingest 持續增加。目前根據批次 1（工業界技術）、TikTok 新版說明頁（[[sources/tiktok-transparency]]）和批次 2（生成式推薦）、批次 3（社會影響）。辯論素材見 [[teaching/chronological-feed-debate]]。更多互動遊戲見 [[teaching/guess-the-signal]]。

## 常見迷思 vs. 事實

| # | 迷思 | 事實（出處） |
|---|---|---|
| 1 | 「粉絲多的人一定會被推更多」 | TikTok 2020 說創作者的粉絲數不是直接因素，但承認粉絲多的人自然可能獲得更多觀看（[[sources/tiktok-foryou]], p.2）。不過「**你**追蹤了誰」是 TikTok 新版說明列出的訊號（[[sources/tiktok-transparency]], p.13）。X 則有「新作者加成」（[[sources/x-algorithm]], #Scoring and Ranking）。各平台不同 |
| 2 | 「演算法只想要你點進去」 | YouTube 在 2016 年就改用觀看時間，因為點擊率會助長標題黨（[[sources/youtube-dnn-2016]], p.5）。X 預測十多種行為（[[sources/x-algorithm]], #Scoring and Ranking） |
| 3 | 「X 的一次檢舉等於抵銷 468 個讚」 | 錯誤。權重乘的是「你本人做出該行為的預測機率」，不是全站累積的次數（[[sources/x-algorithm]], #Scoring and Ranking） |
| 4 | 「推薦不到＝被刪文」 | 不一定。X 的可見度過濾有四種結果，有些規則只影響「推薦給非追蹤者」，追蹤者仍然看得到（[[sources/x-algorithm]], #Labeling Path） |
| 5 | 「TikTok 用的就是 Monolith」 | 論文沒有這樣說，只說用在 BytePlus Recommend（[[sources/monolith]], p.1），見 [[entities/bytedance]] |
| 6 | 「平台完全不管推薦有沒有多樣性」 | 至少在設計上都有多樣性機制，例如 TikTok 不連續推同一位創作者、X 的 DPP（[[sources/tiktok-foryou]], p.3；[[sources/x-algorithm]], #Components）。實際效果需要獨立驗證 |
| 7 | 「演算法一年才更新一次」 | 有的系統以分鐘為單位更新（[[sources/monolith]], p.9）；X 的 README 在 2026 年 8–10 月就有 6 次重要更新（[[sources/x-algorithm]], #Notable Updates） |
| 8 | 「TikTok 會連續推同一首爆紅配樂的影片」 | 前幾名太像（例如同一段配樂）會被換掉（[[sources/tiktok-transparency]], p.8） |
| 9 | 「國中生的影片也會被推上 For You」 | 未滿 16 歲帳號做的內容不會被推薦（[[sources/tiktok-transparency]], p.10） |
| 10 | 「推薦 AI 就是 ChatGPT」 | 生成式推薦借用了 ChatGPT 的「接龍」方法，但模型是用行為紀錄從頭訓練的，不是語言模型（[[sources/hstu]], p.9；[[sources/onerec]], p.25） |
| 12 | 「研究已經證明演算法造成政治極化」 | 最大型的隨機實驗（FB/IG，約 4 萬人，3 個月）沒有偵測到態度變化（[[sources/guess-2023]], p.4）；但演算法確實放大憤怒和敵意的內容（[[sources/milli-2025]], p.6） |
| 13 | 「改回時間序動態就沒問題了」 | 時間序的不文明內容較少，但不可信來源多了 68.8%（[[sources/guess-2023]], p.4） |
| 14 | 「我花很多時間看的東西，就是我想看的」 | 使用者其實比較不想看演算法挑的政治推文（−0.18 SD），即使演算法讓人用得更久（[[sources/milli-2025]], p.8–9） |
| 11 | 「讓 AI 衝高觀看時間，推薦就會變好」 | OneRec 只用看完率當獎勵時，使用者看的影片數反而變少，作者承認有 reward hacking（[[sources/onerec]], p.19–21） |

## 比喻

**迷思像「都市傳說」**：每個都有一點真實成分，但被簡化或誇大了。教學時的重點是**回到原始來源看它到底怎麼說**。

## 課堂例子／互動點子

- **「真的假的」投票**：課堂上逐條念出迷思，學生先舉手投票，再揭曉事實和出處。
- **延伸討論**：為什麼這些迷思會流傳？（例如：權重數字被斷章取義、平台過去不透明。）

## 可上簡報的圖解構想

一張「真／假」翻牌卡：正面寫迷思，翻過來是事實加上出處小字。

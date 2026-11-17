---
type: concept
title: 隱式回饋與互動訊號（Implicit Feedback / Engagement Signals）
sources: [youtube-dnn-2016, tiktok-foryou, x-algorithm, monolith, tiktok-transparency]
updated: 2026-11-17
---

# 隱式回饋與互動訊號（Implicit Feedback）

**一句話定義**：使用者沒有明說「我喜歡」，但透過行為透露了偏好，例如看完、重看、停留、分享、快速滑走。推薦系統主要就是靠這些行為學習。

## 白話解釋

**比喻：餐廳老闆觀察客人。**
- 客人很少填滿意度問卷（**明確回饋**），但老闆看得到他把哪道菜吃光、哪道剩一半、下次又點了什麼（**隱式回饋**）。
- 後者多得多，也更誠實。

**你在滑手機時，每個動作都是在「投票」**：停留兩秒、看完、重看、往回滑、按「不感興趣」。

## 為什麼需要它

- **數量差太多**：YouTube 雖然有按讚／倒讚和問卷，但訓練時用的是觀看紀錄，因為隱式資料「多了好幾個數量級」，連冷門內容都能學到（[[sources/youtube-dnn-2016]], §3.1, p.2）。
- **真實答案很難取得**：YouTube 說它們「很少能取得使用者滿意度的真實答案」，只能用帶雜訊的隱式回饋（[[sources/youtube-dnn-2016]], p.1）。

## 各平台看哪些訊號

| 平台 | 訊號 | 出處 |
|---|---|---|
| TikTok | 按讚、分享、追蹤、留言、自己的創作；**看完長影片是強訊號**；國家相同是弱訊號；裝置和語言權重較低 | [[sources/tiktok-foryou]], p.1–2 |
| TikTok（© 2025 說明頁） | 看了、看完、按讚、略過、**追蹤關係**；會預測點配樂、觀看一定時間、和作者個人頁互動 | [[sources/tiktok-transparency]], p.12–13 |
| YouTube 2016 | 看完影片算正例；觀看時間用來加權；搜尋歷史 | [[sources/youtube-dnn-2016]], p.2, p.7 |
| X 2026 | 喜歡、回覆、轉發、分享、點擊、**停留與停留時間**、影片續看秒數、追蹤；**負面**：不感興趣、靜音、封鎖、檢舉、沒停留 | [[sources/x-algorithm]], #Scoring and Ranking |
| Monolith | 點擊、按讚、轉換（購買）等使用者行為，以串流方式即時收集 | [[sources/monolith]], p.4 |

## 注意事項

- **訊號 ≠ 滿意**：看完不代表喜歡，可能只是忘了關；停留久也可能是被激怒。這就是「代理指標」的問題，見 [[concepts/optimization-objective]]。
- **負面訊號也很重要**：TikTok 的「不感興趣」、隱藏創作者或音樂（[[sources/tiktok-foryou]], p.2）；X 給負面行為負權重（[[sources/x-algorithm]], #Scoring and Ranking）。
- **你的行為主要影響你自己的推薦**：X 特別澄清，權重乘的是「你本人」做出某行為的預測機率，這個機率主要取決於你自己的行為（[[sources/x-algorithm]], #Scoring and Ranking）。

## 相關

- [[concepts/ranking]]、[[concepts/optimization-objective]]、[[concepts/collaborative-filtering]]、[[teaching/what-the-feed-learns-from-you]]

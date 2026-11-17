---
type: teaching
title: 你滑手機時，演算法從你身上學到什麼
sources: [tiktok-foryou, youtube-dnn-2016, x-algorithm, monolith]
concepts: [implicit-feedback, cold-start, online-training, optimization-objective]
updated: 2026-11-17
---

# 你滑手機時，演算法從你身上學到什麼

## 比喻

**你的每個小動作都是一張「選票」。** 停留、看完、重看、分享是贊成票；快速滑走、按「不感興趣」、封鎖是反對票。你沒有填任何問卷，但系統一直在「計票」。

## 你送出的訊號（依平台官方說法）

| 你做的事 | 系統怎麼看 | 出處 |
|---|---|---|
| 把長影片看完 | 強烈的興趣訊號 | [[sources/tiktok-foryou]], p.2 |
| 和創作者同國家 | 弱訊號 | [[sources/tiktok-foryou]], p.2 |
| 按「不感興趣」、隱藏創作者 | 之後少推類似內容 | [[sources/tiktok-foryou]], p.2 |
| 在貼文上停留 | X 會預測停留機率和停留時間 | [[sources/x-algorithm]], #Scoring and Ranking |
| 封鎖、檢舉 | X 給負權重 | [[sources/x-algorithm]], #Scoring and Ranking |
| 搜尋 | YouTube 把搜尋詞當作興趣特徵 | [[sources/youtube-dnn-2016]], p.3 |
| 剛註冊、什麼都還沒做 | 先看熱門內容或選興趣類別 | [[sources/tiktok-foryou]], p.2 |

## 學得有多快？

- 有些系統以**分鐘**為單位更新模型（[[sources/monolith]], p.5, p.9）。
- ⚠️ Monolith 是字節跳動的論文，但沒有說它用在 TikTok，見 [[entities/bytedance]]。

## 常見迷思 vs. 事實

| 迷思 | 事實（出處） |
|---|---|
| 「只要按讚，演算法才知道我喜歡」 | 看完、停留、重看都算，而且看完長影片是強訊號（[[sources/tiktok-foryou]], p.2；[[sources/x-algorithm]], #Scoring and Ranking） |
| 「滑走沒關係，不會被記錄」 | X 把「沒停留（not dwelled）」列為負面行為之一（[[sources/x-algorithm]], #Scoring and Ranking） |
| 「我的推薦是全世界的人一起決定的」 | 部分是（協同過濾），但 X 說權重乘的是「你本人」的預測機率，主要由你自己的行為決定（[[sources/x-algorithm]], #Scoring and Ranking） |

## 課堂例子／互動點子

- **實驗作業**：開一個新帳號，連續 10 分鐘只看某一類影片（例如料理），記錄第 1、5、10 分鐘推薦頁上各類影片的比例。課堂上討論觀察到什麼，以及為什麼。
- **反思題**：如果你的「停留」常常是因為被激怒，系統會學到什麼？

## 可上簡報的圖解構想

一隻手在滑手機，每個動作（停留、看完、滑走、按讚）飛出一張「選票」，投進標著「你的口味模型」的票箱。

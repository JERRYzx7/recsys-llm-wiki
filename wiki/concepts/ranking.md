---
type: concept
title: 排序（Ranking）
sources: [youtube-dnn-2016, x-algorithm, tiktok-foryou, monolith, hstu]
updated: 2026-11-17
---

# 排序（Ranking）

**一句話定義**：對召回來的幾百則候選內容，用比較複雜的模型逐一預測「你會有什麼反應」，算出分數後由高到低排列。

## 白話解釋

**比喻：面試官仔細面試進入複賽的人。**
- 海選（[[concepts/retrieval|召回]]）只看履歷關鍵字。
- 複賽就不同了：面試官會看作品、問問題、考慮這個人跟團隊合不合。人少了，所以每個人都能花時間細看。

排序模型其實就是在**猜你接下來會怎麼做**：會看多久？會按讚嗎？會不會直接滑掉，甚至封鎖？

## 為什麼需要它

召回只是粗篩。排序能使用多很多**特徵**（模型輸入的資訊）——YouTube 的排序模型用了**數百個**特徵（[[sources/youtube-dnn-2016]], p.5），因此能分辨細微差異，例如「你會不會點這個縮圖」。

## 怎麼運作

1. **輸入**：你的資訊（歷史行為、語言、裝置）＋ 內容的資訊（作者、主題、熱度）＋ 你和這則內容的關係。
2. **模型預測**：一個或多個目標，例如觀看時間或各種行為的機率。
3. **合成分數並排序**。

**最有用的特徵**：YouTube 發現，最重要的訊號是「你過去和這則內容、相似內容的互動」，例如你在這個頻道看過幾支影片、上次看這個主題是什麼時候（[[sources/youtube-dnn-2016]], p.6）。

**預測什麼**：見 [[concepts/optimization-objective]]。
- YouTube 2016：預期觀看時間（p.5）。
- X 2026：十多種行為的機率加權，`Final Score = Σ weight × P(action)`（[[sources/x-algorithm]], #Scoring and Ranking）。
- TikTok 2020：依訊號強弱加權，例如「看完長影片」是強訊號（[[sources/tiktok-foryou]], p.2）。

**模型種類**：
- YouTube 2016：多層全連接網路（p.6, Figure 7）。
- X 2026：[[concepts/transformer|Transformer]]。推論時候選彼此看不到對方，所以每則貼文的分數不受同一批其他貼文影響（[[sources/x-algorithm]], #Key Design Decisions）。
- Monolith 的實驗用 DeepFM 和多塔模型，重點在於如何讓排序模型即時更新（[[sources/monolith]], p.6）。

**生成式排序**：HSTU 把排序改寫成「依序讀入內容和你的反應，預測你對下一則內容的反應」（[[sources/hstu]], §2.2, p.3），見 [[concepts/generative-recommendation]]。

## 排序之後的調整

純粹依分數排序，可能讓同一個作者或同一類內容連續出現，所以通常還會再調整，見 [[concepts/diversity-and-exploration]]。

## 相關

- [[concepts/recommendation-funnel]]、[[concepts/optimization-objective]]、[[concepts/implicit-feedback]]、[[concepts/online-training]]

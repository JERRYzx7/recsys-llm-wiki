---
type: concept
title: 召回／候選生成（Retrieval / Candidate Generation）
sources: [youtube-dnn-2016, x-algorithm, hstu, onerec]
updated: 2026-11-17
---

# 召回／候選生成（Retrieval / Candidate Generation）

**一句話定義**：從海量內容裡，快速撈出幾百到幾千則「大概跟你有關」的候選內容，交給後面的[[concepts/ranking|排序]]精挑細選。

## 白話解釋

**比喻：圖書館員先幫你從書庫搬一車書。**
- 你說「我想看推理小說」，館員不會把一百萬本書一本本讀給你聽，而是先推一車大概符合的書過來。
- 這一車書不一定每本都好看，但重點是**不能漏掉好書**。
- 至於哪本最適合你，留給下一步慢慢挑。

## 為什麼需要它

精細的排序模型太慢，無法對數百萬則內容逐一打分。召回必須在**數十毫秒**內從數百萬支影片縮到數百支（[[sources/youtube-dnn-2016]], p.2–3）。

## 怎麼運作

### 1. 向量最近鄰（雙塔模型的概念）

- 把「你」和「每則內容」都變成一串數字，也就是 [[concepts/embedding|embedding 向量]]。
- 找出和「你的向量」最接近的內容向量。
- YouTube 用神經網路從你的觀看和搜尋歷史算出使用者向量，上線時做最近鄰搜尋（[[sources/youtube-dnn-2016]], §3, p.3–4）。
- X 的 Phoenix retrieval 也是把使用者和貼文 embed 成向量，回傳最近的貼文（[[sources/x-algorithm]], #Components）。

### 2. 社交關係

X 的 Thunder 直接拿你追蹤帳號的近期貼文（[[sources/x-algorithm]], #Components）。

### 3. 群集或協同過濾

X 的 SimClusters 依「誰和什麼互動」分群後找候選，見 [[concepts/collaborative-filtering]]（[[sources/x-algorithm]], #Components）。

### 4. 熱門內容

X 有一份共用的熱門貼文清單（[[sources/x-algorithm]], #Components）；TikTok 也會給新使用者熱門影片（[[sources/tiktok-foryou]], p.2）。

### 訓練目標

- YouTube 2016 把召回當成「預測下一支會看的影片」的超多類別分類問題，用看完的影片當正例（[[sources/youtube-dnn-2016]], §3.1, p.2）。
- X 在 2026-10 更新後，召回也開始訓練去找「會被讀完的貼文」（[[sources/x-algorithm]], #October 13th, 2026）。

### 補充：生成式召回

- HSTU 把召回當成「預測你下一個會正面互動的內容」（[[sources/hstu]], Table 1, p.3）。
- OneRec 則直接用解碼器「生成」影片的語意 ID，連排序也一起做掉（[[sources/onerec]], §2.3）。
- 見 [[concepts/generative-recommendation]]。

## 在各來源中的樣貌

- [[sources/youtube-dnn-2016]]：候選生成網路，100 萬支影片的詞彙表、256 維 embedding（§3.5, p.4）。
- [[sources/x-algorithm]]：多個來源平行查詢，包含追蹤中與未追蹤的來源（#Request Path）。

## 相關

- [[concepts/recommendation-funnel]]、[[concepts/embedding]]、[[concepts/ranking]]、[[concepts/collaborative-filtering]]

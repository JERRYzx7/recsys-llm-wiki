---
type: concept
title: 嵌入向量（Embedding）
sources: [youtube-dnn-2016, monolith, x-algorithm, hstu, onerec]
updated: 2026-11-17
---

# 嵌入向量（Embedding）

**一句話定義**：把「使用者」「影片」「搜尋詞」這類只是一個編號的東西，轉成一串有意義的數字（向量），讓電腦可以計算它們之間有多相似。

## 白話解釋

**比喻：用一組分數描述一個人的口味。**
- 假設用三個分數描述你：「喜歡搞笑 0.9、喜歡運動 0.2、喜歡美食 0.7」。
- 每支影片也用同樣三個分數描述。
- 你的分數和影片的分數越接近，你就越可能喜歡它。

實際系統會用幾十到上千個數字，而且這些數字**不是人訂的**，是模型從大量行為資料中自己學出來的，所以通常說不出每個數字代表什麼。

## 為什麼需要它

- 電腦沒辦法直接比較「影片 #384729」和「影片 #102938」像不像，因為編號本身沒有意義。
- 轉成向量後，就能用數學算相似度，用來做[[concepts/retrieval|召回]]的最近鄰搜尋。
- YouTube 的定義：embedding 是把稀疏的個體（單一影片、使用者）對應到一個密集向量（[[sources/youtube-dnn-2016]], §3.1, p.2）。

## 怎麼運作

- **一起學出來**：embedding 和模型其他參數一起用梯度下降訓練（[[sources/youtube-dnn-2016]], §3.2, p.3）。
- **把一串東西變成一個向量**：例如你看過的 50 支影片，取它們 embedding 的平均（[[sources/youtube-dnn-2016]], p.3）。
- **參數大多在這裡**：一百萬個 ID 用 32 維 embedding，參數量是 2048 寬全連接層的 7 倍（[[sources/youtube-dnn-2016]], p.6）。Monolith 也說稀疏參數（embedding）主導了模型大小，正式環境的模型有好幾 TB（[[sources/monolith]], p.5）。

## 大問題：ID 太多、還一直增加，怎麼辦？

這是三份來源給出不同解法的地方：

| 做法 | 來源 | 優點 | 代價 |
|---|---|---|---|
| **截斷詞彙表**：只保留最常出現的前 N 個 ID，其他 ID 對應到零向量 | [[sources/youtube-dnn-2016]], p.6 | 簡單，記憶體固定 | 冷門或新 ID 沒有自己的向量 |
| **無碰撞雜湊表**＋頻率過濾＋過期刪除 | [[sources/monolith]], §2.1, p.3–4 | 每個 ID 有專屬向量，可以動態增加 | 系統較複雜 |
| **多雜湊函數 embedding**（不維護詞彙表） | [[sources/x-algorithm]], #Key Design Decisions | 新貼文可以立刻被表示 | 可能有雜湊碰撞（README 沒有討論） |
| **語意 ID**：用內容和協同訊號把影片編成 3 層、由粗到細的 token，相似影片共享前綴 | [[sources/onerec]], §2.1, p.5–7 | 詞彙固定、新影片也能表示；參數和通訊量大減（p.18） | 需要另外訓練 tokenizer；生成的 ID 可能對不到真實影片（p.21） |

> [!warning] ⚠️ 爭議：雜湊碰撞到底傷不傷模型？
> - **說法 A**：雜湊造成的 ID 碰撞會傷害模型品質，所以應該做無碰撞的雜湊表。在 MovieLens 和內部正式模型上，無碰撞版本的 AUC 都比較高（[[sources/monolith]], p.2, p.7, Figure 7–8）。條件：2022 年；字節跳動；DeepFM 與多塔模型；比較對象是「雜湊後映射到較小空間」的碰撞版本（p.6）。
> - **說法 B**：X 在召回和排序都採用「多個雜湊函數」的 embedding，理由是不用維護詞彙表、新貼文可以立刻被表示（[[sources/x-algorithm]], #Key Design Decisions）。條件：2026 年；X；README 只說明設計理由，沒有提供碰撞影響的數據。
>
> **🧭 wiki 觀點**：這比較像**不同取捨**，不是直接矛盾。
> - Monolith 證明的是「單純雜湊到較小空間造成的碰撞」有害。
> - X 用的是多個雜湊函數。一般認為這種做法能降低碰撞的影響（背景知識，非本 wiki 來源），而且 X 更重視「新貼文立刻可用」，因為 X 的貼文 48 小時後就會被過濾掉（[[sources/x-algorithm]], #Filtering）。
> - 目前證據不足以判斷哪個做法比較好，因為兩者的資料、模型和評估指標都不同。
> - 教學時可以用這個例子說明「工程沒有標準答案，只有取捨」。

**規模感**：HSTU 指出，100 億個 ID、每個 512 維，光是 embedding 加優化器狀態就要 **60TB** 記憶體（[[sources/hstu]], p.5）。這就是為什麼大家想盡辦法處理 embedding 表。

## 在各來源中的樣貌

- [[sources/youtube-dnn-2016]]：召回和排序都用 embedding，同一個 ID 空間共用 embedding（p.6）。
- [[sources/monolith]]：核心貢獻就是 embedding 表的儲存方式（§2.1）。
- [[sources/x-algorithm]]：Phoenix 把使用者和貼文 embed 成向量；vm-ranker 用貼文 embedding 計算相似度來做多樣性重排（#Components）。

## 相關

- [[concepts/retrieval]]、[[concepts/collaborative-filtering]]、[[concepts/online-training]]、[[concepts/diversity-and-exploration]]

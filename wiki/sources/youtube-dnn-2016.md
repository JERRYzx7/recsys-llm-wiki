---
type: source
title: Deep Neural Networks for YouTube Recommendations
raw: raw/02-youtube-dnn-2016.pdf
authors: Paul Covington, Jay Adams, Emre Sargin（Google）
year: 2016
venue: RecSys '16（ACM Conference on Recommender Systems），Boston
sources: [youtube-dnn-2016]
updated: 2026-11-17
---

# YouTube 深度神經網路推薦（Deep Neural Networks for YouTube Recommendations）

**一句話**：YouTube 把推薦拆成兩段：先用一個神經網路從數百萬支影片裡挑出幾百支（召回），再用另一個神經網路精細打分、排序（排序）。排序的目標是「預期觀看時間」，不是點擊率。這篇是業界「兩階段推薦漏斗」的經典範本。

## 背景：它想解決什麼問題

YouTube 推薦有三大難題（p.1）：
- **規模（Scale）**：使用者超過十億、影片庫極大，很多在小資料上有效的演算法在這裡跑不動。
- **新鮮度（Freshness）**：每秒都有好幾小時的新影片上傳，系統要能快速反映新內容和使用者的最新行為，這是「探索／利用（exploration/exploitation）」的平衡問題。
- **雜訊（Noise）**：很少能取得「使用者滿意度」的真實答案，只能用帶雜訊的**隱式回饋**來建模。

模型約有**十億個參數**，用**數千億筆樣本**訓練（p.1）。

## 核心做法

### 1. 兩階段漏斗（§2, p.2, Figure 2）

數百萬支影片 →（候選生成）→ 數百支 →（排序）→ 數十支。
- **候選生成**：只做粗略的個人化（協同過濾），重點是「大致相關」。
- **排序**：用大量特徵細分候選影片的相對重要性。
- 兩階段設計也讓系統可以混入其他來源的候選（p.2）。

### 2. 候選生成：把推薦當成「超多類別分類」（§3.1, p.2）

- 問題定義成：給定使用者和情境，預測他「下一支會看哪一支影片」，數百萬支影片各算一個類別。
- 使用者和影片都被表示成 **embedding（嵌入向量）**（p.2）。
- 訓練資料用**隱式回饋**：看完影片算正例。理由是隱式資料比明確回饋（按讚／倒讚、問卷）多好幾個數量級（p.2）。
- 訓練時只抽樣幾千個負類別（candidate sampling），比傳統 softmax 快 100 倍以上（p.2）。
- 上線時改用「最近鄰搜尋」快速找出分數最高的影片，延遲必須控制在數十毫秒內（p.3）。

### 3. 輸入特徵（§3.2–3.3, p.3, Figure 3）

- **觀看歷史**：把看過的影片 embedding 取平均。實驗中「平均」比加總、取最大值等做法好（p.3）。
- **搜尋歷史**：把搜尋詞切成 token，各自 embed 後取平均。
- **人口統計特徵**：地區、裝置、性別、年齡、是否登入，主要用來讓新使用者也能拿到合理的推薦（p.3）。
- **「樣本年齡（Example Age）」特徵**（p.3, Figure 4）：
  - 問題：機器學習系統是用過去資料預測未來，因此天生偏向過去。
  - 做法：訓練時把樣本的年齡當作特徵輸入，上線時設成 0。
  - 效果：模型能反映「新影片剛上架時特別熱門」的時間動態。

### 4. 標籤與情境的選擇：代理問題（Surrogate Problem）（§3.4, p.3–5）

- 推薦常常是在解一個「代理問題」，再把結果套用到實際情境（p.3）。
- **用所有觀看紀錄訓練**，不只用推薦帶來的觀看，否則新內容很難浮上來，系統也會過度偏向「利用」（p.3）。
- **每位使用者取固定數量的樣本**，避免少數重度使用者主導模型（p.3）。
- **刻意隱藏資訊**（p.3–4）：如果模型知道你剛搜尋「taylor swift」，就會直接把搜尋結果頁複製到首頁，效果很差。
- **預測「下一支」而不是「隨機挖掉一支」**（p.4–5, Figure 5）：
  - 觀看有方向性，例如影集依序看、先看熱門再看小眾。
  - 預測未來的觀看在 A/B 測試中表現更好；隨機挖空則會洩漏未來資訊。

### 5. 排序：預測觀看時間（§4, p.5–7）

- 排序階段只處理幾百支影片，可以使用多很多特徵，通常有**數百個**（p.5）。
- 目標是**每次曝光的預期觀看時間**，不是點擊率（p.5）：
  > "Ranking by click-through rate often promotes deceptive videos that the user does not complete ("clickbait") whereas watch time better captures engagement."
  > （以點擊率排序常會推升使用者不會看完的誘騙影片——標題黨；觀看時間更能反映投入程度。）
- **最重要的訊號**是使用者過去和這部影片、相似影片的互動，例如「你在這個頻道看過幾支影片？上次看這個主題是什麼時候？」（p.6）。
- **曝光頻率特徵**：推過但沒被點的影片下次會自然降級，讓推薦列表有變化（churn）（p.6）。
- **加權邏輯迴歸**（§4.2, p.7）：點擊的正例用觀看時間加權，未點擊的負例權重為 1，模型學到的勝算（odds）就近似預期觀看時間。

## 關鍵數字與結果

- 候選生成實驗用 **100 萬支影片**和 **100 萬個搜尋詞**的詞彙表，每個 embed 成 256 維；最多取最近 50 次觀看和 50 次搜尋（§3.5, p.4）。
- 加入更多特徵、加深網路都能提高離線 MAP（平均精確率）（p.5, Figure 6）。
- 排序模型的「加權 per-user loss」（越低越好，作者報告，以隔天的保留資料測試）（Table 1, p.7）：
  - 無隱藏層：41.6%（Table 1, p.7）
  - 1024→512→256 三層 ReLU：34.6%（最佳，且在 CPU 預算內）（Table 1, p.7）
- 拿掉連續特徵的次方項，loss 增加 0.2%；正負例權重相同時，loss 大幅增加 4.1%（p.7）。
- 一百萬個 ID 用 32 維 embedding，參數量是 2048 寬全連接層的 7 倍。可見模型參數**大多在 embedding**（p.6）。
- 「樣本年齡」特徵讓新上傳影片的觀看時間在 A/B 測試中「大幅增加」，論文未給具體數字（p.7）。

## 限制與注意事項

- **2016 年的系統**：只代表當時的 YouTube，後續架構已有很大變化。
- **沒有給 A/B 測試的具體數字**，多數線上成效只有定性描述。
- **目標仍是「互動／觀看時間」**：論文沒有討論使用者福祉或社會影響。
- 論文也坦承：離線指標和 A/B 測試結果「不一定相關」（p.2）。

## 與其他來源的關係

- **漏斗架構的原型**：[[sources/x-algorithm]] 在 2026 年仍是「候選來源 → 打分 → 過濾 → 選取」的多階段管線（#System Architecture）。
- **優化目標的延續**：YouTube 用觀看時間取代點擊率；[[sources/x-algorithm]] 進一步預測十多種行為再加權；[[sources/tiktok-foryou]] 也把「看完長影片」視為強訊號（p.2）。演變過程見 [[concepts/optimization-objective]]。
- **embedding 詞彙表的處理方式不同**：YouTube 截取最常見的前 N 個 ID，其他 ID 對應到零向量（p.6）；[[sources/monolith]] 用無碰撞雜湊表；[[sources/x-algorithm]] 用多個雜湊函數。比較見 [[concepts/embedding]]。

## 相關頁面

- [[entities/youtube]]、[[concepts/recommendation-funnel]]、[[concepts/retrieval]]、[[concepts/ranking]]、[[concepts/embedding]]、[[concepts/collaborative-filtering]]、[[concepts/implicit-feedback]]、[[concepts/ab-testing]]

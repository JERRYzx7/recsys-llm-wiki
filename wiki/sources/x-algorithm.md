---
type: source
title: X For You Feed Algorithm（GitHub README）
raw: raw/06-x-algorithm.md
authors: X（xAI / X Corp 工程團隊，未具名）
year: 2026
venue: GitHub 開源 repository README（最新更新紀錄為 2026-10-26）
sources: [x-algorithm]
updated: 2026-11-17
---

# X（前 Twitter）For You 演算法開源說明（X For You Feed Algorithm）

**一句話**：X 公開了 For You 動態的程式碼和架構說明。整個系統先從「你追蹤的人」和「你沒追蹤的人」兩邊撈貼文，再用 Transformer 模型預測你對每則貼文做出十多種反應的機率，加權成一個分數後排序，最後由獨立的「可見度過濾」決定哪些貼文可以顯示。

> 出處標示：這是 Markdown 文件，以章節標題標示，例如 `#Overview`、`#Scoring and Ranking`。

## 背景：它想解決什麼問題

說明 X 的 For You 動態「如何決定你看到哪些貼文」，並透過開源程式碼與透明工具提高公眾信任，讓外界可以「稽核、批評，甚至幫忙改進」（#What's not in this repo?）。

## 核心做法

### 1. 兩種候選來源（#Overview, #Components）

- **In-Network（追蹤中）**：`Thunder` 把你追蹤帳號的近期貼文放在記憶體中。
- **Out-of-Network（未追蹤）**：
  - **Phoenix retrieval**：把使用者和貼文都 embed 成向量，找最接近的貼文，也就是「雙塔」召回。
  - **SimClusters**：依「誰和什麼互動」把帳號和貼文分群。
  - **熱門貼文清單**：一開始取自追蹤數最多的活躍帳號。
- 兩邊的候選**用同一個模型一起排序**（#Overview）。

### 2. 請求路徑七步驟（#Request Path）

1. **Query Hydration**：取得你最近的互動序列（模型的主要輸入）、追蹤清單、封鎖／靜音、看過的貼文等。
2. **Candidate Sources**：平行查詢上面的各個來源。
3. **Candidate Hydration**：補上貼文內容、作者資訊、互動數等。
4. **Pre-Scoring Filters**：
   - 去除重複、超過 **48 小時**的舊貼文、自己的貼文、封鎖或靜音帳號、看過的貼文等（#Filtering）。
   - 共 18 種過濾器（#Filtering）。
5. **Scoring**：
   - `PhoenixScorer` 預測各種行為的機率。
   - `RankingScorer` 加權成分數。
   - `VMRanker` 做多樣性重排。
6. **Selection**：依分數取前 K 則。
7. **Post-Selection Filters**：依可見度過濾的結果移除貼文，並收合同一串對話的分支。

之後 **Blending Pipeline** 會把排好的貼文和廣告、「推薦追蹤」、提示等非貼文內容交錯排在一起（#Overview, #Request Path）。

### 3. 打分：多行為預測加權（#Scoring and Ranking）

Phoenix 預測的行為分成五類：
- **互動**：喜歡、回覆、轉發、引用、分享…
- **點擊**：貼文、個人頁、連結…
- **注意力**：停留（dwell）、停留時間、影片續看秒數…
- **作者**：追蹤作者。
- **負面**：不感興趣、靜音、封鎖、檢舉、沒停留。

```
Final Score = Σ (weight_i × P(action_i))
```

- 正面行為的權重為正，負面行為的權重為負。
- **常見誤解**：權重乘的是「你本人做出該行為的預測機率」，不是全站的互動次數。所以「檢舉權重是喜歡的 468 倍」**不等於**「1 次檢舉抵銷 468 個讚」（#Scoring and Ranking；#August 14th, 2026）。

**加權後的三個調整**（#Scoring and Ranking）：
- **作者多樣性**：同一位作者的第二則以後的貼文，分數乘上遞減係數。
- **未追蹤折扣**：來自沒追蹤帳號的貼文乘上小於 1 的係數。
- **新作者加成**：曝光數低於門檻的作者會被往前推。

**多樣性重排**：`vm-ranker` 用行列式點過程（DPP）重排，「犧牲一點分數，換取相鄰貼文不那麼相似」（#Components → Ranking）。

### 4. 排序與可見度是分開的（#Labeling Path, #Key Design Decisions）

- **內容理解**（持續運作，不在請求路徑上）：
  - 分類器偵測垃圾訊息、成人內容、暴力內容。
  - 帳號評分：被封鎖或檢舉的比例、不真實行為、在追蹤圖上算 PageRank 得到的信譽分數（user-cred-v2）。
- **標籤規則**：依事件或模型分數為帳號和貼文貼標籤。
- **可見度過濾**：對每則貼文和每位觀看者給出四種結果之一：
  - ALLOW（正常顯示）
  - NOTICE（附注意標示）
  - INTERSTITIAL（遮罩，點了才看得到）
  - DROP（不顯示）
- **有些規則只對「未追蹤帳號的推薦」生效**：同一則貼文，追蹤者看得到，非追蹤者可能被過濾掉（#Labeling Path）。

### 5. 關鍵設計決策（#Key Design Decisions）

1. **多行為預測**：不預測單一「相關性」，而是預測多種行為，最後再明確地合併。
2. **候選隔離**：Transformer 推論時，候選貼文之間不能互相 attend，只能看使用者情境，所以分數穩定、可以快取。
3. **雜湊 embedding**：用多個雜湊函數查表，不用維護詞彙表，新貼文可以立刻被表示。
4. **排序和可見度分開**：不同服務、不同輸入、不同規則。
5. **可組合的管線架構**。

## 近期更新紀錄（#Notable Updates）

- **2026-08-13**：公開設定參數（含權重）、可見度過濾程式碼、Phoenix 訓練程式碼、SimClusters。
- **2026-08-14**：
  - 說明權重的常見誤解。
  - 依巴西選舉法執行 `Brazil2026ElectionFilter`：移除被報告到巴西選舉法院的帳號貼文，除非觀看者有追蹤該帳號。
- **2026-09-18**：透明工具「Under the Hood」可以顯示貼文是否因法律要求而在某些國家被限制。
- **2026-10-08**：排序模型更準確預測「花在每則貼文上的時間」。
- **2026-10-13**：召回模型也開始訓練去找「人們會完整讀完的貼文」。
- **2026-10-26**：選舉結束，移除巴西選舉過濾器。

## 關鍵數字與結果

- 貼文年齡上限 **48 小時**（#Filtering）。
- 實驗若佔流量 **10% 以上**，目標是在 repo 中可見（#Experiments and Configuration）。
- 「檢舉權重是喜歡的 468 倍」只是官方解釋誤解時用的例子（#Scoring and Ranking）。
- **沒有提供任何成效數據**（沒有 A/B 測試結果，也沒有準確率）。

## 限制與注意事項

- **平台自述加程式碼**：README 是 X 自己寫的說明；程式碼可以檢查，但 README 本身沒有外部驗證。
- **不完全公開**：部分 Grox LLM prompt 和 botmaker 規則沒有放出，理由是防止有人鑽漏洞（#What's not in this repo?）。
- **程式碼預設值 ≠ 線上實際值**：參數預設值由 cron 腳本設成「主要正式環境值」，但實驗中的設定可能不同（#Experiments and Configuration）。
- 本 wiki **只讀了 README**，沒有讀程式碼本身。

## 與其他來源的關係

- **延續** [[sources/youtube-dnn-2016]] 的兩階段漏斗：候選來源 → 打分 → 選取。差別在於 X 在打分後還有重排、可見度過濾，以及和廣告的混排。
- **優化目標的演變**：YouTube 2016 從點擊率改成觀看時間（p.5）；X 預測十多種行為，包含負面行為和停留時間。見 [[concepts/optimization-objective]]。
- **對照** [[sources/tiktok-foryou]]：
  - 兩者都有「同一作者不連續出現」的多樣性規則。
  - TikTok 說追蹤數不是直接因素（p.2）；X 則明確依「是否追蹤」給折扣。
- **對照** [[sources/monolith]]：雜湊 embedding 的取捨，見 [[concepts/embedding]]。

## 相關頁面

- [[entities/x-twitter]]、[[concepts/recommendation-funnel]]、[[concepts/retrieval]]、[[concepts/ranking]]、[[concepts/visibility-filtering]]、[[concepts/diversity-and-exploration]]、[[concepts/cold-start]]、[[syntheses/platform-transparency]]

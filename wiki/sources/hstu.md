---
type: source
title: "Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations"
raw: raw/04-hstu.pdf
authors: Jiaqi Zhai et al.（Meta AI）
year: 2024
venue: ICML 2024（PMLR 235）；arXiv:2402.17152
sources: [hstu]
updated: 2026-11-17
---

# HSTU：Meta 的生成式推薦（Actions Speak Louder than Words）

**一句話**：Meta 把「你的行為紀錄」當成一種語言，用類似 ChatGPT 的方式訓練推薦模型，提出 HSTU 架構。模型做到 **1.5 兆參數**後，效果仍隨算力穩定提升（**scaling law**）。作者稱這可能是推薦系統的「ChatGPT 時刻」（p.2）。

> 頁碼說明：PDF 共 26 頁。正文 p.1–9，Impact Statement 在 p.10，參考文獻 p.10–14，附錄 p.15–26（GPU 實作與額外實驗）。

## 背景：它想解決什麼問題

- **傳統深度推薦模型（DLRM）加算力也不會變好**：業界的 DLRM 用上千個人工設計的特徵和龐大資料，但「大多數無法隨算力擴展」（p.1）。DLRM 的品質大約在 2000 億參數時就飽和（p.8）。
- **三個難點**（p.1–2）：
  1. 推薦特徵沒有明確結構，有 ID、計數、比例等各種形式。
  2. 詞彙表是**十億級、而且一直在變**；語言模型的詞彙表只有約 10 萬個詞，而且是固定的（p.2）。
  3. 計算量巨大：大平台每天的使用者行為「token」數量，比 GPT-3 訓練 1–2 個月處理的 3000 億 token 還多好幾個數量級（p.2）。

## 核心做法

### 1. 把推薦變成「序列接龍」（Generative Recommenders, GRs）（§2, p.2–3）

- **把各種特徵整合成一條時間序列**（p.2, Figure 2）：
  - 以「你互動過的內容」為主軸。
  - 人口統計、追蹤的創作者這類變化慢的特徵，壓縮後插進主序列。
  - 數值特徵（例如過去的點擊率）直接**拿掉**，交給模型自己從序列學。
- **召回和排序都改寫成序列轉換任務**（Table 1, p.3）：
  - 輸入序列像「內容₀、你的反應₀、內容₁、你的反應₁…」。
  - **排序** = 預測你對下一則內容的**反應**（按讚、略過、看完、分享…）。
  - **召回** = 預測你**下一個會正面互動的內容**。
- **生成式訓練**：一個使用者的序列可以一次產生多個訓練目標，計算量降低一個 O(N) 因子（§2.3, p.3–4）。

### 2. HSTU 架構（§3, p.4–6）

- HSTU（Hierarchical Sequential Transduction Unit）是改良過的 Transformer 層，一種模組取代 DLRM 裡五花八門的模組（p.4, Figure 3）。
- **把 softmax 注意力改成「逐點聚合」注意力**（§3.1, p.4–5）：
  - softmax 會正規化，模型因此難以看出「你對某主題的互動有多**頻繁**」，而這正是偏好強度的重要線索。
  - 在合成資料上，兩種注意力的差距最高達 44.7%（Table 2, p.5）。
- **Stochastic Length（隨機長度）**：訓練時隨機截短很長的歷史序列。去掉 80% 以上的 token，品質幾乎不變（p.5–7）。
- **M-FALCON**：推論時把大量候選分成小批次，共用計算結果，讓排序階段能用複雜很多的模型（§3.4, p.6）。

## 關鍵數字與結果（皆為作者報告）

- **公開資料集**：相對 SASRec 基準，HSTU-large 的 NDCG@10 在 Amazon Books 上提升最多 **65.8%**（Table 4, p.7）。
- **速度**：在 8192 長度的序列上比 FlashAttention2 版 Transformer 快 **5.3–15.2 倍**（p.1–2）；訓練效率最高 15.2 倍、推論 5.6 倍（p.7）。
- **線上 A/B 測試**（Table 7, p.7）：
  - 排序：GR 相對 DLRM，主要互動任務（E-Task）**+12.4%**、主要消費任務（C-Task）**+4.4%**（Table 7, p.7）。
  - 召回：把 GR 加為新來源 +6.2%／+5.0%（Table 6, p.7）。
- **規模與效率**：
  - **1.5 兆參數**，部署在「一個擁有數十億使用者的大型網路平台」的多個介面上（p.1）。
  - 模型複雜度是原本的 **285 倍**，吞吐量仍高 1.50–2.99 倍（p.8）。
- **Scaling law**（§4.3.1, p.8–9, Figure 7）：
  - 品質隨訓練算力呈冪律提升，跨越三個數量級。
  - 最大的模型所用算力接近 GPT-3 和 LLaMa-2 的總訓練量（p.8）。
  - 序列長度在推薦中比在語言模型中更重要（p.8–9）。
- **只用內容特徵的版本表現差很多**：召回 HR@100 只有 11.6%，GR 則是 36.9%（Table 6, p.7）。這顯示「使用者行為」本身才是關鍵訊號（p.8）。
- **判讀門檻**：作者認為 NE 降低 0.001 就算顯著，通常對應約 0.5% 的線上指標提升（p.6）。

## 作者對社會影響的主張（Impact Statement, p.10）

> "...could reduce the prevalence of content that do not serve users' long term goals (including clickbaits and fake news) across the web, and better align incentives of platforms with user values."
> （……可能減少不符合使用者長期目標的內容（包括標題黨和假新聞），並讓平台的誘因更符合使用者的價值。）

- 作者也主張，減少對大量異質特徵的依賴，可以讓系統**更保護隱私**（p.10）。
- ⚠️ 這些是作者的**展望**，論文**沒有提出實證**。和批次 3 實證研究的對照見 [[syntheses/do-algorithms-polarize]]。

## 限制與注意事項

- **沒有寫明部署平台**：論文只說「一個擁有數十億使用者的大型網路平台」（p.1），作者都隸屬 Meta AI（p.1）。合理推測是 Meta 旗下產品，但論文沒有明說是哪一個。
- **「+12.4%」的意思要看清楚**：這是主要互動任務在 A/B 測試中的相對提升（Table 7）。論文沒有公開任務的具體定義。
- 公開資料集實驗用的是學界常見的「多輪、全打亂」設定，作者自己也說這和業界的串流訓練很不同（p.6）。
- 程式碼有開源：github.com/facebookresearch/generative-recommenders（p.1）。

## 與其他來源的關係

- **直接挑戰** [[sources/youtube-dnn-2016]] 代表的 DLRM 典範：HSTU 把 YouTube DNN 列為 DLRM 的起點（p.1, p.15），並主張要用生成式推薦取代它。
- **同一陣營** [[sources/onerec]]：兩者都把推薦當作生成任務，也都觀察到 scaling law。差別在於 HSTU 仍保留召回和排序兩個任務，OneRec 則主張用單一模型端到端取代多階段漏斗。見 [[syntheses/cascade-vs-end-to-end]]。
- **和 X 的呼應** [[sources/x-algorithm]]：X 2026 的排序模型也是 Transformer，主要輸入是「使用者的互動序列」（#Request Path）。這和 HSTU「以行為序列為核心」的方向一致。
- **呼應** [[sources/monolith]] 的「詞彙表很大而且一直在變」：HSTU 指出，100 億詞彙、512 維 embedding 光是存 embedding 加優化器狀態就要 60TB（p.5）。

## 相關頁面

- [[entities/meta]]、[[concepts/generative-recommendation]]、[[concepts/transformer]]、[[concepts/scaling-law]]、[[concepts/ranking]]、[[concepts/retrieval]]、[[syntheses/cascade-vs-end-to-end]]

---
type: source
title: "Monolith: Real Time Recommendation System With Collisionless Embedding Table"
raw: raw/03-monolith.pdf
authors: Zhuoran Liu et al.（ByteDance；通訊作者 Youlong Cheng）
year: 2022
venue: ORSUM Workshop @ ACM RecSys 2022；arXiv:2209.07663
sources: [monolith]
updated: 2026-11-17
---

# Monolith：字節跳動的即時推薦系統（Monolith: Real Time Recommendation System With Collisionless Embedding Table）

**一句話**：推薦系統面對的使用者興趣「每分鐘都在變」，所以 Monolith 讓模型**上線後繼續邊服務邊學習**，並以分鐘級的頻率把新參數推到線上。它也用一種「不會撞號」的雜湊表，讓每個使用者和影片都有自己專屬的 embedding。

## 背景：它想解決什麼問題

推薦資料和語言、影像資料有兩點根本不同（p.1）：
1. **特徵大多是稀疏、類別型、而且一直在變**：使用者 ID 和影片 ID 的數量多到單機記憶體放不下，而且會持續增加（p.2）。
2. **資料分布不穩定**，也就是**概念漂移（Concept Drift）**：
   > "Visual and linguistic patterns barely develop in a time scale of centuries, while the same user interested in one topic could shift their zeal every next minute."（p.2）
   > （視覺和語言模式要以世紀為尺度才會改變，同一個使用者對某個主題的熱情卻可能下一分鐘就轉移。）

傳統框架（TensorFlow、PyTorch）把「批次訓練」和「上線服務」完全分開，模型無法即時吸收使用者回饋（p.1）。

## 核心做法

### 1. 無碰撞雜湊表（Collisionless HashTable）（§2.1, p.3–4）

- **問題**：很多系統用「雜湊技巧」把大量 ID 壓進固定大小的表，不同 ID 可能共用同一個 embedding（碰撞）。這個做法假設 ID 出現頻率很平均、碰撞無害，但實際上少數熱門使用者和物品出現次數多得多，碰撞會傷害模型品質（p.2）。
- **做法**：用 **Cuckoo Hashing（布穀鳥雜湊）** 實作 key-value 雜湊表，新 key 插入時不會和舊 key 衝突（p.3）。
- **省記憶體的兩個過濾機制**（p.3–4）：
  - **頻率過濾**：只出現幾次的 ID 不納入。ID 呈長尾分布，冷門 ID 的 embedding 本來就學不好，對結果影響不大（p.3）。
  - **過期機制**：長期沒出現的 ID 自動刪除，例如不再活躍的使用者、過時的短影音（p.3–4）。

### 2. 線上訓練（Online Training）（§2.2, p.4–5, Figure 1, 4）

- **兩個階段**：先用歷史資料做**批次訓練**；模型部署上線後進入**線上訓練**，持續吃即時資料、更新參數（p.4）。
- **資料流**（p.4, Figure 4–5）：
  - 用 Kafka 收集使用者行為（點擊、按讚、轉換…）和特徵。
  - 用 Flink 的「線上 joiner」把特徵和行為配對，產生訓練樣本。
- **負樣本抽樣與修正**：負樣本遠多於正樣本，所以先抽樣，服務時再做 log odds 修正，避免預測偏高（p.5）。

### 3. 參數同步（§2.2.3, p.5）

- 線上模型有**好幾 TB**，不能停機整個替換（p.5）。
- **只同步「被動過」的參數**：短時間內只有少數 ID 被訓練到，所以只把這些 ID 的 embedding 以**分鐘級**間隔推到線上（p.5）。
- **稀疏參數**（embedding）頻繁同步；**密集參數**（神經網路權重）變化慢，每天同步一次（p.5, p.9）。

### 4. 容錯：用可靠性換即時性（§2.3, p.6；§3.2.2, p.9）

- 參數伺服器每天只做一次快照，壞掉時最多損失一天的更新（p.6）。
- 作者的估算（p.9）：
  - 假設參數分散在 1000 台伺服器、每台每天故障率 0.01%，平均每 10 天才會壞一台（p.9）。
  - 以 DAU 1500 萬計算，等於每 10 天損失 1.5 萬名使用者一天的回饋，影響很小（p.9）。

## 關鍵數字與結果（皆為作者報告）

- **碰撞實驗（MovieLens ml-25m 公開資料集）**（p.6, Table 1）：
  - 資料規模：約 2500 萬筆評分、約 16.2 萬名使用者、約 6.2 萬部電影（p.6）。
  - 雜湊後的碰撞率：使用者 ID 7.73%、電影 ID 2.86%（p.6, Table 1）。
  - 無碰撞版本從第一個 epoch 起 AUC 就比較高，收斂值也比較高（p.7, Figure 7）。
- **內部正式環境模型**：約 1000 個 embedding 表；無碰撞版本的線上 AUC 持續較高（p.6–7, Figure 8）。
- **線上訓練實驗（Criteo 廣告資料集）**（p.7–8）：
  - 設定：7 天資料，前 5 天做批次訓練、後 2 天模擬線上訓練。
  - 平均 AUC（Table 2, p.8；表中數值皆出自此表）：

    | 同步間隔 | 線上訓練 | 只做批次訓練 |
    |---|---|---|
    | 5 小時 | 79.66 | 約 79.42–79.44 |
    | 1 小時 | 79.78 | 約 79.42–79.44 |
    | 30 分鐘 | 79.80 | 約 79.42–79.44 |

  - 結論：同步越頻繁越好。
- **線上 A/B 實驗（某個正式廣告模型）**：線上訓練相對批次訓練的「AUC Improvement %」7 天介於 **14.0%–18.1%**（Table 3, p.9）。
  - ⚠️ 論文沒有定義這個「提升百分比」怎麼計算。和離線實驗不到 0.4 個百分點的差距相比，落差非常大，引用時要註明。
- **傳輸量估算**：每分鐘更新 10 萬個 ID、embedding 維度 1024 時，每分鐘約傳 400MB（p.9）。

## 限制與注意事項

- **Workshop 論文**，不是主會議論文；程式碼在論文發表時寫「即將釋出」（p.1 註腳）。
- 論文說 Monolith 已經用在 **BytePlus Recommend**（字節的對外推薦服務），並**沒有明說用在 TikTok／抖音**。摘要只提到短影音排序和線上廣告是這類需求的例子（p.1）。
- 線上 A/B 實驗是**廣告模型**，不是內容推薦模型（p.7, p.9）。
- 重點在系統工程（如何即時訓練），不是推薦什麼內容；論文沒有討論社會影響。

## 與其他來源的關係

- **呼應** [[sources/youtube-dnn-2016]] 的「新鮮度」難題（p.1）：YouTube 用「樣本年齡」特徵補償模型偏向過去的問題；Monolith 則直接讓模型即時更新。兩種做法都在對付「使用者興趣會變」。
- **對照** [[sources/x-algorithm]]：X 也使用雜湊 embedding（多個雜湊函數），理由是「不用維護詞彙表、新貼文可以立刻被表示」（#Key Design Decisions）。Monolith 則主張碰撞會傷害品質。這個張力見 [[concepts/embedding]] 的爭議區塊。
- **同一家母公司**：[[sources/tiktok-foryou]] 是 TikTok 的平台自述，兩者都出自字節跳動，但沒有證據顯示是同一套系統，見 [[entities/bytedance]]。

## 相關頁面

- [[entities/bytedance]]、[[concepts/online-training]]、[[concepts/embedding]]、[[concepts/ab-testing]]、[[concepts/ranking]]

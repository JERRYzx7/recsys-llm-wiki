---
type: concept
title: Transformer 與注意力機制（Transformer / Attention）
sources: [hstu, onerec, x-algorithm]
updated: 2026-11-17
---

# Transformer 與注意力機制（Transformer / Attention）

**一句話定義**：一種神經網路架構，核心是「注意力（attention）」：處理一段序列時，每個位置都可以回頭看序列裡其他位置，並決定哪些比較重要。ChatGPT 就是建立在它之上，現在推薦系統也大量採用。

## 白話解釋

**比喻：讀你的「觀看日記」時劃重點。**
- 模型要猜你下一支想看什麼，會回頭翻你的觀看日記。
- 它不會每一頁都看得一樣仔細，而是**特別注意**和「現在這支候選影片」有關的紀錄，例如你上週連看了五支貓咪影片。
- 「注意力」就是決定每一筆紀錄要給多少重視。

## 為什麼推薦系統需要它

- 你的行為紀錄本身就是一段**有順序的序列**，Transformer 正好擅長處理序列（[[sources/hstu]], p.1–2）。
- 能隨模型和資料規模持續變好，也就是 [[concepts/scaling-law]]（[[sources/hstu]], p.8）。

## 在各來源中的樣貌

- **X 2026**：排序模型 Phoenix 是 Transformer，主要輸入是你最近的互動序列（[[sources/x-algorithm]], #Request Path, #Components）。
  - 特別設計「**候選隔離**」：候選貼文之間不能互相 attend，只能看你的情境，所以每則貼文的分數不受同一批其他貼文影響，也可以快取（#Key Design Decisions）。
- **HSTU（Meta 2024）**：改良版 Transformer（[[sources/hstu]], §3, p.4–6）。
  - **注意力不做 softmax 正規化**：softmax 會把分數壓成總和為 1 的比例，模型就看不出你對某類內容互動了「**多少次**」，而這正是偏好有多強的線索（p.4）。
  - 線性層從 6 個減到 2 個，省記憶體，模型可以堆深 2 倍以上（p.5）。
  - 在推薦資料上，標準 Transformer 訓練時常常「損失爆炸」（p.6）。
- **OneRec（快手 2025）**：編碼器加解碼器的 Transformer，解碼器用混合專家（MoE）擴大容量（[[sources/onerec]], §2.2–2.3, p.7–10）。

## 推薦和語言的差別

| | 語言模型 | 推薦模型 |
|---|---|---|
| 詞彙量 | 約 10 萬，固定 | 十億級，一直在變（[[sources/hstu]], p.2） |
| 序列長度 | 幾千 token | 使用者歷史可達 10 萬（[[sources/hstu]], p.2；[[sources/onerec]], p.8） |
| 每日資料量 | GPT-3 共訓練 3000 億 token | 大平台每天的行為 token 多好幾個數量級（[[sources/hstu]], p.2） |

## 相關

- [[concepts/generative-recommendation]]、[[concepts/scaling-law]]、[[concepts/ranking]]、[[concepts/embedding]]

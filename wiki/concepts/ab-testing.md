---
type: concept
title: A/B 測試與離線指標（A/B Testing & Offline Metrics）
sources: [youtube-dnn-2016, monolith, x-algorithm, hstu, onerec]
updated: 2026-11-17
---

# A/B 測試與離線指標（A/B Testing & Offline Metrics）

**一句話定義**：平台判斷新演算法好不好有兩種方式。**離線指標**是用歷史資料考模型，**A/B 測試**是真的讓一部分使用者用新版、另一部分用舊版，再比較實際行為。最後拍板通常看 A/B 測試。

## 白話解釋

**比喻：新菜色要不要上菜單。**
- **離線評估**：主廚自己試吃、照食譜打分。快、便宜，但不一定代表客人喜歡。
- **A/B 測試**：一半的客人拿到新菜、一半拿到舊菜，看哪邊吃得比較乾淨、比較常回訪。

## 為什麼兩者會不一致

- YouTube：A/B 測試的結果「不一定和離線實驗相關」，所以最終判斷靠線上實驗（[[sources/youtube-dnn-2016]], §2, p.2）。
- YouTube：代理問題選得好不好，對 A/B 測試的影響很大，卻「很難用離線實驗衡量」（§3.4, p.3）。

## 常見指標

| 指標 | 意思 | 來源 |
|---|---|---|
| **AUC** | 模型把「會互動的」排在「不會互動的」前面的機率（0.5＝亂猜，1＝完美） | [[sources/monolith]], p.6 |
| **MAP**（平均精確率） | 推薦清單中「猜對」的項目排得有多前面 | [[sources/youtube-dnn-2016]], p.5 |
| 點擊率、觀看時間 | 線上 A/B 測試看的使用者行為 | [[sources/youtube-dnn-2016]], p.2 |

## 讀數字時要小心（教學重點）

- **離線差距看起來很小**：Monolith 在 Criteo 資料集上，線上訓練和批次訓練的 AUC 只差約 0.2–0.4 個百分點（[[sources/monolith]], Table 2, p.8）。業界常認為這種差距在大規模系統上就有意義（背景知識，非本 wiki 來源）。
- **線上「提升 %」的定義常常不清楚**：Monolith 報告 A/B 實驗的「AUC Improvement 14–18%」，但沒有說明怎麼計算（[[sources/monolith]], Table 3, p.9）。
- **平台很少公開 A/B 數據**：X 只說佔 10% 以上流量的實驗目標是在 repo 中可見，沒有公開結果（[[sources/x-algorithm]], #Experiments and Configuration）。

### 各平台的「顯著」門檻（作者自述）

| 平台 | 門檻 | 出處 |
|---|---|---|
| Meta（HSTU） | NE 降低 0.001 就算顯著，約等於 0.5% 的線上指標提升 | [[sources/hstu]], p.6 |
| 快手（OneRec） | App 停留時間 +0.1%、7 日留存 +0.01% 就算統計顯著 | [[sources/onerec]], p.23 |

🧭 **wiki 觀點**：對數億使用者的平台，0.1% 就代表很多人和很多時間，所以論文裡「+0.54%」這種看起來很小的數字，對平台來說其實很大。教學時值得說明。

### 實驗範圍要看清楚

- OneRec 的「部署到 25% 流量」，在附錄 B 說明是原本用快取應付的那部分流量（[[sources/onerec]], p.30）。
- HSTU 的「+12.4%」是主要互動任務的相對提升，任務的具體定義沒有公開（[[sources/hstu]], Table 7, p.7）。

## 社會面：使用者其實一直在被實驗

X 自述會「定期在一小部分流量上做實驗」（[[sources/x-algorithm]], #Experiments and Configuration）。也就是說，你看到的動態可能和朋友不同，原因不只是個人化，也可能是你們被分到不同的實驗組（🧭 wiki 觀點）。

## 相關

- [[concepts/optimization-objective]]、[[concepts/online-training]]、[[syntheses/platform-transparency]]

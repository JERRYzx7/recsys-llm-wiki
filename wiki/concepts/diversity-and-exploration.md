---
type: concept
title: 多樣性與探索（Diversity & Exploration）
sources: [tiktok-foryou, x-algorithm, youtube-dnn-2016, tiktok-transparency, onerec, hstu]
updated: 2026-11-17
---

# 多樣性與探索（Diversity & Exploration）

**一句話定義**：刻意在推薦中加入「不完全照你過去口味」的內容。一方面避免動態太單調，另一方面讓系統有機會發現你的新興趣（**探索**），而不是只推穩拿分的內容（**利用**）。

## 白話解釋

**比喻：常去的餐廳偶爾推出「主廚推薦」。**
- 老闆知道你愛吃牛肉麵（**利用**），但偶爾會端一小碟新菜請你試吃（**探索**）。
- 你喜歡的話，他就學到你的新口味；不喜歡的話，損失也不大。
- 如果永遠只端牛肉麵，他永遠不會知道你其實也愛吃咖哩。

## 為什麼需要它

1. **避免單調和[[concepts/filter-bubble|過濾泡泡]]**（[[sources/tiktok-foryou]], p.2–3）。
2. **系統需要新資料**：只推你已知喜歡的內容，系統就學不到別的。TikTok 說，偶爾推不同的影片也能幫系統了解更廣泛受眾的喜好（[[sources/tiktok-foryou]], p.3）。
3. **新內容和新創作者需要機會**：YouTube 把新內容和熱門內容之間的平衡視為「探索／利用」問題（[[sources/youtube-dnn-2016]], p.1）。

## 各平台的做法

| 做法 | 平台 | 出處 |
|---|---|---|
| 不連續推同一個創作者或同一個音樂 | TikTok | [[sources/tiktok-foryou]], p.3 |
| **相似度檢查**：前幾名太像（例如同一段配樂）就換掉 | TikTok | [[sources/tiktok-transparency]], p.8 |
| 推薦頁一定包含同地區創作者 | TikTok | [[sources/tiktok-transparency]], p.8 |
| 不推重複內容或已看過的內容 | TikTok、X | [[sources/tiktok-foryou]], p.3；[[sources/x-algorithm]], #Filtering |
| 刻意插入不符合興趣的影片 | TikTok | [[sources/tiktok-foryou]], p.3 |
| **作者多樣性**：同一位作者第二則以後的貼文分數遞減 | X | [[sources/x-algorithm]], #Scoring and Ranking |
| **DPP 重排**：犧牲一點分數，讓相鄰貼文比較不相似 | X | [[sources/x-algorithm]], #Components |
| **新作者加成**：曝光數少的作者被往前推 | X | [[sources/x-algorithm]], #Scoring and Ranking |
| **曝光頻率特徵**：推過但沒被點的影片降級，讓列表有變化（churn） | YouTube | [[sources/youtube-dnn-2016]], p.6 |
| 用全站的觀看來訓練，而不只用推薦帶來的觀看 | YouTube | [[sources/youtube-dnn-2016]], §3.4, p.3 |

**生成式推薦的做法**：
- OneRec 用獎勵壓低內容農場影片的曝光，降低 9.59%（[[sources/onerec]], p.22）。
- OneRec 也宣稱改善了「分發均衡」和冷啟動影片的指標（p.4）。
- HSTU 認為，未來直接生成「一整串推薦」可能比 DPP 這類傳統做法更好，但留待未來研究（[[sources/hstu]], p.18）。

### DPP 是什麼？

**行列式點過程（Determinantal Point Process）**：一種數學工具，挑選一組項目時會同時考慮「每個項目好不好」和「彼此像不像」，越像的組合越吃虧。X 用貼文的 [[concepts/embedding]] 計算相似度（[[sources/x-algorithm]], #Components）。

## 注意

- 這些是**設計意圖**。多樣性實際上加了多少、對使用者有沒有影響，本批來源都沒有提供數據。
- 多樣性和互動指標之間通常有取捨：X 自己就說是「犧牲一點分數」（[[sources/x-algorithm]], #Components）。

## 相關

- [[concepts/filter-bubble]]、[[concepts/ranking]]、[[concepts/cold-start]]、[[concepts/recommendation-funnel]]

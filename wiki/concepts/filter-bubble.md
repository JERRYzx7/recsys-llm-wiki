---
type: concept
title: 過濾泡泡（Filter Bubble）
sources: [tiktok-foryou, x-algorithm, youtube-dnn-2016, tiktok-transparency, guess-2023, haroon-2023, milli-2025]
updated: 2026-11-17
---

# 過濾泡泡（Filter Bubble）

**一句話定義**：推薦系統越來越懂你，結果只給你看你本來就喜歡、本來就同意的東西，讓你接觸的資訊越來越窄。

## 白話解釋

**比喻：只吃自己愛吃的菜。**
- 自助餐廳的服務生發現你每次都拿炸雞，於是乾脆每次都只端炸雞給你。
- 你很開心，但久了營養不均衡，也不知道餐廳其實還有很多好菜。

## 為什麼會發生

- 推薦系統的目標是「你可能會互動的內容」（[[concepts/optimization-objective]]），而最可能互動的通常是**跟你過去很像**的內容。
- TikTok 官方承認這個風險：「過度追求個人化與相關性，有讓影片流越來越同質的風險」（[[sources/tiktok-foryou]], p.2–3）。
- YouTube 也提到，如果只用推薦帶來的觀看來訓練，系統會「過度偏向利用（exploitation）」，新內容很難浮上來（[[sources/youtube-dnn-2016]], §3.4, p.3）。

## 平台說它們怎麼對抗（本批來源）

- **TikTok**：不連續推同一個創作者或同一個音樂；刻意插入不符合你興趣的影片（[[sources/tiktok-foryou]], p.3）。
- **X**：作者多樣性衰減；DPP 重排讓相鄰貼文比較不相似（[[sources/x-algorithm]], #Scoring and Ranking, #Components）。
- **YouTube 2016**：用全站的觀看來訓練，避免只強化推薦本身的結果（[[sources/youtube-dnn-2016]], p.3）。
- **TikTok 新版說明**：相似度檢查會把太像的前幾名換掉（例如同一段配樂）；也提供「重設 For You」讓使用者重新探索（[[sources/tiktok-transparency]], p.8, p.11）。

細節見 [[concepts/diversity-and-exploration]] 和 [[concepts/user-controls]]。

## 重要提醒

- **上面都是平台的自述和設計意圖，不代表實際效果。**

## 實證研究怎麼說（批次 3）

- **YouTube**：推薦以同立場為主。極左和極右假帳號的第 1 個首頁推薦，分別有 58.0% 和 65.5% 是同立場；但也會推一些不同立場的影片（[[sources/haroon-2023]], p.3–4）。
- **Facebook**：演算法動態比時間序多了同立場的內容（53.7% vs. 48.1%），中間立場的內容較少（22.6% vs. 30.9%），作者認為這「可以說符合」同溫層的說法（[[sources/guess-2023]], p.4）。
- **但是**，Facebook 演算法動態裡立場相反的內容也稍多（20.7% vs. 18.7%），可見演算法並沒有把不同觀點完全擋掉（[[sources/guess-2023]], p.4）。
- **照使用者說想看的排序**，反而可能讓同溫更嚴重（[[sources/milli-2025]], p.9–10）。

> [!warning] ⚠️ 爭議：過濾泡泡是演算法造成的，還是人自己選的？
> - **說法 A（演算法有推力）**：控制追蹤對象後，演算法仍然偏向同立場內容（[[sources/guess-2023]], p.4；[[sources/haroon-2023]], p.3–4）。
> - **說法 B（人的選擇也很重要）**：使用者常透過外部連結和訂閱接觸極端頻道（[[sources/milli-2025]], p.2 引述前人研究）；使用者自己挑的內容也偏向同陣營（[[sources/milli-2025]], p.9–10）。
>
> **🧭 wiki 觀點**：兩者都有。演算法會放大同溫，但「人偏好同立場」本身就是很強的力量。Haroon 的證據也顯示，演算法並沒有完全擋掉不同觀點。更完整的整理見 [[syntheses/do-algorithms-polarize]]。

## 相關

- [[concepts/diversity-and-exploration]]、[[concepts/optimization-objective]]、[[teaching/myths-and-facts]]

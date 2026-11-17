---
type: concept
title: 使用者控制工具（User Controls）
sources: [tiktok-transparency, tiktok-foryou, x-algorithm, milli-2025]
updated: 2026-11-17
---

# 使用者控制工具（User Controls）

**一句話定義**：平台提供的按鈕和設定，讓你可以**主動**告訴推薦系統「我不要這個」或「我想重新開始」，而不是只能被動地透過滑動來影響它。

## 白話解釋

**比喻：餐廳點餐時的「不要香菜」。**
- 平常老闆只能觀察你剩下什麼菜來猜你的口味（[[concepts/implicit-feedback|隱式回饋]]）。
- 你也可以直接說「不要香菜」（**關鍵字過濾**）或「這道我不喜歡」（**不感興趣**）。
- 甚至可以說「今天換個口味，什麼都推薦給我試試」（**重設推薦**）。

## 為什麼需要它

- 隱式回饋會誤會你。例如你停在一支影片上可能只是被嚇到，不代表喜歡。主動的控制工具可以讓你直接糾正。
- 這也是「使用者主動權」的問題：推薦系統預設在替你做決定，控制工具讓你拿回一部分決定權（🧭 wiki 觀點）。

## 各平台提供的工具（本 wiki 來源）

| 工具 | 作用 | 平台與出處 |
|---|---|---|
| **不感興趣** | 減少推薦這類內容 | TikTok（[[sources/tiktok-transparency]], p.11；[[sources/tiktok-foryou]], p.2）；X 把「不感興趣」當負面訊號預測（[[sources/x-algorithm]], #Scoring and Ranking） |
| **隱藏創作者或配樂** | 不再推薦特定創作者或使用特定配樂的影片 | TikTok（[[sources/tiktok-foryou]], p.2） |
| **關鍵字過濾／靜音關鍵字** | 濾掉包含特定字詞或 hashtag 的內容 | TikTok（[[sources/tiktok-transparency]], p.11）；X 的 `MutedKeywordFilter`（[[sources/x-algorithm]], #Filtering） |
| **封鎖／靜音帳號** | 不再看到該帳號的內容 | X 的 `AuthorSocialgraphFilter`；封鎖和靜音也是負面訊號（[[sources/x-algorithm]], #Filtering, #Scoring and Ranking） |
| **重設推薦** | 讓推薦頁重新開始，探索新內容 | TikTok 的 For You refresh（[[sources/tiktok-transparency]], p.11） |
| **檢舉** | 送交審核；在 X 也是負面訊號 | TikTok（[[sources/tiktok-transparency]], p.9）；X（[[sources/x-algorithm]], #Scoring and Ranking） |
| **查看自己被貼的標籤** | 了解自己的帳號或貼文是否被限制可見度 | X 的 Under the Hood（[[sources/x-algorithm]], #Under the Hood Label Transparency Tool） |

## 注意事項

- **「不感興趣」的效果有多大，平台沒有公開數據。** TikTok 只說會「限制」這類內容的推薦量（[[sources/tiktok-transparency]], p.11）。
- **主動控制和被動訊號會同時作用**：你按了「不感興趣」，但如果還是常停留在類似內容上，系統可能繼續推（🧭 wiki 觀點，來源未直接說明兩者如何互動）。
- **批次 3 的發現**：
  - Milli 等人指出，在真實平台上，使用者的陳述偏好（問卷、「不要推薦」按鈕）「很少被觀察到」，所以互動訊號仍是主要的排序依據（[[sources/milli-2025]], p.10）。
  - 換句話說，**主動按按鈕很重要**，因為那是少數能讓系統知道「你真正想要什麼」的管道（🧭 wiki 觀點）。
  - 但三篇研究都**沒有直接測量**這些按鈕的效果。
- 見 [[concepts/engagement-vs-stated-preference]]。

## 教學用法

適合放在簡報結尾的「**你可以怎麼做**」：讓學生知道自己不是完全被動，並鼓勵他們實際試試看。

## 相關

- [[concepts/implicit-feedback]]、[[concepts/visibility-filtering]]、[[concepts/filter-bubble]]、[[teaching/guess-the-signal]]

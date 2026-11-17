---
type: concept
title: 冷啟動（Cold Start）
sources: [tiktok-foryou, youtube-dnn-2016, x-algorithm, monolith, onerec]
updated: 2026-11-17
---

# 冷啟動（Cold Start）

**一句話定義**：新使用者沒有任何紀錄，新內容沒人看過，推薦系統「不知道該推什麼給誰」的問題。

## 白話解釋

**比喻：新轉學生的第一天午餐。**
- 學餐阿姨不知道你愛吃什麼，只好先給你今天最多人點的菜（**熱門內容**），或者先問你「你吃不吃辣？」（**選興趣類別**）。
- 吃了幾天後，阿姨就記住你的口味了。

## 為什麼是問題

[[concepts/collaborative-filtering|協同過濾]]靠的是行為紀錄。沒有紀錄，就找不到「和你相似的人」，也不知道「哪些人會喜歡這個新內容」。

## 各平台的做法

### 新使用者

- **TikTok**：請新使用者選興趣類別（例如寵物、旅行）；沒選的人先看熱門影片，再依最初的按讚、留言、重看快速調整（[[sources/tiktok-foryou]], p.2）。
- **YouTube 2016**：用人口統計特徵（地區、裝置、性別、年齡、是否登入）作為「先驗」，讓新使用者也能拿到合理的推薦（[[sources/youtube-dnn-2016]], §3.3, p.3）。
- **X**：新帳號看到的未追蹤貼文必須達到一定的互動門檻（`NewUserMinEngagementFilter`）（[[sources/x-algorithm]], #Filtering）。

### 新內容與新創作者

- **YouTube**：用「樣本年齡」特徵，讓模型懂得新影片剛上架時特別熱門（[[sources/youtube-dnn-2016]], §3.3, p.3）。
- **X**：新作者加成；雜湊 embedding 讓新貼文立刻可以被表示（[[sources/x-algorithm]], #Scoring and Ranking, #Key Design Decisions）。
- **Monolith**：雜湊表可以動態插入新 ID，並用線上訓練快速學到新內容（[[sources/monolith]], §2.1–2.2）。

### 生成式推薦

- OneRec 的語意 ID 讓相似影片共享前綴，「對新影片有更好的泛化」（[[sources/onerec]], p.5）；作者也報告影片冷啟動指標有改善（p.4）。

## 相關

- [[concepts/collaborative-filtering]]、[[concepts/diversity-and-exploration]]、[[concepts/embedding]]、[[teaching/what-the-feed-learns-from-you]]

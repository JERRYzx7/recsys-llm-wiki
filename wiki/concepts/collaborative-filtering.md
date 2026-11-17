---
type: concept
title: 協同過濾（Collaborative Filtering）
sources: [youtube-dnn-2016, x-algorithm, tiktok-foryou, tiktok-transparency, onerec, hstu]
updated: 2026-11-17
---

# 協同過濾（Collaborative Filtering）

**一句話定義**：「跟你口味相似的人喜歡什麼，你可能也會喜歡。」只靠大家的行為紀錄找出相似性，不需要理解內容本身在講什麼。

## 白話解釋

**比喻：問「品味跟你很像的朋友」推薦電影。**
- 你和小明過去喜歡的電影幾乎一樣。
- 小明最近看了一部你沒看過的片，還很喜歡。
- 那這部片推薦給你，成功機率很高。

整個過程完全不需要知道這部片是動作片還是愛情片。

## 為什麼需要它

- 內容的資訊（標題、分類）常常亂七八糟。YouTube 就說影片的 metadata「結構很差，沒有定義良好的分類體系」（[[sources/youtube-dnn-2016]], p.1）。
- 行為資料則非常多，所以「從行為找相似」是最實用的起點。

## 怎麼運作

- **經典做法：矩陣分解（matrix factorization）**。YouTube 在 2016 年之前就是用這種方法，新的深度網路可以看成它的「非線性推廣」（[[sources/youtube-dnn-2016]], p.2）。
- **深度學習版**：YouTube 的候選生成網路「只透過協同過濾提供大致的個人化」（[[sources/youtube-dnn-2016]], §2, p.2）。
- **擴散新發現**：YouTube 用「全站所有觀看」來訓練，不只用推薦帶來的觀看。如果有人從別的管道發現好影片，系統能「透過協同過濾快速擴散給其他人」（[[sources/youtube-dnn-2016]], §3.4, p.3）。
- **分群版**：X 的 SimClusters 依「誰和什麼互動」把帳號和貼文分群，再找候選（[[sources/x-algorithm]], #Components）。
- **TikTok 的說法**：你可能會被推薦「與你興趣相似的其他使用者喜歡的影片」（[[sources/tiktok-foryou]], p.3）。新版說明舉了一個很好懂的例子：有人和你互動過同樣兩支影片，系統就可能推他看過的**第三支**給你（[[sources/tiktok-transparency]], p.5）。課堂遊戲見 [[teaching/guess-the-signal]]。

- **和內容理解結合**：
  - OneRec 的 tokenizer 同時用影片內容（畫面、字幕、語音）和協同訊號，讓「常被同一批人喜歡」的影片表示接近（[[sources/onerec]], §2.1.1, p.5–6）。
  - 作者的案例顯示：只用協同訊號會撈到類別不符的影片，只用內容又只會找到表面相似的影片（p.31–35 附錄 C）。
- **行為比內容更重要**：HSTU 只用內容特徵的版本，召回命中率遠低於用行為的版本（HR@100：11.6% vs. 36.9%）（[[sources/hstu]], Table 6, p.7）。

## 限制

- **冷啟動**：新使用者或新內容沒有行為紀錄，就找不到相似的人，見 [[concepts/cold-start]]。
- **熱門偏誤**：熱門內容出現在很多人的紀錄裡，容易一直被推。這也是為什麼需要[[concepts/diversity-and-exploration|多樣性與探索]]。

## 相關

- [[concepts/retrieval]]、[[concepts/embedding]]、[[concepts/implicit-feedback]]、[[concepts/cold-start]]

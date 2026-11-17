---
type: teaching
title: 課堂遊戲：猜猜演算法在預測什麼？
sources: [tiktok-transparency, x-algorithm, youtube-dnn-2016]
concepts: [optimization-objective, implicit-feedback, diversity-and-exploration, collaborative-filtering, user-controls]
updated: 2026-11-17
---

# 課堂遊戲：猜猜演算法在預測什麼？

## 比喻

**演算法像一個超級八卦的朋友。** 它不只記得你看了什麼，還會猜你「會不會」按讚、會不會看完、會不會點配樂，甚至會不會封鎖對方，然後根據這些猜測決定給你看什麼。

## 遊戲一：「會被預測嗎？」（舉手投票）

念出下面的行為，請學生猜 TikTok 官方有沒有列為「會預測的行為」：

| 行為 | 答案 | 出處 |
|---|---|---|
| 按讚 | ✅ 有 | [[sources/tiktok-transparency]], p.13 |
| 看完影片 | ✅ 有 | p.13 |
| **點擊影片的配樂** | ✅ 有（很多人猜不到！） | p.13 |
| **跟作者的個人頁互動** | ✅ 有 | p.13 |
| 標記「不感興趣」 | ✅ 有，負面行為也會被預測 | p.13 |
| 觀看達到一定時間 | ✅ 有 | p.13 |
| 截圖 | ❓ 官方清單沒有列（清單「並非完整」） | p.12 |

**延伸對照**：X 甚至會預測你會不會**封鎖作者、檢舉**，以及「沒有停留（not dwelled）」（[[sources/x-algorithm]], #Scoring and Ranking）。

## 遊戲二：「為什麼這支被換掉了？」

**情境**：系統排出你的前 3 名影片，結果三支都用同一首爆紅配樂。

**問**：TikTok 會怎麼做？
**答**：相似度檢查會把其中幾支換掉，避免主題重複（[[sources/tiktok-transparency]], p.8）。

**討論**：換掉的影片分數其實比較低。為什麼平台願意「犧牲分數」？（提示：X 的說法是「犧牲一點分數，換取相鄰貼文不那麼相似」（[[sources/x-algorithm]], #Components）。）

## 遊戲三：「第三支影片」

**情境**：你看了 A（貓咪彈鋼琴）和 B（狗狗衝浪）。另一位陌生人也看了 A 和 B，還看了 C（鸚鵡唱歌）。

**問**：系統會推什麼給你？
**答**：很可能推 C。TikTok 官方就是用這個例子說明「別人的行為也會影響你的推薦」（[[sources/tiktok-transparency]], p.5），也就是[[concepts/collaborative-filtering|協同過濾]]。

## 常見迷思 vs. 事實

| 迷思 | 事實（出處） |
|---|---|
| 「演算法只看我按了什麼讚」 | 它預測十多種行為，包括看完、略過、點配樂、觀看時間（[[sources/tiktok-transparency]], p.13） |
| 「國中生拍的影片也可能爆紅上推薦」 | 未滿 16 歲帳號做的內容不會被推上 For You（[[sources/tiktok-transparency]], p.8, p.10） |
| 「推薦頁全是外國網紅」 | TikTok 有規則確保推薦頁包含同地區創作者的內容（[[sources/tiktok-transparency]], p.8） |

## 可上簡報的圖解構想

- 一個「八卦朋友」角色，頭上浮出一排問號泡泡：「會按讚嗎？會看完嗎？會點配樂嗎？會滑走嗎？」每個泡泡旁邊有一個機率數字，最後加總成一顆星星分數。
- 遊戲三：三張動物影片卡，用線把「你」和「陌生人」連起來。

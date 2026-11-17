---
type: source
title: How TikTok recommends videos #ForYou
raw: raw/01-tiktok-foryou.pdf
authors: TikTok（官方 Newsroom，未具名）
year: 2020
venue: TikTok Newsroom 官方部落格（2020-06-18 發布；PDF 為 2026-11-17 網頁列印）
sources: [tiktok-foryou]
updated: 2026-11-17
---

# TikTok 官方說明：For You 怎麼推薦影片（How TikTok recommends videos #ForYou）

**一句話**：TikTok 官方用白話說明 For You 推薦頁會看哪些訊號、怎麼處理新使用者，以及怎麼對付「過濾泡泡」。這是**平台自述**，不是同儕審查的論文。

> 頁碼說明：PDF 共 6 頁，正文在 p.1–3；p.4 有關於透明中心的附註；p.4–6 為網站頁尾與空白頁。

## 背景：它想解決什麼問題

For You 是 TikTok 的核心，也是「大多數使用者花最多時間的地方」（p.1）。這篇文章回應外界對推薦機制的疑問，說明推薦系統的原理、平台如何處理推薦系統的共同問題，以及使用者能怎麼調整自己的推薦（p.1）。

## 核心做法（平台自述）

**1. 推薦依據的三類因素**（p.1–2）：
- **使用者互動**：按讚、分享、追蹤的帳號、留言、自己發布的內容。
- **影片資訊**：字幕、音樂、hashtag。
- **裝置與帳號設定**：語言、國家、裝置類型。這類因素權重較低，因為「使用者並沒有主動表達這些偏好」（p.2）。

**2. 訊號有強弱之分**（p.2）：
- 強訊號，例如是否把一支較長的影片從頭看到尾。
- 弱訊號，例如觀眾和創作者是否在同一個國家。
- 系統依權重排序影片，估計使用者對每支影片感興趣的可能性（p.2）。

**3. 追蹤數「不是直接因素」**（p.2）：
> "neither follower count nor whether the account has had previous high-performing videos are direct factors in the recommendation system."
> （追蹤人數，以及帳號過去是否有爆紅影片，都不是推薦系統的直接因素。）

文章同時承認：追蹤者多的帳號因為累積了較大的粉絲群，影片「可能」會獲得更多觀看（p.2）。

**4. 冷啟動**（p.2）：
- 新使用者可以先選興趣類別（例如寵物、旅行）。
- 沒有選的人會先看到熱門影片，再依最初的按讚、留言、重看來調整推薦。

**5. 負回饋**（p.2）：長按影片選「不感興趣」、隱藏特定創作者或音樂、檢舉，這些都會影響之後的推薦。

## 對抗過濾泡泡與安全措施

- **承認過濾泡泡的風險**：過度追求個人化與相關性，可能讓內容越來越同質（p.2–3）。
- **打斷重複**：一般不會連續推兩支同一個音樂或同一位創作者的影片；不推重複內容、已看過的內容和垃圾內容（p.3）。
- **刻意加入多樣性**：有時會推一些看起來不符合你興趣、按讚數也不高的影片，這是「有意為之」，同時也幫系統了解更廣泛受眾的喜好（p.3）。
- **安全**：部分內容（例如寫實的醫療手術畫面、合法但受管制商品的消費）可能不會被推薦；剛上傳、審查中的影片和刷流量的垃圾內容也可能不會被推薦（p.3）。
- 文章自稱會持續投入研究，對抗「engagement bias」（互動偏誤）（p.3）。
- 附註：洛杉磯的 TikTok 透明中心開放受邀專家檢視演算法與原始碼（p.4）。

## 關鍵數字與結果

- 這份來源**沒有任何量化數字**（沒有權重值或實驗結果），全部是定性描述。

## 限制與注意事項

- **已有較新版本**：TikTok 後來的官方說明頁補充了五步驟流程和預測行為清單，見 [[sources/tiktok-transparency]]。
- **平台自述**：沒有外部驗證，屬於公關與說明性質。
- **年代較早（2020）**：系統在那之後很可能已經改變。
- **沒有技術細節**：沒有模型架構，也沒有優化目標的數學定義。

## 與其他來源的關係

- **補強** [[sources/youtube-dnn-2016]]：兩者都把「看完／觀看時間」當成重要訊號；YouTube 論文提供了技術版本的解釋（p.5, §4）。
- **對照** [[sources/x-algorithm]]：
  - X 明確區分「追蹤中的帳號（in-network）」與「沒有追蹤的帳號（out-of-network）」，並給後者打折（#Scoring and Ranking）。
  - TikTok 則說追蹤數不是直接因素。這是兩個平台的設計差異，不是矛盾，比較見 [[syntheses/platform-pipeline-comparison]]。
- **相關** [[sources/monolith]]：出自同一母公司字節跳動（ByteDance），但 Monolith 論文並沒有說它就是 TikTok 的系統，見 [[entities/bytedance]]。

## 相關頁面

- [[entities/tiktok]]、[[concepts/implicit-feedback]]、[[concepts/cold-start]]、[[concepts/filter-bubble]]、[[concepts/diversity-and-exploration]]、[[concepts/visibility-filtering]]、[[syntheses/platform-transparency]]

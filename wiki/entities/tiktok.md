---
type: entity
title: TikTok
sources: [tiktok-foryou, monolith, tiktok-transparency]
updated: 2026-11-17
---

# TikTok

**是什麼**：字節跳動（[[entities/bytedance]]）旗下的國際版短影音平台，核心是個人化推薦頁「For You」。

## 推薦系統的公開資訊

- **官方部落格（2020）**：[[sources/tiktok-foryou]]
  - 說明推薦因素：互動、影片資訊、裝置與帳號設定。
  - 訊號有強弱之分，「看完長影片」是強訊號。
  - 冷啟動方式：選興趣類別、先看熱門影片。
  - 多樣性措施與安全措施（p.1–3）。
- **官方說法：追蹤數不是直接因素**（[[sources/tiktok-foryou]], p.2）。
- **透明中心**：受邀專家可以在洛杉磯透明中心檢視演算法和原始碼（[[sources/tiktok-foryou]], p.4）。
- **官方推薦系統說明頁（© 2025）**：[[sources/tiktok-transparency]]
  - 五步驟：挑選影片 → 預測 → 排序 → 相似度檢查 → 推薦規則（p.6–8）。
  - 預測十多種行為再合成分數，包括點配樂、觀看一定時間（p.13）。
  - 把「你的追蹤關係」列為訊號（p.13）。
  - 未滿 16 歲的內容不推薦；推薦頁要包含同地區創作者（p.8, p.10）。
  - 使用者工具：不感興趣、關鍵字過濾、重設 For You（p.11）。
- **沒有公開程式碼、模型架構或權重**（截至本 wiki 的來源）。

## 和 Monolith 的關係

[[sources/monolith]] 是字節跳動的論文，摘要提到短影音排序是這類需求的例子（p.1），但論文只說系統用在 BytePlus Recommend，**沒有說用在 TikTok**。所以本 wiki **不能**說「TikTok 用的是 Monolith」，見 [[entities/bytedance]]。

## 時間線

- 2020-06-18：發布〈How TikTok recommends videos #ForYou〉（[[sources/tiktok-foryou]], p.1）。
- 約 2025：官方推薦系統說明頁（頁尾 © 2025，無更新日期）（[[sources/tiktok-transparency]], p.14）。
- 2026-01：TikTok 美國業務改由新成立的 TikTok USDS Joint Venture 經營，演算法要用美國資料重新訓練。⚠️ 目前 raw/ 沒有這份來源，只是待補的線索，不可引用為事實。

## 相關

- [[entities/bytedance]]、[[syntheses/platform-pipeline-comparison]]、[[syntheses/platform-transparency]]

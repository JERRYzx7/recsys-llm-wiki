---
type: entity
title: 字節跳動（ByteDance）
sources: [monolith, tiktok-foryou]
updated: 2026-11-17
---

# 字節跳動（ByteDance）

**是什麼**：中國科技公司，旗下有 [[entities/tiktok]]（國際版）、抖音（中國版），以及對外銷售推薦技術的 BytePlus。

## 推薦系統的公開資訊

- **Monolith（2022）**：[[sources/monolith]]
  - 即時線上訓練加上無碰撞 embedding 表。
  - 論文作者大多是字節跳動員工（p.1）。
  - 已用在 **BytePlus Recommend** 產品（p.1）。
- **TikTok 官方說明（2020）**：[[sources/tiktok-foryou]]。

## ⚠️ 常見誤解：「Monolith 就是 TikTok 的演算法」

- Monolith 論文**只說**系統用在 BytePlus Recommend（[[sources/monolith]], p.1），並以「短影音排序、線上廣告」作為需要即時推薦的例子（p.1）。
- 論文的線上 A/B 實驗是在一個**廣告模型**上做的（p.7, p.9）。
- 🧭 **wiki 觀點**：
  - 可以合理推測，字節跳動內部的推薦系統（包含 TikTok）面臨同樣的需求，可能用了類似技術。
  - 但本 wiki 的來源**沒有直接證據**。教學時應說「TikTok 的母公司發表過這樣的技術」，不要說「TikTok 用的就是這個」。

## 相關

- [[entities/tiktok]]、[[concepts/online-training]]、[[concepts/embedding]]

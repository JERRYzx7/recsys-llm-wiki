---
type: synthesis
title: 平台透明度：部落格、論文、開源程式碼各能告訴我們什麼
sources: [tiktok-foryou, youtube-dnn-2016, monolith, x-algorithm, guess-2023, haroon-2023, milli-2025]
origin: ingest
updated: 2026-11-17
---

# 平台透明度：我們到底能知道多少？

**結論摘要**：
- 本批四份來源代表三種公開方式：官方部落格、工程論文、開源程式碼，可信度和細節程度各不相同。
- **沒有一種方式能告訴我們「演算法實際上對社會造成什麼影響」**，這需要獨立研究。

## 比較

| 公開方式 | 例子 | 能知道什麼 | 不能知道什麼 |
|---|---|---|---|
| **官方部落格** | [[sources/tiktok-foryou]] | 平台想讓大眾理解的原則：訊號種類、多樣性措施（p.1–3） | 技術細節、權重、實際成效；內容無法驗證 |
| **工程論文** | [[sources/youtube-dnn-2016]]、[[sources/monolith]] | 架構、方法、部分實驗數字 | 是否仍在使用、實際線上設定；論文聚焦工程，不談社會影響 |
| **開源程式碼＋README** | [[sources/x-algorithm]] | 管線、權重參數、過濾規則，原則上可以檢查 | 部分規則和 prompt 未公開；實驗中的設定可能和預設值不同（#What's not in this repo?, #Experiments and Configuration） |

## 透明度的兩難

- **公開 → 被鑽漏洞**：X 明說部分規則不公開，是為了降低被規避的風險（[[sources/x-algorithm]], #What's not in this repo?）。
- **X 的折衷**：程式碼加上「結果透明」。Under the Hood 讓使用者看到自己被貼了哪些標籤（[[sources/x-algorithm]], #Under the Hood Label Transparency Tool）。
- **TikTok 的折衷**：讓受邀專家到透明中心看原始碼，但一般大眾看不到（[[sources/tiktok-foryou]], p.4）。

## 🧭 wiki 觀點

- 對教學來說，這三種來源**互補**：
  - 部落格告訴我們「平台想做什麼」。
  - 論文告訴我們「技術上怎麼做」。
  - 程式碼告訴我們「實際上寫了什麼」。
- 但三者都不等於「實際造成什麼結果」。
- 教學時要提醒學生：**平台自述 ≠ 獨立驗證**。

## 第四種管道：獨立研究（批次 3）

| 方式 | 例子 | 能知道什麼 | 限制 |
|---|---|---|---|
| 平台合作實驗 | [[sources/guess-2023]] | 真人、隨機分組、測態度 | 需要平台同意，費用由 Meta 支付（p.6） |
| 外部稽核（假帳號） | [[sources/haroon-2023]] | 不需要平台同意 | 不是真人；Haroon 的作者呼籲平台應更透明（p.7） |
| 使用者外掛加問卷 | [[sources/milli-2025]] | 真實動態、使用者感受 | 單一時間點、樣本有偏 |

方法比較見 [[concepts/algorithmic-audit]]。

🧭 **wiki 觀點**：開源程式碼（X）和透明中心（TikTok）讓外界知道「演算法怎麼寫」；獨立研究才能回答「演算法造成什麼結果」。兩者缺一不可。

## 尚未解決的問題

- 本 wiki 沒有 TikTok 的獨立稽核研究。
- Milli 研究的是 2023 年的 Twitter；X 在 2026 年開源後，是否有研究者用公開程式碼重新驗證，本 wiki 沒有來源。

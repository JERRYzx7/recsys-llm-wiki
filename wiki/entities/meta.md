---
type: entity
title: Meta（Facebook、Instagram 母公司）
sources: [hstu, guess-2023]
updated: 2026-11-17
---

# Meta

**是什麼**：Facebook、Instagram 等社群平台的母公司（背景知識，非本 wiki 來源）。旗下研究單位 Meta AI 發表了生成式推薦架構 HSTU（[[sources/hstu]], p.1）。

## 推薦系統的公開資訊

**HSTU 論文（ICML 2024）**：[[sources/hstu]]
- 作者都隸屬 Meta AI（p.1）。
- 提出生成式推薦（GRs）和 HSTU 架構，模型達 1.5 兆參數（p.1）。
- 部署在「一個擁有數十億使用者的大型網路平台」的多個介面上，A/B 測試提升 12.4%（p.1, Table 7）。
- ⚠️ 論文**沒有寫明**是 Facebook、Instagram 還是其他產品。
- 程式碼開源在 github.com/facebookresearch/generative-recommenders（p.1）。

## 社會影響研究

**Guess 2023（Science）**：[[sources/guess-2023]]
- 2020 美國大選期間，Meta 和外部學者合作，讓約 2.3 萬名 FB 使用者和 2.1 萬名 IG 使用者改用時間序動態 3 個月（p.3）。
- 使用時間和互動大幅下降；內容組成改變；**政治態度沒有可偵測的變化**（p.3–4）。
- 研究費用由 Meta 支付；Meta 沒有發表前審查權（p.6）。
- 論文自述的 FB 動態排序訊號包括互動、使用者滿意度和新聞原創性（p.3）。

## 相關

- [[concepts/generative-recommendation]]、[[concepts/scaling-law]]

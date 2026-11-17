---
type: entity
title: YouTube
sources: [youtube-dnn-2016, haroon-2023]
updated: 2026-11-17
---

# YouTube

**是什麼**：Google 旗下的影音平台。2016 年的論文自稱是「全球最大的影片創作、分享與探索平台」，推薦服務超過十億名使用者（[[sources/youtube-dnn-2016]], p.1）。

## 推薦系統的公開資訊

**2016 年的深度學習推薦論文**：[[sources/youtube-dnn-2016]]
- 兩階段架構：候選生成 → 排序（p.2）。
- 排序目標是「預期觀看時間」，不是點擊率，用來避免標題黨（p.5）。
- 模型約有十億個參數，用數千億筆樣本訓練（p.1）。
- 建立在 Google Brain／TensorFlow 上（p.1）。
- 2016 年以前的系統用矩陣分解（p.2）。

## 時間線

- 2016 年以前：用矩陣分解做候選生成（[[sources/youtube-dnn-2016]], p.2）。
- 2016：發表深度神經網路推薦論文（RecSys '16）。
- 約 2022：Haroon 等人用 10 萬個假帳號稽核 YouTube 推薦（[[sources/haroon-2023]], p.1–2）。
- 其他變化：本 wiki 目前沒有來源。

## 社會影響研究

**Haroon 2023（PNAS）**：[[sources/haroon-2023]]
- 首頁推薦以同立場為主（p.3–4）。
- 一路跟著「下一部」推薦看下去，極端程度只增加一點點，但問題頻道的推薦比例從 1.2% 升到 2.5%（p.5）。
- 有右傾跡象（p.7）。
- 作者引用的數字：YouTube 超過 70% 的觀看來自推薦（p.1，引自 2018 年的報導）。

## 相關

- [[concepts/recommendation-funnel]]、[[concepts/optimization-objective]]、[[syntheses/platform-pipeline-comparison]]

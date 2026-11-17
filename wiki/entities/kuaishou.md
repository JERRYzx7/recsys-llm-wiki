---
type: entity
title: 快手（Kuaishou）
sources: [onerec]
updated: 2026-11-17
---

# 快手（Kuaishou）

**是什麼**：中國的短影音平台，有「快手」和「快手極速版」兩個主要 App（[[sources/onerec]], p.1）。一般認為它是抖音（[[entities/bytedance]]）的主要競爭對手（背景知識，非本 wiki 來源）。

## 推薦系統的公開資訊

**OneRec 技術報告（2025）**：[[sources/onerec]]
- 用一個端到端的生成模型，取代傳統的多階段推薦漏斗（p.3–4）。
- **規模**：主要場景日活 **4 億**（p.23）；尖峰 QPS 超過 40 萬，延遲要求 500 毫秒以內（p.3, p.30）。
- **目標很多**：有「數百個」來自使用者、創作者和平台生態的優化目標（p.3）。
- **部署**：約 25% 的 QPS，是原本用快取應付的那部分流量（p.30）；本地生活服務場景 100%（p.24）。
- **平台治理的例子**：用獎勵壓低「搬運剪輯類內容農場」影片，這類影片的曝光降低 9.59%（p.22）。

## 時間線

- 2025-06：發表 OneRec 技術報告（arXiv v1）；v4 為 2025-09-16（[[sources/onerec]], p.1）。

## 相關

- [[concepts/generative-recommendation]]、[[syntheses/cascade-vs-end-to-end]]、[[concepts/optimization-objective]]

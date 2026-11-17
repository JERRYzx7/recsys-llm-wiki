---
type: entity
title: X（前 Twitter）
sources: [x-algorithm, milli-2025]
updated: 2026-11-17
---

# X（前 Twitter）

**是什麼**：社群平台，前身是 Twitter。首頁的「For You」動態由推薦演算法決定，而且 X 把相關程式碼開源在 GitHub。

## 推薦系統的公開資訊

**開源 repository 與 README**：[[sources/x-algorithm]]
- **候選來源**：Thunder（追蹤中）、Phoenix 雙塔召回、SimClusters、熱門貼文（#Overview）。
- **排序**：Phoenix Transformer 預測十多種行為的機率，再加權成分數（#Scoring and Ranking）。
- **調整**：作者多樣性、未追蹤折扣、新作者加成、DPP 重排（#Scoring and Ranking）。
- **可見度過濾**：和排序分開運作，有四種結果（#Labeling Path）。
- **透明工具「Under the Hood」**：讓使用者看到自己帳號和貼文被貼了哪些影響可見度的標籤（#Under the Hood Label Transparency Tool）。
- **未公開部分**：部分 LLM prompt 和規則，理由是防止有人鑽漏洞（#What's not in this repo?）。

## 社會影響研究

**Milli 2025**：[[sources/milli-2025]]（研究對象是 2023 年 2 月、還叫 Twitter 的時候）
- 互動導向演算法放大黨派性、憤怒、敵視對立陣營的推文（p.6–8）。
- 使用者其實比較不想看演算法挑的政治推文（p.8）。
- 當時的演算法預測 10 種互動，包括「停留至少兩分鐘」（p.2）。
- ⚠️ 2026 年的 X 已經加入負面訊號、DPP 等新機制（[[sources/x-algorithm]]），這些研究結果是否仍然適用，沒有證據。

## 時間線（依 README 的更新紀錄）

- 2026-08-13：公開權重參數、可見度過濾程式碼、Phoenix 訓練程式碼。
- 2026-08-14：說明權重誤解；啟用巴西選舉過濾器。
- 2026-09-18：Under the Hood 加入法律限制資訊。
- 2026-10-08：改善對停留時間的預測。
- 2026-10-13：召回模型也開始訓練去找「會讀完」的貼文。
- 2026-10-26：移除巴西選舉過濾器。

（以上皆見 [[sources/x-algorithm]], #Notable Updates）

## 相關

- [[concepts/visibility-filtering]]、[[concepts/ranking]]、[[syntheses/platform-transparency]]、[[syntheses/platform-pipeline-comparison]]

---
type: concept
title: 可見度過濾與推薦資格（Visibility Filtering / Recommendation Eligibility）
sources: [x-algorithm, tiktok-foryou, tiktok-transparency]
updated: 2026-11-17
---

# 可見度過濾與推薦資格（Visibility Filtering）

**一句話定義**：不管排序分數多高，有些內容會因為安全、法律、垃圾訊息或使用者設定，被禁止推薦、加上警告，或完全不顯示。這是和「排序」分開的一道關卡。

## 白話解釋

**比喻：電視台的播出審查。**
- 節目收視率再高（**排序分數高**），沒通過審查（**可見度過濾**）就不能播。
- 有些節目可以播，但要加上「輔導級」標示（**警告標示**）。
- 有些節目只能在付費頻道播給主動訂閱的人看（**只對追蹤者顯示**）。

## 為什麼要和排序分開

X 把這點列為關鍵設計決策：「排序決定順序，可見度過濾決定能不能顯示。不同服務、不同輸入、不同規則。」（[[sources/x-algorithm]], #Key Design Decisions）

🧭 **wiki 觀點**：分開設計可以讓「好不好看」和「該不該看」兩件事各自負責，也比較容易稽核。

## 怎麼運作（X 的例子）

1. **內容理解**：分類器偵測垃圾訊息、成人內容、暴力內容；帳號則依被封鎖或檢舉的比例、不真實行為、信譽分數評分（[[sources/x-algorithm]], #Labeling Path）。
2. **貼標籤**：規則引擎依事件或分數為帳號和貼文貼標籤（#Labeling Path）。
3. **四種結果**（#Labeling Path）：
   - ALLOW：正常顯示
   - NOTICE：附注意標示
   - INTERSTITIAL：遮罩，點了才看得到
   - DROP：不顯示
4. **「推薦」比「追蹤」更嚴格**：有些規則只對未追蹤帳號的推薦生效，同一則貼文，追蹤者看得到，非追蹤者可能看不到（#Labeling Path, #Filtering）。
5. **法律要求**：例如 2026 年巴西選舉期間的過濾器，選舉後移除（#August 14th, 2026；#October 26th, 2026）。

## TikTok 的說法

- 經審查、被認定可能令一般觀眾震驚的內容（例如寫實的醫療手術畫面、合法但受管制商品的消費）可能**不符合推薦資格**（[[sources/tiktok-foryou]], p.3）。
- 剛上傳或審查中的影片、刷流量的垃圾內容也可能不符合推薦資格（p.3）。
- 新版說明（[[sources/tiktok-transparency]]）：
  - 所有上傳的影片都要經過「機器學習加上人工」的審核。違規的刪除，「不適合廣大受眾」的不推薦（p.9）。
  - **未滿 16 歲帳號**做的內容不會被推上 For You；**13–17 歲帳號**看不到明顯的成人內容（p.10）。
  - 推薦規則要求推薦頁包含**同地區創作者**的內容（p.8）。

## 為什麼這跟社會影響有關

- 「不推薦」不等於「刪除」，但在以推薦為主的平台上，**不被推薦幾乎等於沒人看到**（🧭 wiki 觀點）。
- 這引出透明度問題：使用者知道自己被限制了嗎？X 的「Under the Hood」工具就是在回應這個問題（[[sources/x-algorithm]], #Under the Hood Label Transparency Tool），見 [[syntheses/platform-transparency]]。

## 相關

- [[concepts/recommendation-funnel]]、[[syntheses/platform-transparency]]、[[entities/x-twitter]]

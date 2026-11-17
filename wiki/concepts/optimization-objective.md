---
type: concept
title: 優化目標（Optimization Objective）：點擊、觀看時間、多行為加權
sources: [youtube-dnn-2016, x-algorithm, tiktok-foryou, tiktok-transparency, onerec, hstu, milli-2025, guess-2023]
updated: 2026-11-17
---

# 優化目標（Optimization Objective）

**一句話定義**：推薦系統到底在「最大化」什麼，是點擊、觀看時間，還是一組行為的加權總和。這個選擇決定了系統會推什麼給你。

## 白話解釋

**比喻：老師用什麼標準打分，學生就往哪裡努力。**
- 如果只看「出席率」，學生會來上課但不一定專心。
- 如果只看「考試分數」，學生可能只背考古題。

推薦系統也一樣，它會拚命把你選定的那個數字衝高：
- **只看點擊** → 標題黨。
- **只看停留時間** → 可能推讓你停下來的東西，但不一定是讓你開心的東西。

## 為什麼重要

**模型很少直接優化「使用者滿意」**，因為滿意度量不到，只能挑一個看得到的**代理指標（surrogate／proxy）**。YouTube 明說：推薦常常是在解一個代理問題，而代理問題選得好不好，對 A/B 測試結果的影響「大得不成比例」，卻很難用離線實驗衡量（[[sources/youtube-dnn-2016]], §3.4, p.3）。

## 演變（本批來源）

### 1. 點擊率 → 觀看時間（YouTube 2016）

> "Ranking by click-through rate often promotes deceptive videos that the user does not complete ("clickbait") whereas watch time better captures engagement."（[[sources/youtube-dnn-2016]], p.5）
> （以點擊率排序常會推升使用者不會看完的誘騙影片——標題黨；觀看時間更能反映投入程度。）

做法：用加權邏輯迴歸，讓模型直接學到「預期觀看時間」（§4.2, p.7）。

### 2. 「看完」是強訊號（TikTok 2020）

訊號依強弱加權，看完一支較長的影片屬於強訊號（[[sources/tiktok-foryou]], p.2）。

### 2b. TikTok 也改成預測多種行為（官方說明頁，© 2025）

預測按讚、分享、留言、不感興趣、追蹤作者、看完、略過、收藏、觀看一定時間、點配樂等機率，再「合成一個總分」，但沒有公開權重（[[sources/tiktok-transparency]], p.7, p.13）。

### 3. 多行為預測＋明確加權（X 2026）

- 不預測單一「相關性」，而是預測十多種行為（含負面行為），再用一組寫在程式碼裡的權重合成分數（[[sources/x-algorithm]], #Key Design Decisions, #Scoring and Ranking）。
- 2026-10 的更新加強了「花在貼文上的時間」和「讀完」的預測（#October 8th, 2026；#October 13th, 2026）。

### 4. 用學出來的分數取代人工權重（OneRec 2025）

- OneRec 認為，把點擊、按讚、留言、觀看時間等預測值用**人工調的權重加總**很難調、不夠個人化，目標之間也容易衝突（[[sources/onerec]], §2.4.1, p.10）。
- 改用神經網路學出個人化的「P-Score」，再用強化學習讓模型生成高分的推薦（p.10–12）。
- 對照：X 的權重是**寫在程式碼裡、公開的**（[[sources/x-algorithm]], #Scoring and Ranking）。
- 🧭 **wiki 觀點**：學出來的分數可能更準，但也更不透明，外界很難像看 X 的權重那樣檢查它。

### ⚠️ 代理指標失靈的實例（OneRec）

- 只用「看完率（vtr）」當獎勵時，觀看時間和停留時間上升，但**使用者觀看的影片數明顯下降**。作者明說這「不一定代表高品質推薦」（[[sources/onerec]], p.19–20, Table 6）。
- 作者也承認，獎勵定義不夠好，導致輕微的 **reward hacking**，也就是模型找到拉高分數、卻不見得對使用者好的捷徑（p.21）。
- 這正好印證 YouTube 2016 說的：代理問題的選擇「影響大得不成比例」（[[sources/youtube-dnn-2016]], p.3）。

### 5. 平台目標也寫進獎勵

- 快手有「數百個」來自使用者、創作者和平台生態的目標（[[sources/onerec]], p.3）。
- OneRec 把生態需求直接寫進獎勵，例如壓低內容農場影片的獎勵，讓這類影片的曝光降低 9.59%（p.22）。
- 🧭 **wiki 觀點**：推薦系統優化的從來不只是「你喜歡什麼」，也包含平台想要什麼。

🧭 **wiki 觀點（趨勢）**：從單一指標（點擊）→ 時間類指標 → 多指標加權，並納入負面訊號。各平台都在設法讓代理指標更接近「真正的喜歡」。

## 爭議與社會面（預告）

- TikTok 自己承認要對抗「engagement bias（互動偏誤）」（[[sources/tiktok-foryou]], p.3）。
- HSTU 作者主張，完整的序列建模**可能**減少標題黨和假新聞，讓平台誘因更符合使用者價值，但沒有提出實證（[[sources/hstu]], p.10）。
- 「最大化互動」是否等於「對使用者好」，是社會影響研究的核心問題。
- **批次 3 的實證**：
  - Twitter 的互動導向演算法放大憤怒和敵意內容，而使用者其實比較不想看這些政治推文（[[sources/milli-2025]], p.6–8）。
  - 把 FB/IG 改成時間序後，使用時間大幅下降（[[sources/guess-2023]], p.3），可見互動導向排序確實能衝高使用時間。
  - 見 [[concepts/engagement-vs-stated-preference]] 和 [[syntheses/do-algorithms-polarize]]。

## 相關

- [[concepts/ranking]]、[[concepts/implicit-feedback]]、[[concepts/ab-testing]]、[[concepts/filter-bubble]]、[[teaching/myths-and-facts]]

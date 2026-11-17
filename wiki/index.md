# Index — 推薦演算法：短影音與社群平台如何決定你看什麼

> 這是本 wiki 的內容目錄，每次 ingest 或新增頁面都要同步更新。格式：`- [[path]] — 一句話摘要（來源數 N）`
> 規則見 `AGENTS.md`；時間紀錄見 [[log]]。
> 進度：批次 1 ✅（01, 02, 03, 06）｜單篇 10 ✅｜批次 2 ✅（04, 05）｜批次 3 ✅（07, 08, 09）

## Sources（來源摘要）

- [[sources/tiktok-foryou]] — TikTok 官方部落格（2020）：For You 的推薦因素、冷啟動與多樣性措施（平台自述）（1）
- [[sources/youtube-dnn-2016]] — YouTube 深度學習推薦（RecSys 2016）：兩階段漏斗，排序目標是觀看時間（1）
- [[sources/hstu]] — Meta HSTU（ICML 2024）：生成式推薦、1.5 兆參數、推薦的 scaling law（1）
- [[sources/onerec]] — 快手 OneRec（2025 技術報告）：端到端生成取代多階段漏斗，加上強化學習（1）
- [[sources/monolith]] — 字節跳動 Monolith（2022）：無碰撞 embedding 表加上分鐘級線上訓練（1）
- [[sources/tiktok-transparency]] — TikTok 官方推薦系統說明頁（© 2025）：五步驟、預測十多種行為、未滿 16 歲規則、使用者工具（1）
- [[sources/guess-2023]] — Guess 2023（Science）：FB/IG 改成時間序 3 個月，內容大變、態度沒變（1）
- [[sources/milli-2025]] — Milli（arXiv v6）：Twitter 演算法放大憤怒和敵意；使用者不想看這些政治推文（1）
- [[sources/haroon-2023]] — Haroon 2023（PNAS）：10 萬個假帳號稽核 YouTube；同立場推薦、問題頻道比例上升（1）
- [[sources/x-algorithm]] — X For You 開源 README（2026）：多來源召回、多行為加權打分、可見度過濾（1）

## Concepts（概念）

- [[concepts/recommendation-funnel]] — 推薦漏斗：召回 → 排序 → 重排 → 過濾（3）
- [[concepts/retrieval]] — 召回：從海量內容快速撈出數百則候選（2）
- [[concepts/ranking]] — 排序：預測你的反應並精細打分（4）
- [[concepts/embedding]] — 嵌入向量：處理巨大 ID 空間的四種做法；含「雜湊碰撞」爭議（5）
- [[concepts/collaborative-filtering]] — 協同過濾：口味相似的人喜歡什麼（3）
- [[concepts/implicit-feedback]] — 隱式回饋：看完、停留、滑走都是訊號（4）
- [[concepts/optimization-objective]] — 優化目標：點擊 → 觀看時間 → 多行為加權 → 學出來的獎勵；含 reward hacking 實例（6）
- [[concepts/online-training]] — 線上訓練與概念漂移：模型邊服務邊學（2）
- [[concepts/filter-bubble]] — 過濾泡泡：平台自述的對策、實證研究的發現；含 ⚠️ 爭議（7）
- [[concepts/diversity-and-exploration]] — 多樣性與探索：作者多樣性、DPP、刻意插入新內容（3）
- [[concepts/cold-start]] — 冷啟動：新使用者與新內容怎麼推（4）
- [[concepts/visibility-filtering]] — 可見度過濾：和排序分開的安全與法律關卡（2）
- [[concepts/polarization]] — 極化：議題極化與情感極化；含 ⚠️ 爭議（3）
- [[concepts/engagement-vs-stated-preference]] — 顯示偏好 vs. 陳述偏好：你會點的 ≠ 你想要的（5）
- [[concepts/algorithmic-audit]] — 演算法稽核：假帳號、外掛加問卷、平台合作實驗（3）
- [[concepts/user-controls]] — 使用者控制工具：不感興趣、關鍵字過濾、重設推薦、封鎖（3）
- [[concepts/generative-recommendation]] — 生成式推薦：像 ChatGPT 接龍一樣推薦（3）
- [[concepts/transformer]] — Transformer 與注意力機制：推薦模型的新骨幹（3）
- [[concepts/scaling-law]] — 規模定律：推薦模型也「越大越好」（2）
- [[concepts/ab-testing]] — A/B 測試與離線指標：AUC、MAP，以及讀數字的陷阱（3）

## Entities（平台／系統／公司）

- [[entities/tiktok]] — TikTok：For You 推薦頁，兩份官方說明，未公開程式碼（3）
- [[entities/bytedance]] — 字節跳動：Monolith 的作者；「Monolith ≠ 已證實的 TikTok 系統」（2）
- [[entities/youtube]] — YouTube：2016 年深度學習兩階段推薦（1）
- [[entities/meta]] — Meta：HSTU 作者，部署平台未明說（1）
- [[entities/kuaishou]] — 快手：OneRec，日活 4 億的短影音平台（1）
- [[entities/x-twitter]] — X：開源 For You 演算法，以及 2026 年的更新時間線（1）

## Syntheses（比較／綜合／爭議）

- [[syntheses/platform-pipeline-comparison]] — YouTube、TikTok（2020／2025）、X 推薦管線對照，以及「追蹤」的角色（5）
- [[syntheses/cascade-vs-end-to-end]] — 多階段漏斗 vs. 端到端生成：架構之爭，含 ⚠️ 爭議（5）
- [[syntheses/do-algorithms-polarize]] — 推薦演算法會讓社會更分裂嗎？三篇實證研究的整合（8）
- [[syntheses/platform-transparency]] — 部落格、論文、開源程式碼各能告訴我們什麼（4）

## Teaching（教學素材）

- [[teaching/funnel-analogy]] — 用「選秀節目」解釋推薦漏斗，附課堂活動（2）
- [[teaching/what-the-feed-learns-from-you]] — 你的每個動作都是一張選票（4）
- [[teaching/myths-and-facts]] — 14 個常見迷思與事實（9）
- [[teaching/chronological-feed-debate]] — 課堂辯論：該不該改回時間序？附正反方證據卡（3）
- [[teaching/autocomplete-analogy]] — 推薦也在接龍：輸入法、ChatGPT、選擇題 vs. 申論題（2）
- [[teaching/guess-the-signal]] — 課堂遊戲：猜猜演算法在預測什麼、為什麼被換掉、第三支影片（3）

## Glossary

- [[glossary]] — 49 個術語，附英文與一句白話解釋

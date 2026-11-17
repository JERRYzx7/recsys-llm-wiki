---
type: glossary
title: 詞彙表（Glossary）
sources: [youtube-dnn-2016, monolith, x-algorithm, tiktok-foryou, tiktok-transparency, hstu, onerec, guess-2023, milli-2025, haroon-2023]
updated: 2026-11-17
---

# 詞彙表

> 依英文字母排序。每列包含：術語、英文、一句白話解釋、相關頁。簡報降級時優先使用這裡的白話說法。

| 術語 | English | 一句白話 | 相關頁 |
|---|---|---|---|
| A/B 測試 | A/B Testing | 一部分使用者用新版、另一部分用舊版，比較誰表現好 | [[concepts/ab-testing]] |
| 演算法稽核 | Algorithmic Audit | 外界檢查平台演算法實際推了什麼、造成什麼影響 | [[concepts/algorithmic-audit]] |
| AUC | Area Under the ROC Curve | 模型把「會互動的」排在「不會互動的」前面的機率；0.5 是亂猜 | [[concepts/ab-testing]] |
| 注意力機制 | Attention | 模型讀序列時，決定每一筆紀錄要給多少重視 | [[concepts/transformer]] |
| 候選生成 | Candidate Generation | 召回的另一個說法 | [[concepts/retrieval]] |
| 標題黨 | Clickbait | 讓人想點、點進去卻不想看完的內容 | [[concepts/optimization-objective]] |
| 串接架構／多階段漏斗 | Cascade Architecture | 召回、粗排、精排一關接一關的傳統架構 | [[syntheses/cascade-vs-end-to-end]] |
| 時間序動態 | Chronological Feed | 不用演算法，最新的貼文排最前面 | [[teaching/chronological-feed-debate]] |
| 冷啟動 | Cold Start | 新使用者或新內容沒有紀錄，不知道該推給誰 | [[concepts/cold-start]] |
| 協同過濾 | Collaborative Filtering | 「跟你口味像的人喜歡什麼，你可能也喜歡」 | [[concepts/collaborative-filtering]] |
| 概念漂移 | Concept Drift | 使用者興趣或資料分布隨時間改變 | [[concepts/online-training]] |
| 行列式點過程 | Determinantal Point Process (DPP) | 挑內容時同時考慮「好不好」和「彼此像不像」的數學工具 | [[concepts/diversity-and-exploration]] |
| 停留 | Dwell | 你在一則內容上停下來看的行為或時間 | [[concepts/implicit-feedback]] |
| 深度學習推薦模型 | DLRM (Deep Learning Recommendation Model) | 2016 年起的主流推薦模型，用大量人工特徵和多個專用模組 | [[concepts/generative-recommendation]] |
| 嵌入向量 | Embedding |
| 端到端 | End-to-End | 一個模型從輸入直接做到輸出，中間不分好幾個系統 | [[syntheses/cascade-vs-end-to-end]] | 把一個編號（使用者、影片）變成一串可以計算相似度的數字 | [[concepts/embedding]] |
| 互動導向排序 | Engagement-based Ranking | 依「你會不會點、看多久、會不會轉發」來排序 | [[concepts/engagement-vs-stated-preference]] |
| 探索／利用 | Exploration / Exploitation | 試新東西 vs. 推穩拿分的東西 | [[concepts/diversity-and-exploration]] |
| 生成式推薦 | Generative Recommendation | 像 ChatGPT 接龍一樣，預測你的下一個行為或下一支影片 | [[concepts/generative-recommendation]] |
| 特徵 | Feature | 模型的輸入資訊，例如觀看歷史、語言、裝置 | [[concepts/ranking]] |
| 過濾泡泡 | Filter Bubble | 只看到自己本來就喜歡或同意的內容，視野越來越窄 | [[concepts/filter-bubble]] |
| 雜湊／雜湊碰撞 | Hashing / Hash Collision | 把大量 ID 壓進較小的表；不同 ID 撞在同一格叫碰撞 | [[concepts/embedding]] |
| 情感極化／議題極化 | Affective / Issue Polarization | 越來越討厭對方陣營的人／政策看法越來越兩極 | [[concepts/polarization]] |
| 隱式回饋 | Implicit Feedback | 沒明說喜歡，但用行為（看完、停留）透露偏好 | [[concepts/implicit-feedback]] |
| 追蹤中／未追蹤 | In-Network / Out-of-Network | 來自你追蹤的帳號 vs. 你沒追蹤的帳號 | [[entities/x-twitter]] |
| 矩陣分解 | Matrix Factorization | 經典協同過濾方法，把「使用者 × 內容」表格拆成兩組向量 | [[concepts/collaborative-filtering]] |
| 混合專家 | Mixture of Experts (MoE) | 模型裡有很多「專家」子網路，每次只叫幾個來處理，用來擴大模型又省算力 | [[concepts/transformer]] |
| 線上訓練 | Online Training | 模型上線後持續用最新行為更新自己 | [[concepts/online-training]] |
| 優化目標 | Optimization Objective | 系統努力想衝高的那個數字 | [[concepts/optimization-objective]] |
| 問題頻道 | Problematic Channels | 研究者整理的陰謀論、極端主義等頻道清單 | [[sources/haroon-2023]] |
| 兔子洞 | Rabbit Hole | 跟著推薦一路看下去，被帶到越來越極端的內容 | [[concepts/filter-bubble]] |
| 排序 | Ranking | 對候選內容精細打分、由高到低排列 | [[concepts/ranking]] |
| 推薦資格 | Recommendation Eligibility | 內容可以存在平台上，但不一定「有資格」被推薦給陌生人 | [[concepts/visibility-filtering]] |
| 推薦漏斗 | Recommendation Funnel | 先粗篩、再細排、最後調整的多階段流程 | [[concepts/recommendation-funnel]] |
| 強化學習 | Reinforcement Learning (RL) | 讓模型試做、依獎勵分數調整，越做越好 | [[concepts/optimization-objective]] |
| 召回 | Retrieval |
| 獎勵投機 | Reward Hacking | 模型找到拉高獎勵分數、卻不是真的變好的捷徑 | [[concepts/optimization-objective]] |
| 顯示偏好 | Revealed Preference | 從你的行為（看多久、點什麼）推測你想要什麼 | [[concepts/engagement-vs-stated-preference]] |
| 規模定律 | Scaling Law | 模型、資料、算力越大，效果穩定可預測地變好 | [[concepts/scaling-law]] |
| 語意 ID | Semantic ID | 把一支影片編成幾個由粗到細的 token，相似影片前綴相同 | [[concepts/embedding]] | 從海量內容中快速撈出幾百則候選 | [[concepts/retrieval]] |
| 代理指標／代理問題 | Surrogate / Proxy | 量不到真正的滿意度，只好改量一個看得到的替代數字 | [[concepts/optimization-objective]] |
| 相似度檢查 | Similarity Check | TikTok 排序後，前幾名太像（例如同一段配樂）就換掉 | [[concepts/diversity-and-exploration]] |
| 假帳號稽核 | Sock Puppet Audit | 用大量自動化假帳號，觀察演算法推薦什麼 | [[concepts/algorithmic-audit]] |
| 陳述偏好 | Stated Preference | 直接問你想看什麼 | [[concepts/engagement-vs-stated-preference]] |
| Transformer | Transformer | 用「注意力」處理序列的神經網路架構；ChatGPT、X 的排序模型、HSTU、OneRec 都用它 | [[concepts/transformer]] |
| 使用者控制工具 | User Controls | 不感興趣、關鍵字過濾、重設推薦等「主動告訴演算法」的按鈕 | [[concepts/user-controls]] |
| 雙塔模型 | Two-Tower Model | 使用者一座塔、內容一座塔，各自變成向量再比相似度 | [[concepts/retrieval]] |
| 可見度過濾 | Visibility Filtering | 決定一則內容能不能顯示、要不要加警告 | [[concepts/visibility-filtering]] |
| 觀看時間 | Watch Time | 使用者實際看了多久；YouTube 2016 的排序目標 | [[concepts/optimization-objective]] |

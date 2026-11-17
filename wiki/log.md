# Log

> 只能往後追加，不修改舊紀錄。格式：`## [YYYY-MM-DD] <ingest|query|lint|slides|schema> | <標題>`
> 最近紀錄：`grep "^## \[" wiki/log.md | tail -5`

## [2026-11-17] schema | 建立 wiki 骨架
- 變更：新增 AGENTS.md、CLAUDE.md、.claude/skills/{wiki-ingest,wiki-lint,wiki-slides}、wiki/index.md、wiki/log.md、wiki/glossary.md、wiki/{sources,concepts,entities,syntheses,teaching}/、output/、.raw-manifest.md5（9 份 raw 的 MD5）
- 備註：來源 9 份，分三批 ingest（1：01/02/03/06；2：04/05；3：07/08/09）。下一步：批次 1 ingest。

## [2026-11-17] ingest | 批次 1：工業界技術（01 TikTok、02 YouTube DNN、03 Monolith、06 X README）
- 新增 sources（4）：tiktok-foryou、youtube-dnn-2016、monolith、x-algorithm
- 新增 concepts（13）：recommendation-funnel、retrieval、ranking、embedding、collaborative-filtering、implicit-feedback、optimization-objective、online-training、filter-bubble、diversity-and-exploration、cold-start、visibility-filtering、ab-testing
- 新增 entities（4）：tiktok、bytedance、youtube、x-twitter
- 新增 syntheses（2）：platform-pipeline-comparison、platform-transparency
- 新增 teaching（3）：funnel-analogy、what-the-feed-learns-from-you、myths-and-facts
- 更新：glossary（27 個術語）、index
- 爭議：①雜湊碰撞（Monolith vs. X）→ concepts/embedding；②「追蹤」的角色（TikTok vs. X）→ syntheses/platform-pipeline-comparison。兩者都判定為「不同取捨或定位」，不是直接矛盾
- 備註：Monolith 論文沒有說用在 TikTok，已在 bytedance 和 myths 頁註明；Monolith 的 Table 3「AUC 提升 14–18%」沒有定義計算方式，已標示要保守引用
- 待辦：Transformer 被 5 頁提到但沒有獨立頁面，留到批次 2（HSTU）建立 concepts/transformer 一併處理

## [2026-11-17] lint | 批次 1 後
- 結構：5 項全數 OK（29 頁）
- 內容：#6 補上 7 處數字的頁碼；#7 把「追蹤」的爭議改成標準 ⚠️ 區塊；#9 所有 concept 頁都有白話解釋；#10 補齊 3 處 🧭 標記；修正 3 個表格內的別名連結（Obsidian 會把 `|` 當成表格分隔線）
- #8：Transformer（5 頁）、Phoenix（6 頁）、SimClusters（5 頁）沒有獨立頁面。Phoenix 和 SimClusters 屬於 X 的元件，由 entities/x-twitter 涵蓋；Transformer 留到批次 2
- 待人類決定：見批次 1 回報

## [2026-11-17] ingest | 單篇：10 TikTok 官方推薦系統說明頁（© 2025）
- 流程：照單篇模式，先跟人類討論 5 個重點；人類指示「要有趣一點」、新增 user-controls、raw 檔改名為 10-tiktok-transparency.pdf
- 新增：sources/tiktok-transparency、concepts/user-controls、teaching/guess-the-signal
- 更新：entities/tiktok、sources/tiktok-foryou、concepts/{recommendation-funnel, optimization-objective, collaborative-filtering, visibility-filtering, diversity-and-exploration, implicit-feedback, filter-bubble}、syntheses/platform-pipeline-comparison（TikTok 欄改成 2020→2025；「追蹤」爭議加入說法 A'）、teaching/myths-and-facts（修正 #1，新增 #8 #9）、glossary（+3 個術語）、index
- 爭議更新：「追蹤」——區分「創作者有多少粉絲」和「你追蹤了誰」；新版把後者列為訊號，判定不是矛盾
- 備註：TikTok USDS Joint Venture（2026-01）只寫在 entities/tiktok 的時間線，標為「待補來源、不可引用」

## [2026-11-17] schema | 來源清單新增第 10 份
- AGENTS.md §3 加入 10-tiktok-transparency.pdf（單篇）；來源總數 9 → 10

## [2026-11-17] lint | 單篇 10 後
- 結構：1–4 項 OK（32 頁）；第 5 項有 1 個問題：raw 檔尚未改名，所以 MD5 還沒登記（等人類改名後補登記）

## [2026-11-17] lint | raw 10 改名後
- 人類已把檔案改名為 raw/10-tiktok-transparency.pdf；MD5 已追加到 .raw-manifest.md5
- 結構：5 項全部 OK（32 頁）

## [2026-11-17] ingest | 批次 2：生成式推薦（04 HSTU、05 OneRec）
- 讀法：PDF 超過 20 頁，用 macOS PDFKit 把文字抽到 scratchpad 再讀（raw/ 沒有變動）。HSTU 正文與 Impact Statement、附錄 A–B 細讀，附錄 C–H（GPU 實作）看過節標題；OneRec 正文與附錄 B 細讀，附錄 C 案例略讀
- 新增 sources（2）：hstu、onerec
- 新增 concepts（3）：generative-recommendation、transformer（處理批次 1 留下的 #8 待辦）、scaling-law
- 新增 entities（2）：meta、kuaishou
- 新增 syntheses（1）：cascade-vs-end-to-end（含 ⚠️ 爭議：漏斗會被端到端取代嗎）
- 新增 teaching（1）：autocomplete-analogy
- 更新：concepts/{embedding（第四種做法：語意 ID）, optimization-objective（P-Score、reward hacking 實例、平台目標寫進獎勵）, recommendation-funnel, ranking, retrieval, online-training, collaborative-filtering, diversity-and-exploration, cold-start, ab-testing（顯著門檻、實驗範圍）}、syntheses/platform-pipeline-comparison、teaching/myths-and-facts（+#10 #11）、glossary（+10 個術語 → 40 個）、index
- 重要註記：①OneRec 的「25% QPS」是原本用快取應付的流量（附錄 B p.30）；②HSTU 沒有寫明部署平台；③HSTU 的 Impact Statement 宣稱可能減少標題黨和假新聞，但沒有實證，待批次 3 對照
- 背景知識標註：Meta 是 Facebook 和 Instagram 的母公司、快手與抖音是競爭對手（皆已標「非本 wiki 來源」）

## [2026-11-17] lint | 批次 2 後
- 結構：5 項全數 OK（41 頁）
- 內容：#6 補上 7 處頁碼；#9 所有 concept 頁都有白話解釋；#10 🧭 標記齊全；表格內沒有別名連結
- #8：批次 1 留下的 Transformer 已建頁

## [2026-11-17] schema | 批次 2 確認
- 人類決定：「漏斗 vs. 端到端」在簡報只用一頁帶過（已寫進 syntheses/cascade-vs-end-to-end）；批次 3 照原計畫一次做完

## [2026-11-17] ingest | 批次 3：社會影響（07 Milli、08 Guess、09 Haroon）
- 讀法：PDFKit 抽文字到 scratchpad。Guess 正文加兩份勘誤（p.1–10）全讀；Haroon 全讀（p.1–8）；Milli 正文 p.1–12 全讀，補充資料讀了目錄、S1（方法、樣本）、S2 摘要，其餘表格和問卷沒有逐頁細讀
- 新增 sources（3）：guess-2023、milli-2025、haroon-2023
- 新增 concepts（3）：polarization、engagement-vs-stated-preference、algorithmic-audit
- 新增 syntheses（1）：do-algorithms-polarize（核心整合頁，含 ⚠️ 爭議與「因果鏈」觀點）
- 新增 teaching（1）：chronological-feed-debate（正反方證據卡）
- 更新：concepts/{filter-bubble（實證 + ⚠️ 爭議：演算法 vs. 人的選擇）, optimization-objective, user-controls}、syntheses/platform-transparency（第四種管道：獨立研究）、entities/{meta, youtube, x-twitter}、sources/hstu（Impact Statement 連到整合頁）、teaching/myths-and-facts（+#12–14）、glossary（→ 49 個術語）、index
- 註記：①Milli 的 raw 是 arXiv v6（2024-12），檔名標 2025，期刊正式版資訊不在 raw 中；②Haroon 的摘要和引言對「遇到問題頻道的比例」說法不一致（36.1% vs. 32%），以結果段落為準；③Guess 有兩份勘誤，只影響 Instagram 的指標
- 🧭 主要觀點：三篇研究測的是因果鏈上的不同環節，所以不矛盾；證據較支持「演算法放大分裂性內容、影響短期感受」，而不是「演算法是極化主因」

## [2026-11-17] lint | 批次 3 後（全部 10 份來源 ingest 完畢）
- 結構：5 項全數 OK（49 頁）
- 內容：#6 補上 9 處頁碼；#7 新增 2 個 ⚠️ 爭議區塊（polarization、filter-bubble），加上整合頁；#9 所有 concept 頁都有白話解釋；#10 🧭 標記齊全

## [2026-11-17] lint | 簡報前
- 結構：5 項全數 OK（49 頁）；內容檢查沿用批次 3 後的結果，沒有新增頁面

## [2026-11-17] slides | output/recsys-slides.html
- 28 頁，單一 HTML 檔，沒有外部資源；← → 翻頁、N 講者備忘、T 切換黑板／白紙；寬度 760px 以下改成可捲動的講義模式
- 設計：依人類要求「不要太 AI 美感」，採「老師批改考卷」的風格：白紙或黑板、楷體／明體標題、只在關鍵數字畫紅筆圈（暗色模式改用黃色粉筆）
- 取材頁：concepts/{recommendation-funnel, implicit-feedback, collaborative-filtering, optimization-objective, diversity-and-exploration, visibility-filtering, online-training, generative-recommendation, engagement-vs-stated-preference, polarization, user-controls}、sources/*（10 份）、syntheses/{do-algorithms-polarize, cascade-vs-end-to-end}、teaching/{funnel-analogy, guess-the-signal, chronological-feed-debate, myths-and-facts, autocomplete-analogy}
- 照人類決定：漏斗 vs. 端到端只用一頁（第 15 頁）；wiki 觀點標示為「本課整理的觀點」（第 23 頁）
- 驗證：headless Chrome 截圖檢查 28 頁（深色、淺色、600px 寬），修正 CSS 權重衝突（出處和頁碼被放大）、圖表標籤重疊、參考資料溢出；用模擬按鍵測試翻頁、逐步揭曉、備忘和主題切換，沒有 JS 錯誤；28 頁都有講者備忘
- 尚缺：沒有 TikTok 和快手的獨立社會影響研究；TikTok 美國合資公司（2026）沒有 raw 來源，所以沒放進簡報

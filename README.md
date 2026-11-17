# recsys-llm-wiki

推薦演算法：短影音與社群平台如何決定你看什麼。依照 [Karpathy 的 LLM Wiki 構想](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 建立的知識庫，用來產生給大學生的教學簡報。

- `wiki/`：LLM 維護的知識庫（從 `wiki/index.md` 開始看，建議用 Obsidian 開啟）
- `output/recsys-slides.html`：教學簡報（單一 HTML 檔，離線可開）
- `AGENTS.md`：wiki 的規則；`.claude/skills/`：ingest、lint、簡報流程

`raw/` 的原始論文與網頁受出版社版權保護，**沒有放進 repo**。各來源的書目資訊見 `wiki/sources/`，`.raw-manifest.md5` 記錄了原始檔的雜湊值。在沒有 `raw/` 的環境跑 lint，第 5 項（raw 完整性）會報缺檔，這是預期的結果。

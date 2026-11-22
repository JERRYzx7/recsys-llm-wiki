#!/usr/bin/env python3
"""把 wiki/ 與 report/ 的 Markdown 建成 GitHub Pages 靜態網站。

在 my-wiki/ 執行：  python3 tools/build_site.py
需要：pip install markdown

產出（全部可重建，不要手改）：
  index.html            首頁
  slides.html           簡報頁（上方導覽列 + 內嵌 output/recsys-slides.html）
  workflow.html         ← report/workflow.md
  record.html           ← report/record.md
  reflection.html       ← report/reflection.md
  wiki-html/**.html     ← wiki/**.md
"""
from __future__ import annotations

import html
import os
import re
import shutil
from pathlib import Path

import markdown
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
REPORT = ROOT / "report"
OUT_WIKI = ROOT / "wiki-html"

NAV = [
    ("home", "首頁", "index.html"),
    ("wiki", "Wiki", "wiki-html/index.html"),
    ("slides", "簡報", "slides.html"),
    ("workflow", "流程設計", "workflow.html"),
    ("record", "執行紀錄", "record.html"),
    ("reflection", "反思", "reflection.html"),
]

GROUPS = [
    ("sources", "Sources 來源"),
    ("concepts", "Concepts 概念"),
    ("entities", "Entities 平台與公司"),
    ("syntheses", "Syntheses 跨來源整合"),
    ("teaching", "Teaching 教學素材"),
]
TYPE_LABEL = {"source": "來源", "concept": "概念", "entity": "實體", "synthesis": "整合",
              "teaching": "教學", "glossary": "詞彙表"}

# 來源頁在內文引用時用短名稱（例如「Guess 2023」），比完整論文標題好讀
SOURCE_LABEL = {
    "tiktok-foryou": "TikTok 2020", "youtube-dnn-2016": "YouTube 2016", "monolith": "Monolith 2022",
    "x-algorithm": "X 開源 README", "hstu": "HSTU 2024", "onerec": "OneRec 2025",
    "milli-2025": "Milli", "guess-2023": "Guess 2023", "haroon-2023": "Haroon 2023",
    "tiktok-transparency": "TikTok 說明頁 2025",
}

WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#([^\]|]*))?(?:\\?\|([^\]]*))?\]\]")
FENCE = re.compile(r"^(```|~~~)")


# ---------------------------------------------------------------- parsing
def split_frontmatter(text: str) -> tuple[dict, str]:
    meta: dict = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    v = v.strip().strip('"')
                    if v.startswith("[") and v.endswith("]"):
                        v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                    meta[k.strip()] = v
            text = text[end + 4:].lstrip("\n")
    return meta, text


def short_title(pid: str, title: str) -> str:
    group, _, slug = pid.partition("/")
    if group == "sources":
        return SOURCE_LABEL.get(slug, slug)
    return re.split(r"（|\(", title)[0].strip() or title


def fix_blocks(lines: list[str]) -> list[str]:
    """Obsidian 允許清單／表格緊接在段落後、巢狀清單縮 2 格；Python-Markdown 不行，這裡補齊。"""
    out: list[str] = []
    in_code = False
    quote_buf: list[str] = []

    def flush_quote():
        if quote_buf:
            inner = fix_blocks([re.sub(r"^> ?", "", q) for q in quote_buf])
            out.extend(("> " + q) if q else ">" for q in inner)
            quote_buf.clear()

    for line in lines:
        if FENCE.match(line.lstrip()):
            flush_quote()
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue
        if line.startswith(">"):
            quote_buf.append(line)
            continue
        flush_quote()
        m = re.match(r"^( +)([-*+]|\d+\.) ", line)
        if m and len(m.group(1)) < 4:  # 2 格縮排的巢狀清單 → 4 格
            line = " " * (len(m.group(1)) * 2) + line.lstrip(" ")
        is_list = bool(re.match(r"^([-*+]|\d+\.) ", line))
        is_table = line.startswith("|")
        prev = out[-1] if out else ""
        prev_list = bool(re.match(r"^\s*([-*+]|\d+\.) ", prev))
        prev_table = prev.startswith("|")
        if prev.strip() and not prev.startswith((" ", "\t")):
            if (is_list and not prev_list) or (is_table and not prev_table):
                out.append("")
        out.append(line)
    flush_quote()
    return out


# ---------------------------------------------------------------- site model
class Site:
    def __init__(self):
        self.pages: dict[str, dict] = {}
        for p in sorted(WIKI.rglob("*.md")):
            pid = p.relative_to(WIKI).with_suffix("").as_posix()
            meta, body = split_frontmatter(p.read_text(encoding="utf-8"))
            title = meta.get("title") or {"index": "Wiki 目錄", "log": "操作紀錄（log）"}.get(pid, pid)
            self.pages[pid] = {"meta": meta, "body": body, "title": title,
                               "short": short_title(pid, title), "links": set()}
        for pid, pg in self.pages.items():
            pg["links"] = {m.group(1).strip() for m in WIKILINK.finditer(strip_code(pg["body"]))}
        self.backlinks = {pid: sorted(o for o, pg in self.pages.items() if pid in pg["links"] and o != pid)
                          for pid in self.pages}

    def wiki_href(self, pid: str, from_file: Path) -> str:
        target = OUT_WIKI / f"{pid}.html"
        return os.path.relpath(target, from_file.parent).replace(os.sep, "/")


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```|`[^`\n]*`", "", text, flags=re.S)


def render_md(site: Site, text: str, out_file: Path) -> str:
    def link(m: re.Match) -> str:
        pid, anchor, alias = m.group(1).strip(), m.group(2), m.group(3)
        pid = pid.removesuffix(".md")
        if pid not in site.pages:
            return html.escape(alias or pid)
        label = alias or site.pages[pid]["short"]
        href = site.wiki_href(pid, out_file)
        if anchor:
            href += "#" + slugify_unicode(anchor.strip(), "-")
        return f"[{label}]({href})"

    # 只替換不在 code 裡的 wikilink
    parts = re.split(r"(```.*?```|`[^`\n]*`)", text, flags=re.S)
    text = "".join(p if p.startswith("`") else WIKILINK.sub(link, p) for p in parts)
    text = "\n".join(fix_blocks(text.split("\n")))

    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "attr_list",
                                       "toc"],
                           extension_configs={"toc": {"slugify": slugify_unicode}})
    out = md.convert(text)
    # mermaid
    out = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                 r'<pre class="mermaid">\1</pre>', out, flags=re.S)
    # Obsidian callout：> [!warning] 標題
    out = re.sub(r"<blockquote>\s*<p>\[!(\w+)\]\s*(.*?)(?:</p>|<br\s*/?>)(.*?)</blockquote>",
                 lambda m: f'<aside class="callout {m.group(1)}"><p class="callout-title">{m.group(2)}</p>'
                           f'{m.group(3) if m.group(3).strip().startswith("<") else "<p>" + m.group(3)}</aside>',
                 out, flags=re.S)
    # 表格包一層，窄螢幕可以橫向捲動
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out


# ---------------------------------------------------------------- templates
def page(title: str, active: str, depth: int, content: str, *, body_class: str = "",
         extra_head: str = "", description: str = "") -> str:
    root = "../" * depth
    nav = "".join(
        f'<a href="{root}{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a>'
        for key, label, href in NAV)
    return f"""<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description or '推薦演算法 LLM Wiki 與教學簡報')}">
<link rel="stylesheet" href="{root}assets/site.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
{extra_head}
</head>
<body class="{body_class}">
<header class="site-header">
  <a class="brand" href="{root}index.html">推薦演算法 <span>LLM Wiki</span></a>
  <nav class="site-nav" aria-label="主要導覽">{nav}</nav>
  <button class="theme-btn" type="button" aria-label="切換黑板／白紙">黑板</button>
</header>
{content}
<script src="{root}assets/site.js"></script>
</body>
</html>
"""


MERMAID = """<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
const dark = document.documentElement.dataset.theme === 'dark' ||
  (!document.documentElement.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
mermaid.initialize({startOnLoad: true, theme: dark ? 'dark' : 'neutral', fontFamily: 'PingFang TC, Noto Sans TC, sans-serif'});
</script>"""


def sidebar(site: Site, current: str, out_file: Path) -> str:
    groups = []
    for key, label in GROUPS:
        items = sorted((pid for pid in site.pages if pid.startswith(key + "/")),
                       key=lambda p: site.pages[p]["short"])
        lis = "".join(
            f'<li><a href="{site.wiki_href(pid, out_file)}"{" aria-current=\"page\"" if pid == current else ""}>'
            f'{html.escape(site.pages[pid]["short"])}</a></li>' for pid in items)
        groups.append(f'<div class="side-group"><h3>{label}<span>{len(items)}</span></h3><ul>{lis}</ul></div>')
    misc = "".join(
        f'<li><a href="{site.wiki_href(pid, out_file)}"{" aria-current=\"page\"" if pid == current else ""}>{name}</a></li>'
        for pid, name in [("index", "目錄 index"), ("glossary", "詞彙表 glossary"), ("log", "操作紀錄 log")])
    return f"""<aside class="wiki-side">
<details class="side-details" open>
<summary>全部頁面（{len(site.pages)}）</summary>
<input class="side-search" type="search" placeholder="搜尋頁面…" aria-label="搜尋頁面">
<div class="side-group"><ul>{misc}</ul></div>
{''.join(groups)}
</details>
</aside>"""


def build_wiki(site: Site):
    if OUT_WIKI.exists():
        shutil.rmtree(OUT_WIKI)
    for pid, pg in site.pages.items():
        out_file = OUT_WIKI / f"{pid}.html"
        out_file.parent.mkdir(parents=True, exist_ok=True)
        depth = len(Path(pid).parts)
        meta = pg["meta"]
        chips = []
        if meta.get("type"):
            chips.append(f'<span class="chip type">{TYPE_LABEL.get(meta["type"], meta["type"])}</span>')
        srcs = meta.get("sources") or []
        if isinstance(srcs, list) and srcs and pid != "glossary":
            chips.append("<span class='chip-label'>引用來源</span>" + "".join(
                f'<a class="chip" href="{site.wiki_href("sources/" + s, out_file)}">'
                f'{html.escape(SOURCE_LABEL.get(s, s))}</a>' for s in srcs if f"sources/{s}" in site.pages))
        if meta.get("updated"):
            chips.append(f'<span class="chip-label">更新 {html.escape(str(meta["updated"]))}</span>')
        if meta.get("raw"):
            chips.append(f'<span class="chip-label">原始檔 {html.escape(meta["raw"])}（未公開）</span>')
        back = site.backlinks.get(pid, [])
        back_html = ""
        if back and pid not in ("index", "log"):
            back_html = ('<section class="backlinks"><h2>哪些頁面連到這裡</h2><ul>' + "".join(
                f'<li><a href="{site.wiki_href(b, out_file)}">{html.escape(site.pages[b]["short"])}</a>'
                f'<span>{TYPE_LABEL.get(site.pages[b]["meta"].get("type", ""), "")}</span></li>' for b in back)
                + "</ul></section>")
        body = render_md(site, pg["body"], out_file)
        crumbs = f'<a href="{site.wiki_href("index", out_file)}">Wiki</a>'
        if "/" in pid:
            crumbs += f' / {dict(GROUPS)[pid.split("/")[0]].split(" ")[0]}'
        content = f"""<div class="wiki-layout">
{sidebar(site, pid, out_file)}
<main class="wiki-main prose">
<p class="crumbs">{crumbs}</p>
<div class="meta-row">{''.join(chips)}</div>
{body}
{back_html}
<p class="src-note">這一頁由 <code>wiki/{pid}.md</code> 自動轉成網頁；原檔可用 Obsidian 開啟。</p>
</main>
</div>"""
        extra = MERMAID if 'class="mermaid"' in body else ""
        (out_file).write_text(page(f'{pg["short"]}｜推薦演算法 Wiki', "wiki", depth, content,
                                   body_class="wiki", extra_head=extra), encoding="utf-8")


def build_report(site: Site, name: str, active: str):
    src = REPORT / f"{name}.md"
    out_file = ROOT / f"{active}.html"
    meta, text = split_frontmatter(src.read_text(encoding="utf-8"))
    body = render_md(site, text, out_file)
    content = f'<main class="report prose">{body}</main>'
    extra = MERMAID if 'class="mermaid"' in body else ""
    out_file.write_text(page(meta.get("title", name), active, 0, content, extra_head=extra,
                             description=meta.get("description", "")), encoding="utf-8")


def build_home(site: Site):
    counts = {k: sum(1 for p in site.pages if p.startswith(k + "/")) for k, _ in GROUPS}
    total = len(site.pages)
    n_slides = (ROOT / "output/recsys-slides.html").read_text(encoding="utf-8").count('<section class="slide')
    cards = [
        ("wiki-html/index.html", "Wiki 知識庫", f"{total} 頁",
         f"10 份來源整理成 {counts['concepts']} 個概念、{counts['entities']} 個平台、{counts['syntheses']} 篇跨來源整合、"
         f"{counts['teaching']} 份教學素材。每個數字都標了出處頁碼。"),
        ("slides.html", "教學簡報", f"{n_slides} 頁",
         "給沒學過推薦系統的大學生：它怎麼挑、它想要什麼、會不會改變我們。← → 翻頁，N 看講者備忘。"),
        ("workflow.html", "流程設計", "loop / graph",
         "資料怎麼取得、討論、寫進 wiki、檢查，再變成簡報；哪些步驟會重複、哪裡會退回重做。"),
        ("record.html", "執行紀錄", "4 輪 ingest、6 次 lint",
         "一次完整執行的時間線、每次檢查抓到什麼、簡報和 wiki 的逐頁對照。"),
        ("reflection.html", "反思", "哪裡最常錯",
         "最常出錯的節點、檢查往前移到哪裡，以及規則如何一輪輪補齊。"),
    ]
    card_html = "".join(
        f'<a class="card" href="{href}"><span class="card-kicker">{kicker}</span>'
        f'<h2>{title}</h2><p>{html.escape(desc)}</p></a>' for href, title, kicker, desc in cards)
    content = f"""<main class="home">
<section class="hero">
  <p class="eyebrow">LLM Wiki 作業｜主題：推薦演算法</p>
  <h1>你滑到的影片，<br>是誰決定的？</h1>
  <p class="lede">這個網站有兩部分：一個依 Karpathy「LLM Wiki」構想建立的知識庫，主題是短影音與社群平台的推薦演算法；以及一份只用這個知識庫做成的教學簡報。</p>
  <p class="cta"><a class="btn primary" href="slides.html">看簡報</a><a class="btn" href="wiki-html/index.html">逛 Wiki</a></p>
</section>
<section class="cards">{card_html}</section>
<section class="about prose">
  <h2>關於這個 Wiki</h2>
  <p><strong>主題</strong>：推薦演算法，也就是 TikTok、YouTube、X、Facebook 這類平台，怎麼從數百萬則內容裡挑出你會看到的那幾則，以及這件事對社會有什麼影響。</p>
  <p><strong>資料</strong>：10 份來源，分成三類：工業界技術（YouTube 2016、Monolith、X 開源 README、TikTok 官方說明兩份）、生成式推薦（Meta HSTU、快手 OneRec）、社會影響實證研究（Guess 2023、Milli、Haroon 2023）。</p>
  <p><strong>做法</strong>：人類負責挑來源、決定重點、確認每一批；LLM 負責閱讀、寫頁面、交叉連結、標出處與爭議，並跑檢查。規則寫在 <a href="https://github.com/JERRYzx7/recsys-llm-wiki/blob/main/AGENTS.md">AGENTS.md</a>。</p>
  <p class="muted">原始論文 PDF 有版權，沒有放上網；每份來源的書目資訊在 Wiki 的 Sources 頁。原始檔：<a href="https://github.com/JERRYzx7/recsys-llm-wiki">GitHub repo</a>。</p>
</section>
</main>"""
    (ROOT / "index.html").write_text(page("推薦演算法 LLM Wiki", "home", 0, content), encoding="utf-8")


def build_slides():
    content = """<main class="slides-wrap">
<div class="slides-bar">
  <span>28 頁｜只從 Wiki 取材，每頁都標了出處</span>
  <a href="output/recsys-slides.html" target="_blank" rel="noopener">全螢幕開啟 ↗</a>
</div>
<iframe id="deck" src="output/recsys-slides.html" title="推薦演算法教學簡報"></iframe>
</main>"""
    (ROOT / "slides.html").write_text(page("教學簡報｜推薦演算法", "slides", 0, content, body_class="slides"),
                                      encoding="utf-8")


def main():
    site = Site()
    build_wiki(site)
    for name, active in [("workflow", "workflow"), ("record", "record"), ("reflection", "reflection")]:
        build_report(site, name, active)
    build_home(site)
    build_slides()
    print(f"OK：{len(site.pages)} 個 wiki 頁、3 個說明頁、首頁、簡報頁")


if __name__ == "__main__":
    main()

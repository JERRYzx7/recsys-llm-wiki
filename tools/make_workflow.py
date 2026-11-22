#!/usr/bin/env python3
"""產生 loop / graph 流程圖：assets/workflow.svg → assets/workflow.png（用 headless Chrome 轉檔）。

在 my-wiki/ 執行：  python3 tools/make_workflow.py
"""
from __future__ import annotations

import html
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "assets" / "workflow.svg"
PNG = ROOT / "assets" / "workflow.png"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W, H = 1600, 1000

INK, PENCIL, RULE, PEN, NOTE = "#222222", "#6b6f76", "#cfcfca", "#d0202e", "#fff4cc"
FONT = "PingFang TC, Noto Sans TC, Microsoft JhengHei, sans-serif"
HEAD = "Kaiti TC, STKaiti, BiauKai, KaiTi, serif"

parts: list[str] = []


def text(x, y, s, size=15, color=INK, weight=400, anchor="start", family=FONT):
    parts.append(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" fill="{color}" '
                 f'font-weight="{weight}" text-anchor="{anchor}">{html.escape(s)}</text>')


def node(x, y, w, h, title, lines, kind="step"):
    fill, stroke, dash, sw = "#ffffff", INK, "", 1.4
    if kind == "check":
        stroke, sw = PEN, 2.6
    if kind == "human":
        fill, dash = NOTE, ' stroke-dasharray="6 4"'
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{sw}"{dash}/>')
    if kind in ("check", "human"):
        tag = "✓ 檢查" if kind == "check" else "人類關卡"
        tw = 62 if kind == "check" else 72
        col = PEN if kind == "check" else "#8a6d00"
        parts.append(f'<rect x="{x + w - tw - 8}" y="{y - 11}" width="{tw}" height="22" rx="11" '
                     f'fill="#ffffff" stroke="{col}" stroke-width="1.4"/>')
        text(x + w - tw / 2 - 8, y + 5, tag, 13, col, 600, "middle")
    text(x + 16, y + 34, title, 19, INK, 600)
    for i, ln in enumerate(lines):
        text(x + 16, y + 62 + i * 22, ln, 14.5, PENCIL)


def arrow(points, kind="main", label=None, lx=None, ly=None, anchor="start"):
    color = {"main": INK, "redo": PEN, "next": PENCIL}[kind]
    dash = {"main": "", "redo": ' stroke-dasharray="7 5"', "next": ' stroke-dasharray="3 5"'}[kind]
    marker = {"main": "a-ink", "redo": "a-pen", "next": "a-pencil"}[kind]
    d = "M " + " L ".join(f"{px} {py}" for px, py in points)
    parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{2 if kind == "main" else 1.8}"'
                 f'{dash} stroke-linejoin="round" marker-end="url(#{marker})"/>')
    if label:
        for i, ln in enumerate(label.split("\n")):
            parts.append(f'<text x="{lx}" y="{ly + i * 19}" font-family="{FONT}" font-size="14" fill="{color}" '
                         f'text-anchor="{anchor}" paint-order="stroke" stroke="#ffffff" stroke-width="5">'
                         f'{html.escape(ln)}</text>')


def frame(x, y, w, h, label):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fafaf8" stroke="{RULE}" stroke-width="1.5"/>')
    text(x + 280, y + 30, label, 20, INK, 400, family=HEAD)


# ---------------------------------------------------------------- title & legend
text(40, 50, "LLM Wiki → 教學簡報：loop / graph 設計", 32, INK, 400, family=HEAD)
lx, ly = 1010, 84
parts.append(f'<rect x="{lx - 16}" y="{ly - 26}" width="566" height="128" rx="8" fill="#ffffff" stroke="{RULE}"/>')
parts.append(f'<rect x="{lx}" y="{ly - 12}" width="34" height="20" rx="4" fill="#fff" stroke="{INK}" stroke-width="1.4"/>')
text(lx + 44, ly + 3, "一般步驟（LLM 執行）", 14)
parts.append(f'<rect x="{lx}" y="{ly + 22}" width="34" height="20" rx="4" fill="#fff" stroke="{PEN}" stroke-width="2.6"/>')
text(lx + 44, ly + 37, "檢查節點", 14)
parts.append(f'<rect x="{lx}" y="{ly + 56}" width="34" height="20" rx="4" fill="{NOTE}" stroke="{INK}" stroke-dasharray="5 3"/>')
text(lx + 44, ly + 71, "人類關卡（停下來等人）", 14)
for i, (kind, lab) in enumerate([("main", "主流程"), ("redo", "檢查不過 → 退回重做"), ("next", "下一輪重複")]):
    yy = ly - 2 + i * 34
    arrow([(lx + 270, yy), (lx + 316, yy)], kind)
    text(lx + 328, yy + 5, lab, 14)

# ---------------------------------------------------------------- step 0
node(70, 86, 470, 96, "0. 先討論規則（schema）",
     ["人類＋LLM 一起定：主題、讀者、分批、出處與爭議寫法",
      "寫成 AGENTS.md 和 3 個 skill（ingest / lint / slides）"], "human")

# ---------------------------------------------------------------- phase A
frame(40, 222, 1520, 420, "階段一　建 Wiki：每一輪重複（批次 1 → 單篇 10 → 批次 2 → 批次 3）")
RW, RH = 240, 112
xs = [70, 375, 680, 985, 1290]
y1, y2 = 272, 470
node(xs[0], y1, RW, RH, "1. 取得資料", ["人類把來源放進 raw/（唯讀）", "LLM 登記 MD5"])
node(xs[1], y1, RW, RH, "2. 先討論", ["列 3–5 個重點與既有關係", "人類決定要強調什麼"], "human")
node(xs[2], y1, RW, RH, "3. 精讀＋記筆記", ["PDF 抽文字到暫存區", "數字一律記 PDF 頁碼"])
node(xs[3], y1, RW, RH, "4. 寫 source 頁", ["書目、方法、關鍵數字", "限制、與其他來源的關係"])
node(xs[4], y1, RW, RH, "5. 交叉整合", ["新建或更新 concept、entity、", "synthesis、teaching；標爭議"])
node(xs[4], y2, RW, RH, "6. 更新索引", ["glossary、index.md", "log.md 只能往後追加"])
node(xs[3], y2, RW, RH, "7. 結構檢查（腳本）", ["lint.py：斷鏈、孤兒頁、index、", "frontmatter、raw MD5"], "check")
node(xs[2], y2, RW, RH, "8. 內容檢查（LLM）", ["缺頁碼、未標爭議、缺頁概念、", "缺白話解釋、觀點混雜"], "check")
node(xs[1], y2, RW, RH, "9. 回報、等人類確認", ["變更摘要＋待決問題", "確認後才進下一輪"], "human")

for a, b in zip(xs[:-1], xs[1:]):
    arrow([(a + RW, y1 + RH / 2), (b - 4, y1 + RH / 2)])
arrow([(xs[4] + RW / 2, y1 + RH), (xs[4] + RW / 2, y2 - 4)])
for a, b in [(xs[4], xs[3]), (xs[3], xs[2]), (xs[2], xs[1])]:
    arrow([(a, y2 + RH / 2), (b + RW + 4, y2 + RH / 2)])
arrow([(xs[0] + RW / 2, 182), (xs[0] + RW / 2, y1 - 4)])

# 退回重做
arrow([(xs[3] + RW / 2, y2), (xs[3] + RW / 2, y1 + RH + 4)], "redo", "結構有問題 →\n修頁面、重跑腳本", xs[3] + RW / 2 + 12, 418)
arrow([(xs[2] + RW / 2, y2), (xs[2] + RW / 2, y1 + RH + 4)], "redo", "缺頁碼、缺出處 →\n回 raw 查證", xs[2] + RW / 2 + 12, 418)
arrow([(xs[1] + RW / 2, y2), (xs[1] + RW / 2, y1 + RH + 4)], "redo", "人類要求調整 →\n重新討論重點", xs[1] + RW / 2 + 12, 418)
# 下一輪
arrow([(xs[1], y2 + RH / 2 + 22), (xs[0] + RW / 2, y2 + RH / 2 + 22), (xs[0] + RW / 2, y1 + RH + 4)], "next",
      "下一輪\n（共 4 輪）", xs[0] + RW / 2 + 12, 430)
# 規則回饋
arrow([(760, 222), (760, 134), (544, 134)], "redo", "lint 或人類發現規則漏洞 → 回頭補 AGENTS.md／skill", 776, 206)

# ---------------------------------------------------------------- phase B
frame(40, 682, 1520, 268, "階段二　產簡報：只從 wiki 取材")
BW = 212
bx = [70, 318, 566, 814, 1062, 1310]
yb = 730
node(bx[0], yb, BW, RH, "10. 簡報前 lint", ["結構 5 項＋內容 5 項", "不過就先修 wiki"], "check")
node(bx[1], yb, BW, RH, "11. 查詢 Wiki", ["先讀 index.md 找頁", "不直接讀 raw"])
node(bx[2], yb, BW, RH, "12. 整理大綱", ["三個問題、28 頁", "每頁標出處與取材頁"])
node(bx[3], yb, BW, RH, "13. 生成 HTML", ["單一檔案、講者備忘", "黑板／白紙兩種主題"])
node(bx[4], yb, BW, RH, "14. 實際瀏覽驗證", ["headless Chrome 截圖", "深淺色、手機寬、按鍵"], "check")
node(bx[5], yb, BW, RH, "15. 記 log、發佈", ["log 記下取材頁", "建網站、推上 Pages"])
for a, b in zip(bx[:-1], bx[1:]):
    arrow([(a + BW, yb + RH / 2), (b - 4, yb + RH / 2)])
# A → B
arrow([(xs[1] + RW / 2, y2 + RH), (xs[1] + RW / 2, 662), (bx[0] + BW / 2, 662), (bx[0] + BW / 2, yb - 4)], "main",
      "4 輪都完成", xs[1] + RW / 2 + 12, 610)
# 重新生成
arrow([(bx[4] + BW / 2, yb + RH), (bx[4] + BW / 2, 884), (bx[3] + BW / 2, 884), (bx[3] + BW / 2, yb + RH + 4)], "redo",
      "版面跑掉、按鍵失效 → 重新生成", (bx[3] + bx[4]) / 2 + BW / 2, 912, "middle")
# 回補 wiki
arrow([(bx[2] + BW / 2, yb), (bx[2] + BW / 2, 646)], "redo", "wiki 缺內容 → 回階段一先補", bx[2] + BW / 2 + 12, 704)

# ---------------------------------------------------------------- write
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <marker id="a-ink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker>
  <marker id="a-pen" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{PEN}"/></marker>
  <marker id="a-pencil" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{PENCIL}"/></marker>
</defs>
<rect width="{W}" height="{H}" fill="#ffffff"/>
{chr(10).join(parts)}
<text x="40" y="984" font-family="{FONT}" font-size="13" fill="{PENCIL}">檢查節點：7、8、10、14；人類關卡：0、2、9。重複執行：步驟 1–9 每輪一次，共 4 輪；7–8 不通過就退回，修完重跑。</text>
</svg>
"""
SVG.parent.mkdir(exist_ok=True)
SVG.write_text(svg, encoding="utf-8")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={W},{H}",
                "--force-device-scale-factor=2", f"--screenshot={PNG}", SVG.as_uri()],
               check=True, capture_output=True)
print("OK", SVG, PNG)

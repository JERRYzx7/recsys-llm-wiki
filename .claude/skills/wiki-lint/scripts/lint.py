#!/usr/bin/env python3
"""Structural lint for the recommender-systems LLM wiki.

Run from the wiki root (my-wiki/):  python3 .claude/skills/wiki-lint/scripts/lint.py
Exit code 0 = clean, 1 = problems found.
"""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
MANIFEST = ROOT / ".raw-manifest.md5"

SPECIAL = {"index", "log"}  # no frontmatter required, not orphan-checked
ORPHAN_EXEMPT = SPECIAL | {"glossary"}  # glossary is a hub reached via index
REQUIRED = ["type", "title", "sources", "updated"]
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)


def page_id(p: Path) -> str:
    return p.relative_to(WIKI).with_suffix("").as_posix()


def links_in(text: str) -> set[str]:
    text = CODE_RE.sub("", text)  # ignore links inside code (templates/examples)
    return {m.group(1).strip().removesuffix(".md") for m in LINK_RE.finditer(text)}


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t", "-")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm


def main() -> int:
    problems: dict[str, list[str]] = {
        "1 斷鏈": [], "2 孤兒頁": [], "3 index 不一致": [],
        "4 frontmatter": [], "5 raw 完整性": [],
    }

    pages = {page_id(p): p for p in sorted(WIKI.rglob("*.md"))}
    texts = {pid: p.read_text(encoding="utf-8") for pid, p in pages.items()}
    outlinks = {pid: links_in(t) for pid, t in texts.items()}

    # 1 broken links
    for pid, links in outlinks.items():
        for target in sorted(links):
            if target not in pages:
                problems["1 斷鏈"].append(f"{pid} → [[{target}]]")

    # 2 orphans (inbound links from anything except index/log)
    inbound = {pid: 0 for pid in pages}
    for src, links in outlinks.items():
        if src in SPECIAL:
            continue
        for t in links:
            if t in inbound and t != src:
                inbound[t] += 1
    for pid, n in inbound.items():
        if pid not in ORPHAN_EXEMPT and n == 0:
            problems["2 孤兒頁"].append(pid)

    # 3 index consistency
    if "index" not in pages:
        problems["3 index 不一致"].append("wiki/index.md 不存在")
    else:
        listed = outlinks["index"]
        for pid in pages:
            if pid not in SPECIAL and pid not in listed:
                problems["3 index 不一致"].append(f"未列入 index：{pid}")
        for t in sorted(listed):
            if t not in pages:
                problems["3 index 不一致"].append(f"index 列了但不存在：{t}")

    # 4 frontmatter
    for pid, text in texts.items():
        if pid in SPECIAL:
            continue
        fm = frontmatter(text)
        if fm is None:
            problems["4 frontmatter"].append(f"{pid}：缺 frontmatter")
            continue
        missing = [k for k in REQUIRED if k not in fm]
        if fm.get("type") == "source" and "raw" not in fm:
            missing.append("raw")
        if missing:
            problems["4 frontmatter"].append(f"{pid}：缺 {', '.join(missing)}")

    # 5 raw integrity
    if not MANIFEST.exists():
        problems["5 raw 完整性"].append(".raw-manifest.md5 不存在")
    else:
        expected = {}
        for line in MANIFEST.read_text(encoding="utf-8").splitlines():
            if line.strip():
                h, path = line.split(maxsplit=1)
                expected[path.strip()] = h
        actual = {
            f"raw/{p.relative_to(RAW).as_posix()}": hashlib.md5(p.read_bytes()).hexdigest()
            for p in sorted(RAW.rglob("*")) if p.is_file() and p.name != ".DS_Store"
        }
        for path, h in expected.items():
            if path not in actual:
                problems["5 raw 完整性"].append(f"缺檔：{path}")
            elif actual[path] != h:
                problems["5 raw 完整性"].append(f"內容被改動：{path}")
        for path in actual:
            if path not in expected:
                problems["5 raw 完整性"].append(f"未登記（新來源？）：{path}")

    total = 0
    print(f"wiki 頁面數：{len(pages)}")
    for name, items in problems.items():
        status = "OK" if not items else f"{len(items)} 個問題"
        print(f"[{name}] {status}")
        for it in items:
            print(f"    - {it}")
        total += len(items)
    print(f"\n總計問題：{total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())

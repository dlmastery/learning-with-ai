#!/usr/bin/env python3
"""Render the edited PAPER.md manuscript to docs/paper.html."""
from pathlib import Path
import html
import re

import markdown

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "PAPER.md"
TARGET = ROOT / "docs" / "paper.html"

text = SOURCE.read_text(encoding="utf-8")
body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "toc", "attr_list"],
    output_format="html5",
)
body = body.replace("<table>", '<div class="scroll"><table>').replace("</table>", "</table></div>")
body = (body
        .replace('href="ATLAS.md"', 'href="atlas.html"')
        .replace('href="CORRECTIONS.md"', 'href="https://github.com/dlmastery/learning-with-ai/blob/main/CORRECTIONS.md"')
        .replace('href="research/raw/"', 'href="https://github.com/dlmastery/learning-with-ai/tree/main/research/raw"')
        .replace('href="docs/demos/"', 'href="demos/"'))

title = re.search(r"^# (.+)$", text, re.M).group(1)
words = len(re.findall(r"\b[\w’'-]+\b", text))
minutes = max(1, round(words / 220))
site_css = (ROOT / "docs" / "site.css").read_text(encoding="utf-8")

page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — Learning with AI</title>
<meta name="description" content="Evidence and a reference architecture for persistent, multimodal learning systems.">
<style>{site_css}
body{{padding:0;overflow-x:hidden}}
.top{{position:sticky;top:0;z-index:5;height:50px;display:flex;align-items:center;gap:14px;
padding:0 18px;background:color-mix(in srgb,var(--bg) 91%,transparent);backdrop-filter:blur(12px);
border-bottom:1px solid var(--line);font:13px/1 var(--sans)}}
.top a{{border:0;color:var(--ink-3)}}.top a:hover{{color:var(--felt)}}.top .grow{{flex:1}}
.progress{{position:fixed;z-index:8;left:0;top:0;height:2px;background:var(--felt);width:0}}
article{{max-width:43rem;margin:0 auto;padding:64px 22px 120px;font-size:17px;line-height:1.72}}
article>h1{{font:400 clamp(38px,7vw,64px)/1.03 var(--serif);letter-spacing:-.035em;margin:0 0 12px}}
article>h1+ h2{{font:400 clamp(20px,3vw,27px)/1.35 var(--serif);color:var(--ink-3);
margin:0 0 38px;letter-spacing:-.01em}}
article h2{{font:400 30px/1.2 var(--serif);letter-spacing:-.02em;margin:76px 0 20px;
padding-top:16px;border-top:1px solid var(--line);scroll-margin-top:64px}}
article h3{{font:650 19px/1.35 var(--sans);margin:42px 0 14px;scroll-margin-top:64px}}
article p{{color:var(--ink-2);margin:0 0 18px;max-width:none}}
article li{{color:var(--ink-2);margin-bottom:8px}}
article blockquote{{margin:28px 0;border-left:3px solid var(--felt);padding:4px 0 4px 22px}}
article blockquote p{{font:400 21px/1.5 var(--serif);color:var(--ink);margin:0}}
article code{{font-size:.86em}}article pre{{overflow:auto}}article img{{max-width:100%}}
.scroll{{width:100%;overflow-x:auto;margin:24px 0}}table{{min-width:620px;font-size:14px}}
.meta{{font:12px/1.4 var(--mono);color:var(--ink-3);white-space:nowrap}}
@media(max-width:620px){{.meta{{display:none}}.top{{gap:10px;padding:0 12px}}.top a{{font-size:12px}}}}
@media print{{.top,.progress{{display:none}}article{{padding-top:0;max-width:none}}}}
</style></head>
<body><div class="progress" id="progress"></div>
<nav class="top"><a href="./">← Dashboard</a><a href="atlas.html">Evidence atlas</a>
<span class="grow"></span><span class="meta">Reading edition</span>
<button class="theme" id="theme" aria-label="Toggle colour theme">◐</button></nav>
<article>{body}</article>
<script>
const p=document.getElementById('progress');
addEventListener('scroll',()=>{{const h=document.documentElement.scrollHeight-innerHeight;
p.style.width=(h?scrollY/h*100:0)+'%'}},{{passive:true}});
const r=document.documentElement;document.getElementById('theme').onclick=()=>{{
const d=r.getAttribute('data-theme')==='dark'||(!r.getAttribute('data-theme')&&
matchMedia('(prefers-color-scheme:dark)').matches);r.setAttribute('data-theme',d?'light':'dark')}};
</script></body></html>"""

TARGET.write_text(page, encoding="utf-8")
print(f"{TARGET.relative_to(ROOT)} — {words:,} words, {len(page)//1024} KB")

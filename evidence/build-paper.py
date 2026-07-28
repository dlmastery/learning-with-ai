#!/usr/bin/env python3
"""
Assemble survey/*.md into an actual paper.

A folder of markdown files is not a paper. This produces PAPER.md and
docs/paper.html: abstract, part structure, table of contents, continuous
numbering, and a findings table — one document you can read start to finish.

Re-runnable. Section order and part grouping are declared here, not inferred
from filenames, because the reading order is an editorial decision.
"""
import pathlib, re, subprocess, html, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SURVEY = ROOT / "survey"

PARTS = [
 ("I", "What is established",
  "Before any design argument, the evidence — with its error bars, its "
  "heterogeneity, and its nulls. A reader should be able to check everything "
  "that follows against this part.",
  ["24-the-floor", "01-central-finding", "09-the-scoreboard",
   "23-fifteen-hundred-papers-seven-trials"]),

 ("II", "The system the evidence forces",
  "What follows from that evidence if you take it seriously: an architecture, "
  "a division of labour, and a selection policy — each constrained by a "
  "measurement rather than a preference.",
  ["00-north-star-jarvis", "03-the-vision", "10-the-village",
   "22-the-one-interaction-that-survived", "11-the-archivist"]),

 ("III", "The mechanisms",
  "Seven techniques, each with a measured effect and a specified failure mode. "
  "These are the parts that do the teaching.",
  ["02-teach-to-learn", "05-the-explanation-is-the-work",
   "25-the-ladder-of-explanation", "08-nobody-needs-a-better-scheduler",
   "26-beyond-the-tutor", "06-what-the-object-must-refuse", "17-showing"]),

 ("IV", "Correctness",
  "How a tutor can be wrong safely, and how a learner's work can be measured "
  "when the artifact no longer indicates the person who produced it.",
  ["13-grounding", "12-assessment-after-the-artifact"]),

 ("V", "Who it is for",
  "The learners the evidence was not collected on, the learners it cannot "
  "reach, and the legal floor that turns out to be a design specification.",
  ["04-the-empty-chair", "07-who-is-not-in-the-room", "15-what-we-owe-children"]),

 ("VI", "The field, and what it has already built",
  "The frontier's actual capabilities, the artifacts other people have shipped, "
  "the pedagogical canon that settled most of this decades ago, and the "
  "question of whether anyone wants to continue.",
  ["16-the-substrate", "18-the-textbook-that-writes-itself", "19-the-canon",
   "27-the-market", "28-prior-art", "14-motivation"]),

 ("VII", "What we do not know",
  "The catalogued gaps, the uncatalogued ones, and the conditions under which "
  "this document's central claim would have to be withdrawn.",
  ["21-what-we-cannot-see-from-here", "20-the-agenda"]),
]

ABSTRACT = """\
Generative AI arrived in education as a capability without a specification. Three
years of deployment later, the field has produced roughly 2,900 papers and, by our
census, **seven randomised controlled trials** — of which four are second-language
learning. The literature measures resemblance, preference and engagement. It very
rarely measures whether anyone learned anything, and almost never measures it
**after the tool is taken away**.

This survey is an attempt to write the missing specification. It is built on 32
research reports and roughly 2,100 source citations, every claim carrying an
evidence label, every section carrying at least one documented null result, and
every one of the authors' own errors published in an append-only ledger rather than
quietly edited — eight of the twenty-four corrections were found by an adversarial
reviewer rather than by us.

Three findings organise it. **First, felt learning and real learning move in
opposite directions**: preference shifts at *d* ≈ 0.48 while knowledge does not
move, and the effect survives explicit debiasing — so every metric a product can
easily optimise is the wrong one. **Second, measurement without a decision rule is
inert**: in the randomised trial that settles it, both arms revised instruction more
often and only the arm told *what to change* moved achievement, which disqualifies
the dashboard as an intervention. **Third, unguarded assistance is an active harm**,
leaving learners 17% worse on later unassisted work — while the guardrailed arm's
unassisted coefficient is −0.004, not significant. Restraint removes the harm. It
has not been shown to teach.

From these we specify a system: a registry of certified specialist agents with an
active set of three to five, arbitrating by precedence rather than by vote;
persistent learner state that is local, inspectable and deletable; correctness that
lives in a verifier rather than in the model's manners; explanation held as a
three-rung library entered by measurement rather than a staircase climbed by
preference; and a mentor whose highest-value act is declining to answer.

We design for the margin first. A census of ERIC and Europe PMC returns 30
randomised trials of generative-AI tutoring that mention students and **zero** that
mention disability, dyslexia, ADHD, autism, special education or an IEP. Every
effect size in this field was measured on somebody else's child.

The survey's central claim is that the measured 0.2–0.4 SD band describes systems
that answer freely, forget everything between sessions, cannot see the work, cannot
point, never change method, and agree with the learner — and that nobody has built
and measured the constrained, grounded, pivoting, remembering, teachable
alternative. **That nobody has measured it is proven. That it would do better is a
hypothesis**, and Part VII states the conditions under which we would withdraw it.
"""

def read(slug):
    f = SURVEY / f"{slug}.md"
    if not f.exists(): return None, None
    t = f.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    meta = {}
    if fm:
        for line in fm.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        t = t[fm.end():]
    t = t.lstrip("\n")
    t = re.sub(r"^#\s+.*\n", "", t, count=1)          # drop the section's own H1
    return meta, t.strip()

def build():
    parts_out, toc, n, missing = [], [], 0, []
    stats = {"sections": 0, "words": 0}
    for numeral, ptitle, blurb, slugs in PARTS:
        toc.append(f"\n**Part {numeral} — {ptitle}**\n")
        body = [f"\n\n---\n\n# Part {numeral} · {ptitle}\n\n*{blurb}*\n"]
        for slug in slugs:
            meta, text = read(slug)
            if text is None:
                missing.append(slug); continue
            n += 1
            title = meta.get("title", slug)
            anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
            toc.append(f"{n}. [{title}](#{anchor})")
            src = meta.get("source_report", "")
            srcline = f"\n<sub>Source report: `{src}`</sub>\n" if src else "\n"
            body.append(f"\n## {n}. {title}\n{srcline}\n{text}\n")
            stats["sections"] += 1
            stats["words"] += len(text.split())
        parts_out.append("\n".join(body))

    covered = {s for _, _, _, ss in PARTS for s in ss}
    orphans = sorted(p.stem for p in SURVEY.glob("*.md") if p.stem not in covered)

    head = f"""# Learning in the New Frontier AI World

### A survey of what AI-native learning has actually been measured to do, and a specification for what it should be

**{stats['sections']} sections · {stats['words']:,} words · 32 research reports · ~2,100 source citations**
Corrections ledger: [`CORRECTIONS.md`](CORRECTIONS.md) · Adversarial reviews: [`evidence/`](evidence/)
Interactive demonstrations: <https://dlmastery.github.io/learning-with-ai/demos/>

---

## Abstract

{ABSTRACT}
---

## How to read this

Every claim carries an evidence label — `MEASURED-RCT`, `MEASURED-META`,
`MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`. A `VENDOR` claim is
never restated as a finding. Every section contains at least one documented null,
given its own space rather than a footnote. Where a number could not be verified it
is reported as unverifiable rather than omitted or softened.

Thirteen of the techniques described here have a working demonstration that runs in
a browser with no server and no key. Each demonstration states whether it is
*computed* — the page performs the operation — or *scripted*, a labelled replay.
One of them documents a mechanism this project proposed, benchmarked, and
**falsified**.

---

## Contents

{chr(10).join(toc)}

---
"""
    doc = head + "\n".join(parts_out)
    (ROOT / "PAPER.md").write_text(doc, encoding="utf-8")
    print(f"PAPER.md — {stats['sections']} sections, {stats['words']:,} words, {len(PARTS)} parts")
    if missing: print(f"  declared but missing: {', '.join(missing)}")
    if orphans: print(f"  NOT IN THE PAPER: {', '.join(orphans)}")
    return doc, stats


def build_html():
    """Render PAPER.md to a single readable web page with a sticky contents rail."""
    import markdown
    doc, stats = build()
    body = markdown.markdown(doc, extensions=["tables", "toc", "fenced_code", "attr_list"])
    # Wide content must scroll inside its own container, never the page body.
    body = re.sub(r"<table>", '<div class="scroll"><table>', body)
    body = re.sub(r"</table>", "</table></div>", body)
    css = (ROOT / "docs" / "demos" / "demo.css").read_text()
    page = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Learning in the New Frontier AI World — the paper</title>
<meta name="description" content="A {stats['words']:,}-word survey of AI-native learning. Evidence-labelled throughout, nulls first-class, corrections published.">
<style>
{css}
.wrap{{max-width:860px}}
article h1{{font:400 clamp(30px,5vw,44px)/1.12 var(--serif);letter-spacing:-.022em;margin:0 0 10px}}
article h2{{font:400 30px/1.2 var(--serif);margin:64px 0 14px;padding-top:16px;
  border-top:1px solid var(--line);letter-spacing:-.018em;scroll-margin-top:20px}}
article h3{{font:650 16px/1.4 var(--sans);margin:34px 0 10px}}
article h1+h3{{font:400 19px/1.5 var(--serif);color:var(--ink-3);margin:0 0 26px}}
article p{{max-width:74ch;margin-bottom:17px}}
article ul,article ol{{max-width:74ch;margin:0 0 17px 22px;color:var(--ink-2)}}
article li{{margin-bottom:7px}}
article blockquote{{border-left:2px solid var(--felt);padding:2px 0 2px 18px;margin:22px 0;
  color:var(--ink);font-size:16.5px;max-width:70ch}}
article table{{min-width:0;margin:0}}
article .scroll{{margin:22px 0}}
article pre{{overflow-x:auto;background:var(--sunken);border:1px solid var(--line);
  border-radius:9px;padding:14px;font-size:12.5px}}
article img,article svg{{max-width:100%;height:auto}}
article *{{overflow-wrap:anywhere}}
article hr{{border:0;border-top:1px solid var(--line);margin:56px 0}}
article sub{{color:var(--ink-3);font-size:12px}}
article code{{font-size:12.5px}}
.top{{position:fixed;bottom:20px;right:20px;z-index:40;padding:9px 13px;border-radius:9px;
  background:var(--surface);border:1px solid var(--line-2);font-size:12.5px;cursor:pointer}}
@media print{{.theme,.top,.crumb{{display:none}} body{{padding:0}}}}
</style></head><body>
<button class="theme" id="tt" aria-label="Toggle colour theme">◐</button>
<button class="top" onclick="scrollTo({{top:0,behavior:'smooth'}})">↑ Contents</button>
<div class="wrap">
<nav class="crumb"><a href="./">← Dashboard</a> · <a href="demos/">Demos</a> ·
<a href="https://github.com/dlmastery/learning-with-ai">Repository</a></nav>
<article>
{body}
</article>
<footer>Evidence-labelled throughout. Nulls are first-class.
Corrections are published in
<a href="https://github.com/dlmastery/learning-with-ai/blob/main/CORRECTIONS.md">CORRECTIONS.md</a>.
</footer>
</div>
<script>
const R=document.documentElement;
document.getElementById('tt').onclick=()=>{{const d=R.getAttribute('data-theme')==='dark'||
 (!R.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
 R.setAttribute('data-theme',d?'light':'dark');}};
</script></body></html>"""
    (ROOT / "docs" / "paper.html").write_text(page, encoding="utf-8")
    print(f"docs/paper.html — {len(page)//1024} KB")

if __name__ == "__main__":
    if "--html" in sys.argv: build_html()

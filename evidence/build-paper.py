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
  "Eight techniques, each with a measured effect and a specified failure mode. "
  "These are the parts that do the teaching.",
  ["02-teach-to-learn", "05-the-explanation-is-the-work",
   "25-the-ladder-of-explanation", "29-explaining-hard-things",
   "08-nobody-needs-a-better-scheduler",
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
    """Assemble PAPER.md and return (markdown, stats, structure).

    `structure` is the declarative outline — parts, sections, anchors, word
    counts — that the HTML renderer builds its contents rail from. Both the
    rail and the contents page are generated from it, so neither can drift
    from the document the way the old hand-slugged anchors did (every one of
    the 29 contents links was dead)."""
    parts_out, toc, n, missing = [], [], 0, []
    stats = {"sections": 0, "words": 0}
    structure = []
    for pi, (numeral, ptitle, blurb, slugs) in enumerate(PARTS, 1):
        toc.append(f"\n**Part {numeral} — {ptitle}**\n")
        body = [f"\n\n---\n\n# Part {numeral} · {ptitle}\n\n*{blurb}*\n"]
        prec = {"numeral": numeral, "title": ptitle, "blurb": blurb,
                "anchor": f"p{pi}", "words": 0, "sections": []}
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
            words = len(text.split())
            stats["sections"] += 1
            stats["words"] += words
            prec["words"] += words
            prec["sections"].append({"n": n, "title": title, "anchor": f"s{n}",
                                     "source": src, "words": words, "text": text})
        structure.append(prec)
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
    return doc, stats, structure

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
  ["00-north-star-jarvis", "30-the-compression", "32-pedagogy-has-no-pytest", "38-enumerate-dont-judge", "03-the-vision", "10-the-village",
   "22-the-one-interaction-that-survived", "11-the-archivist",
   "45-sequencing-and-durability"]),

 ("III", "The mechanisms",
  "The techniques, each with a measured effect and a specified failure mode. "
  "These are the parts that do the teaching.",
  ["02-teach-to-learn", "05-the-explanation-is-the-work",
   "25-the-ladder-of-explanation", "39-what-the-explainers-invented", "29-explaining-hard-things", "35-the-explanation-atlas",
   "08-nobody-needs-a-better-scheduler",
   "26-beyond-the-tutor", "06-what-the-object-must-refuse", "17-showing",
   "40-the-relationship", "43-reading-and-writing", "44-second-language"]),

 ("IV", "Correctness",
  "How a tutor can be wrong safely, and how a learner's work can be measured "
  "when the artifact no longer indicates the person who produced it.",
  ["13-grounding", "12-assessment-after-the-artifact"]),

 ("V", "Who it is for",
  "The learners the evidence was not collected on, the learners it cannot "
  "reach, and the legal floor that turns out to be a design specification.",
  ["04-the-empty-chair", "31-the-coordinators-week", "07-who-is-not-in-the-room",
   "15-what-we-owe-children", "42-anxiety-and-self-concept",
   "46-groups-and-the-lifespan"]),

 ("VI", "The field, and what it has already built",
  "The frontier's actual capabilities, the artifacts other people have shipped, "
  "the pedagogical canon that settled most of this decades ago, and the "
  "question of whether anyone wants to continue.",
  ["16-the-substrate", "18-the-textbook-that-writes-itself", "19-the-canon",
   "27-the-market", "37-the-business-of-it", "41-the-exam", "36-the-two-hour-school",
   "28-prior-art", "14-motivation"]),

 ("VII", "What we do not know",
  "The catalogued gaps, the uncatalogued ones, what we would build with none of the "
  "existing containers, and the conditions under which this document's central claim "
  "would have to be withdrawn.",
  ["21-what-we-cannot-see-from-here", "34-attention-and-the-missing-executive", "33-greenfield", "20-the-agenda"]),
]

N_REPORTS = len(list((ROOT / "research" / "raw").glob("*.md")))
N_CORR = len(re.findall(r"^\| \*\*C-\d+\*\*", (ROOT / "CORRECTIONS.md").read_text(), re.M))
N_EXT = len([1 for _l in (ROOT / "CORRECTIONS.md").read_text().splitlines()
             if re.match(r"^\| \*\*C-\d+\*\*", _l) and "EXTERNAL-REVIEW" in _l])


ABSTRACT = f"""\
A frontier model, supervised by a human expert, already tutors like one. On a UK
maths platform in 2025, students who answered a question wrong and were then helped
by **LearnLM drafting under a human tutor's supervision** were correct on the retry
**93.0%** of the time, against **91.2%** for the expert tutor working alone and
**65.4%** for a static hint written for their exact misconception; the supervising
tutors sent **74.4%** of the model's drafts unedited, and a review of all 3,617
messages found zero harmful ones and five factual errors. A Harvard physics RCT the
same year put a purpose-built tutor **d ≈ 0.63** above an active-learning classroom
in a median 49 minutes — developer-built and developer-evaluated, so a starting point
and not a proof. In the field the effects are smaller and stay positive:
**+0.258 SD** adjusted in Sierra Leone, where the unadjusted estimate is **+0.216 SD,
SE 0.137, not significant**; **+0.206 SD** on the school's own exam in Nigeria; and
**+4 percentage points** of exit-ticket mastery across 900 tutors in US Title I
classrooms, **+9** for the students of the lowest-rated tutors.

Every number in that paragraph was measured on an LLM from 2023 onward. This survey
keeps them apart from the figures the field usually quotes, because those measured a
different class of machine. Bloom's two sigma is 1984 and human. VanLehn's *d* = 0.76
is a 2011 rule-based intelligent tutoring system. The **0.288 SD** that Nickow et al.
pool across 96 randomised trials is in-person human tutoring, mostly pre-2020. Each of
those results stands, and none of them is a ceiling on a machine it never saw.

What is missing is the specification. Roughly 2,900 papers into generative AI in
education, our census of the ERIC record finds **seven randomised controlled trials**
of ChatGPT — three of them second-language learning. The field measures resemblance,
preference and engagement; it rarely measures whether anyone learned, and almost never
**after the tool is taken away**. That is a finding about the literature, not about
the capability, and this survey is an attempt to write what the literature has not.
It rests on {N_REPORTS} research reports. Every claim carries an evidence label, every section
carries at least one documented null, and every one of the authors' errors is
published in an append-only ledger rather than quietly edited — **{N_EXT} of\nthe {N_CORR} corrections were found by an adversarial reviewer rather than by us.**
That discipline is the warrant for the opening paragraph, and not a substitute for
making its claim.

**The organising finding is about agents.** An agent differs from a chatbot in four
ways — sampling, execution, persistence, absence — and each is a multiplier on
something else, which gives a rule: *the value of an agentic loop is **bounded by**
the value of the external check it closes on.* That rule explains the whole reliability landscape.
Where a check exists, agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where the check is weak or absent, **21.0%** (PaperBench) and **4.6%**
(SciCode, which has hand-written tests — hence a bound rather than an equality).
Teaching sits in the second column, and the reason is measured: across **223
tutoring domains, the four models tested — a 2024 set, in what the authors call an
initial evaluation — did not beat chance at labelling an incorrect student action.**
Scope that precisely, because the adjacent result runs the other way: on ProcessBench,
open models identify the earliest erroneous step in a reasoning trace competitively
with that same GPT-4o vintage. **Checking a model's own reasoning is not the unsolved
part. Reading a learner's belief from what they did is.**
Coding agents work because `pytest` exists. **Pedagogy has no `pytest`, and every
agentic capability in education is waiting on one.**

Three findings constrain what may be built. Two are facts about learners and hold
whatever machine is in the room. **Felt learning and real learning move in opposite
directions** — across three RCTs of an infographic against a plain-language summary,
n = 334 adults on an immediate quiz, preference shifted at *d* ≈ 0.48 while knowledge
did not, and the easiness effect survives explicit debiasing, so every cheaply
optimisable metric is the wrong one. **Measurement without a decision rule is inert** —
in a 1991 trial of 33 teachers, both measuring arms revised instruction more often and
only the arm told *what to change* moved achievement, which is why the age of that
result does not weaken it. The third was measured on a frontier model: **unguarded
assistance is an active harm**, leaving ~1,000 Turkish high-school students 17% worse
on later unassisted work, while the guardrailed arm's unassisted coefficient is
−0.004, not significant. Restraint removes the harm and has not been shown to teach.

On speed, the popular claim is roughly right and imprecise. Learning is counted in
**opportunities, not days** — across 1.3 million observations, learning *rate* varies
by 1.14× while *prior knowledge* varies by 3.6×, and time-based models fit poorly.
The defensible bound is **10–40× on elapsed calendar and 3–5× on engaged effort**,
one documented case at ~300×, and **1×** on both durability and procedural skill.
Stated honestly: **a week's understanding in an hour; a year's retention in six hours
spread across two months.** What limits polymathy is not learning rate but the fixed
cost of orientation — how many times one can afford to be a beginner.

We design for the margin first. A census returns 30 randomised trials of
generative-AI tutoring that mention students and **zero** that mention disability,
dyslexia, ADHD, autism, special education or an IEP. Every effect size in this field
was measured on somebody else's child.

The central claim follows. Those deployment trials cluster at **0.2–0.4 SD**, which is
a rounding of three field studies carrying no pooled estimate and no confidence
interval — and every system in them answers freely, forgets between sessions, cannot
see the work, cannot point, never changes method, and agrees with the learner. **What
that cluster bounds is a design, and the constrained, grounded, pivoting, remembering, teachable
alternative has never been built and measured. That nobody has measured it is proven.
That it would do better is a hypothesis**, and Part VII states the conditions under
which we would withdraw it.
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
    # PASS 1 — assign paper section numbers before rendering any prose, so that
    # cross-references written as source-file numbers (§04) can be rewritten to
    # paper numbers (§5). Without this, prose and headings use different schemes:
    # 83 of 87 references pointed at the wrong section. See C-34.
    SRC2NUM, _k = {}, 0
    for _, _, _, _slugs in PARTS:
        for _s in _slugs:
            if (SURVEY / f"{_s}.md").exists():
                _k += 1
                SRC2NUM[_s[:2]] = _k

    def renumber(text, papernum=None):
        """§04 (source file) -> §5 (paper section). Unknown refs are left alone
        and reported, never silently rewritten.

        Two rewrites have to happen and NEITHER may see the other's output:

          A. cross-section: a two-digit "§09" is a source filename, and maps
             through SRC2NUM to a paper section number.
          B. intra-section: a single-digit "§3" is a subsection of the current
             section, and must be qualified to "§<papernum>.3" — once assembled,
             a bare "§3" would read as paper section 3. This is C-38.

        Running A then B mangles every cross-ref that lands on a single-digit
        paper section: "§09" becomes "§3", which B then qualifies to "§1.3".
        44 references were wrong this way.

        Running B then A mangles the other direction: B writes a two-digit paper
        number, and A reads "§17.3.3" as a reference to source file 17.

        So A emits a sentinel that A's and B's patterns cannot match, and the
        sentinel is resolved last.
        """
        SENT = "\x00%s\x00"

        def sub(m):
            src = m.group(1)
            if src in SRC2NUM:
                return SENT % SRC2NUM[src]
            unresolved.add(src)
            return m.group(0)
        text = re.sub(r"§\s?(\d{2})\b", sub, text)

        def sub2(m):
            src = m.group(2)
            if src in SRC2NUM:
                return f"{m.group(1)}{SRC2NUM[src]}"
            unresolved.add(src)
            return m.group(0)
        text = re.sub(r"\b(Section|section)\s+(\d{2})\b", sub2, text)

        if papernum is not None:
            text = re.sub(r"§\s?(\d)(?!\d)((?:\.\d+)*)",
                          lambda m: f"§{papernum}.{m.group(1)}{m.group(2)}", text)

        return re.sub(r"\x00(\d+)\x00", r"§\1", text)

    unresolved = set()
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
            # Increment BEFORE renumbering. The section is rendered as "## {n}."
            # after the increment, so passing the pre-increment n qualified every
            # intra-section reference against the *previous* section — 31 of them,
            # each resolving to real but wrong content.
            n += 1
            text = renumber(text, papernum=n)
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
            prec["sections"].append({"n": n, "title": title, "anchor": f"s{n}", "slug": slug,
                                     "source": src, "words": words, "text": text})
        structure.append(prec)
        parts_out.append("\n".join(body))

    # Regression guard for C-38 and C-59. A qualified reference "§N.M" is an
    # INTRA-section pointer, so N must equal the number of the section it sits in.
    # When the renumber passes ran in the wrong order, a cross-section ref like
    # §09 resolved to "§3" and was then re-qualified against its host section,
    # producing "§1.3" — a reference that resolves to real but wrong content, which
    # nothing flags. 44 references were wrong this way. Fail the build instead.
    mangled = []
    total = sum(len(prec["sections"]) for prec in structure)
    for prec in structure:
        for s in prec["sections"]:
            for m in re.finditer(r"§(\d+)\.\d+", s["text"]):
                # §300.320 is an IDEA regulation, not a section of this paper.
                if int(m.group(1)) > total:
                    continue
                if int(m.group(1)) != s["n"]:
                    ctx = s["text"][max(0, m.start()-60):m.end()+30].replace("\n", " ")
                    mangled.append(f"{s['slug']} (paper §{s['n']}) contains {m.group(0)}  …{ctx}…")
    if mangled:
        print(f"  MANGLED CROSS-REFS — {len(mangled)}; a qualified §N.M must have N = "
              f"its own section:")
        for x in mangled[:8]:
            print(f"    {x}")
        raise SystemExit(1)

    if unresolved:
        print(f"  UNRESOLVED cross-refs (left as written): {', '.join(sorted(unresolved))}")

    covered = {s for _, _, _, ss in PARTS for s in ss}
    orphans = sorted(p.stem for p in SURVEY.glob("*.md") if p.stem not in covered)

    head = f"""# Learning in the New Frontier AI World

### A survey of what AI-native learning has actually been measured to do, and a specification for what it should be

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
    print(f"PAPER.md — {stats['sections']} sections, "
          f"{stats['words']:,} words, {len(PARTS)} parts")
    if missing: print(f"  declared but missing: {', '.join(missing)}")
    if orphans: print(f"  NOT IN THE PAPER: {', '.join(orphans)}")
    return doc, stats, structure


# ── HTML rendering ────────────────────────────────────────────────────────────
#
# The page is assembled from the `structure` returned by build(), not from the
# rendered markdown. Contents rail, contents page and section headings all come
# from one outline, so an anchor cannot exist in one and be missing in another.
#
# The 2026-07-28 taste review found all 29 contents links dead: build() slugged
# anchors from the bare title while python-markdown slugged the heading text,
# which carries the section number. Generating both ends from the same record
# is the fix; hand-matched slugs were the bug.

PAPER_CSS = r"""
/* ── paper: reading shell ─────────────────────────────────── */
body{padding:0;overflow-x:hidden}
.progress{position:fixed;top:0;left:0;height:2px;width:0;background:var(--felt);z-index:70;
  transition:width .08s linear}
.bar{position:sticky;top:0;z-index:55;display:flex;align-items:center;gap:14px;
  height:52px;padding:0 16px;background:color-mix(in oklab,var(--bg) 88%,transparent);
  backdrop-filter:saturate(1.4) blur(12px);border-bottom:1px solid var(--line)}
.bar .home{font:650 13px/1 var(--sans);color:var(--ink);white-space:nowrap;border-bottom:0}
@media (max-width:760px){.bar .home .ht{display:none}}
.bar .home:hover{color:var(--felt)}
.bar .where{font:13px/1.3 var(--sans);color:var(--ink-3);overflow:hidden;
  text-overflow:ellipsis;white-space:nowrap;flex:1;min-width:0}
.bar .where b{color:var(--ink-2);font-weight:650}
.bar button{font:600 12.5px/1 var(--sans);padding:8px 11px;border-radius:var(--r-sm);
  border:1px solid var(--line-2);background:var(--surface);color:var(--ink);cursor:pointer;
  white-space:nowrap}
.bar button:hover{border-color:var(--ink-3)}
.theme{position:static;width:34px;height:34px;flex:none}

.shell{display:grid;grid-template-columns:1fr;max-width:1320px;margin:0 auto}
.doc{min-width:0;padding:0 20px 120px}
.doc .col{max-width:41rem;margin:0 auto}

/* ── contents rail ────────────────────────────────────────── */
#rail{background:var(--bg)}
#rail .inner{padding:26px 22px 60px}
#rail .rt{font:600 10.5px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:18px}
#rail ol{list-style:none;margin:0 0 22px;padding:0}
#rail .ph{display:block;font:600 11px/1.3 var(--sans);letter-spacing:.1em;text-transform:uppercase;
  color:var(--felt);padding:14px 0 8px;border-top:1px solid var(--line);margin-top:10px}
#rail ol:first-of-type .ph{border-top:0;margin-top:0;padding-top:0}
#rail a{display:block;font:13.5px/1.4 var(--sans);color:var(--ink-3);padding:6px 0 6px 14px;
  border-bottom:0;border-left:2px solid transparent}
#rail a:hover{color:var(--ink)}
#rail a .rn{font:600 11px/1 var(--mono);color:var(--line-2);margin-right:7px}
#rail a[aria-current="true"]{color:var(--ink);border-left-color:var(--felt);font-weight:650}
#rail a[aria-current="true"] .rn{color:var(--felt)}

@media (min-width:1080px){
  .shell{grid-template-columns:274px minmax(0,1fr);gap:0}
  #rail{position:sticky;top:52px;height:calc(100vh - 52px);overflow-y:auto;
    border-right:1px solid var(--line);scrollbar-width:thin}
  #rail .scrim,#rail .close{display:none}
  .bar .tocbtn{display:none}
  .doc{padding:0 56px 140px}
}
@media (max-width:1079px){
  #rail{position:fixed;inset:0 auto 0 0;width:min(320px,86vw);z-index:80;
    border-right:1px solid var(--line-2);overflow-y:auto;
    transform:translateX(-102%);transition:transform .22s ease;
    box-shadow:0 0 40px rgba(0,0,0,.14)}
  #rail[data-open]{transform:none}
  #rail .close{position:absolute;top:16px;right:14px;width:32px;height:32px;border-radius:8px;
    border:1px solid var(--line-2);background:var(--surface);color:var(--ink);cursor:pointer;
    font:15px/1 var(--sans)}
  .scrim{position:fixed;inset:0;z-index:75;background:rgba(0,0,0,.46);opacity:0;
    pointer-events:none;transition:opacity .22s}
  .scrim[data-open]{opacity:1;pointer-events:auto}
}

/* ── front matter ─────────────────────────────────────────── */
.front{padding:64px 0 0}
.front h1{font:400 clamp(31px,5.6vw,50px)/1.08 var(--serif);letter-spacing:-.024em;margin:0 0 16px}
.front .standfirst{font:400 clamp(18px,2.4vw,21px)/1.5 var(--serif);color:var(--ink-3);
  max-width:42ch;margin:0 0 36px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,auto));
  gap:20px 44px;justify-content:start;border-top:1px solid var(--line);
  border-bottom:1px solid var(--line);padding:20px 0;margin-bottom:8px}
.facts div{min-width:0}
.facts dt{font:600 10.5px/1.35 var(--sans);letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink-3);margin-bottom:8px}
.facts dd{font:400 21px/1 var(--serif);color:var(--ink);letter-spacing:-.01em}

h2.fm{font:400 27px/1.2 var(--serif);margin:64px 0 var(--s4);letter-spacing:-.018em;
  scroll-margin-top:72px}
.abstract p{font-size:17px;line-height:1.72;max-width:38rem}

/* ── contents page ────────────────────────────────────────── */
.toc{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));
  gap:1px;background:var(--line);border:1px solid var(--line);border-radius:var(--r);
  overflow:hidden;margin:var(--s5) 0}
.toc section{background:var(--surface);padding:22px 22px 20px}
.toc .pn{font:600 10.5px/1 var(--sans);letter-spacing:.13em;text-transform:uppercase;
  color:var(--felt);margin-bottom:9px}
.toc h3{font:400 19px/1.25 var(--serif);margin:0 0 8px;letter-spacing:-.012em}
.toc .pb{font-size:12.8px;line-height:1.5;color:var(--ink-3);margin:0 0 16px;max-width:none}
.toc ol{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.toc li{border-bottom:1px solid var(--line)}
.toc li:last-child{border-bottom:0}
.toc a{display:flex;gap:10px;padding:9px 0;font-size:13.6px;line-height:1.4;
  color:var(--ink-2);border-bottom:0}
.toc a:hover{color:var(--felt)}
.toc a .tn{font:600 11px/1.45 var(--mono);color:var(--ink-3);flex:none;width:20px}
.toc .pw{font:600 10.5px/1 var(--mono);color:var(--ink-3);margin-top:14px;letter-spacing:.04em}

/* ── part openers ─────────────────────────────────────────── */
.part{margin:120px 0 0;padding-top:40px;border-top:2px solid var(--ink);scroll-margin-top:72px}
.part .pn{font:600 11px/1 var(--sans);letter-spacing:.16em;text-transform:uppercase;
  color:var(--felt);margin-bottom:14px}
.part h2{font:400 clamp(28px,4.4vw,40px)/1.12 var(--serif);letter-spacing:-.02em;margin:0 0 14px}
.part p{font-size:16.5px;line-height:1.6;color:var(--ink-3);max-width:44ch;margin:0}

/* ── sections ─────────────────────────────────────────────── */
.sec{padding-top:var(--s7);scroll-margin-top:64px}
.sec+.sec{border-top:1px solid var(--line);margin-top:var(--s8)}
.sec>h2{font:400 clamp(24px,3.4vw,31px)/1.2 var(--serif);letter-spacing:-.018em;
  margin:0 0 6px;scroll-margin-top:72px}
.sec>h2 .sn{font:600 12px/1 var(--mono);color:var(--felt);display:block;margin-bottom:12px;
  letter-spacing:.1em}
.sec .src{font:11.5px/1.4 var(--mono);color:var(--ink-3);margin:0 0 var(--s6)}
.sec .src code{background:none;padding:0;color:var(--ink-3);font-size:11.5px}

.prose p,.prose ul,.prose ol,.prose blockquote{max-width:38rem}
.prose{font-size:17px;line-height:1.72}
.prose p{margin-bottom:var(--s4);color:var(--ink-2);overflow-wrap:break-word}
.prose h3{font:650 17px/1.35 var(--sans);margin:var(--s7) 0 var(--s3);color:var(--ink)}
.prose h4{font:650 14.5px/1.4 var(--sans);margin:var(--s6) 0 var(--s2);color:var(--ink-2);
  letter-spacing:.01em}
.prose h5,.prose h6{font:600 12px/1.4 var(--sans);letter-spacing:.09em;text-transform:uppercase;
  color:var(--ink-3);margin:var(--s5) 0 var(--s2)}
.prose ul,.prose ol{margin:0 0 var(--s4) 22px;color:var(--ink-2)}
.prose li{margin-bottom:7px}
.prose blockquote{border-left:2px solid var(--felt);padding:2px 0 2px 20px;margin:var(--s5) 0;
  color:var(--ink);font-size:17px}
.prose blockquote p:last-child{margin-bottom:0}
.prose table{min-width:0;margin:0;font-size:14px}
.prose .scroll{margin:var(--s5) 0}
.prose pre{overflow-x:auto;background:var(--sunken);border:1px solid var(--line);
  border-radius:9px;padding:14px;font-size:12.5px;margin-bottom:var(--s4)}
.prose pre code{background:none;padding:0}
.prose img,.prose svg{max-width:100%;height:auto}
.prose hr{margin:var(--s7) 0}
.prose sub{color:var(--ink-3);font-size:12px}
.prose code{overflow-wrap:break-word}

.next{display:flex;justify-content:flex-end;margin-top:var(--s7)}
.next a{font:600 13px/1 var(--sans);color:var(--ink-3);display:inline-flex;gap:8px;
  align-items:baseline;border-bottom:0}
.next a:hover{color:var(--felt)}
.next a span{color:var(--line-2)}

.endnote{margin:var(--s9) 0 0;padding-top:var(--s5);border-top:1px solid var(--line);
  font-size:13.5px;color:var(--ink-3)}
.endnote a{color:var(--ink-3)}
.endnote a:hover{color:var(--felt)}

@media print{
  .bar,.progress,#rail,.scrim,.next,.theme{display:none!important}
  .doc{padding:0}
  .shell{display:block}
  .part{page-break-before:always}
}
"""

PAPER_JS = r"""
const R=document.documentElement;
document.getElementById('tt').onclick=()=>{
  const d=R.getAttribute('data-theme')==='dark'||
    (!R.getAttribute('data-theme')&&matchMedia('(prefers-color-scheme:dark)').matches);
  R.setAttribute('data-theme',d?'light':'dark');
};

/* ── contents drawer (narrow viewports) ── */
const rail=document.getElementById('rail'), scrim=document.getElementById('scrim');
const openTOC=o=>{
  if(o){rail.setAttribute('data-open','');scrim.setAttribute('data-open','')}
  else {rail.removeAttribute('data-open');scrim.removeAttribute('data-open')}
  document.getElementById('toctoggle').setAttribute('aria-expanded',o?'true':'false');
};
document.getElementById('toctoggle').onclick=()=>openTOC(!rail.hasAttribute('data-open'));
document.getElementById('railclose').onclick=()=>openTOC(false);
scrim.onclick=()=>openTOC(false);
addEventListener('keydown',e=>{if(e.key==='Escape')openTOC(false)});
rail.addEventListener('click',e=>{if(e.target.closest('a')&&innerWidth<1080)openTOC(false)});

/* ── where am I ──────────────────────────────────────────────
   One IntersectionObserver over every part opener and section
   heading. The rail, the top bar and the progress line all read
   from the same observed state, so they cannot disagree.       */
const marks=[...document.querySelectorAll('[data-mark]')];
const links=new Map([...rail.querySelectorAll('a[data-for]')].map(a=>[a.dataset.for,a]));
const where=document.getElementById('where');
let current=null;

function setCurrent(id){
  if(id===current)return; current=id;
  for(const a of links.values())a.removeAttribute('aria-current');
  const a=links.get(id);
  const m=document.getElementById(id);
  if(a){a.setAttribute('aria-current','true');
        if(innerWidth>=1080){const t=a.offsetTop-rail.clientHeight/2;
          if(Math.abs(rail.scrollTop-t)>rail.clientHeight/2)rail.scrollTop=Math.max(0,t);}}
  if(m&&m.dataset.part)where.innerHTML='<b>'+m.dataset.part+'</b> · '+m.dataset.label;
  else if(m)where.innerHTML='<b>'+m.dataset.label+'</b>';
}

const io=new IntersectionObserver(()=>{
  let best=null;
  for(const m of marks){
    const r=m.getBoundingClientRect();
    if(r.top<=140)best=m; else break;
  }
  setCurrent(best?best.id:marks[0].id);
},{rootMargin:'-138px 0px -70% 0px',threshold:0});
marks.forEach(m=>io.observe(m));

const prog=document.getElementById('prog');
let tick=false;
addEventListener('scroll',()=>{
  if(tick)return; tick=true;
  requestAnimationFrame(()=>{
    tick=false;
    const h=document.documentElement.scrollHeight-innerHeight;
    prog.style.width=(h>0?Math.min(100,scrollY/h*100):0)+'%';
    let best=null;
    for(const m of marks){ if(m.getBoundingClientRect().top<=140)best=m; else break; }
    if(best)setCurrent(best.id);
  });
},{passive:true});
setCurrent(marks[0].id);
"""


def _demote(md_text):
    """Section bodies use ## for their own subheads, which collides with the
    section heading level once they are stitched into one document. Push every
    heading in a section body down one level so the outline is a true h2 > h3 > h4."""
    return re.sub(r"^(#{2,5})(\s)", lambda m: "#" + m.group(1) + m.group(2),
                  md_text, flags=re.M)


def _md(text, renderer):
    out = renderer.reset().convert(text)
    # Wide content must scroll inside its own container, never the page body.
    out = out.replace("<table>", '<div class="scroll"><table>').replace("</table>", "</table></div>")
    return out


def build_html():
    """Render the survey as a readable web document: persistent contents rail,
    current-position indication, part-level structure, and a measure that
    survives 73,000 words."""
    import markdown
    doc, stats, structure = build()
    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list"])

    total_sections = stats["sections"]
    minutes = round(stats["words"] / 240)

    # ── contents rail: one <ol> per part ──────────────────────────────────
    rail = []
    for p in structure:
        rail.append(f'<ol><li><a class="ph" href="#{p["anchor"]}" data-for="{p["anchor"]}">'
                    f'Part {p["numeral"]} · {html.escape(p["title"])}</a></li>')
        for s in p["sections"]:
            rail.append(f'<li><a href="#{s["anchor"]}" data-for="{s["anchor"]}">'
                        f'<span class="rn">{s["n"]}</span>{html.escape(s["title"])}</a></li>')
        rail.append("</ol>")
    rail_html = "\n".join(rail)

    # ── contents page: same outline, laid out to be read ──────────────────
    toc = []
    for p in structure:
        toc.append(f'<section><div class="pn">Part {p["numeral"]}</div>'
                   f'<h3>{html.escape(p["title"])}</h3>'
                   f'<p class="pb">{html.escape(p["blurb"])}</p><ol>')
        for s in p["sections"]:
            toc.append(f'<li><a href="#{s["anchor"]}"><span class="tn">{s["n"]}</span>'
                       f'<span>{html.escape(s["title"])}</span></a></li>')
        toc.append('</ol></section>')
    toc_html = "\n".join(toc)

    # ── the document ──────────────────────────────────────────────────────
    flat = [s for p in structure for s in p["sections"]]
    body = []
    for p in structure:
        body.append(f'<div class="part" id="{p["anchor"]}" data-mark '
                    f'data-label="Part {p["numeral"]} · {html.escape(p["title"])}">'
                    f'<div class="pn">Part {p["numeral"]}</div>'
                    f'<h2>{html.escape(p["title"])}</h2>'
                    f'<p>{html.escape(p["blurb"])}</p></div>')
        for s in p["sections"]:
            nxt = flat[s["n"]] if s["n"] < len(flat) else None
            src = (f'<p class="src">Source report <code>{html.escape(s["source"])}</code></p>'
                   if s["source"] else "")
            nav = (f'<div class="next"><a href="#{nxt["anchor"]}">'
                   f'<span>Next</span> {html.escape(nxt["title"])} →</a></div>'
                   if nxt else "")
            body.append(
                f'<article class="sec" id="{s["anchor"]}" data-mark '
                f'data-part="Part {p["numeral"]}" data-label="{html.escape(s["title"])}">'
                f'<h2><span class="sn">Section {s["n"]} of {total_sections}</span>'
                f'{html.escape(s["title"])}</h2>{src}'
                f'<div class="prose">{_md(_demote(s["text"]), md)}</div>{nav}</article>')
    body_html = "\n".join(body)

    css = (ROOT / "docs" / "site.css").read_text(encoding="utf-8")
    page = (PAGE_TEMPLATE
            .replace("@@CSS@@", css + PAPER_CSS)
            .replace("@@JS@@", PAPER_JS)
            .replace("@@ABSTRACT@@", _md(ABSTRACT, md))
            .replace("@@HOWTOREAD@@", _md(HOW_TO_READ, md))
            .replace("@@RAIL@@", rail_html)
            .replace("@@TOC@@", toc_html)
            .replace("@@BODY@@", body_html)
            .replace("@@SECTIONS@@", str(total_sections))
            .replace("@@PARTS@@", str(len(structure)))
            .replace("@@WORDS@@", f"{stats['words']:,}")
            .replace("@@MINUTES@@", str(minutes)))
    (ROOT / "docs" / "paper.html").write_text(page, encoding="utf-8")
    print(f"docs/paper.html — {len(page)//1024} KB, {total_sections} sections, "
          f"{len(structure)} parts, contents rail generated from the outline")
    sync_dashboard(stats)



def sync_dashboard(stats):
    """Write the live counts into docs/index.html.

    C-23 was a correction about hand-maintained copies of a number drifting
    from the thing they counted; the dashboard then carried "24 sections ·
    60,300 words" against a 30-section, 75,352-word paper for a week. Any
    figure a machine can count, a machine counts. Elements carrying
    data-gen="<key>" have their text replaced here."""
    f = ROOT / "docs" / "index.html"
    if not f.exists(): return
    ledger = (ROOT / "CORRECTIONS.md")
    counts = {
        "sections": f"{stats['sections']}",
        "words":    f"{stats['words']:,}",
        "parts":    f"{len(PARTS)}",
        "demos":    str(len([d for d in (ROOT / "docs" / "demos").glob("*.html")
                             if d.name != "index.html"])),
    }
    if ledger.exists():
        rows = re.findall(r"^\|\s*\*\*C-\d+\*\*\s*\|.*$",
                          ledger.read_text(encoding="utf-8"), re.M)
        counts["corrections"] = str(len(rows))
        # "found by someone whose job was to fail us" is the number that carries
        # the argument, so it is counted rather than remembered.
        counts["external"] = str(sum("EXTERNAL-REVIEW" in r for r in rows))
    # docs/index.html carries them as <span data-gen="key">, README.md as
    # <!--gen:key-->…<!--/gen-->. Same counts, two syntaxes, one source.
    targets = [(f, r'(data-gen="%s"[^>]*>)([^<]*)(</span>)'),
               (ROOT / "docs" / "deck.html",
                r'(data-gen="%s"[^>]*>)([^<]*)(</span>)'),
]  # README carries no generated counts — a prose front door does not
                  # open on a word count. The dashboard is where the numbers live.
    for path, tpl in targets:
        if not path.exists(): continue
        src = path.read_text(encoding="utf-8")
        out = src
        for key, val in counts.items():
            out = re.sub(tpl % key, lambda m: m.group(1) + val + m.group(3), out)
        if out != src:
            path.write_text(out, encoding="utf-8")
    print("counts synced into docs/index.html and docs/deck.html: " +
          ", ".join(f"{k}={v}" for k, v in counts.items()))

HOW_TO_READ = """\
Every claim carries an evidence label — `MEASURED-RCT`, `MEASURED-META`,
`MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`. A `VENDOR` claim is
never restated as a finding. Every section contains at least one documented null,
given its own space rather than a footnote. Where a number could not be verified it
is reported as unverifiable rather than omitted or softened.

Thirteen of the techniques described here have a
[working demonstration](demos/) that runs in a browser with no server and no key.
Each one states whether it is *computed* — the page performs the operation — or
*scripted*, a labelled replay. One of them documents a mechanism this project
proposed, benchmarked, and **falsified**.
"""

PAGE_TEMPLATE = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Learning in the New Frontier AI World — the survey</title>
<meta name="description" content="A @@WORDS@@-word survey of what AI-native learning has actually been measured to do. Evidence-labelled throughout, nulls first-class, corrections published.">
<link rel="stylesheet" href="site.css">
<style>
@@CSS@@
</style></head>
<body>
<div class="progress" id="prog" role="presentation"></div>

<div class="bar">
  <button id="toctoggle" class="tocbtn" aria-expanded="false" aria-controls="rail">Contents</button>
  <a class="home" href="./"><span aria-hidden="true">←</span> <span class="ht">Learning in the New Frontier AI World</span></a>
  <div class="where" id="where" aria-live="polite"></div>
  <button class="theme" id="tt" aria-label="Toggle colour theme">◐</button>
</div>

<div class="scrim" id="scrim"></div>

<div class="shell">
  <nav id="rail" aria-label="Contents">
    <button id="railclose" class="close" aria-label="Close contents">✕</button>
    <div class="inner">
      <div class="rt">Contents · @@SECTIONS@@ sections</div>
      @@RAIL@@
    </div>
  </nav>

  <main class="doc">
    <div class="col">
      <div class="front">
        <h1>Learning in the New Frontier AI World</h1>
        <p class="standfirst">What AI-native learning has actually been measured to do,
        and a specification for what it should be.</p>
        <dl class="facts">
          <div><dt>Structure</dt><dd>@@PARTS@@ parts, read in any order</dd></div>
          <div><dt>Every claim</dt><dd>labelled and sourced</dd></div>
          <div><dt>Every section</dt><dd>carries a null result</dd></div>
        </dl>
      </div>

      <h2 class="fm" id="abstract" data-mark data-label="Abstract">Abstract</h2>
      <div class="abstract prose">
@@ABSTRACT@@
      </div>

      <h2 class="fm" id="howtoread" data-mark data-label="How to read this">How to read this</h2>
      <div class="prose">
@@HOWTOREAD@@
      </div>

      <h2 class="fm" id="contents" data-mark data-label="Contents">Contents</h2>
      <div class="toc">
@@TOC@@
      </div>

@@BODY@@

      <div class="endnote">
        <p>Every claim is evidence-labelled and every section carries a documented null.
        Our own errors are published in an append-only ledger, not quietly edited:
        <a href="https://github.com/dlmastery/learning-with-ai/blob/main/CORRECTIONS.md">the
        corrections ledger</a>. The adversarial reviews that produced eight of them are in
        <a href="https://github.com/dlmastery/learning-with-ai/tree/main/evidence"><code>evidence/</code></a>;
        the first two returned <em>not publishable</em>.</p>
        <p><a href="./">Dashboard</a> · <a href="demos/">Demos</a> ·
        <a href="https://github.com/dlmastery/learning-with-ai">Repository</a></p>
      </div>
    </div>
  </main>
</div>

<script>
@@JS@@
</script>
</body></html>
"""

if __name__ == "__main__":
    if "--html" in sys.argv: build_html()
    else: build()

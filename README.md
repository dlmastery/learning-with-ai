# Learning in the New Frontier AI World

**A research survey of what AI tutoring has actually been measured to do — and a specification for
what it should be.**

[Read the survey](https://dlmastery.github.io/learning-with-ai/paper.html) ·
[Run the demos](https://dlmastery.github.io/learning-with-ai/demos/) ·
[15-slide version](https://dlmastery.github.io/learning-with-ai/deck.html) ·
[Corrections ledger](CORRECTIONS.md)

---

## What this is

An open research artifact, not a product or a library. It contains three things:

1. **A survey** — thirty-eight sections, assembled into a single paper, on what the evidence
   actually supports about learning with AI. Every claim carries an evidence label; every section
   carries at least one documented null result.
2. **The research behind it** — forty reports in [`research/raw/`](research/raw/), each written
   against primary sources, kept verbatim and never rewritten. These are the input; the survey is
   the output.
3. **Fourteen working demonstrations** that run in a browser with no server and no API key. Each
   states plainly what it proves and what it merely illustrates. One of them documents a mechanism
   this project proposed, benchmarked, and then falsified.

It is written for people building or funding AI learning systems, for researchers deciding what to
measure next, and for anyone who needs to tell a real finding from a vendor claim in this field.

## Why it exists

Because the field has produced an enormous amount of work and almost no evidence.

Across twenty education-AI subfields there are **2,907 arXiv papers, at most 1.79% carrying any
learning-outcome marker, and eight subfields at exactly zero.** ERIC holds 1,565 records on ChatGPT
in education and **seven randomised trials** — four of them second-language learning. The
literature measures resemblance, preference and engagement. It very rarely measures whether anyone
learned anything, and almost never measures it *after the tool is taken away*.

And there is a specific gap underneath that one. A census of ERIC and Europe PMC returns **30
randomised trials of generative-AI tutoring that mention students, and zero that mention
disability, dyslexia, ADHD, autism, special education or an IEP.** Every effect size in this field
was measured on somebody else's child.

This project started with a specific one: eleven years old, served under a SELPA plan, able to hold
a conversation about photosynthesis and unable to pass a worksheet about it. Designing for her is
the organising constraint here, not a charitable sidebar.

---

## What it found

### The finding the survey turns on

Across **223 real tutoring domains, no language model beat chance at labelling an incorrect student
action.** Not "performed poorly" — chance. Looking at what a learner did and saying what is wrong
with it is the most basic thing a tutor does, and it is currently unverifiable by the systems being
sold to do it.

That is not an isolated weakness. An agent differs from a chatbot in four ways — it can **sample**
many times, **execute** and see what happened, **persist** state across a boundary, and work in
your **absence**. Each is a multiplier on something else, and none produces value alone. Which
gives a rule:

> **The value of an agentic loop is bounded by the value of the external check it closes on.**

Where a strong check exists, agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where it is weak or missing, **21.0%** (PaperBench) and **4.6%** (SciCode, which
does have hand-written tests — which is why the rule is a bound and not an equality). A twenty-fold
spread, and the axis is not task difficulty.

**Coding agents work because `pytest` exists. Pedagogy has no `pytest`** — and every agentic
capability in education is waiting on that one missing instrument.

### Three results that disqualify most of what is being built

**Felt learning and real learning move in opposite directions.** Preference shifts at *d* ≈ 0.48
while knowledge does not move, and the effect survives explicit debiasing. In one controlled
comparison, students in the condition that taught them *more* reported learning *less*.

**Measurement without a decision rule is inert.** In the randomised trial that settles it, both
arms revised instruction more often — and only the arm told *what to change* moved achievement.
Dashboards, streaks, mastery bars and adaptive difficulty are all the arm that measured more and
changed nothing.

**Unguarded assistance is an active harm.** It leaves learners **17% worse** on later unassisted
work. The guardrailed arm's unassisted coefficient is **−0.004, not significant** — harm removed,
benefit not demonstrated.

### On speed

Learning is counted in opportunities, not days. Across 1.3 million observations, learning *rate*
varies by **1.14×** between the 25th and 75th percentile while *prior knowledge* varies by
**3.6×**. The defensible bound is **10–40× on elapsed calendar time and 3–5× on engaged effort**,
with a hard **1×** on durability and on procedural skill.

> A week's understanding in an hour. A year's retention in six hours spread over two months.

What limits polymathy is not learning rate. It is the fixed cost of orientation — how many times
you can afford to be a beginner.

---

## How to read it

| If you are… | Start here |
|---|---|
| Deciding what to build | [The finding](https://dlmastery.github.io/learning-with-ai/paper.html) → the three results above → [the demos](https://dlmastery.github.io/learning-with-ai/demos/) |
| Deciding what to fund | [The 15-slide deck](https://dlmastery.github.io/learning-with-ai/deck.html), then [the long-form thesis](https://dlmastery.github.io/learning-with-ai/thesis.html) |
| A researcher | [The nineteen open problems](research/raw/F9-open-problems.md) — each with a runnable design, power justification, and pre-registered falsifier |
| A parent or teacher | [The Empty Chair](survey/04-the-empty-chair.md) and [The Coordinator's Week](survey/31-the-coordinators-week.md) |
| Sceptical | [The five adversarial reviews](evidence/) — the first four returned *not publishable* |

---

## The central claim, and how to kill it

The measured 0.2–0.4 SD band describes systems that answer freely, forget everything between
sessions, cannot see the work, cannot point, never change method, and agree with the learner.
Nobody has built and measured the constrained, grounded, pivoting, remembering, teachable
alternative.

**That nobody has measured it is proven. That it would do better is a hypothesis.**

The concession conditions are stated in advance: a well-powered trial of the assembled system, with
a delayed, unassisted, novel-item primary outcome, landing *inside* the 0.2–0.4 band rather than
above it. That would mean the mechanisms are decorative and the band is the ceiling.

If you run one of the open problems, the result is wanted whichever way it lands. Especially the
nulls.

---

## How to verify it

This survey got things wrong. The record of that is the reason to trust the rest of it.

[`CORRECTIONS.md`](CORRECTIONS.md) is an append-only ledger with a provenance column, and a
substantial minority of its entries were found by **adversarial reviewers rather than by us** —
including the two most damaging numbers, and one about the ledger itself, which was being silently
edited inside a table headed *"published rather than silently edited."*

Five hostile reviews are in [`evidence/`](evidence/). The first four returned **not publishable**.

Three machine checks guard the repository, and all three are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
python3 evidence/check-repetition.py                         # every restated finding is cross-referenced
node evidence/test-demos.mjs                                 # every demo renders and runs
```

The first version of that corrections checker **did not work.** A reviewer copied the repository,
planted the original errors back in, and it reported zero violations. It now ships with a self-test
that plants each violation and fails if the rule does not fire.

**The editorial standard.** Every claim carries one of `MEASURED-RCT`, `MEASURED-META`,
`MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO` or `INFERENCE`. A `VENDOR` claim is never restated
as a finding. Every section contains at least one documented null result, given its own space.
Claims that could not be verified are reported as unverifiable rather than dropped.

---

## Repository structure

| Path | Contents |
|---|---|
| [`PAPER.md`](PAPER.md) | The survey, assembled — abstract, seven parts, continuous numbering |
| [`survey/`](survey/) | The sections, one file each. The paper and the web edition are built from these |
| [`research/raw/`](research/raw/) | The forty research reports. The input — never rewritten, superseded only by dated successors |
| [`CORRECTIONS.md`](CORRECTIONS.md) | The corrections ledger |
| [`evidence/`](evidence/) | Adversarial reviews, the machine checks, the paper builder, and original measurements |
| [`docs/`](docs/) | The published site — dashboard, paper, deck, thesis, demos |
| [`process/`](process/) | Backstage: the research plan, an audit written against ourselves, the working ledger |

```bash
python3 evidence/build-paper.py --html   # rebuild PAPER.md and the site from survey/
```

## Contributing

Corrections are the currency here. If you find an error, **open an issue with the primary source**
— every correction gets published in the ledger with attribution, including the ones that make this
project look bad. Those are the ones worth having.

If you cite this work, cite the report in [`research/raw/`](research/raw/) rather than the survey
summary. The report carries the sources and the evidence labels.

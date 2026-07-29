# Learning in the New Frontier AI World

A survey of what AI tutoring has actually been measured to do, and a specification for what it
should be.

**[Read it](https://dlmastery.github.io/learning-with-ai/paper.html)** ·
[run the demos](https://dlmastery.github.io/learning-with-ai/demos/) ·
[the fourteen-slide version](https://dlmastery.github.io/learning-with-ai/deck.html) ·
[as one markdown file](PAPER.md)

---

## The finding

Across **223 real tutoring domains, no language model beat chance at labelling an incorrect
student action.** Not "performed poorly" — chance. Looking at what a learner did and saying what
is wrong with it is the most basic thing a tutor does, and it is currently unverifiable by the
systems being sold to do it.

That is not an isolated weakness. It explains the whole reliability landscape.

An agent differs from a chatbot in four ways — it can **sample** many times, **execute** and see
what happened, **persist** state across a boundary, and work in your **absence**. Each is a
multiplier on something else, and none produces value alone. So:

> **The value of an agentic loop is bounded by the value of the external check it closes on.**

Where a strong check exists, agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where it is weak or missing, **21.0%** (PaperBench) and **4.6%** (SciCode,
which does have hand-written tests — which is why the rule is a bound and not an equality).

A twenty-fold spread, and the axis is not task difficulty. It is how good the check is.

**Coding agents work because `pytest` exists. Pedagogy has no `pytest`** — and every agentic
capability in education is waiting on that one missing instrument.

---

## Three results that disqualify most of what is being built

**Felt learning and real learning move in opposite directions.** Preference shifts at *d* ≈ 0.48
while knowledge does not move, and the effect survives explicit debiasing. In one controlled
comparison, students in the condition that taught them *more* reported learning *less*. Every
metric a product can cheaply optimise is the wrong one.

**Measurement without a decision rule is inert.** In the randomised trial that settles it, both
arms revised instruction more often — and only the arm told *what to change* moved achievement.
Dashboards, streaks, mastery bars and adaptive difficulty are all the arm that measured more and
changed nothing.

**Unguarded assistance is an active harm.** It leaves learners **17% worse** on later unassisted
work. The guardrailed arm's unassisted coefficient is **−0.004, not significant** — harm removed,
benefit not demonstrated. Anyone selling restraint as a learning gain is ahead of the evidence,
including an earlier draft of this survey.

---

## On speed

Learning is counted in opportunities, not days. Across 1.3 million observations, learning *rate*
varies by **1.14×** between the 25th and 75th percentile while *prior knowledge* varies by
**3.6×** — and time-based models of learning fit poorly.

The defensible bound is **10–40× on elapsed calendar time and 3–5× on engaged effort**, with one
documented case near 300× where the baseline was informal experience rather than a course. And a
hard **1×** on durability and on procedural skill: a year-durable memory needs gaps of 18–36 days,
and seventy years of compressing language training still leaves 552–2,200 hours.

> A week's understanding in an hour. A year's retention in six hours spread over two months.

What limits polymathy is not learning rate. It is the fixed cost of orientation — how many times
you can afford to be a beginner.

---

## Why it exists

A census of ERIC and Europe PMC returns **30 randomised trials of generative-AI tutoring that
mention students, and zero that mention disability, dyslexia, ADHD, autism, special education or
an IEP.** Every effect size in this field was measured on somebody else's child.

The project began with a specific one: eleven years old, served under a SELPA plan, able to hold
a conversation about photosynthesis and unable to pass a worksheet about it. Designing for her is
the organising constraint here, not a charitable sidebar.

And the field is not measuring the thing it claims to. Across 20 education-AI subfields:
**2,907 arXiv papers, at most 1.79% carrying any learning-outcome marker, eight subfields at
exactly zero.** ERIC holds 1,565 records on ChatGPT in education and **seven randomised trials**,
four of them second-language learning.

---

## The central claim, and how to kill it

The measured 0.2–0.4 SD band describes systems that answer freely, forget everything between
sessions, cannot see the work, cannot point, never change method, and agree with the learner.
Nobody has built and measured the constrained, grounded, pivoting, remembering, teachable
alternative.

**That nobody has measured it is proven. That it would do better is a hypothesis.**

The concession conditions are named in advance: a well-powered trial of the assembled system, with
a delayed, unassisted, novel-item primary outcome, landing *inside* the 0.2–0.4 band rather than
above it. That would mean the mechanisms are decorative and the band is the ceiling.

If you run one of the [nineteen open problems](research/raw/F9-open-problems.md), the result is
wanted whichever way it lands. Especially the nulls.

---

## How to check it

This survey got things wrong. The record of that is the reason to trust the rest of it.

**[`CORRECTIONS.md`](CORRECTIONS.md) is an append-only ledger with a provenance column, and a
substantial minority of its entries were found by adversarial reviewers rather than by us** —
including the two most damaging numbers, and one about the ledger itself, which was being silently
edited inside a table headed *"published rather than silently edited."*

Five hostile reviews are in [`evidence/`](evidence/). The first four returned **not publishable**.
If you want to know whether to trust this document, read those before you read the survey.

Three machine checks guard it, and all three are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
python3 evidence/check-repetition.py                         # every restated finding is cross-referenced
node evidence/test-demos.mjs                                 # every demo renders and runs
```

The first version of that corrections checker **did not work.** A reviewer copied the repository,
planted the original errors back in, and it reported zero violations. It now ships with a
self-test that plants each violation and fails if the rule does not fire.

Every claim in the survey carries one of `MEASURED-RCT`, `MEASURED-META`, `MEASURED-BENCH`,
`OBSERVED`, `VENDOR`, `DEMO` or `INFERENCE`. A `VENDOR` claim is never restated as a finding.
Every section contains at least one documented null result, given its own space. Claims that could
not be verified are reported as unverifiable rather than dropped.

---

## The repository

| | |
|---|---|
| [`PAPER.md`](PAPER.md) | The survey, assembled — abstract, seven parts, continuous numbering |
| [`survey/`](survey/) | The sections, one file each. The paper and the web edition are built from these |
| [`research/raw/`](research/raw/) | The research reports behind every claim. The input, never rewritten — superseded only by dated successors |
| [`CORRECTIONS.md`](CORRECTIONS.md) | The corrections ledger |
| [`evidence/`](evidence/) | The reviews, the checkers, the paper builder, and original measurements |
| [`docs/`](docs/) | The published site |
| [`process/`](process/) | Backstage — the research plan, an audit written against ourselves, the working ledger |

```bash
python3 evidence/build-paper.py --html   # rebuild the paper and the site
```

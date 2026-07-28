# Learning in the New Frontier AI World

**A survey of what AI-native learning has actually been measured to do — and a specification for
what it should be.**
<!--gen:sections-->32<!--/gen--> sections, <!--gen:words-->78,652<!--/gen--> words, built on
~2,100 sources.

**[Read it on the web](https://dlmastery.github.io/learning-with-ai/paper.html)** ·
[as one markdown file](PAPER.md) ·
[thirteen demos that run in a browser](https://dlmastery.github.io/learning-with-ai/demos/) ·
[the dashboard](https://dlmastery.github.io/learning-with-ai/)

---

## The three findings

**1 · Felt learning and real learning move in opposite directions.**
Preference shifts at *d* ≈ 0.48 while knowledge does not move, and the effect survives explicit
debiasing. Students in the condition that taught them *more* reported learning *less*. Every metric
a product can cheaply optimise is the wrong one.

**2 · Measurement without a decision rule is inert.**
In the randomised trial that settles it, both arms revised instruction more often — and **only the
arm told *what to change* moved achievement**. Dashboards, streaks, mastery bars and adaptive
difficulty are all the arm that measured more and moved nothing.

**3 · Unguarded assistance is an active harm.**
It leaves learners **17% worse** on later unassisted work. The guardrailed arm's unassisted
coefficient is **−0.004, not significant**. Restraint removes the harm; it has not been shown to
teach. Anyone selling it as a learning gain is ahead of the evidence.

---

## Why this exists

A census of ERIC and Europe PMC returns **30 randomised trials of generative-AI tutoring that
mention students, and zero that mention disability, dyslexia, ADHD, autism, special education or an
IEP.**

Every effect size in this field was measured on somebody else's child. The project began with a
specific one — eleven years old, served under a SELPA plan, able to discuss photosynthesis and
unable to pass a worksheet about it. Designing for her is the organising constraint, not a
charitable sidebar.

And the field is not measuring the thing it claims to. An exhaustive census across 20
education-AI subfields: **2,907 arXiv papers, at most 1.79% carrying any learning-outcome marker,
eight subfields at exactly zero.** ERIC holds 1,565 records on ChatGPT in education and **seven
RCTs**, four of them second-language learning.

---

## The central claim, and how to kill it

The measured 0.2–0.4 SD band describes systems that answer freely, forget everything between
sessions, cannot see the work, cannot point, never change method, and agree with the learner.
Nobody has built and measured the constrained, grounded, pivoting, remembering, teachable
alternative.

**That nobody has measured it is proven. That it would do better is a hypothesis.**

Part VII names the concession conditions in advance. The shortest version: a well-powered trial of
the assembled system, with a **delayed, unassisted, novel-item** primary outcome, landing *inside*
the 0.2–0.4 band rather than above it. That would mean the mechanisms are decorative and the band
is the ceiling.

If you run one of the [19 open problems](research/raw/F9-open-problems.md), we want the result
whichever way it lands. Especially the nulls.

---

## How to check it

The claim that should make you suspicious of any survey is that it got everything right. This one
did not, and the record is the point.

**<!--gen:corrections-->28<!--/gen--> corrections, published in an append-only ledger with a
provenance column.** <!--gen:external-->8<!--/gen--> were found by an adversarial reviewer, not by us — including the two most
damaging, and one about the corrections ledger itself, which we had been silently editing inside a
table headed *"published rather than silently edited."*

The three review reports are in [`evidence/`](evidence/) and the first two returned **not
publishable**. If you want to know whether to trust this document, read those before you read the
survey.

Two machine checks guard it, and both are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
node evidence/test-demos.mjs                                 # every demo page renders and runs
```

The first version of that corrections checker **did not work** — a reviewer planted the original
errors back in and it reported zero violations. It now ships with a self-test that plants each
violation and fails if the rule does not fire.

Every claim in the survey carries one of `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` ·
`OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`. A `VENDOR` claim is never restated as a finding.
Every section contains at least one documented null, given its own space. Unverifiable claims are
reported as unverifiable — never laundered, never omitted.

---

## What is in this repository

| | |
|---|---|
| [`PAPER.md`](PAPER.md) | The survey, assembled — abstract, seven parts, continuous numbering |
| [`survey/`](survey/) | The sections, one file each. `PAPER.md` and the web version are built from these |
| [`research/raw/`](research/raw/) | The research reports — roughly 406,000 words, ~2,100 sources. The input, never rewritten |
| [`CORRECTIONS.md`](CORRECTIONS.md) | The append-only corrections ledger, with provenance |
| [`evidence/`](evidence/) | Adversarial reviews, measurement harnesses, the checkers, and the paper builder |
| [`docs/`](docs/) | The published site: dashboard, the survey as a web document, thirteen demos |

Rebuild the paper and the site's generated counts:

```bash
python3 evidence/build-paper.py --html
```

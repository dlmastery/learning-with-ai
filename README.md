# Learning in the New Frontier AI World

**A 740,000-word survey of what AI-native learning has actually been measured to do — and a
specification for what it should be.**

### → **[Read the paper](PAPER.md)** · [web version](https://dlmastery.github.io/learning-with-ai/paper.html) · [29 sections, 74,182 words]

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

## What is in here

| | |
|---|---|
| **[`PAPER.md`](PAPER.md)** | The survey — 29 sections in 7 parts, with abstract and contents |
| [`research/raw/`](research/raw/) | 32 research reports, ~406,000 words, ~2,100 sources — the input, never rewritten |
| [`CORRECTIONS.md`](CORRECTIONS.md) | 24 corrections, append-only, with a provenance column |
| [`evidence/`](evidence/) | Three adversarial reviews, measurement harnesses, and the checkers |
| [Demos](https://dlmastery.github.io/learning-with-ai/demos/) | 13 techniques running in a browser — no server, no key |
| [Dashboard](https://dlmastery.github.io/learning-with-ai/) | The numbers, the K-12→postgraduate matrix, the open questions |

---

## How to read it critically

The claim that should make you suspicious of any survey is that it got everything right. This one
did not, and the record is the point.

**24 corrections. 9 of them were found by an adversarial reviewer, not by us** — including
the two most damaging, and one about the corrections ledger itself, which we had been silently
editing inside a table headed *"published rather than silently edited."*

The three review reports are in [`evidence/`](evidence/) and the first two returned **not
publishable**. If you want to know whether to trust this document, read those before you read the
paper.

Two machine checks guard it, and both are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
node evidence/test-demos.mjs                                  # every demo page renders and runs
```

The first version of that corrections checker **did not work** — a reviewer planted the original
errors back in and it reported zero violations. It now ships with a self-test that plants each
violation and fails if the rule does not fire.

---

## The editorial standard

Every claim carries one of `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED` ·
`VENDOR` · `DEMO` · `INFERENCE`.

1. A `VENDOR` claim may **never** be restated as a finding.
2. Every section contains at least one documented **null**, given its own space.
3. Unverifiable claims are reported as unverifiable — never laundered, never omitted.
4. **Effect sizes over adjectives.**
5. A subagent's characterisation of a source is a **lead, not a finding**.
6. Progress is reported in **survey words**, never in report count.

Charts are generated from a declarative spec by a deterministic renderer — never hand-positioned —
because our own research rates hand-written SVG Tier D. The palette is computationally validated
for colour-vision deficiency, not eyeballed.

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

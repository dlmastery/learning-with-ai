# Learning in the New Frontier AI World

**A research survey of what AI tutoring has actually been measured to do, and a specification for
what it should be.**

[Read the survey](https://dlmastery.github.io/learning-with-ai/paper.html) ·
[Run the demos](https://dlmastery.github.io/learning-with-ai/demos/) ·
[The deck](https://dlmastery.github.io/learning-with-ai/deck.html) ·
[Corrections ledger](CORRECTIONS.md)

---

## What this is

An open research artifact. Not a product, not a library. It contains three things:

1. **A survey**, assembled into a single paper, on what the evidence supports about learning with
   AI. Every claim carries an evidence label. Every section carries at least one documented null
   result, given its own space.
2. **The research behind it** in [`research/raw/`](research/raw/), written against primary
   sources and kept verbatim. A report is superseded by a dated successor and never rewritten in
   place. These are the input; the survey is the output.
3. **Working demonstrations** that run in a browser with no server and no API key. Each states
   what it proves and what it merely illustrates. One documents a mechanism this project
   proposed, benchmarked, and then falsified.

It is written for people building or funding AI learning systems, for researchers deciding what
to measure next, and for anyone who needs to tell a real finding from a vendor claim.

## Why it exists

The field has produced an enormous amount of work and almost no evidence.

Across twenty education-AI subfields there are **2,907 arXiv papers, at most 1.79% carrying any
learning-outcome marker, and eight subfields at exactly zero.** ERIC holds 1,565 records on
ChatGPT in education and **seven randomised trials**, three of them second-language learning. The
literature measures resemblance, preference and engagement. It rarely measures whether anyone
learned anything, and almost never measures it *after the tool is taken away*.

Underneath that sits a sharper gap. A census of ERIC and Europe PMC returns **30 randomised
trials of generative-AI tutoring that mention students, and zero that mention disability,
dyslexia, ADHD, autism, special education or an IEP.** Every effect size in this field was
measured on somebody else's child.

This project started with one child: eleven years old, served under a SELPA plan, able to hold a
conversation about photosynthesis and unable to pass a worksheet about it. Designing for her is
the organising constraint, not a charitable sidebar.

---

## What it found

### The finding the survey turns on

Across **223 tutoring domains, the models tested did not beat chance at labelling an incorrect
student action.** Reading a learner's belief from what they did is the most basic thing a tutor
does, and no instrument for it has been built.

Scope it correctly, because that sharpens the claim. Step-checking a model's *own* reasoning
trace is not at chance: ProcessBench reports open models competitive with GPT-4o at finding the
earliest erroneous step. Checking a chain of symbols is solved. **Reading a person is the part
nobody has done**, and the distance between those two is the opportunity.

That weakness is not isolated. An agent differs from a chatbot in four ways. It can sample many
times, execute and see what happened, persist state across a boundary, and work in your absence.
Each multiplies something else and none produces value alone, which gives a rule:

> **The value of an agentic loop is bounded by the value of the external check it closes on.**

Where a strong check exists, agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where it is weak or missing, **21.0%** (PaperBench) and **4.6%** (SciCode,
which does have hand-written tests, and is why the rule is a bound rather than an equality). A
twenty-fold spread that tracks the quality of the check, not the difficulty of the task.

**Coding agents work because `pytest` exists. Pedagogy has no `pytest`**, and every agentic
capability in education is waiting on that one missing instrument.

### Three results that disqualify most of what is being built

**Felt learning and real learning move in opposite directions.** Preference shifts at *d* ≈ 0.48
while knowledge stays flat, and debiasing the learners does not remove it. In one controlled
comparison the students who learned *more* reported learning *less*.

**Measurement without a decision rule is inert.** A randomised trial gave one arm data and the
other arm data plus instructions on what to do about it. Both revised their teaching more often.
Only the second arm's students scored higher. Dashboards, streaks, mastery bars and adaptive
difficulty all sit on the first arm's side of that line.

**Unguarded assistance is an active harm**, leaving learners **17% worse** on later unassisted
work. Adding guardrails takes the damage away without putting a benefit in its place: the
guardrailed arm's unassisted coefficient is **−0.004, not significant.**

### On speed

Learning is counted in opportunities, not days. Across 1.3 million observations, learning *rate*
varies by **1.14×** between the 25th and 75th percentile while *prior knowledge* varies by
**3.6×**. The defensible bound is **10–40× on elapsed calendar time and 3–5× on engaged effort**,
with a hard **1×** on durability and on procedural skill.

> A week's understanding in an hour. A year's retention in six hours spread over two months.

The limit on polymathy is the fixed cost of orientation: how many times you can afford to be a
beginner.

---

## How to read it

| If you are… | Start here |
|---|---|
| Deciding what to build | [The finding](https://dlmastery.github.io/learning-with-ai/paper.html) → the three results above → [the demos](https://dlmastery.github.io/learning-with-ai/demos/) |
| Deciding what to fund | [The deck](https://dlmastery.github.io/learning-with-ai/deck.html), then [the long-form thesis](https://dlmastery.github.io/learning-with-ai/thesis.html) |
| A researcher | [The open problems](research/raw/F9-open-problems.md), each with a runnable design, power justification, and pre-registered falsifier |
| A parent or teacher | [The Empty Chair](survey/04-the-empty-chair.md) and [The Coordinator's Week](survey/31-the-coordinators-week.md) |
| Sceptical | [The adversarial reviews](evidence/). The first four returned *not publishable* |

---

## The central claim, and how to kill it

The measured 0.2–0.4 SD band describes systems that answer freely, forget everything between
sessions, cannot see the work, cannot point, never change method, and agree with the learner.
Nobody has built and measured the constrained, grounded, pivoting, remembering, teachable
alternative.

**That nobody has measured it is proven. That it would do better is a hypothesis.**

The concession conditions are stated in advance. A well-powered trial of the assembled system,
with a delayed, unassisted, novel-item primary outcome, landing *inside* the 0.2–0.4 band rather
than above it, would mean the mechanisms are decorative and the band is the ceiling.

If you run one of the open problems, the result is wanted whichever way it lands. Especially the
nulls.

---

## How to verify it

This survey got things wrong. The record of that is the reason to trust the rest of it.

[`CORRECTIONS.md`](CORRECTIONS.md) is an append-only ledger with a provenance column. A
substantial minority of its entries were found by **adversarial reviewers rather than by us**,
including the two most damaging numbers, and one about the ledger itself, which was being
silently edited inside a table headed *"published rather than silently edited."*

The reviews are in [`evidence/`](evidence/). The first four returned **not publishable**.

Six machine checks guard the repository, and all six are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
python3 evidence/check-repetition.py                         # every restated finding is cross-referenced
python3 evidence/check-stance.py --strict                    # the discipline is the warrant, not the message
python3 evidence/check-voice.py --strict                     # no sentence shape used until it stops meaning anything
node evidence/test-demos.mjs                                 # every demo renders and runs, 390/1400 × light/dark
node evidence/check-links.mjs                                # every internal link and anchor resolves
```

The first version of the corrections checker **did not work.** A reviewer copied the repository,
put the original errors back, and it reported nothing. It now ships with a self-test that plants
each violation and fails if the rule does not fire.

**The editorial standard.** Every claim carries one of `MEASURED-RCT`, `MEASURED-META`,
`MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`, `CRAFT`, `SPEC`, `STATUTE` or
`FILING`. A `VENDOR` claim is never restated as a finding. Claims that could not be verified are
reported as unverifiable rather than dropped.

---

## Repository structure

| Path | Contents |
|---|---|
| [`PAPER.md`](PAPER.md) | The survey, assembled: abstract, seven parts, continuous numbering |
| [`survey/`](survey/) | The sections, one file each. The paper and the web edition are built from these |
| [`research/raw/`](research/raw/) | The research reports. The input, never rewritten, superseded only by dated successors |
| [`CORRECTIONS.md`](CORRECTIONS.md) | The corrections ledger |
| [`evidence/`](evidence/) | Adversarial reviews, the machine checks, the paper builder, original measurements |
| [`docs/`](docs/) | The published site: dashboard, paper, deck, thesis, demos |
| [`process/`](process/) | Backstage: the research plan, an audit written against ourselves, the assumptions log |

```bash
python3 evidence/build-paper.py --html   # rebuild PAPER.md and the site from survey/
```

## Contributing

Corrections are the currency here. If you find an error, **open an issue with the primary
source.** Every correction gets published in the ledger with attribution, including the ones that
make this project look bad. Those are the ones worth having.

If you cite this work, cite the report in [`research/raw/`](research/raw/) rather than the survey
summary. The report carries the sources and the evidence labels.

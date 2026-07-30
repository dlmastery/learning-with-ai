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
the organising constraint here, and never a charitable sidebar.

---

## What it found

### What a 2026 model has been measured to do

Seven trials have put a post-2023 LLM in front of a learner and measured a learning outcome. This
is all of them, each in the form its published correction requires.

| Trial | Result | What the outcome was |
|---|---|---|
| Kestin, Harvard physics, 2025 | *d* ≈ 0.63 | Immediate post-test, in 49 minutes against an assumed 60. Developer-built and developer-evaluated, no funding statement |
| Rori, Ghana, 2024 | +0.37 SD | Eight months, but 11 clusters, and the provider's own staff are the authors |
| Nigeria, World Bank, 2025 | +0.310 SD composite; +0.206 SD on the school's own exam | The one distal outcome here that moved. 43% attrition |
| Sierra Leone, 2026 | +0.258 SD adjusted; +0.216 SD unadjusted and not significant | Endline only. Gains load on Grade 8 and grow with prior attainment |
| LearnLM + Eedi, 2025 | +5.5 p.p. on the next unit's first problem, against human tutors | 165 students, and a 95% credible interval of [−1.4, +12.4] |
| Tutor CoPilot, 2024 | +4 p.p. on the exit ticket | Null on the end-of-year test |
| Bastani, Turkey, 2025 | +127% on assisted practice | −0.004 on unassisted work, not significant |

Two things are true of that table at once. It holds the strongest tutoring result anyone has
measured on a frontier model, and it holds a trial where assistance left learners worse off once
the tool was taken away. Bastani is the one study that isolates why: both of its arms ran the same
GPT-4, and the arm allowed to answer freely produced the harm while the constrained arm did not.
The live variable there is what the system was permitted to do, which is the part a builder
chooses.

**Not one row measured a delayed, unassisted test on items the learner had never seen.** The
frontier era has not run into a ceiling. It has not yet run the experiment that could find one.

### The finding the survey turns on

Across **223 tutoring domains, the four models TutorGym evaluated did not beat chance at
labelling an incorrect student action** — an August–October 2024 snapshot set, prompted zero-shot
with no tools, in what the authors call an initial evaluation. Date it, because that is a
two-year-old measurement and the obvious next move is to rerun it. Reading a learner's belief from
what they did is the most basic thing a tutor does, and no instrument for it has been built.

Scope it correctly, because that sharpens the claim. Step-checking a model's *own* reasoning
trace is not at chance: ProcessBench reports open models competitive with GPT-4o at finding the
earliest erroneous step. Checking a chain of symbols is solved. **Reading a person is the part
nobody has done**, and the distance between those two is the opportunity.

That weakness is not isolated. An agent differs from a chatbot in four ways. It can sample many
times, execute and see what happened, persist state across a boundary, and work in your absence.
Each multiplies something else and none produces value alone, which gives a rule:

> **The value of an agentic loop is bounded by the value of the external check it closes on.**

Where a strong check exists, frontier agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where it is weak or missing, **21.0%** (PaperBench) and **4.6%** (SciCode,
which does have hand-written tests, and is why the rule is a bound and not an equality). A
twenty-fold spread, and what varies across it is the quality of the check. Task difficulty
does not explain it.

**Coding agents work because `pytest` exists. Pedagogy has no `pytest`**, and every agentic
capability in education is waiting on that one missing instrument.

### Three results that disqualify most of what is being built

**Felt learning and real learning move in opposite directions.** Buljan et al. 2018 ran three
RCTs, n = 334 adults, comparing an infographic with a plain-language summary: preference moved
*d* ≈ 0.48 and knowledge moved zero. Kaspar 2025, N = 179, played a debiasing video first and the
easiness effect survived it. Neither study involved a tutor or a model, which is the point:
the dissociation is a property of how people judge their own learning, so a frontier system
inherits it the moment it starts optimising on ratings. In Deslauriers 2019 the students who
learned *more* reported learning *less*.

**Measurement without a decision rule is inert.** Fuchs, Hamlett & Stecker 1991 randomised 33
teachers to progress data, progress data plus a rule for acting on it, or neither. Both measured
arms revised instruction more often. Only the arm with the rule moved achievement. That is a
1991 result about human teachers and an expert system, and it constrains a 2026 dashboard for a
structural reason and not a technological one: dashboards, streaks, mastery bars and adaptive
difficulty are all the arm without the rule.

**Unguarded assistance is an active harm.** Bastani et al. 2025 is a frontier-model RCT, ~1,000
Turkish high-school students with GPT-4, and the arm given an unconstrained assistant came back
**17% worse** on unassisted work. Adding guardrails takes the damage away without putting a
benefit in its place: the guardrailed arm's unassisted coefficient is **−0.004, not significant.**
This is the strongest evidence in the corpus that constraint design is the live variable, and it
is also the reason no constrained system can yet claim a gain. It has 109 citing works in fourteen
months and no replication with a withdrawal design.

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

Three frontier-era field trials have deployed an LLM tutor at scale and measured a learning
outcome: Sierra Leone at +0.258 SD adjusted, Nigeria at +0.310 SD composite, Rori at +0.37 SD.
Three trials, no pooled estimate, no meta-analysis and no confidence interval across them. One of
those headlines is not significant unadjusted. One loses a third of its effect on the school's own
exam. One has eleven clusters and was written by the provider's own staff. That is the whole
measured record, and it is far too thin to be read as a level anything settles at.

The clause the source report calls the genuinely important finding is the one that keeps getting
dropped: those gains arrive **at much lower cost**. Tutor CoPilot ran at $20 per tutor per year.
Measured API spend in a supervised deployment is $19.86 per tutor per year, and inference is 0.43%
of what a delivered session costs. Kestin's arm reached its post-test in a median 49 minutes
against an assumed 60. Cost and time are where the frontier-era numbers are unambiguous, and they
are the half of the finding this survey had been leaving out.

Every one of those trials ran a chatbot with a prompt. It answers freely, forgets everything between
sessions, cannot see the work, cannot point, never changes method, and agrees with the learner. The
constrained, grounded, pivoting, remembering, teachable alternative that this survey specifies has
not been assembled, and so has never been measured against anything.

**That nobody has measured the assembled system is proven. That it would do better is a
hypothesis.**

The concession conditions are stated in advance. A well-powered trial of the assembled system,
with a delayed, unassisted, novel-item primary outcome, run against a plain frontier-model chatbot
as the active control: if the assembled system does not beat that arm, the mechanisms are
decorative and the model was doing all the work. The comparator is a frontier model because that
is the only thing whose defeat would mean anything. Beating a classroom, or a system from another
decade, would leave the question exactly where it is now.

That falsifier has teeth. Fütterer et al. 2026, *n* = 371 across Grades 7–9, ran two designed
GenAI scaffolds against a control arm using plain ChatGPT and found no significant advantage on
domain knowledge, effort or elaboration-based strategy use. Gu & Yan (2025), 19 LLM-tutoring
studies, report *g* = 1.426 with teacher support and *g* = 0.077 without it, which puts most of
the measured effect outside the model. Tutor CoPilot, 900 tutors and 1,800 students,
moved its exit ticket and returned a null on the end-of-year test.

If you run one of the open problems, the result is wanted whichever way it lands. Especially the
nulls.

---

## How to verify it

This survey got things wrong. The record of that is the reason to trust the rest of it.

[`CORRECTIONS.md`](CORRECTIONS.md) is an append-only ledger with a provenance column.
**Adversarial reviewers found a substantial minority of its entries**, including the two most
damaging numbers, and one about the ledger itself, which was being silently edited inside a table
headed *"published rather than silently edited."*

The reviews are in [`evidence/`](evidence/). The first four returned **not publishable**.

Six machine checks guard the repository, and all six are runnable:

```bash
python3 evidence/check-corrections.py --self-test --strict   # no superseded value survives anywhere
python3 evidence/check-repetition.py                         # every restated finding is cross-referenced
python3 evidence/check-stance.py --strict                    # the discipline is the warrant behind the mission
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
reported as unverifiable instead of dropped.

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

If you cite this work, cite the report in [`research/raw/`](research/raw/). The report carries
the sources and the evidence labels; the survey summary carries neither.

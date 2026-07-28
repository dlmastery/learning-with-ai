# Learning in the New Frontier AI World

**A standard-setting survey of AI-native learning — from a five-year-old decoding words to a
doctoral student who knows more than the tutor does.**

📊 **[Dashboard](https://dlmastery.github.io/learning-with-ai/)** ·
🧪 **[Demo gallery](https://dlmastery.github.io/learning-with-ai/demos/)** ·
📖 **[The survey](survey/)** ·
🔬 **[Research reports](research/raw/)** ·
🧾 **[Requirements audit](AUDIT.md)**

---

## What this is

If learning were designed today — with frontier AI assumed rather than bolted onto a
nineteenth-century classroom — what would it look like?

This repository answers that with a survey built on **30 research reports, ~380,000 words, and
roughly 2,000 primary sources**. Every claim carries an evidence label. Every section carries at
least one documented null result. And **every one of our own errors is published rather than
quietly edited**.

It is not a literature review. A literature review tells you what has been said. This tells you
**what is actually established, what is overstated, what is measurably false, and what nobody has
tried** — then specifies the experiments that would settle the difference.

### Why it exists

The project began with a specific child. She is eleven, she is served under a
[SELPA](https://www.cde.ca.gov/sp/se/as/caselpas.asp) plan, and she can hold a conversation about
photosynthesis that would impress you and then fail a worksheet about photosynthesis. Designing for
her is not a charitable sidebar here. It is the organising constraint — a system that works at the
margin works everywhere, and a system that only works for the median works for nobody who needed it.

Then we ran the census. **Across ERIC and Europe PMC: 30 randomised trials of generative-AI tutoring
mention students. Zero mention disability, dyslexia, ADHD, autism, special education, or IEPs.**

Every effect size in the AI-tutoring conversation was measured on somebody else's child. That empty
chair is what this document is for.

---

## Start here

| If you are… | Read |
|---|---|
| **Skimming** | The [dashboard](https://dlmastery.github.io/learning-with-ai/) — headline numbers, the K-12→postgraduate matrix, the corrections ledger, the tough questions |
| **Building a product** | [`survey/01`](survey/01-central-finding.md) (the felt-learning trap) → [`survey/04`](survey/04-the-empty-chair.md) (what the evidence forces) → [`survey/08`](survey/08-nobody-needs-a-better-scheduler.md) (what not to build) |
| **A researcher** | [`research/raw/F9-open-problems.md`](research/raw/F9-open-problems.md) — 19 open problems, each with a runnable experiment, power justification, and pre-registered falsifier |
| **A parent or teacher** | [`survey/04`](survey/04-the-empty-chair.md) and [`survey/05`](survey/05-the-explanation-is-the-work.md) |
| **Sceptical** | [`evidence/review-2026-07-28.md`](evidence/review-2026-07-28.md) — a hostile external review of this repo, verdict **not yet** — and the corrections table below |

---

## The findings, in brief

### What is genuinely established

| Technique | Effect | Base |
|---|---|---|
| Retrieval practice | **g = 0.50** | 222 classroom studies · 48,478 students · **I² = 88%** |
| Spacing / distributed practice | **d = 0.54** | 2025 classroom meta-analysis, 31 effects, N > 3,000 |
| Human tutoring | **d = 0.79** | VanLehn. Pooled RCTs are lower: **0.288** |
| Intelligent tutoring systems | **d = 0.76** | Statistically indistinguishable from human |
| Best measured AI tutor | **d ≈ 0.63** | Kestin RCT — 49 min vs 60. Developer-built, developer-evaluated |
| Learning by teaching *with prior expectancy* | **g = 0.48** | Kobayashi 2024, k = 39 |
| Computer-based scaffolding | **ḡ = 0.46** | Belland, 144 studies |

### What is overstated, contested, or false

| Claim | Reality |
|---|---|
| Bloom's **2 sigma** | Does not replicate. Pooled tutoring RCTs land at **0.288** |
| **Learning styles** matching | No credible support in four decades — yet 89.1% of educators believe it |
| **Expanding** SRS intervals | **g = 0.032**, k = 54, **I² = 0%** — a clean, well-powered nothing |
| **Orton-Gillingham** | **g = 0.22, p = .40** against active comparison |
| Slides vs no slides | **g = 0.067**, CI [−0.103, 0.236] |
| "Now explain it back to me" | **g = −0.02** — the null condition, and how nearly every product ships it |
| Working-memory training | Does not transfer. Externalise memory instead |
| **UDL** as an intervention | A design philosophy. Its *components* are evidenced; the framework is not |
| AI-detection tools | **61.22%** false-positive on non-native writers vs 5.19% native |

### The three findings that change what you build

1. **Measurement without a decision rule is inert.** In a randomised trial, both arms revised
   instruction more often — *only the arm told **what to change** moved achievement.* Dashboards,
   streaks, mastery bars and adaptive difficulty are all the arm that measured more and moved
   nothing.

2. **Guardrails remove a harm; they have not been shown to add a benefit.** Unguarded AI left
   learners **17% worse** on later unassisted work. The guardrailed arm's unassisted coefficient was
   **−0.004, not significant**. Anyone selling restraint as a learning *gain* is ahead of the
   evidence — including an earlier draft of this repository.

3. **Felt learning and real learning move in opposite directions.** Preference moves at **d ≈ 0.48**
   while knowledge moves **zero**, and the effect survives explicit debiasing. Students in the
   condition that taught them *more* reported learning *less*. Every optimisation loop can measure
   satisfaction; almost none measure learning.

---

## Kindergarten to doctorate

The most common question this survey gets: does any of it apply the same way to a six-year-old and
a PhD student? **No — and the axis is not age.**

> **Expertise reversal.** The same instructional support measures **d = +0.505** for novices and
> **d = −0.428** for experts. Not "less useful" — *actively harmful*.

So the span is not a difficulty gradient. It is a **reversal**, and it runs **per topic**, not per
person: the same learner is a novice in one chapter and an expert in the next.

| | The tutor's actual job |
|---|---|
| **K–5** | Be the thing that cannot be argued with. Explicit, systematic, consistent. **Withholding does damage here** — this is where the Socratic instinct is wrong |
| **6–12** | Fade the scaffold on evidence, not schedule. The only band where the reversal happens, so per-topic prior-knowledge measurement becomes load-bearing |
| **Undergraduate** | Stop explaining, start interrogating. Guidance now costs more than it gives. Explanation becomes something the *learner* produces |
| **Postgraduate** | The learner knows more than the tutor. Its job inverts entirely — adversary, verifier, literature memory, connector. It must be **useful without being right** |

Full matrix of 12 techniques × 5 bands on the [dashboard](https://dlmastery.github.io/learning-with-ai/).

---

## The system this argues for

Not one tutor. A crew of seven, each narrow, each **certified against a published eval** — never
merely prompted to be an expert, since persona prompting shows no measured accuracy gain.

| Role | What it does |
|---|---|
| **Mentor** | The only conversational role. Withholds, asks, waits |
| **Diagnostician** | Watches for the misconception behind the wrong answer |
| **Simulator** | Builds the world the concept lives in — *executable*, so it can prove the learner wrong without anyone asserting it |
| **Adversary** | Genuine, **unannounced** objection. Announced devil's advocates measurably *backfire* |
| **Student** | The agent the learner teaches. It must be able to **stay wrong** |
| **Archivist** | The learner model. Local, inspectable, correctable, deletable |
| **Connector** | Brokers contact with *actual humans*. Never simulates friendship |

**No votes.** A precedence ladder where executable ground truth wins outright and dissent is
*recorded*, never averaged away. And the crew must be genuinely heterogeneous — three independent
benchmarks find multi-agent debate does **not** reliably beat plain self-consistency. Seven copies
of one model wearing hats is theatre.

---

## Repository layout

```
survey/            THE DELIVERABLE — the survey itself, one file per section
research/raw/      31 verbatim research reports — the source of truth, never deleted
evidence/          harnesses, verification notes, original measurements
docs/              GitHub Pages dashboard + demo gallery
apps/ambient/      agent-native reference application
artifacts/         supporting work (Hermes skills, infrastructure)
PRD.md             the research plan — 30 sections, editorial standard
CLAUDE.md          crash-survival ledger: requirements, corrections, resume procedure
AUDIT.md           requirements audit written against ourselves
```

**`research/raw/` is the source of truth.** Survey sections are drafted *from* those reports; a raw
report is never deleted, only superseded by a dated successor.

---

## The editorial standard

Every claim carries one of these labels, and the rules are not negotiable:

`MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`

1. A `VENDOR` claim may **never** be restated as a finding.
2. Every section must contain **at least one documented negative or null result**.
3. Unverifiable claims are reported as unverifiable — never laundered, never omitted.
4. **Effect sizes over adjectives.**
5. A subagent's characterisation of a source is a **lead, not a finding**. Any claim that a
   load-bearing number has been corrected or retracted is verified against the publisher record
   before a single sentence changes.
6. **Progress is reported in survey words, never in report count.** Research is the input; prose is
   the deliverable.

Charts are generated from a **declarative spec by a deterministic renderer** — never hand-positioned
— because our own research rates hand-written SVG Tier D. The colour palette is **computationally
validated** for colour-vision deficiency (protan ΔE 16.7 light / 18.3 dark), not eyeballed. The
accessible table view is generated from the same spec, so it cannot drift from the chart. Pages are
tested across mobile, tablet and desktop in both colour schemes before they ship.

---

## What we got wrong

Eleven corrections, each caught by our own research reading a primary source, each published rather
than silently edited. **This list is the reason to trust anything else here.**

| We said | Actually |
|---|---|
| Sierra Leone +0.258 SD, "strongest evidence in edtech history" | **Unadjusted +0.216, SE 0.137 — not significant.** Loads entirely on Grade 8; gaps widened |
| Guardrails teach | They **remove harm**. Unassisted coefficient −0.004, n.s. |
| Orton-Gillingham is decades-replicated | **g = 0.22, p = .40** |
| Expertise reversal d = 0.971 | Unverifiable. Components imply **≈0.93** |
| Concreteness fading has a pooled effect size | Fyfe 2014 is a **systematic review**. No pooled ES exists |
| Bloom's 2σ is the target | Does not replicate. **VanLehn 0.79 · Nickow 0.288** |
| g = 0.56 is the teachable-agent effect | It is **human** learning-by-teaching. The agent version is **untested** |
| AI tutoring widens gaps, full stop | A property of **untargeted delivery**. Across 8 targeted interventions, **none widened gaps** |
| The pāṭha protocol should beat self-consistency | Benchmarked and **falsified** — exactly at chance |
| Deixis is complete greenfield | Substrate exists (arXiv:2604.02893). The tutoring loop does not |
| Bastani's −17% carries a PNAS correction | That correction is an **author-affiliation erratum**. The finding stands |

---

## Open problems

[19 open problems](research/raw/F9-open-problems.md), each with a runnable experiment design, power
justification, and pre-registered falsifier. The three worth running first:

1. **The delayed, unassisted, novel-item outcome.** Seventeen of the nineteen experiments name it as
   their primary outcome, so it is the measurement precondition for everything else. ERIC returns
   **0 records** for `"retention test" AND "ChatGPT"`.
2. **Persistent state versus stateless.** The cleanest ablation in the field and the largest
   unmeasured engineering commitment — three arms differing *only* in what crosses the session
   boundary.
3. **Does the guardrail ever add benefit?** This survey's own thesis on trial.

And the [unknown unknowns](https://dlmastery.github.io/learning-with-ai/), including
**correlated pedagogical error at population scale**: a human teacher's blind spots are
idiosyncratic and average out across thirty teachers; a model's are systematic and identical for
every learner simultaneously. Nobody has studied what happens when ten million children are taught
the same subtle misconception on the same afternoon. There is no monitoring for it, and no name
for it.

---

## Status

| Artifact | State |
|---|---|
| **Survey** — the deliverable | 22 sections · ~56,500 words (target ~45,000 — exceeded) |
| **Research reports** — the input | 30 reports · ~380,000 words · complete |
| Sections written from reports in hand | 22 of 32 |
| Demo pages | Gallery + design system shipped; pages landing incrementally |
| Published corrections | 11 |

Built **incrementally** — one section at a time, committed as it lands. Never generated in one go.

---

## Contributing, citing, and reuse

This is an open research artifact. If you find an error, **open an issue with the primary source** —
corrections are the currency here, and every one gets published with attribution. If you run one of
the open problems, we want the result whichever way it lands, including the nulls. *Especially* the
nulls.

If you cite it, cite the report in `research/raw/` rather than the survey summary — the report
carries the sources and the labels.

---

<sub>Negative results are first-class. Corrections are published. Nobody's thumb, ever again.</sub>

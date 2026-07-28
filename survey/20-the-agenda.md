---
title: "The Agenda — three experiments, and what would falsify this survey"
section: agenda
status: draft
date: 2026-07-28
source_report: research/raw/F9-open-problems.md
---

# The Agenda

Two ERIC queries, run 2026-07-27:

| Query | Records |
|---|---|
| `"retention test" AND "ChatGPT"` | **0** |
| `"transfer test" AND "ChatGPT"` | **0** |

A third, `"artificial intelligence" AND "delayed posttest"`, returns seven, and
the recent entries are EFL vocabulary studies rather than conceptual transfer.

So: **no adequately powered trial of an LLM tutor has measured what a learner can
do, without the AI, on novel items, four or more weeks after the intervention
ended.** Every procurement decision, every scaling decision, every roadmap in
this field is currently made on assisted or immediate outcomes.

The one study that separated them found the sign flips. In a randomised trial of
roughly 1,000 students across ~50 classrooms, assisted practice performance rose
by **+48%** for an unguarded GPT assistant and **+127%** for a hint-only tutor.
On the closed-book exam with the AI removed, the unguarded arm was **−0.054
(SE 0.022), p < .05 — a 17% deficit relative to never having had access** — and
the guardrailed arm was **−0.004 (SE 0.013), not significant.**

That is the whole problem in one study. **A variable that moves an outcome from
−17% to zero is not near a ceiling; it is near a decision.** And nobody has
measured what happens six weeks later.

This section lists the three experiments worth running first, each with its
design and its pre-registered falsifier, and then states at full strength the
case that this survey is wrong.

---

## Experiment 1 — the delayed, unassisted, novel-item outcome

**Why first.** It is the measurement precondition for everything else.
Seventeen of the nineteen open problems in the underlying research name a
delayed unassisted transfer test as their primary outcome. If that instrument is
not built, validated, and shown to be administrable at scale, none of the rest
can be run credibly. It is also cheap: no novel system to build.

| | |
|---|---|
| **Population** | 900 students, grades 8–10, one school system with a stable roll, one curricular unit (e.g. linear functions) not revisited for a full term |
| **Arms** (individually randomised within class, 300 each) | **A** — guardrailed LLM tutor, hint-only · **B** — unguarded LLM assistant · **C** — matched-time supervised study with worked examples, no AI |
| **Power** | 300/arm detects d = 0.23 at 80%; with ANCOVA on a pre-test (r ≈ .6), **d ≈ 0.18**. At 25% attrition it still detects d = 0.21 |
| **Primary outcome** | **Unannounced, unassisted, closed-device test at 6 weeks**, on items never seen, from the same construct specification but a disjoint item family. Blind-scored |
| **Secondary** | Immediate assisted score; immediate unassisted score; procedural vs conceptual retention separately; and the **immediate-to-delayed rank correlation across arms** |

**Pre-registered prediction.** A > C at delay by 0.15–0.30 SD; B ≤ C at delay;
and **the arm ordering at six weeks differs from the arm ordering on the
immediate assisted test.**

That last clause is the finding that matters, because it invalidates the
measurement practice of the entire field rather than one product.

> **Falsifier.** If immediate assisted performance and 6-week unassisted
> performance rank the arms identically, with **r > .8** across a range of
> systems, then immediate measurement is a valid proxy, this problem dissolves,
> and the field's existing evidence base is worth far more than this survey
> credits it for.

The falsifier here is *good news for everyone else*. We should want to run it
precisely because it can rescue a decade of published effect sizes.

Why it has not been run is not an intellectual difficulty. A delayed unannounced
test costs learner goodwill, requires re-contacting a dispersed cohort, and
produces attrition that is almost certainly non-random — the students who show up
are the ones who learned. It is also commercially unattractive: it is the one
measurement that can turn a shipped product's headline number negative, and every
party positioned to fund it has an interest in the immediate number.

---

## Experiment 2 — persistent learner state against a stateless baseline

**Why second.** Memory is the headline feature of the current product
generation and the organising premise of every lifelong-learner-model
architecture, **including this survey's own**. It is being built at real schema
cost, real privacy exposure, and the entire regulatory surface described earlier
in this survey — on **zero** evidence that it changes a learning outcome. No
trial has compared a tutor that remembers a learner across sessions against the
identical tutor that does not.

The census is stark. arXiv `"open learner model"` → 0. `"long-term learner
model"` → 0. `abs:"long-term memory" AND abs:"tutor"` → 0. Six results for
memory + tutoring system + LLM, all system papers, **none containing a
memory-ablation arm.** GitHub `learner model knowledge tracing memory LLM tutor`
→ 0 repositories.

| | |
|---|---|
| **Population** | 600 learners, 12 sessions over 8 weeks, one multi-topic curriculum (introductory statistics — many interlocking prerequisites, high misconception density) |
| **Arms** (200 each) — identical model, prompt, and UI, **differing only in what crosses the session boundary** | **A** — stateless, no carryover · **B** — transcript carryover, prior session summaries in context (what most "memory" products actually are) · **C** — structured learner state: typed per-KC mastery, an explicit misconception register, channel constraints, and pivot history, inspectable and correctable by the learner |
| **Power** | 200/arm detects d = 0.28; with ANCOVA, **d ≈ 0.22**. This matters — the honest prior is *small*, and a study powered only for d = 0.5 produces an uninterpretable null |
| **Primary outcome** | **4-week unassisted transfer on items requiring a prerequisite established in an early session and applied in a late one** — the only place a memory effect can mechanistically appear |
| **Secondary** | Redundant re-explanations of mastered material; time-to-first-correct on prerequisite-dependent items; **learner corrections of the visible state**; and a pre-registered ablation of arm C into **C-typed vs C-untyped** |

**Pre-registered prediction.** C > B > A, with **C − A ≈ 0.25 SD on the
prerequisite-dependent subscale and ≈ 0 on the topic-local subscale.** The
*localisation* is the real prediction; a uniform gain would indicate a confound.

Two design details carry most of the value. The control must be
summary-carryover rather than a true amnesiac, or the comparison measures
politeness rather than memory. And the typed/untyped sub-ablation converts a null
into a **diagnosis** — because the deep obstacle is knowledge-component
alignment, and the numbers there are not encouraging: expert KC models add
**≤ 0.01 AUC on 7 of 9 datasets**, and on 4 of 9 the KC model is so poor that a
skill-only model loses to an item-difficulty-only model. **A memory whose
contents are badly typed may be worth exactly nothing.**

The case for memory also cannot be "better next-item prediction," because that
ceiling is reached: a zero-parameter moving average beats every released FSRS
version on log loss over 350 million reviews, and SAKT fails independent
replication on all nine datasets tested (0.85 reported → 0.73 observed). The case
has to be continuity, diagnosis and pivoting — none of which AUC measures and
none of which anyone has measured either.

> **Falsifier.** C = B = A on prerequisite-dependent transfer, with no advantage
> even on redundant-re-explanation counts, would mean persistent state is an
> engineering preference rather than a pedagogical mechanism — and given its
> privacy cost, **that finding should stop people building it.**

---

## Experiment 3 — does the guardrail that removes harm ever add benefit?

**Why third, and why it is this survey's own thesis on trial.** The central
design claim running through these sections is that **restraint is the active
ingredient**. The evidence for that claim is currently *entirely* about harm
removal. The guardrail took the unassisted effect from −17% to exactly zero. **No
study has ever shown a constrained tutor beating a no-AI control on a delayed
unassisted outcome.** Europe PMC, `"guardrails" AND "learning" AND "randomized"`:
**0 hits**. The one relevant trial has not been replicated.

| | |
|---|---|
| **Population** | 900 students, matched-time design, one curricular unit, single school system |
| **Arms** (300 each, **all receiving identical total instructional time**) | **A** — guardrailed AI tutor: hint-only, withholds solutions, requires a reasoning attempt before help · **B** — unguarded AI assistant · **C** — matched-time worked examples plus retrieval practice, no AI — *the best cheap thing we already know works* |
| **Power** | 300/arm detects d = 0.23; the decisive contrast is **A vs C**, with a pre-registered smallest effect of interest of **d = 0.20** |
| **Primary outcome** | 6-week unassisted novel-item transfer |
| **Secondary** | Help-seeking after AI removal; a **dependency probe** (does arm A attempt fewer unaided problems in a later, unrelated unit?); gap-widening by prior-knowledge quartile |

The matched-time constraint is the whole design. Almost every deployment trial in
the corpus adds the AI *on top of* normal instruction, which makes the AI arm
strictly advantaged and the resulting effect uninterpretable as evidence about
the AI.

**Pre-registered prediction.** A > C by 0.15–0.25 SD — the constrained system
beats the best cheap alternative, but modestly — and B < C. **Honest confidence
in A > C: about 55%.** That is precisely the confidence level at which an
experiment is worth running.

> **Falsifier.** **A ≈ C at adequate power is the result that should change this
> survey's posture most.** It would mean the guardrailed tutor's contribution is
> the *scalability of a known-good intervention*, not a new mechanism — still
> valuable, and a completely different claim, which should then be stated in
> those words.

---

## What would falsify this survey

This survey argues that the measured **0.2–0.4 SD** band for LLM tutoring is the
floor with the brakes on — that constrained, grounded, pivoting, remembering
systems would do better, and that nobody has built the good version and measured
it. Here is the strongest case against that, stated properly rather than as a
strawman. Anyone who cannot state it in this form has not earned the right to the
survey's conclusion.

**Premise 1 — 0.2–0.4 SD is not a floor. It is the modal result of educational
intervention research, full stop.** It is where tutoring lands, where formative
assessment lands, where feedback lands, and where most well-implemented
instructional technology lands once the trial is adequately powered and
independently run. The regularity is not a fact about AI. It is a fact about how
much of the variance in learning outcomes is available to be moved by *any*
instructional manipulation given fixed time, prior knowledge and motivation.
**On this reading, the survey has mistaken a population parameter for a
technology limitation.**

**Premise 2 — the nulls already on record are the honest prior, and they are the
most rigorous studies in their respective literatures.**

| Result | Effect |
|---|---|
| Orton-Gillingham vs comparison instruction | **g = 0.22, p = .40**; g = 0.14, p = .59 |
| Expanding retrieval intervals | **g = 0.034, n.s.** |
| Lesson Study (EEF) | **ES 0.02 [−0.06, 0.09], p = .65**; n = 6,437; 181 schools; **very high** security; null in every subject and subgroup; no dose–response; good fidelity |
| Multimedia pedagogical agents | **g = 0.20** |
| Ruffle&Riley (LLM learning-by-teaching) | **null twice**, N = 100 and N = 200, with high subjective ratings and users needing *more* time |
| Lehmann et al. | **no main effect**, two preregistered experiments — plus gap-widening |
| RTI at federal scale | **negative** Grade-1 impacts, regression discontinuity |
| Working-memory training | **no transfer** |
| UDL | outcomes **not demonstrated** |

**Premise 3 — added mechanism adds load, and the load is real while the benefit
is speculative.** This is the sharpest version, and **this survey's own evidence
supplies it.** Multiple concrete representations *harmed* symbol learning, with
the harm attributable to multiplicity. Five ladder rungs did not beat three
(Mdiff = 0.16 [−0.78, 1.09], p = .738). Persistent decorative detail carries
**g = 0.43 of harm**. Mixing models *reduced* ensemble quality — a single-model
Mixture-of-Agents beat the mixed version by 6.6%. Debate does not reliably beat
self-consistency. Declaring dependencies made notebook reproduction *worse*.
**Every one of those is a case where the elaborated version lost to the plain
one**, and "a village of agents with persistent state, deixis, laddering,
error-holding tutees and a pivot engine" is the most elaborate system anyone has
proposed. The base rate for elaboration in this literature is not good.

**Premise 4 — the mechanism the survey most relies on has a moderator that dwarfs
it.** AI tutoring **with teacher support: g = 1.426. Without teacher support:
g = 0.077** — approximately null. If the human is doing the work, every
architectural refinement is optimising the small term.

**Premise 5 — the field's positive results degrade under scrutiny in one
direction only.** Sierra Leone's unadjusted estimate (**+0.216 SD, SE 0.137**) is
not significant. The largest positive LLM-tutoring meta-analysis (g = 0.867) was
**retracted in 2026**. One prominent tutor was built and analysed by its first
author with no funding statement. One trial has 11 clusters. Another lost 43% of
its sample. **Where independence and rigour increase, effects shrink. That is the
signature of a literature whose true effect is smaller than its published mean.**

### What the survey says back — as reasons to test, not refutations

**One: the nulls are mostly about branding, not mechanism.** Orton-Gillingham
nulls while its active ingredient — explicit systematic decoding instruction —
carries d = 0.41 to 0.55. Expanding intervals null while *scheduling retrieval at
all* carries classroom d = 0.54, with only 12 of 271 massed-versus-spaced
comparisons failing. Lesson Study nulls as a *process* while content-bearing
interventions do not. The pattern is that **the wrapper fails and the mechanism
holds**, and this survey's programme is explicitly mechanism-level.

**Two: the dissociation results are sign results, not ceiling results.** A
ceiling story predicts small positive effects everywhere. It does not predict
−17%, and it does not predict the same model with a different interaction policy
landing at zero in the same study.

**Three: the empty chair.** Zero randomised trials of AI tutoring on learners
with disabilities is not a verdict. The ceiling argument cannot even be assessed
for the population where prior-knowledge, dosage and fidelity constraints bind
hardest — which is exactly where the mechanism-level case is strongest.

---

## The concession conditions, stated in advance

We would concede that 0.2–0.4 SD is a real ceiling rather than a floor, and that
added mechanism does not pay, if:

1. **Experiment 3 returns A ≈ C** at n = 300/arm. The single most decisive test:
   the flagship design against the best cheap known-good alternative on our own
   preferred outcome.
2. **Experiment 2 returns C = B = A** on prerequisite-dependent transfer *and*
   the typed-vs-untyped ablation shows no difference — persistent state buys
   nothing even when correctly typed.
3. **The village-vs-single-agent comparison returns parity at matched compute** —
   architectural elaboration is compute in a costume.
4. **A teachable agent that can genuinely stay wrong returns parity with one that
   cannot**, despite a clean separation in belief persistence — the most
   distinctive mechanism in the design is inert.
5. **Any two of deixis, pivot latency, and laddering return flat.** Those are the
   three "add a mechanism" bets; two of three null puts the elaboration thesis in
   serious trouble regardless of the others.
6. **A well-powered, independent, preregistered trial of a system implementing
   several of these mechanisms together lands inside 0.2–0.4 SD** on a delayed
   unassisted outcome. This is the cleanest trigger and the one we should most
   want run, because it tests the conjunction rather than the parts.

**If (1) and (6) both land, the correct revision is not a hedge.** It is to
rewrite the thesis as: *AI's contribution to learning is the scalable,
high-fidelity, high-dosage delivery of interventions we already knew worked, and
the design space of novel mechanisms is a distraction.*

That would still be an important and actionable finding. It would redirect the
field toward fidelity and dosage — which is precisely what the section on
designing for the margin already argues for special education, where the
known-good intervention base is two orders of magnitude larger than the AI base.
**We say this now, in advance, so that conceding costs us nothing but a
hypothesis.**

---

## What this section commits us to

- **Run the outcome instrument first.** Delayed, unassisted, novel-item,
  blind-scored. Report the immediate-to-delayed rank correlation as a headline
  number, because it tells everyone whether their existing evidence base means
  anything.
- **Ablate memory before building more of it.** Same model, same prompt, same
  UI, differing only in what crosses the session boundary — and split typed from
  untyped so a null is a diagnosis.
- **Put restraint on trial against worked examples plus retrieval practice, at
  matched time.** Not against business as usual. Pre-register d = 0.20 as the
  smallest effect worth claiming.
- **Report gap-widening by prior-knowledge quartile as a pre-registered
  moderator on every trial**, because the sign of the effect depends on the
  learner.
- **Publish the falsifier before the result.** Each of the three experiments
  above has one written down, and none of them is a formality.
- **Three of these are runnable inside one instrumented product** with a few
  hundred consented users and no new modelling work — the memory ablation, the
  gap-widening moderator, and the permutation-vs-self-consistency check, which
  needs no learners at all. A shared delayed-assessment panel is the
  infrastructure that makes the rest reportable.

The measurement gap is the widest one in applied AI: dozens of benchmarks for
whether a model is smart, roughly one field trial per organisation per year for
whether it teaches. **Anyone building in this space is building without a ruler.**
The correct posture is not to wait for the benchmark. It is to build the ruler,
publish the falsifier alongside the design, and be the kind of project that would
notice if it were wrong.

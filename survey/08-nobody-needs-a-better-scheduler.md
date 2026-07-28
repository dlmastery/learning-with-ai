---
title: "Nobody Needs a Better Scheduler — the science of durable remembering"
section: remembering
status: draft
date: 2026-07-27
source_report: research/raw/F11-scientific-remembering.md
---

# Nobody Needs a Better Scheduler

Spaced repetition is the most beloved technique in self-directed learning, and the
part of it everyone optimises is the part that does not matter.

That is a strong claim. It rests on 126 sources, 68 registered null results, and a
350-million-review benchmark that the algorithm's own authors publish.

---

## 1. What is real, and it is very real

Start with what survives, because it is the foundation of everything else in this
survey:

| Practice | Effect | Base |
|---|---|---|
| **Retrieval practice** | **g = 0.499** [0.442, 0.557] (§24)| 222 classroom studies, 48,478 students — **I² = 88%** |
| **Spacing / distributed practice** | **d = 0.54** [0.31, 0.77] | 22 reports, 31 effects, N > 3,000 (classroom meta-analysis, 2025). Cepeda et al. 2006 is the canonical lab meta-analysis |

These are among the largest, most replicated effects in all of learning science.
Testing yourself beats re-reading. Spreading practice out beats massing it.

They are also **heterogeneous**, and honesty requires saying so in the same breath:
retrieval practice carries **I² = 88%**, moderated by the control condition, test-format
consistency, feedback, and number of repetitions. Two boundary conditions matter for
design. At an *immediate* test, restudy often wins — the retrieval advantage appears at
delay. And **unsuccessful retrieval without corrective feedback yields little or
nothing**, which makes feedback part of the intervention rather than an add-on. Spacing
is not scale-free either: **d = 0.11–0.42** for motor tasks, much larger for simple
verbal material.

None of that weakens the recommendation. If a system does nothing else, it should do
these two things, and do them relentlessly — with feedback attached and the test
delayed.

Nothing that follows weakens either finding. What follows is about a **third**
claim that has been quietly bundled with them — that the *scheduling algorithm*
deciding when to show you a card is where the sophistication lives.

---

## 2. The scheduler does not survive

The modern spaced-repetition ecosystem is organised around ever-better interval
predictors: SM-2, then FSRS-4, -5, -6, now -7. Each release is announced with
improved fit on a review-log benchmark.

On that benchmark — **350 million reviews** — three results sit together:

1. A **zero-parameter moving average beats every FSRS version on log loss.**
2. A **34-feature logistic regression beats FSRS-6 and FSRS-7 on all three
   metrics.**
3. The FSRS team themselves published **`RMSE-BINS-EXPLOIT`**, a deliberate
   demonstration that the headline metric can be won by a model with a log loss of
   **4.6** — i.e. the reported scoreboard is gameable, and they said so.

Credit where it is due: publishing your own metric's exploit is better science
than most of this field manages.

But note what these benchmarks are. They are **backtests on logs of what learners
already did.** Predicting whether a review will be recalled is not the same
quantity as causing more to be remembered. A backtest is not an intervention, and
the scheduling literature has almost no interventional evidence at all.

---

## 3. Expanding intervals: verified null, and the mechanism recovered

The single most-repeated claim in spaced repetition is that intervals should
*expand* — review at 1 day, then 3, then 7, then 21 — because retrieving at the
edge of forgetting is desirably difficult.

**g = 0.032, 95% CI [−0.10, 0.17], k = 54, I² = 0%**, no publication-bias
asymmetry. Zero heterogeneity across fifty-four experiments is not a murky
literature. It is a clean, well-powered nothing.

This confirms an earlier finding in this project against independent sources, and
it would be a dead end except that the primary studies contain something better
than the null.

Karpicke and Roediger's Experiment 3 dissociates the two things that were
confounded:

> **Delaying the *first* retrieval helped, regardless of how the repeated tests
> were spaced.** ηp² = .19 for the delay of the initial test; the schedule effect
> was F < 1.

The gain everyone attributed to the expanding *schedule* was coming from **when
the first test happened**. Expanding schedules delay the first test by
construction, so they inherited credit for it.

And the theoretical premise fails in the data too: response latencies **fall**
across expanding repetitions. The retrievals were not getting harder. The
desirable-difficulty story for expanding intervals is not what the timings show.

Dobson (2012, n = 250, 29 days) is the honest counterexample and is reported in
full rather than omitted.

---

## 4. The boundary of the entire paradigm

This is the most important table in the section, and it should govern what anyone
builds:

| What was scheduled | Trials significant |
|---|---|
| Paired associates / flashcard-type material | **11 of 14** |
| **Interdependent content** — where one idea depends on another | **0 of 8** |

**And the headline this table omitted, which an earlier draft should not have.** Across
the review's full set of **41 studies from 34 papers**, the authors write: *"We find
that over half of the studies found that RL-induced policies significantly outperform
baselines."* **21 of 41 (51%) significantly beat all baselines**; 10 found no
significant difference; 1 where the baseline won. Publishing the 0-of-8 sub-cut
without the 21-of-41 headline is selective reporting, and it is the exact failure this
survey exists to name. The domain split above is real and it sits inside a review whose
overall verdict is **positive**.

The authors' own qualifier is the load-bearing part: RL *"has been most successful in
cases where it has been **constrained with ideas and theories from cognitive
psychology and the learning sciences**."* Which is an argument for the architecture in
this document rather than against it.

Adaptive scheduling works on material with no internal structure and has **never**
worked on material with structure. Every trial that tried failed.

Supporting evidence points the same way. Duolingo's half-life regression, tested
against plain Leitner boxes on roughly **one million students**, produced **+0.3%
engagement (not significant)** and **−7.3% practice (significant)** — the adaptive
scheduler made people practise *less*. The famous "+12%" figure comes from a
different experiment and does not describe this comparison. Kerfoot's adaptive
trial: p = 0.37. Cen 2007: p = 0.772 on posttest, p = 0.602 on retention, with 12%
time saved. Mettler's adaptive system was beaten on raw accuracy by a **random**
schedule (d = 0.746).

And knowledge tracing, the sophisticated cousin, does not rescue it. Roughly
**82% of deep knowledge tracing's founding gain was an evaluation-procedure
artefact plus a forgetting term**; an **untrained LSTM is within 0.03 AUC** of the
trained one; and an oracle that *knows the exact moment learning occurred* beats
simple logistic PFA by **0.002**.

That last number deserves a moment. If perfect knowledge of the thing these models
are trying to infer is worth two thousandths of AUC, the modelling target is
nearly exhausted. The remaining headroom is not in the model.

---

## 5. The named product, assessed fairly

This section was commissioned partly to evaluate **zemomemo.com**. It is a free
SvelteKit flashcard application built on FSRS-6, with five study modes, LLM deck
generation, and Quizlet and Anki import. It is competent, and it is free, and
people plainly find it useful.

It cites **no study, trial, or efficacy datum**; its only external reference is the
FSRS community wiki. Four observations place it precisely:

- Its **"stickiness — the number of days a flashcard will stay in your brain"** is
  FSRS's *stability* parameter — the interval at which recall probability falls to
  90% — rendered to the user as a deterministic expiry date. A probabilistic
  quantity presented as a certainty.
- **"Achieve mastery same day"** together with **"remember forever"** straddles a
  combination that Cepeda's 271 massed-versus-spaced comparisons do not support
  (12 exceptions).
- The **same-day regime it markets hardest is the regime FSRS's own benchmark
  excludes** from its headline table — and where FSRS-6 performs worst.
- **FSRS-6 is a version behind FSRS-7.**

None of this makes it a bad product. It makes it a product, and the distinction
this survey exists to hold is between a competent tool and a scientific claim.

---

## 6. What actually becomes buildable

Here is where this gets interesting, because the null results above clear space
rather than closing it. Every capability below is currently at `DEMO` or
confounded-`OBSERVED` — **nobody has run the trial** — and each is now cheap.

**Generate the cue instead of storing it.** A flashcard is a frozen question,
which is why the paradigm only works on unstructured material: the card *is* the
atom. If the question is generated at retrieval time from the concept, then the
same knowledge can be probed from a different angle every time, and recognition of
the card can no longer be mistaken for knowledge of the thing.

**Schedule concepts, not cards.** This is the direct attack on the 0-of-8 result.
Structured material failed under card scheduling because scheduling operated on
the wrong object. Schedule the *concept*, with its prerequisites, and derive the
probe.

**Separate recognition strength from generative competence.** These are different
memories and current systems conflate them. A learner who recognises the answer
instantly and cannot produce it unprompted has one and not the other — and only
the second is what anyone means by knowing.

**Detect inert knowledge.** Retrievable when cued in the original context, and
never spontaneously deployed when relevant. This is the failure mode that most
frustrates teachers, it is invisible to every scheduler in existence, and it is
detectable by a system that watches a learner work rather than only quizzing them.

---

## 7. The subsystem, specified

Concretely, and falsifiably:

- **Three tables, and none of them is a card table.** Concepts, retrieval events,
  and generator state. The card was always a cache of a question, and caching the
  question is what welded the system to unstructured material.
- **Gaps derived from a stated retention horizon**, not from an interval ladder.
  "Still solid in June" is the requirement; the schedule is the consequence.
- **Three generator gates enforcing that difficulty be *semantic*.** This one has
  a number behind it: Bertsch's anagram condition — difficulty that is merely
  perceptual rather than conceptual — is **d = −0.05**. Making the *reading* harder
  is not a desirable difficulty. Making the *retrieval* harder is.

And the cheapest experiment in the document, which follows directly from §3:

> **Push the first retrieval later.** One parameter, a meta-analytic prior, and a
> mechanism dissociated in an existing experiment. If the effect is where
> Karpicke and Roediger's Experiment 3 says it is, this is nearly free.

---

## 8. What this section commits us to

- **Do the practices; stop tuning the scheduler.** Retrieval (g ≈ 0.50) and
  spacing (d ≈ 0.54) are the product. The interval predictor is a rounding error
  wearing a lab coat.
- **Never claim an expanding schedule teaches.** g = 0.032, I² = 0%. Delay the
  first retrieval instead.
- **Do not schedule structured material as cards.** 0 of 8. Schedule concepts and
  generate the probe.
- **Report backtests as backtests.** Log-loss on review history is not a learning
  outcome, and a zero-parameter baseline beating your model is a result about your
  model.
- **Difficulty must be semantic.** d = −0.05 for the alternative.

The pattern here is the one this survey keeps finding from different directions.
The sophisticated-looking component — the scheduler, the deck, the avatar, the
debate among agents — turns out to carry almost none of the effect. What carries
it is something simpler and harder: **that the learner actually retrieved, actually
struggled, actually explained, and actually got told when they were wrong.**

The machinery is worth building. It is just not worth mistaking for the mechanism.

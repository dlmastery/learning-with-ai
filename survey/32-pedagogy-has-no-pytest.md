---
title: "Pedagogy Has No Pytest — what an agent is, and the one thing it is missing"
section: agentic
status: draft
date: 2026-07-28
source_report: research/raw/K2-agentic-frontier.md
---

# Pedagogy Has No Pytest

The complaint that prompts this section is a good one: given agentic AI, why is
everything in this survey so modest? Agents write software, run experiments, and
operate for hours unattended. Why does the tutoring chapter read like 2019?

The answer turns out to be a single sentence, and once you have it the entire
reliability landscape of agentic AI resolves into one line.

---

## 1. What an agent actually is

Strip the marketing and an agent differs from a chatbot in exactly four ways:

| | |
|---|---|
| **Sampling** | It can try many times instead of once |
| **Execution** | It can run things and see what happened |
| **Persistence** | It can carry state across a boundary a conversation does not survive |
| **Absence** | It can work while nobody is watching |

Every one of those is a multiplier on something else. None of them produces value on
its own. Which yields the rule:

> **The value of an agentic loop is bounded by the value of the external check it
> closes on.**

Sampling without a selector is noise. Execution without a test is output. Persistence
without a schema is a transcript. Absence without a verifier is unsupervised drift.

---

## 2. The rule explains the entire reliability gradient

Look at where agents work and where they do not, and it is not about difficulty:

| Benchmark | Score | Is there a check? |
|---|---|---|
| SWE-bench Verified | **79.2%** (396/500) | Yes — `pytest` |
| Terminal-Bench 2.1 | **83.8%** | Yes — the command either works |
| PaperBench | **21.0%** | No |
| SciCode | **4.6%** | Weakly — hand-written tests |

A twenty-fold spread, and the axis is not how hard the task is. It is **how good the
check is**. Note that SciCode is not check-free — it has hand-written tests — and
still lands at 4.6%, which is why the rule is stated as a *bound* rather than an
equality. A weak check bounds you low. A strong one does not guarantee you reach the
bound; it only stops you being capped below it.

**Coding agents work because `pytest` exists.**

Now place teaching on that table. It sits firmly in the second column, and the reason
is measured rather than asserted:

> Across **223 tutoring domains, no model beat chance at labelling an incorrect
> student action.**

**Scoped correctly, because an earlier draft was not.** TutorGym evaluated four
models — `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`,
`gpt-4o-2024-08-06`, `deepseek-v2.5` — in what its authors call an *initial
evaluation*. That model set never appeared in this survey, and the result was
restated here as *"currently unverifiable"* and *"every architecture"*, which is
more than it supports.

**And the adjacent positive literature was never searched.** ProcessBench
(arXiv:2412.06559) asks models to *"identify the earliest step that contains an
error"* in mathematical reasoning, and reports open models with critique capability
**competitive with that same GPT-4o vintage**. A shared task on mistake
identification reports macro-F1 in the low seventies across 50+ teams.

So the honest claim is narrower and more useful. **Step-error identification in a
model's own reasoning trace is not at chance. Diagnosing what a *learner* believes
from what they did is** — and the distance between those two is exactly the gap this
section is about. Not a wall; a specific unbuilt instrument.

Not "performed poorly." **Chance** — on that model set, on that benchmark. The
operation a tutor performs constantly — look at what a learner did and say what is wrong with it — is currently
unverifiable by the systems being sold to do it.

That is why this survey reads modest. It is not a failure of ambition. **Pedagogy has
no `pytest`, and every agentic capability is waiting on one.**

---

## 3. The field is optimising against two instruments that do not work

This is the section's most damaging finding and it is structural.

The leading agentic-education systems — DeepTutor, CogEvo-Edu, AgentSchool — are
**optimised against LLM-simulated students** and **scored by LLM-as-judge**.

Both instruments are measured, and both fail:

- Across seven models, simulated students show **near-zero misconception
  faithfulness**. They do not hold the belief they are role-playing.
- Selection by LLM judge measures **−3.20pp**. Selection by test measures **+8.14pp**.
  An eleven-point spread, in the wrong direction for the judge.

> **The field is tuning tutors against a student model that holds no beliefs, using a
> judge that is worse than not selecting at all.**

Fix nothing else and fix this, and the measured quality of everything downstream moves.

---

## 4. What is genuinely, measurably possible right now

The pessimism above is about one missing component, not about capability. Where a
check exists, the numbers are startling.

Sampling is a real multiplier. Coverage scales log-linearly across **four orders
of magnitude** of samples — and a *weak* model at 250 samples beat a *strong* model at
1: **56% against 43%.** Compute spent on breadth substitutes for model quality,
provided you can select.

Structured disagreement makes non-experts better judges. Debate raised non-expert
human accuracy from **60% to 88%.** Note what this is not: it is not agents agreeing
with each other more efficiently. It is a human adjudicating a genuine disagreement
and getting the right answer.

Literature synthesis is solved well enough to rely on. PaperQA2 matches or exceeds
subject-matter experts, with **70% of flagged contradictions validated.** The "find me
the three papers that resolve my confusion" capability is real today.

**Explanatory animation renders at 93.8%.** The visual half of §17's argument has a
working pipeline.

**And the horizon is doubling every ~129 days** — the length of task an agent can
complete unattended. Whatever the reliable autonomous unit is when you read this, it
is roughly twice that four months later.

---

## 5. Two priors this survey had wrong

**Doroudi et al. (2019) is not a negative review.** An earlier draft cited its
0-of-8 sub-cut on interdependent content and omitted the headline: **21 of 41 studies
(51%) significantly beat all baselines.** The authors' verbatim conclusion is *"over
half of the studies found that RL-induced policies significantly outperform
baselines."* And their qualifier is an argument *for* this document's architecture:
RL *"has been most successful in cases where it has been constrained with ideas and
theories from cognitive psychology and the learning sciences."* Corrected in §08 and
§22; logged as C-29.

The "Google rots your memory" result has failed replication twice (BF01 = 5.07).
It is one of the most-cited claims in every argument about AI and cognition, and it is
not standing.

---

## 6. The absence that is worth more than any capability

Two literatures exist. They have never met.

Self-improvement optimisers — GEPA, DGM, AlphaEvolve — have spent three years
getting very good at optimising a system against a fitness signal. Their fitness
signal has been benchmark accuracy, every time.

Instructional-policy research closed the loop on real human retention with 2014
machinery, and got **+16.5% semester retention** in a middle-school course.

Six arXiv queries and ten ERIC queries confirm it: **zero optimiser-in-the-loop trials
on human learners.** Nobody has ever pointed a modern optimiser at a fitness function
made of delayed unassisted human retention.

That is not a hard research problem. It is two fields that do not read each other, and
it is the largest unclaimed prize in this document.

---

## 7. The five things worth building, in order

**1 · A tutee that will not fold.** A misconception-faithful student model, certified
by a Selective-Flip-Score eval — does it hold the wrong belief under pressure and
abandon it only on genuine disconfirmation? This unlocks learning-by-teaching, and its
*downstream accuracy* is the grounded selector everything else is missing. It is both
the highest-evidence technique and the missing instrument, which is why it is first.

**2 · Generate-and-select on the learner's own test, never on a judge.** The
eleven-point spread is already measured. The scaled version — an optimiser whose
fitness is human retention at delay — is §6's unclaimed prize.

**3 · A step-level verifier for student work.** Pedagogy's missing `pytest`. Currently
at chance, with a public testbed and decades of labelled intelligent-tutoring logs
already sitting there. Whoever builds this unblocks the other four.

**4 · An agent whose only job is enforcing the boring floor.** Retrieval, spacing,
expectancy-before-study, feedback attached to failed retrieval, delayed unassisted
testing. It composes the six largest effects in this survey, requires **no new
capability at all**, and is by some distance the most likely of the five to work.

**5 · Four different arbiters, not four personas.** Heterogeneity of *evidence* — a
symbolic checker, a numeric checker, a corpus, a human — rather than heterogeneity of
prompt. And the disagreement between them surfaced to the learner *as the lesson*,
which is the one use of multi-agent structure the evidence supports.

Note the ordering. **The least sophisticated item on that list is the one most likely
to work**, and the most sophisticated is the one that unblocks the rest.

---

## 8. What this section commits us to

- **Never ship an agentic loop without naming its external check.** If you cannot say
  what plays the role of `pytest`, you have built a chatbot with extra steps.
- **Never optimise against a simulated student.** Near-zero misconception faithfulness
  across seven models. It holds no beliefs to diagnose.
- **Never select by LLM judge.** −3.20pp against +8.14pp. Worse than not selecting.
- **Spend compute on breadth, then select on a test.** A weak model at 250 samples beat
  a strong model at one.
- **Build the verifier first.** It is the bottleneck for every other capability here,
  and the training data already exists.
- **Ship the boring floor while you wait.** It needs no capability that does not exist
  and it composes the largest effects in this survey.

The honest summary of agentic AI in education, as of now: **the sampling is
extraordinary, the execution is extraordinary, the persistence is a solved engineering
problem, and the thing that decides whether any of it teaches anybody anything has not
been built.**

It is one component. It is buildable. Nobody has built it.

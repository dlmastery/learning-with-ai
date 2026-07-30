---
title: "The Explanation Is the Work — generative slides, and the learner as explainer"
section: explanation
status: draft
date: 2026-07-27
source_report: research/raw/C3-slides-and-presentations.md
---

# The Explanation Is the Work

Two requests sit behind this section, and they look like one thing. *Generate
slides on the fly.* *Have the learner explain the topic, give a presentation —
because the best way to learn is to teach.*

They are not one thing. One is about how a machine should show a concept. The
other is about what happens inside a person who has to produce one. The evidence
sends them in opposite directions, and the second finding is going to be
uncomfortable.

---

## Part A — Slides

### 1. The deck is worth nothing

The only meta-analysis that asks whether presentation slides beat chalk-and-talk
finds **g = 0.067, 95% CI [−0.103, 0.236], k = 48.** The interval contains zero.
Whatever value slides have, it is not in *being slides*.

This is the correct starting point because it kills the obvious product. "The AI
generates a deck for any topic" is a feature with a measured effect of
approximately nothing. The field has not noticed: an exhaustive arXiv census of
`"slide generation"` returns **39 papers, roughly 35 on-topic, and zero that
measure whether a human learns anything.** The metrics in use are LLM and VLM
judges, human preference ratings, ROUGE similarity to the author's original deck,
and aesthetics. Not one paper reports an accessibility metric of any kind.

That is the same hole this survey found in animation and in figure generation. A
generation literature has grown up measuring resemblance to an artifact rather
than effect on a mind.

### 2. What *is* worth something

The multimedia design principles, individually, carry real effects — **contiguity
reaches g = 0.74.** So the value is not in producing the deck. It is in
**enforcing the principles the deck must satisfy**, on every deck, without
exception, which is precisely the thing a human author cannot reliably do at 2 a.m.
and a deterministic checker can do every time.

That converts slide generation into the same problem as figure generation, and the
same answer applies. The model does not draw. **The model emits a declarative
specification; a deterministic renderer draws it; a gate checks the specification
before it renders.** Twenty gate predicates, seventeen of them hard-fail.

The tiering follows from what can be checked:

| Tier | Target | Why |
|---|---|---|
| **A** | **Marp**, **Quarto** | Maximally constrained; Quarto takes one source to revealjs/beamer/pptx with executable cells and native citations |
| **B** | Templated HTML with a validated layout grammar | Checkable, but the grammar must be closed |
| **D — prohibited** | Model-authored raster, hand-written SVG, model-computed coordinates | Unverifiable at any useful cost |

An independent result confirms the direction: *"programmatic methods produce
higher-quality slides."*

### 3. The principle everyone cites and nobody states correctly

The redundancy effect — that putting the narration on the slide as text *harms*
learning — is the most-violated principle in AI-generated decks and the most
frequently misstated.

The pooled estimate is **g = 0.15**, and it is **direction-dependent**:

- Adding text to existing audio: **g = 0.29**
- Adding audio to existing text: **g = −0.04, not significant**

And it goes null or reverses under identifiable conditions, including a documented
double reversal of *both* redundancy and modality for second-language learners.

So the rule is not "never put text on the slide." The rule is a **conditional
switch**, evaluated per learner, on language status, pacing control, reading
support, and hearing access — with hard exemptions for formulae, code, and
numerals, which are never redundant with speech.

Here is the part that matters. **A lecturer cannot evaluate that switch. A
generator can, at runtime, per learner.** That is the actual case for generative
slides, and it is a much better case than "decks on demand": not faster
production, but *per-learner compliance with a principle whose correct setting
varies by learner*.

### 4. The real use: a figure that answers a misconception

Which reframes the whole feature. The interesting artifact is not a deck prepared
in advance. It is **one visual, generated in response to a specific misconception
detected in the last thirty seconds**, satisfying the gate, rendered
deterministically, and thrown away afterwards.

Nobody makes that by hand, because it is uneconomical to make a bespoke figure for
one confusion in one head. That constraint is the one that lifts.

---

## Part B — The learner as explainer

### 5. First, the numbers were misattributed — including by us

This survey has repeatedly cited **g = 0.56** as the effect size for *teachable
agents*. That is wrong, and the correction matters because it changes what is and
is not evidenced:

- **g = 0.56** is **human** learning-by-teaching, with a human tutee (Kobayashi
  2019).
- **g = 0.43** is **peer tutoring's effect on the tutor's own achievement**
  (Leung 2018, k = 16).
- The self-explanation pooled estimate is **g = 0.55** (Bisra et al.), not 0.56.

The teachable-agent version — an artificial protégé — does **not** have a
meta-analytic effect size of 0.56 behind it. It has a strong human analogue and an
untested machine implementation. That distinction is the difference between a
finding and a hope, and this document has been blurring it.

### 6. The result that kills the obvious design

**Kobayashi 2024, k = 39:**

| Condition | Effect |
|---|---|
| Teaching after study, **with a prior expectancy to teach** | **g = 0.48** [0.34, 0.63] |
| Teaching after study, **without** a prior expectancy | **g = −0.02** [−0.14, 0.11] |

Delivery still adds **g = 0.38** on top of expectancy alone. So the answer to
"does preparation suffice, or is delivery required?" is neither of the offered
options: **expectancy-framed preparation is a precondition, and delivery
consolidates it.**

Now read the null condition again. *Teaching after study, without a prior
expectancy* — that is **"now explain it back to me,"** asked at the end.

It is the single most common implementation of learning-by-teaching in every
tutoring product on the market, and its measured effect is **−0.02.**

The fix is free. It is the *ordering* of one sentence. Tell the learner **before
they study** that they will be teaching this, and the same downstream activity
moves from zero to nearly half a standard deviation. This is the cheapest
falsifiable claim in the entire survey: a one-line prompt change with a
meta-analytic prior attached.

### 7. The audience is a net cost

This is the finding that inverts the request.

Wang, Cheng & Mayer (2023) compared teaching to a camera, to one student,
and to seven. Teaching to the camera won on transfer — with **lower social
presence, lower pulse rate, lower anxiety, lower cognitive load, and *more* idea
units produced**, mediated by exactly those paths. The audience consumed capacity
that would otherwise have gone into explaining.

Supporting results: written teaching scripts equal spoken teaching at one week,
and written-versus-spoken mode is a null moderator in the meta-analysis.

So "give a presentation to the class" is not the high-value version of this
technique. It is the version with an anxiety tax attached, and the tax buys
nothing.

For a learner with attention differences, anxiety, or speech and language needs —
the learners in §4 — this is decisive:

> **"Give a presentation" is a barrier that buys nothing. Letting the learner
> explain to a camera, or in writing, is not an accommodation. It is the
> higher-scoring design, for everyone.**

That is the curb cut again, and this time the evidence for it is direct rather
than inferred.

### 8. The gap nobody has looked into

No study compares an AI audience to a human audience. Four independent search
routes came up empty.

That absence defines this section's central hypothesis, and it is a sharp one:

> The gain comes from being **interrogated**. The loss comes from being
> **evaluated**. Every human audience delivers both, welded together. A machine
> audience is the first thing that can separate them.

A tutee that asks a genuinely confused follow-up question — "wait, but then why
doesn't the water fall out?" — supplies the interrogation. It supplies no social
evaluation at all, because there is no one there to think less of you. If the
hypothesis holds, an artificial audience should beat a human one on transfer while
producing less anxiety, and the effect should be *largest* for the learners who
currently avoid presenting.

That is testable now, cheaply, and it has never been run.

### 9. Scoring an explanation without a judge

An explanation is worthless as evidence if we cannot score it, and the two obvious
scorers are both disqualified by measurements already in this survey.

Not an LLM judge. Selection by LLM judge alone measured **−3.20pp and
−1.68pp, against +8.14pp** for test-based selection. A judge is worse than
nothing here.

Not a human holistic rater either. Human graders of code reach
**Krippendorff's α ≈ 0.20.** The "gold standard" is noise.

What is left is everything checkable about an explanation:

1. **Proposition coverage** against a reference decomposition — did the required
   propositions appear, in a stated scope?
2. **Elaboration and monitoring counts** — the instruments that actually
   *mediated* the effect in Mayer's studies. Count the behaviour that carries the
   mechanism, not the impression it leaves.
3. **Executable prediction checks** — instantiate the learner's explanation and
   run it. If their model of the circuit says the bulb lights, simulate it. The
   world disagrees, not the tutor.
4. **The tutee's downstream accuracy**, capped — did the protégé, taught only
   this, get the next problem right?

Every one of those is a declaration checked by an arbiter that shares no weights
with the generator. It is the grounding ladder applied to prose.

---

## 10. What this section commits us to

- Slides are generated as a **checked declarative spec**, never drawn. Tier D is
  prohibited, including hand-written SVG — which this project's own dashboard was
  guilty of shipping.
- Redundancy is a **runtime switch per learner**, not a style rule.
- The expectancy sentence comes **before** study. Always. It is free and it is the
  difference between g = 0.48 and g = −0.02.
- The default audience is a **camera or a page**, not a room. Presenting to humans
  is available, never required, and never framed as the real version.
- Explanations are scored on **coverage, elaboration, execution and downstream
  accuracy** — never on a judge's impression of quality.

The unifying idea is small and does a lot of work. In both halves of this section,
the artifact — the deck, the presentation — turned out to be worth almost nothing
on its own. What carries the effect is the **constraint the artifact is produced
under**: a gate the slide must pass, an expectancy the explanation is produced
against.

The explanation is the work. The slides are just where you can see it.

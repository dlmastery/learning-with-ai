---
title: "The Explanation Atlas — mining the best explainers, and what that is worth"
section: explanation-atlas
status: draft
date: 2026-07-29
source_report: research/raw/N4-explanation-atlas.md
---

# The Explanation Atlas

There is an outstanding explainer in almost every field, and their work is public.
The obvious idea is to find the best explanation of each concept, learn what makes it
work, and build delivery on that.

The idea survives investigation. Almost nothing about how you would *identify* the
best explanation does.

---

## 1. The literature exists, filed under a name nobody looks up

We predicted this literature would be empty. It is not — head-to-head comparisons of
explanations live under **refutation text**, and finding them was worth more than the
prediction.

Pooled across 44 studies: **g = 0.41 raw, g = 0.28 after trim-and-fill.** A real
effect, with a publication-bias correction that removes a third of it.

Then the part that matters for anyone building on it:

> **Exactly two studies in that meta-analysis exceeded one month. Transfer was never
> coded at all.**

So the field knows that naming a misconception beats explaining cleanly, at short
delay, on retention-style items. It does not know whether the advantage survives to a
month, and it has never asked whether it transfers.

And the strict question — *two real published explanations, head to head, on a
learning outcome* — has **one journal-quality instance in the entire literature.**

---

## 2. The signal we hoped for does not exist, and the way it died is instructive

Views and likes are the felt axis; this survey has said so throughout. The hope was
that **behavioural** platform signals might be diagnostic where attitudinal ones are
not — specifically that **rewind density** marks where comprehension failed.

That hypothesis is dead, and it died three separate times.

**Measured.** YouTube's "most replayed" heatmap was extracted for 51 videos and
analysed. Median entropy **0.976**, where 1.0 is perfectly flat. Enrichment over
uniform: **1.95×**. Peaks explain roughly **16%** of variance by concept, and land
**closer to chapter boundaries than chance** (49.8s versus 87.6s) — that is, they
mostly mark navigation, not confusion.

**Structurally foreclosed.** The signal is **min–max normalised within each video in
51 of 51 cases.** Every video has a peak at 1.0 by construction. Cross-video
comparison — the entire point of an atlas — is impossible from this data.

**And it was already built.** LectureScape (UIST 2014) implemented exactly this
interface. It was **null on every task**, *slower* than baseline outside peaks, and
significantly better on **perceived** efficiency. The felt/real dissociation, appearing
in the tool built to escape it.

**Worse, the sign may be backwards.** Brinton et al. found backward-scrubbing predicts
getting the *next question right* — engagement, not confusion.

The distinction between attitudinal and behavioural signals was the right one to
draw. Drawing it properly is what killed the proposal.

---

## 3. We ran our own predicate as code, and it mostly did not fire

Section 29 proposed that a simplification is legal iff its **quantifier prefix** is
entailed by the formal statement's, and called this *"decidable, cheap, and the most
valuable entry in the table."*

It was implemented and run against **1,524 sentences of MIT OpenCourseWare
transcripts.**

> **The quantifier-prefix check fired zero times.**

Not because the explanations were flawless. Because **speech elides quantifiers rather
than reordering them.** A lecturer says "as close as you like" and never utters ∀ or ∃
in any recoverable form. The predicate is decidable on *formal statements* and
near-inert on *spoken explanation*, which is the medium this whole section is about.

Overall lexical precision across all §29 predicates: **7 true positives from 30 flags —
23%.**

That does not refute the design. It relocates it: these predicates are for **authored
technical prose and generated output**, where quantifiers are written, and not for
transcript mining. A stage-two check on a generator's output, not a stage-one filter
on the world's video.

We are recording this because a predicate this survey called its most valuable
contribution has now been tested, by us, and mostly did not work.

---

## 4. What does predict a good explanation — the one thing with a number

Amid all of that, one feature has a measured effect size, and it is the one Muller's
thesis isolates: **which misconception the explanation names.**

His four versions of the same physics content, measured:

| Version | Gain |
|---|---|
| Exposition — clear, correct | 1.77 |
| Extended — same, longer | 2.41 |
| **Refutation — the same script, plus the misconception named** | **4.41** |
| **Dialogue — two speakers, one holding the misconception** | **4.77** |

And in the same work, perceived learning was **flat (5.7 vs 5.6)** while real learning
differed by **d = 0.71** — with the better format rated significantly **duller**,
**too long**, and **less wanted in lectures.**

Every one of those three is a signal a recommender system acts on. **A platform
optimising for watch-through would systematically down-rank the version that
teaches.**

---

## 5. The design, and the falsifier that is free today

`DESIGN` — **the explanation atlas.** Harvest candidate explanations per concept, grade
them mechanically, measure delayed unassisted transfer on a subset, and learn which
graded features predict the outcome. Once features predict, you can select or generate
without running a trial each time.

But the ordering has changed, and the reasoning is the useful part:

**Build the error atlas first.** The explanation atlas's only feature with a measured
effect is *which misconception it names* — which is worthless unless you know which
misconceptions a population actually holds. That is precisely the error atlas's output.
The two are sequenced, not parallel.

Two practical constraints reinforce it. The error atlas has a corpus already built and
lawfully available. The explanation atlas's interesting corpus is **legally
foreclosing** — captions now return 200 with zero bytes, and an anti-circumvention suit
was heard in August.

**And the decisive test costs nothing.** Muller published four explanations of the
same content with measured outcomes. Grade them with §29's predicates and see whether
the grader recovers the order.

> **If it ranks the clean Exposition highest, §29 measures tidiness rather than
> teaching.**

That is a day's work, it needs no learners, and it should be done before anything is
spent.

---

## 6. What this section commits us to

- **Never rank an explanation by platform metrics** — including behavioural ones. The
  replay signal is flat, normalised within video, already built, already null, and
  possibly sign-reversed.
- **Name the misconception.** It is the only explanation feature with a measured effect
  size, and it beats clarity by more than double.
- **Confine §29's predicates to authored and generated text.** They do not fire on
  speech, and we said they were our most valuable contribution before testing them.
- **Sequence the atlases.** Errors first; explanations are graded *against* the errors
  they name.
- **Run the free falsifier first.** Four published explanations, known outcomes, one
  day.

The instinct behind this section is sound: somewhere there is a better explanation of
every concept than the one in the book, and it is probably free. What this survey can
now say is that **finding it by popularity selects against it** — and that the one
property worth grading for is whether it names the thing the learner already believes.

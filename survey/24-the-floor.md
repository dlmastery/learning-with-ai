---
title: "The Floor — what learning science actually established, with its error bars"
section: floor
status: draft
date: 2026-07-28
source_report: research/raw/B1-learning-science.md
---

# The Floor

The modality principle — present words as narration rather than on-screen text when
there is also a picture — has been meta-analysed twice. Ginns (2005) reports
**d = 0.72, 95% CI [0.52, 0.92]**, k = 39. Reinwein (2012) reports **g = 0.38
[0.33, 0.43]** across k = 86, falling to **g = 0.20 [0.15, 0.25]** after
publication-bias adjustment.

Same principle. Same literature. A factor of three between the flattering number
and the corrected one.

That is the ground this survey stands on, and this section is where a sceptical
reader should come to check the rest of it. Nothing here is about AI. Everything
here is the baseline any AI claim has to clear.

---

## 1. Three facts that govern every number in this document

**Heterogeneity is enormous.** The best meta-analyses in this literature report
I² between **77% and 91%**: 84% (Rowland), 88% (Yang et al.), 77% (Brunmair &
Richter), ~90% (Tetzlaff et al.). A pooled g of 0.50 is not a prediction that you
will get 0.50. It is a one-number summary of a very lumpy distribution.

**Test alignment inflates effects by roughly 2–3×.** Documented three separate
times: Bloom's tutoring studies gave **0.84 SD on the authors' own narrow tests
versus 0.27 SD on broad standardised tests**; Kulik & Fletcher say the size of the
ITS improvement "depended to a great extent" on whether the test was locally
developed or standardised; Slavin's mastery-learning synthesis found positive
effects on experimenter-made measures and "essentially no evidence" on
standardised ones. **Any evaluation in which the system's designers also wrote the
test should be discounted before you read the number.**

**Corrections shrink effects, and most effects have never been corrected.** The
modality effect went 0.38 → 0.20 under publication-bias adjustment. Almost nothing
else in the multimedia corpus has had the same treatment applied.

---

## 2. Grade A — what replicates

| Finding | Effect | Corpus | Heterogeneity |
|---|---|---|---|
| **Retrieval practice** (classroom) | **g = 0.499 [0.442, 0.557]** | 222 studies, 48,478 students (Yang et al. 2021) | **I² = 88%** |
| Retrieval practice (lab) | g = 0.50 [0.42, 0.58] | Rowland 2014 | I² = 84% |
| Retrieval practice → **transfer** | **d = 0.40 [0.31, 0.50]** | 192 effects, 122 experiments, N = 10,382 (Pan & Rickard 2018) | — |
| **Spacing / distributed practice** | **d = 0.54 [0.31, 0.77]** | 22 reports, 31 effects, N > 3,000 — a **2025 classroom meta-analysis** | — |
| **Worked examples** | **g = 0.48** | 8,033 abstracts screened → 55 studies, 181 effects (Barbieri et al. 2023) | robust variance estimation |
| **Expertise reversal** | novices **+0.505 [0.260, 0.750]**, experts **−0.428 [−0.647, −0.209]** | 60 studies, 176 effects, N = 5,924 (Tetzlaff et al. 2025) | **I² ≈ 88–91%** |
| **Multimedia design, averaged** | **g = 0.38 [0.27, 0.49]** | meta-meta: 29 reviews, 1,189 primary studies, 78,177 participants | principle explains nearly all between-review variance |

Retrieval and spacing are carried in **§08**, and expertise reversal is the
organising result of **§22**; they are restated here only so that their confidence
intervals and their heterogeneity sit on the same page as everything else. The
interval on spacing is the one to notice: **[0.31, 0.77]** is a range in which the
low end is a modest effect and the high end is among the largest in education. Both
are consistent with the data.

Two more numbers set the scale for the whole document. Kraft (2020) finds that
**most education interventions produce 0.10 SD or less** on broad measures. And
Pan & Rickard's transfer estimate is the honest ceiling for "does it generalise":
**0.40, weakest to rearranged stimulus–response items, to untested material seen
during study, and to worked-example problems.** Retention transfers better than
anyone deserves. Transfer transfers about half as well.

---

## 3. The one place where the sign flips

Interleaving is the most instructive result in the corpus because it is not a
matter of magnitude. It is a matter of direction.

Brunmair & Richter (2019), 59 studies, 238 effect sizes nested in 158 samples,
overall **g = 0.42, I² = 77%**:

| Material | Effect |
|---|---|
| Paintings / visual category induction | **g = 0.67** |
| Mathematics tasks | **g = 0.34** |
| Expository texts | n.s. |
| Tastes | n.s. |
| **Words (vocabulary-like items)** | **g = −0.39 — blocking wins** |

The mechanism is discrimination, not spacing: interleaving helps when
between-category similarity is high and within-category similarity is low. Where
there are no categories to discriminate — paired-associate vocabulary —
interleaving is a **harm**, and a substantial one.

The classroom evidence is unusually good. Rohrer, Dedrick, Hartwig & Cheung (2020)
ran a preregistered cluster RCT across **54 seventh-grade mathematics classes**,
four months of interleaved versus blocked assignments, then an **unannounced test
one month later**: **61% versus 38%, d = 0.83**. Teachers implemented it without
training. That is one of the strongest classroom results in all of learning
science, and it lives inside a technique whose pooled effect changes sign by
material type.

**A system that applies "interleave everything" as a global policy will help
mathematics practice and damage vocabulary learning in the same session.** The
policy has to be per-material, and the moderator is stated well enough to
implement.

---

## 4. The nulls

Every section of this survey carries at least one documented negative result. This
one has to carry several, because the floor is defined as much by what failed as by
what held.

**The testing effect failed to appear in a 2026 replication pair.** Two Prolific
experiments with delayed post-tests, corrective feedback, attention checks and fair
pay found no testing effect at all. The authors attribute it to insufficient
sustained engagement in crowdsourced settings. This is the single most
uncomfortable result in the section for anything built on self-directed AI study,
because the condition it identifies — a learner nominally retrieving, without
sustained effortful attention — is exactly the condition a chat interface makes
easy to enter. **The effect is contingent on effortful attentive retrieval, not on
the surface form of being quizzed.**

Self-explanation prompts reduced the worked-example effect. Barbieri et al.
(2023) found pairing worked examples with self-explanation prompts to be a
significant *negative* moderator, and correct examples alone outperformed
incorrect-only and correct-plus-incorrect combinations. The authors: "pairing
examples with self-explanation prompts may not be a fruitful design modification."
This survey argues hard for learner explanation in **§05**, and this is the
strongest evidence against the naive form of that argument. It does not overturn
self-explanation as an activity; it means bolting a prompt onto a worked example is
not the way to get it.

**Intelligent tutoring in K–12 mathematics is near zero.** Steenbergen-Hu &
Cooper (2013): ITS "had no negative and perhaps a small positive effect," with
effects *larger* for the general population than for low achievers. K–12
mathematics is the population most often invoked in AI-tutoring pitches, and it is
the population where the closest technological precedent measured approximately
nothing.

The founding retrieval-practice result had a design confound. Soderstrom, Kerr
& Bjork (2016) replicated Karpicke & Roediger (2008) between subjects, then
controlled the spacing differences inherent to that design within subjects — and
both repeated testing and repeated restudy improved learning. The testing
effect survives. The strong claim that restudy does nothing does not.

Prior knowledge did not moderate multimedia design effects in Noetel's
meta-meta-analysis (**p = 0.14**), which sits in open tension with the
expertise-reversal literature in the row above it. The honest reading: the reversal
is well established for *assistance and guidance* manipulations and is not reliably
detectable across the broad multimedia-design corpus. We report the tension rather
than picking the side that suits us.

---

## 5. Folklore

Germane cognitive load is not a measurable quantity. The
intrinsic/extraneous/germane trichotomy has never been cleanly operationalised as
three separately measurable additive quantities. Kalyuga (2011) argues germane load
is not independently identifiable and that the framework risks unfalsifiability —
any result can be re-described post hoc as a shift between load types. de Jong
(2010) names the circularity: load is inferred from performance and then used to
explain performance. Sweller, van Merriënboer & Paas themselves reconceptualised
germane load in 2019 as resources *redirected to* intrinsic load rather than an
independent source, and consumers of the theory routinely cite the 2019 paper while
still using the old three-bucket model in their measurement.

The empirical tell is clean. Noetel et al. found multimedia design interventions
improved **learning at g = 0.38** and improved measured **cognitive-load management
at only g = 0.22 [0.04, 0.40], k = 68.** The proposed mediator moves less than the
outcome. **Cite cognitive load theory for its design predictions, which are
excellent. Do not cite "reduces extraneous load" as though it were a measured
quantity.**

The redundancy principle is wrong in one direction. Adesope & Nesbit: adding
text to audio, **g = 0.29 [0.20, 0.39]**; adding audio to text, **g = −0.04
[−0.14, 0.06], n.s.** "Never duplicate" is not what the data say.

Decoration does nothing. Decorative animation **g = −0.05, n.s.**; meaningful
representational animation **g = 0.40**. 3D pedagogical agents **g = 0.11, n.s.**;
2D agents g = 0.38. Seductive details harm when persistent on screen (g = 0.43
for removal) and not when transient (g = 0.12, n.s.).

**Conversational style expires at 35 minutes.** The personalisation principle pools
at g = 0.33 [0.23, 0.44] — but its own meta-analysis reports interest **d = 0.15,
n.s., learning-assistance d = 0.16, n.s.**, and effects that are small and
non-significant in studies longer than **35 minutes**. Almost every citation of
this principle omits the boundary.

Pre-training is under-evidenced, not evidenced. No independent systematic
review covers it. The commonly quoted d ≈ 0.75 comes from lab-of-origin tallies of
about sixteen comparisons.

**Learning styles: zero, with 89% belief.** Pashler et al. established that the
meshing hypothesis requires a crossover interaction design; almost no study used
one, and those that did contradicted it. Three subsequent direct tests: Rogowsky et
al. (2015), no interaction; Husmann & O'Loughlin (2019), **N = 426**, VARK scores
uncorrelated with course performance and strategy–style alignment uncorrelated with
outcome; Melzner & Kappes (2024), **N = 222**, adequately powered, no interaction
and no prediction of judgments of learning. Against that: **89.1% of 15,405
educators across 18 countries believe matching works, with no decline over
time, and 91% of 112 recent health-professions education papers** are premised
on it — so an educator who searches the literature is given a consistent and
inaccurate endorsement. An AI that grills a learner for a sensory-modality label is
automating a forty-year null at scale.

Bloom's two sigma is retired in this survey; the argument and the replacement
figures are in **§19** and **§03**, and are not repeated here.

---

## 6. The strongest objection

*If I² is 88%, the pooled numbers are noise and you should stop quoting them.*

Take it seriously, because it is half right. Heterogeneity that large means the
pooled value is a poor predictor of any specific implementation. It does not
mean the direction is unstable. Cepeda's 271 massed-versus-spaced comparisons
produced **only 12** showing no effect or a negative effect. Latimier's expanding-
versus-uniform comparison — the one that came out null — produced **I² = 0%** across
54 effects, which is what a genuinely clean nothing looks like. The literature can
tell the difference between a lumpy real effect and an absence, and it does.

The correct posture is therefore narrow: **treat pooled effects as evidence about
sign and rough order of magnitude, treat moderators as the actionable content, and
never quote a single number as a promise.** Interleaving's g = 0.42 is nearly
useless; its moderator table is a specification.

Two further limits belong to this objection rather than to a footnote. Donoghue &
Hattie's meta-analysis of ten techniques (**242 studies, 1,619 effects, 169,179
participants, mean ES = 0.56) found effects much greater for lower-ability than
higher-ability students and a corpus dominated by surface and factual
outcomes** — the authors explicitly caution against extrapolating to deeper
relational learning. And **6% of classroom retrieval-practice experiments were
conducted in non-WEIRD countries**; the interleaving literature is, in its own
reviewers' words, "dominated by laboratory studies of university undergraduates."

---

## 7. What this section commits us to

- **Every effect size in this survey carries its interval and, where reported, its
  I².** Retrieval practice is g = 0.499 **with I² = 88%**, and the second half of
  that sentence is not optional.
- **Discount any evaluation whose designers wrote the test.** The documented
  inflation is 2–3×.
- **Per-material policies, never global ones.** Interleaving is g = 0.34 in
  mathematics and **g = −0.39** in vocabulary. A single switch cannot serve both.
- **Do not claim to measure germane load.** Use the design effects; drop the
  mediation story.
- **No modality labels, ever.** Adapt on prior knowledge, task properties,
  self-regulation and motivation type — the four adaptation targets with evidence.
- **Assume decline.** ITS effects were significantly larger in earlier studies than
  in later, better-controlled ones. Expect the same trajectory for AI tutoring, and
  write the claims so they survive it.
- **Benchmark honestly.** An AI tutor showing **d ≈ 0.4 on a test it did not help
  design, against an active control, at a delayed post-test** would sit at the top
  of this entire literature. Anything above 0.8 should be presumed to reflect
  aligned tests or weak controls until shown otherwise.

The floor is not low. Retrieval practice and distributed practice are among the
largest, most replicated effects anyone in education has ever measured, and they
were established with paper and a clock. The interesting question for everything
that follows is not whether a machine can beat them. It is whether a machine can
finally get them *run* — with delay, with feedback, with genuine effortful
retrieval — for learners who have never had anyone to run them.

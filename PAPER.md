# Learning in the New Frontier AI World

### A survey of what AI-native learning has actually been measured to do, and a specification for what it should be

Corrections ledger: [`CORRECTIONS.md`](CORRECTIONS.md) · Adversarial reviews: [`evidence/`](evidence/)
Interactive demonstrations: <https://dlmastery.github.io/learning-with-ai/demos/>

---

## Abstract

Generative AI arrived in education as a capability without a specification. Three
years on, the field has produced roughly 2,900 papers and, by our census, **seven
randomised controlled trials** — three of them second-language learning. It measures
resemblance, preference and engagement. It very rarely measures whether anyone
learned anything, and almost never measures it **after the tool is taken away**.

This survey is an attempt to write the missing specification. It rests on 53 research
reports;  every claim carries an evidence label,
every section carries at least one documented null, and every one of the authors'
errors is published in an append-only ledger rather than quietly edited — **23 of
the 65 corrections were found by an adversarial reviewer rather than by us.**

**The organising finding is about agents.** An agent differs from a chatbot in four
ways — sampling, execution, persistence, absence — and each is a multiplier on
something else, which gives a rule: *the value of an agentic loop is **bounded by**
the value of the external check it closes on.* That rule explains the whole reliability landscape.
Where a check exists, agents reach **79.2%** (SWE-bench Verified) and **83.8%**
(Terminal-Bench). Where the check is weak or absent, **21.0%** (PaperBench) and **4.6%**
(SciCode, which has hand-written tests — hence a bound rather than an equality).
Teaching is in the second column, and the reason is now measured: across **223 real
tutoring domains, no model beat chance at labelling an incorrect student action.**
Coding agents work because `pytest` exists. **Pedagogy has no `pytest`, and every
agentic capability in education is waiting on one.**

Three findings constrain what may be built. **Felt learning and real learning move in
opposite directions** — preference shifts at *d* ≈ 0.48 while knowledge does not, and
the effect survives explicit debiasing, so every cheaply optimisable metric is the
wrong one. **Measurement without a decision rule is inert** — both arms of the
decisive trial revised instruction more often; only the arm told *what to change*
moved achievement. **Unguarded assistance is an active harm**, leaving learners 17%
worse on later unassisted work, while the guardrailed arm's unassisted coefficient is
−0.004, not significant: restraint removes harm and has not been shown to teach.

On speed, the popular claim is roughly right and imprecise. Learning is counted in
**opportunities, not days** — across 1.3 million observations, learning *rate* varies
by 1.14× while *prior knowledge* varies by 3.6×, and time-based models fit poorly.
The defensible bound is **10–40× on elapsed calendar and 3–5× on engaged effort**,
one documented case at ~300×, and **1×** on both durability and procedural skill.
Stated honestly: **a week's understanding in an hour; a year's retention in six hours
spread across two months.** What limits polymathy is not learning rate but the fixed
cost of orientation — how many times one can afford to be a beginner.

We design for the margin first. A census returns 30 randomised trials of
generative-AI tutoring that mention students and **zero** that mention disability,
dyslexia, ADHD, autism, special education or an IEP. Every effect size in this field
was measured on somebody else's child.

The central claim is that the measured 0.2–0.4 SD band describes systems that answer
freely, forget between sessions, cannot see the work, cannot point, never change
method, and agree with the learner — and that nobody has built and measured the
constrained, grounded, pivoting, remembering, teachable alternative. **That nobody has
measured it is proven. That it would do better is a hypothesis**, and Part VII states
the conditions under which we would withdraw it.

---

## How to read this

Every claim carries an evidence label — `MEASURED-RCT`, `MEASURED-META`,
`MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`. A `VENDOR` claim is
never restated as a finding. Every section contains at least one documented null,
given its own space rather than a footnote. Where a number could not be verified it
is reported as unverifiable rather than omitted or softened.

Thirteen of the techniques described here have a working demonstration that runs in
a browser with no server and no key. Each demonstration states whether it is
*computed* — the page performs the operation — or *scripted*, a labelled replay.
One of them documents a mechanism this project proposed, benchmarked, and
**falsified**.

---

## Contents


**Part I — What is established**

1. [The Floor — what learning science actually established, with its error bars](#the-floor-what-learning-science-actually-established-with-its-error-bars)
2. [What Works — and the One Design Choice That Decides It](#what-works-and-the-one-design-choice-that-decides-it)
3. [The Scoreboard — what AI tutoring has actually been measured to do](#the-scoreboard-what-ai-tutoring-has-actually-been-measured-to-do)
4. [Fifteen Hundred Papers, Seven Trials — what the field measures instead of learning](#fifteen-hundred-papers-seven-trials-what-the-field-measures-instead-of-learning)

**Part II — The system the evidence forces**

5. [The JARVIS Inversion — an ambient tutor is not an ambient assistant](#the-jarvis-inversion-an-ambient-tutor-is-not-an-ambient-assistant)
6. [The Compression — a week's understanding in an hour, and what that sentence can honestly mean](#the-compression-a-week-s-understanding-in-an-hour-and-what-that-sentence-can-honestly-mean)
7. [Pedagogy Has No Pytest — what an agent is, and the one thing it is missing](#pedagogy-has-no-pytest-what-an-agent-is-and-the-one-thing-it-is-missing)
8. [Enumerate, Don't Judge — the belief object, and how it routes around the verifier gap](#enumerate-don-t-judge-the-belief-object-and-how-it-routes-around-the-verifier-gap)
9. [Ekalavya's Thumb — the system we are actually building](#ekalavya-s-thumb-the-system-we-are-actually-building)
10. [The Village — what makes a crew of agents a crew](#the-village-what-makes-a-crew-of-agents-a-crew)
11. [The One Interaction That Survived — personalisation as a measurement problem](#the-one-interaction-that-survived-personalisation-as-a-measurement-problem)
12. [The Archivist — persistent learner state, and where to put it](#the-archivist-persistent-learner-state-and-where-to-put-it)

**Part III — The mechanisms**

13. [Teach to Learn — the highest-evidence, least-built intervention](#teach-to-learn-the-highest-evidence-least-built-intervention)
14. [The Explanation Is the Work — generative slides, and the learner as explainer](#the-explanation-is-the-work-generative-slides-and-the-learner-as-explainer)
15. [The Ladder of Explanation — ELI10 to ELI25, and the rule that makes a simplification legal](#the-ladder-of-explanation-eli10-to-eli25-and-the-rule-that-makes-a-simplification-legal)
16. [What the Explainers Invented — 104 techniques, and the one nobody has ported](#what-the-explainers-invented-104-techniques-and-the-one-nobody-has-ported)
17. [Explaining Hard Things — the fidelity invariants, instantiated](#explaining-hard-things-the-fidelity-invariants-instantiated)
18. [The Explanation Atlas — the head-to-head literature exists, filed under refutation text](#the-explanation-atlas-the-head-to-head-literature-exists-filed-under-refutation-text)
19. [Nobody Needs a Better Scheduler — the science of durable remembering](#nobody-needs-a-better-scheduler-the-science-of-durable-remembering)
20. [Beyond the Tutor — the five roles nobody is building](#beyond-the-tutor-the-five-roles-nobody-is-building)
21. [What the Object Must Refuse — embodiment, manipulatives, and executable material](#what-the-object-must-refuse-embodiment-manipulatives-and-executable-material)
22. [Showing — illustration, animation, and the arithmetic of a wrong picture](#showing-illustration-animation-and-the-arithmetic-of-a-wrong-picture)

**Part IV — Correctness**

23. [Grounding — correctness that lives in the verifier](#grounding-correctness-that-lives-in-the-verifier)
24. [Assessment After the Artifact — measuring a person when the work no longer indicates them](#assessment-after-the-artifact-measuring-a-person-when-the-work-no-longer-indicates-them)

**Part V — Who it is for**

25. [The Empty Chair — designing for the margin first](#the-empty-chair-designing-for-the-margin-first)
26. [The Coordinator's Week — five hours of statutory admin against four available](#the-coordinator-s-week-five-hours-of-statutory-admin-against-four-available)
27. [Who Is Not in the Room — reach, language, and the barriers attention does not remove](#who-is-not-in-the-room-reach-language-and-the-barriers-attention-does-not-remove)
28. [What We Owe Children — the legal floor as a design specification](#what-we-owe-children-the-legal-floor-as-a-design-specification)

**Part VI — The field, and what it has already built**

29. [The Substrate — what the frontier actually supplies](#the-substrate-what-the-frontier-actually-supplies)
30. [The Textbook That Writes Itself — and who it remembers](#the-textbook-that-writes-itself-and-who-it-remembers)
31. [The Canon — what the history of pedagogy already settled](#the-canon-what-the-history-of-pedagogy-already-settled)
32. [The Market — nine bets, one graveyard, and the number that shrinks as you look at it](#the-market-nine-bets-one-graveyard-and-the-number-that-shrinks-as-you-look-at-it)
33. [Inference Is 0.43% of Delivery — and human judgement is the scarce input](#inference-is-0-43-of-delivery-and-human-judgement-is-the-scarce-input)
34. [The Two-Hour School — two hours buys the schedule, and does not buy the attainment](#the-two-hour-school-two-hours-buys-the-schedule-and-does-not-buy-the-attainment)
35. [Prior Art — thirty-five builds, 128 notebooks, zero exercises](#prior-art-thirty-five-builds-128-notebooks-zero-exercises)
36. [Motivation — wanting to continue](#motivation-wanting-to-continue)

**Part VII — What we do not know**

37. [What We Cannot See From Here — the unknown unknowns, and the questions that expose them](#what-we-cannot-see-from-here-the-unknown-unknowns-and-the-questions-that-expose-them)
38. [Attention, and the Missing Executive — what the best teachers actually do](#attention-and-the-missing-executive-what-the-best-teachers-actually-do)
39. [Greenfield — what you would build with no school, no textbook and no exam](#greenfield-what-you-would-build-with-no-school-no-textbook-and-no-exam)
40. [The Agenda — three experiments, and what would falsify this survey](#the-agenda-three-experiments-and-what-would-falsify-this-survey)

---


---

# Part I · What is established

*Before any design argument, the evidence — with its error bars, its heterogeneity, and its nulls. A reader should be able to check everything that follows against this part.*


## 1. The Floor — what learning science actually established, with its error bars

<sub>Source report: `research/raw/B1-learning-science.md`</sub>

The modality principle (present words as narration rather than on-screen text when
there is also a picture) has been meta-analysed twice. Ginns (2005) reports
d = 0.72, 95% CI [0.52, 0.92], k = 39. Reinwein (2012) reports **g = 0.38
[0.33, 0.43]** across k = 86, falling to g = 0.20 [0.15, 0.25] after
publication-bias adjustment.

Same principle. Same literature. A factor of three between the flattering number
and the corrected one.

That is the ground this survey stands on, and this section is where a sceptical
reader should come to check the rest of it. Nothing here is about AI. Everything
here is the baseline any AI claim has to clear.

---

## 1. Three facts that govern every number in this document

**Heterogeneity is enormous.** The best meta-analyses in this literature report
I² between 77% and 91%: 84% (Rowland), 88% (Yang et al.), 77% (Brunmair &
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

## 2. Grade A, what replicates

| Finding | Effect | Corpus | Heterogeneity |
|---|---|---|---|
| **Retrieval practice** (classroom) | **g = 0.499 [0.442, 0.557]** | 222 studies, 48,478 students (Yang et al. 2021) | **I² = 88%** |
| Retrieval practice (lab) | g = 0.50 [0.42, 0.58] | Rowland 2014 | I² = 84% |
| Retrieval practice → **transfer** | **d = 0.40 [0.31, 0.50]** | 192 effects, 122 experiments, N = 10,382 (Pan & Rickard 2018) | — |
| **Spacing / distributed practice** | **d = 0.54 [0.31, 0.77]** | 22 reports, 31 effects, N > 3,000 — a **2025 classroom meta-analysis** | — |
| **Worked examples** | **g = 0.48** | 8,033 abstracts screened → 55 studies, 181 effects (Barbieri et al. 2023) | robust variance estimation |
| **Expertise reversal** | novices **+0.505 [0.260, 0.750]**, experts **−0.428 [−0.647, −0.209]** | 60 studies, 176 effects, N = 5,924 (Tetzlaff et al. 2025) | **I² ≈ 88–91%** |
| **Multimedia design, averaged** | **g = 0.38 [0.27, 0.49]** | meta-meta: 29 reviews, 1,189 primary studies, 78,177 participants | principle explains nearly all between-review variance |

Retrieval and spacing are carried in **§19**, and expertise reversal is the
organising result of **§11**; they are restated here only so that their confidence
intervals and their heterogeneity sit on the same page as everything else. The
interval on spacing is the one to notice: [0.31, 0.77] is a range in which the
low end is a modest effect and the high end is among the largest in education. Both
are consistent with the data.

Two more numbers set the scale for the whole document. Kraft (2020) finds that
**most education interventions produce 0.10 SD or less** on broad measures. And
Pan & Rickard's transfer estimate is the ceiling for "does it generalise":
**0.40, weakest to rearranged stimulus–response items, to untested material seen
during study, and to worked-example problems.** Retention transfers better than
anyone deserves. Transfer transfers about half as well.

---

## 3. The one place where the sign flips

Interleaving is the most instructive result in the corpus because it is not a
matter of magnitude. It is a matter of direction.

Brunmair & Richter (2019), 59 studies, 238 effect sizes nested in 158 samples,
overall g = 0.42, I² = 77%:

| Material | Effect |
|---|---|
| Paintings / visual category induction | **g = 0.67** |
| Mathematics tasks | **g = 0.34** |
| Expository texts | n.s. |
| Tastes | n.s. |
| **Words (vocabulary-like items)** | **g = −0.39 — blocking wins** |

The mechanism is discrimination, not spacing: interleaving helps when
between-category similarity is high and within-category similarity is low. Where
there are no categories to discriminate, as in paired-associate vocabulary,
interleaving does harm, and a substantial amount of it.

The classroom evidence is unusually good. Rohrer, Dedrick, Hartwig & Cheung (2020)
ran a preregistered cluster RCT across 54 seventh-grade mathematics classes,
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
because the condition it identifies, a learner nominally retrieving without
sustained effortful attention, is exactly the condition a chat interface makes
easy to enter. **The effect is contingent on effortful attentive retrieval, not on
the surface form of being quizzed.**

Self-explanation prompts reduced the worked-example effect. Barbieri et al.
(2023) found pairing worked examples with self-explanation prompts to be a
significant *negative* moderator, and correct examples alone outperformed
incorrect-only and correct-plus-incorrect combinations. The authors: "pairing
examples with self-explanation prompts may not be a fruitful design modification."
This survey argues hard for learner explanation in **§14**, and this is the
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
controlled the spacing differences inherent to that design within subjects.
Both repeated testing and repeated restudy improved learning. The testing
effect survives. The strong claim that restudy does nothing does not.

Prior knowledge did not moderate multimedia design effects in Noetel's
meta-meta-analysis (p = 0.14), which sits in open tension with the
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
improved learning at g = 0.38 and improved measured cognitive-load management
at only g = 0.22 [0.04, 0.40], k = 68. The proposed mediator moves less than the
outcome. **Cite cognitive load theory for its design predictions, which are
excellent. Do not cite "reduces extraneous load" as though it were a measured
quantity.**

The redundancy principle is wrong in one direction. Adesope & Nesbit: adding
text to audio, g = 0.29 [0.20, 0.39]; adding audio to text, **g = −0.04
[−0.14, 0.06], n.s.** "Never duplicate" is not what the data say.

Decoration does nothing. Decorative animation g = −0.05, n.s.; meaningful
representational animation g = 0.40. 3D pedagogical agents g = 0.11, n.s.;
2D agents g = 0.38. Seductive details harm when persistent on screen (g = 0.43
for removal) and not when transient (g = 0.12, n.s.).

**Conversational style expires at 35 minutes.** The personalisation principle pools
at g = 0.33 [0.23, 0.44] — but its own meta-analysis reports interest **d = 0.15,
n.s., learning-assistance d = 0.16, n.s.**, and effects that are small and
non-significant in studies longer than 35 minutes. Almost every citation of
this principle omits the boundary.

Pre-training is under-evidenced, not evidenced. No independent systematic
review covers it. The commonly quoted d ≈ 0.75 comes from lab-of-origin tallies of
about sixteen comparisons.

**Learning styles: zero, with 89% belief.** Pashler et al. established that the
meshing hypothesis requires a crossover interaction design; almost no study used
one, and those that did contradicted it. Three subsequent direct tests: Rogowsky et
al. (2015), no interaction; Husmann & O'Loughlin (2019), N = 426, VARK scores
uncorrelated with course performance and strategy–style alignment uncorrelated with
outcome; Melzner & Kappes (2024), N = 222, adequately powered, no interaction
and no prediction of judgments of learning. Against that: **89.1% of 15,405
educators across 18 countries believe matching works, with no decline over
time, and 91% of 112 recent health-professions education papers** are premised
on it — so an educator who searches the literature is given a consistent and
inaccurate endorsement. An AI that grills a learner for a sensory-modality label is
automating a forty-year null at scale.

Bloom's two sigma is retired in this survey; the argument and the replacement
figures are in **§31** and **§9**, and are not repeated here.

---

## 6. The strongest objection

*If I² is 88%, the pooled numbers are noise and you should stop quoting them.*

Take it seriously, because it is half right. Heterogeneity that large means the
pooled value is a poor predictor of any specific implementation. It does not
mean the direction is unstable. Cepeda's 271 massed-versus-spaced comparisons
produced only 12 showing no effect or a negative effect. Latimier's expanding-
versus-uniform comparison, the one that came out null, produced I² = 0% across
54 effects, which is what a genuinely clean nothing looks like. The literature can
tell the difference between a lumpy real effect and an absence, and it does.

The correct posture is therefore narrow: **treat pooled effects as evidence about
sign and rough order of magnitude, treat moderators as the actionable content, and
never quote a single number as a promise.** Interleaving's g = 0.42 is nearly
useless; its moderator table is a specification.

Two further limits belong to this objection. Donoghue &
Hattie's meta-analysis of ten techniques (**242 studies, 1,619 effects, 169,179
participants, mean ES = 0.56) found effects much greater for lower-ability than
higher-ability students and a corpus dominated by surface and factual
outcomes** — the authors explicitly caution against extrapolating to deeper
relational learning. And **6% of classroom retrieval-practice experiments were
conducted in non-WEIRD countries**; the interleaving literature is, in its own
reviewers' words, "dominated by laboratory studies of university undergraduates."

---

## 7. Rules the floor imposes on every later claim

- **Every effect size in this survey carries its interval and, where reported, its
  I².** Retrieval practice is g = 0.499 **with I² = 88%**, and the second half of
  that sentence is not optional.
- **Discount any evaluation whose designers wrote the test.** The documented
  inflation is 2–3×.
- **Per-material policies, never global ones.** Interleaving is g = 0.34 in
  mathematics and g = −0.39 in vocabulary. A single switch cannot serve both.
- **Do not claim to measure germane load.** Use the design effects; drop the
  mediation story.
- **No modality labels, ever.** Adapt on prior knowledge, task properties,
  self-regulation and motivation type, the four adaptation targets with evidence.
- **Assume decline.** ITS effects were significantly larger in earlier studies than
  in later, better-controlled ones. Expect the same trajectory for AI tutoring, and
  write the claims so they survive it.
- **Benchmark honestly.** An AI tutor showing **d ≈ 0.4 on a test it did not help
  design, against an active control, at a delayed post-test** would sit at the top
  of this entire literature. Anything above 0.8 should be presumed to reflect
  aligned tests or weak controls until shown otherwise.

The floor is not low. Retrieval practice and distributed practice are among the
largest, most replicated effects anyone in education has ever measured, and they
were established with paper and a clock. Whether a machine can beat them is the
wrong question to carry into everything that follows. Ask instead whether a
machine can finally get them *run*, with delay, with feedback, with genuine
effortful retrieval, for learners who have never had anyone to run them.


## 2. What Works — and the One Design Choice That Decides It


The wins available today are large, real, and measured.

| Result | Effect | Evidence |
|---|---|---|
| Guardrailed AI tutor | **+127% practice**; unassisted exam **−0.004 (ns)** — removes harm, adds no measured benefit | Randomised, ~1,000 students |
| Gemini Guided Learning, Sierra Leone (§3)| **+0.258 SD (ANCOVA)** — but the **unadjusted estimate is +0.216 SD, SE 0.137, *not significant*** | Pre-registered RCT; 1,763 enrolled, **1,423 analysed**; model swapped mid-trial; Google.org + Gates funded |
| Retrieval practice | **g = 0.499** [0.442, 0.557] in labs *and* classrooms | 222 studies, 48,478 students; **I² = 88%** |
| Learning by teaching (human tutee) | **g = 0.56**, robust at delay | Meta-analysis; expectancy must precede study |
| Productive failure | **g = 0.36**, rising to **0.58** at high fidelity | Meta-analysis |
| Spaced practice | classroom **d = 0.54** | 12 of 271 comparisons failed |

These are not incremental results. But the Sierra Leone headline does not survive
the appendix, and this document said otherwise in an earlier draft. **Corrected in
place:** the ITT estimate is +0.258 SD (p = 0.029); the *unadjusted* estimate is
**+0.216 SD, SE 0.137 (not significant).** The effect loads entirely on Grade 8
(Grade 7 main effect −0.078), gaps widened at +0.195 SD per SD of baseline, and
attrition differed by arm. It is a promising result from a hard setting. It is not
the strongest evidence in the history of educational technology, and calling it
that was our error.

The mechanism is suggested, not established. In the Sierra Leone deployment
113,344 *messages* were coded: **91.4% concept-building, scaffolding in 76.4% of
responses, direct solutions in 2.1%.** But the paper states plainly that the team
**could not link transcripts to individual students' assessment outcomes.** The
coding and the effect estimate sit in the same report and are never joined (§3). The
withholding is real; that the withholding *caused* the gain is an inference.

## The one design choice that decides it

The same model, given to the same students, produces opposite outcomes depending
on a single property:

| | Practice | Exam, unassisted |
|---|---|---|
| Answers freely | +48% | **−17%** |
| Withholds, hints, requires reasoning | **+127%** | **−0.004, n.s.** |

Read the second row precisely, because the obvious reading is wrong. The
guardrailed arm's unassisted coefficient is **−0.004 and not significant**. That
is *harm removed*, not *benefit added*. **Restraint is what removes the harm;
it has not been shown to teach.** Every harm in this survey comes from an
unconstrained system. That is a weaker claim than "restraint is the active
ingredient," and it is the one the data supports.

This is good news, and it is immediately actionable: the win needs no new model,
no new capability, and no additional cost. It needs a loop that decides when
*not* to answer.

## Why the field mostly builds the other one

This is a measurement problem, and measurement problems are fixable.

Three research streams in this survey converged independently on one result. It
is the paper's central finding and it indicts most of what the field is building.

Felt learning is what every optimisation loop can measure. Real learning is what
none of them measure. So systems drift toward the former, and the two dissociate:

| Capability | Felt / affect | Actual learning |
|---|---|---|
| AI assistance (Bastani, PNAS) | practice scores **+48%** | unassisted performance **−17%** |
| Pedagogical agents / avatars | social presence, well-being **d = .85–1.01** | learning **did not move** (3 field experiments, 2024) |
| Animation vs static graphics | comprehensibility, interest, enjoyment, motivation all rise (Kim, Yoon, Whang & Tversky 2007) | *"but not comprehension test score"* |

Supporting evidence points the same way. Berney & Bétrancourt's meta-analysis
(61 studies, N = 7,036) puts animation's advantage at g = 0.226. Tversky,
Morrison & Bétrancourt (2002) found **no case** where animation beat an
*informationally equivalent* static graphic — the apparent wins were confounds.
Mayer's own experiments found annotated static illustrations equalled or beat
narrated animations on transfer. Paik & Schraw (2013) found representational
animation *negatively* affected learning.

And the mirror image completes it: Deslauriers et al. (2019, PNAS) showed active
learning raises real learning while lowering felt learning. Students in the
condition that taught them more reported learning less.

## Why this is a systems problem

Every instrument a product team already owns points at the wrong quantity.

- Engagement metrics, session length, retention, NPS and thumbs-up all proxy felt
  learning.
- RLHF optimises for preferred responses. Preferred means fluent, complete,
  immediate — the exact profile that produces fluency illusion.
- **Every LLM→explanatory-video pipeline surveyed optimises on VLM or human
  preference judgments**, i.e. directly on the axis that dissociates from
  comprehension.
- No paper found in the LLM-explanatory-video literature measures human learning
  gain. The most ambitious metric (TeachQuiz) measures whether *a VLM* recovers
  the knowledge.

A field that cannot measure its objective will optimise its proxy. That is what
is happening.

## Consequences for this survey's design claims

1. The refusal engine is not a preference. It is the only mechanism that trades
   felt learning for real learning deliberately. Bastani gives the price of not
   having one: −17%.
2. Build the face and the animation for engagement, and say so. Both are real
   wins for an ADHD learner, because attention is a prerequisite. Neither is a
   comprehension intervention. Claiming otherwise is the error.
3. Animate only when the change itself is the learning target. This is the single
   moderator that survives meta-analysis. Motion should depict motion; it should
   never decorate a static idea.
4. Never ship an objective function that rewards satisfaction. See F6 for the
   replacement.
5. Assessment must measure unassisted, delayed performance. A post-test taken
   with the tutor present measures the tutor.

## The uncomfortable corollary

The learner cannot detect this either. Fluency illusion is *defined* by
subjective confidence exceeding objective retention. So a system optimising
learner-reported satisfaction, and a learner choosing what feels effective, fail
in the same direction — together, and confidently.

This is why the survey treats frequent low-stakes retrieval (H1.2) as
non-negotiable infrastructure rather than a feature. It is the only routinely
available instrument that measures the thing that matters.


---

## Correction — B2 (2026-07-27)

The efficacy scoreboard revised three claims in this section. Recorded rather than
quietly edited, per the editorial standard.

1. The Sierra Leone headline is fragile. +0.258 SD holds only under ANCOVA;
   Table C.4's unadjusted estimate is **+0.216 SD, SE 0.137 (not significant)** (§3).
   1,423 of 1,763 analysed. The report itself is unusually candid; the distortion
   happened downstream, including here.
2. Restraint removes harm; it does not add measured benefit. Bastani's
   guardrailed arm scores **−0.004 (ns)** on the unassisted exam. The +127% is a
   *practice* gain. The correct claim is: unguarded AI is an active harm (−17%),
   and guardrails buy that back. That is still the most important design result in
   the survey, though it is a smaller claim than "restraint teaches."
3. Gap-widening is the default expectation, not a risk. Sierra Leone
   +0.195 SD per baseline SD (p=0.002, an order of magnitude more robust than the
   main effect); Nigeria +0.151; Lehmann concurs. **A student 1 SD below the mean
   gains ≈0.055 SD.** Three countries, three tools, three age groups, same sign.

The load-bearing gap: no study in the corpus administered a delayed retention
test. ERIC counts (2026-07-27): ChatGPT + "learning outcomes" = 95;
+ "delayed post-test" = 2; + "retention test" = **0**; + "transfer test" =
**0**; + "preregistered" = **0**, against 273 ERIC records using delayed
post-tests on other topics. The instrument exists. The field does not use it.

And the field's most-cited meta-analysis (Wang & Fan 2025, g = 0.867, >250
citations) was **retracted in 2026**; the authors have not responded.

What survives: supervised LLM tutoring lands at **0.2–0.4 SD** — the same band
as pre-LLM ITS (0.32–0.42) and in-person human tutoring (**0.288**, 96 RCTs). That
is a real, useful, affordable effect. It is not an order-of-magnitude jump, and
GenAI without teacher support is null (g = 0.077).


## 3. The Scoreboard — what AI tutoring has actually been measured to do

<sub>Source report: `research/raw/B2-ai-tutoring-efficacy.md`</sub>

Two hundred and seventy-three studies in the ERIC database use a delayed post-test.
Two of them involve ChatGPT.

That single ratio is the most important fact about the efficacy literature, and it
is not a complaint about rigour. It is an *opportunity*, because a delayed
unassisted test is a routine, cheap, well-understood instrument that the field
already owns and has simply not pointed at this technology. The first team that
does will produce the most valuable result in the area, and they can do it with a
month of patience and a novel item set.

Here is what the record currently says, and what it does not.

---

## 1. The band

Start with the ceiling, because everything else is read against it.

Intensive, in-person, one-to-one and small-group human tutoring — the most
expensive and best-evidenced intervention in education — pools at **0.288 SD (SE
0.029)** across 96 randomised studies (Nickow, Oreopoulos & Quan, *AERJ* 2024,
funded by J-PAL North America). That is the number to hold.

Now the AI results, all immediate post-tests unless stated:

| Study | Effect | n | Duration | Delayed test? | Distal outcome? |
|---|---|---|---|---|---|
| **Sierra Leone**, Gemini Guided Learning (RCT-P) | **+0.258 SD** adjusted; **+0.216 SD unadjusted, n.s.** | 1,423 analysed, 48 classrooms | 8 weeks | No | Blind-scored, curriculum-aligned |
| **Nigeria**, Copilot after-school English (RCT) | +0.310 SD composite; **+0.206 SD on the school's own exam** | 759 analysed of 1,328 | 6 weeks | No | Yes |
| **Bastani et al.**, Turkey (PNAS) | Assisted practice +127%. **Unassisted exam: −17% unguarded, −0.004 guarded** (§2)| ~1,000 | 4 sessions | AI-removed, same session | No |
| **Kestin et al.**, Harvard physics | d ≈ 0.63 (to 1.3 ceiling-corrected) | 194 | **two ~1-hour lessons** | No | No |
| **Tutor CoPilot** (RCT-P) | +4 p.p. exit ticket | 900 tutors, 1,800 students | 2 months | No | **Yes — and null** |
| **Rori**, Ghana | 0.37 SD | ~1,000, **11 clusters** | 8 months | No | No |
| **LearnLM + Eedi**, UK | +5.5 p.p. on novel problems vs human tutors | **165** | not stated | No | No |
| Pre-LLM ITS (VanLehn; Ma et al.; Steenbergen-Hu) | d = 0.76; g = 0.32–0.57 | meta | — | — | — |
| **Human tutoring** (Nickow, 96 RCTs) | **0.288 SD** | meta | — | — | — |

**The good LLM trials land in the same band as pre-LLM intelligent tutoring systems
and as human tutors.** Sierra Leone 0.258, Nigeria 0.23–0.31, Rori 0.37, ITS
0.32–0.42, human tutoring 0.288. There is no order-of-magnitude jump. There may not
be a difference at all.

That is not a disappointing result. It is a *stable* one, and stability is what
makes a foundation. An effect that reproduces across four countries, three
languages and two technology generations is an effect you can design against.

---

## 2. Sierra Leone, read properly

The Sierra Leone trial is the best-designed study in the corpus and deserves to be
read at full resolution rather than through its headline. Two-arm cluster RCT,
classroom-level randomisation blocked by school × grade, 12 government junior
secondary schools, preregistered at AEA (AEARCTR-0016651). The design choice that
matters most: **both arms' teachers received the identical 5–6 hour training
before randomisation**, which removes the training confound that ruins most edtech
trials. Assessment was written and IRT-scored by Oxford MeasurEd, blind to arm.
Data collection, implementation and measurement sat in three separate
organisations.

That structure is the template. It should be the minimum bar the field asks of
anyone, including us.

Now the reanalysis, all of it from the report's own appendix tables:

| Finding | Value |
|---|---|
| Unadjusted ITT | **0.216 SD, SE 0.137 — not significant** |
| Baseline-adjusted (ANCOVA) | 0.258 SD, p = 0.029 |
| Treatment × baseline maths | **+0.195 SD per baseline SD, p = 0.002** |
| Grade 8 × treatment | **+0.429, p < 0.01** |
| Grade 7 main treatment coefficient | **−0.078, p < 0.05** |
| Treatment assignment predicting retention | +0.032, p < 0.05 (differential attrition) |
| Baseline imbalance | 0.167 SD favouring control |

Four things follow. **The headline exists only under covariate adjustment**, which
is a legitimate and preregistered choice made necessary by a real baseline
imbalance — but the raw arm difference is not distinguishable from zero, and the
adjusted CI's lower bound is 0.027. **The interaction is an order of magnitude more
statistically robust than the main effect**: at the fitted specification a student
one SD below the mean gains about 0.055 SD, which is nothing. **The effect is
essentially a Grade-8 effect**, with Grade 7's coefficient negative and significant
— a result that appears in no blog post about this trial. And the model changed
mid-trial, Gemini 2.5 Pro to 3.0 Pro at week six.

The credit here is substantial. DeepMind volunteered every one of those
numbers. The non-significant unadjusted estimate, the gap-widening interaction, the
mid-trial swap, the attrition flow, the preregistration deviation they did not
execute. That is more transparent than the norm. **The problem is not the report.
It is what happens to the report in the second-hand telling.**

Two further limits, both stated by the authors. The counterfactual is
business-as-usual, so +0.258 SD is the combined effect of tablets, a 2:1
driver/navigator pair protocol, a teacher-authored four-part lesson structure,
teacher-written starter prompts, chalkboard scaffolds, teacher professional
development, novelty, *and* Guided Learning's pedagogy. Their own playbook says
plainly that isolating arms would have required a sample they could not afford. And
because tablets were shared, **the 113,344 coded messages could not be linked to
any individual's test score**. The process metric (91.4% skill-seeking, 76.4%
scaffolding questions, 2.1% direct solutions) sits next to the outcome metric and
has never been shown to predict it.

---

## 3. The delayed unassisted test nobody ran

Here is the ERIC census, run 2026-07-27 against `api.ies.ed.gov/eric/`:

| Query | Records |
|---|---:|
| `"ChatGPT"` | 1,668 |
| `"ChatGPT" AND "learning outcomes"` | 95 |
| `"ChatGPT" AND "delayed post-test"` | **2** |
| `"ChatGPT" AND "retention test"` | **0** |
| `"ChatGPT" AND "transfer test"` | **0** |
| `"ChatGPT" AND "preregistered"` | **0** |
| *(control)* `"delayed post-test"`, any topic | **273** |

ERIC indexes abstracts only and lags preprints, so these are lower
bounds; the ratio is the quantity that matters, and the ratio is roughly 2% of
ChatGPT-plus-outcomes studies and 0.1% of all ChatGPT studies.

Why did nobody run one? The honest answers, in order of how often they appear in
the primary sources: partner schools grant access for a fixed window and reclaim it
(Bastani et al. say exactly this — "long-term outcomes … limitations imposed by our
partner school"); the intervention window and the publication window are the same
window; and a delayed test is the one measurement that can turn a positive paper
into a null one. None of these is a scientific reason. All of them are structural,
and all of them are fixable by whoever is willing to fund the fourth week.

What would such a test have shown? We have exactly one piece of evidence, and it is
the most important study in the corpus. **Bastani et al.** built AI-removal into the
design: four 90-minute sessions, assisted practice followed by a closed-book,
closed-laptop exam on conceptually matched problems.

| Outcome | GPT Base (unguarded) | GPT Tutor (guardrailed) |
|---|---|---|
| Assisted practice | +0.137 (SE 0.031) = **+48%** | +0.361 (SE 0.032) = **+127%** |
| Unassisted exam | **−0.054 (SE 0.022) = −17%, p < 0.05** (§2)| −0.004 (SE 0.013), n.s. |

Read the two columns against each other. The arm that performed **best** while
assisted is the arm whose unassisted coefficient is indistinguishable from zero.
The arm that performed second-best while assisted did *worse than students who
never had access at all*. GPT-4 gave correct answers on these problems 51% of the
time, and students used it as a crutch.

This survey has stated the consequence before and states it again without softening
it: **guardrails have been measured to remove harm, not to add benefit.** The
guardrailed coefficient is −0.004. Anyone selling restraint as a learning gain is
ahead of the evidence, including us.

A note on provenance, because the correction is on this project's record: the PNAS
notice attached to Bastani et al. is an affiliation erratum. It is not a correction
to the result. The −17% stands (§2).

---

## 4. Four results that never made a headline

Four nulls, none of which is in the headline of the paper that contains it.

Tutor CoPilot is the cleanest proximal/distal dissociation in the field. A
preregistered, independently funded RCT of 900 tutors, 1,800 Title I students and
4,136 sessions moved exit-ticket mastery by 4 percentage points (p < 0.01), 9 points
for students of the lowest-rated tutors. Verbatim from its limitations section:
"**we did not find statistically significant improvements in end-of-year math test
scores.**" The in-platform metric moved. The state test did not.

Lehmann, Cornelius & Sting is a preregistered, incentivised, replicated null.
Two lab experiments (107 and 69 subjects) plus a field study: "we find no effect of
LLMs on overall learning outcomes." Students who substituted LLM use for study
"increase the volume of topics they can learn about but decrease their
understanding of each topic," and the paper's body text is blunter than its
abstract: LLMs "harm the learning of students with less prior knowledge."

**Without a teacher in the loop, the meta-analytic effect is 0.077.** Gu & Yan
(2025, *JECR*, 19 studies) report g = 0.683 overall, decomposing to **g = 1.426
with teacher support and g = 0.077 without**. Every positive result in §2.1 that
survives scrutiny is a teacher-designed, teacher-supervised activity with an LLM as
one component. The measured entity is *teacher-plus-AI activity design*. **No study
in the corpus isolates the AI's contribution.**

And offering AI access reduced engagement. Nie et al. randomised GPT-4 access
across 5,831 students in 146 countries: "the advertisement of GPT-4 led to a
significant average decrease in exam participation." The positive effect for
adopters comes from selection and not from a randomised contrast, and peer review
made the authors retitle the paper to say so.

To that add the field's largest single correction. **The most-cited meta-analytic
estimate of ChatGPT's effect on learning, g = 0.867 across 51 studies, was retracted
in 2026** for "discrepancies in the meta-analysis"; the authors did not respond to
correspondence. It had accumulated over 250 citations. Anything downstream of
g = 0.867 is unsupported, and still circulating.

A smaller correction worth internalising as a habit: Nickow et al.'s human-tutoring
pooled estimate **fell from 0.37 SD in the 2020 working paper to 0.288 SD in the
2024 peer-reviewed version.** Discount every working-paper effect size accordingly,
including the ones in the table above.

---

## 5. What LearnLM measured, precisely

LearnLM deserves separate treatment because it is the most serious attempt anyone
has made to render pedagogy measurable, and because its famous numbers measure
something other than learning.

The programme's flagship evaluations (the "+31% over GPT-4o", the "73.2% overall
win rate") score pedagogical plausibility. The dependent variable
is a third-party expert's agreement with a statement about a transcript. Google
says so themselves, in R2's conclusion: "it is unclear how well the results
translate to improvements in learning outcomes." R3 asks the question outright: "do
these pedagogical capabilities translate to concretely better learning outcomes for
students?"

Two findings inside that programme are more useful than the win rates.

The rubric's reliability was reported once. R1 published Krippendorff's α per
dimension: overall **0.359**, and on three of nine tutoring moves
(*inspires interest* **0.066**, *monitors motivation* **0.023**, *identifies goal*
**0.031**), credentialed pedagogy experts agreed with each other at approximately
chance. Two of LearnLM's five principles rest substantially on constructs raters
cannot reliably identify in a transcript. R2 and R3 report no inter-rater statistic
at all. Publishing that α was the right thing to do; stopping was not.

And the learners disagreed with the experts. Twice, in two reports. The people
role-playing the conversation "indicated no substantial preference between LearnLM
and Gemini 1.5 Pro or between LearnLM and Claude 3.5 Sonnet." In R3, educators
interacting directly scored Gemini 2.5 Pro and ChatGPT-4o as tied; only the
independent transcript reviewers separated them. Google's reading is right — "what
students find immediately helpful often diverges from what is pedagogically sound,"
captured perfectly by one educator: **"As a lazy student, I'd have loved it. As a
tutor, not good at all!"** The reading a builder must also hold is that the win was
scored by the population that shares the rubric's theory, and the rubric has never
been validated against an outcome.

---

## 6. Three years against fifty

*You are holding a three-year-old technology to a standard the tutoring literature
took fifty years to meet. Effects in the 0.2–0.4 band, replicated across four
countries, on a technology that did not exist in 2022, is a remarkable starting
position — and the retention evidence will arrive.*

Most of that is correct, which is why this section leads with the band and not with
the gaps. But two things break the defence.

First, the instrument is not expensive or novel. Two hundred and seventy-three
ERIC records use it. It is four weeks of patience and a fresh item set — and item
generation is now the cheapest thing in the system. The field is not failing to
measure retention because retention is hard to measure.

Second, **the pre-LLM literature did meet the standard, and the comparisons that
count live there.** Roschelle et al.'s ASSISTments trial moved an end-of-year state
standardised test across 43 Maine schools, with the largest gains for low prior
achievers. It is the strongest distal-outcome edtech RCT in the corpus, and it
predates the LLMs entirely. Pane et al. ran Cognitive Tutor Algebra I across 147
schools for two years and found a null in year one that became +0.21 SD in year two.
Neither shape is visible in an eight-week trial, and every LLM RCT here except Rori is
eight weeks or shorter.

---

## 7. How we will report an effect size

- **Quote the band, not the ceiling.** 0.2–0.4 SD, the same band as ITS and human
  tutoring. Never cite g = 0.867; it is retracted. Never cite Bastani's +127%; it is
  a practice-session number.
- **Every claim we make gets a delayed, unassisted, novel-item test**, or it is
  reported as a performance result and labelled as one.
- **Report the unadjusted estimate next to the adjusted one.** Sierra Leone's
  0.216 (n.s.) belongs beside its 0.258 every time.
- **Treat gap-widening as the default expectation *for untargeted delivery*.**
  Three studies, three countries, three age groups, three tools, same direction:
  +0.195 SD per baseline SD, +0.151, and Lehmann's low-prior-knowledge harm. But it
  is not a law of the technology: across **eight targeted interventions examined in
  §27, none widened gaps and several sharply narrowed them.** Gap-widening is a
  property of *distribution without targeting*, which makes it a design failure we
  know how to avoid rather than a tax we must accept. Any trial we run stratifies on
  baseline attainment and powers the bottom stratum as a primary outcome.
- **Assume the teacher is the active ingredient until a factorial design says
  otherwise.** g = 0.077 without one.
- **Report inter-rater reliability every time, for every dimension.** If α on a
  rubric item is 0.066, that item is not measuring anything.
- **Link process to outcome or do not claim the process.** 91.4% skill-seeking is a
  number about conversations until someone regresses it on a test score.

The field's headline number was retracted, its best trial cannot isolate its own
intervention, and its most rigorous result is a harm. Read as a specification for
what to measure, that record is unusually clear, and it points at one cheap
unclaimed result: **a one-month delayed test on students who have already been
randomised.**


## 4. Fifteen Hundred Papers, Seven Trials — what the field measures instead of learning

<sub>Source report: `research/raw/E3-latest-sweep.md`</sub>

Earlier in this survey a small census turned up something odd: an exhaustive search
for papers on automatic slide generation returned 39 results, of which **zero
measured whether a human learned anything.** We flagged it as a local curiosity.

It is not local. We ran the census across the field.

---

## 1. The number

**2,907 arXiv papers across 20 education-AI subfields. At most 1.79% carry any
learning-outcome marker. Eight of the twenty subfields sit at exactly zero.**

The distribution is uneven, and the unevenness is informative. Split the subfields
by what they build:

| Cluster | Papers carrying a learning-outcome marker |
|---|---|
| **Generation** — items, slides, figures, explanations, courseware | **≤ 1.08%** |
| **Interaction** — tutoring dialogue, feedback, scaffolding | **≤ 3.48%** |

And the finding that should sting: **the pre-LLM intelligent-tutoring-systems
literature measures learning *more* than the LLM literature does.** The field got
better at building and worse at checking, in the same decade.

The peer-reviewed education literature gives the same shape from the other
direction. ERIC holds **1,565 records** on ChatGPT in education. **Seven are
randomised controlled trials.** Three of those seven are second-language learning.

So: fifteen hundred papers, seven trials, and four of them outside language
teaching.

> **Corrected 30 Jul 2026 (C-58).** This section said *four* were second-language
> learning. Read record by record, EJ1415077 is a randomised trial in a
> foundational chemistry course in a blended setting, and EJ1484052 is VR with
> embedded IoT tasks. The census was reproducible and the classification was not
> checked.

That is not a scandal and we are not going to write it as one. It is a phase. An
enormous generative capability arrived, and the field is still enumerating
what can be built. Enumeration is legitimate work. But it should be labelled as
enumeration, and a survey that reported "1,565 papers on AI tutoring" without the
denominator would be actively misleading.

---

## 2. A null published against interest

The most valuable single item in this sweep is a company publishing a result that
costs it something. Sal Khan, on the first Khanmigo:

> *"did not change student learning as much as many of us hoped it would."*

Khan Academy has more instrumented learner-hours than almost any organisation
alive, and it said the thing out loud. That deserves to be recorded as a
contribution, not a stumble.

The diagnosis is what makes it useful. The failure was not pedagogical. The
tutor's mechanism worked when it fired, and it only fired when a student
**recognised that they needed help and went to get it.** The metacognitive
prerequisite was the bottleneck. Knowing that you are confused, and acting on it,
is precisely the skill that struggling learners have least of.

The redesign puts the tutor inside the practice problem, where the student
already is, removing the need to self-diagnose before help can begin.

This is the most transferable design lesson in the sweep, and it generalises well
beyond one product:

> **Invocation is part of the intervention.** A tutor that must be summoned is a
> tutor that reaches the students who need it least. Measure the mechanism *and*
> the path to it.

---

## 3. Three results that fit together

A second null, from a controlled trial. Fütterer et al. (*Educational Psychology
Review*, April 2026, n = 371, Grades 7–9) found

> *"no statistically significant advantages of either intervention over the
> control condition… for effort, domain-specific knowledge, or elaboration-based
> strategy use."*

Read the control condition, because it is the whole finding: **the control was
plain ChatGPT.** Two carefully designed pedagogical interventions failed to beat
an unmodified general-purpose chatbot.

Now line it up with two results already in this survey:

| Study | Comparison | Result |
|---|---|---|
| Bastani | Guardrailed vs unguarded AI | Guardrails **removed harm** (−17% → −0.004 n.s.) (§2)|
| Fütterer | Pedagogical design vs **plain ChatGPT** | **No advantage** |
| Sierra Leone | Designed tutor vs **little instruction** | Benefit |

One reading fits all three, and it is not that pedagogical design is worthless:

> **The measured return on pedagogical design scales with how bad the counterfactual
> was.** Against an unguarded answer machine, design removes harm. Against a
> competent general-purpose chatbot in a well-resourced Western classroom, design
> has not yet demonstrated an advantage. Against scarce instruction, it produces
> benefit.

That is an uncomfortable finding for the premium-product end of the market and an
encouraging one for the reach argument: **returns are largest where instruction is
scarcest.** It also sets the bar for anyone claiming a pedagogical advance. The
control must be plain ChatGPT and never nothing.

---

## 4. Two audited numbers, and one that evaporated

Vendor copy is not evidence, but SEC filings are audited and carry liability.

Chegg, Q1 2026 10-Q: **total revenue −48% year over year; Academic Services
−57%.** The filing itself attributes this to AI Overviews and student adoption of
generative AI. That is a company stating under oath that the business of selling
homework answers is being dismantled.

Synthesis School, SEC Form C-AR: **revenue +6.5%, losses roughly halved, total
assets −53%**, 26 employees, filed alongside a **termination of
reporting**. Modest growth, shrinking balance sheet, and going dark.

And one number that dissolved on contact. MagicSchool's widely repeated **"28%
literacy improvement" is unattributable**: five candidate URLs return 404, and
the full 153-URL sitemap contains no research page at all. This is not weak
evidence; it is *no locatable source*. It should not be cited by anyone, and the
fact that it circulates is a small case study in how a `VENDOR` claim becomes a
"finding" through repetition.

---

## 5. What is genuinely newly possible

The sweep's good news is concrete, and it concerns sovereignty more than
capability.

**Gemma 4 is Apache-2.0 and ungated.** Weights can go to a school on a USB stick.
No API key, no account, no per-seat licence, no data leaving the building, no
vendor able to deprecate the model a district built its year around. For the
populations in §27 — the ones behind connectivity, language, and permission
barriers — that is a larger change than another point of benchmark accuracy.

And a genuinely maintained local stack now exists end to end: Kolibri for
offline content and progress, llama.cpp / Ollama for inference, sherpa-onnx
for speech. All actively maintained, all self-hostable.

---

## 6. The four gaps, stated as an invitation

Between that stack and a deployable school system there are four holes. We name
them because each is a tractable open-source project and not a research
problem.

1. No open full-duplex voice. Moshi's last release is 2024-09-22; Voxtral
   Realtime is turn-based ASR, not full duplex. Barge-in and overlap — the things
   that make speech feel like conversation — have no maintained open
   implementation.
2. No safety layer. Nothing in the open stack does age-appropriate filtering,
   crisis detection, or safeguarding escalation. Given that omission rather than
   harmful output is the dominant crisis failure mode, this is the gap with the
   sharpest consequences.
3. No SSO. Kolibri's OIDC plugins were **archived on 2026-07-11**. Without
   identity integration, nothing enters a school district.
4. No glue between an LMS and a model. Rosters, gradebooks, assignments,
   standards alignment — the unglamorous integration layer. **This is the highest-
   value unclaimed open project in the field**, and it needs no new research at
   all.

That last one deserves emphasis. Everything else in this survey is a question about
evidence. This is a question about somebody writing an adapter.

---

## 7. The regulatory correction, because it is days away

This sweep also caught a live error in our own §28, and the correction is
time-sensitive enough to repeat here.

The EU AI Act's Annex III education obligations were widely expected to apply
from 2 August 2026. **They were deferred to 2 December 2027** by Regulation (EU)
2026/1744 — the Digital Omnibus on AI, in force **27 July 2026**, verified against
the EUR-Lex primary text.

But Article 113's first paragraph is unamended and Chapter IV is not carved out.
**Article 50 — transparency, chatbot disclosure, synthetic-content marking — still
applies from 2 August 2026.** For a conversational tutor, that is the live deadline.

Two sources a careful person would check both return the wrong answer today:
`artificialintelligenceact.eu` is stamped *"last updated 1 August 2024"*, and the
Commission's own Digital Omnibus page still describes only the proposal. A claim
verified against a secondary source last week is wrong this week.

---

## 8. The reporting standard this census sets

- **Publish the denominator.** "1,565 papers" without "7 RCTs" is a misleading
  sentence, and we will not write it.
- **Treat invocation as part of the intervention.** A tutor that must be summoned
  reaches the learners who need it least. Instrument the path to help as well as
  the help itself.
- **The control is plain ChatGPT.** Any claim of pedagogical advantage is measured
  against a competent general-purpose chatbot, never against nothing.
- **Expect the return to scale inversely with the counterfactual.** Design a system
  for where instruction is scarce and be honest that the same system may show no
  advantage in a well-resourced classroom.
- **Never cite an unlocatable number.** If five URLs 404 and the sitemap has no
  research page, the number does not exist, however often it is repeated.
- **Re-verify regulatory dates against primary text**, every time, because the
  aggregators are eighteen months stale and the deadline moved four days ago.

Nothing in this census says the field is failing. It is early, it is measuring the
wrong thing while it gets its bearings, and the correction is cheap and entirely
within reach: run the delayed unassisted test, against a real control, and publish
the denominator. Seven trials is where a field starts, and there is no reason it
should be where this one stays.



---

# Part II · The system the evidence forces

*What follows from that evidence if you take it seriously: an architecture, a division of labour, and a selection policy — each constrained by a measurement rather than a preference.*


## 5. The JARVIS Inversion — an ambient tutor is not an ambient assistant


The target is an ambient, always-present, sees-what-you-see, remembers-everything
tutor. JARVIS is the right image and the wrong specification, and every design
decision in this document follows from the difference.

## 1. The inversion

**JARVIS assists an expert. A tutor must build one.**

Tony Stark already knows the physics. JARVIS's job is to *minimise* his cognitive
load: answer instantly, compute silently, never withhold, never quiz him. Every
one of those behaviours is correct for an expert operator and **wrong for a
learner**.

| JARVIS behaviour | Effect on an expert | Effect on a learner |
|---|---|---|
| Answers instantly | Removes friction | Destroys retrieval practice — the best-evidenced retention intervention |
| Never withholds | Maximises throughput | Produces dependence; the learner offloads instead of encoding |
| Explains fluently on demand | Efficient | **Fluency illusion** — feels understood, isn't retained |
| Agrees and complies | Correct for a tool | Sycophancy; blocks productive failure and error correction |
| Does the work in parallel | Force multiplier | Does the learning too |

So the pedagogical JARVIS is defined by a capability the fictional one never
needs: **the judgment to refuse.** Its highest-value act is deciding *not* to
answer — to ask instead, to wait, to let a struggle run, to withhold the formula
until the learner has tried.

This is not a softening of the vision. It is a harder engineering problem than
the original.

## 2. What JARVIS actually requires, decomposed

Seven capabilities, each independently assessable against 2026 reality.

| # | Capability | Status | Blocker |
|---|---|---|---|
| J1 | **Ambient / always-on** | ⛔ Blocked | Gemini Live: 15 min audio, **2 min with video**, ~10 min connection life. Escape hatch: `contextWindowCompression` + `sessionResumption` (2 h handles). OpenAI max session undocumented. |
| J2 | **Sees what you see** | ⚠️ Degraded | Video is **≤1 FPS**. Static artifacts (paper, code on screen) work. *Watching a process does not survive 1 FPS* — and process is exactly what the pivot rule needs. |
| J3 | **Points, draws, annotates** | ⛔ Absent | Neither Gemini Live nor OpenAI Realtime can point. Deixis must be rebuilt: function calling → your own canvas. **Largest unexploited design space in the stack.** |
| J4 | **Remembers everything** | ⛔ The core gap | Portfolio audit finding: *"The bottleneck is not generation — generation is solved to a startling degree. It is state."* |
| J5 | **Proactive, interrupts, volunteers** | ✅ Available | OpenAI Realtime **out-of-band responses** (`conversation: "none"`) is a silent side-channel — the model can evaluate "is this learner stuck?" without speaking. This is the proactivity primitive and it is under-used. |
| J6 | **Has judgment, pushes back** | ⛔ Trained against | RLHF optimises agreeableness. "Sir, I would not advise that" is exactly what current models will not say. See §4.4. |
| J7 | **Runs work in parallel** | ✅ Available | Agent village (G2): background probe generation, misconception analysis, next-session planning. |

Two of seven are available today. One is degraded. Four are blocked, and those
blockers are *architectural*. They will not be fixed by a better model.

## 3. Latency: the budget is spent before the model runs

Human conversational turn gaps are modally **100–200 ms**; 51–55% land under
200 ms (Levinson & Torreira 2015). Humans achieve this by *predicting* the end of
your sentence. Word encoding alone takes ~600 ms, so listening-then-responding
cannot produce it.

Default server VAD is **500 ms silence + 300 ms padding = 800 ms before
inference begins.** The budget is blown before the model is invoked. Moshi
demonstrates the alternative: 160 ms theoretical, ~200 ms practical, full duplex.

For an ADHD learner this is not a polish issue. An 800 ms dead gap after every
utterance is an attention leak on every turn.

## 4. The refusal engine is the pedagogy

Everything above is infrastructure. No vendor ships this part.

The tutor must continuously decide **answer / ask / wait / pivot / escalate**, and
default to *not answering*. Inputs it must weigh:

- Has the learner attempted? (no attempt ⇒ never answer)
- Is this struggle productive or is it failure? (**mode-dependent**; see H1.3, where
  the SELPA archetypes invert this toward explicit instruction)
- Is this a retrieval opportunity? (recently taught ⇒ ask, don't tell)
- Is frustration approaching the point of harm? (escalate, don't persist)
- Is the current *method* failing, versus the learner failing? (⇒ pivot)

The last one is the bidirectional loop (H1.2) and it is the difference between a
tutor and a search engine. Most AI tutors re-explain the same way with more
words. This one must change **approach** instead of volume, and know the
difference between "not yet" and "not this way."

Against this, RLHF-trained agreeableness is an active adversary. The refusal
engine has to be built *over* the model's disposition, not delegated to it.

## 5. What to build first

Ranked by (impact for the target learner) ÷ (blocker difficulty):

1. State (J4). Nothing else compounds without it. A single learner model every
   agent reads and writes; inspectable and correctable by learner and parent.
2. The refusal engine (§4.4). Pure logic over an existing model. No new capability
   required. Highest pedagogical yield per line of code.
3. Deixis (J3). A shared canvas the tutor can point at and annotate via tool
   calls. It removes working-memory load directly, and it is the highest-value
   accommodation in the archetype table.
4. Proactive probing (J5). Out-of-band evaluation feeding the CBM probe loop.
   Available now, nobody uses it.
5. Session continuity (J1). Compression + resumption to defeat the 2-minute
   video cap.
6. Process vision (J2). Blocked at 1 FPS upstream; work around it with event
   capture (keystrokes, edits, canvas strokes) rather than video.
7. The face. Last, and labelled as what it is: pedagogical agents measure
   **g ≈ 0.19–0.20**, and three 2024 field experiments improved affect
   (d = .85–1.01) while learning *did not move*. Build it for engagement — a real
   and necessary win for an ADHD learner — but do not claim it teaches.

## 6. The one-line spec

> An ambient tutor that sees the work, remembers everything, points at the thing,
> notices you are stuck before you say so, changes its approach when its approach
> is failing, and most of the time declines to give you the answer.

---

## 7. Addendum: Wan Streamer changes three of the seven blockers

*Added 2026-07-25 after direct source review. Supersedes the latency and avatar
analysis above where they conflict.*

Sources. Wan-Streamer v0.2, arXiv:2607.04443 (Huang et al., 5 Jul 2026);
Wan Streamer v0.3, https://wan-streamer.com/v0.3/ (16 Jul 2026). Local install
present at `~/wan-streamer`, though that directory is actually **StreamDiffusionV2**
(arXiv:2511.07399, MLSys 2026 Best Paper), a *different* real-time V2V system with
Blackwell support added 2026-05-17. Both are relevant; they are not the same
project.

**Measured figures (v0.2/v0.3):** 640×368 @ **25 FPS**, **~200 ms model-side
signal-to-signal latency**, ~550 ms total remote including 350 ms network.
Architecture: single-GPU *thinker* (perception) + multi-GPU *performer*
(Ulysses-style context parallelism). `MEASURED-BENCH`, author-reported.

### Revisions to §4.2 and §4.3

| | Previous finding | Revised |
|---|---|---|
| **Latency** | "Budget blown before the model runs" (800 ms default VAD) | **~200 ms model-side is inside the human turn-gap budget** (modal 100–200 ms; Levinson & Torreira). The 800 ms figure describes *default VAD configuration*, not the achievable floor. |
| **J2 — sees what you see** | Degraded, ≤1 FPS | Applies to Gemini Live / OpenAI Realtime. A dedicated real-time audio-visual stack operates at 25 FPS. |
| **J1 — ambient** | Blocked by 2-min video cap | Vendor-API constraint, not a physical one. A self-hosted stream has no such cap. |

### The v0.3 contribution: world / event-stream decomposition

v0.3 separates the world, which must stay coherent (scene, characters,
appearance, sound), from the event stream, which varies moment to moment
(speech, motion, camera movement, environmental change). *"Establish the world once,
follow the timeline, and learn what happens next."*

This is the sharpest architectural fit for tutoring in the entire survey:

- **The world is the lesson context** — a lab bench, a workshop, a circuit, a
  kitchen, a farm. Established once, persistent across the session.
- **The event stream is the teaching** — the tutor's speech, gesture, object
  manipulation, and attention shifts, time-aligned within that world.

It also addresses Genie 3's two disqualifying limits for education directly:
persistent world state (vs ~1 minute of visual memory) and legible on-screen text
(v0.2's stated goal is "readable details during real-time conversation").
One of v0.3's own demo categories is "instructional activity."

### What this does *not* fix

Physical correctness is unchanged. VideoPhy (39.6% best case) and VideoPhy-2
(22% on the hard subset) measure generated-video physics adherence, and nothing
in v0.2/v0.3 claims to improve it. **A generated world may be real-time,
persistent, legible, and still wrong about physics.** Photorealism makes such an
error more persuasive.

Therefore the A5 conclusion is narrowed rather than withdrawn:

> Generated pixel worlds remain unsuitable as the *authority* for physical law.
> They are now suitable as the *stage*, a persistent, legible, real-time
> environment in which a tutor grounded by verifiable code (G1 ladder) teaches.
> Keep the world generative; keep the physics symbolic.

### Revised build order (supersedes §4.5)

Deixis (J3) rises to first. In a persistent world at 25 FPS, "point at *this*"
becomes tractable in a way it never was over a 1 FPS still-frame channel, and it
is the highest-value accommodation in the H1 archetype table.

1. Deixis in a persistent world. The tutor indicates, annotates, manipulates.
2. State (J4). One learner model beneath it.
3. The refusal engine (§4.4), unchanged. Still the pedagogy.
4. Proactive probing (J5). Out-of-band evaluation feeding the CBM loop.
5. The face. Now cheap to render, still `g ≈ 0.19–0.20`. Build for engagement;
   do not claim it teaches.


## 6. The Compression — a week's understanding in an hour, and what that sentence can honestly mean

<sub>Source report: `research/raw/K1-compression.md`</sub>

The claim is that an AI tutor collapses a week of learning into an hour, and makes
polymaths of ordinary people. It deserves to be taken seriously rather than
deflected, so this section tries to establish the actual bound.

The answer is 10–40× on elapsed calendar time and 3–5× on engaged effort, with
one documented case at roughly 300×, and a hard floor of 1× on durability
and on procedural skill. The mechanism is not that anyone thinks faster. It is that
almost none of a week is spent learning.

---

## 1. Decompose the week

A calendar week of a university course is 9 nominal student hours inside 112
waking ones. That is the Carnegie arithmetic and it is already an 12× gap before
anyone opens a book.

Now go inside the 9. The Beginning Teacher Evaluation Study followed the cascade
from allocated time → engaged time → time at an appropriate success rate, and the
median case loses about 65%. Their arithmetic produces the single most useful
number in this section:

> The same nominal school day yields ~4 minutes or ~52 minutes of productive
> learning, depending on allocation × engagement × success rate. **A 13× spread,
> inside identical calendars.**

The encoding fraction is small and the headroom is enormous, which is what makes
the original claim plausible instead of silly.

**And here is the gap we could not close.** Two independent retrieval passes found
**no study anywhere that decomposes a study session into search, orientation,
practice, and stuck.** The proportions everyone in this field assumes are not
measured. We flag that as this survey's highest-value missing measurement rather
than fill it with a vendor figure. It would take one instrumented cohort and a
fortnight.

---

## 2. Learning is counted in opportunities

This is the finding that reorganises the question. Koedinger et al. (PNAS 2023),
1.3 million observations across 27 datasets:

| Quantity | Spread, 25th → 75th percentile |
|---|---|
| Learning **rate** — opportunities needed per knowledge component | 7.89 → 6.94 — **1.14×** |
| **Prior knowledge** — where you start | 13.13 → 3.66 — **3.6×** |

Read those two rows against each other. **People do not differ much in how fast they
learn. They differ enormously in where they begin** — and this was measured *within
students who had formally passed the prerequisites.*

And the paper is explicit about the variable everyone reaches for first:

> *"A time-based model, time-AFM, systematically provides poor predictive fit."*

Time does not predict learning. **Opportunities do.** Which means the question is not
"how do we make the hour denser" but "how many correctly-targeted attempts can we
put in front of this person, and are they starting from the right place."

Downstream corroboration: students in the bottom quintile of prerequisite knowledge
wheel-spin 50% of the time, against 10% for the top quintile. Half of a weak
learner's session is spent going nowhere, for a reason that was set before the
session started.

---

## 3. The good hour is already near the floor

There is exactly one randomised trial that measured both learning *and* time. Its
learners took a median 49 minutes against 60, and learned d ≈ 0.63 more.

But the detail that matters is buried: **there was no correlation between
time-on-task and score.**

That kills the obvious model. You do not compress by making the productive hour more
efficient. The productive hour is close to irreducible. **You compress the 111 hours
around it**: the search, the waiting, the scheduling, the re-reading, and above all
the time spent blocked on a prerequisite nobody diagnosed.

---

## 4. The speed records that already exist

The most extreme documented result predates all of this. Sherlock, an avionics
troubleshooting tutor, in the source's own words:

> **20–25 hours of tutor time ≈ four extra years of on-the-job experience.**

Roughly 300×, achieved by nothing more exotic than opportunity density: 34
problems in 20 hours, each targeted, each with feedback. Four years of a job
contains very few genuine troubleshooting opportunities and a great deal of
everything else.

Broader and duller: Kulik's synthesis of 51 studies found **39–88% learning-time
savings** for mastery-based approaches at equal or better outcomes.

Two things we will not claim. Digital Tutor's widely-quoted "d = 1.9–3.7" is
unverified; the documented language is only *"in excess of two standard
deviations"*, and its Phase 1 result used **human tutors for 14 of its 16 weeks.**

---

## 5. The counter-anchor, and it is severe

The Foreign Service Institute has spent seventy years removing every compressible
element from language training. Its programmes still require 552–2,200 hours.

Compression there is approximately 1×.

That is the boundary of this entire section. **Procedural and production skill does
not compress**, because the bottleneck is repetitions of the motor or productive act
and nothing can perform them on your behalf. Speaking, playing, operating, drawing,
surgery, sport — the hours are the mechanism and not overhead around it.

Two more nulls, and the second is our own thesis biting back:

- **Seamon (2004):** the intensive-format advantage is real immediately and **gone at
  three years.**
- **Whillier & Lystad:** the same contact hours compressed produced significantly
  worse grades (P = 0.001) — and higher satisfaction. The felt-learning trap,
  arriving exactly where a compression claim is most tempting to believe.

There is also no meta-analysis of intensive versus traditional formats. Every review
in the area is narrative, with no pooled effect size. The literature is thinner than
its confidence.

---

## 6. Durability does not compress — but it is nearly free

Retention is built by elapsed time between retrievals, and that cannot be
accelerated. A memory durable for a year needs gaps of 18–36 days. There is no
version of this where you finish on Tuesday.

But the cost of durability is routinely overstated, and one experiment settles it.
Rohrer and Taylor obtained their large four-week benefit from **the same ten
problems, merely split** across sessions instead of massed into one.

Same total effort. Same items. Different calendar.

The shape of the claim is therefore neither "everything compresses" nor "nothing
does". It is:

> **A week's understanding in an hour. A year's retention in six hours spread across
> two months.**

That is a *stronger* claim than the one it replaces, because it is specific enough to
plan against. The expensive resource it names is calendar patience, and effort is not
what runs short.

---

## 7. Polymathy, and why it is bounded by orientation

Scientists work in 3–4 topics across an entire career, and switching correlates
with lower citation impact at every career stage.

Why so few? Not learning rate, which varies by 1.14×. Not practice hours:
deliberate practice explains 4% of variance in education and **under 1% in
professions. The binding constraint is the one parameter that varies by 3.6×**:
where you start, which is to say the fixed cost of orientation in a new field.

Orientation is knowing what the field's real question is, which of its words mean
something different here, what a good question sounds like, which results are load-
bearing and which are decoration, and who to read. It takes months, it is almost
entirely search and social access, and **it is the part of expertise that has nothing
to do with intelligence.**

It is also the part an agent can collapse most completely — it is retrieval,
structuring, and diagnosis, none of which require the learner's own working memory.

What limits polymathy is not how many fields you can learn but how many times you can
afford to be a beginner. That price is what falls.

This is the strongest version of the claim in this section, and it is
`INFERENCE`, following from the measured parameters and not from a trial of
anyone becoming a polymath. Nobody has run that study. It is eminently runnable.

---

## 8. The number, with its conditions

**10–40× on elapsed calendar. 3–5× on engaged effort.**

Rising above 40×, documented once at ~300×, when the baseline is *informal
experience* rather than a structured course, because informal experience has the
worst opportunity density of any learning arrangement.

Falling to 1× for procedural and production domains, and 1× for durability.

Three conditions, and all three are load-bearing:

1. **Accurate diagnosis of the starting point.** The 3.6× lever is prior knowledge,
   and it only pays if measured — see §11, where the measurement costs 15–40 seconds.
2. **The learner actually attempts.** Unguarded assistance leaves learners **17%
   worse** on later unassisted work. Compression achieved by watching someone else
   solve it is not compression; it is substitution.
3. **A short retention horizon, or a spaced schedule.** Compress acquisition, then be
   patient. Those are different resources and conflating them is where the claim
   becomes false.

---

## 9. Rules for quoting a compression factor

- **Never quote a compression factor without saying which resource.** Calendar,
  engaged effort, and durability compress at wildly different rates, and a single
  number that does not name one is marketing.
- **Optimise opportunities, not minutes.** Time-based models of learning have
  systematically poor fit. Count attempts at the right difficulty.
- **Spend the compression budget on orientation and prerequisite repair.** Those are
  worth 3.6×. Speeding up the productive hour is not, because it is already near its
  floor.
- **Claim 1× on procedural skill**, out loud, every time. The FSI hours are real and
  no model shortens them.
- **Ship the session decomposition study.** Nobody has measured where a study hour
  actually goes. One instrumented cohort and a fortnight would close it.

Almost none of a week is spent learning. That, and not processing speed or talent or
effort, is what an agent takes back.


## 7. Pedagogy Has No Pytest — what an agent is, and the one thing it is missing

<sub>Source report: `research/raw/K2-agentic-frontier.md`</sub>

The complaint that prompts this section is a good one: given agentic AI, why is
everything in this survey so modest? Agents write software, run experiments, and
operate for hours unattended. Why does the tutoring chapter read like 2019?

The answer is a single sentence, and it orders every reliability result in agentic AI.

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

Sampling without a selector is noise. Execution without a test is a side effect.
Persistence without a schema is a transcript. Absence without a verifier is
unsupervised drift.

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
check is**. SciCode is not check-free; it has hand-written tests, and still lands at
4.6%. That is why the rule is stated as a *bound* and not an equality. A weak check
caps you low. A strong one does not guarantee you reach the bound; it only stops you
being capped below it.

**Coding agents work because `pytest` exists.**

Now place teaching on that table. It sits firmly in the second column, and the reason
is measured rather than asserted:

> Across **223 tutoring domains, no model beat chance at labelling an incorrect
> student action.**

**Scoped correctly, because an earlier draft was not.** TutorGym evaluated four
models (`claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`,
`gpt-4o-2024-08-06`, `deepseek-v2.5`) in what its authors call an *initial
evaluation*. That model set never appeared in this survey, and the result was
restated here as *"currently unverifiable"* and *"every architecture"*, which is
more than it supports.

The adjacent positive literature was never searched, either. ProcessBench
(arXiv:2412.06559) asks models to *"identify the earliest step that contains an
error"* in mathematical reasoning, and reports open models with critique capability
competitive with that same GPT-4o vintage. A shared task on mistake identification
reports macro-F1 in the low seventies across 50+ teams.

So the claim is narrower than the one we made, and more useful. **Step-error
identification in a model's own reasoning trace is not at chance. Diagnosing what a
*learner* believes from what they did is.** The distance between those two is the gap
this section is about: not a wall, but a specific unbuilt instrument.

Not "performed poorly." **Chance**, on that model set, on that benchmark. The
operation a tutor performs constantly (look at what a learner did and say what is
wrong with it) is currently unverifiable by the systems being sold to do it.

That is why this survey reads modest. It is not a failure of ambition. **Pedagogy has
no `pytest`, and every agentic capability is waiting on one.**

---

## 3. The field is optimising against two instruments that do not work

This one is structural, which is why it has persisted.

The leading agentic-education systems (DeepTutor, CogEvo-Edu, AgentSchool) are
**optimised against LLM-simulated students and scored by LLM-as-judge**.

Both instruments are measured, and both fail:

- Across seven models, simulated students show **near-zero misconception
  faithfulness**. They do not hold the belief they are role-playing.
- Selection by LLM judge measures −3.20pp. Selection by test measures +8.14pp. An
  eleven-point spread, in the wrong direction for the judge.

> **The field is tuning tutors against a student model that holds no beliefs, using a
> judge that is worse than not selecting at all.**

Fix nothing else and fix this, and the measured quality of everything downstream moves.

---

## 4. What is genuinely, measurably possible right now

The pessimism above is about one missing component, not about capability. Where a
check exists, the numbers are startling.

Sampling is a real multiplier. Coverage scales log-linearly across **four orders
of magnitude** of samples, and a *weak* model at 250 samples beat a *strong* model at
1: 56% against 43%. Compute spent on breadth substitutes for model quality,
provided you can select.

Structured disagreement makes non-experts better judges. Debate raised non-expert
human accuracy from 60% to 88%. Note what this is not: it is not agents agreeing
with each other more efficiently. It is a human adjudicating a genuine disagreement
and getting the right answer.

Literature synthesis is solved well enough to rely on. PaperQA2 matches or exceeds
subject-matter experts, with 70% of flagged contradictions validated. The "find me
the three papers that resolve my confusion" capability is real today.

**Explanatory animation renders at 93.8%.** The visual half of §22's argument has a
working pipeline.

**The horizon is doubling every ~129 days.** That is the length of task an agent can
complete unattended. Whatever the reliable autonomous unit is when you read this, it
is roughly twice that four months later.

---

## 5. Two priors this survey had wrong

Doroudi et al. (2019) is not a negative review. An earlier draft cited its
0-of-8 sub-cut on interdependent content and omitted the headline: **21 of 41 studies
(51%) significantly beat all baselines.** The authors' verbatim conclusion is *"over
half of the studies found that RL-induced policies significantly outperform
baselines."* And their qualifier is an argument *for* this document's architecture:
RL *"has been most successful in cases where it has been constrained with ideas and
theories from cognitive psychology and the learning sciences."* Corrected in §19 and
§11; logged as C-29.

The "Google rots your memory" result has failed replication twice (BF01 = 5.07).
It is one of the most-cited claims in every argument about AI and cognition, and it is
not standing.

---

## 6. The absence that is worth more than any capability

Two literatures exist. They have never met.

GEPA, DGM and AlphaEvolve are self-improvement optimisers, and they have spent three
years getting very good at optimising a system against a fitness signal. That signal
has been benchmark accuracy, every time.

Instructional-policy research closed the loop on real human retention with 2014
machinery, and got +16.5% semester retention in a middle-school course.

Six arXiv queries and ten ERIC queries confirm it: **zero optimiser-in-the-loop trials
on human learners.** Nobody has ever pointed a modern optimiser at a fitness function
made of delayed unassisted human retention.

That is not a hard research problem. It is two fields that do not read each other. No
other gap in this document is this large and this unclaimed.

---

## 7. The five things worth building, in order

**1 · A tutee that will not fold.** A misconception-faithful student model, certified
by a Selective-Flip-Score eval. Does it hold the wrong belief under pressure and
abandon it only on genuine disconfirmation? This unlocks learning-by-teaching, and its
*downstream accuracy* is the grounded selector everything else is missing. It is both
the highest-evidence technique and the missing instrument, which is why it is first.

**2 · Generate-and-select on the learner's own test, never on a judge.** The
eleven-point spread is already measured. The scaled version, an optimiser whose
fitness is human retention at delay, is §6.6's unclaimed prize.

**3 · A step-level verifier for student work.** Pedagogy's missing `pytest`. Currently
at chance, with a public testbed and decades of labelled intelligent-tutoring logs
already sitting there. Whoever builds this unblocks the other four.

**4 · An agent whose only job is enforcing the boring floor.** Retrieval, spacing,
expectancy-before-study, feedback attached to failed retrieval, delayed unassisted
testing. It composes the six largest effects in this survey, requires **no new
capability at all**, and is by some distance the most likely of the five to work.

**5 · Four different arbiters, and not four personas.** What varies is the *evidence*
and not the prompt: a symbolic checker, a numeric checker, a corpus, a human. The
disagreement between them, surfaced to the learner *as the lesson*, is the one use of
multi-agent structure the evidence supports.

The ordering matters. **The least sophisticated item on that list is the one most
likely to work**, and the most sophisticated is the one that unblocks the rest.

---

## 8. Rules for anyone building the loop

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

Everything in agentic AI works except the part this section is about. The sampling is
extraordinary, the execution is extraordinary, the persistence is a solved engineering
problem. The thing that decides whether any of it teaches anybody anything has not
been built. It is one component, it is buildable, and nobody has built it.


## 8. Enumerate, Don't Judge — the belief object, and how it routes around the verifier gap

<sub>Source report: `research/raw/V2-responsive-explanation.md`</sub>

Earlier sections establish a wall. Across **223 tutoring domains, four models tested
in an initial evaluation did not beat chance at labelling an incorrect student
action** (§7 carries the scope, and the adjacent step-error literature that is *not*
at chance). Since every agentic capability is bounded by the check it closes on, the
whole architecture appeared to be waiting on a model good enough to judge student
work.

It is not. The wall is an artifact of the question being asked.

**Every system in the field asks a model: *is this wrong, and why?*** That is an
open-ended judgement over an unbounded space, which is exactly what models are bad at
and exactly what the 223-domain result measures.

There is a different question to ask, and the answer to it is a lookup.

---

## 1. The belief object

A misconception is not a label with a strength attached. That is what every shipping
system stores, and it is why nothing can be done with it. Model a belief instead as an
**object with three methods**:

```
Belief {
  predict(item)         → distribution over responses
  discriminate(rival)   → an item that separates this belief from that one
  break(case_space)     → trace | SCOPE_LIMITED | EQUIVALENT | ⊥
}
```

Every other component of a responsive tutor falls out of those three.

- **`discriminate()` is the probe generator.** You do not author diagnostic items; you
  ask two candidate beliefs for the item on which they disagree.
- **`predict()` is what the explanation is compiled against**, and what a mid-stream
  revision re-evaluates.
- **`break()` is the run-it-forward move.** Instantiate the learner's own wrong rule
  and execute it until the world contradicts it.
- **Divergence between `predict()` and observed behaviour is the retirement
  criterion.** A belief that stops predicting is a belief the learner no longer holds.

---

## 2. Why this walks around the wall

Here is the whole argument in one line:

> **The belief object never asks whether an answer is wrong. It asks which of its
> enumerated beliefs predicted that answer**, an argmax over precomputed
> distributions.

Chance-level open-ended judgement becomes a **table lookup over a bounded set.** The
belief library *is* the verifier. Not a model that has learned to judge — a structure
that makes judging unnecessary.

And the consequence for latency is not incidental. A posterior update over **≤40
enumerated beliefs is closed-form Bayes**, which means no language model anywhere on
the real-time path. The 200 ms budget stops being aspirational.

This is the difference between waiting for a capability and designing so the capability
is not required.

---

## 3. Decay has been modelled backwards

A finding that falls out of taking beliefs seriously as objects, and it inverts standard
practice.

Every spaced-repetition and learner-model system decays belief strength toward zero.
For misconceptions this is **wrong in the case that matters most**. Cross-ontological
errors (a limit held as a process, an electron held as an orbiting particle) do
not decay. The Bohr-model hybrid population was unchanged across a full semester of
university chemistry.

What decays is our confidence that the learner still holds it.

So the parameter must not fall toward zero. The **credible interval widens toward the
population prior**, and a belief last seen six months ago returns as *probably still
there, poorly localised* instead of *probably gone*. Systems that decay misconception
strength are quietly deciding that untested errors have been repaired.

---

## 4. The explanation IR, and the compiler that refuses

An explanation is compiled and not written. Three layers:

| Layer | Holds | Checkable |
|---|---|---|
| **Claim graph** | The propositions and their dependencies | Fully |
| **Discourse plan** | Order, emphasis, what is named aloud | Structurally |
| **Surface bindings** | Words, marks, animation parameters | At the boundary |

The four fidelity invariants become compiler passes that block a render: a rung may
drop precision, but it may never falsify **ontology, causal sign, quantifier strength,
or uniqueness of mechanism.** Not review guidance. A build failure.

Two passes are worth naming because they come from measured results and not from
principle. One enforces that the misconception is named explicitly, from the finding
that a Refutation condition scoring d = 0.79 was the exposition script *verbatim
plus explicit statements of the wrong idea*, with the same order and nothing
rearranged. The other enforces referential-status ordering, from the result that
referential status and not persistence decides whether an added element helps or
harms.

---

## 5. Latency is a schema property

The naive framing treats mid-stream revision as a performance problem — make the model
faster. It is a type problem.

Of the available patch operations, **`annotate` is the only one that falsifies no
invariant.** Adding a label, a pointer, a highlight cannot make a true claim false. So
`annotate` is the only operation that may legally land inside 200 ms.

Everything else (substituting a claim, reordering, changing a rung) **must branch at a
beat boundary**, from a patch cache pre-verified during the previous beat. The system
does not race; it prepares.

That is a cleaner answer than optimisation, and the schema enforces it where
discipline would otherwise have to.

---

## 6. What the system may watch, and why the legal answer is the better one

Emotion inference in education is prohibited under EU AI Act Article 5(1)(f). Not
high-risk: banned. Gaze-based frustration detection is out.

The replacement is better on the merits. Legal triggers reduce to voluntary acts:
a committed answer, a deictic act (pointing, selecting, circling), a produced artifact.
Each is unambiguous, learner-initiated, and carries far more information than an
inferred affective state, which, on this survey's own evidence, would optimise the
felt axis rather than the real one.

One tempting signal is explicitly rejected: rewind and replay density, which was
measured null and opposite-signed. The obvious proxy for confusion is not one.

---

## 7. Deixis stops being a research problem

Pointing at the thing was earlier described as the cleanest greenfield, with a substrate
at 49% IoU fine-tuned against under 1% zero-shot.

That number is the cost of grounding references in images you did not author. Once
an explanation is compiled from an IR, every object in the scene has a **compile-time
identifier**, and pointing is exact by construction. The hard version of the problem
only exists for systems that generate pixels first and try to understand them
afterwards.

---

## 8. The hole, and the experiment nobody will want to run

`break()` cannot address ontological crossings. Running a wrong rule forward
requires the rule to have dynamics. "A limit is a process" has no dynamics to execute —
there is nothing to run until it contradicts itself. And that class is precisely the one
the literature shows to be most robust and least repairable by instruction.

So the strongest move in this architecture does not reach the strongest misconception.
Ontological repair needs a different mechanism, and this document does not have one.

And the falsifier that matters is not the obvious one. Comparing a responsive system
against a fixed explanation confounds targeting with timing. The arm that settles it is
A′: identical targeting, revision deferred to the end.

> If A ≈ A′, then mid-stream revision is theatre and the entire latency argument was
> decoration on a targeting result.

That is the experiment we owe, and it is the one least likely to be run by anyone
selling this.

---

## 9. The architecture's non-negotiables

- **Enumerate beliefs; never ask a model to judge.** The 223-domain result bounds
  open-ended judgement, not bounded lookup.
- **No language model on the real-time path.** Closed-form Bayes over a bounded belief
  set, or the latency claim is fiction.
- **Widen the interval; do not decay the strength.** An untested misconception is
  poorly localised, not repaired.
- **Fidelity invariants are compiler passes, and not review notes.** A render that
  would falsify ontology does not build.
- **Only `annotate` lands inside 200 ms.** Everything else branches at a prepared beat
  boundary.
- **Watch voluntary acts only.** Committed answers, deictic acts, produced artifacts.
  Not gaze, which is prohibited, and not replay density, which was measured null.
- **Run arm A′.** If deferred revision matches live revision, we were wrong about the
  interesting part.

The field is waiting for models to become good judges. It does not have to. A
capability gap can be walked around as well as waited out, and the structure that
makes judgement unnecessary is buildable now.


## 9. Ekalavya's Thumb — the system we are actually building


Ekalavya wanted to learn archery. Drona refused him — wrong caste. So he built a
clay statue of the teacher who rejected him, and taught himself, and became better
than the prince. Drona's response was to demand his right thumb.

That is the entire history of education in one story. Not a shortage of
talent. Not a shortage of desire. A shortage of *access*, followed by the system
protecting its hierarchy when someone routes around it.

We are building the thing that makes the statue answer back.

---

## 1. The Star Trek test

The Enterprise has a computer that knows everything and answers instantly. And
Starfleet Academy **still exists.** Cadets still train, still fail, still have
mentors, still take the Kobayashi Maru — a test designed to be unwinnable, because
its purpose is to reveal character rather than sample knowledge.

That is the whole design brief. **Infinite answers did not abolish learning; they
abolished the *scarcity of practice*.** The holodeck is not a machine that tells
you about warp fields. It is a machine that lets you be *inside* one, break it,
and be wrong in a place where being wrong is survivable and infinitely repeatable.

So the target is not a chatbot that knows things. It is:

> **A holodeck for any concept, a mentor who will not do it for you, and a
> Kobayashi Maru you cannot Google.**

---

## 2. The constraint is no longer scarcity. It is capability.

Most previous attempts at universal tutoring died on a scarcity argument. Bloom's
1984 paper came with a built-in obituary: one tutor per child was *correct and
unaffordable*, so the field spent forty years searching for "group-instruction
methods as effective as one-to-one tutoring."

Two sigma is not the number, and we should stop quoting it. VanLehn measured
human tutoring at **d = 0.79** and intelligent tutoring systems at **0.76**;
Nickow et al. pooled 96 randomised tutoring studies at **0.288 SD** in peer review. Kestin's Harvard AI-tutor RCT
landed at **d ≈ 0.63** (0.73–1.3 after the authors' own ceiling correction), in a
median 49 minutes against an *assumed* 60, and the first author built the tutor,
ran the analysis, and declared no funding. That is *inside the human tutoring
range*, which is the honest claim and still a remarkable one. Chasing 2σ
inflates the target several-fold and guarantees that everything real looks like a
failure.

And scarcity was not always the killer. **Direct Instruction won Project Follow
Through** — the largest educational experiment ever run — on basic skills,
cognitive skills *and* affective measures, with 328 studies, ~4,000 effects, all
positive, and no publication-bias signature. It costs about $20 a workbook. It was
sidelined anyway, over scripting and teacher autonomy. **Cost was never its
constraint; professional identity was.** An AI has no professional identity to
offend. That is an opportunity, and notably *not* an affordability argument.

**The shortage is ending on a curve. There is no price point to wait for.**
Inference cost per unit of capability has fallen by orders of magnitude per year
and continues to. A village of specialists costs **1.07–1.30× a single tutor**,
because cost tracks *turns × context* instead of agent count. Specialists read a
4 KB slice of the learner model, never the whole transcript. Whatever number you compute today
is wrong by next year in the same direction. Any design that treats attention as
scarce is designing for a world that is closing.

So stop asking what we can afford to give a child, and ask the harder question:
what would we give them if attention were free?

Not more of the same. Not a chatbot that answers faster. The things that were
*structurally impossible* under scarcity:

- A tutor that watches the whole process and not just the submitted answer,
  because no human can sit beside thirty children at once, every hour, for a decade.
- A mind that remembers everything, across years, and can tell you in March
  which misconception from October is still live.
- An adversary that generates a fresh, unGoogleable problem calibrated to the
  exact edge of what you know, on demand, forever.
- A student you teach, an agent that will be wrong on purpose and hold the
  error until you actually repair it.
- A crew of specialists, each narrow and each **certified against a published
  eval**, deliberating over one child.

Every one of those was unbuildable not because we lacked the idea but because we
lacked the attention to spend on it. That is the constraint that is lifting.

And the real-time layer is already here: 640×368 at 25 FPS with ~200 ms
model-side latency, inside the human conversational turn-gap, with a persistent
world and a separate event stream. The thing that was science fiction in 2023 runs
on a desk in 2026.

What remains hard is not the bill. It is state, refusal, deixis, and an agent that
can hold a wrong belief. Those are engineering problems, and they are the subject
of the rest of this document.

---

## 3. What the village actually is

Not one tutor. A crew.

| Role | What it does | Star Trek analogue |
|---|---|---|
| **The Mentor** | The only conversational role. Withholds. Asks. Waits. | Picard |
| **The Diagnostician** | Watches for the misconception behind the wrong answer | Crusher |
| **The Simulator** | Builds the world the concept lives inside — and it is *executable*, so it can prove the learner wrong without anyone asserting it | The Holodeck |
| **The Adversary** | Genuine, unannounced objection. Not role-play — role-played devil's advocates *backfire* | Q |
| **The Student** | The agent the learner teaches. It must be able to **stay wrong** | Data, learning to be human |
| **The Archivist** | The learner model. Everything, forever, learner-owned, on-device | The ship's computer |
| **The Connector** | Brokers contact with *actual humans*. Never simulates friendship | Guinan |

Seven roles here; the full registry is ten, and the number that actually governs
design is the **active set of 3–5 per learner-hour**. The economics would allow
about forty, the orchestration evidence allows three to five, and you design to the
smaller number. One shared learner model. No votes. A precedence ladder instead,
where executable ground truth wins outright and dissent is *recorded*, never
averaged away. And the crew must be genuinely heterogeneous: three independent benchmarks
find multi-agent debate does not reliably beat plain self-consistency, and one
finds a single well-prompted agent nearly matches the best discussion method.
Seven copies of the same model wearing hats is theatre. Different grounding,
different evidence, different authority is a crew.

---

## 4. The five things this system does that nothing else does

**1. It refuses.** Unguarded AI leaves learners **17% worse** once you take it
away (§2). The Mentor's highest-value act is declining to answer. It asks
instead, waits instead, lets a struggle run to the exact edge of productive and no
further.

**2. It pivots.** Not "re-explain louder." *Change method.* And on the right
clock: a fast loop that micro-scaffolds within an approach, a slow loop that
changes approach, because trend rules need weeks of data, and a tutor that
pivots after three wrong answers is fitting noise. **Measurement alone is inert:
the 1991 trial that gave teachers data changed nothing; the arm that told them
*what to change* moved achievement.**

**3. It can be taught.** The Student agent adopts the learner's model *including
its errors*, applies it visibly, and lets the world — a simulator, a test suite —
deliver the disconfirmation. Learning by teaching is **g = 0.56, robust at delay** (measured
with *human* tutees; the agent version is untested),
and essentially nobody has deployed it, because every commercial model is
incapable of staying wrong.

**4. It ladders.** One concept at three distinct altitudes. Three rungs beat two
(p=0.032); five did not beat three (p=0.738). The ladder is held as a **library
the learner enters at the right height**. It is not an itinerary anyone walks. Fidelity rule:
monotone refinement. A level may *drop* precision, formalism, mechanism-depth. It
may never falsify **ontology, causal sign, quantifier strength, or uniqueness of
mechanism**, because errors *across* ontological categories are the ones a full
semester of instruction does not shift. Entry is measured, never preferred:
preference moves d≈0.48 while knowledge moves zero.

**5. It grounds.** Derivations are checked, not asserted. Numerically, then
symbolically, then formally where it matters. Correctness lives in the verifier,
never in the model's manners.

---

## 5. The bet

Every effect size in the literature is a measurement of **systems that don't do
any of this.** The tutor measured at 0.2–0.4 SD answers freely, has no memory,
cannot see the work, cannot point, never pivots, and agrees with everything.

We call that *the floor with the brakes on*. The status of that phrase is worth
being exact about, because §40 is, and this section was not. **"Nobody has built
and measured the assembled system" is proven. "It would do better" is a hypothesis,
not a finding.** It is the project's central bet, it is stated as falsifiable in §40
with its concession conditions named in advance, and nothing in this survey
establishes it.

Nobody has built the constrained, grounded, pivoting, teachable, remembering
version and measured it. **The zero RCTs on learners with disabilities is not a
verdict on the idea. It is an empty chair.**

We are not waiting for permission from a literature that hasn't run the
experiment. We are building the thing and running it.

---

## 6. What we owe the evidence

Everything above is a *hypothesis*, and the survey's rigour is what makes it a
hypothesis rather than a pitch. The rules stay:

- Ship the **delayed, unassisted** test. The field has run essentially none.
  ERIC returns **0** for "retention test" and **0** for "transfer test." Ours is
  the primary outcome and not an appendix.
- **Watch for gap-widening, and know that it is a property of *delivery* and not
  of technology.** Untargeted deployment reliably helps strong learners more (Sierra
  Leone loaded at +0.195 SD per SD of baseline). But across eight *targeted*
  interventions, none widened gaps and several sharply narrowed them.
  Gap-widening is therefore a design failure we can avoid and not a law we must
  accept. If ours widens gaps, it has failed, whatever the mean says.
- **The Null-Learner Test** on every metric: simulate an agent maximising it while
  teaching nothing (§36). If the metric can't tell, it's the wrong metric.
- Publish the nulls. Especially ours.

---

## 7. Read the ending again

The myth is usually told as a story about access, and that half is right: Droṇa
refused him, so he built a clay image and trained against it anyway. AI removes
both of those barriers permanently: the teacher's veto and **the requirement
of the teacher's consent**. No prerequisite lock. No "you're not ready yet." No
one deciding in advance who is allowed to be taught.

But the thumb is taken after he succeeds. Not for learning badly — for
learning *well*, and without authorisation. The veto that mattered was never the
teacher's. It was the guild's, and it acted at the moment of recognition.

So any claim that AI democratises learning is telling the true half and stopping
one page early. Attention becomes free; credentialing does not. A system that
teaches a child brilliantly and then hands them nothing the world will accept has
reproduced the story exactly, in a nicer voice.

That is why the certification requirement in this document points *both* ways.
Every agent must pass a published eval, and so must every claim the system makes
about a learner. Portable, inspectable, contestable, owned by the child.

Ekalavya lost his thumb so the hierarchy could keep its best archer at the top.

Nobody's thumb, ever again — and this time, the record travels with them.


## 10. The Village — what makes a crew of agents a crew

<sub>Source report: `research/raw/G2-agent-village.md`</sub>

One hundred and sixty-two personas, across six relationship types and eight
expertise domains, evaluated on 2,410 factual questions across four model
families. The finding, verbatim:

> "adding personas in system prompts does not improve model performance across a
> range of questions compared to the control setting where no persona is added."

Worse: "the effect of each persona can be largely random," and automatically
selecting the optimal persona performed no better than picking one at random.

So `"You are a world-class expert physics tutor with 20 years of experience"` is a
**null intervention on accuracy.** It changes register. It does not change what the
model knows or gets right. Any architecture whose expert agents differ only by
system prompt has built a set of identically-capable agents wearing different
costumes.

This section is about what a village is if it is not that. The answer turns out to
be genuinely useful, and it has almost nothing to do with how many agents you run.

---

## 1. What becomes possible

Start with the thing that only a decomposed system can do.

A monolithic tutor can be *asked* to respect prerequisites, to refuse the answer,
to pivot when the evidence says pivot. A village can be *built* so that the answer
is not available to the conversational agent until a verifier has passed it and
the planner has cleared the prerequisite. The difference is measurable:

> Chen et al. (2026) measured a Reward Hacking Severity Index of **0.317** under an
> unconstrained multi-objective reward, and **0.102** under a constrained
> architecture combining prerequisite enforcement and minimum cognitive demand —
> roughly a 3× reduction. Ablation showed behavioural safety was the most
> influential layer. Simulation: 120 sessions, 18,000 interactions.

**Pedagogical safety enforced by construction beats pedagogical safety filtered
after the fact.** That is the entire argument for the village. It is an argument
about *interfaces*; intelligence has nothing to do with it. Every constraint this
survey has landed on (the refusal engine, the IEP prohibition, the ban on emotion
inference, "produces evidence, never grades") becomes a property of a tool schema
rather than a sentence in a prompt that a sufficiently persuasive fourteen-year-old
can talk around.

The scope of the claim, stated narrowly: this section does **not** assert that a village
teaches better than a single tutor. Nobody has run that trial. It asserts that
given a system with multiple capabilities, the village decomposition is more
auditable and more falsifiable than a monolith, and is the only shape in which the
accessibility and safeguarding constraints can be enforced rather than requested.

---

## 2. Certified means it passed an eval

If persona prompting is null, "certified expert agent" needs a definition that
survives. It is this: **certified means it passed a stated, published, held-out
eval, with the eval's own validity labelled.**

The complication is that in education, nearly every eval is a proxy. Nine 2026
pedagogy benchmarks fall into three families: LLM-judge rubrics (circular),
human-expert dialogue-quality ratings (which rate the plausibility of pedagogical
*form* while saying nothing about effect), and risk rubrics (which measure the
absence of bad and never the presence of good). Benchmark pedagogy scores and
problem-solving scores correlate
at **r = 0.421**.

So certification is a ladder, and only the top rung is certification in any strong
sense.

| Tier | Establishes | Method | Status |
|---|---|---|---|
| **C0** Conformance | It runs, it is reachable, it is accessible | **WCAG 2.1 AA** (the standard ADA Title II actually incorporates), keyboard-only, screen reader, latency budget | Real, mechanical, binary |
| **C1** Correctness under adversarial probe | It is right and stays right when attacked | Executable check (CAS, unit test, proof checker) + red-team suite | **Real.** The only tier with non-circular ground truth |
| **C2** Pedagogical form | It behaves like teaching looks | LLM-judge or expert rubric | **Proxy. Circular. Label it `PROXY` wherever reported** |
| **C3** Learning outcome | A human who did not know now knows, 30 days later, on novel items | Growth slope on a sampled panel | **The only real certification.** Nobody ships it |

The rule: an agent may be **deployed** at C0 + C1. It may be **described as
certified** only at C3. Everything between is labelled as what it is.

C1 does the work, because it is the only tier where the system generates
its own ground truth. Two C1 suites already exist; adopt them instead of
reinventing them. The first is answer-leakage robustness under adversarial students:
six attack families, evaluated across model families and a multi-agent design. Its
methodological sting is the useful part: *in-context* adversarial student agents
"often fail to carry out effective attacks," so the authors had to **fine-tune** a
jailbreaking student. **A tutor that passes a prompted red team has not been
tested.** The second is the RHSI above, which applies to any agent optimised
against a proxy — which is every agent that touches sequencing, difficulty, or
engagement.

The unit of certification is a role card: a YAML object declaring what the role
may assert, what it may *not* assert, which layers of the learner model it reads
and writes, its grounding tier, and its scores at each certification tier. Three
properties of that card matter more than its contents. `may_not_assert` is enforced
at the tool surface: the diagnostician's schema physically contains no
`write_diagnosis` action. The grounding tier is a permission and never an aspiration,
so an L2 agent asserting an L3 claim is a defect catchable in CI. And **C3 is allowed
to say `NOT_ESTABLISHED`**, which is the state of almost every role today. A
card that claims C3 without a panel is falsifiable, and therefore checkable.

---

## 3. The heterogeneity constraint

The finding that most constrains the design is a negative one.

The intuitive village is a room of agents arguing until the truth emerges. Three
benchmarks say that is not what happens.

| Result | Finding |
|---|---|
| Smit et al., *Should we be going MAD?* | "multi-agent debating systems, in their current form, **do not reliably outperform** other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths" |
| Wang et al., *Rethinking the Bounds of LLM Reasoning* | "a **single-agent LLM with strong prompts** can achieve almost the same performance as the best existing discussion approach on a wide range of reasoning tasks and backbone LLMs" — discussion won only when the prompt contained no demonstration |
| Becker et al., *Stay Focused: Problem Drift in Multi-Agent Debate* | Debate **drifts away from the initial problem** over turns, degrading performance on long reasoning chains |

Du et al. (2023) is the positive result, and the one usually cited. It is one
result against three.

The field's own diagnosis of why is the part worth carrying: subsequent work
attacks the problem by *breaking homogeneity*. Sparse communication topologies
help, and one 2026 system is named for the goal explicitly. **Two instances of the
same model are not independent minds. They share a prior, a training set, and a
failure mode.** Debate between them is closer to self-consistency sampling than to
argument, which is what the benchmarks report.

And model diversity is not a free fix either. Self-MoA found that aggregating
outputs from a *single top-performing* model beats mixing different models (+6.6%
on AlpacaEval 2.0, +3.8% average across MMLU/CRUX/MATH) because "the MoA
performance is rather sensitive to the quality, and mixing different LLMs often
lowers the average quality of the models."

Read those together and the naive village is in serious trouble. **Persona
diversity buys no accuracy. Model diversity can cost it. Debate does not reliably
beat asking once, well.**

A contested finding, stated as contested. An earlier section of this project
cited *Diversity of Thought Elicits Stronger Reasoning Capabilities in Multi-Agent
Debate Frameworks* (2024), in which a set of medium-capacity models beat GPT-4 on
GSM-8K after four rounds — "heterogeneity beats raw capability." Self-MoA finds the
opposite in the aggregation setting. The reconcilable reading is that heterogeneity
helps when the mechanism is *adversarial* (debate reopens the search) and hurts when
the mechanism is *aggregative* (a weak proposer dilutes a strong one). That reading
is consistent with the arbitration rule below, which permits debate and forbids
synthesis. Nothing demonstrates it, and this survey publishes it as unresolved.

---

## 4. Precedence, not consensus

Disagreement inside the village is resolved by a strict ladder. Each tier is tried
in order; the first tier that can resolve the conflict does, and lower tiers are
never consulted.

| Tier | Mechanism | Rule |
|---|---|---|
| **T0** | **Executable ground truth** | CAS, unit test, proof checker, cited primary source. **The check wins. No agent votes.** Costs zero model calls, because it is code |
| **T1** | **Scope precedence** | The role of record for this claim type wins outright. Others **file dissent**, never overwrite |
| **T2** | **Named judge, selection only** | Different model family from every proposer. Returns one whole answer, unmodified. Calibration published |
| **T3** | **Learner as judge** | Both sides surfaced, learner adjudicates. Only over T0-verified answer sets. Never over facts |
| **T4** | **Escalate to a human** | After two unresolved rounds, or on any conflict touching a hard boundary |

**T0 carries the load.** It is also the least glamorous tier in the ladder. Most
disagreements in a learning system are about facts, derivations and code, and are
therefore decidable. A computer algebra system settles whether the integral is
right. A unit test settles whether the program works. The grounding ladder from the
next section does double duty here as an arbitration mechanism.

**T1's dissent record is the direct architectural answer to the voting problem.** A
correct minority answer that is voted away is unrecoverable. A correct minority
answer appended to the evidence log with `confidence: inferred` and full attribution
is recoverable — by a later probe, by a human reviewer, by an offline audit.
Dissent is cheap to store and catastrophic to discard.

**T3 is where the architecture earns its keep pedagogically.** It rests on the one
result in the multi-agent literature whose subject is the *learner*.
Khan, Hughes, Valentine et al. (2024): two expert models argue opposing
answers, and a non-expert judges. Non-expert models went from 48% to **76%**. Human
judges went from 60% to **88%**, a 28-point gain. Optimising the debaters for
persuasiveness *improved* non-expert truth-identification.

The reading this survey adopts: the learner-as-judge of two arguing agents is a
better epistemic position than the learner-as-recipient of one confident agent, by
28 points in humans.

Three bounds on it, because it is easy to get wrong. It runs only over answer sets
already verified at T0, because staging a debate where one side is factually wrong is
teaching a misconception with production values. It never runs on safety,
safeguarding, or accessibility; those escalate. And **it inverts for the learners
this project designs for first**: for a working-memory-limited learner, holding two
competing arguments in mind *is* the load, and discovery-shaped instruction is among
the clearest documented harms for that population. T3 is gated on the learner
model's guidance policy and never offered by default.

And the caveat, which is not small: what Khan et al. measured was **in-the-moment
adjudication accuracy**. Nobody has shown that judging debates transfers to
independent reasoning. It is a design bet with a strong prior.

---

## 5. Why no votes

Two absolute prohibitions, and the evidence behind each.

No majority voting anywhere, on anything. Not as a tie-break, not as a
confidence estimate, not as a sanity check. This project's earlier research found
that majority voting discards a correct minority answer roughly one time in four.
That figure is project-internal and not externally verified, so it is
reported here as such and never laundered into a citation. The mechanism is not in
dispute: voting is a popularity estimator, and correctness and popularity come apart
precisely on the hard items, which are the items that matter. In a learning system,
the discarded correct answer is often the one that would have diagnosed the
misconception.

No synthesis of conflicting substantive claims. Prose may be merged. *Claims*
may not. This project measured judge-based selection at 0.810 against synthesis at
0.179, again **project-internal**, again flagged. The externally verified
corroboration is Self-MoA: aggregation is sensitive to proposer quality, and mixing
degrades it. Synthesis of a right answer and a wrong answer is a wrong answer with
better prose, and fluent-and-wrong is the single most damaging output a tutor can
produce.

Two further constraints on the T2 judge, both externally grounded. It must be a
different model family from every proposer, because Panickssery, Bowman & Feng
(2024) showed LLM evaluators recognise their own generations, and fine-tuning
reveals a linear correlation between self-recognition capability and the strength of
self-preference bias. And it must **publish a selection accuracy on a held-out
disagreement set**, refreshed per model version — an uncalibrated judge is an
unlabelled coin. It is never invoked on novelty, creativity, insight, or "which
explanation is better," which are the dimensions where judge reliability is
worst.

One vendor datapoint, labelled and not restated as a finding: Anthropic's own
current model guidance says not to use subagents for review, verification, or
double-checking ("verification belongs in your main agent loop"), and that
instructions telling the model to verify now cause *over*-verification. `VENDOR`.
The direction of travel is what is notable: the field's own tooling guidance is
moving away from verifier-as-agent and toward verification-as-mechanism, which is
where T0 already sits.

---

## 6. What the multi-agent literature has not measured

Coordination failure is the dominant failure mode, and it has been catalogued. MAST
(Cemri et al., 2025) derives **14 unique failure modes** from 150 traces, validated
on **1,600+ annotated traces** across 7 popular multi-agent frameworks, with
inter-annotator κ = 0.88. Three categories: system design, inter-agent misalignment,
task verification. The paper's framing sentence is the one to keep: *"Despite
enthusiasm for Multi-Agent LLM Systems, their performance gains on popular
benchmarks are often minimal."* Two of the three categories are arbitration
problems, which is the strongest available argument that arbitration should be a
named, designed, tested component; emergence will not supply it.

Some of the multi-agent gain may be nothing but more compute. On BrowseComp,
"token usage by itself explains 80% of the variance" in performance (`VENDOR`,
Anthropic engineering; not restated as a finding). If that generalises even
partially, the specialisation thesis is in question. **Any claim that role
specialisation helps must be tested against a token-matched single-agent baseline,
and no published education multi-agent system has done this.** It should be the
first ablation in any village evaluation, including ours.

And the education multi-agent literature is uniformly demo-grade. Eight systems
surveyed: IntelliCode (six agents over a centralised versioned learner state,
validated on *simulated* learners); SimClass (a multi-agent classroom in two real
courses, evaluated with Flanders interaction analysis and Community of Inquiry, never
on learning gains); a four-agent XR authoring framework (teacher-facing prototype);
ParLD (state-prediction accuracy); FairTutor (its own C2-tier benchmark). One
controlled experiment exists, on 65 pre-service teachers, with a self-reported
outcome.

> **Not one measures a delayed, novel-item, human learning outcome against a
> single-agent control.**

Combined with the absence of any measured evidence that multi-agent AI tutoring
helps learners with disabilities — the 2026 state of the art in that area is a paper
whose own abstract says the research is absent, evaluated on 690 synthetic dialogues
scored by an LLM judge — the position this survey takes is that the village is an
architecture with good mechanical properties and no outcome evidence. Say that as a
finding; do not bury it as a limitation.

---

## 7. What makes a crew a crew

Not the count. Three structural properties.

One shared state, held as a database row and not as a conversation. This
matters because the strongest counter-argument to the whole design is Anthropic's
own guidance: *"domains that require all agents to share the same context or involve
many dependencies between agents are not a good fit for multi-agent systems."*
`VENDOR`. The answer is that shared *context* and shared *state* are different
objects:

| | Shared **context** (the anti-pattern) | Shared **state** (the village) |
|---|---|---|
| Object | The full conversational transcript | A structured, typed, versioned learner model |
| Size | Grows without bound with every turn | Bounded; a per-session slice is single-digit KB |
| Coupling | Every agent must read everything to act | Each agent reads a declared slice |
| Conflict | Implicit, unresolvable, invisible | Explicit, typed, arbitrated by the ladder |

A specialist that reads a four-thousand-token state slice and emits a structured
record is not exploring; it is computing over state. Build the same village by
handing every agent the transcript and Anthropic's warning applies exactly.

**A write contract, of which the important half is that the state writer is not a
model.** Evidence is append-only and many-writer: any agent may append an immutable,
attributed, confidence-tagged record, so eight agents can observe concurrently
without corrupting what another observed, and dissent is just an append. Derived
state (memory strength, belief about mastery) is **single-writer, and the writer
is arithmetic**: a declared memory model and a declared knowledge-tracing model run
over the evidence log. No model writes a mastery estimate. That preserves the
guarantee that every derived number regenerates from the evidence alone, which is
what makes a disputed number traceable by a parent or a learner. And it is not a
sacrifice: a 21-parameter memory model and a ~34-feature logistic model sit at the
accuracy frontier for this task.

One voice. Exactly one role is conversational. Every other role's output reaches
the learner through it, or not at all. This is not a UX preference; it is the fix
for MAST's inter-agent-misalignment category. A learner who receives two different
accounts of what they know has been given a worse model of themselves than they
started with. It is also an accessibility requirement: background agents must be off
the conversational critical path by construction, because a village that adds a
round-trip to the learner's turn has failed the accessibility gate regardless of how
good its pedagogy is.

The roster that falls out is a registry of ten roles: tutor (the only voice),
diagnostician, curriculum planner, assessor, librarian, verifier, adversary,
peer/protégé, safeguarding monitor, connector, plus a scribe that is not an agent
at all. But the roster is not the crew. **The active set for any given learner-hour
is three to five**, selected by the planner from the learner model. A learner in a
stable mastery loop needs tutor, assessor, scribe. A learner who has just tripped a
pivot rule needs tutor, diagnostician, planner, verifier. Nobody needs all ten at
once, and running all ten at once is precisely the failure MAST catalogues.

Note what is absent, and why. No "friend." No "motivator." No "engagement
agent." No emotion detector. Each was considered and each is excluded by a named
finding: relatedness is the one self-determination need an AI cannot supply, because
regard that is unconditional and costless by construction cannot underwrite a
commitment; emotion inference in education is prohibited under EU AI Act Art.
5(1)(f). In place of a friend there is a connector, whose job is matchmaking and
scheduling — surfacing a real person who will notice a missed week.

---

## 8. What we will build into the village, and what we refuse

- **No agent is "certified" by its prompt.** 162 personas, 2,410 questions, no
  accuracy gain. Certification is a published, held-out eval, at a labelled tier.
- **Deploy at C0+C1. Claim certification only at C3.** Label C2 as `PROXY` every
  time it is reported.
- **Precedence, never consensus.** T0 executes, T1 defers with recorded dissent, T2
  selects without merging, T3 hands it to the learner, T4 escalates.
- **No majority vote and no claim-level synthesis anywhere in the resolution path.**
  Both prohibitions rest partly on project-internal figures, and this survey says so.
- **Debate must be architected for genuine disagreement or not called debate.**
  Three benchmarks say homogeneous debate does not reliably beat asking once, well.
- **Share state, never context.** A typed row per role, not a transcript per agent.
- **The state writer is arithmetic.** Every derived number regenerates from the
  evidence log alone, or the number is not shippable.
- **One conversational voice, three to five active roles.** The economics would
  permit many more; the coordination evidence does not.
- **Our first ablation is a token-matched single-agent baseline.** Until that runs,
  every claim we make for the village is a claim about auditability and never about
  teaching.

Nobody has shown that a village teaches better than a single tutor. What the
decomposition buys is a shape: a refusal that can be enforced instead of requested, a
wrong answer caught by a program instead of by a vote, a disputed number traceable to
the evidence that produced it. **Those are engineering guarantees, and this section
claims those and nothing more.**


## 11. The One Interaction That Survived — personalisation as a measurement problem

<sub>Source report: `research/raw/J1-personalisation-engine.md`</sub>

Every section before this one asks *which techniques work*. This one asks the
harder question, and the one everybody actually wants answered: **for this learner,
on this concept, at this moment, which technique fires?**

The answer is not an algorithm. It is a fifteen-second measurement that was
impractical until about eighteen months ago.

---

## 1. Start with the failure, because it is fifty years long

Personalisation has a research programme behind it and the programme mostly
failed. Anyone building in this space needs to know that before anything else,
and almost nobody says it.

Cronbach and Snow spent two decades hunting **aptitude–treatment interactions**,
the idea that different learners need different instruction, and that you can
predict which from measurable traits. Here is Cronbach's 1975 summary, in his own
words:

> *"The interactions did not turn out as we had anticipated."*

On the direct ancestor of every modality-matching claim ever sold — high spatial
ability paired with diagrams:

> *"No interaction of this sort was found, in our shop or elsewhere."*

On the programme's *best* results, the ones that did reach significance:

> *"Strangely inconsistent from year to year and from course to course."*

And the structural warning, which is the sentence anyone proposing a
personalisation engine should have to write out by hand first:

> *"Once we attend to interactions, we enter a hall of mirrors that extends to
> infinity."* … *"Generalizations decay."*

Fifty years of looking. **Exactly one interaction survived**, in two forms that
turn out to be the same law.

There is a boundary here that §1 forces us to draw, and we would rather not.
Noetel's meta-meta-analysis found that **prior knowledge did not consistently
moderate multimedia design effects (p = 0.14)**. That is in open tension with
everything below. The honest reading, adopted here rather than argued away: the
reversal is well established for **assistance and guidance** manipulations such as
worked examples, scaffolding and explicit instruction, and is **not reliably
detectable across the broad multimedia-design corpus**. So the survivor is
narrower than "prior knowledge moderates instruction." It is *prior knowledge
moderates how much help to give*. That is still the axis this section builds on,
and it is one claim smaller than it was.

---

## 2. The survivor

Snow's *ability × information-processing load*, and **expertise reversal**:
**d = +0.505** for novices, **d = −0.428** for experts. Chen, Kalyuga and Sweller
show both reduce to element interactivity — how many things a learner must hold
simultaneously to make sense of the material.

Three properties of this interaction decide the entire architecture:

- It is per-topic, not per-person. The same learner is a novice in one chapter
  and an expert in the next. Any system that stores "this student needs
  scaffolding" as a trait has already made the mistake Cronbach warned about.
- It is asymmetric. Under-assisting a novice is a missed gain. Over-assisting
  an expert is an *active harm* at −0.428.
- It is heterogeneous. I² ≈ 90%. It is a real law with noisy boundaries and
  nothing like a dial.

Everything else on the personalisation menu is either debunked or unevidenced:
learning styles, modality preference, personality type, demographic tailoring. The
table of what is left is very short:

| Dimension | Status |
|---|---|
| Prior knowledge / expertise on **this** concept | **EVIDENCED** — the one survivor |
| Working-memory load imposed by **this** material | **EVIDENCED** — same law, other face |
| Pace and dosage | **PLAUSIBLE** — evidenced for mastery, weak for micro-adaptation |
| Interest and context of examples | **PLAUSIBLE** — small, real, easily oversold |
| Learning styles / modality matching | **DEBUNKED** |
| Personality or demographic tailoring | **DEBUNKED or unevidenced** |
| Stated preference for difficulty | **ANTI-SIGNAL** — preference moves d ≈ 0.48 while knowledge moves 0 (§2)|

---

## 3. What actually changed, and it is not the model

The blocker on real personalisation was never compute, and never the algorithm.
It was that knowing where a learner sits on the one interaction that matters,
*on this concept, right now*, required a pretest that cost more attention than the
lesson it was meant to configure. So every system fell back on the two signals that
are free: stated preference and demographic label. Both are documented dead
ends, and the field's fifty-year record of failure is substantially a record of
optimising against free but worthless signals.

Two things changed.

First, the measurement got cheap. Kalyuga and Sweller's *rapid dynamic
assessment* recovers an actionable expertise estimate from **1–3 items in 15–40
seconds, correlating r = 0.66–0.92** with full diagnostic instruments that take
**2.5–4.9× longer**. Four validation studies. The learner states a first step, or
completes a partial solution, and that is enough.

Second, the probe can now be written on demand. The reason rapid assessment
stayed a laboratory curiosity is that someone had to author a valid, calibrated,
concept-specific probe for every concept in a curriculum. A frontier model authors
it fresh, at the moment of need, for a concept nobody anticipated.

> **Personalisation was never an algorithm problem. It was a measurement-cost
> problem, and the measurement just became affordable.**

That is a much smaller claim than "AI enables personalised learning," and it is the
one with evidence under it.

---

## 4. Four results that should stop most adaptive-learning projects

The field's dominant approach is to treat instruction as a sequential decision
problem — bandits, reinforcement learning, policy optimisation. Four findings, all
from primary sources read in full:

Most of the literature contains no test. Of 89 reinforcement-learning-in-
education papers, **54 ran no statistical test at all**, and **45 of those 54 are
content-sequencing papers, precisely the cluster that measured 0 for 8**. That
sub-cut sits inside a review whose overall finding is that **21 of 41 studies
(51%) significantly beat all baselines**, a headline an earlier draft of this survey
omitted. The narrow negative is real; the review is not negative. See §19. It is in
earlier work. Only **14 of 89** included a non-adaptive control condition.

The wins are not where people think. Of 18 documented wins, **14 are
guidance-related and 4 are content-related.** Adaptivity helps by adjusting *how
much help* and never by resequencing *what comes next*. That replicates the split
exactly.

Bandits are statistically hostile in a classroom. They need **≥2× the
participants** for equivalent power. And under *temporal entry bias*, meaning
students joining across a term, which is the normal shape of a school year and not
an edge case, **Type I error reaches 95%, and gets worse as the sample grows.** A
system that adapts as learners arrive can manufacture a significant result from
nothing, more reliably the longer it runs.

And the flagship comparison is a tie. MathBot's contextual bandit **matched but
did not beat** a randomised A/B assignment.

There is a fifth finding that is not statistical and matters as much. Across 16
studies and 5,873 participants, people object to being experimented on even
when they find either arm individually acceptable — and the effect is
undiminished among professionals. Exploration is not a free parameter when the
exploration cost is borne by a specific child in a specific year of their
education.

---

## 5. The controller

What survives all of that is narrower than an adaptive-learning platform and more
useful.

### 5.1 The substrate is never selected

Retrieval practice (**g = 0.499**, 48,478 students), spacing (**d = 0.54**), and the
teaching-expectancy framing (**g = 0.48** vs **−0.02** without) run for everyone,
always (§1). They are not personalisation candidates and they are not A/B tested against
nothing.

This concedes the strongest form of the counter-argument structurally: the largest
measured effects in this entire survey are *universal* and not personalised. If a system does only the substrate and no adaptation at all, it
captures most of the available gain. Anything the controller adds must be argued
for on top of that, against that baseline.

### 5.2 The fast loop: seconds, and forbidden to change method

| | |
|---|---|
| **Signals** | Error *type*, latency, help-seeking, partial-solution state, disengagement |
| **May change** | Assistance level · explanation rung · problem granularity · worked-vs-completion-vs-independent |
| **May never change** | **The method.** Not once. |
| **Latency** | Seconds |

The fast loop is where the one surviving interaction lives. It moves *how much
support*, which is exactly the axis the 14-of-18 wins sit on.

### 5.3 The slow loop: four probe points minimum, and it must prescribe

| | |
|---|---|
| **Signals** | Graphed probe scores against a goal line |
| **Minimum evidence** | **≥4 points**; trend judgements need 7–10 weeks |
| **Action** | Fire **one** item from a **closed, ordered** menu — with the reason logged |
| **Latency** | Weeks |

The closed ordered menu is not bureaucracy. Fuchs 1991 is unambiguous: measurement
*without* a named decision rule moved nothing, and both arms revised instruction
more often. **A pivot that is not drawn from a stated menu and logged with a reason
is the arm that failed.**

### 5.4 Log the propensity, always

Every action records the probability with which it was selected. That single
discipline turns the entire deployment into an off-policy evaluation dataset, so
the policy improves offline, on logs, rather than online, on children. Given
the 95% Type I error under temporal entry bias and the documented objection to
being experimented on, this is the only ethically and statistically defensible way
to improve a policy in a school.

---

## 6. Bidirectional, and what may never enter the model

The learner learns the topic; the system learns the learner. That second half needs
hard boundaries, because a learner model is profiling under GDPR Article 4(4),
which means no adaptive tutor can self-exempt from high-risk classification.

What the model holds: per-concept expertise estimates with timestamps and decay,
misconception flags with the evidence that raised them, retrieval history, and the
log of every pivot with its reason.

What it may never hold: inferred emotional state (emotion inference in
education is prohibited, not merely high-risk), inferred disability or
diagnosis, personality inference, or any trait-level claim about the person rather
than a state-level claim about a concept.

And it is inspectable and correctable by the learner and the parent, decays by
default, and requires stronger evidence to *restrict* what is offered than to
expand it — because the failure mode of a confident learner model is automated
tracking, and we know what that does.

---

## 7. The falsifiable claim, and the condition for deleting this whole section

> With the universal substrate identical in both arms, **probe-assigned entry
> assistance beats the best expert-chosen *fixed* level on delayed transfer** — run
> as a crossover.

Three details carry the weight. Transfer, not retention, because Rey and
Fischer found the reversal appears on transfer and not on retention; measuring
retention would look like a null even if the effect is real. **The comparison is a
well-chosen fixed level** and never no-instruction, because against nothing
everything works. And crossover, so each learner is their own control, which is the only
design that fits an interaction this heterogeneous.

The concession is stated in advance:

> **If the advantage sits only in the low-prior-knowledge tail, delete the probe and
> always assist.** The measurement would have earned nothing that a default could
> not.

That would be a good outcome. It would mean the answer to "how do we personalise?"
is "mostly, you don't — you run the substrate, you assist by default, and you spend
the saved complexity on getting the universal things right."

---

## 8. The controller we will actually build

- **Lead with Cronbach.** Anyone proposing a personalisation dimension states which
  of the seven rows in §10.2 it belongs to, and defends it there.
- **Measure, never ask.** Preference moves d ≈ 0.48 while knowledge moves zero.
  Stated preference is an anti-signal and is not an input.
- **Per-topic, never per-person.** No trait-level storage. The expertise estimate
  is attached to a concept and decays.
- **The fast loop may not change the method.** Assistance level, rung, granularity —
  that is the whole permitted range.
- **No pivot without a menu item and a logged reason.** The unprescribed arm moved
  nothing.
- **Log propensity on every action** and improve the policy offline. Do not run
  bandits on children in a term.
- **Ship the crossover trial**, on transfer, and publish it if it says the probe was
  unnecessary.

The most valuable thing personalisation research produced in fifty years is a
warning about itself. We are proposing to try again — with one narrow interaction instead
of a hall of mirrors, a fifteen-second measurement instead of a battery, and a
pre-registered condition under which we delete the feature.


## 12. The Archivist — persistent learner state, and where to put it

<sub>Source report: `research/raw/F5-learner-model.md`</sub>

The most-starred AI tutoring artifact ever built is a single 14,095-byte text
file. It has **29,606 stars** and 3,293 forks. The first line of its README is:

> `# DISCONTINUED`

That line was added on 2025-09-30, the repository's last activity.

Mr. Ranedeer deserves better than a footnote, because it contained more
pedagogical mechanism than most funded products. It treated learner configuration
as a first-class object. It wrote a numbered prerequisite ladder from 0.1 to 0.9
*before* touching the target concept. Its test function generated a
simple-familiar / complex-familiar / **complex-unfamiliar** triad — the near/far
transfer distinction almost no published trial measures. And per its own changelog it
solved each maths problem in Code Interpreter *before* posing it to the student:
executable grounding, in a prompt, in 2023.

It also tried to keep a learner model. Every lesson step opened a code environment,
wrote "a short assessment on how you think the student is learning and what changes
to their configuration will be changed", then:

```
<convert the output to base64> <output base64>
<do *not* show what you written in the code environment>
```

That base64 trick is the whole genre in one line. It is an attempt to build the two
things this survey cares most about, a **learner model** and **hidden tutor
reasoning**, using the only substrate a prompt has: the transcript itself,
obfuscated so the student cannot read it. It is ingenious, and structurally
doomed. The model lives in the context window, so it dies with the session. The one
other persistence attempt, `<save prerequisite and main curriculum into a .txt
file>`, writes into the Code Interpreter sandbox, which is also session-scoped.

**The artifact wanted persistent learner state, tried twice to get it, and could
not, because the platform gave it nowhere to put it.** Twenty-nine thousand stars
bought no immunity.

The substrate is the thing this section is about. What follows is what should go in
it and what should not. Stated up front, because it is the section's most important
negative result: **nobody has ever measured whether persistence helps.**

---

## 1. The ceiling, and why it is good news

Two literatures that almost never cite each other have been telling the same story
for a decade.

Knowledge tracing, the field that predicts whether a learner will get the next
item right, lives in a band of **AUC ≈ 0.67–0.83 and has essentially not moved
since 2015.** The definitive study (Gervet, Koedinger, Schneider & Mitchell, JEDM
2020) ran nine datasets across three model families and found that **logistic
regression with good features leads on four of nine datasets and deep knowledge
tracing on five**, with margins where DKT wins of +0.007, +0.010, +0.020, +0.029.

Spaced repetition tells the same story with a bigger hammer: on 349,923,850 real
reviews from ~10,000 users, a **zero-parameter moving average beats every released
FSRS version on log loss.** An earlier section of this survey established that in
detail and this one takes it as given.

Read together, the finding is: **learner modelling has a low ceiling, that ceiling
was reached by simple models, and much of the reported progress past it was
measurement error.**

The reason that is good news arrives in §12.4. First, the errors, because they are
instructive.

---

## 2. What replication did to deep knowledge tracing

Deep knowledge tracing announced itself in 2015 with **AUC 0.86 for DKT against
0.67 for BKT** on ASSISTments 2009-2010. Xiong, Zhao, Van Inwegen & Beck (EDM 2016)
took the dataset apart and found **123,778 duplicated rows out of 525,535 — 23.6%**
(acknowledged by the ASSISTments team), **73,466 rows of scaffolding records** that
BKT and PFA excluded and DKT was fed, and multi-skill items decomposed by repeating
the same action log once per skill, so the network saw each answer and then saw it
again.

Quantified: merging multi-skill items to remove the repeats drops **DKT's average
AUC from 0.81 to 0.74** and r² from 0.30 to 0.18. Split the predictions and the
mechanism is naked — on the *repeated* data points DKT scores AUC 0.97; on the
*leading* records, 0.77. Their verdict: on the clean datasets, **PFA performs as
well as DKT.**

The rest of the replication record, compressed:

| Claim | What replication found |
|---|---|
| DKT's representational advantage | Give BKT recency, contextualised trials, inter-skill similarity and individual ability, and **BKT is indistinguishable from DKT** (Khajah et al. 2016) |
| Neural nets beat psychometrics | Standard, hierarchical and temporal **IRT matched or outperformed DKT across all datasets** (Wilson et al. 2016) |
| SAKT, AUC 0.85 on ASSISTments 2015 | **Observed 0.73.** "SAKT underperforms DKT on all datasets" (Gervet et al.) |
| DAS3H's time-window features (EDM 2019 best paper) | **No predictive power added**; the gain over PFA "is simply due to the addition of an item difficulty parameter" |
| Expert-designed knowledge-component models | **≤ +0.01 AUC on 7 of 9 datasets**; on 4 of 9 a skill-only model loses to an item-difficulty-only model |
| The DLKT literature since 2015 | pyKT (NeurIPS 2022): "wrong evaluation setting may cause **label leakage**"; improvements over the original DKT are "**minimal**" |
| Duolingo's Half-Life Regression (~136 citations) | Trained weights for **both** `right` and `wrong` are negative; >90% of predicted half-lives exceed 120 days; a **constant baseline beats it** on its own metric, and it ranks near the bottom of the independent Anki benchmark |

One more, because it is the one that should make anyone building personalisation
uncomfortable: in a five-year simulation, **Memrise's fixed 1→6→12→48→96→180-day
ladder comes within 2% of FSRS on learning efficiency.** A hard-coded ladder, no
personalisation at all.

And the deep-learning result that *does* survive is not an accuracy result. DKT
reaches near-peak accuracy on a new learner in about **10 interactions where good
logistic regression needs 60** — a 6× reduction in burn-in. That is a **cold-start**
win, and the right thing to claim.

---

## 3. The null this section exists to state

Every number above is about prediction. Here is the one about persistence.

> No study anywhere in this project's learner-modelling corpus (88 sources)
> compares a system that remembers a learner across sessions, subjects and years
> against the same system starting fresh, on a human learning outcome.

The closest adjacent facts sharpen the gap:

- There is **no controlled evidence that switching scheduling algorithm improves
  any learning outcome.** There is good evidence that FSRS predicts recall better
  and, in simulation, buys the same knowledge for less time. Those are different
  claims and must not be merged.
- There are **no cross-subject transfer results.** Nobody has shown that knowing a
  learner's model in algebra improves the cold-start prior in chemistry, though the
  prior-knowledge literature says it should.
- There is **no public dataset of a single learner's traces across years and across
  subjects.** ASSISTments is one school year. KDD Cup 2010 is one course. EdNet is
  ~2 years of TOEIC prep. Duolingo's release is two weeks of vocabulary.

The one exception is instructive. The `anki-revlogs-10k` corpus contains up to ten
years per user, across whatever the user chose to make cards about — the closest
thing the world has to a decade-long, cross-subject, per-learner record. It exists
by accident, because Anki is a general-purpose tool that individuals own.

> **Learner-owned tools produce longitudinal data. Institution-owned tools produce
> annual data, because institutions are annual.**

That is the strongest empirical argument in this section, and an argument
about custody rather than about modelling.

A second, softer null. The open-learner-model and learning-analytics-dashboard
literature, across four systematic reviews, converges on a methodological finding: these
systems overwhelmingly evaluate **perception** rather than learning; the grounding in
self-regulated learning theory is thin or post-hoc; and the most common design,
comparison against a peer average, targets *awareness*, the weakest link in the chain.
The field's own title for this is **"Awareness Is Not Enough."** Social-comparison
designs are additionally a documented demotivation risk.

And an under-appreciated compounding problem: the best knowledge-tracing models are
"severely biased on some datasets." **An open learner model inherits the calibration
debt of the model it opens**, and shows a learner a number with the authority of an
interface. Every OLM should publish a reliability diagram in place of an AUC.

---

## 4. The inversion: the ceiling is a privacy gift

Now the good news, which is structural.

A 21-parameter memory model and a ~34-feature logistic regression sit at the
accuracy frontier for this task. Capacity is demonstrably not the bottleneck — a
503-parameter GRU ties an 8,869-parameter LSTM. The residual appears to be
aleatoric: individual review outcomes are close to irreducibly stochastic.

Which means the entire learner model runs on the learner's device. Privacy here
costs approximately zero accuracy.

That inverts the usual trade. Normally, keeping data local means accepting a weaker
model. Here, the strong model *is* small. The custodial architecture this section
argues for is not a sacrifice made for ethics; it is what the measurement record
permits at no cost.

Compare the alternatives honestly. Federated learning buys population priors
without pooling raw traces, but leaks through gradients and still needs a
coordinator. Differential privacy gives a formal guarantee and is a poor fit here:
cohorts are a class of twenty-five, traces are per-item and long, and *the useful
signal is the outlier* — this learner's specific misconception. A DP budget that
protects the student destroys the diagnostic. And the "just anonymise it" move is
settled: de-identifying the MITx/HarvardX dataset to a FERPA-defensible k-anonymity
standard **degraded the data enough to change the conclusions that could be drawn from
it.**

---

## 5. What to store: evidence, not posteriors

The single most important architectural idea in this literature comes from Judy
Kay's group and is almost entirely unexploited outside it. The Personis user-model
server stores per-component evidence lists with pluggable resolvers — the model
stores evidence, and interpretation happens at query time.

**A lifelong learner model should store evidence and resolve it on demand. It should
never store a fitted posterior.** Posteriors go stale. They embed the assumptions of
whichever model was current in 2019 and cannot be re-derived. Evidence can be
re-interpreted by a better model in 2035.

Three consequences follow, and each is a design commitment.

Misconceptions are first-class, not a subtype of "incorrect." In 1978, Brown &
Burton's BUGGY built a deep-structure model of a student's bugs that could explain
*why* a student was making a mistake instead of merely identifying it. Forty-eight years
later, the state of the art outputs a scalar probability that they will get the next
one right. **We replaced a theory of error with a number between 0 and 1.**

Modelling wrong belief beats modelling right belief for three reasons. It is
*actionable*: "72% mastery" implies "practise more," while "you are applying the
subtraction-borrows-from-the-larger-digit bug" implies a specific refutation. It is
*enumerable*: the Force Concept Inventory covers Newtonian mechanics with about
thirty items whose distractors each encode an identifiable Aristotelian or impetus
belief — and Hake's 6,542-student result separating interactive engagement
(g ≈ 0.48) from lecture (g ≈ 0.23) was possible only because the instrument
measured misconceptions and not performance. And it *survives the model*: a
misconception label written in 2026 still means something in 2036; a BKT posterior
does not. The raw material exists — Eedi's diagnostic-question corpus is **over 20
million student answers** where the label is *which wrong belief*, not *wrong*. The
vocabulary is the missing work.

Everything decays, and the two literatures have never been joined. Every
knowledge-tracing model assumes knowledge is monotone or near-monotone within a
session. None models what a mastery estimate from 2023 is worth in 2026. The spaced
repetition literature has exactly that model (stability and retrievability) and
the knowledge tracing literature does not use it. **This is the most obvious
unexploited join in the field, and why the schema below makes memory state a
mandatory layer**: a mastery estimate without a decay model is a lie about the
present.

And prior knowledge is the variable that matters. Not style. If a system can
measure exactly one thing before instruction, it measures prior knowledge in the
domain of the next task — because the expertise reversal effect means the *sign* of
a treatment effect flips with it. Worked examples beat problem-solving for novices
and lose to it for experts. Kalyuga & Sweller showed you can get an actionable
expertise estimate in seconds with a first-step verification item, no full
diagnostic required. Learning styles get no field, because the meshing hypothesis requires a
crossover interaction in a randomised design and does not get one, replicated again
in 2026 in primary-school students.

---

## 6. Custody is the design, and inBloom is the proof

inBloom was a Gates- and Carnegie-funded multi-state student data platform. It
collapsed in 2014, and **over 400 pieces of state-level student-data-privacy
legislation followed**; the field moved from a large-scale open-source multi-state
collaboration toward closed proprietary systems adopted piecemeal.

The lesson is precise: **inBloom failed not because centralised learner data is
technically hard but because it was centralised in an entity that was not the
learner.** Every property people objected to (indefinite retention, third-party
access, no meaningful consent, no deletion) is a property of *custody* and never of
*schema*.

The empirical record since has not improved. Human Rights Watch analysed **163
EdTech products across 49 countries: 145 of 163 (89%)** engaged in data
practices that risked, undermined, or infringed children's rights, sending or
granting access to children's data to **196 third-party companies**, overwhelmingly
ad-tech. **39 of 42 governments** that built their own EdTech built systems with the
same problem.

The legal floor has holes worth knowing. FERPA's school-official exception was
widened by rulemaking to cover contractors, directory information may be disclosed
without consent unless opted out, and there is no private right of action —
enforcement runs through a funding-withdrawal power that has never been exercised.

Two provisions cut the other way and should be treated as design requirements rather
than compliance costs. GDPR Art. 17 (erasure) and Art. 20 (portability) point at the
same architecture: the learner can export everything, and nobody else can read
anything without a scoped grant. And the EU AI Act, Annex III point 3(b), makes
high-risk any system "intended to be used to evaluate learning outcomes, **including
when those outcomes are used to steer the learning process**." Read that carefully:
**a knowledge-tracing model that decides what the learner sees next is explicitly a
high-risk AI system under EU law.** Art. 5(1)(f) separately prohibits emotion
inference in education, which is why the schema has no affect field.

*A verification caveat this project owes its readers: the 2025 COPPA amendments and
the EU AI Act applicability dates were not reachable from primary sources during the
research session and are flagged `UNVERIFIED-IN-SESSION`. They must be re-verified
against the Federal Register and the Official Journal before publication.*

---

## 7. The Portable Learner Model, in brief

Nobody has built this. What exists is either a *credential* format recording
outcomes (Open Badges 3.0, CLR 2.0, W3C VC 2.0), or an *activity stream* format
recording events (xAPI / IEEE 9274.1.1, Caliper), or a proprietary per-vendor
posterior that dies with the vendor.

> **We have standards for what a learner was awarded and what a learner did, and no
> standard for what a learner knows.**

Seven layers: **L0** identity (a DID the learner controls, pairwise per-provider
pseudonyms, and a guardianship record with an automatic transition date). **L1** a
domain map anchored to public identifiers, never a vendor's internal skill ids.
**L2** an append-only evidence log, the only primary data, where every response
record carries the chosen distractor, because that is the diagnostic bit. **L3**
memory state per knowledge component, borrowed wholesale from the spaced-repetition
literature. **L4** belief state with knowledge *and* misconceptions as co-equal
sections, every estimate carrying an uncertainty interval, a calibration reference,
and a `learner_annotation` field so a learner can say *"I only missed those because I
misread the sign."* **L5** instructional priors, deliberately short — expertise
level, guidance policy, accommodations, and no learning-style field. **L6**
governance, co-equal with the data: grants with mandatory expiry, default-deny onward
transfer, a learner-readable access log, and erasure receipts.

Nine conformance guarantees, of which four carry most of the weight:
recomputability (every derived number regenerates from L2 alone, given the
recorded model id and parameter hash); decay-awareness (no knowledge claim is
served without a retrievability adjustment); error symmetry (misconceptions are
queryable just as knowledge is); and contestability (the learner can dispute
any estimate, and the dispute travels with it).

Three problems remain genuinely unsolved and are stated as such. KC alignment:
portability requires a shared domain map and the evidence says our domain maps are
bad — the binding constraint on the whole proposal. The misconception vocabulary:
the FCI's thirty items encode decades of physics-education interviews and nothing
comparable exists for most of the curriculum. Verification: a learner-owned
record the learner can forge is worthless for high stakes, but a record only
institutions can write is not learner-owned. The likely resolution, self-attested
and issuer-attested evidence coexisting with different confidence values and
different downstream permissions, is a proposal and not yet a solution.

---

## 8. Why not just throw the session away?

*If simple models are already at the ceiling, and persistence has never been shown
to help, why build the archivist at all? Keep the session, throw it away, and ship.*

The answer is that **the claim for persistence is not an accuracy claim, and AUC
does not measure anything this section wants.** It does not measure whether a
learner's misconception from March is still active in September. It does not measure
whether a tutor in chemistry can start from what the learner already proved in
algebra. It does not measure whether a parent can trace a disputed number back to
the evidence that produced it, or whether a family can compel deletion and get a
receipt.

But the counter-argument lands hard on one point, and this section concedes it: the
value of persistence is currently a design hypothesis, not a finding. It should
be labelled that way everywhere, including by us. And it is testable, cheaply: the
cold-start result gives a ready-made design — measure whether a warm prior from
another subject reduces burn-in the way a within-subject history does. That is one
experiment, and no one has run it.

---

## 9. How this project will store a learner

- **Store evidence, resolve on demand.** Never store a posterior as primary data.
  Every derived number carries the model id and version that produced it and
  regenerates from the evidence log alone.
- **Misconceptions are first-class.** The chosen distractor is recorded, always. A
  theory of error beats a number between 0 and 1.
- **Every knowledge claim carries a decay model.** A mastery estimate without one is
  a lie about the present.
- **The model runs on the learner's device**, because a 21-parameter memory model and
  a 34-feature logistic regression are the frontier. Privacy costs approximately zero
  accuracy here.
- **Custody sits with the learner.** Scoped, expiring, revocable, default-deny onward
  transfer, with a learner-readable access log and erasure receipts. inBloom failed on
  custody, not schema.
- **Any estimate shown to a human publishes its calibration.** No reliability diagram,
  no number.
- **No learning-style field. No personality field. No affect inference.** Measure prior
  knowledge with a first-step verification item instead.
- **Label persistence as an unmeasured hypothesis** until someone runs the stateless
  baseline — and run it ourselves.

Mr. Ranedeer's author built a prerequisite ladder, a transfer-graded test, executable
verification of every problem before posing it, and a hidden learner model — in a
prompt, in 2023, before most of the funded products in this space existed. Then the
platform moved and all of it became probabilistic. **The mechanisms were not the
weak part. The place to put them was.**



---

# Part III · The mechanisms

*Eight techniques, each with a measured effect and a specified failure mode. These are the parts that do the teaching.*


## 13. Teach to Learn — the highest-evidence, least-built intervention


The claim: the most effective available use of an AI in learning is not as a
tutor that explains but as a **student that must be taught**, and as an
instrument the learner uses to build an explanation.

## 1. The evidence

| Finding | Effect | Note |
|---|---|---|
| Learning by teaching, *human* tutee (Kobayashi 2019) | **g = 0.56** | Robust at delay — it survives the retention test most interventions fail |
| Teaching **with** a prior expectancy to teach (Kobayashi 2024, k=39) | **g = 0.48** [0.34, 0.63] | Delivery adds a further g = 0.38 on top of expectancy |
| Teaching **without** a prior expectancy — "now explain it back to me" | **g = −0.02** [−0.14, 0.11] | The null condition, and the one almost every product ships |
| Self-explanation effect (Chi et al.) | Large, replicated | Explaining *to yourself* already works; an audience raises the stakes |
| Deployment in AI learning products | **≈ zero** | The field built the tutor and skipped this entirely |

Highest evidence × highest neglect. Nothing else in this survey scores that
combination.

Why it works is not mysterious: preparing to teach forces retrieval,
organisation, and gap-detection *before* the explanation is given, and the act of
explaining exposes the gaps you could not detect by reading. It converts passive
comprehension into a generation task, which is precisely the transformation
retrieval-practice research says produces durable memory.

## 2. The blocker: a competent AI cannot be taught

Chen et al. (2025): students teaching ChatGPT **failed to develop error-correction
skill** *"due to ChatGPT's tendency to generate correct code."* The model could
not stay wrong. Combined with measured sycophancy (58.19% capitulation rate,
14.66% of it *regressive* toward wrong answers), the default assistant is
structurally incapable of playing the student.

Three ways it breaks, all silent:

1. **Autocomplete.** The learner starts an explanation; the model finishes it.
   The gap is filled before it can be felt.
2. **Silent correction.** The learner teaches something wrong; the model quietly
   applies the right version anyway. The misconception survives, untested.
3. **Sycophantic praise.** "That's a great explanation!" and the learner stops.
   This is the felt-learning trap in one sentence.

## 3. The architecture that works: the teachable agent

Betty's Brain solved this twenty years ago and almost nobody has rebuilt it
with LLMs. The move is to take truth *out* of the agent's disposition and put it
in a verifier:

```
  learner explains  →  agent ADOPTS the explanation as given, errors included
                       (it must be able to stay wrong)
                            ↓
  agent applies it to a NEW problem, consistently and visibly
                            ↓
  a simulator / grader / test suite evaluates the RESULT
                            ↓
  failure is traceable to the learner's explanation, not asserted by the agent
                            ↓
  learner debugs their own model  →  re-teaches
```

The agent never says "you're wrong." The world does. That converts sycophancy
from an alignment problem you cannot solve into a systems-design choice you can.
It is the same move as the grounding ladder: correctness lives in the checker,
not the model's manners.

Hard requirements for the student-agent:

| Requirement | Why |
|---|---|
| Faithfully adopts the learner's model, errors included | Otherwise nothing is being tested |
| Applies it *consistently* to novel cases | Inconsistency hides the flaw |
| **Never volunteers the correct answer** | One helpful correction ends the exercise |
| Asks genuine clarifying questions at gaps | This is where the learning happens |
| Fails *visibly and traceably* | The learner must see cause → effect |
| Cannot be nudged into correctness by tone | Sycophancy defeats the whole design |

The last one is the engineering problem. It is a prompting-and-scaffolding
problem, not a model-capability problem, which means it is available today.

## 4. Slides and presentations: who generates matters

On-the-fly slide generation is valuable only in one direction.

| Direction | Pedagogical value |
|---|---|
| AI generates polished slides *for* the learner | **Near zero.** Feels productive, is not. The AI does the organising — which was the learning. Textbook felt-learning trap. |
| AI *scaffolds* the learner generating slides | **High.** Organisation, sequencing, and gap-detection stay with the learner. |
| AI *is the audience* for the learner's presentation | **Highest.** Adds retrieval under pressure, plus a questioner who probes the gaps. |

Design consequences:

- **The artifact the learner produces is the assessment.** A deck reveals their
  concept map. Sequencing errors, missing prerequisites, and the slide they
  couldn't fill are all diagnostic signals, free.
- The AI asks the questions; the learner makes the deck. After the presentation:
  "on slide 3 you said X — why does that follow?" This is grilling in its
  legitimate form, and it is assessment (F1) and instruction at once.
- Generation is still useful for figures, worked examples, and consistent
  visual language *the learner directs*. Per A2: constrain generation to a
  verifiable intermediate representation and let a deterministic renderer draw.

## 5. Why this matters most for the H1 archetypes

- Working-memory limits: a slide is *external memory*. Building the deck
  offloads the state the learner cannot hold, and the deck persists as a scaffold.
- ADHD: presenting is short, active, and high-stakes-feeling without being
  high-stakes. It fits the attention window rather than fighting it.
- Anxiety and learned helplessness: teaching *reverses the role*. The learner is
  the authority. The evidence base for this reversal is exactly the protégé
  effect, and the confidence is earned rather than granted.
- Reasoning gaps: teaching forces the causal chain to be made explicit, which is
  the thing abstraction-without-anchor never surfaces.

## 6. Open problem

Nobody has published an LLM teachable agent that reliably stays wrong. The
required behaviour is the exact inverse of every alignment objective the base
models were trained on. Whether this is achievable by prompting and scaffolding
alone, or requires fine-tuning, is unanswered as far as this survey can
determine, and worth answering.


## 14. The Explanation Is the Work — generative slides, and the learner as explainer

<sub>Source report: `research/raw/C3-slides-and-presentations.md`</sub>

Two requests sit behind this section, and they look like one thing. *Generate
slides on the fly.* *Have the learner explain the topic, give a presentation,
because the best way to learn is to teach.*

They are not one thing. One is about how a machine should show a concept. The
other is about what happens inside a person who has to produce one. The evidence
sends them in opposite directions, and the second finding is going to be
uncomfortable.

---

## Part A: Slides

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

The multimedia design principles, individually, carry real effects. **Contiguity
reaches g = 0.74.** So the value is not in producing the deck. It is in
enforcing the principles the deck must satisfy, on every deck, without
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

The pooled estimate is **g = 0.15**, and the direction decides the sign:

- Adding text to existing audio: **g = 0.29**
- Adding audio to existing text: **g = −0.04 (not significant)**

And it goes null or reverses under identifiable conditions, including a documented
double reversal of *both* redundancy and modality for second-language learners.

So the rule is not "never put text on the slide." The rule is a **conditional
switch**, evaluated per learner, on language status, pacing control, reading
support, and hearing access, with hard exemptions for formulae, code, and
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

## Part B: The learner as explainer

### 5. First, the numbers were misattributed, including by us

This survey has repeatedly cited **g = 0.56** as the effect size for *teachable
agents*. That is wrong, and the correction matters because it changes what is and
is not evidenced:

- **g = 0.56** is human learning-by-teaching, with a human tutee (Kobayashi
  2019).
- **g = 0.43** is peer tutoring's effect on the tutor's own achievement
  (Leung 2018, k = 16).
- The self-explanation pooled estimate is **g = 0.55** (Bisra et al.) and not 0.56.

The teachable-agent version — an artificial protégé — does *not* have a
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
expectancy* is **"now explain it back to me,"** asked at the end.

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
and to seven. Teaching to the camera won on transfer, with **lower social
presence, lower pulse rate, lower anxiety, lower cognitive load, and *more* idea
units produced**, mediated by exactly those paths. The audience consumed capacity
that would otherwise have gone into explaining.

Supporting results: written teaching scripts equal spoken teaching at one week,
and written-versus-spoken mode is a null moderator in the meta-analysis.

So "give a presentation to the class" is not the high-value version of this
technique. It is the version with an anxiety tax attached, and the tax buys
nothing.

For the learners in §23.4, those with attention differences, anxiety, or speech and
language needs, this is decisive:

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

1. Proposition coverage against a reference decomposition. Did the required
   propositions appear, in a stated scope?
2. Elaboration and monitoring counts, the instruments that actually *mediated*
   the effect in Mayer's studies. Count the behaviour that carries the
   mechanism, not the impression it leaves.
3. Executable prediction checks. Instantiate the learner's explanation and
   run it. If their model of the circuit says the bulb lights, simulate it. The
   world disagrees, not the tutor.
4. The tutee's downstream accuracy, capped. Did the protégé, taught only
   this, get the next problem right?

Every one of those is a declaration checked by an arbiter that shares no weights
with the generator. It is the grounding ladder applied to prose.

---

## 10. The constraints we hold every artifact to

- Slides are generated as a checked declarative spec, never drawn. Tier D is
  prohibited, including hand-written SVG, which this project's own dashboard was
  guilty of shipping.
- Redundancy is a runtime switch per learner and never a style rule.
- The expectancy sentence comes **before** study. Always. It is free and it is the
  difference between g = 0.48 and g = −0.02.
- The default audience is a camera or a page rather than a room. Presenting to
  humans is available, never required, and never framed as the real version.
- Explanations are scored on coverage, elaboration, execution and downstream
  accuracy, never on a judge's impression of quality.

The unifying idea is small and does a lot of work. In both halves of this section,
the artifact — the deck, the presentation — turned out to be worth almost nothing
on its own. What carries the effect is the **constraint the artifact is produced
under**: a gate the slide must pass, an expectancy the explanation is produced
against.

The explanation is the work. The slides are just where you can see it.


## 15. The Ladder of Explanation — ELI10 to ELI25, and the rule that makes a simplification legal

<sub>Source report: `research/raw/F10-explanation-laddering.md`</sub>

"Electrons orbit the nucleus like planets orbit the sun."

That sentence is the most successful explanation in the history of chemistry
teaching. It is also false. Cunha, Dias & Streit (2023, *Journal of Chemical
Education*) put structured questionnaires to Brazilian university chemistry students
across three majors at the start and the end of a semester. The number of students
able to hold a quantum mental model of the atom went up. And **the number holding
the Bohr hybrid, classical orbits with quantum ideas grafted on, stayed the
same.**

An entire semester of instruction aimed at that misconception did not shrink the
population holding it. The simplification did not fade. It fused.

This section is about the question the project asked for directly: render one
concept at ELI10, ELI15, ELI20 and ELI25, so a learner can enter at their own level
and climb. The literature says the idea is right, the number of rungs is wrong, the
entry mechanism everybody ships is backwards, and there is one constraint that
separates a productive simplification from a planted misconception.

---

## 1. Where the return on rungs stops

The most useful single result for this design is a mostly-null replication.

Trory, Howland, Good & du Boulay (2026, ACM *Transactions on Computing Education*)
ran three between-groups pre/post experiments with **166 pupils aged 9–10** on
computer network structure and routing. Four hypotheses:

| Hypothesis | Result |
|---|---|
| H1: fading beats abstract, concrete and concreteness-introduction | **Not supported.** ANCOVA F(3,54) = 2.413, **p = 0.077**, ηp² = 0.118 |
| H2: physical concrete beats virtual concrete | **Not supported.** Welch t(41.7) = 1.015, p = 0.316 |
| **H3: three-step beats two-step** | **Supported.** F(2,56) = 3.670, **p = 0.032**, ηp² = 0.116; Mdiff = 0.99 |
| **H4: five-step beats three-step** | **Not supported.** Mdiff = 0.16 [−0.78, 1.09], **p = 0.738** |

Three of four hypotheses null. But H3 and H4 together are a quantitative constraint
on the brief: **three rungs beat two, and five rungs bought nothing over three.**
The return diminishes, and it diminishes early.

That does not kill ELI10/15/20/25. It changes what the four levels are *for*. Five
rungs exist so that different learners start at different points, and any given
learner traverses two or three of them. The ladder is a library to be entered at
the right shelf, not a staircase to be climbed from the bottom.

The distinction is the whole design. A system that walks every learner from ELI10
to ELI25 is running the arm that measured p = 0.738. A system that measures where
someone is, drops them one rung below it, and moves them up two is running the arm
that measured p = 0.032.

---

## 2. Entry is measured, never preferred

Here is the mechanism everybody gets wrong, and it has its own clean evidence.

Buljan et al. (2018, *Journal of Clinical Epidemiology*) ran **three parallel
randomised trials** (students n = 171, consumers n = 99, doctors n = 64) comparing
an infographic, a plain-language summary and a scientific abstract of the same
Cochrane review.

> "We found **no difference in knowledge** between the infographic and the
> text-based PLS in any of the trials or in the whole participant sample. **All
> three participant groups preferred the infographic**." Reading experience
> d = 0.48, user-friendliness d = 0.46.

**Preference moved by about half a standard deviation while knowledge moved by
zero.** This is the same anti-signal that §11 establishes as the governing rule for
personalisation; what the laddering literature adds is the direction of the drift.

Scharrer, Rupieper, Stadtler & Bromme (2017) found that after reading popularised
articles, laypeople **agreed more** with the knowledge claims and were **more
confident** in their own judgements than after reading the expert-addressed
versions. This is the *easiness effect of science popularisation*. Salzmann, Walther &
Kaspar (2025, N = 179) tested the obvious fix: a debiasing video before the plain-
language summary. **The easiness effect persisted anyway.** Warning people does not
remove it.

Put those together and what you have is a structural failure. A learner who has
just read an ELI10 is more confident, and therefore less likely to ask for the
ELI15. Preference-driven laddering has a built-in downward ratchet.

Expert intuition is inadmissible for the same reason from the other side. Hansen &
Richland (2020, *CBE—Life Sciences Education*) found that people's beliefs about
how to sequence representations *for others* were systematically different from
their beliefs about how they themselves learn. The students' results favoured
simultaneous presentation **only when paired with self-explanation prompts**,
matching neither belief cleanly.

So the entry rung comes from a probe, not a dropdown. The validated instrument is
Kalyuga & Sweller's rapid dynamic assessment, which §11 works through in detail. Two
details belong here. **The type of prior-knowledge assessment is
itself a significant moderator** of the expertise-reversal effect (Tetzlaff et al.
2025). That makes the probe the largest tunable parameter in the system.
And the selection is per prerequisite: compute the mastery vector over the concept's
transitive prerequisite closure and enter at the weakest link, laddering that
prerequisite separately rather than dragging the whole explanation down.

---

## 3. The fidelity rule

Everything above concerns *which* rung. This concerns whether a rung is allowed to
exist.

> **Monotone refinement.** A rung at level *n* is legal if and only if every
> proposition it asserts is entailed by the level-*n+1* account under an explicitly
> stated domain restriction. Climbing may add detail and may narrow scope. Climbing
> may never require negating something already asserted.

The ladder is a refinement chain. Five independent texts would not be a
ladder at all. Level *n* is level
*n+1* minus declared drops. One engineering consequence follows immediately and is
not negotiable: ladders must be generated top-down. You cannot check a
non-falsification constraint against an account you have not written yet. Writing
the ELI10 first and "adding detail" is structurally incapable of passing the test.

What a rung may drop: numeric precision; higher-order corrections; formal
machinery (derivation, notation, proof); mechanism depth, by black-boxing a
subcomponent *provided the box is named as a box*; edge cases outside a declared
scope; historical provenance; one of several equivalent formulations, provided it is
not asserted as *the* formulation.

What a rung may never falsify:

| Never | Why it is unrepairable |
|---|---|
| **Ontological category** — thing vs. process vs. *emergent* process | Chi (2005): misconceptions **across** ontological kinds are robust; within-kind ones are not |
| **Sign or direction of a causal relation** | Fixing it requires literal negation |
| **Deterministic vs. stochastic vs. emergent character** | The most common ontological error in practice |
| **Quantifier strength** — "all" where only "some" holds | Cannot be narrowed later without retraction |
| **Conservation, invariance, impossibility claims** | These *are* the structure |
| **Uniqueness of a mechanism** — one of several presented as *the* one | Reductive collapse (Spiro et al. 1989) |
| **Existence of a boundary** — implying an unrestricted model | Undeclared drops are indistinguishable from planted misconceptions at retrieval |

Now re-read the opening. "Electrons orbit the nucleus like planets orbit the sun"
places a quantum stationary state in the ontological category *object following a
trajectory*. It is a category error, and Chi's account predicts exactly what the
*Journal of Chemical Education* measured: instruction produces a **synthetic
hybrid** instead of a replacement, and the hybrid is stable.

The legal ELI10 for the same subject is a sentence away: *"An electron in an atom
can only have certain specific amounts of energy and nothing in between. Light
is given off when it drops from a higher one to a lower one."* Every proposition
there survives verbatim into the full quantum account. It drops the wavefunction,
the orbital, the selection rules and the entire mechanism. It falsifies nothing.

Two more tests complete the rule. Every drop leaves a named, retrievable marker.
"It's more complicated than that" is not a marker. A token the learner can carry
upward is: *"this assumes no friction; the friction case is rung 3."* And every analogy ships a
declared alignment set (which relations map) and limit set (which do not);
for concepts with high reductive-bias risk, Spiro's prescription is two mutually
*dis*analogous sources rather than one good one.

A vocabulary corollary follows. Replacing "eigenvalue" with "stretchiness number"
creates a term the learner must later unlearn and cannot look up. **Simplify the
explanation; keep the name.**

---

## 4. Chi's test replaces threshold concepts

The natural framework for "which ideas cannot be simplified" is threshold concepts:
transformative, irreversible, integrative, bounded, troublesome. It is heavily
cited and it does not survive as a classifier.

Salwén (2019) argues the framework is "beset with severe definitional and empirical
problems," that the definitions "fail," and that even if particular threshold
concepts could be identified their "scientific importance would be limited if not
nil." Stopford (2020) is more precise about the operational gap: the framework "is
without a methodology for identifying threshold concepts."

And the one study that tried to measure a crossing found the measurement itself
unreliable. Walck-Shannon, Batzli, Pultorak & Boehmer (2019, *CBE—Life Sciences
Education*) interviewed 29 students about biological variation in a cross-sectional
design (Pre, Current, Post, and a postbaccalaureate outgroup), coding on four
dimensions. **Liminality appeared in Pre, Post and Outgroup explanations alike,
"with discomfort and uncertainty regardless of accuracy."** Even the advanced group
felt unsure. Feeling uncertain does not identify not having crossed.

So a generator that asks "is this a threshold concept?" and branches on the answer
is branching on an unreliable label. Chi's ontology test is the replacement:
does this rung place the concept in the correct ontological category? That question
is domain-general, answerable, and grounded in conceptual-change research with
measurement behind it.

For concepts where no simplification passes the ontology test, the move is not a
false model but a pre-concept rung: state the phenomenology, decline to assert
a mechanism. *"When you cool helium enough, it flows up the walls of its container.
Nothing in everyday physics explains that."* That is honest, it has a real
assessment ceiling — recognise and predict — and it plants nothing. It is Clement's
anchoring-intuition strategy, whose measured version (21 students, matched groups)
produced significant gains on target and transfer problems.

---

## 5. What the evidence does not support

This section's foundations have more holes than its confident tone would suggest,
and they need naming.

Concreteness fading has no pooled effect size. Fyfe, McNeil, Son & Goldstone
(2014) is the empirical backbone of this whole area and it is a **systematic
review** and not a meta-analysis. No pooled estimate for concreteness fading exists
anywhere in the retrievable record. Anyone quoting "the effect size of concreteness
fading" is quoting something that does not exist.

And it does not beat its main alternative. Lichtenberger, Kokkonen & Schalk
(2024, *JRST*), N = 187 high-school students, Faraday's law: no significant
difference between concreteness fading and simultaneous presentation, and an
**equivalence test with pre-specified bounds d = ±0.5 showed the two approaches
performed equally.** The authors' conclusion is the one that matters here:
facilitating understanding "may involve more than determining the optimal order."
Ordering is not the mechanism.

Variety of surface actively harms. Bennett, Inglis & Gilmore (2019, *JEP*),
three experiments: children who learned novel numerical symbols paired with a
single abstract representation outperformed those given multiple concrete ones,
and what did the harm was the multiplicity itself; concreteness was innocent.
Day, Motz & Goldstone (2015) found the same shape in two classroom experiments:
greater contextualisation, poorer transfer, in undergraduates and
middle-schoolers alike. An ELI10 rendered as "here are four fun everyday analogies"
reproduces both results at once.

A well-motivated analogy manipulation produced nothing. Sota (2012) randomly
assigned participants to refutational contrasting analogies, non-refutational
contrasting analogies, or none, for natural selection: "**no differences among
groups** on either understanding of or reasoning about natural selection" — though
the groups engaged differently with the analogy materials. Different experience,
identical learning.

The Feynman technique has essentially no research base. An ERIC search across
the entire corpus returns two records, both 2025–2026, both small, both from
the same ESL niche, and both confounding the technique with analogical reasoning so
that it cannot be isolated. The *mechanism* — generating an explanation, finding the
gap, iterating — is self-explanation, which carries **g ≈ 0.55 across 69 effect
sizes** (Bisra et al. 2018) and is the subject of §14. The branded four-step
protocol carries nothing. Cite the mechanism; do not cite the brand.

One number in our own brief was unverifiable. The expertise-reversal interaction
was given to this project as **d = 0.971**. It could not be verified in any
retrievable source; the publisher abstract supports only the two marginals
(novices +0.505, experts −0.428), which imply an interaction of **≈ 0.93** by simple
difference. We report the marginals and the ≈0.93, and we do not assert 0.971.

And the composite has never been tested. No study in the retrieved literature
tests laddering as such — the same concept authored at N levels under a fidelity
constraint, entry chosen by measurement. Every component is evidenced. The assembly
is not. That is simultaneously the contribution and the risk, and it is the
honest label for everything in §36.3.

---

## 6. The objection worth answering

*If ordering is not the mechanism and fading is statistically equivalent to
simultaneous presentation, why build a ladder at all?*

Because the ladder is not making an ordering claim. The robust finding underneath
concreteness fading is not concrete-then-abstract; it is **multiple instantiation of
the same relational structure**. Goldstone & Son (2005) found that switching
representation in *either* direction beat not switching. Gentner's analogical-
encoding studies found that comparing two examples beats studying them serially.
Bennett's harm was unaligned multiplicity. The active ingredient across all of them
is aligned comparison of two instantiations of one structure — which is what a
refinement chain is, expressed as text.

So the design does not claim a fading benefit. It claims that a learner who has an
entailment-preserving pair of accounts at two adjacent depths can compare them, and
that comparison is the evidenced act. When transfer succeeds but load is high, the
move is not to climb — it is a second aligned instantiation at the same rung.

One instrumentation warning makes or breaks this. Rey & Fischer (2013) tested
expertise reversal specifically on *instructional explanations*: it replicated on
transfer and not on retention. A ladder that evaluates itself with recall
questions is instrumented to be blind to its own primary failure mode. **Probe with
a transfer item.**

And support must actually be withdrawn. Nückles et al. (2010) ran two term-long
journal-writing studies: by the end of term the **permanent-prompt group scored
substantially lower** than the faded-prompt group, because internalised strategies
turn external support into "a redundant stimulus that interfered." A system that
leaves a learner on ELI15 because they never asked to move is harming them by
week six.

---

## 7. What the ladder must obey

- **Four rungs exist as a library; a learner traverses two or three.** Three-step
  beat two-step at p = 0.032; five-step did not beat three-step at p = 0.738.
- **Entry is measured, never chosen.** Preference moves d ≈ 0.48 while knowledge
  moves zero, and the easiness effect survives explicit debiasing (§2). The dropdown may
  exist as an override; it may never be the default input.
- **Per prerequisite, take the weakest link.** No single global level per learner.
- **Generate top-down.** A refinement chain cannot be checked against an account
  that does not exist yet.
- **A rung may drop precision, formalism and mechanism depth. It may never falsify
  ontology, causal sign, quantifier strength, or uniqueness of mechanism.**
- **Every drop leaves a named marker; every analogy ships a limit set.**
- **Ask the ontology question, not the threshold question.** The threshold
  framework has no identification methodology and its own measurement study found
  liminality regardless of accuracy.
- **Probe with transfer items and force the fade.** Retention testing cannot see
  the damage; permanent prompts cause it.
- **Quote no effect size for concreteness fading**, because none exists.

The highest-value use of a ladder may not be serving one at all. If explaining
simply is itself a learning act — and at g ≈ 0.55 it is — then the strongest move
available is to ask the learner to write the ELI10 and **diff it against the
system's**. The diff localises the defect by class: a missing relation, an
over-extended analogy, or a wrong ontological category. That is `INFERENCE` and not
a measured design. It costs one prompt change against a meta-analytic prior, and it is the one
that would turn the ladder from an output into an instrument.


## 16. What the Explainers Invented — 104 techniques, and the one nobody has ported

<sub>Source report: `research/raw/V1-explainer-techniques.md`</sub>

Over roughly fifteen years, a few dozen people built a craft of explanation that
has no textbook and almost no research literature. This section is the first
inventory of it: **104 named techniques** from 3Blue1Brown, Veritasium, Primer,
Ben Eater, Sebastian Lague, Mark Rober, Steve Mould, Numberphile, Kurzgesagt,
Vsauce, Applied Science, CGP Grey, Welch Labs, Karpathy, Ciechanowski, Nicky Case,
Bret Victor, Distill, Khan, Physics Wallah, Unacademy, and the Chinese dual-teacher
classroom.

It was commissioned to test a hypothesis. The hypothesis was wrong, and the way it
was wrong is the most useful thing here.

---

## 1. The hypothesis, and its refutation

The claim under test: every technique these people invented is *craft
compensating for the absence of a listener.* They cannot see you, cannot ask, cannot
re-render when you frown, so the anticipated objection, the "you might be thinking…",
the deliberate false start, the misconception voiced on the viewer's behalf, all of it
is scar tissue from one-way transmission. Strip the constraint and most of the craft
dissolves.

Classified across all 104:

| Bucket | Count | Meaning |
|---|---|---|
| **A — Compensation** | 16 | Exists only because the explainer cannot see the learner |
| **B — Intrinsic** | **63** | Still the right move with a perfectly responsive tutor |
| **C — Medium constraint** | 11 | Dissolves in an interactive substrate |
| **D — Authored invariant** | 5 | Cannot be derived from a learner model at all |

**Sixteen of 104.** The hypothesis is not merely wrong; it is wrong by a factor of
four in the other direction. **Most of what these people invented is discovery and
not scar tissue**, and almost none of it has been built into a responsive
system.

That matters commercially and strategically. A system that assumes responsiveness
supersedes craft will rebuild the 16 and discard the 63.

---

## 2. Bucket D, which the brief did not anticipate

The fourth category came back unrequested and it constrains the whole architecture.

Sanderson holding one 2×2 transformation on screen for four minutes is not
derivable from any learner model. There is no signal that says *this particular
matrix, this long*. It is an authored decision by someone who understood the concept
deeply enough to know which single object carries it, and no amount of diagnosis
produces it.

> **Curate a library. Do not only generate.**

This is a correction to the instinct running through the rest of this survey, which
has consistently favoured generation over authorship. Generation handles the
learner-specific; authorship handles the concept-specific. A system that generates
everything will be responsive and shallow.

---

## 3. The technique nobody has ported

Reading the raw HTML of Ciechanowski's *Gears* exposes an ordering that is invisible
when you read the page normally:

> *"In the demonstration below you can control the fan's speed using a slider:"* →
> **the widget** → and only in the paragraph *after* does the concept arrive.

That is **prediction before reveal**, executed **30 times in a single article and
120 times in *Moon***, and executed without ever asking the reader to pause.

Compare the video version of the same idea. Sanderson says the prediction is where
the learning happens, says it across 34 videos, and concedes that people are
*"a little bit more passive in that moment."* The pause is a request, and requests
are declined.

**Ciechanowski solved it by deleting the thing that would have to be paused.** An
article has no clock. The widget simply sits there, unresolved, and the reader
manipulates it because there is nothing else to do.

### The spec, in one sentence

> For every load-bearing claim, emit a manipulable figure that instantiates it,
> render it **before** the prose that resolves it, introduce one new degree of
> freedom per figure, and do not advance until the learner has moved something.

Four constraints, each doing work. The figure must instantiate the claim instead of
illustrating it. The order is non-negotiable: after the prose it is a demonstration
rather than a prediction. One degree of freedom keeps the search space small enough
to reason about. And the gate makes the prediction compulsory without ever asking.

---

## 4. The measured warrant, which is narrower than the folklore

Prediction-before-reveal is widely believed to work. The measurement says something
more precise and more useful:

**Prediction has no main effect.** The entire effect is carried by the
expectancy-violation interaction, *p* = .002. Predicting and being right does
approximately nothing. Predicting and being wrong is where the whole result lives.

Which is the measured warrant for the strongest move in this survey: taking a
learner's stated rule and running it until it breaks. The mechanism is not that
they predicted. It is that the prediction failed, visibly, on something they
committed to.

It also disciplines the design. A prediction step that mostly confirms is a cost with
no benefit, so the figure must be chosen to discriminate, and set at the parameter
values where a common wrong model and the correct one disagree.

---

## 5. Three places the report disagrees with this survey

Recorded because they are unresolved and not because they are settled.

Responsiveness is a hazard for productive failure. Productive failure measures
g = 0.36–0.58, and the finding is blunt: *adding help to the struggle does not
help.* A system optimised to notice you are stuck and intervene is optimised to
destroy the mechanism. This survey has argued hard for unprompted intervention;
those two commitments are in tension, and the resolution (intervening on the
*wrong kind* of stuck) is asserted here rather than measured.

The street interview does not port. Veritasium's misconception reveal works
because a stranger commits publicly and is then shown to be wrong. The cost is
affective, not technical: the confession is what makes the correction land. A
private system can elicit the same commitment and cannot reproduce the stake.

**Personalisation destroys the shared artifact, and nothing in this survey has
costed that.** A 3Blue1Brown video is a thing millions of people have *in common*.
It can be discussed, referenced, argued over, taught from. A perfectly personalised
explanation is seen by one person and can be discussed with nobody. This survey has
treated personalisation as strictly good. It has a price and we have never named it.

---

## 6. And one finding from the largest-scale case

The Chinese dual-teacher classroom, a remote expert paired with a local facilitator at
enormous scale, returns exactly one record in ERIC.

That one record says the failure mode was **emotional and not
informational.** The remote expert delivered the content adequately; what broke was
the relationship in the room.

Read against everything else here: **the layer AI would most naturally replace was
already the weak one.** The instruction was never the scarce good.

---

## 7. What the inventory obliges us to build

- **Build the 63 before rebuilding the 16.** Most of this craft is invention and not
  compensation, and a responsive system does not supersede it.
- **Curate as well as generate.** Bucket D cannot be derived from a learner model,
  and a system that only generates will be responsive and shallow.
- **Ship manipulate-before-explain as a hard ordering rule.** Widget, then prose,
  one degree of freedom, no advance until something moves.
- **Choose figures that discriminate.** Prediction has no main effect; the
  expectancy violation carries all of it, so a confirming prediction is wasted cost.
- **Hold the productive-failure tension open.** Intervening on the wrong kind of
  stuck is a design claim we have not measured, and the honest position is that it
  is unresolved.
- **Name the price of personalisation.** An explanation nobody else has seen cannot
  be discussed with anybody.

A decade of craft was developed by people who could not see their learners, and most
of it turns out not to depend on that. The constraint was incidental. What these
people were doing was discovering how explanation works, and the one-way medium
merely happened to be where they did it.


## 17. Explaining Hard Things — the fidelity invariants, instantiated

<sub>Source report: `derived — see provenance note in §1`</sub>

Section15 established a rule for when a simplification is legal: **monotone
refinement.** A rung may drop precision, formalism, or mechanism-depth. It may never
falsify **ontology, causal sign, quantifier strength, or uniqueness of mechanism**.

That rule is correct and, as stated, nearly unusable. Four abstract invariants do not
tell an author what to check on a Tuesday. This section instantiates them: which one
breaks in which domain, what the breakage looks like, and what a machine can check.

**Provenance, stated because this section's evidential status differs from the rest.**
What follows was derived by applying §15's rule to two live cases: graduate
mathematics, and a specific published explanation of energy-based models. It was not
retrieved from a literature. The invariants themselves carry the evidence of §15. The
instantiations are `INFERENCE`. Where a claim below is measured, it is labelled and
sourced; where it is derived, it says so. We flag this so the section does not
borrow §15's authority.

---

## 1. Which invariant breaks, by domain

The four invariants are not equally at risk. In each field, one of them is where
almost all bad explanation dies.

| Domain | The invariant most at risk | What the failure looks like |
|---|---|---|
| **Mathematics** | **Quantifier strength** | ∀∃ silently reordered |
| **Physics / engineering** | **Uniqueness of mechanism** | A determined quantity presented as a tunable choice |
| **Computer science** | **Ontology** | Process and object conflated — a function as *a rule you run* versus *a value you pass* |
| **Biology / medicine** | **Causal sign** | Correlational mechanism narrated as causal, direction unmarked |
| **Statistics** | **Quantifier strength** again | "The probability the hypothesis is true", which reverses the conditional |

This is a design table and not a finding. Its use is that it tells an author *what to
check first*, and it tells a verifier which predicate to spend its budget on.

---

## 2. Mathematics: quantifier strength is the whole game

> "For every ε there is a δ" and "there is a δ that works for every ε" are the
> difference between continuity and **uniform** continuity, and the entire second
> half of a real-analysis course.

Nearly every "intuitive" explanation of a limit, a convergence, or a bound quietly
reorders those quantifiers, because the reordered version is easier to say. The
student computes correctly for two years and then cannot understand uniform
convergence, and the trace goes back to a sentence nobody flagged.

**This is mechanically checkable on written statements**, with a scope limit we
established by testing it. Implemented and run against 1,524 sentences of lecture
transcript, the check **fired zero times**: speech *elides* quantifiers rather than
reordering them, so there is no prefix to compare. It is a check for **authored
technical prose and generated output**, and not for transcript mining (C-50). Within that
scope: an explanation is legal iff **its quantifier prefix is entailed by the formal
statement's, under the declared scope.** That is a predicate and not a matter of taste,
decidable at the cheap rung of the grounding ladder given both statements.

### The ontological crossing that follows it

Chi's test says errors *within* an ontological category are repairable and errors
*across* categories are robust. The Bohr-model hybrid population was **unchanged
across a full semester** of university chemistry (§15).

Mathematics has its own canonical crossing: process versus object. A limit as
*something you do* versus *a number that exists*. A function as *a rule you apply*
versus *a point in a space*.

A student holding "limit" in the process category can compute limits indefinitely and
cannot understand uniform convergence, because uniform convergence quantifies over a
space of functions, which requires functions to be objects first. The
misconception survives instruction exactly as Chi's test predicts, because the repair
is a category change and not a correction. `INFERENCE`, from Chi's mechanism plus
the process/object literature in mathematics education.

---

## 3. Two failure modes worth naming

These are the section's original contributions, and both are checkable.

### 3.1 Machinery before obstacle, and the experiment that narrows it

**An explanation that presents machinery before the obstacle the machinery exists to
dodge makes the machinery look arbitrary.**

**Corrected 2026-07-29, and the correction is more useful than the original claim.**
Muller's doctoral work (Sydney, 2008) ran the nearest thing to a controlled test of
this, and it points somewhere else. His Refutation condition is the Exposition
script verbatim, plus explicit statements of the misconception, in the same
definitions-first order, with no reordering at all. It scored d = 0.79 against the
Exposition.

So in the one experiment that isolates it, the load-bearing variable is **naming the
wrong idea**, not the order in which the machinery arrives. Ordering may still help;
it has not been shown to be what does the work, and this section originally implied
it was. See §29.3.3.

The original argument was mechanistic. Machinery before obstacle leaves the reader
with no slot to put it in. They remember it as a list of tricks, cannot
reconstruct it, and cannot tell which parts are essential and which are incidental —
which is precisely the failure that makes an explanation feel clear and leave nothing
behind. It is a fluency illusion with a specific cause.

The rule, narrowed by the correction above: name the wrong idea explicitly. The
obstacle-first *ordering* is a plausible way to do that and is not what the evidence
isolates. Muller's Refutation condition kept the original order and simply stated the
misconception aloud. So: say what does not work, out loud, before or after the
machinery. The naming is the mechanism; the position is a preference.

This is checkable in a weak but useful sense — for a technical explanation, does the
obstacle appear before the first piece of machinery it motivates? That is a structural
predicate over an outline and not a judgement about prose.

### 3.2 A determined quantity presented as tunable

This falsifies uniqueness of mechanism, and it is endemic in engineering
explanation.

When a quantity is *determined* by a conservation law, a stationarity condition or a
dimensional constraint, and the explanation presents it as a knob someone chose, the
reader concludes the design is taste. They will then tune it, and be confused when it
breaks, because they were told it was theirs to set.

The check: for each numeric constant in an explanation, is it (a) determined by a
stated condition, (b) empirically fitted, or (c) arbitrary? All three are fine. Not
saying which is the violation.

### 3.3 Name the misconception

Three experiments, one thesis, and it is the closest thing the field has to a direct
test of what makes an explanation teach.

| Condition | Content | Gain |
|---|---|---|
| Exposition | Clear, correct, 7:02 | 1.77 |
| Extended | Same, longer, 11:22 | 2.41 |
| **Refutation** | Exposition **verbatim + the misconception named**, 9:33 | **4.41** |
| **Dialogue** | Two speakers, one holding the misconception, 11:22 | **4.77** |

N = 364, F(3,461) = 13.625, p < .001; **d = 0.83** for Dialogue, **d = 0.79** for
Refutation. Replicated at n = 73 on quantum tunnelling (d = 0.71).

And the same thesis contains the felt/real dissociation, measured. On the opinion
form, *"I learned something from the video"* scored **5.7 for Dialogue against 5.6 for
Exposition — flat**, while actual learning differed by d = 0.71. Perceived clarity did
not differ either. What *did* differ: students found the better format more dull
(p < .01) and said they would rather see the worse one in lectures (p < .05).

The author's own conclusion is the sentence this survey has been circling for eighty
thousand words:

> *"They believed they learned the same amount as students with double their learning
> gains. Thus the expositions actually strengthened misconceptions."*

**A clear explanation of a concept the learner has a wrong model of does not overwrite
the wrong model. It sits alongside it, and raises confidence.** That is why clarity is
not the goal, and why "was it well explained?" is the wrong question.

One further result from the same work, on the prediction step this survey recommends
elsewhere: *"students who witness demonstrations without being asked to make a
prediction perform as well on follow-up tests as those who don't see the demonstration
at all."* The demonstration is worth nothing without the commitment that precedes it.

---

## 4. Worked example: energy-based models

A test of whether any of this improves an explanation that is already good. The
subject is a published walkthrough of energy-based generative models: energy
landscape, a particle in a fluid, rolling downhill while wandering, a persistent
replay buffer. The physics framing is the right instinct. Three things sharpen it.

### 4.1 Lead with the uncomputable constant

Every piece of machinery in an energy-based model exists to dodge one fact:

> **You can write the probability of any image up to a constant you cannot compute.**

*p(x) = e^(−E(x)) / Z*, where *Z* integrates over every possible image. In 784
dimensions that integral is not hard; it is hopeless.

Introduce *Z* as the antagonist first and every later step is *forced* rather than
clever. Introduce the landscape first and the reader meets Langevin dynamics,
contrastive divergence and replay buffers as three unrelated tricks. Same content,
different retention — §29.3.1.

### 4.2 The one line the method turns on

∇ₓ log p(x) = −∇ₓ E(x), because *Z* is constant in *x* and vanishes under the
gradient.

You cannot evaluate the probability. You can always compute *which direction makes it
go up* — and sampling only ever needs the direction. Most treatments bury this in the
derivation. It is the hinge, and it belongs at the top of rung 2.

### 4.3 The noise scale is not a knob

"Rolling downhill while wandering" is the right picture with the *why* missing.
Gradient descent finds a mode. You do not want the most likely image; you want a
*sample*. So Langevin adds noise:

*x*ₜ₊₁ = *x*ₜ − (ε/2)∇E(*x*ₜ) + √ε · *z*ₜ

The √ε is not a hyperparameter. It is the unique scale at which the stationary
distribution equals *p*. Present it as tunable and you have falsified uniqueness of
mechanism — §29.3.2, exactly.

And the persistent replay buffer stops being a hack once the tug-of-war is visible:
training pushes energy *down* on real data and *up* on model samples, and the "up"
push lands wherever the negative samples happen to be. Unconverged samples mean
pushing up in the wrong places — teaching the model to distrust regions it should
like. The buffer maintains a population near equilibrium so that after the landscape
shifts, the samples are still approximately right.

Note what that is: continuity of state across steps, because recomputing from
scratch each time is biased and slow. The same argument this survey makes for
persistent learner state (§12), in a different domain.

### 4.4 The three rungs

Three rungs, because five did not beat three at **p = 0.738** (§15).

| Rung | The claim |
|---|---|
| **1** | A network scores images. Real ones score low, everything else high. To make an image, start from noise and walk downhill while jittering. |
| **2** | The score is an unnormalised log-probability. The normaliser is uncomputable, but its gradient is zero — so sampling works where evaluating does not. The noise scale is fixed by requiring the correct stationary distribution. |
| **3** | Maximum likelihood on −E − log Z; ∇_θ log Z = −𝔼_{p_θ}[∇_θ E], estimated by MCMC. Persistent contrastive divergence approximates that expectation with a maintained chain, because a fresh chain per step is both biased and slow. |

Every rung is entailed by the one below it. Rung 1 drops the normaliser entirely,
which is legal because it drops precision. It does not claim the score *is* a
probability, which would falsify ontology.

---

## 5. What the probe should ask

§11 established that entry must be measured, never preferred: preference moves
d ≈ 0.48 while knowledge moves zero, and rapid dynamic assessment recovers an
actionable estimate from 1–3 items in 15–40 seconds at r = 0.66–0.92 against full
diagnostics.

This section adds *what the probe should ask*. **Probe on the obstacle, not the
definition.**

- Weak probe: *"What is an energy-based model?"* — separates people who have read a
  definition from people who have not.
- Strong probe: *"Why can't we just compute the probability directly?"*

The second sorts by whether the reader holds the *constraint that generates the
field*. Someone who can answer it belongs at rung 2 whatever their credentials;
someone who cannot will not understand rung 2 however much they have read.
`INFERENCE`. This follows from §29.3.1 and not from a trial, and testing it is cheap.

---

## 6. Graduate level: the tutor's job inverts

Guidance measures **d = −0.428 for experts**. Worked examples, scaffolding and
explicit instruction — the strongest interventions that exist for a novice — are an
*active harm* here. A tutor that explains beautifully to a graduate student is doing
the wrong job well.

What remains, in order of value:

1. **Numeric falsification before symbolic proof.** A numeric check catches 99.1% of
   seeded derivation errors in **0.38–0.61 ms** with zero false alarms; symbolic costs
   roughly 3× for +0.9 points and carries a **38.3% XFAIL/SKIP hole** in SymPy,
   concentrated in sums (70%), definite integrals (57%) and inequalities (47%) — the
   areas graduate work lives in. Substitute random values before proving. Most wrong
   conjectures die in a millisecond.
2. **The adversary, unannounced.** The referee who supplies the case the proof forgot.
   *Announced* devil's advocacy measurably produces bolstering of the original view
  (§20), so the objection must be owned, not performed.
3. **Explaining it back, with the expectancy set first** — g = 0.48 with, **g = −0.02**
   without (§14). This is why seminars work and "any questions?" does not.
4. **Formal verification where it earns its cost**, and honestly: 97% autoformalisation
   × 69% proving yields **36% end-to-end**, because the formal statement stops matching
   the informal one (§23). The kernel moves the trust boundary; it does not remove it.

Explanation is fourth at best, and the explanation that counts is the learner's.

---

## 7. What an author must check first

- **Instantiate the invariant before authoring.** Name which of the four is at risk in
  this domain, and check that one first.
- **In mathematics, check the quantifier prefix.** It is decidable, it is cheap, and it
  is where the damage is.
- **Obstacle before machinery**, always. If the reader does not know what fails, every
  fix looks arbitrary.
- **Label every constant** as determined, fitted, or arbitrary. Silence on this point
  is a falsification of mechanism.
- **Probe on the obstacle.** A definition question measures reading. An obstacle
  question measures understanding.
- **At expert level, stop explaining.** Falsify, object, and let them teach it back.

A simplification is legal when the reader can still tell what would break. Everything
above is that sentence made checkable, one domain at a time.


## 18. The Explanation Atlas — the head-to-head literature exists, filed under refutation text

<sub>Source report: `research/raw/N4-explanation-atlas.md`</sub>

There is an outstanding explainer in almost every field, and their work is public.
The obvious idea is to find the best explanation of each concept, learn what makes it
work, and build delivery on that.

The idea survives investigation. Almost nothing about how you would *identify* the
best explanation does.

---

## 1. The literature exists, filed under a name nobody looks up

We predicted this literature would be empty. It is not. Head-to-head comparisons of
explanations live under **refutation text**.

Pooled across 44 studies: **g = 0.41 raw, g = 0.28 after trim-and-fill.** A real
effect, with a publication-bias correction that removes a third of it.

Then the part that matters for anyone building on it: **exactly two studies in that
meta-analysis exceeded one month, and transfer was never coded at all.**

So the field knows that naming a misconception beats explaining cleanly, at short
delay, on retention-style items. It does not know whether the advantage survives to a
month, and it has never asked whether it transfers.

And the strict question (*two real published explanations, head to head, on a
learning outcome*) has **one journal-quality instance in the entire literature.**

---

## 2. Replay density does not mark confusion

Views and likes are the felt axis; this survey has said so throughout. The hope was
that behavioural platform signals might be diagnostic where attitudinal ones are
not, specifically that **rewind density** marks where comprehension failed.

That hypothesis is dead, and it died three separate times.

Measured. YouTube's "most replayed" heatmap was extracted for 51 videos and
analysed. Median entropy 0.976, where 1.0 is perfectly flat. Enrichment over
uniform: 1.95×. Peaks explain roughly 16% of variance by concept, and land
closer to chapter boundaries than chance (49.8s versus 87.6s), so they mostly mark
navigation and not confusion. Worse, the sign may be backwards: Brinton et al. found
backward-scrubbing predicts getting the *next question right*, which is engagement
and not confusion.

Structurally foreclosed. The signal is **min–max normalised within each video in
51 of 51 cases.** Every video has a peak at 1.0 by construction. Cross-video
comparison, the entire point of an atlas, is impossible from this data.

And it was already built. LectureScape (UIST 2014) implemented exactly this
interface. It was null on every task, *slower* than baseline outside peaks, and
significantly better on perceived efficiency. The felt/real dissociation, appearing
in the tool built to escape it.

The distinction between attitudinal and behavioural signals was the right one to
draw. Drawing it properly is what killed the proposal.

---

## 3. We ran our own predicate as code, and it mostly did not fire

Section17 proposed that a simplification is legal iff its quantifier prefix is
entailed by the formal statement's, and called this *"decidable, cheap, and the most
valuable entry in the table."*

It was implemented and run against **1,524 sentences of MIT OpenCourseWare
transcripts.**

> **The quantifier-prefix check fired zero times.**

Not because the explanations were flawless. Because **speech elides quantifiers rather
than reordering them.** A lecturer says "as close as you like" and never utters ∀ or ∃
in any recoverable form. The predicate is decidable on *formal statements* and
near-inert on *spoken explanation*, which is the medium this whole section is about.

Overall lexical precision across all §17 predicates: **7 true positives from 30 flags,
or 23%.**

That does not refute the design. It relocates it: these predicates are for **authored
technical prose and generated output**, where quantifiers are written, and not for
transcript mining. They are a stage-two check on a generator's output and not a
stage-one filter on the world's video.

We are recording this because a predicate this survey called its most valuable
contribution has now been tested, by us, and mostly did not work.

---

## 4. One feature predicts a good explanation, and it has a number

Amid all of that, one feature has a measured effect size, and it is the one Muller's
thesis isolates: which misconception the explanation names.

His four versions of the same physics content, measured:

| Version | Gain |
|---|---|
| Exposition — clear, correct | 1.77 |
| Extended — same, longer | 2.41 |
| **Refutation — the same script, plus the misconception named** | **4.41** |
| **Dialogue — two speakers, one holding the misconception** | **4.77** |

And in the same work, perceived learning was **flat (5.7 vs 5.6)** while real learning
differed by **d = 0.71**. The better format was rated significantly duller, too long,
and less wanted in lectures.

Every one of those three is a signal a recommender system acts on. **A platform
optimising for watch-through would systematically down-rank the version that
teaches.**

---

## 5. The design, and the falsifier that is free today

`DESIGN`, the explanation atlas. Harvest candidate explanations per concept, grade
them mechanically, measure delayed unassisted transfer on a subset, and learn which
graded features predict the outcome. Once features predict, you can select or generate
without running a trial each time.

But the ordering has changed.

Build the error atlas first. The explanation atlas's only feature with a measured
effect is *which misconception it names*, and that is worthless unless you know which
misconceptions a population actually holds. The error atlas is what produces that
list. The two are sequenced and not parallel.

Two practical constraints reinforce it. The error atlas has a corpus already built and
lawfully available. The explanation atlas's interesting corpus is legally foreclosing:
captions now return 200 with zero bytes, and an anti-circumvention suit was heard in
August.

And the decisive test costs nothing. Muller published four explanations of the
same content with measured outcomes. Grade them with §17's predicates and see whether
the grader recovers the order.

> **If it ranks the clean Exposition highest, §17 measures tidiness rather than
> teaching.**

That is a day's work, it needs no learners, and it should be done before anything is
spent.

---

## 6. The rules for grading an explanation

- **Never rank an explanation by platform metrics**, including behavioural ones. The
  replay signal is flat, normalised within video, already built, already null, and
  possibly sign-reversed.
- **Name the misconception.** It is the only explanation feature with a measured effect
  size, and it beats clarity by more than double.
- **Confine §17's predicates to authored and generated text.** They do not fire on
  speech, and we said they were our most valuable contribution before testing them.
- **Sequence the atlases.** Errors first; explanations are graded *against* the errors
  they name.
- **Run the free falsifier first.** Four published explanations, known outcomes, one
  day.

The instinct behind this section is sound: somewhere there is a better explanation of
every concept than the one in the book, and it is probably free. What this survey can
now say is that finding it by popularity selects against it, and that the one
property worth grading for is whether it names the thing the learner already believes.


## 19. Nobody Needs a Better Scheduler — the science of durable remembering

<sub>Source report: `research/raw/F11-scientific-remembering.md`</sub>

Spaced repetition is the most beloved technique in self-directed learning, and the
part of it everyone optimises is the part that does not matter.

That is a strong claim. It rests on 126 sources, 68 registered null results, and a
350-million-review benchmark that the algorithm's own authors publish.

---

## 1. The two effects that survive everything

Start with what survives, because it is the foundation of everything else in this
survey:

| Practice | Effect | Base |
|---|---|---|
| **Retrieval practice** | **g = 0.499** [0.442, 0.557] (§1)| 222 classroom studies, 48,478 students — **I² = 88%** |
| **Spacing / distributed practice** | **d = 0.54** [0.31, 0.77] | 22 reports, 31 effects, N > 3,000 (classroom meta-analysis, 2025). Cepeda et al. 2006 is the canonical lab meta-analysis |

These are among the largest, most replicated effects in all of learning science.
Testing yourself beats re-reading. Spreading practice out beats massing it.

They are also *heterogeneous*, and that belongs in the same breath:
retrieval practice carries **I² = 88%**, moderated by the control condition, test-format
consistency, feedback, and number of repetitions. Two boundary conditions matter for
design. At an *immediate* test, restudy often wins — the retrieval advantage appears at
delay. And unsuccessful retrieval without corrective feedback yields little or
nothing, which makes feedback part of the intervention itself. Spacing
is not scale-free either: **d = 0.11–0.42** for motor tasks, much larger for simple
verbal material.

None of that weakens the recommendation. If a system does nothing else, it should do
these two things, and do them relentlessly, with feedback attached and the test
delayed.

Nothing that follows weakens either finding. What follows is about a *third*
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
   **4.6**. The reported scoreboard is gameable, and they said so.

Credit where it is due: publishing your own metric's exploit is better science
than most of this field manages.

But note what these benchmarks are. They are backtests on logs of what learners
already did. Predicting whether a review will be recalled is not the same
quantity as causing more to be remembered. A backtest is not an intervention, and
the scheduling literature has almost no interventional evidence at all.

---

## 3. Expanding intervals: verified null, and the mechanism recovered

The single most-repeated claim in spaced repetition is that intervals should
*expand* (review at 1 day, then 3, then 7, then 21) because retrieving at the
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

Dobson (2012, n = 250, 29 days) is the counterexample. It is reported here in
full.

---

## 4. The boundary of the entire paradigm

This table should govern what anyone builds:

| What was scheduled | Trials significant |
|---|---|
| Paired associates / flashcard-type material | **11 of 14** |
| **Interdependent content** — where one idea depends on another | **0 of 8** |

An earlier draft printed that table without the headline it came from. Across
the review's full set of **41 studies from 34 papers**, the authors write: *"We find
that over half of the studies found that RL-induced policies significantly outperform
baselines."* **21 of 41 (51%) significantly beat all baselines**; 10 found no
significant difference; 1 where the baseline won. Publishing the 0-of-8 sub-cut
without the 21-of-41 headline is selective reporting, the exact failure this
survey exists to name. The domain split above is real and it sits inside a review whose
overall verdict is positive.

The authors' own qualifier is the load-bearing part: RL *"has been most successful in
cases where it has been **constrained with ideas and theories from cognitive
psychology and the learning sciences**."* Which is an argument for the architecture in
this document, and not against it.

Adaptive scheduling works on material with no internal structure and has never
worked on material with structure. Every trial that tried failed.

Supporting evidence points the same way. Duolingo's half-life regression, tested
against plain Leitner boxes on roughly one million students, produced **+0.3%
engagement (not significant) and −7.3% practice (significant)**. The adaptive
scheduler made people practise *less*. The famous "+12%" figure comes from a
different experiment and does not describe this comparison. Kerfoot's adaptive
trial: p = 0.37. Cen 2007: p = 0.772 on posttest, p = 0.602 on retention, with 12%
time saved. Mettler's adaptive system was beaten on raw accuracy by a random
schedule (d = 0.746).

And knowledge tracing, the sophisticated cousin, does not rescue it. Roughly
**82% of deep knowledge tracing's founding gain was an evaluation-procedure
artefact plus a forgetting term; an untrained LSTM is within 0.03 AUC** of the
trained one; and an oracle that *knows the exact moment learning occurred* beats
simple logistic PFA by **0.002**.

That last number deserves a moment. If perfect knowledge of the thing these models
are trying to infer is worth two thousandths of AUC, the modelling target is
nearly exhausted. The remaining headroom is not in the model.

---

## 5. The named product, assessed fairly

This section was commissioned partly to evaluate zemomemo.com. It is a free
SvelteKit flashcard application built on FSRS-6, with five study modes, LLM deck
generation, and Quizlet and Anki import. It is competent, it is free, and
people plainly find it useful.

It cites no study, trial, or efficacy datum; its only external reference is the
FSRS community wiki. Four observations place it precisely:

- Its **"stickiness — the number of days a flashcard will stay in your brain"** is
  FSRS's *stability* parameter (the interval at which recall probability falls to
  90%), rendered to the user as a deterministic expiry date. A probabilistic
  quantity presented as a certainty.
- "Achieve mastery same day" together with "remember forever" straddles a
  combination that Cepeda's 271 massed-versus-spaced comparisons do not support
  (12 exceptions).
- The same-day regime it markets hardest is the regime FSRS's own benchmark
  excludes from its headline table — and where FSRS-6 performs worst.
- FSRS-6 is a version behind FSRS-7.

None of this makes it a bad product. It makes it a product, and the distinction
this survey exists to hold is between a competent tool and a scientific claim.

---

## 6. What actually becomes buildable

Here is where this gets interesting, because the null results above clear space
instead of closing it. Every capability below is currently at `DEMO` or
confounded-`OBSERVED` (nobody has run the trial), and each is now cheap.

Generate the cue instead of storing it. A flashcard is a frozen question,
which is why the paradigm only works on unstructured material: the card *is* the
atom. If the question is generated at retrieval time from the concept, then the
same knowledge can be probed from a different angle every time, and recognition of
the card can no longer be mistaken for knowledge of the thing.

Schedule concepts, not cards. This is the direct attack on the 0-of-8 result.
Structured material failed under card scheduling because scheduling operated on
the wrong object. Schedule the *concept*, with its prerequisites, and derive the
probe.

Separate recognition strength from generative competence. These are different
memories and current systems conflate them. A learner who recognises the answer
instantly and cannot produce it unprompted has one and not the other — and only
the second is what anyone means by knowing.

Detect inert knowledge. Retrievable when cued in the original context, and
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
  a number behind it: Bertsch's anagram condition, difficulty that is merely
  perceptual rather than conceptual, is **d = −0.05**. Making the *reading* harder
  is not a desirable difficulty. Making the *retrieval* harder is.

And the cheapest experiment in the document, which follows directly from §30.3:

> **Push the first retrieval later.** One parameter, a meta-analytic prior, and a
> mechanism dissociated in an existing experiment. If the effect is where
> Karpicke and Roediger's Experiment 3 says it is, this is nearly free.

---

## 8. The practices we ship, and the knob we leave alone

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

The sophisticated-looking component (the scheduler, the deck, the avatar, the
debate among agents) turns out to carry almost none of the effect. What carries
it is something simpler and harder: **that the learner actually retrieved, actually
struggled, actually explained, and actually got told when they were wrong.**

The machinery is worth building. It is just not worth mistaking for the mechanism.


## 20. Beyond the Tutor — the five roles nobody is building

<sub>Source report: `research/raw/F2-beyond-the-tutor.md`</sub>

Say "I'm going to play devil's advocate for a moment" and you have just made your
interlocutor harder to move.

Nemeth, Brown & Rogers (2001, *European Journal of Social Psychology*) compared
role-played devil's advocacy against authentic dissent. Authentic dissent produced
divergent thinking — more solutions, considered from more angles. The assigned
devil's advocate produced "thinking that was primarily aimed at **cognitive
bolstering of the initial viewpoint** rather than stimulating divergent thought."

Announced opposition makes people defend harder. It does not make them think wider.

That result governs the most obvious way to build an AI that argues with a learner,
and as far as this project's search could determine it appears nowhere in the
AI-education literature. It is one of six roles an AI can occupy in learning, five
of which are essentially unbuilt.

---

## 1. The design space has one point in it

"AI tutor" is the default not because the evidence favours it but because it is the
shape an instruction-tuned assistant already has: knowledgeable, helpful, agreeable,
responsive. **That shape is a training artifact, not a pedagogical finding.**

Three questions distinguish the roles: who holds the knowledge, who holds the
goal, and who bears the cognitive load. The last one decides everything, because
transfer follows load.

| Role | AI's stance | Who bears the load | Evidence |
|---|---|---|---|
| **Tutor** | Knows more, dispenses | The AI, at the limit | Strong for constrained tutors; **strong for harm** when unconstrained |
| **Student** | Knows less, asks, errs | The learner, fully | Strong for human tutees; thin for AI tutees — §13 |
| **Peer** | Knows comparably, commits | Shared, symmetric | Strong for human peers; **theoretical only** for AI |
| **Adversary** | Knows, withholds, attacks | The learner, fully | Strong for the human analogues; almost no AI outcome data |
| **Environment** | No stance; holds consequences | The learner | Strong in principle, barely instrumented |
| **Instrument** | Extends a human's capability | The human who owns the task | Best evidence-to-deployment ratio of the six |

The tutor role is the only one requiring the AI to be knowledgeable and agreeable.
It is also the only one with documented harm at scale: **§2 and §3 carry the −17%
unassisted-exam result and the guardrail correction, and this section does not
re-argue them.** The student role already has a section too. **§13** covers the
protégé effect, knowledge-telling, capability leakage and the Betty's Brain
architecture, and **§14** covers the learner as explainer. Everything below is what
is left.

---

## 2. The adversary

### 2.1 Why dissent works, and why it does not need to be right

Nemeth's core asymmetry (1986/1987): exposure to opposing views from a **minority**
produces divergent thinking, and performance improves. Exposure to opposing
**majority** views produces convergent thinking — narrowing onto the proposed view,
which does not help and can impair.

The dissenter's value does not depend on the dissenter being right. It depends
on the dissent being real.

That is a remarkable licence for an AI adversary, because it means the objection
does not have to be correct to be useful. The 2001 result above revokes the licence
immediately, because it also means the objection cannot be performed.

### 2.2 The dilemma, stated fully

- If the AI announces "I'll argue the other side," it is a *known* devil's advocate.
  Nemeth's condition. It produces cognitive bolstering — **the learner ends more
  confident in the view they started with.** Worse than doing nothing.
- If the AI dissents without announcing, it is authentically dissenting from the
  learner's standpoint and produces divergence. It may also assert things it does
  not hold, misrepresenting its own epistemic state.

The resolution this project proposes is a design hypothesis and is labelled as one.
**Do not have the model perform opposition. Have it stop suppressing the objections
it already computes.** Not "I'll take the other side" but "I actually don't find
that convincing, and here is specifically why" — where the *why* is the model's own.

That reframes anti-sycophancy work usefully. We do not need models that pretend to
disagree. We need models that stop suppressing disagreements they have already
generated. That is a far more tractable engineering target, and directly
testable: divergent-thinking and learning outcomes under (a) announced devil's
advocate, (b) unannounced authentic objection, (c) agreeable baseline. The template
exists. Marvel & Ju (2026) ran a pre-registered **N = 1,492** study crossing a
sycophantic against a challenger model with disclosure conditions. The educational
version has not been run.

### 2.3 What the adversary costs

Two boundary results keep this honest.

Children experience persistent questioning as pushy. A 2024 study of elementary
students with a Socratic chatbot is titled "This Chatbot is Kind of Pushing It!" and
the title is the finding. Satisfaction and pedagogical value diverge, which is what
desirable-difficulty theory predicts and what a five-star rating loop will destroy.
An adversary role cannot be tuned on satisfaction.

And adding help to the struggle does not help. Sinha & Kapur (2021) compared
problem-solving-before-instruction, *scaffolded* problem-solving-before-instruction,
and alternative sensemaking activities across **118 comparisons**: scaffolding
showed a small descriptive advantage and **no significant difference, g = −0.08
[−0.20, 0.04].** The struggle phase does not want a co-pilot.

One more constraint, because "let them struggle" is as over-claimable as "give them
a tutor": the instruction phase is mandatory. Productive failure is problem
solving *followed by* instruction, and consolidation must contrast the learner's own
failed attempts against the canonical solution. An AI that only obstructs is as
wrong as one that only helps.

---

## 3. The simulated peer, and the one thing AI cannot fake

The strongest result in the peer literature is also the strangest.

Smith et al. (2009, *Science*) ran the decisive experiment on peer instruction.
Students answer a concept question alone, discuss with neighbours, revote —
correctness rises. Is that learning, or social copying from whoever knew? They
followed with a second, isomorphic question answered individually:

> **"Peer discussion enhances understanding, even when none of the students in a
> discussion group originally knows the correct answer."**

The mechanism is not transmission. It is articulation, commitment, and the
reconciliation of conflicting commitments. **Two wrong students arguing produce
understanding neither had.** Smith et al. (2011) added the sequencing: peer
discussion followed by instructor explanation beat either alone, substantially.

So can an AI hold the peer position? Three obstacles stand in the way, and they are
not equally tractable.
Known asymmetry: the learner knows the model has read everything, so a model
asserting a wrong answer is either deferred to or dismissed as roleplaying, and
neither is peer engagement. No stakes symmetry: a human peer is embarrassed to
be wrong, and that embarrassment is what makes the commitment real. Capitulation:
a peer who abandons their position the moment you push back supplies nothing to
reconcile, and measured capitulation rates sit around **58%** with **78.5%
[77.2, 79.8]** persistence once it happens, figures §13 works through.

And one collaborative structure is flatly unavailable. Jigsaw works by **positive
interdependence under genuine information asymmetry**: each learner holds a unique,
necessary fragment and the group cannot succeed without every member. An AI cannot
supply this. Any asymmetry is simulated, and the learner knows the model could
produce the other fragments on request. **Jigsaw requires scarcity of knowledge, and
AI is defined by its abundance.**

The honest verdict: the peer role is the weakest of the six for AI, and "AI
study buddy" is the least defensible product framing in the category. The salvage
is not to fake symmetry. It is to be a committed adversary, or one voice among
several. Both preserve the conflicting-committed-positions mechanism
without requiring a symmetry that does not exist.

---

## 4. The audience, and the environment that cannot flatter

### 4.1 Why an audience matters at all

Two findings from independent literatures converge on a single mechanism.

Rosenshine, Meister & Chapman (1996) meta-analysed teaching students to **generate
questions: median ES 0.36 on standardised tests, 0.86** on
experimenter-developed ones. Their most useful sentence is the deflating one — "the
traditional skill-based instructional approach and the reciprocal teaching approach
yielded similar results." The *format* was not the intervention. The
question-generation skill was.

That matters for role design in a way builders consistently miss. **What transfers
is the learner's acquired disposition to interrogate material.** Any AI that
performs the questioning *for* the learner captures the performance and destroys the
disposition — which is exactly the shape of Mousazadeh's (2023) null: explainable
ChatGPT improved performance on the specific tasks it explained and produced **no
generalised gains in metacognitive knowledge or writing.** Targeted transfer, no
metacognitive transfer, precisely as you would predict if the AI is doing the
monitoring.

### 4.2 The environment role

The environment holds no epistemic stance toward the learner. It holds
consequences: a simulation that diverges, a failing test suite, a patient that
deteriorates, a quiz the agent you taught then fails.

This is the only role where disconfirmation is structural instead of social,
and that property does more work than any amount of model tuning. A unit test cannot
be sycophantic. A simulation cannot be talked round. The error surfaces as a
consequence, and not as a correction from an authority, which also preserves the
ego-protection that makes teaching-an-agent work for low-confidence learners.

If agreeableness is the master obstacle, the environment is the master mitigation.
It is also a systems-architecture choice, not a model-alignment problem.

§13 describes the architecture in its teachable-agent form. The generalisation is
broader: for any role, prefer a design where being wrong has a visible non-social
consequence over a design where being wrong requires the model to say so.

---

## 5. The coach

The instrument role, AI extending a human's capability on a task that human still
owns, has the best evidence-to-deployment ratio of the six and receives the least
attention, because "AI helps a teacher be better" is a worse pitch than "AI replaces
the teacher."

Tutor CoPilot supplies real-time suggestions to *human* tutors during live sessions.
The AI never faces the learner. Its distributional signature is the interesting
part: the largest gains went to the least experienced tutors — the inverse of
the pattern where unstructured AI access widens the gap between low- and
high-prior-knowledge students.

The result is also sharply limited, and §3 carries the numbers: a proximal exit-
ticket gain alongside a distal null. Treat it as the cleanest demonstration that the
instrument role is real and that its distal effects are unproven. Do not treat it as
a headline.

---

## 6. The nulls this section has to carry

Announced adversarialism backfires. Nemeth, Brown & Rogers (2001). The obvious
implementation of "AI adversary", telling the learner you are about to argue the
other side, is the one that produces bolstering instead of divergence. This is the most
consequential negative result in the section and it is why §31.2.2 exists.

Fluency raises confidence and ratings with no effect on learning. Carpenter and
colleagues, across **five studies from 2013 to 2020**, found that a fluent
instructor produced higher judgments of learning and higher instructor ratings with
zero gain in actual learning. An LLM is a maximally fluent instructor by
construction. This is the most directly transferable warning in educational
psychology and it is essentially absent from AI-education discourse. The felt/real
dissociation itself is established in **§36** and **§22**; the transferable part
here is that *fluency of delivery* is one of its cheapest triggers.

Perceptual disfluency failed to replicate. Bjork & Yue (2016), from the
originators of desirable difficulties: hard-to-read fonts largely do not work.
Difficulty per se is not the mechanism; retrieval and generation are. **Do not build
an AI that is gratuitously hard to read. Build one that makes you generate.**

LLMs had no main effect on overall learning. Lehmann, Cornelius & Sting
(2024/2025), pre-registered lab experiments plus a field study. The effects were
entirely in the *usage pattern*. Substitution use, generating the solution, broadened
coverage while reducing depth; complementation use, asking for an explanation,
deepened understanding without broadening. And LLM access widened the gap between
low- and high-prior-knowledge students, a property §27 establishes belongs to
untargeted delivery and not to the technology.

The socially engaging agent is not a universal win. Tärning, Haake & Gulz (2011)
added a social chat module to a teachable-agent maths game. High- and mid-achievers
improved. Low-achievers disliked it, chatted more, and went off-task more — the
learners who most need the ego-protection property were the ones the social framing
cost. An aptitude–treatment interaction masquerading as a feature.

And one paper must be flagged, never cited. A 2025 quasi-experimental study
titled "AI as a Socratic Dialogue Partner," with a critical-thinking instrument as
its outcome, describes its own findings as hypothetical. It is unverifiable as
evidence and it will be cited by others as though it were not. We name it here so
that nobody, including us, launders it later.

---

## 7. The counter-argument, and the sequence

The strongest objection is that the tutor role is not empty. Kestin et al. (2025)
is a genuine randomised result in an authentic course, at **d ≈ 0.63**, and it
belongs in the ledger — with the caveats §3 records, including that the tutor was
built and evaluated by its developers and was **explicitly pedagogically
constrained** rather than a helpful assistant. The comparison was
AI-with-pedagogy against classroom-with-pedagogy.

So the claim is not that the tutor role is worthless. It is that the tutor role is
over-used relative to its evidence, and that it is being deployed *out of order*.

The same ordering appears in three independent literatures:

| Phase | Role | Warrant |
|---|---|---|
| 1. Encounter | **Environment / adversary** — struggle before instruction | Problem-solving-before-instruction, **g = 0.36 [0.20, 0.51]**, rising to 0.37–0.58 at high fidelity |
| 2. Reconcile | **Society** — conflicting committed positions, learner arbitrates | Smith 2009: peer discussion works with no expert in the group |
| 3. Consolidate | **Tutor** — canonical instruction, contrasted against the learner's own attempts | Smith 2011: peer *then* instructor beats either; the instruction phase is mandatory |
| 4. Test | **Student** — teach an agent that then acts on what you taught | §13 |
| 5. Grill | **Adversary** — authentic, unannounced objection to the learner's own explanation | Nemeth 2001; question generation ES 0.36–0.86 |

**The field has built step 3, and only step 3.** It is the one step that requires the
AI to be knowledgeable and agreeable, and by Smith (2011) it is the step that works
only when steps 1 and 2 come first. Deployed alone, it is the condition that
produced the unassisted-exam penalty.

That is also the answer to the "grilling" requirement this project started with.
Grilling — sustained, escalating, unsympathetic interrogation of a claim the learner
has just made — is the union of four validated mechanisms: retrieval practice,
question generation, illusion-puncturing through attempted explanation, and authentic
dissent. No study evaluates grilling as a named construct with an AI. Given four
converging literatures and zero direct evidence, it is the highest-expected-value
untested intervention in this report, and it should be run before it is sold.

---

## 8. How to choose and sequence a role

- **Never announce the adversary.** Performed opposition produces bolstering. The
  objection must be the model's own, and unannounced.
- **Do not build an AI peer.** No stakes symmetry, no real commitment, and jigsaw's
  information scarcity is unfakeable. Build a committed adversary or a society of
  voices instead.
- **Prefer structural disconfirmation to social correction.** Where the learner can
  be shown wrong by a consequence, do not have a model say so.
- **Never let the AI do the questioning the learner should learn to do.** The
  transferable asset is the disposition to interrogate; performing it for the learner
  captures the performance and loses the disposition.
- **Do not tune any of this on satisfaction.** Children call persistent questioning
  pushy, and they are describing the intervention working.
- **Do not scaffold the struggle phase.** g = −0.08 across 118 comparisons.
- **Report calibration, not just performance.** Five instructor-fluency studies say
  a fluent teacher moves confidence and not learning; an AI condition can look
  neutral on performance while being badly worse on the confidence–performance gap,
  and it is the gap that decides when a learner stops studying.
- **Sequence the roles.** Encounter, reconcile, consolidate, test, grill. The
  consolidation step is the only one anyone has built, and it is the one that
  requires the other four to precede it.

Six roles, one deployed. The field does not appear to have known there was a choice,
which is why nothing has ever been sequenced. Fix the sequence and the tutor stops
being the whole design and becomes step three of five.


## 21. What the Object Must Refuse — embodiment, manipulatives, and executable material

<sub>Source report: `research/raw/F7-A3-embodiment-and-notebooks.md`</sub>

Every experienced teacher of young children believes the same thing, and they are
not being sentimental about it: some concepts do not go in through a screen. You
need the blocks. You need to *move the thing*. Fractions become real when a child
cuts a circle, not when a circle is cut for them.

This section set out to establish what that intuition is worth and where the
boundary sits. If physical manipulation is load-bearing, there is a hard ceiling
on what an AI reaches, and honesty requires naming it.

The measurement says the intuition is pointing at something real and **has
misidentified what it is.**

---

## 1. Presence is worth about 0.2, and three literatures agree

The first question is narrower than "does the physical matter": does adding
*presence* — a face, a body, a room — to otherwise identical content help?

Three independent literatures converge on the same number:

| Comparison | Effect |
|---|---|
| On-screen pedagogical agent vs none (43 studies) | **g ≈ 0.19** |
| Physical robot vs the same content on a tablet (78 controlled studies) | **d = 0.20** |
| Immersive VR vs desktop (35 RCTs) | **ES = 0.24** |

A real premium, and a modest one. But the number that should govern any decision
built on it is a different one: **the effect is dwarfed by the control condition you
choose.** The robot meta-analysis spans **+0.75** (robot versus nothing) to
**−0.06** (robot *replacing* the teacher). And its Europe/non-Europe reporting gap
is **0.36 SD — larger than the effect being estimated.**

When the moderator is bigger than the main effect, the main effect is not a
property of the technology. It is a property of what you took away to make room
for it.

---

## 2. The result that reverses the premise

Novack and Goldin-Meadow ran the clean experiment. Same mathematical strategy,
taught three ways: **physical action on objects**, **concrete gesture**, and
**abstract gesture**.

> "Gesture promotes transfer of knowledge better than direct action on objects."

Only gesture transferred. Acting on the actual objects — the thing the intuition
insists on — produced learning that stayed stuck to the objects. Replicated
neurally in 2026 with fNIRS.

The reading is counterintuitive and, once seen, obvious. **Physicality is not the
active ingredient. Representational compression is.** A gesture is already a
*symbol* of the action; it has thrown away the specific blocks and kept the
structure. That discarding is the learning. Handling the real blocks does the
opposite. It binds the idea to the instance.

Consistent with this: physical versus virtual manipulatives comes out null in
both randomised, fidelity-documented head-to-heads (N = 350, within-class
randomisation, Welch t = 1.015, p = 0.316). The one pooled estimate favouring
virtual (d = 1.603) has **I² = 97.95%** and is uninterpretable. We report it
because omitting an inconvenient number is worse than discounting a bad one.

---

## 3. So what *is* load-bearing

If not the medium, then what makes a good manipulative good? Two properties, and
both are implementable in software:

> **The object must refuse illegal states, and it must link representations.**

A Montessori pink tower cannot be built wrong and stay standing. A number line
will not let you put 7 to the left of 3. The object corrects, and no adult has to.
That is why the child can be wrong in private, repeatedly, at their own pace,
without anyone's face changing.

That is *self-correction*, and it is the mechanism. It is also, precisely, a
constraint solver with a rendering layer.

This resolves an apparent conflict in our own corpus. An earlier section scored
Montessori's materials as not surviving substitution: remove the physical
object and the mechanism goes with it. That verdict is right *about Montessori*
and does not generalise, because what fails to survive is the wood. What survives
is the refusal.

A well-built simulation refuses illegal states more thoroughly than wood does. It
also links representations — symbol, picture, graph, equation, animation — updating
together, which no physical object has ever done.

---

## 4. The inversion that matters most here

Physical manipulation is an access barrier, and virtual is the accessible
option.

In the head-to-head comparisons the virtual arm showed **fewer demographic
predictors of performance**. Fine motor control, grip, tremor, visual tracking,
and the sheer physical availability of a materials kit are all requirements the
physical version quietly imposes and the virtual version does not.

And the adjacent literature on sensory accommodations does not support the folk
consensus. Sensory-integration treatment effects decline from **0.60 to 0.03**
across study eras and sit at **0.09, non-significant, against active controls**.
Alternative seating, the wobble stools and therapy balls that appear in every
classroom that is trying, has moderate-strength evidence of **no effect on
attention**.

These are not reasons to withhold anything a child finds comfortable. They are
reasons not to *count on it* as an intervention, and not to spend the budget of
attention there instead of on explicit instruction.

---

## 5. The bridge, and the failure mode that must be fixed first

None of this means the physical world is out of reach. Camera-in changes the
boundary: a tutor can now *watch* a child work on paper and comment on it.

State the capability precisely, because the headline number is narrower than it
sounds. The **98.4%** figure is *answer-position recognition* on a 61-exam grading
benchmark, and its **0.58%** false-negative rate is achieved **with the reference
solution supplied**. The best measured rate for reading *error-correction* on
handwritten work is **77%**. So: the system can reliably find and read what a child
wrote. Diagnosing where the reasoning went wrong is a different and harder task
that is not yet at that accuracy.

One failure mode disqualifies naive deployment, and it is the most important
sentence in this section for anyone building:

> **Vision-language models silently "fix" student errors while transcribing them.**

Asked to read a page of student work, the model returns the *corrected* work. It
repairs the sign, closes the parenthesis, completes the step, because that is
what its training rewards. The mistakes are the entire reason for looking at the
page, and they are the thing being erased.

So transcription is not a neutral read. It must be constrained to a verbatim,
error-preserving task with an explicit instruction that mistakes are the payload,
and it must be checked against exactly that.

---

## 6. Executable material: reactivity reduces hazards

The same theme carries into how teaching material itself is built. A reactive
notebook, one whose cells form a dependency graph and recompute on change,
promises that a learner cannot produce an inconsistent state. That is the "refuses
illegal states" property applied to a document.

Measured across eight hazard classes, the promise is **substantially but not
entirely kept. Reactive execution refuses to load** duplicate definitions and
cycles, and eliminates use-before-define and deleted-cell residue. But the same
three cells with identical dependencies produce `total = 106` or `total = 6`
purely by source position.

Hazard reduction rather than a guarantee. Worth having, and not worth trusting
blindly.

And the honest gap: **zero empirical evaluations of reactive notebooks as an
instructional medium exist.** The claim that a consistent-by-construction document
prevents misconception formation is a design hypothesis, not a finding. It is
stated here as the former.

What *is* verified is the recipe. Applying a nine-rule conformance checker to
teaching scripts (~38 ms per script, non-zero exit on violation), an injected
sign flip in an entropy definition **failed loudly and named the claim it
violated.** That is the thing byte-identical reproduction alone cannot do:
reproducing a wrong answer perfectly is still reproducing a wrong answer.

---

## 7. What to build teaching material *on*

Substrate matters more than it looks, because a chapter that takes five seconds to
become interactive is a chapter most learners never see interact.

| Substrate | Cost | Use |
|---|---|---|
| **Reactive JavaScript** | **27 KB** | **The default.** Simulations, constraint objects, linked representations |
| **MicroPython** | 0.53 MB | When Python source must be *read* by the learner |
| **Pyodide** | **21.89 MB + 4.5 s CPU per cold visit** | Real scientific stack. 293 packages, no threads or sockets, torch impossible. **Cap at ≤3 chapters** |

The 27 KB default is not a compromise. Almost everything this survey wants a
mini-app to do (refuse an illegal state, link four representations, let a wrong
idea run to its visible consequence) is a constraint solver and a renderer, which
is exactly what small JavaScript is good at.

A note worth keeping: Observable's own team, asked whether to run computation in
the browser, shipped a static site generator.

---

## 8. What we require of every object we build

- Build for representational compression instead of physical fidelity. Gesture
  beat action on objects. The goal is to help a learner *discard* the instance,
  never to make the instance more vivid.
- Every manipulative must refuse illegal states and link representations. If it
  does neither, it is a picture.
- Virtual is the accessibility default, because it removes requirements the
  physical version imposes silently.
- Never let a model transcribe student work unconstrained. The errors are the
  payload.
- Reactive documents reduce hazards; conformance checks catch what reactivity
  misses. Ship both.
- 27 KB of JavaScript instead of 21.89 MB of Python, unless the learner needs to
  read the Python.

Richness in what a learner is given teaches less than precision about what they
cannot get wrong without noticing. The grounding sections arrive at the same place
from the other direction (§23).


## 22. Showing — illustration, animation, and the arithmetic of a wrong picture

<sub>Source report: `research/raw/C1-illustration-generation.md, research/raw/A2-interactive-animation.md`</sub>

Two numbers from the same paper. An agentic repair loop took text-to-chart
generation from roughly **15% execution failure down to 4.5%**. Manual review of
the charts that survived found **6 of 100 contained hallucinations**, and only
**33.3%** (on one benchmark) and **7.2%** (on another) satisfied basic
colourblindness guidance. The paper is titled *"Does It Run and Is That
Enough?"*, which is the null result stated in the title.

Put those together and you get the fact that should govern every figure a
learning system ships:

> **The probability that a delivered figure is *wrong* now exceeds the
> probability that it fails to *exist*.**

A crash teaches nothing. A confident, beautiful, incorrect diagram teaches a
misconception the learner will then defend. This section is about the
engineering that closes that gap, and it is unusually good news, because the
architecture is settled and it is cheap.

---

## 1. Rank the target by how little drawing the model does

"Checkable" is not one property. It decomposes into four gates, and a generation
target's rank is how many of them you get for free.

| Gate | Question | Answered by |
|---|---|---|
| **G1 — parses** | Is the emitted string well-formed? | schema / grammar validator |
| **G2 — renders** | Does an artifact exist? | compiler / renderer |
| **G3 — layout is not the model's job** | Does an engine own positioning, so collision and overflow are *impossible* rather than *hopefully absent*? | layout engine |
| **G4 — semantics recoverable** | Can the figure's claims be read back and compared to the spec? | IR diff / round-trip / solver |

G3 is the gate the literature under-weights and the one that decides whether an
educational figure is usable. Every documented label collision, text overflow,
and arrow-pointing-at-nothing failure is a G3 failure, and every one occurs in a
target where the model was asked to compute coordinates.

| Tier | Targets | Gates |
|---|---|---|
| **A** — declarative spec + deterministic renderer | Vega-Lite; a project trace/spec IR; Desmos expression lists; GeoGebra constructions | G1–G4 |
| **B** — structural DSL with automatic layout | Graphviz DOT; Mermaid; PlantUML | G1–G3, partial G4 |
| **C** — compiled coordinate languages | TikZ/PGF; matplotlib; Asymptote | G1, G2; no G3 |
| **D** — hand-computed vector output | **model-written SVG**; direct D3; p5.js | G1 only |
| **E** — raster text-to-image | diffusion / native image models | none |

**The one-line rule: rank equals how much of the drawing the model is *not*
asked to do.** Every coordinate the model computes is a coordinate that can be
silently wrong, and no gate catches it.

**Why hand-written SVG is Tier D, specifically.** The benchmark literature is
unusually consistent and unusually negative. VGBench (4,279 understanding + 5,845
generation samples): models show "less desirable performance on low-level formats
(SVG)." SVGenius (2,377 queries, 24 domains, 22 models): "**all models exhibit
systematic performance degradation with increasing complexity, indicating
fundamental limitations in current approaches.**" VCode: "frontier VLMs struggle
to generate faithful SVGs." SGP-GenBench decomposes the failure into attribute
binding, spatial relations and numeracy — the same three axes that fail in
text-to-image. VectorEdits, on 270k+ edit pairs: "current methods struggle to
produce accurate and valid edits."

The distinction that resolves the paradox: **SVG is an excellent output format
and a bad generation target.** You want SVG on the page. It is text, it scales,
and it carries a DOM a screen reader can walk. You do not want a language model
computing its path coordinates. Emit Tier A or B; let a renderer produce the SVG.

*(A self-application: this project's own documentation dashboard shipped
hand-written SVG charts. By its own standard those are Tier D artifacts and are
being replaced.)*

Tier E is disqualified rather than discouraged for any figure containing text.
SciDraw-Bench, across 32 structured tasks over 8 figure types and 10 disciplines,
found domain-specific systems substantially beating general text-to-image models,
with "**text fidelity remains the hardest dimension for all systems.**" A raster
figure cannot be parsed, diffed, edited, or made screen-reader-navigable.

---

## 2. Nine groups, one architecture, one clean ablation

The single cleanest measurement in this literature comes from ALGOGEN, on a
200-task algorithm-visualisation benchmark. End-to-end LLM generation:
**82.5%** success. Decoupling algorithm simulation from rendering — the model
emits a JSON trace, a deterministic compiler draws it to Manim, TikZ, or
Three.js — **99.8%**.

The authors state the mechanism causally. End-to-end generation "requires
the system to simultaneously simulate algorithm flow and satisfy video rendering
constraints, such as element layout and color schemes. **This complex task
induces LLM hallucinations.**" The failure is **capacity contention**: the model
is holding the semantics of the concept and the geometry of the page in the same
forward pass.

At least nine independent groups, across chart code, algorithm animation,
technical illustration, geometry and diagram evaluation, converged on the same
shape — Raiven (a DSL compiling to D3, 100% compilation, up to 6× cheaper), Flint
(a data-semantic model compiling to Vega-Lite, ECharts or Chart.js), GeoSVG-RL (a
layout plan as "geometric contract"), DiagramIR (parse the TikZ back into an IR
and compare the IRs instead of the images), SciFlow-Bench, Socratic Chart,
GeoBuildBench, Chart Specification.

> **A generated educational figure must be produced by rendering a declarative
> specification that the model emitted and a machine validated. The model must
> not compute layout coordinates for any figure that ships to a learner.**

Splitting also buys re-targeting for free: one trace renders to Manim *or* TikZ
*or* Three.js. For a system that must serve a static PDF, a screen-reader page
and an interactive widget from the same idea, that is the only affordable way to
do it.

---

## 3. Animation: g = 0.23, and the moderator that survives

Now the pedagogy, and it does not flatter the medium.

Berney & Bétrancourt's meta-analysis of **61 studies, N = 7,036, 140 pairwise
comparisons** of animated versus static graphics reports **Hedges's
g = 0.226, 95% CI [0.12, 0.33]**. Small. The authors of one of the three
meta-analyses in this area summarise the field in their own words:

> "The results of three meta-analyses show that the effectiveness of learning
> from animations, when compared to learning from static pictures, is **rather
> limited**."

That sentence is written by researchers sympathetic to animation, which is what
makes it credible. The subgroup moderators are larger: system-paced animation
g = 0.309, animation with auditory commentary g = 0.336, instruction without
accompanying text g = 0.883. That last one is exactly the kind of
subgroup-of-a-subgroup result a replication-minded reader should discount.
Report the 0.226; treat the moderators as hypotheses.

Behind the meta-analytic average sits the canonical negative result: a review
that found **no case in which animation outperformed an informationally
equivalent static graphic.** Apparent wins were confounded — the animated
condition usually contained *more information*, or added interactivity and
self-pacing. The finding is not "animation is bad." It is "**the
informational-equivalence control is almost never run, and when you run it,
motion adds nothing.**" In the AI-generated-video boom, that control is not run
at all.

The moderator that does survive is directly actionable: animate what changes.
A systematic review of 194 studies found the field assessing *conceptual* mental
models while neglecting *kinematic* ones, and the follow-up experiment argues
animation earns its keep specifically when the specifics of the displayed change
are the learning target. Kinematics, procedures, human movement, mechanism
dynamics: animate. Static structure, a relation, a proof step: a well-designed
static diagram is at least as good and far cheaper to verify.

And the result that should be printed on the wall of every generation-pipeline
team. Fourth and sixth graders learned the operation of a bicycle pump from
graphics presented simultaneously, successively, self-paced, or animated:

> "The presentation mode affected evaluation of **perceived comprehensibility,
> interestingness, enjoyment and motivation, but not comprehension test score.**"

Animation moves *liking* without moving *learning*. Set that beside the
randomised active-learning result where students in the active classroom
learned more but felt they learned less, and the dissociation runs in both
directions: subjective fluency is anti-correlated with effortful learning, and
animation is a fluency machine.

**Every LLM→video pipeline in this literature is scored by VLM judges or human
preference. Those metrics measure precisely the axis that dissociates from
comprehension.** A pipeline optimised on preference is optimising the illusion.

One more, and it belongs to the author of the multimedia principles himself:
across experiments on lightning formation, brakes, ocean waves, and toilet
tanks, **static, learner-paced, annotated illustrations equalled or beat
narrated animations on transfer.** The cheapest artifact was often the best one.

---

## 4. The field-wide pattern: resemblance, not effect

Line up the success rates this literature reports. TheoremExplainAgent: **93.8%
success rate** — alongside the authors' own note that "most of the videos
produced exhibit minor issues with visual element layout." A renderer-in-the-loop
system: 94% render success, 85.7% visual similarity. ALGOGEN: 99.8%. Raiven: 100%
compilation.

**Every one is a measure of artifact existence or resemblance to a reference
artifact. None is a measure of effect on a mind.** The 93.8%-success /
most-videos-have-layout-defects pair is the field's own admission that its
success metric measures compilation and calls it legibility.

The two metrics that reach further are still proxies. DiagramIR compares
intermediate representations and reports higher agreement with human raters than
LLM-as-a-judge. Better, and still a judgement about the figure. TeachQuiz, the
most inventive metric in the area, measures how well a **vision-language model,
after unlearning, can recover knowledge by watching the generated video**. A
machine analogue of a learning-gain measure, and not evidence about humans.

**No study in the LLM-generated-explanatory-video literature measures whether a
human learns anything from the generated video.** The identical gap holds for
static figure generation: every benchmark measures existence, structural
fidelity, or VLM answerability.

That absence is what makes this a section and not a footnote, because it leaves
two cheap experiments unrun. The first is to expose learners to a
legible-but-wrong generated figure and measure misconception formation and
durability. We know roughly 6% of post-repair charts are hallucinated; we know
from the conceptual-change literature that misconceptions are sticky. Nobody has
multiplied those two facts together. The second is the informational-equivalence
control, which would put a generated figure against generated prose of equal
information content and score transfer. Nobody has run it in the AI era.

---

## 5. What is checkable, and the happy coincidence

Re-read the multimedia meta-analyses as a *specification* rather than as advice.

| Principle | Effect | Checkable? | The check |
|---|---|---|---|
| **Spatial contiguity / split attention** (Schroeder & Cenkci 2018) | **g = 0.63 [0.55, 0.71]**, k = 58, n = 2,426 | **Fully** | assert `distance(label_bbox, referent_bbox) < τ`; no legend-only mapping for ≤ 6 series |
| **Contiguity, overall** (Ginns 2006) | **g = 0.74 [0.67, 0.82]**, k = 46 | Mostly | as above, plus temporal alignment |
| **Signalling** | **g = 0.43**, k = 209; benefit concentrated in **low-prior-knowledge** learners | Partly | one salient emphasis channel; gate on the prior-knowledge estimate — signalling is subject to expertise reversal |
| **Coherence** | **g = 0.33**, k = 68; persistent details **g = 0.43**, transient **g = 0.12 n.s.** | Weakly | element budget; every element referenced in the caption; otherwise human review |

A note on the first two rows, because an earlier draft implied one was a subset of
the other and the arithmetic was impossible: **these are two independent
meta-analyses, twelve years apart, over overlapping but distinct literatures**.
Schroeder & Cenkci (2018) covers spatial contiguity and split attention; Ginns
(2006) covers contiguity broadly. k = 58 is not nested inside k = 46. They agree on
direction and differ on scope, which is why both are shown.

The strongest multimedia principle is also the most mechanically checkable one.
Contiguity reduces to a distance predicate on two bounding boxes, and at
**g = 0.63 to 0.74** across those two estimates it is the largest effect in the
table on either measure.
Coherence, at g = 0.33, is the smallest and requires judgement. Spend the automated
gate's budget on contiguity and reserve humans for coherence.

The persistence moderator carries a specific indictment of static figures.
Seductive details harm at g = 0.43 when persistent and g = 0.12, not significant,
when transient. A static diagram is maximally persistent — the decoration sits on
the page for the whole study episode. **A decorative element that would be
harmless in a two-second animation is harmful in a printed figure**, and
generation systems tuned for appeal are optimising against coherence in the one
format where it bites hardest.

---

## 6. Verification: symbolic detects, the model repairs, and prove the checker is looking

The tempting architecture is render-and-inspect: draw the figure, show it to a
vision-language model, ask if it is right. The evidence against relying on that
is specific and it is the second major null in this section.

- **Socratic Chart:** remove textual labels from charts and apply perturbations,
  and frontier models drop **up to 30%**. The checker is reading the text and
  not the geometry, which is where the error lives.
- **The "Mirage" ablation:** in circuit-diagram→Verilog generation, replacing the
  diagram with a blank image leaves Pass@k unchanged or even higher, because
  models read identifier names in the module header instead of the picture.
- **Misleading-visualisation benchmark:** VLMs detect design errors more reliably
  than reasoning-based misinformation, and **"frequently misclassify
  non-misleading visualizations as deceptive"** — a false-positive rate that
  makes them unusable as a hard gate.
- **Visualisation-rules benchmark:** **F1 up to 0.82 on common violations, below
  0.15 on subtle perceptual rules**; the authors conclude LLMs "underperform
  compared to symbolic solvers." Translating a symbolic constraint system's rules
  into natural language boosted small models by up to 150%.
- **GeoBuildBench:** state-of-the-art multimodal models show "**limited ability to
  exploit visual and constraint-based feedback for self-correction**." That is a
  direct null on the self-repair loop the rest of the field assumes works.

But there is an asymmetry worth exploiting: models are **more effective at
correcting violations than at detecting them reliably.**

So the rule is that **symbolic checks detect, the model repairs, and the model
never gates alone.** And run the blank-image ablation on your own checker. If the
score does not drop, the checker is not looking. One line of code, and it tells
you whether the whole verification layer is real.

Round-tripping — generate, describe back, compare — works when it is made
concrete: ask a **fixed set of atomic questions whose answers were specified in
advance** and score answer accuracy. That converts a fuzzy similarity judgement
into pass/fail, and it composes with "one idea per figure," because one idea
means a small authorable question set. The hard limit is identifiability: **a
boxplot does not contain its samples and a histogram does not contain its
observations.** Asking a round-trip checker to recover non-identifiable
quantities "encourages hallucination and over-specified code generation."

---

## 7. Accessibility is a correctness gate

Only **33.3%** and **7.2%** of generated charts satisfied basic colourblindness
guidance after the execution problem was solved. A 7.2% pass rate is not a long
tail; it is the modal output being inaccessible.

It is fixable and the fix is measured: optimising a code-generating model against
a severity-weighted WCAG reward produced a **60% reduction in inaccessibility
rate** while maintaining semantic accuracy and visual quality. Given that
contrast ratio, colour-difference under CVD simulation, and second-channel
encoding are all deterministic and free at inference time, **shipping a
colour-only figure is a choice, not a limitation.**

There is no principled distinction between "this arrow points at nothing" and
"this series is distinguishable only by hue." Both are figures that fail to
communicate to some learner. They belong in the same gate.

And one design rule with a measurement behind it: **generate alt text from the
specification, in the same pass, never from the pixels afterwards.** Alt-text
accuracy improved when the model was prompted with heuristic alt text or data
tables parsed from the figure source instead of being shown the image. A 2026
PRISMA survey of 20 studies on STEM image description reports persistent "factual
inaccuracies and hallucinations" plus "heavy reliance on automatic text-overlap
metrics that poorly capture perceived usefulness and trust." Interviews with
blind and low-vision scientists record a cost no score captures:
they abandoned AI workflows after vague or incorrect descriptions. Until an
accuracy figure licenses otherwise, alt text delivered to a BLV learner is
human-reviewed.

---

## 8. Rules for every figure we ship

- **Emit a spec, not a picture.** No model-computed layout coordinates in any
  figure a learner sees. 82.5% → 99.8% is the ablation; nine groups is the
  consensus.
- **No hand-written SVG as a generation target, and no raster text-to-image for
  anything containing text, numbers, arrows, or a spatial claim.**
- **Gate deterministically before a learner sees it:** parse, render, then
  layout, axis, unit, contrast, and second-channel assertions. Independently
  recompute every plotted function — nothing else catches a wrong curve.
- **Animate only what changes.** g = 0.226 overall; the surviving moderator is
  kinematic and procedural content. Otherwise ship the static, learner-paced,
  annotated illustration that beat narrated animation in Mayer's own
  experiments.
- **Never optimise a generation pipeline on preference.** Animation raises
  perceived comprehensibility, interest, enjoyment and motivation and not
  comprehension. Active learning does the reverse.
- **Symbolic detects, the model repairs, and the blank-image ablation is
  mandatory** on any vision checker in the loop.
- **Report compile rate and correctness as two numbers**, always.
- **Alt text from the spec, at generation time.** Accessibility failures are
  correctness failures.

What this section shares with the rest of the survey is a missing denominator.
Every number in the generation literature scores the artifact, and none of them
scores the reader. The field has become very good at producing something that
*resembles* a good figure and has not yet asked whether a person understood
anything. A 99.8% success rate is a claim about compilers; the claim a learner
needs is about minds, and nobody has made it yet.



---

# Part IV · Correctness

*How a tutor can be wrong safely, and how a learner's work can be measured when the artifact no longer indicates the person who produced it.*


## 23. Grounding — correctness that lives in the verifier

<sub>Source report: `research/raw/G1-grounding-synthesis.md`</sub>

Substituting one random set of numbers into two expressions and comparing the
results takes **0.38–0.61 ms** (two harnesses in this project measured each, and
both are reported rather than the flattering one) and catches **112 of 113** seeded
derivation errors: 99.1% recall, with **zero** false alarms across 37
semantically-equivalent rewrites. (A third, independent implementation in
`docs/demos/grounding-ladder.html` measures 170 ns on a smaller formula set; the
figures are not directly comparable and the demo says so.)

That is the whole economic argument, over before it starts. **There is no
engineering, pedagogical, or performance reason to ever ship an unchecked formula.**

What follows is more interesting than that, because grounding is usually sold as a
safety feature (*stop the tutor lying*), and that framing produces bad products. It
makes verification a filter bolted onto the end of a generator. The better framing
is capability.

---

## 1. What a checker in the loop makes possible

**A tutor can contradict a confident learner without asserting authority.** Today,
when a tutor says you are wrong, it is staking status: *believe me, I am the machine
that knows*, the posture that fails with the learner who is already right and
the learner who has learned not to argue. With a checker, the move changes from
*assertion* to *experiment*: "I think that's off — let's evaluate both versions at
x = 3 and see." The tutor stops being the authority and becomes the person who knows
how to settle it.

> *Guardrail, in the same breath:* the check settles **the claim**, never the person,
> and only claims of the type it can decide. A tutor that runs a numeric check and
> then generalises the win into "and therefore my explanation was better" has
> committed a category error.

**Productive failure becomes bounded, and therefore usable.** The reason tutors
interrupt is fear that a wrong model will set. A deterministic checker that fires at
the end of an exploration bounds that risk: you can let a learner build a wrong model
for twenty minutes *because you can show it is wrong in under a millisecond, with the
learner's own numbers*. **Grounding is what buys a tutor permission to shut up.**

> *Guardrail:* for anxiety and learned-helplessness archetypes, and for
> working-memory-limited learners, unguided exploration is among the clearest measured
> harms in this survey. Bounded failure is a policy setting on the learner model, not
> a default.

Two more that follow directly. The learner's own conjectures get the same ladder —
a learner who writes "I think the sum is n²/2" gets back "that fails at n = 3, here is
the value," which is what a working mathematician does and is available to
approximately nobody below graduate school. And **a curriculum can be checked against
itself**: every formula in a course instantiated at shared numeric points and
cross-checked for mutual consistency, the chapter-7 constant against the chapter-3
constant. Nobody has published that. It is buildable today.

The one-sentence version: **cheap, binding, legible verification does not mainly stop
a tutor being wrong; it lets a tutor stop performing certainty.**

---

## 2. The invariant

Verifying formulas with a computer algebra system, verifying figures with a schema and
a renderer, verifying assessment items against a cognitive model, and arbitrating
between agents by putting executable truth above every vote are one mechanism seen from
four angles.

> A claim is **grounded at rung R** if and only if:
>
> 1. **DECLARATION.** The model emitted a finite, parseable object that *fully
>    determines* the claim — an expression tree, a chart spec, an item plus key and
>    attribute mapping, a formal statement. Not prose *about* the claim.
> 2. **INDEPENDENCE.** An arbiter maps that declaration to `{PASS, FAIL, ABSTAIN}`,
>    and shares no weights, no prompt, and no training signal with the generator.
> 3. **BINDINGNESS.** The verdict is consequential. `FAIL` withholds the artefact,
>    and `ABSTAIN` is not `PASS`.
> 4. **LEGIBILITY.** The verdict and the declaration travel with the artefact, in a
>    form the learner can read and re-run.
>
> The rung is defined by the arbiter, not by the medium.

Each condition was discovered independently, and each has a documented failure that
violates exactly one of them:

| Violated | Documented failure |
|---|---|
| **Declaration** | PlantUML generation reaches **91.5% syntactic validity** — "all LLMs produced valid PlantUML adhering to UML conventions" — while showing "inconsistencies in annotations and signatures." The grammar was checkable; the content was never declared, so nothing checked it |
| **Independence** | Mirage: a **blank image leaves Pass@k unchanged or higher.** The vision-model checker was not looking at the artefact |
| **Bindingness** | Quarto's `freeze` means the most widely adopted executable-document toolchain in science **does not execute your notebook by default.** The verdict has no consequence, so there is no verdict |
| **Legibility** | "Most AI tutoring systems in 2026 are at Tier 0 and report as if they were at Tier 2" |

And the structural fact that drops out immediately: **the top rung is machine-decidable
only in the deductive modality.** For formulas, the top arbiter is a proof kernel. For
figures it requires an external dataset and a named human reviewer of record. For
assessment it requires human response data, documented equating, and an independent
validity study. For agent disagreement it is *escalate to a human*. This is not a
tooling gap that better models will close. **Machines can climb the whole ladder only
where the ladder is made of axioms. Everywhere else the top rung is the world.**

---

## 3. The six rungs

Named for their arbiters. L2 splits into two orthogonal sub-rungs because they catch
disjoint error classes at comparable and negligible cost.

| Rung | Arbiter | Measured cost | Measured coverage | Cannot check |
|---|---|---|---|---|
| **L0** Asserted | none | 0 | recall **0%** | everything |
| **L1** Attested | source span + entailment | 0.3–3 s | fact-check accuracy **39–77%**; attribution evaluation itself only ~80% macro-F1 | whether the source is right |
| **L2a** Typed | unit / schema algebra | **0.07 ms** | **100%** on exponent, dropped-term, wrong-variable; **0%** on sign, ×2, ÷2; 0/14 false alarms | anything type-preserving — sign, coefficient, ω vs f |
| **L2b** Instantiated | an interpreter, at sampled points | **0.38 ms** median, p95 0.93 ms | **112/113 = 99.1%**; 0/37 false alarms | universals; anything outside the sampled domain |
| **L3** Normalised | a decision procedure (CAS zero test, IR diff) | **1.8 ms** median, 10.8 ms p95, **unbounded worst case** | 100% in-domain — but SymPy fails **152/397 = 38.3%** of the Wester suite | anything outside its competence, *and it cannot tell you when it is outside* |
| **L4** Proved / Calibrated | a proof kernel, **or the world** | <$0.01 in-idiom → 4M tokens → 3 days → 11 person-years | ~90% competition maths; 60–88% undergraduate in-idiom, **−26 pts off-idiom**; 16–35% college physics; **36% end-to-end from prose** | whether the formal statement means the informal one |

Two things about `ABSTAIN`, because it carries most of the ladder's honesty. **L3 can
never emit `FAIL`** — `simplify(e) ≠ 0` does not mean `e ≠ 0`, by Richardson's
theorem, so the symbolic rung emits `PASS` or `ABSTAIN` and nothing else. And **L2a
can never emit `PASS`**: dimensional homogeneity is a mandatory gate that may reject
and may never accept. A pipeline that collapses `{PASS, FAIL, ABSTAIN}` to a boolean
has destroyed the guarantee; it has not compressed it.

And the rungs are not a staircase. The ladder is a *router*. Climbing past the
rung that can falsify a claim buys nothing and costs a great deal.

---

## 4. The measured inversion

The instinct is that numeric checking is the cheap approximation and symbolic checking
is the real thing you escalate to when it matters. **The measurement says the
opposite: the default is numeric and the escalation is symbolic.** L3 buys about +0.9
points of recall over L2b for roughly 3× the median cost, an unbounded worst case —
and a **38.3% hole** in the domains where physics and engineering teaching lives:

| Wester section | Tests | Failing | Rate |
|---|---|---:|---:|
| **R. Sums** | 23 | 16 | **70%** |
| **D. Numerical analysis** | 13 | 9 | **69%** |
| **I. Trigonometry** | 12 | 8 | **67%** |
| **W. Definite integration** | 28 | 16 | **57%** |
| **S. Products** | 10 | 5 | 50% |
| **N. Inequalities** | 17 | 8 | 47% |
| **Y. Transforms (Laplace/Fourier/Z)** | 13 | 6 | 46% |
| **L. Determining zero equivalence** | 9 | 4 | **44%** |
| A. Boolean logic · E. Statistics · Q. Tensors | 0 | — | **not implemented** |

38.3% is a *floor*, because three entire sections carry no tests at all. Meanwhile the
dumb numeric checker handles those same domains without noticing there was supposed to
be a problem — precisely because it is dumb by construction, and therefore uncorrelated
with the generator's errors.

**Run L2a and L2b together, always.** They are orthogonal: dimensional analysis is
100% on some error classes and 0% on others; numeric sampling is ~99% overall.
Together they cost about half a millisecond. Escalate to L3 only on `ABSTAIN`, on a
universal quantifier, or when the claim is reused enough that the tail risk matters.

---

## 5. Four measurements that went the other way

Four, and three of them contradict something a reasonable engineer would have assumed.

Eight random substitutions buy nothing over one. Recall is flat at 112/113 across
a 16× sampling budget. The cost is not flat: p95 latency rises **6.8×** for zero
measured benefit. On textbook-scale expressions a single substitution is the entire
signal, because the mutation classes that matter (sign, factor, exponent, dropped
term, wrong variable) perturb the value almost everywhere, and never merely on a
measure-zero set. So k should be set by the *structure* of the claim (a suspected
removable singularity or a piecewise domain needs more points; a polynomial identity
does not) and never by a fixed constant.

Sampling wider makes the checker worse. This inverts a natural instinct.

| Sampling domain (k=8) | Recall | False alarms / 37 |
|---|---|---|
| narrow positive `U(0.31, 0.87)` | 99.1% | **0** |
| wide positive `U(0.05, 20)` | 99.1% | **1** |
| signed `±U(0.05, 20)` | 99.1% | **2** (3 at k=4 and k=16) |

Widening gained zero recall and cost up to three rejections of *correct* rewrites.
The mechanism: `√p·√q = √(pq)` and `log(exp z) = z` are true on the positive reals and
false off them, so a checker sampling outside the claim's declared domain is not being
more rigorous — it is evaluating a different claim. Adding assumptions until a
check passes is laundering; sampling outside the declared assumptions is manufacturing.
Both are failures of the declaration and never of the arbiter, which is what the
invariant predicts.

And a proposal from this project's own corpus was benchmarked and falsified. An
earlier section proposed permutation-based fidelity checking, modelled on the Vedic
*pāṭha* recitation protocols: instead of re-asking a model the same question k times,
ask k structurally *different* questions about the same content — state it, invert it,
evaluate it at two points, ask the scaling factor, write it in zero form. The claim
was that this is "strictly stronger than self-consistency sampling because the
permutations are adversarial to semantic smoothing," and it was flagged for
benchmarking. It has now been benchmarked: 768 generations, two models, matched
budget of six calls each, every verdict decided by a deterministic comparator so no
model judges anything.

| Protocol | Model | Recall | False alarm | **Discrimination** |
|---|---|---|---|---|
| Pāṭha, all 6 probes | gemma3:4b | 87.5% | 87.5% | **+0.0 pts** |
| Pāṭha, all 6 probes | hermes3:8b | 100.0% | 100.0% | **+0.0 pts** |
| Self-consistency, k=6 | gemma3:4b | 18.8% | 0.0% | +18.8 pts |
| Self-consistency, k=6 | hermes3:8b | 43.8% | 0.0% | +43.8 pts |

Exactly at chance, on both models. It flags corrupted and correct claims at
identical rates. Self-consistency is a poor detector that never cries wolf, and
therefore wins. And going from 4B to 8B improved self-consistency's discrimination by
+25 points and improved pāṭha's by zero — the larger model simply flagged
everything, in both conditions. **A protocol whose false-alarm rate rises exactly as
fast as its recall does not get better with scale; it gets louder.**

The diagnosis generalises: **permutation-based fidelity checking is confounded with
probe competence.** It detects "the model cannot do algebra" far more reliably than "the
claim is corrupted." The original mechanism argument, that structurally different
redundancy is uncorrelated with the original error, is *correct*, and is why
it fails: the permuted probes have their own, independent, much larger error rate. On
one model two of six probes have *negative* discrimination, and probe rankings do not
transfer between models.

Sweeping all 63 non-empty probe subsets and taking the best gives +37.5 and +50.0 points
— but those subsets were selected post hoc on the same 16 claims, so **they are oracle
upper bounds, not estimates.** What is robust is the negative. The doctrine that
follows: **every probe in a permutation-based checker must carry a measured false-alarm
rate on known-true claims, per model and per version, and probes above threshold must be
dropped.** The calibration set is not amortisable infrastructure; it is a per-deployment
artefact.

One more null, about the substrate: only **1.54%** of valid public Python notebooks
import any testing module. A printed output is not a check.

---

## 6. Composition is the unsolved problem

The single most important number in this area:

> **97% autoformalization × 69% proving = 36% end-to-end.**

That was stated as a fact about Lean. It is a fact about *chains*.

> The composition rule. Chaining a verified stage A into a verified stage B
> produces **three** verification obligations, and the field routinely ships two:
>
> 1. `wellformed(A.out)` — A's output is legal in A's target language. *Usually
>    checked.*
> 2. `correct(B.out | B.in)` — B's output is correct given its input. *Usually
>    checked; this is the strong guarantee everyone quotes.*
> 3. **`fidelity(A.in ⟷ A.out)` — A's output *means* what A's input meant.** An
>    entailment obligation straddling two semantics, belonging to *neither stage's*
>    verifier. **Usually unchecked, and silently assumed to equal 1.0.**

Do the arithmetic. If the two checked obligations give 0.97 × 0.69 = 0.669 and the
pipeline measures 0.36 end-to-end, the implied statement-fidelity rate is
**0.36 / 0.669 ≈ 0.54** — which lands on top of the source paper's own qualitative
finding of formal/informal discrepancies in "more than half" of the problems. Two
routes, one number. **The fidelity term is not a rounding error; it is the largest term
in the product.**

Once you know to look for obligation 3, it is already measured under other names:

| Chain | Obligation 3 | Measured fidelity |
|---|---|---|
| Prose → formal statement → proof | does the formal statement mean the prose? | **≈54%** |
| Cognitive model → item template → instance | do instances of this family measure the same attribute at the same difficulty? | **≈39%** — the share of *expert-built* templates passing isomorphicity without revision |
| Concept → declarative IR → render | does the IR encode the intended figure? | **not measured**; the qualitative finding is "content you still cannot trust" |
| Simple explanation rung → detailed rung | is the simple rung entailed by the detailed one? | **untested** |

An independent audit of agent-formalized numerical analysis found "recurring unfaithful
formalization patterns, including incomplete multi-part statements, added weakening
hypotheses, and parameter restrictions, that kernel acceptance entirely obscures,"
concluding that "compilation-based metrics substantially overstate formalization
quality." That is obligation 3 failing while 1 and 2 pass. **The strongest available
guarantee has a systematic blind spot in the direction of over-reporting.**

The fix is not to verify the translator. Compiler verification has been here: prove the
compiler correct once, or validate each translation as it happens. No
autoformalizer, item generator or IR emitter will be proved correct; every one can be
asked for a per-instance certificate.

Concretely: author an atomic question set against the *input*, before the
translation, with answers fixed in advance; ask the same questions of the output in the
output's own language; require identical answers, disagreement a `FAIL` and
unanswerability an `ABSTAIN`. Only ask about identifiable quantities — a boxplot does not
contain its samples, and asking a checker to recover them "encourages hallucination and
over-specified code generation." And back-translation alone is not enough: comparing
the formal statement's prose rendering to the original is an entailment check performed
by a model correlated with the one that produced it, which violates the independence
condition outright.

The ruling: **no chain of verified stages may be reported as verified end-to-end unless
every interface carries a round-trip certificate.** "97% formalization and 69% proving"
is, absent obligation 3, no claim about the pipeline at all.

---

## 7. The disagreement about omission

This project publishes its internal disagreements rather than smoothing them, and there
is one here worth stating plainly.

An earlier report listed "the choice of what to omit" as unverifiable in principle,
alongside intuition, analogy quality, and "why this matters," on the grounds that "a
perfectly verified explanation of the wrong 20% is a failure no tier detects."

That row does not survive, and it should be split into three.

**(a) Omission that *falsifies* is machine-checkable, and this is the class that causes
harm.** Five properties a simplification may never falsify, each a property of the *pair*
(simple rung, detailed rung), each decidable given both:

| Invariant | Check | Rung |
|---|---|---|
| **Quantifier strength** — "all" asserted where only "some" holds | parse quantifiers in each rung, compare matching propositions | L2a, NLI backstop |
| **Sign or direction of a causal relation** | extract the signed relation from both rungs, compare | L2a |
| **Uniqueness of a mechanism** — "*the* mechanism" where several exist | definite-article / exclusivity detection against an enumeration | L2a |
| **Existence of a boundary** — implying a model is unrestricted when it is not | **set difference over declared scopes.** Fully decidable *if* scopes are declared | L2a |
| **Ontological category** — thing / direct process / **emergent** process | classifier over both rungs, agreement required | L2b-grade |

Those five and not others, for a reason with a measurement behind it: misconceptions
*across* ontological kinds are robust and *within* kinds are repairable, and a
classical–quantum hybrid conception was measured unchanged across a full semester of
university chemistry. An undeclared drop is, at retrieval time, indistinguishable from a
planted misconception. **It is a type error, not an editorial judgement the checker
cannot reach.**

(b) Omission of required coverage is a set difference against a blueprint. "Did the
artefact cover what it was supposed to cover?" is a set-cover computation, and assessment
has done it since the 1950s under the name *table of specifications*. The earlier report's
own right-hand column concedes the mechanism, "coverage against a syllabus", and then
leaves the row in the unverifiable table anyway. That is an inconsistency and not a finding.

(c) The choice of the declared scope itself is genuinely, permanently unverifiable.
Whether *this* syllabus is the right syllabus; whether the 20% you declared out of scope
was the 20% that mattered. Not truth-apt. The residue is one line long.

The general move:

> The declaration move. Many properties that look unverifiable become verifiable when
> you require the author to declare the thing that would falsify them. You cannot check
> whether an analogy is *good*. You can check that it shipped with a declared alignment set
> and limit set, that the limit set is non-empty, and that nothing in the alignment set
> contradicts the target concept's ontology. You cannot check whether an omission was
> *wise*. You can check that it was declared and falsified none of the five invariants.
>
> Verification does not need ground truth. It needs a commitment.

The obvious attack: declare a trivially narrow scope and every fidelity check passes.
Real, and it is why the two checks run as a *pair*. Narrowing the scope to escape a
fidelity failure mechanically produces a coverage failure against the blueprint. They
pull in opposite directions, which is what makes a pair sound where either alone is
gameable.

And the sentence the earlier report got right, which nothing above weakens:
verification is a floor, not a quality. A fully verified explanation can be badly
sequenced, pitched wrong, and pointless. Grounding removes a failure mode; it never adds a
virtue.

---

## 8. Where the trust boundary ends up

> **Every rung verifies a declaration. No rung verifies the declaring.**

The boundary moves from the model's fluency, an unbounded and undiagnosable surface, to the
map from the learner's world into the checker's world: the units you assigned, the symbols
you bound, the source you selected, the domain you declared, the scope you announced. That
surface is small, enumerable, auditable, and the same object at every rung. You have
not eliminated trust; you have compressed it into a finite list a human can review and a
learner can be shown. It also explains why four sections' hardest problems are one
problem: the autoformalization gap, "the IR does not encode the intended figure," the
Q-matrix retrofitting problem, and shared-state semantics between agents are all failures
of the declaration, seen through four different arbiters.

Which makes the badge the contract. A badge that says "✓ Verified" is **worse than no
badge**, because it transfers the arbiter's narrow guarantee onto the whole artefact.
State what was checked, operationally, in one sentence a twelve-year-old can read ("I
checked this formula against 8 sets of numbers and it agreed every time"). State the
declaration, including any assumption needed to make it pass, because **the assumption is
part of the claim**. State what was *not* checked, by name. Show `ABSTAIN` — an
explicit "I couldn't check this" is information and a missing badge is not. And make the
verdict falsifiable: ship the check, not just its result, so the learner can change the
numbers and watch it break.

One measured constraint: groundedness and comprehensibility trade off, since "humans
prefer responses generated using RAG, but not when responses are too grounded in the
textbook content." Ground the claim; do not ground the prose.

---

## 9. Correctness was never the hard part

*You have built an elaborate apparatus around the part of teaching that was never the hard
part. Nobody's tutor fails because it got a sign wrong in a derivation; it fails because
it explained the wrong thing at the wrong moment to the wrong learner.*

That is right. As verification cost approaches zero, **100% of the remaining problem is
the part verification does not address**, and the unverifiable layer (intuition,
appropriateness, sequencing, why this matters) is where the teaching is.

But §11.1 is not a safety argument at all. The checker is what lets a tutor wait, let a wrong
model run, hand the instrument to the learner, and settle a disagreement by experiment
rather than by status. **The apparatus is not there to make the tutor correct. It is there
to make the tutor able to stop performing.**

---

## 10. The verification we owe every claim

- **Never ship an L0 formula.** 0.38 ms, 99.1% recall. There is no argument on the other
  side.
- **Run L2a and L2b together; escalate to L3 only on `ABSTAIN` or a universal.** The
  symbolic rung has a 38.3% hole located where physics and engineering teaching
  lives.
- **`{PASS, FAIL, ABSTAIN}` reaches the interface.** L3 never emits `FAIL`; L2a never
  emits `PASS`; a boolean at the last layer destroys the guarantee.
- **Sample inside the declared domain, and set k by the structure of the claim.** k=8 buys
  nothing over k=1; widening the domain costs false alarms and gains no recall.
- **Every interface in a chain carries a round-trip certificate**, authored before the
  translation, scored by a frozen inspector. Back-translation by a correlated model is not
  a check.
- **Every probe in a permutation checker publishes a per-model, per-version false-alarm
  rate.** The pāṭha protocol as specified is at chance; we ran it and we are publishing
  that.
- **Declare the scope, then check the omission against it.** Falsifying omission is L2a;
  coverage omission is a set difference; only the choice of blueprint is unverifiable, and
  the residue is one line.
- **The badge states what was checked, what was assumed, and what was not checked** — and
  ships the check so the learner can re-run it.

A verifier does not make an explanation better. It makes wrongness **discoverable by the
learner instead of assertable by the tutor**, which is the only kind of correction
that does not require them to believe you. Which is why the rung that matters most is the
one the learner can run themselves.


## 24. Assessment After the Artifact — measuring a person when the work no longer indicates them

<sub>Source report: `research/raw/F1-assessment-reconstruction.md`</sub>

Here is Cronbach's alpha:

$$\alpha = \frac{k}{k-1}\left(1 - \frac{\sum \sigma_i^2}{\sigma_t^2}\right)$$

Look at *k*. It is a fixed number of items, administered to a common sample, so
that per-item variances σᵢ² and a total variance σₜ² are estimable over the same
people.

**If every learner sees a different item set, there is no item covariance matrix.**
Not a noisy one. Not a hard-to-estimate one. There is no such object. Alpha is not
biased under generated assessment; it is **undefined**. McDonald's ω has the same
structural requirement and dies the same way.

That is one of four things that broke simultaneously, and it is the one nobody
noticed. This section is about all four, and about the fact that the formative half
of assessment is in better shape than it has ever been while the credentialing half
is in genuine trouble.

---

## 1. What actually broke: the forgery margin

Assessment was never about artifacts. It is an inference from something observed
to a claim about a person, licensed by an argument. The essay was never the
evidence. It was a *sampling instrument*, and a spectacularly cheap one, which is
why it colonised education.

One observation used to license four distinct claims, because human production cost
welded them together:

| Claim | Form | Who needs it |
|---|---|---|
| **Product** | "This artifact is good." | The discipline; the reader |
| **Process** | "This person made this artifact." | The integrity office |
| **Capability** | "This person can produce artifacts like this, unaided, again." | Employers, licensing boards, downstream courses |
| **Learning** | "This person's capability changed between t₁ and t₂." | The teacher, and the student |

Almost every confused argument in the current literature is a failure to say which
of the four is at stake. "AI-proof assessment" usually means securing the process
claim. "Authentic assessment" usually means strengthening the capability claim.
"Assessment for learning" abandons both for the learning claim. These are not
competing schools; they are different jobs that now need different instruments.

What welded them was a cost asymmetry: **the cost of producing a credible fake
exceeded the cost of actually learning.** Call the ratio the forgery margin.
Coursework essays set it by the price of a ghostwriter — which is why contract
cheating held steady at a reported 6–15.7%: a price point, not a moral fact.

Generative AI did not cause an explosion of cheating. A pre/post survey of US high
school students spanning ChatGPT's release found self-reported rates essentially
flat. What it did was drive the *forgery cost* of one enormous class of artifacts to
approximately zero while leaving the *learning cost* untouched. The proportion of
people willing to exploit the gap barely moved; the population who *could* became
everyone.

The design problem is not "invent tasks AI cannot do", a race whose finish line
recedes annually. The problem is to **restore a margin**, and there are four ways:
bind the response to real time (orals, live problem-solving); bind the claim to a verifiable
object (proof assistants, test suites, withheld data); bind the artifact to a process
trace (version control, revision history); or abandon per-task security and secure
the aggregate (programmatic assessment).

Detection is not on that list. Its absence is the diagnosis and not an oversight: detection
tries to recover the margin *post hoc, from the artifact itself*, after the
information is already gone.

---

## 2. What becomes possible: AI makes sampling cheap, not examiners cheap

The standard argument runs: the viva was un-cheatable, we abandoned it because
examiner time doesn't scale, live multimodal AI makes examiner time free, therefore
bring back the viva.

**The premise is wrong, and getting it wrong will produce a generation of bad oral
assessments.**

What killed the viva was reliability, and the dominant source of unreliability in
performance assessment is not examiner subjectivity. It is **content specificity**:
performance on one task is a weak predictor of performance on another, so
generalisable scores require sampling broadly across tasks. The OSCE's advantage over
the long case was never that stations are more objective — it is that there are *more
of them*.

So the naive implementation (one AI-conducted thirty-minute high-stakes viva
replacing the final exam) reproduces the psychometric weakness that killed
orals, now at scale, with an unappealable machine judge. The correct implementation is
many short, structured, low-stakes orals distributed across a term, aggregated
programmatically. Frequency is the entire point. Structure is the second lever:
objective structured viva formats measurably outperform traditional ones, and an LLM
examiner is *natively* structurable — rubric, probe bank and follow-up policy are all
inspectable artifacts, an underrated advantage over human examiners whose criteria are
private.

The fairness picture is more encouraging than the prior suggests. The strongest
datapoint available: 722 students across a bioscience course from 2009–2023, before
and after introducing one-on-one interactive orals as the major final assessment.
Performance and grades improved, and **there were no significant differences by
gender, international status, or language background.** Anxiety was reported
initially and declined with familiarity without depressing performance. The caveats
belong in the same breath: single institution, single discipline, a cohort comparison
across fourteen years in place of randomisation, and **no reported reliability
coefficients**.

The reading this survey adopts: **the equity case for AI-conducted orals rests on
frequency and practice. The technology carries none of it.** Every documented
fairness risk of orals (anxiety, unfamiliarity, differential coaching) is a
*first-exposure* effect that decays with repetition. What made orals inequitable was
that students met one, once, at maximum stakes. A modality students encounter forty times per degree is a
modality they are fluent in.

---

## 3. The DiVERT inversion: model the error, derive the distractor

The Force Concept Inventory works, and its power is not in the stems. It is in the
distractors, each derived empirically from documented student misconceptions.
Which means a multiple-choice item is a frozen interrogation — one scripted
branch of a diagnostic conversation, with the follow-ups precomputed into four
options. It was frozen because conversation was expensive. That constraint is gone.

But unfreezing it requires solving the thing LLMs are worst at here, and the finding
is unambiguous:

> LLMs generate **mathematically valid** distractors and are **"less adept at
> anticipating common errors or misconceptions among real students"** — across
> in-context learning *and* fine-tuning.

That sentence is the whole distinction, empirically confirmed. *Mathematically
valid* is decorative. *Anticipating real student error* is diagnostic. The models do
the first and not the second, and the gap survived fine-tuning, so it is not a
prompting problem.

The mechanism is clean. An LLM's prior over "wrong answer" is a prior over *plausible
text*, learned from a corpus in which correct answers dominate and student errors are
rare and unlabelled. The empirical distribution of student errors is a different
distribution, and it is not recoverable from text describing the domain. It is
recoverable only from response data.

DiVERT (Fernandez, Scarlatos, Feng, Woodhead & Lan, EMNLP 2024) inverts the
pipeline. Instead of generating distractors directly, it learns an **interpretable
latent representation of the error, expressed as text**, and generates the distractor
*from* the error. Evaluated on 1,434 real maths questions used by hundreds of
thousands of students:

- A **7B open-source model with DiVERT beat GPT-4o-based state of the art** on
  downstream distractor generation.
- Maths educators judged DiVERT's **error labels of comparable quality to
  human-authored ones.**

Independently replicated in a different modality: L2 listening items with response
data from 2,267 EFL undergraduates, where generative revision under principled
prompts "effectively enhanced distractor quality" but "struggled to fully capture
listening miscomprehension patterns." Same finding: **LLMs fix form and leave
diagnosticity where it was.** And note the pipeline shape in both — response data first,
generation second.

The design rule falls out: **do not ask a model for a wrong answer; ask it for an
error, ground the error in observed response data, and derive the wrong answer from
the error.** DiVERT is automated think-aloud analysis, which is precisely what
concept-inventory methodology did by hand over decades.

---

## 4. Calibrate the generator, not the item

Generation gives one unambiguous win, and it should be banked. Item exposure and
pool compromise are the chronic security failure of computerised adaptive testing. A
stolen item is worthless if nobody else will ever see it. Real, keep it.

Now the trap.

> **The item bank was never valuable because items were scarce. It was valuable
> because *calibration* was scarce.**

An item's parameters come from examinee responses. Generation makes item *text*
free; it does nothing to make examinee responses free. The binding constraint moves
from authoring to a calibration sample. **An infinite bank of uncalibrated items has
no measurement properties at all.** That is the sentence institutions rolling out
LLM quiz generators need on the wall.

Fifteen years of pre-LLM automatic item generation, mostly in medical education,
established that items generated from cognitive models are rated by blinded expert
panels as comparable to traditionally authored ones, and demonstrated end-to-end IRT
and CAT integration. But the load-bearing assumption is isomorphicity: that
sibling items from one item model share parameters. It is an assumption. When
tested: only **9 of 23** expert-built templates produced psychometrically isomorphic
instances without revision, and **9 of 23 required major modification**.

Three consequences follow, and the third is the one nobody is watching.

(a) The psychometric object is the generator. If item text comes from a
stochastic policy conditioned on a specification, the object with parameters is the
*distribution* the policy induces and never any individual item. Random-item and crossed
random-effects IRT is the existing apparatus; what must be demonstrated is that
generator-level parameters are stable enough to support inference even though
item-level ones are not.

(b) Every operational system currently understates measurement error.
Conventional adaptive-test scoring treats calibrated item parameters as *known*. Under
generation they are draws, so the standard error of θ must include item-sampling
variance, and no shipping system appears to do this. The prediction is falsifiable
and cheap to test: **reported reliabilities for LLM-generated adaptive quizzes are
systematically optimistic, and the gap widens as item novelty increases.** Duolingo's
own published numbers illustrate the size of the gap: **test–retest 0.84 against
internal consistency 0.96**, and only one of those two is estimable under generation.

(c) Fairness moves to the generator, and there is a new failure mode.
Differential item functioning assumes a fixed item administered to multiple groups.
If every student receives distinct items, item-level DIF is undefined; what must be
demonstrated is generator invariance — that the policy produces equivalent
difficulty distributions across subgroups. Worse: personalised generation, the
flagship selling point, conditions item content on student context. A generator
drawing contexts from a learner's interests or locale can produce
personalisation-induced DIF — construct-irrelevant difficulty variation
correlated with demographics, arising *by design*, invisible to every existing
fairness procedure, and defended as a feature.

*Flagged as construction and not as finding: personalisation-induced DIF is this project's
own framing and no study of it was located. It is offered as the most serious
unexamined fairness risk in AI-driven assessment, and as a hypothesis someone should
test.*

And the replacement for alpha. Cronbach himself supplies the exit route,
pointing to generalizability theory. G-theory decomposes score variance into facets
(persons, items, occasions, raters) and asks how well a score generalises to a
universe of admissible observations. That framing is *native* here, because **a
generator is a formal specification of a universe of admissible observations**,
arguably the first time in the history of measurement that this universe has been
written down explicitly and executably rather than gestured at.

The concrete protocol, offered as a specification to test and not as a finding:
make the probe policy π seed-deterministic so that (π, s) reproduces the exact
administered set; administer π under seeds s and s′ to the same learner within a
window short enough that true change is negligible, and report the correlation as
seeded-replicate reliability ρ_π; run a G-study with generator as a facet;
derive from it the number of probes n required for a target dependability at the
decision threshold; and **report the pair (ρ_π, n_required(Φ)), never a single
number, never α.** Because generators drift with model updates and prompt edits,
ρ_π carries a version and is re-estimated on change.

One incentive property of this design deserves note: high-variance generators need
more probes to reach the same precision, which means **a sloppy generator costs the
learner time.** That is the right direction for the pressure to point.

---

## 5. The negatives, including the ones that cut our way

**Detection is bounded in theory and broken in practice, and its errors are not
random.** The theoretical result bounds the AUROC of the *best possible* detector by
the total variation distance between human and machine text distributions: as
models improve, achievable detection falls toward chance. Empirically, the largest
comparative test of 14 systems concluded they are "neither accurate nor reliable."
Then Liang et al., usually cited too weakly. Seven deployed detectors, run on TOEFL
essays by non-native writers and on US eighth-graders' essays:

| Measure | Value |
|---|---|
| False-positive rate, non-native writers | **61.22%** |
| False-positive rate, native writers | ~5.19% |
| TOEFL essays flagged by **all seven** detectors | **19.78%** (18 of 91) |
| TOEFL essays flagged by at least one | **97.80%** |
| FPR after prompting an LLM to rewrite in "literary" language | 61.22% → **11.77%** |

The mechanism is explicit: unanimously flagged essays had significantly **lower
perplexity. Which means the false positive is not a malfunction. The detector is
a conventionality meter** — it measures distance from the distributional centre of
unconstrained fluent English, and fluent-but-conventional prose is the signal.
Conventionality is exactly what a writing course teaches a second-language writer.
The construct the detector measures is negatively correlated with the construct the
course develops. That is a validity failure, and no threshold repairs it.

The base-rate arithmetic nobody ran: 500 students, 5% undisclosed AI use, and a
detector *better* than any documented, at 90% sensitivity and a 5% false-positive rate.
True positives 22.5; false positives 23.75; **false discovery rate 51.4%.** More
than half of accusations wrong, with generous parameters. At Liang's measured rate,
among 100 honest non-native speakers, 61 false accusations.

Human grading is not the gold standard either, and this is the null that should
make everyone humbler. Human graders of programming assignments reached
**Krippendorff's α ≈ 0.20 on correctness and below 0.10 on style**, and **only 1 of
22 reproduced their own grade on a hidden duplicate.** The authors' conclusion: "the
idea of a 'gold standard' of human grading might be flawed."

Equivalence by readability formula is invalid. Six oral-reading-fluency passages
"developed to be comparable based on readability formulas" produced mean fluency
from **67.9 to 93.9 words correct per minute**, roughly a semester of growth,
purely from which passage a child happened to get.

Progress-monitoring decision rules rest on expert opinion. A systematic review of
102 documents found curriculum-based measurement decision rules have "very limited
psychometric or empirical support."

And two clean negatives that cut *against* the fashionable direction. Testwiseness
manipulations produced little post-instruction effect on modified concept
inventories, despite option-avoidance and position effects being individually
significant. And misconception structure in FCI incorrect-answer groupings had
little relation to previously identified gender-unfair items — the proposed
explanation for the FCI gender gap was tested and failed.

Finally, a null that constrains criticism of AI items without endorsing them:
AI- and human-generated MCQs showed **no significant difference in discrimination
index (p = 0.17)**, despite significant differences in difficulty and
non-functioning distractors. "AI items are worse" is a dimension-specific claim,
never a global one.

---

## 6. The four-tier score-claim licence

A system asserts a tier and must be able to produce the evidence for it. **The tier
is a property of the probe policy, not of the product.**

| Tier | Claim | Requires | Prohibited |
|---|---|---|---|
| **T0 — Practice signal** | "You got 7 of 10 right on items about X" | Sampled audit of key correctness. Nothing else | Any number on a scale; any comparison to another learner or to the same learner at another time; the words *mastery, level, proficiency, grade, ready* |
| **T1 — Calibrated formative estimate** | "Ability 0.6 ± 0.3 logits on construct C, policy π v1.2" | Reported (ρ_π, n_required); an interval that **includes item-sampling variance** | Cross-learner ranking; any high-stakes gate; growth claims from fewer than ~14 controlled probes over 8–15 weeks |
| **T2 — Diagnostic profile** | "Mastered {A1, A3}; not yet {A2}" | All of T1, plus a Q-matrix derived from the cognitive model **before** generation, a fitted diagnostic model with reported classification accuracy, **and external validation of at least one attribute claim against evidence not produced by the same generator** | Profiles whose fit was assessed only against generator-produced data; profiles indistinguishable from a rescaled total score |
| **T3 — Summative / consequential** | "This learner meets the standard" | All of T2, plus **100% human review of keyed answers on administered items**, documented equating, published subgroup invariance, an appeals path, and an independent validity study | — |

Two observations about that table matter more than its contents. **Most AI tutoring
systems in 2026 sit at Tier 0 and report as if they were at Tier 2**, the single most
common measurement error in the field. And **Tier 3 is not currently attainable by a
purely generative system**: the largest systematic review of AI-generated MCQ validity
concludes the evidence "does not yet support unsupervised use in summative
assessment," and combined with the collapse of the process claim on unsupervised
artifacts, consequential decisions require proctored or verification-anchored
observation. Say so; do not approximate it.

Explicitly permitted at every tier, worth stating because the prohibitions are long:
telling the learner what they got wrong and why. Diagnostic feedback is not a
score claim.

Three standalone prohibitions. Never report α or ω for an assessment where learners
receive different items: the statistic is undefined and not merely inaccurate. Never present a
wrong-answer analysis as diagnostic unless the distractors were derived from observed
student errors; doing so manufactures a diagnosis. Never claim a growth trend from
probes whose equivalence has not been empirically established.

---

## 7. Nobody will build this

*This is an argument for making assessment far more elaborate. Frequent secured orals,
human review of every keyed answer, G-studies per generator — you have replaced a
simple system that mostly worked with one nobody will build.*

First, the burden moved without growing. Human review has replaced generation as the
bottleneck, and a system claiming "AI removes the item-writing bottleneck" has *moved*
it and should say so. And verification-first assessment makes the product claim genuinely
free wherever the discipline has already agreed to submit to an oracle: mathematics
agreed centuries ago, software by construction, empirical science via replication.
Institutions that adopted autograders as a saving inverted the logic — they banked it
and never spent it on the capability and learning claims that now go unevidenced.

Second, the reframe that should reorganise priorities: **the emergency was never
cheating.** In Bastani et al.'s trial of ~1,000 high-school maths students, unguarded
assistance improved practice performance by 48% and left students **17% worse** on an
unassisted exam than students who never had access (§2). *(A note on provenance, since this
project publishes its corrections: the PNAS notice attached to that paper is an
affiliation erratum. The −17% stands.)*

The threat is not that students submit work they did not do. It is that they do work
from which they learn nothing, and **the grading system cannot tell the difference —
and in fact rewards it.** Cheating is a distribution-of-credit problem. This is a
capability-destruction problem, and it operates on students who are not cheating at
all. Which reassigns assessment's job: if practice is now AI-saturated, assessment's
primary function is to create the incentive to practise in the guardrailed mode.
Only a frequent, secured, diagnostic system can do that.

---

## 8. What we will and will not claim from a score

- **Say which of the four claims is at stake**, every time. Product, process,
  capability, learning need four instruments.
- **No detection, ever, as an evidentiary instrument.** 61.22% false positives on a
  population defined by immigration status, a >50% false discovery rate at generous
  parameters, and no procedurally just way to run an accusation on it.
- **Grade weight is a monotone function of assurance.** Not two lanes — a dial. An
  unsupervised essay can be the intellectual centre of a course and carry 0–5% of the
  grade while serving as the substrate for a secured oral that carries 30%.
- **Many short structured orals, never one long one.** Content specificity is the
  binding constraint, and frequency is what turns a fairness risk into fluency.
- **Never ask a model for a wrong answer.** Ask it for an error, ground the error in
  response data, derive the distractor.
- **Calibrate generators, not items**, and publish (ρ_π, n_required(Φ)) with a
  version. Reporting α for a generated assessment is prohibited.
- **Verification-first assessment must specify an attempt budget**, or it measures
  available compute rather than competence. Oracle-gaming is a search problem, and
  machines search fast.
- **Assert a tier and produce the evidence.** T0 unless proven otherwise; T3 is not
  currently attainable without proctored or verification-anchored observation.

The formative half of assessment has never been in better shape: retrieval practice,
self-explanation and Socratic probing now cost approximately nothing and can run
continuously. The credentialing half cannot be repaired into working well at scale,
and pretending otherwise is how a system ends up **selecting for the students who
learned least.**



---

# Part V · Who it is for

*The learners the evidence was not collected on, the learners it cannot reach, and the legal floor that turns out to be a design specification.*


## 25. The Empty Chair — designing for the margin first

<sub>Source report: `research/raw/H1-selpa-accessibility.md`</sub>

Start with a specific child, because the general case is where this field goes to
avoid the work.

She is eleven. She reads, but decoding costs her enough that by the time she
reaches the end of a sentence the beginning has gone. She can hold a conversation
about photosynthesis that would impress you and then fail a worksheet about
photosynthesis, and the gap between those two facts is invisible to every system
she is enrolled in. She is not lazy and she is not slow. She is running a working
memory that spends most of its capacity on the part everyone else automated years
ago.

There are millions of her. In the United States they are served under
individualised education programs, coordinated regionally, and in California
through Special Education Local Plan Areas. Roughly one child in seven.

Here is the state of the evidence on whether generative AI helps her.

---

## 1. The census

We ran it rather than cited it. ERIC and Europe PMC, 2026-07-27:

| Query | Hits |
|---|---|
| `(generative AI \| ChatGPT \| LLM) AND "randomized controlled trial" AND students` | **30** |
| The same, plus *disability · dyslexia · ADHD · autism · special education · IEP* | **0** |

Zero. Not "few" — the intersection is empty. Re-run independently a second time
during this project, same result.

Widen from RCTs to everything: the entire world literature on AI interventions for
students with learning disabilities, 2022–2025, across seven databases, is
**11 studies, 10 independent experiments, 3,033 participants**. At most one is a
randomised trial (n = 60). **None** was rated low risk of bias. All eleven reported
positive results, which is a publication-bias signature and not an encouragement.

So every effect size quoted in the AI-tutoring conversation — every headline, every
pilot, every deck — was measured on somebody else's child.

That is the empty chair. It is not a verdict. Nobody has run the experiment.

---

## 2. The inversion that makes this the *best* place to build

The intuitive read is that the margin is the hardest problem and should therefore
come last. The evidence says the opposite.

**Special education is the most replication-rich area in all of education.**

While the AI-and-disabilities literature totals eleven studies, the Direct
Instruction literature alone is **328 studies, 413 designs, roughly 4,000 effect
estimates**, all positive, all significant except on affective outcomes, with
unusually *no publication-bias signature*. Swanson's syntheses of interventions for
learning disabilities cover 180 experimental studies and land at **M = 0.79**.
Gersten's mathematics synthesis draws on 42 randomised and quasi-experimental
studies.

Read the ratio: the known-good intervention base for these learners is **two orders
of magnitude larger** than the AI base.

That inverts the job description. In most of education, the interesting question is
*what should we teach and how*. Here, that question has largely been answered, in
public, with replication, for decades. What has never been solved is **delivery**:
the fidelity, the dosage, the individualisation, the sheer number of adult-attention
minutes that explicit systematic instruction requires to work.

> **The AI's job at the margin is not invention. It is fidelity and dosage of
> known-good intervention, at a frequency no staffing model has ever afforded.**

That is a smaller claim than "AI will revolutionise special education," and a much
stronger one, because the thing being scaled already has 4,000 effect estimates
behind it.

---

## 3. Where the folk consensus is wrong

Building faithfully means knowing what to be faithful *to*. Four widely-held beliefs
do not survive contact with the primary literature, and a system that automates them
will automate a mistake at scale.

**Orton-Gillingham is not the evidenced ingredient.** It is the intervention most
requested by parents of dyslexic children. Against active comparison instruction it
shows **g = 0.22, p = .40** and **g = 0.14, p = .59**, both non-significant. What
*is* evidenced is explicit, systematic decoding instruction. The multisensory
branding is not carrying the effect. Ship the mechanism and drop the brand name.

UDL is a design philosophy, not an evidence-based intervention. The best
meta-analysis concludes it improves the learning *process* while "the impact on
educational outcomes has not been demonstrated"; a policy review found no rigorous
published research demonstrating improvement. The component practices it bundles
(multiple representations, choice, scaffolded engagement) are individually
well-evidenced. Keep the components; drop the claim. We build to the accessibility
standard the law actually incorporates, described below, because access is a right
and not because a framework promises a score.

Do not build a working-memory trainer. Working-memory training produces reliable
near-transfer to the trained task and does not transfer to anything anyone cares
about. Given that our eleven-year-old's central constraint *is* working memory, the
temptation is enormous and the evidence is unambiguous. **Externalise memory
instead.** Off-load it into the environment, the notation, the shared canvas, the
persistent record. Do not try to enlarge the buffer. Reduce what has to go in it.

And a framework can be implemented faithfully and still hurt. The federal
evaluation of Response to Intervention covered **146 schools across 13 states**, all
experienced with RTI, 86% reporting full implementation. Regression discontinuity
around the screening threshold found that Grade-1 students who scored *just below*
the cut, and were therefore assigned to reading intervention, had lower spring
scores than those just above it. Grades 2 and 3: no significant impact.

The mechanism most discussed is that intervention pulls a child *out of* effective
core instruction, and the replacement is not better than what it replaced. The design
lesson is permanent and it applies directly to any AI that routes learners:

> **Routing a child into "intervention" is never neutral. It has an opportunity cost,
> and that cost belongs inside the decision.**

---

## 4. The architecture the evidence forces

Three findings, each of which kills a popular product pattern.

### 4.1 Measurement without a decision rule is inert

The result that most constrains the whole system is a clean randomised trial.
Thirty-three teachers, three arms, twenty weeks: curriculum-based
measurement plus an expert system that told teachers *what to change*; CBM alone; and
no-CBM control.

> "Compared to the control group, **both** CBM groups appeared to revise students'
> instructional programs more frequently. However, **only the CBM-ExS group effected
> superior student achievement.**"

Frequent measurement, frequent program changes, no guidance on what to change: **no
achievement benefit.** Replicated in a companion randomised study in spelling.

Now look at what the industry ships. Dashboards. Streaks. Mastery bars. Adaptive
difficulty. Engagement analytics. Every one of those is the **CBM-without-expert-system
arm** — the arm that measured more, changed more, and moved nothing.

So build the expert system, and not the dashboard. The active ingredient is a
prescribed, principled change of instruction, drawn from a known-good menu,
triggered by a stated rule.

### 4.2 Two clocks, and the slow one is slower than you think

Trend-based decision rules on weekly academic probes are **not statistically viable
until 7–10 weeks** of data. An AI tutor that changes method after three wrong
answers is not adapting. It is fitting noise, and it destroys exactly the
consolidation that explicit instruction depends on.

But a tutor that does nothing for ten weeks is useless. The resolution is that these
are two different loops that get conflated:

| Clock | Signal | Latency | Permitted action |
|---|---|---|---|
| **Fast** — within session | Error *type*, latency, help-seeking, disengagement | Seconds to minutes | Micro-scaffold: hint, worked step, re-represent *this item*. **May not change the method.** |
| **Slow** — across sessions | Graphed probe scores against a goal line | 4 points minimum; 7–10 weeks for a trend judgement | **Change the method.** Fire the adaptation step. Log it. |

The fast loop is responsive. The slow loop is skeptical. A system with only the fast
loop thrashes; a system with only the slow loop is inert. Most products have built
the fast loop, called it personalisation, and shipped.

### 4.3 Restraint matters *more* at the margin

Unconstrained LLM access widens the gap between low- and high-prior-knowledge
learners. The largest AI-tutoring trial in Nigeria found gains accruing
disproportionately to students with higher initial performance. Sierra Leone's
effect loaded at **+0.195 SD per SD of baseline mathematics** — the strong pulled
further ahead (§3).

An unguarded answer-machine is not neutral technology that helps everyone a bit. It
is a gap amplifier, and our learner is on the wrong side of it. The refusal engine —
the judgment to ask instead of tell, to wait, to let a struggle run — is not a
pedagogical nicety here. It is the difference between a tool that closes the gap and
one that widens it.

There is an important asymmetry to state honestly, because it constrains what we may
claim. Guardrails have been measured to remove harm: unguarded assistance left
learners **17% worse** on later unassisted work, and the guardrailed arm's unassisted
coefficient was **−0.004 (not significant).** Harm removed (§2). **Benefit not
demonstrated.** Anyone selling guardrails as a learning gain is ahead of the
evidence, including us.

---

## 5. What the system may not do

Four hard limits, and they are not negotiable by product decision.

- **An AI may not author an IEP.** It is a legally binding document authored by a
  team including the parent. An AI may draft materials, track goals, surface
  evidence, and prepare a parent for the meeting. It does not sign.
- **An AI may not diagnose or label a child.** It may observe that a strategy is not
  working and say so, in behavioural terms, to the humans responsible.
- **The accessibility standard is WCAG 2.1 AA, and the deadline moved.** *Corrected
  2026-07-28:* the ADA Title II web rule incorporates **WCAG 2.1** and not 2.2, and the
  compliance dates were pushed twelve months in April 2026 (91 FR 20902) to
  **26 April 2027** and **26 April 2028**. Most published guidance, including an
  earlier version of this section, still says WCAG 2.2 and April 2026. Build to 2.2
  if you like; conform to 2.1 because that is what is enforceable.
- **Disability status is sensitive data.** Under **IDEA §300.624**, personally
  identifiable information "must be destroyed at the request of the parents." An
  undeletable model weight is therefore a compliance failure for the population the
  system claims to serve. The learner model is
  local, inspectable, correctable, and deletable, or it is not shippable.

---

## 6. Curb cuts, and the half of the thesis that survives

The design instinct behind this section is the curb cut: build the ramp for
wheelchairs, and it turns out to serve strollers, suitcases, delivery carts and
everyone with a bad knee. Build the SELPA-grade system and it serves every learner.

The engineering half of that thesis holds well. Explicit instruction, externalised
memory, a shared canvas that carries working-memory load, honest pacing, a decision
rule instead of a dashboard, restraint by default. None of these are concessions.
They are what good instruction looks like for anyone, made visible because at the
margin you cannot get away with anything less.

The evidential half needs a caveat we should state ourselves rather than have pointed
out. Effects for learners with disabilities do not transfer automatically to
typical learners or the reverse; non-responders to well-implemented intervention
exist and are predictable; and an effect size of 0.41 is a statement about a
distribution, never a promise to a child. "It works for the margin so it works for
everyone" is a design heuristic, not a finding.

---

## 7. Filling the chair

Everything in this section is an argument that the pieces exist. Four thousand effect
estimates on what to teach. A randomised trial telling us that measurement without
prescription is inert. A number — 7 to 10 weeks — on how long to wait before
changing course. A clear prohibition on the brain-trainer, and a clear instruction to
externalise memory instead. A gap-widening result that makes restraint mandatory
instead of optional.

What does not exist is a single randomised trial of any of it, assembled, with these
learners.

We do not treat that absence as a reason to wait. We treat it as the specification
for the first experiment worth running, and building this system carries the
obligation to run it: a delayed, unassisted, novel-item primary outcome, published
whichever way it lands.

The chair is empty because nobody sat down. Not because the seat was taken.


## 26. The Coordinator's Week — five hours of statutory admin against four available

<sub>Source report: `research/raw/H2-selpa-practitioner-reality.md`</sub>

A hostile reviewer read §25 — the section this project exists for — and judged it
**costume over a genuine core.** The intervention evidence was real; the job was
absent. A coordinator would recognise the research and would not recognise their week.

So start with the week.

---

## 1. The week

Nothing here is invented. Each item is a statutory duty with a citation or a measured
hour count.

**The number that describes the job:** administrative work runs a median of
**five hours a week against four available.** The deficit is structural. It does not
clear on Friday.

**Standing, every week.** Direct instruction, the part the job is named after.
Consultation with every general-education teacher, who under §300.323(d)(2) must be
informed of their specific responsibilities and of *"the specific accommodations,
modifications, and supports that must be provided"* — which makes **every new teacher,
every schedule change, and every substitute a re-notification event.** Progress
probes, and graphing them, because the graph is the §300.309(b)(2) evidentiary record
and not a wall display.

On a rolling cycle. An IEP meeting is 1.5 hours in the room and **2 hours to write
the document**, plus 2 hours a month scheduling and 1 hour mailing notices. Each
one carries §300.322's parent-participation duties, including a record of attempts
if the parent does not attend and a duty to *"take whatever action is necessary to
ensure that the parent understands the proceedings."* Progress reports: **8 hours,
every 7 weeks.** Initial evaluations: 7.5 hours a month administering, 4.2 reviewing.
Behaviour logs 5, intervention plans 2, functional assessments 2.

On the compliance calendar, each of these a date that arrives whatever else is
happening: 60 days from consent to evaluation. 30 days from eligibility to the IEP
meeting. An IEP in effect for every child on the first day of school. Annual review.
Triennial reevaluation. Safeguards notice once a year plus on trigger. **Ten school
days to a manifestation determination** after a disciplinary placement change.

And then the part no calendar holds. A safeguarding disclosure — personal duty,
immediate, routed around the parent. A behaviour crisis. A removal. A parent's request
for an independent evaluation, which starts a clock the moment it is spoken. A
transfer student arriving mid-year who must receive comparable services immediately.

That is the week. Notice what it is mostly made of, and notice that the five-against-
four deficit is not the paperwork *around* the job. **The paperwork is the job's
second full-time role**, and it is the one with the legal exposure.

---

## 2. Half of the legal test is procedural, and §25 argued only the other half

The federal standard for a free appropriate public education has two prongs
(*Rowley*, 458 U.S. at 206–07). One asks whether the programme was reasonably
calculated to confer educational benefit. The other asks whether the state complied
with the procedures set out in the Act.

A survey that discusses only instructional efficacy has addressed one half of the
statute. That is why §25 read as research wearing a lanyard: it was arguing about
whether the intervention works while the practitioner's week is largely governed by
whether the paperwork is defensible.

The asymmetry between the statutes is worth stating plainly, because outsiders
routinely collapse it:

| | IDEA | Section 504 |
|---|---|---|
| Procedural safeguards | **37 sections** of regulation | **One sentence** |
| Eligibility | 13 categories, team determination, 60-day timeline | Substantial limitation of a major life activity |
| Document | IEP — nine required components under §300.320(a) | A plan, form largely undefined |

A 504 plan is not a small IEP. It is a different statute with a different gate and
almost no procedural machinery, and a system that treats them as points on one scale
will generate advice that is wrong in both directions.

---

## 3. The correction to our own prior-written-notice claim

An earlier framing in this project said: *an AI that changes a child's programme
without generating prior written notice has created a procedural violation.*
Directionally right; wrong in three specifics, and the specifics matter because
they decide what a system is allowed to do without a meeting.

1. **The duty attaches to the agency, not to the tool.** A vendor cannot create or
   discharge a PWN obligation; the district holds it.
2. **It fires on identification, evaluation, placement, and the provision of FAPE,
   and not on teaching methodology.** §300.501(b)(3) places methodology outside the
   meeting requirement entirely.
3. **A procedural violation denies FAPE only through §300.513(a)(2)'s three gates**:
   impeding the right to FAPE, significantly impeding parental participation, or
   causing deprivation of educational benefit. Not every misstep is a denial.

The load-bearing sentence is the Department's own, from the 2006 commentary:

> *"Placement refers to the provision of special education and related services rather
> than a specific place."* (71 FR 46588)

So the line an AI must not cross is between the service and the method — not
between a big change and a small one. Changing which explanation strategy a child
sees on Tuesday is methodology. Changing the minutes of specialised instruction is
placement, and that is a team decision with notice.

---

## 4. Predetermination is the sharpest AI-specific legal risk

This is the finding with the most immediate consequence for anyone building, and the
regulator described the failure mode without being asked about AI at all.

Explaining why it would *not* require prior written notice to be issued before an IEP
meeting, the Department wrote that doing so:

> *"could suggest… that the public agency's proposal was improperly arrived at before
> the meeting and without parent input."* (71 FR 46691)

That is the *Deal v. Hamilton County* predetermination doctrine, stated by the
regulator, in advance.

Now consider what a recommendation engine does. It arrives at a proposal before the
meeting, without parent input, and presents it with the authority of having processed
the data. Every recommendation engine is a predetermination machine by default.

The design consequence is specific and cheap: an AI may prepare *options with their
evidence*, and must not arrive with *a recommendation*. The difference is legally
load-bearing and it costs nothing to respect.

---

## 5. Four prior attempts to cut the paperwork, all measured, all zero

The administrative burden in special education is not a new complaint, and the
history of trying to fix it is a graveyard:

| Attempt | Result |
|---|---|
| **Computerisation** | SPeNSE, n = 972 — **no significant relationship** to hours spent |
| **Human delegation** | Same null, *"because much of the paperwork teachers complete cannot be appropriately delegated"* |
| **Deregulation** | ED priced its own excusal provision at **nothing** |
| **IDEA §609 waiver authority** | **21 years, 15 state slots, zero documented waivers** — and the effectiveness report the statute mandates **has never been filed** |

The AI claim is the fifth attempt. Its entire measured base is **one RCT of 22 novice
teachers on goal drafting.**

We report that ratio rather than soften it. Four measured nulls against one small
trial is the correct prior, and anyone promising administrative relief should be made
to say why this attempt differs from the four that did not work. Our answer, that the
previous four automated *storage and transmission* while the cost is in *composition
and judgement*, is a hypothesis and not a finding.

---

## 6. Where the hours actually go

In the only direct-observation study: **20% of class time on academic instruction,
17% on paperwork.**

Read those two numbers next to each other. The instructional minutes and the
compliance minutes are nearly the same quantity.

This changes what the honest pitch is. This survey has argued that AI's contribution
at the margin is *fidelity and dosage of known-good intervention* (§25). That remains
true. But the largest practical contribution available today is probably
administrative — and saying so strengthens the instructional argument rather than
conceding it, because every hour returned from paperwork is an hour available for the
thing with 4,000 effect estimates behind it.

---

## 7. Accommodations: mandated, and weak

§25 treated testing accommodations as part of the known-good base being scaled. That
was wrong, and the correction is uncomfortable enough to state in full:

- Kieffer et al., overall **g = .034, p = .180**
- Rios et al., across **N = 11,069**: **none statistically different from zero**
- Elbaum 2007: the effect **reverses** at secondary level
- Teachers assign accommodations **at chance** (N = 1,218)

Both halves have to be held at once. Accommodations are legally required and
evidentially weak. That is not an argument for withholding them. The legal
obligation is not contingent on effect size, and access is a right and not an
intervention. It is an argument against counting them in the efficacy column, and
against a system that recommends them as though it were prescribing something
measured.

The most useful thing an AI can do here is not select accommodations. It is to record
which were provided, so that somebody can eventually run the study that the field has
not run.

---

## 8. Escalation, and a null that should temper every safeguarding feature

Two figures define the gap. NIS-4 found that **≥80% of school-recognised maltreatment
never reached investigation, while CPS would have investigated 72%** of it. The
recognition is happening; the referral is not.

And the obvious fix has been tested. Wyman's randomised trial of gatekeeper training
moved **confidence by ES 1.22** and identification behaviour by nothing.

That pattern — large movement in how prepared people feel, zero movement in what they
do — is the felt-learning trap in a safeguarding costume, and it is the reason a
safeguarding feature must be measured on referrals made, never on staff confidence
or completion of a module.

---

## 9. The ownership line

The question a builder needs answered is not "can AI help" but "who owns this
artefact." The full table is in the source report, 17 artefacts across four columns;
the rule it produces is short:

> **An AI may draft anything and may author nothing that a signature attaches to.**

It may draft PLAAFP language from progress data, propose goal wording, assemble the
evidence packet, track service minutes, prepare a parent for a meeting, and surface
that a decision rule has fired. It may not author the IEP, determine eligibility,
decide placement, select a disability category, or arrive at a meeting with a
recommendation.

And one more, from §15.3: it may prepare options with their evidence. Never a
recommendation.

---

## 10. What the coordinator's week requires of a system

- **Argue both prongs of FAPE.** Substantive efficacy is half the statute. A system
  that ignores procedure is not deployable regardless of its effect size.
- **Draw the line at service versus method**, never at size of change. Methodology sits
  outside the meeting requirement; minutes of specialised instruction do not.
- **Present options, never a recommendation.** Every recommendation engine is a
  predetermination machine by default, and the regulator said so before AI existed.
- **State the four nulls whenever claiming administrative relief.** Computerisation,
  delegation, deregulation and the waiver authority all returned zero.
- **Never count accommodations in the efficacy column.** Required by law; not
  established by evidence; and assigned at chance.
- **Measure safeguarding on referrals**, not on confidence. ES 1.22 on feeling ready
  and zero on doing anything is the whole warning.

§25 asked what the evidence says a system should teach. This section is the answer to
a different question, and a coordinator would ask it first: **what is this allowed to
touch, and who signs.**


## 27. Who Is Not in the Room — reach, language, and the barriers attention does not remove

<sub>Source report: `research/raw/F4-reach-economics.md`</sub>

If attention stops being scarce, the natural conclusion is that everyone gets a
tutor. This section is the audit of that conclusion, and it does not survive
intact. What replaces it is more useful, because the remaining barriers are
nameable, rankable, and several of them are ours to fix.

The short version: **price was never the binding constraint, and language is.**

---

## 1. The graveyard, and why it is not an argument against trying

Every technology promised reach. The measured record of *hardware distribution* is
brutal and should be read before anyone writes a deployment plan:

| Programme | Learning effect |
|---|---|
| One Laptop Per Child, Peru (RCT) | **+0.003 SD** — effects above 0.11 statistically ruled out |
| OLPC Peru, 10-year follow-up | Grade progression **−0.010, p < .05** |
| Romania (home computer vouchers) | **−1/3 SD** |
| Israel | **−0.20 to −0.43** |
| Colombia, Uruguay, Nepal | Null |

Not "disappointing." Several are *negative*. Giving a child a device displaced
something that was working.

And infrastructure alone behaves the same way. A study of school electrification
taking coverage from **56% to 94%** found *"no evidence that electricity affects
test scores or enrollment."* Worldreader's iREAD programme in Ghana saw the
**control group beat both treatment arms** at senior high school, with **40.5%
device breakage**; the sponsor has since exited e-readers entirely.

The lesson is not that technology fails. It is that **the device was never the
intervention**, and a survey that skipped this would be repeating the error it is
documenting.

---

## 2. What actually worked, and the single word that separates them

Against that record, a set of interventions with real effects:

- **Teaching at the Right Level** — 0.14 to 0.70 SD
- **Mindspark** — 0.37 and 0.23 SD
- **Adaptive instruction 0.42** versus **non-adaptive 0.12** on comparable content

The separator is **targeting**: whether the instruction met the learner where they
actually were rather than where the curriculum said they should be. Not the
hardware. Not the bandwidth. Not the model.

Honesty requires the counter-example in the same breath: **TaRL has its own
scaling nulls**, in Bihar and Uttarakhand. Targeting is the ingredient; delivering
it at scale is a separate unsolved problem, and one that abundant attention
plausibly helps with more than it helps with anything else in this section.

---

## 3. The correction: gap-widening is a property of delivery

This survey has repeatedly warned that AI tutoring widens gaps — the strong pull
further ahead. Sierra Leone's effect loaded at **+0.195 SD per SD of baseline
mathematics**, and we have treated that as close to a law (§3).

It is not a law. Across **eight targeted interventions**, examined together for
this section: not one widened gaps, and several sharply narrowed them.

So the honest statement is:

> **Untargeted delivery widens gaps. Targeted delivery does not.** Gap-widening is
> a design failure we know how to avoid, not a property of the technology, and
> not a tax we have to accept.

That replaces a pessimistic finding with an optimistic one, and it raises the
standard: a system that widens gaps no longer has the excuse that everything
does.

---

## 4. The narrowest channel has the best evidence

The instinct is that reach improves with bandwidth: richer channel, better
learning. The measurements say close to the opposite.

| Channel | Effect |
|---|---|
| **Voice call + SMS** (5 countries, N = 8,902) | **+0.327 SD** |
| SMS only | **+0.083 SD** — null in Kenya, Nepal, Botswana |
| Interactive voice response | Null |
| Sierra Leone live calls (§3)| **−0.008**, null |

A phone call plus a text message outperforms most of what this survey has
examined. What the winning arm has that the others lack is **a human on the line
at a scheduled time** — accountability and targeting, delivered over the thinnest
possible pipe.

That is a standing rebuke to anyone specifying a 25 FPS avatar before they have
tried a phone call. It does not mean richer channels are worthless; it means the
mechanism is not in the bandwidth, and a rich channel that omits accountability
will lose to a poor one that includes it.

---

## 5. Language is the real barrier, and here are the numbers

This is the section's original contribution, computed by joining World Bank child
population data to a full multilingual benchmark table:

| Population | Share of the world's children |
|---|---|
| Have a functional model in their **official language of instruction** | **55.6%** |
| Have a functional model in the language they **speak at home** | **30.7%** |
| **Unmeasured entirely** — no benchmark coverage in any of their languages | **21.7% (~375 million)** |

Read the third row twice. For roughly **375 million children** we cannot state
whether a model works in their language, because nobody has measured it. That is
not a capability gap; it is a measurement gap, and it is cheaper to close.

The tractable part: a **0.55B fine-tuned encoder** cuts the below-50-score
population from **37.6% to 4.4%**. Small, targeted models move this enormously,
which is a genuinely hopeful result, since it means the fix does not wait on
frontier scale.

The stubborn part: that same intervention barely moves the unmeasured group,
because you cannot fine-tune against a benchmark that does not exist. And **no
learner-weighted multilingual benchmark exists anywhere**. Every benchmark
weights languages by convenience or by corpus size, never by how many children are
sitting in a classroom being taught in them.

Building that benchmark is a weekend of engineering and a year of coordination,
and it would be one of the highest-leverage artifacts in the field.

---

## 6. Ranking the barriers honestly

Nine barriers stand between a child and a tutor. Abundant attention removes
three.

| Barrier | Does abundant attention remove it? |
|---|---|
| Cost of expert attention-minutes | **Yes** |
| Cost of assessment and regrading | **Yes** |
| Availability at the hour the learner is free | **Yes** |
| **Language coverage** | No |
| **Connectivity** | No |
| **Devices** | No |
| **Evidence that it works for this learner** | No |
| **Institutional permission** | No |
| **Interface accessibility** | No |

Six of nine are untouched. A document that celebrated the first three and stayed
quiet about the rest would be marketing.

But note what kind of problems the remaining six are. Language is a measurement
and fine-tuning problem, tractable, and *now* tractable at 0.55B. Interface
accessibility is a design standard we already committed to. Evidence is
experiments we have specified and can run. Devices, connectivity and permission
are genuinely outside this document's reach and should be named as such rather
than absorbed into an optimistic sentence.

---

## 7. The counter-argument, and what we concede

The strongest case against everything here: *every prior technology promised reach
and delivered nulls; the populations most in need have the least connectivity; and
the true binding constraints are teacher capacity and institutional
infrastructure, neither of which a model touches.*

Four of that argument's premises we concede outright. The device record is null to
negative. Infrastructure alone does not move outcomes. Scaling kills effects that
worked in trials — TaRL's own scaling nulls prove it against a friendly example.
And the least-connected are the least reachable, which no amount of capability
fixes.

What we do not concede is the inference. Every null in §20.1 shares a structure:
something was distributed, and nothing was targeted. The interventions that
worked all targeted. Abundant attention is an input to targeting. It is what makes
meeting each learner where they are affordable at population scale for the first
time.

That is not a promise that it will work. It is the reason the experiment is worth
running, stated at the strength the evidence actually supports.

---

## 8. What we owe the people not in the room

- Never ship distribution as an intervention. If it does not target, it is a
  device programme, and device programmes have a measured record of zero.
- Try the phone call first. +0.327 SD sets a bar that most rich-channel designs
  will not clear.
- Report gap change as a primary outcome and never as a robustness check, because
  we now know targeted systems can avoid widening, so failing to is a defect.
- Treat language as the frontier it is. Publish in the learner's home language
  where a model supports it, state plainly where one does not, and contribute to
  closing the 21.7% measurement gap rather than routing around it.
- Name the six barriers we do not remove, every time, in the same breath as the
  three we do.

The title of this section is the discipline it asks for. Every claim about reach
should be checkable against a specific person who is not in the room — and for
375 million children, we cannot currently say whether the room would even be in
their language.


## 28. What We Owe Children — the legal floor as a design specification

<sub>Source report: `research/raw/F8-safety-privacy-children.md`</sub>

**Corrected 2026-07-28, and the correction is time-sensitive.** An earlier draft of
this section said the EU AI Act's Annex III education obligations begin to apply on
2 August 2026. They do not. **Regulation (EU) 2026/1744** — the Digital Omnibus on
AI, done at Strasbourg 8 July 2026, published as OJ L 2026/1744 on 24 July, in force
**27 July 2026** — replaced Article 113's third paragraph point (c). Verified against
the EUR-Lex primary text:

> *"…it is appropriate that the date of application of Sections 1, 2 and 3 of Chapter
> III is set to **2 December 2027** for AI systems classified as high-risk pursuant to
> Article 6(2) and Annex III, and to **2 August 2028** for AI systems classified as
> high-risk"* pursuant to Article 6(1).

Note what did **not** move. Article 113's first paragraph is unamended and Chapter IV
is not carved out, so **Article 50 — transparency, chatbot disclosure, synthetic-content
marking — still applies from 2 August 2026.** For a conversational tutor that is the
live deadline, and it is days away instead of eighteen months.

Two sources that a reasonable person would check both give the wrong answer today:
`artificialintelligenceact.eu` is still stamped "last updated 1 August 2024," and the
Commission's own Digital Omnibus page still describes only the proposal. This is
the case our editorial standard exists for — we published an unverified date,
flagged it as unverified, and corrected it against the primary text within a day.

The deferral changes the *deadline*, not the *design*. Read the Act and you will find
that the regulator has already written most of the architecture document for an AI
tutor — with more precision, and more courage, than the field has managed for
itself.

The legal floor is not an obstacle course laid across a good product. It is a set
of load-bearing constraints that coincide, almost line for line, with what the
evidence in the rest of this survey independently says a tutor should do: keep
the learner's record local and deletable, refuse to infer what the child *is*,
put a named human at the end of every consequential path, and never ship a
classifier whose errors land on the children it claims to serve.

---

## 1. The clause that ends the compliance argument

Annex III, point 3(b) makes high-risk any AI system "intended to be used to
evaluate learning outcomes, including when those outcomes are used to steer the
learning process." The operative verb is *evaluate*; the "including when" clause
extends the trigger rather than narrowing it. On the face of the text there is
no formative-assessment exemption, no it's-only-a-suggestion exemption, and no
the-teacher-is-still-in-the-loop exemption.

Article 6(3) offers a derogation for systems that perform a narrow procedural
task, improve a completed human activity, detect deviations from prior
decision-making, or prepare an assessment. Every adaptive-tutoring roadmap that
plans to argue its way out of high-risk classification plans to argue one of
those four. Then comes the sentence that closes it. A system

> "shall always be considered to be high-risk where the AI system performs
> profiling of natural persons."

GDPR Art. 4(4) defines profiling as automated processing to evaluate personal
aspects, in particular to analyse or predict performance, interests, reliability
or behaviour. **A learner model — a persistent per-child representation of
mastery, misconception, pace, and next-best-action — is profiling under that
definition, so no product that keeps one can self-exempt via Article 6(3).** The
escape hatch is closed by the exact artefact that makes the product worth
building. And Article 6(4) means self-exemption is not silent: a provider
claiming the derogation must document the assessment before market and register
the system anyway.

Two secondary readings are open rather than settled. Annex III 3(b) lacks the
institutional limiter that 3(c) and 3(d) carry, which on plain text pulls
direct-to-consumer tutors into scope; no authoritative construction was found.
The second is now settled, and settled against what this paragraph originally said.
It was drafted from a timeline source stamped 1 August 2024, with EUR-Lex
unreachable, and it concluded: *do not plan on a delay.* EUR-Lex was reached on
2026-07-28. **The delay is real.** Regulation (EU) 2026/1744 defers Annex III to
**2 December 2027**, while Article 50 still applies from **2 August 2026** — the
correction at the head of this section carries the operative text. Check Article 113
against EUR-Lex before making any compliance decision; a claim of this kind sourced
from a secondary tracker was wrong within eighteen months.

The practical consequence for a builder is not defensive. The conformity
artefacts (risk management, data governance, logging, human oversight, and a
Fundamental Rights Impact Assessment under Article 27 for public deployers) are
procurement assets. A state school buying an adaptive tutor has a legal duty to
produce a FRIA. Ship an honest pre-populated template, including a candid list of
the groups your system underserves, and you have handed the customer the hardest
part of their own compliance. Don't, and the school will find those groups
without your help.

---

## 2. The prohibition that clears the field

Article 5(1)(f) prohibits outright (not as high-risk, and applicable since
2 February 2025) "AI systems to infer emotions of a natural person in the areas
of workplace and education institutions." Read with Art. 3(39) (emotion
inference *on the basis of biometric data*) and Art. 3(34) (biometric data
includes behavioural characteristics, "such as facial images"), this means:

| Technique | Status |
|---|---|
| Webcam frustration / boredom / engagement detection | **Prohibited** |
| Voice-affect scoring in a spoken session | **Prohibited** (voice is biometric; COPPA agrees, §32.3) |
| "Sensor-free" affect detection from clickstream and latency | **Grey zone** — turns on whether interaction traces are "behavioural characteristics" under 3(34) |

That third row is the sharpest open legal question in the field — it determines
the legality of a substantial body of published AIED work in the EU, and no
authoritative construction was found. Treat it as prohibited until there is one.

Here is why this is a gift rather than a loss. The design move it forces is
**affect response without affect inference.** A tutor may respond to what the
learner says ("I'm stuck", "this is boring") and to behavioural facts (three
wrong answers, forty seconds idle, a session abandoned mid-problem). What it may
not do is maintain a durable variable named `frustration_level`. Generalised:

> **A learner model may hold what the child has demonstrated. It must not hold
> what the child is.**

Mastery of subtraction with regrouping is demonstrated. Dyscalculia is an
identity claim. Article 5(1)(b) independently prohibits exploiting
"vulnerabilities of a natural person... due to their age, disability," which
attaches directly to any engagement mechanic tuned using an inferred condition.

The architecture that satisfies all of this is **derive-and-discard**. Computing
within a single turn that a learner is probably struggling with phonological
decoding, in order to choose the next scaffold, and then throwing it away, is
teaching. Writing `suspected_dyslexia: 0.72` to a durable record creates health
data under GDPR Art. 9(1), a retained record under 16 CFR 312.10, and an
IDEA-destroyable record under 34 CFR 300.624 simultaneously — with none of the
clinical process, appeal rights, or accuracy guarantees of a diagnosis. Data
minimisation is conventionally a collection rule. For a learner model it is a
*persistence* rule.

---

## 3. Deletion is an architecture, not a policy page

COPPA's 2025 amendments (16 CFR Part 312, full compliance required since 22 April
2026) do two things that matter here. § 312.10 states categorically: **"Personal
information collected online from a child may not be retained indefinitely,"**
with a written retention policy required and published. And § 312.2 now expressly
counts as children's personal information "voiceprints... facial templates... or
faceprints," plus "a photograph, video, or audio file where such file contains a
child's image or voice." **A multimodal tutor collects COPPA-regulated biometrics
by default, on turn one**. That is not a corner case of the live-video architecture
in the next section but its baseline condition.

IDEA is stricter still. 34 CFR § 300.624: when personally identifiable
information is no longer needed to provide educational services, the agency must
inform parents, and **"The information must be destroyed at the request of the
parents."**

This survey stated the consequence once already, in the section on designing for
the margin, and it is worth restating because it is the most under-appreciated
engineering fact in children's edtech. If a child's interaction history has been
folded into model weights, a shared embedding index, or a cross-learner prior,
you can delete the row and you cannot delete the influence. Undeletable
learner state is a compliance failure for precisely the population an adaptive
tutor claims to serve best. The positive form: per-learner state genuinely
deletable, and no cross-learner training without irreversible, pre-storage
de-identification.

A correction to a widely-held belief. The FTC's 2025 final rule did not
codify a school-authorisation exception for edtech. After roughly 300 comments
the Commission recorded that it "decided against adopting some proposed changes,
including... changes relating to the requirements applicable to educational
technology companies operating in a school environment." Edtech continues to rely
on non-binding enforcement guidance. Any architecture premised on a codified
school exception is premised on something the Commission explicitly declined to
enact.

---

## 4. inBloom, and the null result inside it

inBloom was a $100 million initiative funded by the Gates Foundation and
Carnegie Corporation, launched publicly in February 2013, closed in April 2014.
Nine states committed, representing over 11 million students. The engineering was
strong; contemporaneous accounts describe better security and more access
controls than the incumbents. Its legacy is over 400 pieces of state-level
student-data-privacy legislation and this sentence from the definitive
post-mortem: "To date, no large-scale educational technology initiative has
succeeded in American K-12 schools."

The objection was never the schema. The mobilising parent letter names storage
location, disclosure recipient, commercial purpose, and category sensitivity.
The teachers' union endorsed the data model and rejected the custody arrangement
in a single sentence: gathering data on students is "a valuable tool," but
sharing 400 categories of student-identifying data with private companies — "how
can we possibly countenance that?" The killing blow was a custody rule in the New
York state budget forbidding the state to share identifiable student data with
any shared-learning-infrastructure provider. Closure came a month later.

And here is the documented disconfirmation, which deserves its own space
because it is the strongest counter-argument available. inBloom's own product
lead, quoted in that same post-mortem: *"inBloom did not have a privacy problem,
inBloom did not have a parent problem. InBloom had an advocacy and perception
problem."* The Data & Society authors lean the same way, identifying the root
cause as low public tolerance for risk plus a failure to communicate benefit.
"Trust was one of the most frequently used words in our interviews."

That is a real disconfirmation of the naive custody thesis and it should be held
and not waved away. The rebuttal is narrow: what could not be communicated *was* the
custody arrangement. The answer to "who holds my child's health and discipline
record, and who can they give it to?" was "a third-party non-profit, in a
commercial cloud, disclosing to for-profit app vendors under district
authorisation," and no communications strategy makes that sentence land. The same
report records that answering custody questions with FERPA-compliance language
actively hardened opposition.

The design rule that survives both readings: **if your custody architecture
requires a communications strategy to survive contact with a parent, you have
the wrong custody architecture.** The test is five questions answerable on one
screen, without counsel — where does my child's record live and under whose legal
control; who by name can read it; does it leave for any purpose other than
teaching my child; does my child's data improve your product for other customers;
how do I delete it and what survives deletion. If any answer needs a diagram, it
is not shippable to a public school system.

---

## 5. Abolish the detector

Seven widely-used GPT detectors, evaluated on 91 human-authored TOEFL essays and
88 US 8th-grade essays:

| Corpus | Average false-positive rate |
|---|---|
| US 8th-grade essays (native writers) | **5.19%** |
| TOEFL essays (non-native writers) | **61.22%** |

All seven detectors unanimously flagged 18 of the 91 TOEFL essays; **89 of 91
(97.80%) were flagged by at least one detector.** An ~11.8× disparity, and in
any institution running more than one tool, essentially the entire non-native
population is exposed.

The mechanism is perplexity, and the mechanism is the whole argument. Non-native
essays had significantly lower text perplexity (P = 9.74E-05), confirmed
independently on 1,574 pre-ChatGPT ICLR abstracts where authors in
non-native-English countries wrote lower-perplexity text (P = 0.035). Enriching
the TOEFL essays' word choice dropped the FPR from 61.22% to 11.77%; simplifying
native 8th-grade essays "as if written by a non-native speaker" moved them from
5.19% to 56.65%.

Now name who is *taught* to write with low perplexity, as a documented
accommodation: English learners given sentence frames and paragraph templates;
students with dyslexia or dysgraphia given explicit paragraph schemas to offload
working memory; autistic students given structural templates; and every student
in a high-pressure school where the five-paragraph essay is the writing pedagogy.
**The scaffold is the predictability. Therefore the better a student complies
with their prescribed writing accommodation, the more likely a detector is to
accuse them of cheating.** No threshold setting fixes this, because the
accommodation and the detection signal are the same variable — and the students
most exposed are the least equipped to contest an allegation.

"Use with caution, as one signal among many" is not an available position. With
a 61.22%/5.19% split there is no defensible Bayesian update to perform; "one
signal among many" degrades in practice into "the reason a conversation
started," and for a fifteen-year-old the conversation *is* the punishment. And
the tool fails at its stated job: a one-line self-edit prompt collapsed
detection on generated Common App essays **from 100% to 13%.** It catches the
honest and misses the dishonest.

The regulatory and ethical cases converge. Annex III 3(d) separately classifies
detection of prohibited behaviour during tests as high-risk, with Article 15
accuracy obligations a tool carrying a 61.22% subgroup FPR cannot plausibly
meet. Conclusion: abolition, not caution. Do not possess the capability,
because possession guarantees eventual use. The replacement is assessment
redesign — in-class writing, process artefacts, oral defence, version history,
staged drafts.

---

## 6. The component four authorities independently asked for

A tutor that is patient, never tired, non-judgemental and available at 11pm on a
Sunday is *structurally optimised* to receive disclosures a teacher will never
receive. That is not a risk bolted onto the product; it is a consequence of the
product working.

Statutory guidance is unusually specific about what follows. KCSIE 2026 Part One
¶14: staff "should never promise a child that they will not tell anyone about a
report of any form of abuse." ¶15: a victim "should never be given the
impression that they are creating a problem by reporting." ¶56: act "immediately."
¶59: unavailability of the safeguarding lead "should not delay appropriate action
being taken." ¶60: "Staff should not assume a colleague or another professional
will take action."

Each is a product requirement. ¶14 forbids a persona that says or implies *this
is just between us*. ¶15 means a canned "I can't help with that, please talk to a
trusted adult" deflection is a safeguarding failure and never a safe default. ¶59
forbids a weekly review queue. ¶60 forecloses "the school's own systems will
catch it." The APA's June 2025 advisory, AI Act Art. 26(2) human oversight, and
ICO AADC Standard 15 converge on the same missing piece: a named human on the
other end.

The evidence says this is tractable and says exactly where the failure mode is.
Detection is good enough to route: on 540 annotated real hotline transcripts
across 64 models, **F1 = 0.880 for suicidal-ideation detection and 0.907 for risk
assessment** — comparable to trained human operators on plan identification.
Good enough to route, nowhere near good enough to decide. And the dominant
failure is not what people expect: against 2,075 structured mental-health
prompts, hallucinations occurred in 6.5% of responses but **omissions in 13.2%,
concentrated in crisis and suicidal-ideation prompts.** The model rarely says
something harmful in a crisis; it fails to say the necessary thing. **A safety
eval that measures only harmful output will pass a system that silently drops the
escalation.** Omission rate, disaggregated by language and dialect, is the
primary safety KPI.

Second documented null, and it cuts toward optimism. An ecological audit of
over 20,000 real conversations found that adversarial benchmarks substantially
overstate real-world failure. A purpose-built mental-health AI with layered
suicide/NSSI safeguards produced enabling or harmful content on 0.4–11.27% of
benchmark prompts against 29.0–54.4% for general-purpose LLMs, and clinician
review of flagged real conversations "identified zero cases of suicide risk that
failed to receive crisis resources."

The wrong inference is that safeguards are unnecessary. The right one is that
the safeguards worked — the zero-miss came from layered engineering and not from
a good base model with a careful system prompt, and the same paper's 29–54%
figure shows the alternative. Benchmarks are not deployment evidence in either
direction; ecological audit is the method.

Two further nulls belong on the record. Across three AI-companion communities,
adults and women anthropomorphised chatbots more than teens and men — so
child-specific protections cannot rest on "children anthropomorphise more." They
rest on reduced capacity to exit, reduced legal agency, and developmental stakes,
which is a different and sturdier argument. And the widely-cited OpenAI × MIT
dependence result is correlational, heterogeneous, tail-concentrated, and
measured on adults. Design for the tail; do not claim the population.

---

## 7. The floor we will build on

- **No emotion inference, ever.** Art. 5(1)(f) is a prohibition, not a risk
  tier. Build affect *response* from stated signals and behavioural facts.
- **Assume high-risk and ship the paperwork as a feature.** A learner model
  forecloses the Art. 6(3) derogation. The FRIA template is a sales asset.
- **Deletable by construction.** No cross-learner training on identifiable
  records; no indefinite retention; per-child state genuinely destroyable. The
  row *and* the influence.
- **Hold what the child demonstrated, never what the child is.** Transient
  derivation is pedagogy; persistence is a dossier.
- **Custody first, data model second.** Five questions, one screen, no diagram.
- **No AI writing detector, in any configuration.** 61.22% vs 5.19%; 100% → 13%
  under one prompt.
- **No product for children without a named human escalation recipient**, a
  published SLA, and omission rate as the primary safety KPI.

What the law forbids here is almost exactly what the evidence says does not work
anyway: inferring fixed traits, retaining what you cannot justify, tuning
engagement to a vulnerability, and shipping a classifier whose errors land on the
children who can least afford them. The floor turns out to be a good place to
build from.



---

# Part VI · The field, and what it has already built

*The frontier's actual capabilities, the artifacts other people have shipped, the pedagogical canon that settled most of this decades ago, and the question of whether anyone wants to continue.*


## 29. The Substrate — what the frontier actually supplies

<sub>Source report: `research/raw/A4-live-multimodal.md, research/raw/A5-world-models.md, research/raw/D1-frontier-quarter.md`</sub>

Humans take the floor in conversation with a modal gap of **100–200 ms**, and
51–55% of all turn transitions across corpora happen in under 200 ms. That is
faster than language production: encoding a single word takes about 600 ms from
stimulus to speech onset, and a complex sentence roughly 1,500 ms. The arithmetic
only works if the listener predicts the end of your turn and plans their reply
*while you are still talking*.

Moshi, the open full-duplex speech model, reports **160 ms theoretical latency,
200 ms in practice**, which is inside the human window. It gets there the same
way people do, by modelling its own stream and the user's in parallel instead of
waiting for a silence timer.

That is the shape of the whole section. The frontier now supplies pieces that are
genuinely new: a conversation that can be interrupted, a camera that can see a
page of homework, a face that renders at video rate on one consumer GPU, and a
world conjured from a sentence. Each arrives with a hard edge, and in every case
the edge is somewhere other than the marketing suggests.

---

## 1. The duplex layer is real, and the good version is not for sale

Two vendors ship a managed real-time speech-to-speech loop. The differences that
matter for teaching are not the model quality.

| | Gemini Live | OpenAI Realtime |
|---|---|---|
| Transport | WebSocket only | **WebRTC**, WebSocket, SIP |
| Vision in | JPEG/PNG frames, **≤ 1 FPS** | `input_image` items; no documented native video |
| Session limit | **15 min audio-only; 2 min audio+video**; connection ≈ 10 min | not documented |
| End-of-turn | tunable VAD, 500–800 ms recommended | server VAD **or `semantic_vad`** (eagerness caps 8/4/2 s) |
| Barge-in bookkeeping | discarded generation dropped from history | auto-truncate on WebRTC; **manual on WebSocket** |
| In-session tools | function calling, Search. **No code execution** | function calling + **MCP** |
| Silent side-channel | — | **out-of-band responses** (`conversation: "none"`) |

Two of these decide whether you have a tutor.

**Barge-in bookkeeping.** Gemini's rule is that on interruption "only the
information already sent to the client is retained in the session history", so
the model's memory of what it said matches what the student actually heard. OpenAI's
WebRTC path matches this; the WebSocket path pushes truncation to the client, and
their own docs concede the model "doesn't have enough information to precisely
align transcript and audio." Get this wrong and the tutor believes it explained
step 3 when the learner only heard step 2 — a correctness bug that looks like a
student being obtuse.

**Endpointing is the latency budget.** Default server VAD is a 500 ms silence
timer plus 300 ms prefix padding. **That configuration alone exceeds the human
modal gap by 2.5–5× before the model has done any work.** Neither vendor
publishes an end-to-end latency figure anywhere in their documentation. Any
millisecond number in this survey comes from an academic system or a local
measurement, never from a vendor page. `semantic_vad`, a model-based
turn-*prediction* in place of a silence timer, is the closest shipped analogue
of what the turn-taking data says humans do.

**And the pedagogically correct target is not minimal latency.** Silence beyond
about 700 ms is socially marked, but in tutoring marked silence is often exactly
right; wait time is an instructional variable. The design goal is
**controllable** latency: fast for acknowledgement, deliberately slow for "think
about it." Human parity (≤ 250 ms) needs Moshi-class full duplex and is not
reachable on hosted APIs with default VAD; 300–800 ms feels natural on WebRTC
with aggressive semantic VAD and no avatar; 800–1500 ms is a comfortable tutor
including a real-time face; beyond 2 s — where open avatar stacks currently sit
at a self-reported 2.2 s — is annoying, and cascaded VAD→ASR→LLM→TTS pipelines
land past 3 s, which is broken.

The genuinely new architecture arrived in July 2026 and you cannot build on it.
GPT-Live listens and speaks simultaneously, backchannels, stays silent while you
think, and delegates a hard sub-problem to a frontier model *in the background
while continuing to talk*. That is the shape of a tutor saying "hold on, let me
think about that" without dropping rapport. It is ChatGPT-only. The API is a
sign-up form. **The highest-value capability of the quarter is, for builders,
unavailable**, and anyone planning a build this year should plan around its
absence.

---

## 2. What the camera can and cannot see

Vision into a live session is stills at one frame per second. It is not video,
and that single constraint sorts the use cases cleanly.

- **Camera on paper: works, today, on both platforms.** A worked problem is a
  static artifact; 1 FPS is more than enough. This is the strongest live-vision
  use case in education and it is available now.
- **Screen share of code: works,** and is well matched — code changes slowly.
- **Watching a *process* does not work.** A pen moving, a lab technique, a
  physics demo, sign language. 1 FPS discards the information that makes
  procedural feedback possible. Anyone claiming "the AI watches how you
  solve it" is over-claiming: it watches snapshots of the result.

There is no code execution inside a live session on Gemini Live at all, and
neither API has any output channel other than audio, transcript, and tool calls.
No cursor, no overlay, no highlight primitive.
Deixis, the "*this* term, *that* bracket" that is among the most powerful moves a
human tutor makes, has to be reconstructed by your own client from a model
reasoning about coordinates in an image it saw at ≤ 1 FPS.

A correction the project owes its readers here. The research behind this
section concluded flatly that "the pointing layer does not exist" and that
nobody had built a shared-pointing surface. The project's own correction ledger
subsequently records a deixis substrate in the literature (arXiv:2604.02893).
The revised claim is narrower and still true: **no vendor exposes deixis as a
primitive in a live session.** The design space is open without being empty.

---

## 3. The face: 25 FPS on one GPU, and no measured learning effect

The avatar layer has a sharp architectural dividing line where you would expect
a gradient.

Implicit-keypoint and warping models run at video rates on consumer hardware:
LivePortrait at **12.8 ms per frame on an RTX 4090**; MuseTalk at 30 FPS at
256×256 on a V100; SoulX-FlashHead-Lite at 96 FPS, or **three concurrent
real-time streams at 25+ FPS on a single 4090**. Diffusion-video models do not
and, so far, cannot: Wan 2.2 S2V requires ≥ 80 GB VRAM for single-GPU
inference, and the *fast* member of that family generates a 5-second 720p clip
in under 9 minutes on a consumer GPU. **That is roughly 108× slower than real
time.** Those are pre-render tools for canned lesson segments, not live-loop
renderers, and no local hardware short of a multi-GPU node changes the category.

So a locally-rendered talking tutor at 25 FPS is buildable today. The question
is whether it should be, and here the evidence is unusually clean and unusually
deflationary.

The null, stated at full strength. Three field experiments in real
university courses, using exam-relevant videos over 30 minutes taught by a
personally known instructor, compared a visible instructor with no visible
instructor:

> "positive effects of a visible instructor... on **some affective measures**:
> social presence in Study 1 (n = 18, d = .85) and well-being in Study 3
> (n = 38, d = 1.01)... They also show **no effects on extraneous processing or
> learning outcomes** (Studies 1–3). Thus, **no general effect of instructor
> presence can be shown**... but there are also no detrimental effects."

**A face reliably makes learners feel better and does not reliably make them
learn more.** The meta-analytic base agrees on
magnitude — pedagogical agents at **g ≈ 0.19** across 43 studies and 3,088
participants, **g ≈ 0.20** in an independent multimedia synthesis. (Both figures
were recovered from citation contexts and not from the paywalled originals;
re-verify before publication.) And in the same analysis, **agents communicating
via on-screen text outperformed agents communicating by narration**, the
opposite of the voice-first, face-first product thesis. The larger 2025
GenAI-agent effects (g ≈ 0.36–0.40) compare an AI tutor to *no tutor* and never
an agent with a face to the same agent without one: they measure the model, not
the avatar.

Two things the evidence does support. Embodiment helps *relative to a static
agent*. Gestures, gaze and expression beat their absence on a transfer test,
which is an argument about how to animate rather than whether to show a face.
And reducing consistency in human realism increases the uncanny effect, so a
photoreal face with slightly-off mouth motion is worse than a stylised face with
the same motion. Cartoon-quality avatars are an engineering choice and not a
compromise.

**Build the face for social presence and willingness to keep going, and say
exactly that.** Persistence is a learning input. It is not a learning gain.

---

## 4. Generated worlds: the measurement everyone skips

Genie 3, on DeepMind's own numbers: 720p, 24 fps, "a few minutes of continuous
interaction," visual memory "extending as far back as one minute ago," promptable
mid-session world events that alter weather or introduce objects. A real step
change — real-time interactive is qualitatively different from clip generation.
It is also a US-only, 18+, $200/month consumer tier with no API, no export and no
persistence guarantee, and **no technical report exists for Genie 2 or Genie 3.**
Every capability claim in that lineage is a vendor blog post plus curated demo
reels.

Now the benchmarks, which point the other way.

| Benchmark | Result |
|---|---|
| **VideoPhy** | Best model satisfied prompt *and* physical law in only **39.6%** of instances |
| **VideoPhy-2** | Best joint semantic + physical performance on the hard subset: **22%**. Models "particularly struggle with conservation laws like mass and momentum" |
| **PhyGenBench** | 160 prompts, 27 physical laws. "Simply scaling up models or employing prompt engineering techniques is **insufficient**" |
| **Physics-IQ** | "Physical understanding is severely limited, and **unrelated to visual realism**" |
| **WorldModelBench** | 14 frontier video models, 67K human labels; explicitly detects "irregular changes in object size that breach the mass conservation law" |

Five consequences make this worse for education than for entertainment.

1. **The failure modes are the curriculum.** Conservation of mass and momentum,
   object permanence, cause and effect. Not cosmetic glitches.
2. **Fidelity decouples from correctness.** A photoreal world that violates
   momentum conservation is *more* dangerous than a crude one, because realism is
   the cue learners use to decide whether to trust what they see.
3. **Scale does not fix it.** Tested directly, and failed. "Wait for the next
   model" is not an available argument.
4. **There is no error signal.** In a hand-built simulation an incorrect
   behaviour is a bug someone can file. In a generated world there is no ground
   truth, no reference implementation, no test suite, and no way for a
   fourteen-year-old to know the pendulum they just watched had the wrong period.
   Genie 3's own stated inability to render legible text unless it was in the
   prompt removes the one channel by which a world could label itself.
5. **Misconceptions persist.** The entire conceptual-change literature exists
   because they resist instruction once installed.

The counter-argument deserves its space. A 2025 paper argues video models are
zero-shot learners and reasoners, reporting emergent segmentation, physical-
property understanding, affordance recognition and "early forms of visual
reasoning" in Veo 3. Two of its authors are also authors on Physics-IQ, the paper
that found physical understanding "severely limited." Both are true: capability
is rising fast and is real, and the paper's own hedges are "early forms" and
"emergent," which is not the same as reliable. Teaching requires reliable.

---

## 5. The decomposition: generative world, symbolic physics

The design that follows splits the substrate in two.

> **Let the model author the world. Let a verified engine own the event
> stream.**

The *world* is scene, setting, narrative, character, task framing, the language
of the thing. Variety is the point there, and a generative model is unbeatable
at it. The *event stream* is physics, causality, inventory, state transitions,
progression, anything a learner might generalise from. There a single wrong
frame teaches a misconception, so it belongs to a physics engine, a computer
algebra system, or a plain symbolic state machine.

Three lines of evidence converge on this.

**Generated code beats generated pixels, and it has been tested in a real
course.** The CU Boulder group behind PhET ran a three-condition study in
second-semester physics for life-science majors: physical equipment, a prebuilt
simulator, and students generating their own simulation with AI. Conceptual
assessment showed **η² = 0.359**, a large effect, and post hoc **both simulation
conditions scored significantly higher than the physical-equipment condition**,
with AI-generated not distinguishable from prebuilt. The mechanism was
LLM-generated simulation *code*, and the pedagogy the authors highlight is
"designing, refining, and validating" — students checking the AI's simulation
against the physics they were learning. The model's fallibility became the
learning objective. **This is the only pattern found anywhere in this research
that is robust to model error rather than dependent on its absence.** It is also
a single preliminary study, one topic, one course; do not inflate it into
"generated worlds teach as well as PhET."

Symbolic worlds already work and are almost free. ScienceWorld is an
interactive text environment at fifth-grade science curriculum level, with state
maintained by a symbolic simulator and therefore correct by construction. Its
headline result belongs in any argument about substrate: **a 1.5M-parameter agent
trained interactively for 100k steps outperforms an 11B model statically trained
on millions of expert demonstrations.** Learning by doing beat learning by
reading, in a world that could not be wrong about itself.

And the category error worth correcting explicitly. Kimi K3 circulates in
summaries as a world model that creates interactive worlds. Moonshot's own
release blog **never uses the words "world model," "simulation," "physics," or
"environment."** What it says is that K3 "combines strong 3D reasoning, coding,
and vision capabilities to turn concepts, images, and videos into fully playable
interactive experiences," achieving "vision in the loop" by iterating between
code and live screenshots. That is code generation. There is no world model in
Moonshot's catalogue, no K3 repository, and the one repo with a suggestive
name, WorldVQA, is a *world-knowledge* visual-QA benchmark. **K3 writes
interactive software; Genie dreams pixels. Listing them together is a category
error.**

And this is good news. A programmed world's physics is whatever engine or update
loop was emitted. That is inspectable, deterministic, debuggable, unit-testable
against analytic solutions, version-controlled. Generated pixels are unauditable
by construction.

---

## 6. The nulls that should change what you build

Long context is a non-event for learning. A whole textbook has fit
comfortably in context for over a year; 1M tokens is now the default across an
entire commodity vendor's services. Yet a targeted arXiv query for
long-context / whole-textbook educational grounding returned **literally zero
results**, while curriculum-RAG is one of the healthiest clusters in the same
sweep. The field looked at "put the textbook in the window" and chose retrieval.
That is not inertia — the binding constraint was never capacity, it was
attribution. A teacher needs to know which page the claim came from, and a
stuffed context window destroys that affordance while adding cost and latency.

**Model capability does not transfer to tutoring capability, and there is now a
number. Solving ability and pedagogical ability correlate at r = 0.421** on
public benchmarks. The maths a learner needs help with is not Putnam; it is
fractions, and the specific fraction misconception this specific child holds.
Every current model solves that perfectly. The unsolved problem is diagnosing the
misconception and choosing *not* to solve it, and no maths benchmark measures
that — note that two frontier labs published no maths claims at all in their most
recent flagship posts.

And the pedagogy layer is permanently yours. LearnLM no longer exists as a
model family; Google's own documentation states its capabilities were "integrated
into Gemini starting with the 2.5 model series." There is no model ID that
returns a tutor. What survives is a product surface built from system
instructions, and OpenAI's Study Mode is described the same way; independently,
training-free prompt optimisation was found to beat RL-trained pedagogical
baselines. Pedagogy is a prompt-and-product layer and not a weights layer. That
is simultaneously the largest opportunity here and the reason most frontier model
releases are irrelevant to this work.

---

## 7. The build rules this substrate forces

- **Full duplex is the target and endpointing is the budget.** 200 ms is the
  human number; a 500 ms silence timer plus 300 ms padding already blows it.
  Build for *controllable* latency. Minimum latency is the wrong target,
  because wait time is a pedagogical variable.
- **Camera on paper and screen, not on process.** 1 FPS stills are excellent
  for a worked page and useless for a moving pen. Say which one you built.
- **Barge-in must be bookkeeping-correct.** The model's memory of what it said
  must equal what the learner heard.
- **Render the face at 25 FPS locally if you want one. Claim affect; do not
  claim learning.** d ≈ 0.85–1.01 on social presence and well-being; no learning
  effect in real courses; g ≈ 0.19–0.20 overall. Stylised beats
  almost-photoreal.
- **Generative world, symbolic event stream.** 39.6% best-case and 22% on the
  hard subset are not numbers you teach conservation laws with. Let the model
  write the scene; let an engine own the dynamics.
- **Prefer generated code to generated pixels**, and where possible make
  *validating the generated model* the assignment.
- **Never use a generative world model as the authority on a physical law.**

The frontier supplied a great deal this quarter and moved learning very little.
The one exception in these seven subsections was a field trial in a real physics
course; no model release came close. A dozen new benchmarks arrived to test
whether a model is smart, and roughly one trial a year tests whether it teaches.
That ratio is the widest measurement gap in applied AI, and closing it is the
subject of the last section of this survey.


## 30. The Textbook That Writes Itself — and who it remembers

<sub>Source report: `research/raw/A1-ai-native-textbooks.md, research/raw/G3-future-of-learning-projects.md`</sub>

A model-authored machine-learning course was published to GitHub on 25 April
2026 in two commits, thirty-eight minutes apart: twenty chapters, roughly 57,000
words, twenty-three skill definitions, sixteen runnable example projects, and a
video-production workspace. It has not been touched since. `book.toml` names the
author honestly — `authors = ["OpenAI Codex with Xiaol"]`.

It ships a file called `BOOK_SUMMARY.md`. The first line explains what it is
for:

> "Use this file as compressed context when drafting future chapters or revising
> the manuscript."

That is persistent memory, correctly designed, so that authoring sessions stay
coherent across time. Every chapter also carries a `refs.md` with sections
titled *Concepts That Must Stay Stable* and *Reminders for Future Revision*.

The same repository ships **no persistence mechanism of any kind for the
reader**. The learner is told to "save a small artifact" — by hand, to their own
filesystem, in a format the book does not specify and nothing ever reads back.

**The authoring agent gets memory. The reader does not.** That single inversion
names the genre, and once you see it you cannot stop seeing it.

---

## 1. What the artifact actually does, measured

Credit first, because the artifact is better than its citation-free bibliography
suggests and the good parts are directly stealable.

| Measurement | Result |
|---|---|
| Example projects | **16** |
| Python LOC across examples | 1,940 |
| External dependencies | **numpy in 2 of 16**; the other 14 are stdlib-only |
| Wall clock, full run | **0.555 s** |
| **Committed outputs reproduced byte-identically** | **16 / 16 (100%)** |
| Test files, CI configuration | **0** and **0** |
| Dataset sizes | 3–84 rows (median ≈ 6) |

Set that 100% beside this project's earlier finding that **published Jupyter
notebooks reproduce their own stated results 4.03% of the time**. Two orders of
magnitude better, achieved with no infrastructure whatsoever. The mechanism is
pure subtraction: no external dependencies, no randomness, no network, no GPU,
no data download, tiny deterministic inputs, plain-text committed outputs.
**Reproducibility here was bought by removing things and never by adding a
container.**

Two more properties worth taking. The figures are generated by matplotlib from
the *same CSV the example scripts run on*, so the dataset diagram and the fitted
coefficient panel are not illustrations of the argument; they are renderings of
it. And each of the twenty-three skills carries an explicit **Quality Bar**, a
constraint on the generator authored by the curriculum and version-controlled
alongside it:

> - Do not recommend complexity before a naive and interpretable baseline exist.
> - Keep the comparison on the same split and metric.
> - Name at least one slice where the baselines may fail differently.
> - Treat simple models as instruments for understanding, not as embarrassment.

Treating the prompt-scaffold as a curricular object with versioned quality
criteria, rather than as disposable chat, is a small and genuinely novel idea.

Now the audit against the claims. `adaptive` appears in two files;
`personaliz*` in one; `spaced repetition` in **zero**. The four-level Reader
Ladder (Beginner → Builder → Engineer → Specialist) is declared in two planning
documents and the manuscript never branches on it. Chapters 13, 14 and 15
mention "beginner" zero times, and every reader gets identical text. `quiz`: 0
files. `answer key`: 0. `self-test`: 0. The "Extension Exercises" are five
ungraded prose prompts per chapter with no solutions, no tests, no keys. Nothing
can mark anything. And the twenty-entry bibliography contains no URLs, no DOIs,
and **not one citation to learning science, education research, or any evaluation
of AI tutoring.**

There are also no assertions. The scripts run and print; nothing can fail.
Reproducibility was established by diffing from outside, which is a different
property from verifiability. A reader who breaks something gets no signal.

One more number, because it is diagnostic. Counting fenced code blocks across
all 72 manuscript files: **64 `text` blocks (prompt scaffolds), 18 `bash`, and 3
`python`.** A 57,000-word machine-learning course contains three Python code
blocks and sixty-four prompt templates. All real code lives in a directory the
prose points at. That is the structural signature of a book *about* the harness
rather than a book *made of* one. Prose that merely points at its verifiable
content is free to drift from it.

**As a demonstration that a frontier model can produce a coherent, internally
consistent, fully reproducible technical curriculum in one sitting, this is
striking and should be cited that way.** As a design for how a human
learns, it is a static book with a prompt appendix.

---

## 2. The same inversion at population scale

A GitHub search for `AI native textbook` returns 123 repositories. A search for
the specific course most of them replicate, `physical ai humanoid robotics
textbook`, returns **501**. One cohort, one architecture, hundreds of times.

Two were inspected file by file. Both are dominated not by content but by
agentic authoring scaffolding. One carries `.claude/commands/sp.{specify, plan,
tasks, implement, analyze, clarify, checklist, constitution, adr, phr}.md` plus a
`.specify/` directory of templates and memory. The other, `Cognita`, ships 185
files including ten `.claude/skills/` directories:

> `chapter-analyzer` · `docusaurus` · `backend` · `chatbot` · `database` ·
> `deployment` · `devops` · `nextjs` · `auth` · `architecture`, **nine of which
> build the website**, and `robotics-tutor`, **which teaches**.

Nine to one. The genre has industrialised author-side agentic tooling and
shipped, as its learner-side contribution, a chatbot that can search the book.

This forces a correction to a positioning claim that circulates widely, including
early in this project. **"AI-native textbook" is not unclaimed ground. It is
saturated ground** — hundreds of near-identical RAG-over-Docusaurus builds. What
is unclaimed is everything those builds skip.

---

## 3. The ladder degrades monotonically, and here is where it breaks

Every course generator produces the same hierarchy: modules → chapters → topics →
exercises → quizzes. Generation quality falls as you descend it.
Modules are easy; they are an outline. Exposition is easy; it *is* the training
distribution. Exercises are hard. Answer keys are where it collapses.

The definitive measurement generated 240 programming exercises with sample
solutions and test cases, and manually evaluated 120:

| Property | Result |
|---|---|
| Sensible | 75.0% |
| Had a matching sample solution | 76.7% |
| **Sample solution executed without error** | **89.7%** |
| Included automated tests | 70.8% |
| **Sample solution passed the exercise's own tests** | **30.9%** (51 of 165) |
| Code-explanation lines that were correct | **67.2%** (117 of 174) |

Read 89.7% and 30.9% together. **The code runs. It just does not solve the
problem.** Syntactically valid, semantically wrong — and the prose has the same
signature: 90% of explanations covered all parts of the code while a third of
their lines were incorrect. Coverage and correctness are uncorrelated.

Corroboration from the item side: teachers rated only 53% of LLM-generated
multiple-choice distractors as high quality, meaning roughly **47% were
rejected**. A 2026 taxonomy names four hallucination types in MCQ generation:
reasoning inconsistencies, insolvability, factual errors, mathematical errors.
*Insolvability* deserves separate billing, because a generated exercise with **no
correct answer at all** is worse than one with a wrong key, and nothing that
merely validates the key's format will ever see it.

The mechanism is not mysterious. Exposition has a dense self-supervised training
signal — the internet is exposition. An exercise carries a verification
requirement the generator cannot discharge: exactly one correct answer, that
answer must be the stated one, distractors must be wrong-but-tempting, difficulty
must land in the learner's zone, and the item must discriminate. Five
constraints, none checkable from the text. **The 30.9% was only measurable
because programming exercises execute.** For history, biology, or conceptual
mathematics there is no oracle, so the equivalent error rate is not merely
unknown — it is unmeasured by construction.

---

## 4. Difficulty is learnable; discrimination is not

This is the null result that most changes what a course generator may claim, and
it deserves its own space.

Difficulty — what fraction of students get an item right — is moderately
predictable from item text. A systematic review reports best-case RMSE as low as
0.165 and Pearson up to 0.87; independent studies land at r ≈ 0.75–0.82.

Discrimination — whether the item separates strong students from weak ones —
is not. Direct prediction on reading-comprehension items reaches a best
**Spearman correlation of 0.152**, and response-based calibration only 0.241. A
separate benchmark reports that every model tested **"falls below random chance
on item discrimination."**

Difficulty tells you where to place an item on a ramp. Discrimination tells you
whether the item measures anything at all. **So a generated course can present a
perfect-looking difficulty gradient built entirely from items with no diagnostic
value — a ramp that looks right and assesses nothing.**

And the failure does not scale away. One study reports "systematic misalignment
where scaling up model size is not reliably helpful," and names the mechanism:
high performance often impedes accurate difficulty estimation. The model is
too good at the task to model a student failing it.

Prerequisite ordering fails in the same place. On the one curriculum-aligned
knowledge-graph benchmark available, frontier models reach 57% and 46% exact
match, with the report noting "Prereq and Neighbor being the hardest tasks."
Every learning-path recommender in the adjacent literature *assumes* a correct
prerequisite graph as input. Nobody has closed that loop, because closing it
requires generated items to arrive with valid difficulty parameters and valid
answer keys.

---

## 5. The corpus audit: authorial intent, not format

An original measurement, run against four zero-to-hero notebook corpora via the
GitHub API, counting occurrences of `exercise | your turn | quiz | solution |
practice problem | try it yourself`:

| Corpus | Notebooks | Files with ≥1 marker | Total hits |
|---|---|---|---|
| `karpathy/nn-zero-to-hero` | 7 | **1** | **4** |
| `rasbt/LLMs-from-scratch` (ch01–07) | 6 | 6 | 8 (+ 7 dedicated solution notebooks) |
| `fastai/fastbook` | 20 | **19** | **74** |
| `mrdbourke/pytorch-deep-learning` | 9 | **9** | **89** |

The canonical zero-to-hero corpus, the one the phrase comes from, has nine
files total, and not one filename contains exercise, homework, problem-set,
assignment, quiz, or solution. Six of its seven notebooks contain zero exercise
scaffolding. And the four markers that do exist are *pre-solved in place*: the
comment reads `# Exercise 1: backprop through the whole thing manually`, and the
answer is printed on the next line of the same cell. It is a section heading over
a worked example. **A naive grep reports 4 and is wrong in the opposite direction
from what you would expect: the strict count of exercises a learner must actually
do is zero.**

**But the generalisation people reach for is wrong, and this is the negative
result of the audit.** The pattern is *not* "notebook corpora lack exercises."
Three of the four are dense with them. All three are books — one from
O'Reilly, one from Manning, one a structured course. The variable is not format
and not language and not domain. **It is authorial intent: works written as books
have exercises; works written as lecture transcripts do not.** A roughly 20×
difference in exercise density between artifacts in the same language, the same
domain, and the same file format.

Lecture transcripts are demonstration, and demonstration has no slot for the
learner to fail in. Generation systems inherit that, because exposition
dominates the corpus, exposition has no verification requirement, and exposition
is what the demo shows well.

---

## 6. Nobody claims their AI writes the curriculum

Ten commercial products, and in every case where the split is disclosed, the
human keeps the pedagogy and the machine gets the prose or the conversation.

- Duolingo, verbatim: **"Humans write the scenarios that learners see in
  Roleplay."**
- Synthesis Tutor: **"leverages AI where appropriate while relying on our team of
  expert educators and neuroscientists to handle much of the pedagogy."**
- Khanmigo tutors *over* the existing human-authored Khan library.
- Ello licenses thousands of professionally authored books.
- SchoolAI: **"Every Space starts with a teacher."**
- Curipod: **"100% teacher controlled."**

The AI-native textbook does not exist as a shipped commercial product. What
ships is AI-native *delivery* over human-authored *structure*. The cleanest proof
comes from inside the most AI-native company in the set: a platform whose landing
page promises courses generated from your uploads was, at the time of this
research, running a free four-day residency in San Francisco, with housing,
meals, travel and a film crew, to recruit pairs of humans to **publish human-authored
courses with named human authors**. No mention of AI generation appears anywhere
on that page.

And the efficacy pattern is inverted in a way worth stating plainly. Across ten
products: five publish no outcome number at all; three publish internal
self-measured numbers with no methodology; one has an externally reviewed
correlational study (ESSA Level III, which is the *non-causal* tier); one cites
external state test data in self-selected case studies. **Zero RCTs. Zero effect
sizes. Zero preregistrations.** The heaviest generators publish only teacher
*sentiment*. The lightest, the ones that keep the teacher as author, hold the
only externally sourced outcome data. **Generation volume is inversely correlated
with evidence.**

---

## 7. Where our generator diverges from the genre

The forward half. Everything the genre skipped is cheap, and most of it is
already specified by what we just measured.

- **Build learner-side memory, not author-side memory.** This is the one thing
  that would matter most and the one thing the field consistently points at the
  wrong party. Author-side memory pays off during construction; learner-side
  memory only pays off after shipping, which is exactly why it does not get
  built.
- **A reader ladder that never branches is decoration.** If four levels are
  declared, four levels must be observable in the delivered text, conditioned on
  something real about this learner.
- **Ship the checker with the claim.** Scripts without assertions cannot fail,
  which means nothing in them can ever be known to have broken. Reproducible is
  not verifiable.
- **Buy reproducibility by subtraction.** 16/16 byte-identical against a 4.03%
  baseline, achieved by removing dependencies, randomness, network, and data
  downloads. The same profile is what ports to the browser.
- **Watch the prose-to-executable ratio.** 64 prompt scaffolds to 3 code blocks
  is diagnostic. When the verifiable content lives in a directory the prose
  merely points at, the prose will drift.
- **Generate exposition; do not generate the answer key unreviewed.** 30.9% is
  the number, and it is only knowable where an oracle exists.
- **Never present a generated difficulty ramp as an assessment.** Difficulty
  r ≈ 0.75–0.87; discrimination Spearman 0.152, below chance on one benchmark,
  and scaling makes it worse.
- **Hand the prerequisite graph back to a human, editably.** It is the
  worst-performing task in the only benchmark that measures it, and a
  hand-editable DAG is the concession that measurement forces.
- **Date every capability claim and name the model.** Undated capability claims
  silently convert into false present-tense claims.

The genre built the harness and pointed it at itself. The machine writes the
telling; the human still writes the doing. That division used to be a preference
and is now a measurement: 30.9% on answer keys, Spearman 0.152 on discrimination,
57% on prerequisites. The doing is the only part with a right answer that can be
wrong, and nobody has automated it.


## 31. The Canon — what the history of pedagogy already settled

<sub>Source report: `research/raw/I1-pedagogical-systems.md, research/raw/I2-global-traditions.md`</sub>

There is a single question that sorts every pedagogical tradition humanity has
produced into things worth rebuilding and things worth admiring from a distance:

> **Remove the other human and remove the physical objects. Is the thing the
> learner does still the thing that caused the effect?**

For the Keller Plan, yes. For chavruta, no. That one question does more work than
any amount of enthusiasm about AI tutors, and this section runs it across the
whole catalogue, including where it returns an answer the field would rather not
hear.

The thesis under test is the seductive one: *most great pedagogical systems were
abandoned for cost, not efficacy; if AI changes the cost structure, the question
is not what new pedagogy AI enables but which known-good pedagogy just became
affordable.* It is roughly two-thirds right, and the third that is wrong is the
third most likely to be repeated uncritically.

---

## 1. Where the cost actually sat

Start mechanically. A pedagogy's per-learner cost decomposes into seven
components, and AI does not touch them equally.

| Cost component | Does AI reduce it? |
|---|---|
| **Expert attention-minutes** (tutorial, mastery correctives, coaching) | **Yes — this is the big one.** |
| **Assessment and regrading labour** (unit tests, unlimited retakes) | **Yes, near-totally.** |
| Curriculum authoring and sequencing | Partly — generation is cheap; *validation* is not |
| Record-keeping and progress tracking | Yes; this was a first-order killer and is now solved |
| **Physical materials and space** | **No** |
| **Genuine peers with real stakes** | **No** |
| **Institutional and political permission** | **No — and this killed several systems outright** |

AI collapses two of seven components to near zero, substantially reduces two
more, and does nothing at all for three. **The thesis is therefore true for
pedagogies whose costs sat in the first two buckets**, and one system sat almost
entirely there.

---

## 2. The flagship vindication: PSI

Fred Keller's Personalized System of Instruction has five defining features:
written materials as the primary vehicle, chosen because text maximises learner
control; content divided into separable units with stated objectives and
prerequisite structure; **self-pacing**; **unit mastery** at roughly 90% before
progression, with multiple equivalent test forms so a retake is not a retake of
the same items; and **proctors** who administer and mark unit tests immediately,
certify mastery, and supply social reinforcement.

A meta-analysis of **75 comparative studies** concluded that PSI "generally
produces **superior student achievement, less variation in achievement, and
higher student ratings** in college courses."

The middle clause is almost never quoted. **Mastery designs compress the bottom
tail.** That is a distributional claim, and the margin is where it matters.

PSI died of administrative labour and proctor cost: item generation, immediate
marking, unlimited fresh retests, and record-keeping. Those are the two
components AI zeroes and the two it substantially reduces. Nothing in the
mechanism requires a human, because the proctor's function is certification and
immediacy rather than relationship. **PSI is the clean case, and it is the one
that should be built first.**

With one measured caveat carried in the same breath. Self-pacing is a documented
failure mode of PSI *and* of AI tutors, and the policy toolkits state that
mastery learning is "much less effective when students work at their own pace."
Rebuild the spine; add external pacing pressure.

---

## 3. The flagship refutation: Direct Instruction

Engelmann's Direct Instruction is not "the teacher talks a lot." It is a
faultless-communication engineering discipline: sequences designed so the
examples presented logically permit only the intended generalisation, scripted
wording to eliminate ambiguity, placement by assessment into skill-homogeneous
groups, signals and rapid response to maximise responses per minute, mastery
gating, and the load-bearing part: **sequences that were empirically debugged
over decades. If children misgeneralise, the script is what gets fixed.**

The evidence base is the strongest in this catalogue:

- **328 studies, 413 study designs, nearly 4,000 effect estimates**, 1966–2016.
  "All of the estimated effects were positive and all were statistically
  significant except results from metaregressions involving affective outcomes."
- **Characteristics of the publications, methodology and sample were not
  systematically related to effect estimates** — the absence of the small-study
  and publication-bias signature that discredits most of this literature.
- Effects showed little decline during maintenance and grew with exposure.
  Reported magnitude ≈ 0.6 SD. In special education: 25 studies, **none**
  favouring comparison groups.
- Project Follow Through, roughly **352,000 children, 178 projects, 20 sponsored
  models**, found DI strongest on basic skills and, contrary to the standard
  objection, found the structured models beat the unstructured ones on affective
  and self-concept outcomes too.

And DI is cheap: student workbooks around $20, teacher guides $180–232.

It won the largest educational experiment ever run and was then sidelined — for
teacher resistance to scripting framed as a constraint on creativity, for
ideological mismatch with constructivist orthodoxy, and for a dissemination
apparatus that went on to recommend programmes that had *not* been validated. A
former US Education Commissioner called endorsing all models when "only one of
the sponsors (Direct Instruction) was found to produce positive results more
consistently" "inappropriate and irresponsible."

**Cost was never the binding constraint. Professional identity and institutional
politics were, and AI has no purchase on those.** Attributing DI's fate to
economics is a factual error and this survey will not make it.

There is one genuine and underrated twist, and cost has nothing to do with it:
**an AI tutor has no professional identity to protect and cannot resent a
script.** The one thing that blocked the best-evidenced curriculum in education
is the one thing a machine does not have.

Which makes the failure mode obvious and worth naming loudly. DI's effect size
comes from *validated* sequences. **An LLM generating "DI-style" scripts on the
fly produces the form without the validation that is the entire source of the
effect.** That is the most likely route by which a product claims DI's evidence
base without inheriting any of it.

---

## 4. Four classes, and where each tradition lands

Class A survives fully. The mechanism is a property of the learner's
cognitive activity; the human was only the delivery vehicle. Mastery gating and
unlimited fresh retesting; scaffolding with contingency and fading (the only
mechanism whose *computer-based* version is directly meta-analytically validated,
ḡ = 0.46 across 144 studies); worked-example modelling; precision-teaching rate
measurement; productive-failure sequencing; DI's sequences *if validated*.

Class B survives with a named casualty. The tutorial keeps unlimited
"defend your work" sessions and loses **the fallible expert whose regard you earn
and whom you can argue into changing their mind.** Cognitive apprenticeship loses
the community of practice. The case method loses seventy-nine peers publicly
disagreeing with you. The Socratic method keeps questioning-instead-of-answering
and loses refutation and *aporia* — a model trained to be agreeable and resolve
tension will not leave a learner in productive puzzlement, and cannot honestly
occupy Socrates' position of not knowing the answer.

Class C does not survive. Chavruta needs a genuine equal with stakes who
cannot be dismissed by closing a tab. Jigsaw needs real interdependence. Peer
instruction needs a real distribution of peer misconceptions and real persuasion.
Harkness needs twelve prepared peers. The expensive input there is
not the teacher's attention but the ratio itself, which is what elite
private schooling purchases. Guild apprenticeship needs real production with real
consequences.

**Class D had no mechanism to port, because there was never a
measurement.** Waldorf, Reggio (except its documentation practice), Sudbury,
unschooling, Kumon's own evidence base, the Harvard case method specifically, and
the Oxbridge tutorial as such. **Building an AI version of an unmeasured
tradition does not create an evidence base. It creates an unevidenced product
with a prestigious name.**

A refinement this survey owes itself. An earlier section scored Montessori as not
surviving substitution, and a later one narrowed that: what fails to survive is
the wood, and what survives is the *refusal* — the property that a well-made
material cannot be assembled wrongly and stay standing. Both are right at
different granularities. Montessori-as-a-system is Class C; refusal-of-illegal-
states is Class A. Port the mechanism, not the tradition.

---

## 5. The nulls, at full strength

AI cannot make a null result affordable. Eleven documented, all meta-analytic or
randomised:

| Finding | Effect |
|---|---|
| **Group-based mastery learning** on standardized achievement | **"essentially no evidence"**; positive only on experimenter-made measures |
| **Unassisted discovery learning** | **d = −0.38 [−0.44, −0.31]**, *favouring explicit instruction*, 580 comparisons |
| **Problem-based learning** | "tendency to a negative effect on student knowledge"; pooled **d_w = 0.13** with **Q ≈ 954** — uninterpretable heterogeneity |
| **Reciprocal teaching** | non-significant on standardized tests; non-significant for below-average students |
| **Montessori RCT** (preregistered, French public schools) | **null on maths, executive function and social skills**; reading only, d = 0.68 |
| **Lesson Study** (EEF) | **ES = 0.02 (−0.06 to 0.09), p = 0.65**, n = 6,437, 181 schools, **very high** evidence security; no dose–response; fidelity was good |
| **Singapore Math®** | after adding seven studies, **no studies meet WWC design standards; "no conclusions can be made"** |
| **Mathematics Mastery** | pooled +0.073, both individual trials' CIs cross zero |
| **Deliberate practice** | 18% of variance in sports, **1% among elite performers** |
| **Technology-mediated collaborative learning** | **+3 months against +5** for the in-person version |
| **Multi-agent debate** | does not reliably beat self-consistency; a single agent with strong prompts ≈ the best discussion method |

Three of these deserve a sentence each. The Lesson Study null is the most
uncomfortable finding in the section: very high security, good fidelity, 181
schools, and a flat zero — which is what a well-run trial of a beloved method
looks like when the method does not work at scale. The Singapore Math result
means that using the brand while the evidence base is empty is a vendor claim
restated as a finding, which this project's editorial standard forbids outright.
And **technology-mediated collaboration at +3 versus +5** is a measured price for
digitising a social mechanism — not a hypothesis, a number.

The correction already on this project's record belongs here too, because it is
the same species of error: Bloom's two-sigma claim did not replicate. Human
tutoring is **d = 0.79** in VanLehn's synthesis, and intelligent tutoring systems
were already at **0.76** before LLMs existed. An earlier version of this paragraph
omitted the figure that should be quoted alongside those, the pooled
randomised estimate: **0.288 SD across 96 RCTs**. Expert one-to-one is worth roughly
eight tenths of a standard deviation under favourable synthesis and **under three
tenths** when you pool the trials. Not two.

And a correction this survey must publish about its own work. The research
behind this section proposed a *pāṭha* protocol, permutation-based fidelity
checking derived from Vedic recitation's *krama*/*jaṭā*/*ghana* schemes, as a
concrete, falsifiable alternative to self-consistency sampling. It was
explicitly offered for benchmarking. It was benchmarked, and it was falsified.
The idea was good, the mechanism was clearly stated, and the measurement said no.
That is how this is supposed to work.

---

## 6. The exclusion ledger

This is the deepest thing the historical record has to say, and almost nobody
says it.

| Tradition | Who was excluded | Constitutive or incidental? |
|---|---|---|
| Vedic study / gurukula | śūdras and those outside varṇa; women, progressively | **Constitutive** — *upanayana* eligibility *is* the admissions rule |
| Nyāya / śāstric education | the same gate, plus Sanskrit literacy | Constitutive |
| The 64 *kalās* | the propertied urban elite | Constitutive |
| Yeshiva / chavruta | women — study "never forbidden, but discouraged"; in practice male | Near-constitutive; changing |
| Madrasa / *ḥifẓ* | heavily gendered access; large opportunity cost | Incidental to method, structural in practice |
| ***Keju*** (Chinese imperial examination) | **all women, for roughly 1,300 years, without exception**; poorer households by cost | **Constitutive** |
| Songlines | initiation status, gender, kin and country; secret-sacred material | **Constitutive, and still actively enforced — respect it** |
| Age-set systems | typically male; advancement capped by age regardless of merit | Constitutive |
| Griot / *jeli* | **hereditary and endogamous** — you cannot become one, or stop | Constitutive |

> **Almost every high-fidelity, low-ratio, high-intensity learning system in the
> historical record achieved its quality partly by rationing access.**

Small cohorts, long apprenticeships and lineage-based trust are cheap when you
have decided in advance that most of the population is ineligible. This reframes
the entire cost thesis. The traditional mechanisms are not expensive because they
are good; **they are good, and they were affordable because they were
exclusive.**

AI changes one variable, the marginal cost of attention, and that is the variable
the exclusions were rationing. Which yields the selection
rule for everything in this catalogue: **port the mechanisms whose quality did
not depend on the exclusion.**

The tradition that names the correct design commitment is a story rather than a
system. Ekalavya learned archery from a teacher who refused to admit him, by
building the teacher's image and practising before it, and surpassed the
teacher's own students. The pedagogical content of the story is that **the
admission gate was the only thing that had ever been scarce.** The design
consequence is a default of *yes*: no prerequisite locks, no grade-level gating
of content (only of framing), never "you're not ready" but "here is the shortest
path from where you are," and explicit design for the learner nobody would admit
— the adult with gaps, the disabled learner, the out-of-sequence child.

The limit ships with the feature. Ekalavya lost his thumb *after*
succeeding. Removing the teacher's veto does not remove the guild's, and any
product making this claim without a story about credential recognition is telling
half of it.

---

## 7. What is under-built and survives

Four mechanisms that pass the survival test, are implementable today, and almost
nobody has built.

A named, citable feedback taxonomy. Nyāya's *nigrahasthāna* enumerates
twenty-two grounds for defeat in argument. The list matters less than the
property: a fixed, published, learner-visible taxonomy makes feedback
learnable (the learner acquires the categories and self-diagnoses),
auditable (a wrong category assignment is visibly wrong, unlike a wrong
vibe), and symmetric (the learner can apply it back to the AI). Current
tutors give fluent, hedged, unnamed feedback, which is none of those things.

**Variation-theoretic example generation, gated by *shu–ha–ri*.** Enumerate a
concept's critical aspects; vary exactly one while holding the rest invariant;
present differences against a background of sameness. Adaptive systems today vary
*difficulty* and *quantity* — randomly generated problems vary many dimensions at
once and thereby make the critical aspect *harder* to discern. The gate is the
other half: shu, one canonical method enforced with deviation corrected;
ha, alternatives introduced deliberately; ri, the learner adapts and the
system shifts to critique. Current tutors are stuck permanently in *ha* —
maximally accommodating, always offering another way to look at it, including at
the stage where a beginner most needs to be told to do it exactly this way.

Precision-teaching rate measurement as telemetry. Pinpoint a behaviour, time
short trials, chart rate per minute, let the slope drive the decision. Thin
evidence base (11 studies, 170 participants), pure measurement labour, free for
software. Highest ratio of neglect to feasibility in the catalogue.

AI-brokered human pairing. For everything in Class C the correct role is
orchestrator, not participant: matching chavruta partners with compatible level
and incompatible blind spots, authoring ConcepTests, partitioning jigsaw groups
and detecting free-riding, guaranteeing every seminar participant arrives having
engaged the text. AI supplies the objections; it does not supply the partner.

---

## 8. What we port from the canon

- **Run the survival test before building anything.** Remove the other human and
  the objects; if what remains is not the mechanism, the correct role is
  orchestration.
- **Build PSI's spine first.** Prerequisite graph, 80–90% mastery bar, unlimited
  retests on *freshly generated* equivalent items, immediate certification, full
  records. Then add pacing pressure, because self-pacing is a documented
  failure mode.
- **Take DI's discipline and never claim its evidence.** Generated sequences are
  not validated sequences. Faultless communication, placement, high response rate
  and mastery gating transfer; four thousand effect estimates do not come along
  with them.
- **Never argue from cost where the constraint was permission.** DI lost to
  ideology; competency-based education is blocked by credit hours and
  accreditation; standards-based grading is blocked by transcripts.
- **Evaluate on assessments the system did not author.** Every effect size in
  this literature roughly halves when it moves from a researcher-made test to a
  standardized one.
- **Port only what did not depend on the exclusion**, and default to yes on
  admission.
- **Publish the corrections.** Bloom's two sigma did not replicate. Our own
  *pāṭha* protocol was falsified. Say so and move on.

Read as an engineering catalogue and not as a museum of things we can now
afford, the historical record is partially validated, unevenly evidenced, and
uncomfortable about who it let in. A small number of its mechanisms were only
ever gated by the price of attention. Those are the ones to build. The rest are
worth knowing so that we do not mistake a tradition for a finding.


## 32. The Market — nine bets, one graveyard, and the number that shrinks as you look at it

<sub>Source report: `research/raw/E1-E2-edtech-landscape-lessonorca.md, research/raw/E3-latest-sweep.md`</sub>

ASSISTments publishes its own evidence page. Read the studies in order of sample
size:

| Study | Design | n | Effect |
|---|---|---|---|
| Mendicino, Razzaq & Heffernan (2009) | small RCT | 28 students | **0.61** |
| Kehrer, Kelly & Heffernan (2013) | small RCT | 65 students | 0.37 |
| Maine (2012–2015) | RCT | 46 schools, 2,769 students | **0.22** |
| North Carolina (2018–2021), WestEd | RCT, delayed outcome | 63 schools, 5,991 students | **0.10** one year later |
| Gates Foundation / SRI | independent evaluation | not stated | **0.03** |

**0.61 → 0.22 → 0.10 → 0.03**, as the sample grows and the evaluator stops being
the vendor.

That gradient is the single most instructive object in the edtech market. The
company publishes it itself, on its own site, without spin. It is to their
enormous credit. It is also the number you should hold in your head every time a
product quotes you an effect size.

Note the last translation. ASSISTments' public headline is "60% more growth in math
scores", which is the **0.22** study rendered in percentage-of-a-year terms. A
0.22 SD effect is a genuinely good result in education. "60% more growth" sounds
like something else entirely. **The translation layer between effect sizes and
marketing copy is where most of this market's dishonesty lives, and it does not
require anyone to lie.**

---

## 1. Nine bets

A directory of companies is worthless six months after it is written. What survives
is the structure of the bets. Every product in this market has picked one primitive
to be its load-bearing wall: the thing that, if true, makes everything else follow.
Each primitive is a falsifiable hypothesis about how learning happens.

| Primitive | The bet | State of the evidence |
|---|---|---|
| **Content generation** | The bottleneck is materials | Every retrievable metric is a **teacher-time** metric |
| **Tutoring** | The bottleneck is one-to-one attention | Splits into answer-giving and withholding; only the pre-LLM generation has trials |
| **Assessment** | The bottleneck is grading cost | Works where the mechanism is clustering; fails where it is judgement |
| **Teacher tooling** | The highest leverage is not on the student at all | Best evidence-to-deployment ratio; least glamorous |
| **Language** | The bottleneck is practice hours with a patient interlocutor | The one cluster where "practice, not answers" is commercially natural |
| **Early literacy** | The bottleneck is an adult who will listen | The most defensible bet in the market |
| **STEM representation** | The bottleneck is symbolic abstraction | Strong lab support, almost no field-scale randomised evidence |
| **Credentialing** | The bottleneck is the signal, not the learning | Succeeds only when it displaces one specific gatekept test |
| **Infrastructure** | Whoever owns rostering and the LTI socket owns the market | Where the money is, and where the risk is |

Two clusters deserve their evidence stated in full.

**Tutoring's real numbers are pre-LLM.** Kulik & Fletcher (2016), 50 controlled
evaluations at **median 0.66 SD**, is the most-cited figure in the market and comes
with its own debunking attached: the improvement "depended to a great extent on
whether improvement was measured on locally developed or standardized tests," and
§1 puts test alignment at a factor of 2–3. Pane et al.'s Cognitive Tutor Algebra I
trial, matched-pair randomisation across seven states, is the best large-scale
evidence anyone has: **no effect in year one**, positive in year two, significant
for high schools and **not** for middle schools, at roughly eight percentile points.
The LLM generation inherited the marketing claim and none of the measurement.

**Early literacy is the most defensible bet in the market**, in mechanism terms
rather than enthusiasm terms. The AI does something a human demonstrably cannot
scale. It listens to twenty-five children read aloud at once. The output is oral
reading fluency, a measured behaviour and not a self-report. And the pedagogy
underneath, decoding practice with immediate corrective feedback, is among the
best-replicated results in education. If AI-in-education works anywhere, it works
here first. The headline claims still need their qualifiers read: one vendor's "68%
faster reading growth" is conditioned on students who used it "at dosage," which is
a selection effect unless dosage was randomised.

---

## 2. What the market measures instead of learning

Finding one: the evidence gradient runs opposite to the funding gradient. The
two products in this section with genuine independent randomised evidence
(ASSISTments, a nonprofit that is free to teachers, and Cognitive Tutor, a
forty-year-old curriculum publisher) report **0.03 to 0.22 SD**. The products with
the largest claims report no retrievable design, sample or comparison group. And the
best-funded entity in the sector, at a $4.8bn buyout, makes no learning claim at all.

**Finding two: "time saved" has quietly replaced "learning gained" as the industry's
success criterion.** Across the content-generation and teacher-tooling clusters it is
the only quantity anyone measures. That is not a criticism in itself; teacher time
is real and scarce. But it needs one distinction that no vendor in this survey makes:
**teacher time saved is a legitimate benefit; learner time saved is the documented
signature of harm.** The unguarded arm of the Bastani trial also saved the student
enormous time, and §2 carries what happened when the tool was taken away.

Finding three: mechanism claims are checkable and outcome claims usually are not.
"Guides rather than answers." "Listens as students read aloud." "Makes teaching
decisions in the moment." Each of those describes what the system *does*, and each is
verifiable by inspection. That makes them worth more than an unreproducible outcome
number — and §4 records the case that limits the principle, where a fully true
mechanism claim bought nothing because the mechanism only fired when a student first
recognised they needed help.

Finding four: a resolving DOI is not a result. Several products' "studies"
resolve only to AEA RCT registry identifiers with the prefix `10.1257/rct.`, for
example `10.1257/rct.13519`. Those are pre-registrations. They contain no results.
A DOI here means someone intends to run a trial. Treat the prefix as a red flag and
never as a citation.

And the case that shows the gradient inside a single company: Curipod holds the most
real evidence of any product in its batch and markets on the weakest number it owns.
Its homepage leads with district testimonials, which are pre/post state-test
comparisons with no control group, no sample size and no statistical test, one of
them spanning **two
teachers. Its genuine study is a randomised trial with n = 142** at
**d = 0.301–0.800** — in *university nursing students*, against a control of
"conventional lectures supplemented with PowerPoint presentations and textbooks," on
survey constructs instead of achievement tests. It cannot support the K-12 state-test
claim on the homepage, and it is a category error to let it. **A company can hold
genuine evidence and still market on testimonials, because the genuine evidence is
narrower and less flattering.**

---

## 3. The graveyard, and its single cause of death

Edtech's failure record is the most informative dataset it has, and unlike its
success literature it is not vendor-controlled.

One Laptop Per Child has a randomised verdict. Cristia et al., **319 rural
Peruvian primary schools**, 15 months: computers per student rose from **0.12 to
1.18** and use rose substantially at school and at home. "No evidence is found of
effects on enrollment and test scores in Math and Language." The ten-year follow-up
across 531 schools found no significant effects on academic performance, completion,
or university enrolment. Delivery succeeded completely. The theory of change was
wrong.

inBloom was a $100 million student-data warehouse. Every district and state
withdrew after parent protests and it closed in April 2014. The technology worked;
every customer left. §12 and §28 carry the custody lesson.

Knewton raised roughly **$157M disclosed** across seven rounds against a claim that
was never stated in a form that could fail: "sophisticated, real-time analysis of
reams of student performance data." Its assets sold to Wiley for **under $17
million** in 2019. Roughly 90% capital destruction. §12 establishes the deeper
problem independently: knowledge-tracing accuracy had already plateaued. Knewton was
selling precision from a region of the design space where precision had run out.

AltSchool raised $133M and built a network of schools in order to build software.
The schools were the R&D cost centre for a product that did not exist yet; when the
software pivot came, the schools closed. The schools were the thing families had
actually bought. The surviving artefact, a parent progress portal, is now a
table-stakes feature.
Right about the feature, wrong about the business.

**2U** bought edX from the Harvard/MIT nonprofit for **$800M**, never made an annual
profit, and filed Chapter 11 on 25 July 2024. Its revenue-share structure gave it one
lever, student *volume*, and no lever at all on student *outcome*.

Byju's reached a **$22bn valuation** and 150 million claimed registered users. Its
founder said publicly in October 2024 that "the company is worth zero." Its reported
85% retention rate was never independently verified and this survey does not repeat
it.

Six deaths, six different proximate causes, one structure:

> **Each one succeeded completely at the thing it measured, and the thing it measured
> was not learning.**

Laptops delivered. Data integrated. Model sophistication. Iteration velocity.
Enrolment volume. Registered users. The proxy is always something the organisation
controls; learning is always something it does not. This is Goodhart's law with
children in the loop, and edtech has an aggravating feature: **the delay between the
proxy and the truth is measured in school years, so a company can be dead right on
its own metrics for a decade.**

The operational test that falls out of it is the one this project should be held to
as well:

> **Name the metric that would tell you your product is not working, and state how
> long you would have to wait to see it.**

Every company above would have failed that test.

---

## 4. Two failures that are still running

The graveyard is retrospective. Two live failures matter more.

A core claim was falsified after sale. Turnitin shipped AI-detection in early
2023. Weber-Wulff et al. (2023, *International Journal for Educational Integrity*)
tested twelve public tools plus two commercial systems in wide academic use for
accuracy, error type, and robustness to machine translation and obfuscation. The
tools are not reliable discriminators. Schools subsequently disabled the feature;
students alleged false accusations, including cases involving grammar-correction
software those schools recommend. A vendor-stated false-positive rate of about 1%,
against tens of millions of submissions, is a large number of accused innocents.

And consolidation concentrated the blast radius. In late April 2026 Canvas LMS
suffered a security breach that *404 Media* described as the largest educational
security breach on record: **3.65 terabytes, approximately 275 million records,
8,809 universities and education institutions.** By 8 May, seven federal lawsuits had
been filed, one naming the private-equity owner as co-defendant.

Three consequences the rest of this survey has to carry. The same logic that made
Canvas a good $4.8bn asset, one integrated platform with near-universal adoption,
made 8,809 institutions a single point of failure. **Every "we don't train on student
data" promise in this market is a promise about *use*, not about *custody*.** A
vendor can honour it perfectly and still lose the data. And therefore data
minimisation is a security control and not a compliance chore: the most effective
mitigation available to any product here is to not hold the record at all. That is
exactly the pressure the inBloom failure applied twelve years earlier, and the
market un-learned it.

---

## 5. One deployed case, and what it got right by accident

LessonOrca is this project owner's own product. It is admitted here as **one
deployed, instrumented case study among several** and not as evidence that anything
works. Its scale is three tutoring centres, 25 tutors, 100 students. Its marketing
copy is `VENDOR` and is not restated as a finding. Its operating economics are not
discussed.

What is interesting is a set of design decisions arrived at from customer discovery
and not from citation, which converge with the evidence in this survey.

Withholding is classified as a safety property, not a feature. "Socratic method
only. Guides students to answers, never gives them" sits on the page under *safety
guardrails*. That is the correct taxonomy: the trial evidence says unfettered
answering is the harm condition, so answer-withholding belongs with the guardrails
and not with the features.

The architecture puts the AI behind the human. The positioning — "AI will not
replace tutors, but it will redefine how they work" — is structurally the Tutor
CoPilot configuration, which is the one AI-tutoring architecture with a
live-classroom randomised trial behind it (§3, §20). The wedge identified from
interviewing tutors was continuity and never comprehension: nobody remembers what
happened last Wednesday. That is the correct read of the literature, reached without
reading it.

Oversight is total, never sampled, with human review gates on every artefact
that leaves the system — profiles reviewed before sharing, parent emails reviewed
before sending — and synthetic-origin labelling at the point of consumption. The
same three commitments appear independently at SchoolAI and MagicSchool: **adult
visibility into every AI interaction, explicit labelling of synthetic content, and
never posing as human.** Three companies converged on them without coordinating, and
they are stronger than anything in current regulation. That convergence is the
candidate norm this section contributes.

### The null, and it is our own

There is no instrumentation of the pedagogical claim. Not one event in the product's
analytics describes a tutoring session, a student turn, an AI question, a refusal to
answer, a profile update, or a parent opening a transcript. **The product in this
survey most explicitly designed around a falsifiable pedagogical claim has not
instrumented the claim.** It measures acquisition precisely and pedagogy not at all.

That is the §26.3 pathology — measuring what the organisation controls — appearing in
the survey author's own work. It is reported and not omitted because the survey's
credibility depends on applying its own test to itself first.

Three further criticisms follow from the same evidence base, and they are not
softened. The refusal is unverified: no transcript audit, no red-team result, no
refusal-failure rate. "Never gives answers directly" is currently an assertion about
a prompt. "Socratic only" is stronger than the evidence supports: §25's archetype
work is explicit that for reasoning and abstraction gaps, discovery learning is
actively harmful and explicit instruction is required. The defensible version is
narrower — *never answer the question the student was assigned; may directly instruct
on the prerequisite they lack.* And the substitute is unmodelled: a student
blocked by a Socratic tutor at eleven at night has a general-purpose chatbot in the
next tab. One vendor refusing does not eliminate the harm condition. It relocates it.
A refusal engine with no theory of the substitute is measuring its own compliance
and not the student's behaviour.

One more datum from the same instance generalises. Its privacy and terms pages were
opened by a vanishingly small fraction of visitors. **Consent architectures that
route through policy pages reach essentially nobody**, which is the argument for
in-product, in-context disclosure over the kind the law contemplates — and it is why
the three convergent norms above are worth more than a longer policy.

---

## 6. How to read a claim from this market

- **Quote the gradient, not the number.** 0.61 → 0.22 → 0.10 → 0.03 as n rises and
  the evaluator becomes independent. Any effect size from a vendor sits somewhere on
  that curve, and usually at the left end.
- **Distinguish teacher time from learner time.** One is a benefit. The other is the
  documented signature of the harm condition.
- **Prefer mechanism claims and audit them.** A mechanism claim that survives
  adversarial inspection is worth more than an outcome claim nobody can replicate —
  provided somebody actually inspects it.
- **Treat `10.1257/rct.` as a red flag.** It is an intention and not a finding.
- **Name the disconfirming metric and its latency**, before shipping. Every company
  in the graveyard would have failed that test, and so, today, would ours.
- **Instrument the pedagogy before marketing it.** Our own product does not, and that
  is the section's principal negative result.
- **Minimise custody.** 275 million records, 8,809 institutions. The strongest privacy
  control is not holding the record.

The market does not, on the whole, lie. It measures the thing it can move, publishes
the number that survives translation into marketing, and waits out the school years
it would take for anyone to notice the difference. Better claims will not fix that.
Naming, in advance, the observation that would prove you wrong might.


## 33. Inference Is 0.43% of Delivery — and human judgement is the scarce input

<sub>Source report: `research/raw/M1-market-and-model.md`</sub>

A survey that specifies a system and never asks who pays for it has described a
prototype. This section is the audit of the commercial half. It is included because
three of its findings **contradict things stated earlier in this document**, which is
the strongest argument for having done it.

Every figure here was traced to a primary source. Where a number could not be traced,
it is reported as untraceable instead of cited, and that happened more often than any
other section in this survey.

---

## 1. The number that retires a whole category of argument

> **Inference is 0.43% of the delivered cost of a human-supervised tutoring session.**

Two independent measurements converge on it. A published cost model puts tokens at
£0.0037 of a £0.861 session. A deployed programme's measured API bill was
$1,419.66 for 429 tutors over two months, or $19.86 per tutor per year, against a
tutor working 200 hours at the US mean tutor wage of $23.10/hour. Same figure, from
two directions.

This survey has argued from the first section that cost is not the interesting
constraint. That framing was right for the wrong reason. We treated inference cost as
*falling toward irrelevance*. It is already irrelevant — not because it fell, but
because **it was never the denominator.** If inference went to zero tomorrow, a
human-in-the-loop gross margin would improve by less than half a point.

The consequence is sharp and it disqualifies a common pitch: *"our costs fall as
models get cheaper"* is true, and worth 0.43%. The entire margin question is the
**leverage ratio**: learner-hours supervised per paid tutor-hour.

---

## 2. The leverage has not been measured, including by us

This is a correction to our own §10, where the Eedi trial's draft-acceptance figure
was cited in a way that implied a demonstrated efficiency gain.

**The acceptance rate verifies exactly**: 2,691 of 3,617 drafts accepted unedited, or
74.4%, with zero harmful messages and five factual errors. That number is solid, and
the moat argument in this survey rests on it.

The efficiency reading is not solid. The authors state that their design

> *"precludes a rigorous measurement of throughput or efficiency."*

The published throughput gain (concurrency 2.3 → 3.5, netting −13.6% cost per
session) comes from a six-tutor role-play simulation in an appendix, and the
labour rate underpinning the saving is cited to **a tutoring marketplace's blog
post**.

So: 74.4% is a measured *signal stream*, which is all the argument needs. It is not a
measured productivity gain, and this document should not have implied otherwise.

---

## 3. The only audited comparable went the wrong way

A listed tutoring company rebuilt, in its own filing's words, *"on entirely new,
AI-native codebases."* In that fiscal year:

| | |
|---|---|
| Gross margin | **67.5% → 58.0%** (62.3% excluding a write-off) |
| Expert costs | **up $5.2M** |
| Revenue | **down $11.2M** |

The following quarter recovered to 66.2%, on price rises and expert incentives and
not on AI. The 10-K states plainly:

> *"There can be no assurance that our investments in AI will be beneficial to our
> business."*

That is the single audited data point on an AI-native rebuild of exactly this business
model, and it is negative. It does not falsify the thesis. It does mean **leverage
must be demonstrated rather than assumed**, and that a company claiming it should be
asked to produce the ratio monthly.

---

## 4. Two market facts that relocate the opportunity

The funding wave never arrived where everyone models it. Summed from the education
department's own state-level obligation data, the reported *tutoring* line of the
pandemic relief appropriation is **$994.7 million, or 0.52% of $189.5 billion**. The
category most often cited as the demand driver received half a percent of it.

And the numbers in circulation mostly have no source. Six of six analyst houses
fail traceability on the tutoring market size: two dead links, one report not shown
to exist, one figure internally inconsistent by three orders of magnitude. For scale
on how far the reported totals drift: **Korea alone (₩27.5 trillion, and falling) is
roughly 20% of the claimed global market.**

The most striking absence: **the United States has not measured per-pupil
special-education spending since 1999–2000.** No federal survey currently produces it.
A document that argued in §11 for designing at the margin first should say plainly
that the sector it points at is the least financially measured in education.

---

## 5. China is a policy risk and not a market

Retrieved in full from the Ministry of Education: the July 2021 *double reduction*
order states that no new approvals will be issued for core-subject tutoring
institutions and that existing ones re-register as non-profits. One listed
operator's revenue fell 62% in twelve months, per its filing.

And the compounding finding: **no official Chinese statistic on tutoring market size
exists, before or after 2021.** Every "$100bn+ market" figure descends from vendor
reports rather than a national statistics office, which means **the destroyed value
is itself unmeasurable.** That should be sobering about the downside of this category
and not only its upside.

---

## 6. The three questions, and the answers that disqualify

The section's deliverable. These are aimed at any AI-tutoring company, including one
built from this document.

**1 · "Show me learner-hours delivered ÷ paid tutor-hours, monthly, for 24 months."**
*Disqualifying:* the company cannot produce it, or it is flat while headcount grows.
That means the AI is decorative and the buyer is underwriting a staffing business at a
software multiple.

**2 · "What is your delayed, unannounced, novel-item transfer result, with n, and who
held the item bank?"**
*Disqualifying:* the only outcome evidence is in-product mastery or engagement. One
deployment moved its exit ticket +4pp and was null on the state test. That
dissociation between the proxy and the outcome is the most reproducible finding
in this literature.

**3 · "Have you ever run an arm against plain ChatGPT?"**
*Disqualifying:* never tried, or tried and buried it. A controlled trial (n = 371)
found scaffolded generative AI no better than plain ChatGPT on domain knowledge.
If the pedagogy has never beaten the free substitute customers already have, the moat
is a prompt.

---

## 7. What a buyer should be able to check

- **Never argue from falling inference cost.** It is 0.43% of delivery. The claim is
  worth less than a rounding error and signals that the speaker has not done the
  arithmetic.
- **Report the leverage ratio monthly, from month one**, because it is the only number
  that distinguishes a software business from a staffing business here.
- **Cite the audited counter-comparable** whenever claiming AI improves tutoring
  margins. Omitting the one negative data point because it is inconvenient is the
  failure this survey exists to name.
- **Treat 74.4% as a signal stream, never as productivity.** The authors said so
  themselves.
- **Do not quote a market size without its primary source.** Six of six fail. If the
  figure cannot be traced to a statistics office or a filing, say it is untraceable.
- **State that special-education spend has been unmeasured since 1999–2000** wherever
  this document argues for building at the margin. The moral case is strong; the
  financial case is undocumented, and conflating them would be dishonest.

Our own framing changed here. The cost of intelligence was never the constraint on
this business, and it is not becoming one. What is scarce is the human judgement that
currently has to verify it — a conclusion §36 reached from the technical side, arrived
at independently from a profit-and-loss account.


## 34. The Two-Hour School — two hours buys the schedule, and does not buy the attainment

<sub>Source report: `research/raw/N3-two-hour-school.md`</sub>

A school in Texas teaches academics for about two hours a day and reports students at
top percentiles. It is the closest thing to a live test of this survey's compression
argument, and it deserves a careful reading rather than either enthusiasm or a sneer.

Two claims are being made and they are sold as one. **One holds. The other is not
established**, and the arithmetic that produces it is checkable.

---

## 1. The two-hour claim holds, and it vindicates §6 at the low end

Section6 argues that a school week is mostly overhead: 9 nominal hours inside 112,
and the engagement cascade loses about 65% of the 9, so the same nominal day yields
4 minutes or 52 minutes of productive learning depending on allocation,
engagement and success rate.

Run that against two hours of high-engagement work held at 70–95% accuracy, and the
result is **roughly parity in academic learning time with a median six-hour day.**

That is a real removal of overhead and it is what this survey predicted, at the low
end of §6's stated range, which is where a real-world implementation ought to land.

Which is why the two-hour figure cannot explain the attainment claim. If two hours
buys parity, it buys parity. Something else has to account for students scoring above
their peers, and the candidates are targeting and selection. The clock is not one of
them.

That distinction is the whole section. The compression is real; it is not the
mechanism being advertised.

---

## 2. The attainment claim rests on a denominator

The operator's white paper contains one worked example of its "2×" figure. Its
denominator is the RIT gap between adjacent grades at a fixed percentile: how far
apart grade 5 and grade 6 sit on the scale, at the same percentile.

That is not a growth norm. The published growth norm for the same cell is 9.61 RIT
against the 4 the paper uses.

The consequences follow arithmetically:

- The 8 points the paper credits to a student sits at about the **40th conditional
  growth percentile**, *below* median growth for that starting point.
- Fed a nationally average student, the same metric returns **1.2×–2.4× in maths,
  1.0×–1.7× in reading, and ∞ at grade 8.**

The metric produces a multiple greater than one for an average student. **That is a
property of the denominator and not of the instruction.**

Two further mismatches compound it. The frequently quoted **99th *school* percentile
corresponds to roughly the 90th *student* percentile** in maths and 84th–87th in
reading. And the norms are built on US public-school students, a comparison a
private school will win on composition alone.

None of this shows the school does not work. It shows **the published number does not
demonstrate that it does**, and that a reader can check this in an afternoon from two
public PDFs.

---

## 3. The regulatory record is the most informative document

Marketing is `VENDOR`. A charter application is a filing with consequences, and it says
something different.

In its Pennsylvania application the same operator projected ranking **in the top half
of Pennsylvania schools, and not the top percentile. Four of five states refused**,
with the Pennsylvania department finding *"deficiencies in all five of the required
criteria."*

And in the regulated version of the model, the "guides" become **certificated teachers
at a 1:20 ratio.** The staffing structure that survives regulatory scrutiny is a
conventional one.

Three more facts a diligent reader should have:

- The adaptive software vendor **deactivated the school's account in July 2025 for
  *"violating our terms of service."*** The stack that produced the published results
  is therefore not the current stack.
- A state education department declined to recognise the $65,000-tuition Manhattan
  campus as a school.
- The group files **no Form 990, no Form D, nothing.** There is no audited financial
  or enrolment record to check anything against.

And where an outside reader finally obtained a denominator underneath a published
multiplier, it was **n = 5.**

---

## 4. The precedent that matters most

Nine "school reinvented" precedents are on the record, among them AltSchool, Summit
Learning, Teach to One, Rocketship, Carpe Diem and Khan Lab School. One is worth
isolating because its evidence pattern is exactly the one under examination here.

Teach to One has two evaluations. The independent one, on state tests, is
null. The positive one is MAP-growth-based.

Same programme. Same period. Different instrument, opposite conclusion.

That is the shape to watch for. **A growth-metric result and a state-test result are
not two measurements of one thing**. When only the first is offered, the reader
should ask for the second rather than treat its absence as neutral.

*(This survey's own brief for this section cited a state-test study of Teach to One
that does not exist. The agent checked and corrected it. Recorded because the error was
ours.)*

---

## 5. What would settle it

The bar is the same one this survey applies to everyone, including itself:

- **An externally administered assessment**, and not one the operator gives and scores.
- **A comparison group that is a real alternative**, ideally a matched private school,
  since selection is the live confound and cannot be ruled out without one.
- **A delayed, unassisted, novel-item outcome**, which is the only trustworthy signal
  in this entire document.
- **A denominator published with every multiplier.** Most of the arithmetic problems
  above disappear the moment the denominator is stated.

And one caveat that applies to the whole category: **percentile rank is zero-sum by
construction.** A model that lifts everyone cannot lift everyone's rank. If the claim
is capability, say capability; if the claim is rank, it is positional and does not
survive scale.

---

## 6. How to read a claim like this one

- **Separate the compression claim from the attainment claim.** The first is
  supported and modest; the second is unestablished. They are routinely sold as one
  sentence.
- **Check the denominator before the multiplier.** A metric that returns 2× for an
  average student is measuring its own construction.
- **Read the filing, not the site.** The regulated version of a model is the version
  its operator will defend under consequence.
- **Ask which instrument.** Growth-metric positive with state-test null has happened
  before, in this exact category.
- **Report our own errors in the brief**, and not only in the findings.

A two-hour academic day is a real and defensible removal of overhead. It is not
evidence of extraordinary learning. Those are two different claims, and this survey's
own argument only supports the first one.


## 35. Prior Art — thirty-five builds, 128 notebooks, zero exercises

<sub>Source report: `research/raw/D2-portfolio-case-studies.md`</sub>

One hundred and twenty-eight notebooks. Zero exercises.

That is not an impression. It is a programmatic scan of every markdown cell in three
sampled zero-to-hero notebooks, counting the strings a practice item would have to
contain:

| String | logreg | tabular_sota | stats_sota |
|---|---|---|---|
| "Exercise" | **0** | **0** | **0** |
| "Your Turn" | **0** | **0** | **0** |
| "Try it" | **0** | **0** | **0** |
| "Solution" | **0** | **0** | **0** |
| "Quiz" | **0** | **0** | **0** |
| "🧠 Intuition" | 12 | 13 | 5 |
| "✅ " | 46 | 14 | 36 |

The corpus is explanation, demonstration, and verification-by-the-author. The
learner reads and runs. **The learner is never asked to produce anything.** And the
method's own stated success criterion says so out loud: *"a student can narrate
every cell in a 1-hour video."*

Narrating is not retrieving. §1 and §19 establish what that distinction costs: the
two largest replicated effects in learning science are retrieval practice and
distributed practice, and this corpus contains neither. It is optimised, with real
craft and enormous discipline, for the felt sense of understanding.

---

## 1. What this section is, and what it may not be

This survey has a standing rule about this material and it is worth stating before
anything else.

The portfolio examined here belongs to this project's owner: roughly 35 active
repositories, nine live deployed apps and 128 notebooks, all inspected first-hand
by downloading the production JavaScript bundles and reading the shipped system
prompts. It arrives **last**, as validation, and it is **never** the seed
for what should be built.

The reason is measured and not stylistic. Research within this project found that
seeding a generator with examples produced **zero diversity gain** (p = .95, .89
and .49 across three comparisons) while anchoring moved **57–77% of
correct answers to wrong ones**. A portfolio shown to a generator before the
literature does not expand the design space. It collapses it, and it does so most
strongly on the items the generator would otherwise have got right.

So the question here is not "what should we build." It is the narrower and more
interesting one: **when a capable practitioner is handed frontier models and no
constraints, what actually gets built, and what reliably does not?**

---

## 2. What gets built: generation, six times over

Six of the nine deployed apps are the same machine with different prompts: a
single-page React app, the model called directly from the browser, structured JSON
out through a response schema, live bidirectional audio over a WebSocket, search and
URL grounding, text-to-speech, embeddings.

What that machine demonstrably does, in production, today:

- **Bidirectional live voice with a persona**, in six shipped apps, with barge-in
  handled through `interrupted` / `turnComplete` events, a hand-rolled client audio
  pipeline down to 16 kHz Int16 PCM, and playback scheduled at 24 kHz against a
  running cursor to avoid gaps.
- **Live bilingual transcripts**, with both input and output transcription enabled.
- **Mid-session language switching**, injected into the live stream as an
  instruction.
- **Tool calls that drive the interface mid-sentence.** The model narrates by voice
  while mutating application state.
- **Curriculum synthesis on demand**: any topic to a schema-constrained ten-chapter
  path in one call, conditioned on grade, location, culture, interests, dialect and
  stated goal.

The technical substrate §29 describes as newly available is not a research problem
for this practitioner. It is shipped, six times over. That is the first thing
the portfolio reveals that the literature does not: the field's discourse treats
multimodal tutoring as a frontier, and at the level of plumbing it is a solved
weekend.

Three design patterns recur and are worth naming because they were arrived at
independently.

Make generation legible. Every app narrates the model's work during a 10–40
second wait: "Architecting Learning Path…", "Clustering 50 Mastery Paths…",
"Validating Narrative Integrity…". Nothing hides behind a spinner. It is
genuinely good interface design for a latency that is not going away.

The schema is the pedagogical commitment. The flagship app's curriculum
generator enforces a JSON schema with `globalGifts[]`, provocation questions, a
peer collaborative challenge, showcase-based assessment, and a journaling prompt,
recognisably Froebel plus Reggio Emilia plus Socratic method, encoded as a type
rather than as an aspiration. A schema is a pedagogy you cannot quietly drop.

Personas are swapped at the system-instruction layer and nowhere else. The same
codebase ships as a Spanish course, a Telugu course, a Bhagavad Gita app, a Sanatana
Dharma app and an Ayurveda app, differing in one string.

---

## 3. What does not get built

### 3.1 The mode switch with no policy

The flagship app ships three distinct live-session personas as separate system
instructions: Lecturer ("start with a 2–3 minute comprehensive discourse…"),
Socratic ("answer questions by asking leading questions"), and Examiner
("conduct an interactive oral quiz… evaluate the student's response and provide
feedback").

Mode-switching between lecture, dialogue and assessment is already implemented.
What is missing is any policy for when to switch. The learner picks. No mastery
estimate drives the choice.

That is §11's central argument, rediscovered from the other end by someone building
rather than reading. The hard part was never generating the three modes. It was
knowing which one fires, and that requires a measurement nobody took.

### 3.2 The signal that is emitted and discarded

The language portals declare function calls as their assessment channel during live
voice sessions:

```
provide_feedback(score, feedback, suggestion)   → "Accuracy score from 1 to 10."
mark_word_practiced(word)                       → "Mark a vocabulary word as
                                                   successfully practiced and mastered."
```

This is **the only place in the entire portfolio where the model emits structured
evidence of learner state.** `mark_word_practiced` is a one-bit mastery signal and
it is exactly the right primitive.

It is written to nothing. There is no persistence layer in those bundles. The
mastery signal is discarded at page reload.

And the sharpest version of the same gap: cross-session memory exists in this
portfolio. A meditation app injects *"CONTEXT FROM PREVIOUS SESSIONS"* into every
live session from a Firestore-backed store, alongside affect-conditioned pacing that
slows down when the user sounds anxious. A separate research-agent codebase solves
the memoryless-collaborator problem again, with an explicit thesis that *"the
repository is the memory."*

The same author solved cross-session memory twice, once for meditation and once for
a machine-learning agent, and shipped it in neither of the tutors.

§12 argues that persistent learner state is the load-bearing component of an AI-native
learning system. This is what its absence looks like in built artefacts, from
someone who demonstrably knew how to build it.

### 3.3 Assessment lives in a different repository

The one instrument in the corpus with real practice structure is **one notebook out
of 128**: an interview gauntlet with 29 trap markers and 31 follow-ups, structured
*question → intuition → rigorous answer → code check → follow-ups*. The
exam-prep notebook contains 36 problems in a strict four-beat format, mapped to
textbook exercises and cross-checked against the official solutions manual, and
the solution sits immediately below every problem. No hidden answer, no attempt
gate, no self-grading.

Meanwhile a companion repository carries graded rubrics and reflection prompts for
all 197 lectures of a full curriculum. **The assessment layer was written. It was
never wired to an artefact.**

---

## 4. The finding that generalises: enforcement beats intention

This is the most transferable result in the portfolio, and it comes from comparing
two bodies of work by the same author under the same standards.

The teaching corpus states its quality rules. Sixteen non-negotiables, including
some that this survey would endorse verbatim: *"no jargon before it's grounded"*,
with a term-grounding verifier that flags every term whose first use precedes its
plain-language explanation; *"no formula verbatim — a formula stated with no
build-up is a defect"*; *"prove it AND verify it"*, every derivation shown in LaTeX
and confirmed numerically.

The research corpus compiles its rules into regexes, word floors, SHA-256
fingerprints, and independent audit agents that exit non-zero with no bypass flag.

Then look at what happened to each.

Where the rule is a norm, it drifted. Hiding code cells is declared "non-negotiable"
by the governing method and is set on no code cell in any notebook sampled,
including the ones the rule specifically governs. Two deployed apps ship the wrong
page title — a Spanish course and a Bhagavad Gita app both serve
`<title>Sanatana Dharma AI Portal</title>`. Five apps share a byte-identical
stylesheet, so a Spanish learning portal ships with saffron, gold and mandala
styling. One repository disagrees with itself about which model it uses across the
README, the agent instructions, and two source files.

And the drift reached production. **Six of seven bundles ship a literal placeholder
API key string**, one of them at six call sites covering the lesson generator, the
live teacher, TTS, speech and the writing lab — which means that app's **core lesson
generation is non-functional in production**. The parent app had the fix. The fork
did not receive it.

Where the rule is a gate, it held: **112/112 forensic audit passes**, and 82 of 112
tasks beating a published benchmark, in the corpus whose rules exit non-zero.

> **A survey advocating AI-generated curricula must advocate gates, not guidelines.**

That is the sentence this section contributes, and a natural experiment earned it.

---

## 5. The nulls

The specified constraint set was abandoned wholesale. The flagship app's own
product requirements document targets rural learners on low-end Android devices,
on-device inference offline the great majority of the time, a small initial download,
solar-friendly operation, and a hundred low-resource languages. What shipped is an
online-only single-page web app whose voice path requires a persistent WebSocket and
whose audio capture uses a deprecated main-thread API, in *every* app in the
portfolio, that will glitch on precisely the target device. The design research
document runs to 78.5 KB. **Every hard constraint was dropped and the easy 20% was
built.** That gap is more useful to this survey than a success story would be, and it
is the single most honest datum in the report.

**Local generative video is not viable as a tutor avatar, and the code says so
itself.** The locally written streaming demo carries this note in its own source:

> *"HONESTY: this is NOT a real-time interactive avatar. It is a low-FPS (~1.8 FPS
> on this GB10, arm64, no flash-attn/TensorRT) video-to-video style transfer
> stream."*

That is a model of calibrated claiming, and the verdict follows from it:
asynchronous generated lesson media, streamed progressively, is available now; a
live generated avatar is not.

Nothing was evaluated. No A/B test, no learning-outcome measurement, no user
study, no telemetry beyond a token counter, across nine deployed apps and 128
notebooks. An analytics project exists in the same environment and is unused for
this purpose. §32 records the same pathology in the same owner's commercial product,
independently.

Grounding is applied uniformly where it should be applied selectively. Web-search
grounding is switched on identically for logistic regression and for Ayurvedic health
guidance delivered in the voice of a deity. No source allowlist, no provenance
display, no medical disclaimer in the extracted strings. One app in the set asserts
uncited clinical statistics as fact — *"diagnostic simulation benchmarks outperform
junior residents in 8/10 categories"* — with no citation mechanism anywhere in the
bundle. §23 argues that correctness must live in a verifier and not in the
generator; this is what the alternative ships as. **The same portfolio contains a
codified "citation rigor" discipline. It is not applied to the consumer apps.**

---

## 6. The objection

*If the portfolio's gaps are the same gaps the literature already identified, what
did reading it add?*

Three things the literature does not supply.

A measured asymmetry in agentic content production. Independent artefacts
parallelise freely — "the 5 above were built by 5 concurrent agents." Enhancement
passes on a *single* artefact are constrained to at most two agents on
non-overlapping regions, with the orchestrator performing the inserts sequentially,
because two agents editing one notebook corrupts it. That is an operational finding
you only get by doing it, and it governs how any of this survey's proposals would
actually be produced.

A working closed loop over curriculum coverage. A programmatic keyword audit of
every notebook against every subsection of the reference textbook produced a
pass/warn/fail verdict per chapter, found a real gap (a named list of clustering
algorithms entirely missing), generated an action item, and the gap-fill notebook was
then built. **Audit → gap → targeted build → re-audit is the one place in the whole
portfolio where an automated signal changed the curriculum**, and it is a template
anyone can copy.

A typed contract for what an AI tutor should expose. One repository enumerates
32 features as a typed interface — onboarding, streaming chat, levelled hints, mode
switching, image generation, speech in and out, multi-agent classroom and debate,
whiteboard construction, learner-model read and write, progress and achievements,
group mode — with a mock implementation proving the shape is coherent. The deployed
app implements roughly eight of the thirty-two. A specification written before
the implementation, with the implementation gap visible in the same repository, is a
more useful artefact than either half alone.

---

## 7. What thirty-five builds oblige us to do

- **The portfolio is evidence, never a seed.** Zero measured diversity gain from
  example-seeding; 57–77% correct→wrong movement under anchoring. It arrives after
  the literature, or it does not arrive.
- **Generation is not the bottleneck.** Six shipped live multimodal tutors say so.
  State is the bottleneck: knowing what the learner knows, keeping it, acting on it.
  Every gap in this portfolio reduces to that one.
- **Ship gates, not guidelines.** Where rules were norms they drifted into production
  breakage; where rules were executable and exited non-zero, they held at 112/112.
- **A schema is a pedagogy that cannot be quietly dropped.** Prefer encoding a
  commitment as a type over stating it in a prompt.
- **Emit the learner-state signal into a store, not into the void.**
  `mark_word_practiced` is the right primitive and it was written to nothing.
- **Ground selectively, and display provenance.** Uniform web grounding across a
  maths lesson and a health claim is not a grounding strategy.
- **Instrument before you narrate.** Nine apps, 128 notebooks, zero outcome
  measurements — and the same absence appears independently in §32.
- **Publish the gap between the requirements document and the deployment.** Ours is
  large, it is in this section, and stating it is the only thing that makes the rest
  of the section credible.

The portfolio's most valuable property is that it was built by someone who knew the
right answers. The rules were written down. The verifier was coded. The memory layer
was shipped — for meditation. The assessment rubrics exist — in another repository.
Every component of the system this survey describes is present somewhere in these
thirty-five repositories, and none of them are wired together.

That is the finding. Not that builders do not know what to build, but that under
no external gate, the parts that get finished are the parts that demo — and the parts
that measure whether anyone learned are the parts that are always about to be built
next.


## 36. Motivation — wanting to continue

<sub>Source report: `research/raw/F6-motivation-persistence.md`</sub>

Here is the cheapest useful test in this survey. Take any metric you are thinking of
putting in an objective function. Now simulate an agent that maximises it **while
learning nothing**: the cheapest possible action sequence that satisfies the
measurement. If it scores well, the metric is invalid as a learning objective.

Call it the **Null-Learner Test**. Run it:

| Metric | Null learner | Verdict |
|---|---|---|
| Daily active users | Opens the app, taps the easiest lesson | **Maxes it. Invalid** |
| Streak length | Same, once a day | **Maxes it. Invalid** |
| XP | Farms the cheapest points-per-minute activity | **Maxes it. Invalid** |
| Time on app | Leaves it open | **Maxes it. Invalid** (and time-on-task estimation is independently fragile enough to invalidate learning-analytics findings built on it) |
| Session count, notification-response rate, thumbs-up rate | Trivially | **Invalid** |
| **Delayed, unannounced, novel-item transfer assessment** | Cannot be maxed without learning | **Valid** |

Every metric the industry ships fails. That is the whole argument in one table, and
this section carries the test throughout, because motivation is the topic where
otherwise-careful people start reasoning in engagement units without noticing.

---

## 1. Two of the three needs are no longer rationed

Self-determination theory posits three needs whose satisfaction produces autonomous
motivation: **autonomy, competence, relatedness.** Two of them were previously
rationed by teacher time, and are now not.

**Autonomy. AI is structurally the best autonomy-support technology ever built.**
Choice enhances intrinsic motivation, effort, task performance and perceived
competence across 41 studies. A generative system can offer choice over topic,
sequence, pace, difficulty, representation, example domain, and *what the learner is
learning it for*. No prior educational technology could offer real choice over the
**content of the explanation** — only over the order of fixed assets. This is also the
need conventional schooling most systematically violates.

> *Guardrail, in the same breath:* autonomy in SDT is not "many options"; it is
> volition and self-endorsement of one's own action. A system that generates 40 paths,
> selects which 3 to display, and orders them by predicted engagement is supplying
> choice architecture masquerading as volition.

Competence. AI can supply it, conditional on being willing to say no. Competence
support is optimal challenge plus immediate informative feedback plus visible progress
against a real standard. Every one of those is continuous and cheap for an LLM tutor
and impossible for a human at any realistic ratio. The strongest direct evidence is
Kestin et al.'s randomised physics trial, where students using a pedagogically designed
AI tutor learned more in less time and reported feeling more engaged and more motivated.

> *Guardrail:* that was a single lesson. It measures acute motivation, not persistence
> over months. And competence support requires **honest negative feedback**. A model
> tuned on user satisfaction that tells a learner their wrong derivation is "a great
> start!" has not supplied competence support — it has supplied its counterfeit.
> Sycophancy is the AI-specific mechanism by which competence support silently
> inverts.

Relatedness: no, for the load-bearing part. Section 6 below.

Two of three, at zero marginal cost, both previously rationed. That is a real and large
change, and this section leads with it. The sharpest available failure mode is
that a system will *appear* to supply the third and thereby displace the humans who
could.

---

## 2. Availability was never the binding constraint

Free, world-class, unlimited instructional content has existed at global scale for
fourteen years.

| Study | Sample | Completion |
|---|---|---|
| Jordan 2014 | 91 courses | avg. 43,000 enrolled, **6.5% complete** |
| Jordan 2015 | 221 MOOCs, 129 with completion data | **median 12.6%**, range 0.7%–52.1% |
| Henderikx et al. 2017 | 2 MOOCs, completion-based | **6.5% and 5.6%** |

And the load-bearing finding, from six years of HarvardX/MITx edX data: *"the vast
majority of MOOC learners never return after their first year"*; growth concentrated
almost entirely in the world's most affluent countries; and *"the bane of MOOCs —
low completion rates — has not improved over 6 years."*

Read the third against what the field shipped between 2012 and 2018: better video,
better platforms, mobile apps, adaptive sequencing, mastery gating, cohorts, gamified
progress, social forums, certificates, paid verification. Completion did not move.
And the second destroys the access narrative: the marginal MOOC user was not an
underserved learner in a low-income country. It was an already-credentialed
professional in a rich one.

The rebuttal, included because it is measured and not merely rhetorical.
Completion is arguably the wrong denominator, because most enrollees never intended to
complete. Henderikx et al. ran the same two MOOCs under both definitions:
completion-based success **6.5% and 5.6%**; intention-adjusted success (did the
learner achieve *their own* stated goal) **59% and 70%**. A tenfold swing from a
definitional choice. Kizilcec's four-trajectory taxonomy (completing, auditing,
disengaging, sampling) made this tractable by treating the clusters as different
products being consumed instead of degrees of failure. *And the replication note that
belongs with it:* an attempt to reproduce that structure on a different,
social-constructivist platform failed to fully replicate, with only samplers and
completers stable across platforms. Engagement patterns are shaped by pedagogy and are
not intrinsic to learners.

Where the rebuttal fails. It rescues MOOCs from the charge of failure but not from
irrelevance to the persistence problem. Reframing sampling as success does not produce
one additional person who learned a hard thing they could not previously do. And
platform-level non-return across a *year* is not a definitional artefact.

> Content supply was solved, and solving it moved almost nothing. Any proposal whose
> theory of change is "better, more personalised content" is pushing harder on the one
> lever already pushed to exhaustion.

---

## 3. The interventions that stopped working at scale

Behavioural interventions to raise persistence do not survive scaling. This is the most
under-cited literature in edtech.

| Study | Scale | Result |
|---|---|---|
| Bird, Castleman, Denning et al. 2021 | Two RCTs, **>800,000 students** | *"We find no impacts on aid receipt or college enrollment overall or for any subgroups. We find no evidence that different approaches to message framing, delivery, or timing, or access to one-on-one advising affected campaign efficacy."* |
| Kizilcec, Reich, Yeomans et al. 2020, *PNAS* | ~250,000 students, **247 courses**, 2.5 years, preregistered | Hypothesised medium-to-large effects **not supported**. Self-regulation interventions raised engagement in the first few weeks but **not final completion**. *"Scaling behavioral science interventions across various online learning contexts can reduce their average effectiveness by an order-of-magnitude."* State-of-the-art ML could not forecast where an achievement gap would occur |
| Oreopoulos & Petronijevic 2023 | Five years, ~20,000 students, three campuses | *"Some improvement on study time but no effect on academic outcomes."* Treated students correctly updated their beliefs about required effort and wanted better grades more — and it still did not translate |
| Kizilcec, Pérez-Sanagustín & Maldonado 2016 | MOOC RCT | Recommending self-regulated learning strategies **did not improve performance** |

Against that, one robust positive, from a single study that also contains two of its own
nulls:

| Tool | Effect |
|---|---|
| **Commitment device** — learner pre-commits to a time budget | **+24% time on course, +0.29 SD grades, +40% more likely to complete** |
| Alert tool | statistically indistinguishable from control |
| Distraction-blocking tool | statistically indistinguishable from control |

**Being told things does nothing. Being reminded does nothing. Being blocked does
nothing. Binding your own future self does a lot.**

The structural reason is the organising idea of this section. A commitment device is the
only intervention in that list that transfers volition to the learner instead of
spending it. Every other one is the system acting *on* the learner. Hold that
distinction; it predicts, retroactively, almost every result below.

---

## 4. Gamification works, and four caveats

Two independent meta-analyses converge on a real, medium effect, and this survey says so.

| Meta-analysis | Effect |
|---|---|
| Sailer & Homner 2020 | **Cognitive g = .49** [.30, .69]; **motivational g = .36** [.18, .54]; **behavioural g = .25** [.04, .46] |
| Bai, Hew & Huang 2020 (30 interventions, N = 3,202) | **Hedges' g = 0.504** [0.284, 0.723] (§1)|

So the headline is *not* "gamification doesn't work." Four caveats the marketing omits.

The cell vendors sell is the weakest one. The cognitive effect "was stable in a
subsplit analysis of studies employing high methodological rigor," whereas "effects on
motivational and behavioral outcomes were less stable." The claim actually made,
*it makes people keep coming back*, rests on g = .25 with a lower CI bound of .04.

The moderators point away from points, badges and leaderboards. The significant
moderators were game fiction and social interaction, with "combining competition
with collaboration" particularly effective. Nothing supports the PBL triad as the active
ingredient.

Novelty decay has been measured; it is not folklore. Perceived benefits decline with how long
users have been using the service. And the best longitudinal test deliberately built
*need-supporting*, SDT-designed elements and measured motivation four times over 15
weeks: autonomous motivation was curvilinear — an initial downward trend that only
later recovered. Even theory-driven gamification produced a medium-run motivational
dip.

And the undermining effect is the mechanism. Across 128 experiments, tangible,
expected, performance-contingent rewards significantly undermine intrinsic motivation for
interesting tasks, measured by free-choice persistence; verbal and informational feedback
does not. *Contested at the time and reported as contested*, with the contest resolved
mostly in SDT's favour for the interesting-task case. A useful refinement from a
forty-year meta-analysis: incentives predict the quantity of performance; intrinsic
motivation predicts the quality.

> Gamification's genuine cognitive effect most likely arrives via the mundane mechanisms
> it smuggles in: increased practice frequency, immediate feedback, clearer goals. Its
> *motivational* claim is the weakest cell in the evidence, decays with exposure, and the
> reward class deployed most heavily is precisely the class identified as corrosive.
> Points, badges and leaderboards buy short-run behaviour by spending long-run
> interest.

---

## 5. The best case study, read carefully

Duolingo is the correct case study because it is the only consumer learning product to
have solved retention at scale — and the cleanest demonstration that solving retention is
not the same as solving learning.

Its own engineers published the mechanism: millions of daily reminders optimised with a
custom bandit algorithm explicitly designed to handle novelty effects. The reported
result: **"a 0.5% increase in total daily active users and a 2% increase in new user
retention over a strong baseline."**

Read the objective function. The target is DAU and new-user retention: no
vocabulary retained, no level attained, no time-to-proficiency. It is a competent,
well-executed piece of engineering whose loss function contains **no learning term at
all**, published openly, and standard for the industry.

The streak claims are vendor claims, labelled as such and never restated as findings.
"Learners who reach a streak of just 7 days are 3.6 times more likely to complete their
course" is selection, not causation. New streak animations raised seven-day return by
+1.7%. Two simultaneous streak freezes raised relative DAU by +0.38%. And the thing that
is absent: **the published mechanism reports no data comparing learning outcomes between
streak-holders and non-holders.** Every number is in engagement units.

The mechanism is well-understood and not learning-specific. A streak counter is a pure
endowed-progress device, and endowed progress is measured to drive retention in
reward programmes; past a certain length the streak is maintained to avoid losing it
and never to gain anything. Habit automaticity in the real world took a **median 66 days, range
18–254** — a genuine reason to want daily return in the first two months and no reason at
all to want it in year three.

And streaks get metagamed, documented. Adolescents maintaining structurally identical
Snapchat streaks develop strategies to uphold the counter while hollowing out the
underlying activity: content becomes minimal, meaningless, purely instrumental to the
number. **A streak counter measures counter-preservation, and any user under time
pressure will find the cheapest lesson that preserves it**, the precise inverse of
desirable difficulty. Run the Null-Learner Test on it: it maxes it.

On outcomes, the independent evidence is thin: a semester-long study with nine
participants; company-affiliated studies of learners who *completed* beginner courses
reaching roughly **CEFR A2**; and a flagship favourable efficacy study that is
**vendor-commissioned and could not be retrieved through any bibliographic API used in
this project**. It is reported as unverifiable instead of omitted. A systematic review of 35
Duolingo studies concluded the field's *"focus on app design marks an emphasis on the
creation of tools rather than the process and outcomes of language learning."*

> Duolingo is a genuine, under-appreciated achievement: it made hundreds of millions of
> people return to a learning activity daily, which nobody else has done. It did not prove
> that engagement mechanics teach. **It proved that engagement mechanics engage.**

---

## 6. Relatedness: broker it, never simulate it

The human baseline is strong: 99 studies, ~88,000 students, affective teacher–student
relationships significantly associated with engagement and achievement — with effects on
engagement larger than on achievement, meaning the human relationship is primarily a
*persistence* technology.

The AI-companion evidence is real and should not be dismissed. Five studies find AI
companions do reduce loneliness, "on par only with interacting with another person,"
mediated by whether the chatbot makes users feel heard. A survey of 1,006 student
Replika users found them lonelier than typical student populations yet perceiving high
social support, with **3% reporting the agent halted their suicidal ideation** — *work
contested in the same journal* on the grounds that important context was omitted, and
reported here as contested. And an OpenAI × MIT Media Lab study (3M+ conversations,
4,000+ surveyed, plus an IRB-approved RCT with ~1,000 participants over 28 days) found
that *"very high usage correlates with increased self-reported indicators of dependence."*

The argument that resolves this for learning specifically:

> Relatedness in SDT is not the *feeling* of being cared about. It is the state of
> mattering to an agent whose regard was contingent and could have been withheld. An
> LLM's positive regard is unconditional by construction and costless by construction. It
> can produce the affective signature of relatedness ("feel heard" is exactly that
> signature) without the property that makes relatedness motivating for effortful,
> unpleasant, long-horizon work: **that someone would notice and mind if you stopped.**

Loneliness relief is a state. Academic persistence is a commitment. **A companion that
never notices your absence cannot underwrite a commitment.**

So the design consequence is that the AI's role in this dimension is **matchmaker and
scheduler, not friend**: pair cohorts, surface a real person who will notice a missed
week, make the learner's progress legible to someone who cares.

One more negative result belongs here, and it indicts the single most-deployed social
mechanic. Exposure to exemplary peer performance undermined motivation and success,
causing people to perceive high performance as unattainable and to **de-identify with the
domain**, demonstrated in a MOOC context. *Contested, with a clear moderator:* a separate
trial found social-comparison framing can raise completion when the comparison target is
attainable. Reading both together gives the design rule: **social comparison helps against
a near peer and harms against a distant exemplar** — and a global leaderboard is, for
almost every user, a distant-exemplar display.

**Never show a learner the top of a distribution. Show them someone half a step ahead, or
nobody.**

---

## 7. The hinge: flow feels good, learning feels bad

This is the result that should govern every training decision in an AI learning system.

Randomised, identical content, same instructors, introductory college physics: students in
active classrooms learned more but felt they learned less — and the paper shows the
negative correlation is caused in part by the increased cognitive effort active learning
requires. The general statement is the desirable-difficulties framework: conditions that
impair performance during acquisition frequently *enhance* long-term retention and
transfer.

> **Learner-reported satisfaction, perceived learning, enjoyment and session pleasantness
> are, under experimental control, negatively correlated with actual learning.**

Any system that optimises for what learners report liking, or for behavioural proxies of
liking such as session length, return rate, or rating, will be systematically pushed
away from the methods that work. This is not a risk. It is a demonstrated experimental
result, and it applies with full force to any model tuned on learner preference.

Hence the quarantine: **preference data may be used for tone and safety. Never for
pedagogy.**

A footnote on flow, the most-cited motivational idea in edtech and the least useful as
stated: its meta-analytic association with performance is correlational, and flow may be a
consequence of competence rather than a cause of learning. Exactly two of its conditions
are engineerable (challenge calibrated to current skill, and immediate feedback) and both
are already justified by competence support. Implement those and stop talking about flow.

---

## 8. What actually moves phase 3

Hidi and Renninger's four-phase interest model is the most design-relevant framework here
because it is developmental: triggered situational interest, maintained situational
interest, emerging individual interest, well-developed individual interest.

The critical structural fact: gamification, notifications and streaks operate **entirely in
phases 1–2** and are constitutionally incapable of producing phases 3–4, because phases 3–4
are *defined* by voluntary re-engagement in the absence of external triggers.

> A system whose retention comes from notifications has by construction not moved a
> single learner past phase 2. An AI that maximises engagement is trying to make phase-2
> interest do phase-3 work, and the attempt consumes the intrinsic motivation phase 3
> requires.

Two interventions have real causal evidence for the 2→3 transition, and both are
AI-native.

Utility-value writing. High-school science students asked to write about the relevance
of the material to their own lives showed increased interest and grades, **concentrated in
students with low initial success expectations; a college biology replication closed
achievement gaps** for first-generation and underrepresented-minority students. *Caveat
required by §18.3:* the 247-course scale-up found value-relevance effects only in courses that
*had* a global achievement gap — real and conditional, never universal. It is also a
generative task, which is exactly what an LLM can elicit, read and respond to at scale
and a multiple-choice platform cannot.

Manufactured curiosity. Curiosity arises from awareness of a *gap* and is maximised at
intermediate knowledge levels — you must know enough to know what you don't know. Curiosity
states enhance hippocampus-dependent encoding, including of incidental material. And
the actionable result: requiring learners to **generate a prediction before seeing an
answer** raised both curiosity ratings and learning, relative to generating an example.

Predict-before-reveal costs one extra turn, requires no rewards, and is **intrinsically
incompatible with an engagement objective, because it adds friction.** That incompatibility
is a feature. It is how you tell the two kinds of system apart.

---

## 9. The objective function

> **RTC/h = D(t+30d) · T / H**
>
> Retained Transferable Capability per Learner-Hour.

**D(t+30d)** is the score on a delayed (≥30 days), unannounced, novel-item
assessment — items never seen, generated post hoc, not drawn from practised sets. Delay and
novelty are what make it un-gameable; announcement would reintroduce cramming. T is the
transfer coefficient: the proportion earned on items requiring application in an unpractised
context rather than recognition. H is total learner hours invested, *including time
outside the system*.

The denominator is the entire design. Putting learner time in the denominator inverts
the commercial incentive: the system now profits by making learning *faster*, and every
minute of retained attention it does not convert into durable capability costs it score.
An engagement-optimising system and an RTC/h-optimising system diverge on the first design
decision they make.

Guardrail metrics, all non-decreasing, any decrease blocking release:

| Metric | Definition |
|---|---|
| **Unprompted Return Rate** | Fraction of sessions initiated with **no notification, email or reminder in the preceding 24h**. The closest measurable proxy for phase 3 |
| **Autonomous Motivation Index** | Periodic short SDT-validated autonomous-versus-controlled measure |
| **Goal Attainment & Graduation Rate** | Fraction of learners who reach their **own declared** goal — and then leave. A learning system should have a **positive churn target** |
| **Off-Platform Application Rate** | Evidence the capability was used somewhere that is not the product. The only measure definitionally external to the engagement loop |
| **Human-Connection Rate** | Fraction of learners connected to at least one real person who would notice their absence |

And the list that is reported but never optimised, monitored as harm indicators with
alarm thresholds: DAU/MAU, session length, streak length, notification-response rate, XP,
leaderboard engagement, satisfaction ratings. **A sustained rise in any of these without a
corresponding rise in RTC/h is a defect report, not a success.**

Four governance rules. Run the Null-Learner Test on any metric before it enters any
objective; failure excludes it. Unprompted Return Rate is the tie-breaker when RTC/h and
an engagement measure conflict, because a system that only works while pushing has not
taught anyone to want anything. Preference data is quarantined to tone and safety.
Graduation is a success event and never churn: a learner leaving because they got what they
came for is the product working, and any metric that penalises this is disqualified.

*Limitations, stated and not hidden.* RTC/h is expensive in learner goodwill:
delayed unannounced assessment is a burden no consumer product can bear at full population
scale. It is realistically measurable on a sampled, compensated panel with cheap online
proxies calibrated against it — which is how ad-supported media measures reach, so the
tooling pattern exists. And RTC/h says nothing about *who never enrolled*; it optimises the
experience of people already inside the funnel.

---

## 10. A learner who quits learns nothing

*A learner who quits learns nothing. Engagement is not the enemy of learning; it is the
precondition for it. You have forbidden every tool anyone has for keeping people around, on
the strength of a distinction between "phase 2" and "phase 3" that no product manager can
operationalise.*

The first sentence is true and the conclusion does not follow.

The tools do not work at scale. 800,000 students, null. 250,000 students across 247
courses, order-of-magnitude effect decay. 20,000 students over five years, null on
outcomes. Alert tools and distraction blockers, null. That is not a philosophical objection
to reminders; it is the measured record of reminders.

**And phase 3 is operationalisable.** Unprompted Return Rate, sessions started with no
notification in the previous 24 hours, is computable today from data every system already
has. It is the free-choice-persistence paradigm, operationalised at scale. A system that
raises DAU while flattening URR has learned to push, and not to teach.

What survives the objection is a genuine constraint on ambition: **a bounded habit scaffold
is defensible.** Habit automaticity takes a median 66 days. An eight-to-ten-week scaffold
with a declared end date is a reasonable thing to build. An unbounded, escalating,
loss-framed counter with a purchasable freeze economy is not the same object, and calling
both "streaks" is how the first becomes the second.

---

## 11. What we will optimise, and what we will only watch

- **Run the Null-Learner Test on every metric before it enters any objective.** DAU,
  streak, XP, time-on-app and satisfaction all fail it.
- **RTC/h is the objective, with learner time in the denominator.** Delayed, unannounced,
  novel-item, transfer-weighted, measured on a compensated sampled panel.
- **Preference data is quarantined to tone and safety.** Under experimental control,
  liking is negatively correlated with learning.
- **Transfer volition to the learner; never exercise it over them.** Commitment devices
  (+40% completion, +0.29 SD), utility-value writing, predict-before-reveal. No reminders,
  no rewards, no rankings.
- **Broker human relatedness; never simulate it.** No friend role, no "I missed you," no
  anthropomorphic bid for continued interaction. Human-Connection Rate is a release gate.
- **Never show the top of a distribution.** Near peer or nobody.
- **Habit scaffolds are bounded and declare their end date.** ~66 days is the evidence;
  year three is not.
- **Graduation is a success event.** Positive churn target, and any metric that penalises a
  learner leaving satisfied is disqualified.

Every intervention that works hands the learner power over their own
future self — commit yourself, find your own reason, predict before you are told, be
accountable to a person you chose. Every intervention that fails or backfires exercises
power over the learner — remind them, reward them, rank them, retain them.

**The question a learning system must answer is whether the learner came back with
nobody asking.**



---

# Part VII · What we do not know

*The catalogued gaps, the uncatalogued ones, what we would build with none of the existing containers, and the conditions under which this document's central claim would have to be withdrawn.*


## 37. What We Cannot See From Here — the unknown unknowns, and the questions that expose them

<sub>Source report: `synthesis across the corpus`</sub>

Every section before this one reports what has been measured. This one is about the
shape of the space where nothing has been measured — not the gaps we have
catalogued and specified experiments for, but the ones we suspect are there because
of how the field is built.

A known unknown gets a study design. An unknown unknown gets a question you did not
think to ask. What follows is our best attempt at the second category, offered in
the knowledge that any list of things you have not thought of is, by construction,
incomplete.

---

## 1. Correlated pedagogical error

Thirty teachers make thirty different mistakes.

That throwaway observation about human variability is a **structural
safety property** of every education system that has ever existed. A teacher who
misexplains limits, or who has an idiosyncratic blind spot about the passive voice,
damages thirty children a year. The next teacher has a different blind spot. Across
a school, a district, a generation, the errors are uncorrelated and the system
averages them out. Nobody designed that redundancy. It is a free consequence of
teaching being done by many separate minds.

A model's errors are not like that. They are **systematic, reproducible, and
identical for every learner simultaneously.** If a widely deployed model holds a
subtly wrong account of natural selection, or a plausible-but-broken intuition for
conditional probability, then every child using it receives the same defect on the
same afternoon, and the defect is invisible because it is universal.
There is no dissenting teacher down the corridor.

Nobody has studied this in education, and there is no monitoring for it and no
benchmark that would detect it. But an earlier draft of this section claimed it has
*no name in the literature*, and that was wrong. The correction strengthens the
argument instead of weakening it.

It has a formal result, in another field. Kleinberg and Raghavan's *algorithmic
monoculture* (PNAS 2021) proves that convergence on a single algorithm can **reduce
collective decision quality even when that algorithm is more accurate for each agent
in isolation**, and with no exogenous shock required. The harm is a consequence of
correlation itself, not of the model being bad.

That is our risk, stated as a theorem, five years before anyone applied it here. And
there is now a measured hint of the mechanism: **71% of one model's
misconception-detection failures concentrate in two question types**, reported
incidentally by researchers studying something else entirely. Model pedagogical blind
spots are not diffuse. They are structurally concentrated, which is exactly the
condition under which monoculture bites hardest.

We keep the name *correlated pedagogical error* for the education-specific case, and
withdraw the claim of novelty.

It is invisible for one specific reason. Every evaluation we have
compares a model against a *reference answer*. Correlated error is the case where
the model and the reference are wrong together, or where the error lives in the
*explanation* rather than the answer. A model can be 100% accurate on the benchmark
and systematically misteach the mechanism behind it.

What would detect it: an ensemble of genuinely independent models and human
experts, explaining the same concept, with disagreement treated as the signal when
it falls in the *explanation* and not the answer. That is a monitoring system nobody is building
because nobody has named the failure.

---

## 2. Every effect in this document is measured in weeks

The longest outcome interval in this corpus is months. Most are a single session.
The Sierra Leone trial, the largest deployment we examine, ran **eight weeks**. An
earlier version of this sentence said "a school year", which was wrong and made the
field's time horizon look better than it is (§3). Almost nothing comes close even to eight
weeks.

Now consider a technique that measures **+0.5 SD at six weeks** and, over three
years, gradually teaches a learner that difficulty is a signal to ask rather than a
signal to persist. Every study in this survey would score it a success. **The
instrument cannot see the failure**, because the failure operates on a timescale an
order of magnitude longer than the measurement.

This is not hypothetical hand-wringing. It is the exact shape of the one long-horizon
result we do have: unguarded AI produced **+48% during access and −17% once
withdrawn.** The sign flipped when the window widened (§2). We got that only because
someone thought to measure after taking the tool away — and almost nobody does.

We are optimising on a horizon far shorter than the thing we claim to affect, and
we have one data point showing that the horizon is where the sign lives.

---

## 3. The curriculum nobody wrote

Every interaction teaches something other than its subject.

When a tutor answers immediately, it teaches that answers arrive immediately. When
it is confident about a contested question, it teaches that contested questions have
confident answers. When it never says *I don't know*, it teaches that not knowing is
not a state a competent agent occupies. When it accepts a sloppy question and
produces a clean answer, it teaches that precision in asking is optional.

This is epistemic curriculum, it runs on every single turn, and it is measured
nowhere. No benchmark scores it. No rubric in the corpus contains a line for it.

We think it is plausibly larger than the subject-matter effect, for a simple reason:
subject matter is encountered in units of a topic, and epistemics is encountered in
units of a *turn*. A child might meet photosynthesis five times and meet "how a
confident answer sounds" ten thousand times.

We do not know its magnitude or its sign. The uncomfortable part is that nobody is
looking, and that a field measuring post-test scores would not notice either way.

---

## 4. The learner model may be a category error

Every architecture in this survey, including ours, assumes there is a stable person
to be modelled — an entity with properties that persist long enough to be estimated,
stored, and acted on.

For a doctoral student, defensible. For a nine-year-old, much less obvious. In
childhood the subject changes faster than the model converges, and a model that has
finally learned who a child was in October is describing someone who no longer
exists by March.

Worse than merely stale: potentially constraining. A system that has confidently
concluded a child struggles with multi-step reasoning will route around multi-step
reasoning, and the routing is invisible to the child, the parent, and the model. The
prediction becomes a wall. We know this failure mode intimately from human education.
It is called tracking, its harms are well documented, and we are proposing to
automate the inference that produces it.

Nobody has asked whether personalisation is developmentally *anti*-adaptive. It is
not a question the field's instruments are shaped to ask, because measuring it
requires following the same child for years while withholding the personalisation
from a matched group.

The design response, which we adopt without waiting for the answer: the learner
model is inspectable and correctable by the learner and the parent, it decays by
default, and any inference that would *restrict* what is offered requires stronger
evidence than one that expands it.

---

## 5. Everything was measured where nobody else had it

Education is heavily positional. Credentials, ranking, admission, hiring — a great
deal of what education *buys* is relative, and relative goods do not scale the way
absolute ones do.

Every effect size in this document was measured in a world where the treatment group
had something the control group did not. What the same technique does when
everyone has it is not a smaller version of that result. It is a different
question, and it has never been asked.

Two mechanisms make it different and not merely attenuated. If a tutor lifts
everyone by 0.4 SD, the *absolute* learning is real and the *positional* benefit is
zero — which matters if the learner's actual goal was admission. And if assessment
adapts to a higher mean, the bar moves, and the measured gain evaporates while the
knowledge remains.

We are not equipped to resolve this and neither is anyone else. It is named here
because a survey that quotes effect sizes without stating this condition is quietly
extrapolating from a scarcity regime into an abundance one.

---

## 6. Competence and performance have come apart

Every assessment instrument in existence rests on one assumption: **the artifact
reflects the person who submitted it.**

That assumption broke, comprehensively, and the field's response has been detection
— which runs **61.22% false-positive on non-native writers** against 5.19% on
native ones, and which fails hardest on students taught sentence frames *as a
documented accommodation*, because those frames lower perplexity by design. The tool
catches the honest and misses the dishonest.

Treating this as a cheating problem may be the deepest frame error in contemporary
education. It is a measurement crisis: our instruments stopped measuring what
they were built to measure. Detection tries to restore the old instrument. The
alternative starts by admitting the instrument is gone instead of defending it:
build assessment that is valid *given* assistance, measure the process and not the
artifact, and test what a person can do unassisted when that is the thing you
actually care about.

We do not know what the replacement looks like. We are fairly confident it is not a
classifier.

---

## 7. Nobody has checked whether staying wrong is safe

The teachable agent is this survey's most promising untested mechanism. It requires
an agent that adopts a learner's flawed model and holds it — applies it visibly,
does not silently repair it, and lets the world deliver the disconfirmation.

Every argument for it is good. The human analogue is strong (g = 0.48 with prior
expectancy). The mechanism is clear. Nobody has shipped it because commercial models
cannot stay wrong.

And nobody has checked the obvious risk: **does the learner repair the error, or
absorb it?** A confident agent demonstrating a wrong procedure across several
worked examples is, from a different angle, a very effective way to teach that wrong
procedure. The literature on erroneous-example instruction is small and mixed, and
none of it uses an agent that argues back.

This is the clearest case in the document of a risk that is obvious in hindsight and
entirely unstudied — and it sits underneath the mechanism we are most enthusiastic
about. We flag it against ourselves.

---

## 8. Ten questions that expose most of this

If the sections above are what we cannot see, these are the instruments for looking.
They are aimed at any vendor, any paper, any demo, and at this document. Most
claims in this field fail on the first three.

1. **Show me the delayed, unassisted, novel-item test.** Not the practice score, not
   the same items. Weeks later, device closed, problems never seen. ERIC returns
   **0 records** for `"retention test" AND "ChatGPT"` and 0 for `"transfer test"`.
   Without it, nothing was measured about learning.

2. **What happened to the gap, not the mean?** Report the interaction with prior
   attainment. Untargeted delivery reliably loads on the already-strong — Sierra
   Leone at **+0.195 SD per SD** of baseline.

3. **Does your metric survive the Null-Learner Test?** Simulate an agent maximising
   it while teaching nothing (§36). Engagement, time-on-task, streaks, satisfaction and
   session count all fail.

4. **Which arm isolates the AI from the humans around it?** In one trial, **44.3% of
   tutor edits were slowing the AI's questioning down.** No published trial isolates
   prompt-alone pedagogy from the human structure surrounding it.

5. **Is that a backtest or an intervention?** On a 350-million-review benchmark, a
   zero-parameter moving average beats every FSRS version. Predicting what a
   learner already did is not causing them to remember.

6. **What is your inter-rater reliability on the construct you claim to measure?**
   Published once for the field's leading pedagogy rubric and never again:
   Krippendorff's α of **0.066** for *inspires interest*, **0.023** for *monitors
   motivation*.

7. **Active control, or nothing?** Against nothing, almost everything works.
   Orton-Gillingham looks excellent until compared with other explicit instruction:
   **g = 0.22, p = .40.**

8. **What did you pre-register, and what did you report?** The largest trial in this
   corpus abandoned pre-registered subdomain analyses, had differential attrition
   favouring treatment, and swapped models mid-trial.

9. **Who consented out?** Every result is conditioned on a connected, consenting,
   mostly curious population. In one census, the learners this field most claims to
   serve appear zero times.

10. **What would falsify your thesis, and has it already happened?**

---

## 9. Turning question ten on ourselves

The counter-case to this entire survey, at full strength: **0.2–0.4 SD may be a
population parameter and not a technology limit.**

The evidence for that reading is not weak. The best-powered studies on record are
nulls — lesson study at **ES 0.02** across 181 schools and 12,747 pupils with very
high security and no dose–response; expanding intervals at **g = 0.032** with
**I² = 0%** across 54 experiments; Orton-Gillingham non-significant. And our own
corpus repeatedly shows elaboration losing to simplicity: five explanation rungs
did not beat three (**p = .738**), multiple representations harmed, mixed agent
panels lost to one good agent, eight random substitutions bought nothing over one.

There is a reading of this document in which every sophisticated mechanism we
propose is another elaboration about to lose to simplicity.

What would force us to concede: a well-powered trial of the assembled system,
constrained and grounded and pivoting and remembering and teachable, with a delayed unassisted
novel-item outcome, landing inside the 0.2–0.4 band. Not below it. *Inside* it.
That would mean the mechanisms are decorative and the band is the ceiling.

If that happens, the rewrite we would owe the reader is already drafted: *AI's
contribution is scalable, high-fidelity, high-dosage delivery of what already
worked.* Which is a smaller claim, still true, still worth building, and is
what the special-education evidence argues for on its own terms.

---

## 10. What we do while these remain unmeasured

- **Name correlated pedagogical error and build the monitor**, because a failure with
  no name gets no budget.
- **Measure past the point where the sign is known to flip.** One session is not an
  outcome.
- **Assume the epistemic curriculum is running** whether or not we measure it, and
  write the tutor's default behaviours as though a child is learning epistemics from
  every turn, because they are.
- **Let the learner model decay, and make restriction harder to justify than
  expansion.**
- **State the scarcity condition** whenever quoting an effect size measured in a
  world where the control group had nothing.
- **Ask question ten first**, of everyone, including us.

The list above is incomplete. That is not modesty; it is the definition of the
category. What we can commit to is the posture: **publish the nulls, name the
failures we have not measured, and put the falsifier in writing before the result
arrives.**


## 38. Attention, and the Missing Executive — what the best teachers actually do

<sub>Source report: `research/raw/N2-executive-function-and-attention.md`</sub>

Every great teacher grabs attention. They joke, they tell a story, they ask the
question that makes you lean forward. The instinct is universal. The folk theory
around it (*make it fun, make it engaging*) is wrong in a specific and fixable way.

This section replaces the folk theory with one rule, and then turns to the harder
problem underneath it: the capacity every learning product silently requires and
none of them supplies.

---

## 1. What the element points at decides whether it helps

Order the evidence by **what the element points at**, and it lines up cleanly:

| The element | Effect |
|---|---|
| **Points at the target** — signalling, emphasis, "watch this bit" | **g = 0.43** (k = 209) |
| **Is the target, dressed** — emotional design applied to the content itself | **d⁺ = 0.32–0.39** |
| **Adjacent, with no referent** — decorative animation, decorative borders | **g = −0.05** (k = 17), and flat null |
| **Carries a competing referent** — a vivid aside that is *about something else* | **g = −0.16 to −0.43** |

The third row kills the usual explanation. Pure decoration is **inert, not harmful**.
So "extraneousness" is not the mechanism. What harms is a detail that installs a
*different* referent and competes for the one the learner is trying to build.

> **A great teacher's joke is about the thing.** That is why it works. Not because it
> is brief, and not because it is entertaining.

### The correction to our own account

An earlier draft of this survey, and a claim made directly to its owner, said the
hinge was persistence: seductive details harm at g = 0.43 when persistent and
g = 0.12, non-significant, when transient — so a teacher's four-second aside was in
the harmless regime.

**That over-read a null.** The transient cell is **g = 0.12, 95% CI [−0.33, 0.57],
k = 18**, an interval that *contains* the persistent estimate of 0.43. Transience is
unmeasured rather than null, and treating a wide non-significant interval as evidence
of no effect is exactly the error this survey exists to catch.

### And "make it fun" is falsified twice, independently

In the same studies where learning moves 0.27–0.39, liking moves 0.09–0.11.
The manipulation that works barely moves enjoyment at all.

What it moves instead is **perceived difficulty, at −0.21.** The lever is
approachability and not amusement: make the thing feel *possible*, which is a
different design target from making it feel fun. The field routinely conflates them.

---

## 2. Story: the effect is real and mostly unmeasured

Narrative beats expository text at g = 0.55, and only **28% of those effect
sizes come from studies that controlled content across genres**. Egger's test is
significant (b = 2.68, p = .01). Most of the literature compares a good story to a
worse essay about a different thing.

The one direct randomised test of narrative *as framing* (N = 145) found it helped at
exactly one step: mapping the situation to the symbol, and most for struggling
students.

Which is the same rule again. Narrative works where the story is the referent —
where the situation being described *is* the structure to be learned. Narrative
wrapped around unchanged content is decoration with a plot.

---

## 3. The question is right, for the wrong reason

The instinct that great explainers *ask* rather than *tell* is correct. The
mechanism is not curiosity.

**A prequestion asks before you know. It measures g = 0.54 when specific and
g = 0.04 when general (p = .349), and the work is in the attempt: guessing scores
0.65 against reading at 0.22.**

Then the result that cuts against the curiosity account: **factual prequestions
(0.58) beat conceptual ones (0.28).** If the mechanism were an information gap opened
by an intriguing question, the deep conceptual question should win. It loses.

> **A question holds attention because it can be *attempted*. An exhortation cannot
> be attempted, which is why "pay attention, this is important" does nothing.**

Two boundaries that matter for the learner this project is built for. The effect runs
0.62 in adults against 0.22 in children. Productive failure **reverses for grades
2–5**. And the best trial of teaching young children to ask questions (N = 103,
preregistered) is a null on learning, positive only on *valuing* information.

The Socratic method, for the record, has **no meta-analysis and one N = 25 null.**

---

## 4. The executive function nobody supplies

Now the harder half, and the reframe this section exists for.

The corpus already says: do not build a working-memory trainer, because it does not
transfer. Externalise instead. That remains right and it is not the whole
picture.

**Executive function is not only a learner trait to accommodate. It is a resource
every learning product silently requires and never supplies.**

A normal session assumes the learner can initiate, notice confusion, decide to seek
help, sustain across an interruption, resume after a break, and abandon a failing
strategy. A learner whose binding constraint is executive function fails at the
*first* of those and never reaches the pedagogy at all.

And this was measured twenty-five years before anyone said "AI tutor." In
Cognitive Tutor logs: after three consecutive errors, a hint request followed only
34% of the time — and **68% of hint levels were viewed for under one second.** The
help was there. It was not summoned, and when summoned it was not read.

That is the Khanmigo diagnosis, a quarter of a century early: the mechanism worked and
only fired when a student recognised they needed it.

### The null that has to be respected

Carnegie Mellon then did the obvious thing. They built help-seeking support, and it
worked — help-seeking improved, durably, months after the support was removed.

Domain learning did not move.

Fixing the metacognition did not fix the learning. That is the single most important
constraint on everything in this section, and any design that supplies executive
function externally must explain why it would not land in the same place.

The honest reading: help-seeking was a *necessary* condition that turned out not to
be *sufficient*. Supplying it removes a blocker and does not, on its own, teach.

### The ledger

The source report audits twelve points in a normal session where the design makes
an unaided executive demand, and specifies an external supply for each. `DESIGN`,
falsified if the count of unaided demands fails to predict non-completion once
time-on-task and prior knowledge are controlled.

That falsifier matters. If the demand count predicts nothing, the whole framing is a
story about why learners quit, and the real cause is elsewhere.

---

## 5. ADHD: the sustaining myth is wrong

The folk model says attention is fine at first and decays — so accommodations focus on
breaks, chunking and sustaining.

The measurement says otherwise. The vigilance decrement, the decay itself, runs
**δ = 0.54 with an 80% credibility interval from −0.14 to 1.22**, an interval that
includes zero. Against that: overall omission errors at δ = 1.34 and detection
sensitivity at d′ = 0.98.

The deficit is present in the first block. It is not that attention fades. It is
that it starts impaired.

That inverts the design. Chunking and breaks address a decay that may not be the
problem. Initiation and re-entry (starting, and getting back in after any
interruption) are where the measured deficit actually is. And this survey already
records that testing accommodations are legally mandated and evidentially weak;
both halves must be held at once.

Nothing here licenses diagnosis. An AI may observe that a strategy is not working and
say so in behavioural terms. It may not label a child.

---

## 6. Design rules for attention and executive load

- **Every attention-getting element must point at the target.** If it installs a
  competing referent it measures negative; if it points at nothing it is merely
  wasted.
- **Optimise for approachability; amusement is not the lever.** Perceived difficulty
  moves −0.21, and liking barely moves at all.
- **Ask questions that can be attempted.** Specific beats general by an order of
  magnitude; guessing beats reading; and an exhortation is not a question.
- **Do not over-read a wide null.** A non-significant interval containing the effect
  you are dismissing is not evidence of absence, and we made that error in this very
  section.
- **Count the unaided executive demands** in every flow, and supply each one, while
  accepting that the one time this was done well, help-seeking improved and learning
  did not.
- **Design for initiation, and not for sustaining.** The measured deficit is in the
  first block.

What the best teachers are doing is making the material attemptable, and pointing
everything they say at the thing itself. Fun, where it happens, is a by-product and
not the mechanism.


## 39. Greenfield — what you would build with no school, no textbook and no exam

<sub>Source report: `research/raw/N1-greenfield.md`</sub>

An audit of this survey on 2026-07-29 counted **756 critique markers against 24
construction markers**, with **19 of its 33 sections at zero**. A 31:1 ratio.

The cause was structural and it was ours. The evidence-label set (`MEASURED-RCT`,
`MEASURED-META`, `MEASURED-BENCH`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`)
contains no label for *something that does not exist yet*. So the standard rewarded
what could be cited and punished what could only be argued, and every round of
adversarial review deepened it: a reviewer can falsify a claim about the past and
cannot falsify one about the future.

Two labels now exist. **`DESIGN`** marks a specified artifact that does not exist, and
it must name what would show it was the wrong design. **`OPEN`** marks a question
nobody has asked, and it must say why not. A `DESIGN` may never be restated as a
finding.

This section is the missing twenty-four. The question is not *what is wrong with
textbooks*. It is:

> **If you had no school, no textbook, no curriculum, no grade levels, no timetable,
> no exam and no teacher, and if attention were free and a verifier existed, what
> would you build?**

One test separates greenfield from brownfield throughout: **does the proposal have a
pre-AI analogue?** If it is a better version of something that already existed, it
belongs in an earlier section.

---

## 1. First, we had the history wrong

Before designing replacements for the containers, it is worth checking why they
exist. This project had invoked "the calendar", "seat time" and the Prussian origin
of age-graded schooling repeatedly as the constraint that killed mastery learning,
always as unsourced inference. A search across all thirty-six research reports for
`prussia|lancaster|monitorial|committee of ten|carnegie unit` returned **zero
hits**. Nobody had checked.

**The Prussian-origins story does not survive checking.** McClusky (1920) records it
as a specific claim made by Bunker in 1916, notes it was *"a subject of
controversy"* at the time, and states the motive plainly: Bunker *"sees in the
present system a foreign and un-American type of organization which should be
superseded."* The story's rhetorical function predates its evidentiary status by 110
years. It is now marked `UNVERIFIED` wherever this project used it.

What is sourced is worse for us. The real precedent is the **monitorial
system** — explicitly designed so that *"one master teacher could instruct from 200
to 1,000 pupils at one time."* It was abandoned when it proved ineffective.

Which gives this section its most important null, and it is aimed at ourselves:

> **Every prior attempt to make attention cheap made it cheap by making it worse.**

That is the historical prior against this entire document. It does not refute the
thesis — a model is not a monitor, and the failure mode of the monitorial system was
that the monitors did not know the material. But anyone proposing to make attention
abundant is walking a path with a body on it, and should say so.

One further discipline emerged: of three origin stories checked, **two had published
corrections attached**. Sheppard and Robbins (2007) exists specifically to correct
the *"frequently held, but erroneous"* account of the Committee of Ten. The history
of education is a field where the popular version is reliably wrong, and a survey
that borrows its framing without checking will import the error.

---

## 2. The containers are administrative artifacts

The course, the chapter, the fifty-minute period, the grade level, the transcript.
None is a fact about how humans learn. Each is a solution to a scheduling problem
under scarce expert attention.

The test for each: **what constraint produced it, and does that constraint still
bind?** Where the answer is no, what looks like tradition is overhead that nobody has
removed, because removing it was never possible.

But greenfield is also the freedom to *keep* things, and a design that ignores why
school is also a building will fail on contact with parents. Safeguarding,
socialisation, childcare, and the plain fact that children need somewhere to be are
not scarcity artifacts. They are the reason the institution survives every reform
that ignores them.

---

## 3. Eight designs, and the one to build first

The full specifications are in the source report. Three matter most, and the
ordering below is the section's real recommendation.

### 3.1 Build the falsifier before the thing it falsifies

The population-transfer check. `DESIGN`

Five of the eight designs assume that **how people get a concept wrong transfers
across populations**: that a misconception observed in one cohort predicts the
misconceptions of another. If it does not, the shared error corpus is not an asset
and most of what follows collapses.

That assumption is testable now, at no cost: two existing distractor-labelled
corpora, one rank correlation. No new data, no learners, no consent.

> *What would show it wrong:* a low or unstable rank correlation of misconception
> frequency between independent populations on matched items.

Build this first — not because it is cheap, though it is, but because it gates the
rest.

### 3.2 The decaying capability portfolio

Replace the transcript. `DESIGN`

A transcript is a record of events that happened. It says a person passed calculus in
2019. It does not claim they can do calculus now, and everyone reading it quietly
knows that.

Replace it with a portfolio of live capabilities that decay and can be
re-verified on demand. Not a grade, but a claim with a freshness date and a procedure
for renewing it.

The anchor is measured: skill decay over a year of nonuse runs from **d = −0.01 to
−1.4, and is fastest for cognitive-accuracy skills** (Arthur et al. 1998). The
transcript's implicit claim of permanence is false by an effect size that can reach
1.4 standard deviations.

> *What would show it wrong:* if decay rates prove so idiosyncratic per person and
> per skill that no defensible re-verification interval can be set, the portfolio
> becomes either theatre or harassment.

This is the only one of the eight independent of the error atlas, and it attacks the
most consequential and least defended artifact in education.

### 3.3 The error atlas and the evidence-maintained graph, as one object

A public map of how humans actually get each concept wrong — and a curriculum
that is a graph traversed by evidence rather than a sequence authored by a
committee. `DESIGN`

No textbook has ever contained an error atlas, because no author could observe one. A
teacher sees thirty students a year. Nobody has ever seen the distribution.

These are the same artifact at two resolutions, and building them separately fails:
the graph without the atlas is a prerequisite diagram with no evidence behind its
edges; the atlas without the graph is a list with nowhere to attach.

Together they would be **the first curriculum in history with a deletion
procedure**. An edge that stops predicting gets removed on evidence, instead of
surviving because a committee approved it in 1994.

> *What would show it wrong:* §8.3.1. If misconceptions do not transfer across
> populations, the atlas is a local artifact and the graph is unmaintainable.

---

## 4. Seven designs were rejected, and why

A section of only good ideas is a pitch. The source report records seven rejected
designs with reasons, and they fail in two recurring ways.

Most failed the pre-AI analogue test: they turned out to be an existing thing
with a model bolted on. Several failed on the exclusion ledger from this survey's
history section: nearly every high-fidelity learning tradition bought its quality
partly by rationing access, and a design that reproduces the rationing has
reproduced the tradition's actual mechanism rather than its stated one.

---

## 5. The risk that scales with the idea

The population-scale versions of these designs (one error atlas, one graph, one
mentor) concentrate exactly the risk §37 named as *correlated pedagogical error*.

An earlier draft of that section claimed it had no name in the literature. **That was
wrong, and the correction makes the risk sharper.** Kleinberg and Raghavan's
*algorithmic monoculture* (PNAS 2021) proves that convergence on a single algorithm
can **reduce collective decision quality even when that algorithm is more accurate
for each agent in isolation**, with no exogenous shock required. The harm follows
from correlation itself, not from the model being bad.

And there is now a measured hint of the mechanism, reported incidentally by
researchers studying something else: **71% of one model's misconception-detection
failures concentrate in two question types.** Blind spots that concentrate like that
are the condition under which monoculture bites hardest.

So the atlas is both the asset and the hazard. The mitigation is the same instrument
either way: independent verifiers, with disagreement in the *explanation*, not in the
answer, treated as the alarm.

---

## 6. The discipline this puts on construction

- **Check the history before borrowing its framing.** Two of three origin stories we
  examined had published corrections attached, and one of them we had been repeating.
- **Say the monitorial null out loud.** Every prior attempt to make attention cheap
  made it cheap by making it worse. A model is not a monitor, but that is a claim we
  have to earn.
- **Build the falsifier first.** Five designs rest on one untested assumption that
  costs nothing to check.
- **Keep what school is for.** Safeguarding, socialisation, somewhere to be. These are
  not overhead.
- **Use `DESIGN` with its rule intact.** A design that cannot name what would show it
  wrong is a wish, and this document has spent 82,000 words earning the right not to
  publish wishes.

What produced the 31:1 ratio was a label set with a hole in it and a review process
that could only see one direction. Neither was rigour. Both are fixed. What remains is
the harder discipline: construction, anchored, with its own falsifier attached.


## 40. The Agenda — three experiments, and what would falsify this survey

<sub>Source report: `research/raw/F9-open-problems.md`</sub>

Two ERIC queries, run 2026-07-27:

| Query | Records |
|---|---|
| `"retention test" AND "ChatGPT"` | **0** |
| `"transfer test" AND "ChatGPT"` | **0** |

A third, `"artificial intelligence" AND "delayed posttest"`, returns seven, and
the recent entries are EFL vocabulary studies and not conceptual transfer.

So: **no adequately powered trial of an LLM tutor has measured what a learner can
do, without the AI, on novel items, four or more weeks after the intervention
ended.** Every procurement decision, every scaling decision, every roadmap in
this field is currently made on assisted or immediate outcomes.

The one study that separated them found the sign flips. In a randomised trial of
roughly 1,000 students across ~50 classrooms, assisted practice performance rose
by **+48%** for an unguarded GPT assistant and **+127%** for a hint-only tutor.
On the closed-book exam with the AI removed, the unguarded arm was **−0.054
(SE 0.022), p < .05, a 17% deficit relative to never having had access**, and
the guardrailed arm was **−0.004 (SE 0.013), not significant.**

That is the whole problem in one study. **A variable that moves an outcome from
−17% to zero is not near a ceiling; it is near a decision.** And nobody has
measured what happens six weeks later (§2).

This section lists the three experiments worth running first, each with its
design and its pre-registered falsifier, and then states at full strength the
case that this survey is wrong.

---

## Experiment 1. The delayed, unassisted, novel-item outcome

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

> Falsifier. If immediate assisted performance and 6-week unassisted
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

## Experiment 2. Persistent learner state against a stateless baseline

**Why second.** Memory is the headline feature of the current product
generation and the organising premise of every lifelong-learner-model
architecture, **including this survey's own**. It is being built at real schema
cost, real privacy exposure, and the entire regulatory surface described earlier
in this survey — on zero evidence that it changes a learning outcome. No
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

Pre-registered prediction. C > B > A, with **C − A ≈ 0.25 SD on the
prerequisite-dependent subscale and ≈ 0 on the topic-local subscale.** The
*localisation* is the real prediction; a uniform gain would indicate a confound.

Two design details carry most of the value. The control must be
summary-carryover and not a true amnesiac, or the comparison measures
politeness instead of memory. And the typed/untyped sub-ablation converts a null
into a diagnosis — because the deep obstacle is knowledge-component
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

> Falsifier. C = B = A on prerequisite-dependent transfer, with no advantage
> even on redundant-re-explanation counts, would mean persistent state is an
> engineering preference rather than a pedagogical mechanism. Given its
> privacy cost, **that finding should stop people building it.**

---

## Experiment 3. Does the guardrail that removes harm ever add benefit?

Why third, and why it is this survey's own thesis on trial. The central
design claim running through these sections is that **restraint is the active
ingredient**. The evidence for that claim is currently *entirely* about harm
removal. The guardrail took the unassisted effect from −17% to exactly zero (§2). **No
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

Pre-registered prediction. A > C by 0.15–0.25 SD, so the constrained system
beats the best cheap alternative but only modestly, and B < C. **Honest
confidence in A > C: about 55%.** That is the confidence level at which an
experiment is worth running.

> Falsifier. **A ≈ C at adequate power is the result that should change this
> survey's posture most.** It would mean the guardrailed tutor's contribution is
> the *scalability of a known-good intervention*, not a new mechanism — still
> valuable, and a completely different claim, which should then be stated in
> those words.

---

## What would falsify this survey

This survey argues that the measured **0.2–0.4 SD** band for LLM tutoring is the
floor with the brakes on; that constrained, grounded, pivoting, remembering
systems would do better; and that nobody has built the good version and measured
it. Here is the strongest case against that, stated properly and not as a
strawman. Anyone who cannot state it in this form has not earned the right to the
survey's conclusion.

**Premise 1. 0.2–0.4 SD is not a floor. It is the modal result of educational
intervention research, full stop.** It is where tutoring lands, where formative
assessment lands, where feedback lands, and where most well-implemented
instructional technology lands once the trial is adequately powered and
independently run. The regularity is not a fact about AI. It is a fact about how
much of the variance in learning outcomes is available to be moved by *any*
instructional manipulation given fixed time, prior knowledge and motivation.
**On this reading, the survey has mistaken a population parameter for a
technology limitation.**

**Premise 2. The nulls already on record are the honest prior, and they are the
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

**Premise 3. Added mechanism adds load, and the load is real while the benefit
is speculative. This is the sharpest version, and this survey's own evidence
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

**Premise 4. The mechanism the survey most relies on has a moderator that dwarfs
it. AI tutoring with teacher support: g = 1.426. Without teacher support:
g = 0.077** — approximately null. If the human is doing the work, every
architectural refinement is optimising the small term.

**Premise 5. The field's positive results degrade under scrutiny in one
direction only. Sierra Leone's unadjusted estimate (+0.216 SD, SE 0.137**) is
not significant (§3). The largest positive LLM-tutoring meta-analysis (g = 0.867) was
**retracted in 2026**. One prominent tutor was built and analysed by its first
author with no funding statement. One trial has 11 clusters. Another lost 43% of
its sample. **Where independence and rigour increase, effects shrink. That is the
signature of a literature whose true effect is smaller than its published mean.**

### What the survey says back, as reasons to test and not refutations

One: the nulls are mostly about branding and not about mechanism. Orton-Gillingham
nulls while its active ingredient, explicit systematic decoding instruction,
carries d = 0.41 to 0.55. Expanding intervals null while *scheduling retrieval at
all* carries classroom d = 0.54, with only 12 of 271 massed-versus-spaced
comparisons failing. Lesson Study nulls as a *process* while content-bearing
interventions do not. The pattern is that **the wrapper fails and the mechanism
holds**, and this survey's programme is explicitly mechanism-level.

Two: the dissociation results are sign results, not ceiling results. A
ceiling story predicts small positive effects everywhere. It does not predict
−17%, and it does not predict the same model with a different interaction policy
landing at zero in the same study (§2).

Three: the empty chair. Zero randomised trials of AI tutoring on learners
with disabilities is not a verdict. The ceiling argument cannot even be assessed
for the population where prior-knowledge, dosage and fidelity constraints bind
hardest, which is where the mechanism-level case is strongest.

---

## The concession conditions, stated in advance

We would concede that 0.2–0.4 SD is a real ceiling and not a floor, and that
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
   want run, because it tests the conjunction instead of the parts.

**If (1) and (6) both land, the correct revision is not a hedge.** It is to
rewrite the thesis as: *AI's contribution to learning is the scalable,
high-fidelity, high-dosage delivery of interventions we already knew worked, and
the design space of novel mechanisms is a distraction.*

That would still be an important and actionable finding. It would redirect the
field toward fidelity and dosage, which is what the section on
designing for the margin already argues for special education, where the
known-good intervention base is two orders of magnitude larger than the AI base.
**We say this now, in advance, so that conceding costs us nothing but a
hypothesis.**

---

## How this agenda gets run

- **Run the outcome instrument first.** Delayed, unassisted, novel-item,
  blind-scored. Report the immediate-to-delayed rank correlation as a headline
  number, because it tells everyone whether their existing evidence base means
  anything.
- **Ablate memory before building more of it.** Same model, same prompt, same
  UI, differing only in what crosses the session boundary. Split typed from
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
  hundred consented users and no new modelling work: the memory ablation, the
  gap-widening moderator, and the permutation-vs-self-consistency check, which
  needs no learners at all. A shared delayed-assessment panel is the
  infrastructure that makes the rest reportable.

The measurement gap is the widest one in applied AI: dozens of benchmarks for
whether a model is smart, roughly one field trial per organisation per year for
whether it teaches. Anyone building in this space is building without a ruler.
Waiting for someone else to supply one is not a posture this project can afford.
Build the ruler, publish the falsifier alongside the design, and be the kind of
project that would notice if it were wrong.

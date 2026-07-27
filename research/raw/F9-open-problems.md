---
title: "Open Problems — What Nobody Has Measured, and the Experiments That Would Settle It"
wave: F
date_researched: 2026-07-27
sources_count: 78
---

# F9 — OPEN PROBLEMS

> A survey that reports what is known is a literature review. A survey that states
> precisely what is *not* known, and specifies how to find out, sets an agenda.
> This section is the second kind.

---

## 0. How to read this section

**What counts as "open."** A problem earns a place here only if it survived three
filters:

1. **It is decision-relevant.** Somebody is shipping a design choice on it *right now*
   with no evidence underneath. A merely unstudied question is not interesting; an
   unstudied question that determines what gets built is.
2. **It is answerable.** Every entry carries a runnable experiment. "What is
   understanding?" is not on this list. "Does an agent that holds a false belief teach
   better than one that doesn't?" is.
3. **It was checked.** Twenty-one API queries were run against arXiv, ERIC, Europe PMC
   and Crossref on **2026-07-27** specifically to try to *kill* candidate problems by
   finding the paper that already solved them. Three candidates died that way and were
   downgraded or rewritten. Results are logged in §5 so the census is reproducible and
   falsifiable.

**Evidence labels** are as elsewhere in this project: `MEASURED-RCT` · `MEASURED-META` ·
`MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`. An absence established
by a stated, reproducible query is labelled `OBSERVED — absence`, never treated as proof
of non-existence. Abstract-and-keyword indexing misses studies that report a finding only
in a results table; every census below inherits that limit.

**The framing.** These are not complaints. Each one is an experiment somebody can run
this year, most of them cheaply, several of them at a scale a single well-instrumented
product can reach. The field's evidence base is thin in exactly the places where the
interesting designs live — which means the marginal study here is worth an order of
magnitude more than the marginal study on "does ChatGPT help students," of which there
are now hundreds.

**Power conventions used throughout.** Two-arm, individually randomised, α = .05
two-tailed, power = .80 ⇒ **n per arm ≈ 15.7/d²** (d = 0.20 → 393; 0.30 → 175; 0.40 →
99; 0.50 → 63). ANCOVA with a pre-test correlating r = .60 with the post-test multiplies
n by (1 − r²) = **0.64**. Cluster randomisation multiplies n by the design effect
1 + (m − 1)ρ; with classes of m = 25 and ICC ρ = .15 that is **4.6×**, which is why every
design below randomises individuals where the intervention permits it. These conventions
are stated once and applied without re-derivation.

---

## PART I — WHAT WE CANNOT SEE
### The measurement layer

---

### OP-1. The delayed, unassisted, novel-item outcome has essentially never been measured for LLM tutoring

**Statement.** No adequately powered trial of an LLM tutor has measured what a learner
can do, without the AI, on novel items, four or more weeks after the intervention ended.

**Why it matters.** Every deployment decision in the field — procurement, scaling,
regulatory approval, product roadmaps — is currently made on *assisted or immediate*
outcomes, and the one study that separated them found the sign flips. If the true
delayed effect of a class of systems is zero or negative, every ranking of those systems
built on immediate gains is not merely noisy but ordered wrongly.

**What we know.**
- **Bastani et al. (2025), PNAS.** ~1,000 students, ~50 classrooms, Turkey, four 90-min
  sessions ≈ 15% of the maths curriculum. Assisted practice: GPT Base **+0.137 (SE
  .031) = +48%**, GPT Tutor **+0.361 (SE .032) = +127%**. Unassisted closed-book exam:
  GPT Base **−0.054 (SE .022) = −17%, p < .05**; GPT Tutor **−0.004 (SE .013), n.s.**
  The exam is AI-removed but **same-session**; the authors state the partner school
  blocked long-term follow-up. `MEASURED-RCT` — doi:10.1073/pnas.2422633122
- **Sierra Leone (LearnLM/Fab AI, 2026).** +0.258 SD ANCOVA (95% CI 0.027–0.488,
  p = .029); **unadjusted ITT +0.216 SD, SE 0.137, not significant**; 1,763 enrolled,
  1,423 analysed; 8 weeks. **No delayed test.** `MEASURED-RCT` — AEARCTR-0016651
- **Tutor CoPilot (Stanford, 2024).** +4 p.p. on the exit ticket (p < .01); **null on
  end-of-year test.** 900 tutors, 1,800 students. `MEASURED-RCT`
- **Kestin et al. (2025).** d ≈ 0.63 on a researcher-built post-test administered
  immediately; two ~1-hour lessons; **no retention test**; first author built the tutor
  and ran the analysis. `MEASURED-RCT`
- Against this: the effect the field is trying to produce is well characterised when it
  *is* measured properly. Retrieval practice **g = 0.50** (222 studies, 48,478
  students); transfer specifically **d = 0.40, 95% CI [0.31, 0.50]** across 192 effect
  sizes / 122 experiments / N = 10,382 (Pan & Rickard 2018). `MEASURED-META`
- **Census, run 2026-07-27.** ERIC: `"retention test" AND "ChatGPT"` → **0 records**;
  `"transfer test" AND "ChatGPT"` → **0 records**; `"artificial intelligence" AND
  "delayed posttest"` → 7, of which the recent entries are EFL vocabulary studies, not
  conceptual transfer. `OBSERVED — absence`

**Why it is hard.** Not intellectually — logistically. A delayed unannounced test costs
learner goodwill, requires re-contacting a cohort that has dispersed, and produces
attrition that is almost certainly non-random (the students who show up are the ones who
learned). It is also *commercially unattractive*: it is the one measurement that can
turn a shipped product's headline number negative, and every party positioned to fund
it has an interest in the immediate number. Nigeria lost ~43% of its sample at endline
with no delay at all.

**The experiment that would settle it.**
*Population.* 900 students, grades 8–10, in a single school system with a stable roll,
one curricular unit (e.g. linear functions) that is not revisited for a full term.
*Arms* (individually randomised within class, 300 each): **(A)** guardrailed LLM tutor,
Bastani-style hint-only; **(B)** unguarded LLM assistant; **(C)** matched-time
supervised study with worked examples and no AI.
*N justification.* 300/arm detects d = 0.23 between any two arms at 80% power; with
ANCOVA on a pre-test (r ≈ .6) the detectable difference falls to **d ≈ 0.18**, below the
smallest effect anyone would act on. Budget 25% attrition at the delayed test and the
design still detects d = 0.21.
*Primary outcome.* **Unannounced, unassisted, closed-device test at 6 weeks
post-intervention**, on items the learner has never seen, drawn from the same construct
specification but a disjoint item family. Blind-scored.
*Secondary.* Immediate assisted score, immediate unassisted score, 6-week retention of
procedural vs conceptual sub-scores separately, and the immediate-to-delayed *rank
correlation across arms* — the quantity that tells us whether immediate measurement is a
usable proxy at all.
*Pre-registered prediction.* Arm A > Arm C at delay by **0.15–0.30 SD**; Arm B ≤ Arm C
at delay; and the **arm ordering at 6 weeks differs from the arm ordering at immediate
assisted test** — which is the finding that matters, because it invalidates the
measurement practice of the entire field, not just one product.

**Falsifier.** If immediate assisted performance and 6-week unassisted performance rank
the arms identically, with correlation r > .8 across a range of systems, then immediate
measurement is a valid proxy, this problem dissolves, and the field's existing evidence
base is worth far more than this survey credits it for.

---

### OP-2. The felt/real gap: nobody has built a system that learners prefer *and* that teaches

**Statement.** Every measured attempt to make learning feel better has moved preference
without moving knowledge, and no study has demonstrated a manipulation that moves both.

**Why it matters.** This is the single most consequential unknown in applied edtech,
because *preference is the only signal a product loop can cheaply observe.* Every
ratings-driven optimisation, every RLHF pass over tutoring transcripts, every A/B test
on engagement is steering on a variable that has repeatedly been shown to dissociate
from the outcome. If the two can be jointly moved, the entire industry's optimisation
apparatus is salvageable. If they cannot, it is actively counterproductive and must be
replaced with sampled outcome panels.

**What we know.**
- **Buljan et al. (2018).** Infographic vs plain-language summary, three RCTs: preference
  moved **d ≈ 0.48**, user-friendliness **d = 0.46**, and **knowledge did not move at
  all**. `MEASURED-RCT` — doi:10.1016/j.jclinepi.2017.12.003
- **Deslauriers et al. (2019), PNAS.** Students in active-learning classrooms **learned
  more and felt they learned less.** Randomised. `MEASURED-RCT` —
  doi:10.1073/pnas.1821936116
- **Bastani (above).** Practice performance **+48%**, unassisted exam **−17%**. The
  felt/real gap with an effect size and a sign flip. `MEASURED-RCT`
- **Ruffle&Riley**, an LLM learning-by-teaching conversational tutor, nulled twice —
  N = 100 (arXiv:2310.01420) and N = 200 (arXiv:2404.17460) — with **high subjective
  ratings of understanding and helpfulness in both**, and users needing *more* time.
  `MEASURED-RCT`
- **N = 214 sixth-graders**, AI-generated vs textbook materials: non-significant on
  learning outcomes, significantly better on interest, self-efficacy and reported
  cognitive load (arXiv:2412.15747). `MEASURED-RCT`
- **Pedagogical agents / avatars:** multimedia pedagogical agents **g = 0.20**
  (Castro-Alonso et al. 2021, doi:10.1007/s10648-020-09587-1), with the authors' own
  conclusion that "students may be able to learn similarly from different types of
  agents." `MEASURED-META`

**Why it is hard.** The two constructs are measured on different clocks. Preference is
available continuously, at population scale, at zero marginal cost. Knowledge is
available in a sampled panel, weeks later, at high cost, with attrition. Any experiment
that tries to move both must run the expensive measurement at every cell of the cheap
one — which is why nobody does it. There is also a *theoretical* obstacle: the
best-evidenced learning mechanisms (retrieval practice, productive failure, desirable
difficulty, spacing) are, by construction, the ones that feel worse in the moment.

**The experiment that would settle it.**
*Population.* 1,600 adult learners on a self-paced technical course with a
pre-instrumented delayed assessment.
*Design.* **2 × 2 factorial.** Factor 1 — **pedagogical core**: retrieval-heavy,
hint-only, spaced (the effective condition) vs explanation-heavy, answer-on-request
(the preferred condition). Factor 2 — **surface affordances**: high-polish
(fast response, encouraging register, visible progress, low-friction navigation,
learner-selected entry point) vs plain. 400 per cell.
*N justification.* 400/cell gives 80% power for a **d = 0.20 main effect** and, at
n = 800 per factor level, detects the **interaction** at d = 0.28 — the quantity of
interest, since the hypothesis under test is that polish can be added to an effective
core without cost.
*Primary outcomes, co-primary and both pre-registered.* (i) **4-week unassisted novel-item
transfer score**; (ii) **voluntary return rate at 4 weeks** (not satisfaction rating —
revealed preference, which is what a product actually needs).
*Pre-registered prediction.* Main effect of pedagogical core on transfer **d ≈ 0.30**;
main effect of surface affordances on return rate **d ≈ 0.40**; **interaction ≈ 0**.
That is the constructive result: polish and rigour are orthogonal, and the felt/real gap
is a consequence of confounding them, not a law.

**Falsifier.** A significant negative interaction — polish *reducing* the effectiveness
of the effective core — would mean the trade-off is real and that this survey's central
design programme (build the constrained thing and make it pleasant) is incoherent.
Equally, if the effective core produces a return rate so low that its transfer advantage
is wiped out by non-completion at the population level, the "build it rigorous" advice
fails on its own terms.

---

### OP-3. There is no agreed reliability coefficient for an assessment in which every learner sees different items

**Statement.** Cronbach's α and McDonald's ω are **undefined** — not biased, not noisy,
undefined — when items are generated per learner, and no replacement coefficient has been
computed, published, or agreed for a deployed generative assessment.

**Why it matters.** On-the-fly item generation is the flagship feature of almost every
AI-native learning product, and gating decisions (mastery, placement, credential) are
already being made on its output. Meanwhile the field's entire vocabulary for "is this
score trustworthy" assumes a fixed form. Any number currently reported as reliability
for such a system describes a different instrument than the one deployed.

**What we know.**
- α = (k/(k−1))(1 − Σσ²ᵢ/σ²ₜ) requires a fixed k and item variances estimable across
  people. If every learner sees a different item set there is **no item covariance
  matrix** — not a hard-to-estimate one, no such object. ω inherits the same structural
  requirement via its factor model. `INFERENCE` — a definitional consequence, not a
  contestable empirical claim.
- Cronbach himself supplied the exit: α "covers only a small perspective… and should be
  viewed within a much larger system of reliability analysis, **generalizability
  theory**." Cronbach & Shavelson (2004). `OBSERVED` — doi:10.1177/0013164404266386
- G-theory (Brennan 2001, doi:10.1007/978-1-4757-3456-0) decomposes score variance into
  facets and asks how a score generalises to a **universe of admissible observations**.
  A generator *is* a written-down, executable specification of exactly that universe.
  `INFERENCE`
- **Saturation is the confound nobody prices.** A narrow generator produces spuriously
  high reliability because it emits fewer effectively distinct items than it appears to
  (Cole et al. 2020, ERIC EJ1227607). `OBSERVED`
- **Census, run 2026-07-27.** ERIC: `"generalizability theory" AND "automatic item
  generation"` → **1 record**, from 2013, on retest effects across alternate forms —
  i.e. not the study. `OBSERVED — absence`
- Item-quality error rates in LLM generation span **<1% to 45%** across 71 studies
  (Kıyak et al. 2026, doi:10.1093/postmj/qgag057) — so the object being measured is
  itself highly variable. `MEASURED-META`

**Why it is hard.** A proper G-study with the **generator as a facet** requires the same
learner to be measured twice under seeded replicates from the same generator — which
means either a deliberately repeated assessment (contaminated by memory) or a
counterbalanced parallel-forms design with enough learners to estimate a
person × generator × occasion variance decomposition. It also requires the generator to
be *frozen and versioned*, which conflicts with the commercial practice of continuously
updating prompts and models. And there is a genuine identification problem: low
saturation inflates reliability and is invisible without an effective-item-count estimate
that nobody currently computes.

**The experiment that would settle it.**
*Population.* 1,200 learners, one well-specified construct (e.g. two-step linear
equations) with a published Q-matrix.
*Design.* Each learner takes **three seeded replicate forms** from the same frozen
generator π, counterbalanced in order, spaced ≥ 7 days to suppress item memory, plus one
**calibrated fixed anchor form** embedded in every session.
*Analysis.* A crossed **p × i:g × o** G-study (persons × items nested in generator ×
occasions), producing (a) **ρ_π**, a generalizability coefficient with the generator as
the universe; (b) **n_required(Φ)**, the item count needed to hit a target dependability
index; (c) an **effective-item-count / saturation estimate** reported alongside, so the
narrow-generator inflation is visible.
*N justification.* Variance-component estimation, not mean comparison. 1,200 persons × 3
occasions × ~20 items gives ≈72,000 observations; simulation work on G-study precision
puts the standard error of the person-variance component under 10% of its value at this
scale. The binding constraint is *occasions*, not persons — two occasions cannot separate
occasion from generator variance, which is why three is the minimum.
*Pre-registered prediction.* **ρ_π will come in materially below the α that the same
system would have reported** from a pilot fixed form — my estimate is ρ_π ≈ 0.70–0.78
where a pilot α of 0.85–0.90 would have been claimed — and the gap will be **largest for
the narrowest generators**, i.e. exactly the ones that look best under current practice.
*Deliverable.* The published (ρ_π, n_required(Φ), effective-item-count) triple as a
reporting standard, so a second lab can compute it on a different generator and the
numbers are comparable.

**Falsifier.** If ρ_π turns out to track a naively computed α closely across generators
of varying breadth, then the practical damage from the definitional problem is small,
current practice is roughly right by accident, and this becomes a footnote rather than a
prohibition.

---

### OP-4. No benchmark measures whether an explanation teaches a human

**Statement.** Every educational LLM benchmark scores a proxy — rubric adherence, judge
preference, solution accuracy, dialogue-act distribution — and none has been validated
against a measured human learning gain.

**Why it matters.** Model selection, fine-tuning objectives, and public leaderboards for
"educational" models are all being driven by these proxies. If the proxies do not track
learning, the field is optimising a target that is at best orthogonal to the goal, and
every capability improvement is being credited to pedagogy without warrant.

**What we know.**
- **Pedagogical ability and solving ability are only partially aligned: r = 0.421** on
  public benchmarks (arXiv:2606.16206). Model capability is *not* tutoring capability,
  and the two have now been separated empirically. `MEASURED-BENCH`
- Nine 2026 education benchmarks surveyed in this project; **all proxies**, none
  anchored to a human outcome. `MEASURED-BENCH` (own survey, D1 §5)
- **LLM judges self-prefer, causally:** self-recognition capability correlates linearly
  with self-preference strength under fine-tuning, with confounders ruled out
  (arXiv:2404.13076). Same-family judging is invalid, which removes the cheapest
  candidate anchor. `MEASURED-BENCH`
- **LLM judgements of item complexity show low ICC against trained human raters**
  (arXiv:2304.05372). `MEASURED-BENCH`
- The same hole exists one level down in the media literature: no paper in the
  LLM-generated explanatory-video corpus measures human learning gain (A2 §5), and no
  benchmark measures learning from a generated figure (C1 §8). `OBSERVED — absence`

**Why it is hard.** Anchoring a benchmark to human learning requires running a human
study *per benchmark item*, which is why nobody does it — the cost scales with the
benchmark, not with the model. The obstacle is real but not insurmountable: you do not
need to anchor every item, only enough to estimate the proxy-to-outcome mapping and its
confidence interval.

**The experiment that would settle it.**
*Population.* 2,000 learners; a bank of **120 explanation instances** — the same 40
concepts explained by three systems of deliberately different quality (a frontier model
with a pedagogy prompt, a frontier model with a bare prompt, and a deliberately weakened
system).
*Design.* Each learner is randomly assigned **6 explanations** (crossed design, ~100
learners per explanation instance), studies each, and takes an immediate and a 2-week
delayed 5-item transfer test on that concept. Every explanation instance thereby acquires
an **empirical teaching score** with a usable standard error.
*N justification.* 100 learners per instance gives an instance-level mean with SE ≈ 0.10
SD. With 120 instances, the correlation between benchmark proxy score and empirical
teaching score is estimated with 95% CI width ≈ ±0.17 around r — enough to distinguish
r = 0.2 from r = 0.6, which is the decision the field needs.
*Primary outcome.* **The correlation between each existing proxy metric and the empirical
teaching score**, computed at the instance level, disattenuated for measurement error.
*Pre-registered prediction.* Judge-preference proxies will correlate with delayed
teaching score at **r ≈ 0.2–0.4** (i.e. in the same weak band as the already-measured
pedagogy-vs-solving r = 0.421), while a proxy built from *learner-response features*
(does the explanation force a retrieval attempt; does it withhold; does it check) will
correlate substantially higher. That result would hand the field a cheap benchmark that
is actually anchored.
*Deliverable.* A released, permanently-anchored benchmark subset — 120 explanations with
human teaching scores attached — that any future metric can be validated against for free.

**Falsifier.** If existing judge-based proxies correlate with delayed teaching score at
r > 0.7, the benchmarks are fine, the leaderboards mean what they claim, and this problem
was a false alarm.

---

### OP-5. Personalisation-induced differential item functioning has never been measured

**Statement.** When an item generator conditions item content on a learner's interests,
locale, or context — the flagship selling point of personalised assessment — it can
introduce construct-irrelevant difficulty variance correlated with demographics, and no
study has measured whether it does.

**Why it matters.** Item-level DIF analysis is routine, cheap, and legally load-bearing
in high-stakes testing. It is also **undefined** when every learner receives distinct
items. What must be demonstrated instead is **generator invariance** — that the
generation policy yields equivalent difficulty distributions across subgroups. No
deployed system reports it, and the failure mode is invisible to every existing fairness
procedure *and defended as a feature*.

**What we know.**
- The scoring-side fairness literature is mature: automated essay scoring carries
  measurable accuracy-fairness trade-offs (Huang et al. 2026,
  doi:10.1016/j.asw.2026.101047). The generation side has had **no comparable
  scrutiny**. `OBSERVED`
- Closest published work: Falcão et al. (2024), ERIC EJ1416068 — a single study, one
  language. `MEASURED-BENCH`
- Every published machine item-screener is evaluated on items from the same model family
  that generated them (Gorgun & Bulut 2025, ERIC EJ1460469). **Cross-family screening is
  untested**, so the screener that would catch this is itself uncalibrated.
  `OBSERVED`
- Related and directionally alarming: trace-based learner models **do not generalise
  across national populations** (Finland / Slovakia / US, PIAAC 2012; ERIC EJ1501422)
  `MEASURED-BENCH`; dialect prejudice is present in model decisions (arXiv:2403.00742)
  and **prompt-level mitigation barely works** — activation steering reduced bias "5 to
  20 times more than prompting" (arXiv:2607.06845) `MEASURED-BENCH`.
- **Census, run 2026-07-27.** ERIC: `"differential item functioning" AND "large language
  model"` → **1 record** (2023, on speaking-assessment bias mitigation, not item
  generation). `OBSERVED — absence`

**Why it is hard.** Three obstacles compound. (i) The unit of analysis has to move from
the item to the **generator**, and the psychometric machinery for generator-level
invariance testing barely exists. (ii) Measuring subgroup effects requires collecting the
demographic data that privacy-first design correctly minimises — a real tension, not a
rhetorical one. (iii) The personalisation itself is the treatment, so you cannot hold it
constant and still study it; you need randomly equivalent groups created *by seed
assignment*, which requires the generator to be instrumented for it from the start.

**The experiment that would settle it.**
*Population.* 3,000 learners across at least three subgroups defined on a dimension the
personaliser conditions on (e.g. stated interest domain, locale, home language), with
consented, minimised demographic capture.
*Arms.* Within-subject: each learner receives, in counterbalanced order, **(A)** a
personalised generated form and **(B)** a neutral-context generated form from the same
generator with the personalisation channel ablated, plus **(C)** a common calibrated
anchor form embedded in both.
*N justification.* DIF detection with adequate power needs roughly **200–500 per focal
group** per item family at the effect sizes that matter (moderate DIF, ETS category B/C);
1,000 per subgroup across three subgroups is comfortable and permits family-level rather
than item-level estimation.
*Primary outcome.* **Difference in anchor-equated difficulty between personalised and
neutral forms, by subgroup** — i.e. a generator-level invariance statistic, reported as
the subgroup × personalisation interaction on equated θ.
*Pre-registered prediction.* Personalisation will shift equated difficulty by **0.10–0.25
logits differentially across subgroups**, concentrated in items whose personalised
context carries unequal familiarity — small enough to be invisible in aggregate accuracy,
large enough to matter at a cut score.
*Deliverable.* A **generator-invariance reporting template**: the personalised-vs-neutral
equated-difficulty gap by subgroup, published alongside ρ_π from OP-3.

**Falsifier.** A tight null — personalisation shifting equated difficulty by < 0.05
logits with no subgroup interaction — would mean personalised generation is fairness-neutral
by construction, which would be genuinely excellent news and worth publishing loudly.

---

## PART II — WHAT NOBODY HAS BUILT AND MEASURED
### The mechanism layer

---

### OP-6. Persistent learner state has never been measured against a stateless baseline

**Statement.** No trial has compared a tutor that remembers a learner across sessions
against the identical tutor that does not.

**Why it matters.** "Memory" is the headline feature of the current product generation
and the organising premise of every lifelong-learner-model architecture, including this
survey's own. It is being built at enormous cost — schema design, privacy exposure,
regulatory burden, the entire inBloom risk surface — on **zero** evidence that it changes
a learning outcome. This is the cleanest, highest-leverage ablation available in the
field, and it has never been run.

**What we know.**
- **The feature is not new and was not invented by LLMs.** Runestone has had full event
  logging, per-student progress, and an analytics portal since before LLMs. The ITS stack
  built this a decade ago; the LLM stack discarded it when it went serverless.
  `OBSERVED`
- **arXiv census (this project):** `"open learner model"` → 0; `"long-term learner
  model"` → 0; `"knowledge tracing" AND "large language model"` → 45, essentially all
  about *predicting* knowledge state on benchmarks (SINKT, CIKT, LLM-KT, MERIT), **none
  about persisting and reusing state across multi-session deployments with a measured
  benefit.** GitHub `learner model knowledge tracing memory LLM tutor` → **0 repos**.
  `OBSERVED — absence`
- **Replicated 2026-07-27.** arXiv `abs:"long-term memory" AND abs:"tutor"` → **0
  results**. `abs:"memory" AND abs:"tutoring system" AND abs:"large language model"` →
  **6 results**, all system papers (persona/memory/forgetting-aware tutoring, LECTOR,
  Sakshm AI, chained-LLM private tutoring); **none contains a memory-ablation arm.**
  `OBSERVED — absence`
- **The prediction ceiling is already reached, which sharpens the question.** A
  zero-parameter moving-average baseline beats every released FSRS version on log loss
  over 350M reviews; cleaned of leakage, PFA matches DKT; IRT variants match or beat DKT
  on all tested datasets; SAKT fails independent replication on all nine
  (0.85 reported → 0.73 observed). `MEASURED-BENCH` — F5 §1–2. So the case for memory
  cannot be "better next-item prediction." It has to be continuity, diagnosis, and
  pivoting — none of which AUC measures, and none of which anyone has measured either.
- Two hobbyist agent-skill implementations (`Flagrare/llm-tutor` with atomic-write
  `state.json`; `TovTechOrg/Tov-learn` with an append-only per-lesson learner model)
  appeared within ten weeks, 39 stars combined, **zero evaluation**. `OBSERVED`

**Why it is hard.** Three real obstacles. (i) **Duration** — a memory effect cannot
appear inside a single session, so the trial must run ≥ 8 sessions over ≥ 6 weeks, which
is where attrition eats designs. (ii) **The ablation is not clean by default**: a
stateless arm loses not only memory but conversational coherence, so the control must be
a *summary-carryover* arm rather than a true amnesiac, or the comparison measures
politeness. (iii) **The KC alignment problem** — the deep obstacle. There is no adequate
public knowledge-component vocabulary: expert KC models add **≤ 0.01 AUC on 7 of 9
datasets**, and on 4 of 9 the KC model is so poor that a skill-only model loses to an
item-difficulty-only model (Gervet et al.). `MEASURED-BENCH` A memory whose contents are
badly typed may be worth exactly nothing, and that is a mechanism-level reason the effect
could be null.

**The experiment that would settle it.**
*Population.* 600 learners, 12 sessions over 8 weeks, one multi-topic curriculum
(introductory statistics is ideal — many interlocking prerequisites, high misconception
density).
*Arms* (individually randomised, 200 each), **identical model, identical prompt,
identical UI, differing only in what crosses the session boundary**:
 - **A — Stateless.** No carryover.
 - **B — Transcript carryover.** Prior session summaries in context. (This is what most
   "memory" products actually are.)
 - **C — Structured learner state.** Typed per-KC mastery estimates, an explicit
   misconception register, channel constraints (reading load, attention window), and a
   pivot history — inspectable and correctable by the learner.
*N justification.* 200/arm detects d = 0.28 at 80% power; with ANCOVA on a pre-test the
detectable difference is **d ≈ 0.22**. This matters: the honest prior for this effect is
*small*, and a study powered only for d = 0.5 would produce an uninterpretable null.
*Primary outcome.* **Delayed (4-week) unassisted transfer across topics** — specifically
on items requiring a prerequisite established in an *early* session and applied in a
*late* one, which is the only place a memory effect can mechanistically show up.
*Secondary and diagnostic.* Number of redundant re-explanations of already-mastered
material; time-to-first-correct on prerequisite-dependent items; **learner corrections of
the visible state** (a direct test of the bidirectional-loop premise); and a
**pre-registered ablation of arm C into C-typed vs C-untyped**, which converts a null
into a diagnosis of the KC alignment problem rather than a verdict on memory.
*Pre-registered prediction.* C > B > A, with **C − A ≈ 0.25 SD** on the
prerequisite-dependent subscale and **≈ 0 on the topic-local subscale**. The
localisation of the effect is the real prediction; a uniform gain would suggest a
confound.

**Falsifier.** C = B = A on prerequisite-dependent transfer, with no advantage even on
redundant-re-explanation counts, would mean persistent state is an engineering
preference rather than a pedagogical mechanism — and given its privacy cost, that finding
should stop people building it.

---

### OP-7. Nobody has built a teachable agent that can actually stay wrong

**Statement.** No system deliberately installs a specific false belief in an agent and
holds it under pressure until the learner corrects it, and therefore nobody has measured
whether error-holding is what makes learning-by-teaching work.

**Why it matters.** Learning by teaching is one of the largest well-replicated effects in
the corpus (**g = 0.56**, robust at delay) and is essentially undeployed. The mechanistic
story — recursive feedback, ego-protected error confrontation, the need to *diagnose* a
tutee — requires a genuine non-knower. Every commercial model is trained to be a knower.
If error-holding is the active ingredient, the entire teachable-agent product category is
currently shipping a decoration; if it is not, the category can be built on prompting and
scaled tomorrow.

**What we know.**
- **The failure mechanism is documented.** LLMs *prompted* to act like novices **drift
  back to expert-level correct answers** during the interaction; the authors reach for
  **machine unlearning** to produce a stably novice tutee, evaluated on a Python MCQ set
  (arXiv:2603.26142). This is *suppression of knowledge*, not *insertion of a specific
  error* — the nearest existing work, and it stops short. `MEASURED-BENCH`
- **Learning-by-teaching with ChatGPT** improved knowledge gains and code quality but
  **not error-correction skill**, explicitly "because ChatGPT tends to generate correct
  code, reducing opportunities to practice debugging" (arXiv:2412.15226). `OBSERVED`
- The agent's "expansive knowledge… discourages learners from teaching"
  (arXiv:2309.14534). `OBSERVED`
- **MathDial** (arXiv:2305.14536): 3k dialogues with an LLM prompted to represent common
  student errors — scripted wrongness at dataset scale, not live error-holding.
  `MEASURED-BENCH`
- **The warning.** Where LLM learning-by-teaching *has* been tested at reasonable power —
  Ruffle&Riley, N = 100 then N = 200 — it **nulled both times** on learning gain while
  scoring high on subjective ratings. `MEASURED-RCT`
- **Census, run 2026-07-27.** arXiv `abs:"teachable agent"` → **18 results total**; the
  2025–2026 entries are student-error simulation, unlearning-based novice simulation, a
  36-participant within-subject comparison of tutoring vs teaching (Chrysalis,
  arXiv:2510.05271), and a 28-participant music-theory study (arXiv:2504.00636). Europe
  PMC `"teachable agent" AND "randomized"` → **0 hits**. **No study installs and defends
  a specific false proposition.** `OBSERVED — absence`

**Why it is hard.** Error-holding appears to be a **weight-level or architecture-level
property, not a prompt-level one** — which is precisely why the one team that took it
seriously reached for machine unlearning. A system prompt decays mid-session. It is also
genuinely risky: an agent that defends a falsehood convincingly is, viewed from another
angle, a misinformation generator, and it must never leak outside the teaching frame.
And the belief has to be *specific and diagnosable* — "be a novice" is not a
manipulation, "believe that heavier objects fall faster and defend it with a plausible
mechanism" is.

**The experiment that would settle it.**
*Population.* 480 undergraduates, introductory mechanics; six misconceptions drawn from
the FCI's attested error set (so the wrong beliefs are real ones, not invented ones).
*Arms* (individually randomised, 160 each):
 - **A — Error-holding tutee.** A model whose weights have been edited (unlearning +
   targeted belief insertion) to hold one specific attested misconception per topic, with
   a **held-belief persistence check** logged every turn.
 - **B — Prompted-novice tutee.** Identical interface; the misconception is specified in
   the system prompt only. This arm doubles as the *measurement* of drift.
 - **C — Standard tutor.** Same content, agent explains to the learner.
*N justification.* 160/arm detects d = 0.31 at 80% power. Given that the adjacent
paradigm has **already nulled twice at N = 100 and N = 200**, this study must be powered
for a genuinely modest effect, and the A-vs-B contrast — the one that isolates
error-holding from teaching-as-such — is the contrast that needs the power.
*Primary outcome.* **FCI-derived delayed (3-week) conceptual gain**, plus a
misconception-specific subscale on the exact beliefs the tutee held.
*Instrumented mediator, and this is the point of the design.* **Belief persistence** —
the proportion of turns on which the tutee still asserts the installed error before
correction. If arm B's persistence decays across the session (the predicted drift) and
arm A's does not, the study yields a **dose-response relationship between persistence and
learning gain** even if the arm contrast is modest.
*Pre-registered prediction.* Belief persistence: A ≈ 0.9, B ≈ 0.4 and falling. Learning:
**A > C by ≈ 0.3 SD**; **B ≈ C**; and persistence correlates with gain at **r ≈ 0.4**
across all learners in arms A and B pooled.

**Falsifier.** If arm A ≈ arm B on learning despite a large, clean separation in belief
persistence, then error-holding is *not* the active ingredient in learning by teaching,
the effect is carried by the act of explaining alone, and the whole engineering programme
of weight-level tutee construction is unnecessary — a genuinely useful, cost-saving null.

---

### OP-8. Deixis — an AI pointing at a shared referent — is unbuilt for tutoring and unmeasured

**Statement.** Nobody has built a tutoring system in which the AI points at a specific
element of a shared visual field while talking about it, and nobody has measured what
that does to learning.

**Why it matters.** Deixis — "*this* term, *that* bracket, the one *here*" — is one of
the most ordinary things a human tutor does and one of the most load-bearing: it collapses
the referential ambiguity that otherwise consumes working memory. Every live multimodal
stack now *sees* and *talks*; the pointing layer between them does not exist, and no
vendor supplies it. This is the clearest case in the survey of a capability gap that is
purely one of assembly.

**What we know.**
- **arXiv census (this project):** `"referring expression" AND "tutor"` → 0; `"pointing"
  AND "multimodal tutor"` → 0; `"gaze" AND "tutoring"` → 7, none about an AI pointing at
  shared content. GitHub: `AI tutor whiteboard pointing` → **0 repos**; `screen share
  tutor LLM` → **0**; `multimodal tutor pointing gesture` → **0**; `shared canvas AI
  tutor` → 2. `OBSERVED — absence`
- **Replicated and refined 2026-07-27.** arXiv `abs:"deictic" AND abs:"tutor"` → **0**.
  `abs:"referring expression" AND abs:"education"` → **1**: *Toward an Artificial General
  Teacher: Procedural Geometry Data Generation and Visual Grounding with Vision-Language
  Models* (arXiv:2604.02893). **This is the closest thing that exists and it is worth
  stating precisely**: it treats visual explanation in geometry as referring-image
  segmentation, builds a procedural engine emitting **200,000+ synthetic geometry diagrams**
  with pixel-perfect masks and diverse referring expressions, and reports a fine-tuned
  Florence-2 at **49% IoU / 85% buffered IoU**, against **< 1% IoU zero-shot**.
  `MEASURED-BENCH`
- The learning-science warrant is strong and old: split-attention and spatial-contiguity
  effects are among the best-replicated multimedia findings, and deixis is the dynamic
  form of spatial contiguity. `MEASURED-META` (Mayer principles, B1)

**Why it is hard.** It was hard; it is now mostly *unattempted*. The honest technical
obstacles are (i) grounding accuracy on the messy, hand-drawn, partially-occluded artifacts
learners actually produce — the 49%/85% figure is on **synthetic** diagrams; (ii) latency,
since a pointer that lags the speech is worse than no pointer; and (iii) evaluation, since
"did the pointing help" needs a control that holds the *words* constant while removing the
*pointing*, which requires the informationally-equivalent-control discipline that this
literature has never adopted.

**The experiment that would settle it.**
*Population.* 400 students, grades 9–11, geometry — the domain where the grounding model
already exists.
*Arms* (individually randomised, 200 each), **speech held identical between arms by
construction — the same generated utterance script is played in both**:
 - **A — Deictic.** The system highlights/points at the referenced element in the shared
   canvas, synchronised to the utterance, within 200 ms.
 - **B — Non-deictic.** Identical audio; the referent is described verbally
   ("the angle at the top-left of the triangle"); no highlight.
*N justification.* 200/arm detects **d = 0.28**; ANCOVA on a spatial-ability and
prior-geometry pre-test brings it to **d ≈ 0.22**. Spatial-contiguity effects in the
multimedia literature typically run d ≈ 0.4–0.8, so this is comfortably powered, and a
null would be informative rather than ambiguous.
*Primary outcome.* Immediate and 2-week transfer on novel geometric configurations.
*Secondary, and the mechanistically interesting one.* **Referential repair rate** — how
often the learner asks "which one?" or points at the wrong element — plus subjective
cognitive load (Paas scale). If deixis works through referential-ambiguity reduction, the
repair rate must fall, and it must fall more for learners with lower spatial ability.
*Pre-registered prediction.* Transfer **d ≈ 0.35** in favour of the deictic arm;
referential repair rate roughly **halved**; and a **significant interaction with spatial
ability**, deixis helping low-spatial learners more — which is the H1 curb-cut argument in
testable form.

**Falsifier.** No transfer difference *and* no reduction in referential repairs would mean
verbal description is sufficient at the granularity tutoring actually operates at, and
that the pointing layer is a nicety rather than a mechanism.

---

### OP-9. Does a village of agents beat one well-prompted agent at matched compute?

**Statement.** No study has compared a multi-agent educational system against a
**token-matched** single agent on a human learning outcome.

**Why it matters.** The society-of-specialists architecture — subject experts,
diagnostician, assessor, devil's advocate, librarian — is the reference architecture in
this survey and in a growing share of the field. Its entire justification rests on
benchmark results from non-educational domains, several of which point the other way, and
on an uncontrolled confound: multi-agent systems consume far more compute than the
baselines they beat.

**What we know.**
- **Token usage is the dominant explanatory variable.** "Token usage by itself explains
  80% of the variance" on BrowseComp; three factors explained 95%. `VENDOR` — but the
  direction is corroborated widely. This is the confound: *any* claim that role
  specialisation helps must be tested against a token-matched single-agent baseline, and
  **no published education multi-agent system has done this.**
- **Mixing models can reduce ensemble quality.** Self-MoA (single best model,
  self-aggregated) beat mixed Mixture-of-Agents: **+6.6% AlpacaEval 2.0, +3.8% average**
  (arXiv:2502.00674). `MEASURED-BENCH`
- **Debate does not reliably beat self-consistency.** Three independent benchmark
  results converge: Smit et al., "Should we be going MAD?" (arXiv:2311.17371); Wang et
  al., "Rethinking the Bounds of LLM Reasoning" (arXiv:2402.18272); Becker et al.,
  "Problem Drift in Multi-Agent Debate" (arXiv:2502.19559). `MEASURED-BENCH`
- **Coordination failure is the dominant failure mode and it is catalogued**: MAST, 14
  failure modes, 1,600+ traces, 7 frameworks, κ = 0.88 (arXiv:2503.13657).
  `MEASURED-BENCH`
- **The one genuinely pro-village result is about the human, not the machines.** Khan et
  al.: **+28 percentage points** for human non-expert judges evaluating a *two-sided
  debate* rather than a single advocate. That is a result about the learner's epistemic
  position — which is exactly the mechanism a village should be built to exploit.
  `MEASURED-BENCH`
- **The measured education multi-agent literature is uniformly demo-grade**: IntelliCode
  (simulated learners), CodeEdu (platform metrics), SimClass (interaction-analysis
  frameworks, not learning gains), ParLD (state-prediction accuracy), FairTutor
  (benchmark proxy). **Not one measures a delayed, novel-item human learning outcome
  against a single-agent control.** `DEMO` / `OBSERVED`
- **Census, run 2026-07-27.** arXiv `abs:"multi-agent" AND abs:"classroom" AND
  abs:"learning gains"` → **0**. Europe PMC `"intelligent tutoring" AND "multi-agent"` →
  4, all architecture papers. `OBSERVED — absence`

**Why it is hard.** Matching compute is the whole difficulty and it is fiddly: you must
give the single-agent arm the *same* token budget, which in practice means extended
reasoning, self-critique passes, and multiple drafts — i.e. the single agent must be
allowed to be as expensive as the village. Most published comparisons quietly compare a
lavish village to a thrifty solo agent. There is also a **selection-versus-synthesis**
confound: village gains may come from having a judge pick among candidates rather than
from role specialisation at all, and the two must be separated.

**The experiment that would settle it.**
*Population.* 600 learners, 10 sessions, one curriculum with both procedural and
conceptual demands.
*Arms* (individually randomised, 150 each), **all four matched on total tokens per
learner-session within ±10%**:
 - **A — Single agent, thrifty.** The honest floor.
 - **B — Single agent, token-matched.** Same tokens as the village, spent on extended
   reasoning and self-critique.
 - **C — Village, role-specialised, single writer.** Orchestrator + diagnostician +
   subject expert + assessor, one integration point, one shared learner state.
 - **D — Village with an explicit two-sided disagreement surfaced to the learner.**
   Same roles, but when specialists disagree the learner adjudicates — the Khan et al.
   mechanism, operationalised.
*N justification.* 150/arm detects d = 0.32 pairwise at 80%; the pre-planned contrasts
are **C vs B** (does structure beat compute?) and **D vs C** (does surfacing
disagreement beat resolving it silently?), each of which is the one that carries the
design decision.
*Primary outcome.* 4-week unassisted transfer.
*Secondary.* Contradiction rate across agents as observed by the learner; MAST-coded
coordination failures per session; and learner calibration (Brier score on
confidence-tagged answers), which is where the debate mechanism should show up.
*Pre-registered prediction.* **C ≈ B** — i.e. role specialisation buys little once
compute is matched — while **D > C by ≈ 0.25 SD** on calibration and ≈ 0.15 SD on
transfer. If that pattern holds, the village's value is not in the division of labour but
in **making disagreement visible to the learner**, which is a completely different and
much cheaper architecture.

**Falsifier.** C > B by a clear margin on transfer at matched tokens would vindicate role
specialisation on its own terms and make the village architecture the default. C ≈ B ≈ D
would mean the whole village programme is compute in a costume.

---

### OP-10. The pivot rule: what signal triggers a change of method, and how long must you wait?

**Statement.** Nobody knows the correct latency or trigger for changing instructional
method in response to non-response, and the only calibrated evidence comes from a
weekly-probe regime that AI systems have already blown past by two orders of magnitude in
data density.

**Why it matters.** "Detect non-response and change approach" is the architectural centre
of the bidirectional loop in this survey and of every adaptive-instruction claim in the
market. Most AI tutors re-explain the same way with more words; the ones that do adapt
adapt on no principled rule at all. **Too fast is as harmful as too slow** — method-thrash
prevents any method from consolidating — and the field has a number for "too slow" and no
number for "too fast."

**What we know.**
- **Measurement without a decision rule does not work.** Fuchs, Hamlett & Stecker (1991),
  33 teachers randomised to three conditions over 20 weeks: **both** CBM groups revised
  programmes more often, but only **CBM plus an expert system that told teachers what to
  change** produced superior achievement. `MEASURED-RCT` — the single most
  architecturally load-bearing finding for any adaptive system.
- Systematic formative evaluation overall: **ES = 0.70** across 21 controlled studies /
  96 effect sizes, moderated by **how** data were used, not merely that they were
  collected (Fuchs & Fuchs 1986). `MEASURED-META` — doi:10.1177/001440298605300301
- **The "too fast" bound, such as it is.** CBM trend-line decision rules are **not viable
  until 7–10 weeks of weekly data** (Van Norman et al. 2023). An AI tutor that changes
  method after two wrong answers is operating far inside the noise floor.
  `MEASURED-BENCH`
- Review-scale confirmation that the active ingredients are **systematic data-based
  decision rules, skills-analysis feedback, and explicit modification recommendations**
  (Stecker, Fuchs & Fuchs 2005, doi:10.1002/pits.20113). `MEASURED-META`
- Nothing in this evidence base was collected under a regime that observes **hundreds of
  responses per hour** with latency, error-type, and hesitation traces. Whether the 7–10
  week bound is about *weeks* or about *number of independent observations* is unresolved
  and consequential. `INFERENCE`

**Why it is hard.** The quantity of interest is a **policy**, not a treatment, so the
experiment must randomise policies rather than content. Policies interact with the
learner's trajectory, which makes the analysis sequential rather than cross-sectional.
And there is a definitional trap: "changing method" must be operationalised precisely
(representation, granularity, modality, pacing, prerequisite level) or the manipulation
is unfalsifiable.

**The experiment that would settle it.**
*Population.* 800 learners, 16 sessions over 10 weeks, a curriculum with a documented
prerequisite DAG.
*Arms* (individually randomised, 200 each) — **pivot latency**, holding the pivot
*repertoire* identical:
 - **A — Fast.** Pivot after 2 consecutive errors on a KC.
 - **B — Medium.** Pivot after 4 consecutive points below the goal line (the DBI rule,
   transposed to per-item granularity).
 - **C — Slow.** Pivot only on a trend-line rule with ≥ 20 observations.
 - **D — No pivot.** Re-explain in the same modality (the industry default).
*Secondary factor, half-crossed into arms A–C.* Pivot **trigger**: accuracy-only vs
accuracy + error-*type* classification. The second is the one this survey believes in and
the one nobody has isolated.
*N justification.* 200/arm detects **d = 0.28** pairwise; the pre-planned contrast is the
**quadratic trend across A → B → C**, for which the effective N is 600 and the
detectable curvature corresponds to d ≈ 0.20 between the best and worst latency.
*Primary outcome.* 4-week delayed unassisted transfer, plus **KCs mastered per hour** as
a co-primary (a policy that helps transfer while destroying throughput is not obviously a
win).
*Secondary.* Method-thrash index (pivots per KC); proportion of pivots that were
*reversed* within two sessions; and the learner-visible-state correction rate.
*Pre-registered prediction.* An **inverted-U in latency with the optimum near B** —
faster than the 7–10 week CBM bound because the observation density is ~100× higher, but
far slower than the two-error trigger products currently ship. And **error-type triggers
beat accuracy-only triggers by ≈ 0.2 SD**, because "wrong" is not a diagnosis and the
pivot target should be a function of *which* wrong.

**Falsifier.** A flat response across latencies A–C would mean pivot timing does not
matter and only the pivot *repertoire* does — which would simplify every adaptive
architecture in the field. D outperforming all pivoting arms would be a much larger
result: it would say re-explanation persistence beats method-switching, and would
invalidate the bidirectional loop as designed.

---

### OP-11. Does the guardrail that removes harm ever *add* benefit?

**Statement.** The guardrail in the one trial that measured it took the unassisted effect
from **−17% to zero**, and no study has ever shown a constrained tutor beating a
no-AI control on a delayed unassisted outcome.

**Why it matters.** This survey's central design claim is that **restraint is the active
ingredient**. The evidence for that claim is currently *entirely* about harm removal. If
restraint only ever gets you back to baseline, then the honest headline is "AI tutoring
is safe when guardrailed," not "AI tutoring works" — and the whole constrained-system
programme needs a different justification.

**What we know.**
- **Bastani et al. (2025).** GPT Tutor (hint-only, no direct solutions) unassisted exam
  coefficient: **−0.004 (SE 0.013), not significant.** Versus GPT Base at −0.054 (SE
  0.022), p < .05. The guardrail removed a harm and produced **no measurable benefit over
  the no-AI control.** `MEASURED-RCT`
- The positive field results *do* exist but are all against weak or absent counterfactuals
  and without delay: Sierra Leone +0.258 SD ANCOVA (unadjusted +0.216, n.s.), Nigeria
  +0.310 SD composite / +0.206 SD on the school's own exam with ~43% attrition, Rori
  +0.37 SD with only 11 clusters. `MEASURED-RCT` ×3
- **The strongest moderator in the LLM meta-analytic literature cuts the same way.** Gu &
  Yan (2025): overall **g = 0.683**; **with teacher support g = 1.426; without teacher
  support g = 0.077 (≈ null)**. `MEASURED-META` The AI's measured effect without a human
  in the loop is approximately zero.
- The largest positive LLM-tutoring meta-analysis (g = 0.867) was **retracted in 2026**
  for discrepancies in the meta-analysis. `MEASURED-META` [RETRACTED]
- **Census, run 2026-07-27.** Europe PMC `"guardrails" AND "learning" AND "randomized"` →
  **0 hits**. Bastani has not been replicated. `OBSERVED — absence`

**Why it is hard.** The comparison needs a **no-AI active control** that is matched on
time, attention, and materials — not "business as usual," which confounds the AI with the
extra hour. Almost every deployment trial in the corpus adds the AI *on top of* normal
instruction, which makes the AI arm strictly advantaged and the resulting effect
uninterpretable as evidence about the AI.

**The experiment that would settle it.**
*Population.* 900 students, matched-time design, one curricular unit, single school
system.
*Arms* (individually randomised, 300 each, **all receiving identical total instructional
time**):
 - **A — Guardrailed AI tutor** (hint-only, withholds solutions, requires a reasoning
   attempt before help).
 - **B — Unguarded AI assistant.**
 - **C — Matched-time worked examples + retrieval practice, no AI** — i.e. the best
   cheap thing we already know works.
*N justification.* 300/arm detects **d = 0.23**; the decisive contrast is **A vs C**, and
the pre-registered smallest effect of interest is **d = 0.20**, below which the guardrail
programme should not claim a benefit.
*Primary outcome.* 6-week unassisted novel-item transfer.
*Secondary.* Help-seeking behaviour after AI removal; a **dependency probe** (does arm A
attempt fewer unaided problems in a later, unrelated unit?); and gap-widening by
prior-knowledge quartile (see OP-15).
*Pre-registered prediction.* **A > C by 0.15–0.25 SD** — the constrained system beats the
best cheap alternative, but modestly — and **B < C**. My honest confidence in A > C is
about 55%, which is exactly why the study is worth running.

**Falsifier.** **A ≈ C** at adequate power is the result that should change this survey's
posture most. It would mean the guardrailed tutor's contribution is *scalability of a
known-good intervention*, not a new mechanism — still valuable, but a completely
different claim, and one that should be stated in those words.

---

### OP-12. "Grilling" — adversarial prior-knowledge diagnosis — has never been tested as a named intervention

**Statement.** No study evaluates a deliberately adversarial diagnostic interrogation at
the start of instruction, as a distinct construct, with an AI.

**Why it matters.** Four independent literatures converge on it — pre-testing effects,
misconception elicitation, the expertise-reversal effect, and retrieval-based
diagnosis — and it is the intervention this survey identifies as having the highest
expected value per unit of engineering effort. It is also the mechanism that makes every
downstream personalisation decision (entry level, pivot target, scaffold density) rest on
measurement rather than on preference. If grilling does not work, the adaptive-entry
premise of F10's laddering and H1's bidirectional loop both lose their foundation.

**What we know.**
- **No study evaluates "grilling" as a named construct with an AI.** `OBSERVED — absence`
  (F2 §6)
- The component literatures are strong. Pre-testing and retrieval-based diagnosis sit
  inside the retrieval-practice base (**g = 0.50**, 222 studies, 48,478 students);
  productive failure is **g = 0.36**, rising to **0.58** at high implementation fidelity.
  `MEASURED-META`
- The expertise-reversal effect makes the *consequence* of bad diagnosis concrete: an
  explanation matched to the wrong level actively harms. `MEASURED-META` (F10 §R2)
- **Level selection must be driven by measured prior knowledge, never by preference** —
  and preference is exactly what moves (d ≈ 0.48) when knowledge does not (OP-2).
  `MEASURED-RCT`
- The redirection matters and is already settled in this project: grilling must diagnose
  **prior knowledge and misconceptions**, not "learning style," for which there is no
  credible crossover evidence. `MEASURED-META` (Pashler et al.; F5 §5.2)

**Why it is hard.** Grilling is aversive. The anxiety archetype in H1 says prior failure
history is itself a barrier and errors are threatening; an adversarial opening is exactly
the wrong move for a subset of learners, and possibly a large one. So the experiment
cannot just measure whether grilling improves routing — it must measure whether the
routing gain survives the **dropout** it causes. That is a composite outcome, and
composite outcomes are where studies go to become uninterpretable unless the analysis is
specified in advance.

**The experiment that would settle it.**
*Population.* 800 learners entering a multi-level technical curriculum with genuinely
heterogeneous prior knowledge (the population where routing has something to do).
*Arms* (individually randomised, 200 each):
 - **A — Grill.** 10-minute adversarial diagnostic: retrieval-based probes, deliberate
   near-miss traps drawn from an attested misconception taxonomy, requests to predict and
   justify before being told.
 - **B — Conventional pre-test.** Same duration, same construct coverage, non-adversarial
   multiple-choice.
 - **C — Self-report entry.** Learner picks their own level (the industry default).
 - **D — No diagnosis.** Fixed entry at the curriculum's nominal level.
*N justification.* 200/arm detects **d = 0.28**. The pre-registered primary contrast is
**A vs C**, which is the design decision every product faces on day one.
*Primary outcome (composite, specified in advance).* **Delayed unassisted transfer,
analysed intention-to-treat with dropouts scored at their last observed level** — so
that a routing gain purchased with attrition cannot masquerade as a win.
*Secondary.* Routing accuracy (assigned level vs level implied by a blind post-hoc expert
assessment); session-1 dropout; self-efficacy at session 1 and session 5; and a
pre-specified **interaction with baseline anxiety and prior-failure history**, because
that is where the harm, if any, will live.
*Pre-registered prediction.* **A > B > C ≈ D** on transfer, with **A − C ≈ 0.3 SD**; and
**A showing 5–10 percentage points higher session-1 dropout**, concentrated in the
high-anxiety stratum — which, if it replicates, immediately generates the follow-up
design (grill *after* an early success rather than before).

**Falsifier.** A ≈ B would mean adversarial framing adds nothing over a plain pre-test and
the cheap thing is sufficient. A < C on the ITT composite would mean grilling's routing
gain does not survive its own aversiveness, and the intervention should not ship in that
form.

---

### OP-13. Laddering as such — one concept at multiple altitudes, simultaneously — has never been tested

**Statement.** No study tests rendering the *same* concept at several sophistication
levels held as a navigable library, against a single level matched to the learner.

**Why it matters.** Explanation-depth laddering is a named primitive of this survey and is
being built into products as a differentiator. Its component evidence (concreteness
fading, spiral curriculum, adaptive entry) is about **sequences over time**, not about
**simultaneous availability**. Those are different interventions with different cognitive
consequences — simultaneous availability adds navigation cost and a selection decision
that the learner may make badly, exactly as they do with self-reported level (OP-12).

**What we know.**
- **No study in the retrieved literature tests laddering as such** — the same concept at
  N levels, learner-navigable. `OBSERVED — absence` (F10 §14)
- **The rung-count evidence is real and unusually clean.** ACM TOCE 2026: **three-step >
  two-step, ANOVA F(2,56) = 3.670, p = .032, ηp² = 0.116, Mdiff = 0.99, p = .037**; but
  **five-step did not beat three-step, Mdiff = 0.16 [−0.78, 1.09], p = .738**. Three of
  four hypotheses in that study were null. `MEASURED-RCT` — ERIC EJ1510953. Diminishing
  returns arrive early.
- **Concreteness fading is not domain-general** on principled analysis
  (doi:10.1007/s10648-020-09581-7), was **statistically equivalent to simultaneous
  presentation** within pre-specified bounds of d = ±0.5 at N = 187
  (doi:10.1002/tea.21947), and **multiple concrete representations harmed** symbol
  learning relative to a single abstract one, with the harm attributable to multiplicity
  (doi:10.1037/edu0000318). `MEASURED-RCT` ×3. Every one of those points *against* naive
  laddering.
- The **fidelity rule** — monotone refinement, where level n is entailed by level n+1
  under a declared scope restriction, and climbing may never require negating a prior
  assertion — is **untested**. Its ontology test rests on Chi (2005). `INFERENCE`
- **Census, run 2026-07-27.** arXiv `abs:"explanation" AND abs:"expertise reversal"` →
  **0 results**. `OBSERVED — absence`

**Why it is hard.** The manipulation is easy to confound with *quantity of exposure*: a
learner who reads three rungs has read more than one who read one. The control must hold
**total study time and total information** constant, which means the single-level arm gets
elaboration or a second pass. And the fidelity rule needs an independent audit — you have
to demonstrate that the ladder actually *is* a refinement chain, not five texts, before
you can attribute anything to laddering rather than to inconsistency.

**The experiment that would settle it.**
*Population.* 600 adult learners, 8 concepts in one technical domain, with a verified
three-rung ladder per concept audited for monotone refinement by two independent domain
experts (report κ).
*Arms* (individually randomised, 200 each; **total study time fixed at 12 minutes per
concept in all arms**):
 - **A — Ladder, learner-navigable.** All three rungs available, learner chooses entry
   and may climb or descend freely.
 - **B — Single level, measured-matched.** One rung, selected by a pre-test (the OP-12
   grill), with elaboration filling the time.
 - **C — Single level, preference-matched.** One rung, selected by the learner's stated
   preference — the arm that isolates whether *measurement* is doing the work.
*N justification.* 200/arm detects **d = 0.28**; the decisive contrasts are **A vs B**
(does simultaneity add anything over correct matching?) and **B vs C** (does measurement
beat preference?), the second of which has an unusually strong prior given d ≈ 0.48
preference / zero knowledge.
*Primary outcome.* Delayed (2-week) transfer, plus a **misconception-acquisition
subscale** built from the propositions each rung legally drops — the direct test of the
fidelity rule.
*Secondary.* Navigation traces (how many rungs actually visited; direction of movement);
a planted-misconception detector using deliberately fidelity-violating ladders in a
fourth, small calibration arm (n = 60), to confirm the misconception subscale has
sensitivity.
*Pre-registered prediction.* **B > C by ≈ 0.3 SD** (measurement beats preference — the
strongest prediction in this entry); **A ≈ B on mean transfer but with lower variance**,
because navigation rescues the learners the pre-test misrouted; and **near-zero
misconception acquisition in all three arms** given audited monotone refinement, versus
a detectable rate in the calibration arm.

**Falsifier.** A < B would mean simultaneous availability actively harms — plausibly via
the multiplicity harm already measured — and laddering should be delivered as an
adaptively-selected single rung, not a library. B ≈ C would remove the case for
diagnostic entry altogether and would be a major concession.

---

## PART III — WHO HAS NEVER BEEN MEASURED
### The population layer

---

### OP-14. The empty chair: there are zero randomised trials of AI tutoring on learners with disabilities

**Statement.** Not one adequately powered randomised trial has measured whether an LLM
tutor improves learning outcomes for students with identified disabilities.

**Why it matters.** This survey argues the design order should be inverted — build the
SELPA-grade system, and it serves everyone. That argument is currently made on mechanism
and analogy, not on outcome data for the population it centres. Meanwhile every effect
size being quoted in procurement conversations was measured on typical learners, and the
best available evidence says the transfer direction is **negative**, not neutral.

**What we know.**
- **A reproducible census, run against live APIs on 2026-07-27 and independently
  replicated for this section on the same date.** Europe PMC: `("generative AI" OR
  "ChatGPT" OR "large language model") AND "randomized controlled trial" AND "students"`
  → **30 hits**; the same query plus disability terms (`disability`, `disabilities`,
  `dyslexia`, `ADHD`, `autism`, `special education`) → **0 hits**. ERIC: `"generative
  artificial intelligence" AND education` → 922; `AND "students with disabilities"` → 3;
  `AND "randomized controlled trial"` → **0**. `"intelligent tutoring" AND "students with
  disabilities"` → 20; `AND randomized` → **0**. `MEASURED-BENCH` (own census; method
  stated, reproducible, limited to abstract/keyword indexing).
- **The 19 ChatGPT × special-education records are a teacher-productivity literature**:
  IEP drafting, workload, TPACK, pre-service perceptions, bias audits. **Not one is a
  controlled student-outcomes study.** `OBSERVED`
- **The systematic review confirms it.** Paglialunga & Melogno (2025): the entire world
  literature on AI interventions for students with learning disabilities, 2022–2025,
  seven databases, is **11 studies / 3,033 participants**, of which **at most one is an
  RCT (n = 60)** and **none was rated low risk of bias**. All 11 reported positive
  results — a publication-bias signature. `MEASURED-META` — doi:10.3390/brainsci15080806
- **The known-good base is two orders of magnitude larger.** Direct Instruction alone:
  **328 studies / 413 designs / ~4,000 effects** (Stockard et al. 2018). `MEASURED-META`
  The AI's job here is fidelity and dosage of known-good intervention, not invention.
- **The expected transfer direction is negative.** Unconstrained LLM use **widens** the
  gap between low- and high-prior-knowledge learners (Lehmann et al., two preregistered
  experiments, no main effect); the Nigeria RCT's gains accrued more to students with
  higher initial performance. `MEASURED-RCT` ×2

**Why it is hard.** Genuinely hard, and the difficulty is worth naming precisely rather
than treating the gap as negligence. (i) **Consent and data sensitivity** — disability
status is special-category data under GDPR and protected under FERPA/IDEA, so recruitment
and telemetry both carry elevated burden. (ii) **Heterogeneity** — the modal learner has
*co-occurring* profiles (ADHD + working-memory limitation + prior-failure history), which
makes clean subgroup definition hard and inflates the N needed. (iii) **The ethics of the
control arm** — withholding a validated intervention is not acceptable, so the comparison
must be AI-augmented-known-good vs known-good, never vs nothing. (iv) **Outcome
instruments** — standard achievement tests floor for this population; CBM is the right
instrument and is unfamiliar to most AI researchers.

**The experiment that would settle it.**
*Population.* 400 students on IEPs with a documented reading or mathematics goal, across
≥ 12 schools in a SELPA or equivalent consortium. Co-occurring profiles are **included,
not excluded**, and stratified.
*Arms* (individually randomised within school, 200 each) — **the control is the validated
intervention, never nothing**:
 - **A — Validated explicit-instruction protocol delivered as usual** (the known-good
   floor).
 - **B — Same protocol, same scope and sequence, AI-delivered for dosage** — the AI's job
   is *fidelity and frequency*, not novel pedagogy: more sessions, unlimited repetition
   without visible exasperation, on-demand re-representation, immediate feedback, and a
   documented pivot rule (OP-10).
*N justification.* 200/arm detects **d = 0.28**; with CBM-slope ANCOVA on 4 weeks of
baseline probes (r ≈ .6 with the outcome slope) the detectable effect drops to **d ≈
0.22**. The relevant benchmark is that systematic formative evaluation *with* a decision
rule has ES ≈ 0.70 — so this design is powered to detect even a fraction of the dosage
advantage. Add 15% for attrition.
*Primary outcome.* **CBM growth slope over 20 weeks** — brief, frequent, graphed,
non-punitive, low-stakes by construction — analysed as an individual growth curve.
*Secondary.* Delayed unassisted transfer; **pivot events and their outcomes**; and
mandatory pre-registered reporting of **effects by baseline severity quartile**, because
the mean is the least interesting number this study will produce.
*Non-negotiable design constraints, stated in the protocol.* The AI may not author IEP
content, may not diagnose or label, and may not gate services. Accessibility is a floor
(WCAG 2.2 AA, keyboard-only, screen-reader correct, adjustable motion). Disability status
is minimised and never trained on.
*Pre-registered prediction.* **B > A on CBM slope by ≈ 0.3 SD**, driven predominantly by
*dosage* (sessions completed) rather than by per-session efficacy — and this decomposition
is itself pre-registered, because the mediation analysis is what makes the result
generalisable to other systems.

**Falsifier.** B ≈ A on CBM slope, *with* dosage successfully increased, would be the
single most important null in the field: it would mean the "infinite patience at
unlimited dosage" argument — the core technical case for AI in special education — is
wrong, and that something about human delivery is load-bearing. B < A would mean active
harm and should stop deployment in this population immediately.

---

### OP-15. Is AI tutoring a Matthew-effect machine? Conditional effects are almost never reported

**Statement.** The distributional effect of AI tutoring — who gains and who does not —
has been observed incidentally in three studies and pre-registered as a primary outcome in
none.

**Why it matters.** A mean effect of +0.3 SD is compatible with +0.6 SD for the top
quartile and 0.0 for the bottom, which is a *worse* system than one with a uniform +0.2.
Every equity claim made for AI tutoring — and they are the field's most common
justification — rests on a quantity nobody has made primary.

**What we know.**
- **Lehmann, Cornelius & Sting.** No main effect in either preregistered lab experiment;
  substitutive use ↓ understanding, complementary use ↑ understanding; and **LLMs widen
  the low/high prior-knowledge gap**. Lab N = 107 + 69; field N = 113 grad students
  (6,775 question observations). `MEASURED-RCT`
- **Nigeria (World Bank).** Larger effects for **higher-performing** students.
  `MEASURED-RCT`
- **Tutor CoPilot** points the other way: **+9 p.p. for the lowest-rated tutors** vs +4
  p.p. overall — a compression effect, but on *tutors*, not learners. `MEASURED-RCT`
- **Nie et al., "The GPT Surprise"** (N = 5,831, 146 countries): significant average
  *decrease* in exam participation; the positive exam effect appears only among adopters —
  **selection, not ITT**. `MEASURED-RCT`
- **Trace-based learner models do not generalise across national populations**
  (Finland/Slovakia/US, PIAAC 2012; ERIC EJ1501422) — so a mastery estimator validated in
  one market carries an unmeasured distributional risk in another. `MEASURED-BENCH`

**Why it is hard.** Detecting an interaction requires roughly **four times** the sample of
detecting a main effect of the same size — which is why interactions get relegated to
exploratory analyses and then reported without correction. There is also a ceiling
artefact: high-prior-knowledge learners often sit near the top of researcher-built
instruments, which mechanically compresses their measured gain and can *mask* gap-widening.

**The experiment that would settle it.** This is best run as a **pre-registered
distributional protocol layered onto every other trial in this agenda**, not as a
standalone study — which is what makes it cheap.
*Design requirement.* Any trial reporting a mean effect must **pre-register
prior-knowledge quartile as a moderator**, power for the interaction (4× the main-effect
N, or explicitly declare the study underpowered for it), and use an instrument with
demonstrated headroom at the top quartile (pilot ceiling rate < 10%).
*Standalone version, if run alone.* 1,600 learners stratified by pre-test quartile (400
per quartile), two arms (guardrailed AI vs matched-time no-AI), 4-week delayed transfer.
1,600 detects a **quartile × arm interaction of d = 0.28** at 80% power.
*Primary outcome.* The **arm × prior-knowledge-quartile interaction coefficient**, not
the mean.
*Pre-registered prediction.* A positive interaction for **unguarded** AI (gap-widening,
consistent with Lehmann) and a **null-to-slightly-negative** interaction for
**guardrailed** AI (gap-neutral or gap-closing) — because the mechanism of widening is
substitutive use, and the guardrail's entire function is to prevent substitution. That
prediction is the sharpest available test of the restraint thesis.

**Falsifier.** Gap-widening under the *guardrailed* system as well would mean restraint
does not fix the equity problem, and the survey's claim that constrained systems serve the
margin would need to be withdrawn or heavily qualified.

---

## PART IV — WHAT WE CANNOT CHECK
### The verification layer

---

### OP-16. Statement fidelity across a verification chain: 97% × 69% → 36%

**Statement.** Component-level verification accuracies do not compose, and nobody has
measured or bounded the loss at each hop of a real generation-to-verification pipeline.

**Why it matters.** "Verified" is becoming a product claim. The one benchmark that
measured end-to-end rather than per-component found that **the kernel does not verify the
thing the learner was told** — because the formalisation may not mean what the prose meant.
Every "grounded explanation" architecture in the field, including the grounding ladder in
this survey, inherits this hole, and its size is unmeasured outside competition
mathematics.

**What we know.**
- **miniF2F-v2 (arXiv:2511.03108).** End-to-end informal-statement → formal-statement →
  proof → correspondence-check pipeline: **~36%**, "considerably lower than the individual
  SoTA accuracies, **97% and 69%**, reported in the autoformalization and theorem-proving
  literature." Diagnosis: "discrepancies between the formal and informal statements for
  **more than half** of the problems in miniF2F." After benchmark repair, end-to-end
  reaches **70% (vs 40% on the original)** — an improvement that is *entirely a
  benchmark-quality artefact*. `MEASURED-BENCH`
- **Off-manifold formalisation costs ~26 points.** TaoBench (arXiv:2603.12744): provers
  drop ~26% on definitionally equivalent statements when the definitions are a textbook's
  rather than mathlib's. A tutor that must follow *a specific course* is exactly the
  off-manifold case. `MEASURED-BENCH`
- **The applied domains are the weakest.** College physics **16% (best expert Lean
  prover) – 35% (Claude Sonnet 4)** on LeanPhysBench (arXiv:2510.26094); numerical
  analysis largely absent from mathlib; CAS failure rates of 57–70% on Wester's classic
  sums, definite integrals and transforms. **The domains where formulas matter most to
  learners have the weakest grounding infrastructure.** `MEASURED-BENCH`
- **What is already solved, and should be said loudly:** a millisecond of dimensional plus
  numeric checking catches ~99% of derivation errors with **zero false alarms**, and
  almost nobody runs it. The most common objection — that automated checking punishes
  correct answers written differently — **did not replicate at textbook scale**.
  `MEASURED-BENCH` (F3 §4, §9)

**Why it is hard.** The failing hop is a **natural-language semantics judgement** sitting
*upstream* of the kernel, so no amount of kernel strength helps. Existing semantic-fidelity
metrics are early (GTED, arXiv:2507.07399), and formalisation is **not robust to
paraphrase** (arXiv:2511.12784) — meaning the same claim, restated as a tutor would restate
it, formalises differently.

**The experiment that would settle it.**
*Object.* A **statement-fidelity benchmark for pedagogical content**, not competition
mathematics: 500 claims sampled from three undergraduate textbooks (mechanics,
electromagnetism, introductory statistics), including definitions the books construct
themselves — the off-manifold case deliberately over-sampled.
*Design.* Every claim runs the full chain: prose → formalisation → verification →
**back-translation to prose** → blind expert adjudication of whether the round trip
preserved the claim. Three independent domain experts per item; report κ.
*Arms.* Four formalisation targets (Lean/mathlib, CAS symbolic, dimensional+numeric
executable check, and natural-language entailment against a cited source span), so the
per-tier fidelity loss is measured **separately** rather than as a single pipeline
number.
*N justification.* 500 items with 3 raters estimates a per-tier fidelity rate with 95% CI
of roughly **±4 percentage points** — precise enough to distinguish 90% from 80%, which is
the distinction that decides whether a tier can be trusted unsupervised.
*Primary outcome.* **Per-tier statement-fidelity rate**, plus the **composed end-to-end
rate** and the gap between them.
*Pre-registered prediction.* Dimensional + numeric checking will show fidelity **> 95%**
(it barely formalises, so it barely loses meaning); CAS symbolic **85–92%**; full formal
**60–75%**, worst on textbook-specific definitions; and the composed pipeline will fall
**10–20 points below the product of component rates**, because the errors are correlated
in the direction of plausibility.
*Deliverable.* A published per-tier fidelity table that lets a builder choose the tier
whose guarantee they can actually cash, and an **ABSTAIN rate** per tier — because
collapsing {PASS, FAIL, ABSTAIN} to a boolean destroys the entire guarantee.

**Falsifier.** If per-tier fidelity on pedagogical content comes in above 90% across the
board and composes near-multiplicatively, the grounding ladder is stronger than this
survey claims and can be deployed with far less human audit than recommended.

---

### OP-17. Is "what was omitted" verifiable against a declared scope, or unverifiable in principle?

**Statement.** Two of this survey's own sections disagree about whether omission is
checkable, and the disagreement has never been tested.

**Why it matters.** This is the flagged internal contradiction in the corpus and it is
load-bearing. **The choice of what to omit is the highest-leverage editorial act in
teaching.** A perfectly verified explanation of the wrong 20% is a failure that no
checker in the grounding ladder detects. If omission *is* checkable against a declared
scope, then scope declaration becomes a mandatory artifact of every generated explanation
and a new verification tier exists. If it is not, human review is permanently required at
exactly the point where AI generation is cheapest.

**What we know.**
- **F3 §7 says unverifiable.** "Choice of what to omit — the highest-leverage editorial
  act in teaching, and invisible to every checker in this section. A perfectly verified
  explanation of the wrong 20% is a failure no tier detects." The suggested substitute is
  expert review and coverage against a syllabus. `INFERENCE`
- **F10 §11.1 says checkable, conditionally.** The monotone-refinement rule: "a rung at
  level n is legal iff every proposition it asserts is entailed by the level-n+1 account
  under an **explicitly stated domain restriction**." Under that rule, omission is legal
  *iff scope is declared*, and mechanism-depth may be black-boxed **iff the box is named
  as a box**. That is a checkable predicate — against the level above, not against the
  world. `INFERENCE`
- **The reconciliation is a genuine hypothesis, not a fudge.** Omission relative to a
  *declared* scope is checkable; omission relative to the *right* scope is not, because
  the right scope is a claim about the learner's future. Whether the checkable version
  captures enough of the harm is an empirical question about how often mis-scoping causes
  measurable misconceptions. `INFERENCE`
- Related and encouraging: automated screening works as **triage that raises reviewer
  yield**, never as substitution (ERIC EJ1460469), and item-quality error rates span
  **<1%–45%** (doi:10.1093/postmj/qgag057) — so a checker that catches even a third of
  omission failures changes the review economics substantially. `MEASURED-META`

**Why it is hard.** You need a ground truth for "should have been included," which is
exactly the judgement under dispute. The trick — and it is the design contribution here —
is to construct ground truth **downstream**: define a harmful omission as one that
produces a measurable, durable misconception in a learner, and then ask whether a
scope-declaration checker flags the omissions that do damage.

**The experiment that would settle it.**
*Object.* 200 explanations of 40 concepts, each generated in two variants: **(i)
scope-declared** — the explanation states what it covers and what it defers, and is
checked for monotone refinement against a full-depth reference account; **(ii) undeclared**
— the same content, scope statement stripped.
*Stage 1 — checker validity.* Two independent expert panels rate every explanation for
**harmful omission** (an omission that would cause a learner to over-generalise). Compute
the automated monotone-refinement checker's **sensitivity and specificity against the
expert consensus** on 200 items with 3 raters each.
*Stage 2 — the outcome test, which is the one that matters.* 600 learners randomised
across scope-declared vs undeclared variants, with a **misconception-acquisition
assessment at 2 weeks** built specifically from the over-generalisations each omission
licenses.
*N justification.* 300/arm detects **d = 0.23** on the misconception subscale. Stage 1's
200 items with 3 raters estimates checker sensitivity to ±7 percentage points.
*Primary outcome.* (Stage 1) checker sensitivity to expert-identified harmful omission;
(Stage 2) misconception acquisition rate by arm.
*Pre-registered prediction.* The checker will reach **sensitivity ≈ 0.6–0.75** — good
enough to be a triage tier, not good enough to be a guarantee — and **scope declaration
alone will reduce misconception acquisition by ≈ 0.2 SD**, because naming the box does
much of the work even when the checker misses. If both hold, omission gets a tier in the
grounding ladder labelled honestly: *screens, does not certify.*

**Falsifier.** Checker sensitivity near chance (< 0.3) with no effect of scope
declaration on misconception acquisition would settle it for F3's side: omission is
unverifiable in practice as well as in principle, and human review is permanent. That is a
perfectly acceptable answer and should be stated as such.

---

### OP-18. Does permutation-based fidelity checking (the *pāṭha* protocol) beat self-consistency?

**Statement.** The proposal that **structurally different** redundancy detects errors that
**resampled** redundancy cannot has never been benchmarked.

**Why it matters.** Self-consistency sampling is the default verification method in
deployed systems and it shares its failure mode with the original generation: re-asking
the same question the same way resamples the same plausible error. If structured
permutation — derive in a different order, state the inverse, evaluate at boundary values,
restate symbolically then numerically then in prose, reverse each derivation step —
detects a disjoint error class, it is a cheap, immediately deployable improvement to every
verification stack. It also transfers directly to **assessing the learner**: a student who
memorised a surface string passes "state the formula" and fails the permutation set.

**What we know.**
- The mechanism is a two-thousand-year-old error-detecting code. The Vedic *pāṭha* system
  (*krama*, *jaṭā*, *ghana*) encodes a text in multiple structurally distinct orderings so
  that corruption in one is detectable against the others. `HISTORICAL` — and "the Vedic
  *pāṭha* system improves learning" is explicitly a claim **nobody has tested**.
- **Homogeneous re-asking gains little**, which is the negative space the proposal
  occupies. Three independent benchmark results: Smit et al. (arXiv:2311.17371); Wang et
  al. (arXiv:2402.18272); Becker et al. problem drift (arXiv:2502.19559).
  `MEASURED-BENCH`
- **Sparse and heterogeneous communication topologies help where dense homogeneous ones
  do not** (arXiv:2406.11776; arXiv:2601.05746; arXiv:2410.12853) — consistent with the
  proposal's core claim that the redundancy must be *structurally* different, not merely
  resampled. `MEASURED-BENCH`
- **The proposal is explicitly untested** and was flagged by its author for benchmarking.
  `INFERENCE` — I2 §9.2, §13.8
- **Census, run 2026-07-27.** arXiv `abs:"permutation" AND abs:"self-consistency"` → 16
  results, **none in a verification-of-generated-content setting** (materials chemistry,
  audio-language models, IR ranking, physics). `OBSERVED — absence`

**Why it is hard.** Constructing the permutation set requires domain-specific transforms —
"state the inverse" means something different in linear algebra, thermodynamics and
grammar — so the method is not a single prompt but a per-domain library. And the
comparison must be **compute-matched**: k permutations against k self-consistency samples,
or the result is another token-count artefact (see OP-9).

**The experiment that would settle it.**
*Object.* 1,000 items across four domains with verbatim-fidelity requirements: algebraic
derivations, unit-bearing physics formulas, statutory/definitional statements, and API
contracts. Ground truth established independently.
*Arms* (compute-matched at k = 5 generations per item):
 - **A — Self-consistency.** 5 independent samples, majority vote.
 - **B — Permutation (*pāṭha*).** 1 generation + 4 structurally distinct re-derivations
   (different order, inverse, boundary evaluation, modality shift), checked for mutual
   consistency.
 - **C — Hybrid.** 3 samples + 2 permutations.
*N justification.* 1,000 items detects a **5-percentage-point difference in error-detection
rate** between arms at 80% power (McNemar, paired by item, assuming ~30% baseline error
rate and moderate discordance). The pre-registered smallest effect of interest is 5 points,
because below that the added engineering is not worth it.
*Primary outcome.* **Error-detection rate** (recall on seeded and naturally occurring
errors) at matched **false-alarm rate** — reported as an ROC comparison, not a single
number, because a method that flags everything is not a method.
*Secondary, and the theoretically decisive one.* **Disjointness**: the proportion of errors
caught by B that A missed, and vice versa. If the sets are largely disjoint, the hybrid
dominates and the right answer is "do both."
*Pre-registered prediction.* B > A on error detection by **8–15 percentage points** at
matched false-alarm rate, with the advantage **concentrated in unit/dimension errors and
sign errors** (where inverse-and-boundary permutations bite hardest) and **near zero on
retrieval-style factual errors** (where there is nothing to permute). C dominates both.

**Falsifier.** B ≈ A at matched compute, with high overlap in the errors caught, would
mean permutation is self-consistency wearing a costume, and the proposal should be
withdrawn. That is a clean, cheap test and it should be run before the idea propagates
further.

---

## PART V — WHAT WE ARE NOT ALLOWED TO KNOW
### The governance layer

---

### OP-19. Does clickstream-derived affect detection fall inside EU AI Act Art. 5(1)(f)?

**Statement.** Whether interaction traces count as "behavioural characteristics" under
Art. 3(34) — and therefore whether sensor-free affect detection in education is a
*prohibited* practice rather than a high-risk one — has no authoritative construction.

**Why it matters.** This single question determines the legality of a large body of
AIED work in the EU. Sensor-free affect detection from clickstream data is a
well-established research programme with a decade of published work, and it is the
mechanism behind "the system noticed you were frustrated." If Art. 5(1)(f) reaches it,
that entire line is not merely regulated but banned in education, and a large class of
adaptive designs must be rebuilt around **behavioural** triggers (latency, error type,
abandonment) with no affective interpretation attached. Builders need to know *now*,
because the architecture differs.

**What we know.**
- **Art. 5(1)(f)** prohibits emotion-inference systems in the workplace and in education,
  with narrow exceptions. **Art. 3(34)** defines the relevant system by reference to
  biometric data. Whether clickstream traces are "behavioural characteristics" within that
  definition is the pivot. `VERIFIED` (statutory text) / `INFERENCE` (the construction)
- **No authoritative construction found.** Flagged in F8 as **the highest-value open legal
  question in this domain.** EUR-Lex returned HTTP 202 with an empty body throughout the
  F8 session, so the consolidated text could not be read directly. `[UNVERIFIED-IN-SESSION]`
- A related unresolved question: **does Annex III(3)(b) reach direct-to-consumer tutors?**
  3(b) lacks the institutional limiter present in 3(c) and 3(d); plain-text reading says
  yes; no guidance found. `INFERENCE`
- **Whether the 2 August 2026 Annex III date is still operative could not be verified** —
  the best available timeline source is stamped 2024-08-01 and cannot reflect later
  amendment. **Verify Art. 113 against EUR-Lex before any compliance decision.**
  `[UNVERIFIED-IN-SESSION]`
- **Census, run 2026-07-27.** arXiv `abs:"emotion recognition" AND abs:"AI Act"` → **1
  result** (arXiv:2509.20153, affective computing and emotional data under privacy
  regulation, the AI Act and ethics) — a discussion paper, not a construction.
  `OBSERVED — absence`
- The design counsel this project has already adopted regardless: the lifelong learner
  model **carries no affect or emotion inference**, and the survey treats Art. 5(1)(f) as
  good policy rather than as a constraint. `INFERENCE`

**Why it is hard.** It is a legal question, so it resolves through guidance, enforcement,
or litigation, not through experiment — which is precisely why it belongs in an open-problems
section aimed at builders rather than being quietly assumed away. The technical
complication is that the boundary is **fuzzy by construction**: a model that predicts
disengagement from latency and error patterns and a model that predicts "frustration" from
the same features may be the same model with a different label on its output.

**What would settle it (this one is not an RCT, and pretending otherwise would be a
category error).**
1. **A formal request for guidance** to the relevant national supervisory authority or the
   AI Office, posing the question with two worked system descriptions attached: System A
   predicts *next-action abandonment probability* from latency and error type and triggers
   a pivot; System B predicts *frustration* from identical features and triggers identical
   behaviour. **If A and B are treated differently, the boundary is the output label; if
   they are treated the same, the boundary is the feature set.** That is the disambiguating
   probe, and it is cheap.
2. **A published construction** — a law-review-grade analysis of Art. 3(34) against the
   sensor-free-affect-detection literature, which would give the field something to cite.
3. **In the meantime, a testable design hypothesis with a real experiment attached:**
   does a pivot policy triggered on **behavioural** signals alone (latency, error type,
   abandonment) perform as well as one triggered on **inferred affect**? That is a clean
   two-arm study, n = 200/arm for d = 0.28, and it is the arm of OP-10 that this legal
   question makes urgent. If behavioural triggers match affective ones, the legal question
   becomes moot for builders — which is the best possible outcome and the reason to run it
   first.

**Falsifier (of the design hypothesis).** If affect-inferred triggers materially outperform
behavioural ones, the legal question becomes load-bearing and the field needs the guidance
in (1) urgently. If they perform identically, build the behavioural version, and the
prohibition costs nothing.

---

## 2. WHAT WOULD FALSIFY THIS SURVEY'S OWN THESIS

The document argues that the measured **0.2–0.4 SD** band for LLM tutoring is *"the floor
with the brakes on"* — that constrained, grounded, pivoting, remembering, teachable systems
would do better, and that nobody has built the good version and measured it. Intellectual
honesty requires stating the strongest case against that, not a strawman of it.

### 2.1 The counter-argument, in its strongest form

**Premise 1 — 0.2–0.4 SD is not a floor, it is the modal result of educational
intervention research, full stop.** It is where tutoring lands, where formative
assessment lands, where feedback lands, where most well-implemented instructional
technology lands once the trial is adequately powered and independently run. The
regularity is not a fact about AI. It is a fact about how much of variance in learning
outcomes is available to be moved by *any* instructional manipulation given fixed time,
fixed prior knowledge, and fixed motivation. On this reading, the survey has mistaken a
population parameter for a technology limitation.

**Premise 2 — the null results already on record are the honest prior, and they are not
peripheral.** They are the *most rigorous* studies in their respective literatures:

| Result | Effect | Note | Label |
|---|---|---|---|
| **Orton-Gillingham vs comparison instruction** | **g = 0.22, p = .40**; g = 0.14, p = .59 | The most-requested dyslexia intervention. The evidenced ingredient is explicit systematic decoding, not the branded method | `MEASURED-META` (Stevens et al. 2021) |
| **Expanding retrieval intervals** | **g = 0.034, n.s.** | The curve marketed by SM-2/FSRS is not the active ingredient | `MEASURED-META` (Latimier 2020) |
| **Lesson Study (EEF)** | **ES 0.02, 95% CI [−0.06, 0.09], p = .65** | n = 6,437; 181 schools, 12,747 pupils; **very high** security; null across maths, reading, SPAG, science; null in every subgroup; **no dose–response**; fidelity was good | `MEASURED-RCT` |
| **Multimedia pedagogical agents** | **g = 0.20** | Authors' own conclusion: students "may be able to learn similarly from different types of agents" | `MEASURED-META` (Castro-Alonso et al. 2021) |
| **Ruffle&Riley** (LLM learning-by-teaching) | **null twice**, N = 100 and N = 200 | High subjective ratings; users needed *more* time | `MEASURED-RCT` |
| **Lehmann et al.** | **no main effect**, two preregistered experiments | And gap-widening | `MEASURED-RCT` |
| **RTI at federal scale** | **negative** Grade-1 impacts | Regression discontinuity; framework fidelity ≠ framework benefit | `MEASURED-RCT` (Balu et al. 2015) |
| **Working-memory training** | **no transfer** | Do not build a brain trainer | `MEASURED-META` (Melby-Lervåg et al. 2016) |
| **UDL** | outcomes **not demonstrated** | The bundled components are individually evidenced; the bundle's claim is not | `MEASURED-META` |

**Premise 3 — added mechanism adds cognitive load and complexity, and the load is real
while the benefit is speculative.** This is the sharpest version and the survey's own
evidence supplies it. Multiple concrete representations **harmed** symbol learning, with
the harm attributable to multiplicity (doi:10.1037/edu0000318). Five ladder rungs did not
beat three (p = .738). Seductive details — coherent but extraneous material — are costly.
Persistent decorative detail carries **g = 0.43** of *harm*. Mixing models **reduced**
ensemble quality (Self-MoA, +6.6% for the simpler system). Declaring dependencies made
notebook reproduction *worse*. Every one of those is a case where the elaborated version
lost to the plain one. A "village of agents with persistent state, deixis, laddering,
error-holding tutees and a pivot engine" is the most elaborate system anyone has proposed,
and the base rate for elaboration in this literature is not good.

**Premise 4 — the mechanism this survey most relies on has a moderator that dwarfs it.**
Gu & Yan (2025): AI tutoring **with teacher support g = 1.426; without teacher support
g = 0.077**. If the human is doing the work, then every architectural refinement is
optimising the small term. `MEASURED-META`

**Premise 5 — the field's positive results degrade under scrutiny in one direction only.**
Sierra Leone's unadjusted estimate is not significant. The largest positive meta-analysis
was retracted. Kestin's tutor was built and analysed by its first author with no funding
statement. Rori has 11 clusters. Nigeria lost 43% of its sample. Where independence and
rigour increase, effects shrink. That is the signature of a literature whose true effect
is smaller than its published mean.

**That is a serious argument.** Anyone who cannot state it in that form has not earned the
right to the survey's conclusion.

### 2.2 What the survey says back — briefly, and without overclaiming

Three responses, offered as reasons the hypothesis is still worth testing, not as
refutations:

1. **The nulls are mostly about *branding*, not *mechanism*.** Orton-Gillingham nulls while
   explicit systematic decoding instruction — its active ingredient — carries **d = 0.41
   to 0.55** in the National Reading Panel syntheses. Expanding intervals null while
   *scheduling retrieval at all* carries classroom **d = 0.54**, with only 12 of 271
   massed-vs-spaced comparisons failing. Lesson Study nulls as a *process* while the
   content-bearing interventions do not. The pattern is: the wrapper fails, the mechanism
   holds. The survey's programme is explicitly mechanism-level.
2. **The dissociation results are not ceiling results, they are *sign* results.** A
   ceiling story predicts small positive effects everywhere. Bastani found **−17%**, and
   the same model with a different interaction policy found **zero**. A variable that
   moves an outcome from −17% to 0 within one study is not near a ceiling; it is
   near a *decision*.
3. **The strongest single argument is the empty chair.** Zero RCTs on learners with
   disabilities is not a verdict, and the ceiling argument cannot be assessed for the
   population where prior-knowledge, dosage and fidelity constraints bind hardest —
   which is exactly the population where the mechanism-level case is strongest.

### 2.3 The concession conditions — stated in advance

We would concede that 0.2–0.4 SD is a real ceiling rather than a floor, and that added
mechanism does not pay, if:

1. **OP-11 returns A ≈ C** at n = 300/arm — the guardrailed tutor does not beat matched-time
   worked examples plus retrieval practice on a 6-week unassisted outcome. This is the
   single most decisive test, because it compares the survey's flagship design against the
   best cheap known-good alternative on the survey's own preferred outcome.
2. **OP-6 returns C = B = A** on prerequisite-dependent transfer *and* the typed-vs-untyped
   ablation shows no difference — persistent state buys nothing even when correctly typed.
3. **OP-9 returns C ≈ B ≈ D** at matched compute — architectural elaboration is compute in
   a costume.
4. **OP-7 returns A ≈ B despite a clean separation in belief persistence** — the most
   distinctive mechanism in the survey's design is inert.
5. **Any two of OP-8, OP-10, OP-13 return flat** — deixis, pivot latency and laddering are
   the three "add a mechanism" bets; if two of three are null, the elaboration thesis is in
   serious trouble regardless of the others.
6. **A well-powered, independent, preregistered trial of a system implementing *several*
   of these mechanisms together lands inside 0.2–0.4 SD** on a delayed unassisted outcome.
   This is the cleanest concession trigger and the one we should most want run, because
   it tests the conjunction rather than the parts.

If (1) and (6) both land, the correct revision is not a hedge. It is to rewrite the thesis
as: *AI's contribution to learning is the scalable, high-fidelity, high-dosage delivery of
interventions we already knew worked, and the design space of novel mechanisms is a
distraction.* That would still be an important and actionable finding — it would redirect
the field toward fidelity and dosage, which is precisely what H1 argues for special
education already. We should say so now, in advance, so that conceding costs us nothing
but a hypothesis.

---

## 3. THE RESEARCH AGENDA

### 3.1 Ranking

Scored on **expected information gain** (how much would the answer move design decisions
across the field, not just for one product) × **feasibility** (can a competent team run it
within one academic year with resources a mid-sized research group or a well-instrumented
product organisation already has). Both 1–5; product is the rank key. `INFERENCE` — this
is the author's judgement, stated as such.

| Rank | # | Problem | EIG | Feas. | Score |
|---|---|---|---|---|---|
| 1 | **OP-1** | Delayed, unassisted, novel-item outcome | 5 | 5 | **25** |
| 2 | **OP-6** | Persistent state vs stateless baseline | 5 | 5 | **25** |
| 3 | **OP-11** | Does the guardrail add benefit? | 5 | 4 | **20** |
| 4 | **OP-14** | The empty chair (disability RCT) | 5 | 3 | **15** |
| 5 | **OP-18** | *Pāṭha* permutation vs self-consistency | 3 | 5 | **15** |
| 6 | **OP-15** | Gap-widening as a primary outcome | 4 | 4 | **16** |
| 7 | **OP-9** | Village vs token-matched single agent | 4 | 4 | **16** |
| 8 | **OP-4** | Benchmarks anchored to human learning | 5 | 3 | **15** |
| 9 | **OP-8** | Deixis | 4 | 4 | **16** |
| 10 | **OP-2** | Felt/real: liked *and* effective | 5 | 3 | **15** |
| 11 | **OP-7** | An agent that can stay wrong | 4 | 3 | **12** |
| 12 | **OP-10** | Pivot latency and trigger | 4 | 3 | **12** |
| 13 | **OP-3** | Reliability for generated assessment | 4 | 3 | **12** |
| 14 | **OP-12** | Grilling as a named intervention | 4 | 3 | **12** |
| 15 | **OP-13** | Laddering as such | 3 | 4 | **12** |
| 16 | **OP-16** | Statement fidelity across the chain | 4 | 3 | **12** |
| 17 | **OP-17** | Verifying the omission | 4 | 2 | **8** |
| 18 | **OP-5** | Personalisation-induced DIF | 4 | 2 | **8** |
| 19 | **OP-19** | Affect detection under Art. 5(1)(f) | 4 | 2 | **8** |

*Ties are broken by how many other problems the answer unblocks.* OP-1 and OP-6 tie at 25;
OP-1 is placed first because **every other experiment in this agenda uses its primary
outcome**, so running it first also validates the instrument the rest depend on.

### 3.2 The three to run first

**1 — OP-1: the delayed, unassisted, novel-item outcome.**
*Why first.* It is the **measurement precondition for everything else in this document.**
Seventeen of the nineteen experiments above name a delayed unassisted transfer test as
their primary outcome; if that instrument is not built, validated and shown to be
administrable at scale, none of the rest can be run credibly. It is also the study with
the highest chance of overturning the field's existing conclusions, because it is the one
measurement nobody has made and the one measurement whose absence could be hiding a sign
flip. And it is cheap: no novel system to build, three arms, one curricular unit, one
school system.
*The number that decides it.* The **rank correlation between immediate-assisted and
6-week-unassisted arm ordering.** If it is high, the field's existing evidence base is
salvageable. If it is low, a large fraction of published edtech effect sizes are
measuring the wrong construct, and that is the single most consequential finding available
in this space.

**2 — OP-6: persistent learner state against a stateless baseline.**
*Why second.* It is the **cleanest ablation in the field and the largest unmeasured
engineering commitment.** Memory is being built everywhere — at real privacy cost, real
regulatory cost, and real architectural cost — on zero outcome evidence. The design is a
pure ablation: same model, same prompt, same interface, differing only in what crosses the
session boundary. Any product with 600 users and a delayed assessment can run it. And the
built-in typed-vs-untyped sub-ablation means a null produces a *diagnosis* (the KC
alignment problem) rather than a dead end — which is what makes it worth running even if
you expect it to null.
*The number that decides it.* **Arm C − Arm A on the prerequisite-dependent transfer
subscale.** Localisation is the prediction; a uniform gain would indicate a confound and a
uniform null would end the memory programme.

**3 — OP-11: does the guardrail ever add benefit?**
*Why third.* It is the **survey's own thesis on trial**, and it is the concession trigger
named in §2.3. The restraint claim currently rests on a single study in which the
guardrail moved the effect from −17% to *exactly zero*. Until somebody shows a constrained
tutor beating matched-time worked examples plus retrieval practice on a delayed unassisted
outcome, the honest headline is "safe when guardrailed," not "works." Running this third —
after the outcome instrument exists (OP-1) and the memory question is settled (OP-6) —
means the guardrailed arm can be built with whatever those two studies say actually
matters, giving the thesis its fairest test rather than its cheapest one.
*The number that decides it.* **A − C on 6-week unassisted transfer**, with a
pre-registered smallest effect of interest of **d = 0.20**. My honest prior that A > C is
about 55%. That is precisely the confidence level at which an experiment is worth running.

### 3.3 What a single well-instrumented product can contribute

Three of the top five are runnable inside one deployed product with a few hundred
consented users and no new modelling work: **OP-6** (memory ablation), **OP-15**
(gap-widening as a pre-registered moderator on any trial already running), and **OP-18**
(permutation vs self-consistency, which needs no learners at all — 1,000 items and a
compute budget). **OP-1**'s delayed-assessment panel is the shared infrastructure that
makes the others reportable. That is a realistic first-year programme, and it would place
its owner in possession of four of the field's missing numbers.

---

## 4. NEGATIVE AND NULL RESULTS IN THIS SECTION

Per the project's evidence rules. This section is, unusually, composed almost entirely of
absences — but these are the *substantive* nulls it relies on and reports as findings
rather than as caveats:

1. **Lesson Study: ES 0.02 [−0.06, 0.09], p = .65**, n = 6,437, 181 schools / 12,747
   pupils, very high security; null in every subject and every subgroup; no dose–response;
   fidelity was good. `MEASURED-RCT` — ERIC ED581145
2. **Expanding retrieval intervals: g = 0.034, n.s.** The marketed schedule shape is not
   the active ingredient. `MEASURED-META` — Latimier 2020
3. **Orton-Gillingham: g = 0.22, p = .40; g = 0.14, p = .59.** `MEASURED-META` — Stevens
   et al. 2021
4. **Multimedia pedagogical agents: g = 0.20**, with the authors concluding students may
   learn similarly from different agent types. `MEASURED-META` —
   doi:10.1007/s10648-020-09587-1
5. **Ruffle&Riley nulled twice** (N = 100; N = 200) on learning gain while scoring high on
   subjective ratings. `MEASURED-RCT` — arXiv:2310.01420, arXiv:2404.17460
6. **Five ladder rungs did not beat three** (Mdiff = 0.16 [−0.78, 1.09], p = .738); three
   of four hypotheses in that study were null. `MEASURED-RCT` — ERIC EJ1510953
7. **Self-MoA beat mixed Mixture-of-Agents** (+6.6% AlpacaEval 2.0): diversity is not free.
   `MEASURED-BENCH` — arXiv:2502.00674
8. **Debate does not reliably beat self-consistency** — three independent benchmark
   results. `MEASURED-BENCH`
9. **AI tutoring without teacher support: g = 0.077 (≈ null)** vs g = 1.426 with it.
   `MEASURED-META` — Gu & Yan 2025
10. **The largest positive LLM-tutoring meta-analysis (g = 0.867) was retracted in 2026.**
11. **Prompted novice agents drift back to expert-level answers** — prompting cannot hold
    an error. `MEASURED-BENCH` — arXiv:2603.26142
12. **CBM alone produced more programme revisions and no achievement gain**; only CBM plus
    an instructional decision rule worked. `MEASURED-RCT` — Fuchs, Hamlett & Stecker 1991
13. **The objection that automated checking punishes correct answers written differently
    did not replicate at textbook scale** — a null reported because it is the absence of an
    expected effect, and it clears the way for cheap grounding. `MEASURED-BENCH` — F3 §9

---

## 5. VERIFICATION LOG — what was checked on 2026-07-27

Run specifically to try to falsify the open problems above. **Three candidates were
downgraded or rewritten as a result** and are marked ▲.

| Query | Endpoint | Result | Effect on this section |
|---|---|---|---|
| `("generative AI" OR "ChatGPT" OR "LLM") AND "randomized controlled trial" AND "students"` | Europe PMC | **30 hits** | Calibration for the next row |
| …same + disability terms | Europe PMC | **0 hits** | **OP-14 confirmed**, independently of H1's census |
| `abs:"teachable agent"` | arXiv | **18 total**; none installs/defends a specific false proposition | **OP-7 confirmed, narrowed** — the claim is not "teachable agents are unstudied" (they are, at small N) but "error-holding has never been isolated" ▲ |
| `"teachable agent" AND "randomized"` | Europe PMC | **0 hits** | Supports OP-7's power warning |
| `abs:"long-term memory" AND abs:"tutor"` | arXiv | **0** | OP-6 confirmed |
| `abs:"memory" AND abs:"tutoring system" AND abs:"large language model"` | arXiv | **6**, all system papers, **no ablation arm** | OP-6 confirmed |
| `abs:"deictic" AND abs:"tutor"` | arXiv | **0** | OP-8 confirmed |
| `abs:"referring expression" AND abs:"education"` | arXiv | **1** — arXiv:2604.02893, geometry RIS, 200k synthetic diagrams, **49% IoU / 85% BIoU** fine-tuned vs <1% zero-shot | **OP-8 rewritten** ▲ — the grounding substrate now partly exists; the gap is the tutoring loop and the efficacy measurement, not the model |
| `abs:"multi-agent" AND abs:"classroom" AND abs:"learning gains"` | arXiv | **0** | OP-9 confirmed |
| `"intelligent tutoring" AND "multi-agent"` | Europe PMC | **4**, all architecture | OP-9 confirmed |
| `"generalizability theory" AND "automatic item generation"` | ERIC | **1**, from 2013, off-target | OP-3 confirmed |
| `"differential item functioning" AND "large language model"` | ERIC | **1**, 2023, scoring not generation | OP-5 confirmed |
| `"retention test" AND "ChatGPT"` | ERIC | **0** | OP-1 confirmed |
| `"transfer test" AND "ChatGPT"` | ERIC | **0** | OP-1 confirmed |
| `"artificial intelligence" AND "delayed posttest"` | ERIC | **7**, recent ones EFL vocabulary | **OP-1 narrowed** ▲ — delayed post-tests exist in AI-assisted *language* learning; the gap is conceptual transfer, not the instrument |
| `abs:"guardrails" AND abs:"learning" AND abs:"randomized"` | arXiv | 7, none relevant | OP-11 confirmed |
| `"guardrails" AND "learning" AND "randomized"` | Europe PMC | **0** | Bastani unreplicated |
| `abs:"permutation" AND abs:"self-consistency"` | arXiv | **16**, none in generated-content verification | OP-18 confirmed |
| `abs:"emotion recognition" AND abs:"AI Act"` | arXiv | **1**, discussion paper | OP-19 confirmed |
| `abs:"explanation" AND abs:"expertise reversal"` | arXiv | **0** | OP-13 confirmed |
| `all:"Ruffle&Riley"` | arXiv | **2** — 2310.01420, 2404.17460, both located | Null claims verified as existing papers |

**Unreachable this session, stated rather than guessed:**
- **OpenAlex** — the works endpoint returned malformed/blocked responses on all three
  attempted queries. No OpenAlex evidence is used in this section.
- **Semantic Scholar Graph API** — not attempted; rate-limited throughout prior sessions.
- **EUR-Lex CELEX:32024R1689** — consolidated AI Act text could not be read in prior
  sessions (HTTP 202, empty body). **OP-19's date and Annex III questions remain
  `[UNVERIFIED-IN-SESSION]` and must be checked against EUR-Lex before any compliance
  decision.**
- **arXiv over plain HTTP** returned zero bytes; all arXiv queries above used HTTPS.

**Standing limitation on every census in this section.** All are abstract-and-keyword
searches. A study reporting a relevant finding only in a results table would be missed.
Each is reported as `OBSERVED — absence` with the query string given, so that any reader
can reproduce it and any counter-example can be produced cheaply. **A stated open problem
that turns out to be answered is a correction we would welcome and publish.**

---

## 6. SOURCES

**Randomised trials — LLM tutoring**
1. Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), *PNAS* — https://doi.org/10.1073/pnas.2422633122 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ `MEASURED-RCT`
2. Correction to Bastani et al. — https://doi.org/10.1073/pnas.2518204122
3. LearnLM Team, Google & Fab AI (2026), Sierra Leone Guided Learning — https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf · AEARCTR-0016651 `MEASURED-RCT`
4. World Bank (2025), Nigeria after-school GenAI tutoring — https://blogs.worldbank.org/en/education/From-chalkboards-to-chatbots-Transforming-learning-in-Nigeria `MEASURED-RCT`
5. Kestin et al. (2025), *Scientific Reports* — https://www.nature.com/articles/s41598-025-97652-6 `MEASURED-RCT`
6. Tutor CoPilot (Stanford, 2024) `MEASURED-RCT`
7. Nie et al. (2025), "The GPT Surprise", L@S `MEASURED-RCT`
8. Lehmann, Cornelius & Sting, "AI Meets the Classroom" — arXiv:2409.09047 `MEASURED-RCT`
9. Ruffle&Riley — arXiv:2310.01420 (N=100); arXiv:2404.17460 (N=200) `MEASURED-RCT`
10. AI-generated vs textbook materials, N=214 — arXiv:2412.15747 `MEASURED-RCT`

**Meta-analyses — learning science floor**
11. Retrieval practice, 222 studies / 48,478 students `MEASURED-META` (B1)
12. Pan & Rickard (2018), transfer, *Psych. Bulletin* — https://doi.org/10.1037/bul0000151 `MEASURED-META`
13. Latimier (2020), expanding intervals, **g = 0.034 n.s.** `MEASURED-META`
14. Cepeda (2008), optimal spacing gaps `MEASURED-META`
15. Stevens et al. (2021), Orton-Gillingham, **g = 0.22 p=.40** `MEASURED-META`
16. Castro-Alonso, Wong, Adesope & Paas (2021), pedagogical agents **g = 0.20** — https://doi.org/10.1007/s10648-020-09587-1 `MEASURED-META`
17. Schroeder, Adesope & Gilbert (2013), pedagogical agents, *JECR* 49(1) `MEASURED-META`
18. Gu & Yan (2025), *JECR*, **g = 0.683 / 1.426 / 0.077** `MEASURED-META`
19. Wang & Fan (2025), *Hum Soc Sci Commun* — **RETRACTED 2026**
20. Ehri et al. (2001), systematic phonics **d = 0.41 / 0.55 / 0.27** — https://doi.org/10.3102/00346543071003393 `MEASURED-META`
21. Stockard et al. (2018), Direct Instruction, 328 studies `MEASURED-META`
22. Paglialunga & Melogno (2025), *Brain Sciences* 15(8):806 — https://doi.org/10.3390/brainsci15080806 `MEASURED-META`
23. Fuchs & Fuchs (1986), formative evaluation **ES = 0.70** — https://doi.org/10.1177/001440298605300301 `MEASURED-META`
24. Stecker, Fuchs & Fuchs (2005) — https://doi.org/10.1002/pits.20113 `MEASURED-META`
25. Melby-Lervåg, Redick & Hulme (2016), working-memory training `MEASURED-META`
26. Kıyak, Kaya & Emekli (2026), 71 studies, error rates <1%–45% — https://doi.org/10.1093/postmj/qgag057 `MEASURED-META`
27. EEF *Lesson Study* (Murphy et al. 2017), **ES 0.02** — ERIC ED581145 `MEASURED-RCT`
28. Balu et al. (2015), RTI federal evaluation, negative Grade-1 impacts `MEASURED-RCT`

**Randomised — pedagogy and measurement**
29. Deslauriers, McCarty, Miller, Callaghan & Kestin (2019), *PNAS* — https://doi.org/10.1073/pnas.1821936116 `MEASURED-RCT`
30. Buljan et al. (2018), *J Clin Epidemiol* — https://doi.org/10.1016/j.jclinepi.2017.12.003 `MEASURED-RCT`
31. Fuchs, Hamlett & Stecker (1991), *AERJ*, CBM + expert system `MEASURED-RCT`
32. Deno (1985), CBM origin — https://doi.org/10.1177/001440298505200303 `OBSERVED`
33. Van Norman et al. (2023), CBM trend-line viability 7–10 weeks `MEASURED-BENCH`
34. Concreteness-fading ladder study, three-step > two-step (p=.032), five ≯ three (p=.738) — ERIC EJ1510953 `MEASURED-RCT`
35. Concreteness fading ≡ simultaneous presentation, N=187 — https://doi.org/10.1002/tea.21947 `MEASURED-RCT`
36. Multiple concrete representations harmed symbol learning — https://doi.org/10.1037/edu0000318 `MEASURED-RCT`
37. Concreteness fading not domain-general — https://doi.org/10.1007/s10648-020-09581-7 `MEASURED-META`
38. Seductive details cost — https://doi.org/10.1007/s10648-020-09522-4 `MEASURED-META`

**Benchmarks — models, agents, verification**
39. miniF2F-v2 / miniF2F-Lean revisited — arXiv:2511.03108 `MEASURED-BENCH`
40. TaoBench — arXiv:2603.12744 `MEASURED-BENCH`
41. Lean4Physics / LeanPhysBench — arXiv:2510.26094 `MEASURED-BENCH`
42. GTED autoformalization metric — arXiv:2507.07399 `MEASURED-BENCH`
43. Autoformalization robustness to paraphrase — arXiv:2511.12784 `MEASURED-BENCH`
44. Formalizing numerical analysis: audit beyond kernel acceptance — arXiv:2606.14000 `MEASURED-BENCH`
45. MAST, multi-agent failure taxonomy — arXiv:2503.13657 `MEASURED-BENCH`
46. Self-MoA — arXiv:2502.00674 `MEASURED-BENCH`
47. Du et al., multi-agent debate — arXiv:2305.14325 `MEASURED-BENCH`
48. Smit et al., "Should we be going MAD?" — arXiv:2311.17371 `MEASURED-BENCH`
49. Wang et al., "Rethinking the Bounds of LLM Reasoning" — arXiv:2402.18272 `MEASURED-BENCH`
50. Becker et al., problem drift in multi-agent debate — arXiv:2502.19559 `MEASURED-BENCH`
51. Sparse communication topology in debate — arXiv:2406.11776 `MEASURED-BENCH`
52. DynaDebate — arXiv:2601.05746 `MEASURED-BENCH`
53. Diversity of thought — arXiv:2410.12853 `MEASURED-BENCH`
54. LLM judges self-prefer — arXiv:2404.13076 `MEASURED-BENCH`
55. "Measuring Whether LLM Tutors Teach or Solve", r = 0.421 — arXiv:2606.16206 `MEASURED-BENCH`
56. Novice simulation via machine unlearning — arXiv:2603.26142 `MEASURED-BENCH`
57. Learning-by-teaching with ChatGPT — arXiv:2412.15226 `OBSERVED`
58. Teachable-agent knowledge discouragement — arXiv:2309.14534 `OBSERVED`
59. MathDial — arXiv:2305.14536 `MEASURED-BENCH`
60. Chrysalis, teaching vs tutoring, N=36 — arXiv:2510.05271 `OBSERVED`
61. LLM teachable agent, music theory, N=28 — arXiv:2504.00636 `MEASURED-RCT` (small)
62. HypoCompass — arXiv:2310.05292 `MEASURED-BENCH`
63. **Toward an Artificial General Teacher: geometry visual grounding, 49% IoU / 85% BIoU** — arXiv:2604.02893 `MEASURED-BENCH` *(verified 2026-07-27)*
64. In-context adversarial student agents underestimate leakage — arXiv:2604.18660 `MEASURED-BENCH`
65. Affective use and well-being, 28-day RCT n≈1,000 — arXiv:2504.03888 `MEASURED-RCT`

**Psychometrics and fairness**
66. Cronbach & Shavelson (2004), *EPM* — https://doi.org/10.1177/0013164404266386 `OBSERVED`
67. Brennan (2001), *Generalizability Theory* — https://doi.org/10.1007/978-1-4757-3456-0 `OBSERVED`
68. Revelle & Zinbarg (2009), *Psychometrika* — https://doi.org/10.1007/s11336-008-9102-z `OBSERVED`
69. Geerlings, Glas & van der Linden (2012), calibrated-feature generation — https://doi.org/10.1177/0146621612468313 `OBSERVED`
70. Cole et al. (2020), saturation — ERIC EJ1227607 `MEASURED-BENCH`
71. Gorgun & Bulut (2025), LLM quality control / cross-family screening — ERIC EJ1460469 `MEASURED-BENCH`
72. Falcão et al. (2024), *Educ Inf Technol* — ERIC EJ1416068 `MEASURED-BENCH`
73. Huang et al. (2026), *Assessing Writing* — https://doi.org/10.1016/j.asw.2026.101047 `MEASURED-BENCH`
74. Gorgun & Yildirim-Erbasli (2026), cross-national non-generalisation — ERIC EJ1501422 `MEASURED-BENCH`
75. LLM item-complexity judgements, low ICC — arXiv:2304.05372 `MEASURED-BENCH`

**Governance**
76. EU AI Act, Art. 3 (definitions), Art. 5 (prohibited practices), Art. 113 (application dates), Annex III — https://artificialintelligenceact.eu/ `VERIFIED`
77. EUR-Lex CELEX:32024R1689 — `[UNVERIFIED-IN-SESSION]`
78. Affective computing and emotional data under privacy regulation and the AI Act — arXiv:2509.20153 `OBSERVED`

**Internal — this project's own reports, cited as `INTERNAL-REPORT`**
A1 · A2 · A4 · B1 · B2 · C1 · C2 · D1 · D3 · F1 · F2 · F3 · F4 · F5 · F6 · F8 · F10 · G2 · G3 · H1 · I1 · I2, all at `research/raw/`.

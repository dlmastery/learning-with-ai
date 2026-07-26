---
title: "The Learning-Science Floor: What We Actually Know Works, Independent of AI"
wave: B
section: B1
date_researched: 2026-07-25
sources_count: 109
status: source-archive
synthesis: B1-learning-science-control-loop-2026.md
---

# The Learning-Science Floor

> **Source-archive note:** This long-form effect-size and replication review is
> retained as the foundational evidence spine. The July 2026 frontier synthesis,
> organized as an executable teaching control loop, is
> [B1-learning-science-control-loop-2026.md](B1-learning-science-control-loop-2026.md).

**Purpose of this section.** Every AI capability claimed in this survey should be judged against
what non-AI instructional science already delivers, at what effect size, with what replication
record. This section establishes that baseline and is deliberately unkind to popular ideas that
the evidence does not support.

**How to read the effect sizes.** Almost every number below is a standardized mean difference
(Cohen's *d* or Hedges' *g*). Three warnings apply throughout:

1. **Heterogeneity is enormous.** The best meta-analyses in this literature report I² between
   77% and 91%. A pooled *g* of 0.50 does not mean "you will get 0.50"; it means the true effects
   range widely and the pooled value is a summary of a very lumpy distribution.
2. **Test alignment inflates effects.** Researcher-made, narrowly aligned tests produce effects
   roughly 2–3× those measured on broad standardized instruments (documented explicitly for
   tutoring and for ITS; see §7, §8).
3. **Publication-bias corrections shrink effects.** Where corrections have been applied, effects
   fall substantially (e.g. the modality effect: g = 0.38 → g = 0.20).

A rough grading used below:

- **A (well-replicated)** — multiple independent meta-analyses, classroom RCTs, survives
  publication-bias correction.
- **B (solid but bounded)** — meta-analytically supported, but with large moderators or
  restricted to lab/undergraduate samples.
- **C (contested / thin)** — small corpora, unstable under rigor subsplits, or theoretically
  disputed.
- **F (not supported)** — the popular claim is not supported by the evidence.

---

## 1. Retrieval practice / the testing effect — **Grade A**

### Core finding

Retrieving information from memory produces better long-term retention than re-studying the same
material for the same amount of time.

**Roediger & Karpicke (2006, *Psychological Science*)** established the canonical crossover:
after a 5-minute delay, repeated *study* beat repeated *testing*; after 2 days and 1 week, the
ordering reversed and testing won decisively. This crossover is the single most important design
fact in the literature — the benefit is invisible or negative at short delays and appears only at
educationally realistic retention intervals.

**Karpicke & Roediger (2008, *Science*, 10.1126/science.1152408)** showed that once an item has
been recalled correctly, *further study* has essentially no effect on delayed recall while
*further testing* has a large positive effect. Critically, "students' predictions of their
performance were uncorrelated with actual performance" — the metacognitive failure is part of the
finding, not an aside.

### Meta-analytic magnitudes

| Meta-analysis | Corpus | Effect | Notes |
|---|---|---|---|
| Rowland (2014), *Psych. Bulletin*, 10.1037/a0037559 | lab-dominated | **g = 0.50, 95% CI [0.42, 0.58]** | I² = 84%. Recall tests > recognition tests. Feedback matters: unsuccessful retrieval without feedback yields little or negative benefit. |
| Adesope, Trevisan & Sundararajan (2017), *RER*, 10.3102/0034654316689306 | practice testing vs. all controls | **g = 0.61** overall; **g = 0.51 vs. restudy**; **g = 0.93 vs. no activity** | The 0.93 is a floor-effect comparison; 0.51 is the honest number. |
| Yang, Luo, Vadillo, Yu & Shanks (2021), *Psych. Bulletin*, 10.1037/bul0000309 | **222 studies, 48,478 students, classroom settings** | **g = 0.499, 95% CI [0.442, 0.557]** | I² = 88%. The single best applied estimate. Moderated by control-condition strategy, test-format consistency, feedback provision, repetitions, and design. |
| Pan & Rickard (2018), *Psych. Bulletin*, 10.1037/bul0000151 | **transfer**: 192 effect sizes, 122 experiments, N = 10,382 | **d = 0.40, 95% CI [0.31, 0.50]** | Transfer is real but weaker than retention. Strongest across test formats and to application/inference questions; **weakest to rearranged stimulus–response items, to untested material seen during study, and to worked-example problems**. PET-PEESE and selection-method corrections left moderators largely intact but the intercept estimate was more sensitive. |
| Agarwal, Nunes & Blunt (2021), *EPR*, 10.1007/s10648-021-09595-9 | 50 classroom experiments, 49 effect sizes, n = 5,374 | 57% of effects medium or large | **Only 6% of experiments were conducted in non-WEIRD countries.** |

### Boundary conditions — say these out loud

- **Delay is required.** At immediate test, restudy often wins (Roediger & Karpicke, 2006, Exp. 1).
- **Feedback is near-mandatory when retrieval fails.** Rowland (2014) and Fiechter & Benjamin
  (2018): unsuccessful retrieval without corrective feedback produces little or negative benefit.
- **Material complexity is disputed.** van Gog & Sweller (2015, *EPR*, 10.1007/s10648-015-9310-x)
  argued the testing effect *decreases or disappears* as element interactivity rises;
  Karpicke & Aue (2015, *EPR*, 10.1007/s10648-015-9309-3) rebutted with "The Testing Effect Is
  Alive and Well with Complex Materials." The dispute is unresolved. Pan & Rickard's finding that
  transfer is weakest to worked-example problems is at least partially consistent with van Gog &
  Sweller.
- **Engagement is a hard prerequisite.** A 2026 pair of Prolific experiments (PMC12894256) with
  delayed post-tests, corrective feedback, attention checks and fair pay found **no testing effect
  at all**, and attributed it to insufficient sustained engagement in crowdsourced settings. This
  is directly relevant to AI-mediated self-study: the effect is contingent on effortful,
  attentive retrieval, not on the surface form of "being quizzed."
- **A design confound in the founding study.** Soderstrom, Kerr & Bjork (2016, *Psych. Science*,
  10.1177/0956797615617778) replicated Karpicke & Roediger (2008) in a between-subjects design,
  but when spacing differences inherent to that design were controlled within-subjects,
  **both repeated testing and repeated restudy improved learning**, and learners' metacognitive
  awareness improved too. The testing effect survives; the strong "restudy does literally nothing"
  claim does not.

---

## 2. Spaced / distributed practice — **Grade A**

### The canonical meta-analysis

**Cepeda, Pashler, Vul, Wixted & Rohrer (2006, *Psych. Bulletin*, 10.1037/0033-2909.132.3.354)**:
839 assessments across 317 experiments in 184 articles. Of **271 massed-vs-spaced comparisons,
only 12 showed no effect or a negative effect from spacing.** Even at retention intervals under
one minute, spacing improved final-test performance by ~9 percentage points. There is no retention
interval at which massing is preferable. Crucially, the inter-study interval (ISI) and retention
interval (RI) interact: the optimal ISI grows as RI grows.

### The gap-ratio result (the practically important one)

**Cepeda, Vul, Rohrer, Wixted & Pashler (2008, *Psych. Science*,
10.1111/j.1467-9280.2008.02209.x)**: N > 1,350, gaps up to 3.5 months, final test up to 1 year
later. Final performance rises then falls as the gap increases — a "temporal ridgeline." Expressed
as a proportion of the test delay, the **optimal gap declines from roughly 20–40% of a 1-week
delay to roughly 5–10% of a 1-year delay.** The authors' conclusion: "many educational practices
are highly inefficient."

### Other magnitudes

- **Donovan & Radosevich (1999, *JAP*, 10.1037/0021-9010.84.5.795)**, "Now you see it, now you
  don't": overall **d ≈ 0.46**, but strongly moderated by task complexity — small for complex
  motor tasks (**d = 0.11–0.42**), much larger for simple verbal material. The title is the
  finding: spacing is not scale-free.
- **Classroom meta-analysis (2025, PMC12189222)**: 22 reports, 31 effect sizes, N > 3,000,
  curriculum-relevant materials and timescales: **d = 0.54, 95% CI [0.31, 0.77]**. Larger effects
  with longer retention intervals, higher education levels, and *fewer* re-exposures.
- **Latimier, Peyre & Ramus (2020, *EPR*, 10.1007/s10648-020-09572-8)**: spaced vs. massed
  *retrieval practice*, 39 effect sizes: **g = 0.74**. And — importantly — expanding vs. uniform
  spacing schedules, 54 effect sizes: **g = 0.034, n.s.** **There is no meta-analytic support for
  the widely-held belief that intervals must expand.** This directly contradicts the design
  folklore embedded in most spaced-repetition software (SM-2, Anki-style expanding intervals).
  Their moderator analysis found expansion helps only as the number of retrieval exposures per
  item grows.

### Practical translation

For a target retention of one month, gaps of ~1–3 days; for one year, gaps of ~2–5 weeks. Uniform
scheduling is not meaningfully worse than expanding scheduling.

---

## 3. Interleaving vs. blocked practice — **Grade B (helps in specific places, hurts in others)**

**Brunmair & Richter (2019, *Psych. Bulletin*, 10.1037/bul0000209)**: 59 studies, 238 effect sizes
nested in 158 samples. Overall **Hedges' g = 0.42** (I² = 77%). The moderator structure is the
whole story:

| Material | Effect |
|---|---|
| Paintings / visual category induction | **g = 0.67** |
| Mathematics tasks | **g = 0.34** |
| Expository texts | n.s. |
| Tastes | n.s. |
| **Words (vocabulary-like items)** | **g = −0.39 — blocking is better** |

Multiple meta-regression: interleaving works better when **between-category similarity is high,
within-category similarity is low, and material is more complex**. The mechanism is discrimination
(the attentional-bias / sequential-attention account), not spacing per se.

**Firth, Rivers & Boyle (2021, *Review of Education*, 10.1002/rev3.3266)**: 26 studies, 17 in the
meta-analysis (32 datasets). Memory benefits **up to g = 0.65**, transfer to novel items **up to
g = 0.66**; greatest when differences between items are subtle; extends to delayed tests. Their
own caveat: "the literature is dominated by laboratory studies of university undergraduates."

**The best classroom evidence** is **Rohrer, Dedrick, Hartwig & Cheung (2020, *JEP*,
10.1037/edu0000367)**: preregistered cluster RCT, 54 seventh-grade mathematics classes, 4 months
of interleaved vs. blocked assignments, then an **unannounced test one month later**:
**61% vs. 38%, d = 0.83**. Teachers implemented it without training and endorsed it before seeing
results. This is one of the strongest classroom results in the whole literature.

**Where it hurts:** rote paired-associate / vocabulary learning (g = −0.39). Also note the
practical cost — interleaved practice feels harder and slower during acquisition (see §9).

---

## 4. Worked examples and the expertise reversal effect — **Grade A for the reversal itself**

### Worked examples

Origin: Sweller & Cooper's worked-example effect; formalized in Sweller, van Merriënboer & Paas
(1998; updated 2019, 10.1007/s10648-019-09465-5). Studying worked solutions beats solving
equivalent problems for novices, because means–ends problem solving consumes working memory
without building schemas.

**Barbieri, Miller-Cotto, Clerjuste & Chawla (2023, *EPR*, 10.1007/s10648-023-09745-1)** — the
first proper meta-analysis, screening 8,033 abstracts, yielding 43 articles / 55 studies /
181 effect sizes, analysed with robust variance estimation: **g = 0.48**. Two counterintuitive
moderators:

- **Correct examples alone outperformed incorrect-only or correct+incorrect combinations.**
- **Pairing examples with self-explanation prompts significantly *reduced* the effect** —
  a negative moderator. The authors: "pairing examples with self-explanation prompts may not be a
  fruitful design modification."

Related: **Alfieri, Brooks, Aldrich & Tenenbaum (2011, *JEP*, 10.1037/a0021017)**: 164 studies.
Unassisted discovery is *worse* than explicit instruction (**d = −0.38**, 580 comparisons); but
*assisted/enhanced* discovery — with feedback, worked examples, scaffolding, elicited explanations
— beats other instruction (**d = 0.30**, 360 comparisons). See also Kirschner, Sweller & Clark
(2006, *Educational Psychologist*, 10.1207/s15326985ep4102_1).

### Expertise reversal — the governing constraint for "zero to hero" design

**Kalyuga, Ayres, Chandler & Sweller (2003, *Educational Psychologist*,
10.1207/s15326985ep3801_4)** named the effect: instructional support that helps novices becomes
*redundant and harmful* as expertise grows, because the learner must reconcile the provided
guidance with an already-adequate internal schema.

**The definitive quantification is new: Tetzlaff, Simonsmeier, Peters & Brod (2025,
*Learning and Instruction*, 10.1016/j.learninstruc.2025.102142)** — 60 experimental studies,
176 effect sizes, N = 5,924, PRISMA, metafor with dependency correction:

| Comparison | Effect |
|---|---|
| **Low prior knowledge**: high-assistance vs. low-assistance instruction | **d = 0.505, 95% CI [0.260, 0.750]**, k = 88, j = 60, I² = 90.9% |
| **High prior knowledge**: high-assistance vs. low-assistance instruction | **d = −0.428, 95% CI [−0.647, −0.209]**, k = 88, I² = 87.6% |
| **The reversal itself (interaction)** | **d = 0.971, 95% CI [0.631, 1.312]** |

Four things follow, and they matter enormously for progression design:

1. **The reversal is real and large** — nearly a full standard deviation of interaction.
2. **It is asymmetric.** Giving novices support helps more (+0.505) than withholding support from
   experts helps them (+0.428). The authors' explicit instructional implication: *"rather provide
   assistance than to withhold it when in doubt."* A system that errs toward scaffolding does less
   damage than one that errs toward withdrawal.
3. **Moderators**: significant by educational status (strongest in higher education, weak/unclear
   in primary school), by content area (strong in law/business/crafts and STEM, **weak in language
   learning and humanities**), and by how prior knowledge was assessed.
4. **Heterogeneity is ~90%.** The reversal point is not a fixed threshold; it is
   learner-and-domain-specific. Any system claiming to detect "when to fade scaffolding" must
   demonstrate it empirically, not assume a schedule.

Corroborating primary studies: Richter, Scheiter & Eitel (2018, *JEP*) — an 8th-grade quasi-
experimental field study where multimedia integration signals helped low-prior-knowledge learners
and were **detrimental** to high-prior-knowledge learners; Rey & Buchwald (2011, *JEP: Applied*)
and Rey & Fischer (2013, *Instructional Science*) — experimentally induced expertise, reversal
replicated for transfer (not always for retention).

---

## 5. Cognitive load theory — **Grade A for the design effects, Grade C for the three-way split**

### What is solid

The *instructional design effects* derived from CLT replicate well and are independently
meta-analysed: worked-example effect (g = 0.48), split-attention / spatial contiguity (g = 0.63),
modality (g = 0.20–0.72), redundancy (direction-dependent), expertise reversal (interaction
d = 0.971), segmenting (g = 0.34). Working memory limits are real (Cowan, 2001, *BBS*: ~4 chunks,
not 7).

### What is not solid: the intrinsic / extraneous / germane trichotomy

Report this plainly. The three-way decomposition is a **theoretical taxonomy that has never been
cleanly operationalized as three separately measurable, additive quantities.**

- **Kalyuga (2011, *EPR*, 10.1007/s10648-010-9150-7), "Cognitive Load Theory: How Many Types of
  Load Does It Really Need?"** — argues germane load is not independently identifiable and that
  the framework risks unfalsifiability: any result can be re-described post hoc as a shift between
  load types.
- **de Jong (2009/2010, *Instructional Science*, 10.1007/s11251-009-9110-0)**, "some food for
  thought" — the central critique of circularity: load is inferred from performance and then used
  to explain performance. Moreno (2009) replies in the same issue.
- **Schnotz & Kürschner (2007, *EPR*, 10.1007/s10648-007-9053-4)**, "A Reconsideration of
  Cognitive Load Theory."
- **Anmarkrud, Andresen & Bråten (2019, *Educational Psychologist*,
  10.1080/00461520.2018.1554484)** — conceptual and measurement issues; the field largely relies
  on single-item subjective mental-effort ratings (Paas scale) or the Leppink et al. (2013,
  *Behavior Research Methods*) three-factor instrument, whose factor structure does not cleanly
  recover the theoretical trichotomy.
- **Sweller, van Merriënboer & Paas (2019)** themselves reconceptualized germane load: it is no
  longer treated as an independent additive source of load but as working-memory resources
  *redirected to* intrinsic load. Consumers of CLT frequently cite the 2019 paper while still
  using the old additive three-bucket model, including in measurement.
- Debate continues: Greenberg & Zheng (2022), "Revisiting the debate on germane cognitive load
  versus germane resources"; Kalyuga & Plass (2025), "Reconceptualizing Cognitive Load Theory."

### The empirical tell

**Noetel et al. (2021)** found that multimedia design interventions improved *learning* at
g = 0.38 but improved measured *cognitive load management* at only **g = 0.22, 95% CI
[0.04, 0.40], k = 68**. The proposed mediator moves less than the outcome. The design principles
work; the load-mediation story is weakly instrumented.

**Verdict for the survey:** cite CLT for its design predictions, which are excellent. Do not cite
"reduces extraneous cognitive load" as if it were a measured quantity, and do not treat germane
load as a design target you can dial up.

---

## 6. Mayer's multimedia principles — **Grade A/B per principle, but the canonical effect sizes are inflated**

### Use the independent synthesis, not Mayer's own tallies

The standard citations for these principles are Mayer's own chapter-length tallies of median
effect sizes across experiments largely from his own lab. The best *independent* synthesis is:

**Noetel, Griffith, Delaney & Harris (2021/2022, *Review of Educational Research*,
10.3102/00346543211052329)** — an overview of reviews with meta-meta-analysis:
**29 systematic reviews, 1,189 primary studies, 78,177 participants**, quality-appraised with an
abbreviated AMSTAR2. Across the 11 largest reviews (**808 effect sizes, 66,553 participants**),
the average effect of multimedia design principles on learning was **g = 0.38, 95% CI
[0.27, 0.49]**, with the specific principle explaining essentially all between-review variance.

They also state the credibility problem directly: meta-analytic evidence substantiates stronger
causal claims "than reviews that either present a subset of confirmatory papers (Sweller et al.,
2019) or pool effects from an unrepresentative sample of studies (Mayer, 2008)."

### Per-principle table (best available review for each, via Noetel et al.)

| Principle | Effect on learning | Source review | Notes |
|---|---|---|---|
| **Captioning L2 video** | **g = 0.99 [0.60, 1.38]**, k = 15 (comprehension); g = 0.87 [0.58, 1.15], k = 10 (vocabulary) | Montero Perez et al. (2013) | Largest single effect in the corpus |
| **Contiguity (overall)** | **g = 0.74 [0.67, 0.82]**, k = 46 | Ginns (2006) | |
| **Temporal contiguity** | **g = 0.78 [0.64, 0.92]**, k = 13 | Ginns (2006) | Small k |
| **Spatial contiguity / split attention** | **g = 0.63 [0.55, 0.71]**, k = 58, n = 2,426 | Schroeder & Cenkci (2018), 10.1007/s10648-018-9435-9 | Validated by eye-tracking |
| **Signaling** | **g = 0.43 [0.35, 0.50]**, k = 209 | Schneider et al. (2018) | Load g = 0.25; motivation g = 0.13; fixations g = 0.39. **Richter, Scheiter & Eitel (2016, *Educational Research Review*, 10.1016/j.edurev.2015.12.003) report r = 0.17 and find the benefit is concentrated in low-prior-knowledge learners** — i.e. signaling is subject to expertise reversal |
| **Modality** | **g = 0.38 [0.33, 0.43]**, k = 86 → **g = 0.20 [0.15, 0.25]** after publication-bias adjustment (Reinwein, 2012); **d = 0.72 [0.52, 0.92]**, k = 39 (Ginns, 2005, 10.1016/j.learninstruc.2005.07.001) | two reviews | **Two meta-analyses of the same principle differ by a factor of ~2–3.** Report the range, not the flattering number. |
| **Segmenting** | **g = 0.34 [0.30, 0.38]**, k = 123 | Rey et al. (2019) | System-segmented **g = 0.41** > learner-segmented **g = 0.20**. Cognitive load g = 0.23. **Segmenting increases time on task (g = 0.92)** — a real cost |
| **Personalization (conversational style)** | **g = 0.33 [0.23, 0.44]**, k = 55 | Ginns, Martin & Marsh (2013), 10.1007/s10648-013-9228-0 | Their own paper: retention d = 0.30, transfer d = 0.54; friendliness d = 0.46; effective processing d = 0.62; but **interest d = 0.15 n.s. and learning-assistance d = 0.16 n.s.**, and **effects are small and non-significant in studies longer than 35 minutes** — a hard boundary condition largely ignored in citation |
| **Coherence / removing seductive details** | **g = 0.33 [0.18, 0.48]**, k = 68 | Sundararajan & Adesope (2020), 10.1007/s10648-020-09522-4 | Persistent on-screen details **g = 0.43**; transient details **g = 0.12 n.s.** — the harm depends on persistence |
| **Verbal redundancy** | **g = 0.15 [0.08, 0.22]**, k = 57 | Adesope & Nesbit (2012) | **Direction-dependent: adding text to audio g = 0.29 [0.20, 0.39]; adding audio to text g = −0.04 [−0.14, 0.06] n.s.** The "redundancy principle" as usually stated ("never duplicate") is wrong in one direction |
| **Animation** | **g = 0.23 [0.12, 0.33]** (Berney & Bétrancourt, 2016) | | Meaningful/representational animation **g = 0.40**; **decorative animation g = −0.05 n.s.** (Höffler & Leutner, 2007) |
| **Pedagogical agents** | **g = 0.19 [0.12, 0.27]**, k = 43 (Schroeder et al., 2013) | | Agents that signal: g = 0.28; **3D agents g = 0.11 n.s.**; 2D g = 0.38 |
| **Anthropomorphics / pleasant colour** | **g = 0.35 [0.29, 0.42]**, k = 45 (Brom et al., 2018) | | Intrinsic motivation g = 0.25; perceived difficulty g = 0.21 |
| **Pre-training** | **Not covered by any independent systematic review in Noetel's corpus** | — | Mayer's own summaries report medians around d ≈ 0.75 over ~16 comparisons, but these are lab-of-origin tallies, not systematic reviews. **Treat pre-training as plausible but under-evidenced relative to the others.** |

### Cross-cutting moderators (Noetel et al.)

- **Pacing**: design matters more when material is **system-paced** (lecture/video, g = 0.41) than
  **learner-paced** (website, g = 0.27). Directly relevant to AI: chat/self-paced interfaces are
  the *lower*-payoff regime for multimedia design fixes.
- **Complexity**: design matters far more for complex material (high element interactivity,
  **g = 0.70**) than simple material (**g = 0.20**).
- **Prior knowledge did *not* consistently moderate effects across reviews** (p = 0.14). This is
  in tension with the expertise-reversal literature (§4) and with Richter et al.'s signaling
  result. The honest reading: the reversal is well established for *assistance/guidance*
  manipulations (Tetzlaff et al., d = 0.971) but is not reliably detectable across the broad
  multimedia-design corpus.

---

## 7. Bloom's "2 sigma" — **Grade F as usually stated**

### The original claim

Bloom (1984, *Educational Researcher*, 10.3102/0013189X013006004), "The 2 Sigma Problem":
one-to-one tutoring combined with mastery learning produced achievement about **two standard
deviations** above conventional group instruction, framed as a challenge to find scalable group
methods that match it.

### What it actually rests on

Per **von Hippel (2024), "Two-Sigma Tutoring: Separating Science Fiction from Science Fact,"
*Education Next***:

- The empirical base is **two University of Chicago doctoral dissertations** (Joanne Anania;
  Arthur J. Burke), not credited as co-authors.
- **Small samples of 4th, 5th and 8th graders**, **three-week** experiments, on **probability**
  (grades 4–5) and **cartography** (grade 8).
- Outcomes measured on **narrow, specialized tests written by the study authors** on unfamiliar
  material.
- The "tutoring" condition was a **bundle**: one-to-one tutoring + intensively coached tutors
  (trained in cueing, summarizing, step-by-step and inquiry techniques) + **mastery-style repeated
  quizzing with corrective feedback and retesting** + tutoring that **replaced** rather than
  supplemented classroom instruction.

### Why the number does not survive

| Evidence | Result |
|---|---|
| Same experiments, narrow vs. broad tests | **0.84 SD on narrow tests vs. 0.27 SD on broad standardized tests** |
| Contribution of the quiz–feedback–retest loop | von Hippel estimates roughly **half** the 2σ effect; Anania's tutored students scored ~30 percentage points higher on retest than initial test |
| Cohen, Kulik & Kulik (1982, *AERJ*, 10.3102/00028312019002237), 65 studies | mean tutoring effect ≈ **0.33 SD**; **only one of 65 studies reported a two-sigma effect** |
| Nickow, Oreopoulos & Quan (2023, *AERJ*, 10.3102/00028312231208687), meta-analysis of preK–12 tutoring field experiments | pooled **ES = 0.288 SD (SE = 0.029)**; the 2020 NBER version reports ~0.37 for a somewhat different sample. **Across 96 randomized studies, none produced a two-sigma effect.** |
| VanLehn (2011) on adult human tutoring | **d = 0.79**, not 2.0 (§8) |
| Real-world programs | Chicago supplemental tutoring 2008–12: **0.06 SD**. Saga Education high-dosage math tutoring: **0.16–0.37 SD** (described by its own authors as "sizable," doubling or tripling annual gains) |

### The mastery-learning half of the claim also failed replication

**Slavin (1987, *RER*, 10.3102/00346543057002175), "Mastery Learning Reconsidered"** — a
best-evidence synthesis of group-based mastery learning in real schools over ≥4 weeks found
"essentially no evidence" of effectiveness on **standardized** achievement measures; effects on
**experimenter-made** measures were positive but moderate with little evidence of maintenance.
Kulik, Kulik & Bangert-Drowns (1990, *RER*, 10.3102/00346543060002265) found positive effects
across 108 evaluations, but this rested heavily on experimenter-made tests; the Slavin–Guskey–
Kulik exchange (RER 1987–1990) is the record of an unresolved methodological dispute in which the
test-alignment issue was never fully answered.

### How to state it in the survey

> Bloom's 2σ figure is a *ceiling estimate from two small, short, unreplicated dissertation
> studies using author-written tests of unfamiliar material, in which tutoring was confounded with
> mastery testing, corrective feedback, tutor training, and replacement of regular instruction.*
> The best modern estimate for well-designed intensive tutoring measured on broad tests is
> **about one-third of a standard deviation** (von Hippel, 2024; Nickow et al., 2023). Any AI
> system benchmarked against "2 sigma" is being benchmarked against a number that human tutoring
> itself has never reproduced.

Also relevant: **Kraft (2020)** — most education interventions produce effects of **0.10 SD or
less** on broad measures; von Hippel argues Bloom's essay "helped to anchor education researchers'
expectations for unrealistically large effect sizes."

---

## 8. Intelligent tutoring systems — **Grade B: real, moderate, and dependent on the comparison**

| Study | Corpus | Result |
|---|---|---|
| **VanLehn (2011), *Educational Psychologist*, 10.1080/00461520.2011.611369** | review of human/computer/no-tutoring comparisons | Widely believed values were d ≈ 0.3 (answer-based CAI), 1.0 (ITS), 2.0 (human tutors). **The review did not confirm these.** Human tutoring: **d = 0.79**. ITS (step-based/substep): **d = 0.76**. The "interaction plateau": going finer than step-based granularity buys little |
| **Kulik & Fletcher (2016), *RER*, 10.3102/0034654315581420** | 50 controlled evaluations | **median ES = 0.66** (50th → 75th percentile). But **"the amount of improvement depended to a great extent on whether improvement was measured on locally developed or standardized tests."** Six evaluations with non-conventional controls and four with flawed implementations showed **small** effects |
| **Ma, Adesope, Nesbit & Liu (2014), *JEP*, 10.1037/a0037123** | 107 effect sizes, N = 14,321 | vs. teacher-led large-group **g = 0.42**; vs. non-ITS computer-based instruction **g = 0.57**; vs. textbooks/workbooks **g = 0.35**; **vs. individualized human tutoring g = −0.11 (n.s.)**; **vs. small-group instruction g = 0.05 (n.s.)** |
| **Steenbergen-Hu & Cooper (2014), *JEP*, 10.1037/a0034752** — college | 35 reports, 39 studies, 22 ITS | **g = 0.32 to 0.37**. Less effective than human tutoring; outperformed all other comparisons. **"Effectiveness in earlier studies appeared to be significantly greater than in more recent studies"** |
| **Steenbergen-Hu & Cooper (2013), *JEP*, 10.1037/a0032447** — K–12 mathematics | | **"ITS had no negative and perhaps a small positive effect."** Effectively near zero. Effects were *larger* for the general population than for low achievers |

### The honest synthesis

1. ITS effects are **0.3–0.7**, with the higher figures driven by locally-aligned tests and by
   weak comparison conditions.
2. **ITS ≈ human tutoring** in head-to-head comparisons (Ma et al.: g = −0.11 n.s.;
   VanLehn: 0.76 vs 0.79) — but that is only impressive if you remember that human tutoring itself
   is ~0.3–0.8, not 2.0.
3. **The K–12 mathematics result is close to null.** This is the population most often invoked in
   AI-tutoring pitches.
4. **Effects have declined over time** (Steenbergen-Hu & Cooper, 2014), which is the classic
   signature of better-controlled comparisons and stronger control conditions replacing early
   optimistic evaluations.

**Benchmark for AI claims:** an AI tutor that demonstrates **d ≈ 0.4 on a test it did not help
design, against a genuinely active control, at a delayed post-test** would be at the top of this
literature. Claims above ~0.8 should be presumed to reflect aligned tests or weak controls until
shown otherwise.

---

## 9. Desirable difficulties — **Grade A for the phenomenon, Grade A for the misprediction**

**Bjork & Bjork's** framing, developed in **Soderstrom & Bjork (2015, *Perspectives on
Psychological Science*, 10.1177/1745691615569000), "Learning Versus Performance"**: what is
observable during instruction is *performance*; what matters is *learning* (relatively permanent
changes supporting long-term retention and transfer). Manipulations can have **opposite effects on
the two**. Retrieval practice, spacing, interleaving, generation, and varied practice all slow
acquisition while improving retention.

### Learners systematically mispredict this

- **Karpicke & Roediger (2008, *Science*)**: students' predictions of performance were
  **uncorrelated** with actual performance.
- **Kornell & Bjork (2008, *Psych. Science*, 10.1111/j.1467-9280.2008.02127.x)**: interleaved
  ("spaced") study of paintings by artist beat blocked study for inductive category learning —
  yet "participants rated massing as more effective than spacing, **even after their own test
  performance had demonstrated the opposite**."
- **Kornell, Castel, Eich & Bjork (2010, *Psychology and Aging*, 10.1037/a0017807)**: replicated
  in both young and older adults; the misprediction persisted.
- **Koriat & Bjork (2005, *JEP:LMC*, 10.1037/0278-7393.31.2.187)**: the **foresight bias** —
  judgments of learning are made in the presence of information that will be absent at test,
  instilling an unwarranted sense of competence.
- **Deslauriers, McCarty, Miller & Callaghan (2019, *PNAS*, 10.1073/pnas.1821936116)**: randomized
  comparison of passive lecture vs. active learning with identical materials —
  **students in the active classroom learned more but felt they learned less**, mediated by
  increased cognitive effort. The authors recommend explicitly intervening on the misperception.

### The critical boundary: not all difficulty is desirable

The difficulty must engage retrieval/discrimination processes the learner can actually complete.
Where the learner lacks the prior knowledge to succeed, added difficulty is simply load — which is
exactly the novice half of the expertise-reversal result (**Tetzlaff et al., 2025: novices gain
d = 0.505 from *more* assistance**). "Desirable difficulty" and "expertise reversal" are the same
constraint viewed from opposite ends.

**Direct implication for AI:** any system that optimizes for learner-reported satisfaction, felt
fluency, or in-session performance will systematically select *against* the interventions with the
best long-term evidence. This is a measurable, predictable failure mode, not a hypothetical one.

---

## 10. Learning styles — **Grade F. There is no credible evidence.**

### The evidential situation

**Pashler, McDaniel, Rohrer & Bjork (2008/2009, *Psychological Science in the Public Interest*,
10.1111/j.1539-6053.2009.01038.x)** were commissioned to determine whether learning-styles-based
instruction is supported. Their finding: credible validation of the **meshing hypothesis**
(instruction should match assessed style) requires a **crossover interaction** design — style A
learners do better with method A, style B learners do better with method B. Almost no studies used
that design; the few that did produced results **contradicting** the meshing hypothesis.

### Subsequent direct tests, all null

- **Rogowsky, Calhoun & Tallal (2015, *JEP*, 10.1037/a0037478)**, "Matching Learning Style to
  Instructional Method": no interaction between assessed style and instructional modality on
  comprehension.
- **Husmann & O'Loughlin (2019, *Anatomical Sciences Education*, 10.1002/ase.1777)**, "Another
  Nail in the Coffin for Learning Styles?": **N = 426** anatomy students. Most students did **not**
  study in ways that matched their VARK profile; **VARK scores were uncorrelated with course
  performance**; alignment of strategy with VARK was uncorrelated with outcome. What *did* predict
  grades were specific study strategies (e.g. virtual-microscope use) **irrespective of VARK**.
- **Melzner & Kappes (2024, *Instructional Science*, 10.1007/s11251-024-09689-1)**: **N = 222**
  prospective teachers, revised Verbalizer–Visualizer Questionnaire, ecologically valid course
  materials, adequately powered. **No interaction** between presentation mode and style on
  learning; styles also failed to predict judgments of learning or confidence.

### The belief persists anyway

- **Newton & Salvi (2020, *Frontiers in Education*, 10.3389/feduc.2020.602451)**: systematic review
  of **37 studies, 15,405 educators, 18 countries, 2009–2020**. Self-reported belief in matching
  instruction to learning styles: **weighted 89.1%** (range 58–97.6%). **No decline over time.**
  **95.4% of trainee teachers** agreed matching is effective.
- **Newton et al. (2021, *Frontiers in Human Neuroscience*, 10.3389/fnhum.2021.708540)**: **91% of
  112 recent health-professions education research papers** were premised on learning styles being
  a useful approach — meaning an educator who *searches the literature* is given a consistent but
  inaccurate endorsement.

### What the evidence *does* support for adaptation

This matters directly for any "grill the learner to find their best mode of learning" feature. The
adaptations with real evidence are:

| Adaptation target | Evidence |
|---|---|
| **Prior knowledge** | The single best-supported basis for adaptation. Tetzlaff et al. (2025): interaction **d = 0.971**. Richter et al. (2016): signaling helps low-prior-knowledge learners, harms high |
| **Task/material properties** | Interleaving works when between-category similarity is high and within-category similarity is low (Brunmair & Richter, 2019); design principles matter far more for complex, system-paced material (Noetel et al., 2021: g = 0.70 vs 0.20) |
| **Self-regulation and strategy use** | SRL training g = 0.38 (Theobald, 2021, §12); the strategies themselves (§12) |
| **Motivation type** | Intrinsic and identified regulation predict achievement and persistence; external regulation does not (Howard et al., 2021, §11) |
| **Broad learner characteristics** | Schneider & Preckel (2017, *Psych. Bulletin*, 10.1037/bul0000098): **38 meta-analyses, 105 correlates, 3,330 effect sizes, ~2 million students**. High achievers are characterized by **self-efficacy, prior achievement and intelligence, conscientiousness, and goal-directed strategy use**. Learning style is not on the list. Notably, **instructional/communication technology showed comparably weak effects that did not increase over time** |

**Recommended framing for the survey:** a diagnostic interview that infers *what the learner
already knows*, *what they can do unaided*, *how they regulate study*, and *what they find
valuable* is well supported. A diagnostic that assigns a sensory-modality label and then matches
content to it is implementing a construct with a 40-year null record and ~89% practitioner belief
— a textbook case of an AI system automating a myth at scale.

---

## 11. Motivation and engagement — **Grade A for SDT correlations, Grade C for gamification**

### Self-determination theory

- **Howard, Bureau, Guay & Chong (2021, *Perspectives on Psychological Science*,
  10.1177/1745691620966789)**: **344 samples, 223,209 participants**, 26 outcomes. **Intrinsic
  motivation** relates to success and well-being; **identified regulation** (personal value) is
  the strongest predictor of persistence; **introjected regulation** predicts persistence *and*
  ill-being; **external regulation (rewards/punishment avoidance) was not associated with
  performance or persistence** and was associated with decreased well-being; amotivation predicts
  poor outcomes.
- **Bureau, Howard, Chong & Guay (2021, *RER*, 10.3102/00346543211042426)**: 144 studies,
  >79,000 students. **Competence** is the strongest predictor of self-determined motivation, then
  **autonomy**, then **relatedness**. Teacher autonomy support > parental autonomy support.
- **Deci, Koestner & Ryan (1999, *Psych. Bulletin*, 10.1037/0033-2909.125.6.627)**: 128 studies.
  Tangible expected rewards undermine free-choice intrinsic motivation — engagement-contingent
  **d = −0.40**, completion-contingent **d = −0.36**, performance-contingent **d = −0.28**;
  self-reported interest also undermined (d = −0.15 to −0.17). **Positive feedback enhances**
  (free-choice d = 0.33, interest d = 0.31). This meta-analysis is contested — see the
  simultaneously published critique by **Lepper, Henderlong & Gingras (1999, same issue,
  10.1037/0033-2909.125.6.669)**, "Uses and abuses of meta-analysis," and the long-running
  Cameron/Eisenberger dispute. The undermining effect is real but its magnitude and generality are
  argued over.

### Gamification — report the mixed picture, not the headline

| Meta-analysis | Corpus | Result |
|---|---|---|
| **Sailer & Homner (2020, *EPR*, 10.1007/s10648-019-09498-w)** | cognitive k = 19, N = 1,686; motivational k = 16, N = 2,246; behavioral k = 9, N = 951 | cognitive **g = 0.49 [0.30, 0.69]**; motivational **g = 0.36 [0.18, 0.54]**; behavioral **g = 0.25 [0.04, 0.46]**. **Critically: the cognitive effect was stable in a subsplit of methodologically rigorous studies; the motivational and behavioral effects were *not* stable.** |
| **Huang, Ritzhaupt, Sommer & Zhu (2020, *ETR&D*, 10.1007/s11423-020-09807-z)** | 30 studies, N = 3,083 | **g = 0.464 [0.244, 0.684]** |
| **Bai, Hew & Huang (2020, *Educational Research Review*, 10.1016/j.edurev.2020.100322)** | 30 interventions, 24 studies, N = 3,202 | **g = 0.504 [0.284, 0.723]** |

**Why this is Grade C despite three positive meta-analyses:**

1. **The corpora are tiny** — k = 9–30 studies, N ≈ 1,000–3,200. Compare: retrieval practice,
   222 studies / 48,478 students.
2. **The motivational claim — the entire rationale for gamification — is the least stable result**
   (Sailer & Homner's own rigor subsplit).
3. **Novelty confound.** Short interventions in a novel medium reliably inflate effects
   (Clark, 1983); Sailer & Homner explicitly flag this.
4. **Theoretical conflict with SDT.** Points, badges and leaderboards are performance- and
   completion-contingent tangible rewards — precisely the class Deci et al. (1999) found undermines
   intrinsic motivation (d = −0.28 to −0.40). Bai et al.'s own paper opens by noting gamification
   "has attracted considerable controversy" and derogatory labels ("exploitationware").
5. Sailer & Homner found **game fiction** and **competition combined with collaboration** to be
   the significant moderators for behavioral outcomes — i.e. the effective ingredients are the
   social/narrative ones, not the points.

### Curiosity and interest

- **Kang, Hsu, Krajbich, Loewenstein et al. (2009, *Psych. Science*,
  10.1111/j.1467-9280.2009.02402.x)**: curiosity while reading trivia questions correlated with
  caudate (reward-anticipation) activity; participants spent scarce resources to resolve
  curiosity; **higher initial curiosity predicted better recall of surprising answers 1–2 weeks
  later**.
- **Gruber, Gelman & Ranganath (2014, *Neuron*, 10.1016/j.neuron.2014.08.060)**: curiosity states
  enhance hippocampus-dependent learning of **both target and incidental** information via the
  dopaminergic circuit. Framework update: Gruber & Ranganath (2019, *TiCS*), the PACE framework.
  These are small-sample fMRI studies — treat as mechanism, not as an effect-size benchmark.
- **Hidi & Renninger (2006, *Educational Psychologist*, 10.1207/s15326985ep4102_4)**: the
  four-phase model — situational interest can be triggered externally but must be developed into
  individual interest to persist.
- **Harackiewicz, Rozek, Hulleman & Hyde (2012, *Psych. Science*, 10.1177/0956797611435530)**:
  a utility-value intervention delivered to *parents* (two brochures + a website) caused students
  to take nearly **one additional semester** of maths/science in the last two years of high school.
  A cheap, distal, behaviourally-measured motivation effect — a useful contrast to gamification's
  proximal, self-report-heavy evidence base.

---

## 12. Metacognition and self-regulated learning — **Grade A for the deficits, Grade B for the fixes**

### What students actually do vs. what works

**Dunlosky, Rawson, Marsh, Nathan & Willingham (2013, *Psychological Science in the Public
Interest*, 10.1177/1529100612453266)** evaluated 10 techniques for generalizability across
learning conditions, student characteristics, materials, and criterion tasks:

| Utility | Techniques |
|---|---|
| **High** | **Practice testing**, **distributed practice** |
| **Moderate** | Elaborative interrogation, self-explanation, interleaved practice |
| **Low** | **Highlighting/underlining**, **rereading**, summarization, keyword mnemonic, imagery for text |

The two lowest-utility techniques — highlighting and rereading — are the two students report using
most. That gap is the core self-regulation problem.

**Donoghue & Hattie (2021, *Frontiers in Education*, 10.3389/feduc.2021.581216)** meta-analysed the
same ten techniques: **242 studies, 1,619 effects, 169,179 unique participants, overall mean
ES = 0.56**. Distributed practice and practice testing were again highest; underlining and
summarization lowest (though still non-trivial). Two moderators worth reporting: effects were
**much greater for lower-ability than higher-ability students**, and the corpus is dominated by
**surface/factual outcomes** — the authors explicitly caution against extrapolating to deeper,
relational learning.

### Can self-regulation be trained?

**Theobald (2021, *Contemporary Educational Psychology*, 10.1016/j.cedpsych.2021.101976)**:
three-level meta-analysis of extended SRL training programmes, **49 studies, 5,786 participants,
251 effect sizes**:

- Overall **g = 0.38**
- Metacognitive strategies **g = 0.40**; resource management **g = 0.39**; academic performance
  **g = 0.37**; motivation **g = 0.35**; cognitive strategies **g = 0.32**
- Range by specific strategy: **0.23 (rehearsal) to 0.61 (attention/concentration)**
- **Feedback predicted larger training effects** for metacognitive strategies, resource management
  and motivation; cooperative arrangements predicted larger effects for cognitive and metacognitive
  strategies; metacognitively-grounded programmes outperformed cognitively-grounded ones for
  achievement.

So: SRL is trainable at roughly half a testing-effect's worth of gain, and **feedback is the
active ingredient** — an obvious affordance for AI systems.

### The illusion of fluency (the mechanism behind the deficits)

**Bjork, Dunlosky & Kornell (2013, *Annual Review of Psychology*,
10.1146/annurev-psych-113011-143823), "Self-Regulated Learning: Beliefs, Techniques, and
Illusions"** is the canonical synthesis: people hold a faulty mental model of their own learning
and are therefore "prone to both misassessing and mismanaging" it. The specific mechanisms:

- **Fluency misattribution** — ease of processing during study is read as evidence of learning.
  Rereading is maximally fluent and minimally effective.
- **Foresight bias** (Koriat & Bjork, 2005) — judgments made with the answer present.
- **Current-performance anchoring** — in-session accuracy drives judgments of learning even when
  the manipulation improves session performance at the cost of retention (Soderstrom & Bjork,
  2015).
- **Resistance persists after disconfirmation** (Kornell & Bjork, 2008; Kornell et al., 2010;
  Deslauriers et al., 2019).

Remedies with evidence: delayed judgments of learning, cue-only (rather than cue+target) judgments
(Koriat & Bjork, 2006, *Memory & Cognition*), and explicit instruction about the
learning–performance distinction (Deslauriers et al. describe a successful intervention of this
kind).

---

## Cross-cutting cautions for the survey

1. **Heterogeneity dominates.** I² = 84% (Rowland), 88% (Yang et al.), 77% (Brunmair & Richter),
   ~90% (Tetzlaff et al.). Pooled effect sizes in this field are weak predictors of any specific
   implementation. Report ranges and moderators, never single numbers.
2. **Test alignment is the largest single source of inflation.** Documented explicitly for
   Bloom/tutoring (0.84 narrow vs 0.27 broad), for ITS (Kulik & Fletcher: "to a great extent"),
   and for mastery learning (Slavin, 1987). Any evaluation where the system's designers also wrote
   the test should be discounted heavily.
3. **Publication-bias corrections shrink effects.** Modality: 0.38 → 0.20. Most principles in this
   literature have never been corrected.
4. **The lab/classroom gap is systematic.** Lab retrieval-practice effects (g = 0.50–0.61) survive
   into classrooms (g = 0.50), which is unusually good. Interleaving's lab effects (g = 0.42–0.67)
   have exactly *one* large preregistered classroom RCT (Rohrer et al., 2020, d = 0.83). Multimedia
   principles are almost entirely short-duration lab studies — and the personalization principle
   explicitly **fails beyond 35 minutes of instruction**.
5. **WEIRD and undergraduate dominance.** 6% of classroom retrieval-practice experiments were in
   non-WEIRD countries (Agarwal et al., 2021); the interleaving literature is "dominated by
   laboratory studies of university undergraduates" (Firth et al., 2021).
6. **Effects decline as evaluations improve.** Steenbergen-Hu & Cooper (2014) found ITS effects
   significantly larger in earlier studies. Expect the same trajectory for AI tutoring.
7. **The three highest-leverage, best-replicated levers are retrieval practice, distributed
   practice, and prior-knowledge-adaptive scaffolding** — in that order of evidential strength.
   Everything else in this section is either smaller, more bounded, or contested.

---

## Benchmarks the survey should hold AI capabilities to

| Claim an AI system might make | Non-AI baseline it must beat |
|---|---|
| "Personalized tutoring at scale" | Human tutoring d ≈ 0.29–0.37 on broad tests (Nickow et al., 2023; von Hippel, 2024), d = 0.79 in VanLehn's lab-leaning review. **Not 2σ.** |
| "Adaptive/intelligent tutoring" | ITS g = 0.32–0.42 vs. classroom instruction; **g ≈ −0.11 to 0.05 vs. human tutoring or small-group**; near-null in K–12 maths |
| "Generates practice questions" | Practice testing g = 0.50 in classrooms — but only with delay, feedback, and genuine effortful retrieval |
| "Optimal review scheduling" | Spaced practice d = 0.54 in classrooms; optimal gap ≈ 10–20% of the retention interval; **expanding schedules confer no advantage (g = 0.03)** |
| "Adapts to your learning style" | **Zero.** No credible evidence for the meshing hypothesis (Pashler et al., 2008; Rogowsky et al., 2015; Husmann & O'Loughlin, 2019; Melzner & Kappes, 2024) |
| "Adapts to your level" | Prior-knowledge adaptation is the real thing: interaction **d = 0.971** (Tetzlaff et al., 2025). Asymmetric — err toward scaffolding |
| "Engaging / gamified" | Cognitive g = 0.49 but from k = 19; motivational and behavioural effects unstable under rigor subsplit; conflicts with Deci et al. (1999) on contingent tangible rewards |
| "Beautiful multimedia explanations" | Average multimedia-design principle g = 0.38; matters most for **complex, system-paced** material (g = 0.70) and least for simple, learner-paced material (g = 0.20) |
| "Learners love it / rate it highly" | **Anti-correlated with learning** in the desirable-difficulties literature (Deslauriers et al., 2019; Kornell & Bjork, 2008; Karpicke & Roediger, 2008) |

---

## Reference list

**Retrieval practice**
1. Roediger, H. L., & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science*, 17(3), 249–255.
2. Karpicke, J. D., & Roediger, H. L. (2008). The critical importance of retrieval for learning. *Science*, 319(5865), 966–968. doi:10.1126/science.1152408
3. Soderstrom, N. C., Kerr, T. K., & Bjork, R. A. (2016). The critical importance of retrieval—and spacing—for learning. *Psychological Science*, 27(2), 223–230. doi:10.1177/0956797615617778
4. Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. *Psychological Bulletin*, 140(6), 1432–1463. doi:10.1037/a0037559
5. Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A meta-analysis of practice testing. *Review of Educational Research*, 87(3), 659–701. doi:10.3102/0034654316689306
6. Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. *Psychological Bulletin*, 147(4), 399–435. doi:10.1037/bul0000309
7. Pan, S. C., & Rickard, T. C. (2018). Transfer of test-enhanced learning: Meta-analytic review and synthesis. *Psychological Bulletin*, 144(7), 710–756. doi:10.1037/bul0000151
8. Agarwal, P. K., Nunes, L. D., & Blunt, J. R. (2021). Retrieval practice consistently benefits student learning. *Educational Psychology Review*, 33, 1409–1453. doi:10.1007/s10648-021-09595-9
9. van Gog, T., & Sweller, J. (2015). Not new, but nearly forgotten: The testing effect decreases or even disappears as the complexity of learning materials increases. *EPR*, 27, 247–264. doi:10.1007/s10648-015-9310-x
10. Karpicke, J. D., & Aue, W. R. (2015). The testing effect is alive and well with complex materials. *EPR*, 27, 317–326. doi:10.1007/s10648-015-9309-3
11. Larsen, D. P., Butler, A. C., & Roediger, H. L. (2008). Test-enhanced learning in medical education. *Medical Education*, 42(10), 959–966.
12. McDaniel, M. A., Roediger, H. L., & McDermott, K. B. (2007). Generalizing test-enhanced learning from the laboratory to the classroom. *Psychonomic Bulletin & Review*, 14(2), 200–206.
13. Roediger, H. L., & Butler, A. C. (2011). The critical role of retrieval practice in long-term retention. *Trends in Cognitive Sciences*, 15(1), 20–27.
14. [2026] Testing the testing effect on Prolific: When retrieval practice fails to boost learning. PMC12894256. (Two experiments, null results, engagement boundary.)

**Spacing**
15. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin*, 132(3), 354–380. doi:10.1037/0033-2909.132.3.354
16. Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science*, 19(11), 1095–1102. doi:10.1111/j.1467-9280.2008.02209.x
17. Donovan, J. J., & Radosevich, D. J. (1999). A meta-analytic review of the distribution of practice effect: Now you see it, now you don't. *Journal of Applied Psychology*, 84(5), 795–805. doi:10.1037/0021-9010.84.5.795
18. Latimier, A., Peyre, H., & Ramus, F. (2021). A meta-analytic review of the benefit of spacing out retrieval practice episodes on retention. *EPR*, 33, 959–987. doi:10.1007/s10648-020-09572-8
19. [2025] The distributed practice effect on classroom learning: A meta-analytic review of applied research. PMC12189222. (d = 0.54 [0.31, 0.77].)
20. Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning. *Policy Insights from the Behavioral and Brain Sciences*, 3(1), 12–19.

**Interleaving**
21. Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. *Psychological Bulletin*, 145(11), 1029–1052. doi:10.1037/bul0000209
22. Firth, J., Rivers, I., & Boyle, J. (2021). A systematic review of interleaving as a concept learning strategy. *Review of Education*, 9(2), 642–684. doi:10.1002/rev3.3266
23. Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. *Journal of Educational Psychology*, 112(1), 40–52. doi:10.1037/edu0000367
24. Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science*, 19(6), 585–592. doi:10.1111/j.1467-9280.2008.02127.x
25. Kornell, N., Castel, A. D., Eich, T. S., & Bjork, R. A. (2010). Spacing as the friend of both memory and induction in young and older adults. *Psychology and Aging*, 25(2), 498–503. doi:10.1037/a0017807

**Worked examples & expertise reversal**
26. Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist*, 38(1), 23–31. doi:10.1207/s15326985ep3801_4
27. Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *EPR*, 19, 509–539. doi:10.1007/s10648-007-9054-3
28. Tetzlaff, L., Simonsmeier, B. A., Peters, T., & Brod, G. (2025). A cornerstone of adaptivity — A meta-analysis of the expertise reversal effect. *Learning and Instruction*, 98, 102142. doi:10.1016/j.learninstruc.2025.102142
29. Barbieri, C. A., Miller-Cotto, D., Clerjuste, S. N., & Chawla, K. (2023). A meta-analysis of the worked examples effect on mathematics performance. *EPR*, 35, 11. doi:10.1007/s10648-023-09745-1
30. Alfieri, L., Brooks, P. J., Aldrich, N. J., & Tenenbaum, H. R. (2011). Does discovery-based instruction enhance learning? *Journal of Educational Psychology*, 103(1), 1–18. doi:10.1037/a0021017
31. Kirschner, P. A., Sweller, J., & Clark, R. E. (2006). Why minimal guidance during instruction does not work. *Educational Psychologist*, 41(2), 75–86. doi:10.1207/s15326985ep4102_1
32. Paas, F., & van Merriënboer, J. J. G. (1994). Variability of worked examples and transfer of geometrical problem-solving skills. *JEP*, 86(1), 122–133.
33. Rey, G. D., & Buchwald, F. (2011). The expertise reversal effect: Cognitive load and motivational explanations. *JEP: Applied*, 17(1), 33–48.
34. Rey, G. D., & Fischer, A. (2013). The expertise reversal effect concerning instructional explanations. *Instructional Science*, 41, 407–429.
35. Kalyuga, S., & Renkl, A. (2009). Expertise reversal effect and its instructional implications. *Instructional Science*, 37, 209–215. doi:10.1007/s11251-009-9102-0
36. Schwonke, R., Renkl, A., Krieg, C., et al. (2009). The worked-example effect: Not an artefact of lousy control conditions. *Computers in Human Behavior*, 25(2), 258–266.

**Cognitive load theory**
37. Sweller, J., van Merriënboer, J. J. G., & Paas, F. (1998). Cognitive architecture and instructional design. *EPR*, 10, 251–296.
38. Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *EPR*, 31, 261–292. doi:10.1007/s10648-019-09465-5
39. Kalyuga, S. (2011). Cognitive load theory: How many types of load does it really need? *EPR*, 23, 1–19. doi:10.1007/s10648-010-9150-7
40. de Jong, T. (2010). Cognitive load theory, educational research, and instructional design: Some food for thought. *Instructional Science*, 38, 105–134. doi:10.1007/s11251-009-9110-0
41. Moreno, R. (2010). Cognitive load theory: More food for thought. *Instructional Science*, 38, 135–141. doi:10.1007/s11251-009-9122-9
42. Schnotz, W., & Kürschner, C. (2007). A reconsideration of cognitive load theory. *EPR*, 19, 469–508. doi:10.1007/s10648-007-9053-4
43. Anmarkrud, Ø., Andresen, A., & Bråten, I. (2019). Cognitive load and working memory in multimedia learning: Conceptual and measurement issues. *Educational Psychologist*, 54(2), 61–83. doi:10.1080/00461520.2018.1554484
44. Leppink, J., Paas, F., van der Vleuten, C., et al. (2013). Development of an instrument for measuring different types of cognitive load. *Behavior Research Methods*, 45, 1058–1072. doi:10.3758/s13428-013-0334-1
45. Greenberg, K., & Zheng, R. (2022). Revisiting the debate on germane cognitive load versus germane resources. *Journal of Cognitive Psychology*, 35(3). doi:10.1080/20445911.2022.2159416
46. Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87–114.
47. van Merriënboer, J. J. G., Kirschner, P. A., & Kester, L. (2003). Taking the load off a learner's mind. *Educational Psychologist*, 38(1), 5–13.

**Multimedia learning**
48. Noetel, M., Griffith, S., Delaney, O., Harris, N., et al. (2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research*, 92(3), 413–454. doi:10.3102/00346543211052329 (preprint: doi:10.31234/osf.io/pynzr)
49. Schroeder, N. L., & Cenkci, A. T. (2018). Spatial contiguity and spatial split-attention effects in multimedia learning environments: A meta-analysis. *EPR*, 30, 679–701. doi:10.1007/s10648-018-9435-9
50. Richter, J., Scheiter, K., & Eitel, A. (2016). Signaling text-picture relations in multimedia learning: A comprehensive meta-analysis. *Educational Research Review*, 17, 19–36. doi:10.1016/j.edurev.2015.12.003
51. Richter, J., Scheiter, K., & Eitel, A. (2018). Signaling text-picture relations in multimedia learning: The influence of prior knowledge. *Journal of Educational Psychology*, 110(4), 544–560.
52. Ginns, P. (2005). Meta-analysis of the modality effect. *Learning and Instruction*, 15(4), 313–331. doi:10.1016/j.learninstruc.2005.07.001
53. Ginns, P. (2006). Integrating information: A meta-analysis of the spatial contiguity and temporal contiguity effects. *Learning and Instruction*, 16(6), 511–525.
54. Ginns, P., Martin, A. J., & Marsh, H. W. (2013). Designing instructional text in a conversational style: A meta-analysis. *EPR*, 25, 445–472. doi:10.1007/s10648-013-9228-0
55. Sundararajan, N., & Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. *EPR*, 32, 707–734. doi:10.1007/s10648-020-09522-4
56. Adesope, O. O., & Nesbit, J. C. (2012). Verbal redundancy in multimedia learning environments: A meta-analysis. *Journal of Educational Psychology*, 104(1), 250–263.
57. Rey, G. D., et al. (2019). A meta-analysis of the segmenting effect. *EPR*, 31, 389–419.
58. Schneider, S., Beege, M., Nebel, S., & Rey, G. D. (2018). A meta-analysis of how signaling affects learning with media. *Educational Research Review*, 23, 1–24.
59. Höffler, T. N., & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. *Learning and Instruction*, 17(6), 722–738.
60. Berney, S., & Bétrancourt, M. (2016). Does animation enhance learning? A meta-analysis. *Computers & Education*, 101, 150–167.
61. Schroeder, N. L., Adesope, O. O., & Gilbert, R. B. (2013). How effective are pedagogical agents for learning? A meta-analytic review. *Journal of Educational Computing Research*, 49(1), 1–39.
62. Brom, C., Stárková, T., & D'Mello, S. K. (2018). How effective is emotional design? A meta-analysis. *Educational Research Review*, 25, 100–119.
63. Montero Perez, M., Van Den Noortgate, W., & Desmet, P. (2013). Captioned video for L2 listening and vocabulary learning: A meta-analysis. *System*, 41(3), 720–739.
64. Reinwein, J. (2012). Does the modality effect exist? And if so, which modality effect? *Journal of Psycholinguistic Research*, 41, 1–32.
65. Mayer, R. E., & Fiorella, L. (2014/2021). Principles for reducing extraneous processing in multimedia learning. *The Cambridge Handbook of Multimedia Learning*.

**Bloom's 2 sigma and tutoring**
66. Bloom, B. S. (1984). The 2 sigma problem. *Educational Researcher*, 13(6), 4–16. doi:10.3102/0013189X013006004
67. von Hippel, P. T. (2024). Two-sigma tutoring: Separating science fiction from science fact. *Education Next*, 24(3).
68. Cohen, P. A., Kulik, J. A., & Kulik, C.-L. C. (1982). Educational outcomes of tutoring: A meta-analysis of findings. *AERJ*, 19(2), 237–248. doi:10.3102/00028312019002237
69. Nickow, A., Oreopoulos, P., & Quan, V. (2024). The promise of tutoring for preK–12 learning: A systematic review and meta-analysis. *AERJ*, 61(1), 74–107. doi:10.3102/00028312231208687 (also NBER w27476, 2020)
70. Slavin, R. E. (1987). Mastery learning reconsidered. *Review of Educational Research*, 57(2), 175–213. doi:10.3102/00346543057002175
71. Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *RER*, 60(2), 265–299. doi:10.3102/00346543060002265
72. Guskey, T. R. (1987). Rethinking mastery learning reconsidered. *RER*, 57(2), 225–229.

**Intelligent tutoring systems**
73. VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4), 197–221. doi:10.1080/00461520.2011.611369
74. Kulik, J. A., & Fletcher, J. D. (2016). Effectiveness of intelligent tutoring systems: A meta-analytic review. *RER*, 86(1), 42–78. doi:10.3102/0034654315581420
75. Ma, W., Adesope, O. O., Nesbit, J. C., & Liu, Q. (2014). Intelligent tutoring systems and learning outcomes: A meta-analysis. *JEP*, 106(4), 901–918. doi:10.1037/a0037123
76. Steenbergen-Hu, S., & Cooper, H. (2014). A meta-analysis of the effectiveness of intelligent tutoring systems on college students' academic learning. *JEP*, 106(2), 331–347. doi:10.1037/a0034752
77. Steenbergen-Hu, S., & Cooper, H. (2013). A meta-analysis of the effectiveness of intelligent tutoring systems on K–12 students' mathematical learning. *JEP*, 105(4), 970–987. doi:10.1037/a0032447
78. Koedinger, K. R., Corbett, A. T., & Perfetti, C. (2012). The Knowledge-Learning-Instruction framework. *Cognitive Science*, 36(5), 757–798.

**Desirable difficulties & metacognition**
79. Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science*, 10(2), 176–199. doi:10.1177/1745691615569000
80. Bjork, R. A., Dunlosky, J., & Kornell, N. (2013). Self-regulated learning: Beliefs, techniques, and illusions. *Annual Review of Psychology*, 64, 417–444. doi:10.1146/annurev-psych-113011-143823
81. Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one's knowledge during study. *JEP: LMC*, 31(2), 187–194. doi:10.1037/0278-7393.31.2.187
82. Koriat, A., & Bjork, R. A. (2006). Illusions of competence during study can be remedied. *Memory & Cognition*, 34, 959–972.
83. Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). Measuring actual learning versus feeling of learning. *PNAS*, 116(39), 19251–19257. doi:10.1073/pnas.1821936116
84. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving students' learning with effective learning techniques. *PSPI*, 14(1), 4–58. doi:10.1177/1529100612453266
85. Donoghue, G. M., & Hattie, J. A. C. (2021). A meta-analysis of ten learning techniques. *Frontiers in Education*, 6, 581216. doi:10.3389/feduc.2021.581216
86. Theobald, M. (2021). Self-regulated learning training programs enhance university students' academic performance. *Contemporary Educational Psychology*, 66, 101976. doi:10.1016/j.cedpsych.2021.101976

**Learning styles**
87. Pashler, H., McDaniel, M., Rohrer, D., & Bjork, R. (2008). Learning styles: Concepts and evidence. *PSPI*, 9(3), 105–119. doi:10.1111/j.1539-6053.2009.01038.x
88. Rogowsky, B. A., Calhoun, B. M., & Tallal, P. (2015). Matching learning style to instructional method: Effects on comprehension. *JEP*, 107(1), 64–78. doi:10.1037/a0037478
89. Husmann, P. R., & O'Loughlin, V. D. (2019). Another nail in the coffin for learning styles? *Anatomical Sciences Education*, 12(1), 6–19. doi:10.1002/ase.1777
90. Melzner, L., & Kappes, C. (2024). Testing the meshing hypothesis in prospective teachers. *Instructional Science*. doi:10.1007/s11251-024-09689-1
91. Newton, P. M., & Salvi, A. (2020). How common is belief in the learning styles neuromyth, and does it matter? *Frontiers in Education*, 5, 602451. doi:10.3389/feduc.2020.602451
92. Newton, P. M., Najabat-Lattif, H. F., Santiago, G., & Salvi, A. (2021). The learning styles neuromyth is still thriving in medical education. *Frontiers in Human Neuroscience*, 15, 708540. doi:10.3389/fnhum.2021.708540
93. Rohrer, D., & Pashler, H. (2012). Learning styles: Where's the evidence? *Medical Education*, 46(7), 634–635.
94. Newton, P. M. (2015). The learning styles myth is thriving in higher education. *Frontiers in Psychology*, 6, 1908.

**Motivation, engagement, interest**
95. Howard, J. L., Bureau, J., Guay, F., Chong, J. X. Y., & Ryan, R. M. (2021). Student motivation and associated outcomes: A meta-analysis from self-determination theory. *Perspectives on Psychological Science*, 16(6), 1300–1323. doi:10.1177/1745691620966789
96. Bureau, J. S., Howard, J. L., Chong, J. X. Y., & Guay, F. (2022). Pathways to student motivation: A meta-analysis of antecedents. *RER*, 92(1), 46–72. doi:10.3102/00346543211042426
97. Deci, E. L., Koestner, R., & Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. *Psychological Bulletin*, 125(6), 627–668. doi:10.1037/0033-2909.125.6.627
98. Lepper, M. R., Henderlong, J., & Gingras, I. (1999). Understanding the effects of extrinsic rewards on intrinsic motivation — Uses and abuses of meta-analysis. *Psychological Bulletin*, 125(6), 669–676. doi:10.1037/0033-2909.125.6.669
99. Sailer, M., & Homner, L. (2020). The gamification of learning: A meta-analysis. *EPR*, 32, 77–112. doi:10.1007/s10648-019-09498-w
100. Huang, R., Ritzhaupt, A. D., Sommer, M., & Zhu, J. (2020). The impact of gamification in educational settings on student learning outcomes: A meta-analysis. *ETR&D*, 68, 1875–1901. doi:10.1007/s11423-020-09807-z
101. Bai, S., Hew, K. F., & Huang, B. (2020). Does gamification improve student learning outcome? *Educational Research Review*, 30, 100322. doi:10.1016/j.edurev.2020.100322
102. Kang, M. J., Hsu, M., Krajbich, I. M., Loewenstein, G., et al. (2009). The wick in the candle of learning. *Psychological Science*, 20(8), 963–973. doi:10.1111/j.1467-9280.2009.02402.x
103. Gruber, M. J., Gelman, B. D., & Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning via the dopaminergic circuit. *Neuron*, 84(2), 486–496. doi:10.1016/j.neuron.2014.08.060
104. Gruber, M. J., & Ranganath, C. (2019). How curiosity enhances hippocampus-dependent memory: The PACE framework. *TiCS*, 23(12), 1014–1025.
105. Hidi, S., & Renninger, K. A. (2006). The four-phase model of interest development. *Educational Psychologist*, 41(2), 111–127. doi:10.1207/s15326985ep4102_4
106. Harackiewicz, J. M., Rozek, C. S., Hulleman, C. S., & Hyde, J. S. (2012). Helping parents to motivate adolescents in mathematics and science. *Psychological Science*, 23(8), 899–906. doi:10.1177/0956797611435530

**Cross-cutting**
107. Schneider, M., & Preckel, F. (2017). Variables associated with achievement in higher education: A systematic review of meta-analyses. *Psychological Bulletin*, 143(6), 565–600. doi:10.1037/bul0000098
108. Kraft, M. A. (2020). Interpreting effect sizes of education interventions. *Educational Researcher*, 49(4), 241–253.
109. [2024] No simple solutions to complex problems: Cognitive science principles can guide but not prescribe. PMC10950551. (Source for pooled effect sizes and heterogeneity statistics quoted above.)

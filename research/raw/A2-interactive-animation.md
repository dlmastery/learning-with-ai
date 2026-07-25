---
title: "Interactive Animation and Visual Explanation as Pedagogy, and the Toolchains That Generate It"
wave: A
section: A2
date_researched: 2026-07-25
sources_count: 68
status: raw
---

# A2 — Interactive Animation and Visual Explanation as Pedagogy, and the Toolchains That Generate It

**Research constraint note:** WebSearch budget was exhausted for this session. All findings below come from
WebFetch on known URLs, the arXiv HTML search interface, the Crossref REST API, the Semantic Scholar Graph API,
Unpaywall, and the authenticated GitHub API. OpenAlex was unavailable (daily API budget exhausted at the account
level). Where a primary abstract could not be retrieved, this is stated explicitly and the claim is downgraded.

**Evidence-strength key used throughout:**
- **[A]** Primary source retrieved and quoted this session (peer-reviewed empirical work or meta-analysis).
- **[B]** Primary source retrieved and quoted this session, but preprint / non-peer-reviewed / self-evaluated.
- **[C]** Bibliographic record verified (Crossref/Semantic Scholar) but abstract or numbers not retrievable this
  session; substantive claim reported from secondary summary.
- **[V]** Vendor claim. Marketing copy, not independent evidence.
- **[O]** Observational fact about a repository or artifact (GitHub API, docs), verifiable but not evidence about learning.

---

## 0. Executive framing: the honest version of the animation story

The single most important thing this section must not do is assume that "animation helps learning." It mostly
does not, or does so weakly and conditionally. The strongest available summary sentence in the literature is
from the people who *ran* one of the meta-analyses:

> "The results of three meta-analyses show that the effectiveness of learning from animations, when compared to
> learning from static pictures, is rather limited."
> — Ploetzner, Berney & Bétrancourt (2021), *Instructional Science* 
> DOI: [10.1007/s11251-021-09541-w](https://doi.org/10.1007/s11251-021-09541-w) — **[A]** (abstract retrieved via
> Semantic Scholar Graph API)

That sentence should be quoted in the survey. It is written by authors who are sympathetic to animation, which
makes it more credible, not less.

The realistic synthesis is:

1. Animation vs. static picture: small positive average effect (g ≈ 0.23), heavily moderated, with a large
   moderator-hunting literature that smells of publication bias.
2. Animation *specifically* wins when the thing to be learned **is the change itself** — kinematics, procedures,
   human movement, mechanism dynamics — and loses or is neutral when the target knowledge is conceptual/structural.
3. Learners systematically **prefer** animations and **rate them as more comprehensible** while learning no more
   from them. This is a metacognitive illusion, and it is directly load-bearing for the AI-video-generation
   boom: an LLM pipeline optimized on human preference will optimize for the illusion.
4. Interactivity (learner-controlled pacing, manipulation, prediction) does far more work than motion does.
   The evidence for interactive simulation (PhET) and for active learning generally is much stronger than the
   evidence for animation per se.

---

## 1. The evidence base: does animation actually help learning?

### 1.1 The canonical negative result — Tversky, Morrison & Bétrancourt (2002)

- **"Animation: can it facilitate?"** Tversky B., Morrison J.B., Bétrancourt M. *International Journal of
  Human-Computer Studies* 57(4):247–262, 2002. DOI:
  [10.1006/ijhc.2002.1017](https://doi.org/10.1006/ijhc.2002.1017).
  Crossref citation count 1,155; Semantic Scholar 1,889. **[C]** — bibliographic record verified via Crossref;
  the abstract itself is paywalled (Unpaywall: `is_oa: false`, `oa_status: closed`) and could not be retrieved
  verbatim this session.
- The paper's argument, as consistently represented across the citing literature: a review of studies comparing
  animated with static graphics found **no case in which animation outperformed an informationally equivalent
  static graphic**. Apparent animation wins were attributable to confounds — the animated condition typically
  contained *more information* than the static condition, or added interactivity/self-pacing. The paper proposes
  the **Congruence Principle** (the structure of the external representation should correspond to the structure
  of the desired internal representation) and the **Apprehension Principle** (the representation must be
  accurately perceivable and comprehensible — animation frequently violates this because it is fast, transient,
  and shows many changes at once).
- Companion: Morrison J.B. & Tversky B., **"The (in)effectiveness of animation in instruction,"** CHI '01
  Extended Abstracts, DOI: [10.1145/634288.634290](https://doi.org/10.1145/634288.634290). **[C]** The title is
  itself a data point about how the authors read their own results.

**Survey note:** the Tversky result is *not* "animation is bad." It is "the informational-equivalence control is
almost never run, and when you run it, motion adds nothing." That distinction matters enormously for AI-generated
explanatory video, where the comparison is essentially never run at all.

### 1.2 Meta-analyses

**Höffler & Leutner (2007), "Instructional animation versus static pictures: A meta-analysis,"**
*Learning and Instruction* 17(6):722–738. DOI:
[10.1016/j.learninstruc.2007.09.013](https://doi.org/10.1016/j.learninstruc.2007.09.013).
Crossref citation count 734; Semantic Scholar 998. **[C]** — record verified via Crossref and Semantic Scholar;
Unpaywall reports `is_oa: false, oa_status: closed`, Semantic Scholar reports the abstract "elided by the
publisher," and ScienceDirect returned HTTP 403. **The commonly cited headline is an overall advantage of
animation of about d ≈ 0.37, with the effect concentrated in representational (not decorative) animations and
largest for procedural-motor knowledge. I could not verify those exact numbers from a primary source in this
session and the survey should either verify them independently or cite the effect qualitatively.**

**Berney & Bétrancourt (2016), "Does animation enhance learning? A meta-analysis,"** *Computers & Education*
101:150–167. DOI: [10.1016/j.compedu.2016.06.005](https://doi.org/10.1016/j.compedu.2016.06.005).
Green OA at [archive-ouverte.unige.ch/unige:92234](https://archive-ouverte.unige.ch/unige:92234). **[A]** —
abstract retrieved verbatim:

- **61 primary studies (N = 7,036), 140 pairwise comparisons** of animated vs. static graphic visualizations.
- **Overall Hedges's g = 0.226, 95% CI [0.12, 0.33].** A small effect.
- Moderators with larger effects: system-paced animation **g = 0.309**; animation with auditory commentary
  **g = 0.336**; instruction *without* accompanying text **g = 0.883**.

**Reading the moderators honestly:** the g = 0.883 figure for "no accompanying text" is the kind of subgroup
result that survey authors love to quote and that replication-minded readers should distrust — it is a subgroup
of a subgroup in a literature with small studies and a strong pro-animation publication incentive. Report the
overall g = 0.226 as the headline and the moderators as hypotheses.

**Chan K.K.L. & Leung S.W. (2014), "Dynamic Geometry Software Improves Mathematical Achievement: Systematic
Review and Meta-Analysis,"** *Journal of Educational Computing Research* 51(3):311–325. DOI:
[10.2190/ec.51.3.c](https://doi.org/10.2190/ec.51.3.c), 63 citations. **[C]** — Crossref abstract retrieved but
truncated before the effect size; states it pooled **quasi-experimental** studies 1990–2013 using random-effects
SMD. **Caveat to carry into the survey: quasi-experimental only, and the DGS/GeoGebra literature is dominated by
small regional-journal studies (see §5.6).**

### 1.3 The moderator that actually survives: "learn the change"

**Ploetzner, Berney & Bétrancourt (2020), "A review of learning demands in instructional animations: The
educational effectiveness of animations unfolds if the features of change need to be learned,"** *Journal of
Computer Assisted Learning* 36(6):838–860. DOI:
[10.1111/jcal.12476](https://doi.org/10.1111/jcal.12476), 61 citations. **[A]** — Crossref abstract retrieved:

> "In a systematic review, **194 studies** on learning from animation were analysed. ... Research on learning
> from animation focuses on assessing **conceptual** at the neglect of **kinematic** mental models. This is in
> contrast to an important rationale for making use of animations: that it needs to be learned what animations
> can [display]..."

**Ploetzner, Berney & Bétrancourt (2021), "When learning from animations is more successful than learning from
static pictures: learning the specifics of change,"** *Instructional Science*, DOI:
[10.1007/s11251-021-09541-w](https://doi.org/10.1007/s11251-021-09541-w), 44 citations. **[A]** — abstract
retrieved: three-group experiment, **N = 88 university students**; frames the field as "three meta-analyses show
that the effectiveness ... is rather limited," and argues animation wins specifically when *the specifics of the
displayed changes* are the learning target.

**This is the single most useful design rule to give AI-video builders:** animate the thing that is changing and
that the learner must internalize as a change. If the target knowledge is a static structure, a relation, or a
proof step, a well-designed static diagram is at least as good and cheaper to verify.

### 1.4 The metacognitive-illusion results (the ones the industry ignores)

**Paik E.S. & Schraw G. (2013), "Learning with animation and illusions of understanding,"** *Journal of
Educational Psychology* 105(2):278–289. DOI:
[10.1037/a0030281](https://doi.org/10.1037/a0030281), 62–63 citations. **[A/B]** — abstract elided by publisher;
Semantic Scholar's model-generated TLDR (retrieved this session) states the study used
"a randomized, double-blind, 2 × 2 factorial design using two different types of animation — representational and
directive — and found that **representational animation had a negative effect on learning**, and directive
animation had a positive effect." Treat the TLDR as **[B]** (machine summary) and verify against the paper.

**Kim S., Yoon M., Whang S.-M., Tversky B. & Morrison J. (2007), "The effect of animation on comprehension and
interest,"** *Journal of Computer Assisted Learning* 23(3):260–270. DOI:
[10.1111/j.1365-2729.2006.00219.x](https://doi.org/10.1111/j.1365-2729.2006.00219.x), 59 citations. **[A]** —
Crossref abstract retrieved verbatim:

> "Although animations are believed to be effective in learning and teaching, **several studies have failed to
> confirm this**. ... Fourth and sixth grade students learned the operation of a bicycle pump from graphics that
> were: (i) presented simultaneously; (ii) presented successively; (iii) self-paced, or (iv) animated. **The
> presentation mode affected evaluation of perceived comprehensibility, interestingness, enjoyment and
> motivation, but not comprehension test score.**"

**This is the load-bearing negative finding for the AI era.** Animation moves *liking* without moving *learning*.
Every LLM→video pipeline in §3 is evaluated on VLM-judged or human-preference-judged quality. Those metrics are
measuring exactly the axis that Kim et al. showed dissociates from comprehension.

The parallel result in the active-learning literature is **Deslauriers, McCarty, Miller, Callaghan & Kestin
(2019), "Measuring actual learning versus feeling of learning in response to being actively engaged in the
classroom,"** *PNAS* 116(39):19251–19257. DOI:
[10.1073/pnas.1821936116](https://doi.org/10.1073/pnas.1821936116), 988 citations. **[A]** — Crossref abstract
retrieved: randomized, identical materials; students in the active classroom **learned more but felt they learned
less**. Same dissociation, opposite sign. Together these two results say: *subjective fluency is anti-correlated
with effortful learning, and animation is a fluency machine.*

### 1.5 Why animation fails, mechanistically

- **Selective attention to salience, not relevance.** Lowe R. (1999), "Extracting information from an animation
  during complex visual learning," *European Journal of Psychology of Education*, DOI:
  [10.1007/BF03172967](https://doi.org/10.1007/BF03172967), 417 citations **[C]**; Lowe R. (2003), "Animation and
  learning: selective processing of information in dynamic graphics," *Learning and Instruction* 13(2):157–176,
  DOI: [10.1016/s0959-4752(02)00018-x](https://doi.org/10.1016/S0959-4752(02)00018-X), 379 citations **[C]**.
  Learners extract what *moves most conspicuously*, not what is thematically important. Directly predicts a
  failure mode for LLM-generated animation, which has no model of thematic relevance and defaults to animating
  whatever is easiest to animate.
- **Transient information effect.** Animation is transient; working memory must hold earlier frames to integrate
  with later ones. Ayres P. & Paas F. (2007), "Making instructional animations more effective: a cognitive load
  approach," *Applied Cognitive Psychology* 21(6):695–700, DOI:
  [10.1002/acp.1343](https://doi.org/10.1002/acp.1343), 149 citations **[C]**; and "Can the cognitive load
  approach make instructional animations more effective?" DOI:
  [10.1002/acp.1351](https://doi.org/10.1002/acp.1351), 104 citations **[C]**. Leahy & Sweller, "Cognitive load
  theory, the transient information effect and e-learning," *Learning and Instruction* (2012), DOI:
  [10.1016/j.learninstruc.2012.05.004](https://doi.org/10.1016/j.learninstruc.2012.05.004), 267 citations
  **[B]** (Semantic Scholar TLDR retrieved). Practical corollary: **segmentation and learner pacing are the
  interventions with the best cost/benefit** — they convert transient into inspectable.
- **Top-down knowledge dominates.** Kriz S. & Hegarty M. (2007), "Top-down and bottom-up influences on learning
  from animations," *IJHCS* 65(11):911–930, DOI:
  [10.1016/j.ijhcs.2007.06.005](https://doi.org/10.1016/j.ijhcs.2007.06.005), 186 citations **[C]**. Novices
  without a mental model do not benefit; animation helps those who already have the scaffolding.
- **The framing critique.** Hegarty M. (2004), "Dynamic visualizations and learning: getting to the difficult
  questions," *Learning and Instruction* 14(3):343–351, DOI:
  [10.1016/j.learninstruc.2004.06.007](https://doi.org/10.1016/j.learninstruc.2004.06.007), 226 citations
  **[C]**. Argues the field asks "does animation help?" when it should ask "which learners, which content, which
  interaction affordances."

### 1.6 The strongest *negative-for-animation, positive-for-static* experiment

**Mayer R.E., Hegarty M., Mayer S. & Campbell J. (2005), "When static media promote active learning: Annotated
illustrations versus narrated animations in multimedia instruction,"** *Journal of Experimental Psychology:
Applied* 11(4):256–265. DOI:
[10.1037/1076-898x.11.4.256](https://doi.org/10.1037/1076-898X.11.4.256); Crossref 216 citations, Semantic
Scholar 475. **[C]** — record verified; abstract paywalled/elided and not retrievable this session. Across a
series of experiments comparing paper-based annotated static illustrations against narrated computer animations
on the same content (lightning formation, brakes, ocean waves, toilet tanks), the **static, learner-paced,
annotated illustrations equalled or beat the narrated animations on transfer**. Robert Mayer — the author of the
multimedia principles — published the result that his own medium's flashiest form loses to paper. That is worth
foregrounding.

### 1.7 The theory everyone cites: Mayer's Cognitive Theory of Multimedia Learning (CTML)

- Mayer R.E. & Moreno R. (2003), **"Nine Ways to Reduce Cognitive Load in Multimedia Learning,"** *Educational
  Psychologist* 38(1):43–52. DOI:
  [10.1207/s15326985ep3801_6](https://doi.org/10.1207/S15326985EP3801_6), **2,737 citations**. **[A]** — Crossref
  abstract retrieved: dual-channel assumption, limited-capacity assumption, active-processing assumption; then a
  taxonomy of five overload scenarios and nine load-reduction techniques.
- Mayer R.E., **"Cognitive Theory of Multimedia Learning,"** in *The Cambridge Handbook of Multimedia Learning*:
  2005 ed. DOI: [10.1017/cbo9780511816819.004](https://doi.org/10.1017/CBO9780511816819.004) (1,080 citations);
  2014 ed. DOI: [10.1017/cbo9781139547369.005](https://doi.org/10.1017/CBO9781139547369.005) (770 citations);
  2021 ed. DOI: [10.1017/9781108894333.008](https://doi.org/10.1017/9781108894333.008) (95 citations). **[C]**
- Bétrancourt M. (2005), **"The Animation and Interactivity Principles in Multimedia Learning,"** *Cambridge
  Handbook of Multimedia Learning*, pp. 287–296. DOI:
  [10.1017/cbo9780511816819.019](https://doi.org/10.1017/CBO9780511816819.019), 166 citations. **[C]** — the
  handbook chapter that formalizes "use animation only when it is needed, and pair it with interactivity."

**The principles most directly binding on AI-generated explanatory video** (all from CTML, cited above): coherence
(cut decorative material), signalling (cue the relevant element), redundancy (do not narrate on-screen text
verbatim), spatial contiguity (label adjacent to referent), temporal contiguity (narration synchronized to the
visual), segmenting (learner-paced chunks), and pre-training (name the components before showing the mechanism).
Notably, **generated-animation pipelines routinely violate redundancy and spatial contiguity by construction** —
they narrate the on-screen equation and they place labels wherever the layout engine has room (see §4).

### 1.8 The positive case: interactivity, not motion

- **Freeman S. et al. (2014), "Active learning increases student performance in science, engineering, and
  mathematics,"** *PNAS* 111(23):8410–8415. DOI:
  [10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111), **6,789 citations**. **[A]** — Crossref
  significance statement retrieved: active learning raises exam performance by roughly half a letter grade and
  reduces failure rates. This is the empirical warrant for Brilliant-style *problem-first* design, not for
  animation.
- **PhET Interactive Simulations.** Perkins, Adams, Dubson, Finkelstein, Reid, LeMaster & Wieman (2006), "PhET:
  Interactive Simulations for Teaching and Learning Physics," *The Physics Teacher* 44(1):18–23, DOI:
  [10.1119/1.2150754](https://doi.org/10.1119/1.2150754), 224 citations **[A/C]**; Wieman C., Adams W. & Perkins
  K. (2008), "PhET: Simulations That Enhance Learning," *Science* 322(5902):682–683, DOI:
  [10.1126/science.1161948](https://doi.org/10.1126/science.1161948), 272 citations **[C]**. PhET is the
  best-documented case of *interactive* animated visualization with a research-based design process
  (interviews, think-alouds, iterative redesign). Its evidence base is stronger for engagement and
  representational understanding than for exam scores, and the survey should say so.

---

## 2. Brilliant.org — interactive-problem pedagogy

### 2.1 What Brilliant says it does (all **[V]** vendor claims unless noted)

From [brilliant.org/about](https://brilliant.org/about/) (fetched 2026-07-25), verbatim:

- Mission framing: help people "excel in STEM, in less time, with more purpose and joy," with learning designed
  to be "interactive, adaptive, and fun."
- **Problem-first / pretesting:** *"We don't teach how to do something before asking questions. Instead, we
  pretest on the material, letting the learner try to find a solution before learning the procedure."*
- **Lesson composition:** *"a mix of direct instruction and blocked problem solving"*; lessons begin by building
  intuition with *"visual explanations, hands-on manipulation, and concrete computation."*
- **Instrumentation, not efficacy:** *"We measure everything. Knowing how many users practice every day, and
  whether people solve problems of increasing difficulty over time, allows us to get the learning experience just
  right."* and *"With millions of problem tries every day, we're rapidly increasing the pace at which we're able
  to test our pedagogical ideas."*

From [brilliant.org](https://brilliant.org/) homepage (fetched 2026-07-25), verbatim:
- "10 million+ learners around the world"; "100,000+ 5-star app store reviews."
- "Every session is visual and interactive."
- Curriculum credited to staff from MIT, Harvard, Stanford, Cornell, Caltech.
- **New as of this fetch:** an AI tutor named **"Koji"** — *"A world-class tutor for math and coding"*; *"Koji
  tracks what you've mastered and where you're stuck, then builds practice around the gaps."* Testimonial
  claims include a student learning slope in "20 minutes talking to Koji" and "I learned the basics of
  Trigonometry in 12 days."
- **Absence finding [O]:** the homepage carries **no quantified learning-outcome claim** — no "X% improvement,"
  no "N× faster than video." All numbers are satisfaction/scale numbers. That is a meaningful restraint compared
  to much of edtech marketing, and it is also an admission.

### 2.2 What a lesson actually looks like structurally

Fetched [brilliant.org/courses/math-fundamentals/](https://brilliant.org/courses/math-fundamentals/) **[O]**:

- Course → **5 levels** (levels function as chapters) → **27 lessons** → **363 exercises**.
- Levels are ordered by conceptual dependency: (1) Visualizing fractions, 6 lessons; (2) Equivalent fractions,
  6; (3) Comparing fractions, 5; (4) Adding fractions, 5; (5) Multiplying fractions, 6.
- Every level terminates in a **Level Review**.
- Stated approach: *"we'll build your understanding of fractions using visuals."*
- Catalog is organized into **"Learning Paths — step-by-step paths to mastery"**
  ([brilliant.org/courses/](https://brilliant.org/courses/)).

**Structural model to state in the survey:** a Brilliant lesson is a *sequence of ~10–15 single-screen interactive
problems*, each with (a) a manipulable or visual stimulus, (b) a forced answer commitment, (c) immediate
correctness feedback with a worked explanation, and (d) a difficulty ratchet across the sequence. The unit of
content is the **problem**, not the exposition; exposition is delivered as feedback *after* a commitment.
Ratio evidence: 363 exercises to 27 lessons ≈ **13.4 exercises per lesson** — the platform is overwhelmingly
assessment-shaped. **[O]**

### 2.3 Efficacy evidence

**There is essentially none in the peer-reviewed literature.** Crossref bibliographic searches for
"Brilliant.org informal STEM learning platform study" and "gamified problem solving app STEM learning outcomes
randomized Brilliant" returned **zero studies about the platform** (results were unrelated informal-STEM papers).
**[O — absence of evidence, searched via Crossref API 2026-07-25]**

So the honest position for the survey is:

- Brilliant's *design principles* are individually well-supported by independent literature it does not itself
  cite: pretesting/generation before instruction (Richland, Kornell & Kao; Kapur's productive failure), immediate
  feedback, spaced/blocked practice, active problem solving (Freeman et al. 2014, DOI
  [10.1073/pnas.1319030111](https://doi.org/10.1073/pnas.1319030111) **[A]**).
- Brilliant's *product* has no published efficacy evaluation, no independent RCT, and no released A/B results
  despite claiming "millions of problem tries every day" of experimental capacity. Its own strongest claim is
  about measurement infrastructure, not outcomes.
- Label every efficacy statement about Brilliant as **[V]**.

### 2.4 Why Brilliant matters to this survey anyway

Brilliant is the existence proof that **interactive-problem pedagogy scales as a content format**, and it is the
format an LLM is *worst* at generating well and *best* at generating cheaply. A Brilliant lesson requires: a
correct answer key, plausible-but-instructive distractors, a manipulable visual whose state maps to the
mathematics, and feedback text that diagnoses the specific error. Items 1 and 4 are LLM-tractable; items 2 and 3
are where generation quality collapses (see §4).

---

## 3. The generation toolchains

### 3.1 Manim

**Repository facts (GitHub API, fetched 2026-07-25) [O]:**

| | `3b1b/manim` (ManimGL) | `ManimCommunity/manim` (ManimCE) |
|---|---|---|
| Created | 2015-03-22 | 2020-05-19 |
| Stars | 88,858 | 39,692 |
| Forks | 7,406 | 2,979 |
| Open issues | 493 | 514 |
| License | MIT | MIT |
| Last push | 2026-07-17 | 2026-07-24 |
| Latest releases | (no release cadence; commits titled e.g. "Video work") | v0.20.1 (2026-02-27), v0.20.0 (2026-02-20), v0.19.2 (2026-01-17), v0.19.1 (2025-12-01), v0.19.0 (2025-01-20) |

**Architecture [O]** — module trees retrieved via GitHub contents API:

- `ManimCommunity/manim/manim/`: `animation/`, `camera/`, `cli/`, `mobject/`, `opengl/`, `plugins/`,
  `renderer/`, `scene/`, `utils/`, plus `constants.py`, `data_structures.py`, `typing.py`.
- `3b1b/manim/manimlib/`: `animation/`, `camera/`, `event_handler/`, `mobject/`, `scene/`, `shaders/`,
  `shader_wrapper.py`, `window.py`, `tex_templates.yml`, `default_config.yml`.

The core object model is: **Mobject** (mathematical object — a `VMobject` is a Bézier-path vector object) →
composed into a **Scene** whose `construct()` method issues **Animation** objects via `self.play(...)` → rendered
by a **Renderer** (Cairo for ManimCE's default path, OpenGL/shader pipeline for ManimGL and ManimCE's `opengl`
backend) → muxed by ffmpeg. LaTeX is a hard external dependency for any `Tex`/`MathTex` object; ffmpeg is a hard
dependency for output.

**The fork/version problem — this is central to the LLM story.** From the ManimCE README **[O, quoted]**:

> "The community edition of Manim (ManimCE) is a version maintained and developed by the community. It was forked
> from 3b1b/manim, a tool originally created and open-sourced by Grant Sanderson... While Grant Sanderson
> continues to maintain his own repository, we recommend this version..."

> "These instructions are for the community version *only*. Trying to use these instructions to install
> [3b1b/manim] or instructions there to install this version **will cause problems**."

There are effectively **three** things called "manim" (3b1b's ManimGL, ManimCE, and the abandoned `manim` PyPI
name history), with **incompatible APIs**, and the training corpus contains all of them intermixed across ten
years of API churn. This is the direct mechanical cause of the dominant LLM failure mode in this domain
(see §3.2 and §4.1).

**What Manim is good at:** exact mathematical objects (graphs, transformations, vector fields, coordinate
systems), morphing one mathematical expression into another (`Transform` on LaTeX), camera moves over a
mathematically-defined scene, and deterministic reproducibility. **What it costs:** Manim is a *programming*
task, not an authoring task. There is no timeline, no direct manipulation, no visual layout feedback; positioning
is code (`.next_to()`, `.shift()`, `.to_edge()`), and every render is a compile-and-watch cycle measured in tens
of seconds to minutes. The layout system has **no collision avoidance** — this is why every LLM→Manim paper
below independently rediscovers overlap as the primary defect.

Academic framing paper: **Zhang C. (2025), "Manim for STEM Education: Visualizing Complex Problems Through
Animation,"** arXiv:[2510.01187](https://arxiv.org/abs/2510.01187). **[B]** Claims Manim lowers authoring burden
via "Python's straightforward syntax" and asserts animations "significantly enhance learning outcomes" relative
to static visuals — **an unsupported claim in light of §1**; its "evaluation" is analysis of social-media viewer
feedback, i.e. engagement, not learning. Cite it as an example of the field's uncritical prior.

### 3.2 Can an LLM reliably generate correct Manim? The literature (all preprints, **[B]**)

This turns out to be a surprisingly dense and fast-moving subfield. Fourteen relevant arXiv entries were
identified via the arXiv HTML search interface on 2026-07-25.

**Benchmarks and the failure taxonomy**

- **TheoremExplainAgent / TheoremExplainBench** — Ku M., Chong T., Leung J. et al., arXiv:[2502.19400](https://arxiv.org/abs/2502.19400) (Feb 2025).
  Agentic generation of **>5-minute** theorem explanation videos in Manim. Benchmark: **240 theorems** across STEM,
  5 automated metrics. Best result: **o3-mini, 93.8% success rate, overall score 0.77**. But, verbatim:
  *"most of the videos produced exhibit minor issues with visual element layout"* and *"multimodal explanations
  expose deeper reasoning flaws that text-based explanations fail to reveal."* **The second clause is the more
  interesting finding: forcing a model to draw a theorem surfaces reasoning errors that prose hides.** That is an
  argument for visual generation as an *evaluation* technique, independent of its pedagogical value.
- **ManiBench** — Oli N., arXiv:[2603.13251](https://arxiv.org/abs/2603.13251) (Mar 2026). Explicitly names the two
  failure modes:
  - **Syntactic Hallucinations** — "valid Python referencing non-existent or deprecated Manim APIs."
  - **Visual-Logic Drift** — "generated visuals diverging from intended mathematical logic through timing errors
    or missing causal relationships."
  150–200 problems, five difficulty levels (calculus, linear algebra, probability, topology, AI), grounded in
  analysis of 3Blue1Brown's ManimGL source (**53,000 lines, 143 scene classes**). Four-tier evaluation:
  Executability, **Version-Conflict Error Rate**, Alignment Score, Coverage Score. The existence of a dedicated
  "version-conflict" metric confirms the §3.1 diagnosis. *(No pass rates in the abstract.)*
- **MORSE-500** — Cai Z. et al., arXiv:[2506.05523](https://arxiv.org/abs/2506.05523) (Jun 2025). Uses Manim +
  Matplotlib + MoviePy as *deterministic generators* for a video reasoning benchmark — an inverted use of the
  toolchain worth a sentence.

**Spatial/geometric correctness — the recurring defect**

- **SGA (Symbolic Geometric Agent)** — Lopez J., Hinojosa C., Ghanem B., arXiv:[2607.18116](https://arxiv.org/abs/2607.18116) (Jul 2026).
  Verbatim: *"ensuring spatial correctness and visual legibility remains challenging, as existing frameworks
  emphasize pedagogical content while overlooking geometric occlusions."* Intercepts LLM code, does **partial
  execution to extract a symbolic scene graph**, refines when spatial conflicts are found. Introduces **MVQS**
  (Manim Visual Quality Score), a rendering-free spatial-integrity proxy. Results on MMMC-Code across 4 LLM
  backbones × 2 pipelines: peak **MVQS 73.11** (Code2Video + GPT-5.1), **+16.1% relative** over raw baseline,
  improving **7 of 8** configurations. **Note the ceiling: even the best configuration scores 73/100 on a metric
  the authors designed.**
- **ALGOGEN** — Liao K. et al., arXiv:[2605.12159](https://arxiv.org/abs/2605.12159) (May 2026). The cleanest
  quantitative baseline in the literature: end-to-end LLM methods reach **82.5%** success on a 200-task LeetCode
  algorithm-visualization benchmark; ALGOGEN reaches **99.8%** (+17.3 pts) by **decoupling algorithm execution
  from rendering** — the LLM emits a Python tracker producing a "Visualization Trace Algebra" JSON trace, and a
  *deterministic* renderer draws it (Manim / LaTeX-TikZ / Three.js). Explicitly names the three failures fixed:
  **execution failure, element overlap, inter-frame inconsistency**. Core insight, verbatim in paraphrase:
  requiring LLMs to *simultaneously* simulate the algorithm and satisfy rendering constraints induces
  hallucination.

**Training and inference strategies**

- **ManimTrainer / ManimAgent (RITL)** — Rammuni Silva R.S., Lotfi A., Ihianle I.K. et al.,
  arXiv:[2604.18364](https://arxiv.org/abs/2604.18364) (Apr 2026). Verbatim: Manim generation *"requir[es] spatial
  reasoning, temporal sequencing, and familiarity with domain-specific APIs that are **underrepresented in general
  pre-training data**."* SFT + GRPO with a fused code+visual reward; inference-time **Renderer-in-the-Loop
  (RITL)** and **RITL-DOC** (API-documentation-augmented). Evaluated **17 open-source sub-30B LLMs × 9
  strategy combinations** on ManimBench. Finding: **SFT improves code quality; GRPO improves visual output and
  self-correction responsiveness.** Best: Qwen 3 Coder 30B + GRPO + RITL-DOC → **94% Render Success Rate**,
  **85.7% Visual Similarity**, **+3 pts VS over GPT-4.1**.
  **Read carefully: "render success" is compile-and-produce-a-file, not correctness.**
- **ManimAgent (self-evolving memory)** — Jiang W., Cai Z., Shao Y. et al.,
  arXiv:[2606.30296](https://arxiv.org/abs/2606.30296) (Jun 2026). Dual-channel **Episodic Memory Bank**: a
  positive channel M+ of success rationales as soft "Reference Examples," and a negative channel M− of validated
  failure patterns as hard "Known Pitfalls," accumulated without weight updates. A VLM scores rendered keyframes.
  Reports blind human Pass@1 rising and reflection rounds falling as memory grows (no absolute numbers in the
  abstract).
- **PairCoder++** — Chen J., Li X., Chen M. et al., arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) (Jul 2026).
  Not Manim-specific but the most general statement of the pattern, verbatim:
  > "In this regime single pass inference is brittle, because **the compiler, renderer, or simulator that decides
  > whether the artifact exists is invisible to the model**."
  Driver/Navigator pair-programming with role switching, grounded in toolchain evidence (diagnostics, execution
  results, renderings beside the target). Across **17 public benchmarks × 7 models × 3 vendors**: Blender scene
  executability **0.20 → 0.78**; **TikZ compile rate up 10–30 points on every model**; cost **2.9–9.2× single
  model (≈7× overall)**. Crucially honest: *"the method ties or mildly regresses where the oracle is weak."*
  **The generalizable law: verified generation works exactly as well as your verifier.**

**Pipeline/product systems**

- **Code2Video** — Chen Y., Lin K.Q., Shou M.Z., arXiv:[2510.01174](https://arxiv.org/abs/2510.01174) (Oct 2025).
  Planner / Coder / Critic agents emitting executable Python; **+40% over direct code generation**; introduces
  the **MMMC** benchmark of professionally produced educational videos and **TeachQuiz**, "a novel end-to-end
  metric that quantifies how well a VLM, **after unlearning**, can recover knowledge by watching the generated
  videos." TeachQuiz is the most interesting evaluation idea in this literature — a machine-analogue of a
  learning-gain measure rather than a preference score — and also, obviously, not evidence about humans.
- **Manimator** — Samarth P., Jain V., Golugula S., Sathvik M.S., arXiv:[2507.14306](https://arxiv.org/abs/2507.14306) (Jul 2025). Research papers → Manim explanatory animations.
- **LLM2Manim** — Joshi A., Ke H., Gajjar M. et al., arXiv:[2604.05266](https://arxiv.org/abs/2604.05266) (Apr 2026). "Pedagogy-aware" narrated STEM animation pipeline.
- **ANVIL** — Noviello Y., Birillo A., Migut G., arXiv:[2605.16295](https://arxiv.org/abs/2605.16295) (May 2026).
  Generates a **textual analogy** first, compiles it into a "structured visual screenplay," then into executable
  Manim. Notable because analogy-first is an actual pedagogical commitment rather than a rendering trick.
- **PhysicsSolutionAgent** — Thole A., Agrawal A., Ramamoorthy A., Kumar D., arXiv:[2601.13453](https://arxiv.org/abs/2601.13453) (Jan 2026). Up to 6-minute physics explanation videos; assessment pipeline of **15 quantitative parameters** plus VLM feedback loops.
- **TeachMaster** — Wang Y., Yang R., Wu L., Zhang J. et al., arXiv:[2601.04204](https://arxiv.org/abs/2601.04204) (Jan 2026). Multi-agent planning/design/rendering with "code as an intermediate semantic medium"; claims production cost of **0.3% of traditional online course videos**. **[B/V]** — a 300× cost claim with no human learning outcome reported; treat as an economics claim only.
- **LASEV** — Yan L., Wu J., Xie D. et al., arXiv:[2602.11790](https://arxiv.org/abs/2602.11790) (Feb 2026). Solution/Illustration/Narration agents → "structured executable video script ... deterministically compiled into synchronized visuals and narration."

**Synthesis for the survey.** Across a dozen independent groups the same architecture keeps winning:

> **Do not let the LLM draw. Let the LLM emit a structured, verifiable intermediate representation, and let a
> deterministic renderer draw it — then feed the compiler/renderer/VLM back into the loop.**

ALGOGEN (VTA traces), LASEV (executable video script), SGA (symbolic scene graph), PairCoder++ (toolchain-grounded
review), Raiven (DSL mediation, §3.5) are five independent rediscoveries of the same principle. This is the
single most transferable finding in this section.

### 3.3 Remotion

**Repository facts (GitHub API, 2026-07-25) [O]:** `remotion-dev/remotion`, created 2020-06-23, **54,280 stars**,
3,964 forks, 192 open issues, last push 2026-07-25, license `NOASSERTION` (source-available, not OSI open source).

**Model** — from [remotion.dev/docs/the-fundamentals](https://www.remotion.dev/docs/the-fundamentals) **[O]**:
> "A video is a function of images over time. If you change content every frame, you'll end up with an animation."

A video is a React component. `useCurrentFrame()` gives the frame index; `useVideoConfig()` gives
`{width, height, durationInFrames, fps}`; frames run `0 … durationInFrames - 1`. Videos are registered as
`<Composition>` elements in `src/Root.tsx`. Rendering paths
([remotion.dev/docs/render](https://www.remotion.dev/docs/render), [/docs/renderer](https://www.remotion.dev/docs/renderer)) **[O]**: Remotion Studio GUI,
CLI (`npx remotion render <Composition>`), server-side Node APIs (`@remotion/renderer`: `renderMedia()` and
`renderFrames()`), **AWS Lambda**, **Google Cloud Run (alpha)**, and GitHub Actions. Variant outputs: audio-only,
image sequences (`--sequence`), stills, GIF, transparent video. Rendering is done by driving a headless
Chromium and capturing frames — which is why the whole web platform is available inside a video.

**Licensing [O, quoted from `remotion-dev/remotion/LICENSE.md` via GitHub API]:**
- Free for: "an individual," "a for-profit organization with **up to 3 employees**," non-profits, and evaluation.
- "You are required to obtain a **Company License**" otherwise (pricing at remotion.pro).
- Disallowed: "copy or modify Remotion code for the purpose of selling, renting, licensing, relicensing, or
  sublicensing your own derivate of Remotion."
- Note: "In Remotion 5.0, the license will slightly change."

**This licensing detail matters for the survey:** any AI-education company above 3 employees that generates
explanatory video with Remotion owes a commercial license. Manim (MIT) does not have this constraint. That
asymmetry will shape which toolchain AI-generated-education products standardize on.

**Remotion vs Manim — the comparison to make:**

| Axis | Manim | Remotion |
|---|---|---|
| Primitive | Mathematical Mobject (Bézier vector, LaTeX) | DOM/React component, CSS, SVG, Canvas, WebGL |
| Time model | Imperative: `self.play(anim, run_time=...)` sequences | Declarative: pure function of `frame` |
| Determinism | High | High (frame-indexed pure render) |
| Math typesetting | First-class (LaTeX built in) | Requires KaTeX/MathJax integration |
| Layout | Manual, relative positioning; **no collision avoidance** | Full CSS layout engine — flexbox/grid solve label placement *for free* |
| Interactivity in output | None (video only) | None in the video, but the same components run as a live interactive page |
| Preview loop | Compile-and-watch (slow) | Hot-reloading Studio with a scrubbable timeline |
| Ecosystem for LLM | Small, version-fragmented Python API | Enormous React/CSS/JS corpus in pretraining |
| Licence | MIT | Source-available; commercial licence >3 employees |
| Rendering | Cairo / OpenGL + ffmpeg | Headless Chromium + ffmpeg, parallelizable to Lambda/Cloud Run |

**Why Remotion is arguably the better AI target, and why the literature nonetheless uses Manim.** Remotion's
advantages for generation are real: (a) React/CSS/SVG is far better represented in pretraining than Manim's
API; (b) **CSS layout eliminates the #1 documented failure mode** — overlapping and out-of-frame elements — because
flexbox/grid computes positions rather than the model guessing coordinates; (c) the *same* generated component can
be shipped as an interactive page or as an mp4, which matters given §1's finding that interactivity, not motion,
carries the learning effect; (d) rendering parallelizes trivially over Lambda. Its disadvantages: no native
mathematical object model, math typesetting is bolted on, and the licence.

The reason every paper in §3.2 targets Manim is sociological, not technical: 3Blue1Brown made Manim the *aesthetic
reference* for what a good math explanation looks like, and the benchmarks (MMMC, TheoremExplainBench) are built
from that aesthetic. **This is worth naming in the survey as a case of benchmark capture by a style.**
**[Interpretation — my analysis, not a cited finding.]**

### 3.4 TikZ / PGF — the best-studied generation target

TikZ is the LaTeX vector-graphics DSL. Because it compiles (pass/fail) and because 360k+ human-written examples
exist, it has become the *de facto* benchmark substrate for "can models draw."

- **AutomaTikZ** — Belouadi J., Lauscher A., Eger S., arXiv:[2310.00367](https://arxiv.org/abs/2310.00367) (Oct 2023). Introduces **DaTikZ**, 120k TikZ drawings aligned with captions. **[B]**
- **DeTikZify** — Belouadi J., Ponzetto S.P., Eger S., arXiv:[2405.15306](https://arxiv.org/abs/2405.15306) (May 2024). **DaTikZv2, >360k human-created TikZ graphics**; synthesizes TikZ from sketches/figures; MCTS-based inference-time refinement. **[B]**
- **TikZero** — Belouadi J., Ilg E., Keuper M. et al., arXiv:[2503.11509](https://arxiv.org/abs/2503.11509) (Mar 2025). Decouples graphics-program generation from text understanding for zero-shot text-guided synthesis. **[B]**
- **TikZilla** — Greisinger C., Eger S., arXiv:[2603.03072](https://arxiv.org/abs/2603.03072) (Mar 2026). SFT + RL; "matches GPT-5 in the image-based evaluation." **[B]**
- **GeoTikzBridge** — Sun J., Sun C., Yang B. et al., arXiv:[2603.22687](https://arxiv.org/abs/2603.22687) (Mar 2026). **2.5M image-to-TikZ pairs, "16× larger than existing open-sourced datasets."** **[B]**
- **vTikZ** — Reux C., Acher M., Khelladi D.E. et al., arXiv:[2505.04670](https://arxiv.org/abs/2505.04670) (May 2025). Benchmark for *editing* TikZ while preserving visual intent. Verbatim: *"state-of-the-art LLMs ... struggle to reliably modify code in alignment with visual intent."* **[B]** *(no numbers in abstract)*. **This is an under-appreciated failure axis: iterative refinement of a diagram, which is the actual teaching workflow, is harder than one-shot generation.**
- **DiagramIR** — Kumar V., Mishra S., Hao R. et al., arXiv:[2511.08283](https://arxiv.org/abs/2511.08283) (NeurIPS 2025 Math-AI Workshop). Automatic evaluation of **educational math diagrams** by parsing LaTeX/TikZ into an intermediate representation rather than comparing images. Claims **higher agreement with human raters than LLM-as-a-Judge**, and that **GPT-4.1-mini performs comparably to GPT-5 at ~10× lower inference cost**. **[B]** — the closest thing in the literature to an education-specific diagram-quality metric.
- **Text to Automata Diagrams** — Young E., Wang Z., Taylor A. et al., arXiv:[2603.07936](https://arxiv.org/abs/2603.07936) (Mar 2026). Pipeline: scanned *student-drawn* diagram → VLM description → human correction → LLM → TikZ. Verbatim finding: *"descriptions generated directly from images using vision-language models are often incorrect and human correction can substantially improve the quality."* **[B]** — a direct negative result on VLM diagram *reading*, which bounds any grade-my-diagram application.
- **Control-GPT** — Zhang T., Zhang Y., Vineet V. et al., arXiv:[2305.18583](https://arxiv.org/abs/2305.18583) (May 2023). Uses GPT-4-authored TikZ as a *spatial sketch* to steer a diffusion model — the earliest clear statement that symbolic code fixes what diffusion cannot: layout. **[B]**

### 3.5 Mermaid

- Repo `mermaid-js/mermaid` **[O]**: created 2014-11-01, **89,417 stars**, 9,142 forks, MIT, last push 2026-07-25.
- **MermaidSeqBench** — Shbita B., Ahmed F., DeLuca C., arXiv:[2511.14967](https://arxiv.org/abs/2511.14967) (Nov 2025). **132 samples**, hybrid human-verified + LLM-augmented + rule-expanded. Metrics: syntax correctness, activation handling, error handling, practical usability. Verbatim: *"the lack of existing benchmarks ... hinders the reliable deployment of these models in production environments"*; evaluations *"reveal significant capability gaps across models and evaluation modes."* **[B]** *(no absolute numbers in abstract)*.
- **"Evaluating Ill-Defined Tasks in Large Language Models"** — Zhou Y., Shbita B., arXiv:[2603.17067](https://arxiv.org/abs/2603.17067) (Mar 2026). Uses NL→Mermaid sequence diagrams as the case study for how evaluation criteria expose distinct failure modes. **[B]**
- **Pedagogical read:** Mermaid is the *cheapest* generation target (tiny grammar, text-first, renders in Markdown, GitHub-native) and correspondingly the *least expressive* — it can express structure (flow, sequence, state, class, ER, Gantt) but almost no quantitative or geometric content. It is the right target for "explain this system's architecture" and the wrong target for anything mathematical. Its grammar is small enough that syntax hallucination is largely solvable by constrained decoding.

### 3.6 D3.js, Vega-Lite, and chart code

- Repo `d3/d3` **[O]**: created 2010-09-27, **113,289 stars**, 22,689 forks, ISC.
- **Raiven** — arXiv:[2604.10008](https://arxiv.org/abs/2604.10008) (Apr 2026). LLM visualization authoring **mediated by a DSL (RaivenDSL) that compiles to D3 or VTK.js**. Claims **100% compilation**, **up to 6× faster and 6× cheaper** than direct SOTA-LLM generation, on a 100-task benchmark, "with guaranteed correctness and no silent data errors." **[B]**
- **The finding to generalize:** direct D3 generation is a bad idea and everyone who measures it concludes so. D3 is an imperative, low-level, heavily-idiomatic API; a constrained DSL or a grammar-of-graphics layer (Vega-Lite) is the correct LLM target. **Silent data errors** — a chart that renders beautifully and encodes the wrong column — are the characteristic and most dangerous failure, because unlike a compile error nothing surfaces it.

### 3.7 p5.js, Excalidraw, Observable

- `processing/p5.js` **[O]**: created 2013-02-26, **23,815 stars**, LGPL-2.1, active (last push 2026-07-25).
  Strengths as a generation target: the smallest possible mental model (`setup()`/`draw()`), enormous
  pretraining corpus of creative-coding sketches, runs in a browser sandbox with zero build step, and is
  *natively interactive* (mouse/keyboard) — which by §1.8 is the axis that actually matters. Weakness:
  immediate-mode canvas has no layout engine and no scene graph, so text/label collision must be hand-computed —
  the same defect as Manim.
- `excalidraw/excalidraw` **[O]**: created 2020-01-02, **128,332 stars**, 14,558 forks, MIT. Its scene format is a
  flat JSON array of typed elements with explicit `x/y/width/height`, which makes it a plausible *structured
  intermediate representation* target for LLMs (in the ALGOGEN sense) rather than a code target. Hand-drawn
  aesthetic is a deliberate signal of provisionality — pedagogically useful because it invites the learner to
  disagree with the diagram. No benchmark literature found. **[O — absence]**
- `observablehq/framework` **[O]**: created 2023-09-27, **3,557 stars**, ISC. Observable notebooks pioneered the
  reactive-dataflow notebook (cells re-evaluate on dependency change) and the `viewof` binding that makes a
  slider a first-class program variable — arguably the cleanest "explorable explanation" substrate. The
  original observablehq.com notebook runtime is a hosted product; Framework is the static-site successor.
  Small ecosystem relative to the others; no LLM-generation literature found. **[O — absence]**

### 3.8 GeoGebra and Desmos

- `geogebra/geogebra` **[O]**: 2,282 stars, described as "GeoGebra apps (mirror)" — i.e. GitHub is not the
  development locus. GeoGebra is a dynamic-geometry + CAS system with a scripting language and an embeddable
  applet API, used at enormous scale in school mathematics.
- **Evidence quality warning [O, based on Crossref result sets retrieved 2026-07-25]:** searches for GeoGebra
  efficacy return a large volume of studies in low-visibility regional journals (e.g. *Journal of Education and
  Practice*, *Al-Jabar*, *Jurnal Pendidikan Matematika*, various Turkish education journals), typically small
  quasi-experiments with large reported effects. Representative: Kaya A. & Öçal M.F. (2018), a Turkish-language
  GeoGebra meta-analysis, DOI [10.17522/balikesirnef.505918](https://doi.org/10.17522/balikesirnef.505918);
  Cantürk Günhan B. & Açan H. (2016), DOI [10.16949/turcomat.67541](https://doi.org/10.16949/turcomat.67541);
  Zulnaidi H., Oktavika E., Hidayat R. (2019), *Education and Information Technologies*, DOI
  [10.1007/s10639-019-09899-y](https://doi.org/10.1007/s10639-019-09899-y) (62 citations, the strongest venue in
  the set). **The survey should say plainly that the dynamic-geometry efficacy literature is high-volume and
  low-rigour, and that the pooled effects (e.g. Chan & Leung 2014) should be discounted for small-study and
  publication bias.**
- Desmos: the retrieved literature is thinner still and similarly distributed (e.g. Bhatia K. & Chakraborty P.
  (2024), *IETE Journal of Education*, DOI [10.1080/09747338.2024.2341068](https://doi.org/10.1080/09747338.2024.2341068), 4 citations; Liang S. (2015), *IJRES*, DOI
  [10.21890/ijres.62743](https://doi.org/10.21890/ijres.62743), 18 citations). **[C]**
- As generation targets, both matter because their state is **declarative and small**: a Desmos graph is a list of
  expressions; a GeoGebra construction is a list of constrained objects. An LLM emitting `y=\sin(x)+a` plus a
  slider definition is far more likely to be correct than one emitting 80 lines of Manim positioning code — and
  the result is *interactive*, which §1.8 says is where the learning effect lives. **[Interpretation.]**

---

## 4. What fails when LLMs generate diagrams and visuals

Consolidating across §3, six distinct failure classes are documented, each with a citation:

**4.1 API/version hallucination.** Valid code referencing non-existent or deprecated APIs — ManiBench's
"Syntactic Hallucinations," severe enough to warrant a dedicated **Version-Conflict Error Rate** metric
(arXiv:[2603.13251](https://arxiv.org/abs/2603.13251)). Root cause is corpus-level: two incompatible Manim forks
plus a decade of API churn (§3.1). Mitigation with measured effect: documentation-augmented renderer-in-the-loop
(RITL-DOC, arXiv:[2604.18364](https://arxiv.org/abs/2604.18364)); pair-programming with compiler diagnostics
(**TikZ compile rate +10–30 points on every model**, arXiv:[2607.01883](https://arxiv.org/abs/2607.01883)).

**4.2 Spatial reasoning / occlusion / label collision.** The most universally reported defect.
- SGA: *"ensuring spatial correctness and visual legibility remains challenging ... overlooking geometric
  occlusions"*; best-in-class MVQS only **73.11/100** (arXiv:[2607.18116](https://arxiv.org/abs/2607.18116)).
- ALGOGEN names **element overlap** as one of three core failures (arXiv:[2605.12159](https://arxiv.org/abs/2605.12159)).
- TheoremExplainAgent: even at **93.8% "success," "most of the videos produced exhibit minor issues with visual
  element layout"** (arXiv:[2502.19400](https://arxiv.org/abs/2502.19400)). **The gap between 93.8% success and
  "most videos have layout defects" is the single most instructive number pair in this literature: the success
  metric is measuring compilation, not legibility.**
- SGP-GenBench evaluates compositionality specifically as **attribute binding, spatial relations, and numeracy**
  (arXiv:[2509.05208](https://arxiv.org/abs/2509.05208)) — the same three things that fail in text-to-image.

**4.3 Mathematical/semantic incorrectness of the figure itself.** ManiBench's **Visual-Logic Drift** — visuals
diverging from the intended mathematical logic through timing errors or missing causal relationships
(arXiv:[2603.13251](https://arxiv.org/abs/2603.13251)). ALGOGEN's diagnosis: forcing the model to simulate the
algorithm *and* satisfy rendering constraints simultaneously induces hallucination; decoupling raised success
**82.5% → 99.8%** (arXiv:[2605.12159](https://arxiv.org/abs/2605.12159)). Raiven's "**silent data errors**" — a
correct-looking chart bound to the wrong data — is the same class in the visualization domain
(arXiv:[2604.10008](https://arxiv.org/abs/2604.10008)).

**4.4 Scientific figure generation broadly.** **ScImage** — Zhang L., Eger S., Cheng Y. et al.,
arXiv:[2412.02368](https://arxiv.org/abs/2412.02368) (Dec 2024). Evaluates GPT-4o, Llama, AutomaTikZ, DALL-E,
StableDiffusion on **spatial understanding, numeric accuracy, and attribute comprehension**, in English, German,
Farsi, and Chinese, comparing code-based (Python/TikZ) against direct raster generation. Verbatim:
**"all models face challenges in this task, especially for more complex prompts."** GPT-4o handles single-dimension
tasks but degrades sharply when multiple comprehension types must be combined. **[B]**

**4.5 Vector-graphics generation generally.** A consistent picture across the SVG benchmark literature **[B]**:
- **VGBench** (arXiv:[2407.10972](https://arxiv.org/abs/2407.10972)): 4,279 understanding + 5,845 generation samples; LLMs show "less desirable performance on low-level formats (SVG)."
- **SVGenius** (arXiv:[2506.03139](https://arxiv.org/abs/2506.03139)): 2,377 queries, 24 domains; **"all models exhibit systematic performance degradation"** as complexity rises.
- **VCode** (arXiv:[2511.02778](https://arxiv.org/abs/2511.02778)): **"frontier VLMs struggle to generate faithful SVGs."**
- **VectorEdits** (arXiv:[2506.15903](https://arxiv.org/abs/2506.15903)): 270k+ SVG edit pairs; **"current methods struggle to produce accurate and valid edits."**
- **Socratic Chart** (arXiv:[2504.09764](https://arxiv.org/abs/2504.09764)): MLLMs suffer **up to a 30% performance drop when textual labels are removed from charts** — i.e. models are reading the text, not the geometry. Directly relevant to any "AI grades the student's diagram" application.
- **StarVector** (arXiv:[2312.11556](https://arxiv.org/abs/2312.11556)): notes **"pixel-based metrics like MSE fail"** for vector evaluation — an evaluation-methodology warning worth carrying.

**4.6 Reading diagrams is also broken, which bounds the feedback loop.** Text-to-Automata-Diagrams found VLM
descriptions of student-drawn diagrams "often incorrect" without human correction
(arXiv:[2603.07936](https://arxiv.org/abs/2603.07936)). Robertson C. & Wolff P., "LLM world models are mental:
Output layer evidence of **brittle** world model use in LLM mechanical reasoning," arXiv:[2507.15521](https://arxiv.org/abs/2507.15521) (Jul 2025), tests models on TikZ-rendered pulley systems and reports brittle
mechanical reasoning. **[B]** If the model cannot reliably *read* a mechanism diagram, VLM-in-the-loop critique
of generated mechanism diagrams inherits that ceiling.

**The meta-point about all these numbers.** Almost every "success rate" reported above (93.8%, 94% RSR, 99.8%,
100% compilation) is a measure of **artifact existence**, not pedagogical correctness. The two metrics that try
to do better — Code2Video's TeachQuiz (VLM learns from the video after unlearning) and DiagramIR (IR-level
agreement with human raters) — are both proxies, and neither has been validated against human learning gain.
**No paper in this literature measures whether a human learns anything from the generated video.** That gap
should be stated flatly in the survey.

---

## 5. Synthesis: the claims this survey section should make

1. **Animation's average effect on learning is small (g = 0.226, 95% CI [0.12, 0.33]; Berney & Bétrancourt 2016
   **[A]**) and the researchers themselves describe the three meta-analyses as showing effectiveness that is
   "rather limited" (Ploetzner et al. 2021 **[A]**).** Any survey claiming the AI-animation boom is
   pedagogically justified by the animation literature is misreading it.

2. **The best-supported moderator is "animate what changes."** Animation earns its keep for kinematic/procedural/
   mechanism content and not for conceptual structure (Ploetzner et al. 2020/2021 **[A]**). This is a directly
   actionable content-routing rule for a generation pipeline.

3. **Animation reliably raises perceived comprehensibility, interest, enjoyment and motivation without raising
   comprehension scores** (Kim, Yoon, Whang & Tversky 2007 **[A]**), and representational animation may
   *hurt* learning relative to directive animation (Paik & Schraw 2013 **[B]**). Meanwhile active learning
   raises real learning while *lowering* felt learning (Deslauriers et al. 2019 **[A]**). **Any generation
   pipeline optimized on preference is optimizing the illusion.** This is the sharpest thing this section
   can say to the AI-education field.

4. **Static, learner-paced, annotated illustrations beat narrated animations on transfer in Mayer's own
   experiments** (Mayer, Hegarty, Mayer & Campbell 2005 **[C]**). The cheapest artifact is often the best one.

5. **Interactivity, segmentation and learner pacing carry more of the effect than motion does** — transient
   information effect (Ayres & Paas; Leahy & Sweller **[B/C]**), system-paced moderator in Berney & Bétrancourt
   **[A]**, PhET's design-research tradition **[C]**, Freeman et al. 2014 on active learning **[A]**.
   **Implication: generate interactive artifacts (p5/Desmos/GeoGebra/Observable/Remotion-as-page), not just
   video.**

6. **Brilliant is a well-designed instantiation of principles with independent support, and has published no
   efficacy evidence of its own.** Its structure (≈13 exercises per lesson, problem-before-instruction,
   level reviews, learning paths) is measurable **[O]**; its outcome claims are absent, and the peer-reviewed
   literature on the platform is empty **[O — Crossref, absence]**.

7. **The LLM→animation toolchain literature has converged on one architecture: constrain the model to a
   verifiable intermediate representation and put the compiler/renderer/VLM in the loop.** Independent
   rediscoveries: ALGOGEN (VTA), SGA (symbolic scene graph), LASEV (executable script), Raiven (DSL), PairCoder++
   (toolchain-grounded pair review). PairCoder++ states the general law honestly: it helps "where the toolchain
   provides an informative oracle" and "ties or mildly regresses where the oracle is weak"
   (arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) **[B]**).

8. **The reported success rates are inflated by construction.** 93.8% "success" coexisting with "most videos
   exhibit visual layout issues" (arXiv:[2502.19400](https://arxiv.org/abs/2502.19400) **[B]**) is the field's
   own admission. Report compile-rate and correctness as separate numbers.

9. **No study in the LLM-generated-explanatory-video literature measures human learning gain.** The most
   ambitious metric (TeachQuiz) measures whether a *VLM* recovers knowledge from the video. This is the
   field's largest open gap and the most useful thing to point at.

10. **Tool choice has a pedagogy embedded in it.** Manim → beautiful non-interactive math video, no layout
    engine, fragmented API, MIT-licensed, aesthetically canonized by 3Blue1Brown. Remotion → web-native,
    CSS layout solves collisions, same artifact can be interactive, commercial licence above 3 employees.
    TikZ → static, compiles, best-studied, print-quality. Mermaid → structural only, cheapest and safest.
    Desmos/GeoGebra/p5/Observable → interactive, small declarative state, best aligned with what the learning
    evidence actually supports. **A survey that treats these as interchangeable rendering backends misses that
    they encode different theories of what an explanation is.** **[Interpretation.]**

---

## 6. Open questions for the survey

- Nobody has run the Tversky control in the AI era: **generated animation vs. an informationally equivalent
  generated static diagram, on human transfer.** It is cheap to run now and would be the highest-value
  experiment in this space.
- Does the metacognitive illusion (Kim et al. 2007) get *worse* with AI-generated video, given that generation
  pipelines are RLHF'd toward appealing output?
- Can generation be routed by content type — animate only kinematic/procedural targets per Ploetzner et al. —
  and does routing beat animate-everything on learning outcomes?
- Is the "LLM drawing surfaces reasoning flaws that prose hides" observation from TheoremExplainAgent
  reproducible? If so, generated diagrams are a *verification* instrument for model reasoning, independent of
  their pedagogical use.
- Does an LLM-generated *interactive* artifact (Desmos/GeoGebra/p5) outperform an LLM-generated video on
  learning, as the interactivity literature predicts?

---

## 7. Source index

**Learning-science evidence (peer-reviewed):**
1. Tversky, Morrison & Bétrancourt (2002) — 10.1006/ijhc.2002.1017 — **[C]**
2. Morrison & Tversky (2001) CHI EA — 10.1145/634288.634290 — **[C]**
3. Höffler & Leutner (2007) — 10.1016/j.learninstruc.2007.09.013 — **[C]**
4. Berney & Bétrancourt (2016) — 10.1016/j.compedu.2016.06.005 — **[A]** (OA: archive-ouverte.unige.ch/unige:92234)
5. Ploetzner, Berney & Bétrancourt (2020) — 10.1111/jcal.12476 — **[A]**
6. Ploetzner, Berney & Bétrancourt (2021) — 10.1007/s11251-021-09541-w — **[A]**
7. Mayer, Hegarty, Mayer & Campbell (2005) — 10.1037/1076-898x.11.4.256 — **[C]**
8. Paik & Schraw (2013) — 10.1037/a0030281 — **[B]**
9. Kim, Yoon, Whang, Tversky & Morrison (2007) — 10.1111/j.1365-2729.2006.00219.x — **[A]**
10. Lowe (1999) — 10.1007/BF03172967 — **[C]**
11. Lowe (2003) — 10.1016/s0959-4752(02)00018-x — **[C]**
12. Hegarty (2004) — 10.1016/j.learninstruc.2004.06.007 — **[C]**
13. Kriz & Hegarty (2007) — 10.1016/j.ijhcs.2007.06.005 — **[C]**
14. Ayres & Paas (2007a) — 10.1002/acp.1343 — **[C]**
15. Ayres & Paas (2007b) — 10.1002/acp.1351 — **[C]**
16. Leahy & Sweller (2012) — 10.1016/j.learninstruc.2012.05.004 — **[B]**
17. Mayer & Moreno (2003) — 10.1207/s15326985ep3801_6 — **[A]**
18. Mayer, CTML chapters — 10.1017/cbo9780511816819.004 / 10.1017/cbo9781139547369.005 / 10.1017/9781108894333.008 — **[C]**
19. Bétrancourt (2005) animation & interactivity principles — 10.1017/cbo9780511816819.019 — **[C]**
20. Rieber (1990) — 10.1007/bf02298250 — **[C]**
21. Freeman et al. (2014) — 10.1073/pnas.1319030111 — **[A]**
22. Deslauriers et al. (2019) — 10.1073/pnas.1821936116 — **[A]**
23. Perkins et al. (2006) PhET — 10.1119/1.2150754 — **[A/C]**
24. Wieman, Adams & Perkins (2008) — 10.1126/science.1161948 — **[C]**
25. Chan & Leung (2014) DGS meta-analysis — 10.2190/ec.51.3.c — **[C]**
26. Zulnaidi, Oktavika & Hidayat (2019) GeoGebra — 10.1007/s10639-019-09899-y — **[C]**
27. Kaya & Öçal (2018) GeoGebra meta-analysis (TR) — 10.17522/balikesirnef.505918 — **[C]**
28. Cantürk Günhan & Açan (2016) DGS meta-analysis (TR) — 10.16949/turcomat.67541 — **[C]**
29. Bhatia & Chakraborty (2024) Desmos — 10.1080/09747338.2024.2341068 — **[C]**
30. Liang (2015) Desmos/limits — 10.21890/ijres.62743 — **[C]**
31. Wong, Castro-Alonso, Ayres & Paas (2015) Lego manipulative animations — 10.1016/j.compedu.2014.12.022 — **[B]**
32. Ehrhart, Höffler, Grund & Lindner (2024) "Less might be more" — 10.1037/edu0000821 — **[C]**

**LLM → Manim / educational video (arXiv preprints, all [B]):**
33. TheoremExplainAgent — 2502.19400
34. ManiBench — 2603.13251
35. SGA / MVQS — 2607.18116
36. ManimTrainer + RITL — 2604.18364
37. ManimAgent (episodic memory) — 2606.30296
38. ALGOGEN — 2605.12159
39. Code2Video / MMMC / TeachQuiz — 2510.01174
40. Manimator — 2507.14306
41. LLM2Manim — 2604.05266
42. ANVIL — 2605.16295
43. PhysicsSolutionAgent — 2601.13453
44. TeachMaster — 2601.04204
45. LASEV — 2602.11790
46. MORSE-500 — 2506.05523
47. Manim for STEM Education — 2510.01187
48. PairCoder++ — 2607.01883

**TikZ / diagrams / SVG (arXiv, all [B]):**
49. AutomaTikZ — 2310.00367
50. DeTikZify — 2405.15306
51. TikZero — 2503.11509
52. TikZilla — 2603.03072
53. GeoTikzBridge — 2603.22687
54. vTikZ — 2505.04670
55. DiagramIR — 2511.08283
56. Text to Automata Diagrams — 2603.07936
57. ScImage — 2412.02368
58. Control-GPT — 2305.18583
59. SGP-GenBench — 2509.05208
60. VGBench — 2407.10972
61. SVGenius — 2506.03139
62. VCode — 2511.02778
63. VectorEdits — 2506.15903
64. Socratic Chart — 2504.09764
65. StarVector — 2312.11556
66. MermaidSeqBench — 2511.14967
67. Evaluating Ill-Defined Tasks (Mermaid case study) — 2603.17067
68. Raiven (DSL → D3/VTK.js) — 2604.10008
69. LLM world models are mental (brittle mechanical reasoning) — 2507.15521
70. See it. Say it. Sorted (sketch→SVG agentic) — 2508.15222

**Product / repository sources [O/V]:**
71. brilliant.org, brilliant.org/about, brilliant.org/courses, brilliant.org/courses/math-fundamentals
72. github.com/3b1b/manim; github.com/ManimCommunity/manim (+README, module tree, releases)
73. docs.manim.community
74. github.com/remotion-dev/remotion (+LICENSE.md); remotion.dev/docs/the-fundamentals, /docs/render, /docs/renderer
75. github.com/mermaid-js/mermaid; github.com/d3/d3; github.com/processing/p5.js; github.com/excalidraw/excalidraw; github.com/observablehq/framework; github.com/geogebra/geogebra

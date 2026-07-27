---
title: "Assessment Item Generation and Psychometrics Under Infinite Items"
wave: C
date_researched: 2026-07-27
sources_count: 128
---

# Assessment Item Generation and Psychometrics Under Infinite Items

> **Scope note.** §F1 handles assessment *philosophy* — the forgery margin, the abolition of
> detection, orals, verification-first design. This section handles the **measurement
> machinery**: how items get made, whether the numbers that come out the other end mean
> anything, and what a system is permitted to say about a score. F1 asks *what may be
> inferred*. C2 asks *with what precision, and on what calibration evidence*.

---

## 0. The inversion nobody has priced in

Here is the load-bearing observation, and it is not how the psychometric literature frames
itself.

**An item bank was never valuable because it contained items. It was valuable because it
contained *calibrated* items.** The scarce good was never the sentence with four options
underneath it — any competent teacher can write forty of those in an afternoon, and has.
The scarce good was the pair (item, θ-response-function), and that pair is expensive
because it requires field-testing against several hundred real examinees whose abilities
you already know. Item writing was a bottleneck; item *calibration* was the actual
bottleneck, and it was invisible because writing and calibrating were bundled in the same
budget line.

Generative models have driven the marginal cost of *item production* to approximately zero.
They have driven the marginal cost of *item calibration* to exactly zero times zero — which
is to say, they have not touched it at all. Calibration requires response data from humans.
There is no synthetic substitute, and the one place where a shortcut looked plausible
(predicting difficulty from item text) has a measured, disappointing ceiling (§4.4).

So the field has inverted. Pre-2022, you had few items and rich calibration per item.
Post-2022, you have unbounded items and approximately no calibration per item. Every
psychometric technique built on the old regime — internal-consistency reliability, item
exposure control, item-level equating, retrofitted Q-matrices, item banking itself —
either breaks, becomes vacuous, or must be rebuilt around a different unit of analysis.

The rest of this section works out what that rebuild looks like, and ends with a standard
(§10) that a system can actually be held to.

**The single most important consequence, stated up front:** when items are generated on
demand, the object you calibrate is *the generator*, not the item. Everything follows from
that. A generator has a difficulty distribution, not a difficulty. A score derived from
samples out of that distribution carries two variance components — person uncertainty *and*
item-sampling uncertainty — and essentially every shipping system in 2026 reports only the
first (§4.3). That omission is not a rounding error; on the published within-family variance
estimates it is often the larger of the two.

---

## 1. Automatic Item Generation: the pre-LLM tradition

### 1.1 The architecture

AIG as a discipline predates LLMs by roughly three decades, and its intellectual apparatus
is better than what has replaced it. The founding collections are Irvine & Kyllonen's
*Item Generation for Test Development*
([doi:10.4324/9781410602145](https://doi.org/10.4324/9781410602145)) and Gierl & Haladyna's
*Automatic Item Generation*
([doi:10.4324/9780203803912](https://doi.org/10.4324/9780203803912)). `OBSERVED`

The canonical method is three-step (Gierl, Lai & Turner 2012, *Medical Education* 46:757–765,
[doi:10.1111/j.1365-2923.2012.04289.x](https://doi.org/10.1111/j.1365-2923.2012.04289.x)):

1. **Cognitive model.** A subject-matter expert specifies the knowledge, skills and
   problem-solving steps the item is to elicit, and the *sources of variation* that make
   instances differ.
2. **Item model.** A template — a stem with slots (`elements`) and constrained value sets
   for each slot, plus the logic that computes the key and the distractors from the slot
   values.
3. **Generation.** Combinatorial expansion under the constraints.

Gierl & Lai formalised the item-model layer in *International Journal of Testing*
([doi:10.1080/15305058.2011.635830](https://doi.org/10.1080/15305058.2011.635830)),
distinguishing **strong-theory** models (the cognitive model fully predicts the psychometric
properties of each instance) from **weak-theory** models (the template is a surface
scaffold and the properties must be discovered empirically). `OBSERVED`

That distinction is the whole ballgame, and the LLM literature has almost entirely forgotten
it. An LLM prompted to "write five questions about photosynthesis" is a **weak-theory
generator with no template at all** — the weakest possible case, with none of the
compensating machinery.

### 1.2 What pre-LLM AIG actually achieved

- **Blind expert review, medical MCQs.** Gierl & Lai 2013, *Medical Education*
  ([doi:10.1111/medu.12202](https://doi.org/10.1111/medu.12202)): 45 therapeutics items in
  three arms (Group 1 traditional, Group 1 AIG, Group 2 traditional), rated by a four-member
  expert medical panel on eight indicators of MCQ quality. AIG and traditional items were
  **comparable on seven of eight indicators**; the eighth — where AIG lost — was **distractor
  plausibility**. In a blind classification task the panel's accuracy at identifying which
  items were machine-generated was **42%**, i.e. below the 50% chance rate for a two-class
  decision. `MEASURED-BENCH`
  → Note the shape of this result carefully. It is *exactly* the shape that recurs in the
  LLM era eleven years later: generated items pass on stem quality, fail on distractors,
  and are indistinguishable to reviewers who are not specifically looking at distractors.

- **Operational psychometrics.** Gierl, Lai, Pugh, Touchie, Boulais & De Champlain 2016,
  *Applied Measurement in Education*
  ([doi:10.1080/08957347.2016.1171768](https://doi.org/10.1080/08957347.2016.1171768))
  put generated items into live medical assessment and evaluated their empirical
  characteristics. `MEASURED-BENCH`

- **Predictable psychometrics from item structures.** Embretson & Kingston 2018, *Journal of
  Educational Measurement* ([ERIC EJ1171125](https://eric.ed.gov/?id=EJ1171125)): generated
  mathematics achievement items were put through multi-stage qualitative review and then
  operational tryout. High success rates; **items generated from the same item structure had
  predictable psychometric properties**, supporting a more limited and expedient review
  process. `MEASURED-BENCH`

- **Progress testing, IRT-level.** Falcão, Pereira, Pêgo & Costa 2024, *Education and
  Information Technologies* ([ERIC EJ1416068](https://eric.ed.gov/?id=EJ1416068)): 126
  five-option MCQs (23 AIG) from the 2021 University of Minho medical progress test,
  analysed with IRT, dimensionality, item fit, DIF and distractor analysis. AIG items were
  **parallel to hand-written items on difficulty and information**, with a **similar
  proportion of functional distractors**, and expert review rated AIG item *quality* higher.
  `MEASURED-BENCH`
  → This is the best single pre-LLM result and the strongest counterexample to "AIG can't
  do distractors." It is also, crucially, *strong-theory template* AIG with expert-authored
  cognitive models — not free-form generation.

- **Non-English, non-medical.** Rafatbakhsh et al. 2021, *EMIP*
  ([ERIC EJ1298981](https://eric.ed.gov/?id=EJ1298981)): corpus-driven AIG for English
  idioms; 400 generated items reviewed by ten TEFL experts, 40-item sample administered to
  110 learners and validated by Rasch. Most items acceptable on both criteria.
  `MEASURED-BENCH`

- **Neural AIG before ChatGPT.** von Davier 2018, *Psychometrika*
  ([doi:10.1007/s11336-018-9608-y](https://doi.org/10.1007/s11336-018-9608-y)) used RNNs
  for item generation; Hommel et al. 2022, *Psychometrika*
  ([doi:10.1007/s11336-021-09823-9](https://doi.org/10.1007/s11336-021-09823-9)) extended
  transformer-based, construct-specific generation to *non-cognitive* constructs, where
  template AIG had never worked because personality/attitude items have no combinatorial
  slot structure. `MEASURED-BENCH`

### 1.3 The economics, which nobody quotes

Kosh, Simpson, Bickel, Kellogg & Sanford-Moore 2019, *EMIP*
([ERIC EJ1209262](https://eric.ed.gov/?id=EJ1209262)) did the only careful cost-benefit
analysis. AIG has a large fixed cost (cognitive model + item model development + tooling)
and a near-zero marginal cost; manual writing is the reverse. Break-even in K-12 mathematics
was **173 to 247 items within a single fine-grained content area** (e.g. "area of figures,
grades 4–7"). `MEASURED-BENCH`

Two implications the LLM discourse ignores:
- The break-even is *per content area*, not per programme. A system covering 4,000 fine-grained
  objectives needs 4,000 × ~200 items before template AIG pays — which is precisely the
  regime where an adaptive tutor operates, and precisely why LLM generation (fixed cost ≈ one
  prompt) is genuinely transformative rather than merely faster.
- Kosh's cost model prices *item development*. It does not price calibration, review, or the
  ongoing security cost. Under LLM generation the development term collapses and **review
  becomes 100% of the cost**. Optimising the wrong term is the field's dominant error.

### 1.4 Saturation: generators run out of items before you do

Cole, Lima-Walton, Brunnert, Vesey & Raha 2020, *Journal of Applied Testing Technology*
([ERIC EJ1227607](https://eric.ed.gov/?id=EJ1227607)) demonstrated **diminishing marginal
syntactic return** for AIG using a saturation-detection approach, and built an unsupervised
clustering pipeline to partition a generated bank into syntactically distinct clusters for
test assembly. `MEASURED-BENCH`

This is the quiet refutation of "infinite items." A generator's *effective* item count is
the number of psychometrically and syntactically distinguishable instances it can emit, and
that number saturates well below the combinatorial count. A learner who sees 30 probes from
one template has not seen 30 independent observations. Treat generator output as a
**population with an effective sample size**, and measure that ESS.

---

## 2. The LLM era: what quality is actually reached

### 2.1 The headline synthesis

The single most useful source is the newest: Kıyak, Kaya & Emekli 2026, "Validity of
AI-generated multiple-choice questions in medical education: a systematic review",
*Postgraduate Medical Journal*
([doi:10.1093/postmj/qgag057](https://doi.org/10.1093/postmj/qgag057)). PRISMA 2020, four
databases through 15 Feb 2026, 1,352 records screened, **71 studies from 24 countries**,
JBI quality appraisal, findings organised by Messick's five sources of validity evidence.
`MEASURED-META`

Its numbers are the best available calibration on the whole field:

| Quantity | Value |
|---|---|
| Studies reporting **content** evidence | 71 / 71 |
| Reporting **relations to other variables** | 40 / 71 |
| Reporting **response process** | 35 / 71 |
| Reporting **internal structure** | 31 / 71 |
| Reporting **consequences** | 25 / 71 |
| **Error rate in generated items** | **<1% to 45%** |
| Median item difficulty (p) | 0.67 |
| Median discrimination | 0.28 |
| Test reliability range | 0.51 – 0.81 |
| Reported efficiency gain | up to **31×** time saving |

Conclusion, verbatim: LLMs "appear useful drafting tools but current evidence does not yet
support unsupervised use in summative assessment."

Read the error-rate row again. **The spread is two orders of magnitude across studies**, and
nothing in the literature predicts where in [<1%, 45%] a given deployment will land. That
variance — not the mean — is the governing fact for anyone building a system. A pipeline
that assumes 2% and gets 40% ships a broken test.

Also note the *median discrimination of 0.28*. Classical item-analysis convention treats
D ≥ 0.30 as acceptable and D ≥ 0.40 as good. The median AI-generated item in the published
literature sits just below the acceptability line.

Supporting reviews:
- Kıyak & Emekli 2024, *Postgraduate Medical Journal*
  ([doi:10.1093/postmj/qgae065](https://doi.org/10.1093/postmj/qgae065)): 1,920 records
  screened, 23 studies; catalogues the prompts used and the validity evidence claimed;
  "mixed accuracy rates," some comparable to human items, others differing in difficulty and
  discrimination. `MEASURED-META`
- Tan, Armoush, Mazzullo, Bulut & Gierl 2025, *IJATE*
  ([ERIC EJ1476463](https://eric.ed.gov/?id=EJ1476463)): 60 LLM-AIG studies across seven
  databases. Verdict: "**many studies have overlooked the quality of the generated items,
  indicating a lack of a solid educational foundation.**" `MEASURED-META`
- Kurdi, Leo, Parsia, Sattler & Al-Emari 2020, *IJAIED*
  ([doi:10.1007/s40593-019-00186-y](https://doi.org/10.1007/s40593-019-00186-y)): the
  pre-LLM AQG review, and still the best taxonomy of evaluation practice — which it finds
  to be dominated by intrinsic, non-psychometric metrics. `MEASURED-META`
- Falcão, Costa & Pêgo 2022, *Advances in Health Sciences Education*
  ([ERIC EJ1336013](https://eric.ed.gov/?id=EJ1336013)): narrative review, 119 records
  screened, 10 studies included; concludes AIG is feasible and valid but explicitly notes
  "there is still no evidence to encourage a general application." `MEASURED-META`

### 2.2 The primary studies, with their numbers

**Cheung et al. 2023, PLOS ONE**
([doi:10.1371/journal.pone.0290691](https://doi.org/10.1371/journal.pone.0290691)) —
multinational (HK, Singapore, Ireland, UK). 50 ChatGPT MCQs vs 50 professor-written MCQs
from the same textbooks; five independent international assessors scoring five domains.
`MEASURED-BENCH`
- Generation time: **20 min 25 s (ChatGPT) vs 211 min 33 s (two human examiners)** — ~10×.
- Only one domain differed significantly: **relevance**, AI 7.56 ± 0.94 vs human 7.88 ± 0.52,
  p = 0.04.
- No significant difference on total score or other domains.
- **"Questions generated by A.I. yielded a wider range of scores, while those created by
  humans were consistent and within a narrower range."**

That last sentence is the most important finding in the LLM-AIG literature and it is almost
never quoted. **The mean is fine; the variance is not.** Human item writers are a
low-variance process. LLMs are a high-variance process with a comparable mean. For a
*formative* system that draws many samples, high variance is tolerable — errors average out
across probes. For a *summative* decision resting on 20 items, high variance is fatal,
because the realised test is a single draw.

**Dhanvijay et al. 2025, *Advances in Physiology Education***
([ERIC EJ1490902](https://eric.ed.gov/?id=EJ1490902)) — 200 physiology MCQs (100 faculty,
100 DeepSeek R1), 50 from each arm administered to undergraduate medical students.
`MEASURED-BENCH`
- Difficulty index: **chatbot 0.64 ± 0.22 vs faculty 0.47 ± 0.19, p < 0.0001** (AI items
  markedly easier).
- Discrimination index: **no significant difference, p = 0.17**.
- Non-functioning distractors: **faculty median 0 vs chatbot median 1, p = 0.0063**.
- Authors' conclusion: "AI can complement but not yet replace human expertise."

**Young, Courtney, Kah, Wilkerson & Chen 2025, *Teaching of Psychology***
([ERIC EJ1474433](https://eric.ed.gov/?id=EJ1474433)) — 20 GPT-4-generated items from a
psychology textbook chapter, 190 undergraduates, IRT analysis plus expert review.
`MEASURED-BENCH`
- Items were **low in difficulty and high in discrimination**.
- Expert reviewers found nearly all items logically sound, aligned to objectives, and
  meeting prevailing MCI standards.
- Explicit recommendation: use for **formative, not summative** assessment, *because of the
  uniformly low difficulty*.

**Gündeger Kilci 2025, *IJATE***
([ERIC EJ1491386](https://eric.ed.gov/?id=EJ1491386)) — ChatGPT vs DeepSeek, one 5-option
item per each of 10 Bloom-aligned learning outcomes, expert review, then 120 students.
`MEASURED-BENCH`
- Inter-expert agreement **Kendall's W = 0.58** — moderate, and itself a warning about
  using expert review as a gold standard.
- No significant differences between models on difficulty, discrimination, variance or
  reliability; KR-20 and split-half "acceptable for a classroom-based assessment."
- **"Most revisions focused on improving distractor quality."**
- A generalisability/decision study on the *expert ratings* recommended a minimum of
  **seven experts** for reliable item-quality evaluation.
  → Quietly devastating for the review-cost story: if you need 7 raters to reliably judge
  an item's quality, "human-in-the-loop review" is not cheap, and single-reviewer QA is
  measurement theatre.

**Doughty et al. 2024, ACE '24**
([doi:10.1145/3636243.3636256](https://doi.org/10.1145/3636243.3636256), preprint
[arXiv:2312.03173](https://arxiv.org/abs/2312.03173)) — the largest CS-education comparison:
**651 GPT-4-generated and 449 human-crafted MCQs** aligned to **246 learning objectives**
across **6 Python courses**. GPT-4 produced items with clear language, a single correct
choice, high-quality distractors, and good LO alignment. `MEASURED-BENCH`
→ Caveat that matters: this is *expert-rated* quality, not response-data psychometrics. No
θ, no discrimination indices, no field test.

**Ripoll y Schmitz & Sonnleitner 2025, *Large-scale Assessments in Education***
([ERIC EJ1477454](https://eric.ed.gov/?id=EJ1477454)) — GPT-4-generated German reading
comprehension passages for Luxembourg's large-scale assessment, blinded online review with
**N = 89** reviewers. Reviewers **could not consistently identify authorship**. One-shot
prompts anchored to a Text Analysis Cognitive Model were effective for *informative* texts;
**human-written texts remained superior for narratives**. `MEASURED-BENCH`
→ The narrative/informative split is a real and reproducible boundary, and it maps onto
the strong-theory/weak-theory distinction: informative text has enumerable propositional
structure; narrative does not.

**Falcão et al. 2024** (above) remains the only study in this cluster with full IRT + DIF +
distractor analysis on operational data.

### 2.3 Machine review of machine items

Gorgun & Bulut 2025, *EMIP* ([ERIC EJ1460469](https://eric.ed.gov/?id=EJ1460469)):
instruction-tuned **Llama 3-8B** used to evaluate automatically generated cloze items. The
tuned model "was able to filter out the majority of good and bad items accurately," and the
authors position it as an **intermediate triage step between generation and field testing**,
not as a replacement for review. `MEASURED-BENCH`

This is the correct architecture and should be adopted: *generate → machine-screen →
human-review the survivors → field-test → calibrate*. The machine screen's job is to raise
the human reviewer's yield, not to substitute for them. There is a live, unaddressed
circularity risk — a screener trained on one model family scoring items from that same
family — and no published study has tested cross-family screening. **Open problem.**

---

## 3. Distractor generation: the hard part, and the actual dividing line

### 3.1 What a concept inventory does that a quiz does not

The Force Concept Inventory (Hestenes, Wells & Swackhamer 1992, *The Physics Teacher*,
[doi:10.1119/1.2343497](https://doi.org/10.1119/1.2343497)) is the template for
*diagnostic* multiple choice, and its construction procedure is the point. Distractors are
not written to be plausible. They are **transcribed from what students actually said** in
open-ended administration and interview. `OBSERVED`

The modern instantiation is explicit and repeated:
- Erceg, Aviani, Mešić, Glunčić & Žauhar 2016, *PRPER*
  ([ERIC EJ1122500](https://eric.ed.gov/?id=EJ1122500)): literature review → think-alouds
  on open-ended questions → **"transformed the open-ended questions into multiple-choice
  questions, whereby distractors were based on the results of the think alouds"** → 22 items
  → 250 students across universities → teacher-survey content validity. `MEASURED-BENCH`
- Flame Test Concept Inventory ([ERIC EJ1166996](https://eric.ed.gov/?id=EJ1166996)):
  52 students interviewed about atomic emission before any item was drafted.
- Reaction Coordinate Diagram Inventory ([ERIC EJ1263565](https://eric.ed.gov/?id=EJ1263565))
  and the Quantization and Probability Representations Inventory
  ([ERIC EJ1224931](https://eric.ed.gov/?id=EJ1224931)): both sequential mixed-methods,
  distractors generated from semi-structured interview analysis.
- Resonance Concept Inventory ([ERIC EJ1445121](https://eric.ed.gov/?id=EJ1445121)) states
  the definition outright: "a multiple-choice assessment where the incorrect answer choices
  stem from commonly held alternate conceptions."

**This is the distinction that separates diagnostic from decorative assessment.** A
decorative distractor is wrong. A diagnostic distractor is wrong *in a specific, named,
empirically attested way*, such that selecting it is itself an informative event — it
localises the learner in a space of misconceptions rather than merely on a scale of
correctness.

### 3.2 Distractors carry structure, and it is measurable

- Scott & Schumayer 2018, *PRPER*
  ([ERIC EJ1168701](https://eric.ed.gov/?id=EJ1168701)): FCI incorrect responses form
  **distinct groupings**, the two largest corresponding to the *impetus* worldview; certain
  "central" items anchor the groupings and "connector" items bridge them. The wrong answers
  are not noise; they are a **coherent alternative theory of mechanics**. `MEASURED-BENCH`
- Wells, Henderson, Stewart, Stewart, Yang & Traxler 2019, *PRPER*
  ([ERIC EJ1227806](https://eric.ed.gov/?id=EJ1227806)): modified module analysis on
  **N_pre = 4,509 / N_post = 4,716**. Recovered **9 incorrect-answer groups pre-instruction
  and 11 post-instruction**, most mapping onto the misconceptions the FCI authors used to
  build the distractors. `MEASURED-BENCH`
  **Negative sub-result:** not all recovered groups were misconceptions — several were
  artifacts of the FCI's blocked item structure (multiple items sharing a stem). And the
  identified groups had **little relation** to previously reported gender-unfair items, so
  differences in misconception structure **cannot** explain the FCI's reported gender gap.
  → Two lessons: (a) distractor-based diagnosis recovers real structure *and* item-format
  artifacts, and you cannot tell them apart without the analysis; (b) a plausible causal
  story about subgroup differences was tested and failed.

- Distractors carry *ability* information too, and the psychometric machinery to use it
  exists: Rasch distractor models ([ERIC EJ562026](https://eric.ed.gov/?id=EJ562026)),
  information-bearing distractors deserving partial credit
  ([ERIC EJ954592](https://eric.ed.gov/?id=EJ954592)), the multidimensional nested logit
  model ([ERIC EJ959349](https://eric.ed.gov/?id=EJ959349)), and differential distractor
  functioning ([ERIC EJ617262](https://eric.ed.gov/?id=EJ617262)). Almost no generated-item
  system uses any of it. `OBSERVED`

### 3.3 Can a model generate a *misconception* distractor? The measured answer is: partly

This is the crux question of the section and the literature answers it with unusual clarity.

**The core negative result.** Feng, Lee, McNichols, Scarlatos, Smith, Woodhead, Ornelas &
Lan 2024, "Exploring Automated Distractor Generation for Math Multiple-choice Questions via
Large Language Models," *Findings of NAACL 2024*
([doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193),
[aclanthology.org/2024.findings-naacl.193](https://aclanthology.org/2024.findings-naacl.193/)).
Wide sweep of LLM approaches — in-context learning through fine-tuning — on a real-world
math MCQ dataset. Verbatim conclusion: **"although LLMs can generate some mathematically
valid distractors, they are less adept at anticipating common errors or misconceptions among
real students."** `MEASURED-BENCH` ← **primary negative result for this section**

That sentence is the whole distinction, empirically confirmed. *Mathematically valid* =
decorative. *Anticipating real student error* = diagnostic. The models do the first and not
the second, and the gap is not a prompting problem — it survived fine-tuning.

**Why**, mechanistically: an LLM's prior over "wrong answer" is a prior over *plausible
text*, learned from a corpus in which correct answers dominate and student errors are
rare and unlabelled. The empirical distribution of student errors is a different
distribution entirely, and it is *not recoverable from text describing the domain*. It is
recoverable only from **response data**. `INFERENCE`

**The constructive answer, and it confirms the mechanism.** Fernandez, Scarlatos, Feng,
Woodhead & Lan 2024, "DiVERT: Distractor Generation with Variational Errors Represented as
Text," *EMNLP 2024*
([doi:10.18653/v1/2024.emnlp-main.512](https://doi.org/10.18653/v1/2024.emnlp-main.512),
[aclanthology.org/2024.emnlp-main.512](https://aclanthology.org/2024.emnlp-main.512/)).
Instead of generating distractors directly, DiVERT learns an **interpretable latent
representation of the *error*** — expressed as text — and generates the distractor from
the error. Evaluated on **1,434 real math questions used by hundreds of thousands of
students**. `MEASURED-BENCH`
- A **7B open-source model with DiVERT beat GPT-4o-based state-of-the-art** on downstream
  distractor generation.
- Math educators judged DiVERT's **error labels of comparable quality to human-authored
  ones**.

Read those two papers together and the design rule falls out: **do not ask a model for a
wrong answer; ask it for an error, ground the error in observed response data, and derive
the wrong answer from the error.** Model the misconception as a first-class object. That is
also, not coincidentally, exactly what the concept-inventory methodology does with
interviews — DiVERT is automated think-aloud analysis.

**Independent replication of the limitation, different domain, different method.**
Wang & Meng 2026, *Language Testing*
([ERIC EJ1501926](https://eric.ed.gov/?id=EJ1501926)): L2 listening MCQs, response data from
**2,267 EFL Chinese undergraduates**, problematic distractors identified via a **two-parameter
logistic nested logit model (2PLNLM)**, then iteratively revised by GenAI under
principle-based prompts with human expert feedback, then re-evaluated by expert judgment and
cosine-similarity analysis. GenAI "effectively enhanced distractor quality by maintaining
content and structural alignment and ensuring semantic independence" — **but "struggled to
fully capture listening miscomprehension patterns and contextualized language use."**
`MEASURED-BENCH`
→ Same finding as Feng et al., in a different modality, with the psychometrics attached:
LLMs fix *form*, not *diagnosticity*. And note the pipeline shape — **response data first,
generation second**. This is the strongest published template for distractor repair.

**Convergent evidence from item analysis.** Every LLM-vs-human comparison that measured
distractor function found the same asymmetry: Gierl & Lai 2013 (distractor plausibility the
sole failing indicator of eight); Dhanvijay et al. 2025 (NFD median 1 vs 0, p = 0.0063);
Gündeger Kilci 2025 ("most revisions focused on improving distractor quality"). Falcão et al.
2024 is the exception — equal functional-distractor proportion — and it used expert-authored
**cognitive models with explicit distractor logic**, not free generation. `MEASURED-BENCH`

### 3.4 Distractor engineering that works, and evaluation that doesn't

- **Distractor suites** (Kosh 2021, *JATT*,
  [ERIC EJ1296053](https://eric.ed.gov/?id=EJ1296053)): rather than specifying each option
  independently, specify a *suite* of options that must cohere across all possible stem
  instantiations — solving both the "options don't blend" problem and the specification-labour
  problem in template AIG. `OBSERVED`
- **Evaluation metrics are broken.** Ghanem & Fyshe, "DISTO," EDM 2024
  ([ERIC ED675568](https://eric.ed.gov/?id=ED675568)): distractor-generation models are
  routinely evaluated with **machine-translation metrics** (BLEU and relatives), which
  reward surface overlap with a reference distractor and are indifferent to whether the
  distractor attracts anyone. `OBSERVED` — a whole subfield optimising a metric with no
  measurement-theoretic justification.
- **Systematic review:** Awalurahman & Budi 2024, *PeerJ Computer Science*
  ([doi:10.7717/peerj-cs.2441](https://doi.org/10.7717/peerj-cs.2441)) — 60 distractor-generation
  studies, 2009–2024, across ACM DL, IEEE Xplore, ScienceDirect and Scopus. `MEASURED-META`
- **Distractors leak construct-irrelevant signal.** DeVore, Stewart & Stewart 2016, *PRPER*
  ([ERIC EJ1122481](https://eric.ed.gov/?id=EJ1122481)): >9,500 students at one university
  and >2,500 at another. **Student avoidance of "none of the above" / "zero" distractors was
  statistically significant, and distractor position significantly affected selection
  probability.** Testwiseness itself produced little post-instruction score effect on
  modified instruments — a genuine null — but the option-level biases are real.
  `MEASURED-BENCH`
  → For generated items this is an actionable constraint: **randomise option order per
  administration** (free when items are generated), and **forbid "none of the above" in
  generated stems** unless the cognitive model specifically calls for it.

---

## 4. Psychometrics when items are infinite

### 4.1 The unit of calibration moves from item to generator

The theory for this was worked out for *item cloning* two decades before anyone typed a
prompt.

**Glas & van der Linden 2003**, "Computerized Adaptive Testing With Item Cloning,"
*Applied Psychological Measurement*
([doi:10.1177/0146621603027004001](https://doi.org/10.1177/0146621603027004001)). The
central move: a **multilevel (hierarchical) IRT model** in which the 3PL parameters of the
clones in a family are themselves draws from a family-level distribution. You estimate the
*hyperparameters* of that distribution — the family's mean difficulty and, critically, its
**within-family variance**. Adaptive administration becomes two-stage: **select the family
optimal at the current θ̂, then sample an item at random from within it.** Validated by
simulation on an LSAT item pool. `MEASURED-BENCH`

Everything a modern generative assessment system needs is in that paper. It has 88
citations. The generative-AI education literature cites it approximately never.

The surrounding apparatus:
- **Sinharay, Johnson & Williamson 2003**, *JEBS*
  ([doi:10.3102/10769986028004295](https://doi.org/10.3102/10769986028004295)): MCMC
  estimation of the Glas–van der Linden model plus the **Family Expected Response Function
  (FERF)** — the probability of a correct response to an item *drawn at random from a
  family*, as a function of θ. **The FERF is the correct summary object for a generator.**
  `MEASURED-BENCH`
- **Johnson & Sinharay 2005**, *APM*
  ([doi:10.1177/0146621605276675](https://doi.org/10.1177/0146621605276675)): extension to
  polytomous families, family score functions, Bayes-factor model selection between the
  hierarchical and the simple (isomorphic) model. `MEASURED-BENCH`
- **Geerlings, Glas & van der Linden 2011**, "Modeling Rule-Based Item Generation,"
  *Psychometrika* ([doi:10.1007/s11336-011-9204-x](https://doi.org/10.1007/s11336-011-9204-x)):
  hierarchical IRT where families are defined by **combinations of design rules**, so
  parameters are modelled as functions of the rules themselves — Bayesian, data-augmented
  Gibbs. This is the LLTM tradition made generative. `MEASURED-BENCH`
- **Cho, De Boeck, Embretson & Rabe-Hesketh 2014**, "Additive Multilevel Item Structure
  Models with Random Residuals," *Psychometrika*
  ([doi:10.1007/s11336-013-9360-2](https://doi.org/10.1007/s11336-013-9360-2)): latent
  regressions of *both* discrimination and difficulty on covariates at item and
  item-category levels, **with random residuals at both levels**. The random residual is the
  admission that item features never fully determine item parameters — the irreducible
  generator noise. `MEASURED-BENCH`
- **Geerlings, van der Linden & Glas 2012**, "Optimal Test Design With Rule-Based Item
  Generation," *APM* ([doi:10.1177/0146621612468313](https://doi.org/10.1177/0146621612468313)):
  three regimes — (a) assemble from pregenerated calibrated items; (b) **generate on the fly
  from calibrated item families**; (c) **generate on the fly directly from calibrated
  features**. Cases (b) and (c) "do not assume any item calibration under a regular response
  theory model." Results "highlight both the effects of **within-family item-parameter
  variability** and the severity of the constraint sets on optimal solutions."
  `MEASURED-BENCH`

Case (c) is the theoretical target state for an LLM-driven system: **you calibrate the
feature space, and the generator instantiates within it.** The theory exists. Nobody has
built it on top of an LLM. **Open problem, and the highest-value one in this section.**

### 4.2 The isomorphy assumption fails, and there is a number for it

The convenient assumption is that instances from one template are *isomorphs* —
psychometrically interchangeable. If true, calibrate once, ship forever. It is largely false.

**Fu, Choe, Lim & Choi 2022**, "An Evaluation of Automatic Item Generation: A Case Study of
Weak Theory Approach," *EMIP* ([ERIC EJ1357630](https://eric.ed.gov/?id=EJ1357630)). Three
instances from each of **23 templates** built for a large-scale assessment were pilot-tested
and evaluated with a new **differential child item functioning (DCIF)** analysis. Result:
`MEASURED-BENCH` ← **second primary negative result**

| Outcome | Templates |
|---|---|
| Successfully generated isomorphic instances | **9 / 23 (39%)** |
| Required **minor** revision to become isomorphic | 5 / 23 (22%) |
| Required **major** modification | **9 / 23 (39%)** |

**Fewer than two in five hand-built, expert-authored templates produced psychometrically
equivalent instances without revision.** These were deliberate, strong-effort templates for
an operational large-scale assessment. A free-form LLM prompt is a far weaker generator, and
there is no reason to expect it to do better.

Corroboration: **Sinharay & Johnson 2008**, "Use of Item Models in a Large-Scale Admissions
Test: A Case Study," *International Journal of Testing*
([doi:10.1080/15305050802262019](https://doi.org/10.1080/15305050802262019),
[ERIC EJ805764](https://eric.ed.gov/?id=EJ805764)) frames the central research question as
"**whether these items are isomorphic; that is, if they behave the same psychometrically**,"
develops rough diagnostics plus a statistical diagnostic for degree of isomorphicity, and
closes by noting that **scoring under item models "is an area that needs more research."**
`MEASURED-BENCH`

Eighteen years later it still is. The scoring problem — *how do you convert responses to
never-repeated items into a comparable score* — has no settled answer, and it is now the
operative problem for every adaptive tutor on the market.

**Operational rule this implies:** *isomorphy is a hypothesis to be tested per template, not
a property to be assumed.* DCIF (Fu et al.) and the Sinharay–Johnson diagnostics are the
tests. A system that has never run them is asserting isomorphy on faith, and the base rate
for that faith being justified is 39%.

### 4.3 Item-sampling variance: the missing term in every shipped SE(θ)

This is the most consequential technical claim in this section, so state it precisely.

Under a fixed-form or calibrated-bank test, the standard error of θ̂ is
`SE(θ̂) = 1/√I(θ̂)`, with `I(θ̂)` the test information — the sum of item informations for
the *specific items administered, whose parameters are known*. Under generation-on-demand,
the administered items' parameters are **not known**; they are draws from a family
distribution. The posterior variance of θ therefore has two components:

```
Var(θ̂)  =  Var(θ̂ | item parameters)        ← the term everyone reports
         +  E[ Var(θ̂ | θ) induced by sampling items from the family ]   ← the missing term
```

The second term is a direct function of the **within-family parameter variance**, the exact
quantity that Glas & van der Linden's hyperparameters estimate, that Geerlings et al. 2012
found "highlight[ed]" in optimal-design solutions, and that Cho et al. 2014 carry as random
residuals. `MEASURED-BENCH` for the existence and estimability of the term; `INFERENCE` for
the claim that shipping systems omit it.

The inference is well supported by absence: across the 71 studies in Kıyak et al. 2026
([doi:10.1093/postmj/qgag057](https://doi.org/10.1093/postmj/qgag057)) and the 60 in Tan et
al. 2025 ([ERIC EJ1476463](https://eric.ed.gov/?id=EJ1476463)), **no reported study
propagates item-sampling variance into the reported score precision.** Tan et al.'s finding
that most studies "overlooked the quality of the generated items" is the same absence seen
from a different angle. `MEASURED-META`

**Consequence, stated bluntly.** A generative assessment system that reports "your estimated
mastery is 0.72 ± 0.05" where the ±0.05 is computed as though the items were calibrated
fixed items is reporting a **number that is too small by an unknown factor**. Given Fu et
al.'s 39% isomorphy rate, the neglected term is not small. Every downstream decision rule
calibrated on that SE — mastery thresholds, "you're ready to advance," intervention triggers
— inherits the error and fires too often.

The fix is not exotic. It is: **estimate the within-generator variance from field data, and
add it.** §10 makes this a requirement.

### 4.4 Can you calibrate without field-testing? Partially, and the ceiling is known

The dream is text-to-difficulty: predict item parameters from the item itself, skip the
field test. The field has run this as a shared task on high-quality operational data.

**Yaneva, North, Baldwin, Ha, Rezayi, Zhou, Ray Choudhury, Harik & Clauser 2024**,
"Findings from the First Shared Task on Automated Prediction of Difficulty and Response
Time for Multiple-Choice Questions," BEA @ NAACL 2024
([aclanthology.org/2024.bea-1.39](https://aclanthology.org/2024.bea-1.39/)). **667 retired
USMLE® MCQs** with real difficulty and mean response times; **17 teams submitted, 12 filed
system reports.** `MEASURED-BENCH`

**Bulut, Gorgun & Tan 2024**, "Item Difficulty and Response Time Prediction with Large
Language Models: An Empirical Analysis of USMLE Items," same workshop
([aclanthology.org/2024.bea-1.44](https://aclanthology.org/2024.bea-1.44/)): BiomedBERT best
for difficulty, fine-tuned FastText best for response time — **different feature families
win on the two targets**, indicating the difficulty signal in item text is weak and
domain-specific rather than general. `MEASURED-BENCH`

**Štěpánek, Dlouhá & Martinková 2023**, *Mathematics*
([doi:10.3390/math11194104](https://doi.org/10.3390/math11194104)): systematic comparison of
regularisation, SVMs, trees, random forests, backprop networks and Naïve Bayes for
predicting reading-comprehension item difficulty from item text — **benchmarked against
domain experts**. Elastic net won on RMSE for continuous difficulty; random forests on
classification. Conclusion: ML on item-text features **"can compete with predictions made by
domain experts"** and should be used to **inform** expert predictions, **"especially when
item pre-testing is limited or unavailable."** `MEASURED-BENCH`

Now put that beside a much older result: **item-writer judgments of difficulty correlate
poorly with actual difficulty** (Language Assessment Quarterly case study,
[doi:10.1080/15434303.2010.536924](https://doi.org/10.1080/15434303.2010.536924)).
`MEASURED-BENCH`

So the honest summary is: **text-based difficulty prediction is now about as good as an
expert's guess, and an expert's guess is not good.** "Competitive with human judgment"
sounds like success and is actually the statement of the ceiling. It is enough to **route**
items — to bin a generated item into a coarse difficulty stratum for adaptive selection —
and nowhere near enough to **score** them. Predicted parameters are a prior, not a
calibration. `INFERENCE`

### 4.5 Equating and comparability when no form is ever repeated

Classical equating needs either common items or randomly equivalent groups. Under
generation-on-demand you have neither by default: every learner sees a unique form, and
learners are self-selected into the moment they took it.

What survives:

1. **Anchor by generator, not by item.** If families are calibrated (§4.1), the family
   *is* the anchor. Two learners who each sampled from families {A, C, F} are on a common
   scale by construction — with the FERF supplying the response function. `INFERENCE`
   grounded in [doi:10.3102/10769986028004295](https://doi.org/10.3102/10769986028004295).
2. **Embedded calibrated anchors.** Administer a small fixed subset of genuinely calibrated,
   never-generated items in every session. This is the boring, robust answer and it costs
   3–5 items. It also directly reintroduces exposure risk for that subset (§5) — which is
   acceptable precisely because the anchor's job is scaling, not scoring.
3. **Random-groups by construction.** Because generation is stochastic and assignment can
   be *seeded*, you can enforce randomly equivalent groups by design — impossible in
   paper-and-pencil, free here. A system that assigns generator seeds at random creates the
   random-groups equating design as a side effect. `INFERENCE`
4. **Post-hoc concurrent calibration.** Accumulate response data across all learners, fit
   the hierarchical model periodically, and rescale historical θ̂. This makes scores
   *revisable*, which is uncomfortable but honest — and is exactly what continuous large-scale
   programmes already do. The comparison base for IRT linking methods under random-groups
   designs is well studied ([ERIC EJ875216](https://eric.ed.gov/?id=EJ875216)).
   `MEASURED-BENCH` for the linking methods; `INFERENCE` for the application.

What does **not** survive: any claim of comparability made *before* response data exist.
A brand-new generator on day zero has no scale. Its outputs are ordinal at best.

---

## 5. Adaptive testing when items are not scarce

### 5.1 What CAT was solving

CAT selects, at each step, the item maximising Fisher information at the current θ̂
(van der Linden & Glas 2000, *Computerized Adaptive Testing: Theory and Practice*,
[doi:10.1007/0-306-47531-6](https://doi.org/10.1007/0-306-47531-6)). Left unconstrained,
maximum-information selection is pathological: a small subset of items gets administered to
nearly everyone while most of the pool is never used
([ERIC ED421526](https://eric.ed.gov/?id=ED421526),
[ERIC ED454279](https://eric.ed.gov/?id=ED454279)).

Hence **exposure control** — an entire literature whose sole purpose is to make a scarce
pool last:
- Sympson–Hetter probabilistic exposure control and its conditional variants
  ([ERIC ED442837](https://eric.ed.gov/?id=ED442837));
- Stocking & Lewis, "Controlling item exposure conditional on ability in CAT," *JEBS* 1998
  ([doi:10.3102/10769986023001057](https://doi.org/10.3102/10769986023001057); ETS RR-95,
  [doi:10.1002/j.2333-8504.1995.tb01660.x](https://doi.org/10.1002/j.2333-8504.1995.tb01660.x));
- a-stratified designs to spread exposure across discrimination strata
  ([ERIC EJ779492](https://eric.ed.gov/?id=EJ779492));
- comparative evaluations across models and item types
  ([ERIC EJ727350](https://eric.ed.gov/?id=EJ727350),
  [ERIC ED475147](https://eric.ed.gov/?id=ED475147));
- and empirical study of **organised item theft** as an attack on continuous testing
  ([ERIC EJ1111472](https://eric.ed.gov/?id=EJ1111472)).
`OBSERVED` / `MEASURED-BENCH`

Every one of these is a workaround for pool scarcity.

### 5.2 What becomes irrelevant, and what replaces it

**Irrelevant:** exposure-rate control as such. If each learner receives freshly generated
instances, no instance is over-exposed because no instance recurs. Item theft as classically
conceived — memorising and circulating a live item — targets an object that no longer
persists. `INFERENCE`

**What replaces it — five successor problems, none solved:**

1. **Generator exposure.** The secret is no longer the item; it is the **item model / cognitive
   model / prompt + constraint set**. Compromise of a template compromises its entire orbit
   at once. Exposure control must be re-specified over *families*: how many instances from
   family F may a single learner (or a coordinating group) see before the family's structure
   is inferable? Glas & van der Linden's two-stage selection already provides the hook —
   family selection is where the control belongs. `INFERENCE`
2. **Effective-item-count control.** Per Cole et al. 2020
   ([ERIC EJ1227607](https://eric.ed.gov/?id=EJ1227607)), generators saturate. Exposure
   control is replaced by **saturation monitoring**: track the syntactic/semantic diversity
   of what a learner has actually received and treat a saturated family as an exhausted one.
   `INFERENCE` from a `MEASURED-BENCH` result.
3. **Content balancing and constraint satisfaction**, which never went away and now dominate.
   Geerlings et al. 2012 ([doi:10.1177/0146621612468313](https://doi.org/10.1177/0146621612468313))
   shows on-the-fly assembly with explicit constraints, and finds that **constraint-set
   severity materially changes the optimal design** — i.e. the binding limit on adaptive
   efficiency is now the content blueprint, not the pool.
4. **Item-quality gating in the loop.** With a fixed bank, every item was pre-vetted. With
   generation, a defective item can reach a learner *during* the adaptive session, and a
   defective item administered at the point of maximum information does maximum damage to
   θ̂. Real-time screening (Gorgun & Bulut 2025,
   [ERIC EJ1460469](https://eric.ed.gov/?id=EJ1460469)) moves from nice-to-have to
   load-bearing. `INFERENCE`
5. **Selection under parameter uncertainty.** Maximum-information selection assumes known
   item parameters. With family-level parameters and within-family variance, the right
   criterion is *expected* information under the family distribution — which systematically
   **downweights high-variance families**. This is a substantive change to the selection
   rule, and it is derivable directly from the Glas–van der Linden formulation.
   `INFERENCE` from `MEASURED-BENCH`.

### 5.3 A real operational reference point

The **Duolingo English Test** is the only large-scale operational system that combines
computer-adaptive delivery with heavy automatic item generation and publishes its
psychometrics. Reported figures: **internal consistency and reliability coefficients both
0.96, SEM stable across the score range, and test–retest reliability 0.84** for the first
operational year ([doi:10.46999/hqep1801](https://doi.org/10.46999/hqep1801)); measurement
model and real-time rating system in
[doi:10.46999/mfkw9830](https://doi.org/10.46999/mfkw9830); subscore analysis in
[doi:10.46999/wbqi4443](https://doi.org/10.46999/wbqi4443). `VENDOR`

**These are vendor-published research reports and must not be restated as independent
findings.** They are nonetheless the right *shape* of evidence — note especially that the
vendor reports **test–retest (0.84)** alongside internal consistency (0.96), and that the
gap between them is large. §7 argues that under generated items the test–retest figure is
the meaningful one and the internal-consistency figure is close to meaningless.

---

## 6. Cognitive diagnostic models and the retrofitting problem

### 6.1 The models

- **DINA** — conjunctive, two parameters per item (slip, guess), attributes required by an
  item specified in a **Q-matrix**. Junker & Sijtsma 2001, *APM*
  ([doi:10.1177/01466210122032064](https://doi.org/10.1177/01466210122032064)). `OBSERVED`
- **G-DINA** — de la Torre 2011, *Psychometrika*
  ([doi:10.1007/s11336-011-9207-7](https://doi.org/10.1007/s11336-011-9207-7)): saturated
  general framework; DINA, DINO, A-CDM etc. are constrained special cases. 632 citations.
- **Attribute hierarchies** — Leighton, Gierl & Hunka 2004, *JEM*
  ([doi:10.1111/j.1745-3984.2004.tb01163.x](https://doi.org/10.1111/j.1745-3984.2004.tb01163.x)):
  the Attribute Hierarchy Method, a variant of Tatsuoka's rule space that imposes
  prerequisite structure on attributes and thereby collapses the attribute-profile space.
  Templin & Bradshaw 2014, *Psychometrika*
  ([doi:10.1007/s11336-013-9362-0](https://doi.org/10.1007/s11336-013-9362-0)) gave the
  hierarchical DCM with formal tests for the presence of a hierarchy.
- **Negative/critical.** von Davier & Haberman 2014, *Psychometrika*
  ([doi:10.1007/s11336-013-9363-z](https://doi.org/10.1007/s11336-013-9363-z)): a direct
  commentary arguing that hierarchical DCMs, as analysed, effectively **morph into
  unidimensional models** — that the claimed multi-attribute diagnosis is not doing the work
  it appears to do. `MEASURED-BENCH` / `OBSERVED`
  → Anyone shipping "skill mastery profiles" should read this before claiming their profile
  is more than a rescaled total score.

### 6.2 The retrofitting problem, named

Gierl & Cui 2008, "Defining Characteristics of Diagnostic Classification Models and the
Problem of Retrofitting in Cognitive Diagnostic Assessment," *Measurement*
([doi:10.1080/15366360802497762](https://doi.org/10.1080/15366360802497762)). `OBSERVED`

The problem: DCMs were designed for tests *built* to measure specified attributes. In
practice they are almost always applied to tests built for something else — PISA reading,
a state maths assessment, a licensure exam — with a Q-matrix **inferred after the fact** by
expert judgment or statistical search. The diagnosis is then an artifact of the retrofit.

Sessoms & Henson 2018, "Applications of Diagnostic Classification Models: A Literature
Review and Critical Commentary," *Measurement*
([doi:10.1080/15366367.2018.1435104](https://doi.org/10.1080/15366367.2018.1435104), 83
citations) is the field's own audit and finds retrofitting to be the dominant applied
practice. `MEASURED-META`

The literature is thick with retrofits, openly labelled: G-DINA on PISA reading
([ERIC EJ1112138](https://eric.ed.gov/?id=EJ1112138)), G-DINA on a high-stakes L2 reading
test ([ERIC EJ1226655](https://eric.ed.gov/?id=EJ1226655)), DINA on a statewide mathematics
assessment ([ERIC EJ1265426](https://eric.ed.gov/?id=EJ1265426)).

And the damage is quantified. Rupp & Templin 2008, *EPM*
([ERIC EJ782123](https://eric.ed.gov/?id=EJ782123)) show that **Q-matrix misspecification
degrades parameter estimates and inflates misclassification rates** in DINA. De la Torre
2008, *JEM* ([ERIC EJ819613](https://eric.ed.gov/?id=EJ819613)) had to invent empirical
Q-matrix *validation* precisely because "most model fit analyses in cognitive diagnosis
assume that a Q matrix is correct after it has been constructed, without verifying its
appropriateness." Country-specific Q-matrix refinement changes results on international
large-scale data ([ERIC EJ1356133](https://eric.ed.gov/?id=EJ1356133)). `MEASURED-BENCH`

### 6.3 Does generation-on-demand fix retrofitting? Yes — and it moves the problem

**The direct evidence is new and it is affirmative.** Effatpanah, Kunina-Habenicht, Bernard,
Hornung & Sonnleitner 2026, "Optimizing Large-Scale Mathematical Assessments," *EMIP*
([ERIC EJ1506971](https://eric.ed.gov/?id=EJ1506971)). `MEASURED-BENCH`

Design: **5,336 third-grade students**, Luxembourgish image-based standardised mathematics
exam. Instead of inferring a Q-matrix, **items were constructed from cognitive models
derived from the curriculum — which yields the Q-matrix directly** — and attribute
hierarchies were specified rather than discovered. Multiple DCMs and hierarchical extensions
were compared.

Result: the **hierarchical A-CDM outperformed the alternatives**, classifying students into
**60 latent classes** with acceptable attribute- and test-level classification accuracy and
**more interpretable results than G-DINA**. Authors' conclusion: cognitive-model-based item
generation plus specified attribute hierarchies "enhance the accuracy and interpretability
of DCM-based diagnostics."

This is exactly the AIG cognitive model doing double duty. **In template AIG you must write
a cognitive model to generate an item at all — and a cognitive model is a Q-matrix row.**
Generation-on-demand therefore dissolves retrofitting *by construction*: the attribute
specification is upstream of the item, not reverse-engineered from it.

**But the problem moves, and the new location is worse in one respect.** Three transfers:

1. **From Q-matrix inference to cognitive-model validity.** You no longer have to guess
   which attributes an item measures — but you now have to be *right* about the attribute
   ontology itself, before any data exist. A wrong Q-matrix used to be a fitting problem
   with diagnostics (de la Torre 2008); a wrong cognitive model is a **generation** problem
   that manufactures items measuring a construct nobody has. Its errors are invisible in the
   fit statistics because the data were generated to match it. `INFERENCE`
2. **From expert judgment about items to expert judgment about hierarchies.** Effatpanah
   et al. specified hierarchies from curriculum. Kwon, Huggins-Manley, Templin & Zheng 2024,
   *JEM* ([doi:10.1111/jedm.12387](https://doi.org/10.1111/jedm.12387)) show for sequential
   HDCMs that hierarchy **misspecification lowers classification accuracy — specifically
   when the misspecified model has fewer attribute profiles than the true model**, i.e.
   over-constraining is the dangerous direction. `MEASURED-BENCH`
   → Design rule: **when uncertain, under-specify the hierarchy.** A missing prerequisite
   edge costs less than a false one.
3. **From retrofitting to unfalsifiability.** If the generator writes items *from* the
   Q-matrix and the model is *fit with* that Q-matrix, model fit no longer tests the
   attribute theory. You have closed the loop. The only escape is external validation:
   attribute-level predictions must be checked against **something not generated by the same
   model** — transfer tasks, delayed retention, human-rated performance, downstream course
   outcomes. `INFERENCE`

A further gift that is underexploited: **DCMs need response data at the attribute level, and
generation-on-demand can produce items targeting exactly the attribute combination whose
mastery is currently uncertain.** That is adaptive testing at the level of the Q-matrix
rather than θ — a design that was impossible with fixed banks because you never had an item
for the cell you needed. Kwon et al.'s sequential HDCM for multiple-attempt classroom data
is the closest published model. **This is the single most promising unbuilt thing in this
section.** `INFERENCE`

---

## 7. Reliability without a fixed item set — the field's central open measurement problem

### 7.1 Why α and ω are not merely inconvenient but undefined

Cronbach's α is a function of the covariance matrix of **a fixed set of items administered
to a common sample**. Concretely, α = (k/(k−1))(1 − Σσ²ᵢ/σ²ₜ) requires: a fixed k; item
variances σ²ᵢ estimable across people; a total-score variance from the same k items.
McDonald's ω (Revelle & Zinbarg 2009, *Psychometrika*,
[doi:10.1007/s11336-008-9102-z](https://doi.org/10.1007/s11336-008-9102-z)) is preferable to
α on unidimensionality grounds but has the *same* structural requirement: it is estimated
from a factor model over a fixed item set.

**If every learner sees a different item set, there is no item covariance matrix.** Not a
noisy one. Not a hard-to-estimate one. There is no such object. α and ω are not biased under
generated assessment; they are **undefined**. `INFERENCE` — and this is a definitional
consequence, not a debatable empirical claim.

Anyone reporting α for a generated-item system has silently done one of three things:
(a) computed it over the small subset of learners who happened to receive the same items —
a non-random and usually tiny sample; (b) computed it over *positions* rather than items,
treating "item 3" as the same variable across learners when it is not; or (c) computed it
over a pilot fixed form and then shipped a generative system. All three are reporting a
number about a different instrument than the one deployed.

Cronbach himself supplies the exit route. Cronbach & Shavelson 2004, "My Current Thoughts on
Coefficient Alpha and Successor Procedures," *EPM*
([doi:10.1177/0013164404266386](https://doi.org/10.1177/0013164404266386)): α "covers only a
small perspective of the range of measurement uses for which reliability information is
needed and… should be viewed within a much larger system of reliability analysis,
**generalizability theory**." `OBSERVED`

### 7.2 Generalizability theory is the right frame, and it was built for this

G-theory (Brennan 2001, *Generalizability Theory*,
[doi:10.1007/978-1-4757-3456-0](https://doi.org/10.1007/978-1-4757-3456-0), ~985 citations)
decomposes observed-score variance into components attributable to **facets** — persons,
items, occasions, raters, forms — and asks how well a score **generalises to the universe of
admissible observations**. `OBSERVED`

That framing is *native* to generated assessment. The universe of admissible observations
**is the generator's output distribution.** A generator is a formal specification of a
universe of admissible observations — arguably the first time in the history of measurement
that this universe has been written down explicitly and executably, rather than gestured at.
`INFERENCE`

And the analogous problem has already been solved once, in CBM. Christ & Ardoin 2009,
*Journal of School Psychology* ([ERIC EJ821847](https://eric.ed.gov/?id=EJ821847)) used
**generalizability and dependability studies** to choose among procedures for building
equivalent CBM-R passage sets — 88 students × 50 passages. G-theory is how the CBM literature
established that a *set of interchangeable probes* could support decisions (§9). It is the
existence proof that this can be done. `MEASURED-BENCH`

### 7.3 A concrete proposal: seeded-replicate reliability

The literature does not offer a settled protocol. Here is one, assembled from the pieces
above. Everything below is `INFERENCE`, built on `MEASURED-BENCH` foundations, and is offered
as a specification to be tested, not a finding.

**Definitions.**
- A **probe policy** π is the tuple (cognitive model, item model / prompt + constraints,
  selection rule, stopping rule, scoring rule). It is the thing that produces a score.
- A **seed** s is the random state that determines which instances π actually emits.
- An **independently seeded replicate** is π run again with s′ ⟂ s.

**The protocol.**

1. **Seed determinism.** π must be reproducible: (π, s) → the exact administered set. Without
   this, none of the following is estimable, and the system is unauditable. *This is a
   software requirement with psychometric consequences and it must be designed in from day
   one.*
2. **Replicate–probe test–retest (the headline coefficient).** Within a window short enough
   that true θ change is negligible relative to the decision's precision needs, administer
   π with s and π with s′ to the same learner. The correlation across learners,
   `r(θ̂_s, θ̂_s′)`, is the **seeded-replicate reliability** ρ_π. This is the direct analogue
   of alternate-forms reliability where the "forms" are draws from the generator, and it is
   the number that answers the user's actual question: *if I took this again, would I get the
   same answer?*
   - Duolingo's published test–retest of **0.84** against internal consistency of **0.96**
     ([doi:10.46999/hqep1801](https://doi.org/10.46999/hqep1801), `VENDOR`) illustrates why
     the distinction matters: the two numbers differ by 0.12 and only one of them is
     estimable under generation.
3. **G-study with generator as a facet.** Design: persons × (instances **nested within**
   generator) × occasions. Estimate σ²_p, σ²_i:g, σ²_g, σ²_o, and the interactions. The
   generalizability coefficient over the universe defined by π is the reliability of a score
   from π. **σ²_i:g is the within-family variance of §4.3** — the same quantity, arrived at
   from the reliability side. Estimating it once serves both purposes.
4. **Decision (D) study to set probe count.** Given σ²_i:g, compute the number of probes n
   required for a target dependability index Φ at the decision threshold. This replaces
   "how many items should the quiz have?" with a derived answer, and it will differ per
   generator — high-variance generators need more probes to reach the same precision. That
   is the correct incentive: **a sloppy generator costs the learner time.**
5. **Report the pair, never one number.** A generated assessment reports
   **(ρ_π, n_required(Φ))** — reliability of the policy, and probes needed at the decision
   point. Not α.
6. **Continuous monitoring.** Because generators drift (model updates, prompt edits,
   retrieval-corpus changes), ρ_π has a **version**. Any change to π invalidates prior
   estimates. Treat ρ_π like a model card metric: versioned, dated, re-estimated on change.
7. **Where test–retest is contaminated** — memorable items, short intervals, practice
   effects — use the **split-policy** variant: partition the generator's output space a
   priori into two disjoint sub-policies π₁, π₂ (e.g. by constraint partition, per Cole
   et al.'s syntactic clustering), administer both in one session, and correlate. This is
   split-half reliability rebuilt at the policy level and it costs one session instead of
   two.

**What this buys.** A defensible reliability claim that does not require a fixed form, is
estimable from data the system already collects, degrades gracefully (you can compute ρ_π
from a subsample), and is falsifiable.

**What it does not buy.** It says nothing about validity. A generator can be perfectly
reliable and measure the wrong thing with great precision — indeed high ρ_π with low
σ²_i:g is exactly what a **narrow, saturated** generator produces (§1.4). **Reliability and
saturation are confounded here in a way they never were with human-written banks**, and any
honest report must present ρ_π next to an effective-item-count estimate. This confound is,
as far as this search found, unnamed in the literature. `INFERENCE`

---

## 8. Automated scoring: short answer, essay, code

### 8.1 The human baseline is worse than the discourse assumes

Before any machine-vs-human comparison, fix the baseline.

**Messer, Brown, Kölling & Shi 2025**, "How Consistent Are Humans When Grading Programming
Assignments?", *ACM TOCE* ([ERIC EJ1488833](https://eric.ed.gov/?id=EJ1488833)).
`MEASURED-BENCH` ← **third primary negative result**

Design: **28 participants**, each grading **40 CS1 Java assignments** on correctness, code
elegance, readability and documentation, in seven groups of four so that within-group
agreement is measurable; one assignment secretly duplicated across batches to measure
*intra*-rater consistency.

| Measure | Result |
|---|---|
| Krippendorff's α, **correctness** | **≈ 0.20** |
| Krippendorff's α, elegance / readability / documentation | **< 0.10** |
| Recommended threshold for tentative conclusions | α > 0.667 |
| Graders who reproduced their own grade on the duplicate (of 22 who didn't notice) | **1** |
| Mean self-inconsistency, correctness | **1.79 grade points** |

Authors' conclusion: "human graders in our study cannot agree on the grade to give a piece
of student work and are often individually inconsistent, suggesting that **the idea of a
'gold standard' of human grading might be flawed**." A shared rubric alone was not enough.

This reframes the entire automated-scoring literature. **"Agrees with human raters" is a
weak criterion when human raters agree with each other at α = 0.2.** A machine scorer that
correlates 0.75 with a single human rater may be *more* reliable than that human, and the
comparison as usually reported cannot distinguish "the machine is good" from "the human is
noisy."

Context: Messer et al.'s systematic review of automated grading and feedback tools for
programming (121 papers, 2017–2021, *ACM TOCE*,
[ERIC EJ1419855](https://eric.ed.gov/?id=EJ1419855)) finds most tools assess **correctness
in object-oriented languages** — i.e. the dimension where humans were *least* bad — and
largely ignore the dimensions where human agreement collapses. `MEASURED-META`

### 8.2 Essay scoring: agreement, and the construct problem

e-rater is the reference system (Attali & Burstein, e-rater v2, ETS RR-04-45,
[ERIC EJ1110978](https://eric.ed.gov/?id=EJ1110978)). Operational evaluations across TOEFL
independent/integrated prompts ([ERIC EJ1109838](https://eric.ed.gov/?id=EJ1109838)),
Praxis I ([ERIC EJ1109680](https://eric.ed.gov/?id=EJ1109680)) and a large-scale English
language testing programme ([ERIC EJ1109947](https://eric.ed.gov/?id=EJ1109947)) report
quadratic weighted kappas, Pearson correlations and standardised mean differences against
human scores. A meta-analysis of human–machine inter-rater agreement in essay scoring is at
[ERIC EJ1407232](https://eric.ed.gov/?id=EJ1407232). `MEASURED-BENCH` / `MEASURED-META`

**The construct critique, and it is a genuine null.** Perelman 2014, "When 'the state of the
art' is counting words," *Assessing Writing*
([doi:10.1016/j.asw.2014.05.001](https://doi.org/10.1016/j.asw.2014.05.001), 74 citations),
re-analysing the Hewlett/ASAP results (Shermis & Hamner, in *Handbook of Automated Essay
Evaluation*, [doi:10.4324/9780203122761-27](https://doi.org/10.4324/9780203122761-27)),
argues that reported machine performance is largely explained by **essay length and other
surface proxies**, and that agreement statistics therefore certify a construct nobody
intended to measure. `OBSERVED`
→ The general lesson generalises past e-rater: **agreement with human scores is not evidence
of construct validity when the machine and the human can both be tracking the same
irrelevant surface feature.** Under LLM scoring this risk is different in kind but not
obviously smaller.

**LLM raters, measured.** Jiao, Song & Lee 2026, "Evaluating Rater Effects of Large Language
Models in Automated Essay Scoring," *EMIP*
([doi:10.1111/emip.70018](https://doi.org/10.1111/emip.70018)): ten LLMs (GPT-3.5/4/4o, o1,
Claude 3.5 Sonnet, Gemini 1.5/1.5 Pro/2.0, DeepSeek V3/R1) vs human expert raters on two
writing tasks, evaluated for accuracy, **intra-rater consistency**, and **rater effects via
Many-Facet Rasch measurement** — severity, centrality, halo. Results supported GPT-4o,
Gemini 1.5 Pro and Claude 3.5 Sonnet; the authors explicitly decline to rank models given
the small sample. `MEASURED-BENCH`
→ The methodological contribution matters more than the ranking: **MFRM is the right tool
for LLM raters**, because an LLM is a rater with severity and centrality tendencies, and
those are estimable and correctable exactly as they are for humans. Very few deployments do
this.

Also relevant: LLM-based scoring of L2 writing with prompting-strategy ablations and
intra-rater reliability ([ERIC EJ1490580](https://eric.ed.gov/?id=EJ1490580)); GPT-4o
strengths and weaknesses as an EFL scoring tool ([ERIC EJ1495977](https://eric.ed.gov/?id=EJ1495977));
LLM accuracy across cognitive domains ([ERIC EJ1452603](https://eric.ed.gov/?id=EJ1452603));
and a scoping review of hierarchical rater models applied to AES
([ERIC EJ1470142](https://eric.ed.gov/?id=EJ1470142)).

### 8.3 The documented bias against non-standard dialects and L2 writers

This is the part that must not be softened.

**Bridgeman, Trapani & Attali 2012**, "Comparison of Human and Machine Scoring of Essays:
Differences by Gender, Ethnicity, and Country," *Applied Measurement in Education*
([doi:10.1080/08957347.2012.635502](https://doi.org/10.1080/08957347.2012.635502), 106
citations). The foundational study establishing that **human–machine score discrepancies are
not uniform across demographic groups** — they vary systematically by gender, by
ethnicity, and by country of origin of the test taker. `MEASURED-BENCH`

**Ramineni & Williamson 2018**, "Understanding Mean Score Differences Between the e-rater
Automated Scoring Engine and Humans for Demographically Based Groups in the GRE General
Test," ETS Research Report ([doi:10.1002/ets2.12192](https://doi.org/10.1002/ets2.12192)).
`MEASURED-BENCH` — and the honesty of this report is worth noting since it is vendor-authored:
- **"Notable mean score differences… for essays from certain demographic groups were
  observed"** on the pre-2012 GRE.
- The operational mitigation was **using e-rater only as a *check score* with discrepancy
  thresholds**, which "prevented an adverse impact on the examinee score at the item or test
  level." *The bias was real; the harm was contained by architecture, not by fixing the
  model.*
- Root-cause analysis: human raters "appeared to be using **conditional logic and a
  rule-based approach**," while e-rater uses **linear weighting of all features** — the
  human rating process "did not fully correspond to the e-rater scoring mechanism."
  The disagreement is structural, not a tuning defect.

**Loukina, Madnani & Zechner 2019**, "The many dimensions of algorithmic fairness in
educational applications," BEA @ ACL
([doi:10.18653/v1/W19-4401](https://doi.org/10.18653/v1/W19-4401),
[aclanthology.org/W19-4401](https://aclanthology.org/W19-4401/)). Investigates multiple
formal fairness definitions and shows, on simulated and real data, that **test-takers'
native language background influences automated English proficiency scores**. Central
conclusion: **"total fairness may not be achievable and… different definitions of fairness
may require different solutions."** `MEASURED-BENCH`
→ This is not a counsel of despair; it is a design requirement. A system must **declare
which fairness criterion it optimises**, because it cannot satisfy them all, and an
undeclared choice is a choice made by the loss function.

Earlier and structural: ETS's own work on **population invariance in automated scoring**
found that the *sampling approach used to build the scoring model* affects invariance
([ERIC EJ1110012](https://eric.ed.gov/?id=EJ1110012)) — i.e. subgroup bias is partly
inherited from training-set composition, which is a decision, not a fact. `MEASURED-BENCH`
Open-source tooling explicitly built to support fairness analysis in automated scoring:
[doi:10.18653/v1/W17-1605](https://doi.org/10.18653/v1/W17-1605).

Recent methodological work on detecting **predictive bias** in AES specifically: Chen, Wu &
Zhang 2026, *Assessing Writing*
([doi:10.1016/j.asw.2026.101066](https://doi.org/10.1016/j.asw.2026.101066)). `OBSERVED`

**What this means for a generative learning system.** Automated scoring bias is *directional
and demographic*, it is not eliminated by better models (Ramineni & Williamson's root cause
is a structural mismatch between rule-based human judgment and linear feature weighting), and
the only intervention with published evidence of containing harm is **architectural**: use
the machine as a check score with discrepancy thresholds and route disagreements to a human.
That is a design constraint, and §10 encodes it.

### 8.4 Short answer and code

- **ASAG systematic reviews.** An assessment-perspective systematic review of automated
  short-answer grading — explicitly framed around validity rather than F1 —
  [doi:10.31234/osf.io/geayp_v1](https://doi.org/10.31234/osf.io/geayp_v1) (`OBSERVED`,
  preprint). Domain-specific LLM–human agreement in sustainability education:
  [doi:10.1002/jcal.70160](https://doi.org/10.1002/jcal.70160). `MEASURED-BENCH`
- **Code.** Automated grading of programming has a 20-year history of structural and
  output-based marking (e.g. [ERIC EJ790945](https://eric.ed.gov/?id=EJ790945),
  [ERIC EJ866194](https://eric.ed.gov/?id=EJ866194)) and near-human accuracy on richly
  structured problems via generative grading
  ([ERIC ED615516](https://eric.ed.gov/?id=ED615516)). `MEASURED-BENCH`
  **The important asymmetry:** code correctness is *verifiable* — a test suite is not a
  rater, it is a proof — while code elegance, readability and design are rater judgments
  where humans hit α < 0.1 (§8.1). These must never be reported on the same scale or with
  the same confidence. This connects directly to F1's verification-first argument: **for the
  verifiable component, there is no rater bias because there is no rater.**

---

## 9. Curriculum-Based Measurement: the progress-monitoring backbone

CBM matters here for a specific reason: it is the **only** mature measurement tradition that
was designed from the start around *brief, frequent, interchangeable probes drawn from a
pool*, with **formal decision rules** attached. It is the closest existing analogue to
generated assessment, it has 40 years of psychometrics, and — critically — it documents in
detail **how the equivalence of probes was achieved and how often it failed**. This is the
H1 progress-monitoring backbone.

### 9.1 What CBM is

Deno 1985, "Curriculum-Based Measurement: The Emerging Alternative," *Exceptional Children*
([ERIC EJ326811](https://eric.ed.gov/?id=EJ326811)). `OBSERVED` Short (typically 1-minute),
standardised, repeatable probes; scores plotted over time against a goal line; instructional
decisions driven by the trend.

Fuchs & Deno 1991 ([ERIC EJ428597](https://eric.ed.gov/?id=EJ428597)) draw the load-bearing
distinction: **general outcome measurement (GOM)** — every probe samples the same global
construct, so scores are comparable across the year — versus **specific subskill mastery
measurement (SSMM)** — each probe targets the current instructional objective, so scores are
*not* comparable across time. `OBSERVED`

**This distinction is the one most often violated by AI tutoring systems.** A system that
generates items about *whatever the learner is currently studying* is doing SSMM and cannot
plot a growth trend, because the measure changes as the curriculum changes. A system that
wants a growth trend must hold the construct fixed while the content advances — which is
what GOM means and what makes CBM hard.

### 9.2 How CBM probes are constructed, and what makes them equivalent

The honest history: **CBM probes were originally sampled from curriculum materials, and this
did not work.** The equivalence had to be engineered, and the engineering is documented.

- **Readability formulas are insufficient.** Christ & Ardoin 2009, *JSP*
  ([ERIC EJ821846](https://eric.ed.gov/?id=EJ821846)) investigated the psychometric basis
  for claims of CBM-R passage equivalence and found **readability statistics inadequate to
  justify equivalence**. `MEASURED-BENCH`
- **Field testing works.** Christ & Ardoin 2009, *JSP*
  ([ERIC EJ821847](https://eric.ed.gov/?id=EJ821847)): 88 second- and third-graders each
  read **50 CBM-R passages**; four selection procedures compared — random sampling, Spache
  readability, **mean performance level**, and **Euclidean distance** on observed
  performance — evaluated by generalizability and dependability studies. **The two
  field-testing-based procedures won.** `MEASURED-BENCH`
  → *You cannot certify probe equivalence from properties of the probe. You must observe
  responses.* This is the CBM version of §4.4's ceiling on text-based difficulty prediction,
  found independently and 14 years earlier.
- **The magnitude of failure when you don't.** Francis, Santi, Barr, Fletcher, Varisco &
  Foorman 2008, *JSP* ([ERIC EJ789795](https://eric.ed.gov/?id=EJ789795)): 134 second-graders
  randomly assigned to read six 1-minute DIBELS passages **"developed to be comparable based
  on readability formulas"** in one of six fixed orders across seven weeks.
  **Mean ORF varied from 67.9 to 93.9 WCPM across the six passages** — a spread of **26
  words per minute**, on passages certified equivalent by the standard method. Presentation
  order had no effect. The passage effects **altered the shape of growth trajectories and
  biased estimates of linear growth rate**, and were **removed by explicit equating**.
  `MEASURED-BENCH` ← **fourth primary negative result**
  Authors' conclusion: "**Explicit equating is essential** to the development of equivalent
  forms, which can vary in difficulty despite high correlations across forms and apparent
  equivalence through readability indices."
  → Context for the 26-WCPM spread: typical expected *weekly* growth in second-grade ORF is
  on the order of 1–2 WCPM. **The form effect is roughly an entire semester of growth.**
- **Form effects persist in modern commercial sets.** DIBELS Next ORF progress-monitoring
  passages, ~572 students per grade, Grades 1–6, total N ≥ 3,092
  ([ERIC EJ995832](https://eric.ed.gov/?id=EJ995832)); non-equivalence severe enough to
  motivate formal equating studies ([ERIC EJ995835](https://eric.ed.gov/?id=EJ995835));
  high variability specifically for below-benchmark students on well-designed passage sets
  ([ERIC EJ1155019](https://eric.ed.gov/?id=EJ1155019)); partial replication of passage
  effects in Grade 2 ([ERIC EJ1196832](https://eric.ed.gov/?id=EJ1196832)); controlling
  difficulty level changes measured sensitivity to growth
  ([ERIC EJ683511](https://eric.ed.gov/?id=EJ683511)). `MEASURED-BENCH`
- **Probe-set choice changes the standard error.** Ardoin & Christ 2009, *SPR*
  ([ERIC EJ842725](https://eric.ed.gov/?id=EJ842725)): 68 students, twice-weekly
  administration of three passage sets — the experimental **FAIP-R**, AIMSweb, and DIBELS.
  **Significant differences in intercept, weekly growth, and standard error**, with SE
  smallest for the controlled experimental set. `MEASURED-BENCH`
- **The construction recipe that emerges** (synthesis, `INFERENCE` over the above): (1) write
  many more probes than needed; (2) constrain surface features (length, readability,
  vocabulary, syntax) as a *filter*, not a certificate; (3) **field-test every probe on a
  representative sample**; (4) select the subset minimising performance dispersion — mean
  level and Euclidean distance from the set centroid; (5) **equate the survivors explicitly**;
  (6) verify with G/D studies; (7) re-verify for the subpopulation you will actually monitor,
  because variability is worse for at-risk students.

  Step 3 is the one generative systems skip, and it is the one CBM proved you cannot skip.
  The equivalent for CBM in mathematics problem-solving is spelled out in
  [ERIC EJ866533](https://eric.ed.gov/?id=EJ866533).

### 9.3 Decision rules, and the field's own negative verdict

**Ardoin, Christ, Morena, Cormier & Klingbeil 2013**, "A Systematic Review and Summarization
of the Recommendations and Research Surrounding CBM-R Decision Rules," *Journal of School
Psychology* ([ERIC EJ1001681](https://eric.ed.gov/?id=EJ1001681)). 171 journal articles,
chapters and manuals identified; **102 meeting criteria** evaluated. `MEASURED-META`
← **fifth primary negative result**

Verdict, verbatim: **"most decision-making practices are based on expert opinion and… there
is very limited psychometric or empirical support for such practices. There is a lack of
published evidence to support program evaluation and progress monitoring with CBM-R."**

Forty years of the most-studied progress-monitoring system in education, and its own
systematic review says the decision rules are expert opinion. **Any AI system proposing
"data-driven instructional decisions" from frequent probes is proposing to do, at speed and
scale, something the field that invented it has not validated.**

**How much data a decision actually needs:**
- **Christ, Zopluoglu, Long & Monaghen 2012**, *Exceptional Children*
  ([ERIC EJ970685](https://eric.ed.gov/?id=EJ970685)): linear mixed-effects simulation across
  durations 6–20 weeks and residual SD σ_ε ∈ {5, 10, 15, 20}. Outcomes are sufficient to
  guide educational decisions **only if** (a) trend is estimated by **ordinary least
  squares**, (b) the dataset is **very good** (low residual), and (c) it comprises a
  **minimum of 14 CBM-R data points**. `MEASURED-BENCH`
- **Thornblad & Christ 2014**, *SPR* ([ERIC EJ1142188](https://eric.ed.gov/?id=EJ1142188)):
  external validation with 40 second-graders on a **6-week daily** schedule. Quality improved
  with duration and data points, but **"the quality of estimates was only marginal after 6
  weeks."** `MEASURED-BENCH`
- Multi-study evaluation of schedule, duration and dataset quality
  ([ERIC EJ1001684](https://eric.ed.gov/?id=EJ1001684)); baseline-estimation effects on trend
  quality across 6–20 weeks ([ERIC EJ1055845](https://eric.ed.gov/?id=EJ1055845));
  SE-of-slope confidence intervals ([ERIC EJ788238](https://eric.ed.gov/?id=EJ788238));
  the argument that medium/high-stakes decisions require error computed within a **fixed
  linear regression model rather than a CTT model**
  ([ERIC EJ980203](https://eric.ed.gov/?id=EJ980203)); confidence-interval-overlap methods
  for detecting reliable growth ([ERIC EJ1113651](https://eric.ed.gov/?id=EJ1113651));
  robust regression to blunt the influence of extreme values on OLS slopes
  ([ERIC EJ1058459](https://eric.ed.gov/?id=EJ1058459)); accuracy comparison of data-point,
  median and trend-line rules ([ERIC EJ1417097](https://eric.ed.gov/?id=EJ1417097));
  a general-outcome vs subskill-mastery slope comparison finding GOM decisions "must be made
  15 weeks after implementation" ([ERIC EJ1375326](https://eric.ed.gov/?id=EJ1375326)); and
  G-theory applied directly to RTI progress-monitoring decisions
  ([ERIC EJ1069868](https://eric.ed.gov/?id=EJ1069868)). `MEASURED-BENCH`

**The number to carry forward: ~14 data points, ~8–15 weeks, and only with a well-controlled
probe set.** Any system that claims to detect a change in learning trajectory from three
quizzes in a week is making a claim the CBM literature has specifically measured and
rejected. `INFERENCE` over `MEASURED-BENCH`.

### 9.4 What CBM tells generated assessment

Four transferable results, each earned the hard way:

1. **Surface-feature control does not produce equivalence.** Readability formulas failed
   (Christ & Ardoin 2009; Francis et al. 2008 with a 26-WCPM spread). The generative analogue
   — "the prompt constrains difficulty" — will fail the same way. `INFERENCE`
2. **Field-test and equate, or don't claim a trend.** Explicit equating removed the passage
   effects. Generated probes need the same treatment: response data, then equating, then
   trend claims.
3. **G-theory is the right reliability frame for interchangeable probes**, and CBM already
   demonstrated it works (Christ & Ardoin 2009; [ERIC EJ1069868](https://eric.ed.gov/?id=EJ1069868)).
   This is the empirical warrant for §7.3.
4. **Decision rules need a documented error model and a minimum data requirement,** and the
   honest ones are slower than anyone wants. Generation makes probes cheap; it does not make
   *trends* fast, because the binding constraint is measurement error per probe and true
   growth rate, neither of which generation improves.

---

## 10. The standard: Generated Assessment That Remains Valid (GAV-1)

Everything above compresses into a checkable standard. `INFERENCE` throughout, grounded in
the cited measurements. Written to be auditable rather than aspirational.

### 10.1 The unit of accountability

> **GAV-0.** The accountable object is the **probe policy** π = (cognitive model, item model
> / prompt + constraint set, selection rule, stopping rule, scoring rule, model version).
> Not the item. Every claim below attaches to π, is versioned with π, and **expires when π
> changes**.

Rationale: §4.1–4.2. Instances are draws; the generator is the estimand.

### 10.2 What must be calibrated

| # | Requirement | Evidence basis |
|---|---|---|
| **C1** | π's response function is estimated as a **family expected response function** or equivalent hierarchical-IRT family parameterisation — not as a point item parameter. | [doi:10.1177/0146621603027004001](https://doi.org/10.1177/0146621603027004001); [doi:10.3102/10769986028004295](https://doi.org/10.3102/10769986028004295) |
| **C2** | **Within-family parameter variance σ²_i:g is estimated and published.** A π with unestimated σ²_i:g is uncalibrated regardless of how many items it has produced. | [doi:10.1007/s11336-011-9204-x](https://doi.org/10.1007/s11336-011-9204-x); [doi:10.1177/0146621612468313](https://doi.org/10.1177/0146621612468313); [doi:10.1007/s11336-013-9360-2](https://doi.org/10.1007/s11336-013-9360-2) |
| **C3** | **Item-sampling variance is propagated into every reported SE(θ̂).** Reporting `1/√I(θ̂)` as though instances were calibrated fixed items is prohibited. | §4.3 |
| **C4** | **Isomorphy is tested, never assumed.** Each template/prompt family carries a DCIF or equivalent isomorphicity diagnostic. Prior: ~39% of expert-built templates pass without revision. | [ERIC EJ1357630](https://eric.ed.gov/?id=EJ1357630); [doi:10.1080/15305050802262019](https://doi.org/10.1080/15305050802262019) |
| **C5** | **Text-predicted difficulty is a prior, not a calibration.** Predicted parameters may route items into difficulty strata; they may not enter a reported score's error model. | [aclanthology.org/2024.bea-1.39](https://aclanthology.org/2024.bea-1.39/); [doi:10.3390/math11194104](https://doi.org/10.3390/math11194104) |
| **C6** | **Scale anchoring is explicit**: calibrated anchor items embedded in every session, or family-level anchoring with published FERFs, or both. Random seed assignment is used to create randomly equivalent groups by design. | §4.5 |
| **C7** | **Effective item count (saturation) is measured per π** and reported alongside reliability, because a narrow generator produces spuriously high reliability. | [ERIC EJ1227607](https://eric.ed.gov/?id=EJ1227607); §7.3 |
| **C8** | **Automated raters are calibrated as raters** — severity, centrality and halo estimated via many-facet Rasch or equivalent, and corrected. | [doi:10.1111/emip.70018](https://doi.org/10.1111/emip.70018) |
| **C9** | **Subgroup invariance is measured**, not assumed: score differences between automated and human scoring are reported *by subgroup*, including L2 status and dialect where knowable and consented. The fairness criterion being optimised is **declared**, because they cannot all be satisfied. | [doi:10.1080/08957347.2012.635502](https://doi.org/10.1080/08957347.2012.635502); [doi:10.1002/ets2.12192](https://doi.org/10.1002/ets2.12192); [doi:10.18653/v1/W19-4401](https://doi.org/10.18653/v1/W19-4401) |
| **C10** | **Reliability is reported as (ρ_π, n_required(Φ))** from seeded-replicate test–retest plus a G/D study with generator as facet. **Reporting Cronbach's α for a generated-item assessment is prohibited** — it is undefined. | §7; [doi:10.1177/0013164404266386](https://doi.org/10.1177/0013164404266386); [doi:10.1007/978-1-4757-3456-0](https://doi.org/10.1007/978-1-4757-3456-0) |

### 10.3 What must be human-reviewed

Machine screening is permitted as **triage that raises reviewer yield**
([ERIC EJ1460469](https://eric.ed.gov/?id=EJ1460469)), never as substitution. The following
require a qualified human, and the error-rate spread of <1%–45%
([doi:10.1093/postmj/qgag057](https://doi.org/10.1093/postmj/qgag057)) is why.

| # | Object | Reviewer | Why |
|---|---|---|---|
| **H1** | **Keyed-answer correctness** for any item entering a summative or gating decision. | SME | Error rates reach 45%. Non-negotiable. |
| **H2** | **Distractor diagnosticity** — does each distractor correspond to a *named, attested* error, or is it merely wrong? | SME with access to error taxonomy | The reproducible failure mode: [doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193); [doi:10.1111/medu.12202](https://doi.org/10.1111/medu.12202); [ERIC EJ1490902](https://eric.ed.gov/?id=EJ1490902); [ERIC EJ1501926](https://eric.ed.gov/?id=EJ1501926) |
| **H3** | **The cognitive model / Q-matrix**, before generation. Under generation-on-demand this is where all construct validity now lives. | SME + measurement specialist | §6.3 |
| **H4** | **Attribute hierarchy specification**, with a bias toward under-specification. | SME | [doi:10.1111/jedm.12387](https://doi.org/10.1111/jedm.12387) |
| **H5** | **Fairness / sensitivity review** of stems and options. | Trained reviewer, not the item author | Standard practice; unchanged by generation |
| **H6** | **Construct-irrelevant cueing**: option-order effects, "none of the above", implausible-length keys. Mitigate by per-administration option randomisation (free under generation) and by forbidding NOTA unless the cognitive model requires it. | SME or automated rule + spot check | [ERIC EJ1122481](https://eric.ed.gov/?id=EJ1122481) |
| **H7** | **All flagged score discrepancies** between automated and human scoring, above a published threshold — the check-score architecture. | Human rater | The only intervention with published evidence of containing scoring bias: [doi:10.1002/ets2.12192](https://doi.org/10.1002/ets2.12192) |
| **H8** | Where item-quality review is used as *evidence*, it must involve **enough raters to be reliable** — a G/D study on the review process itself recommended ≥7. Single-reviewer QA may be used for triage, never cited as validity evidence. | — | [ERIC EJ1491386](https://eric.ed.gov/?id=EJ1491386) |

**Corollary on review economics.** H1–H8 mean human review, not generation, is the cost
centre — inverting Kosh et al.'s 2019 cost model
([ERIC EJ1209262](https://eric.ed.gov/?id=EJ1209262)). A system claiming "AI removes the
item-writing bottleneck" has *moved* the bottleneck, and should say so.

### 10.4 What claims a system may make about a score

Four tiers. A system asserts a tier and must be able to produce the evidence for it. **The
tier is a property of π, not of the product.**

---

**Tier 0 — Practice signal.** *"You got 7 of 10 right on items about X."*
- **Requires:** H1 (key correctness) on a sampled audit basis. Nothing else.
- **Permitted:** descriptive feedback, next-item selection, learner-facing "you seem shaky
  here."
- **Prohibited:** any number on a scale, any comparison to another learner, any comparison
  to the same learner at another time, the words "mastery," "level," "proficiency,"
  "grade," "ready."
- *Most AI tutoring systems in 2026 are here and report as if they were at Tier 2.*

---

**Tier 1 — Calibrated formative estimate.** *"Estimated ability 0.6 ± 0.3 logits on
construct C, from policy π v1.2."*
- **Requires:** C1, C2, C3, C4, C7, C10 (formative-grade), H1–H3, H6.
- **Permitted:** an ability estimate **with an honest interval that includes item-sampling
  variance**; adaptive routing; within-learner comparison **only** across ≥ the n_required(Φ)
  probes established by the D-study.
- **Prohibited:** cross-learner ranking; any high-stakes gate; growth claims from fewer than
  the CBM-derived minimum (~14 well-controlled probes over ~8–15 weeks;
  [ERIC EJ970685](https://eric.ed.gov/?id=EJ970685), [ERIC EJ1142188](https://eric.ed.gov/?id=EJ1142188)).
- **Explicitly permitted despite the above:** telling the learner what they got wrong and
  why. Diagnostic feedback is not a score claim.

---

**Tier 2 — Diagnostic profile.** *"Mastered attributes {A1, A3}; not yet {A2}."*
- **Requires:** all of Tier 1, plus C6, plus H4; a Q-matrix derived from the cognitive model
  **prior to** generation (never retrofitted); a fitted DCM with reported attribute-level
  and test-level classification accuracy; **and external validation of at least one attribute
  claim against evidence not produced by the same generator** (transfer task, delayed
  retention, human-rated performance, downstream outcome).
- **Grounding:** [ERIC EJ1506971](https://eric.ed.gov/?id=EJ1506971) shows this is achievable
  — hierarchical A-CDM, 5,336 students, 60 latent classes, cognitive-model-derived Q-matrix.
- **Prohibited:** presenting a profile whose model fit was assessed only against
  generator-produced data (§6.3, the closed loop); presenting an attribute profile that is
  not distinguishable from a rescaled total score
  ([doi:10.1007/s11336-013-9363-z](https://doi.org/10.1007/s11336-013-9363-z)).

---

**Tier 3 — Summative / consequential.** *"This learner meets the standard."*
- **Requires:** all of Tier 2, plus C5, C8, C9; **100% human review of keyed answers on
  administered items** (not sampled); documented equating to a stable scale; published
  subgroup invariance analysis; a documented appeals path; and an independent (non-vendor)
  validity study.
- **Current field position:** the largest systematic review of AI-generated MCQ validity
  concludes that evidence **"does not yet support unsupervised use in summative assessment"**
  ([doi:10.1093/postmj/qgag057](https://doi.org/10.1093/postmj/qgag057)). Combined with
  §F1's argument that unsupervised remote artifacts cannot support a process claim at all,
  the honest position for a purely generative system in 2026 is: **Tier 3 is not currently
  attainable without human-proctored or verification-anchored observation.** Say so rather
  than approximating it.

---

### 10.5 Three prohibitions worth stating separately

1. **Never report Cronbach's α or McDonald's ω for an assessment in which learners receive
   different items.** It is undefined, not merely inaccurate (§7.1). Report (ρ_π, n_required).
2. **Never present a "wrong answer analysis" as diagnostic unless the distractors were
   derived from observed student errors.** A model-generated plausible wrong answer carries
   no misconception information; treating it as if it does manufactures a diagnosis
   ([doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193)).
   If you want diagnostic distractors, mine response data and generate from the *error*
   ([doi:10.18653/v1/2024.emnlp-main.512](https://doi.org/10.18653/v1/2024.emnlp-main.512)).
3. **Never claim a growth trend from probes whose equivalence has not been empirically
   established.** CBM measured the cost of this shortcut at a 26-WCPM spread across passages
   certified equivalent by readability formula — roughly a semester of growth, on the
   standard method ([ERIC EJ789795](https://eric.ed.gov/?id=EJ789795)).

---

## 11. Negative and null results ledger

Collected for auditability; the section requires ≥1 and has six.

| # | Finding | Source | Label |
|---|---|---|---|
| N1 | LLMs generate mathematically valid distractors but are **"less adept at anticipating common errors or misconceptions among real students"** — across in-context learning *and* fine-tuning. | Feng et al. 2024, NAACL Findings, [doi:10.18653/v1/2024.findings-naacl.193](https://doi.org/10.18653/v1/2024.findings-naacl.193) | `MEASURED-BENCH` |
| N2 | Only **9 of 23** expert-built AIG templates produced psychometrically isomorphic instances without revision; **9 of 23 required major modification**. Isomorphy is not a safe assumption. | Fu, Choe, Lim & Choi 2022, EMIP, [ERIC EJ1357630](https://eric.ed.gov/?id=EJ1357630) | `MEASURED-BENCH` |
| N3 | Human graders of programming assignments reached **Krippendorff's α ≈ 0.20** on correctness and **< 0.10** on style dimensions; only 1 of 22 reproduced their own grade on a hidden duplicate. "The idea of a 'gold standard' of human grading might be flawed." | Messer, Brown, Kölling & Shi 2025, ACM TOCE, [ERIC EJ1488833](https://eric.ed.gov/?id=EJ1488833) | `MEASURED-BENCH` |
| N4 | Six DIBELS ORF passages "developed to be comparable based on readability formulas" produced mean fluency ranging **67.9 to 93.9 WCPM**, biasing growth-trajectory shape and slope estimates. Readability-based equivalence is invalid; explicit equating is required. | Francis et al. 2008, JSP, [ERIC EJ789795](https://eric.ed.gov/?id=EJ789795) | `MEASURED-BENCH` |
| N5 | Systematic review of 102 documents: CBM-R progress-monitoring decision rules are **"based on expert opinion"** with **"very limited psychometric or empirical support"**; "a lack of published evidence to support program evaluation and progress monitoring with CBM-R." | Ardoin et al. 2013, JSP, [ERIC EJ1001681](https://eric.ed.gov/?id=EJ1001681) | `MEASURED-META` |
| N6 | Automated essay-scoring performance is substantially attributable to **essay length and surface proxies**, so agreement statistics do not license a construct claim. | Perelman 2014, *Assessing Writing*, [doi:10.1016/j.asw.2014.05.001](https://doi.org/10.1016/j.asw.2014.05.001) | `OBSERVED` |
| N7 (null) | Testwiseness manipulations produced **little post-instruction effect** on student performance on modified FCI/CSEM instruments — a genuine null — even though option-avoidance and position effects were individually significant. | DeVore, Stewart & Stewart 2016, PRPER, [ERIC EJ1122481](https://eric.ed.gov/?id=EJ1122481) | `MEASURED-BENCH` |
| N8 (null) | Misconception structure in FCI incorrect-answer groupings had **little relation** to previously identified gender-unfair items — the proposed explanation for the FCI gender gap was tested and failed. | Wells et al. 2019, PRPER, [ERIC EJ1227806](https://eric.ed.gov/?id=EJ1227806) | `MEASURED-BENCH` |
| N9 (null) | AI- and human-generated MCQs showed **no significant difference in discrimination index** (p = 0.17) despite significant differences in difficulty and non-functioning distractors — the "AI items are worse" claim is dimension-specific, not global. | Dhanvijay et al. 2025, *Adv Physiol Educ*, [ERIC EJ1490902](https://eric.ed.gov/?id=EJ1490902) | `MEASURED-BENCH` |
| N10 | Hierarchical diagnostic classification models, as analysed, may **collapse toward unidimensional models** — the multi-attribute diagnosis may not be doing the work claimed. | von Davier & Haberman 2014, *Psychometrika*, [doi:10.1007/s11336-013-9363-z](https://doi.org/10.1007/s11336-013-9363-z) | `OBSERVED` |

---

## 12. Open problems, ranked by how much they would change

1. **On-the-fly calibration from features, on an LLM.** Geerlings et al. 2012 case (c) —
   generating directly from *calibrated features* with no per-item and no per-family
   calibration — is fully specified in theory
   ([doi:10.1177/0146621612468313](https://doi.org/10.1177/0146621612468313)) and has never
   been built on a neural generator. This is the difference between "generation with
   psychometrics bolted on" and "psychometrics as the generation interface."
2. **Attribute-adaptive testing.** Generate the item that targets the Q-matrix cell whose
   mastery is currently most uncertain. Impossible with fixed banks; trivial to *attempt*
   with generators; unstudied. Nearest published work: sequential HDCM for multiple-attempt
   classroom data ([doi:10.1111/jedm.12387](https://doi.org/10.1111/jedm.12387)).
3. **Misconception mining at scale, then generation from mined errors.** DiVERT
   ([doi:10.18653/v1/2024.emnlp-main.512](https://doi.org/10.18653/v1/2024.emnlp-main.512))
   proves the loop closes on 1,434 math items. Nobody has run it continuously — mine errors
   from live responses, update the error taxonomy, regenerate distractors, re-measure
   diagnosticity — which is the only architecture that gets *better* with use.
4. **A reliability coefficient for generated assessment that the field agrees on.** §7.3 is a
   proposal, not a standard. Somebody has to run the G-study, publish ρ_π next to an
   effective-item-count estimate, and demonstrate the reliability/saturation confound.
5. **Cross-family screening.** Every published machine item-screener is evaluated on items
   from the same model family that generated them
   ([ERIC EJ1460469](https://eric.ed.gov/?id=EJ1460469)). The circularity is untested.
6. **Fairness of *generated items*, as distinct from fairness of *automated scoring*.** The
   scoring-bias literature is mature (§8.3). The item-generation-bias literature is
   essentially empty: nobody has systematically measured DIF in LLM-generated items by
   learner subgroup, despite DIF analysis being routine and cheap. Falcão et al. 2024
   ([ERIC EJ1416068](https://eric.ed.gov/?id=EJ1416068)) is the closest and it is a single
   study in one language.
7. **Distractor-generation evaluation metrics that are measurement-theoretic.** BLEU-family
   metrics dominate ([ERIC ED675568](https://eric.ed.gov/?id=ED675568)). The right metric is
   distractor *attractiveness conditional on θ* — estimable from a nested-logit model
   ([ERIC EJ959349](https://eric.ed.gov/?id=EJ959349)) and used by exactly one of the studies
   reviewed here ([ERIC EJ1501926](https://eric.ed.gov/?id=EJ1501926)).

---

## Sources

**Automatic item generation — foundations (11)**
1. Irvine & Kyllonen (eds), *Item Generation for Test Development* — https://doi.org/10.4324/9781410602145
2. Gierl & Haladyna (eds), *Automatic Item Generation* — https://doi.org/10.4324/9780203803912
3. Gierl & Lai 2012, *IJT*, "The Role of Item Models in AIG" — https://doi.org/10.1080/15305058.2011.635830
4. Gierl, Lai & Turner 2012, *Medical Education* — https://doi.org/10.1111/j.1365-2923.2012.04289.x
5. Gierl & Lai 2013, *Medical Education* — https://doi.org/10.1111/medu.12202
6. Gierl, Lai, Pugh, Touchie, Boulais & De Champlain 2016, *AME* — https://doi.org/10.1080/08957347.2016.1171768
7. Gierl & Lai 2016, *EMIP*, review process — https://doi.org/10.1111/emip.12129
8. Embretson & Kingston 2018, *JEM* — https://eric.ed.gov/?id=EJ1171125
9. Kosh et al. 2019, *EMIP*, cost-benefit — https://eric.ed.gov/?id=EJ1209262
10. Cole et al. 2020, *JATT*, saturation — https://eric.ed.gov/?id=EJ1227607
11. Rafatbakhsh et al. 2021, *EMIP*, idioms — https://eric.ed.gov/?id=EJ1298981

**Neural / LLM item generation (15)**
12. von Davier 2018, *Psychometrika*, RNN AIG — https://doi.org/10.1007/s11336-018-9608-y
13. Hommel et al. 2022, *Psychometrika*, transformer AIG — https://doi.org/10.1007/s11336-021-09823-9
14. Kıyak, Kaya & Emekli 2026, *Postgrad Med J*, systematic review (71 studies) — https://doi.org/10.1093/postmj/qgag057
15. Kıyak & Emekli 2024, *Postgrad Med J*, prompt review — https://doi.org/10.1093/postmj/qgae065
16. Tan, Armoush, Mazzullo, Bulut & Gierl 2025, *IJATE* (60 studies) — https://eric.ed.gov/?id=EJ1476463
17. Kurdi et al. 2020, *IJAIED*, AQG review — https://doi.org/10.1007/s40593-019-00186-y
18. Falcão, Costa & Pêgo 2022, *AHSE* — https://eric.ed.gov/?id=EJ1336013
19. Cheung et al. 2023, *PLOS ONE* — https://doi.org/10.1371/journal.pone.0290691
20. Doughty et al. 2024, ACE '24 — https://doi.org/10.1145/3636243.3636256 · https://arxiv.org/abs/2312.03173
21. Young et al. 2025, *Teaching of Psychology* — https://eric.ed.gov/?id=EJ1474433
22. Dhanvijay et al. 2025, *Adv Physiol Educ* — https://eric.ed.gov/?id=EJ1490902
23. Gündeger Kilci 2025, *IJATE* — https://eric.ed.gov/?id=EJ1491386
24. Ripoll y Schmitz & Sonnleitner 2025, *LSAE* — https://eric.ed.gov/?id=EJ1477454
25. Falcão, Pereira, Pêgo & Costa 2024, *Educ Inf Technol* — https://eric.ed.gov/?id=EJ1416068
26. Gorgun & Bulut 2025, *EMIP*, LLM quality control — https://eric.ed.gov/?id=EJ1460469

**Distractors and misconceptions (19)**
27. Hestenes, Wells & Swackhamer 1992, FCI — https://doi.org/10.1119/1.2343497
28. Scott & Schumayer 2018, *PRPER*, central distractors — https://eric.ed.gov/?id=EJ1168701
29. Wells et al. 2019, *PRPER*, modified module analysis — https://eric.ed.gov/?id=EJ1227806
30. Erceg et al. 2016, *PRPER*, KMT concept inventory — https://eric.ed.gov/?id=EJ1122500
31. Flame Test Concept Inventory 2018, *JCE* — https://eric.ed.gov/?id=EJ1166996
32. Reaction Coordinate Diagram Inventory 2020, *JCE* — https://eric.ed.gov/?id=EJ1263565
33. QuPRI 2019, *JCE* — https://eric.ed.gov/?id=EJ1224931
34. Resonance Concept Inventory 2023, *JCE* — https://eric.ed.gov/?id=EJ1445121
35. DeVore, Stewart & Stewart 2016, *PRPER*, testwiseness — https://eric.ed.gov/?id=EJ1122481
36. Feng et al. 2024, *Findings of NAACL* — https://doi.org/10.18653/v1/2024.findings-naacl.193
37. Fernandez et al. 2024, *EMNLP*, DiVERT — https://doi.org/10.18653/v1/2024.emnlp-main.512
38. Wang & Meng 2026, *Language Testing* — https://eric.ed.gov/?id=EJ1501926
39. Awalurahman & Budi 2024, *PeerJ CS*, SLR — https://doi.org/10.7717/peerj-cs.2441
40. Kosh 2021, *JATT*, distractor suites — https://eric.ed.gov/?id=EJ1296053
41. Ghanem & Fyshe, DISTO, EDM 2024 — https://eric.ed.gov/?id=ED675568
42. Bolt et al. 2012, *Psychometrika*, multidimensional nested logit — https://eric.ed.gov/?id=EJ959349
43. Rasch analysis of distractors, *JOM* 1998 — https://eric.ed.gov/?id=EJ562026
44. Distractors with information, *JAM* 2011 — https://eric.ed.gov/?id=EJ954592
45. Differential distractor functioning, *JAM* 2000 — https://eric.ed.gov/?id=EJ617262

**Random-item / hierarchical IRT and item families (8)**
46. Glas & van der Linden 2003, *APM*, item cloning — https://doi.org/10.1177/0146621603027004001
47. Sinharay, Johnson & Williamson 2003, *JEBS*, FERF — https://doi.org/10.3102/10769986028004295
48. Johnson & Sinharay 2005, *APM*, polytomous families — https://doi.org/10.1177/0146621605276675
49. Sinharay & Johnson 2008, *IJT*, admissions case study — https://doi.org/10.1080/15305050802262019 · https://eric.ed.gov/?id=EJ805764
50. Geerlings, Glas & van der Linden 2011, *Psychometrika* — https://doi.org/10.1007/s11336-011-9204-x
51. Geerlings, van der Linden & Glas 2012, *APM*, optimal test design — https://doi.org/10.1177/0146621612468313
52. Cho, De Boeck, Embretson & Rabe-Hesketh 2014, *Psychometrika*, AMIS — https://doi.org/10.1007/s11336-013-9360-2
53. Fu, Choe, Lim & Choi 2022, *EMIP*, weak-theory AIG / DCIF — https://eric.ed.gov/?id=EJ1357630

**Difficulty prediction and calibration shortcuts (4)**
54. Yaneva et al. 2024, BEA shared task findings — https://aclanthology.org/2024.bea-1.39/
55. Bulut, Gorgun & Tan 2024, BEA, USMLE — https://aclanthology.org/2024.bea-1.44/
56. Štěpánek, Dlouhá & Martinková 2023, *Mathematics* — https://doi.org/10.3390/math11194104
57. Item-writer judgments vs actual difficulty, *LAQ* 2011 — https://doi.org/10.1080/15434303.2010.536924

**Adaptive testing, exposure, security (12)**
58. van der Linden & Glas 2000, *CAT: Theory and Practice* — https://doi.org/10.1007/0-306-47531-6
59. Stocking & Lewis 1998, *JEBS*, conditional exposure control — https://doi.org/10.3102/10769986023001057
60. Stocking & Lewis 1995, ETS RR, new exposure-control method — https://doi.org/10.1002/j.2333-8504.1995.tb01660.x
61. Sympson–Hetter conditional procedure evaluation — https://eric.ed.gov/?id=ED442837
62. a-stratified + Sympson–Hetter, *APM* 2002 — https://eric.ed.gov/?id=EJ779492
63. Exposure control under GPCM, *APM* 2004 — https://eric.ed.gov/?id=EJ727350
64. Test-development exposure control — https://eric.ed.gov/?id=ED421526
65. Organised item theft in CAT, ETS RR-06-22 — https://eric.ed.gov/?id=EJ1111472
66. IRT linking under random-groups equating, *AME* 2010 — https://eric.ed.gov/?id=EJ875216
67. Duolingo English Test reliability (VENDOR) — https://doi.org/10.46999/hqep1801
68. Duolingo English Test psychometric considerations (VENDOR) — https://doi.org/10.46999/mfkw9830
69. Duolingo English Test subscores (VENDOR) — https://doi.org/10.46999/wbqi4443

**Cognitive diagnostic models (15)**
70. Junker & Sijtsma 2001, *APM*, DINA — https://doi.org/10.1177/01466210122032064
71. de la Torre 2011, *Psychometrika*, G-DINA — https://doi.org/10.1007/s11336-011-9207-7
72. Leighton, Gierl & Hunka 2004, *JEM*, AHM — https://doi.org/10.1111/j.1745-3984.2004.tb01163.x
73. Templin & Bradshaw 2014, *Psychometrika*, HDCM — https://doi.org/10.1007/s11336-013-9362-0
74. von Davier & Haberman 2014, *Psychometrika*, commentary — https://doi.org/10.1007/s11336-013-9363-z
75. Gierl & Cui 2008, retrofitting — https://doi.org/10.1080/15366360802497762
76. Sessoms & Henson 2018, DCM applications review — https://doi.org/10.1080/15366367.2018.1435104
77. de la Torre 2008, *JEM*, empirical Q-matrix validation — https://eric.ed.gov/?id=EJ819613
78. Rupp & Templin 2008, *EPM*, Q-matrix misspecification — https://eric.ed.gov/?id=EJ782123
79. Country-specific Q-matrices, *LSAE* 2022 — https://eric.ed.gov/?id=EJ1356133
80. Effatpanah et al. 2026, *EMIP*, cognitive-model-derived Q-matrices — https://eric.ed.gov/?id=EJ1506971
81. Kwon, Huggins-Manley, Templin & Zheng 2024, *JEM*, sequential HDCM — https://doi.org/10.1111/jedm.12387
82. G-DINA retrofit to PISA reading — https://eric.ed.gov/?id=EJ1112138
83. G-DINA retrofit to high-stakes L2 reading — https://eric.ed.gov/?id=EJ1226655
84. DINA Q-matrix specifications, statewide maths — https://eric.ed.gov/?id=EJ1265426

**Reliability (4)**
85. Cronbach & Shavelson 2004, *EPM* — https://doi.org/10.1177/0013164404266386
86. Revelle & Zinbarg 2009, *Psychometrika*, ω — https://doi.org/10.1007/s11336-008-9102-z
87. Brennan 2001, *Generalizability Theory* — https://doi.org/10.1007/978-1-4757-3456-0
88. G-theory for RTI progress-monitoring decisions — https://eric.ed.gov/?id=EJ1069868

**Automated scoring (17)**
89. Bridgeman, Trapani & Attali 2012, *AME* — https://doi.org/10.1080/08957347.2012.635502
90. Ramineni & Williamson 2018, ETS RR — https://doi.org/10.1002/ets2.12192
91. Loukina, Madnani & Zechner 2019, BEA — https://doi.org/10.18653/v1/W19-4401 · https://aclanthology.org/W19-4401/
92. Perelman 2014, *Assessing Writing* — https://doi.org/10.1016/j.asw.2014.05.001
93. Shermis & Hamner, ASAP contrast — https://doi.org/10.4324/9780203122761-27
94. Jiao, Song & Lee 2026, *EMIP*, LLM rater effects — https://doi.org/10.1111/emip.70018
95. Chen, Wu & Zhang 2026, *Assessing Writing*, predictive bias — https://doi.org/10.1016/j.asw.2026.101066
96. Attali & Burstein, e-rater v2, ETS RR-04-45 — https://eric.ed.gov/?id=EJ1110978
97. e-rater TOEFL evaluation, ETS RR-12-06 — https://eric.ed.gov/?id=EJ1109838
98. Population invariance in automated scoring, ETS RR-13-18 — https://eric.ed.gov/?id=EJ1110012
99. Fairness tooling for automated scoring, ACL Ethics 2017 — https://doi.org/10.18653/v1/W17-1605
100. Meta-analysis, human vs machine essay scoring agreement — https://eric.ed.gov/?id=EJ1407232
101. Messer, Brown, Kölling & Shi 2025, *ACM TOCE*, human grading consistency — https://eric.ed.gov/?id=EJ1488833
102. Messer et al. 2024, *ACM TOCE*, automated grading review (121 papers) — https://eric.ed.gov/?id=EJ1419855
103. Generative grading, EDM 2021 — https://eric.ed.gov/?id=ED615516
104. ASAG systematic review (assessment perspective) — https://doi.org/10.31234/osf.io/geayp_v1
105. LLM–human agreement, sustainability education — https://doi.org/10.1002/jcal.70160

**Curriculum-Based Measurement (23)**
106. Deno 1985, *Exceptional Children* — https://eric.ed.gov/?id=EJ326811
107. Fuchs & Deno 1991, GOM vs SSMM — https://eric.ed.gov/?id=EJ428597
108. Ardoin, Christ, Morena, Cormier & Klingbeil 2013, *JSP*, systematic review — https://eric.ed.gov/?id=EJ1001681
109. Christ, Zopluoglu, Long & Monaghen 2012, *Exceptional Children* — https://eric.ed.gov/?id=EJ970685
110. Thornblad & Christ 2014, *SPR*, 6 weeks daily — https://eric.ed.gov/?id=EJ1142188
111. Christ & Ardoin 2009, *JSP*, passage equivalence & probe-set development — https://eric.ed.gov/?id=EJ821847
112. Christ & Ardoin 2009, *JSP*, readability statistics & equating — https://eric.ed.gov/?id=EJ821846
113. Ardoin & Christ 2009, *SPR*, standard errors across passage sets — https://eric.ed.gov/?id=EJ842725
114. Francis et al. 2008, *JSP*, DIBELS form effects — https://eric.ed.gov/?id=EJ789795
115. DIBELS Next ORF form effects — https://eric.ed.gov/?id=EJ995832
116. DIBELS ORF equating study — https://eric.ed.gov/?id=EJ995835
117. DIBELS Next variability for at-risk readers — https://eric.ed.gov/?id=EJ1155019
118. ORF passage/order effects partial replication — https://eric.ed.gov/?id=EJ1196832
119. Passage variance and CBM sensitivity — https://eric.ed.gov/?id=EJ683511
120. Christ 2006, *SPR*, SE of slope & confidence intervals — https://eric.ed.gov/?id=EJ788238
121. Christ et al. 2013, *JSP*, multi-study schedule/duration — https://eric.ed.gov/?id=EJ1001684
122. Baseline estimation effects on CBM-R trend — https://eric.ed.gov/?id=EJ1055845
123. Defensible progress-monitoring data for medium/high-stakes decisions — https://eric.ed.gov/?id=EJ980203
124. Confidence-interval overlap for reliable growth — https://eric.ed.gov/?id=EJ1113651
125. Robust regression for CBM slope — https://eric.ed.gov/?id=EJ1058459
126. Decision-rule accuracy comparison (CBM-R vs NWF) — https://eric.ed.gov/?id=EJ1417097
127. GOM vs SSMM slope stability & validity — https://eric.ed.gov/?id=EJ1375326
128. CBM of maths problem solving: establishing score equivalence — https://eric.ed.gov/?id=EJ866533
</content>
</invoke>

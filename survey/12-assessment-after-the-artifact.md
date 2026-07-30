---
title: "Assessment After the Artifact — measuring a person when the work no longer indicates them"
section: assessment
status: draft
date: 2026-07-28
source_report: research/raw/F1-assessment-reconstruction.md
---

# Assessment After the Artifact

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

Assessment was never about artifacts. It is an inference — from something observed
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

This reframing is generative rather than gloomy, because it says the design problem
is not "invent tasks AI cannot do" — a race whose finish line recedes annually. The
problem is to **restore a margin**, and there are exactly four ways: bind the
response to real time (orals, live problem-solving); bind the claim to a verifiable
object (proof assistants, test suites, withheld data); bind the artifact to a process
trace (version control, revision history); or abandon per-task security and secure
the aggregate (programmatic assessment).

Detection is not on that list. That is the diagnosis, not an oversight: detection
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

So the naive implementation — one AI-conducted thirty-minute high-stakes viva
replacing the final exam — reproduces exactly the psychometric weakness that killed
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
across fourteen years rather than randomisation, and **no reported reliability
coefficients**.

The reading this survey adopts: **the equity case for AI-conducted orals rests on
frequency and practice, not on the technology.** Every documented fairness risk of
orals — anxiety, unfamiliarity, differential coaching — is a *first-exposure* effect
that decays with repetition. What made orals inequitable was that students met one,
once, at maximum stakes. A modality students encounter forty times per degree is a
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
listening miscomprehension patterns." Same finding: **LLMs fix form, not
diagnosticity.** And note the pipeline shape in both — response data first,
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
no measurement properties at all** — that is the sentence institutions rolling out
LLM quiz generators need on the wall.

Fifteen years of pre-LLM automatic item generation, mostly in medical education,
established that items generated from cognitive models are rated by blinded expert
panels as comparable to traditionally authored ones, and demonstrated end-to-end IRT
and CAT integration. But the load-bearing assumption is isomorphicity — that
sibling items from one item model share parameters — and it is an assumption. When
tested: only **9 of 23** expert-built templates produced psychometrically isomorphic
instances without revision, and **9 of 23 required major modification**.

Three consequences follow, and the third is the one nobody is watching.

(a) The psychometric object is the generator. If item text comes from a
stochastic policy conditioned on a specification, the object with parameters is the
*distribution* the policy induces, not any individual item. Random-item and crossed
random-effects IRT is the existing apparatus; what must be demonstrated is that
generator-level parameters are stable enough to support inference even though
item-level ones are not.

(b) Every operational system currently understates measurement error.
Conventional adaptive-test scoring treats calibrated item parameters as *known*. Under
generation they are draws, so the standard error of θ must include item-sampling
variance, and no shipping system appears to do this. The prediction is falsifiable
and cheap to test: **reported reliabilities for LLM-generated adaptive quizzes are
systematically optimistic, and the gap widens as item novelty increases.** Duolingo's
own published numbers illustrate the size of the gap — **test–retest 0.84 against
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

*Flagged as construction, not finding: personalisation-induced DIF is this project's
own framing and no study of it was located. It is offered as the most serious
unexamined fairness risk in AI-driven assessment, and as a hypothesis someone should
test.*

And the replacement for alpha. Cronbach himself supplies the exit route,
pointing to generalizability theory. G-theory decomposes score variance into facets —
persons, items, occasions, raters — and asks how well a score generalises to a
universe of admissible observations. That framing is *native* here, because **a
generator is a formal specification of a universe of admissible observations**,
arguably the first time in the history of measurement that this universe has been
written down explicitly and executably rather than gestured at.

The concrete protocol, offered as a specification to test rather than a finding:
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

## 5. The nulls, given their own space

**Detection is bounded in theory and broken in practice, and its errors are not
random.** The theoretical result bounds the AUROC of the *best possible* detector by
the total variation distance between human and machine text distributions — as
models improve, achievable detection falls toward chance. Empirically, the largest
comparative test of 14 systems concluded they are "neither accurate nor reliable."
Then Liang et al., usually cited too weakly — seven deployed detectors, run on TOEFL
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
detector *better* than any documented — 90% sensitivity, 5% false-positive rate.
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
from **67.9 to 93.9 words correct per minute** — roughly a semester of growth,
purely from which passage a child happened to get.

Progress-monitoring decision rules rest on expert opinion. A systematic review of
102 documents found curriculum-based measurement decision rules have "very limited
psychometric or empirical support."

And two clean negatives that cut *against* the fashionable direction, reported
because omitting inconvenient nulls is worse than reporting them. Testwiseness
manipulations produced little post-instruction effect on modified concept
inventories, despite option-avoidance and position effects being individually
significant. And misconception structure in FCI incorrect-answer groupings had
little relation to previously identified gender-unfair items — the proposed
explanation for the FCI gender gap was tested and failed.

Finally, a null that constrains criticism of AI items rather than endorsing them:
AI- and human-generated MCQs showed **no significant difference in discrimination
index (p = 0.17)**, despite significant differences in difficulty and
non-functioning distractors. "AI items are worse" is dimension-specific, not global.

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
systems in 2026 sit at Tier 0 and report as if they were at Tier 2** — the single most
common measurement error in the field. And **Tier 3 is not currently attainable by a
purely generative system**: the largest systematic review of AI-generated MCQ validity
concludes the evidence "does not yet support unsupervised use in summative
assessment," and combined with the collapse of the process claim on unsupervised
artifacts, consequential decisions require proctored or verification-anchored
observation. Say so rather than approximating it.

Explicitly permitted at every tier, worth stating because the prohibitions are long:
telling the learner what they got wrong and why. Diagnostic feedback is not a
score claim.

Three standalone prohibitions. Never report α or ω for an assessment where learners
receive different items — undefined, not merely inaccurate. Never present a
wrong-answer analysis as diagnostic unless the distractors were derived from observed
student errors; doing so manufactures a diagnosis. Never claim a growth trend from
probes whose equivalence has not been empirically established.

---

## 7. The strongest counter-argument

*This is an argument for making assessment far more elaborate. Frequent secured orals,
human review of every keyed answer, G-studies per generator — you have replaced a
simple system that mostly worked with one nobody will build.*

Two answers.

First, the burden moved rather than grew. Human review, not generation, is now the
bottleneck — a system claiming "AI removes the item-writing bottleneck" has *moved* it
and should say so. And verification-first assessment makes the product claim genuinely
free wherever the discipline has already agreed to submit to an oracle: mathematics
agreed centuries ago, software by construction, empirical science via replication.
Institutions that adopted autograders as a saving inverted the logic — they banked it
and never spent it on the capability and learning claims that now go unevidenced.

Second, the reframe that should reorganise priorities: **the emergency was never
cheating.** In Bastani et al.'s trial of ~1,000 high-school maths students, unguarded
assistance improved practice performance by 48% and left students **17% worse** on an
unassisted exam than students who never had access (§01). *(A note on provenance, since this
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

## 8. What this section commits us to

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

---
title: "Supplying the Executive — a specification for a system that provides the executive function the learner is missing, rather than requiring it"
wave: V
section: V5
date_researched: 2026-07-29
sources_count: 58
status: raw-research
---

# V5 — Supplying the Executive

> **What this document is.** N2 established the finding. This is the machine that acts on it.
> Nothing here is a summary of what exists. Every numbered artifact below is a specification for
> something that does not exist, built on measured constraints, with the conditions that would
> show it was wrong stated at the point of design.
>
> **The four licensed conclusions this builds on**, from `research/raw/N2-executive-function-and-attention.md`:
>
> 1. Executive function is a resource products require and do not supply. The measured failure
>    point is **recognising the need**, not accessing the help — and repairing the recognition,
>    on its own, does not repair learning.
> 2. A question holds attention because it can be **attempted**; an exhortation cannot —
>    **g = 0.54** on its own answer, **g = 0.04** in general.
> 3. **Referential status**, not persistence, decides whether an added element helps or harms.
> 4. The ADHD design target is **signal-to-noise per opportunity** and **delay-to-payoff**, not
>    session length. The measured deficit is in the **first block**, not a vigilance decrement.
>
> And the independent confirmation from the other direction: the best-instrumented tutor in the
> world published a null, and the diagnosis was **invocation** — the mechanism worked when it
> fired, and it only fired when a student recognised they needed help and went to get it.
>
> **The single design commitment.** Every executive act the current generation of products asks a
> learner to perform, this system performs on the learner's behalf, from observable interaction
> state, and then measurably gives back — with the giving-back instrumented as tightly as the
> supplying.

---

## Source reachability log (2026-07-29)

WebSearch exhausted per `process/CLAUDE.md` §5. Retrieval ran on **ERIC**
(`api.ies.ed.gov/eric/`), **Crossref**, **Semantic Scholar**, and direct `curl` +
`pdftotext` against `files.eric.ed.gov`.

- **ERIC is the workhorse for this section.** The educational-data-mining literature that carries
  the detector evidence (Baker's affect and gaming detectors, Beck & Gong wheel-spinning, Wan &
  Beck, the EDM proceedings series) is deposited there and almost nowhere else. Bare keyword
  queries work; `id:` queries work; quoted-phrase field queries return `numFound 0` unpredictably.
- **`files.eric.ed.gov/fulltext/<ID>.pdf` serves to `curl`** with a browser User-Agent. This
  recovered **Baker et al. (2012)**, *Towards Sensor-Free Affect Detection in Cognitive Tutor
  Algebra*, ED537205, in full — the source of the detector performance table and the feature
  lists quoted verbatim in §2. It is the most load-bearing new source in this document.
- **Semantic Scholar** returned `HTTP 429` on the first call and thereafter served at roughly one
  call per 4 s. Publisher-elided abstracts (ACM, Elsevier) come back `null` even when the record
  resolves.
- **ACM Digital Library** deposits no abstracts to Crossref or Semantic Scholar. The
  interruption-timing literature (Adamczyk & Bailey 2004; Iqbal & Bailey 2006, 2008) is therefore
  **cited by title, venue and DOI with its magnitudes UNVERIFIED**. The structural claim those
  papers carry — that the cost of an interruption depends on where in a task's structure it lands
  — is used; no number from them is.
- **Springer** served `link.springer.com/content/pdf/10.1007/s11251-009-9107-8.pdf` as an HTML
  paywall shell, so **Salden et al. (2010)** on adaptive fading is quoted from its ERIC abstract
  (EJ880294) and its **effect sizes are UNVERIFIED**. This matters and is flagged again at point
  of use, because that paper is the only positive result for adaptive fading in the document.

**Evidence labels.** Per `CLAUDE.md` §2, plus the two authorised in N2 and one added here:

`MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` ·
`INFERENCE` · `DESIGN` · `OPEN` · **`SPEC`**

- A **`SPEC`** claim describes an artifact designed in this document. It has no evidential
  standing whatsoever, it names the measured constraints it is built from, and it may never be
  restated as a finding. It differs from `DESIGN` only in granularity: `DESIGN` names an artifact,
  `SPEC` names a parameter, threshold, rule or interface element inside one.
- An absent citation is not a reason to leave something unspecified. Where the literature is
  silent, the parameter is chosen, marked `SPEC`, and given a rule for revising it from data.

**Builds on, does not repeat:** N2 (the whole evidential base), B1 (the learning-science floor),
B2 (the −17% withdrawal result), E3 (the Khanmigo null), F5 (the learner-model schema and its
legal constraints), F8 (EU AI Act, COPPA, FERPA), F9 (OP-19, the clickstream-affect legal
question), F10 (expertise reversal), F11 (FSRS and scheduling), H1/H2 (SELPA, accommodations),
K1 (compression, wheel-spinning, opportunities-to-mastery), N2 §4.4 (the twelve demand points).

---

## 0. The deliverable table

One row per executive function, plus the two cross-cutting machines that serve all four.

| Function | Observable signal | Intervention | Fading rule | Failure mode | Buildable today |
|---|---|---|---|---|---|
| **Initiation** | Time-from-cue-to-first-submitted-response; sessions opened per scheduled cue; time-of-day gap against the learner's own established routine | If-then cue bound to an existing routine; the session opens itself with the first item already on screen and answerable in one action; no menu, no goal-setting screen | Fade the pre-loading (not the cue) once the learner's median time-to-first-response is below the population 40th percentile across 10 consecutive sessions. Cue itself is never faded — it costs nothing and its removal has no upside | The cue becomes a notification the learner learns to dismiss. Detect by cue→open conversion falling below its own 20-session baseline | **Yes** |
| **Sustaining** | Opportunities completed per session; within-session slope of accuracy at matched item difficulty; inter-action gap distribution; abandonment position within a segment | Instructor-segmented chunks with system-set boundaries; a state card that survives the gap between segments; session self-terminates at a competence threshold, not a clock | Not a support to be faded. Segmentation is a property of the material, and prior knowledge does not moderate design principles (**p = .14**, Noetel et al. 2021) | Extending the session because the learner is engaged. Converts a persistence win into a satiation loss and, per Dovis et al., persistence is the one thing incentives *do* move | **Yes** |
| **Monitoring** | The eleven features in §2.3 — latency z-scored per step, post-error latency, error-run length, edit churn, backtracking, help dwell < 1 s, help-avoidance after 3 errors, opportunity count without 3-in-a-row-correct, within-learner RT variability, revision-to-submit ratio, idle-gate state | The Stall Detector (§2) fires an *unrequested worked step with a required response* inside the intermediate-mastery band; outside the band it fires prerequisite repair (low) or a strategy change (high) | The intervention *content* fades under §4's unaided-evidence rule. The *detector* never fades — it is instrumentation, not a support, and the learner never sees its output | Interrupting productive struggle. The cost is highest exactly where the detector is most confident, because low prior knowledge produces both the strongest stall signal and the strongest case for letting the learner fail (Roll et al. 2014) | **Partial** — features and labels are free from any step-based tutor's logs; calibration to a *behavioural* target rather than an affective one has not been done |
| **Shifting** | Beck & Gong wheel-spin criterion (≥10 opportunities on a KC without three consecutive correct); repeated identical wrong answer; strategy fingerprint unchanged across ≥5 failed attempts | Forced strategy change: the KC is suspended, a *different* representation of the same KC is delivered, and the original is re-queued behind a prerequisite probe. Not a hint | The forced change fades to an *offered* change once the learner initiates a strategy change unprompted on 3 separate KCs | Presenting the shift as a verdict on the learner. And shifting on a single error, which teaches that errors terminate work | **Partial** — the detector is a threshold rule and is trivial; the alternative representation per KC is the expensive part and is a content problem, not an ML problem |
| *(cross-cutting)* **Unaided Competence Estimate** | Every opportunity, tagged with the assistance weight present at the time | Discount each opportunity's contribution to the competence estimate by the assistance present; spend ~10% of opportunities on deliberately unassisted probes | n/a — this *is* the fading instrument | The estimate drifts optimistic because probes are scheduled where they are cheap, and where they are cheap is where they are easy | **Partial** — knowledge tracing is standard; assistance-weighted tracing is not |
| *(cross-cutting)* **Externalised state** | Which surfaces the learner's pointer and gaze-free interactions actually touch; whether a support is consulted at all | Goal line, state card, worked ledger, open-loop list (§6) | A surface is removed when its consult-rate is zero across 20 opportunities, or when the learner's unaided time-per-opportunity is shorter than their assisted time | Adding a surface that creates a new obligation rather than replacing an existing one. That is a competing referent, and persistence multiplies its dose | **Yes** |

Legend for the last column: **Yes** = standard engineering on data a step-based tutor already
logs. **Partial** = one component is standard and one is not. **No** = requires a research result
that does not exist. Nothing in this specification is rated **No**, and that is a deliberate
constraint on the design: a specification that requires an unfound research result is a wish.

---

## 1. The four functions, separately

They are lumped together as "executive function" because they load on a common factor in
individual-differences research. That is a fact about variance decomposition, not about design.
For a builder they are four different observables, four different interventions, four different
ways to be wrong, and four different endpoints.

The training literature settles what this section does *not* do. **Kassai, Futó, Demetrovics &
Takács (2019)**, *Psychological Bulletin*: "training a component **did not have a significant
effect on the untrained components** (g = 0.11, k = 17, **p = .11**)." **Rapport, Orban, Kofler &
Friedman (2013)**: training attention did not improve attention; training mixed executive
functions did not improve the targeted executive functions, both 95% CIs including zero.
**Westwood et al. (2023)**, 36 RCTs, blinded outcomes: ADHD total **SMD 0.12 [−0.01, 0.25]**,
with inattention rising to 0.40 **only inside the training setting**. `MEASURED-META` throughout.

So each of the four is *supplied*, never *trained*. The word "supplied" carries a specific
operational meaning here: the system performs the act, from observable state, without asking the
learner to perform it and without telling the learner that it performed it.

### 1.1 Initiation

**What the system observes.** Four quantities, none of them a self-report.

| Signal | Definition | Why this one |
|---|---|---|
| `cue_to_open` | Seconds from a scheduled if-then cue firing to the app being opened | The implementation-intention literature measures behaviour at exactly this point |
| `open_to_first_response` | Seconds from app open to the first *submitted* response | Not "time on screen." A screen the learner is staring at is not an initiation |
| `cue_conversion` | Fraction of scheduled cues followed by a session within the cue's window | Distinguishes a cue that works from a cue that has become wallpaper |
| `routine_anchor_stability` | Variance in the wall-clock time of the learner's completed sessions over the last 20 | An if-then intention needs an *existing* routine to bind to; this measures whether one exists |

**What it does.** `SPEC`. Three things, in order, and the order is the design.

1. **Bind the cue to a routine the learner already has**, not to a clock. The implementation-
   intention meta-analysis — **Breitwieser & Reinelt (2026)**, *British Journal of Psychology*,
   registered report, 52 effect sizes / 42 studies / **N = 12,957**, mean age 10.67 — reports
   **Hedges' g = 0.31 [0.21, 0.41]**, I² = 65.2%, with effects "**stronger in studies with
   younger children and (in some analyses) children with ADHD**, suggesting that implementation
   intentions are **particularly effective when self-regulation abilities are limited**."
   `MEASURED-META`. The system discovers the anchor from `routine_anchor_stability` rather than
   asking for it, and proposes it once, in the form *"after X, then Y"*, where X is an event the
   log already shows recurring.
2. **The session opens itself at the cue** with the first item rendered and answerable. Not a
   dashboard, not a "continue where you left off" card, not a streak. One item, one action.
3. **The first item is chosen for answerability, not for value.** It is a two-alternative
   discrimination on a knowledge component already above 0.85 mastery, and its correctness signal
   arrives in under two seconds. Its instructional value is close to zero and that is fine; its
   job is to convert an open app into a submitted response. `SPEC`.

**What it must never do.**

- Never present a choice as the first act. Choosing what to work on is a *separate* executive
  demand (N2 §4.4 row 2) and putting it in front of the initiation demand stacks two failures
  into one moment.
- Never require a goal statement, an intention, a mood check, or a "how much time do you have?"
  prompt before the first item.
- Never use loss framing on a missed cue. A streak that breaks converts an initiation failure
  into an avoidance signal, and the population this is designed for is the one with a measured
  delay-aversion profile (**d = 0.43**, Jackson & MacKillop 2016, N = 3,913, p < 10⁻¹⁵).
- Never fire more than one cue per day per learner. A second cue is a notification.

**How you would know it worked.** `cue_conversion` and `open_to_first_response`, both against the
learner's own pre-intervention baseline, and neither against a population mean. The falsifier: if
`cue_conversion` rises while `opportunities_completed` per session falls, the cue has produced
attendance without work, which is a worse outcome than no cue because it consumes the anchor.

### 1.2 Sustaining

**What the system observes.** `opportunities_completed`; the within-session slope of accuracy at
matched item difficulty; the inter-action gap distribution; and the position within a segment at
which abandonment occurs.

**What it does.** Segments the material itself and refuses to hand the segmentation to the
learner. **Rey et al. (2019)**, via Noetel et al.'s meta-meta-analysis: instructor-segmented
**g = 0.41 [0.32, 0.50]** against learner-segmented **g = 0.20 [0.11, 0.28]**, k = 32 each; and
segmented content takes **longer** to study, **g = 0.92 [0.82, 1.02]**, k = 19. System-paced
design principles are worth **g = 0.41 [0.33, 0.49]** against learner-paced **g = 0.27 [0.19,
0.35]**, p = .02. `MEASURED-META`.

Noetel et al.'s explanation of the pacing moderator is the operative one, and it is the reason
this row belongs in a document about executive function at all: "when self-paced, learners can
more easily use their **own strategies** to manage high levels of cognitive load." Learner-paced
delivery offloads load management onto the resource the learner does not have.

**What it must never do.**

- Never extend a session because engagement is high. **Dovis et al. (2012)**, 30 children with
  ADHD against 31 controls: "even the strongest incentives (10 euros and Gaming) were unable to
  normalize their performance … **Only children with ADHD showed a decrease in performance over
  time. Importantly, the strongest incentives … normalized persistence** in these children."
  `MEASURED-RCT`. Persistence is the variable an engagement layer moves. Extending the session
  spends the one thing the layer bought.
- Never use a variable-ratio reward schedule. Deci, Koestner & Ryan's 128 experiments on tangible
  expected performance-contingent rewards are carried from the corpus, and the AI Act's Art.
  5(1)(b) prohibition on exploiting age or disability vulnerability makes engagement mechanics
  tuned to a known impulsivity profile a legal question rather than a taste question (F8).
- Never treat a pause as disengagement. See the idle gate, §2.5.

**How you would know it worked.** The within-session accuracy slope at matched difficulty, and
`opportunities_completed`. Not minutes. Acquisition is counted in opportunities — roughly seven
to 80% mastery of a knowledge component (corpus K1, Koedinger et al. 2023) — and a time-based
model of learning "systematically provides poor predictive fit."

### 1.3 Monitoring

This is the keystone and it gets §2 to itself. The summary position: **the system detects
stuck-ness before the learner does, from behaviour alone, and never asks.**

The number that forces this: after **three consecutive errors on a step**, a student's next action
was a hint request only **34%** of the time (Aleven & Koedinger 2000, Geometry Cognitive Tutor
logs); and students viewed **68%** of hint levels prior to the last for **under one second**
(Aleven & Koedinger 2001). `OBSERVED`. The learner who most needs the help is the learner who
least often asks for it, and the learner who does ask most often mines the answer.

**What it must never do**, stated here because it constrains §2's whole architecture.

- Never ask "are you stuck?" That question requires precisely the function that is missing, and
  it converts a behavioural signal into a self-report, which is a downgrade in both accuracy and
  legality.
- Never infer, label, name, store, or act on an emotion. §2.2.
- Never show the learner the stall score. A visible risk score is a judgement, and a judgement
  invites the learner to manage the score.

### 1.4 Shifting

The most neglected of the four, and the one with the cleanest measured target.

**What the system observes.** The wheel-spinning signature. **Beck & Gong (2013)**, AIED, define
it operationally: students who "practiced the same skill set over 10 times but failed to submit
correct answers three times in a row." `OBSERVED` for the threshold; the paper's own prevalence
figure is publisher-closed and **UNVERIFIED**. **Wan & Beck (2015)**, EDM, ERIC ED560558, on
ASSISTments data: "students in the **bottom 20% of pre-required knowledge exhibited wheel spinning
behavior 50% of the time**, while those in the **top 20%** … exhibited it **only 10% of the
time**." `OBSERVED`. Adding prerequisite performance to the detector moved R² 0.264 → 0.268 and
AUC 0.884 → 0.888.

Two things that reading gives a builder. The 5× differential is the target: **50% → 10%** is a
named, measured gap, and closing it is a testable product claim. And the tiny AUC gain from
adding prerequisite state says prerequisite state is not a new signal so much as a re-description
of what knowledge tracing already carries — so the shifting detector is cheap.

**Caveat carried from K1, and it is not small.** **Zhang et al. (2019)**, EDM, ERIC ED599222:
"two prominent criteria for wheel spinning **diverge substantially**." The construct is not
measured consistently across papers, so prevalence figures are non-comparable and this
specification fixes one criterion (Beck & Gong's) by fiat rather than by evidence. `SPEC`.

**What it does.** `SPEC`. On the wheel-spin trigger, the system does **not** deliver a hint. It
suspends the knowledge component, delivers a structurally different representation of the same
component, and re-queues the original behind a prerequisite probe. The reason it is not a hint:
**Roll et al. (2014)**, EDM, via Aleven et al. (2016) — "When students have a **medium level of
skills**, hints do have beneficial effect … When students have a **low or high level of skill,
attempts at solving (without help) are more effective**." `OBSERVED`. A learner at the wheel-spin
threshold is, by construction, at low skill on that component. A hint is the wrong object.

The "structurally different representation" is where the cost lives, and it should be stated
plainly: this is a content obligation, not a modelling one. Every knowledge component needs at
least two representations that are not paraphrases of each other. The corpus supplies the
criterion for what counts as different — **case comparison d = 0.50 [0.44, 0.56]**, 57 experiments
/ 336 tests (Alfieri, Nokes-Malach & Schunn 2013), with only four of fifteen moderators reliable,
one of which is that the principle is presented **after** the comparison.

**What it must never do.**

- Never shift on a single error, or on two. The threshold is ten opportunities, and it is high on
  purpose.
- Never present the shift as a verdict. The system's copy at this moment describes the object,
  not the learner: *"Here is the same idea drawn differently"*, never *"This isn't working for
  you."*
- Never shift twice within one knowledge component without escalating out of it entirely. A
  second failed representation is a prerequisite problem, and prerequisite state is the 3.6×
  term in the time-to-mastery decomposition (corpus K1).

**How you would know it worked.** Wheel-spin rate in the bottom prerequisite quintile, tracked
against the 50% baseline, with the top quintile's 10% as the target. This is the single most
concrete endpoint in the document because both numbers are measured and published.

---

## 2. The detector — specified hardest

Everything else in this document depends on this section. If the detector does not work, the
interruption policy has nothing to fire on, the fading schedule has no evidence to act on, and
the whole reframe reduces to a rearrangement of features.

### 2.1 What it must predict, and what it must not

The design move that makes the rest of it legal, cheap and honest is a change of target variable.

The existing literature builds detectors that predict **affective states** from interaction logs,
labelled by human observers. This document specifies a detector that predicts **behavioural
outcomes** from the same interaction logs, labelled by the log itself.

| | Affect detector (existing) | Stall detector (`SPEC`) |
|---|---|---|
| Target | Confusion, frustration, boredom, engaged concentration | Did this learner reach mastery on this KC within the next W opportunities; did the session end without a further submitted response |
| Label source | Trained human observers coding in classrooms | The log, W opportunities later |
| Label cost | Observer-hours; Baker et al. (2012) coded in situ | Zero |
| Label ceiling | Expert coders reach **κ ≈ 0.6–0.7** (Baker et al. 2012, verbatim) | None. The label is the ground truth, not a judgement about it |
| Legal exposure | EU AI Act Art. 5(1)(f) — the open question in F9 OP-19 | None on the emotion-inference ground. The system infers no emotional state |
| Actionability | "The learner is frustrated" → what? | "This learner will not master this KC in the next 10 opportunities" → intervene, or repair the prerequisite |

The features are, in large part, the same features. That is the crux, and it is the thing to be
precise about rather than to hide. §2.2 handles it directly.

### 2.2 The legal constraint, stated exactly

**EU AI Act Art. 5(1)(f)** prohibits the placing on the market, putting into service, or use of AI
systems to infer emotions of a natural person **in the areas of workplace and education
institutions**, with narrow exceptions for medical or safety reasons. Art. 3(39) defines an
emotion-recognition system, and Art. 3(34) defines biometric data. This is carried from F8, where
it was verified against `artificialintelligenceact.eu` (the AI Act text via EUR-Lex returned HTTP
202 with an empty body across two sessions). `VERIFIED` (statutory text, secondary rendering).

The unresolved question is F9's **OP-19**, restated here because it governs the architecture:
whether clickstream traces count as "behavioural characteristics" within Art. 3(34), and therefore
whether sensor-free affect detection in education is *prohibited* rather than merely high-risk.
F9's own statement of why it is hard is the sentence a builder should act on:

> "The boundary is **fuzzy by construction**: a model that predicts disengagement from latency and
> error patterns and a model that predicts 'frustration' from the same features may be the same
> model with a different label on its output."

`INFERENCE`. No authoritative construction was located; an arXiv census in F9 returned **one**
result for `abs:"emotion recognition" AND abs:"AI Act"`, a discussion paper.

**The design consequence, and it is not a hedge.** Because the boundary is drawn by the *output
label* and not by the input features, the compliant architecture is the one whose output is not an
emotion under any reading. So:

`SPEC` — **the emotion firewall.** Five rules, all mechanically checkable in CI.

1. **No affective label may appear anywhere in the pipeline.** Not as a target variable, not as an
   intermediate representation, not as a column name, not as a model name, not as a log field, not
   in UI copy, not in a system prompt to a language model that reads the state. A string match
   over the repository for `frustrat|bored|confus|anxious|engaged|affect|emotion|mood|sentiment`
   in model and telemetry code is a build-breaking check.
2. **No biometric input.** No camera, no microphone-as-sensor, no eye tracking, no keystroke
   dynamics used as a physiological signal, no pointer-velocity-as-arousal. This is stricter than
   the Act requires and it is stricter on purpose: it removes the entire class of arguments about
   whether a given signal is biometric.
3. **Every feature must be justifiable as task state.** The justification is written into the
   feature registry at definition time: *what task fact does this measure?* A feature whose only
   justification is that it correlates with a feeling is rejected at review. "Time since last
   action on this step" measures a task fact. "Hesitation" does not.
4. **Every output must be a behaviour with a future observable value.** `P(mastery within W)`,
   `P(session ends without another response)`, `P(wheel-spin)`. Each of these is resolved by the
   log within hours, which means every prediction the system makes is auditable against what
   actually happened. An emotion prediction is never resolvable in this way, which is a second,
   independent reason to prefer the behavioural target.
5. **No inference about the person.** Carried directly from N2 §5.7 and `CLAUDE.md` §3: the
   system may not diagnose or label a child. Every trigger is defined on within-learner task state.
   Response-time variability, in particular, is used **only** against the learner's own rolling
   baseline, never against a population norm — which is also the psychometrically correct use,
   since **Kofler et al. (2013)**, 319 studies, found adolescents and adults with ADHD
   **indistinguishable from clinical controls** on RT variability (children only **g = 0.25**
   against clinical controls, against **g = 0.76** against typical development). `MEASURED-META`.
   It is a good design signal and a bad diagnostic one, and rule 5 is what keeps it the former.

`OPEN` — **whether rules 1–4 are sufficient has no authoritative answer, and will not have one
until guidance or enforcement arrives.** *Why not:* it resolves through law, not experiment. The
position taken here is that a system predicting `P(mastery within 10 opportunities)` from response
latency is not an emotion-recognition system under any plain reading of Art. 3(39), and that the
same features feeding a model whose output is named "frustration" probably is. Builders in the EU
should get counsel; builders anywhere should adopt the firewall regardless, because the behavioural
target is better engineering.

### 2.3 The features

Grounded, wherever possible, in features that a published detector has already found predictive on
real tutor logs. **Baker, Gowda, Wixon, Kalka, Wagner, Salvi, Aleven, Kusbit, Ocumpaugh & Rossi
(2012)**, ED537205, recovered in full as PDF, lists the machine-selected features for each of its
four detectors. The features selected for **confusion** — the state closest to what this document
calls a stall — are quoted verbatim:

> "The percentage of clip actions involving actions taking longer than **5 seconds after two
> incorrect answers**. The percentage of actions in the clip that were **hint requests**. The
> **minimum number of previous incorrect actions** for any skill in the clip. The maximum product
> of the probability of guess P(G) as computed using contextual guess model, across sequences of
> three actions in a row. The average time the student took to respond, **unitized across time
> taken by all students on the same problem steps**, within sequences of five actions in a row
> that were correct."

`OBSERVED`. Every one of those is task state. None of them is biometric. The affective content of
that detector lives entirely in its label, which is exactly the point §2.2 makes.

The specified feature set, eleven features, each with its justification-as-task-state:

| # | Feature | Definition | Task fact it measures | Provenance |
|---|---|---|---|---|
| 1 | `latency_z` | Time since last action on this step, z-scored against the population distribution **for this step** | How long this step is taking relative to how long it takes | Baker et al. 2012 (unitized response time) |
| 2 | `post_error_latency` | Fraction of actions in the window taking > 5 s after two incorrect answers | Slowing down after failing | Baker et al. 2012, verbatim |
| 3 | `error_run` | Consecutive incorrect submissions on the current step | The Aleven & Koedinger trigger | Aleven & Koedinger 2000 (34%) |
| 4 | `edit_churn` | Input revisions before submission, and reverts to a previously-typed value | Changing the answer without new information | `SPEC` |
| 5 | `backtrack` | Navigations to an already-completed step in this problem | Re-reading what was already done | `SPEC` |
| 6 | `help_dwell` | Median seconds a help level is displayed before the next action | Whether help is read or mined | Aleven & Koedinger 2001 (68% under 1 s) |
| 7 | `help_avoidance` | Errors on this step ≥ 3 with zero help requests | The measured bottleneck itself, as a feature | Aleven & Koedinger 2000 |
| 8 | `spin_count` | Opportunities on this KC without three consecutive correct | Beck & Gong's criterion, live | Beck & Gong 2013 |
| 9 | `rt_var_self` | Rolling SD of response time on correct actions, against this learner's own 50-action baseline | Within-learner consistency | Kofler et al. 2013 (used non-diagnostically per §2.2 rule 5) |
| 10 | `prereq_state` | Mastery estimate on the KCs this step depends on | Whether the failure is here or upstream | Wan & Beck 2015 |
| 11 | `idle_state` | Boolean: no keystroke, pointer or scroll event for > 90 s | Present or absent | `SPEC`, see §2.5 |

Features 4, 5 and 11 have no published predictive validity in this setting and are `SPEC`. They
are included because they are cheap, because they are unambiguously task state, and because the
feature-selection step will drop them if they carry nothing. Features 1, 2, 6, 8 and 10 are drawn
from published detectors and carry `OBSERVED` support for their predictive value **on affective
and wheel-spin targets** — not on the behavioural target specified here, which no one has fitted.

**Excluded by construction**, and the exclusion list ships in the documentation: camera, microphone,
gaze, facial landmarks, prosody, keystroke pressure or rhythm as a physiological signal,
pointer-velocity-as-arousal, self-reported mood, personality inventories, and any demographic
attribute. The personality case is worth naming because a 2024 *IEEE TLT* paper (EJ1405383)
proposes adding Big Five traits to improve sensor-free affect detection; under this specification
that is prohibited twice over, as an affective target and as an inference about the person.

### 2.4 The model

`SPEC`. Two stages, because the two stages answer different questions and mixing them produces a
detector that cannot be interrogated.

**Stage 1 — the expectation.** A standard knowledge-tracing model (BKT or PFA; the choice does not
matter and F5 records that expert KC models add ≤ 0.01 AUC on 7 of 9 datasets) produces
`P(mastery)` per KC and, from it, an expected next-action correctness. This is the baseline
against which everything is a residual.

**Stage 2 — the stall estimate.** A gradient-boosted classifier over the eleven features plus the
Stage-1 expectation, predicting:

- `P_stall = P(this learner does not reach mastery on this KC within the next W opportunities)`,
  W = 10 by default, chosen to match Beck & Gong's threshold. `SPEC`.
- `P_abandon = P(this session ends without another submitted response within the next 3 actions)`.

Two outputs, not one, because they license different interventions. A learner who will not master
the KC but will keep working needs a strategy change. A learner who is about to leave needs the
session closed on a success, not a rescue.

**The requirement that matters more than accuracy: calibration.** An AUC-optimised detector is
useless for an interruption policy, because the policy in §3 compares a probability against a cost,
and a discriminative-but-uncalibrated score has no probability to compare. So:

- Report **expected calibration error** and a reliability diagram, per learner-decile and per KC-
  difficulty-tercile, alongside AUC and κ.
- The published claim about the detector is a calibration claim: *"of learners in this state, 71%
  did not master this KC within ten opportunities."* That sentence is checkable by anyone with the
  logs, and it is the sentence the interruption policy consumes.
- Cross-validate **at the student level**, never at the observation level. Baker et al. (2012) make
  this correction explicitly against earlier work, and it is the difference between a detector that
  generalises to new learners and one that memorises the ones it saw.

**What accuracy to expect, honestly.** The nearest published comparators, under student-level
cross-validation on Cognitive Tutor Algebra logs (Baker et al. 2012, Table 1):

| Detector | A′ | κ |
|---|---|---|
| Engaged concentration | 0.71 | 0.31 |
| Confusion | 0.99 | 0.40 |
| Frustration | 0.99 | 0.23 |
| Boredom | 0.69 | 0.28 |
| **Average across constructs** | **0.85** | **0.30** |

`OBSERVED`. And the authors' own framing: "These new features have only achieved **30% of potential
progress towards perfect detection**, and, while perfect detection is probably infeasible (after
all, even expert coders only achieve Kappa values around **0.6 or 0.7**), there is clearly
substantial room for improvement."

`INFERENCE` — **the behavioural target should beat these numbers, and the reason is the label, not
the model.** Those κ values are bounded above by the reliability of human affect coding. A label
read off the log W opportunities later has no such bound. The wheel-spinning literature, which
already predicts a behavioural target, reports **AUC 0.884–0.888** on ASSISTments (Wan & Beck
2015) — an order of usefulness above κ = 0.30, on a target of the same shape as the one specified
here. That comparison is the single strongest reason to believe this detector is buildable.

**The null that must be held alongside it.** **Zhang et al. (2022)**, EDM, ED624075: a previously
validated gaming detector, applied across conditions in algebra-tutor experiments, found that "the
detected gaming was **not associated with learning**, challenging its construct validity."
`OBSERVED`. A detector that fits its label and predicts nothing downstream is a real and documented
outcome in exactly this literature. The defence specified here is that the label *is* the
downstream outcome, so construct validity and predictive validity are the same quantity. A related
result cuts the other way and is worth carrying: **Zhang et al. (2022)**, ED624076, found gaming
detectors trained on data logs still predicting gaming **16 years later**, with a classic decision
tree holding up best. Detectors of behaviour in step-based tutors are durable objects.

### 2.5 The three ways this detector is wrong, and the gate for each

Named at design time, because a detector whose failure modes are discovered in production has
already interrupted several thousand people.

**(a) The fast-and-wrong learner looks calm.** Low latency, high error rate, no hesitation. Every
latency feature reads "fluent." This is the answer-mining profile, and it is the majority behaviour
in the founding data (68% of hint levels under one second). *Gate:* `P_stall` is computed on error
structure independently of latency; a submission rate above the 90th percentile with accuracy below
chance fires the stall regardless of latency. `SPEC`.

**(b) The slow-and-right learner looks stuck.** Deliberate, careful, long latencies, no errors. The
worst possible learner to interrupt, and the easiest to interrupt by accident. *Gate:* latency
features are gated on `error_run ≥ 1`. A long pause with no error is not a stall signal; it is a
learner thinking, and interrupting it is the highest-cost false positive in the system. This gate
matters more than any threshold in §3.

**(c) The absent learner.** No events for minutes. Every latency feature saturates. *Gate:* the
`idle_state` boolean. If no keystroke, pointer or scroll event has occurred for > 90 s, all
latency-derived features are set to missing and no intervention fires. Absence is not a stall.
When the learner returns, the resumption path is a re-entry item (N2 §4.4 row 9), not the pending
intervention. `SPEC`.

`SPEC` for the 90 s constant. It is chosen, not derived. The revision rule: set it at the
learner-population 95th percentile of *inter-action gaps that were followed by a resumed action*,
recomputed monthly. If the constant is right, roughly 5% of gates fire on a learner who was still
there.

### 2.6 Cold start

The personal baseline for feature 9 needs ~50 actions; the per-step population distributions for
feature 1 need ~30 learners per step. Before either exists:

- Use population priors only, with the operating threshold set high (§3.4) so the system
  intervenes rarely and on strong evidence.
- Never use a demographic prior. Not as a feature, not as a prior, not as a cohort assignment.
- Report the detector's own coverage: the fraction of decisions made with a full feature vector.
  A product that does not know when its detector is guessing is a product that will interrupt
  new learners most, which inverts the intent.

---

## 3. The interruption policy

If help must arrive unrequested, the interruption policy is the product. This section resolves a
real tension rather than routing around it, and the resolution comes from a coincidence in the
evidence that is worth stating before the machinery.

### 3.1 The tension, at full strength

**Productive struggle is an evidenced mechanism and interrupting it destroys the mechanism.**

- Problem-solving-before-instruction over instruction-first: **g = 0.36 [0.20, 0.51]**, 53 studies
  / 166 comparisons, publication-bias-corrected g = 0.87 (**Sinha & Kapur 2021**), with effect
  sizes reversing for grades 2–5 and for domain-general skills. `MEASURED-META`.
- **Roll, Baker, Aleven & Koedinger (2014)**, *Journal of the Learning Sciences*, 38 high-school
  students, Geometry Cognitive Tutor, two months of fine-grained logs, verbatim: "contrary to many
  help-seeking theories, **avoiding help (and failing repeatedly) is associated with better
  learning than seeking help on steps for which students have low prior knowledge**. These results
  suggest that novice learners may benefit from engaging in solution attempts before they can make
  sense of given assistance." `OBSERVED`.
- And the boundary condition from the same programme: "When students have a **medium level of
  skills**, hints do have beneficial effect on student learning within the tutor … When students
  have a **low or high level of skill, attempts at solving (without help) are more effective**."
  `OBSERVED` (Roll et al. 2014 EDM, via Aleven et al. 2016).

Read those together and the tension resolves into a shape rather than a compromise. **The value of
a correctly-timed intervention and the cost of interrupting productive struggle are anti-correlated
across the mastery axis, and both are functions of the same variable the system already estimates.**
Help is worth something in the middle band and worth nothing at the ends. Struggle is worth most at
the low end. The policy does not need to trade these off in the abstract; it needs to know where on
the mastery axis the learner is, which is the one thing knowledge tracing has been good at for
thirty years.

### 3.2 The firing rule

`SPEC`. An expected-value rule with three terms, each operationally defined.

```
FIRE  ⟺   P_stall · V(m)   >   (1 − P_stall) · C_int(m)   +   C_dep(a)

where
  m       = P(mastery) on the current KC, from Stage 1
  P_stall = the detector's calibrated output (§2.4)
  V(m)    = value of a correctly-timed intervention at mastery m
  C_int(m)= cost of terminating productive struggle at mastery m
  C_dep(a)= dependence cost of intervention of assistance-weight a
```

**V(m) — the value curve.** Zero below m = 0.35, zero above m = 0.75, peaked in between. This is
Roll et al.'s finding rendered as a function. The band edges are `SPEC` and the revision rule is
empirical: fit the observed next-opportunity-success gain from delivered interventions against m,
and set the band where the fitted gain crosses zero.

**C_int(m) — the struggle cost.** Highest at low m, declining with m. This is the Sinha & Kapur and
Roll etc. finding rendered as a function, and it has a corollary that is the most counter-intuitive
consequence in this document: **the learner who looks most stuck is the learner the system should
most often leave alone.** A learner at m = 0.15 with a five-error run and rising latency produces
the strongest possible stall signal, and the evidence says their repeated failure is doing work
that a hint would prevent. What that learner gets is not help and not silence; it is §1.4's
prerequisite probe, which is a different object with a different cost.

**C_dep(a) — the dependence cost.** The **−17%** term. **Bastani et al. (2025)**, *PNAS*,
`10.1073/pnas.2422633122`, ~1,000 high-school students across ~50 classrooms: unguarded GPT access
produced **+48%** on practice problems and **−17%** on the unassisted exam (β = −0.054, SE 0.022,
p < .05) against students who never had access; the pedagogically guardrailed variant produced
+127% on practice and **−0.004 (n.s.)** on the exam. `MEASURED-RCT`. Carried from B2, with B2's
own caveat that it rests on a single school in one country and has not been replicated, and with
the corpus correction on the record that the PNAS "correction" was an affiliation erratum and the
−17% stands.

`C_dep` is charged **per unrequested delivery, in proportion to assistance weight** (§4.2). A
complete answer delivered unrequested carries the full charge. A worked step that requires a
response before proceeding carries roughly a fifth of it. `SPEC` for the ratio; the revision rule
is §7's prosthetic gap, which measures the thing `C_dep` is a proxy for.

### 3.3 Timing — never mid-action

The rule and its cost are separate decisions and are separately specified.

`SPEC` — **the earliest legal firing moment is immediately after a submitted response, never during
input.** A learner mid-keystroke is mid-retrieval, and the retrieval is the mechanism.

The supporting literature is HCI rather than education, and it is cited for its structure rather
than its magnitudes, which could not be retrieved. **Adamczyk & Bailey (2004)**, *CHI*, "If not
now, when? The effects of interruption at different moments within task execution",
`10.1145/985692.985727`; **Iqbal & Bailey (2006)**, *CHI*, "Leveraging characteristics of task
structure to predict the cost of interruption", `10.1145/1124772.1124882`; **Iqbal & Bailey
(2008)**, *ACM TOCHI*, "Understanding changes in mental workload during execution of goal-directed
tasks and its application for interruption management", `10.1145/1314683.1314689`. `OBSERVED`;
**all magnitudes UNVERIFIED** — the ACM Digital Library deposits no abstracts to Crossref or
Semantic Scholar and no open copy was reachable. The structural claim used is that interruption
cost varies with position in task structure and is lowest at subtask boundaries. No number from
these papers is used.

Consequences of the rule:

- The intervention is delayed by up to one action. That is the cost, and it is accepted.
- Exception: the initiation gate at session start, where no task is in progress to interrupt.
- Second exception, and it is the only one that fires during input: the `P_abandon` output. If the
  detector predicts the session ends in the next three actions, the system may act before the next
  submission, and what it does is not help — it closes the session on the last success and writes
  the state card (§6.2). Ending well is a different act from rescuing.

### 3.4 The threshold, and how it adapts

`SPEC`. θ is not a constant and is not global.

**Initial value.** θ = 0.80, deliberately high. The system starts by intervening rarely. The
asymmetry is intentional: a missed intervention costs one stalled opportunity, and a wrongly-timed
intervention costs the mechanism plus a dependence charge plus the learner's trust in every
subsequent intervention.

**Adaptation.** Per learner, a one-armed comparison on a measurable outcome:

- Every intervention is followed by a measurement: the learner's success on the **next opportunity
  on the same KC, unassisted**.
- A matched counterfactual is assembled from *non-intervened* episodes at the same `P_stall` decile
  and the same mastery band — available for free, because θ = 0.80 means most stall episodes go
  un-intervened by construction, and those episodes are the control group.
- If the realised gain over the counterfactual is positive and stable across 20 episodes, lower θ
  by 0.05. If it is negative, raise θ by 0.10. Asymmetric, in the direction of intervening less.
- Floor θ at 0.50. Below that the system is guessing, and a system that intervenes on a coin flip
  is a nag with a model attached.

**The rate limit, which is not optional.** At most **one unrequested intervention per five
opportunities**, and at most **three per session**. `SPEC`. A well-calibrated detector on a
struggling learner will fire continuously; a budget is what converts a detector into a policy. The
budget refills only on evidence of benefit, so a learner for whom interventions do not help
converges to a system that leaves them alone — which is the correct behaviour and is not the
behaviour any deployed product exhibits.

**What is spent when the budget runs out.** Nothing is queued. An intervention that could not fire
is discarded and logged. The log of discarded interventions is itself a product metric: it is the
measure of how much stall the system is choosing to tolerate, and it should be published to the
team, never to the learner.

### 3.5 What the intervention actually is

The Help Tutor null is the reason this subsection exists. **Carnegie Mellon built a model-tracing
tutor for help-seeking itself** — roughly 80 production rules, a taxonomy of Help Abuse, Help
Avoidance and Try-step Abuse, real-time metacognitive feedback — and, from **Aleven, Roll, McLaren
& Koedinger (2016)**, *IJAIED* 26:205–223, verbatim:

> "We found that this feedback led to a **lasting improvement in help-seeking behavior, even months
> after the Help Tutor was turned off** … **However, we did not find improved domain-level learning
> due to feedback on help seeking.**"
>
> "**The main disappointment was that despite improvement in help-seeking behavior, the Help Tutor
> had no influence on students' domain-level learning outcomes.** … After years of agonizing and
> soul searching, we have come to view **this null result as interesting and important in its own
> right**."

`MEASURED-RCT` (null). N2 records the tension with the same team's 2010 abstract, which reported
transfer to new domain content; the 2016 retrospective is the considered position eleven years in
and is the one relied on.

The diagnosis in the same paper names what the intervention must therefore be:

> "principle-based hints during tutored problem solving may aid conceptual learning … For these
> beneficial effects to occur, **students must self-explain the hints or otherwise make sense of
> them, which however cannot be taken for granted**."

`SPEC` — **the intervention is a worked step with a required response.** Never a prompt to seek
help, never an invitation, never a text hint the learner can dismiss. Concretely:

1. One step of the solution is shown worked, with its principle named.
2. The next step is presented faded (§4), and the learner must submit it before proceeding.
3. A self-explanation prompt is attached to the worked step, in the constrained form the evidence
   supports rather than the open form it does not.

The warrant for step 3 and its boundary: **Bisra, Liu, Nesbit, Salimi & Winne (2018)**,
*Educational Psychology Review*, 69 effect sizes from 64 reports, overall **g = 0.55**;
`MEASURED-META`. And in digital environments specifically, **Yang et al. (2025)**, *Educational
Psychology Review*, three-level meta-analysis, 204 effect sizes / 56 studies: total **g = 0.46**;
retention **0.31**, transfer **0.33**, immediate **0.45**, delayed **0.35**. `MEASURED-META`. The
bounding result: **Rittle-Johnson, Loehr & Durkin (2017)**, *ZDM*, on mathematics — prompted
self-explanation produces small-to-moderate immediate gains, but "evidence that self-explanation
reliably promotes learning **within a classroom context** or **retention of knowledge over a
delay** is much more limited," with the effect stronger when high-quality explanation is
**scaffolded** rather than merely requested. `MEASURED-META`. So the prompt is structured
(select the principle that justifies this step, from four options) rather than open ("explain why").

And the delivery-format constraint, from **Van der Kleij, Feskens & Eggen (2015)**, *Review of
Educational Research*, 40 studies / 70 effect sizes: elaborated feedback **0.49**, correct-response
feedback **0.32**, knowledge-of-result-only **0.05**; effect sizes "negatively affected by delayed
feedback timing and by primary and high school." `MEASURED-META`. The intervention is elaborated
and immediate. Knowledge of result alone is worth 0.05 and is not an intervention.

### 3.6 The false-positive accounting

Stated as a table, because "false positive" means four different things here and they have
different costs.

| Type | What happened | Cost | Detection |
|---|---|---|---|
| **Struggle termination** | Fired on a learner whose repeated failure was productive | The mechanism. Highest cost in the system, and invisible until a delayed test | Matched-counterfactual gain (§3.4) goes negative; and the delayed unassisted probe (§4.3) fails more often in intervened cohorts |
| **Thinking interruption** | Fired on a long pause with no error | Moderate. Breaks a retrieval | Gate (b) in §2.5 should make this rare; measure by the rate of interventions with `error_run = 0` |
| **Absence rescue** | Fired at someone who left the room | Near zero in learning terms; non-zero in trust terms | Gate (c); measure by interventions followed by no action for > 5 min |
| **Nagging** | Fired correctly, repeatedly, and the learner stopped reading | High and compounding. Converts a working detector into ignored furniture | Intervention→response-rate decay over a session; when it falls below 0.5, the budget halves |

The first row is the one that matters and the one that is hardest to see. It is the reason §8's
falsifiable claim has a delayed unassisted endpoint and not an in-session one.

---

## 4. Fading — the difference between a prosthetic and a crutch

The hardest design problem in the document, and the section where the evidence is least
comfortable. That discomfort is reported rather than smoothed, because a fading schedule presented
as settled would be the exact failure this repository has documented in others.

### 4.1 What the literature actually says about fading

Four results, and they do not agree.

- **Belland, Walker, Kim & Lefler (2017)**, *Review of Educational Research*, 144 experimental
  studies / 333 outcomes, computer-based scaffolding in STEM: overall **ḡ = 0.46**, and — verbatim
  — "scaffolding's influence on cognitive outcomes **did not vary on the basis of context-
  specificity, presence or absence of scaffolding change, and logic by which scaffolding change is
  implemented**." `MEASURED-META`. Fading, adding, and not changing at all were indistinguishable
  across 144 studies.
- **Belland, Walker, Olsen & Leary (2015)**, *Educational Technology & Society*, the pilot
  meta-analysis: computer-based scaffolding **g = 0.53**, and "studies with **no fading had higher
  effect sizes than studies with fixed fading**" — with fading or its absence explaining **30% of
  the variability** in outcomes. The authors' own conclusion is to "steer scaffold designers **away
  from fixed fading**." `MEASURED-META`.
- **Salden, Aleven, Schwonke & Renkl (2010)**, *Instructional Science*, one lab and one classroom
  experiment inside a Cognitive Tutor, comparing a standard tutor against example-enhanced versions
  with fixed or adaptive fading: "Both experiments provide evidence of **improved learning results
  from adaptive fading over fixed fading over problem solving**." `MEASURED-RCT`; **effect sizes
  UNVERIFIED** (Springer paywall; ERIC abstract only).
- **Nelson, Ziegler & Zhang (2021)**, *Educational Psychology*, ecological-validity test of faded
  worked examples, N = 135 undergraduates, four homework assignments over four weeks on Canvas:
  "students in the **problem-solving group outperformed those exposed to fading with self-
  explanation prompts**," with no difference between fading alone and self-explanation alone.
  `MEASURED-RCT` (reversal).

**How to read this honestly.** Fixed fading has failed twice, once in a meta-analysis where its
absence did better and once in a classroom where plain problem-solving beat it. Adaptive fading has
succeeded twice, in one lab, on one platform, with effect sizes this session could not verify. The
2017 meta-analysis, the largest of the four, finds no moderation by fading at all.

The design position that follows is narrower than "fade the scaffolds," and it is the one this
section specifies: **fade on unaided evidence, one support at a time, or do not fade.** A fixed
schedule is worse than no schedule by the only meta-analysis that compared them, and the case for
adaptive fading rests on two experiments from one group.

### 4.2 Assistance weight

`SPEC`. Every support in the system carries a declared weight in [0, 1], and the weight is the
central bookkeeping object of the whole design. It governs `C_dep` in §3.2, the fading order here,
and the Unaided Competence Estimate in §7.

| Support | Weight | Rationale |
|---|---|---|
| Complete answer delivered | 1.00 | The learner produced nothing |
| Bottom-out hint | 0.95 | Empirically the same thing (68% mined in under 1 s) |
| Worked step, no response required | 0.70 | Sense-making "cannot be taken for granted" |
| Worked step, response required | 0.35 | The learner produced the next step |
| Faded step (one blank) | 0.20 | Scaled by fraction of the step left blank |
| Principle named, no steps | 0.15 | Signalling, not solution |
| Prerequisite repaired, then retry | 0.00 | Different KC. Charges nothing here |
| Goal line / state card visible | 0.00 | Externalised memory, not externalised reasoning. §6 |

The last two rows carry the load of the distinction this section exists to draw. **Supplying memory
is free; supplying reasoning is charged.** A learner who can see the goal and the derivation so far
is not being given the answer; a learner who is shown the next step is. The whole argument for
externalisation in §6 rests on this row of the table being right, and it is `SPEC` — the assignment
of weight 0.00 to persistent state is a design assertion, and §8's falsifier tests it.

### 4.3 The five fading rules

**Rule 1 — remove only on unaided evidence.** A support may be faded only on the basis of
opportunities where that support was **absent or demonstrably unconsulted**. Assisted success never
counts toward the readiness estimate for the support that produced it. This is the rule that kills
the crutch dynamic at its root, and it is the rule that every deployed system violates, because
every deployed system's competence estimate is fitted to in-tutor performance with all supports
present.

**Rule 2 — one support at a time, backwards.** Fade the *last* step of a worked example first
(backward fading), then the second-to-last, and never fade two supports in the same window, because
a joint removal cannot be attributed when performance drops. The backward direction is Renkl and
Atkinson's; **Renkl, Atkinson & Große (2003)** report that combining fading with self-explanation
prompts "produced medium to large effects on near and far transfer **without requiring additional
time on task**." `MEASURED-RCT`; effect sizes elided in the ERIC abstract and **UNVERIFIED**.

**Rule 3 — the probe is the evidence, and it is budgeted.** Readiness to fade is measured by a
deliberately unassisted opportunity whose only purpose is measurement. Three constraints:

- **Rate:** ~10% of opportunities, per KC. `SPEC`.
- **Placement:** never on an item that counts toward anything the learner can see as a score, and
  never as the first item of a session (§5's first-block rule owns that slot).
- **Framing:** the learner is not told it is a probe. Telling them converts it into a test, and the
  measured quantity is unaided competence, not test-taking behaviour.

The probe costs accuracy. That cost is the price of an honest estimate and it is the single line
item that a product manager will want to delete. It is also, per §7, the only thing that makes the
central metric mean anything.

**Rule 4 — asymmetric restoration.** If a probe fails, the support returns **immediately** and
returns **one level below where it was**, not at its original level. Fade slowly, restore fast, and
restore partially. The asymmetry exists because a failed probe is evidence about a specific step,
not about the learner's need for the whole scaffold, and restoring the full scaffold discards the
progress that the fade had already validated.

**Rule 5 — the faded-too-late signals.** Two, and they are the ones nobody instruments:

- **Zero consultation.** Every support carries a usage counter. A support present for 20
  opportunities and consulted zero times is either invisible or unneeded. Both conclusions say
  remove it, and which one it is can be settled by removing it and watching.
- **The expertise-reversal crossing.** When a learner's median time-per-opportunity is **shorter
  without** the support than with it, the support has become the load. That crossing is the
  measurable moment expertise reversal predicts, and it is directly observable from the probe
  stream, since probes generate the unassisted arm for free. This is `SPEC` as an operational
  trigger; the underlying effect is the corpus's F10 material, and **Kalyuga's** work is the
  standard reference.

**And the moderator to respect.** **Ziegler, Nelson & Zhang (2026)**, *British Journal of
Educational Psychology*, N = 114 sixth-graders on ASSISTments, four conditions (worked examples
with self-explanation, fading with self-explanation, fading, problem-solving only): "fading
demonstrat[ed] the largest effect sizes from pre to posttest. Further, **only prior knowledge
moderated the effect of fading**" — working memory did not. `MEASURED-RCT`. Fade on the knowledge
estimate. Do not fade on anything that looks like a capacity estimate, which is also what §2.2
rule 5 requires for unrelated reasons.

### 4.4 What would show the fading spec is wrong

Three falsifiers, in increasing order of how much they would cost.

1. **If unaided-evidence fading does not beat fixed fading** on a delayed unassisted test, at
   matched total assistance, then Rule 1 is bureaucracy and the cheaper fixed schedule wins.
2. **If the probe budget does not improve the calibration of the competence estimate** — measured
   as the gap between predicted and realised unassisted performance at the delayed test — then the
   probes are costing accuracy and buying nothing, and they should be replaced by the far cheaper
   expedient of one unassisted block per week.
3. **If assigning weight 0.00 to persistent externalised state is wrong** — that is, if learners
   with the goal line and state card visible throughout show the same post-removal decline as
   learners given worked steps — then §4.2's central distinction collapses, §6 is supplying
   reasoning while claiming to supply memory, and the entire externalisation argument needs
   rebuilding on a different basis. This is the falsifier most likely to fire.

---

## 5. The ADHD-specific specification

**Standing constraint, restated.** Per `CLAUDE.md` §3 and N2 §5, an AI may not diagnose or label a
child. Nothing below identifies anyone. Every parameter is applied universally, and every trigger
is defined on observable task state. The design serves a measured profile without assigning it.

### 5.1 What the profile actually is, and what it is not

The folk model — short attention span, therefore shorter lessons — is falsified by the best
available meta-analysis and it is worth restating the falsification because it is what makes this
section's design different from every "ADHD-friendly" redesign on the market.

**Huang-Pollock, Karalunas, Tam & Moore (2012)**, *Journal of Abnormal Psychology*, 47
continuous-performance-test studies. Overall omission errors **δ = 1.34** (k = 39, N = 3,192). The
vigilance decrement — performance *over time* — omissions **δ = 0.54, 80% credibility interval
−0.14 to 1.22**, crossing zero; commissions 0.24; reaction time 0.27; SD of reaction time 0.22.
The mechanism, from signal-detection and diffusion modelling in the same paper: perceptual
sensitivity **d′ = 2.68 vs 3.57, d = 0.98, p < .001**; drift rate **v = 0.18 vs 0.28, d = 0.75,
p = .001**; **response bias ln β: d = 0.04, n.s.** `MEASURED-META`.

Read as a design brief: the impairment is present **from the first block**, in the rate at which
evidence accumulates from each stimulus. It is not in a steeper decline across time. And it is in
*sensitivity*, not in *bias* — which means the lever is the quality of the evidence each item
supplies, not the threshold at which the learner decides.

Add the delay term, which is the largest clean effect in this literature: delay discounting
**d = 0.43**, 25 comparisons, N = 3,913, p < 10⁻¹⁵, no moderation by age or by real-versus-
hypothetical reward (**Jackson & MacKillop 2016**); choice impulsivity **g = 0.47**, N = 4,320
(**Patros et al. 2016**). `MEASURED-META`.

Two design parameters follow, and they are the two the brief names: **signal-to-noise per
opportunity**, and **delay-to-payoff**.

### 5.2 The first block, specified to the second

`SPEC` throughout. The first 90 seconds of a session, as a sequence with a budget.

| t | What is on screen | Budget | Why |
|---|---|---|---|
| 0 s | The app opens itself at the if-then cue, with item 1 rendered | — | Initiation is supplied, not requested (§1.1) |
| 0–10 s | Item 1: a two-alternative forced-choice discrimination on a KC already above 0.85 mastery, answerable in one click | **≤ 10 s to first answerable item** | The deficit is in the first block. The first block must therefore be the highest-d′ item in the session, not a warm-up |
| ≤ 2 s after response | Correctness signal | **≤ 2 s action → payoff** | Delay discounting d = 0.43. Every architectural choice that lengthens this interval is a tax levied on this profile |
| 10–40 s | Items 2–4, same structure, ascending difficulty inside the mastered band | 3 opportunities | Acquisition is counted in opportunities (≈7 to 80% mastery); front-load the count |
| ~45 s | First visible unit of progress completes | **≤ 60 s to first completed unit** | Prospective payoff moved inside the discounting window |
| 45–90 s | The first *new* KC's prequestion, with a required guess | — | Guessing **g = 0.65** vs reading **g = 0.22** (St. Hilaire et al. 2024) |

The three budget numbers — 2 s, 10 s, 60 s — are `SPEC`. They are anchored, not derived: the 2 s
figure is set below any plausible perception of delay and is supported in direction by Van der
Kleij's finding that effect sizes are "negatively affected by delayed feedback timing"; the 10 s
and 60 s figures are chosen. The revision rule is empirical and cheap: A/B the budget against
session-completion and `opportunities_completed`, per budget, one at a time.

**The counter-intuitive part.** Item 1 has almost no instructional value. It is a two-alternative
discrimination on something the learner already knows. Its entire job is to convert an opened app
into a submitted response inside the delay window. A product manager will want that slot for
something valuable; giving it to something valuable is the mistake, because a valuable item is a
hard item and a hard item in the first block is where the measured deficit is.

### 5.3 Raising d′ per opportunity

Because the mechanism is sensitivity and not bias, the design target is the discriminability of
each item. Four moves, three of them evidenced and one `SPEC`.

1. **Contrast-controlled items.** Two options that differ in exactly one respect, on the diagnostic
   dimension, with every other dimension held identical. This is the perceptual-learning-module
   construction, and its results are the strongest in the corpus for fluency: **Kellman, Massey &
   Son (2010)**, algebraic transformations, solving time **~28 s → ~12 s**, preserved at two weeks,
   with learners never solving equations, only judging legality; **Ahmad et al. (2021)**, N = 83,
   at one month PALM accuracy **d = 0.89** and fluency **d = 1.16** against a lecture that retained
   accuracy (d = 0.44) and **not fluency**. `MEASURED-RCT`.
2. **Signalling.** An on-screen element that points at the target: **g = 0.43 [0.35, 0.50]**,
   k = 209 (Schneider et al. 2018, via Noetel et al. 2021). The best-evidenced single design act
   available, and it is a d′ intervention: it tells the learner which dimension is diagnostic.
3. **Remove competing referents, not decoration.** This is the move that separates this
   specification from every ADHD-friendly redesign, so it is stated at length in §5.4.
4. **Mastery gating, not clever sequencing.** **Kellman et al. (2023)**, CogSci: signal-detection-
   based *retirement criteria* mattered (**F(1,72) = 4.861, p = .031, ηp² = .063**) while
   signal-detection-based *sequencing* did **not** (**F(1,72) = 0.44, p = .509**). `MEASURED-RCT`.
   Spend the engineering on when to stop practising an item, not on what order to present items in.

### 5.4 What noise gets removed, and what does not

The removal list, in priority order, from the referential ordering in N2 §1.3.

**Remove first — elements carrying their own competing referent.** An interesting, self-contained,
irrelevant story. Measured at **g = −0.16** overall (Cheng et al. 2026 MASEM, 177 effect sizes / 50
studies) to **−0.43** when persistent (Sundararajan & Adesope 2020, k = 47), with the harm mediated
by **extraneous cognitive load only** — intrinsic and germane load do not mediate. `MEASURED-META`.
And the dose finding: **Wirzberger group (2025)**, *Applied Cognitive Psychology* — five seductive
details grouped into one interruption against five interspersed produced **no significant
difference**; the effect "might rather depend on the **amount** of seductive details presented than
the number of interruptions." `MEASURED-RCT`. Dose, not structure.

**Remove second — decisions the learner does not need to make.** Menus, settings panels, "choose
your path", difficulty selectors, and pacing controls. Each is an executive demand disguised as
respect for autonomy, and the pacing evidence says the disguise is expensive: system-paced
**g = 0.41** against learner-paced **g = 0.27** (p = .02), instructor-segmented **g = 0.41**
against learner-segmented **g = 0.20**.

**Remove third — deferred consequences.** Batched feedback, end-of-unit grading, weekly reports as
the primary signal. Each lengthens the action-to-payoff interval, and that interval carries
d ≈ 0.43–0.47.

**Do not remove — non-referential decoration.** This is the instruction that will be argued with,
so here is the evidence. Decorative animation against static: **g = −0.05 [−0.17, 0.07]**, k = 17,
against representational animation **g = 0.40 [0.34, 0.46]**, k = 59 (Höffler & Leutner 2007, via
Noetel). Decorative page furniture: **no significant effect on retention, transfer, or time**,
N = 95, 3×3 design (Rey 2012, *JEMH*). `MEASURED-META` / `MEASURED-RCT`. Non-referential decoration
is **inert**, not harmful.

And there is a positive reason to keep it. Emotional design moves learning at **d+ = 0.317–0.387**
(Brom, Stárková & D'Mello 2018, 33 samples, N = 2,924) and replicates at **g+ = 0.27–0.35** (Wong &
Adesope 2021) — while moving liking only **0.10–0.11** and leaving perceived effort flat
(**d+ = 0.051, p > .227**). The one affective variable that moves in line with learning is
**perceived difficulty, down 0.21**. `MEASURED-META`, twice, independently.

So the design target for the affective surface is **approachability**, not amusement, and stripping
a learning surface to grey austerity in the name of focus spends something that costs nothing and
buys the "looks like something I could do" effect. The austerity budget belongs entirely to
competing referents.

### 5.5 Session length is not a design parameter

Stated as a prohibition because it is the default every team reaches for. The vigilance decrement
crosses zero (δ = 0.54, 80% CV −0.14 to 1.22). The deficit is in the first block. Sessions
terminate on a **measured competence threshold**, not on a clock, and the reported endpoint is
`opportunities_completed`, never minutes.

The one thing an incentive layer is licensed to target: **within-session persistence**, per Dovis
et al. — and not with a tangible expected performance-contingent reward, which is the only kind
Dovis actually tested and the kind 128 experiments warn against. That tension is real, is
unresolved in the literature, and is not resolved here.

### 5.6 The read-aloud default

The one accommodation with a differential-boost finding in ADHD is read-aloud — two randomised
experiments in younger students (**Lovett & Nelson 2021**, *JAACAP*, 510 documents screened, 68
included: "most accommodations fail to show evidence of benefits that are specific to students with
ADHD … **An exception is read-aloud accommodations**"). `MEASURED-META`.

`SPEC` — **read-aloud is on by default, for everyone, with no eligibility determination.** It is
free in software, universal, and stigma-free. Extended time is mandated where an IEP requires it,
must be provided, and must not be described to a family as an intervention known to work — three
independent failures, one in the wrong direction (Lovett & Leja 2015: more symptoms → *less*
benefit).

---

## 6. Externalise, do not train

Working-memory training does not transfer. That is settled in this repository (§1's three
meta-analyses) and it is the tempting wrong answer because it is the one that sounds like helping.
What follows is what externalising actually means as an interface, with the test each element must
pass before it earns screen space.

### 6.1 The three tests

An externalised element reduces load only if it passes all three. `SPEC`, built on N2 §1.3's
referential ordering.

**Test 1 — referential.** The element names a referent inside the target schema, or points at one.
An element with no referent is inert (costs nothing, buys nothing, does not belong on a surface
that is supposed to be doing work). An element with a *competing* referent harms in proportion to
dose, and persistence is the dose multiplier — which means a persistent surface is exactly where a
competing referent is most expensive. The canvas is the highest-risk real estate in the product.

**Test 2 — substitution.** The element replaces something the learner would otherwise hold in
working memory. It does not introduce something the learner would otherwise never have had to
track. A note that creates a new obligation is a second referent wearing a helpful costume, and it
fails this test no matter how relevant it is.

**Test 3 — contiguity.** The element sits adjacent to the thing it describes. Spatial contiguity is
one of the largest effects in the multimedia corpus (g in the 0.6–0.8 band via Noetel et al.'s
review of reviews). A state card on a second screen, in a collapsible panel, or behind a tab is not
a substitution; it is a new element with a retrieval cost attached, and it fails.

### 6.2 The four surfaces

`SPEC`. Four, and the number is a constraint rather than a starting point.

**(1) The goal line.** One sentence. In the learner's own words, captured once at KC entry and not
rewritten by the system into curriculum language. Always visible. Updated only at KC boundaries.
This is signalling (g = 0.43) applied to the learner's own objective, and its job is N2 §4.4 row 3:
holding the goal while working, which is otherwise a working-memory maintenance task the learner
performs continuously and silently.

**(2) The state card.** Four fields, written by the system, never by the learner:

```
GOAL      what we are trying to do          (from the goal line)
LAST      the last thing you did            (verbatim, the learner's own input)
NEXT      the next thing to do              (one action, imperative)
OPEN      the question still outstanding    (the current prequestion, unanswered)
```

Continuously written, so it survives an interruption of arbitrary length. This is the object that
makes N2 §4.4 rows 8 and 9 possible — sustaining across an interruption, and resuming after a
break. It also makes the segmentation finding affordable: segmented content teaches better and
**takes longer** (g = 0.92), and the time is spent in the gaps between segments, which is precisely
where state is lost.

The `LAST` field carries the learner's own input verbatim, not a paraphrase. A paraphrase is a
second referent for the same fact and the learner has to map between them.

**(3) The worked ledger.** Every step the learner has taken on the current problem, in the
learner's own notation, scrollable, never cleared mid-problem. The thing being externalised is the
*derivation*, and the derivation **is** the target schema, so this surface passes Test 1 by
construction. That is why it is the least risky of the four and should be the largest.

**(4) The open-loop list.** Every question asked and not yet answered. Maximum three items,
hard-capped. This externalises prospective memory. The cap is what keeps it from becoming a to-do
list, and a to-do list fails Test 2 the moment it contains anything the learner was not already
tracking.

### 6.3 Why this reduces load rather than adding it

The mechanism is Test 2 and it is worth being precise about, because "externalise working memory"
is the kind of phrase that survives without a mechanism attached.

Each of the four surfaces holds a fact the learner was already holding. The goal, the last action,
the next action, the outstanding question, the derivation so far. Rendering them does not add
elements to the learner's world; it moves elements from an unreliable store to a reliable one. The
cost of the move is a small, constant visual-search cost, paid at contiguity, and the saving is the
continuous rehearsal the learner was doing to keep those facts alive.

The failure mode is precise and is the thing to watch for in review: **a surface that holds a fact
the learner was not already holding is not an externalisation.** A "related concepts" panel, a
progress-toward-goal meter, a peer-comparison bar, a suggested-next-topic card — each of these adds
a referent. Under the seductive-details mediation result (harm travels through extraneous load
only), each of them is charged to exactly the account the design exists to protect, and persistence
multiplies the charge.

### 6.4 The canvas is written by the system

`SPEC`, and it is the rule most likely to be violated by a product team that likes note-taking
features. **The learner reads the canvas; the learner does not maintain it.** A canvas the learner
must keep current is a new executive demand — organisation, prospective memory, self-monitoring —
introduced by the very component that exists to remove executive demands.

The supporting pattern from the ADHD literature is consistent enough to be worth stating:
organisational-skills training reliably improves organisation and does not move academic outcomes.
**Nissley-Tsiopinis et al. (2024)**: organisational deficits **d = 0.96–1.20**, "effects on
academic measures were **not significant**." **Langberg et al. (2012)**, the HOPS intervention:
parent-rated **d = .63–1.05**, **teacher ratings not significant**. **DuPaul, Eckert & Vilardo
(2012)**, 60 studies / 85 effect sizes: behaviour **0.18 n.s.**, academic **0.43 n.s.**
between-subjects. `MEASURED-META` / `MEASURED-RCT`. Teaching a learner to maintain an external
system teaches them to maintain an external system.

The learner may annotate. Annotation is optional, never load-bearing, and never a prerequisite for
anything the system does next.

---

## 7. The thing nobody has built

One swing.

### 7.1 The Unaided Competence Estimate, and the prosthetic gap

**The observation it is built on.** Every deployed learner model estimates performance *inside the
tutor*. Knowledge tracing's outcome variable is next-step correctness within the environment, with
all scaffolding present, all hints available, all state externalised. That is, by construction, an
**assisted** measure. The entire field's central instrument measures the learner-plus-system, and
reports it as a property of the learner.

Bastani's **−17%** is what that gap looks like when someone finally measures it: an assisted
estimate meeting an unaided reality, once, at the end, by removing the tool. The measurement
happened after the intervention was over, on a single cohort, in a single school. Nobody measures
it continuously, and nobody measures it per learner, and nobody uses it to steer.

**The artifact.** `DESIGN`.

1. **Every opportunity is logged with the assistance weight present at the time** (§4.2's table).
2. **The competence estimate is assistance-discounted.** An opportunity's contribution to the
   Unaided Competence Estimate for a KC is scaled by (1 − a). A step solved after a bottom-out hint
   contributes 0.05 of an opportunity. A step solved with the goal line and state card visible
   contributes a full opportunity, because §4.2 assigns externalised memory weight 0.00 — and that
   assignment is the design's most exposed assertion.
3. **~10% of opportunities are unassisted probes** (§4.3), which exist solely to keep the estimate
   honest and to supply the unassisted arm for the fading rules and the expertise-reversal
   crossing.
4. **The system publishes one scalar per learner, continuously: the prosthetic gap.**

```
prosthetic_gap  =  assisted_competence  −  unaided_competence     (per KC, and pooled)
```

**What the gap means, and why it is the right object.** A prosthetic keeps the gap flat or shrinking
while both terms rise. A crutch grows it: assisted competence climbs, unaided competence does not,
and the learner is on a trajectory to Bastani's −17% without anyone knowing until the tool is taken
away.

That is the operational difference between a prosthetic and a crutch, it is measurable **during**
use rather than only after removal, and it is measurable per learner rather than per cohort.

### 7.2 Why nobody has built it

Three reasons, and none of them is that it is hard.

- **The instrument does not exist because the incentive does not.** No vendor benefits from
  publishing a number that goes up when their product is creating dependence. Engagement,
  completion, time-on-task and in-product gain all move in the flattering direction under exactly
  the conditions that grow the gap.
- **The probes cost measured accuracy.** ~10% of opportunities delivered without support will
  depress every in-product metric a team currently reports. The probe budget is the first thing
  cut in any optimisation pass, and it is the only thing that makes the metric mean anything.
- **The field's measurement tradition has nowhere to put it.** F9's OP-3 records the parallel gap:
  every instrument in the field operationalises executive function as a property of a *person*, and
  there is no validated instrument that scores an *interface* for what it charges its user. The
  prosthetic gap is the same category of missing object, one level down: a measure of what the
  learner can do *without* the thing measuring them.

### 7.3 What would show this was the wrong design

**It is wrong if the prosthetic gap does not predict post-removal performance.** The test is direct
and cheap: in any cohort that experiences a removal — end of term, end of licence, a deliberate
withdrawal week — regress post-removal unassisted performance on the gap, controlling for assisted
competence and prior knowledge. If the gap adds no incremental predictive validity over assisted
competence alone, then assistance-discounting is elaborate bookkeeping and the simple estimate
should be used.

**It is also wrong if the gap is a re-description of the probe score.** If `prosthetic_gap`
correlates above ~0.9 with raw probe accuracy, then the whole assistance-weight apparatus is a
complicated way of saying "test them without help occasionally," and the correct product is a
weekly unassisted block, which costs almost nothing to build.

**And a third, which is the one that would hurt.** If the gap is stable across designs — if
supplying executive function externally does not change it relative to a system that supplies
nothing — then executive-function supply is not the variable that governs dependence, something
else is, and this document has specified the wrong machine correctly.

---

## 8. The falsifiable claim

**The claim.** A system that detects stall from behaviour and intervenes unrequested, under the
policy in §3 and the fading rules in §4, produces higher **unassisted, delayed** performance than
the same system with the same content and the same model where help is available on request.

### 8.1 The trial

| | |
|---|---|
| Design | Two-arm randomised, learner-level, same content, same knowledge-tracing model, same interface, same supports available |
| Arm A | Help available on request. Always visible, never unrequested. The shipping default of every conversational tutor and every ITS |
| Arm B | The interruption policy (§3): unrequested intervention inside the mastery band, under the expected-value rule, the rate limit and the adaptive threshold |
| Primary endpoint | **Accuracy under a time gate on untrained instances, at 4+ weeks, with the system removed** |
| Effect to beat | **d ≥ 0.25** |
| Secondary | Prosthetic gap trajectory; wheel-spin rate in the bottom prerequisite quintile (against the 50% baseline); `opportunities_completed`; session return rate |

The primary endpoint is chosen against the two failure modes this whole literature demonstrates. It
is **unassisted**, because Bastani's result says assisted performance and unassisted performance
move in opposite directions. It is **delayed**, because Roll et al.'s intervention changed behaviour
durably and learning not at all, and only a delayed measure separates those. It is on **untrained
instances under a time gate**, because Krasne et al. found raw accuracy declining at a 6–7 week
delay while correct-within-12-seconds did not, and fluency is what retains.

### 8.2 The prediction that makes it non-trivial

**Arm B must lose or tie on in-session accuracy, and must take longer per knowledge component.**

This is not hedging; it is the strongest available check on the comparison. The policy deliberately
withholds help exactly where struggle pays (low mastery), and the corpus is unambiguous that
designs which win on delayed transfer lose in-session:

- Contrasting cases: in-lesson worksheet **84.7% vs 91.8%, F(1,113) = 4.5, p = .037**, with delayed
  transfer **d = .33** (Schwartz, Chase, Oppezzo & Chin 2011).
- Segmentation: **g = 0.92** on time taken, while teaching better (Rey et al. 2019).

**If Arm B wins on in-session accuracy *and* on the delayed unassisted endpoint, the comparison is
broken** — most likely because Arm A was not a genuine on-request control, or because the delayed
test leaked into the training material. The result should not be believed.

### 8.3 Three cheaper tests, to run first

**Test 1 — the invocation counterfactual. Costs nothing but log access, and it tests the core claim
directly.** On existing logs from any step-based tutor: label stall episodes post hoc using the
Beck & Gong criterion; identify the subset where the learner did *not* request help; and measure
what happened next. Then compare against episodes where help *was* requested at the same mastery
band and stall level.

If un-helped learners recovered at the same rate as helped learners, **the recognition failure is
not costly**, the 34% is a statistic about behaviour rather than about outcomes, and the entire
reframe this document is built on is decorative. That would be a genuinely important result and it
is available today, on public datasets, without a trial.

**Test 2 — the calibration test.** Fit the §2 detector on any step-based tutor's logs against the
behavioural target. If it cannot beat the wheel-spinning literature's **AUC ≈ 0.88** on a target of
the same shape, the detector is not good enough to license unrequested interruption, and the
correct product is one that waits to be asked.

**Test 3 — the false-positive cost.** Within Arm B, compare intervened against matched
non-intervened episodes at the same `P_stall` decile and mastery band. If the intervened episodes
show *worse* unaided next-opportunity performance at low mastery — which is what Roll et al.'s
help-avoidance finding predicts — then the mastery-band gate in §3.2 is set wrong, and it is
recoverable by moving the band rather than abandoning the design.

### 8.4 The most likely way this fails

Stated plainly because the corpus supplies the precedent. **Arm B moves behaviour and not learning.**
Fewer stalls, more help consumed at the right moment, better help-seeking, lower wheel-spin rate,
and a flat delayed unassisted endpoint. That is exactly the Help Tutor result with better
instrumentation, and it is the outcome the null in N2 §4.3 predicts for any intervention that
repairs one executive demand in isolation.

The specific defence this design mounts against that outcome is that it repairs the demand
*and supplies the content*: the intervention is a worked step with a required response and a
structured self-explanation, not a prompt to seek help. Whether that is sufficient is exactly what
the trial tests, and there is no evidence either way, because the combination has not been built.

---

## 9. Nulls and negative results that constrain this design

Every one of these makes the specification narrower rather than wider.

| # | Result | Numbers | Constraint it imposes |
|---|---|---|---|
| 1 | **Fixing help-seeking behaviour did not improve learning** | Lasting behaviour change months after removal; "we did not find improved domain-level learning" (Aleven et al. 2016) | §3.5: the intervention must deliver content with a required response, not a prompt to seek help |
| 2 | **Hints do not help at low or high skill** | Help helps only at intermediate skill; at low or high, attempting without help was more effective (Roll et al. 2014 EDM) | §3.2: the mastery-band gate. The whole firing rule |
| 3 | **Help avoidance beats help seeking at low prior knowledge** | "avoiding help (and failing repeatedly) is associated with better learning than seeking help on steps for which students have low prior knowledge" (Roll et al. 2014, JLS, N = 38, 2 months) | §3.1: C_int(m) is highest where the stall signal is strongest |
| 4 | **Fixed fading underperformed no fading** | No-fading > fixed fading; fading or its absence explained **30%** of variability (Belland et al. 2015) | §4.1: no fixed schedules |
| 5 | **Fading did not moderate scaffolding's effect at all** | 144 studies / 333 outcomes: no variation by "presence or absence of scaffolding change, and logic by which scaffolding change is implemented" (Belland et al. 2017) | §4.3: fade on unaided evidence or do not fade. Fading is not a free win |
| 6 | **Faded worked examples lost to plain problem-solving in a classroom** | N = 135, four weeks, Canvas: problem-solving > fading-with-self-explanation (Nelson et al. 2021) | §4.4 falsifier 1 is a live possibility, not a formality |
| 7 | **Sensor-free affect detectors are barely better than chance** | Average **κ = 0.30**, A′ = 0.85; "30% of potential progress"; expert coders themselves reach only κ ≈ 0.6–0.7 (Baker et al. 2012) | §2.1: change the target variable. The label ceiling is the binding constraint, not the model |
| 8 | **A validated gaming detector's output was not associated with learning** | "the detected gaming was not associated with learning, challenging its construct validity" (Zhang et al. 2022, ED624075) | §2.4: the label must *be* the downstream outcome, so construct and predictive validity coincide |
| 9 | **Training an executive function does not transfer to untrained ones** | **g = 0.11, k = 17, p = .11** (Kassai et al. 2019); training attention did not improve attention (Rapport et al. 2013) | The entire premise: supply, never train |
| 10 | **ADHD is not primarily a deficit in sustaining over time** | Vigilance-decrement omissions **δ = 0.54, 80% CV −0.14 to 1.22** against overall omissions δ = 1.34 (Huang-Pollock et al. 2012) | §5.5: session length is not a design parameter |
| 11 | **Organisational-skills training teaches organisation, not achievement** | Organisational deficits d = 0.96–1.20, academic measures **not significant** (Nissley-Tsiopinis et al. 2024); teacher ratings n.s. (Langberg et al. 2012) | §6.4: the system maintains the canvas, not the learner |
| 12 | **Self-explanation's classroom and delayed evidence is much weaker than its lab evidence** | Small-to-moderate immediate gains; "evidence that self-explanation reliably promotes learning within a classroom context or retention over a delay is much more limited" (Rittle-Johnson et al. 2017) | §3.5: the prompt is structured and constrained, not open |
| 13 | **Knowledge-of-result feedback is worth almost nothing** | KR **0.05** against elaborated **0.49**, correct-response **0.32** (Van der Kleij et al. 2015) | §3.5: "correct/incorrect" is not an intervention |
| 14 | **Confusion induction alone did not produce learning gains** | "The contradictions alone did not result in enhanced learning gains" (D'Mello et al. 2013, IJAIED) | Manufacturing difficulty is not the same as supplying the function to work through it |
| 15 | **The wheel-spinning construct is not measured consistently** | "two prominent criteria for wheel spinning diverge substantially" (Zhang et al. 2019) | §1.4: the criterion is fixed by fiat here, and prevalence figures across papers are non-comparable |

---

## 10. Limitations

The detector has not been fitted. Every performance expectation in §2 is an extrapolation from
detectors fitted to a *different target* (affect, κ ≈ 0.30) or on a *different platform*
(wheel-spinning, AUC ≈ 0.88), and the claim that a log-derived behavioural label removes the
human-coding ceiling is an argument, not a result.

Three parameter families are chosen rather than derived, and are marked `SPEC` at each use: the
mastery band [0.35, 0.75]; the timing budgets (2 s / 10 s / 60 s); and the assistance weights in
§4.2, of which the assignment of 0.00 to persistent externalised state is the most consequential
and the least supported. Each has a stated revision rule from data, which is the most that can
honestly be offered for a number nobody has measured.

The fading evidence does not support the fading design as strongly as the design's prominence
implies. The largest meta-analysis finds no moderation by fading at all; the only positive result
for adaptive fading is two experiments from one group with effect sizes this session could not
verify.

The legal position in §2.2 is a construction, not a holding. Whether clickstream-derived inference
falls inside Art. 5(1)(f) has no authoritative answer, and the firewall is designed to be robust to
either resolution rather than to predict one.

And the load-bearing precedent is a null. Carnegie Mellon repaired the recognition failure, durably,
and domain learning did not move. This document's answer is that they repaired recognition without
supplying content, and that the combination is different. That answer has never been tested.

---

## 11. Bibliography

Ordered by first appearance. `†` marks sources whose full text was recovered and quoted verbatim in
this document; `‡` marks sources with numbers flagged **UNVERIFIED** at point of use. Sources
carried from N2 without re-retrieval are marked `[N2]`.

**Executive function, help seeking, and the diagnosis**

1. † Aleven, V., Roll, I., McLaren, B. M., & Koedinger, K. R. (2016). Help helps, but only so much: Research on help seeking with intelligent tutoring systems. *IJAIED*, 26, 205–223. `10.1007/s40593-015-0089-1`. `OBSERVED` + `MEASURED-RCT` (null) `[N2]`
2. Aleven, V., & Koedinger, K. R. (2000). Limitations of student control: Do students know when they need help? *ITS 2000*. `10.1007/3-540-45108-0_33`. `OBSERVED` `[N2]`
3. Aleven, V., & Koedinger, K. R. (2001). Investigations into help seeking and learning with a Cognitive Tutor. *AIED Workshop*. `OBSERVED` `[N2]`
4. † Roll, I., Baker, R. S. J. d., Aleven, V., & Koedinger, K. R. (2014). On the benefits of seeking (and avoiding) help in online problem-solving environments. *Journal of the Learning Sciences*. ERIC EJ1044739. `OBSERVED`
5. Roll, I., Aleven, V., McLaren, B. M., & Koedinger, K. R. (2010). Improving students' help-seeking skills using metacognitive feedback in an intelligent tutoring system. *Learning and Instruction*. `10.1016/j.learninstruc.2010.07.004`. `MEASURED-RCT` — tension with #1 reported in N2 §4.3 `[N2]`
6. Kassai, R., Futó, J., Demetrovics, Z., & Takács, Z. K. (2019). A meta-analysis of the experimental evidence on near- and far-transfer among children's executive function skills. *Psychological Bulletin*. `10.1037/bul0000180`. `MEASURED-META` (null) `[N2]`
7. Rapport, M. D., Orban, S. A., Kofler, M. J., & Friedman, L. M. (2013). Do programs designed to train working memory, other executive functions, and attention benefit children with ADHD? *Clinical Psychology Review*. `10.1016/j.cpr.2013.08.005`. `MEASURED-META` (null) `[N2]`
8. Westwood, S. J., Parlatini, V., Rubia, K., Cortese, S., & Sonuga-Barke, E. J. S. (2023). Computerized cognitive training in ADHD. *Molecular Psychiatry*. `10.1038/s41380-023-02000-7`. `MEASURED-META` (null) `[N2]`
9. Breitwieser, J., & Reinelt, T. (2026). The effectiveness of implementation intentions in children: A systematic review and meta-analysis. *British Journal of Psychology*. `10.1111/bjop.70065`. `MEASURED-META` `[N2]`
10. Guo, L. (2022). Using metacognitive prompts to enhance self-regulated learning and learning outcomes. *JCAL*. `10.1111/jcal.12650`. `MEASURED-META` `[N2]`
11. Jansen, R. S., van Leeuwen, A., Janssen, J., Jak, S., & Kester, L. (2019). Self-regulated learning partially mediates the effect of SRL interventions on achievement. *Educational Research Review*. `10.1016/j.edurev.2019.100292`. `MEASURED-META` `[N2]`

**Detectors, educational data mining, and the stall signal**

12. † Baker, R. S. J. d., Gowda, S. M., Wixon, M., Kalka, J., Wagner, A. Z., Salvi, A., Aleven, V., Kusbit, G. W., Ocumpaugh, J., & Rossi, L. (2012). Towards sensor-free affect detection in Cognitive Tutor Algebra. *EDM 2012*, ERIC **ED537205**, full text recovered as PDF. `OBSERVED`
13. Beck, J. E., & Gong, Y. (2013). Wheel-spinning: Students who fail to master a skill. *AIED 2013*, LNCS 7926. `10.1007/978-3-642-39112-5_44`. `OBSERVED`; prevalence **UNVERIFIED** ‡ `[K1]`
14. Wan, H., & Beck, J. E. (2015). Considering the influence of prerequisite performance on wheel spinning. *EDM 2015*, ERIC **ED560558**. `OBSERVED` `[K1]`
15. Zhang, Y., et al. (2019). Two prominent criteria for wheel spinning diverge substantially. *EDM 2019*, ERIC ED599222. `OBSERVED` `[K1]`
16. Zhang, J., et al. (2022). Item response theory-based gaming detection. *EDM 2022*, ERIC **ED624075**. `OBSERVED` (construct-validity null)
17. Zhang, J., et al. (2022). Evaluating gaming detector model robustness over time. *EDM 2022*, ERIC **ED624076**. `OBSERVED`
18. Kai, S., Almeda, M. V., Baker, R. S., Heffernan, C., & Heffernan, N. (2018). Decision tree modeling of wheel-spinning profiles. *JEDM*, ERIC EJ1183799. `OBSERVED` `[K1]`
19. Baker, R. S. J. d. (2009). Differences between intelligent tutor lessons, and the choice to go off-task. *EDM 2009*, ERIC ED539066. `OBSERVED`
20. Improving sensor-free affect detection by considering students' personality traits (2024). *IEEE Transactions on Learning Technologies*, ERIC EJ1405383. `OBSERVED` — cited as an approach this specification **prohibits**
21. Kofler, M. J., Rapport, M. D., Sarver, D. E., et al. (2013). Reaction time variability in ADHD: A meta-analytic review of 319 studies. *Clinical Psychology Review*. `10.1016/j.cpr.2013.06.001`. `MEASURED-META` `[N2]`

**Interruption timing**

22. Adamczyk, P. D., & Bailey, B. P. (2004). If not now, when? The effects of interruption at different moments within task execution. *CHI '04*. `10.1145/985692.985727`. `OBSERVED` ‡ (magnitudes UNVERIFIED — ACM deposits no abstract)
23. Iqbal, S. T., & Bailey, B. P. (2006). Leveraging characteristics of task structure to predict the cost of interruption. *CHI '06*. `10.1145/1124772.1124882`. `OBSERVED` ‡
24. Iqbal, S. T., & Bailey, B. P. (2008). Understanding changes in mental workload during execution of goal-directed tasks and its application for interruption management. *ACM TOCHI*. `10.1145/1314683.1314689`. `OBSERVED` ‡
25. Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems. *Computers in Human Behavior*. `10.1016/j.chb.2005.12.009`. `OBSERVED` ‡

**Scaffolding, fading, worked examples, self-explanation, feedback**

26. Belland, B. R., Walker, A. E., Kim, N. J., & Lefler, M. (2017). Synthesizing results from empirical research on computer-based scaffolding in STEM education: A meta-analysis. *Review of Educational Research*, ERIC **EJ1133348**. `MEASURED-META`
27. Belland, B. R., Walker, A. E., Olsen, M. W., & Leary, H. (2015). A pilot meta-analysis of computer-based scaffolding in STEM education. *Educational Technology & Society*, ERIC **EJ1062484**. `MEASURED-META`
28. Salden, R. J. C. M., Aleven, V., Schwonke, R., & Renkl, A. (2010). The expertise reversal effect and worked examples in tutored problem solving. *Instructional Science*, ERIC **EJ880294**. `MEASURED-RCT` ‡ (effect sizes UNVERIFIED — Springer paywall)
29. Nelson, et al. (2021). Testing the ecological validity of faded worked examples in algebra. *Educational Psychology*, ERIC **EJ1289301**, N = 135. `MEASURED-RCT` (reversal)
30. Ziegler, et al. (2026). Does working memory moderate the effect of fading on math performance? *British Journal of Educational Psychology*, ERIC **EJ1496086**, N = 114. `MEASURED-RCT`
31. Renkl, A., Atkinson, R. K., & Große, C. S. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. ERIC **EJ678596**. `MEASURED-RCT` ‡
32. Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F., & Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review*, ERIC **EJ1186664**. 69 ES / 64 reports, g = 0.55. `MEASURED-META`
33. Yang, et al. (2025). Enhancing academic performance through self-explanation in digital learning environments: A three-level meta-analysis. *Educational Psychology Review*, ERIC **EJ1461751**. 204 ES / 56 studies. `MEASURED-META`
34. Rittle-Johnson, B., Loehr, A. M., & Durkin, K. (2017). Promoting self-explanation to improve mathematics learning: A meta-analysis and instructional design principles. *ZDM*, ERIC **EJ1149060**. `MEASURED-META`
35. Van der Kleij, F. M., Feskens, R. C. W., & Eggen, T. J. H. M. (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: A meta-analysis. *Review of Educational Research*, ERIC **EJ1081708**. `MEASURED-META`
36. D'Mello, S., et al. (2013). Inducing and tracking confusion with contradictions during complex learning. *IJAIED*, ERIC EJ1190004. `MEASURED-RCT` (null on the main effect)
37. D'Mello, S., & Graesser, A. (2012). Confusion and complex learning during interactions with computer learning environments. *Internet and Higher Education*, ERIC EJ969230. `OBSERVED`
38. Koedinger, K. R., & Aleven, V. (2007). Exploring the assistance dilemma in experiments with Cognitive Tutors. *Educational Psychology Review*, ERIC EJ785065. `OBSERVED`

**Design principles, pacing, segmentation, referential status**

39. † Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., & Parker, P. D. (2021). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research*. `10.3102/00346543211052329`. `MEASURED-META` `[N2]`
40. Rey, G. D., Beege, M., Nebel, S., et al. (2019). Segmenting meta-analysis (numbers via Noetel). `MEASURED-META` `[N2]`
41. Schneider, S., Beege, M., Nebel, S., & Rey, G. D. (2018). Signalling meta-analysis (numbers via Noetel). `MEASURED-META` `[N2]`
42. Höffler, T. N., & Leutner, D. (2007). Instructional animation versus static pictures: A meta-analysis. *Learning and Instruction*. `MEASURED-META` `[N2]`
43. Rey, G. D. (2012). How seductive are decorative elements in learning materials? *JEMH*, ERIC EJ981639. `MEASURED-RCT` (null) `[N2]`
44. Cheng, C., Wu, Y., Wang, R., & Wang, Z. (2026). Seductive details, cognitive load, and learning outcomes: A multi-level meta-analysis and MASEM. *Educational Psychology Review*. `10.1007/s10648-025-10099-z`. `MEASURED-META` `[N2]`
45. Sundararajan, N., & Adesope, O. (2020). Keep it coherent: A meta-analysis of the seductive details effect. *Educational Psychology Review*. `10.1007/s10648-020-09522-4`. `MEASURED-META` `[N2]`
46. Wirzberger group (2025). Seductive details in learning text — grouped or interspersed? *Applied Cognitive Psychology*. `10.1002/acp.70065`. `MEASURED-RCT` `[N2]`
47. Brom, C., Stárková, T., & D'Mello, S. K. (2018). How effective is emotional design? *Educational Research Review*. `10.1016/j.edurev.2018.09.004`. `MEASURED-META` `[N2]`
48. Wong, R. M., & Adesope, O. (2021). Meta-analysis of emotional designs in multimedia learning. *Educational Psychology Review*. `10.1007/s10648-020-09545-x`. `MEASURED-META` `[N2]`

**Questions, struggle, comparison, perceptual learning**

49. St. Hilaire, K. J., Chan, J. C. K., & Ahn, D. (2024). Guessing as a learning intervention: A meta-analytic review of the prequestion effect. *Psychonomic Bulletin & Review*, 31, 411–441. `10.3758/s13423-023-02353-8`. `MEASURED-META` `[N2]`
50. Sinha, T., & Kapur, M. (2021). When problem solving followed by instruction works. *Review of Educational Research*. `10.3102/00346543211019105`. `MEASURED-META` ‡ `[N2]`
51. Schwartz, D. L., Chase, C. C., Oppezzo, M. A., & Chin, D. B. (2011). Practicing versus inventing with contrasting cases. *Journal of Educational Psychology*, 103(4), 759–775. `10.1037/a0025140`. `MEASURED-RCT` `[N2]`
52. Alfieri, L., Nokes-Malach, T. J., & Schunn, C. D. (2013). Learning through case comparisons: A meta-analytic review. *Educational Psychologist*. `10.1080/00461520.2013.775712`. `MEASURED-META` `[N2]`
53. Kellman, P. J., Massey, C. M., & Son, J. Y. (2010). Perceptual learning modules in mathematics. *Topics in Cognitive Science*. `10.1111/j.1756-8765.2009.01053.x`. `MEASURED-RCT` `[N2]`
54. Kellman, P. J., Krasne, S., Massey, C. M., & Mettler, E. (2023). Adaptive learning schedules in a skin-cancer perceptual learning module. *CogSci*, eScholarship qt83z22046. `MEASURED-RCT` `[N2]`
55. Ahmad, S., Ashraf, M., Kellman, P. J., Krasne, S., & Ramanathan, S. (2021). Ophthalmology PALM randomised comparison. `10.21203/rs.3.rs-806381/v1`. `MEASURED-RCT` `[N2]`
56. Krasne, S., Hillman, J. D., Kellman, P. J., & Drake, T. A. (2013). Perceptual and adaptive learning in introductory histopathology. *Journal of Pathology Informatics*. `10.4103/2153-3539.123991`. `MEASURED-RCT` `[N2]`

**ADHD, accommodations, and the withdrawal result**

57. Huang-Pollock, C. L., Karalunas, S. L., Tam, H., & Moore, A. N. (2012). Evaluating vigilance deficits in ADHD: A meta-analysis of CPT performance. *Journal of Abnormal Psychology*. `10.1037/a0027205`. `MEASURED-META` `[N2]`
58. Jackson, J. N. S., & MacKillop, J. (2016). ADHD and monetary delay discounting: A meta-analysis. *Biological Psychiatry: CNNI*. `10.1016/j.bpsc.2016.01.007`. `MEASURED-META` `[N2]`
59. Patros, C. H. G., Alderson, R. M., Kasper, L. J., et al. (2016). Choice-impulsivity in children and adolescents with ADHD. *Clinical Psychology Review*. `10.1016/j.cpr.2015.11.001`. `MEASURED-META` `[N2]`
60. Dovis, S., Van der Oord, S., Wiers, R. W., & Prins, P. J. M. (2012). Can motivation normalize working memory and task persistence in children with ADHD? *JACP*. `10.1007/s10802-011-9601-8`. `MEASURED-RCT` `[N2]`
61. Lovett, B. J., & Nelson, J. M. (2021). Systematic review: Educational accommodations for children and adolescents with ADHD. *JAACAP*. `10.1016/j.jaac.2020.07.891`. `MEASURED-META` `[N2]`
62. Lovett, B. J., & Leja, A. M. (2015). ADHD symptoms and benefit from extended time testing accommodations. *Journal of Attention Disorders*. `10.1177/1087054713510560`. `MEASURED-RCT` (negative direction) `[N2]`
63. Nissley-Tsiopinis, J., et al. (2024). Organizational skills training, tier 2. *Journal of Consulting and Clinical Psychology*. `10.1037/ccp0000909`. `MEASURED-RCT` `[N2]`
64. Langberg, J. M., Epstein, J. N., Becker, S. P., Girio-Herrera, E., & Vaughn, A. J. (2012). Evaluation of the HOPS intervention. *School Psychology Review*. `MEASURED-RCT` `[N2]`
65. DuPaul, G. J., Eckert, T. L., & Vilardo, B. (2012). The effects of school-based interventions for ADHD: A meta-analysis 1996–2010. *School Psychology Review*. `MEASURED-META` `[N2]`
66. Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning. *PNAS*. `10.1073/pnas.2422633122`. `MEASURED-RCT` `[B2]`

**Legal**

67. Regulation (EU) 2024/1689 (AI Act), Art. 3(34), Art. 3(39), Art. 5(1)(b), Art. 5(1)(f), Art. 26(11), Annex III(3)(b). Verified against `artificialintelligenceact.eu`; EUR-Lex CELEX:32024R1689 returned HTTP 202 with an empty body across sessions. `VERIFIED` (secondary rendering) `[F8, F9]`

**Carried from the corpus, not re-derived:** Koedinger et al. (2023) opportunities-to-mastery;
Cepeda et al. (2008) optimal spacing gap; Kalyuga et al. expertise reversal; Deci, Koestner & Ryan
(1999) tangible rewards; Sailer & Homner (2020) gamification moderators; Gervet et al. on KC-model
AUC; F5's Portable Learner Model schema; F9 OP-3 and OP-19.

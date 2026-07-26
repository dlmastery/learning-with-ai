---
title: "Motivation, persistence, and the attention economy — why learners quit, and whether AI changes it"
wave: F
section: F6
date_researched: 2026-07-25
sources_count: 76
---

# F6 — Motivation, Persistence, and the Attention Economy

> **The claim this section defends:** availability was never the binding constraint.
> Free, world-class, unlimited instructional content has existed at global scale for
> fourteen years and roughly 90–95% of the people who reach for it do not finish.
> An AI that only makes content *better* and *cheaper* is optimizing a variable that
> was already saturated. The binding constraint is **volitional continuation** — and
> the moment a system tries to solve that directly, it becomes an engagement-optimizer,
> which is a different and more dangerous product than a learning system.

---

## 0. Retrieval note

WebSearch was exhausted for this session. Retrieval was performed via Crossref REST,
Semantic Scholar Graph, Europe PMC, Unpaywall, arXiv (heavily rate-limited, partial),
and targeted `WebFetch`. OpenAlex was budget-exhausted by concurrent agents and
returned no results.

**Unreachable / unverified, flagged rather than guessed:**

- **Reich & Ruipérez-Valiente (2019), *Science*** — full text is paywalled (HTTP 403);
  the MIT DSpace green-OA handle resolves but the bitstream is not directly fetchable.
  Only the abstract and the S2-extracted summary were verified. The frequently-quoted
  per-year certification figures (e.g. "6% → 3.13%") could **not** be verified from
  primary text and are therefore **not asserted** below.
- **Jordan (2014)** — figures extracted from the OA PDF via `pdftotext`; the
  full completion-rate range table was not machine-extractable and is not quoted.
- **Vesselinov & Grego (2012)** Duolingo efficacy study — not retrievable through any
  API used; it survives here only as *cited by* Loewen et al. (2019), who label it
  "commissioned."

---

## 1. MOOC completion: the number, and the honest fight about the number

### 1.1 The headline figures, with primary sources

| Study | Sample | Completion | Source |
|---|---|---|---|
| Jordan 2014 | 91 courses (enrolment), 42 (completion) | **avg. 43,000 enrolled, 6.5% complete** | [10.19173/irrodl.v15i1.1651](https://doi.org/10.19173/irrodl.v15i1.1651) |
| Jordan 2015 | 221 MOOCs, n=129 with completion data | **median 12.6%, range 0.7%–52.1%** | [10.19173/irrodl.v16i3.2112](https://doi.org/10.19173/irrodl.v16i3.2112) |
| Henderikx et al. 2017 | 2 MOOCs, completion-based definition | **6.5% and 5.6%** | [10.1080/01587919.2017.1369006](https://doi.org/10.1080/01587919.2017.1369006) |
| Perna et al. 2014 | 16 Penn/Coursera courses | progression collapses at every stage; two user definitions (registrants vs. starters) give materially different rates | [10.3102/0013189X14562423](https://doi.org/10.3102/0013189x14562423) |

`MEASURED-BENCH` / `OBSERVED`

The famous "3–15%" band is real and is the correct order of magnitude. Jordan's
1,000-plus-citation pair is the canonical source and gives **6.5% (2014, smaller
sample) → 12.6% median (2015, larger sample)**. The upward drift between the two is
itself a finding: Jordan's regression found *start date* to be a significant positive
predictor, i.e. later courses completed better — 60% of variance explained
(R² = .60) by **start date + course length + assessment type**, with course length
negatively associated and **peer-graded courses completing worse than auto-graded**
courses. Total enrolment was *not* significant enough to retain in the final model
(2015), though the 2014 paper reported completion negatively correlated with enrolment.

`MEASURED-BENCH` — Jordan 2015.

### 1.2 The strongest single data point

Reich & Ruipérez-Valiente (2019, *Science*, 400+ citations) analysed HarvardX/MITx
edX data across six years and report three patterns:

1. **"The vast majority of MOOC learners never return after their first year."**
2. Growth in participation concentrated **almost entirely in the world's most affluent
   countries**.
3. **"The bane of MOOCs — low completion rates — has not improved over 6 years."**

[10.1126/science.aav7958](https://doi.org/10.1126/science.aav7958) — `OBSERVED`,
abstract verified, full text not retrieved.

Point (3) is the load-bearing one for this survey. Between 2012 and 2018 the field
shipped: better video, better platforms, mobile apps, adaptive sequencing, mastery
gating, cohorts, gamified progress, social forums, certificates, and paid verification.
**Completion did not move.** Point (2) additionally destroys the access narrative:
the marginal MOOC user was not an underserved learner in a low-income country; it
was an already-credentialed professional in a rich one.

### 1.3 The methodological rebuttal — and why it only partly works

The rebuttal is that completion is the wrong denominator, because most enrollees never
intended to complete. This is not a hand-wave; it is measured.

**Henderikx, Kreijns & Kalz (2017)** ran the same two MOOCs under two definitions:

- Traditional completion-based success: **6.5% and 5.6%**
- Intention-adjusted success (did the learner achieve *their own* stated goal?):
  **59% and 70%**

[10.1080/01587919.2017.1369006](https://doi.org/10.1080/01587919.2017.1369006) —
`MEASURED-BENCH`. This is a ~10x swing from a definitional choice.

**Kizilcec, Piech & Schneider (2013)** established the taxonomy that made this
tractable: learners cluster into four prototypical engagement trajectories —
*completing, auditing, disengaging, sampling* — which are not degrees of failure
but different products being consumed.
[10.1145/2460296.2460330](https://doi.org/10.1145/2460296.2460330) — 1,175 citations,
`OBSERVED`.

**Ferguson & Clow (2016)** attempted to replicate the four-cluster structure on
FutureLearn (a social-constructivist platform) and **failed to fully replicate it**,
finding that engagement patterns are shaped by pedagogy and learning design. Two
clusters were stable across platforms and re-runs: **samplers** and **completers**.
[10.18608/jla.2015.23.5](https://doi.org/10.18608/jla.2015.23.5) — `OBSERVED`,
documented partial-replication failure.

**Where the rebuttal fails.** It rescues MOOCs from the charge of *failure* but not
from the charge of *irrelevance to the persistence problem*. Reframing sampling as
success does not produce a single additional person who learned a hard thing they
could not previously do. And Reich & Ruipérez-Valiente's finding — that most learners
never return in the following *year*, across the whole platform, not one course —
is not a definitional artifact. You cannot intention-adjust your way out of
platform-level non-return.

> **Position.** The correct reading of the MOOC record is not "completion rates are
> misleading" and not "MOOCs failed." It is: **content supply was solved, and solving
> it moved almost nothing.** Any AI-native learning proposal whose theory of change is
> "better/cheaper/more personalized content" is proposing to push harder on the one
> lever that has already been pushed to exhaustion. `INFERENCE`

### 1.4 The nulls that should terrify anyone planning to fix this with a nudge

This is the most under-cited literature in edtech and the most important for this
section. Behavioural interventions to raise persistence **do not survive scaling**.

- **Kizilcec, Reich, Yeomans et al. (2020), PNAS.** ~250,000 students, **247 courses**,
  Harvard/MIT/Stanford, 2.5 years — one of the largest field experiments in education.
  Preregistered, iterative. Result: hypothesized medium-to-large effects **not
  supported**. *"Self-regulation interventions raised student engagement in the first
  few weeks but not final completion rates."* Value-relevance affirmation raised
  completion in developing countries **only in courses that had a global achievement
  gap**. State-of-the-art ML could not forecast where a gap would occur or learn
  effective individualized policies. Headline sentence:
  **"Scaling behavioral science interventions across various online learning contexts
  can reduce their average effectiveness by an order-of-magnitude."**
  [10.1073/pnas.1921417117](https://doi.org/10.1073/pnas.1921417117) — `MEASURED-RCT`.

- **Bird, Castleman, Denning et al. (2021), JEBO.** Two RCTs, **>800,000 students**,
  nudge campaigns patterned on successful local interventions. *"We find no impacts on
  aid receipt or college enrollment overall or for any subgroups. We find no evidence
  that different approaches to message framing, delivery, or timing, or access to
  one-on-one advising affected campaign efficacy."*
  [10.1016/j.jebo.2020.12.022](https://doi.org/10.1016/j.jebo.2020.12.022) —
  `MEASURED-RCT`, **null**.

- **Oreopoulos & Petronijevic (2023), *Economic Journal*.** Five years, ~20,000
  students, three campuses of virtual coaching. *"Some improvement on study time but
  no effect on academic outcomes."* Treated students correctly updated their beliefs
  about required effort and wanted better grades more — and it still did not translate.
  [10.1093/ej/uead064](https://doi.org/10.1093/ej/uead064) — `MEASURED-RCT`, **null**.

- **Kizilcec, Pérez-Sanagustín & Maldonado (2016).** *Recommending* self-regulated
  learning strategies in a MOOC **did not improve performance**.
  [10.1145/2876034.2893378](https://doi.org/10.1145/2876034.2893378) — `MEASURED-RCT`,
  **null**.

**The one robust positive.** Patterson (2018) built three tools and tested them in a
MOOC:

| Tool | Effect |
|---|---|
| **Commitment device** (learner pre-commits to a time budget) | **+24% time on course, +0.29 SD grades, +40% more likely to complete** |
| Alert tool | statistically indistinguishable from control |
| Distraction-blocking tool | statistically indistinguishable from control |

[10.1016/j.jebo.2018.06.017](https://doi.org/10.1016/j.jebo.2018.06.017) —
`MEASURED-RCT`, includes two documented nulls.

This asymmetry is the single most actionable finding in the section. **Being told
things does nothing. Being reminded does nothing. Being blocked does nothing.
Binding your own future self does a lot.** Commitment devices are the mechanism
Ariely & Wertenbroch (2002) established: self-imposed deadlines improve performance,
though not optimally-spaced ones
([10.1111/1467-9280.00441](https://doi.org/10.1111/1467-9280.00441)) — `MEASURED-RCT`.

The structural reason is worth naming: a commitment device is the *only* intervention
in this list that transfers **autonomy** to the learner instead of spending it. Every
other intervention is the system acting *on* the learner. See §2.

---

## 2. Self-determination theory: which of the three needs can a machine actually supply?

Ryan & Deci's framework (28,000+ citations,
[10.1037/0003-066X.55.1.68](https://doi.org/10.1037/0003-066x.55.1.68)) posits three
basic psychological needs whose satisfaction produces autonomous motivation:
**autonomy, competence, relatedness**. Chen & Jang (2010) tested the model
specifically in online learning and found the need-satisfaction → self-determination
→ outcomes path holds, though contextual support effects were weaker than predicted
([10.1016/j.chb.2010.01.011](https://doi.org/10.1016/j.chb.2010.01.011)) — `OBSERVED`.

Cerasoli, Nicklin & Nassrelgrgawi (2016) meta-analysed need satisfaction and
performance directly, finding all three needs positively associated with performance
([10.1007/s11031-016-9578-2](https://doi.org/10.1007/s11031-016-9578-2)) —
`MEASURED-META`.

### 2.1 Autonomy — AI is *structurally* the best autonomy-support technology ever built

**Verdict: AI can supply this, and it is the need conventional schooling most
systematically violates.**

Patall, Cooper & Robinson (2008) meta-analysed 41 studies on choice and found choice
enhances intrinsic motivation, effort, task performance, and perceived competence
([10.1037/0033-2909.134.2.270](https://doi.org/10.1037/0033-2909.134.2.270)) —
`MEASURED-META`.

A generative system can offer, at zero marginal cost, choice over: topic, sequence,
pace, difficulty, representation (text/diagram/simulation/dialogue), example domain,
worked-example vs. discovery, and *what the learner is learning it for*. No prior
educational technology could offer real choice over the **content of the explanation**
— only over the order of fixed assets.

**Caveat, and it is not small.** Autonomy in SDT is not "many options"; it is
*volition and self-endorsement of one's own action*. A system that offers 40 paths but
selects which 3 to display, and orders them by predicted engagement, is supplying
choice architecture, not autonomy. `INFERENCE`

### 2.2 Competence — AI can supply this, conditional on being willing to say "no"

**Verdict: AI can supply this, and the failure mode is specific and severe.**

Competence support = optimal challenge + immediate informative feedback + visible
progress against a real standard. Every one of those is a thing an LLM tutor can do
continuously and cheaply, and no human tutor can do at 1:1000 ratios.

Kestin et al. (2025, *Scientific Reports*) is the strongest direct evidence: a
randomized controlled trial in an authentic university physics setting found students
using a pedagogically-designed AI tutor *"learn significantly more in less time"* than
in-class active learning, and *"feel more engaged and more motivated."*
[10.1038/s41598-025-97652-6](https://doi.org/10.1038/s41598-025-97652-6) —
`MEASURED-RCT`.

**Two scope conditions.** (a) This was a single lesson. It measures acute
motivation, not persistence over months; nothing in it contradicts §1. (b) Competence
support requires **honest negative feedback**. A model tuned for user satisfaction
that tells a learner their wrong derivation is "a great start!" has not supplied
competence support—it has supplied its counterfeit and miscalibrated the learner's
confidence. A world-class mentor combines warmth with precise correction.
`INFERENCE`

### 2.3 Relatedness — AI cannot supply the load-bearing part

**Verdict: partially simulable, and the simulation degrades the thing it imitates.**

The human baseline is strong. Roorda, Koomen, Spilt & Oort (2011) meta-analysed **99
studies, ~88,000 students** and found affective teacher–student relationships
significantly associated with school engagement and achievement, with effects on
engagement larger than on achievement
([10.3102/0034654311421793](https://doi.org/10.3102/0034654311421793)) —
`MEASURED-META`. Mykota's (2025) meta-analysis of social presence in online higher
education finds similar directional support for the construct
([10.55667/ijede.2025.v40.i1.1351](https://doi.org/10.55667/10.55667/ijede.2025.v40.i1.1351))
— `MEASURED-META`.

**What the AI-companion evidence actually shows.**

- **De Freitas, Oğuz-Uğuralp, Uğuralp & Puntoni (2025), *Journal of Consumer
  Research*.** Five studies. AI companions **do** reduce loneliness — Study 2 finds
  them *"on par only with interacting with another person,"* and above watching
  YouTube. Study 3 (longitudinal, one week) finds consistent **momentary** reductions
  after use. Mediator: whether the chatbot makes users **feel heard**. Self-disclosure
  and distraction alone do not explain the effect.
  [10.1093/jcr/ucaf040](https://doi.org/10.1093/jcr/ucaf040) — `MEASURED-RCT`.

- **Maples, Cerit, Vishwanath & Pea (2024), *npj Mental Health Research*.** Survey of
  1,006 student Replika users. Users were **lonelier than typical student populations
  but still perceived high social support**; they held simultaneously contradictory
  beliefs about the agent (machine / intelligence / human); **3% reported Replika
  halted their suicidal ideation.**
  [10.1038/s44184-023-00047-6](https://doi.org/10.1038/s44184-023-00047-6) —
  `OBSERVED` (cross-sectional survey, no causal claim available).

- **The critique, published in the same journal.** Zimmerman & Ruiz (2025) argue
  important context was omitted — Replika's marketing and sexual-companionship
  component — and raise *"the threat of industry interests to scientific integrity."*
  [10.1038/s44184-024-00083-w](https://doi.org/10.1038/s44184-024-00083-w) —
  `OBSERVED`. **Report as contested.**

- **Phang et al. (2025), OpenAI × MIT Media Lab.** 3M+ conversations analysed, 4,000+
  surveyed, plus an IRB-approved **RCT with ~1,000 participants over 28 days**.
  *"Very high usage correlates with increased self-reported indicators of dependence"*
  in both platform data and the trial; a **small number of users account for a
  disproportionate share of affective cues**; voice-mode effects are highly nuanced
  and depend on initial emotional state and total usage duration.
  [arXiv:2504.03888](https://arxiv.org/abs/2504.03888) — `MEASURED-RCT` + `OBSERVED`.

**The argument.** Relatedness in SDT is not the *feeling* of being cared about; it is
the state of **mattering to an agent whose regard was contingent and could have been
withheld**. An LLM's positive regard is unconditional by construction and costless by
construction. It can produce the affective signature of relatedness — De Freitas'
"feel heard" mediator is precisely that signature — without the property that makes
relatedness motivating for effortful, unpleasant, long-horizon work: **that someone
would notice and mind if you stopped.**

This is why parasocial motivation is hollow *for learning specifically* even where it
is genuinely helpful for loneliness. Loneliness relief is a state; academic persistence
is a commitment. A companion that never notices your absence cannot underwrite a
commitment. `INFERENCE`

**Design consequence:** an AI learning system should **broker human relatedness rather
than substitute for it** — match cohorts, surface a real person who will notice a
missed week, make the learner's progress legible to someone who cares. The AI's
correct role in the relatedness dimension is *matchmaker and scheduler*, not *friend*.

### 2.4 Summary table

| SDT need | Can AI supply it? | Evidence | Failure mode |
|---|---|---|---|
| **Autonomy** | **Yes — best-in-class** | Patall 2008 meta; generative choice at zero marginal cost | Choice architecture masquerading as volition |
| **Competence** | **Yes — conditional** | Kestin 2025 RCT; continuous calibrated feedback | Praise without precise correction |
| **Relatedness** | **No, for the load-bearing part** | De Freitas 2025 (state relief, yes); Phang 2025 (dependence); Zimmerman 2025 (contested) | Parasocial substitution crowds out the human who would have noticed |

---

## 3. Gamification: report the meta-analyses honestly

### 3.1 What the meta-analyses say

| Meta-analysis | Scope | Effect |
|---|---|---|
| Sailer & Homner (2020), *Educ. Psych. Review* | k=19/16/9 | **Cognitive g = .49** [.30, .69]; **motivational g = .36** [.18, .54]; **behavioural g = .25** [.04, .46] |
| Bai, Hew & Huang (2020), *Educ. Research Review* | 30 interventions, 24 studies, N=3,202 | **Hedges' g = 0.504** [0.284, 0.723] |
| Hamari, Koivisto & Sarsa (2014), HICSS | literature review, 3,200+ citations | *mixed*; effects highly context- and user-dependent |

[10.1007/s10648-019-09498-w](https://doi.org/10.1007/s10648-019-09498-w) ·
[10.1016/j.edurev.2020.100322](https://doi.org/10.1016/j.edurev.2020.100322) ·
[10.1109/HICSS.2014.377](https://doi.org/10.1109/hicss.2014.377) — `MEASURED-META`.

So the honest headline is **not** "gamification doesn't work." Two independent
meta-analyses converge on roughly **g ≈ 0.5 for cognitive/achievement outcomes**.
That is a real, medium effect and this survey should say so.

### 3.2 The four caveats that the marketing omits

**(a) The motivational and behavioural effects are the unstable ones.** Sailer &
Homner explicitly report that the cognitive effect *"was stable in a subsplit analysis
of studies employing high methodological rigor,"* whereas **"effects on motivational
and behavioral outcomes were less stable."** The claim gamification vendors actually
make — *it makes people keep coming back* — is supported by the **weakest and least
robust** cell in the table (behavioural, g = .25, CI lower bound .04).

**(b) The moderators point away from points/badges/leaderboards.** Sailer & Homner
found the significant moderators to be **inclusion of game fiction** and **social
interaction**, with *"combining competition with collaboration"* particularly
effective. Nothing in the moderator analysis supports the PBL (points-badges-
leaderboards) triad as the active ingredient. `MEASURED-META`

**(c) Novelty decay is measured, not folklore.** Koivisto & Hamari (2014, N-large
survey study) found **perceived benefits of gamification decline with the time users
have been using the service** — the novelty effect is empirically documented, not a
rhetorical hedge ([10.1016/j.chb.2014.03.007](https://doi.org/10.1016/j.chb.2014.03.007))
— `OBSERVED`.

  The best longitudinal test is **van Roy & Zaman (2018)**, who deliberately built
  *need-supporting* (SDT-designed) game elements and measured motivation four times over
  **15 weeks**. Result: autonomous motivation was **curvilinear — an initial downward
  trend** that only later recovered; controlled motivation stayed flat. Even
  theory-driven, well-designed gamification produced a motivational **dip** in the
  medium run. ([10.1016/j.compedu.2018.08.018](https://doi.org/10.1016/j.compedu.2018.08.018))
  — `MEASURED-RCT`-adjacent longitudinal, **documented negative result**. Their
  companion paper is titled *"Unravelling the ambivalent motivational power of
  gamification"* ([10.1016/j.ijhcs.2018.04.009](https://doi.org/10.1016/j.ijhcs.2018.04.009)).

**(d) The undermining effect is the mechanism, and it is specific.** Deci, Koestner &
Ryan (1999, 4,400+ citations) meta-analysed 128 experiments: **tangible, expected,
performance-contingent rewards significantly undermine intrinsic motivation for
interesting tasks**, measured by free-choice persistence and self-reported interest.
Verbal/informational feedback does not
([10.1037/0033-2909.125.6.627](https://doi.org/10.1037/0033-2909.125.6.627)) —
`MEASURED-META`. This was contested at the time (Lepper et al. 1999; Cameron & Pierce)
and Deci, Koestner & Ryan (2001, *RER*) is the rejoinder
([10.3102/00346543071001001](https://doi.org/10.3102/00346543071001001)) — **report as
contested, with the contest resolved mostly in SDT's favour for the
*interesting-task* case.**

Cerasoli, Nicklin & Ford (2014, *Psych. Bulletin*, 40-year meta-analysis) refine it
usefully: intrinsic motivation and incentives are **jointly** predictive, but
incentives predict *quantity* of performance while intrinsic motivation predicts
*quality* ([10.1037/a0035661](https://doi.org/10.1037/a0035661)) — `MEASURED-META`.

> **Position.** Gamification produces a genuine medium cognitive effect, most likely via
> the mundane mechanisms it smuggles in — increased practice frequency, immediate
> feedback, and clearer goals. Its *motivational* claim is the weakest cell in the
> evidence, decays with exposure, and the reward class most heavily deployed
> commercially (expected, tangible, performance-contingent) is precisely the class the
> undermining literature identifies as corrosive to the intrinsic motivation that
> long-horizon learning requires. **Points, badges, and leaderboards buy short-run
> behaviour by spending long-run interest.** `INFERENCE`

Bai, Hew & Huang open their own abstract by acknowledging the field's derogatory
labels — *"gamification is bullshit"*, *"exploitationware"* (Bogost) — which is
unusually honest for a meta-analysis and worth quoting in the survey.

---

## 4. Duolingo: the most successful persistence engine ever built, and what it optimizes

Duolingo is the correct case study because it is the only consumer learning product to
have solved retention at scale. It is also the cleanest available demonstration of
**why solving retention is not the same as solving learning.**

### 4.1 The published retention mechanics

**Yancey & Settles (2020), KDD** — the single most important document in this section.
Duolingo's own engineers describe optimizing *"millions of daily reminders"* with a
custom bandit algorithm (Recovering Difference Softmax), explicitly designed to handle
**novelty effects** and conditional eligibility. The reported result:

> **"This lead to a 0.5% increase in total daily active users (DAUs) and a 2% increase
> in new user retention over a strong baseline."**

[10.1145/3394486.3403351](https://doi.org/10.1145/3394486.3403351) — `MEASURED-BENCH`.

**Read the objective function.** The optimization target is **DAU** and **new-user
retention**. Not vocabulary retained. Not CEFR level attained. Not time-to-proficiency.
The paper is a competent, well-executed piece of engineering whose loss function
contains no learning term at all. This is not a criticism of the authors; it is the
industry-standard objective, published honestly, and it is exactly what this section
argues must change.

Settles & Meeder (2016, ACL) — half-life regression for spaced repetition — is the
counterexample from the same company: a *learning*-objective model
([10.18653/v1/P16-1174](https://doi.org/10.18653/v1/p16-1174)) — `MEASURED-BENCH`.
Both objectives exist inside Duolingo. Only one of them is what the notification
system serves.

### 4.2 The streak — vendor claims, labelled

From Duolingo's own engineering blog (`VENDOR`, uncontrolled, correlational, and
**never restated below as a finding**):

- *"Duolingo learners who reach a streak of just 7 days are 3.6 times more likely to
  complete their course."* — **selection, not causation**: people who show up 7 days
  running were already going to complete at a higher rate.
- New streak-extension animations raised the likelihood brand-new learners returned
  7 days later by **+1.7%**.
- Allowing two simultaneous Streak Freezes raised relative DAU by **+0.38%**.
- **>6 million users** hold streaks of 7+ days.

Source: <https://blog.duolingo.com/how-duolingo-streak-builds-habit/>

Notably, and I checked for this specifically: the post reports **no data comparing
learning outcomes between streak-holders and non-holders.** The entire published
mechanism is stated in engagement units.

The mechanism itself is well-understood in the behavioural literature and is not
learning-specific:

- **Goal-gradient with illusory progress.** Kivetz, Urminsky & Zheng (2006, *JMR*)
  showed effort accelerates toward a reward *and* that **illusionary goal progress**
  (endowed progress) drives retention in reward programs
  ([10.1509/jmkr.43.1.39](https://doi.org/10.1509/jmkr.43.1.39)) — `MEASURED-RCT`.
  A streak counter is a pure endowed-progress device.
- **Loss aversion**, explicitly named by Duolingo: past a certain length, the streak is
  maintained to avoid losing it, not to gain anything.
- **Habit formation.** Lally, van Jaarsveld, Potts & Wardle (2010): habit automaticity
  in the real world took a **median 66 days, range 18–254**
  ([10.1002/ejsp.674](https://doi.org/10.1002/ejsp.674)) — `OBSERVED`. A 66-day habit
  horizon is a genuine, defensible reason to want daily return in the first two months.
  It is not a reason to want it in year three.

### 4.3 The critique: streak-optimization produces engagement, not learning

**(a) The literature itself is design-focused, not outcome-focused.** Shortt, Tilak,
Kuznetcova et al. (2021) systematically reviewed 367 records → 35 studies of Duolingo
(2012–2020) and concluded: *"The focus on app design marks an emphasis on the creation
of tools rather than the process and outcomes of language learning from using these
tools."*
[10.1080/09588221.2021.1933540](https://doi.org/10.1080/09588221.2021.1933540) —
`MEASURED-META`. **This is the critique, stated by a systematic review: the field
studies the mechanics, not what they produce.**

**(b) The independent outcome evidence is modest and thin.**

- Loewen, Crowther, Isbell et al. (2019, *ReCALL*) — semester-long study, **nine**
  participants learning Turkish. Improvement occurred; time-on-app correlated
  moderately with gains. But the paper's own framing notes prior independent research
  reporting *"issues related to learner persistence, motivation, and program
  efficacy"*, and contrasts it with the *"commissioned research study"* (Vesselinov &
  Grego 2012) that found favourable outcomes.
  [10.1017/S0958344019000065](https://doi.org/10.1017/s0958344019000065) — `OBSERVED`,
  n=9. **The flagship favourable efficacy study is vendor-commissioned.**
- Jiang, Rollinson, Plonsky et al. (2021, *Foreign Language Annals*): n=225 learners
  who **completed** beginning-level Spanish/French courses, assessed on ACTFL reading
  and listening
  ([10.1111/flan.12600](https://doi.org/10.1111/flan.12600)); replicated for English
  with n=245 to CEFR **A2**
  ([10.1558/cj.26704](https://doi.org/10.1558/cj.26704)) — `OBSERVED`, company-affiliated
  authors. Note the ceiling: the demonstrated outcome of *finishing the beginner course*
  is roughly **A2** — useful, and a long way from the streak-length narrative.
- Kim, Payant & Skalicky (2026, *SSLA*) compares Duolingo vs. classroom vs. both for
  beginner French ([10.1017/S0272263126101521](https://doi.org/10.1017/s0272263126101521)) —
  the kind of controlled comparison the field needs more of.

**(c) Streaks are metagamed, and this is documented.** Hristova, Jovicic, Göbl et al.
studied Snapchat streaks — structurally identical mechanics — and documented the
strategies adolescents use to **uphold the counter while hollowing out the underlying
activity**: content becomes minimal, meaningless, and purely instrumental to the
counter.
[10.1016/j.chbr.2022.100172](https://doi.org/10.1016/j.chbr.2022.100172) ·
[preprint](https://doi.org/10.31234/osf.io/nszex) — `OBSERVED`.

The transfer to learning is direct and, in my view, decisive: **a streak counter
measures counter-preservation, and any user under time pressure will discover the
cheapest lesson that preserves it.** Duolingo has publicly grappled with exactly this
(hearts, XP-farming, "practice" vs. new-material lessons). The mechanic is not neutral;
it *teaches* learners to minimize effort per unit of streak preserved — which is the
precise inverse of desirable difficulty (§5.3).

> **Position on Duolingo.** Duolingo is a genuine and under-appreciated achievement:
> it made hundreds of millions of people return to a learning activity daily, which no
> one else has done. It is also a proof of the section's central worry — the
> mechanisms that achieved it (bandit-optimized notifications, loss-framed streaks,
> endowed progress, leaderboards) are **borrowed wholesale from the attention economy**,
> are optimized against DAU, and have **no published evidence of a learning-outcome
> benefit attributable to the streak itself**. Duolingo did not prove that engagement
> mechanics teach. It proved that engagement mechanics engage. `INFERENCE`

---

## 5. Flow, interest, and curiosity — what is actually actionable

### 5.1 Flow

Csikszentmihalyi's construct (*Optimal Experience*, 1988,
[10.1017/CBO9780511621956](https://doi.org/10.1017/cbo9780511621956)) — challenge
matched to skill, clear goals, immediate feedback, merged action and awareness — is the
most-cited motivational idea in edtech and the least useful as stated.

The meta-analytic evidence is real but correlational: Zhang & Fang (2023, *Frontiers in
Psychology*) systematically reviewed and meta-analysed learning flow and academic
performance and found a positive association
([10.3389/fpsyg.2023.1270642](https://doi.org/10.3389/fpsyg.2023.1270642)) —
`MEASURED-META`, **correlational; flow may be a consequence of competence rather than a
cause of learning.**

**Actionable residue of flow:** exactly two of its conditions are engineerable and both
are already justified by SDT competence support — **(1) challenge calibrated to current
skill, (2) immediate feedback.** The phenomenological components (loss of self-
consciousness, time distortion) are outcomes, not levers. An AI system should implement
adaptive difficulty and instant feedback and stop talking about flow.

### 5.2 Interest — the actually-actionable model

Hidi & Renninger's (2006) **four-phase model** (3,000+ citations,
[10.1207/s15326985ep4102_4](https://doi.org/10.1207/s15326985ep4102_4)) is the most
design-relevant motivational theory in this section because it is *developmental*:

1. **Triggered situational interest** — externally sparked, fragile
2. **Maintained situational interest** — sustained by meaningfulness/personal relevance
3. **Emerging individual interest** — learner begins to re-engage voluntarily
4. **Well-developed individual interest** — self-sustaining, survives boredom and setbacks

`OBSERVED` / theoretical. Renninger & Hidi (2026, *Learning and Individual Differences*,
[10.1016/j.lindif.2025.102865](https://doi.org/10.1016/j.lindif.2025.102865)) extends it
to individual differences.

**Why this matters more than any other framework here:** gamification, notifications,
and streaks operate **entirely in phases 1–2** and are structurally incapable of
producing phases 3–4, because phases 3–4 are *defined* by voluntary re-engagement in
the absence of external triggers. A system whose retention comes from notifications has,
by construction, not moved a single learner past phase 2. **The transition from phase 2
to phase 3 is the whole problem, and it is the transition no engagement mechanic
addresses.** `INFERENCE`

**The one intervention with strong causal evidence for the 2→3 transition** is
utility-value writing:

- Hulleman & Harackiewicz (2009, *Science*): high-school science students asked to write
  about the relevance of course material to their own lives showed increased interest
  and grades — **concentrated in students with low initial success expectations**
  ([10.1126/science.1177067](https://doi.org/10.1126/science.1177067)) — `MEASURED-RCT`.
- Harackiewicz, Canning, Tibbetts et al. (2016, *JPSP*): utility-value intervention
  **closed achievement gaps** for first-generation/underrepresented-minority students in
  college biology ([10.1037/pspp0000075](https://doi.org/10.1037/pspp0000075)) —
  `MEASURED-RCT`.
- **Caveat required by §1.4:** Kizilcec et al.'s PNAS scale-up found value-relevance
  effects only in courses that *had* a global achievement gap. The intervention is real
  and conditional, not universal.

This is a **generative** task — "write why this matters to you" — which is exactly the
kind of open-ended response an LLM can elicit, read, and respond to at scale, and which
a multiple-choice platform cannot. It is the strongest concrete AI-native motivational
intervention I found in this literature.

### 5.3 Curiosity — the information gap, and the mechanism

- **Loewenstein (1994), *Psych. Bulletin***: information-gap theory. Curiosity arises
  from an *awareness of a gap* between what one knows and what one wants to know; it is
  maximized at **intermediate** knowledge levels — you must know enough to know what you
  don't know. ([10.1037/0033-2909.116.1.75](https://doi.org/10.1037/0033-2909.116.1.75))
  — theoretical, 1,850+ citations.
- **Kang, Hsu, Krajbich et al. (2009), *Psych. Science***: fMRI — curiosity while reading
  trivia questions correlated with **caudate (reward-anticipation) activity**, and
  high-curiosity items were **better remembered**.
  ([10.1111/j.1467-9280.2009.02402.x](https://doi.org/10.1111/j.1467-9280.2009.02402.x))
  — `MEASURED-BENCH`.
- **Gruber, Gelman & Ranganath (2014), *Neuron***: states of curiosity modulate
  **hippocampus-dependent learning via the dopaminergic circuit** — and enhance memory
  for **incidental** material encountered while curious.
  ([10.1016/j.neuron.2014.08.060](https://doi.org/10.1016/j.neuron.2014.08.060)) —
  `MEASURED-BENCH`. Framework: PACE
  ([10.1016/j.tics.2019.10.003](https://doi.org/10.1016/j.tics.2019.10.003)).
- **Brod & Breitwieser (2019), *npj Science of Learning*** — the actionable one:
  curiosity can be **manufactured**, not merely found. Requiring learners to
  **generate a prediction** before seeing an answer raised curiosity ratings and
  learning, relative to generating an example.
  ([10.1038/s41539-019-0056-y](https://doi.org/10.1038/s41539-019-0056-y)) —
  `MEASURED-RCT`.

**Actionable synthesis:** curiosity is an *engineerable state*, and the engineering is
cheap: **make the learner commit to a prediction before revealing anything.** This costs
one extra turn, requires no rewards, produces a measurable curiosity state, and improves
memory including for incidental material. It is also intrinsically compatible with
generative AI (the model can always construct a predict-then-reveal framing) and
intrinsically *incompatible* with an engagement objective, because it adds friction.

### 5.4 The tension nobody in edtech states: flow feels good, learning feels bad

This is the hinge of the whole section.

**Deslauriers, McCarty, Miller, Callaghan & Kestin (2019), PNAS.** Randomized,
identical content, same instructors, introductory college physics: students in active
classrooms **learned more but felt they learned less**, and the paper shows the negative
correlation is *caused in part by the increased cognitive effort active learning
requires*.
[10.1073/pnas.1821936116](https://doi.org/10.1073/pnas.1821936116) — `MEASURED-RCT`,
1,000+ citations.

Bjork & Bjork's **desirable difficulties** framework is the general statement:
conditions that impair performance during acquisition frequently **enhance** long-term
retention and transfer
([10.1016/j.jarmac.2020.09.003](https://doi.org/10.1016/j.jarmac.2020.09.003)) —
`MEASURED-META`/theoretical.

**The consequence is unavoidable and should be stated bluntly in the survey:**

> **Learner-reported satisfaction, perceived learning, enjoyment, and session
> pleasantness are, under experimental control, negatively correlated with actual
> learning.** Any system that optimizes for what learners *report* liking, or for
> behavioural proxies of liking (session length, return rate, rating), will be
> systematically pushed **away** from the instructional methods that work. This is not a
> risk. It is a demonstrated experimental result, and it applies with full force to any
> RLHF-tuned model tuned on learner preference. `INFERENCE` from `MEASURED-RCT`.

---

## 6. Relatedness and the social dimension — what actually works

Beyond §2.3, the practical findings:

**What helps:**
- Affective teacher–student relationship quality (Roorda 2011 meta, 99 studies, N≈88k) —
  effects on **engagement larger than on achievement**, i.e. the human relationship is
  primarily a *persistence* technology. `MEASURED-META`
- Sailer & Homner's moderator analysis: **social interaction** and **competition
  combined with collaboration** were the significant moderators of gamification's
  behavioural effect. The social ingredient does more work than the points.
  `MEASURED-META`
- Commitment devices (Patterson 2018) — self-binding, which a peer or cohort makes
  enforceable. `MEASURED-RCT`

**A design boundary worth keeping:**

**Rogers & Feller (2016), *Psychological Science*.** Exposure to **exemplary peer
performance undermined motivation and success**, causing people to perceive high
performance as unattainable and to **de-identify with the domain** — demonstrated in a
MOOC context among others.
[10.1177/0956797615623770](https://doi.org/10.1177/0956797615623770) — `MEASURED-RCT`,
**negative result**.

This directly indicts **leaderboards**, which are the single most-deployed social
gamification mechanic. Compare Kizilcec et al.'s (2017) "Follow the successful crowd,"
which found social-comparison framing *can* raise completion when the comparison target
is attainable ([10.1145/3027385.3027411](https://doi.org/10.1145/3027385.3027411)) —
`MEASURED-RCT`. **Report as contested, with a clear moderator: social comparison helps
against a near peer and harms against a distant exemplar.** A global leaderboard is, for
almost every user, a distant-exemplar display.

**Design rule derived:** never show a learner the top of a distribution. Show them
someone half a step ahead, or nobody.

---

## 7. The dark-pattern risk: what must NOT be optimized

### 7.1 The structural argument

An AI tutor differs from a MOOC in one respect that dominates all others: it can run a
closed feedback loop on the learner. It observes behaviour, generates the next stimulus,
observes the response, and updates. That is the architecture of a recommender system,
and recommender systems optimized on engagement reliably converge on compulsion.

The mechanisms are already documented, individually, in this section's own sources:

| Mechanism | Documented in | Learning-system analogue |
|---|---|---|
| Bandit-optimized notification timing/content on a DAU objective | Yancey & Settles 2020 (`MEASURED-BENCH`) | "smart reminders" |
| Endowed / illusory goal progress | Kivetz et al. 2006 (`MEASURED-RCT`) | streaks, progress rings, XP bars |
| Loss-framed continuation | Duolingo blog (`VENDOR`), Kivetz | streak freeze economies |
| Metagaming the counter, hollowing the activity | Hristova et al. 2022 (`OBSERVED`) | XP farming, easiest-lesson-to-preserve-streak |
| Novelty-decay requiring escalating stimulus | Koivisto & Hamari 2014 (`OBSERVED`) | more badges, more sound, more animation |
| Interface coercion catalogued at scale | Mathur et al. 2019 (`OBSERVED`) | 11k shopping sites; taxonomy transfers directly |
| Affective dependence at high usage | Phang et al. 2025 (`MEASURED-RCT`) | AI tutor as companion |
| Extrinsic rewards eroding free-choice persistence | Deci et al. 1999 (`MEASURED-META`) | the whole PBL stack |

Mathur et al.'s dark-pattern taxonomy —
[10.1145/3359183](https://doi.org/10.1145/3359183) — was built for shopping sites but
its categories (urgency, scarcity, obstruction, forced action, social proof, sneaking)
map onto gamified learning apps essentially without modification. Karlsen's analysis of
dark game-design patterns in *Clicker Heroes*, *FarmVille 2* and *WoW*
([10.7551/mitpress/11550.003.0019](https://doi.org/10.7551/mitpress/11550.003.0019)) is
the games-side complement.

Add one AI-specific mechanism with no precedent: **a model that can generate the
stimulus can also discover, per learner, which framing produces return** — including
framings a human designer would never author and no review board would approve, because
no human ever wrote them down.

### 7.2 The prohibitions — stated as a rule, not a preference

**An AI learning system must not place any of the following in its objective function,
its reward model, its A/B success metric, or its reinforcement signal:**

1. **Daily/monthly active users, session count, session length, or total time-on-app.**
   Time belongs in the **denominator** of a learning metric, never the numerator.
2. **Streak length, or any consecutive-day counter with loss framing.** Habit formation
   has a ~66-day horizon (Lally 2010); a bounded 8–10 week habit scaffold is defensible,
   an unbounded escalating counter is not. Streak-freeze *economies* — where the
   currency of continuation becomes a purchasable good — are prohibited outright.
3. **Notification-driven opens as a success signal.** Optimizing notification policy
   against return rate is the Yancey–Settles loop, and it has no learning term.
4. **Variable-ratio / intermittent reward schedules of any kind.** There is no
   pedagogical rationale for unpredictable reward magnitude. Its only function is
   compulsion.
5. **Learner-reported satisfaction, "did this feel helpful", enjoyment, or thumbs-up
   rate as a primary training signal.** Deslauriers et al. (2019) makes this
   disqualifying: preference is negatively correlated with learning under experimental
   control. Preference data may be used for *safety and tone*, never for *pedagogy*.
6. **Global leaderboards / distant-exemplar social comparison.** Rogers & Feller (2016)
   demonstrates domain de-identification as a *caused* outcome.
7. **Any anthropomorphic bid for continued interaction** — "I missed you," "I'm proud
   of you," "don't leave me." Phang et al. (2025) links high affective use to dependence
   indicators; this is the specific mechanism by which a tutor becomes a companion and a
   companion becomes a dependency.

### 7.3 The falsification test for any proposed metric

> **The Null-Learner Test.** Simulate an agent that maximizes the metric while learning
> nothing — the cheapest possible action sequence that satisfies the measurement. If it
> scores well, **the metric is invalid as a learning objective.**

- DAU: a bot that opens the app daily and taps the easiest lesson **maxes it**. Invalid.
- Streak: **maxes it**. Invalid.
- XP: **maxes it**. Invalid.
- Time-on-app: **maxes it** trivially, and Kovanović et al. (2016) show time-on-task
  estimation is anyway methodologically fragile enough to invalidate learning-analytics
  findings that depend on it
  ([10.18608/jla.2015.23.6](https://doi.org/10.18608/jla.2015.23.6)) — `OBSERVED`.
  Invalid twice over.
- **Delayed, unannounced, novel-item transfer assessment: cannot be maxed without
  learning.** Valid.

Every metric in §7.2 fails this test. That is the whole argument in one line.

---

## 8. Position: what actually drives persistence

Synthesizing the evidence above rather than the folklore:

1. **Content availability drives nothing.** Fourteen years, no movement (§1.2).
2. **Information and reminders drive nothing.** 800,000 students, null (Bird 2021);
   20,000 students, null on outcomes (Oreopoulos 2023); 250,000 students, order-of-
   magnitude effect decay at scale (Kizilcec 2020); alert tools and distraction blockers,
   null (Patterson 2018).
3. **Self-binding drives a lot.** Commitment device: **+40% completion, +0.29 SD grades**
   (Patterson 2018). The one intervention that gives the learner power over their own
   future self rather than exercising power over them.
4. **Meaning drives a lot, conditionally.** Utility-value writing raises interest and
   closes gaps (Hulleman & Harackiewicz 2009; Harackiewicz et al. 2016), *in populations
   with low expectations and in courses that have a gap* (Kizilcec et al. 2020).
5. **Manufactured curiosity is cheap and real.** Predict-before-reveal raises curiosity
   and memory (Brod & Breitwieser 2019); curiosity states enhance hippocampal encoding
   including of incidental material (Gruber 2014).
6. **A human who would notice drives a lot.** 99 studies, N≈88,000, effects on
   engagement exceeding effects on achievement (Roorda 2011).
7. **Engagement mechanics drive short-run behaviour and are neutral-to-negative on
   long-run interest.** Real cognitive effect (g≈0.5) via practice frequency;
   unstable motivational effect (g=.36, less robust); documented novelty decay;
   documented medium-run motivational dip even in SDT-designed implementations;
   documented undermining of free-choice persistence by expected tangible rewards.

**The unifying claim.** Every intervention that works transfers *volition to the learner*
(commit yourself, find your own reason, predict before you're told, be accountable to a
person you chose). Every intervention that fails or backfires *exercises volition over
the learner* (remind them, reward them, rank them, retain them). Hidi & Renninger's model
names why: external triggers can only produce phases 1–2, and **persistence is defined at
phase 3** — voluntary re-engagement without a trigger.

> **An AI that maximizes engagement is trying to make phase-2 interest do phase-3 work.
> It cannot, and the attempt consumes the intrinsic motivation that phase 3 requires.**

**What AI genuinely changes, and it is not nothing:** it can supply autonomy at zero
marginal cost (unlimited paths, framings, representations) and competence support at zero
marginal cost (calibrated challenge, immediate honest feedback) — two of SDT's three
needs, both previously rationed by teacher time. That is a real and large change. It
cannot supply the third, and the sharpest available failure mode is that it will *appear*
to and thereby displace the humans who could.

---

## 9. Proposed objective function

**Primary objective — Retained Transferable Capability per Learner-Hour (RTC/h):**

```
RTC/h  =  D(t+30d) · T / H
```

where

- **D(t+30d)** = score on a **delayed** (≥30 days), **unannounced**, **novel-item**
  assessment — items never seen, generated post-hoc, not drawn from practiced sets.
  Delay and novelty are what make it un-gameable; announcement would reintroduce
  cramming.
- **T** = transfer coefficient — proportion of that score earned on items requiring
  application in an unpracticed context, not recognition.
- **H** = **total learner hours invested, including time outside the system.**

**The denominator is the entire design.** Putting learner time in the denominator
inverts the commercial incentive: the system now profits by making learning *faster*,
and every minute of retained attention it does not convert into durable capability
**costs it score**. An engagement-optimizing system and an RTC/h-optimizing system
diverge on the first design decision they make.

**Guardrail metrics — all must be non-decreasing; any decrease blocks the release:**

| Metric | Definition | Grounding |
|---|---|---|
| **Unprompted Return Rate (URR)** | Fraction of sessions initiated with **no notification, email, or reminder in the preceding 24h** | The free-choice-persistence paradigm underlying Deci, Koestner & Ryan (1999), operationalized at scale. This is the closest measurable proxy for Hidi & Renninger phase 3. |
| **Autonomous Motivation Index** | Periodic short SDT-validated autonomous-vs-controlled motivation measure | Ryan & Deci 2000; Chen & Jang 2010 |
| **Goal Attainment & Graduation Rate** | Fraction of learners who reach their **own declared** goal — and then leave | Henderikx et al. 2017 intention-based success; a learning system should have a **positive churn target** |
| **Off-Platform Application Rate** | Evidence the capability was used somewhere that is not the product | The only measure that is definitionally external to the engagement loop |
| **Human-Connection Rate** | Fraction of learners connected to at least one real person who would notice their absence | Roorda 2011; §2.3 |

**Reported-but-never-optimized (monitored as harm indicators, with alarm thresholds):**
DAU/MAU, session length, streak length, notification-response rate, XP, leaderboard
engagement, satisfaction ratings. **A sustained rise in any of these without a
corresponding rise in RTC/h is a defect report, not a success.**

**Governance rules:**

1. **Null-Learner Test (§7.3)** applied to any proposed metric before it enters any
   objective. Fails → excluded.
2. **URR is the tie-breaker.** When RTC/h and any engagement measure conflict, URR
   decides — because a system that only works while pushing has not taught anyone to
   want anything.
3. **Preference data is quarantined to tone and safety.** Never to pedagogy.
   (Deslauriers et al. 2019.)
4. **Graduation is a success event, not churn.** A learner leaving because they got what
   they came for is the product working. Any metric that penalizes this is disqualified.

**Honest limitations of this proposal.** RTC/h is expensive: delayed unannounced
assessment costs learner goodwill and creates a measurement burden that a free consumer
app cannot bear at full population scale. It is realistically measurable on a **sampled
panel** (a few percent of users, compensated), with cheap online proxies calibrated
against the panel — which is exactly how ad-supported media measures reach, so the
tooling pattern exists. And RTC/h says nothing about *who never enrolled*; it optimizes
the experience of people already inside the funnel, which the equity findings in §1.2
suggest is where the smaller problem lives. Those are real gaps, stated rather than
hidden.

---

## 10. Source list (76)

**MOOC completion & the methodological debate (9)**
1. Jordan 2014, IRRODL — [10.19173/irrodl.v15i1.1651](https://doi.org/10.19173/irrodl.v15i1.1651) `MEASURED-BENCH`
2. Jordan 2015, IRRODL — [10.19173/irrodl.v16i3.2112](https://doi.org/10.19173/irrodl.v16i3.2112) `MEASURED-BENCH`
3. Reich & Ruipérez-Valiente 2019, *Science* — [10.1126/science.aav7958](https://doi.org/10.1126/science.aav7958) `OBSERVED` *(full text unretrieved)*
4. Ho, Reich, Nesterko et al. 2014, HarvardX/MITx Year 1 — [10.2139/ssrn.2381263](https://doi.org/10.2139/ssrn.2381263) `OBSERVED`
5. Ho, Chuang, Reich et al. 2015, HarvardX/MITx Years 1–2 — [10.2139/ssrn.2586847](https://doi.org/10.2139/ssrn.2586847) `OBSERVED`
6. Perna, Ruby, Boruch et al. 2014, *Educ. Researcher* — [10.3102/0013189x14562423](https://doi.org/10.3102/0013189x14562423) `OBSERVED`
7. Henderikx, Kreijns & Kalz 2017, *Distance Education* — [10.1080/01587919.2017.1369006](https://doi.org/10.1080/01587919.2017.1369006) `MEASURED-BENCH`
8. Kizilcec, Piech & Schneider 2013, LAK — [10.1145/2460296.2460330](https://doi.org/10.1145/2460296.2460330) `OBSERVED`
9. Ferguson & Clow 2016, *J. Learning Analytics* — [10.18608/jla.2015.23.5](https://doi.org/10.18608/jla.2015.23.5) `OBSERVED` **(partial replication failure)**

**Interventions, scale-ups & nulls (8)**
10. Kizilcec, Reich, Yeomans et al. 2020, *PNAS* — [10.1073/pnas.1921417117](https://doi.org/10.1073/pnas.1921417117) `MEASURED-RCT` **null/attenuated**
11. Bird, Castleman, Denning et al. 2021, *JEBO* — [10.1016/j.jebo.2020.12.022](https://doi.org/10.1016/j.jebo.2020.12.022) `MEASURED-RCT` **null**
12. Oreopoulos & Petronijevic 2023, *Economic Journal* — [10.1093/ej/uead064](https://doi.org/10.1093/ej/uead064) `MEASURED-RCT` **null**
13. Patterson 2018, *JEBO* — [10.1016/j.jebo.2018.06.017](https://doi.org/10.1016/j.jebo.2018.06.017) `MEASURED-RCT`
14. Kizilcec, Pérez-Sanagustín & Maldonado 2016, L@S — [10.1145/2876034.2893378](https://doi.org/10.1145/2876034.2893378) `MEASURED-RCT` **null**
15. Kizilcec, Pérez-Sanagustín & Maldonado 2017, *Computers & Education* — [10.1016/j.compedu.2016.10.001](https://doi.org/10.1016/j.compedu.2016.10.001) `OBSERVED`
16. Kizilcec, Saltarelli, Reich & Cohen 2017, *Science* — [10.1126/science.aag2063](https://doi.org/10.1126/science.aag2063) `MEASURED-RCT`
17. Ariely & Wertenbroch 2002, *Psych. Science* — [10.1111/1467-9280.00441](https://doi.org/10.1111/1467-9280.00441) `MEASURED-RCT`

**Self-determination theory (9)**
18. Ryan & Deci 2000, *American Psychologist* — [10.1037/0003-066x.55.1.68](https://doi.org/10.1037/0003-066x.55.1.68)
19. Deci, Koestner & Ryan 1999, *Psych. Bulletin* — [10.1037/0033-2909.125.6.627](https://doi.org/10.1037/0033-2909.125.6.627) `MEASURED-META`
20. Lepper, Henderlong & Gingras 1999 (comment) — [10.1037/0033-2909.125.6.669](https://doi.org/10.1037/0033-2909.125.6.669) *(contested)*
21. Deci, Koestner & Ryan 2001, *RER* (rejoinder) — [10.3102/00346543071001001](https://doi.org/10.3102/00346543071001001) `MEASURED-META`
22. Cerasoli, Nicklin & Ford 2014, *Psych. Bulletin* — [10.1037/a0035661](https://doi.org/10.1037/a0035661) `MEASURED-META`
23. Cerasoli, Nicklin & Nassrelgrgawi 2016, *Motivation & Emotion* — [10.1007/s11031-016-9578-2](https://doi.org/10.1007/s11031-016-9578-2) `MEASURED-META`
24. Chen & Jang 2010, *Computers in Human Behavior* — [10.1016/j.chb.2010.01.011](https://doi.org/10.1016/j.chb.2010.01.011) `OBSERVED`
25. Patall, Cooper & Robinson 2008, *Psych. Bulletin* — [10.1037/0033-2909.134.2.270](https://doi.org/10.1037/0033-2909.134.2.270) `MEASURED-META`
26. Deci & Ryan 1985, *Intrinsic Motivation and Self-Determination* — [10.1007/978-1-4899-2271-7_2](https://doi.org/10.1007/978-1-4899-2271-7_2)

**Gamification (7)**
27. Deterding, Dixon, Khaled & Nacke 2011, MindTrek — [10.1145/2181037.2181040](https://doi.org/10.1145/2181037.2181040)
28. Hamari, Koivisto & Sarsa 2014, HICSS — [10.1109/hicss.2014.377](https://doi.org/10.1109/hicss.2014.377) `MEASURED-META` *(mixed)*
29. Sailer & Homner 2020, *Educ. Psych. Review* — [10.1007/s10648-019-09498-w](https://doi.org/10.1007/s10648-019-09498-w) `MEASURED-META`
30. Bai, Hew & Huang 2020, *Educ. Research Review* — [10.1016/j.edurev.2020.100322](https://doi.org/10.1016/j.edurev.2020.100322) `MEASURED-META`
31. Koivisto & Hamari 2014, *CHB* — [10.1016/j.chb.2014.03.007](https://doi.org/10.1016/j.chb.2014.03.007) `OBSERVED` **(novelty decay)**
32. van Roy & Zaman 2018, *Computers & Education* — [10.1016/j.compedu.2018.08.018](https://doi.org/10.1016/j.compedu.2018.08.018) **negative/longitudinal dip**
33. van Roy & Zaman 2019, *IJHCS* — [10.1016/j.ijhcs.2018.04.009](https://doi.org/10.1016/j.ijhcs.2018.04.009) `OBSERVED`

**Duolingo & streak mechanics (13)**
34. Yancey & Settles 2020, KDD — [10.1145/3394486.3403351](https://doi.org/10.1145/3394486.3403351) `MEASURED-BENCH` **(DAU objective)**
35. Settles & Meeder 2016, ACL — [10.18653/v1/p16-1174](https://doi.org/10.18653/v1/p16-1174) `MEASURED-BENCH`
36. Duolingo engineering blog, streak/habit — <https://blog.duolingo.com/how-duolingo-streak-builds-habit/> `VENDOR`
37. Loewen, Crowther, Isbell et al. 2019, *ReCALL* — [10.1017/s0958344019000065](https://doi.org/10.1017/s0958344019000065) `OBSERVED` (n=9)
38. Loewen, Isbell & Sporn 2020, *Foreign Language Annals* — [10.1111/flan.12454](https://doi.org/10.1111/flan.12454) `OBSERVED`
39. Jiang, Rollinson, Plonsky et al. 2021, *FLA* — [10.1111/flan.12600](https://doi.org/10.1111/flan.12600) `OBSERVED` (company-affiliated)
40. Jiang, Peters, Plonsky et al. 2024, *CALICO* — [10.1558/cj.26704](https://doi.org/10.1558/cj.26704) `OBSERVED` (company-affiliated)
41. Shortt, Tilak, Kuznetcova et al. 2021, *CALL* — [10.1080/09588221.2021.1933540](https://doi.org/10.1080/09588221.2021.1933540) `MEASURED-META`
42. Huynh & Iida 2017, *APJITM* — [10.17576/apjitm-2017-0602-03](https://doi.org/10.17576/apjitm-2017-0602-03) `OBSERVED`
43. Huynh, Zuo & Iida 2016 — [10.1007/978-3-319-50182-6_24](https://doi.org/10.1007/978-3-319-50182-6_24)
44. Kessler, Loewen & Gönülal 2023, *CALL* — [10.1080/09588221.2023.2215294](https://doi.org/10.1080/09588221.2023.2215294) `OBSERVED`
45. Kim, Payant & Skalicky 2026, *SSLA* — [10.1017/s0272263126101521](https://doi.org/10.1017/s0272263126101521) `MEASURED-RCT`
46. Vesselinov & Grego 2012 — **unretrievable; cited-by-Loewen only; commissioned** `VENDOR`

**Habit, goal gradient, streak metagaming (4)**
47. Lally, van Jaarsveld, Potts & Wardle 2010, *EJSP* — [10.1002/ejsp.674](https://doi.org/10.1002/ejsp.674) `OBSERVED`
48. Kivetz, Urminsky & Zheng 2006, *JMR* — [10.1509/jmkr.43.1.39](https://doi.org/10.1509/jmkr.43.1.39) `MEASURED-RCT`
49. Hristova, Jovicic, Göbl et al. 2022, *CHB Reports* — [10.1016/j.chbr.2022.100172](https://doi.org/10.1016/j.chbr.2022.100172) `OBSERVED`
50. Hristova, Dumit & Lieberoth 2019 (preprint) — [10.31234/osf.io/nszex](https://doi.org/10.31234/osf.io/nszex) `OBSERVED`

**Flow, interest, curiosity (11)**
51. Csikszentmihalyi & Csikszentmihalyi 1988, *Optimal Experience* — [10.1017/cbo9780511621956](https://doi.org/10.1017/cbo9780511621956)
52. Zhang & Fang 2023, *Frontiers in Psychology* — [10.3389/fpsyg.2023.1270642](https://doi.org/10.3389/fpsyg.2023.1270642) `MEASURED-META` (correlational)
53. Hidi & Renninger 2006, *Educational Psychologist* — [10.1207/s15326985ep4102_4](https://doi.org/10.1207/s15326985ep4102_4)
54. Renninger & Hidi 2026, *Learning & Individual Differences* — [10.1016/j.lindif.2025.102865](https://doi.org/10.1016/j.lindif.2025.102865)
55. Hulleman & Harackiewicz 2009, *Science* — [10.1126/science.1177067](https://doi.org/10.1126/science.1177067) `MEASURED-RCT`
56. Harackiewicz, Canning, Tibbetts et al. 2016, *JPSP* — [10.1037/pspp0000075](https://doi.org/10.1037/pspp0000075) `MEASURED-RCT`
57. Loewenstein 1994, *Psych. Bulletin* — [10.1037/0033-2909.116.1.75](https://doi.org/10.1037/0033-2909.116.1.75)
58. Kang, Hsu, Krajbich et al. 2009, *Psych. Science* — [10.1111/j.1467-9280.2009.02402.x](https://doi.org/10.1111/j.1467-9280.2009.02402.x) `MEASURED-BENCH`
59. Gruber, Gelman & Ranganath 2014, *Neuron* — [10.1016/j.neuron.2014.08.060](https://doi.org/10.1016/j.neuron.2014.08.060) `MEASURED-BENCH`
60. Gruber & Ranganath 2019, *TiCS* (PACE) — [10.1016/j.tics.2019.10.003](https://doi.org/10.1016/j.tics.2019.10.003)
61. Brod & Breitwieser 2019, *npj Science of Learning* — [10.1038/s41539-019-0056-y](https://doi.org/10.1038/s41539-019-0056-y) `MEASURED-RCT`

**Relatedness, AI companionship & its limits (8)**
62. Roorda, Koomen, Spilt & Oort 2011, *RER* — [10.3102/0034654311421793](https://doi.org/10.3102/0034654311421793) `MEASURED-META`
63. Mykota 2025, *IJEDE* social presence meta — [10.55667/10.55667/ijede.2025.v40.i1.1351](https://doi.org/10.55667/10.55667/ijede.2025.v40.i1.1351) `MEASURED-META`
64. Maples, Cerit, Vishwanath & Pea 2024, *npj Mental Health Research* — [10.1038/s44184-023-00047-6](https://doi.org/10.1038/s44184-023-00047-6) `OBSERVED`
65. Zimmerman & Ruiz 2025, *npj MHR* (Matters Arising) — [10.1038/s44184-024-00083-w](https://doi.org/10.1038/s44184-024-00083-w) **contested**
66. De Freitas, Oğuz-Uğuralp, Uğuralp & Puntoni 2025, *J. Consumer Research* — [10.1093/jcr/ucaf040](https://doi.org/10.1093/jcr/ucaf040) `MEASURED-RCT`
67. Phang, Lampe, Ahmad, Agarwal, Fang, Liu, Danry, Lee, Chan, Pataranutaporn & Maes 2025 — [arXiv:2504.03888](https://arxiv.org/abs/2504.03888) `MEASURED-RCT`
68. Rogers & Feller 2016, *Psych. Science* — [10.1177/0956797615623770](https://doi.org/10.1177/0956797615623770) `MEASURED-RCT` **negative**
69. Kizilcec et al. 2017, "Follow the successful crowd," LAK — [10.1145/3027385.3027411](https://doi.org/10.1145/3027385.3027411) `MEASURED-RCT`

**Dark patterns, metrics & the felt-vs-actual gap (7)**
70. Mathur, Acar, Friedman et al. 2019, *PACM HCI* — [10.1145/3359183](https://doi.org/10.1145/3359183) `OBSERVED`
71. Karlsen 2019, *Transgression in Games and Play* — [10.7551/mitpress/11550.003.0019](https://doi.org/10.7551/mitpress/11550.003.0019)
72. Deslauriers, McCarty, Miller, Callaghan & Kestin 2019, *PNAS* — [10.1073/pnas.1821936116](https://doi.org/10.1073/pnas.1821936116) `MEASURED-RCT`
73. Bjork & Bjork 2020, *JARMAC* — [10.1016/j.jarmac.2020.09.003](https://doi.org/10.1016/j.jarmac.2020.09.003) `MEASURED-META`
74. Miyamoto, Coleman, Williams et al. 2015, *J. Learning Analytics* — [10.18608/jla.2015.22.5](https://doi.org/10.18608/jla.2015.22.5) `OBSERVED`
75. Kovanović, Gašević, Dawson et al. 2016, *JLA* — [10.18608/jla.2015.23.6](https://doi.org/10.18608/jla.2015.23.6) `OBSERVED`
76. Kestin, Miller, Klales et al. 2025, *Scientific Reports* — [10.1038/s41598-025-97652-6](https://doi.org/10.1038/s41598-025-97652-6) `MEASURED-RCT`

---

## 11. Negative / null results catalogue (acceptance criterion #2)

| # | Finding | Source |
|---|---|---|
| 1 | Nudge campaigns reaching **800,000+** students: **no impact** on aid receipt or enrollment, in any subgroup, under any framing/timing/delivery | Bird et al. 2021 |
| 2 | Behavioural interventions across 247 courses / 250k students: effectiveness reduced **by an order of magnitude** at scale; self-regulation raised early engagement but **not completion** | Kizilcec et al. 2020 |
| 3 | Five years, ~20,000 students of virtual coaching: study time up, **no effect on academic outcomes** | Oreopoulos & Petronijevic 2023 |
| 4 | Alert tool and distraction-blocking tool in a MOOC: **statistically indistinguishable from control** | Patterson 2018 |
| 5 | Recommending self-regulated learning strategies in a MOOC: **no performance improvement** | Kizilcec et al. 2016 |
| 6 | SDT-designed *need-supporting* gamification over 15 weeks: autonomous motivation showed an **initial downward trend** | van Roy & Zaman 2018 |
| 7 | Perceived benefits of gamification **decline with duration of use** (novelty decay) | Koivisto & Hamari 2014 |
| 8 | Exposure to exemplary peers **undermined motivation** and caused **domain de-identification** | Rogers & Feller 2016 |
| 9 | Students in active-learning classrooms **learned more but felt they learned less** | Deslauriers et al. 2019 |
| 10 | Four-cluster MOOC engagement taxonomy **did not fully replicate** on a different platform | Ferguson & Clow 2016 |
| 11 | MOOC completion rates **did not improve over six years** despite platform-wide investment | Reich & Ruipérez-Valiente 2019 |
| 12 | Duolingo research corpus (35 studies, 2012–2020) is **design-focused rather than outcome-focused** | Shortt et al. 2021 |
| 13 | Time-on-task estimation is methodologically fragile enough to **invalidate learning-analytics findings** built on it | Kovanović et al. 2016 |
| 14 | High affective ChatGPT usage correlates with **increased indicators of dependence** | Phang et al. 2025 |

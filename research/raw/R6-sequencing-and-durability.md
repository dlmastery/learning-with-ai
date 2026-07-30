---
title: "Sequencing, durability, and the skills that live in the hands: where the order of topics comes from, what survives three years later, and what motor learning knows that we do not"
wave: R
section: R6
date_researched: 2026-07-30
sources_count: 58
status: raw-research
---

# R6 — Sequencing and Durability

> **The gap this report was commissioned to close.** `J1`'s personalisation engine computes a
> *"prerequisite closure of c, transitively closed"* and drops the learner back to the weakest
> link inside it. `F10` disclaims topic ordering by design. `A1` generates textbooks whose
> chapters must come in some order. Forty-five reports presuppose a prerequisite graph and not
> one of them says where it comes from, whether it is real, or what happens if you violate it.
>
> **Three findings, stated first.**
>
> 1. **The graph is real in one place and unproven almost everywhere else.** The one programme
>    that built an empirical ordering and then tried to break it — the early-mathematics learning
>    trajectories — found that teaching one level above a child beat skipping to the target level,
>    at **d = 1.20** in a trial of 291 kindergartners. All of those trials come from one
>    laboratory. Against that, the largest tally of automated sequencing experiments found **zero
>    of eight** studies sequencing interdependent content beat a hand-built baseline, and two
>    meta-analyses of the one deployed system built entirely on prerequisite structure put it at
>    **g ≈ 0.05** against ordinary teaching.
> 2. **Nobody has shown that a sequencing or mastery intervention's advantage survives.** Slavin's
>    1987 synthesis found mastery learning's *retention* effects "essentially zero," and that has
>    not been overturned in thirty-nine years. The best-documented early intervention here decayed
>    from about 0.8 SD to statistical zero by third grade, and the mechanism study on that trial
>    found forgetting explained only a quarter of the decay: most of the fade was the control
>    group catching up.
> 3. **Motor learning reached the performance–learning dissociation independently, and only half
>    of it replicated.** Contextual interference survives meta-analysis at **SMD = 0.63** overall
>    but collapses to **0.23** in applied settings and **0.02** in learners under 18. The
>    feedback-scheduling half of the doctrine does not survive at all: 75 comparisons, 2,228
>    participants, no effect at any timepoint and no reversal.
>
> The eleven-year-old this project is organised around is inside two of those boundary conditions
> at once. He is under eighteen and he is not in a laboratory.

---

## 0. Retrieval note (2026-07-30)

`WebSearch` returns `budget exhausted (200/200)` for this session, per `process/CLAUDE.md` §5;
two calls were spent confirming it. Retrieval therefore ran on ERIC (`api.ies.ed.gov`, the
workhorse and the only route to the special-education, mastery-learning and evaluation-report
literature), Crossref REST, Europe PMC, and `curl` against open-access PDFs.

- OpenAlex worked for about eight queries then hard-stopped with `HTTP 429`. It is metered by
  daily spend (`cost_usd: 0.001` per query, visible in the response envelope). Semantic Scholar
  returned `429` on nearly every call even at 6-second spacing and contributed one record.
- SAGE, Taylor & Francis and APA PsycNet returned `403` to `WebFetch`, blocking direct retrieval
  of Rupp & Templin (2007), Sun et al. (2021), Arthur et al. (2003) and Bahrick (1984). Each is
  handled below by a route that is stated at the point of use.
- **`files.eric.ed.gov/fulltext/ED*.pdf` serves to `curl`** and was the most productive route of
  the session: Slavin (1987) in full, both Clements grantee submissions, the TRIAD long-term
  conference paper, the Teach to One impact report, and two Annenberg working papers.
- `gwern.net/doc/psychology/spaced-repetition/` serves Bahrick & Phelps (1987) and Bahrick et al.
  (1993); the 1984 and 1991 papers are not mirrored there.

Evidence labels are the project standard. `MEASURED-RCT` · `MEASURED-META` · `OBSERVED` ·
`VENDOR` · `INFERENCE` · `SPEC`.

---

## 1. What the corpus assumed

Three reports build machinery that consumes an ordering, and none produces one.

`J1` §4 specifies `P ← prerequisite closure of c, transitively closed`, a rule that *"a rung is
interpretable only if every prerequisite it invokes is [held]"*, and a repair action,
`M2_prerequisite_dropback`, whose evidence line in `J1`'s own menu reads *"no pooled ES;
mechanism-level INFERENCE."* `F10` hands the ordering problem away in its first paragraph. `A1`
generates modules → chapters → topics. `C2` and `F5` own measurement machinery that could in
principle recover an ordering from response data and is not pointed at the task.

`Z1`'s census puts numbers on it: across 45 reports and 40 survey sections, `curriculum
sequencing` 2 hits, `scope and sequence` 1, `backward design` 0, `knowledge space` 0, `ALEKS` 2.
`prerequisite` appears 196 times. That is the shape of the problem: the concept is everywhere and
its warrant is nowhere. `OBSERVED — absence`

---

## 2. Learning trajectories: the one programme that built an ordering and then tried to break it

A learning trajectory in Clements and Sarama's sense is a triple: a goal, a hypothesised
developmental progression of levels of thinking, and instructional tasks matched to each level.
The claim under test is narrow and falsifiable: **instruction is most effective when it targets
the level one step above the child's current level of thinking.**

### 2.1 The efficacy trials

Clements, Sarama, Spitler, Lange & Wolfe (2011), *JRME*, ERIC EJ918252. Cluster-randomised,
42 schools serving low-resource communities, randomised block design, 1,375 preschoolers in 106
classrooms, three conditions. The Building Blocks curriculum, structured around the trajectories,
against business-as-usual: **g = 0.72** on the researcher-administered early-mathematics measure,
with classroom mathematics environment and teaching quality partially mediating.
`MEASURED-RCT`

Follow-through mattered more than the pre-K dose alone. **Sarama, Clements, Wolfe & Spitler
(2012)**, *JREE*, ERIC EJ961450: at the end of kindergarten, intent-to-treat **g = 0.33** with
follow-through and **g = 0.22** without; treatment-on-the-treated 0.38 and 0.30.
Clements, Sarama, Wolfe & Spitler (2013), *AERJ*, ERIC EJ1014930, reports at the end of the
third year **g = 0.51** (follow-through) and **g = 0.28** (no follow-through) against control,
with follow-through beating no-follow-through at **g = 0.24**. `MEASURED-RCT`

**A discrepancy I could not reconcile.** The 2013 published figures are *larger* than the 2012
end-of-kindergarten figures, which is not what "persistence of effects" ordinarily looks like,
and they do not line up with the trajectory reported in the same team's later long-term analysis
(§6.1), which has effects decaying monotonically from pre-K. The two analyses use different
models, different outcome instruments across grades, and different analytic samples. I could not
obtain both full texts to reconcile them and I am not going to smooth it over. **Anyone citing
"the Building Blocks persistence effect" should say which paper and which model.** `OBSERVED`

### 2.2 The decisive design: skip a level and see what breaks

This is the part that makes trajectories a scientific object rather than a curriculum convention,
and it is the closest thing the field has to a direct test of prerequisite ordering. In each
study, the counterfactual is not "no instruction" but *equal-dose instruction aimed straight at
the target level*, skipping the intervening levels.

- Clements, Sarama, Baroody, Joswick & Wolfe (2019), *AERJ*, ERIC EJ1234710, grantee
  submission ED594902. Early shape composition. Preschoolers at least two levels below the
  target received either trajectory-based instruction or an equal amount of instruction focused
  only on the target level. The trajectory group learned significantly more, **mainly on
  near-transfer items**, with no significant child-level moderators. `MEASURED-RCT`
- Clements, Sarama, Baroody & Joswick (2020), *ZDM* 52(4):637–648, ERIC EJ1261937. Addition
  and subtraction. Thirteen kindergartners in the trajectory condition against twelve in the
  skip condition, teaching experiments embedded in a quasi-experimental design. More children in
  the trajectory group showed greater learning. **n = 25 total.** This study is frequently cited
  as evidence for trajectories and it should not be cited without its sample size. `OBSERVED`
- Clements, Sarama, Baroody, Kutaka & Chernyavskiy (2021), *JEP* 113(7):1323–1337, ERIC
  EJ1318761, grantee submission ED619003. The one with power. **291 kindergartners** from four
  schools, randomly assigned to one-on-one instruction one level above their present level, or
  to one-on-one instruction on story problems three levels above their initial level.
  Baseline equivalence established (Cohen's d = .05 counting, .07 arithmetic). Dosage was
  equalised and non-significant between arms (196 minutes over 13.4 sessions versus 212 minutes
  over 14.3). The trajectory condition scored higher at posttest, **d = 1.20** for the main
  effect of condition in the baseline model, and the advantage was largest for children with low
  entry knowledge of arithmetic. Child gender and dosage were not significant moderators.
  `MEASURED-RCT`

**What this licenses.** For early arithmetic and early geometry, in one-to-one instruction, with
a level structure that has been validated against clinical interviews, the ordering carries real
instructional weight and the effect is large. It is also concentrated where a tutor would most
want it: on the children who arrive with the least.

**What it does not license.** All three studies come from the same research group, sharing
instruments, trajectory definitions and analytic conventions; two share four of five authors.
That is not a criticism of the work, it is a statement about what "replicated" means. The 2019
result was mainly on near transfer. The domains are early number and shape, where
developmental sequence is unusually constrained by what the arithmetic itself permits. Nothing
here establishes that a prerequisite graph over, say, secondary chemistry has the same standing.
`INFERENCE`

---

## 3. Is prerequisite structure empirically real, or is it curricular convention?

Four literatures bear on this, and they do not agree.

### 3.1 Learning progressions do not behave like levels

Learning progressions are the science-education cousin of trajectories: ordered descriptions of
how understanding of a concept develops. If the ordering is real, a student should sit *at* a
level and reason from it consistently.

Steedle & Shavelson (2009), *JRST*, ERIC EJ850695, tested this with latent class analysis on
diagnostic multiple-choice items about forces on an object moving at constant speed. Students
with a scientifically accurate understanding did reason systematically across items. **Many other
students did not**, and the authors' conclusion is that interpretations of learning-progression
level diagnoses "would often be invalid" on the progression they examined. `MEASURED-BENCH`

Alonzo & Steedle (2009), *Science Education*, ERIC EJ836037, found the same thing from the
other direction: students **do not respond consistently to similar problems set in different
contexts**, and misinterpretation of item language produces inaccurate level diagnoses for a
subset of students. Their own conclusion is that this matters less for classroom use than for
large-scale testing. `MEASURED-BENCH`

For a tutor this is the load-bearing warning. A system that places a learner at "level 3 of the
fractions progression" and routes the next hour of instruction from that placement is doing
large-scale testing whatever it looks like from the outside: a single-shot inference from a
handful of items, on a construct the measurement literature says is not stable enough across
contexts to carry it. `INFERENCE`

### 3.2 Q-matrices: the machinery exists and it is fragile

The formal object a tutor would need is a Q-matrix: items on the rows, latent skills on the
columns, a 1 where the item requires the skill. Cognitive diagnostic models such as DINA estimate
each learner's skill profile from responses given a Q-matrix. Two facts about them govern any
design that leans on this machinery.

First, Q-matrices can be validated against data and not only asserted by experts: de la Torre &
Chiu (2016), *Psychometrika* 81(2):253–273, `10.1007/s11336-015-9467-8`, give a general empirical
validation method, extended to sequential G-DINA by Ma & de la Torre (2019), *BJMSP*
73(1):142–163. `MEASURED-BENCH`

Second, misspecification is costly. Rupp & Templin (2007), *EPM* 68(1):78–96,
`10.1177/0013164407301545`, is the standard citation for what deleting or adding entries does to
parameter estimates and attribute classification accuracy in DINA; Kunina-Habenicht, Rupp &
Wilhelm (2012), *JEM* 49(1):59–81, covers log-linear diagnostic classification models. Both
publishers returned `403` to every route available here. **I did not obtain either paper's
numbers and am citing scope, not a result.** `OBSERVED — untraceable in this session`

The design consequence stands even without the numbers. An LLM asked to emit a prerequisite graph
for a topic is producing an expert-judgement Q-matrix with no validation step, in a formalism
whose known failure mode is that misspecification propagates into every individual classification
the system then makes. `INFERENCE`

### 3.3 The decisive tally: what happens when you actually sequence

Doroudi, Aleven & Brunskill (2019), *IJAIED* 29:568–620, `10.1007/s40593-019-00187-x`,
ERIC EJ1235264, reviewed every empirical study since the 1960s that compared a
reinforcement-learning-induced instructional policy against a baseline sequencing policy. Thirty-
six studies met inclusion. The headline is positive: 21 of 36 found at least one RL-induced
policy significantly better than all baselines, and the significant studies often reported
Cohen's *d* of 0.8 or more. `MEASURED-META`

The headline is not the finding. The authors cluster the studies by *what was being sequenced*,
and the clusters separate cleanly (their Table 2):

| Cluster | Sig | ATI | Mixed | Not sig | Sig worse |
|---|---|---|---|---|---|
| Paired-associate learning tasks | 11 | 0 | 0 | 2 | 1 |
| Concept learning tasks | 4 | 0 | 2 | 1 | 0 |
| Sequencing interdependent content | 0 | 0 | 2 | 6 | 0 |
| Sequencing activity types | 4 | 4 | 0 | 2 | 0 |
| Maximising other objectives | 2 | 0 | 0 | 0 | 0 |

The third row is curriculum sequencing. It is the cluster the authors describe as "closest to
traditional curriculum sequencing, or ordering various content areas for a given topic," and the
one where "a network specifying the relationship between different content areas or KCs (such as
a prerequisite graph) must either be prespecified or automatically inferred from data." **Zero of
eight beat their baselines.** The nulls include Clement et al. (2015) with 133 seven-to-eight
year-olds on arithmetic, Doroudi et al. (2017) with 69 fourth and fifth graders on fractions, and
the authors' own Appendix B study with 100 more. `MEASURED-META`

Meanwhile the two clusters that *did* work are the ones where the sequencing decision is about
when to bring an item back (paired-associate scheduling, which is the spacing literature
`F11` already owns) and what kind of activity to give next for fixed content (worked example
versus problem, which is `J1`'s territory). Both are decisions about time and modality within a
fixed topic. Neither is a decision about which topic comes next.

**`J1` should read that table as a verdict on its own architecture.** Selecting techniques for a
given content target is the part with evidence behind it. The graph traversal that selection is
wrapped in is the part with no positive evidence anywhere. `INFERENCE`

### 3.4 ALEKS: the deployed system whose whole premise is prerequisite structure

Knowledge space theory, due to Doignon & Falmagne (collected in *Knowledge Spaces*,
Springer 1999, `10.1007/978-3-642-58625-5`), models a domain as a family of *knowledge states* —
the sets of problems a learner could plausibly be able to solve — closed under union. The
"outer fringe" of a state is the set of items the learner is ready to learn next. ALEKS
is the commercial instantiation.

**The vendor's own claims are about mechanism, not outcome.** `aleks.com/about_aleks/research_behind`
(retrieved 2026-07-30) describes the theory, the NSF funding, and the claim that the system can
assess a knowledge state "after the student has answered only 20–25 questions" and determine
"precisely what each individual student knows, and what the student is ready to learn next." It
cites no efficacy study and reports no effect size. `VENDOR`

**Two independent meta-analyses reach the same place.**

- Fang, Ren, Hu & Graesser (2019), *Educational Psychology*, ERIC EJ1232632. 15 studies,
  24 independent samples, 2005–2015. Conclusion: ALEKS was **as good as, but not better than,
  traditional classroom teaching**. Effect sizes did not differ by schooling level, by
  implementation type, or by standardised versus instructor-designed outcome, and were *larger
  for shorter* implementations. `MEASURED-META`
- Sun, Else-Quest, Hodges, French & Dowling (2021), *Investigations in Mathematics Learning*,
  ERIC EJ1314175. 33 studies, 56 independent effect sizes, **9,238 students**, 2000 to August
  2020. Pooled **Hedges' g = 0.05**, with ALEKS "especially effective when used to supplement
  traditional instruction" at **g = 0.43**. `MEASURED-META`
  *Caveat on the interval.* The ERIC record prints the pooled CI as `[-0.01, 0.20]` and the
  supplemental CI as `[0.02, 0.83]`; the first is not symmetric about 0.05 and the publisher
  returned `403`, so I could not check it against the article. **Cite the point estimates; do not
  cite that interval without checking the paper.** `OBSERVED — untraceable in this session`

**These two are not independent.** Sun et al.'s window subsumes Fang et al.'s and the study
pools certainly overlap. What survives is that no meta-analysis of the flagship prerequisite-
structured system finds a general advantage over ordinary teaching, and that its one positive
moderator is a dosage result: adding a supplementary practice system to teaching beats teaching
alone. `INFERENCE`

**Cross-reference, not duplication.** `F11` §(vii) already carries the strongest single datum on
the inside of ALEKS: Matayoshi, Cosyn, Uzun & Kurd-Misto (2025), *JEDM* 17(1), 32.9 million
randomised topic sequences in production, in which the high mastery threshold cost **+29% time**
for a retention difference of **under 0.02** on a base rate near 0.60. And Prihar et al. (2022),
50 RCTs in ASSISTments, found the mastery threshold's measurable effect ran through assignment
dropout and not through learning. Read together with §3.3: inside a fixed topic, how hard you
push mastery barely matters; across topics, which order you use has never been shown to matter
either.

### 3.5 What would decide it

No study located here took an assumed prerequisite ordering in a real domain, randomised
learners to respect or violate it, and measured delayed transfer. The Clements skip-level trials
come closest and operate at the scale of one trajectory in one domain under one-to-one
instruction; the Doroudi cluster randomises the *policy* traversing the graph, not the graph.
§9.2 specifies the missing trial. `OBSERVED — absence`

---

## 4. Mastery-based sequencing against the spiral, and what the two-sigma claim rests on

`B1` §7 already grades Bloom's 2σ "F as usually stated" and `F10` §2 already establishes that
Bruner's spiral is cited constantly and evidenced thinly. Two things those sections do not
contain belong here.

### 4.1 The number under the number

Slavin's 1987 synthesis (recovered in full as ERIC ED294891; published as *RER* 57(2):175–213,
`10.3102/00346543057002175`) sets out the claims it was testing, in the claimants' own figures:
Kulik et al. reported mean effect sizes of **0.52** pre-college and **0.54** college; Guskey &
Gates claimed **0.94 / 0.72 / 0.65** by level; Walberg **0.81** for science mastery learning;
Bloom himself claimed an effect size of **1.00** "when mastery learning procedures are done
systematically and well," and predicted that mastery learning would consistently reach two sigma.

Against that, Slavin restricted to practical applications in real schools running at least four
weeks, with equal time for treatment and control, on standardised measures. Seven studies
qualified. **Median effect size = +0.04.** The single non-trivial result in the set (+0.25) came
from a study in which teachers self-selected into conditions or were assigned by their principals,
and was not significant at the class level. `MEASURED-META`

Slavin's summary judgement is worth having verbatim, because it is more precise than "mastery
learning does not work": the evidence supports the *weak* claim that mastery learning "can be an
effective means of holding teachers and students to a specified set of instructional objectives"
and does not support the *strong* claim that it beats traditional instruction "given equal time
and fair achievement measures."

He also notes why the corrective loop may under-deliver, which reads as a specification for what
an AI tutor could change: in none of the sixteen studies did corrective instruction occupy more
than **one period per week, or 20% of instructional time**, and it was delivered in groups or by
peer tutors. Mastery learning has never been tested with unlimited individual corrective
instruction, because until now nobody could afford to. `INFERENCE`

### 4.2 The provenance detail that matters most

Bloom's two-sigma essay rests on University of Chicago dissertations, principally Anania and
Burke. Slavin's methods section supplies the design facts that the essay's citation trail
usually drops: **Anania's study ran three weeks**, with one period each week set aside for
corrective instruction. All the Chicago dissertations Bloom cited "provided the mastery learning
classes with similar amounts of additional instruction," amounting to 20–33% more time than
control classes received. Bloom's own characterisation of this was that "the time or other costs
of the mastery learning procedures have usually been very small." `OBSERVED`

A three-week experiment with a 20–33% time advantage for the treatment arm and author-written
outcome measures is the foundation of the most-cited number in educational technology.
`B1`'s grade stands and this is the evidence behind it.

### 4.3 The mastery finding nobody quotes

Slavin also examined maintenance: six comparisons in five studies assessed retention 4–12 weeks
out, all on experimenter-made measures. **The median effect size overall is essentially zero**,
and the largest retention effect (+0.49) came from the one study that had found no differences on
standardised measures. `MEASURED-META`

This is the hinge between this report's two commissions. The strongest claim mastery-based
sequencing makes is that by refusing to advance you build something that lasts. That claim has
been tested, at least in group-based form, and it did not hold. Thirty-nine years later I could
locate no synthesis that overturns it. `OBSERVED — absence`

### 4.4 Spiral against mastery

`F10` §2 covers the spiral's evidence base and I will not repeat it. Two additions. The *direct*
comparison literature is thin and partisan: Snider (2004), *Journal of Direct Instruction*, ERIC
EJ755132, argues for "strand" against spiral organisation and is an argument, not an evaluation.
`OBSERVED`

And the empirically strong descendant of the spiral is interleaving, which the corpus already
covers at depth (46 occurrences across `F11`, `N2`, `B1`, including Brunmair & Richter's 2019
moderator meta-analysis and Nemeth et al.'s 2019 null in elementary mathematics). Interleaving is
a *within-topic* scheduling decision of the kind §3.3 shows pays; "spiral curriculum" is a
*between-topic* ordering decision of the kind that has never been shown to. Bruner and Battig are
not making the same claim and the evidence separates them the same way. `INFERENCE`

---

## 5. The required null: a sequencing-first model, three years, five schools, nothing

**Ready, Conn, Bretas & Daruwala (2018/2019), Consortium for Policy Research in Education,
Teachers College, ERIC ED618425.** "Final Impact Results from the i3 Implementation of *Teach to
One: Math*."

Teach to One is the purest deployed instantiation of the thesis this report is testing: a daily
algorithmic scheduler assigns each student the mathematics content their diagnosed skill state
says they are ready for, in whatever modality suits it, breaking the grade-level sequence
entirely. New Classrooms ran it under an Investing in Innovation grant in five schools in
Elizabeth, New Jersey, for three academic years from September 2015.

CPRE ran a comparative interrupted time series against 16 non-Teach-to-One schools in the same
district. **36,158 student-level measurements** nested in 209 school-by-year cohorts. Outcome
z-scored within grade and year. Adjusted treatment estimates, with standard errors:

| Implementation year | Estimate (SD) | SE |
|---|---|---|
| Year 1 (2015–16) | +0.062 | 0.089 |
| Year 2 (2016–17) | −0.113 | 0.087 |
| Year 3 (2017–18) | −0.170 | 0.087 |

All three are statistically non-significant; the unadjusted estimates trace the same V-shape. The
report's own summary: "the results of the CITS models were statistically non-significant in each
of the three implementation years." `MEASURED-BENCH` (quasi-experimental; CITS, not randomised)

Two things make this the right null to give space to. It is a three-year funded deployment of
the architecture a "school in a box" would build, not a laboratory manipulation. And the point
estimates drift *downward* across the three years, the opposite of the implementation-maturity
curve every adaptive-sequencing vendor forecasts.

A second null in the same family: KinderTEK, an iPad mathematics program with individualised
progression, cluster-randomised across 70 kindergarten classrooms, **1,368 students**. No
significant differences on early number fluency, broad mathematics achievement, or proximal math
content. ERIC ED679597, grantee submission, forthcoming in *IJTE*. `MEASURED-RCT`

---

## 6. What happens after

`B2` owns the absence: nobody measures retention. Here is the positive treatment.

### 6.1 The best-documented fade-out in the corpus is the corpus's own best sequencing result

The TRIAD trial (§2.1) was followed to fifth grade. **Clements, Sarama, Layzer, Unlu & Wolfe
(2016)**, SREE conference paper, ERIC ED567218, reports the trajectory in standard deviations:

| Timepoint | TRIAD follow-through | TRIAD no-follow-through |
|---|---|---|
| End of pre-K | 0.86 | 0.75 |
| End of kindergarten | ≈ 0.4 SD lower than pre-K, still significant | ≈ 0.4 SD lower, still significant |
| End of grade 1 | ≈ 0.2 SD lower again; significant at *p* < .10 for FT only | not significant |
| Grades 3 and 4 | not distinguishable from zero | not distinguishable from zero |
| End of grade 5 | 0.26 (significant) | 0.21 (significant) |

`MEASURED-RCT` (conference paper; the published version is **Clements, Sarama, Layzer & Unlu
(2023)**, *JRME*, ERIC EJ1372925, `10.5951/jresematheduc-2020-0245`, whose abstract states that
"early effects on mathematics achievement decreased through fourth grade but reemerged at fifth
grade." **The numeric trajectory above is from the conference paper and should be labelled as
such; the published paper is the citation of record for the pattern.**)

The re-emergence is the interesting part. The authors read it as effects reappearing "at two
critical points in elementary education — the transitions to the increasing demands of the
curricula of first and fifth grades," so that early foundations show up when the curriculum
finally asks for them. That *latent foundation* reading makes a falsifiable prediction: fade-out
measured on a test that does not demand the foundation is not evidence the foundation is gone.

The subgroup pattern cuts against the usual story. Effects for higher-SES students in the
no-follow-through condition were significant at every timepoint and reached 0.6–0.7 SD in fourth
and fifth grade; lower-SES students' effects were significant only in pre-K and kindergarten.
Durability was greatest where the sustaining environment was strongest. `OBSERVED`

### 6.2 The mechanism study, on the same trial

Kang, Duncan, Clements, Sarama & Bailey (2019), *JEP*, ERIC EJ1213721, decomposed the fade.
Children who received the intervention forgot more in the following year than children who
did not — but forgetting accounted for **only about one quarter** of the fade-out. An offsetting
transfer effect was small and statistically non-significant, worth roughly one tenth of the
end-of-program treatment effect. The authors' conclusion: **most of the fade-out was the control
group catching up.** `MEASURED-RCT`

This changes what fade-out means for a product. If most of the decay is convergence and not
loss, an early tutoring advantage is largely an *acceleration*, and the durable question becomes
whether acceleration is worth anything on its own. Measuring "did the learner retain it" against
a control group also answers a different question from "does the learner still have it," and the
corpus has been conflating them.

### 6.3 How general is fade-out?

Watts, Hart & Bailey (2025), EdWorkingPaper 25-1366, Annenberg Institute, ERIC ED678313.
87 randomised trials of educational interventions across developmental stages, **1,459 follow-up
effect sizes**. Average impact **0.21 SD at posttest**, falling to **0.07 SD at follow-up**
(*p* < .01), with longer-run estimates hovering near 0.10 SD and imprecisely estimated. The
authors tested widely held theories about which intervention features predict persistence and
found that "salient features of interventions explained only a small portion" of the variation.
`MEASURED-META` — **working paper, not peer-reviewed; discounted accordingly.**

A companion working paper, Rosengarten, Hart, Bailey, McCormick & Lovett (2024),
EdWorkingPaper 24-1069, ERIC ED672296, tested the popular "constrained skills" explanation — that
impacts on skills everyone eventually masters should fade while impacts on open-ended skills
persist. Across the same meta-analytic database, they **found no evidence** that unconstrained
skills persisted better; in some specifications the sign ran the other way. `MEASURED-META`
— **working paper.**

The peer-reviewed anchor is Bailey, Duncan, Odgers & Yu (2017), *JREE*, ERIC EJ1125358, which
sets out three competing mechanisms — skill-building, foot-in-the-door, sustaining environments —
that generate competing predictions about *when* and *whom* to target. Both sides have numbers:
Pages, Protzko & Bailey (2022), *JREE*, ERIC EJ1349873, found Abecedarian's impacts on IQ
subtests from age 5 to 21 (n = 107) consistent with a persistent effect on general ability, with
subtest-specific variance fading. Which one you observe depends on how broad the measured
construct is. `MEASURED-RCT`

### 6.4 What actually survives: the permastore work

The fade-out literature measures a *relative advantage against a control group*. The Bahrick
programme measures what is more directly relevant to a tutor's promise: **absolute retention of
formally taught material across decades**.

Bahrick (1984), *JEP: General* 113(1):1–29, `10.1037/0096-3445.113.1.1`, is the cross-
sectional study of Spanish learned in school and tested up to fifty years later. The publisher
blocked retrieval; I am characterising it through Bahrick's own restatement in
Bahrick & Phelps (1987), *JEP:LMC* 13(2):344–349, which I did obtain:

> "A portion of the acquired knowledge has a life span of more than 25 years even if the knowledge
> is not rehearsed or accessed during that long interval. Another part of the originally acquired
> knowledge is lost within 5 years after training terminates, and **virtually no knowledge is lost
> during the interval between 5 and 25 years** following acquisition."

`OBSERVED` — the shape of the curve is a steep drop for roughly five years and then a plateau.
Bahrick's later summary adds that the size of the surviving portion "depended on the total amount
and the distribution of practice."

Bahrick & Phelps (1987) itself: 35 individuals who had learned and relearned 50
English-Spanish word pairs, tested for recall and recognition after 8 years. Two variables
predicted permastore retention — the spacing between relearning sessions and the number of
presentations needed to encode a pair — and together they spanned a range from **0% to 23%
recall**. Optimum recall came from words encoded in 1–2 presentations and accessed at intervals
of **30 days**. `MEASURED-RCT`

Bahrick, Bahrick, Bahrick & Bahrick (1993), *Psychological Science* 4(5):316–321, is the
9-year longitudinal follow-up. Four subjects, 300 English-foreign word pairs, 13 or 26
relearning sessions at intervals of 14, 28, or 56 days, retention tested at 1, 2, 3 and 5 years.
Longer intervals slowed acquisition slightly. The retention functions **crossed over during the
first year** and stayed crossed for five: recall became lowest for the 14-day interval and
highest for the 56-day interval. **Thirteen sessions spaced at 56 days yielded retention
comparable to 26 sessions spaced at 14 days** — half the training for the same durable outcome.
Five-year recall reached 40% (13 sessions) and 54% (26 sessions) at a 28-day interval, against
15% at eight years in the 1987 study with seven sessions.

Two cautions the citation trail usually drops. **n = 4.** And the authors record frequent
departures from schedule, unscheduled extra sessions, an omitted terminal session, a three-year
test given at four years, and subjects who travelled in France or watched films in the target
language. `MEASURED-RCT` — extraordinary in duration, tiny in sample, imperfectly controlled.

The authors themselves reach for Schmidt & Bjork (1992) to explain the crossover, which is where
this report's third commission begins.

---

## 7. Transfer to work

`transfer to work` is 0 hits in the corpus, and close to 0 in the literature in the sense that
matters.

**The best evidence is medical and it states its own limits.** Vermylen, Cohen, Cook, McGaghie,
Issenberg, Kessler et al. (2025), *Simulation in Healthcare*, `10.1097/sih.0000000000000895`,
PMID 41217357, is a systematic review and meta-analysis of competency-based (mastery) simulation
education for medical procedural skills across many domains and professions. In the authors'
summary statement, competency-based simulation beats non-competency-based simulation for skill
outcomes (large effect), while "outcomes are favorable, but small, for behaviors in practice and
patient effects." **No instructional design feature** they examined significantly affected skill
acquisition, and they name the gap: "a limited number of studies assessing the impact on
behaviors in practice and patient effects." `MEASURED-META`

That is the whole transfer-to-work story in one sentence: mastery sequencing reliably produces
the measured skill, and the further you get from the measurement the smaller it becomes.

**The lifecycle result nobody in edtech cites.** Hanushek, Schwerdt, Woessmann & Zhang, "General
Education, Vocational Education, and Labor-Market Outcomes over the Lifecycle," *Journal of Human
Resources* 52(1):48–87, `10.3368/jhr.52.1.0415-7074r`. Using International Adult Literacy Survey
micro-data for 18 countries, a difference-in-differences comparison of employment rates across
ages finds that the early employment advantage of vocational education decreases with age, and
that the trade-off is "most pronounced in countries emphasizing apprenticeship programs." Robust
to ability controls and propensity-score matching. `OBSERVED` (quasi-experimental)

This is the durability question asked of an entire education system, and the answer is that the
most job-transferable curriculum is the one whose advantage decays fastest. Any product promising
"skills for the job you want" is choosing a point on that curve whether it knows it or not.

**The untraceable number.** The claim that "only 10% of training transfers to the job" is
ubiquitous in corporate learning and has appeared in edtech decks for two decades. It traces to
Georgenson (1982), where it was, in the words of the paper that chased it down, a
**"conversational gambit"** and not an estimate. Farrington (2011), "Training Transfer: Not the
10% Solution," *Performance Improvement Quarterly*, ERIC EJ921207, documents the provenance and
concludes that assigning a general effect size for training transfer is "far from simple."
Fitzpatrick (2001), "The strange case of the transfer of training estimate," and Saks's (2002)
reply are indexed in PsycEXTRA (`10.1037/e576912011-002`, `10.1037/e576922011-004`); the SIOP
newsletter page for the Fitzpatrick article returned only site navigation to `WebFetch`, so I
have the record and not the text. **Do not cite the 10% figure. It has no study behind it.**
`OBSERVED — untraceable`

**What is absent.** No study located in this session followed learners from an instructional
intervention through to measured job performance with a randomised design outside of health
professions education. Arthur, Bennett, Edens & Bell (2003), *JAP* 88(2):234–245,
`10.1037/0021-9010.88.2.234`, is the standard meta-analysis of organisational training
effectiveness by Kirkpatrick criterion and would be the right anchor; **I could not obtain its
effect sizes** (APA `403`; the DTIC technical-report mirror returned an HTML error page rather
than the PDF) and I am not quoting numbers I did not read. `OBSERVED — untraceable in this
session`

---

## 8. The skills that live in the hands

`Z1` row 15 is right that the corpus covers manipulatives and simulation and not motor learning.
The reason to close that gap is not completeness: this corpus's central empirical theme, that
felt learning and real learning dissociate, appears to have been discovered twice. The question
is how much of that convergence survives inspection.

### 8.1 The convergence, stated carefully

`F11` already imports Schmidt & Bjork (1992), *Psychological Science* 3(4):207–218,
`10.1111/j.1467-9280.1992.tb00029.x`, and quotes its thesis: "Manipulations that maximize
performance during training can be detrimental in the long term; conversely, manipulations that
degrade the speed of acquisition can support the long-term goals of training." `F11`'s worked
example is Shea & Morgan (1979).

**That paper is a unification, not an independent replication, and the corpus should say so.**
Robert Bjork is an author of Schmidt & Bjork (1992) and the originator of the desirable-
difficulties framework on the verbal side. A paper that argues two literatures agree, co-authored
by the person whose framework one of them is, cannot be counted as the two literatures agreeing.
`INFERENCE`

What *is* independent is the empirical work. Shea & Morgan (1979), *JEP: Human Learning and
Memory* 5(2):179–187, `10.1037/0278-7393.5.2.179`, ran in a motor-behaviour laboratory on a
barrier-knockdown task, in a tradition descending from Battig (1966), with no methodological
contact with the verbal spacing literature. Blocked practice won during acquisition; random
practice won at 10-minute and 10-day retention, and won whether the retention test was itself
blocked or random. That is an independent arrival at the same dissociation, from a different
discipline, on a different response system. `MEASURED-RCT`

The right claim is therefore narrower than "two literatures converged" and stronger than nothing:
**one specific manipulation, contextual interference, reproduces the acquisition–retention
reversal in a discipline that did not borrow it.** Whether the *rest* of the motor doctrine
reproduces is a separate question, and the answer is largely no.

### 8.2 Contextual interference under meta-analysis, with the boundary conditions

Czyż, Wójcik, Solarská & Kiper (2024), *Scientific Reports* 14, "High contextual interference
improves retention in motor learning: systematic review and meta-analysis,"
`10.1038/s41598-024-65753-3`. 1,255 records screened, 294 full texts, **54 studies in the
meta-analysis**, delayed retention (>24 h) only. Two models were fitted: a three-level mixed model
and a random-effects model on study-averaged effects. `MEASURED-META`

| Subgroup | Three-level SMD | 95% CI | Notes |
|---|---|---|---|
| Overall | 0.63 | 0.33, 0.93 | 0.43 (0.19, 0.67) after outlier removal; random-effects model gives 0.71 |
| Laboratory settings | 0.92 | 0.48, — | random-effects model 0.99 |
| Applied settings | 0.23 | −0.16, 0.62 | after outlier removal −0.01 (−0.35, 0.32), *p* = .94, favouring blocked |
| Under 18 ("young") | 0.02 | −0.90, 0.94 | *p* = .97; 49 effect sizes, 418 participants |
| Adults (18–59) | 0.63 | 0.30, 0.96 | 119 effect sizes, 1,425 participants |
| Older adults (≥60) | 1.45 | 0.55, 2.35 | 24 effect sizes, 205 participants |

Heterogeneity is high throughout (I² in the 62–83% range where reported).

**Two of those rows are the ones a tutor for an eleven-year-old must read.** In applied settings —
gyms, courts, clinics, anything that is not a laboratory task — the effect is not distinguishable
from zero and flips sign under outlier removal. In learners under 18 it is 0.02.

This is not an artefact of the meta-analysis. Wulf & Shea (2002), *Psychonomic Bulletin & Review*
9(2):185–211, `10.3758/BF03196276`, found the same pattern in the primary studies twenty years
earlier: French, Rink & Werner found no differential effect of blocked, random or mixed schedules
for ninth-graders learning volleyball; Farrow & Maschette found random practice better for 10–12
year-olds and **blocked practice better for 8–9 year-olds** on the tennis forehand; Pinto-Zipp &
Gentile found blocked practice benefited 5–6 year-olds and random practice benefited adults on
frisbee throwing; Al-Mustafa found the same age split on a throwing task. Albaret & Thon
manipulated task complexity directly with drawing tasks of varying segment counts: a clear
random-practice advantage on the simplest version, "systematically reduced as the number of
segments was increased and even reversed" for the hardest. `MEASURED-META`

Wulf & Shea's synthesis is the mechanism: high contextual interference helps when the learner has
spare processing capacity and hurts when they do not. Their title is the warning label —
*Principles derived from the study of simple skills do not generalize to complex skill learning.*

### 8.3 The half that did not replicate: feedback scheduling

The other pillar of the motor-learning dissociation is the guidance hypothesis (Salmoni,
Schmidt & Walter, 1984): augmented feedback after every trial functions like physical guidance,
propping up performance during acquisition while preventing the learner from developing intrinsic
error detection, so that reduced-frequency feedback should lose during practice and win at
retention. This is the source of the "fade the feedback" advice in every motor-learning textbook,
and it is the instance `F11` §5 already flagged as cutting against its own guidance on corrective
feedback.

McKay, Hussien, Vinh, Mir-Orefice, Brooks & Ste-Marie (2022), *Psychology of Sport and
Exercise* 61:102165, `10.1016/j.psychsport.2022.102165` (preprint `10.31234/osf.io/v2cp7`, from
which the text below is quoted). 1,662 records screened; **61 papers, k = 75, N = 2,228**.

> "Results revealed substantial heterogeneity but no significant moderators, high levels of
> uncertainty, and **no significant effect of reduced feedback frequency at any time point.**
> Further, multilevel analyses revealed **no evidence of a significant change in effect from
> acquisition or immediate retention to delayed retention.** Z-curve analysis suggested the
> included studies were severely underpowered."

Their own highlight list ends: "The guidance hypothesis is not supported by the extant research."
`MEASURED-META`

**The same group's other two results complete the picture.** McKay, Yantha, Hussien, Carter &
Ste-Marie (2022), *Meta-Psychology* 6, `10.15626/mp.2021.2803`, on self-controlled practice: a
naive random-effects model over 52 comparisons (N = 2,061) gives **g = 0.44** (95% CI 0.31, 0.56),
but published and unpublished findings differ significantly with only the published ones showing
a benefit, a selection-corrected weight-function model puts the true average at **g = 0.107**
(95% CI 0.047, 0.18), and p-curve analysis "suggested a lack of evidential value."
`MEASURED-META` The preregistered test agrees: St. Germain, McKay, Poskus, Williams, Leshchyshen,
Feldman, Cashaback & Carter (2023), *Psychonomic Bulletin & Review* 30:621–633,
`10.3758/s13423-022-02170-5`, **N = 228** across two experiments, "did not find any evidence to
support a self-controlled learning advantage." `MEASURED-RCT`

### 8.4 Massed against distributed motor practice: located, not quoted

The canonical meta-analyses are Lee & Genovese (1988), *RQES* 59(4):277–287, and its follow-up
Lee & Genovese (1989), *RQES* 60(1):59–65, whose title names the central moderator —
*Different Effects for Discrete and Continuous Tasks* — and Donovan & Radosevich (1999), *JAP*
84(5):795–805, "A meta-analytic review of the distribution of practice effect: Now you see it,
now you don't," whose title names its own.

**I could not obtain the pooled estimates from any of the three** (Taylor & Francis and APA both
`403`; OpenAlex exhausted). Their DOIs and titled findings are in the source list; no numbers are
attached to them here. `OBSERVED — untraceable in this session`

What can be said without them, from Wulf & Shea's review: distribution of practice is one of the
variables they list as characterised almost entirely on simple laboratory tasks, so it falls under
the same complexity caveat as contextual interference.

### 8.5 What the analogy licenses

`K1`'s compression argument is derived from cognitive encoding. Here is the boundary, stated as a
design constraint rather than a disclaimer:

1. **The dissociation itself is real and independently arrived at.** Practice conditions that
   flatter performance during acquisition can degrade retention. Shea & Morgan established it in
   a discipline with no contact with verbal spacing research. `MEASURED-RCT`
2. **One of its two named instances does not survive meta-analysis.** Feedback frequency shows no
   effect and no reversal at k = 75. A designer who "fades feedback because that is what the
   motor literature says" is following a textbook, not a finding. `MEASURED-META`
3. **The surviving instance has boundary conditions that exclude this project's organising
   learner.** Applied settings: 0.23 falling to −0.01. Under-18: 0.02. Complex tasks with novice
   performers: reversed. `MEASURED-META`
4. **The mechanism that explains all four rows is capacity, and it is the same mechanism the
   corpus already runs on.** Desirable difficulty is desirable exactly to the extent that the
   learner has capacity left to meet it, which is `J1`'s expertise-reversal law and `N2`'s
   executive-function argument arriving from a third direction. `INFERENCE`

Point 4 is the transferable claim. Points 1–3 are the reason not to state it as "motor learning
confirms our theory."

---

## 9. What is buildable, what to run, and what I could not find out

### 9.1 Buildable now

**A prerequisite graph with a stated epistemic status on every edge.** Edges come in three kinds
and a system that treats them alike will be wrong in a specific way. *Constitutive* edges are
entailed by the domain's own logic (you cannot compose shapes you cannot recognise). *Empirical*
edges are ones a Clements-style skip-level trial has tested. *Conventional* edges are everything
else, which is most of them. `SPEC`

**A graph that is used for diagnosis and not for gating.** §3.3's tally is the design rule: the
sequencing decisions with positive evidence are within-topic (when to revisit, what activity type
to give next), and the between-topic ones have none. `J1`'s `M2_prerequisite_dropback` is
therefore the *right* use of a graph — triggered by a diagnosed error, aimed at a named missing
component — and "the learner may not proceed to c until the closure of c is verified" is the
wrong one. The corpus can adopt the first and should drop the second until it is tested. `SPEC`

**A durability instrument, because nobody has one.** Kang et al. show that a control-referenced
retention measure answers the wrong question. A tutor can do what no trial could afford: schedule
unannounced delayed transfer probes at 30, 90 and 365 days on material the learner has stopped
studying, on freshly generated items, and report *absolute* retention alongside any comparative
claim. Bahrick & Phelps's 30-day optimum and the 1993 crossover give the schedule a starting
shape. `SPEC`

**A capacity gate on every difficulty manipulation.** Contextual interference, feedback fading and
practice distribution should all be treated as capacity-conditional and defaulted *off* for
novices, for complex tasks, and for learners under 18 — which for this project's organising
learner means off by default and earned by measurement. `SPEC`

### 9.2 The single highest-value experiment

**Randomise the graph, not the policy.** Every existing study randomises which traversal policy
walks a fixed graph. The untested question is whether the graph earns its cost.

*Design.* Within-learner, topic-level randomisation, mirroring Matayoshi et al.'s production
design. For each learner, each eligible topic is randomly assigned to graph-respecting entry
(the tutor verifies the prerequisite closure and remediates any gap before teaching the target)
or demand-driven entry (the tutor teaches the requested target immediately and repairs
prerequisites only reactively, when an error diagnoses a specific missing component). Total
instructional time is capped identically in both arms, which is the condition Slavin showed
almost no mastery-learning study met.

*Primary outcome.* Delayed transfer at 28 days on freshly generated items for the target topic,
scored blind. *Secondary.* Time to criterion; a 90-day retention probe; and the proportion of
graph-respecting sessions in which the verified prerequisite gap turned out to be real.

*Framing and power.* The question is not whether there is a difference — the ALEKS threshold
experiment found a real but negligible one across 32.9 million sequences — but whether any
difference is large enough to pay for the graph. So this is an **equivalence trial** with a
pre-registered margin of **δ = 0.10 SD**, roughly Kraft's small-effect benchmark and below the
smallest difference that would change the design. Two one-sided tests, α = .05, power 90%, paired
within learner with a between-condition correlation of 0.5 gives σ_d ≈ 1.0 SD and
n ≈ (1.645 + 1.282)² / 0.10² ≈ **857 learners**, each contributing at least eight topic pairs.
At a correlation of 0.7, σ_d falls to ≈ 0.77 and n to ≈ 510. Budget 900 learners × 8 pairs:
about 7,200 topic sequences, roughly two terms of a mid-sized deployment and four orders of
magnitude smaller than the ALEKS study.

*Why this one.* No other design returns a result the corpus cannot get anywhere else. If the
graph is equivalent within 0.10 SD, `J1` should stop computing prerequisite closures and `A1`'s
generative-textbook problem collapses from "construct a validated ordering" to "answer the
question that was asked." If the graph wins by more than 0.10 SD, the corpus has its first direct
warrant for an architecture four reports already assume.

### 9.3 What I could not find out

- **Whether prerequisite orderings are real outside early mathematics.** The only skip-level
  trials in existence are in early number and early shape, from one laboratory. Nobody has run
  the design in secondary algebra, chemistry, programming, or a second language.
- **The pooled estimates from Lee & Genovese (1988, 1989) and Donovan & Radosevich (1999)**, and
  with them the size and moderators of the massed-versus-distributed effect in motor learning.
  Publisher `403`s; recorded as untraceable rather than guessed.
- **Rupp & Templin's (2007) numbers** on how badly a misspecified Q-matrix degrades attribute
  classification — the quantitative form of the risk in letting a language model emit a graph.
- **Arthur et al.'s (2003) effect sizes by Kirkpatrick criterion**, and any defensible general
  number for how much organisational training reaches job behaviour. The quoted 10% figure is a
  1982 conversational aside and should never be cited.
- **Whether the ALEKS pooled interval in Sun et al. (2021) is as printed in ERIC.** The point
  estimate (g = 0.05) is safe; the interval is not.
- **Whether Building Blocks' third-year effects are 0.51/0.28 or the ≈0.26 implied by the
  long-term analysis.** Two papers, same team, same trial, and the abstracts and conference paper
  did not reconcile them.
- **Anything about transfer from instruction to job performance outside health professions
  education.** The largest measured absence in this report. The trial that would settle it —
  randomise instructional sequence, follow to employment, measure supervisor-rated performance at
  12 and 36 months — has, so far as this session's retrieval establishes, never been run.

---

## Sources

**Learning trajectories and Building Blocks**

1. Clements, D. H., Sarama, J., Spitler, M. E., Lange, A. A., & Wolfe, C. B. (2011). Mathematics learned by young children in an intervention based on learning trajectories: A large-scale cluster randomized trial. *JRME* 42(2). ERIC EJ918252. `MEASURED-RCT`
2. Sarama, J., Clements, D. H., Wolfe, C. B., & Spitler, M. E. (2012). Longitudinal evaluation of a scale-up model. *JREE*. `10.1080/19345747.2011.627980`, ERIC EJ961450. `MEASURED-RCT`
3. Clements, D. H., Sarama, J., Wolfe, C. B., & Spitler, M. E. (2013). Persistence of effects in the third year. *AERJ* 50(4). `10.3102/0002831212469270`, ERIC EJ1014930. `MEASURED-RCT`
4. Clements, D. H., Sarama, J., Baroody, A. J., Joswick, C., & Wolfe, C. B. (2019). Evaluating the efficacy of a learning trajectory for early shape composition. *AERJ*. `10.3102/0002831219842788`, ERIC EJ1234710 / ED594902. `MEASURED-RCT`
5. Clements, D. H., Sarama, J., Baroody, A. J., & Joswick, C. (2020). Efficacy of a learning trajectory approach compared to a teach-to-target approach. *ZDM* 52(4):637–648. `10.1007/s11858-019-01122-z`, ERIC EJ1261937 / ED619220. `OBSERVED` (n = 25)
6. Clements, D. H., Sarama, J., Baroody, A. J., Kutaka, T. S., & Chernyavskiy, P. (2021). Comparing the efficacy of early arithmetic instruction based on a learning trajectory and teaching-to-a-target. *JEP* 113(7):1323–1337. `10.1037/edu0000633`, ERIC EJ1318761 / ED619003. `MEASURED-RCT`
7. Clements, D. H., Sarama, J., Layzer, C., Unlu, F., & Wolfe, C. B. (2016). Effects of TRIAD on mathematics achievement: Long-term impacts. SREE. ERIC ED567218. `MEASURED-RCT` (conference paper)
8. Clements, D. H., Sarama, J., Layzer, C., & Unlu, F. (2023). Implementation of a scale-up model in early childhood: Long-term impacts on mathematics achievement. *JRME*. `10.5951/jresematheduc-2020-0245`, ERIC EJ1372925. `MEASURED-RCT`

**Learning progressions, Q-matrices, sequencing policies**

9. Steedle, J. T., & Shavelson, R. J. (2009). Supporting valid interpretations of learning progression level diagnoses. *JRST*. `10.1002/tea.20308`, ERIC EJ850695. `MEASURED-BENCH` (negative)
10. Alonzo, A. C., & Steedle, J. T. (2009). Developing and assessing a force and motion learning progression. *Science Education*. `10.1002/sce.20303`, ERIC EJ836037. `MEASURED-BENCH`
11. de la Torre, J., & Chiu, C.-Y. (2016). A general method of empirical Q-matrix validation. *Psychometrika* 81(2):253–273. `10.1007/s11336-015-9467-8`. `MEASURED-BENCH`
12. Ma, W., & de la Torre, J. (2019). An empirical Q-matrix validation method for the sequential G-DINA model. *BJMSP* 73(1):142–163. `10.1111/bmsp.12156`. `MEASURED-BENCH`
13. Rupp, A. A., & Templin, J. (2007). The effects of Q-matrix misspecification on parameter estimates and classification accuracy in the DINA model. *EPM* 68(1):78–96. `10.1177/0013164407301545`. **Full text unobtainable (`403`); cited for scope only.**
14. Kunina-Habenicht, O., Rupp, A. A., & Wilhelm, O. (2012). The impact of model misspecification on parameter estimation and item-fit assessment in log-linear diagnostic classification models. *JEM* 49(1):59–81. `10.1111/j.1745-3984.2011.00160.x`. **Unobtainable.**
15. Doroudi, S., Aleven, V., & Brunskill, E. (2019). Where's the reward? A review of reinforcement learning for instructional sequencing. *IJAIED* 29:568–620. `10.1007/s40593-019-00187-x`, ERIC EJ1235264. `MEASURED-META`
16. Doignon, J.-P., & Falmagne, J.-C. (1999). *Knowledge Spaces*. Springer. `10.1007/978-3-642-58625-5`.
17. ALEKS / McGraw Hill, `aleks.com/about_aleks/research_behind`, retrieved 2026-07-30. `VENDOR` (mechanism claims only; no efficacy claim on the page)
18. Fang, Y., Ren, Z., Hu, X., & Graesser, A. C. (2019). A meta-analysis of the effectiveness of ALEKS on learning. *Educational Psychology*. `10.1080/01443410.2018.1495829`, ERIC EJ1232632. `MEASURED-META`
19. Sun, S., Else-Quest, N. M., Hodges, L. C., French, A. M., & Dowling, R. (2021). The effects of ALEKS on mathematics learning in K-12 and higher education: A meta-analysis. *Investigations in Mathematics Learning*. `10.1080/19477503.2021.1926194`, ERIC EJ1314175. `MEASURED-META` (CI unverified)
20. Khazanchi, R., Di Mitri, D., & Drachsler (2023). Measuring efficacy of ALEKS as a supportive instructional tool. *JCMST*. ERIC EJ1411006. `OBSERVED` (quasi-experimental; teacher-led outperformed ALEKS-led)

**Mastery learning and the two-sigma claim**

21. Slavin, R. E. (1987). Mastery learning reconsidered. *RER* 57(2):175–213. `10.3102/00346543057002175`; full text ERIC ED294891. `MEASURED-META`
22. Kulik, C.-L. C., Kulik, J. A., & Bangert-Drowns, R. L. (1990). Effectiveness of mastery learning programs: A meta-analysis. *RER* 60(2):265–299. `10.3102/00346543060002265`, ERIC EJ415887. `MEASURED-META`
23. Kulik, J. A., Kulik, C.-L. C., & Bangert-Drowns, R. L. (1990). Is there better evidence on mastery learning? A response to Slavin. *RER* 60(2):303–307. `10.3102/00346543060002303`.
24. Slavin, R. E. (1990). Mastery learning re-reconsidered. *RER* 60(2):300–302. `10.3102/00346543060002300`.
25. Guskey, T. R. (1987). Rethinking mastery learning reconsidered. *RER*. ERIC EJ369712.
26. Bloom, B. S. (1984). The 2 sigma problem. *Educational Researcher* 13(6):4–16. ERIC EJ303699. [Graded in `B1` §7; provenance detail added here.]
27. Anania, J. (1983). The influence of instructional conditions on student learning and achievement. *Evaluation in Education* . ERIC EJ294214.
28. Snider, V. E. (2004). A comparison of spiral versus strand curriculum. *Journal of Direct Instruction*. ERIC EJ755132. `OBSERVED` (argument, not evaluation)

**Nulls**

29. Ready, D. D., Conn, K., Bretas, S. S., & Daruwala, I. (2018). Final impact results from the i3 implementation of *Teach to One: Math*. CPRE, Teachers College. ERIC ED618425. `MEASURED-BENCH` (CITS; null in all three years)
30. Strand Cary, M., Shanley, L., Smolkowski, K., Clarke, B., & Crowley, R. (2026). Exploring KinderTEK's efficacy in kindergarten classrooms. Grantee submission, ERIC ED679597. `MEASURED-RCT` (null; n = 1,368)

**Fade-out, persistence, long-term retention**

31. Bailey, D., Duncan, G. J., Odgers, C. L., & Yu, W. (2017). Persistence and fadeout in the impacts of child and adolescent interventions. *JREE*. `10.1080/19345747.2016.1232459`, ERIC EJ1125358.
32. Kang, C. Y., Duncan, G. J., Clements, D. H., Sarama, J., & Bailey, D. H. (2019). The roles of transfer of learning and forgetting in the persistence and fadeout of early childhood mathematics interventions. *JEP*. `10.1037/edu0000297`, ERIC EJ1213721. `MEASURED-RCT`
33. Watts, T. W., Hart, E. R., & Bailey, D. H. (2025). How general is educational intervention fadeout? EdWorkingPaper 25-1366, Annenberg Institute. ERIC ED678313. `MEASURED-META` — **working paper**
34. Rosengarten, M. L., Hart, E. R., Bailey, D. H., McCormick, M. P., & Lovett, B. J. (2024). Using meta-analytic data to examine fadeout and persistence on constrained and unconstrained skills. EdWorkingPaper 24-1069. ERIC ED672296. `MEASURED-META` — **working paper** (null)
35. Pages, R., Protzko, J., & Bailey, D. H. (2022). The breadth of impacts from the Abecedarian Project early intervention on cognitive skills. *JREE*. `10.1080/19345747.2021.1969711`, ERIC EJ1349873. `MEASURED-RCT`
36. Bahrick, H. P. (1984). Semantic memory content in permastore: Fifty years of memory for Spanish learned in school. *JEP: General* 113(1):1–29. `10.1037/0096-3445.113.1.1`. **Characterised via the author's own restatement in [37]; full text unobtainable.**
37. Bahrick, H. P., & Phelps, E. (1987). Retention of Spanish vocabulary over 8 years. *JEP:LMC* 13(2):344–349. `MEASURED-RCT`
38. Bahrick, H. P., Bahrick, L. E., Bahrick, A. S., & Bahrick, P. E. (1993). Maintenance of foreign language vocabulary and the spacing effect. *Psychological Science* 4(5):316–321. `MEASURED-RCT` (n = 4)
39. Bahrick, H. P., & Hall, L. K. (1991). Lifetime maintenance of high school mathematics content. *JEP: General* 120(1):20–33. `10.1037/0096-3445.120.1.20`. **Located, not read.**

**Transfer to work**

40. Vermylen, J. H., Cohen, E. R., Cook, D. A., McGaghie, W. C., Issenberg, S. B., … Kessler, D. O. (2025). Competency-based simulation training for procedural skills: A systematic review and meta-analysis. *Simulation in Healthcare*. `10.1097/sih.0000000000000895`, PMID 41217357. `MEASURED-META`
41. Hanushek, E. A., Schwerdt, G., Woessmann, L., & Zhang, L. (2017). General education, vocational education, and labor-market outcomes over the lifecycle. *JHR* 52(1):48–87. `10.3368/jhr.52.1.0415-7074r`. `OBSERVED`
42. Farrington, J. (2011). Training transfer: Not the 10% solution. *Performance Improvement Quarterly*. `10.1002/piq.20105`, ERIC EJ921207. `OBSERVED`
43. Fitzpatrick, R. (2001). The strange case of the transfer of training estimate. *TIP*/PsycEXTRA `10.1037/e576912011-002`; Saks, A. (2002) reply, `10.1037/e576922011-004`. **Records located; text unobtainable.**
44. Arthur, W., Bennett, W., Edens, P. S., & Bell, S. T. (2003). Effectiveness of training in organizations: A meta-analysis of design and evaluation features. *JAP* 88(2):234–245. `10.1037/0021-9010.88.2.234`. **Effect sizes unobtainable in this session.**

**Motor and procedural skill**

45. Shea, J. B., & Morgan, R. L. (1979). Contextual interference effects on the acquisition, retention, and transfer of a motor skill. *JEP:HLM* 5(2):179–187. `10.1037/0278-7393.5.2.179`. `MEASURED-RCT`
46. Schmidt, R. A., & Bjork, R. A. (1992). New conceptualizations of practice. *Psychological Science* 3(4):207–218. `10.1111/j.1467-9280.1992.tb00029.x`. [Already in `F11`; re-labelled here as a unification, not an independent replication.]
47. Czyż, S. H., Wójcik, A. M., Solarská, P., & Kiper, P. (2024). High contextual interference improves retention in motor learning: Systematic review and meta-analysis. *Scientific Reports* 14. `10.1038/s41598-024-65753-3`. `MEASURED-META`
48. Wulf, G., & Shea, C. H. (2002). Principles derived from the study of simple skills do not generalize to complex skill learning. *Psychonomic Bulletin & Review* 9(2):185–211. `10.3758/BF03196276`. `MEASURED-META`
49. Magill, R. A., & Hall, K. G. (1990). A review of the contextual interference effect in motor skill acquisition. *Human Movement Science*. [Located; superseded for quantitative purposes by 47.]
50. Salmoni, A. W., Schmidt, R. A., & Walter, C. B. (1984). Knowledge of results and motor learning: A review and critical reappraisal. *Psychological Bulletin*. [The guidance hypothesis; falsified as a general claim by 51.]
51. McKay, B., Hussien, J., Vinh, M.-A., Mir-Orefice, A., Brooks, H., & Ste-Marie, D. M. (2022). Meta-analysis of the reduced relative feedback frequency effect on motor learning and performance. *Psychology of Sport and Exercise* 61:102165. `10.1016/j.psychsport.2022.102165`; preprint `10.31234/osf.io/v2cp7`. `MEASURED-META` (null)
52. McKay, B., Yantha, Z., Hussien, J., Carter, M. J., & Ste-Marie, D. M. (2022). Meta-analytic findings of the self-controlled motor learning literature: Underpowered, biased, and lacking evidential value. *Meta-Psychology* 6. `10.15626/mp.2021.2803`. `MEASURED-META` (null after bias correction)
53. St. Germain, L., McKay, B., Poskus, A., Williams, A., Leshchyshen, O., Feldman, S., Cashaback, J. G. A., & Carter, M. J. (2023). Exercising choice over feedback schedules during practice is not advantageous for motor learning. *Psychonomic Bulletin & Review* 30:621–633. `10.3758/s13423-022-02170-5`. `MEASURED-RCT` (preregistered null, N = 228)
54. Winstein, C. J., & Schmidt, R. A. (1990). Reduced frequency of knowledge of results enhances motor skill learning. *JEP:LMC* 16(4):677–691. `10.1037/0278-7393.16.4.677`. [The canonical positive result; see 51 for its status under meta-analysis.]
55. Lee, T. D., & Genovese, E. D. (1988). Distribution of practice in motor skill acquisition. *RQES* 59(4):277–287. `10.1080/02701367.1988.10609373`. **Pooled estimates unobtainable.**
56. Lee, T. D., & Genovese, E. D. (1989). Distribution of practice in motor skill acquisition: Different effects for discrete and continuous tasks. *RQES* 60(1):59–65. `10.1080/02701367.1989.10607414`. **Unobtainable.**
57. Donovan, J. J., & Radosevich, D. J. (1999). A meta-analytic review of the distribution of practice effect: Now you see it, now you don't. *JAP* 84(5):795–805. `10.1037/0021-9010.84.5.795`. **Unobtainable.**

**Carried from the corpus, not re-derived**

58. Matayoshi, Cosyn, Uzun & Kurd-Misto (2025), *JEDM* 17(1) — ALEKS mastery-threshold production RCT; Prihar et al. (2022), EDM, ERIC ED624051 — ASSISTments mastery-threshold meta; Brunmair & Richter (2019) interleaving moderators; Nemeth et al. (2019) interleaving null; Kraft (2020) effect-size benchmarks; Nickow, Oreopoulos & Quan (2023) tutoring pooled ES; von Hippel on Bloom. All are cited above by way of `F11`, `B1`, `F10` and `B2`, which own them.

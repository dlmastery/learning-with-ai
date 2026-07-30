---
title: "Zero of Eight — sequencing pays inside a topic and has never been shown to pay between them"
section: sequencing
status: draft
date: 2026-07-30
source_report: research/raw/R6-sequencing-and-durability.md
---

# Zero of Eight

Doroudi, Aleven & Brunskill (2019), *IJAIED* 29:568–620, collected every empirical
study since the 1960s that pitted a machine-induced instructional sequencing policy
against a baseline. Their headline is positive, and this survey has already published
a correction for quoting it selectively: **over half** the comparisons, 21 of 41,
found an induced policy significantly better than every baseline, often at Cohen's
*d* of 0.8 or more. The finding is in their Table 2, where the comparisons are grouped
by *what was being sequenced*.

| Cluster | Sig | ATI | Mixed | Not sig | Sig worse |
|---|---|---|---|---|---|
| Paired-associate learning tasks | 11 | 0 | 0 | 2 | 1 |
| Concept learning tasks | 4 | 0 | 2 | 1 | 0 |
| **Sequencing interdependent content** | **0** | **0** | **2** | **6** | **0** |
| Sequencing activity types | 4 | 4 | 0 | 2 | 0 |
| Maximising other objectives | 2 | 0 | 0 | 0 | 0 |

`MEASURED-META`

The third row is curriculum sequencing: the cluster the authors describe as "closest
to traditional curriculum sequencing," where "a network specifying the relationship
between different content areas or KCs (such as a prerequisite graph) must either be
prespecified or automatically inferred from data." **Zero of eight beat their
baselines.** The six clean nulls include Clement et al. (2015) with 133 seven- and
eight-year-olds on arithmetic, Doroudi et al. (2017) with 69 fourth and fifth graders
on fractions, and the authors' own Appendix B study with 100 more children — none of
which shows in a headline where over half the comparisons favoured the induced policy.

The two clusters that did win are decisions about *when to bring an item back*
(paired-associate scheduling, the spacing literature §08 owns) and *what kind of
activity to give next for fixed content* (worked example against problem, §22's
territory). Both concern time and modality inside a topic that has already been
chosen. Neither is a decision about which topic comes next.

---

## 1. The move this survey specifies is the move with zero wins

§25 states the entry rule for an explanation: *compute the mastery vector over the
concept's transitive prerequisite closure and enter at the weakest link, laddering
that prerequisite separately.* The learner-model machinery behind it carries a
prerequisite-dropback repair whose own evidence line reads "no pooled ES;
mechanism-level `INFERENCE`."

Read against Table 2, the two halves of that rule have opposite standing. Picking the
technique for a chosen target has meta-analytic support. Traversing a prerequisite
closure to decide what the target should be has no positive result anywhere in sixty
years of experiments. It is `SPEC` with no measured warrant, load-bearing in at least
three places in this document. The word `prerequisite` appears 196 times across this
project's research corpus; `curriculum sequencing` twice and `knowledge space` never.
`OBSERVED — absence`

For the eleven-year-old this survey is organised around, the gap has a face. She can
hold a conversation about photosynthesis and cannot pass a worksheet about it. A
system that verifies the transitive closure before teaching the target will find gaps
in it — her mathematics is behind, her writing fluency is behind — and route her away
from the one topic she was ready to think about. The gate is the expensive part of the
architecture and the part with no evidence behind it.

---

## 2. The one ordering anybody has tried to break

Clements and Sarama's learning trajectories are a goal, a hypothesised developmental
progression of levels of thinking, and tasks matched to each level. The claim is
narrow and falsifiable: instruction works best when it targets the level one step
above the child's current level. The decisive studies compare that against *equal-dose
instruction aimed straight at the target*, skipping the intervening levels.

Clements, Sarama, Baroody, Kutaka & Chernyavskiy (2021), *JEP* 113(7):1323–1337, is
the one with power. **291 kindergartners** from four schools, randomly assigned to
one-on-one instruction one level above their present level, or to one-on-one
instruction on story problems three levels above it. Baseline equivalence was
established (d = .05 counting, .07 arithmetic), and dosage was equalised and
non-significant between arms: 196 minutes over 13.4 sessions against 212 minutes over
14.3. The one-level-up condition scored higher at posttest, **d = 1.20** for the main
effect of condition in the baseline model, **and the advantage was largest for children
with low entry knowledge of arithmetic.** `MEASURED-RCT`

The boundary conditions deserve the same prominence as the number. All three
skip-level studies come from one laboratory, sharing instruments, trajectory
definitions and analytic conventions; two share four of five authors. The domains are
early number and early shape, where developmental order is unusually constrained by
what the arithmetic itself permits. The instruction is one-to-one. And the 2019 *AERJ*
companion on shape composition, which found the trajectory group learned significantly
more, found it **mainly on near-transfer items**. A fourth study in the same series
(Clements et al. 2020, *ZDM*) is cited constantly and has **n = 25** across both arms;
it should never appear without that number. `INFERENCE`

Nothing here establishes that a prerequisite graph over secondary chemistry, or
programming, or a second language, has the same standing. Nobody has run the
skip-level design outside early mathematics.

---

## 3. Levels are not stable enough to route from

If an ordering is real, a learner should sit *at* a level and reason from it
consistently. Steedle & Shavelson (2009), *JRST*, tested that with latent class
analysis on diagnostic items about forces on an object moving at constant speed.
Students with a scientifically accurate understanding did reason systematically.
**Many other students did not**, and the authors conclude that interpretations of
learning-progression level diagnoses "would often be invalid" on the progression they
examined. `MEASURED-BENCH` Alonzo & Steedle (2009) reached the same place from the
other side: students do not respond consistently to similar problems set in different
contexts. `MEASURED-BENCH`

A tutor that places a learner at "level 3 of the fractions progression" and routes the
next hour from that placement is doing large-scale testing whatever it looks like
from the outside: a single-shot inference from a handful of items, on a construct the
measurement literature says is not stable enough across contexts to carry it.

The formal object such a system needs is a Q-matrix, items on the rows and latent
skills on the columns. These can be validated against response data instead of
asserted (de la Torre & Chiu 2016), and the standard citation for what misspecification
costs is Rupp & Templin (2007), cited for scope because its numbers sat behind a
publisher block. The design consequence survives the missing numbers: a model asked to
emit a prerequisite graph is producing an expert-judgement Q-matrix with no validation
step, in a formalism whose known failure mode is that misspecification propagates into
every classification the system then makes. `INFERENCE`

---

## 4. The deployed system built entirely on prerequisite structure sits at g ≈ 0.05

ALEKS is the commercial instantiation of knowledge space theory (Doignon &
Falmagne). Its own research page describes the mechanism, a knowledge state assessed
"after the student has answered only 20–25 questions," and cites no efficacy study and
no effect size. `VENDOR` Two meta-analyses reach the same place. Fang, Ren, Hu &
Graesser (2019), *Educational Psychology*, 15 studies and 24 independent samples:
ALEKS was as good as, but not better than, traditional classroom teaching. Sun,
Else-Quest, Hodges, French & Dowling (2021), 33 studies, 56 independent effect sizes,
**9,238 students**: pooled **Hedges' g = 0.05** against ordinary instruction, with a
supplemental-use moderator at **g = 0.43**. `MEASURED-META`

Two flags travel with those numbers. The ERIC record prints a pooled interval that is
not symmetric about the point estimate and could not be checked against the article,
so the point estimates are citable and the interval is not. And **the two
meta-analyses are not independent**: Sun et al.'s window subsumes Fang et al.'s and
the study pools certainly overlap. What survives is that no synthesis of the flagship
prerequisite-structured system finds a general advantage, and that its one positive
moderator is a dosage result — adding a supplementary practice system to teaching
beats teaching alone.

§08 carries the strongest datum from inside the same system: across 32.9 million
randomised topic sequences in production, raising the mastery threshold cost +29% time
for a retention difference under 0.02. Inside a fixed topic, how hard you push mastery
barely moves anything; across topics, which order you use has never been shown to move
anything either.

---

## 5. Mastery learning was given 20–33% more time, and Bloom's study ran three weeks

Slavin's 1987 synthesis (*RER* 57(2):175–213) is where the two-sigma provenance
lives. The claims it was testing ran from Kulik et al.'s 0.52 and 0.54 through
Walberg's 0.81 to Bloom's own 1.00 "when mastery learning procedures are done
systematically and well," with two sigma as the prediction.

Slavin then restricted to practical applications in real schools running at least four
weeks, with equal time for treatment and control, on standardised measures. Seven
studies qualified. **Median effect size +0.04.** The single non-trivial result (+0.25)
came from a study where teachers self-selected into conditions, and was not significant
at the class level. `MEASURED-META`

Two design facts from his methods section rarely survive the citation trail.
**Anania's study — one of the Chicago dissertations Bloom's essay rests on — ran three
weeks.** And all the Chicago dissertations "provided the mastery learning classes with
similar amounts of additional instruction," amounting to **20–33% more instructional
time** than control classes received. Bloom's own characterisation was that the time
costs "have usually been very small." `OBSERVED` §24 and §19 retire the two-sigma
claim on replication grounds; this is the mechanism underneath that verdict.

Then the part nobody quotes. Slavin also examined maintenance: six comparisons in
five studies assessing retention 4–12 weeks out, all on experimenter-made measures.
**The median retention effect is essentially zero**, and the largest one (+0.49) came
from the single study that had found no differences on standardised measures.
`MEASURED-META` The strongest claim mastery-based sequencing makes is that refusing
to advance builds something durable. In group-based form that claim has been tested,
it did not hold, and thirty-nine years later no synthesis overturns it.
`OBSERVED — absence`

Slavin also names why the corrective loop may under-deliver, and it reads as a
specification. In none of the sixteen studies did corrective instruction occupy more
than **one period per week, or 20% of instructional time**, and it was delivered in
groups or by peer tutors. Mastery learning has never been tested with unlimited
individual correction, because until now nobody could afford it. That is the version
this project can build. `INFERENCE`

---

## 6. Teach to One: three years, five schools, and estimates that drift downward

Ready, Conn, Bretas & Daruwala (2018), Consortium for Policy Research in Education,
ERIC ED618425, evaluated the purest deployed instantiation of the thesis this section
is testing. Teach to One: Math runs a daily algorithmic scheduler that assigns each
student the mathematics content their diagnosed skill state says they are ready for,
in whatever modality suits it, breaking the grade-level sequence entirely. New
Classrooms ran it under an Investing in Innovation grant in five New Jersey schools
for three academic years from September 2015. CPRE ran a comparative interrupted time
series against 16 comparison schools in the same district: **36,158 student-level
measurements** nested in 209 school-by-year cohorts, outcomes z-scored within grade
and year.

| Implementation year | Adjusted estimate (SD) | SE |
|---|---|---|
| Year 1 (2015–16) | +0.062 | 0.089 |
| Year 2 (2016–17) | −0.113 | 0.087 |
| Year 3 (2017–18) | −0.170 | 0.087 |

All three are statistically non-significant, and the unadjusted estimates trace the
same V. `MEASURED-BENCH` (quasi-experimental)

This is a three-year funded deployment of the architecture a "school in a box" would
build, and not a laboratory manipulation. And the point estimates drift *downward*
across the three years, the opposite of the implementation-maturity curve every
adaptive-sequencing vendor forecasts.

A second null in the same family: KinderTEK, an iPad mathematics program with
individualised progression, cluster-randomised across 70 kindergarten classrooms,
**1,368 students**, with no significant differences on early number fluency, broad
mathematics achievement, or proximal math content (ERIC ED679597). `MEASURED-RCT`

---

## 7. Most of fade-out was the control group catching up

The TRIAD trial is this corpus's best-documented early-mathematics effect and its
best-documented decay. Clements, Sarama, Layzer, Unlu & Wolfe (2016), SREE conference
paper ERIC ED567218, gives the trajectory in standard deviations: **0.86** (with
follow-through) and **0.75** (without) at the end of pre-K, falling through
kindergarten and grade 1, **not distinguishable from zero at grades 3 and 4**, then
**0.26 and 0.21, both significant, at the end of grade 5.** The citation of record for
the pattern is the published Clements, Sarama, Layzer & Unlu (2023), *JRME*: early
effects "decreased through fourth grade but reemerged at fifth grade." The numbers
above belong to the conference paper. `MEASURED-RCT`

Kang, Duncan, Clements, Sarama & Bailey (2019), *JEP*, decomposed that decay on the
same trial. Treated children did forget more in the following year than controls —
but forgetting accounted for **only about one quarter of the fade-out**, and an
offsetting transfer effect was small and non-significant, worth roughly one tenth of
the end-of-program treatment effect. **Most of the fade was the control group catching
up.** `MEASURED-RCT`

That distinction changes what a durability claim means. If the majority of the decay
is convergence, an early tutoring advantage is largely an *acceleration*, and the
question becomes whether acceleration is worth anything by itself. It also means that
"did the learner retain it," measured against a control group, answers a different
question from "does the learner still have it." §09 documents that almost nobody in
AI tutoring measures retention at all; this is why measuring it against a control
would still not settle the promise. The subgroup pattern compounds it: durability was
greatest where the sustaining environment was strongest, with higher-SES children in
the no-follow-through arm reaching 0.6–0.7 SD by fifth grade while lower-SES effects
held only through kindergarten. `OBSERVED`

Absolute retention is the other question, and Bahrick's permastore programme is where
it lives. His summary of the fifty-year Spanish study, restated in Bahrick & Phelps
(1987): part of what is acquired is lost within five years, and "virtually no
knowledge is lost during the interval between 5 and 25 years" after acquisition.
`OBSERVED` That study of 35 learners, tested at 8 years, put optimum recall at
**30-day** access intervals across a range running from 0% to 23%. `MEASURED-RCT`

The nine-year follow-up (Bahrick, Bahrick, Bahrick & Bahrick 1993, *Psychological
Science* 4(5):316–321) found retention functions that crossed over during the first
year and stayed crossed for five, so that **13 relearning sessions spaced at 56 days
matched 26 sessions spaced at 14 days** — half the training for the same durable
outcome. Two cautions the citation trail drops: **n = 4**, and the authors record
schedule departures, an omitted terminal session, a three-year test given at four
years, and subjects who travelled in France. `MEASURED-RCT` — extraordinary in
duration, tiny in sample, imperfectly controlled.

---

## 8. Motor learning arrived independently, and half of it does not replicate

This survey's central empirical theme is that conditions producing the best
performance during practice produce the worst retention. Motor learning reached the
same dissociation independently, which looks like corroboration and is only partly
that.

The bridge citation the corpus reaches for is Schmidt & Bjork (1992), *Psychological
Science* 3(4):207–218. Robert Bjork co-authored it and originated the
desirable-difficulties framework on the verbal side, so a paper arguing that two
literatures agree cannot be counted as those two literatures agreeing. This project
forbids claiming independence between two of its own workstreams; the rule applies to
a citation we imported. `INFERENCE`

The genuinely independent arrival is Shea & Morgan (1979), *JEP:HLM* 5(2):179–187: a
barrier-knockdown task in a motor-behaviour laboratory descending from Battig (1966),
with no methodological contact with verbal spacing research. Blocked practice won
during acquisition; random practice won at 10-minute and 10-day retention, whether the
retention test was itself blocked or random. `MEASURED-RCT` One manipulation,
contextual interference, reproduces the acquisition–retention reversal in a discipline
that did not borrow it.

Whether the rest reproduces is a separate question. Czyż, Wójcik, Solarská & Kiper
(2024), *Scientific Reports* 14, meta-analysed **54 studies** on delayed retention
(>24 h):

| Subgroup | Three-level SMD | 95% CI |
|---|---|---|
| Overall | 0.63 | 0.33, 0.93 (0.43 after outlier removal) |
| Laboratory settings | 0.92 | 0.48, — |
| Applied settings | 0.23 | −0.16, 0.62 (−0.01 after outlier removal, *p* = .94) |
| Under 18 | 0.02 | −0.90, 0.94 (*p* = .97; 49 effects, 418 participants) |
| Adults (18–59) | 0.63 | 0.30, 0.96 |
| Older adults (≥60) | 1.45 | 0.55, 2.35 |

`MEASURED-META`, I² in the 62–83% range where reported.

**The eleven-year-old this project is for sits inside both boundary conditions at
once.** She is under eighteen and she is not in a laboratory. Wulf & Shea (2002) found
the same split in the primary studies twenty years earlier — Farrow & Maschette found
random practice better for 10–12 year-olds and **blocked practice better for 8–9
year-olds** on the tennis forehand — and their title is the warning label: *principles
derived from the study of simple skills do not generalize to complex skill learning.*

The feedback half of the doctrine fails outright. The guidance hypothesis (Salmoni,
Schmidt & Walter 1984) holds that feedback after every trial props up acquisition
while preventing intrinsic error detection, so reduced-frequency feedback should lose
during practice and win at retention. McKay, Hussien, Vinh, Mir-Orefice, Brooks &
Ste-Marie (2022), *Psychology of Sport and Exercise* 61:102165, screened 1,662 records
to **61 papers, k = 75, N = 2,228**, and found "no significant effect of reduced
feedback frequency at any time point" and "no evidence of a significant change in
effect from acquisition or immediate retention to delayed retention." Their highlight
list ends: "The guidance hypothesis is not supported by the extant research."
`MEASURED-META` The same group's self-controlled practice meta-analysis lands in the
same place: a naive g = 0.44 over 52 comparisons (N = 2,061) falls to **g = 0.107
[0.047, 0.18]** once selection bias is modelled.

What transfers is the mechanism and not the doctrine. Difficulty is desirable to the
degree the learner has spare capacity to meet it, which is §22's expertise-reversal
law and §34's executive-function argument arriving from a third direction. Contextual
interference, feedback fading and practice distribution are therefore
capacity-conditional, and for a novice, on a complex task, under eighteen, they
default **off** and are earned by measurement.

---

## 9. Numbers this section refuses to carry

The source report marks several things untraceable, and they stay untraceable here.

- **"Only 10% of training transfers to the job."** Two decades of edtech decks rest on
  it. It traces to Georgenson (1982), where it was, in the words of the paper that
  chased it down, a **"conversational gambit"** and never an estimate (Farrington 2011,
  *PIQ*, ERIC EJ921207). No study stands behind it.
- **Rupp & Templin's (2007) misspecification numbers**, the quantitative form of the
  risk in letting a model emit a graph.
- **Pooled estimates from Lee & Genovese (1988, 1989) and Donovan & Radosevich
  (1999)** on massed against distributed motor practice.
- **The pooled interval in Sun et al. (2021).** The point estimate is safe.
- **Which Building Blocks persistence figure is right.** The 2013 *AERJ* third-year
  effects (0.51 / 0.28) do not reconcile with the same team's long-term analysis, so
  anyone citing that persistence effect must say which paper and which model.
- **Transfer from instruction to job performance outside health professions
  education.** In the one place it is measured (Vermylen et al. 2025), mastery
  sequencing reliably produces the measured skill, while "outcomes are favorable, but
  small, for behaviors in practice and patient effects."

---

## 10. Demote the graph, then randomise it

The graph does not go away. It changes job.

**Every edge gets a stated epistemic status.** *Constitutive* edges are entailed by the
domain's own logic — you cannot compose shapes you cannot recognise. *Empirical* edges
are ones a skip-level trial has tested, which today means early number and shape.
*Conventional* edges are everything else, which is most of them. A system that treats
the three alike will be wrong in a predictable way. `SPEC`

**The graph is used for diagnosis and never for gating.** A dropback triggered by a
diagnosed error, aimed at a named missing component, is the supported use. "The
learner may not proceed to *c* until the closure of *c* is verified" is the
unsupported one, and §25 should drop it until it is tested. For the learner in §04
this is the difference between a tutor that teaches photosynthesis and one that sends
her back to fractions first.

**A durability instrument, because nobody has one.** A tutor can afford what no trial
could: unannounced delayed transfer probes at 30, 90 and 365 days, on freshly
generated items the learner has stopped studying, reporting *absolute* retention
alongside any comparative claim. Bahrick's 30-day optimum and the 56-day crossover
give the schedule a starting shape. `SPEC`

**And the experiment: randomise the graph, not the policy.** Every existing study
randomises which traversal policy walks a fixed graph. The untested question is
whether the graph earns its cost. Within-learner, topic-level randomisation, mirroring
the ALEKS production design: each eligible topic is randomly assigned to
graph-respecting entry (verify the closure, remediate any gap, then teach the target)
or demand-driven entry (teach the requested target immediately, repair prerequisites
reactively when an error names a missing component). Instructional time is capped
identically in both arms, the condition Slavin showed almost no mastery-learning study
met. Primary outcome: delayed transfer at 28 days on freshly generated items, scored
blind. Secondary: time to criterion, a 90-day probe, and how often a verified
prerequisite gap turned out to be real.

The question is whether any difference is large enough to pay for the graph, so this
is an **equivalence trial** at a pre-registered margin of **δ = 0.10 SD**. Two
one-sided tests, α = .05, 90% power, paired within learner at a between-condition
correlation of 0.5 gives **n ≈ 857 learners** × 8 topic pairs: about 7,200 topic
sequences, two terms of a mid-sized deployment, four orders of magnitude smaller than
the ALEKS study.

Either answer is worth having. If the graph is equivalent within 0.10 SD, §25 stops
computing prerequisite closures and §18's generative-textbook problem collapses from
"construct a validated ordering" to "answer the question that was asked" — the cheaper
system, and the one that meets a curious child where she is. If the graph wins by more
than 0.10 SD, this project has its first direct warrant for an architecture four of its
own reports already assume, and will have earned the gate it has been using on credit.

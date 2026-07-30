---
title: "Exam technique and revision — what a score is made of, what coaching actually buys, and the one place in education where a correctness oracle already exists"
wave: R
section: R2
date_researched: 2026-07-30
sources_count: 41
status: raw-research
---

# R2 — Exam Technique and Revision

> **Why this report exists.** `Z1-coverage-audit.md` row 8 records the gap: `exam technique` 0 hits,
> `study skills` 0, `past paper` 0, `test preparation` 1, `homework` 26 hits all incidental. The
> markets this project has named are SAT, PSAT, NEET, JEE, GATE, EAMCET and the gaokao — the places
> where the customer's stated goal is a number and where the largest sums in tutoring already sit.
>
> **The four findings, stated first.**
>
> 1. **Commercial coaching moves admissions-test scores by roughly a tenth to a sixth of a standard
> deviation, and the industry advertises three to seven times that.** The best observational
> estimate on the SAT is 6–8 scale points on verbal and 13–18 on mathematics (Powers & Rock, ETS);
> the best meta-analysis is +0.09 SD verbal and +0.16 SD mathematics (Becker); the best independent
> reanalysis on national longitudinal data agrees within a point or two (Briggs). Powers and Rock
> converted their own largest estimate into the only unit that matters to a buyer: about one extra
> question correct per eight hours of effort.
> 2. **The one number this project's own market repeats — 20 hours on Khan Academy is worth 115
> SAT points — is a press-release framing of an uncontrolled pre-post gain.** The joint College
> Board / Khan Academy technical report, which is a working paper and an observational study by its
> own first sentence, puts the controlled figure at +21 points at six hours and +39 points at six
> hours plus one "best practice" behaviour. That is an effect size of 0.11 and 0.20. It is a real
> and cheap effect. It is not 115.
> 3. **The learner's default revision technique is the one the measurement literature rates lowest,
> and the reason is a felt/real dissociation this survey already turns on.** 83.6% of surveyed
> students list rereading; 54.8% rank it first; 1.1% rank self-testing first. In the experiment
> that quantifies the cost, the condition that read a passage 14.2 times was the most confident it
> would remember, and recalled 40% at one week against 61% for the condition that read it 3.4 times
> and tested three times.
> 4. **Public examinations are the one domain in education that ships an external correctness
> oracle, and the oracle is gameable in a documented, measured way.** Mark schemes make the
> learner's answer checkable in a sense that `survey/32` says pedagogy lacks. Koretz's
> score-inflation literature says the check can be optimised against without the underlying
> competence moving: high-stakes gains run 3–5× low-stakes gains on the same students. §12 states
> the boundary that reconciles them, and §14 turns it into a trial design.

---

## Source reachability log (2026-07-30)

WebSearch budget was exhausted at 200 calls mid-session. Everything after that ran on **ERIC**
(`api.ies.ed.gov/eric/`, the workhorse and the only route to the test-preparation and homework
literature), **Crossref REST** (abstracts present for Becker 1990, Cepeda 2008 and the *Economic
Journal* coaching null; absent for most APA titles), **Semantic Scholar** (empty result sets for
every query attempted), and direct `curl` + `pdftotext -layout` against open PDF hosts.

- **Full texts recovered and quoted verbatim below:** Powers & Rock's ETS report and Koretz's CSE
  Report 655 from `files.eric.ed.gov`; the Official SAT Practice technical report from
  `research.collegeboard.org` including Appendix F's propensity-score sensitivity analysis, which is
  the part the press coverage never reaches; Briggs's CHANCE draft from `nepc.colorado.edu`;
  Roediger & Karpicke (2006) and Karpicke, Butler & Roediger (2009) from Washington University and
  Purdue; the full Dunlosky et al. (2013) monograph including Table 4 from `whz.de`; the 2022 PISA
  parental-homework meta-analysis from `psicothema.com`; Cooper, Robinson & Patall (2006) from UC
  Riverside.
- **ScienceDirect, SAGE, Wiley, APA PsycNet** all returned `403`. Rawson & Kintsch (2005) full text
  was **UNREACHABLE-IN-SESSION**; its abstract is quoted from ERIC and no claim here rests on a
  number I did not see.
- **Untraceable and reported as such:** any causal estimate of the effect of Kota / Allen / Aakash
  / Physics Wallah coaching on NEET or JEE outcomes. Searched: ERIC (`"entrance exam" AND coaching
  AND India`, 2 hits, both ethnographic; `"shadow education" AND India AND achievement`, 0 hits),
  WebSearch on econometric and causal framings. §3 reports the absence as the finding.

**Evidence labels** per the project standard: `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` ·
`OBSERVED` · `VENDOR` · `INFERENCE` · `CRAFT` · `SPEC` · `FILING`. A `VENDOR` claim is never
restated as a finding.

**Builds on, does not repeat:** `F11-scientific-remembering.md` owns spacing, retrieval practice
and FSRS, and its Cepeda and Adesope readings are carried here rather than re-derived. `B1` owns
the learning-science floor. `C2` and `F1` own psychometrics and assessment reconstruction. `N2` and
`V5` own executive function. **`R3` owns test anxiety**; §9 states the interaction and hands off.

---

## 0. The numbers that carry the argument

| # | Quantity | Value | Source | Label |
|---|---|---|---|---|
| 1 | SAT coaching effect, seven estimators | verbal 6–12 pts, math 13–26 pts; medians 8 and 18 | Powers & Rock 1999 | `OBSERVED` |
| 4 | SAT coaching, independent national data | math +14 to +15, verbal +6 to +8, combined ~20 pts | Briggs 2001, NELS:88, n = 4,730 | `OBSERVED` |
| 6 | Advertised at the time | Kaplan 120 pts, Princeton Review 140 pts combined; PR guaranteed 100 | quoted in Powers & Rock 1999 | `VENDOR` |
| 8 | Khan Academy OSP, 6 hours, controlled | +21 SAT points, ES 0.11 | Weatherholtz et al. 2020, n ≈ 299,315 linkers | `OBSERVED` (working paper) |
| 11 | Private tutoring and the gaokao | average effect on NCEE total not significant | Zhang 2013, *Econ. Educ. Rev.* | `OBSERVED` (null) |
| 12 | Any test in 15 weeks vs no tests | ~+0.5 SD on criterion exam | Bangert-Drowns, Kulik & Kulik 1991, 40 studies | `MEASURED-META` |
| 14 | Practice testing vs restudy | g = 0.51; vs no activity g = 0.93; overall g = 0.61 | Adesope et al. 2017 (carried from F11) | `MEASURED-META` |
| 15 | Cramming's purchase: recall at 5 minutes | restudy 81% vs test 75%, d = 0.52 for restudy | Roediger & Karpicke 2006, Exp. 1, n = 120 | `MEASURED-RCT` |
| 19 | Optimal review gap as a fraction of test delay | 20–40% at a 1-week delay; 5–10% at a 1-year delay | Cepeda et al. 2008, n > 1,350 | `MEASURED-RCT` |
| 22 | Students listing rereading as a study strategy | 83.6%; 54.8% rank it first | Karpicke, Butler & Roediger 2009, n = 177 | `OBSERVED` |
| 24 | Dunlosky utility ratings, low | summarisation, highlighting, keyword mnemonic, imagery for text, rereading | Dunlosky et al. 2013, *PSPI* | `MEASURED-META` |
| 26 | Homework vs no homework, experiments | d = 0.60 [0.38, 0.82], k = 5; randomised subset d = 0.53 [0.29, 0.79], k = 3 | Cooper, Robinson & Patall 2006 | `MEASURED-META` |
| 27 | Time-on-homework × achievement, Grades 7–12 | r = +0.25 fixed / +0.20 [0.17, 0.22] random, k = 23 | ibid. | `MEASURED-META` |
| 31 | Parental help with homework, PISA 2009–2018 | more help → lower achievement, d = 0.23 [0.21, 0.25], 180 effects | Fernández-Alonso et al. 2022 | `MEASURED-META` |
| 34 | Low-touch study-skills coaching, 5 years | study time up, academic outcomes unmoved, N ≈ 20,000 | Oreopoulos et al. 2023, *Economic Journal* | `MEASURED-RCT` (null) |
| 35 | Rereading a real textbook chapter, 4 experiments | "with only several exceptions, rereading did not significantly increase performance" | Callender & McDaniel 2009 | `MEASURED-RCT` (null) |
| 37 | High-stakes score gains vs low-stakes gains, same students | typically 3–5×; in numerous cases the low-stakes gain is zero | Koretz 2005, CSE Report 655 | `OBSERVED` |

---

## 1. What coaching buys on the SAT, with the estimand attached

### 1.1 Powers & Rock: seven estimators, one answer

The reference study is **Powers, D. E., & Rock, D. A. (1999), "Effects of coaching on SAT I:
Reasoning test scores," *Journal of Educational Measurement* 36(2), 93–118**, issued by ETS as
Research Report 98-53 and recovered in full from the ERIC mirror this session. Its design is
observational, and the authors say so in the first line of their discussion: *"The major limitation
of the study described here is its observational (or nonexperimental) nature: There was no random
assignment to treatments."* `OBSERVED`

The sample is a stratified random sample of about **6,700 SAT I registrants** — one in every 200
seniors registering for the October, November or December 1995 administrations and one in every 200
juniors for May or June 1996. About 4,200 responded (63%), of whom nearly 12% had attended a
coaching programme outside their school.

Because the treatment is self-selected, the authors ran seven estimators against the same data on
the theory that the true effect should lie inside their envelope.

| Model | n coached | SAT-V effect (SE) | SAT-M effect (SE) |
|---|---|---|---|
| Propensity matching | 233 | 6 (5) | 15 (4)** |
| Instrumental variable | 235 | 6 (4) | 16 (3)** |
| ANCOVA | 235 | 6 (4) | 18 (3)** |
| Raw change | 427 | 8 (3)** | 18 (3)** |
| Repeated measures | 427 | 8 (3)** | 18 (3)** |
| Belson | 469 | 8 (9) | 26 (9)** |
| Heckman | 237 | 12 (4)** | 13 (6)* |

The authors' own summary: *"if two outlier estimates are discounted… then, on average, coaching
seems to affect SAT I verbal scores by about 6–8 points, and SAT I math scores by about 13–18
points (or about twice as much as for verbal scores). By commonly used standards (Cohen, 1988),
these effects can be regarded as small."*

The estimand is a **difference in SAT scale points between coached and matched-uncoached test
takers on an operational retest**, not a pre-post gain. That distinction is the whole argument.
Raw pre-post gains in the same data were verbal 29 for coached and 21 for uncoached, math 40 and
22. A vendor reporting the coached column alone reports 29 and 40 as its "effect", and both numbers
are mostly regression, practice and real growth.

Against that, the advertised claims the authors quote from the two firms' websites in November 1997
are 120 combined points (Kaplan) and 140 (Princeton Review), with Princeton Review guaranteeing 100
and Kaplan claiming 28% of its students improve by at least 170. `VENDOR` Powers and Rock note that
these are documented *"only by surveying previous customers to ascertain score changes after
coaching."*

The most useful sentence in the paper is the one that converts the finding into a purchase decision:

> *"The largest effect that we noted in any of our analyses was about 33 points for SAT I math for
> one of the coaching programs. This effect is equivalent to about three or four additional
> questions correct on the 60-question math portion… Assuming that a coached student attending a
> major program spends nearly 40 hours in classroom instruction and perhaps another 10–20 hours
> completing homework assignments (and that approximately half of this time is devoted to the math
> portion of the test), the benefit is approximately one additional question correct for every eight
> or so hours of effort."*

One further detail: Table 6 splits by provider. One company's SAT-M effect ran 31–38 points across
estimators and was significant in six of seven; the other's ran 5–17 and was significant in none.
Verbal ran the other way. The authors declined to name them. `OBSERVED` The between-vendor spread is
larger than the average effect, and this is the only place in the literature where that appears.

### 1.2 Becker: the meta-analysis, and what moderates it

**Becker, B. J. (1990), "Coaching for the Scholastic Aptitude Test: Further synthesis and
appraisal," *Review of Educational Research* 60(3), 373–417** (`doi:10.3102/00346543060003373`,
abstract retrieved verbatim from Crossref). Forty-eight studies documented in 23 reports.
`MEASURED-META`

> *"Published comparison studies gave consistent results with coached groups exceeding controls by
> 0.09 standard deviations on SAT-V and 0.16 on SAT-M."*

The estimand is a standardised mean difference between coached and control groups. On the pre-1995
SAT with a section SD near 110, 0.09 SD ≈ 10 points and 0.16 SD ≈ 18. Powers & Rock report Becker's
raw-scale equivalents as about 9 verbal and 19 math, and note their own medians of 8 and 18 are
*"extremely similar."* These are not independent confirmations; Becker's corpus and the ETS work
share provenance and the two teams cite each other. **No manufactured independence:** treat them as
one literature with two readings.

The moderator list is where exam technique enters the record for the only time in a meta-analysis:
effect magnitude was related to *"whether instruction included test practice and attention to
test-taking skills, and whether homework was assigned to students."* `MEASURED-META` That is the
strongest measured support this report found for the proposition that exam technique per se does
anything. It is a moderator in a 1990 synthesis of studies the same author calls *"rather poorly
reported and designed."*

### 1.3 Briggs: the independent reanalysis, and the null inside it

**Briggs, D. C. (2001), "The effect of admissions test preparation: Evidence from NELS:88,"
*Chance* 14(1), 10–18** (draft recovered in full). Briggs's claim of independence is material: most
researchers with SAT and ACT score access are affiliated with the testing organisations, which he
identifies as one reason the public discounts small estimates. NELS:88 tracks a nationally
representative panel from Grade 8; 4,730 students took the PSAT, then the SAT or ACT, and answered
the test-preparation item. `OBSERVED` X1 controls only prior PSAT on the matching section; X2
approximates Powers & Rock's covariate set; X3 adds seven motivation proxies and five other
test-preparation activities.

| Specification | SAT-M | SAT-V | Combined |
|---|---|---|---|
| X1 (prior PSAT only) | +19 | +14 | 33 |
| X2 (+ demographics, ability) | +14 | +8 | 22 |
| X3 (+ motivation, other prep) | +15 | +6 | 21 |

Briggs's conclusion: *"After controlling for group differences, the average coaching boost on the
math section of the SAT is 14 to 15 points. The boost is smaller on the verbal section of the test,
just 6 to 8 points. The combined effect of coaching on the SAT for the NELS sample is about 20
points."*

The ACT results are the ones nobody quotes. Under full controls the coaching effect on ACT
mathematics is not statistically significant; on English it is +0.3 to +0.6 scale points; on
**reading it is negative, about −0.6 to −0.7**. Briggs offers the mechanism: coached students
perform worse on ACT reading than uncoached students matched on prior PSAT verbal. `OBSERVED` A
preparation regime tuned to one test's item style can transfer negatively to another test of the
same construct. That is Koretz's non-substantive coaching (§11) showing up as a sign flip.

Two calibration facts from the same data. Students retaking improved by about **33 points on math
and 27 on verbal with no intervention at all**, so a 20-point coaching effect is roughly a third of
what waiting a year already delivers. And coaching's benefit was largest for high-SES students with
good maths grades, smallest for those already scoring high on PSAT maths.

### 1.4 The Khan Academy study, correctly labelled

The claim in circulation is that 20 hours of Official SAT Practice on Khan Academy is worth 115
points. Its origin is a **College Board / Khan Academy press release of 8 May 2017**, and the
quantity is an average **PSAT/NMSQT-to-SAT score change** among students reporting 20 hours of study
in a cohort of about 250,000 early adopters, with no comparison group net of typical growth. Typical
growth between those two tests is large: Briggs's NELS figure is about 60 combined points for simply
waiting and retaking. Restating 115 as an effect is the arithmetic error Powers and Rock diagnosed
in 1999. `VENDOR`

The primary source is **Weatherholtz, K., Grimaldi, P., Hicks, C., Hill, K. M., Freeman, C.,
Akbayin-Sahin, B., Coker, C., Ma, J., & Henneman, L. (2020), *Use of Khan Academy Official SAT
Practice and SAT Achievement: An Observational Study*, Khan Academy technical report, first released
17 August 2020**. It is a working paper and says so: *"these working papers have not undergone blind
peer review, but they were reviewed externally by experts before their release."* Its methodological
reviewers were Derek Briggs and Laura O'Dwyer. Under this project's standard it is discounted
relative to a peer-reviewed estimate, and there is no peer-reviewed estimate.

What it reports, for the class of 2019, PSAT/NMSQT to **first** SAT, controlling for PSAT composite,
gender, race/ethnicity, parental education, administration type and weeks between tests: six or more
hours on the platform gives **+21 points, effect size 0.11**; six or more hours plus at least one of
three "best practice" behaviours (levelling up skills, completing a full practice exam, following
recommended tasks) gives **+39 points, effect size 0.20**; reaching 0.20 required 12.3 hours.
Appendix F's propensity-score check on the six-hours-plus-one-best-practice group returns ATT
estimates of **35.7 to 38.6** across logistic and GBM weighting.

And the retrospective correction of its own 2017 predecessor, in the report's own words: *"the
specific added growth from spending six to eight hours practicing on OSP was 30 additional points on
their last SAT compared to students who did not use OSP."* The 2017 study's controlled figure was 30
points, not 115.

The selection problem the authors state plainly: *"our analysis… cannot control for students'
self-selection and possible systematic confounds between our observed groups."* They could not
observe motivation, nor SAT preparation done elsewhere, so a student with low platform activity and
a private tutor is scored as a low-dose control.

`INFERENCE` (ours): the OSP estimate is the most credible large-N figure in the modern
test-preparation literature and it is bounded above by roughly 0.2 SD. It also sits inside the
Powers & Rock envelope once you convert: 39 points combined against a 21–34-point combined
commercial-coaching envelope. **A free platform and a $1,500 course produce effects of the same
order.** The distribution of usage is the more interesting number for a product: about 80% of users
spend under three hours, and the median is 1.8. The binding constraint on test-preparation efficacy
in the field is not efficacy per hour. It is hours.

---

## 2. Whose scores move

One moderator recurs across all four sources and bears directly on the project's equity claim.
Powers & Rock found math coaching effects correlated negatively with prior PSAT-M (r = −.12, lower
scorers gained slightly more) but positively with English grades (r = .14), maths grades (r = .12)
and parental education (r = .12 each). Briggs found coaching most effective for high-SES students.
The OSP report found best-practice behaviours least common where they would help most: in the bottom
PSAT quartile 5% levelled up 15+ skills against 24% in the top quartile, and 8% completed a practice
exam against 19%. `OBSERVED`

**Preparation is a complement to prior advantage, not a substitute for it**, and the free platform
reproduces the paid platform's gradient because the gradient lives in usage rather than in access.

---

## 3. NEET, JEE and the gaokao: an enormous market with no causal literature

This section reports an absence, established by stated queries, and treats the absence as the
finding.

**What exists.** ERIC's entire holding on Indian entrance-examination coaching, under the query
`"entrance exam" AND coaching AND India`, is two records, both sociological: Ørberg (2018) in
*Higher Education* on the JEE coaching industry's relationship with the IITs, and Punjabi (2020) in
*Contemporary Education Dialogue* on how IIT-JEE coaching pedagogy displaces school pedagogy in
Delhi. Neither estimates an effect on a score. `"shadow education" AND India AND achievement`
returns zero.

**Scale, from official statistics.** India's NSS 75th round (July 2017–June 2018) records private
coaching as **11.8% of average household education expenditure**, with incidence peaking at the
secondary level around 29–31% of students. `FILING` The 2025 Comprehensive Modular Survey on
Education reports roughly 27% of students taking private coaching, higher in urban areas. `FILING`

**Scale, from a filing.** Physics Wallah's FY25 disclosures ahead of its IPO report operating
revenue of ₹2,886.6 crore, of which coaching services contributed more than ₹2,498 crore, with 4.46
million paid users. `FILING` (Reported by Indian business press citing the company's DRHP; the
prospectus itself was not retrieved this session, so this is a second-hand reading of a primary
filing and should be re-verified before publication.)

**What does not exist.** No causal estimate of the effect of attending Kota, Allen, Aakash or
Physics Wallah on a NEET or JEE rank or score. No randomised trial. No regression-discontinuity
design exploiting a coaching-institute admission cutoff. No published estimate of selection: the
industry's headline metric is the count of its students in the top ranks, a survivorship statistic
on a population selected on ability at intake. `VENDOR`, and never restated here as a finding.

**China is one degree better, and the answer is null.** **Zhang, Yu (2013), "Does private tutoring
improve students' National College Entrance Exam performance? A case study from Jinan, China,"
*Economics of Education Review* 32, 1–28.** ERIC abstract, verbatim:

> *"This study finds that private tutoring has mixed and heterogeneous effects on mathematics,
> Chinese language, and English language respectively and on the NCEE total score. **The average
> effect of private tutoring is not significant**, but it may have a significant and positive effect
> on urban students with lower achievement or in schools with certain quality."*

`OBSERVED` (null). One city, one 2010 dataset, observational. It is the only estimate this session
located of tutoring's effect on the gaokao itself.

`INFERENCE`: the two largest examination-preparation markets on earth have between them one
non-significant observational estimate and zero trials. Everything else offered as evidence is a
selection statistic published by a seller. The design that would fix this is not exotic: coaching
institutes run their own entrance tests with score cutoffs, and a regression discontinuity at the
cutoff would identify the effect for marginal admits.

---

## 4. Past-paper practice as a distinct intervention

Retrieval practice and spacing are `F11`'s territory and are not re-derived. What `F11` does not
cover is the specific thing revising students do: work through complete previous examination papers
under something approaching examination conditions. Three results bear on it, and one of them is
uncomfortable.

**The first test is worth a lot; the tenth is worth little.** **Bangert-Drowns, R. L., Kulik, J. A.,
& Kulik, C.-L. C. (1991), "Effects of frequent classroom testing," *Journal of Educational
Research*.** Forty studies. ERIC abstract: students who took at least one test over 15 weeks scored
*"one-half of a standard deviation higher on criterion examinations than did students who took no
tests."* The 1986 conference version states the dose-response result that the journal abstract
drops: *"improvement was much smaller, about one-tenth of a standard deviation, when frequently
tested students were compared to other students who also received tests, only less frequently."*
`MEASURED-META`

That is a strongly diminishing return, and it constrains one of the two obvious AI product pitches.
An unlimited supply of practice papers is worth roughly 0.1 SD over a limited supply, against 0.5 SD
for the first paper over none. `INFERENCE`: the marginal value of the twentieth past paper is
mostly in what is *diagnosed* from it, not in the retrieval event itself. §13 builds on that.

**Format matters, and it matters in the direction that favours the harder format.** Stenlund,
Sundström & Jonsson (2016), *Educational Psychology*, n = 54, mean age 16: both multiple-choice and
short-answer practice testing beat rereading on short- and long-term retention, and short-answer
practice was superior to multiple-choice after correcting the latter for guessing. `MEASURED-RCT`
(small). Where a real examination uses constructed response, practice on multiple-choice
approximations is a weaker intervention than practice on the real format.

**The practice-testing effect size, carried across.** Adesope, Trevisan & Sundararajan (2017),
*RER* 87(3), 659–701: g = 0.51 against restudy, g = 0.93 against no activity, g = 0.61 overall.
Carried from `F11` §, which carried it from `B1`. `MEASURED-META`

**What is missing.** No trial was located that randomises complete past-paper practice under timed
conditions against an equal-time alternative, with a real public-examination outcome. The nearest
approaches are single-course quizzing studies with researcher-written items. The population that
does the most past-paper practice on earth — candidates for GCSE, A-level, the gaokao, NEET and JEE
— is not represented in the experimental literature at all. `OBSERVED — absence`

---

## 5. Cramming, costed

The trade-off has a shape, and the shape is a crossover interaction with a hinge measured in hours.

**Roediger, H. L., III, & Karpicke, J. D. (2006), "Test-enhanced learning: Taking memory tests
improves long-term retention," *Psychological Science* 17(3), 249–255.** Full text recovered.
`MEASURED-RCT`

Experiment 1 (n = 120, 20 per cell): after an initial reading of a prose passage, students either
restudied or took a recall test with no feedback, then took a final recall test at one of three
delays.

| Final test | Restudy | Test | Effect |
|---|---|---|---|
| 5 minutes | 81% | 75% | d = 0.52 favouring restudy |
| 2 days | 54% | 68% | d = 0.95 favouring testing |
| 1 week | 42% | 56% | d = 0.83 favouring testing |

The crossover is complete by two days. The tested group's one-week recall (56%) slightly exceeded
the restudy group's two-day recall (54%), which the authors describe as testing having *"prevented
forgetting of information for an additional 5 days relative to repeated study."*

Experiment 2 (n = 180, 30 per cell) escalates the dose. SSSS studied four times, SSST studied three
times and tested once, STTT studied once and tested three times. Recorded passes through the
passage: 14.2, 10.3 and 3.4.

| Final test | SSSS | SSST | STTT |
|---|---|---|---|
| 5 minutes | 83% | 78% | 71% |
| 1 week | 40% | 56% | 61% |

Proportional forgetting over the week: 52% for SSSS, 28% for SSST, 14% for STTT.

**Rawson, K. A., & Kintsch, W. (2005), "Rereading effects depend on time of test," *Journal of
Educational Psychology* 97(1), 70–80**, n = 423. Full text UNREACHABLE-IN-SESSION; ERIC abstract
verbatim: *"On an immediate test, performance was greater after massed versus single reading,
whereas performance for distributed rereading was not significantly greater than after single
reading. On a delayed test, performance was greater after distributed versus single reading, whereas
performance for massed rereading and single reading no longer differed significantly."* The delay
was **two days**. `MEASURED-RCT`

**So: what does cramming buy on a test tomorrow?** The answer is narrower than folklore. Massing
buys roughly 5–12 percentage points of recall on a test taken within minutes, and by 48 hours that
advantage has decayed to zero relative to a single reading. Cramming trades long-term retention for
short-term performance across a horizon of **hours**, not days. A student who crams on Thursday for
a Friday-morning examination is already outside the window where the evidence shows massing
winning.

**What does it cost at three months?** No cell in either experiment runs to three months, and this
report will not extrapolate one. What runs further is **Cepeda, Vul, Rohrer, Wixted & Pashler
(2008), "Spacing effects in learning: A temporal ridgeline of optimal retention," *Psychological
Science* 19(11), 1095–1102**, n > 1,350, gaps up to 3.5 months and test delays up to a year.
Crossref abstract, verbatim: *"when measured as a proportion of test delay, the optimal gap declined
from about 20 to 40% of a 1-week test delay to about 5 to 10% of a 1-year test delay."*
`MEASURED-RCT`

Read as a revision rule: for an examination one week away the optimal gap between two study episodes
is **one and a half to three days**, not zero. For an examination three months away it is roughly a
week to ten days. There is no test delay in the measured range at which zero gap is optimal.
`F11` §2.1 carries the companion figure from Cepeda et al. (2006): of 271 massed-versus-spaced
comparisons, 12 showed no effect or a negative effect.

`INFERENCE`, the practically useful one: **the defensible case for cramming is a case about
coverage, not about memory.** A student with four days and forty topics is not choosing between
massed and spaced encoding of the same material; they are choosing between shallow coverage of forty
topics and spaced coverage of twelve. That is an allocation problem with a probabilistic objective
(expected marks given a topic-sampling distribution). It is a different problem from the one the
spacing literature answers. Nobody has posed it as such. §13 does.

---

## 6. The three techniques coaching sells, and what is measured about them

### 6.1 Predicted questions and question spotting

Nothing was located that measures it. `OBSERVED — absence` The nearest evidence is indirect and it
is Koretz's (§11): substantive coaching, defined as *"an emphasis on the narrow, substantive aspects
of a test that capitalizes on a particular style or emphasis of test items,"* raises scores by
biasing performance on individual elements. Koretz's worked example is a teacher who noticed the
state test always used regular polygons and advised colleagues to teach only those. Question
spotting is that behaviour performed by the candidate rather than the teacher. Whether it raises a
score is not in doubt; whether the raised score means anything is the question. Koretz answers it
negatively.

### 6.2 Mark-scheme literacy

The construct — knowing how credit is allocated, and writing to it — has a small literature under
the heading of rubric transparency, weakly designed. The most-cited positive result is **Jonsson, A.
(2010), *Assessment in Education* 17(1)**: three successive cohorts of student teachers (n = 170,
154, 138); introducing self-assessment criteria, a scoring rubric and exemplars between the 2004 and
2005 cohorts produced **d = 3.21**, against d = 0.27 between 2005 and 2006 with no change.
`OBSERVED` A between-cohort difference of three standard deviations is not a plausible instructional
effect; it is far more likely an artefact of a changed instrument or changed marking, and the design
cannot separate those. Reported because it is what the field has, and flagged as uninterpretable.
Jonsson (2014) measures whether students appreciate and use rubrics, not attainment.

Panadero & Romero (2014), *Assessment in Education*, n = 218 pre-service teachers randomised to
rubric or non-rubric self-assessment, is the closest thing to a trial: the rubric group showed
higher reported strategy use, higher performance and higher self-assessment accuracy, and **also
more difficulty coping with stress and higher performance-avoidance self-regulation**, which the
authors call detrimental to learning. `MEASURED-RCT` (small, single task, pre-service teachers).
The tool that improves calibration also raises evaluative pressure. That interaction hands
straight to `R3`.

### 6.3 Time allocation within a paper

The psychometric side of this is well developed and the instructional side is empty. Speededness —
the extent to which scores depend on time limits rather than ability — has a measurement literature
going back to Dorans et al. (1988) on differential speededness by ethnic group on the SAT, and a
current one on how to score not-reached items (Gorgun & Bulut, 2021, *Educational and Psychological
Measurement*). What is absent is any trial of teaching time allocation.

The test-taking-strategies literature that does exist is scale development and think-aloud protocol:
Dodeen (2008), *Assessment & Evaluation in Higher Education*, builds a 31-item scale across four
samples (n = 50, 828, 553, 235) with subscales for "before-test", "time management", "during-test"
and "after-test"; Tunç & Şenel (2021) build another. ERIC query
`"test-taking strategies" AND meta-analysis` returns 96 records and no meta-analysis of an
intervention. `OBSERVED — absence`

`INFERENCE`: **exam technique, the product that a very large industry sells, is the least-measured
object in this report.** The one meta-analytic trace of it is Becker's 1990 moderator finding that
coaching programmes including test practice and test-taking skills produced larger effects. Everything
since is scale construction.

---

## 7. Why the market works: fluency mistaken for knowing

This is where the report meets the survey's central finding from a different direction. `survey/01`
establishes that active learning raises real learning while lowering felt learning (Deslauriers et
al. 2019). Revision produces the mirror image: **the technique that maximises felt learning is the
one that minimises real learning, and learners choose it overwhelmingly.**

**What learners actually do.** Karpicke, Butler & Roediger (2009), "Metacognitive strategies in
student learning: Do students practise retrieval when they study on their own?", *Memory* 17(4),
471–479. Free-report survey of 177 undergraduates at a highly selective university.

| Strategy | Listed it | Ranked it #1 |
|---|---|---|
| Rereading notes or textbook | 83.6% (148) | 54.8% (97) |
| Do practice problems | 42.9% | 12.4% |
| Flashcards | 40.1% | 6.2% |
| Rewrite notes | 29.9% | 12.4% |
| Practise recall (self-testing) | 10.7% (19) | 1.1% (2 of 177) |
| Highlight | 6.2% | 1.6% |

Forced choice after reading a chapter once: 57% would restudy, 18% would try to recall, 21% would do
something else. And of the 91% who said they do quiz themselves at some point, **68% said they do it
"to figure out how well I have learned the information I'm studying"** rather than because it
improves learning. Self-testing is used as a thermometer, not as a treatment. `OBSERVED`

**Why they choose it.** Roediger & Karpicke's Experiment 2 asked students at the end of the learning
session how well they thought they would remember the passage in a week (7-point scale):

| Condition | Predicted recall | Actual recall at 1 week |
|---|---|---|
| SSSS (read 14.2 times) | 4.8 | 40% |
| SSST | 4.2 | 56% |
| STTT (read 3.4 times) | 4.0 | 61% |

The prediction ordering is the exact inverse of the outcome ordering, and the differences are
significant (SSSS vs SSST d = 0.54; SSSS vs STTT d = 0.61). `MEASURED-RCT` Repeated reading produces
processing fluency, fluency is read as evidence of knowing, and the reading is wrong in a direction
that is stable and predictable.

The primary source for the mechanism is **Koriat, A., & Bjork, R. A. (2005), "Illusions of
competence in monitoring one's knowledge during study," *JEP: Learning, Memory, and Cognition*
31(2), 187–194**: judgments of learning are inflated whenever information present at study is absent
at test, because learners fail to discount the availability of the answer in front of them.
Rereading is the study condition that maximises that availability. The companion paper, **Koriat &
Bjork (2006), *Memory & Cognition* 34(5), 959–972**, shows the illusion is **remediable** by
manipulations that increase sensitivity to retrieval conditions at test. `Z1` §2.1 flags that this
corpus cites the remedy in `B1` and loses it downstream, and that its design rule "measure, never
ask" overstates a source literature which says stated judgment is biased and partly correctable.
That correction applies here: the revision assistant's job is to **ask under retrieval conditions**,
where the judgment is far better calibrated, not to stop asking.

**And the field's own verdict on the technique.** Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan,
M. J., & Willingham, D. T. (2013), "Improving students' learning with effective learning techniques:
Promising directions from cognitive and educational psychology," *Psychological Science in the
Public Interest* 14(1), 4–58. Full monograph recovered; Table 4 reproduced:

| Technique | Utility | Learners | Materials | Criterion tasks | Implementation | Educational contexts |
|---|---|---|---|---|---|---|
| Practice testing | High | P-I | P | P | P | P |
| Distributed practice | High | P-I | P | P-I | P | P-I |
| Elaborative interrogation | Moderate | P-I | P | I | P | I |
| Self-explanation | Moderate | P-I | P | P-I | Q | I |
| Interleaved practice | Moderate | I | Q | P-I | P | P-I |
| Summarisation | Low | Q | P-I | Q | Q | I |
| Highlighting | Low | Q | Q | **N** | P | **N** |
| Keyword mnemonic | Low | Q | Q | Q-I | Q | Q-I |
| Imagery for text | Low | Q | Q | Q-I | P | I |
| Rereading | Low | I | P | Q-I | P | I |

P = positive, N = largely ineffective, Q = positive under some conditions only, I = insufficient
evidence. `MEASURED-META`

Highlighting is the only technique carrying an **N** rating, and it carries two: on criterion tasks
and in educational contexts. The authors add a specific harm — highlighting *"may actually hurt
performance on higher-level tasks that require inference making"* (their reading of Peterson, 1992),
because underlining draws attention to individual concepts at the expense of connections across
them. On rereading: *"The relative disadvantage of rereading to other techniques is the largest
strike against rereading and is the factor that weighed most heavily in our decision to assign it a
rating of low utility."*

The two techniques rated high are the two things a competent revision system does. The five rated
low are what a learner does unaided. That gap is the product.

---

## 8. Homework, and the moderation everybody quotes wrong

### 8.1 What the two Cooper syntheses actually say

**Cooper, H. (1989)**, reviewing ~120 studies: of 20 experiments comparing homework to no homework
between 1962 and 1986, 14 favoured homework. The average high-school student in a homework class
outperformed 69% of the no-homework class; the junior-high effect was half that; *"in elementary
school, homework had no association with achievement gains."* Across 50 correlational studies the
average time-on-homework correlation was *"nearly r = 0"* in elementary, r = .07 in middle grades
and r = .25 in high school.

**Cooper, H., Robinson, J. C., & Patall, E. A. (2006), "Does homework improve academic achievement?
A synthesis of research, 1987–2003," *Review of Educational Research* 76(1), 1–62.** Full text
recovered. `MEASURED-META`

The experimental arm: five studies from which effect sizes could be computed, weighted mean
**d = 0.60, 95% CI [0.38, 0.82]**; the three with successful random assignment **d = 0.53 [0.29,
0.79]**; trim-and-fill imputing two missing effects lowers the pooled estimate to **d = 0.48 [0.22,
0.74]**. The sobering robustness check is the authors' own: recomputing with an assumed intraclass
correlation of .35 to account for classroom-level assignment gives d = 0.63 [0.03, 1.23], and *"the
mean d-index would not have been significant if an intraclass correlation of .4 was assumed."*

So the causal evidence that homework works is **five studies, three of them randomised, with a
pooled effect whose significance turns on an assumed clustering parameter**, and an estimand of a
standardised difference on unit tests, mostly secondary, over short durations. The correlational arm
is where the quotable number lives: 35 samples, weighted r = .243 [.240, .246] fixed, r = .161
random.

### 8.2 The grade-level moderation, correctly

Here is the table everybody paraphrases and nobody reads (Cooper et al. 2006, Table 9; random-effects
point estimates in parentheses):

| Moderator | k | Mean r |
|---|---|---|
| Grades K–6 | 10 | −.04 (+.05) |
| Grades 7–12 | 23 | +.25 (+.20) |
| Student-reported time | 30 | +.25 (+.19) |
| Parent-reported time | 7 | −.03 (−.02) |

The standard paraphrase is "homework does not work in primary school." Three corrections.

First, the K–6 estimate is **negative under fixed effects (r = −.04, CI [−.06, −.02]) and positive
and non-significant under random effects (r = +.05, CI [−.03, .13])**. The two models disagree about
the sign. Quoting either alone misrepresents the evidence.

Second, the correlational estimand is **self-reported time on homework**, not homework assigned. In a
population where struggling students take longer over the same assignment, a zero or negative
correlation is the expected observation under a *positive* causal effect. Cooper et al. say so
explicitly of the parent data.

Third, and this is the part that is almost never carried: **every one of the seven parent-report
correlations came from Grades K–6.** Respondent and grade band are confounded. The authors re-ran
the grade analysis using student reports only:

> Fixed model: secondary r = .25 versus elementary r = .06 [−.00, .11], Q(1) = 47.48, p < .0001.
> Random model: secondary r = .19 [.17, .22] versus elementary **r = .22 [−.00, .42], Q(1) = 0.57,
> ns.**

Under a random-effects model with respondent held constant, **the grade-level moderation
disappears**. The headline finding of the homework literature is partly an artefact of who was asked
how long the child worked. Cooper et al. state the reading themselves: *"for elementary school
students, parents report a small negative relationship between the amount of time their child spends
on homework and their achievement, while the students themselves report a positive relationship."*

`INFERENCE`: the defensible summary is that **assigned homework has a modest positive causal effect
at secondary level on aligned unit tests, resting on three randomised studies; that the elementary
evidence is too weak and too confounded to support a directional claim in either direction; and that
time-on-homework correlations are contaminated by reverse causation in a way that makes them nearly
uninterpretable as evidence about assignment policy.**

### 8.3 Parental involvement, where the sign is genuinely negative

**Patall, E. A., Cooper, H., & Robinson, J. C. (2008), "Parent involvement in homework: A research
synthesis," *Review of Educational Research* 78(4).** Twenty-two samples from 20 correlational
studies: positive associations at elementary and high school, **a negative association at middle
school**, strongest association for parental rule-setting, negative for mathematics achievement and
positive for verbal. Separately, 14 studies manipulating parent training produced higher homework
completion, fewer homework problems, and *"possibly improved academic performance among elementary
school children."* `MEASURED-META`

**Fernández-Alonso, R., Álvarez-Díaz, M., García-Crespo, F. J., Woitschach, P., & Muñiz, J. (2022),
"Should we help our children with homework? A meta-analysis using PISA data," *Psicothema* 34(1),
56–65.** Full text recovered. `MEASURED-META` One hundred and eighty effects, drawn from PISA 2009,
2012, 2015 and 2018 in every country that fielded the family questionnaire; effective samples in the
millions of weighted 15-year-olds.

> *"Students who had more help with homework had lower academic achievement, with an overall effect
> (d) = 0.23, 95% CI [0.21, 0.25]."*

Moderated by region: Europe d = 0.30 [0.27, 0.33]; Latin America and the Caribbean 0.19 [0.16, 0.22];
Southeast Asia 0.09 [0.07, 0.11]. Stable across subject (maths .24, reading .23, science .22) and
across the four PISA cycles. For Germany, Hungary and Croatia the authors estimate the gap between
frequently-helped and autonomous students at around a year and a half of schooling.

The caveat is large and the authors name it: this is cross-sectional, and the obvious mechanism is
reverse causation, with parents helping the children who are struggling. `INFERENCE` The regional
moderation is the pattern that reverse causation alone does not explain well, and the authors'
own conclusion is the useful design claim: *"it is more important how that help is given than how
much."* That maps directly onto Patall et al.'s finding that rule-setting is the strongest positive
form.

For an AI system this is the cleanest actionable result in the homework literature. **The role the
evidence supports is structure-setting and monitoring, not answer-supplying.** An assistant that
supplies the answer is doing the thing measured at d = 0.23 in the wrong direction.

---

## 9. Test anxiety: the interaction, then the hand-off

`R3` owns anxiety and this report will not duplicate it. One interaction belongs here because it is
about technique rather than affect.

The technique this report recommends most strongly — frequent low-stakes practice testing — is
routinely resisted on the grounds that it makes anxious students worse. The meta-analysis says the
opposite. **Yang, C., Li, J., Zhao, W., Luo, L., & Shanks, D. R. (2023), "Do practice tests (quizzes)
reduce or provoke test anxiety? A meta-analytic review," *Educational Psychology Review*.** Twenty-four
studies, 25 effects, 3,374 participants: practice tests **reduce** test anxiety, **g = −0.52**, with
strong Bayesian support (BF₁₀ > 25,000) and minimal evidence of publication bias. Easy practice tests
reduce anxiety more than difficult ones; the authors also note that quizzes are themselves more
stressful than other learning activities in the moment. `MEASURED-META`

The design consequence for a revision system is a difficulty schedule that opens easy. The
countervailing signal is Panadero & Romero's rubric result in §6.2, where the calibration tool also
raised performance-avoidance. Both go to `R3`.

---

## 10. Nulls, given their own space

**10.1 A five-year, twenty-thousand-student programme of study-skills coaching that moved study time
and nothing else.** Oreopoulos, P., et al. (2023), "The promises and pitfalls of using (mostly)
low-touch coaching interventions to improve college student outcomes," *The Economic Journal*,
`doi:10.1093/ej/uead064`. Crossref abstract, verbatim:

> *"We present results from a five-year effort to design promising virtual coaching interventions to
> improve college student achievement. Across nearly 20,000 students at three campuses, we find some
> improvement on study time, but no effect on academic outcomes. We interpret the results with unique
> survey data and a model of student effort. Treated students learn that more effort is needed to
> attain good grades and develop stronger preferences for high grades, but these effects are too
> small to translate into academic benefits."*

`MEASURED-RCT` (null). This is the strongest null available on the subject of this report: randomised,
published in a top-five economics journal, powered to detect small effects, and with the mediator
measured. The intervention changed the thing everyone assumes is the bottleneck (time spent) and did
not change the outcome. It is a direct constraint on any product whose theory of change is "get the
learner to study more."

**10.2 Rereading a real textbook chapter does not work.** Callender, A. A., & McDaniel, M. A. (2009),
"The limited benefits of rereading educational texts," *Contemporary Educational Psychology*. Four
experiments, textbook chapters and a *Scientific American* article, intentional-learning instructions,
assessed by multiple choice, short answer and text summaries. ERIC abstract: *"With only several
exceptions, rereading did not significantly increase performance on the assessments. We also found
that reading comprehension ability did not alter this pattern."* `MEASURED-RCT` (null). The estimand
is a difference between one reading and two readings on educationally realistic materials and
educationally realistic outcomes. The technique 83.6% of students report using has a null result
against doing it once, under the conditions closest to real study.

**10.3 Coaching does nothing for the learners who have never sat the test.** Briggs (2001), the
second population in his NELS analysis: students who took the SAT or ACT without having first taken
the PSAT. *"For students that do not take the PSAT first, the estimated effect of coaching is not
statistically significant for any of the sections of the SAT or ACT… In fact, the largest significant
effect size for a test preparation variable is a negative one associated with the use of a
preparatory video."* `OBSERVED` (null). This is the subgroup Briggs predicted a priori would gain
most, on the theory that preparation substitutes for the experience of sitting the test. It gained
nothing. Whatever coaching does, it appears to require a prior encounter with the instrument.

**10.4 The gaokao null.** Zhang (2013), §3: average effect of private tutoring on NCEE total score
not significant. `OBSERVED` (null).

---

## 11. The falsifier: a score can rise while nothing else does

Before proposing that examinations give this project a correctness oracle, the case against has to be
put at full strength.

**Koretz, D. (2005), *Alignment, High Stakes, and the Inflation of Test Scores*, CSE Report 655,
CRESST/UCLA** (also *Yearbook of NSSE* 104(2)). Full text recovered. It reports the first empirical
study of score inflation, **Koretz, Linn, Dunbar & Shepard (1991)**, and the design is a genuine
experiment embedded in a district.

A large district used a commercial multiple-choice achievement test through 1986, by which point its
third graders averaged a grade equivalent of 4.3 in mathematics, tested in the seventh month of grade
three — half an academic year above the national median. In 1987 the district switched to a competing
test and the average fell to 3.7, exactly national. Over three years it climbed back to 4.3. In 1990,
Koretz and colleagues administered the **retired** test to randomly selected classrooms. Those
classrooms scored half an academic year lower than the district's current test showed.
`MEASURED-RCT` (randomised assignment of classrooms to instruments)

> *"Regardless of the test used, students scored half a year lower on a test that was unexpected than
> on a test for which teachers had time to prepare."*

And the generalisation across the literature since:

> *"Typically, gains on high-stakes tests have been 3 to 5 times as large as gains on other tests
> (such as the National Assessment of Educational Progress) with low (or lower) stakes, and in
> numerous cases, large gains on high-stakes tests have been accompanied by no gains whatsoever on
> lower-stakes tests. Moreover, the problem is not confined to commercial, off-the-shelf,
> multiple-choice tests. It has appeared as well with standards-based tests and with tests using no
> multiple choice items."*

Koretz's taxonomy of test preparation is the most useful classification this report found, because it
separates preparation that produces real gains from preparation that produces inflation, and puts
most of the coaching industry in the second category:

1. **Working harder / teaching more effectively**, and 2. **teaching more** (extra hours) — both
   produce meaningful gains.
3. **Reallocation** — shifting instructional resources toward tested elements. Inflates when the
   deemphasised elements matter for the inference. Does not bias performance on individual elements.
4. **Alignment** — a special case of reallocation; no better protected.
5. **Coaching**, in two forms. *Substantive*: exploiting a narrow stylistic or content emphasis of
   the items. *Non-substantive*: distractor characteristics, unimportant features of scoring rubrics,
   process of elimination, plug-in. Koretz: *"In some cases… a modest amount of certain types of
   non-substantive coaching can increase scores and improve validity by removing irrelevant barriers
   to performance. In most cases, however, it either wastes time or inflates scores."*
6. **Cheating** — no meaningful gains by construction.

And the mechanical distinction that matters most for §12:

> *"Reallocation and alignment inflate scores by making the tested elements unrepresentative of the
> domain as a whole, without biasing estimates of performance on individual elements. In contrast,
> coaching does bias performance on individual elements."*

The principle behind all of it is **Campbell, D. T. (1979), *Evaluation and Program Planning* 2(1),
67–90**: *"The more any quantitative social indicator is used for social decision-making, the more
subject it will be to corruption pressures and the more apt it will be to distort and corrupt the
social processes it is intended to monitor."* Campbell's own 1976 education example: *"when test
scores become the goal of the teaching process, they both lose their value as indicators of
educational status and distort the educational process in undesirable ways."*

`INFERENCE`: what §1 measured is item 5 on Koretz's list. The coaching industry sells substantive and
non-substantive coaching, its measured effect is 0.1–0.2 SD, and Koretz's framework predicts that
most of that small effect is inflation rather than learning. Briggs's negative ACT-reading coefficient
is what that prediction looks like when the preparation is aimed at a different instrument.

---

## 12. Is a mark scheme pedagogy's `pytest`? Testing the claim hard

`survey/32` argues that agentic capability is bounded by the quality of the external check, that
coding agents work because `pytest` exists, and that *"pedagogy has no `pytest`, and every agentic
capability is waiting on one."* Public examinations look like a counter-example, because they ship
the one artefact the rest of education does not: a published, externally audited, per-item scoring
rubric. Before committing to that, four objections.

**Objection 1: a mark scheme checks the learner's answer, not the tutor's diagnosis.** This is
correct and it is the decisive scoping point. `pytest` verifies the *agent's* output. In tutoring the
agent's output is an explanation or a diagnosis, and a mark scheme says nothing about either. The
corrected `survey/32` states the boundary well: *"Step-error identification in a model's own
reasoning trace is not at chance. Diagnosing what a learner believes from what they did is."* A mark
scheme grades the artefact and is silent about the belief. So the claim cannot be "exams solve the
verifier problem."

**Objection 2: the oracle is gameable, and the gaming is measured.** §11. Optimising against a scoring
rubric produces gains of 3–5× the gain on an unoptimised instrument, and Koretz's specific finding is
that coaching *biases performance on individual elements* — meaning the per-item signal itself, the
thing that looks most like a unit test, is the part most susceptible to corruption. A `pytest` that
the agent can overfit is a `pytest` you cannot trust as a fitness function.

**Objection 3: mark schemes are not deterministic**, since extended-response marking has real
inter-rater variance (`C2` owns that machinery). A rubric two examiners apply differently is a flaky
test. **Objection 4: the domain is narrow.** Public examinations cover perhaps a dozen years of a
learner's life in a subset of subjects; nothing in early literacy, vocational skill or the SELPA
population this project centres has a comparable artefact.

**What survives all four.** Something does, and it is narrower and more useful than the headline.

A mark scheme provides a **per-item ground-truth signal on a held-out instrument**, at a granularity
of one or two marks, for millions of released items across decades, in the exact format the learner
will face. That is not a verifier for the tutor's diagnosis. It is a **falsifiable prediction target**
for the tutor's *model of the learner*. Restate the loop: instead of asking a model to judge whether
its own explanation was good, ask it to **predict, before the learner attempts a past paper, which
marks the learner will lose and why**. Then mark the paper against the published scheme. The
prediction is scored automatically. Diagnostic accuracy becomes a measurable quantity with a
per-item resolution and no human in the loop.

That reframing does two things. It converts an unverifiable output (an explanation) into a verifiable
one (a prediction), which is the same move that made `pytest` useful. And it gives Koretz's objection
a defence: **the fitness function is prediction accuracy on unseen papers, not score on seen ones**.
A system that inflates the score by teaching item-style tricks will not thereby improve its
predictions on a paper drawn from a different year with a different emphasis; if anything it will
degrade them, because its learner model will have absorbed a stylistic regularity rather than a
knowledge state. Score inflation and prediction accuracy come apart, and the second is the safer
target.

`INFERENCE`, stated as ours and offered for demolition: **the mark scheme is not pedagogy's `pytest`,
but it is pedagogy's held-out test set, and this survey has been treating the absence of the first as
though it implied the absence of the second.** The two are different instruments with different jobs.
`survey/32`'s rule — never ship an agentic loop without naming its external check — is satisfied here
by an artefact that already exists, is free, and is published annually by every examination board on
earth.

---

## 13. What a system can do here that a coaching centre cannot

Everything in this section is `SPEC` unless labelled otherwise. None of it is measured. Each item
names what would show it was the wrong design.

**13.1 Per-item diagnosis of why a mark was lost, not whether.** A coaching centre marks a past paper
and returns a score and a worked solution. The information a learner needs is the attribution: was
this mark lost to a knowledge gap, a misread question, a procedural slip, a mark-scheme convention
not followed, or running out of time? Those five failures have five different remedies and the
industry's feedback loop does not distinguish them. Bangert-Drowns's dose-response result (§4) is the
reason this matters commercially: the marginal past paper is worth ~0.1 SD, so the value has to come
from what is extracted per paper, not from paper count.

*Falsifier*: if per-item attributions produced by the system agree with expert human attributions at
no better than chance, the whole design collapses. This is testable today against marked scripts and
should be tested before anything is built on it. TutorGym's result (`survey/32`) says the adjacent
operation is hard; ProcessBench and the BEA 2025 shared task say the neighbouring operations are not.
The specific question — attribute a lost mark on a real examination script to one of five causes — is
unmeasured. `OBSERVED — absence`

**13.2 Calibrated generation instead of a fixed bank.** Every coaching centre has a finite item bank,
which is why question spotting works and why the same predicted questions circulate. A generator
conditioned on a published specification and calibrated against released items produces an unbounded
supply at a chosen difficulty. `C2` owns the psychometrics of whether generated items behave. The
revision-specific requirement is **difficulty targeting on the learner's current posterior**, which
`J1` and `F5` already specify machinery for.

*Falsifier*: if generated items' empirical difficulty does not track their intended difficulty, the
supply is unlimited and useless.

**13.3 The allocation problem, posed properly.** §5 ended on it. A candidate with four days and forty
topics faces an expected-marks maximisation under a topic-sampling distribution that past papers
estimate directly: count how often each specification point has appeared, weight by marks, condition
on the learner's per-topic posterior, and allocate remaining hours to maximise expected marks. This is
a small optimisation problem with real inputs and it is the calculation every candidate performs badly
by intuition. Neither the spacing literature nor the coaching industry poses it.

*Falsifier*: if a randomised comparison of optimiser-allocated revision against learner-allocated
revision does not move marks, the intuition was already good enough. That trial is §14's proposal.

**13.4 Retrieval conditions for the confidence question.** §7 established that asking a learner how
well they know something is biased when the material is in front of them and better calibrated when
it is not (Koriat & Bjork 2006). The design rule is therefore not "never ask" but **"ask only after a
closed-book attempt, never before."** This is a one-line change to the interaction protocol and it
corrects a rule this corpus over-generalised.

**13.5 The one thing not to build.** Oreopoulos's null (§10.1) says an intervention whose mechanism
is encouragement, nudging or time-management advice does not move outcomes at n = 20,000. Anything in
this space that reduces to messaging should be assumed ineffective until a trial says otherwise.

**13.6 The homework role the evidence supports.** §8.3: structure-setting and monitoring, measured
positively; answer-supplying, measured at d = 0.23 in the wrong direction. For a system with a parent
in the loop, the parent-facing product is a structure, and the child-facing product is a tutor. They
should not be the same surface.

---

## 14. What is now buildable, the experiment worth running, and what I could not find out

### 14.1 Buildable now, that was not before this report

Three things changed status.

**The score is no longer an unmeasurable target.** Before this report the project's stated markets
were named and their evidence base was unexamined. It is now bounded: commercial coaching moves an
admissions test by 0.09–0.16 SD, the best free digital alternative moves it by 0.11–0.20 SD, and
nobody has measured NEET, JEE or the gaokao at all. A product entering this market should promise a
number in that range and should say so, because the competition's advertised numbers are three to
seven times their measured ones and that gap is now documented well enough to be used.

**The revision loop has a specified floor.** Five findings compose into a default schedule that
requires no new capability: closed-book retrieval rather than rereading (Dunlosky's two high-utility
techniques against the five low); a first practice test early, because the first test is worth 0.5 SD
and the tenth 0.1; review gaps of 20–40% of the time remaining, from Cepeda's ridgeline; confidence
elicited only after a closed-book attempt; and easy practice items first, from Yang's anxiety
moderator. `survey/32`'s item 4 — "an agent whose only job is enforcing the boring floor" — now has a
revision-specific instantiation.

**The verification argument has a boundary.** §12. Mark schemes are a held-out test set for a
learner-model's predictions, and are not a verifier for a tutor's explanation. Stating that boundary
lets the project use the artefact without overclaiming, and gives `survey/32` a scope it currently
lacks.

### 14.2 The single highest-value experiment

**Randomise revision allocation, not revision technique.**

*Design.* Candidates for a public examination with published past papers and mark schemes (GCSE or
A-level mathematics is the cleanest, because mark schemes are granular and the specification is
stable). Randomise at the individual level to two arms. Control: full access to the same past-paper
library, the same generated items, and the same marking, with the learner choosing what to work on.
Treatment: identical resources, with the system allocating each session's topics by expected-marks
maximisation over the learner's per-topic posterior and the specification's historical topic weights
(§13.3). Both arms get closed-book retrieval and the same spacing defaults, so the contrast isolates
**allocation** and nothing else. Primary outcome: marks on the real public examination. Secondary:
per-topic marks, to test whether any gain is concentrated where the optimiser reallocated.

*Why this contrast and not "AI tutor versus nothing."* Every ingredient except allocation is either
already established (retrieval, spacing) or already null (nudging). Allocation is the one degree of
freedom that is both large and unmeasured, the one a coaching centre structurally cannot
personalise because it teaches a cohort.

*Power.* The effects worth detecting are the size of the ones this report measured: 0.10–0.20 SD.
For a two-arm individually-randomised trial at 80% power and α = .05 two-sided, detecting d = 0.15
requires **n ≈ 700 per arm, 1,400 total**. Conditioning on a pre-test — and the analogue here is
strong, since the OSP study's PSAT covariate and Briggs's PSAT controls both show prior-test
correlations near .9 with the outcome — an ANCOVA adjustment with ρ = 0.80 multiplies the required n
by (1 − ρ²) = 0.36, giving **n ≈ 252 per arm, about 510 total**. Add 20% for attrition between
consent and the examination sitting and the trial is **roughly 620 candidates**. That is a
single-school-district trial, not a national programme, and it produces a marks outcome that is
externally scored, publicly documented, and immune to the LLM-as-judge failure `survey/32` warns
about.

*The audit condition that makes it credible.* §11 requires it. Add a third, small arm or a
within-subject audit: a held-out instrument the system never trained or allocated against — a paper
from a different examination board covering the same specification. If the treatment arm's gain
appears on the primary examination and not on the audit paper, the system has produced score
inflation and the trial has said so. **No test-preparation study in this literature has ever included
an audit instrument, and every one of them should have.**

### 14.3 What I could not find out

- **Whether coaching for NEET, JEE, GATE, EAMCET or the gaokao does anything.** One non-significant
  observational estimate exists for the gaokao (Zhang 2013). For India there is nothing causal at all,
  only ethnography and vendor selection statistics. The identification strategy is sitting in plain
  view — coaching institutes admit on their own entrance tests with score cutoffs — and nobody has
  used it.
- **Whether exam technique, as taught, does anything.** Becker's 1990 moderator finding is the only
  meta-analytic trace. Since then the literature is scale development. No trial of teaching time
  allocation, question interpretation, or mark-scheme reading against an equal-time control was
  located.
- **Whether past-paper practice under timed conditions differs from untimed practice testing.** The
  laboratory testing effect is established at g ≈ 0.5–0.6. Whether the timed, full-paper,
  exam-conditions version adds anything beyond it is unmeasured.
- **Rawson & Kintsch's cell means.** Full text UNREACHABLE-IN-SESSION behind APA. The direction is
  quoted verbatim from the abstract and no numeric claim here rests on it.
- **Physics Wallah's prospectus at first hand.** §3's revenue and user figures come from business
  press citing the DRHP; the filing itself was not retrieved and the numbers should be re-verified
  against SEBI before publication.
- **Whether the per-item mark-loss attribution in §13.1 is achievable at above-chance accuracy.**
  This is the load-bearing empirical unknown for the constructive half of this report, it is cheap to
  test against marked scripts, and it has not been tested by anyone.

---

## References

1. Bangert-Drowns, R. L., Kulik, J. A., & Kulik, C.-L. C. (1991). Effects of frequent classroom
   testing. *Journal of Educational Research*. ERIC EJ435387 / ED274677 (1986 conference version).
2. Becker, B. J. (1990). Coaching for the Scholastic Aptitude Test: Further synthesis and appraisal.
   *Review of Educational Research*, 60(3), 373–417. doi:10.3102/00346543060003373
3. Briggs, D. C. (2001). The effect of admissions test preparation: Evidence from NELS:88. *Chance*,
   14(1), 10–18. (Author's draft, NEPC.)
4. Briggs, D. C. (2002). *SAT Coaching, Bias and Causal Inference*. PhD dissertation, UC Berkeley.
5. Callender, A. A., & McDaniel, M. A. (2009). The limited benefits of rereading educational texts.
   *Contemporary Educational Psychology*. ERIC EJ842288.
6. Campbell, D. T. (1979). Assessing the impact of planned social change. *Evaluation and Program
   Planning*, 2(1), 67–90.
7. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in
   verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380. [carried from F11]
8. Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in
   learning: A temporal ridgeline of optimal retention. *Psychological Science*, 19(11), 1095–1102.
   doi:10.1111/j.1467-9280.2008.02209.x
9. Cooper, H. (1989). *Homework*. Longman. (Summarised in ref. 10, pp. 4–5.)
10. Cooper, H., Robinson, J. C., & Patall, E. A. (2006). Does homework improve academic achievement?
    A synthesis of research, 1987–2003. *Review of Educational Research*, 76(1), 1–62.
11. Dodeen, H. (2008). Assessing test-taking strategies of university students. *Assessment &
    Evaluation in Higher Education*.
12. Dorans, N. J., et al. (1988). *The Standardization Approach to Assessing Differential
    Speededness*. ETS. ERIC ED303504.
13. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). Improving
    students' learning with effective learning techniques. *Psychological Science in the Public
    Interest*, 14(1), 4–58. doi:10.1177/1529100612453266
14. Fernández-Alonso, R., Álvarez-Díaz, M., García-Crespo, F. J., Woitschach, P., & Muñiz, J. (2022).
    Should we help our children with homework? A meta-analysis using PISA data. *Psicothema*, 34(1),
    56–65. doi:10.7334/psicothema2021.65
15. Gorgun, G., & Bulut, O. (2021). A polytomous scoring approach to handle not-reached items in
    low-stakes assessments. *Educational and Psychological Measurement*.
16. Jonsson, A. (2010). The use of transparency in the "interactive examination" for student teachers.
    *Assessment in Education*, 17(1).
17. Jonsson, A. (2014). Rubrics as a way of providing transparency in assessment. *Assessment &
    Evaluation in Higher Education*.
18. Karpicke, J. D., Butler, A. C., & Roediger, H. L., III (2009). Metacognitive strategies in
    student learning: Do students practise retrieval when they study on their own? *Memory*, 17(4),
    471–479.
19. Koretz, D. (2005). *Alignment, High Stakes, and the Inflation of Test Scores*. CSE Report 655,
    CRESST/UCLA. ERIC ED488711. Also *Yearbook of NSSE*, 104(2).
20. Koretz, D., Linn, R. L., Dunbar, S. B., & Shepard, L. A. (1991). The effects of high-stakes
    testing: Preliminary evidence about generalization across tests. AERA/NCME, Chicago. (Reported in
    full in ref. 19.)
21. Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one's knowledge during
    study. *JEP: Learning, Memory, and Cognition*, 31(2), 187–194.
22. Koriat, A., & Bjork, R. A. (2006). Illusions of competence during study can be remedied by
    manipulations that enhance learners' sensitivity to retrieval conditions at test. *Memory &
    Cognition*, 34(5), 959–972.
23. Ministry of Statistics and Programme Implementation, Government of India. *Key Indicators of
    Household Social Consumption on Education in India*, NSS 75th Round (July 2017–June 2018); and
    *Comprehensive Modular Survey: Education* (2025).
24. Oreopoulos, P., et al. (2023). The promises and pitfalls of using (mostly) low-touch coaching
    interventions to improve college student outcomes. *The Economic Journal*.
    doi:10.1093/ej/uead064
25. Ørberg, J. W. (2018). Uncomfortable encounters between elite and "shadow education" in India.
    *Higher Education*.
26. Panadero, E., & Romero, M. (2014). To rubric or not to rubric? *Assessment in Education*, 21(2).
27. Patall, E. A., Cooper, H., & Robinson, J. C. (2008). Parent involvement in homework: A research
    synthesis. *Review of Educational Research*, 78(4). ERIC EJ896560.
28. Powers, D. E., & Rock, D. A. (1999). Effects of coaching on SAT I: Reasoning test scores.
    *Journal of Educational Measurement*, 36(2), 93–118. ETS RR-98-53, ERIC ED562638.
29. Punjabi, S. (2020). Is shadow education becoming the "new" formal? *Contemporary Education
    Dialogue*.
30. Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests
    improves long-term retention. *Psychological Science*, 17(3), 249–255.
31. Rawson, K. A., & Kintsch, W. (2005). Rereading effects depend on time of test. *Journal of
    Educational Psychology*, 97(1), 70–80. doi:10.1037/0022-0663.97.1.70 (abstract only; full text
    UNREACHABLE-IN-SESSION).
32. Stenlund, T., Sundström, A., & Jonsson, B. (2016). Effects of repeated testing on short- and
    long-term memory performance across different test formats. *Educational Psychology*.
33. Weatherholtz, K., Grimaldi, P., Hicks, C., Hill, K. M., Freeman, C., Akbayin-Sahin, B., Coker,
    C., Ma, J., & Henneman, L. (2020). *Use of Khan Academy Official SAT Practice and SAT
    Achievement: An Observational Study*. Khan Academy technical report (working paper).
34. Yang, C., Li, J., Zhao, W., Luo, L., & Shanks, D. R. (2023). Do practice tests (quizzes) reduce
    or provoke test anxiety? A meta-analytic review. *Educational Psychology Review*.
35. Zhang, Yu (2013). Does private tutoring improve students' National College Entrance Exam
    performance? A case study from Jinan, China. *Economics of Education Review*, 32, 1–28. ERIC
    EJ997907.
36. Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). Rethinking the use of tests: A
    meta-analysis of practice testing. *Review of Educational Research*, 87(3), 659–701. [carried
    from F11 / B1]

**Cross-references within this corpus:** `F11` (spacing, retrieval, FSRS — not re-derived here),
`B1` (learning-science floor), `C2` and `F1` (psychometrics, assessment), `J1` and `F5` (learner
model, difficulty targeting), `N2` and `V5` (executive function, prequestions), `survey/32`
(the verifier argument this report bounds), `Z1` §2.1 (the Koriat & Bjork remedy this corpus
dropped downstream), `R3` (test anxiety, handed off in §9).

---
title: "Anxiety, threat and self-concept — the affective layer that is not motivation, and what a private tutor can and cannot do about it"
wave: R
section: R3
date_researched: 2026-07-30
sources_count: 46
status: raw-research
---

# R3 — Maths anxiety, test anxiety, stereotype threat, mindset, self-concept

> **Why this report exists.** `Z1` row 11 found the clinical-affective layer absent from the
> corpus: `math anxiety` 2 hits, `test anxiety` 0, `stereotype threat` 0, `self-concept` 3,
> `growth mindset` 0. `F6` owns *why learners quit*. It does not own *why a specific child
> freezes on a worksheet they can discuss fluently*. Those are different mechanisms.
>
> **The five findings, stated first.**
>
> 1. The maths-anxiety/achievement correlation is real, replicated across half a century, and
>   small: r ≈ −.28 pooled over 747 effect sizes. It is a *pairing*, not a diagnosis. In the
>   largest prevalence study, **77% of children with high maths anxiety had typical or high
>   maths performance**, and in the meta-analysis the correlation collapses to r = −.09 in
>   samples selected for low maths ability. A system that treats anxiety as a proxy for a
>   knowledge gap will mis-route roughly three quarters of the anxious children it meets.
> 2. Direction is genuinely bidirectional and the two arms have different evidence. Prior
>   *performance* predicting later *anxiety* is the arm supported by longitudinal data;
>   anxiety depressing performance is the arm supported by experimental manipulation. This
>   means the intervention question has no single answer, and it is answerable by a
>   three-arm trial that nobody has run.
> 3. The working-memory mechanism is specific enough to be an item-selection rule. Anxiety
>   costs capacity only when the task loads it: computation-based span correlates −.40 with
>   maths anxiety while verbal span shows no group difference at all, and the damage in the
>   dual-task study appeared on carry problems under high load, not on the rest.
> 4. Two of the five constructs the audit named do not survive contact with their replication
>   records in the textbook form. Stereotype threat in operational testing conditions is
>   d = −.14 falling to −.09 after trim-and-fill and **d = −.01 in the four actual
>   high-stakes samples**. Growth-mindset interventions restricted to trials where the
>   manipulation check passed are d̄ = 0.04, 95% CI [−0.01, 0.10]. The moderated versions of
>   both survive; the general versions do not.
> 5. The survey's most reproducible finding is present here in its cleanest form. In the
>   National Study of Learning Mindsets the intervention moved the belief it targeted by
>   0.33 SD and moved higher-achieving students' grades by 0.01 SD, in the same
>   pre-registered trial. Felt change and real change dissociate, and every affective
>   feature this report proposes is therefore specified with a delayed unassisted outcome
>   attached.

---

## Source reachability log (2026-07-30)

WebSearch budget exhausted mid-session at 200 calls, per the pattern `N2` and `Z1` both
record. Retrieval then ran on **ERIC** (`api.ies.ed.gov`), **Europe PMC** (search +
`fullTextXML`), **Crossref REST**, and the **arXiv API**. Semantic Scholar returned `HTTP 429`
on every attempt in two bursts and contributed nothing.

- **Open PDFs that served to `curl` and `pdftotext`, quoted verbatim below:** Barroso et al.
  (2021) accepted manuscript at `psycnet.apa.org/manuscript/2020-80018-001.pdf`; Caviola et al.
  (2022) at the Genoa IRIS repository; Flore & Wicherts (2015) at a Warsaw mirror; Shewach
  et al. (2019) and Warne (2022) at `gwern.net`; Macnamara & Burgoyne (2023) at
  `englelab.gatech.edu`; the EEF *Changing Mindsets* evaluation report at UCL Discovery;
  Sammallahti et al. (2023) at `files.eric.ed.gov`; Ashcraft & Krause (2007) at
  `link.springer.com/content/pdf/`.
- **Europe PMC `fullTextXML`** recovered the Yeager et al. (2019) *Nature* paper in full
  (`PMC6786290`), including every coefficient and confidence interval quoted in §5.
- **Publisher walls hit:** SAGE, Wiley, Taylor & Francis, Elsevier and `nature.com` all
  returned `403` or an identity-provider redirect. Flore, Mulder & Wicherts (2018) was
  recovered from the Tilburg research portal rather than the journal.
- **UNVERIFIED and flagged at point of use:** the cell means and interaction statistics of
  Beilock & Carr (2005). Three routes (ResearchGate, Semantic Scholar, SAGE) returned 403 or
  empty. The finding is reported from the published abstract and from Ashcraft & Krause's
  description of the adjacent Beilock, Kulp, Holt & Carr (2004) work, and no design claim in
  this report rests on the unretrieved numbers alone.
- **Working-paper discount applied once:** Bula et al. (2025), a PsyArXiv preprint on
  Finnish grades 2–3, is used in §2 as corroboration only and is labelled as a preprint at
  point of use. No conclusion rests on it.

**Evidence labels** are the project standard: `MEASURED-RCT` · `MEASURED-META` · `OBSERVED` ·
`INFERENCE` · `SPEC` · plus `OBSERVED — absence` for a gap established by a stated,
reproducible query, which is never treated as proof of non-existence.

**Builds on, does not repeat:** `F6` (self-determination, gamification, attrition), `N2`
(executive function, help-seeking, seductive detail), `H1` §4.7 (which opens this subject and
which §2.3 below corrects), `H2` (SELPA practitioner reality), `F11` (retrieval and spacing),
`survey/05` §8 (the machine-audience hypothesis, which §8 here supplies evidence for and
against).

---

## 0. The numbers that carry the argument

| # | Quantity | Value | Source | Label |
|---|---|---|---|---|
| 1 | Maths anxiety × maths achievement, the founding estimate | r = **−.27**, 26 studies, elementary and secondary | Ma 1999, *JRME* 30(5) | `MEASURED-META` |
| 2 | The modern replacement | r = **−.28** [−.29, −.26], 223 studies / 747 effect sizes, 1992–2018, I² = 90.42 | Barroso et al. 2021, *Psych. Bull.* | `MEASURED-META` |
| 3 | The largest by participants | r = **−.30** [−.32, −.28], 177 studies / 250 samples / 906,311 participants | Caviola et al. 2022, *EPR* 34 | `MEASURED-META` |
| 4 | …the same paper's test-anxiety estimate | r = −.23 [−.26, −.19], notably weaker than maths anxiety | ibid. | `MEASURED-META` |
| 5 | Barroso's grade-level gradient | grades 3–5 −.20 [−.25, −.14]; 6–8 −.30; **9–12 −.34** [−.36, −.31] | Barroso et al. 2021 | `MEASURED-META` |
| 6 | Barroso's ability moderator | samples selected for **low** maths ability r = **−.09** [−.17, −.004], k = 18, vs −.28 elsewhere | ibid. | `MEASURED-META` |
| 7 | Publication-status moderator, same paper | published k = 520 r = −.29; unpublished k = 227 r = −.23; Egger z = 2.59, p = .01 | ibid. | `MEASURED-META` |
| 8 | …and the direction of the missing studies | trim-and-fill imputes 129 effect sizes **to the left**; adjusted r = −0.29 | ibid. | `MEASURED-META` |
| 9 | Children with developmental dyscalculia who are highly maths-anxious | **twice** the rate of typically-performing children | Devine et al. 2018, *JEP*, n = 1,757 | `OBSERVED` |
| 10 | Children with high maths anxiety who have typical or high maths performance | **77%** | ibid. | `OBSERVED` |
| 11 | Maths anxiety × computation-based working-memory span | r = **−.40**; verbal-based spans show **no** anxiety-group difference | Ashcraft & Kirk 2001, via Ashcraft & Krause 2007 | `OBSERVED` |
| 12 | Maths anxiety × working memory, pooled | r = −0.168 [−0.203, −0.133], 57 studies / 66 samples / 16,589 participants, I² = 75.6% | Finell et al. 2022 | `MEASURED-META` |
| 13 | …the mediated path from anxiety through WM to performance | indirect effect −0.092 [−0.169, −0.015], **8 studies**, 1,824 participants | ibid. | `MEASURED-META` |
| 14 | Test-anxiety interventions, university students | test anxiety g = **−0.76**; academic performance g = **0.37**; 44 RCTs, n = 2,209; publication bias found | Huntley et al. 2019, *J. Anxiety Disord.* | `MEASURED-META` |
| 15 | Mindfulness for test anxiety | ES = −0.716 [−1.383, −0.049], 18 studies / 1,275 participants; Egger p = .025; **no achievement outcome anywhere in the meta** | Yılmazer et al. 2024 | `MEASURED-META` |
| 16 | Maths-anxiety interventions | anxiety g = −0.467; performance g = 0.502; 50 studies / 75 effect sizes; Egger significant on both | Sammallahti et al. 2023, *J. Numerical Cognition* | `MEASURED-META` |
| 17 | …and the study-quality gradient inside it | higher EPHPP quality ratings associated with **non-significant** outcomes | ibid. | `MEASURED-META` |
| 18 | Stereotype threat in schoolgirls | g = −0.22 [−0.34, −0.10], k = 47, I² = 61.75%, credibility interval [−0.85, 0.41] | Flore & Wicherts 2015, *JSP* | `MEASURED-META` |
| 19 | …after trim-and-fill (11 imputed) | g = **−0.07** [−0.21, 0.06], **p = .27** | ibid. | `MEASURED-META` |
| 20 | …small (N < 60) vs large (N ≥ 60) samples | −0.34 [−0.52, −0.16] vs **−0.13, p = .10** | ibid. | `MEASURED-META` |
| 21 | Stereotype threat, overall | d = −.31, k = 181, N = 10,436 | Shewach et al. 2019, *JAP* | `MEASURED-META` |
| 22 | …restricted to operational-test-like conditions | d = **−.14**, k = 45, N = 3,532; trim-and-fill **−.09** | ibid. | `MEASURED-META` |
| 23 | …in actual high-stakes settings | d = **−.01**, k = 4, N = 1,670, vs lab d = −.36, t(179) = −5.73, p < .01 | ibid. | `MEASURED-META` |
| 24 | …with monetary incentives present | d = **.00**, k = 9, N = 526 | ibid. | `MEASURED-META` |
| 25 | Large pre-registered replication, Dutch high schools | **no** overall effect and **no** moderated effect, N = 2,064 | Flore, Mulder & Wicherts 2018 | `MEASURED-RCT` (null) |
| 26 | NSLM: effect on the *belief* the intervention targets | fixed-mindset beliefs B = −0.38, SE .04, n = 5,650, t = −10.14, p < .001, **SMD 0.33** | Yeager et al. 2019, *Nature* | `MEASURED-RCT` |
| 27 | NSLM: effect on core GPA, **lower-achieving** students | B = **0.10** grade points [0.04, 0.16], SE .03, n = 6,320, k = 65, p = .001, **SMD 0.11** | ibid. | `MEASURED-RCT` |
| 28 | NSLM: effect on core GPA, **higher-achieving** students | B = 0.01 [−0.03, 0.06], n = 6,170, **p = .634, SMD 0.01** | ibid. | `MEASURED-RCT` (null) |
| 29 | Growth mindset, all studies | d̄ = 0.05 [0.02, 0.09], 63 studies, N = 97,672; PET-corrected d̄ = **0.01** [−0.03, 0.05], p = .667 | Macnamara & Burgoyne 2023, *Psych. Bull.* | `MEASURED-META` |
| 30 | …restricted to trials whose manipulation check passed | d̄ = **0.04** [−0.01, 0.10], 13 studies, N = 18,355 | ibid. | `MEASURED-META` |
| 31 | …restricted to the highest-quality designs | d̄ = 0.02 [−0.06, 0.10], 6 studies, N = 13,571 | ibid. | `MEASURED-META` |
| 32 | The counterpart estimate, overlapping study pool | targeted subgroups at high fidelity, achievement d = 0.14 [0.06, 0.22] | Burnette et al. 2023, *Psych. Bull.* | `MEASURED-META` |
| 33 | Big-fish-little-pond effect, pooled | β = **−0.28** [−0.32, −0.24], Z = −13.84, 33 studies / 56 effect sizes / N = 1,276,838, I² = 99.78% | Fang et al. 2018 | `MEASURED-META` |
| 34 | …across 26 countries | mean β = −.20 (SD .08), negative in **all 26**, N = 103,558 | Marsh & Hau 2003, *Am. Psychol.* | `OBSERVED` |
| 35 | Inclusive vs segregated placement, general learning difficulties | cognitive d = **0.35**; psychosocial d = **0.00**; 40 studies / 428 ES / N = 11,987 | Krämer et al. 2021, *RER* | `MEASURED-META` |
| 36 | Self-concept interventions for students with LD | benefit is confined to students with **documented low self-concept**; for them effect sizes are large | Elbaum & Vaughn 2003, *JLD* | `MEASURED-META` |
| 37 | Reading anxiety × reading achievement | r = **−.30**, 64 studies / 180 ES / 14,467 participants; **learning-disability status is not a moderator** | Johnson et al. 2026, *Psych. Bull.* | `MEASURED-META` |
| 38 | An adaptive dyscalculia trainer's responders | benefit concentrated in children with **low** maths anxiety and no comorbid literacy disorder; 67 children, randomised | Kohn et al. 2020 | `MEASURED-RCT` |
| 39 | EEF *Changing Mindsets*, 101 schools, 5,018 pupils | maths ES −0.01 [−0.04, 0.01]; reading −0.00; GPS −0.00; **and all four self-report subscales null too** | Foliano et al. 2019 | `MEASURED-RCT` (null) |
| 40 | Growth mindset at scale, 202 Argentine schools | no effect on intimidation, climate, performance, achievement or post-secondary plans; small effects ruled out | Ganimian 2020, *EEPA* | `MEASURED-RCT` (null) |

---

## 1. Maths anxiety: a real, small, and badly interpreted correlation

Ma's 1999 meta-analysis in the *Journal for Research in Mathematics Education* pooled 26
studies of elementary and secondary students and reported a population correlation of −.27
between anxiety toward mathematics and mathematics achievement. Ma found the relation stable
across gender, grade level, ethnicity, anxiety instrument and publication year, and varying
significantly by *achievement* instrument and by publication type. Hembree's 1990 review had
put the range at −.25 to −.40. `MEASURED-META`

That estimate has been superseded twice, and both replacements land in the same place.

Barroso, Ganley, McGraw, Geer, Hart & Daucourt (2021, *Psychological Bulletin* 147(2),
134–168) pooled 223 studies and 747 correlation coefficients published between 1992 and 2018.
The abstract, retrieved verbatim from the accepted manuscript this session: *"we found a
small-to-moderate, negative, and statistically significant correlation (r = −.28) between
math anxiety and math achievement."* The confidence interval is [−.29, −.26]; heterogeneity is
severe, Q = 7784.61, df = 747, I² = 90.42. `MEASURED-META`

Caviola, Toffalini, Giofrè, Ruiz, Szűcs & Mammarella (2022, *Educational Psychology Review*
34, 363–399) pooled 177 studies and 250 independent samples totalling 906,311 participants and
report r = −.30 [−.32, −.28] on 169 samples. `MEASURED-META` These two are **not independent
confirmations**: they overlap heavily in primary literature and differ mainly in inclusion
window and in Caviola's separate treatment of test anxiety. Reporting them as convergent
evidence would be manufactured independence. Reporting them as *stable across two independent
coding teams and two inclusion protocols* is fair, and that is what they are.

Namkung, Peng & Lin (2019, *Review of Educational Research*) pooled 131 studies and 478 effect
sizes among school-aged students and obtained r = −0.34, with three moderators that matter for
a tutoring system: anxiety scales capturing both cognitive and affective dimensions correlate
more strongly than affective-only scales; *advanced multistep* mathematical tasks correlate
more strongly than foundational ones; and maths measures that **affect the learner's grade**
correlate more strongly than measures administered purely for research. `MEASURED-META` The
last of those is a stakes effect hiding inside a correlation, and §3 returns to it.

### 1.1 What the correlation is not

Two moderators in Barroso destroy the naive reading.

The first: samples *selected for low maths ability* show r = −.09, 95% CI [−.17, −.004], k =
18, against r = −.28 [−.30, −.26] in the 729 effect sizes from unselected samples. In children
who are already struggling, anxiety and attainment come apart. `MEASURED-META`

The second comes from outside the meta-analysis and is sharper. Devine, Hill, Carey & Szűcs
(2018, *Journal of Educational Psychology*) screened 1,757 primary (8–9) and secondary (12–13)
school children for developmental dyscalculia and for maths anxiety. Children with dyscalculia
were twice as likely as typically-performing children to have high maths anxiety. But
**77% of the children with high maths anxiety had typical or high mathematics performance**,
and the authors conclude that *"cognitive and emotional mathematics problems largely
dissociate."* `OBSERVED`

`INFERENCE`: for a tutoring system, this is a routing rule and not a footnote. Distress is not
evidence of a knowledge gap, and competence is not evidence of comfort. A system that infers
"anxious, therefore behind" will over-remediate three quarters of the anxious children it
meets, and a system that infers "correct, therefore fine" will miss the child who is fluent
and terrified. The corpus already owns the machinery to separate these: `F5`'s learner model
holds knowledge state, `J1` selects technique. Neither carries an affect channel, and neither
should infer one from accuracy.

### 1.2 The gradient that matters for an eleven-year-old

Barroso's grade-level moderator: grades 3–5 r = −.20 [−.25, −.14], k = 89; grades 6–8 r = −.30
[−.35, −.26], k = 116; grades 9–12 r = −.34 [−.36, −.31], k = 99; undergraduates and graduates
−.24; non-student adults −.32. Caviola's cut is the same in shape, children r = −.31 against
adults −.25. `MEASURED-META`

An eleven-year-old sits at the start of the steepest section. The correlation is roughly a
third stronger by the end of middle school than at the beginning, which is consistent with
either causal story and decides nothing. It does say that the window in which the pairing is
weakest is the window a system is most likely to be given.

---

## 2. Direction: what actually causes what

This is the question the project needs answered, because it determines whether you treat the
feeling or the gap.

Carey, Hill, Devine & Szűcs (2016, *Frontiers in Psychology* 6:1987) framed it well and did
not resolve it, which is the correct outcome. They name two accounts: the **Deficit Theory**,
in which *"poor performance… leads to higher anxiety about that situation in the future"*, and
the **Debilitating Anxiety Model**, in which *"anxiety reduces performance by affecting the
pre-processing, processing, and retrieval of information."* Their summary of the evidence, as
retrieved from `PMC4703847`: *"the Deficit Theory is supported by longitudinal studies and
studies of children with mathematical learning disabilities, but the Debilitating Anxiety
Model is supported by research which manipulates anxiety levels and observes a change in
mathematics performance."* They propose a **Reciprocal Theory** in which *"poor performance may
trigger MA in certain individuals, [and] it may further reduce their maths performance in a
vicious cycle."* `MEASURED-META` (review)

The asymmetry in that sentence is the finding. The arm supported by *longitudinal* evidence is
performance → anxiety. The arm supported by *experimental* evidence is anxiety → performance.
Longitudinal designs have the causal ordering but not the manipulation; experiments have the
manipulation but induce a state, not a trait, and measure performance minutes later.

The numbers on the longitudinal arm are small. Ma & Xu (2004), quoted in Carey et al., found
correlations of **−0.11 to −0.2** between a student's achievement in one year and their maths
anxiety in the following year. Sorvo, Kiuru, Koponen, Aro, Viholainen, Ahonen & Aro (2022,
*Annals of the New York Academy of Sciences*) ran a cross-lagged model on 848 Finnish students
from grade 6 to grade 7 and found the other arm: *"High anxiety in sixth grade predicted low
performance in seventh grade,"* alongside a situational effect in a second substudy of 149
students, *"when anxiety was aroused, the participants performed more poorly compared to their
skill level."* Their conclusion is explicitly two-fold. `OBSERVED`

A Finnish preprint (Bula, Khanolainen, Koponen, Sorvo & Torppa 2025, PsyArXiv; **working
paper, discounted**) tracked 800 children across grades 2 and 3 and reports a bidirectional
relation between maths anxiety and arithmetic fluency but a *unidirectional* one from reading
fluency to reading anxiety. If that survives peer review, the domains differ, and the
worksheet problem may be a reading problem with an anxiety consequence rather than the
reverse.

### 2.1 What the answer is, and what follows from it

Reciprocal, with the two arms differently evidenced and neither large. `INFERENCE`

The design consequence is not "treat the anxiety" or "treat the gap." It is that a system
which can hold one constant while moving the other is the instrument the field is missing.
Every trial in this literature moves both at once: an intervention that reduces anxiety also
changes exposure to the material, and an intervention that raises skill also changes the
felt threat. A tutor with item-level control can run the dismantling design directly, and §9
specifies it.

### 2.2 The transmission channel nobody has costed

Two field studies identify where a child's maths anxiety comes from, and both implicate the
helper.

Beilock, Gunderson, Ramirez & Levine (2010, *PNAS* 107(5)) measured maths anxiety in first-
and second-grade female teachers and their students' achievement across a year. At the start
of the year there was no relation. By the end, *"the more anxious teachers were about math,
the more likely girls (but not boys) were to endorse the commonly held stereotype that 'boys
are good at math, and girls are good at reading' and the lower these girls' math
achievement."* `OBSERVED`

Maloney, Ramirez, Gunderson, Levine & Beilock (2015, *Psychological Science*) found the same
pattern in parents: children of more maths-anxious parents learned significantly less maths
across the year and ended with higher maths anxiety, **but only when those parents reported
helping frequently with maths homework**. Where help was infrequent, parental anxiety
predicted nothing. Parental maths anxiety did not predict children's *reading* achievement.
`OBSERVED`

`INFERENCE`: this is the one place where a machine has a structural advantage that is not a
hypothesis. The channel these two studies identify is the helper's own affect leaking into the
help. A language model does not have maths anxiety, does not sigh at fractions, and does not
transmit a stereotype it holds about who is good at this. That claim is bounded: it says
nothing about what a model transmits from its training data, which `F8` and `C1` handle, and
it does not predict a benefit. It identifies a documented harm that is absent by construction.

### 2.3 A correction to file against `H1`

`H1` §4.7 states: *"math anxiety correlates with performance at r = −0.168 across 57 studies /
150 effect sizes, with working memory as a mediating pathway (Finell, Sammallahti, Korhonen &
Eklöf 2022)."*

The source, retrieved this session, reports r = −0.168 [−0.203, −0.133] as the correlation
between **maths anxiety and working memory**, on 57 studies / 66 unique samples / 16,589
participants, I² = 75.6%. The mediated indirect effect through working memory to performance
is a separate and much thinner estimate: −0.092 [−0.169, −0.015], from **8 studies** and 1,824
participants, I² = 47%. The maths-anxiety-to-performance correlation is r ≈ −.28 to −.34 from
the sources in §1, not −0.168.

The direction of `H1`'s design conclusion is unaffected and its evidence is understated by
roughly half. The citation should be corrected in place and the −.28 figure substituted. `[X]`

---

## 3. The working-memory mechanism, and why it is an item-selection rule

Ashcraft and Kirk (2001, *Journal of Experimental Psychology: General* 130, 224–237) is the
study everyone cites and few state carefully. Ashcraft & Krause (2007, *Psychonomic Bulletin &
Review*), retrieved in full this session, restates it with the numbers:

> *"we used two different verbal-based span assessments, and found no significant anxiety-group
> differences at all. But when a computation-based span task was administered, we found a
> pronounced decline in assessed working memory capacity; the full-scale correlation was a
> significant .40… a math-anxious person's working memory resources are drained… only when the
> actual math anxiety is aroused."*

That is a conditional deficit, not a trait deficit. `OBSERVED`

The dual-task experiment sharpens it further. Participants did two-column addition alone or
with a concurrent letter-recall task, under a two-letter or six-letter load. Errors grew
modestly for every anxiety group in the control and two-letter conditions. *"But in the
difficult six-letter condition, with the working-memory-demanding carry problems, the effect
of the dual task was quite strong, and affected the high-anxious group the most."* The authors
note that if the dual task were simply inducing state anxiety, errors would have risen on
non-carry trials too, and they did not. `OBSERVED`

Finell, Sammallahti, Korhonen, Eklöf & Jonsson (2022) pooled the mechanism: maths anxiety ×
working memory r = −0.168 [−0.203, −0.133], with the mediated path to performance at −0.092
[−0.169, −0.015] from only eight studies. Funnel asymmetry was present. `MEASURED-META` The
mechanism is real and the pooled magnitude is modest; Caviola's independent pooling gives
maths anxiety × overall working memory r = −0.18 [−0.24, −0.13], dropping to −0.15 after
trim-and-fill.

### 3.1 The choking literature and who it damages

Beilock & Carr (2005, *Psychological Science* 16, 101–105) reported that *"only individuals
high in working memory capacity were harmed by performance pressure, and… these skill
decrements were limited to math problems with the highest demands on working memory
capacity."* The full text was unobtainable through three routes and the cell means are
**UNVERIFIED** here. `MEASURED-RCT` (abstract only)

Taken with the Ashcraft dual-task result, the two produce a single architectural claim that is
stronger than either: **the harm is concentrated where load is highest**, and the learner most
exposed to a pressure manipulation is the one who was relying on capacity in the first place.

### 3.2 The behaviour that shows up in telemetry

Ashcraft & Krause report one further result that a tutoring system can actually see:

> *"high-math-anxious participants often sacrifice accuracy for speed, especially as problems
> become more difficult, which we interpreted as an avoidance-like effort to finish the
> testing session as quickly as possible… Consequences of this — say, in terms of achievement
> testing or learning from homework — have yet to be investigated."*

`OBSERVED — absence`, stated by the authors themselves in 2007 and, on the searches run this
session, still unstated in 2026.

`INFERENCE`: response latency falling while accuracy falls, on items whose difficulty is
rising, is a signature that distinguishes avoidance from disengagement and from
gaming-the-system. `N2` documents the adjacent behaviour in Cognitive Tutor logs: after three
consecutive errors on a step, students requested a hint only 34% of the time, and clicked
through 68% of hint levels in under a second. Those logs measure help-avoidance; this measures
speed-avoidance. They are the same child.

### 3.3 What follows for item selection

`SPEC` — **load-aware pacing under an affect flag.** When the avoidance signature is present,
hold working-memory load flat while difficulty rises. Concretely: keep the carry, drop the
concurrent demand. Present one sub-goal at a time with intermediate results written down and
persistent on screen, so the item's *conceptual* difficulty is preserved and its *storage*
demand is externalised. This is the coherence and split-attention machinery `N2` and `C1`
already specify, aimed at a different variable.

The falsifier, and the outcome measure this proposal is required to name: **delayed unassisted
transfer**, at least seven days later, on isomorphic items presented without the scaffold. If
externalising storage produces a learner who cannot do the item once the scratchpad is
withdrawn, the design has bought a feeling and lost the skill, which is the failure mode §10
is about.

---

## 4. Test anxiety is a different construct, and the interventions are weaker than they look

Test anxiety and maths anxiety are correlated but separable, and the meta-analytic evidence
says the domain-specific one is the stronger predictor of domain performance. Caviola et al.
(2022) computed both on the same corpus: maths anxiety × maths performance r = −.30 [−.32,
−.28]; test anxiety × maths achievement r = −.23 [−.26, −.19]. Test anxiety × working memory
was r = −.18 [−.27, −.08]. `MEASURED-META`

Barroso's own decomposition of the anxiety construct is finer and worth having: worry k = 14,
r = −.37 [−.50, −.23]; emotionality k = 7, r = −.35; both together k = 11, r = −.24; maths
*evaluation* anxiety k = 55, r = −.21; maths *learning* anxiety k = 35, r = −.28. `MEASURED-META`
The evaluation/learning split matters for a tutor: the anxiety attached to being *assessed*
correlates less with achievement than the anxiety attached to *learning the material*, which
is the one a tutor spends its time inside.

von der Embse, Jester, Roy & Post (2018, *Journal of Affective Disorders*) synthesised 238
studies from 1988 onward and found test anxiety negatively related to standardised tests,
university entrance exams and GPA, *"most pronounced at the middle grades level"*, with
perceived test difficulty and the high-stakes nature of the test both predicting higher
anxiety, and effect magnitudes *"in the small to moderate range."* `MEASURED-META`

### 4.1 What reduces it, and what that reduction buys

Huntley, Young, Temple, Longworth, Smith, Jha & Fisher (2019, *Journal of Anxiety Disorders*
63, 36–50) pooled 44 randomised controlled trials of interventions for test-anxious university
students, n = 2,209. Interventions beat controls at post-treatment on test anxiety at
**g = −0.76** and on academic performance at **g = 0.37**, with behaviour therapy carrying the
most support. The authors' own qualification, verbatim: *"Evidence of publication bias was
found and poor quality of reporting meant that confidence in results should be moderated."*
`MEASURED-META`

Note the ratio. The self-report outcome moves twice as far as the performance outcome in the
same trials. That ratio recurs everywhere in this literature and it is the single most useful
regularity in this report.

Yılmazer, Hamamcı & Türk (2024, *Frontiers in Psychology*) pooled 18 studies and 20
comparisons of mindfulness-based interventions for test anxiety across 1,275 participants:
ES = −0.716, 95% CI [−1.383, −0.049], with Egger's test significant at p = .025. The
confidence interval nearly touches zero, and **the meta-analysis contains no achievement
outcome at all**. `MEASURED-META` The entire mindfulness-for-test-anxiety literature, as
pooled in 2024, has never been asked whether the students then did better.

For maths anxiety specifically, Sammallahti, Finell, Jonsson & Korhonen (2023, *Journal of
Numerical Cognition* 9(2), 346–362) pooled 50 studies and 75 effect sizes: g = −0.467 for
reducing maths anxiety and g = 0.502 for improving maths performance. Their category
breakdown is the interesting part. Emotion-regulation interventions g = −0.523 [−0.778,
−0.268] and cognitive-support interventions g = −0.525 [−0.732, −0.318] both reduced anxiety;
**motivation interventions did not**, g = −0.251 [−0.595, 0.094], and did not improve
performance either, g = 0.2. Egger's test was significant for both outcomes. And the sentence
that should be quoted whenever this meta-analysis is: *"higher EPHPP-ratings were associated
with non-significant intervention outcomes, whereas interventions with lower EPHPP-ratings
were related to significant outcomes."* `MEASURED-META`

`INFERENCE`: that quality gradient runs the same direction as Macnamara & Burgoyne's in §5 and
Shewach's in §6. Three separate literatures, three independent quality codings, and in all
three the better-designed studies find less. The corpus should treat this as a property of
affective-intervention research generally rather than a quirk of any one construct.

### 4.2 The `F6` boundary, drawn explicitly

`F6` owns motivation, and the maths-anxiety intervention meta-analysis says motivation
interventions do not reduce anxiety. These are separate levers with separate evidence, and the
corpus can now say so with a number attached: g = −0.251, CI containing zero, k reported in
Sammallahti's supplementary table.

---

## 5. Growth mindset: the strongest study, and the gap between it and the claims

The National Study of Learning Mindsets is the best evidence in this field and it is worth
stating at full resolution, because the summary versions in circulation lose the parts that
matter. All figures below are from the *Nature* paper retrieved in full from `PMC6786290`.

**Design.** A stratified random sample of 65 regular US public high schools; 12,490 ninth
graders individually randomised within school; two online sessions totalling *"less than one
hour"*, median 21 days apart; pre-registered analysis plan at `osf.io/tn6g4`; independent data
collection by ICF; blinded Bayesian corroboration. `MEASURED-RCT`

**Effect on the belief.** Among lower-achieving adolescents, fixed-mindset beliefs fell,
B = −0.38, 95% CI [−0.31, −0.46], SE 0.04, n = 5,650, k = 65, t = −10.14, p < 0.001,
**standardised mean difference 0.33**.

**Effect on grades, lower-achieving students.** Core-course GPA rose B = **0.10 grade points**,
95% CI [0.04, 0.16], SE 0.03, n = 6,320, k = 65, t = 3.51, p = 0.001, **SMD 0.11**. Maths and
science GPAs gave B = 0.10 as well.

**Effect on grades, higher-achieving students.** B = 0.01 grade points, 95% CI [−0.03, 0.06],
SE 0.02, n = 6,170, t = 0.480, **p = 0.634, SMD 0.01**. The intervention × lower-achiever
interaction was B = 0.09 [0.01, 0.17].

**Moderation.** The GPA effect was smaller in higher-achieving schools: interaction B = −0.07,
SE 0.03, z = −2.76, p = 0.006, standardised β = −0.25, with medium-achieving schools showing
larger effects than the top quartile. Peer norms supporting challenge-seeking, measured by a
behavioural "make-a-math-worksheet" task aggregated from the control group, moderated the
effect positively; self-reported mindset norms did not.

**Course-taking runs the other way.** Advanced-mathematics enrolment in tenth grade
(41 schools) moved with interaction B = 0.04 [0.00, 0.08], z = 2.26, p = 0.024, *"the opposite
of what we found for core course GPAs"*: +4 percentage points in the top quartile of schools
(t = 2.37, p = 0.018) against +2 points in the lower 75% (t = 2.00, p = 0.045).

So the honest one-line summary is: an under-one-hour online intervention moved a self-reported
belief by a third of a standard deviation, moved grades by a tenth of a standard deviation in
the half of students who were behind, moved grades not at all in the half who were not, and
moved course-taking mainly in the schools where it did not move grades.

### 5.1 The comparison against the field

Macnamara & Burgoyne (2023, *Psychological Bulletin*) reviewed 63 studies with N = 97,672 and
ran three meta-analyses. Verbatim from the abstract: *"we observed a small overall effect:
d̄ = 0.05, 95% CI = [0.02, 0.09], which was nonsignificant after correcting for potential
publication bias… When examining only studies demonstrating the intervention influenced
students' mindsets as intended (13 studies, N = 18,355), the effect was nonsignificant:
d̄ = 0.04, 95% CI = [−0.01, 0.10]. When examining the highest-quality evidence (6 studies,
N = 13,571), the effect was nonsignificant: d̄ = 0.02, 95% CI = [−0.06, 0.10]."* The
publication-bias correction by precision-effect test gave d̄ = 0.01, 95% CI [−0.03, 0.05],
p = .667. They also report that authors with a financial incentive to find positive effects
published significantly larger ones. `MEASURED-META`

Burnette, Billingsley, Banks, Knouse, Hoyt, Allison & Larkin (2023, *Psychological Bulletin*)
analysed a heavily overlapping study pool with multilevel meta-regression and reported that
when interventions were delivered to targeted subgroups with high fidelity, achievement
effects were d = 0.14, 95% CI [0.06, 0.22], and mental-health effects d = 0.32 [0.10, 0.54].
`MEASURED-META` These two meta-analyses are **not independent**; they descend from
substantially the same primary trials and disagree about how to model heterogeneity, not about
what the trials found.

The reconciliation that survives both: **the effect exists in a narrow subgroup, is roughly a
tenth of a standard deviation there, and is indistinguishable from zero everywhere else.**
Yeager's pre-registered subgroup estimate of SMD 0.11 and Burnette's targeted-subgroup estimate
of d = 0.14 are the same claim; Macnamara's d̄ = 0.02 in the six highest-quality trials is the
claim about the general case. The gap between "growth mindset raises achievement" and that
sentence is the finding about this field.

### 5.2 Two nulls at scale

Foliano, Rolfe, Buzzeo, Runge & Wilkinson (2019), the EEF *Changing Mindsets* effectiveness
trial: 101 English schools, 5,018 Year 6 pupils, teacher professional development plus an
eight-week pupil programme of up to 2.5 hours a week, at £4 per pupil. KS2 maths effect size
−0.01, 95% CI [−0.04, 0.01], p = 0.37, n = 4,454; reading −0.00 [−0.02, 0.02], p = 0.72; GPS
−0.00 [−0.03, 0.03], p = 0.90. Minimum detectable effect size at randomisation, 0.19.
`MEASURED-RCT` (null)

Ganimian (2020, *Educational Evaluation and Policy Analysis*): 202 public secondary schools in
Salta, Argentina, Grade 12. *"The intervention was implemented as intended. Yet, I find no
evidence that it affected students' propensity to find tasks less intimidating, school
climate, school performance, achievement, or post-secondary plans. I rule out small effects
and find little evidence of heterogeneity."* `MEASURED-RCT` (null)

---

## 6. Stereotype threat: what survives the replication record

This is the most contested item in the brief and it deserves the numbers rather than a verdict.

**The original.** Steele & Aronson (1995) reported four laboratory studies in which reminders
of racial stereotypes lowered the test scores of African American examinees and not of White
examinees. The most consequential feature of the design was not in most retellings of it:
scores were analysed **adjusted for prior SAT**. Sackett, Hardison & Cullen (2004, *American
Psychologist* 59(1), 7) showed that the paper demonstrates threat *creating* a gap on adjusted
scores and does **not** show that removing threat eliminates the raw Black–White mean
difference. A 2022 re-audit in *Personnel Assessment and Decisions* found the misinterpretation
rate in journal articles had fallen from 90.9% to 62.8%, and in textbooks from 55.6% to 41.2%.
`OBSERVED`

**The child and adolescent meta-analysis.** Flore & Wicherts (2015, *Journal of School
Psychology* 53(1), 25–44) pooled 47 effect sizes from (quasi-)experimental studies of girls
under 18 on maths, science and spatial tests. Random-effects estimate g = −0.22, z = −3.63,
p < .001, CI [−0.34, −0.10]. Heterogeneity τ̂² = 0.10, Q(46) = 117.19, I² = 61.75%, with a 95%
credibility interval of [−0.85, 0.41] — a range that includes substantial *reverse* effects.
None of the four pre-registered moderators reached significance.

Then the bias analyses, quoted verbatim from the retrieved PDF: trim-and-fill imputed 11
missing effect sizes and *"reduced the estimated effect size to g = −0.07, z = −1.10, p = .27,
CI95 = −0.21; 0.06."* Egger's test z = −3.25, p = .001; Begg and Mazumdar's rank correlation
Kendall's τ = −.27, p = .01. Splitting by sample size: small samples (N < 60) g = −0.34 [−0.52,
−0.16], k = 24; large samples (N ≥ 60) g = −0.13 [−0.29, 0.03], **p = .10**, k = 23. Ioannidis
and Trikalinos's excess-significance test χ²(1) = 8.50, p = .004. The authors' conclusion:
*"publication bias might seriously distort the literature on the effects of stereotype threat
among schoolgirls. We propose a large replication study."* `MEASURED-META`

**The replication they proposed, run by them.** Flore, Mulder & Wicherts (2018, *Comprehensive
Results in Social Psychology* 3(2), 140–174), a registered report with N = 2,064 Dutch high
school students, tested the overall effect and four theoretical moderators (domain
identification, gender identification, maths anxiety, test difficulty). They found *"neither an
overall effect of stereotype threat on math performance, nor any moderated stereotype threat
effects."* Most variance in maths performance was explained by gender, domain identification
and maths identification. `MEASURED-RCT` (null)

**The operational-settings meta-analysis.** Shewach, Sackett & Quint (2019, *Journal of Applied
Psychology* 104(12), 1514) is the largest and the most decision-relevant, because it asks what
size of effect can occur in the conditions a real test actually has. Overall sample:
d = −.31, k = 181, N = 10,436, SDδ = .38 (d = −.33 with covariate studies included, k = 212,
N = 11,521). Restricting to conditions plausible in operational testing gives a focal sample
d = −.14, k = 45, N = 3,532, and trim-and-fill on that focal sample gives **d = −.09**. The
four samples conducted in actual operational contexts give **d = −.01, k = 4, N = 1,670**,
against lab contexts d = −.36, k = 177, N = 8,766, a significant difference at
t(179) = −5.73, p < .01. Studies with motivational incentives d = −.14, k = 11, against
d = −.41 without, k = 137; the monetary-incentive subset gives **d = .00, k = 9, N = 526**.
Published studies d = −.37 (k = 132) against unpublished d = −.17 (k = 49), t(179) = −3.08,
p < .01. The 10% most precise studies give d = −.11; the least precise give d = −.38.
`MEASURED-META`

**The contested meta-analysis and its commentary.** Picho-Kiroga, Turnbull &
Rodriguez-Leahy (2021, *Journal of Advanced Academics*) reported a mean d = .28 in females and
argued that effects are inflated by designs omitting the theory's own necessary conditions.
Their own Table 2 shows the effect **falling** as more of Steele's three essential conditions
are present, until studies with all three are statistically indistinguishable from zero.
Warne (2022, same journal) re-analysed their data file: median sample size 40; mean a priori
power .189; 31 of 101 computable effect sizes significant against 19.0 expected under no bias,
χ² = 8.656, p = .003; correlation between sample size and effect size in their file
r = −.361, p < .001. His arithmetic on required samples: at d = .28, 202 participants per group
for 80% power and 270 for 90%; a typical 20-per-group study has power .1386. He concludes the
data are *"most consistent with a population effect size of zero."* `MEASURED-META` plus
commentary.

### 6.1 What this report concludes, and from which numbers

The laboratory phenomenon is real in the sense that it can be produced in a laboratory. The
effect that could occur in a setting resembling a real test is **d = −.09 to −.14** (Shewach's
focal sample, before and after trim-and-fill), and in the only four operational samples that
exist it is **d = −.01**. In children and adolescents the pooled estimate is g = −0.22 and
becomes g = −0.07, p = .27 once funnel asymmetry is corrected, with the large-sample subset at
p = .10. The one large pre-registered replication, N = 2,064, found nothing, including nothing
for any of the four moderators the theory names. `INFERENCE`

What this does **not** license is the reverse overcorrection. Shewach's overall d = −.31 is
not zero, the female subgroup d = −.33 is the largest cell in his table, and none of these
analyses touches whether stereotypes affect *enrolment, persistence and choice*, which is a
different dependent variable with a different literature. What the numbers rule out is the
proposition that a tutoring system needs a stereotype-threat countermeasure in order for a
learner's test score to be valid. That proposition has been tested at scale and does not hold.

`INFERENCE` for this project: build nothing for stereotype threat. The design moves it would
motivate (removing demographic questions before assessment, avoiding diagnostic framing) are
either already required by `F8`'s data-minimisation posture or already justified by the test
anxiety evidence in §4, which is stronger. There is no unique architectural obligation here.

---

## 7. Academic self-concept, the pond, and what happens when you drain it

Academic self-concept is the construct with the strongest and least contested evidence in this
report, and it is the one with the sharpest unexamined consequence for a personalised tutor.

**The reciprocal effects model.** Guay, Marsh & Boivin (2003, *Journal of Educational
Psychology*) tested the causal ordering and supported a reciprocal model in which achievement
affects self-concept and self-concept affects achievement. Seaton, Parker, Marsh, Craven &
Yeung (2014) juxtaposed self-concept against achievement-goal orientations across four waves
in 2,786 Australian students aged 11–17: *"when all were included in a single model, only
self-concept had significant reciprocal relationships with achievement."* `OBSERVED`

**The big-fish-little-pond effect.** Marsh & Hau (2003, *American Psychologist*) tested
103,558 fifteen-year-olds across 26 countries. School-average achievement had a negative effect
on individual academic self-concept in **all 26 countries**, mean β = −.20, SD = .08.
`OBSERVED` Fang, Huang, Zhang, Huang, Li & Yuan (2018, *Frontiers in Psychology* 9:1569) pooled
33 studies and 56 effect sizes over N = 1,276,838: β = −0.28, Z = −13.84, p < 0.001, CI [−0.32,
−0.24], I² = 99.78%. Age moderated it (high school −0.32, middle −0.28, college −0.23, primary
−0.21), as did region (Asia −0.35, Europe −0.30, North America −0.20) and domain (verbal −0.31,
STEM −0.30, general −0.22). Comparison target, class against school, did not. `MEASURED-META`

Marsh, Chessor, Craven & Roche (1995, *AERJ*) followed 53 Australian elementary students into
gifted-and-talented programmes and found systematic declines in three components of academic
self-concept and in none of four non-academic components. `OBSERVED` Parker, Dicke, Guo,
Basarkod & Marsh (2021, *Educational Researcher*) showed across four TIMSS cycles that
country-level **ability stratification** predicts the size of a country's BFLPE. `OBSERVED`

And a counterweight that the corpus should carry, because it bounds the effect: Preckel &
Brüll (2010) found that in German gifted-track classes a positive *assimilation* effect of
class type counterbalanced the negative *contrast* effect of class-average ability, with the
two of comparable size and no net BFLPE. `OBSERVED` Being in the pond and being labelled as
belonging to a prestigious pond are separate inputs with opposite signs.

### 7.1 The question nobody has costed

A personalised tutor removes the comparison class. There is no class average because there is
no class. On the BFLPE literature's own logic that should be protective: the contrast effect
has nothing to contrast against. On the assimilation literature's logic it should be neutral
or harmful, because the positive glow of belonging to a group has nothing to attach to either.
And the reciprocal-effects model says self-concept is not decorative, it feeds back into
achievement, so getting this wrong has a measurable cost.

`OBSERVED — absence`: searches this session across ERIC, Europe PMC, Crossref and arXiv found
**no study measuring academic self-concept in learners using a one-to-one AI tutor**, and no
study of what a frame of reference does when there is no reference group. Queries run:
`big-fish-little-pond` (ERIC, 101 records, none involving a tutoring system), `"academic
self-concept" AND (chatbot OR "AI tutor" OR "intelligent tutoring")` (Europe PMC), and the
arXiv API on `all:"math anxiety"` and `abs:"anxiety" AND abs:"tutor"`, which returned eight and
three records respectively, none an intervention trial.

This is a first-order gap for the product thesis. `INFERENCE`: the corpus's `F5` learner model
and `J1` selection policy both assume the learner's self-evaluation is either irrelevant or
downstream. The BFLPE literature says it is an *input*, formed by a comparison the system is
about to eliminate, and no one knows the sign of that elimination.

`SPEC` — **the reference-class decision, made explicitly.** A personalised system must choose
what a learner is implicitly compared to, because it will imply one whether or not it decides.
Three candidates: the learner's own past (a personal growth curve), a curricular standard
(grade-level expectation), or nothing. `H1` §4.7 already commits to the first. The BFLPE
evidence supports that commitment and adds a constraint the corpus has not stated: the
comparison must not be *reintroduced* through incidental surfaces such as cohort leaderboards,
percentile framings, or "students like you" language. The outcome measure that would test the
choice is not self-concept alone; it is **delayed unassisted performance at 6+ weeks, with
academic self-concept as a mediator**, because a design that raises self-concept and lowers
achievement has failed on the reciprocal model's own terms.

---

## 8. Students with disabilities: what is known, and how thin it is

The corpus's organising learner is served under a SELPA plan, so this section carries more
weight than its evidence base can comfortably support. That is itself the finding.

**Self-concept.** Bear, Minke & Manning (2002, *School Psychology Review*) meta-analysed 61
studies and found that children with learning disabilities perceive their academic ability
less favourably than peers, with **no difference as a function of special education setting**.
Elbaum (2002, *Learning Disabilities Research & Practice*) meta-analysed 40 studies on
placement and found no association between self-concept and placement in four of five
comparisons; the exception was that students in self-contained classrooms within regular
schools had lower self-concept than those in special schools, which is the BFLPE running
inside a building. `MEASURED-META` Nelson (2012) pooled 22 studies of adults with learning
disabilities: general self-concept d = −0.34, academic self-concept **d = −0.56**, social
−0.32, physical −0.13. The deficit is domain-specific and it is academic. `MEASURED-META`

**Placement.** Krämer, Möller & Zimmermann (2021, *Review of Educational Research*) pooled 40
studies, 428 effect sizes, N = 11,987 on inclusive against segregated settings for students
with general learning difficulties: cognitive outcomes d = 0.35, **psychosocial outcomes
d = 0.00**. Students without difficulties differed neither cognitively (d = −0.14) nor
psychosocially (d = 0.06). `MEASURED-META` Inclusion buys attainment and buys nothing
affective, in either direction, for either group.

**Interventions.** Elbaum & Vaughn (2001, *Elementary School Journal*) pooled 64 school-based
self-concept intervention studies for students with LD. Their 2003 follow-up in the *Journal of
Learning Disabilities* is the one with the design consequence: *"only students with documented
low self-concept benefited significantly from intervention. For these students effect sizes
were quite large."* `MEASURED-META` Treating the whole population produces a diluted average;
the effect lives in the subgroup that screens positive. This is the same shape as Yeager's
lower-achiever restriction and Burnette's targeted-subgroup restriction, arriving from a third
direction.

**Anxiety specifically.** Devine et al. (2018) gives the prevalence structure in §1.1. Namkung,
Peng & Goodrich (2025, *Learning Disability Quarterly*) re-analysed an RCT of 245 sixth graders,
65 with mathematics learning difficulties: for students without MLD, mathematics vocabulary and
computational fluency **fully mediated** the relation between maths anxiety and mathematics
competence; for students with MLD, only mathematics vocabulary had a direct effect. They
conclude that *"the nature of the relation between mathematics anxiety and mathematics
competence differs by MLD status, and students with MLD may require different types of
intervention."* `OBSERVED`

**Reading anxiety, which is what a worksheet actually taxes.** Johnson, Schaefer, Norris,
Wagner & Hart (2026, *Psychological Bulletin*) pre-registered a meta-analysis of 64 studies,
180 effect sizes and 14,467 participants across 14 countries and 11 languages: reading anxiety
× reading achievement r = **−.30**, Q = 996. *"Learning disability status, gender, reading
domain, and age were not significant moderators."* `MEASURED-META` The affective tax on reading
is the same size as the one on maths, and it does not spare children with an identified
disability, nor is it larger for them.

**Learned helplessness.** The evidence here is old and it is thin. Johnson (1981, *JEP*) found
that low self-concept was predicted by school failure, internal attributions for failure and
external attributions for success. Valås (2001) tracked 1,580 Norwegian students across three
grade bands and found achievement related both directly and indirectly to attributions,
expectations, helplessness and psychological adjustment. The attributional-retraining
intervention literature is almost entirely first-year university students (Perry and colleagues
across three decades), where the best-evidenced result is a reduction in course failure from
14.6% to 6.4% in an introductory psychology course, and where Hall, Jackson Gradt, Goetz &
Musu-Gillette (2011) found *"unanticipated negative treatment effects for students with higher
self-esteem."* `OBSERVED`

`OBSERVED — absence`: ERIC queries this session for learned helplessness or attributional style
**in students with an IEP** return work from the 1980s and no modern intervention trial. There
is no meta-analysis of attributional retraining in K–12 special education, and no trial of it
delivered by any digital system. A tutoring product that intends to address a failure history
is operating on a literature whose most recent controlled evidence concerns Canadian
undergraduates.

**And one measured warning specific to adaptive software.** Kohn, Rauscher, Kucian, Käser,
Wyschkon, Esser & von Aster (2020, *Frontiers in Psychology*) randomised 67 children with
developmental dyscalculia to the adaptive trainer Calcularis 2.0 or a waiting control, at a
minimum of 42 sessions. The programme worked, with gains stable at three months. The
responder analysis is the part this project needs: *"this self-directed training was especially
beneficial for children with low math anxiety scores and without an additional reading and/or
spelling disorder."* `MEASURED-RCT` Adaptivity did not neutralise anxiety. The anxious children
benefited least from the thing built to help them.

---

## 9. A documented null, given its own space

The brief asks for at least one anxiety or mindset intervention that moved self-report and did
not move achievement. There are three, at increasing levels of evidential force.

**One: mindfulness for test anxiety has never been asked the question.** Yılmazer, Hamamcı &
Türk (2024) pooled 18 studies and 1,275 participants and found ES = −0.716, 95% CI [−1.383,
−0.049] on test anxiety. Achievement appears nowhere in the meta-analysis, because it appears
nowhere in the primary studies at the level required for pooling. This is not a null result; it
is a literature that measured only the feeling. `MEASURED-META`

**Two: the National Study of Learning Mindsets, within one pre-registered trial.** The
intervention reduced fixed-mindset beliefs at SMD 0.33 (n = 5,650, t = −10.14, p < 0.001) and
produced a core-GPA effect in higher-achieving students of SMD 0.01, B = 0.01 grade points, 95%
CI [−0.03, 0.06], n = 6,170, **p = 0.634**. Same trial, same intervention, same schools, same
randomisation. The belief moved by thirty-three hundredths of a standard deviation and the
grade moved by one hundredth. `MEASURED-RCT` (null in the higher-achieving stratum)

**Three, and this is the strongest form of the finding: Macnamara & Burgoyne's manipulation-check
meta-analysis.** They isolated the 13 studies, N = 18,355, that *demonstrated the intervention
influenced students' mindsets as intended* — that is, the subset in which the self-report
outcome verifiably moved. In precisely that subset, the achievement effect was **d̄ = 0.04, 95%
CI [−0.01, 0.10]**, non-significant. `MEASURED-META`

That is the required null stated as cleanly as this literature permits: **conditioning on the
intervention having successfully changed what learners report about themselves does not produce
a detectable change in what they achieve.** It is worth noting that this cuts against the
theory's own mediation claim, since the studies that best establish the mediator are the ones
that fail to show the outcome.

Two supporting full nulls, where neither the feeling nor the achievement moved: Myers, Davis &
Chan (2021, *Cognitive Research: Principles and Implications*) tested expressive writing and an
instructional intervention across four authentic psychology exams and report *"Neither
intervention was effective at reducing test anxiety or improving exam performance."*
`MEASURED-RCT` (null) Thormodsæter and colleagues (2026, *CBE—Life Sciences Education*)
attempted a multi-institution replication of a cognitive-reappraisal intervention across 12
courses at 7 institutions: *"the intervention failed to impact self-reported test anxiety or
student performance."* `MEASURED-RCT` (null) The second of these is a direct replication attempt
of the intervention family that Ramirez & Beilock (2011, *Science*) made famous.

---

## 10. What a patient, private, unlimited system can actually do

The constructive half. Everything in this section is `SPEC` and each item names its
unassisted, delayed outcome measure, because §9 is what happens when they do not.

### 10.1 The evidence for the privacy premise, and against it

The premise is that a learner can be wrong in front of a machine at no social cost. It has
evidence on both sides and the project should hold both.

**For.** Lucas, Gratch, King & Morency (2014, *Computers in Human Behavior*) manipulated
whether participants believed a virtual interviewer was human-operated or automated:
*"participants who believed they were interacting with a computer reported lower resistance to
self-disclosure, lower impression management and higher system usability."* The belief did the
work; whether the agent was actually automated affected only usability ratings. `MEASURED-RCT`

Qu & Chen (2026, *Frontiers in Psychology*) ran a ten-week quasi-experiment with 59 Chinese
EFL undergraduates, GenAI interlocutor against peer partner. The AI group showed greater
reduction in speaking anxiety and better intercultural speaking performance, with learners
describing the environment as psychologically safe. Intact classes, not randomised, self-report
heavy. `OBSERVED`

**Against.** Alsaad and colleagues (2026, *Healthcare*) ran a scenario-based between-subjects
experiment with n = 373 comparing face-to-face, human-through-computer and chatbot
consultations. *"Results revealed no evidence of increased disinhibition in the chatbot
condition. Conversely, participants were significantly less willing to disclose sensitive
health information to chatbots than to humans."* `MEASURED-RCT` The privacy premise is
domain-dependent, and where trust concerns dominate it inverts.

Qi & Zhao (2026, *PLoS One*) analysed 30,000 matched dialogue turns from human-AI and
human-human help-seeking. Learners dropped the hedges and politeness markers that are mandatory
in human communities, but *"contrary to the expectation that users would 'confess' ignorance to
AI, we found that learners adopt an authoritative 'Director' stance rather than a humble
'Petitioner' role."* `OBSERVED`

`INFERENCE`: removing the audience removes impression management, and it does not
automatically produce disclosure of confusion. The child who will not put their hand up may
also not type "I don't understand." The design problem is not building a safe space; it is
building an *elicitation* that does not require the learner to volunteer the admission.
`survey/05` §8 states the adjacent hypothesis for the teaching case: the gain comes from being
interrogated, the loss from being evaluated, and a machine audience is the first thing that can
separate them. This section supplies the first evidence on both halves and the evidence is
mixed.

### 10.2 Four designs

`SPEC` — **1. The error that leaves no record.** Make wrongness cheap by construction: no
score is written until the learner asks for one; every attempt is revisable; the visible
artifact is the eventual correct solution and the learner's own path to it. This is the
low-stakes commitment `H1` §4.7 already makes, given a mechanism. It is supported by von der
Embse's finding that perceived stakes predict test anxiety and by Barroso's finding that
maths measures which affect the learner's grade correlate more strongly with anxiety
(k = 113, r = −.27) than research-only measures.
*Outcome measure:* delayed unassisted post-test at 14 days on items never seen, scored blind,
with the trap being that a system where nothing counts may produce a learner who never
retrieves under any pressure. `F11`'s retrieval-practice evidence requires frequency, not
stakes; this design must be checked against the possibility that it removes both.

`SPEC` — **2. Load-flat difficulty escalation.** From §3.3. When the avoidance signature
appears (latency falling as accuracy falls on rising difficulty), hold storage demand constant
and let conceptual demand rise, by externalising intermediate state.
*Outcome measure:* delayed unassisted transfer at 7+ days on isomorphic items **without** the
externalisation, compared against a matched arm that received the same items with the same
pacing and no externalisation.

`SPEC` — **3. Screen, then treat.** Elbaum & Vaughn's finding that only students with
documented low self-concept benefit, Yeager's lower-achiever restriction, and Burnette's
targeted-subgroup restriction all say the same thing: affective interventions delivered
universally produce diluted averages. Administer a short validated instrument (the modified
Abbreviated Math Anxiety Scale for children, which Devine and colleagues used) once, and gate
the affective machinery on it.
*Outcome measure:* the pre-registered interaction between screening status and treatment on
delayed unassisted performance, not the main effect. A design justified by a subgroup must be
evaluated on that subgroup's interaction term.

`SPEC` — **4. Do not import the pond.** From §7.1. No cohort percentiles, no "students like
you", no leaderboard, no comparison to a class average that the system could compute and the
learner never asked for. The learner's own past performance is the only reference class the
BFLPE evidence supports.
*Outcome measure:* academic self-concept as a **mediator** in a model whose outcome is delayed
unassisted performance at 6+ weeks. A self-concept gain that does not carry through to the
performance outcome is the §9 failure mode wearing a different label.

### 10.3 The trap, stated plainly

The most reproducible regularity in this report is that the self-report outcome moves roughly
twice as far as the achievement outcome in the same trials: Huntley's g = −0.76 against
g = 0.37; Sammallahti's g = −0.467 against g = 0.502 with a quality gradient running the wrong
way; Yeager's SMD 0.33 against SMD 0.11 and SMD 0.01; Macnamara's manipulation-check subset at
d̄ = 0.04. An affective feature that makes an eleven-year-old feel better about maths and
teaches no maths is a product that will test well, review well, retain well, and fail the child
it was built for. The corpus already knows this shape from Deslauriers and from Bastani's
guardrailed arm. This literature is where it is easiest to commit.

Any affective feature that ships without a delayed unassisted outcome measure attached is,
on the evidence assembled here, more likely than not to be measuring the wrong thing.

---

## 11. Buildable, testable, unknown

### 11.1 What is now buildable that was not before

Four things.

**A routing rule that separates distress from deficit.** Devine's 77% and Barroso's r = −.09 in
low-ability samples jointly say that affect and knowledge state must be modelled as separate
channels, and that neither may be inferred from the other. `F5` can carry an affect flag with
a stated provenance (screening instrument, or behavioural signature) and `J1` can branch on it,
and neither may derive it from accuracy.

**A behavioural detector with a published signature.** Falling latency plus falling accuracy on
rising difficulty is the avoidance pattern Ashcraft and colleagues described in 1996 and 2007
and explicitly noted had never been studied in achievement testing or homework. It is directly
computable from interaction logs and the corpus already logs the necessary fields for `N2`'s
help-seeking analysis.

**A defensible reference-class policy.** The BFLPE is β = −0.28 pooled over 1.28 million
students and negative in all 26 countries tested. A personalised system that suppresses cohort
comparison is acting on the best-evidenced construct in this report. That is now a citable
design commitment rather than a preference.

**A stop-list.** Do not build a stereotype-threat countermeasure; the operational estimate is
d = −.01 across four samples and d = −.09 after bias correction on the focal sample. Do not
build a general growth-mindset module; the manipulation-check subset is d̄ = 0.04, CI
[−0.01, 0.10]. Do not build a motivation-flavoured anxiety reducer; g = −0.251, CI containing
zero. Each of these saves engineering and each is a claim the corpus can defend with numbers.

### 11.2 The single highest-value experiment

**A three-arm dismantling trial that resolves the direction question, run inside a tutor.**

No study in this literature can hold anxiety constant while moving skill, or the reverse,
because every classroom intervention moves both. A system with item-level control can. Three
arms, stratified on a baseline maths-anxiety screen:

- **A — skill only.** Adaptive remediation of the prerequisite gap, with all affective
  features disabled: no reframing, no reassurance, no low-stakes framing beyond the platform
  default.
- **B — affect only.** The §10.2 features at full strength, with item selection held to the
  learner's existing level so that no new skill is taught.
- **C — both.**

Primary outcome: **delayed unassisted performance on transfer items at 6 weeks**, administered
without the tutor, blind-scored. Secondary: maths anxiety on the same instrument at 6 weeks,
and the avoidance signature rate from logs.

Deficit Theory predicts A ≈ C > B on both outcomes. The Debilitating Anxiety Model predicts
B > A on the anxiety outcome and B ≈ A on performance in the short run, with B's advantage
appearing only at follow-up. The Reciprocal Theory predicts C > A ≈ B on performance with a
super-additive gap. These are distinguishable, which is the point.

**Power.** Take the smallest difference worth detecting between two arms as d = 0.25, which sits
between Yeager's pre-registered SMD of 0.11 and Sammallahti's bias-inflated g = 0.50, and above
Macnamara's high-quality d̄ = 0.02. For three pairwise contrasts at Bonferroni-corrected
α = .0167 two-sided and 80% power, n = 2(2.394 + 0.842)² / 0.25² = **335 per arm, 1,005 total**.
Covariate adjustment for a baseline unassisted pre-test correlating r = 0.6 with the outcome
reduces residual variance by (1 − r²) = 0.64, giving **215 per arm, 645 total**. Enriching the
sample to the top tercile of the anxiety screen raises the expected effect, since Elbaum &
Vaughn, Yeager and Burnette all locate the effect in the screened subgroup, and would bring the
required sample below 500 while narrowing the population the answer applies to. At 645
learners across two school terms this is within reach of a single district partnership, and it
would be the first experiment in the field capable of separating the two causal arms.

**The pre-registration must state the null it is willing to report:** that arm B moves the
anxiety instrument and does not move the 6-week unassisted outcome, which is the result §9
predicts and which would be worth more to this project than a positive finding.

### 11.3 What I could not find out

- **The cell means of Beilock & Carr (2005).** Three retrieval routes returned 403 or empty.
  The choking finding is reported here from its abstract and is marked UNVERIFIED. The
  moderator claim (high working-memory learners are the ones harmed) is load-bearing for §3.1
  and rests on an abstract plus an adjacent description in Ashcraft & Krause.
- **Whether any AI tutor has ever been measured on an anxiety outcome.** Europe PMC on
  `("AI tutor" OR chatbot OR "large language model" OR "intelligent tutoring") AND "math
  anxiety"` returned 10 records, none an intervention trial with anxiety as a pre-registered
  outcome; the arXiv API on `all:"math anxiety"` returned 8 records, all network-psychometric
  or dataset papers; `abs:"anxiety" AND abs:"tutor"` returned 3. `OBSERVED — absence`. The
  closest is Qu & Chen (2026), a 59-participant quasi-experiment in second-language speaking.
- **What removing the comparison class does to academic self-concept.** §7.1. No study exists,
  and this bears directly on whether the product's core mechanism is protective or corrosive.
- **The confidence interval on Huntley's g = 0.37 for academic performance.** The published
  abstract gives point estimates only and the full text is behind Elsevier. The reported
  outlier-removed values circulating in secondary sources (g = −0.64 and g = 0.28) could not be
  traced to the paper this session and are **not** cited above.
- **Modern evidence on learned helplessness in students with an IEP.** The controlled evidence
  is from the 1980s and from undergraduate populations. If a tutoring system is to address a
  failure history, it is doing so without a current evidence base, and the trial in §11.2
  would be the first to generate one for this population.
- **Whether the anxious child benefits less from adaptive systems in general.** Kohn et al.
  (2020) found exactly that pattern in 67 children with dyscalculia. One trial, one programme,
  one disorder. Whether it generalises is unknown and it is the finding most likely to
  invalidate this project's premise if it does.

---

## References

Ordered by first appearance. `†` marks a source whose full text was retrieved and quoted
verbatim this session; others are cited from abstract, indexed record, or a retrieved
secondary description that is named at point of use.

1. Ma, X. (1999). A meta-analysis of the relationship between anxiety toward mathematics and achievement in mathematics. *Journal for Research in Mathematics Education*, 30(5), 520–540. ERIC EJ595981. `MEASURED-META`
2. Hembree, R. (1990). The nature, effects, and relief of mathematics anxiety. *JRME*, 21(1), 33–46. Cited via Barroso et al. and Caviola et al. `MEASURED-META`
3. † Barroso, C., Ganley, C. M., McGraw, A. L., Geer, E. A., Hart, S. A., & Daucourt, M. C. (2021). A meta-analysis of the relation between math anxiety and math achievement. *Psychological Bulletin*, 147(2), 134–168. `10.1037/bul0000307`. `MEASURED-META`
4. † Caviola, S., Toffalini, E., Giofrè, D., Ruiz, J. M., Szűcs, D., & Mammarella, I. C. (2022). Math performance and academic anxiety forms, from sociodemographic to cognitive aspects: a meta-analysis on 906,311 participants. *Educational Psychology Review*, 34, 363–399. `10.1007/s10648-021-09618-5`. `MEASURED-META`
5. Namkung, J. M., Peng, P., & Lin, X. (2019). The relation between mathematics anxiety and mathematics performance among school-aged students: a meta-analysis. *Review of Educational Research*, 89(3). ERIC. `MEASURED-META`
6. Devine, A., Hill, F., Carey, E., & Szűcs, D. (2018). Cognitive and emotional math problems largely dissociate: prevalence of developmental dyscalculia and mathematics anxiety. *Journal of Educational Psychology*, 110(3). `10.1037/edu0000222`. `OBSERVED`
7. † Carey, E., Hill, F., Devine, A., & Szűcs, D. (2016). The chicken or the egg? The direction of the relationship between mathematics anxiety and mathematics performance. *Frontiers in Psychology*, 6, 1987. `10.3389/fpsyg.2015.01987`, PMC4703847. `MEASURED-META` (review)
8. Ma, X., & Xu, J. (2004). The causal ordering of mathematics anxiety and mathematics achievement. *Journal of Adolescence*, 27(2). Quoted via Carey et al. (2016). `OBSERVED`
9. Sorvo, R., Kiuru, N., Koponen, T., Aro, T., Viholainen, H., Ahonen, T., & Aro, M. (2022). Longitudinal and situational associations between math anxiety and performance among early adolescents. *Annals of the NY Academy of Sciences*, 1512(1). `10.1111/nyas.14788`. `OBSERVED`
10. Bula, M. M., Khanolainen, D., Koponen, T., Sorvo, R., & Torppa, M. (2025). The interplay between math and reading anxiety and academic skills in primary school. PsyArXiv `10.31234/osf.io/jwh6m_v1`. **Preprint, discounted.** `OBSERVED`
11. Beilock, S. L., Gunderson, E. A., Ramirez, G., & Levine, S. C. (2010). Female teachers' math anxiety affects girls' math achievement. *PNAS*, 107(5), 1860–1863. `10.1073/pnas.0910967107`, PMC2836676. `OBSERVED`
12. Maloney, E. A., Ramirez, G., Gunderson, E. A., Levine, S. C., & Beilock, S. L. (2015). Intergenerational effects of parents' math anxiety on children's math achievement and anxiety. *Psychological Science*, 26(9). `10.1177/0956797615592630`. `OBSERVED`
13. Ashcraft, M. H., & Kirk, E. P. (2001). The relationships among working memory, math anxiety, and performance. *JEP: General*, 130(2), 224–237. PMID 11409101. `OBSERVED`
14. † Ashcraft, M. H., & Krause, J. A. (2007). Working memory, math performance, and math anxiety. *Psychonomic Bulletin & Review*, 14(2), 243–248. `10.3758/BF03194059`. Source of the verbatim quotations in §3. `OBSERVED`
15. † Finell, J., Sammallahti, E., Korhonen, J., Eklöf, H., & Jonsson, B. (2022). Working memory and its mediating role on the relationship of math anxiety and math performance: a meta-analysis. *Frontiers in Psychology*, 12, 798090. `10.3389/fpsyg.2021.798090`. `MEASURED-META`
16. Beilock, S. L., & Carr, T. H. (2005). When high-powered people fail: working memory and "choking under pressure" in math. *Psychological Science*, 16(2), 101–105. PMID 15686575. **Full text unobtainable; cell means UNVERIFIED.** `MEASURED-RCT`
17. Faust, M. W., Ashcraft, M. H., & Fleck, D. E. (1996). Mathematics anxiety effects in simple and complex addition. *Mathematical Cognition*, 2(1). Cited via Ashcraft & Krause (2007). `OBSERVED`
18. von der Embse, N., Jester, D., Roy, D., & Post, J. (2018). Test anxiety effects, predictors, and correlates: a 30-year meta-analytic review. *Journal of Affective Disorders*, 227, 483–493. `10.1016/j.jad.2017.11.048`. `MEASURED-META`
19. Huntley, C. D., Young, B., Temple, J., Longworth, M., Smith, C. T., Jha, V., & Fisher, P. L. (2019). The efficacy of interventions for test-anxious university students: a meta-analysis of randomized controlled trials. *Journal of Anxiety Disorders*, 63, 36–50. `10.1016/j.janxdis.2019.01.007`. `MEASURED-META`
20. Yılmazer, E., Hamamcı, Z., & Türk, F. (2024). Effects of mindfulness on test anxiety: a meta-analysis. *Frontiers in Psychology*, 15, 1401467. `10.3389/fpsyg.2024.1401467`, PMC11238660. `MEASURED-META`
21. † Sammallahti, E., Finell, J., Jonsson, B., & Korhonen, J. (2023). A meta-analysis of math anxiety interventions. *Journal of Numerical Cognition*, 9(2), 346–362. `10.5964/jnc.8401`, ERIC EJ1400784. `MEASURED-META`
22. Steele, C. M., & Aronson, J. (1995). Stereotype threat and the intellectual test performance of African Americans. *JPSP*, 69(5), 797–811. Design described via Sackett et al. (2004) and Warne (2022). `MEASURED-RCT`
23. Sackett, P. R., Hardison, C. M., & Cullen, M. J. (2004). On interpreting stereotype threat as accounting for African American–White differences on cognitive tests. *American Psychologist*, 59(1), 7–13. `10.1037/0003-066x.59.1.7`. `OBSERVED`
24. Sackett and colleagues (2022). On the continued misinterpretation of stereotype threat as accounting for Black–White differences on cognitive tests. *Personnel Assessment and Decisions*. `10.25035/pad.2022.01.001`. `OBSERVED`
25. † Flore, P. C., & Wicherts, J. M. (2015). Does stereotype threat influence performance of girls in stereotyped domains? A meta-analysis. *Journal of School Psychology*, 53(1), 25–44. `10.1016/j.jsp.2014.10.002`. `MEASURED-META`
26. Flore, P. C., Mulder, J., & Wicherts, J. M. (2018). The influence of gender stereotype threat on mathematics test scores of Dutch high school students: a registered report. *Comprehensive Results in Social Psychology*, 3(2), 140–174. `10.1080/23743603.2018.1559647`. Abstract retrieved from the Tilburg research portal. `MEASURED-RCT` (null)
27. † Shewach, O. R., Sackett, P. R., & Quint, S. (2019). Stereotype threat effects in settings with features likely versus unlikely in operational test settings: a meta-analysis. *Journal of Applied Psychology*, 104(12), 1514–1534. `10.1037/apl0000420`. `MEASURED-META`
28. Picho-Kiroga, K., Turnbull, A., & Rodriguez-Leahy, A. (2021). Stereotype threat and its problems: theory misspecification in research, consequences, and remedies. *Journal of Advanced Academics*, 32(3), 231–264. `10.1177/1932202X20986161`. `MEASURED-META`
29. † Warne, R. T. (2022). No strong evidence of stereotype threat in females: a reassessment of the Picho-Kiroga et al. (2021) meta-analysis. *Journal of Advanced Academics*. `10.1177/1932202X211061517`, ERIC EJ1341866. Commentary. `MEASURED-META`
30. † Yeager, D. S., Hanselman, P., Walton, G. M., Murray, J. S., Crosnoe, R., Muller, C., Tipton, E., et al. (2019). A national experiment reveals where a growth mindset improves achievement. *Nature*, 573, 364–369. `10.1038/s41586-019-1466-y`, PMC6786290. Full text retrieved via Europe PMC. `MEASURED-RCT`
31. † Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. `10.1037/bul0000352`. `MEASURED-META`
32. Burnette, J. L., Billingsley, J., Banks, G. C., Knouse, L. E., Hoyt, C. L., Allison, J. M., & Larkin, S. (2023). A systematic review and meta-analysis of growth mindset interventions: for whom, how, and why might such interventions work? *Psychological Bulletin*, 149(3–4), 174–205. PMID 36227318. **Overlapping study pool with (31).** `MEASURED-META`
33. † Foliano, F., Rolfe, H., Buzzeo, J., Runge, J., & Wilkinson, D. (2019). *Changing Mindsets: effectiveness trial — evaluation report*. Education Endowment Foundation / NIESR. UCL Discovery 10118795. `MEASURED-RCT` (null)
34. Ganimian, A. J. (2020). Growth-mindset interventions at scale: experimental evidence from Argentina. *Educational Evaluation and Policy Analysis*, 42(3). `10.3102/0162373720938041`. `MEASURED-RCT` (null)
35. Guay, F., Marsh, H. W., & Boivin, M. (2003). Academic self-concept and academic achievement: developmental perspectives on their causal ordering. *Journal of Educational Psychology*, 95(1). ERIC. `OBSERVED`
36. Seaton, M., Parker, P., Marsh, H. W., Craven, R. G., & Yeung, A. S. (2014). The reciprocal relations between self-concept, motivation and achievement. *Educational Psychology*, 34(1). ERIC. `OBSERVED`
37. Marsh, H. W., & Hau, K.-T. (2003). Big-fish-little-pond effect on academic self-concept: a cross-cultural (26-country) test. *American Psychologist*, 58(5), 364–376. PMID 12971085. `OBSERVED`
38. Fang, J., Huang, X., Zhang, M., Huang, F., Li, Z., & Yuan, Q. (2018). The big-fish-little-pond effect on academic self-concept: a meta-analysis. *Frontiers in Psychology*, 9, 1569. `10.3389/fpsyg.2018.01569`. `MEASURED-META`
39. Marsh, H. W., Chessor, D., Craven, R., & Roche, L. (1995). The effects of gifted and talented programs on academic self-concept: the big fish strikes again. *AERJ*, 32(2). ERIC. `OBSERVED`
40. Parker, P., Dicke, T., Guo, J., Basarkod, G., & Marsh, H. (2021). Ability stratification predicts the size of the big-fish-little-pond effect. *Educational Researcher*, 50(6). ERIC. `OBSERVED`
41. Preckel, F., & Brüll, M. (2010). The benefit of being a big fish in a big pond: contrast and assimilation effects on academic self-concept. *Learning and Individual Differences*, 20(5). ERIC. `OBSERVED`
42. Bear, G. G., Minke, K. M., & Manning, M. A. (2002). Self-concept of students with learning disabilities: a meta-analysis. *School Psychology Review*, 31(3). ERIC. `MEASURED-META`
43. Elbaum, B. (2002). The self-concept of students with learning disabilities: a meta-analysis of comparisons across different placements. *Learning Disabilities: Research & Practice*, 17(4). ERIC. `MEASURED-META`
44. Elbaum, B., & Vaughn, S. (2001). School-based interventions to enhance the self-concept of students with learning disabilities: a meta-analysis. *Elementary School Journal*, 101(3). ERIC. `MEASURED-META`
45. Elbaum, B., & Vaughn, S. (2003). For which students with learning disabilities are self-concept interventions effective? *Journal of Learning Disabilities*, 36(2). ERIC. `MEASURED-META`
46. Nelson, J. M. (2012). General and domain-specific self-concepts of adults with learning disabilities: a meta-analysis. *Learning Disabilities: A Multidisciplinary Journal*, 18(1). ERIC. `MEASURED-META`
47. Krämer, S., Möller, J., & Zimmermann, F. (2021). Inclusive education of students with general learning difficulties: a meta-analysis. *Review of Educational Research*, 91(3). ERIC. `MEASURED-META`
48. Namkung, J. M., Peng, P., & Goodrich, M. J. (2025). The relation between mathematics anxiety and mathematics competence for students with versus without mathematics learning difficulties. *Learning Disability Quarterly*. ERIC. `OBSERVED`
49. Johnson, R. M., Schaefer, M., Norris, C. U., Wagner, R. K., & Hart, S. A. (2026). The association between reading anxiety and reading achievement: a meta-analysis and systematic review. *Psychological Bulletin*. `10.1037/bul0000517`, PMC13225606. Pre-registered. `MEASURED-META`
50. Johnson, D. S. (1981). Naturally acquired learned helplessness. *Journal of Educational Psychology*, 73(2). ERIC. `OBSERVED`
51. Valås, H. (2001). Learned helplessness and psychological adjustment. *Scandinavian Journal of Educational Research*, 45(1). ERIC. `OBSERVED`
52. Haynes Stewart, T. L., Clifton, R. A., Daniels, L. M., Perry, R. P., Chipperfield, J. G., & Ruthig, J. C. (2011). Attributional retraining: reducing the likelihood of failure. *Social Psychology of Education*, 14(1). ERIC. `MEASURED-RCT`
53. Hall, N. C., Jackson Gradt, S. E., Goetz, T., & Musu-Gillette, L. E. (2011). Attributional retraining, self-esteem, and the job interview. *Journal of Experimental Education*, 79(3). ERIC. `MEASURED-RCT`
54. Kohn, J., Rauscher, L., Kucian, K., Käser, T., Wyschkon, A., Esser, G., & von Aster, M. (2020). Efficacy of a computer-based learning program in children with developmental dyscalculia: what influences individual responsiveness? *Frontiers in Psychology*, 11, 1115. `10.3389/fpsyg.2020.01115`, PMC7373797. `MEASURED-RCT`
55. Myers, S. J., Davis, S. D., & Chan, J. C. K. (2021). Does expressive writing or an instructional intervention reduce the impacts of test anxiety in a college classroom? *Cognitive Research: Principles and Implications*, 6, 44. `10.1186/s41235-021-00309-x`, PMC8192598. `MEASURED-RCT` (null)
56. Thormodsæter, R. S., Ballen, C. J., Fagbodun, S., et al. (2026). Can we mitigate the impacts of test anxiety through reappraisal interventions? A replication study in science courses across multiple institution types. *CBE—Life Sciences Education*. `10.1187/cbe.25-04-0055`, PMC12936497. `MEASURED-RCT` (null)
57. Ramirez, G., & Beilock, S. L. (2011). Writing about testing worries boosts exam performance in the classroom. *Science*, 331(6014), 211–213. `10.1126/science.1199427`. Named as the intervention family (55) and (56) failed to reproduce. `MEASURED-RCT`
58. Lucas, G. M., Gratch, J., King, A., & Morency, L.-P. (2014). It's only a computer: virtual humans increase willingness to disclose. *Computers in Human Behavior*, 37, 94–100. `10.1016/j.chb.2014.04.043`. `MEASURED-RCT`
59. Qu, Z., & Chen, L. (2026). Simulating the "cultural other": the impact of GenAI interlocutors on EFL learners' intercultural communicative competence, speaking anxiety, and learning engagement. *Frontiers in Psychology*. `10.3389/fpsyg.2026.1799695`, PMC13071047. Quasi-experimental, N = 59. `OBSERVED`
60. Alsaad, A., Alanezi, S., Melhim, L. K. B., Alsyouf, A., & Alsaad, A. (2026). Can medical chatbots trigger disinhibition and encourage health information disclosure? *Healthcare*, 14(9), 1218. `10.3390/healthcare14091218`, PMC13163985. `MEASURED-RCT`
61. Qi, L., & Zhao, L. (2026). Social friction vs. cognitive efficiency: a comparative analysis of help-seeking behaviors in human communities and generative AI. *PLoS One*. `10.1371/journal.pone.0348441`, PMC13127939. `OBSERVED`

**Carried from the corpus, not re-derived:** `H1` §4.7 (the anxiety design consequence, with
the citation correction filed in §2.3); `N2` (Aleven & Koedinger help-seeking logs, the
coherence and split-attention machinery); `F6` (self-determination and gamification, whose
boundary against this report is drawn in §4.2); `F11` (retrieval frequency without stakes);
`survey/05` §8 (the machine-audience hypothesis); `survey/01` (Deslauriers, Bastani).

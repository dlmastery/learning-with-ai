---
title: "What AI Tutoring Has Actually Been Measured To Do: A Sober Scoreboard"
wave: B
section: B2
date_researched: 2026-07-27
sources_count: 47
---

# What AI Tutoring Has Actually Been Measured To Do

**Purpose of this section.** This is the accountability chapter. Every claim in this survey about
what AI can do for learning must survive contact with the measurement record. That record is
thinner, shorter-horizon, and more conflicted than the discourse suggests. The core finding of this
section, stated up front:

> **Almost every positive result in the LLM-tutoring literature is an immediate post-test
> administered at the end of the intervention window. Almost none of it measures retention.
> Almost none of it measures transfer. A short-term gain with no retention is not learning —
> it is performance.**

The second core finding:

> **The largest and most-cited meta-analytic estimate of ChatGPT's effect on learning
> (g = 0.867) was retracted by the publisher in 2026.** The field's headline number no longer
> exists, and nothing has replaced it.

---

## Evidence labels used throughout

| Label | Meaning |
|---|---|
| **[RCT-P]** | Preregistered randomized controlled trial, primary report read directly |
| **[RCT]** | Randomized controlled trial, not preregistered or preregistration unverified |
| **[QE]** | Quasi-experimental / matched / non-randomized |
| **[META]** | Meta-analysis or systematic review |
| **[PRE]** | Preprint, not peer reviewed |
| **[VEND]** | Report authored or funded by the party selling/building the product |
| **[CORR]** | Correlational or self-report survey; **cannot** support causal claims |
| **[RETRACT]** | Formally retracted by the publisher |
| **[SEC]** | Secondary source (news, blog, aggregator) — flagged as such, not load-bearing |

A **funder-independence** flag is applied throughout:
**(D)** = developer of the tool is an author or funder of the evaluation;
**(I)** = evaluation independent of the tool's developer;
**(M)** = mixed (independent assessment contractor inside a developer-run trial).

---

## 1. THE SCOREBOARD

This is the table a skeptic should cite. Every row is sourced in §3–§6 below.
"Retention?" means **a post-test administered after a delay, on the same or transferred content,
with the AI removed**. "Distal?" means an outcome measure not authored by the intervention team
(state test, school exam, standardized instrument).

### 1a. LLM-era tutoring studies

| # | Intervention | Effect size | n | Duration | Retention measured? | Distal outcome? | Funder / independence |
|---|---|---|---|---|---|---|---|
| 1 | **Gemini Guided Learning, Sierra Leone** (DeepMind + Fab AI, 2026) **[RCT-P]** | **+0.258 SD** math, ITT, ANCOVA (95% CI 0.027–0.488, p=0.029). **Unadjusted ITT +0.216 SD, SE 0.137 — not significant.** ToT at 12 h: +0.380 SD | 1,763 enrolled; **1,423 analysed** (balanced panel); 48 classrooms, 12 schools | 8 weeks (ran 9; 6 Oct–5 Dec 2025) | **NO** — endline only, no delayed test | Partial: IRT-scaled curriculum-aligned test built + scored blind by Oxford MeasurEd | Google.org + Gates Foundation; Google authored **(M)** |
| 2 | **Copilot/GPT-4 after-school English, Nigeria** (World Bank, 2025) **[RCT]** | +0.310 SD composite (SE 0.068); **+0.23–0.24 SD English**; **+0.206 SD** on school's third-term exam (SE 0.067) | 1,328 randomized (657 T / 671 C); **759 analysed (422/337) — ~43% attrition** | 6 weeks, 12 × 90 min after school | **NO** | **Yes** — third-term curricular exam, broader than intervention | World Bank **(I)** |
| 3 | **Bastani et al., GPT Tutor vs GPT Base, Turkey** (PNAS 2025) **[RCT]** | Practice: +48% (GPT Base, β=0.137, SE .031) / +127% (GPT Tutor, β=0.361, SE .032). **Unassisted exam: −17% for GPT Base (β=−0.054, SE .022, p<0.05)**; GPT Tutor −0.004 (ns) | ~1,000 high-school students, ~50 classrooms | 4 × 90-min sessions ≈15% of curriculum | **Partial — the exam is AI-removed, but same-session.** Authors: long-term outcomes blocked by partner school | No — researcher-built exam | Wharton AI & Analytics Initiative, Fishman-Davidson Center, Wharton Global Initiatives **(I)** |
| 4 | **Kestin et al., Harvard physics AI tutor** (Sci Rep 2025) **[RCT]** | d ≈ **0.63** (regression); 0.73–1.3 after ceiling correction; p<10⁻⁸ | 194 enrolled; 142 AI / 174 in-class post-tests | **Two single ~1-hour lessons**, one week apart | **NO** | No — researcher-built post-test, ceiling-limited | **No funding statement; no competing interests declared.** First author built the tutor and ran the analysis **(D)** |
| 5 | **Tutor CoPilot** (Stanford, 2024) **[RCT-P]** | **+4 p.p.** exit-ticket mastery (p<0.01); +9 p.p. for lowest-rated tutors | 900 tutors, 1,800 K-12 students, 4,136 sessions | ~2 months | **NO** | **Yes — and it was NULL.** "we did not find statistically significant improvements in end-of-year math test scores" | Smith Richardson Foundation; Arnold Ventures / Accelerate **(I)** |
| 6 | **Nie et al., "The GPT Surprise"** (L@S 2025) **[RCT]** | **Negative on engagement**: significant average decrease in exam participation. Positive exam effect *for adopters* — selection, not ITT | **5,831** students, 146 countries | Full online coding course | NO | No | Stanford (Code in Place) **(I)** |
| 7 | **LearnLM + Eedi, UK secondary** (Google, Dec 2025) **[PRE][RCT]** | +5.5 p.p. on novel problems (66.2% vs 60.7%) vs **human tutors** | **165** students, 5 schools | Not stated | **NO** | No | Google DeepMind + Eedi **(D)** |
| 8 | **Rori WhatsApp math tutor, Ghana** (2024) **[PRE][RCT]** | **0.37 SD** math growth (p<0.001) | ~1,000 students, **only 11 schools = 11 clusters** | 8 months, 2 × 30 min/week, **on top of** normal instruction | **NO** — "they only report on year 1" | No | Rising Academies staff are the authors **(D)** |
| 9 | **Lehmann, Cornelius & Sting, "AI Meets the Classroom"** **[RCT-P][PRE]** | **NO main effect** in either preregistered lab experiment. Substitutive use ↓ understanding; complementary use ↑ understanding. **LLMs widen the low/high prior-knowledge gap** | Lab: 107 + 69; field: 113 grad students (6,775 student-question obs) | 45-min learning phase (lab); 4–5 weeks (field) | Post-test immediately after; no delay | No | University, incentivized lab **(I)** |
| 10 | **wisdomBot assignment completion, China** (2025) **[QE]** | Assignment performance ↑, **learning outcomes / motivation harmed** | 127 middle-school students | One assignment cycle | NO | No | University **(I)** |
| 11 | **Khanmigo "Estudia Khanmigo" pilot** (Digital Promise, 2024) **[QE/descriptive]** | **No control group; no causal effect size.** Mixed-methods pilot; reports motivation/self-efficacy and infrastructure barriers | 2 schools (~310 + ~350 students) | Pilot | NO | NO | **Gates Foundation (D-adjacent)** |

### 1b. Meta-analytic estimates — LLM era

| # | Source | Estimate | k / n | Status |
|---|---|---|---|---|
| 12 | **Wang & Fan (2025), Hum Soc Sci Commun** | g = **0.867** learning performance; 0.456 perception; 0.457 higher-order thinking | 51 studies | **[RETRACT] — retracted 2026 for "discrepancies in the meta-analysis"; authors did not respond** |
| 13 | Wu & Yu (2023), *BJET* **[META]** | "large effect"; **short interventions > long** — authors attribute to novelty wearing off | 24 randomized studies | Live |
| 14 | **Gu & Yan (2025)**, *JECR* **[META]** | g = **0.683** overall; **with teacher support g = 1.426; without teacher support g = 0.077 (≈null)** | 19 studies, k=24 | Live — the single most important moderator finding in the LLM literature |
| 15 | (2025) *JCAL* 70117 **[META]** | g = 0.68 overall (cognitive 0.795 / competency 0.711 / affective 0.507) | 34 studies | Live |
| 16 | **Liu, Guo, He & Hu (2025)**, *JECR* **[META]** | achievement **0.857**, motivation 0.803 | 49 articles | Live — magnitude indistinguishable from the retracted paper |

### 1c. Pre-LLM baselines — what ITS actually delivered

| # | Source | Estimate | Scale | Note |
|---|---|---|---|---|
| 17 | **VanLehn (2011)** *Educ Psychologist* **[META]** | Human tutoring **d = 0.79** (not 2.0); ITS **d = 0.76** | Review of controlled experiments | **Demolishes Bloom's 2-sigma folklore.** ONR + NSF funded |
| 18 | **Ma et al. (2014)** *JEP* **[META]** | vs teacher-led g=0.42; vs other CBI g=0.57; vs textbook g=0.35. **vs individual human tutoring g = −0.11 (ns); vs small group g = 0.05 (ns)** | 107 ES, **14,321** participants | ITS ≈ human tutor is the *ceiling*, not a triumph |
| 19 | **Steenbergen-Hu & Cooper (2014)** *JEP* **[META]** | g = **0.32–0.37** (college); ITS **less effective than human tutoring**; **earlier studies significantly larger than recent ones** | 39 studies | Effect decay over time is the field's oldest warning sign |
| 20 | **Kulik & Fletcher (2016)** *RER* **[META]** | median **0.66** — but "the amount of improvement … depended to a great extent on whether improvement was measured on **locally developed or standardized tests**" | 50 controlled evaluations | Test-alignment is the dominant moderator |
| 21 | **Létourneau et al. (2025)** *npj Sci Learn* **[META]** | Positive but "**mitigated when compared to non-intelligent tutoring systems**" | 28 studies, N=4,597, mostly quasi-experimental | K-12; calls for longer interventions |
| 22 | **Pane et al. (2014), Cognitive Tutor Algebra I at scale** **[RCT]** | **Year 1: no effect.** Year 2: **+0.21 SD** high school; **not significant** middle school | 147 schools, 7 states, 2 years | The canonical at-scale ITS result. Efficacy ≠ effectiveness |
| 23 | **Roschelle et al. (2016/2020), ASSISTments** **[RCT]** | Significant gain on **end-of-year state standardized test**; largest for low prior achievers | 2,769–2,850 7th graders, 43 schools, Maine, 1 year | **The strongest distal-outcome ed-tech RCT in the corpus — and it is pre-LLM** |

### 1d. The human-tutoring ceiling — real numbers

| # | Source | Estimate | Scale | Funder |
|---|---|---|---|---|
| 24 | **Nickow, Oreopoulos & Quan (2024)**, *AERJ* **[META]** | Pooled **0.288 SD (SE 0.029)** | **96 randomized studies**, preK-12 | J-PAL North America **(I)** |
| 25 | Same team, NBER w27476 (2020 working paper) | Pooled **0.37 SD** | Same 96 studies | **The number fell from 0.37 → 0.288 between working paper and peer review.** Treat all working-paper effect sizes accordingly |
| 26 | Nickow et al., large-sample subset | **≈0.25 SD** for studies with n > 400 | — | Effects plateau, do not vanish, with sample size |

**The ceiling, stated plainly:** intensive, in-person, human one-to-one and small-group tutoring —
the most expensive and best-evidenced intervention in education — buys **≈0.29 SD**. Any AI
tutoring claim substantially above that, measured over weeks, on a researcher-built test, with no
retention check, should be treated as a measurement artifact until proven otherwise.

---

## 2. How to read the scoreboard

Three arithmetic facts kill most of the enthusiasm:

1. **The best LLM tutoring RCTs land in the same band as pre-LLM ITS and human tutoring.**
   Sierra Leone +0.258 SD, Nigeria +0.23–0.31 SD, Rori +0.37 SD, human tutoring 0.288 SD,
   ITS vs classroom 0.32–0.42 g. There is no order-of-magnitude jump. There may not even be a
   difference.

2. **The gap between proximal and distal outcomes is where the effect dies.** Tutor CoPilot:
   +4 p.p. on the exit ticket, **null** on the end-of-year test. Nigeria: 0.31 SD on the
   intervention-aligned composite, 0.206 SD on the school's own exam. Kulik & Fletcher found the
   same pattern in 2016 for ITS. This is the single most reproducible finding in the entire
   literature and it is almost never in the headline.

3. **Where the AI is removed, the sign can flip.** Bastani et al. is the only large study that
   builds AI-removal into the design, and unguarded GPT-4 produced a **−17%** exam effect —
   students did *worse than students who never had access*. That is not a null. That is a harm.

---

## 3. LLM TUTORING RCTs — the detail

### 3.1 Sierra Leone: Gemini Guided Learning (DeepMind + Fab AI, May 2026) **[RCT-P]**

- **Report:** "Teaching with Gemini: Measuring the impact of Guided Learning on student
  mathematics progress in Sierra Leone," LearnLM Team, Google & Fab AI, 2026-05-15.
  https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf
- **Blog:** https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/
- **Preregistration:** AEA RCT Registry **AEARCTR-0016651**. Ethics: Sierra Leone Ethics and
  Scientific Review Committee No. 007/09/2025.

**Design.** Two-arm cluster RCT, 12 government-supported junior secondary schools, Port Loko
District. N = 1,763 students aged 13+, 48 grade-7/8 maths classrooms. **Randomization at classroom
level within school × grade block.** Treatment teachers integrated Gemini Guided Learning (Pro
model) into half of weekly maths lessons — 2 periods (90 min) per week for 8 weeks, target 12 hours.
Students shared devices 2:1. Control continued standard instruction. **Both arms' teachers received
the identical 5–6 hour training** — a genuinely good design choice that rules out a training
confound.

**Result (verbatim).** "a gain of +0.258 standard deviations across the Guided Learning classrooms
(intent to treat; 95% confidence interval [0.027, 0.488], p = 0.029)."

**What the skeptic must add.** Table C.4 of the report gives three specifications:

| Specification | Treatment coefficient | SE | Significant? |
|---|---|---|---|
| (1) Unadjusted | **0.216** | 0.137 | **No** |
| (2) Baseline-adjusted (ANCOVA) | 0.258 | 0.115 | Yes (p<0.05) |
| (3) Fully adjusted | 0.259 | 0.116 | Yes (p<0.05) |

The headline effect exists only under covariate adjustment. ANCOVA is a legitimate and
almost certainly preregistered specification, and the arms were balanced — but the raw
difference between the arms is not statistically distinguishable from zero, and the adjusted
CI's lower bound (0.027) is a rounding error away from nothing.

**Other caveats the report itself discloses, to its credit:**
- **Heterogeneity, the buried headline.** "For each additional standard deviation of mathematics
  proficiency a student demonstrated at baseline, the treatment effect increased by +0.195 SD
  (95% CI [0.074, 0.315], **p = 0.002**)." The interaction is *an order of magnitude more
  statistically robust than the main effect*. Arithmetically: at the main-effect specification
  (0.250 + 0.195 × baseline), a student one SD **below** the mean gains ≈**0.055 SD** — nothing.
  The intervention worked for students who were already ahead. The authors say so: "new tools
  frequently widen achievement gaps rather than close them … our ambition is the opposite."
- **The model changed mid-trial.** Gemini 2.5 Pro for six weeks, Gemini 3.0 Pro for the final
  three (rolled out 18 Nov). The trial measures a moving target.
- **Analysis n is 1,423, not 1,763.** Baseline 1,547; 124 dropouts; 214 mid-trial entrants;
  endline 1,637; balanced panel 1,423. Follow-up rates 0.907 (control) / 0.933 (treatment).
- **Maths only.** Reading was measured at baseline as a covariate. Secondary coverage claiming
  gains "in math and English tests" **[SEC]** is not supported by the report.
- **NO retention or transfer test.** Endline is administered at the end of the intervention.
- **"1.2 to 1.7 years of learning" is a benchmark conversion**, using Evans & Yuan's LMIC
  progress benchmarks, not a measured longitudinal quantity.

**Independence.** Google authored the study and built the product. Mitigating: assessment
development and scoring were contracted to **Oxford MeasurEd**, blind to treatment assignment,
explicitly "to insulate outcome measurement from potential bias." Funders: Google.org and the
Gates Foundation; partners Fab AI, Sierra Leone MBSSE, EducAid, Laterite. Rate this **(M)** —
better than developer-graded, weaker than developer-independent.

**Independent critique** **[SEC]**: https://everydaydatascience.com/article/google-s-ai-tutor-raised-maths-scores-in-sierra-leone-it-raised-them-most-for-st
— makes the heterogeneity, CI-width, and moving-model points above.

### 3.2 Nigeria: World Bank / Microsoft Copilot after-school English **[RCT]**

De Simone, Tiberti, Barron Rodriguez, Manolio, Mosuro & Dikoru (2025), "From Chalkboards to
Chatbots," World Bank Policy Research Working Paper 11125.
https://doi.org/10.1596/1813-9450-11125 ·
Slides: https://voxdev.org/sites/default/files/2026-03/From%20Chalkboards%20to%20Chatbots.pdf

- Six-week after-school programme, **12 sessions × 90 minutes**, Microsoft Copilot (GPT-4),
  9 public schools, Benin City; first-year senior secondary (~15 yrs); students in pairs;
  teachers supervised but did not instruct; prompts explicitly grounded in retrieval practice,
  elaborative interrogation, concrete examples, desirable difficulties.
- **Student-level** randomization within school. 657 treatment / 671 control.
- ITT: **0.310 SD** weighted composite (SE 0.068); 0.263 IRT-scaled; **0.206 SD on the school's
  own third-term exam** (SE 0.067). English alone **0.23–0.24 SD**.
- Heterogeneity: treatment × female **+0.420** (main effect for males −0.039, ns);
  treatment × baseline score **+0.151**; treatment × SES **+0.113**. So: **gains concentrate in
  girls and in higher-baseline students** — the same gap-widening as Sierra Leone on the ability
  dimension, but reversed on gender.
- Cost: ~$9 marginal per student; benefit-cost ratio of the pilot claimed at 161–260.

**What the skeptic must add.**
- **~43% attrition, and it is differential.** 1,328 randomized → 759 analysed
  (422/657 = 64% treatment retained vs 337/671 = 50% control retained). The authors report Lee
  bounds and inverse-probability weighting and say effects survive; that is the right response, but
  a 14-point differential retention gap is a first-order threat, not a footnote.
- **The composite outcome includes "knowledge of artificial intelligence and digital skills"** —
  content the treatment arm was directly exposed to and the control arm was not. Cite the English
  (0.23) or the third-term exam (0.206) figure, never the 0.31 composite.
- **The control got nothing.** This is an *additional-instructional-time* study. Part of the
  effect is simply 18 extra hours of supervised English. There is no active-time control.
- **The "1.5–2 equivalent years of schooling" and the extrapolated "2.23 SD over 36 weeks"** are
  linear extrapolations from a 6-week dose. Nothing in the education literature supports linear
  dose-response over a school year; Pane et al. (2014) is direct evidence against it.
- **NO retention test.**

### 3.3 Bastani et al., PNAS 2025 — the most important study in the corpus **[RCT]**

Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), "Generative AI without guardrails can
harm learning: Evidence from high school mathematics," *PNAS*.
https://doi.org/10.1073/pnas.2422633122 · Open: https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/
· Working paper: https://doi.org/10.2139/ssrn.4895486

- ~1,000 students, ~50 classrooms, a large school in **Turkey**, 9th–11th grade, Fall 2023–24.
- Four 90-minute sessions ≈ 15% of the maths curriculum. Three arms: control (textbook/notes),
  **GPT Base** (plain ChatGPT-like), **GPT Tutor** (guardrailed: no direct solutions, hints only).
- Each session: teacher review → **assisted practice** → **unassisted closed-book, closed-laptop
  exam** on conceptually matched problems.

| Outcome | GPT Base | GPT Tutor |
|---|---|---|
| Assisted practice | +0.137 (SE 0.031) = **+48%** | +0.361 (SE 0.032) = **+127%** |
| Unassisted exam | **−0.054 (SE 0.022) = −17%, p<0.05** | −0.004 (SE 0.013), ns |

**Why this study matters more than the others.** It is the only large trial whose primary design
feature is *taking the AI away*. It therefore isolates exactly what the rest of the literature
cannot see: performance while assisted is not learning. Students using GPT Base copied — "GPT Base
provided correct answers only 51% of the time," and students used it as a crutch. Guardrails
restored the null but did **not** produce a positive learning effect: GPT Tutor's unassisted exam
coefficient is −0.004.

**The honest reading:** the best-designed guardrailed LLM tutor in the literature produced
**zero measurable learning benefit** on unassisted performance, and the unguardrailed version
produced harm. The +127% headline is a *practice-session* number and should never be quoted as a
learning effect.

**Limits.** Authors state explicitly: "we focus on short-term outcomes due to limitations imposed
by our partner school; studying long-term outcomes is a key direction for future research." Exam
is same-session, so this is AI-removal without a delay — better than everyone else, still not
retention.
**Funding:** Wharton AI & Analytics Initiative, Fishman-Davidson Center, Wharton Global
Initiatives. **(I)**

### 3.4 Kestin et al., Harvard physics **[RCT]**

Kestin, Miller, Klales, Milbourne & Ponti (2025), "AI tutoring outperforms in-class active
learning," *Scientific Reports* 15:17458. https://doi.org/10.1038/s41598-025-97652-6

- Undergraduate physics at Harvard, **N = 194** enrolled; 142 AI-arm and 174 in-class post-tests
  pooled across two weeks. Crossover: each group got one AI lesson and one in-class active-learning
  lesson, one week apart. Topics: surface tension (wk 1), fluid flow (wk 2). Pre-test before each.
- AI arm median post-test 4.5 vs in-class 3.5 (pre-test baseline 2.75). Regression d ≈ **0.63**,
  ceiling-corrected 0.73–1.3, p<10⁻⁸. AI students spent a **median 49 minutes** vs an assumed
  60 minutes of in-class learning time.
- Perceptions: engagement 4.1 vs 3.6 (p<0.0001); motivation 3.4 vs 3.1 (p<0.001).

**What the skeptic must add.**
- **The intervention is two hours of a student's life.** Any claim generalising this to a course,
  a term, or a curriculum is unsupported by the data.
- **Immediate post-test only. No retention, no transfer.** The authors are explicit that this is
  future work: "systematic integration of well-established retention enhancing strategies (e.g.,
  spacing)" is listed as a *compelling direction for future work* — i.e. it was not done.
- **Ceiling effects are acknowledged by the authors**, which is why the effect size is reported as
  a range up to 1.3. A post-test that saturates is a post-test that cannot measure depth.
- **The comparison is not tutor-vs-teacher, it is medium-vs-medium with unequal conditions.**
  The AI arm worked at home, self-paced, with expert-crafted per-question prompts, pre-written
  correct answers supplied to the model, and professionally produced Harvard Bok Center videos.
  The in-class arm got one lecture hall session minus 15 minutes of testing. This is a comparison
  of a heavily engineered artifact against ordinary practice.
- **No funding statement. "The authors declare no competing interests."** The first author
  conceptualised, engineered, administered, validated and analysed the AI tutor he was evaluating.
  That is a developer-evaluator conflation regardless of the declaration. **(D)**

### 3.5 Tutor CoPilot (Stanford) — the null nobody quotes **[RCT-P]**

Wang, Ribeiro, Robinson, Loeb & Demszky (2024), "Tutor CoPilot: A Human-AI Approach for Scaling
Real-Time Expertise." arXiv:2410.03017 · https://arxiv.org/abs/2410.03017 ·
Preregistration: https://osf.io/8d6ha

- **900 tutors, 1,800 K-12 students** from Title I schools, US Southern district, majority
  Hispanic. Randomization **at tutor level** (not student level). ~2 months from end-March 2024.
  4,136 sessions, 550,000+ messages.
- Headline: students of treatment tutors **4 p.p. more likely to pass the exit ticket** (p<0.01);
  **9 p.p.** for students of the lowest-rated tutors; 14 p.p. in one subgroup. Cost $20/tutor/year.
- Mechanism: treatment tutors used "asking questions to guide thinking" ≈2 SD more on a log-odds
  scale and gave away answers less.

**The buried result, verbatim from §7 Limitations:**

> "while we observed substantial improvements in students' proximal learning gains (i.e., the
> students' exit ticket performance), **we did not find statistically significant improvements in
> end-of-year math test scores**; please refer to Appendix K for this analysis."

This is the cleanest proximal/distal dissociation in the LLM literature: a well-powered,
preregistered, independently funded RCT that moved the in-platform metric and did not move the
state test. The authors attribute it to low treatment dosage and the two-month window — plausible,
and untested.

**Funding:** Smith Richardson Foundation; Arnold Ventures/Accelerate. **(I)**

### 3.6 Nie et al., "The GPT Surprise" — the engagement harm **[RCT]**

Nie, Chandak, Suzara, Malik, Woodrow, Peng, Sahami, Brunskill & Piech (2024/2025).
arXiv:2407.09975 · L@S 2025: https://doi.org/10.1145/3698205.3733960

- **5,831 students from 146 countries** in a large free online coding class; randomized offer of
  GPT-4 chat access.
- Verbatim: "we estimate positive benefits on exam performance for adopters, the students who used
  the tool, but **over all students, the advertisement of GPT-4 led to a significant average
  decrease in exam participation**. We observe similar decreases in other forms of course
  engagement."
- Moderated by development level: offering LLM access to students from **low-HDI countries
  increased** their exam participation.
- Authors' own conclusion: "potential harms for engagement, which makes their **longer term impact
  on student success unclear**."

**Publication-honesty note:** the 2024 preprint was titled "…Reduced Engagement but **Increased**
Adopters Exam Performances." The peer-reviewed 2025 version reads "…but **May Increase**…" — the
adopter effect is selection, not a randomized contrast, and peer review made them say so. That is
the system working; it is also a warning about every preprint effect size in this section.

### 3.7 LearnLM + Eedi, UK **[PRE]**

"AI tutoring can safely and effectively support students: An exploratory RCT in UK classrooms,"
Google LearnLM Team & Eedi, Dec 2025. https://arxiv.org/abs/2512.23633

- **165 students**, 5 UK secondary schools. LearnLM drafts tutoring messages; **expert human tutors
  supervise and can edit** before sending. 76.4% of AI-drafted messages needed zero or minimal
  edits.
- Result: LearnLM-guided students "performed at least as well as students chatting with human
  tutors"; **+5.5 p.p.** on novel problems (66.2% vs 60.7%).
- **Note the comparator is human tutors, and the claim is non-inferiority, not superiority.**
  n=165 is far too small to establish equivalence with any precision. No retention. Google + Eedi
  authored. **(D)**

### 3.8 Rori, Ghana **[PRE]**

Henkel, Horne-Robinson, Kozhakhmetova & Lee (2024), "Effective and Scalable Math Support:
Experimental Evidence on the Impact of an AI-Math Tutor in Ghana." arXiv:2402.09809

- ~1,000 students, grades 3–9, **11 schools**, 8 months, two 30-min WhatsApp sessions/week
  **in addition to** regular instruction. Effect **0.37 SD** on math growth, p<0.001.
- **Cluster problem:** assignment is at school level with 11 clusters. Standard errors from 11
  clusters are not to be trusted; this alone should downgrade the result.
- **Additional-time confound** again: treatment gets ~35 extra hours; control gets nothing.
- Authors are Rising Academies personnel — the network that built and sells Rori. **(D)**
- Authors' own caution, verbatim: "the results should be interpreted judiciously, as they only
  report on year 1."
- A larger independent J-PAL/Oxford full-scale RCT of Rori is registered
  (https://www.povertyactionlab.org/initiative-project/scaling-ai-powered-math-tutoring-across-diverse-educational-contexts-full-scale)
  and its results are the thing to wait for. **[SEC]**

### 3.9 Khanmigo — the evaluation that does not exist

The most-marketed AI tutor in K-12 has **no published randomized efficacy trial**.

- The substantive study is a Gates-funded **pilot**: "Estudia Khanmigo: An equity-focused pilot
  exploration," Digital Promise, Sept 2024.
  https://digitalpromise.org/wp-content/uploads/2024/09/SRM-Gates-Khanmigo-Report-Final.pdf
  Two Puerto Rico schools (~310 and ~350 students), mixed-methods, **no control group**. It reports
  math motivation and self-efficacy, and finds that "pervasive and deeply rooted infrastructural
  limitations hinder students and teachers from using the tool to its full potential." It does not
  and cannot estimate a learning effect. The report itself flags an intended "island-wide
  three-year randomized control trial" as future work. **[QE]**
- Figures circulating as "Khanmigo produced a 0.15 SD gain" or "12% improvement after a full year"
  trace to **SEO-farm blogs, not to any peer-reviewed or vendor-published study**
  (e.g. edrus.org, k12flash.com, plainai.aguidetocloud.com). **[SEC] — do not cite.**
- **Action for this survey:** Khanmigo should be listed as *unevaluated*, not as *effective*.

---

## 4. THE NULLS AND THE HARMS

Underreported by construction: journals publish effects, vendors publish wins, and null results in
this area are usually buried in a limitations section (Tutor CoPilot) or a working paper.

### 4.1 Retention/transfer removal → the effect inverts

**Bastani et al. (2025)** (§3.3). GPT Base: **−17%** on the unassisted exam vs students who never
had access. This is the strongest evidence in the field that assisted performance and learning
dissociate, and it is a *harm*, not a null. The mechanism is documented: students used GPT-4 as a
crutch, and GPT-4 was wrong 49% of the time on these problems.

### 4.2 Lehmann, Cornelius & Sting — the preregistered null

"AI Meets the Classroom: When Do Large Language Models Harm Learning?" arXiv:2409.09047 (v2, Mar
2025). **[RCT-P][PRE]**

- **Study 1 (field):** two graduate programming courses, Dutch university, Spring 2023. 56 + 57 =
  **113 students**, 6,775 student-question observations. Negative effect of *substitutive* LLM use.
- **Study 2 (lab, preregistered, incentivized):** German university lab pool, **107 subjects**
  after exclusions; 45-min Python learning phase, 20-question pre/post-tests. Post-test 9.0 (T) vs
  7.9 (C); pre-test 3.6 vs 3.1. **No support for either hypothesis.** (Copy-paste was accidentally
  disabled in the lab, which the authors treat as an unintended treatment on LLM usage cost.)
- **Study 3 (exact replication with copy-paste enabled):** **69 subjects**. Treated covered more
  topics but understood each one less.
- **Headline, verbatim:** "In two pre-registered and incentivized laboratory experiments, **we find
  no effect of LLMs on overall learning outcomes**. … Students who substitute some of their
  learning activities with LLMs … increase the volume of topics they can learn about but decrease
  their understanding of each topic. … **We also observe that LLMs widen the gap between students
  with low and high prior knowledge.**"
- Body text is blunter: "LLMs support the learning of students with more prior knowledge but
  **harm** the learning of students with less prior knowledge."

**This is the third independent observation of the same gap-widening pattern** (Sierra Leone
+0.195 SD per baseline SD; Nigeria +0.151 per baseline SD; Lehmann). Three studies, three
countries, three age groups, three tools, same direction. Treat gap-widening as the **default
expectation** for LLM tutoring, not a risk.

### 4.3 Assignment completion harms — wisdomBot

"Impact of Assignment Completion Assisted by Large Language Model-Based Chatbot on Middle School
Students' Learning," *Education and Information Technologies* (2025).
https://doi.org/10.1007/s10639-024-12898-3 · **[QE]**, 127 Chinese middle-school students.
Assignment performance improves; learning outcomes and motivation do not follow. Quasi-experimental
— weak design, but directionally consistent with Bastani.

### 4.4 The teacher-support moderator — GenAI alone is ≈null

Gu & Yan (2025), "Effects of GenAI Interventions on Student Academic Performance: A Meta-Analysis,"
*JECR*. https://doi.org/10.1177/07356331251349620 · **[META]**, 19 studies, 24 effect sizes.

> Overall g = 0.683. **"Students with teacher support in the student–GenAI interaction have
> significantly larger gains (g = 1.426) than those without teacher support (g = 0.077)."**

Read that again. In the meta-analytic corpus, **GenAI without a teacher in the loop produces
g = 0.077 — statistically and practically indistinguishable from nothing.** Every positive
result in §3 that survives scrutiny (Sierra Leone, Nigeria, Kestin, Tutor CoPilot) is a
teacher-designed, teacher-supervised intervention with the LLM as one component. The DeepMind
report says this itself: "the intervention in this trial is not a technological fix … The teachers
played an especially key role."

**Implication for the survey:** the measured entity is *teacher-plus-AI activity design*, not
*AI tutoring*. No study in this corpus isolates the AI's contribution.

### 4.5 Metacognitive offloading — weak evidence, strong claims

This literature is much worse than its citation counts suggest.

- **Gerlich (2025)**, "AI Tools in Society: Impacts on Cognitive Offloading and the Future of
  Critical Thinking," *Societies* 15(1):6, https://doi.org/10.3390/soc15010006 — 732 citations.
  **[CORR]** — a **survey and interview study of 666 participants**. Cross-sectional,
  self-reported, correlational. It cannot establish that AI use *causes* reduced critical thinking,
  and it does not measure learning. It also carries a published **Correction**
  (https://doi.org/10.3390/soc15090252). Cite it as evidence of an association and a hypothesis;
  never as a causal finding.
- **Lee et al. (2025)**, "The Impact of Generative AI on Critical Thinking: **Self-Reported**
  Reductions in Cognitive Effort and Confidence Effects From a **Survey** of Knowledge Workers,"
  CHI 2025, https://doi.org/10.1145/3706598.3713778. **[CORR]** — the title is honest; the
  citations are not. Self-report, knowledge workers, not students, not learning outcomes.
- **Kosmyna et al. (2025)**, "Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an
  AI Assistant for Essay Writing Task," arXiv:2506.08872. **[PRE]** — **54 participants**, three
  sessions, only **18** returned for the fourth; 216 pages; EEG connectivity plus essay-recall.
  LLM users showed weakest neural connectivity and "struggled to accurately quote their own work."
  Suggestive and mechanistically interesting; **n=18 at the critical crossover session, not peer
  reviewed**. It is not evidence that AI tutoring harms learning; it is evidence that essay-writing
  with an LLM engages less of the brain, which is close to tautological.

**Honest summary of §4.5:** the "AI rots your brain" literature currently consists of two surveys
and one small unrefereed EEG preprint. The *rigorous* evidence for offloading harm is
**Bastani et al. and Lehmann et al.** — behavioural, randomized, and specific about mechanism.
Lead with those.

---

## 5. MEASUREMENT VALIDITY — press this hard

### 5.1 The corpus does not measure retention. Here is the count.

ERIC full-corpus record counts, queried 2026-07-27 via https://api.ies.ed.gov/eric/ :

| Query | Records |
|---|---:|
| `"ChatGPT"` | 1,668 |
| `"ChatGPT" AND "learning outcomes"` | 95 |
| `"ChatGPT" AND "post-test"` | 27 |
| **`"ChatGPT" AND "delayed post-test"`** | **2** |
| **`"ChatGPT" AND "retention test"`** | **0** |
| **`"ChatGPT" AND "transfer test"`** | **0** |
| `"ChatGPT" AND "randomized controlled trial"` | 7 |
| **`"ChatGPT" AND "preregistered"`** | **0** |
| `"large language model" AND "delayed post-test"` | 0 |
| `"artificial intelligence" AND "delayed post-test"` | 4 |
| `"intelligent tutoring" AND "delayed post-test"` | 2 |
| *(control)* `"delayed post-test"` — any topic | **273** |

The control row is the point. **"Delayed post-test" is a routine construct in education research —
273 ERIC records use it. Two of them involve ChatGPT.** The field has the instrument and does not
use it. Likewise: zero ERIC records combine ChatGPT with "preregistered," and seven with
"randomized controlled trial," out of 1,668.

*Caveat on method:* ERIC indexes abstracts and descriptors, not full text, and lags recent
preprints; these counts are a lower bound and the ratio is the meaningful quantity, not the
absolute numbers. The ratio is roughly **2%** of ChatGPT-plus-outcomes studies, and **0.1%** of
all ChatGPT studies.

### 5.2 Proximal vs distal: the effect shrinks or disappears

| Study | Proximal (aligned/in-platform) | Distal (external/standardized) |
|---|---|---|
| Tutor CoPilot | +4 p.p. exit ticket, p<0.01 | **null** on end-of-year math test |
| Nigeria | +0.310 SD composite | +0.206 SD third-term school exam |
| Pane et al. 2014 (ITS) | — | Yr 1 null; Yr 2 +0.21 SD HS only |
| Kulik & Fletcher 2016 (ITS) | median 0.66 overall | "depended to a great extent on whether … locally developed or standardized tests" |
| Nickow et al. 2024 (human tutoring) | — | pooled 0.288 SD |

This is not an AI phenomenon; it is the oldest known confound in instructional evaluation, and the
LLM literature has reproduced it without acknowledging it.

### 5.3 The three things a positive result must survive

Any AI tutoring claim should be interrogated with:

1. **Was the AI removed at test time?** If not, it measures assisted performance. (Only Bastani
   et al. designed for this.)
2. **Was there a delay?** If not, it measures encoding, not retention. (Nobody in the LLM corpus
   did this.)
3. **Who wrote the test?** If the intervention team did, expect roughly 2–3× inflation relative to
   a standardized instrument — the documented pattern in ITS and human tutoring meta-analyses.

**No study in this section passes all three. Bastani et al. passes one and a half.**

### 5.4 Novelty and duration

Wu & Yu (2023), *BJET*, https://doi.org/10.1111/bjet.13334 **[META]**, 24 randomized studies:
short interventions produce **stronger** effects than long ones, which the authors attribute
directly to novelty — "the novelty effects of AI chatbots could improve learning outcomes in short
interventions, but it has worn off in the long interventions."

Steenbergen-Hu & Cooper (2014) found the same temporal decay across the ITS corpus: "effectiveness
in earlier studies appeared to be significantly greater than that in more recent studies."

Pane et al. (2014) found the opposite shape at scale — **null in year 1, +0.21 SD in year 2** —
which is implementation ramp, not novelty. Both patterns exist. Neither is measurable in an
8-week trial. Every single LLM tutoring RCT in §3 except Rori (8 months) is 8 weeks or shorter.

---

## 6. PUBLICATION BIAS, RETRACTION, AND WHO PAID

### 6.1 The field's headline meta-analysis was retracted

**Wang, J. & Fan, W. (2025).** "The effect of ChatGPT on students' learning performance, learning
perception, and higher-order thinking: insights from a meta-analysis." *Humanities and Social
Sciences Communications*, published 6 May 2025. https://doi.org/10.1057/s41599-025-04787-y

Reported, from 51 studies (Nov 2022 – Feb 2025):
**g = 0.867** learning performance, **g = 0.456** learning perception, **g = 0.457** higher-order
thinking.

**Retraction Note (2026), https://doi.org/10.1057/s41599-026-07310-z, verbatim:**

> "The Editor has decided to retract this article due to concerns relating to discrepancies in the
> meta-analysis. These concerns were initially raised by Magnus Ingebrigtsen and Marko Lukic. Taken
> together, the identified issues undermine the Editor's confidence in the validity of the analysis
> and the conclusions drawn from it. **The authors have not responded to correspondence regarding
> this retraction.**"

**[RETRACT]** This paper accumulated >250 citations before retraction and is the source of most
"ChatGPT has a large effect on learning" claims in the popular and grey literature. Assume it is
still being cited. Anything downstream of g = 0.867 is now unsupported.

### 6.2 The rest of the meta-analytic corpus reports implausibly similar numbers

| Source | Effect | k |
|---|---|---|
| Wang & Fan 2025 **[RETRACTED]** | g = 0.867 | 51 |
| Liu, Guo, He & Hu 2025, *JECR* | achievement **0.857**, motivation 0.803 | 49 |
| *JCAL* 2025 (10.1111/jcal.70117) | g = 0.68 (cognitive 0.795) | 34 |
| Gu & Yan 2025, *JECR* | g = 0.683 — **0.077 without teacher support** | 19 |
| *JECR* 2024 (10.1177/07356331241277937) | significant positive | 28 articles / 65 studies / **1,909 participants total** |

Observations a skeptic should make:

1. **These effect sizes are 2–3× the human-tutoring gold standard (0.288 SD)**, produced by
   interventions costing a fraction as much, measured over weeks. That is prima facie implausible.
2. **The primary corpus is tiny and low-powered.** The 2024 *JECR* meta-analysis pools 65 studies
   totalling **1,909 participants** — a mean of ~29 participants per study. Small-sample
   quasi-experiments with researcher-built tests are exactly the recipe for inflated pooled
   effects.
3. **The moderator that matters is buried.** The one meta-analysis that tested for teacher support
   found the effect collapses to g = 0.077 without it.
4. **Compare the human-tutoring corpus for what rigour looks like:** Nickow et al. restricted to
   RCTs, reported that unpublished papers had *larger* effects than published ones (evidence
   *against* publication bias), and their pooled estimate **fell from 0.37 SD in the 2020 working
   paper to 0.288 SD in the 2024 peer-reviewed version**. No GenAI meta-analysis in the table above
   has been through that kind of correction cycle.

### 6.3 Who paid for which study

| Study | Funder(s) | Tool built by | Assessment by | Flag |
|---|---|---|---|---|
| Sierra Leone Gemini | Google.org, Gates Foundation | **Google (author)** | Oxford MeasurEd, blind to arm | **(M)** |
| LearnLM/Eedi UK | Google DeepMind, Eedi | **Google + Eedi (authors)** | Eedi platform | **(D)** |
| Rori Ghana | Rising Academies | **Rising Academies (authors)** | in-house | **(D)** |
| Khanmigo pilot | **Gates Foundation** | Khan Academy | Digital Promise | **(D-adjacent)**; no causal design |
| Nigeria Copilot | World Bank | Microsoft (off-the-shelf) | World Bank team | **(I)** |
| Bastani et al. | Wharton AI & Analytics Initiative; Fishman-Davidson Center; Wharton Global Initiatives | authors (prompt layer over GPT-4) | authors | **(I)** |
| Tutor CoPilot | Smith Richardson Foundation; Arnold Ventures/Accelerate | **authors (Stanford)** | platform exit tickets + state test | **(I)** funding, **(D)** tool |
| Kestin et al. | **none declared** | **first author** | first author | **(D)** |
| Nie et al. | Stanford (Code in Place) | authors | course exam | **(I)** |
| Lehmann et al. | university lab, incentivized subjects | off-the-shelf LLM | authors | **(I)** |
| Nickow et al. (human tutoring baseline) | J-PAL North America | n/a | n/a | **(I)** |
| VanLehn 2011 (ITS baseline) | ONR N00014-00-1-0600; NSF (5 grants) | n/a | n/a | **(I)** |

**Pattern:** the *largest* effect sizes (Kestin d≈0.63–1.3, Rori 0.37) come from **(D)** studies
where the tool's builder ran the evaluation. The *smallest and most negative* results
(Tutor CoPilot's distal null, Bastani's −17%, Lehmann's null, Nie's engagement drop) come from
**(I)** studies. The Sierra Leone trial's **(M)** structure — developer-run, independently and
blindly assessed — is currently the best compromise on offer and should be the minimum bar the
field demands going forward.

**A note in DeepMind's favour.** The Sierra Leone report volunteers the non-significant unadjusted
estimate, the gap-widening interaction, the mid-trial model swap, and the attrition flow, and
preregisters at AEA. That is materially more transparent than the norm for vendor research.
The problem is not the report; it is what happens to the report in the second-hand telling.

---

## 7. WHAT HAS NOT BEEN MEASURED

The studies the field needs and does not have. Each of these is a concrete, fundable design.

1. **A delayed post-test, AI removed, ≥4 weeks.** *Nobody has done this.* Take any of the positive
   RCTs in §3 and re-test the same students one month later with no AI. Until this exists, the
   field has no evidence that AI tutoring produces durable learning. This is the single highest-value
   missing study in the entire literature.

2. **A transfer test.** Every outcome in §3 is near-transfer at best (Bastani: "each problem in the
   exam corresponds to a conceptually very similar practice problem"). Zero far-transfer measures.

3. **An active-time-matched control.** Nigeria and Rori both give the treatment arm substantial
   extra instructional hours against a do-nothing control. The correct comparison is
   *AI tutoring vs equal-time human-supervised study*, and nobody has run it.

4. **Isolation of the AI's contribution.** Every successful intervention is
   teacher + activity design + peer pairing + AI. The meta-analytic evidence says the effect is
   ~0.077 without the teacher. A factorial design (teacher-designed activity with vs without AI)
   would settle in one trial whether the AI is doing anything.

5. **A trial powered on the bottom quartile.** Three studies now show gap-widening by prior
   attainment. None was designed to detect or fix it. The needed study **stratifies on baseline
   attainment and powers the low-baseline stratum as a primary outcome**, not an appendix
   interaction. DeepMind states the intent; nobody has executed it.

6. **A multi-year, at-scale effectiveness trial.** The longest LLM tutoring RCT here is 8 months
   (Rori, 11 clusters, developer-run). Pane et al. (2014) showed a null in year 1 that became
   +0.21 SD in year 2 — the LLM field has no study capable of seeing either shape.

7. **Preregistered replication of Bastani et al.** The most consequential result in the field
   (unguarded LLM access → −17%) rests on a single school in one country. It has not been
   replicated. If it holds, it should govern deployment policy globally.

8. **Metacognitive calibration as an outcome.** The classic finding is that learners' judgments of
   learning are uncorrelated with actual retention. LLM tutors are optimised for perceived
   helpfulness — Kestin reports higher engagement and motivation, students *feel* better. Nobody
   has measured whether AI tutoring **worsens metacognitive calibration**, which would be the
   precise mechanism by which a pleasant tutor produces worse learners.

9. **Independent, non-vendor evaluation of the mass-market products.** Khanmigo has no RCT.
   ChatGPT Study Mode, Gemini Guided Learning outside Google's own trials, and Copilot in schools
   have no independent efficacy evidence. Hundreds of millions of student-hours, zero independent
   trials.

10. **Harm surveillance.** Nie et al. found a randomized *engagement* harm across 5,831 students.
    No study in this corpus prospectively monitors for dependency, help-seeking suppression,
    reduced peer collaboration, or effort withdrawal as pre-specified safety outcomes. Education
    research has no equivalent of an adverse-event registry, and this is the technology that most
    needs one.

---

## 8. THE ONE-PARAGRAPH VERDICT

Well-designed, teacher-supervised LLM tutoring interventions produce immediate post-test gains of
roughly **0.2–0.4 SD** — the same band as pre-LLM intelligent tutoring systems (0.32–0.42 g) and
in-person human tutoring (0.288 SD), at much lower cost, which is the genuinely important finding.
But the effect is measured almost exclusively at the end of the intervention, on tests aligned to
the intervention, with the AI still in the room; where a distal outcome exists it shrinks
(Nigeria) or vanishes (Tutor CoPilot); where the AI is removed without guardrails it inverts
(Bastani, −17%); where teacher support is removed it collapses (g = 0.077); it consistently
benefits already-advantaged learners more (three independent studies); the field's headline
meta-analysis has been retracted; the largest reported effects come from developer-run
evaluations; and **not one study in the corpus has administered a delayed retention test.**
The honest claim is: *AI tutoring reliably improves short-run performance on aligned assessments
when embedded in a teacher-designed activity, and nobody has yet shown that it produces learning
that lasts.*

---

## SOURCE LIST

**Primary LLM tutoring trials**
1. LearnLM Team, Google & Fab AI (2026). Teaching with Gemini: Sierra Leone. https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf · AEARCTR-0016651 **[RCT-P]**
2. Google DeepMind blog. https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/ **[VEND]**
3. De Simone et al. (2025). From Chalkboards to Chatbots. https://doi.org/10.1596/1813-9450-11125 **[RCT]**
4. Slides: https://voxdev.org/sites/default/files/2026-03/From%20Chalkboards%20to%20Chatbots.pdf
5. Bastani et al. (2025). PNAS. https://doi.org/10.1073/pnas.2422633122 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ **[RCT]**
6. Bastani et al. working paper. https://doi.org/10.2139/ssrn.4895486
7. Kestin et al. (2025). Sci Rep 15:17458. https://doi.org/10.1038/s41598-025-97652-6 **[RCT]**
8. Wang, Ribeiro, Robinson, Loeb & Demszky (2024). Tutor CoPilot. https://arxiv.org/abs/2410.03017 · https://osf.io/8d6ha **[RCT-P]**
9. Tutor CoPilot journal version. https://doi.org/10.21203/rs.3.rs-5363154/v1
10. Nie et al. (2024). The GPT Surprise (preprint). https://arxiv.org/abs/2407.09975 **[PRE]**
11. Nie et al. (2025). L@S. https://doi.org/10.1145/3698205.3733960 **[RCT]**
12. Google LearnLM & Eedi (2025). UK classrooms RCT. https://arxiv.org/abs/2512.23633 **[PRE][VEND]**
13. Henkel et al. (2024). Rori, Ghana. https://arxiv.org/abs/2402.09809 **[PRE][VEND]**
14. J-PAL/Oxford full-scale Rori RCT (registered). https://www.povertyactionlab.org/initiative-project/scaling-ai-powered-math-tutoring-across-diverse-educational-contexts-full-scale
15. Digital Promise (2024). Estudia Khanmigo. https://digitalpromise.org/wp-content/uploads/2024/09/SRM-Gates-Khanmigo-Report-Final.pdf **[QE]**
16. Henkel et al. (2024). Safe Generative Chats in a WhatsApp ITS. https://arxiv.org/abs/2407.04915 **[PRE]**

**Nulls and harms**
17. Lehmann, Cornelius & Sting (2025). AI Meets the Classroom. https://arxiv.org/abs/2409.09047 **[RCT-P][PRE]**
18. wisdomBot study (2025). Educ Inf Technol. https://doi.org/10.1007/s10639-024-12898-3 **[QE]**
19. Gerlich (2025). Societies 15(1):6. https://doi.org/10.3390/soc15010006 **[CORR]**
20. Correction to Gerlich (2025). https://doi.org/10.3390/soc15090252
21. Lee et al. (2025). CHI. https://doi.org/10.1145/3706598.3713778 **[CORR]**
22. Kosmyna et al. (2025). Your Brain on ChatGPT. https://arxiv.org/abs/2506.08872 **[PRE]**

**Meta-analyses, LLM era**
23. Wang & Fan (2025). https://doi.org/10.1057/s41599-025-04787-y **[RETRACT]**
24. Retraction Note (2026). https://doi.org/10.1057/s41599-026-07310-z
25. Wu & Yu (2023). BJET. https://doi.org/10.1111/bjet.13334 **[META]**
26. Effects of GenAI Interventions (2025). JECR. https://doi.org/10.1177/07356331251349620 **[META]**
27. Meta-Analysis of Impact of GAI on Learning Outcomes (2025). JCAL. https://doi.org/10.1111/jcal.70117 **[META]**
28. Effects of GenAI on K-12 and HE Students (2025). JECR. https://doi.org/10.1177/07356331251329185 **[META]**
29. Does GenAI Improve Academic Achievement of College Students? (2024). JECR. https://doi.org/10.1177/07356331241277937 **[META]**
30. Exploring the Impact of GAI on Learning Outcomes (2025). Educ Inf Technol. https://doi.org/10.1007/s10639-025-13420-z **[META]**
31. Impact of ChatGPT on Academic Achievement (2025). JCAL. https://doi.org/10.1111/jcal.70096 **[META]**

**Pre-LLM ITS baselines**
32. VanLehn (2011). Educ Psychologist 46(4). https://doi.org/10.1080/00461520.2011.611369 **[META]**
33. Ma, Adesope, Nesbit & Liu (2014). JEP. https://doi.org/10.1037/a0037123 **[META]**
34. Steenbergen-Hu & Cooper (2014). JEP. https://doi.org/10.1037/a0034752 **[META]**
35. Kulik & Fletcher (2016). RER. https://doi.org/10.3102/0034654315581420 **[META]**
36. Létourneau et al. (2025). npj Sci Learn. https://doi.org/10.1038/s41539-025-00320-7 **[META]**
37. Pane, Griffin, McCaffrey & Karam (2014). EEPA 36(2):127-144. https://doi.org/10.3102/0162373713507480 **[RCT]**
38. RAND addendum WR-1050-DEIES. http://www.rand.org/pubs/working_papers/WR1050.html
39. Roschelle, Feng, Murphy & Mason (2016). AERA Open. https://doi.org/10.1177/2332858416673968 **[RCT]**
40. Roschelle et al. (2020). JREE. https://doi.org/10.1080/19345747.2019.1710885 **[RCT]**
41. Baker (2016). Stupid Tutoring Systems, Intelligent Humans. IJAIED. https://doi.org/10.1007/s40593-016-0105-0

**Human tutoring baseline**
42. Nickow, Oreopoulos & Quan (2024). AERJ. https://doi.org/10.3102/00028312231208687 — pooled **0.288 SD (SE 0.029)**, 96 studies, funded by J-PAL North America **[META]**
43. Nickow et al. (2020). NBER w27476. https://doi.org/10.3386/w27476 — pooled 0.37 SD **[META]**
44. Major, Francis & Tsapali (2021). Technology-supported personalised learning in LMICs. BJET. https://doi.org/10.1111/bjet.13116 **[META]**

**Method / corpus queries**
45. ERIC API, counts run 2026-07-27. https://api.ies.ed.gov/eric/
46. OpenAlex API (bibliographic verification). https://api.openalex.org
47. Independent critique of the Sierra Leone trial. https://everydaydatascience.com/article/google-s-ai-tutor-raised-maths-scores-in-sierra-leone-it-raised-them-most-for-st **[SEC]**

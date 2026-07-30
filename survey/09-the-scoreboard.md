---
title: "The Scoreboard — what AI tutoring has actually been measured to do"
section: efficacy
status: draft
date: 2026-07-28
source_report: research/raw/B2-ai-tutoring-efficacy.md
---

# The Scoreboard

Two hundred and seventy-three studies in the ERIC database use a delayed post-test.
Two of them involve ChatGPT.

That single ratio is the most important fact about the efficacy literature, and it
is not a complaint about rigour. It is an *opportunity*, because a delayed
unassisted test is a routine, cheap, well-understood instrument that the field
already owns and has simply not pointed at this technology. The first team that
does will produce the most valuable result in the area, and they can do it with a
month of patience and a novel item set.

Here is what the record currently says, and what it does not.

---

## 1. The band, and the three machines inside it

Start with what each number measured and when it ran, because the class of system
that produced an effect size decides what that effect size can be evidence about.

Intensive, in-person, one-to-one and small-group human tutoring — the most
expensive and best-evidenced intervention in education — pools at **0.288 SD (SE
0.029)** across 96 randomised studies (Nickow, Oreopoulos & Quan, *AERJ* 2024,
funded by J-PAL North America). Those are 96 randomised trials of human tutors and
zero trials of anything else. So 0.288 is the benchmark a machine has to clear: what
a hired, trained person alone with a child has been measured to deliver. It is not a
bound on any machine, because no machine appears in it.

One thing we cannot tell you about it, and should say so: **the corpus establishes
the year of the synthesis and not the years of the trials inside it.** Nickow's pool
appeared as an NBER working paper in 2020 and in *AERJ* in 2024; no source we hold
gives the date range of the 96. The same is true of VanLehn's reviewed experiments
and of both 2014 ITS meta-analyses. Where a vintage below is a publication year and
not a fieldwork year, the column says so.

Now the AI results, all immediate post-tests unless stated. Every row carries the
class of system it measured and the year that system ran, because those two facts
govern what the row can be quoted for:

| Study | Class · ran | Effect | n | Duration | Delayed test? | Distal outcome? |
|---|---|---|---|---|---|---|
| **Sierra Leone**, Gemini Guided Learning (RCT-P) | FRONTIER · Gemini 2.5→3.0 Pro, ran Oct–Dec 2025 | **+0.258 SD** adjusted; **+0.216 SD unadjusted, n.s.** | 1,423 analysed, 48 classrooms | 8 weeks | No | Blind-scored, curriculum-aligned |
| **Nigeria**, Copilot after-school English (RCT) | FRONTIER · GPT-4, reported 2025 | +0.310 SD composite; **+0.206 SD on the school's own exam** | 759 analysed of 1,328 | 6 weeks | No | Yes |
| **Bastani et al.**, Turkey (PNAS) | FRONTIER · prompt layer over GPT-4, PNAS 2025 | Assisted practice +127%. **Unassisted exam: −17% unguarded, −0.004 guarded** (§01)| ~1,000 | 4 sessions | AI-removed, same session | No |
| **Kestin et al.**, Harvard physics | FRONTIER · purpose-built tutor, *Sci Rep* 2025 | d ≈ 0.63 (to 1.3 ceiling-corrected) | 194 | **two ~1-hour lessons** | No | No |
| **Tutor CoPilot** (RCT-P) | FRONTIER · ran from March 2024 | +4 p.p. exit ticket | 900 tutors, 1,800 students | 2 months | No | **Yes — and null** |
| **Rori**, Ghana | FRONTIER-era chatbot · 2024 | 0.37 SD | ~1,000, **11 clusters** | 8 months | No | No |
| **LearnLM + Eedi**, UK | FRONTIER · LearnLM, Dec 2025 | +5.5 p.p. on novel problems vs human tutors | **165** | not stated | No | No |
| Pre-LLM ITS (VanLehn; Ma et al.; Steenbergen-Hu & Cooper) | ITS · rule-based; syntheses **2011** and **2014**; trial years unestablished | d = 0.76 (VanLehn); g = 0.32–0.37 college (Steenbergen-Hu & Cooper); g = 0.42 vs teacher-led, 0.57 vs other computer-based instruction (Ma et al.) | meta | — | — | — |
| **Human tutoring** (Nickow, 96 RCTs) | HUMAN · synthesis **2024** (working paper 2020); trial years unestablished | **0.288 SD** | meta | — | — | — |

**The classroom deployment trials land in the same band as pre-LLM intelligent
tutoring systems and as human tutors.** Sierra Leone 0.258, Nigeria 0.23–0.31,
Rori 0.37, ITS 0.32–0.42, human tutoring 0.288. Three classes of machine, one band.
There is no order-of-magnitude jump in those numbers, and there may be no difference
between the three classes at all.

Two things have to be said about that comparison before anyone uses it again. **The
frontier side of the band is three field trials**, Sierra Leone and Nigeria and
Rori, and it is a rounding of those three and not a pooled estimate: no
meta-analysis, no confidence interval, n = 3. And **the ITS figure 0.32–0.42 appears
in no single source.** It splices Steenbergen-Hu & Cooper's college range
(0.32–0.37) onto Ma et al.'s ITS-versus-teacher-led figure (0.42), which is why the
table above prints 0.32–0.57 instead: that upper endpoint is Ma's comparison against
other computer-based instruction, a third comparator again. The spliced range stays
visible here because this survey published it. It does not get quoted again without
both of its sources.

Two readings of that coincidence are available and only one is licensed. **It does
not license 0.2–0.4 as a ceiling on a frontier system.** No study in the ITS or
human-tutoring meta-analyses had a frontier model in it, and every frontier trial
inside the band shares one design: a general-purpose assistant distributed into a
classroom, six to eight weeks, measured the week it stopped. That is a measurement
of a deployment pattern.

What it does license is the thing worth having. **The band is a floor**, and it
reproduces across four countries, three languages and three classes of technology.
A result that stable is something you can design against instead of hope for.

The frontier-era number sitting outside the band is Kestin's **d ≈ 0.63**, which is
also the row with the least independence and the shortest exposure: two hours, an
immediate ceiling-limited post-test, and a first author who built the tutor, ran the
analysis, and declared no funding (§03). It is evidence that an engineered frontier
tutor cleared an active control in two hours. It is not evidence about a term, and
this survey does not quote it as one.

---

## 2. Sierra Leone, read properly

The Sierra Leone trial is the best-designed study in the corpus and deserves to be
read at full resolution rather than through its headline. Two-arm cluster RCT,
classroom-level randomisation blocked by school × grade, 12 government junior
secondary schools, preregistered at AEA (AEARCTR-0016651). The design choice that
matters most: **both arms' teachers received the identical 5–6 hour training
before randomisation**, which removes the training confound that ruins most edtech
trials. Assessment was written and IRT-scored by Oxford MeasurEd, blind to arm.
Data collection, implementation and measurement sat in three separate
organisations.

That structure is the template. It should be the minimum bar the field asks of
anyone, including us.

Now the reanalysis, all of it from the report's own appendix tables:

| Finding | Value |
|---|---|
| Unadjusted ITT | **0.216 SD, SE 0.137 — not significant** |
| Baseline-adjusted (ANCOVA) | 0.258 SD, p = 0.029 |
| Treatment × baseline maths | **+0.195 SD per baseline SD, p = 0.002** |
| Grade 8 × treatment | **+0.429, p < 0.01** |
| Grade 7 main treatment coefficient | **−0.078, p < 0.05** |
| Treatment assignment predicting retention | +0.032, p < 0.05 (differential attrition) |
| Baseline imbalance | 0.167 SD favouring control |

Four things follow. **The headline exists only under covariate adjustment**, which
is a legitimate and preregistered choice made necessary by a real baseline
imbalance — but the raw arm difference is not distinguishable from zero, and the
adjusted CI's lower bound is 0.027. **The interaction is an order of magnitude more
statistically robust than the main effect**: at the fitted specification a student
one SD below the mean gains about 0.055 SD, which is nothing. **The effect is
essentially a Grade-8 effect**, with Grade 7's coefficient negative and significant
— a result that appears in no blog post about this trial. And the model changed
mid-trial, Gemini 2.5 Pro to 3.0 Pro at week six.

The credit here is substantial. DeepMind volunteered every one of those
numbers. The non-significant unadjusted estimate, the gap-widening interaction, the
mid-trial swap, the attrition flow, the preregistration deviation they did not
execute. That is more transparent than the norm. **The problem is not the report.
It is what happens to the report in the second-hand telling.**

Two further limits, both stated by the authors. The counterfactual is
business-as-usual, so +0.258 SD is the combined effect of tablets, a 2:1
driver/navigator pair protocol, a teacher-authored four-part lesson structure,
teacher-written starter prompts, chalkboard scaffolds, teacher professional
development, novelty, *and* Guided Learning's pedagogy. Their own playbook says
plainly that isolating arms would have required a sample they could not afford. And
because tablets were shared, **the 113,344 coded messages could not be linked to
any individual's test score**. The process metric (91.4% skill-seeking, 76.4%
scaffolding questions, 2.1% direct solutions) sits next to the outcome metric and
has never been shown to predict it.

---

## 3. The delayed unassisted test nobody ran

Here is the ERIC census, run 2026-07-27 against `api.ies.ed.gov/eric/`:

| Query | Records |
|---|---:|
| `"ChatGPT"` | 1,668 |
| `"ChatGPT" AND "learning outcomes"` | 95 |
| `"ChatGPT" AND "delayed post-test"` | **2** |
| `"ChatGPT" AND "retention test"` | **0** |
| `"ChatGPT" AND "transfer test"` | **0** |
| `"ChatGPT" AND "preregistered"` | **0** |
| *(control)* `"delayed post-test"`, any topic | **273** |

ERIC indexes abstracts only and lags preprints, so these are lower
bounds; the ratio is the quantity that matters, and the ratio is roughly 2% of
ChatGPT-plus-outcomes studies and 0.1% of all ChatGPT studies.

Why did nobody run one? The honest answers, in order of how often they appear in
the primary sources: partner schools grant access for a fixed window and reclaim it
(Bastani et al. say exactly this — "long-term outcomes … limitations imposed by our
partner school"); the intervention window and the publication window are the same
window; and a delayed test is the one measurement that can turn a positive paper
into a null one. None of these is a scientific reason. All of them are structural,
and all of them are fixable by whoever is willing to fund the fourth week.

What would such a test have shown? We have exactly one piece of evidence, and it is
the most important study in the corpus. **Bastani et al.** built AI-removal into the
design: four 90-minute sessions, assisted practice followed by a closed-book,
closed-laptop exam on conceptually matched problems.

| Outcome | GPT Base (unguarded) | GPT Tutor (guardrailed) |
|---|---|---|
| Assisted practice | +0.137 (SE 0.031) = **+48%** | +0.361 (SE 0.032) = **+127%** |
| Unassisted exam | **−0.054 (SE 0.022) = −17%, p < 0.05** (§01)| −0.004 (SE 0.013), n.s. |

Read the two columns against each other. The arm that performed **best** while
assisted is the arm whose unassisted coefficient is indistinguishable from zero.
The arm that performed second-best while assisted did *worse than students who
never had access at all*. GPT-4 gave correct answers on these problems 51% of the
time, and students used it as a crutch.

This survey has stated the consequence before and states it again without softening
it: **guardrails have been measured to remove harm, not to add benefit.** The
guardrailed coefficient is −0.004. Anyone selling restraint as a learning gain is
ahead of the evidence, including us.

A note on provenance, because the correction is on this project's record: the PNAS
notice attached to Bastani et al. is an affiliation erratum. It is not a correction
to the result. The −17% stands (§01).

---

## 4. Four results that never made a headline

Four nulls, none of which is in the headline of the paper that contains it.

Tutor CoPilot is the cleanest proximal/distal dissociation in the field. A
preregistered, independently funded RCT of 900 tutors, 1,800 Title I students and
4,136 sessions moved exit-ticket mastery by 4 percentage points (p < 0.01), 9 points
for students of the lowest-rated tutors. Verbatim from its limitations section:
"**we did not find statistically significant improvements in end-of-year math test
scores.**" The in-platform metric moved. The state test did not.

Lehmann, Cornelius & Sting is a preregistered, incentivised, replicated null.
Two lab experiments (107 and 69 subjects) plus a field study: "we find no effect of
LLMs on overall learning outcomes." Students who substituted LLM use for study
"increase the volume of topics they can learn about but decrease their
understanding of each topic," and the paper's body text is blunter than its
abstract: LLMs "harm the learning of students with less prior knowledge."

**Without a teacher in the loop, the meta-analytic effect is 0.077.** Gu & Yan
(2025, *JECR*, 19 studies) report g = 0.683 overall, decomposing to **g = 1.426
with teacher support and g = 0.077 without**. Every positive result in §1 that
survives scrutiny is a teacher-designed, teacher-supervised activity with an LLM as
one component. The measured entity is *teacher-plus-AI activity design*. **No study
in the corpus isolates the AI's contribution.**

And offering AI access reduced engagement. Nie et al. randomised GPT-4 access
across 5,831 students in 146 countries: "the advertisement of GPT-4 led to a
significant average decrease in exam participation." The positive effect for
adopters comes from selection and not from a randomised contrast, and peer review
made the authors retitle the paper to say so.

To that add the field's largest single correction. **The most-cited meta-analytic
estimate of ChatGPT's effect on learning, g = 0.867 across 51 studies, was retracted
in 2026** for "discrepancies in the meta-analysis"; the authors did not respond to
correspondence. It had accumulated over 250 citations. Anything downstream of
g = 0.867 is unsupported, and still circulating.

A smaller correction worth internalising as a habit: Nickow et al.'s human-tutoring
pooled estimate **fell from 0.37 SD in the 2020 working paper to 0.288 SD in the
2024 peer-reviewed version.** Discount every working-paper effect size accordingly,
including the ones in the table above.

---

## 5. What LearnLM measured, precisely

LearnLM deserves separate treatment because it is the most serious attempt anyone
has made to render pedagogy measurable, and because its famous numbers measure
something other than learning.

The programme's flagship evaluations (the "+31% over GPT-4o", the "73.2% overall
win rate") score pedagogical plausibility. The dependent variable
is a third-party expert's agreement with a statement about a transcript. Google
says so themselves, in R2's conclusion: "it is unclear how well the results
translate to improvements in learning outcomes." R3 asks the question outright: "do
these pedagogical capabilities translate to concretely better learning outcomes for
students?"

Two findings inside that programme are more useful than the win rates.

The rubric's reliability was reported once. R1 published Krippendorff's α per
dimension: overall **0.359**, and on three of nine tutoring moves
(*inspires interest* **0.066**, *monitors motivation* **0.023**, *identifies goal*
**0.031**), credentialed pedagogy experts agreed with each other at approximately
chance. Two of LearnLM's five principles rest substantially on constructs raters
cannot reliably identify in a transcript. R2 and R3 report no inter-rater statistic
at all. Publishing that α was the right thing to do; stopping was not.

And the learners disagreed with the experts. Twice, in two reports. The people
role-playing the conversation "indicated no substantial preference between LearnLM
and Gemini 1.5 Pro or between LearnLM and Claude 3.5 Sonnet." In R3, educators
interacting directly scored Gemini 2.5 Pro and ChatGPT-4o as tied; only the
independent transcript reviewers separated them. Google's reading is right — "what
students find immediately helpful often diverges from what is pedagogically sound,"
captured perfectly by one educator: **"As a lazy student, I'd have loved it. As a
tutor, not good at all!"** The reading a builder must also hold is that the win was
scored by the population that shares the rubric's theory, and the rubric has never
been validated against an outcome.

---

## 6. Three years against fifty

*You are holding a three-year-old technology to a standard the tutoring literature
took fifty years to meet. Effects in the 0.2–0.4 band, replicated across four
countries, on a technology that did not exist in 2022, is a remarkable starting
position — and the retention evidence will arrive.*

Most of that is correct, which is why this section leads with the band and not with
the gaps. But two things break the defence.

First, the instrument is not expensive or novel. Two hundred and seventy-three
ERIC records use it. It is four weeks of patience and a fresh item set — and item
generation is now the cheapest thing in the system. The field is not failing to
measure retention because retention is hard to measure.

Second, **the pre-LLM literature did meet the standard, which makes it the place the
design template lives.** Those trials are not the bar a frontier system has to come
in under. They are the shape of a study that could tell you where it came in.
Roschelle et al.'s ASSISTments trial moved an end-of-year state
standardised test across 43 Maine schools, with the largest gains for low prior
achievers. It is the strongest distal-outcome edtech RCT in the corpus, and it
predates the LLMs entirely. Pane et al. ran Cognitive Tutor Algebra I across 147
schools for two years and found a null in year one that became +0.21 SD in year two.
Neither shape is visible in an eight-week trial, and every LLM RCT here except Rori is
eight weeks or shorter.

---

## 7. How we will report an effect size

- **Quote every number with its class and its year.** The 0.2–0.4 band is what
  six-to-eight-week classroom deployments of general-purpose assistants measured; it
  happens to coincide with pre-LLM ITS and with human tutoring, and a reader is owed
  which of the three is being invoked. Never cite g = 0.867; it is retracted. Never
  cite Bastani's +127%; it is a practice-session number.
- **Never bound one class of system with a measurement of another.** VanLehn 2011
  measured rule-based ITS against human tutors. Nickow pools 96 randomised trials of
  human tutors. Bloom 1984 measured human tutors on their own aligned tests, and is
  retired here (§24). Each is the right benchmark for the machine it measured and
  evidence about no other.
- **Give a synthesis year when that is all we have.** The corpus establishes when
  Bloom, VanLehn, Ma, Steenbergen-Hu and Nickow were *published* and never when their
  constituent trials were *run*. Write "the 2011 review" and never "the 1980s
  studies", which would be a span nobody has established.
- **Every claim we make gets a delayed, unassisted, novel-item test**, or it is
  reported as a performance result and labelled as one.
- **Report the unadjusted estimate next to the adjusted one.** Sierra Leone's
  0.216 (n.s.) belongs beside its 0.258 every time.
- **Treat gap-widening as the default expectation *for untargeted delivery*.**
  Three studies, three countries, three age groups, three tools, same direction:
  +0.195 SD per baseline SD, +0.151, and Lehmann's low-prior-knowledge harm. But it
  is not a law of the technology: across **eight targeted interventions examined in
  §07, none widened gaps and several sharply narrowed them.** Gap-widening is a
  property of *distribution without targeting*, which makes it a design failure we
  know how to avoid rather than a tax we must accept. Any trial we run stratifies on
  baseline attainment and powers the bottom stratum as a primary outcome.
- **Assume the teacher is the active ingredient until a factorial design says
  otherwise.** g = 0.077 without one.
- **Report inter-rater reliability every time, for every dimension.** If α on a
  rubric item is 0.066, that item is not measuring anything.
- **Link process to outcome or do not claim the process.** 91.4% skill-seeking is a
  number about conversations until someone regresses it on a test score.

The field's headline number was retracted, its best trial cannot isolate its own
intervention, and its most rigorous result is a harm. Read as a specification for
what to measure, that record is unusually clear, and it points at one cheap
unclaimed result: **a one-month delayed test on students who have already been
randomised.**

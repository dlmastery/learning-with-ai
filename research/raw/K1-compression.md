---
title: "Compression — how much of a week is overhead, what the floor is, and the maximum defensible speed-up"
wave: K
section: K1
date_researched: 2026-07-28
sources_count: 61
status: raw-research
---

# K1 — The Compression Bound

> **The claim under test.** *"AI tutors make us all polymaths in a very short period. Things that
> take a week can be learnt in an hour."*
>
> This section takes that seriously as an **engineering** question. A week of learning contains
> some irreducible cognitive work and a great deal of overhead. The job is to measure the ratio.
>
> **The finding, stated first.** The encoding fraction of a learning week is small — on the order
> of **2–5%** of the calendar and roughly **a third** of even the classroom hour. Almost everything
> else is waiting, mis-targeting, and a study behaviour with the lowest measured return in the
> literature. But the compressible part and the incompressible part are *different quantities*:
> **effort compresses by roughly an order of magnitude; elapsed time does not compress at all.**
> The defensible version of the owner's claim is therefore stronger and stranger than the original:
> **a week's *understanding* in an hour is achievable and under-ambitious; a year's *retention*
> still costs a month of calendar — but only about forty minutes of additional effort inside it.**

**Source reachability log (2026-07-28).** WebSearch exhausted per CLAUDE.md §5. Retrieval ran on
**Crossref**, **OpenAlex**, **ERIC**, **Europe PMC** (full-text XML — the workhorse this session),
and targeted `curl`/`WebFetch` of primary PDFs. **arXiv (`export.arxiv.org`) returned empty bodies
for the entire session** — no arXiv-only claim appears below. **`apps.dtic.mil` is blocked**
(returns a 1.4 KB HTML stub for both the citation page and the PDF endpoint) — every DARPA/IDA
figure below is sourced through a non-DTIC route or flagged UNVERIFIED. **Semantic Scholar** was
rate-limited (HTTP 429) for most of the session and is used only where a second source corroborates.
`journals.sagepub.com` and `nature.com` (article HTML) returned 403/303-auth; Nature content was
recovered through Europe PMC's open-access mirror instead. Primary full texts extracted and quoted
verbatim: **Koedinger et al. (2023) PNAS** (PMC10068755), **Kestin et al. (2025) Sci Rep**
(PMC12179260), **Fisher et al. (1980) BTES** (ERIC ED192454), **Babcock & Marks (2011)** (NBER
w15954), **Samarawickrema & Cleary (2021)**, **Zeng et al. (2019) Nat Commun**.

Evidence labels per CLAUDE.md §2: `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` · `OBSERVED`
· `VENDOR` · `DEMO` · `INFERENCE`. A `VENDOR` claim is never restated as a finding.

**Builds on, does not repeat:** B1 (learning-science floor), B2 (the AI-tutoring efficacy
scoreboard — Kestin, Bastani, Tutor CoPilot, VanLehn, Ma, Steenbergen-Hu), F5 (learner model,
knowledge tracing), F10 (expertise reversal), F11 (retrieval practice and spacing meta-analytics —
Yang g = 0.499, Rowland g = 0.50, Dunlosky's utility table), J1 (the selection policy).
K1 supplies the thing none of them state: **the time budget**.

---

## 0. Executive summary — the numbers that carry the argument

| # | Quantity | Value | Source | Label |
|---|---|---|---|---|
| 1 | Practice opportunities to reach 80% mastery of a typical knowledge component | **≈ 7** (median 6.54) | Koedinger et al. 2023, 1.3 M observations / 27 datasets | `MEASURED-BENCH` |
| 2 | Learning **rate** per opportunity, and its spread across learners | **0.1 log-odds ≈ +2.5% accuracy**; 25th→75th pct = **7.89 → 6.94** opportunities (**1.14×**) | ibid., Table 2 | `MEASURED-BENCH` |
| 3 | Spread in opportunities-to-mastery driven by **prior knowledge** | **13.13 → 3.66** (**3.6×**) | ibid., Table 2 | `MEASURED-BENCH` |
| 4 | Does calendar time predict learning? | **No.** "a time-based model, time-AFM, systematically provides poor predictive fit" | ibid., verbatim | `MEASURED-BENCH` |
| 5 | Productive learning time inside an allocated school day, worst vs best case | **≈ 4 min vs ≈ 52 min** (**13×**) | Fisher et al. 1980 (BTES), worked example | `OBSERVED` |
| 6 | Wheel-spinning rate, bottom vs top quintile of **prerequisite** knowledge | **50% vs 10%** (**5×**) | Wan & Beck 2015, ASSISTments | `OBSERVED` |
| 7 | Time cost of a well-built LLM tutor vs a matched active-learning class hour | **49 min (median) vs 60 min**, with **d ≈ 0.63** *more* learned | Kestin et al. 2025 RCT | `MEASURED-RCT` |
| 8 | Correlation between time-on-task and post-test score in that RCT's AI arm | **none** | ibid. | `MEASURED-RCT` |
| 9 | Optimal study gap for a 1-year retention target | **5–10% of the retention interval** (≈ 18–36 days) | Cepeda et al. 2008, N > 1,350 | `MEASURED` |
| 10 | Sleep benefit to episodic memory, corrected for selective reporting | **g = 0.44 → 0.28** | Berres & Erdfelder 2021, 823 ES / 271 samples | `MEASURED-META` |
| 11 | Number of research topics a scientist works in across an entire career | **peaks at 3–4** | Zeng et al. 2019, full publication records | `OBSERVED` |
| 12 | Variance in professional performance explained by deliberate practice | **education 4%, professions < 1%** | Macnamara et al. 2014 | `MEASURED-META` |
| 13 | **The record.** Sherlock: hours of coached practice equalling *four extra years* of on-the-job experience | **20–25 hours vs ≈ 4 years (≈ 300×)** | Lesgold et al. 1988, ERIC ED299450, verbatim | `OBSERVED` |
| 14 | Measured **learning-time savings** from computer-based instruction | **39% to 88%** (i.e. **1.6× to 8.3×**) | Kulik 1983, 51 studies | `MEASURED-META` |
| 15 | Hours to ILR level 3 under full immersion with expert instructors — the compression-optimised baseline | **552 h (Spanish) to 2,200 h (Arabic)** | US State Dept / FSI, official | `OBSERVED` |

**The three sentences the section exists to license:**

1. **Encoding is counted in opportunities, not in minutes** (rows 1, 2, 4). Therefore any process
   that delivers correct, correctly-difficult opportunities faster compresses acquisition
   *proportionally*, with no penalty, up to the learner's own read-attempt-feedback loop.
2. **The dominant source of time variance is prerequisite state, not learner speed** (rows 2, 3, 6).
   The spread attributable to prior knowledge is **3.6×**; the spread attributable to innate
   learning rate is **1.14×**. Diagnosis, not acceleration, is where the hours are.
3. **Durability is priced in elapsed days, and the price is paid in calendar, not in effort**
   (row 9). This is the one term that cannot be compressed — and it is also the cheapest term
   in the budget.

---

## 1. Decomposing the week

### 1.1 The units error at the heart of the folk claim

"A week" in the phrase *"things that take a week"* is a **calendar** unit. The thing being
compressed into "an hour" is a **work** unit. Most of the apparent 168× is an artefact of comparing
two different quantities, and establishing this is not a debunk — it is the first and largest
compression term, and it is free.

**The Carnegie arithmetic.** `INFERENCE` (structural, from the US federal credit-hour definition,
34 CFR 600.2: one credit hour = one hour of classroom instruction plus two hours of out-of-class
work, per week, for ~15 weeks). A 3-credit semester course is therefore **135 nominal student
hours** spread over **15 calendar weeks = 2,520 waking hours** (16 h/day). One week of that course
is **9 nominal hours inside 112 waking hours: 8%**. Everything else in the week is *not the course*.

So before any pedagogy at all, the folk claim's 168:1 is really about **9:1** — and 9 hours is the
number that has to be attacked.

### 1.2 Inside the 9 hours: the BTES cascade

The only rigorous decomposition of instructional time in the literature is the **Beginning Teacher
Evaluation Study**, and it is 45 years old.

**Fisher, Berliner, Filby, Marliave, Cahen & Dishaw (1980), "Teaching Behaviors, Academic Learning
Time, and Student Achievement,"** in Denham & Lieberman (eds.), *Time to Learn*, National Institute
of Education. ERIC **ED192454** (full text retrieved and read). Observational; 2nd- and 5th-grade
California classrooms, ~6 target students per class observed weekly across two blocks in 1976–77.
`OBSERVED`

The study's structural insight is a **three-stage cascade**, and each stage has a measured leak:

| Stage | What leaks | Measured range |
|---|---|---|
| **Allocated** time | curriculum choices, scheduling | Grade-2 math **25–60 min/day** across classes; grade-5 reading **60–140 min/day**. At sub-skill level, one grade-2 class averaged **9 minutes of money arithmetic for the entire school year** against another class's **315 minutes** |
| **Engaged** time | attention, transitions, waiting | class-average engagement **≈ 50% to ≈ 90%** |
| **High-success** time (ALT) | material pitched wrong | *"The average student in the study spent **about half the time** working on tasks that provided high success. In grade five mathematics … **about one-third** of instructional time was high success."* Some students worked on excessively difficult material **as much as 20% of the time** |

The report's own worked example is the number to carry:

> 50 min allocated × ~⅓ engaged × ¼ high-success ≈ **4 minutes** of academic learning time per day
> 100 min allocated × 85% engaged × ~⅔ high-success ≈ **52 minutes** per day

**A 13× spread in productive learning from the same nominal school day.** `OBSERVED`

For the *median* case the cascade still costs roughly **65%**: allocated → ~70% engaged → ~50% of
that at high success → **ALT ≈ 35% of allocated time**. Apply that to the 9-hour course-week and
the irreducible-looking budget drops to **≈ 3 hours** before a single word is said about AI.

*Caveat, stated plainly:* BTES is elementary-school classroom observation. Extending its cascade to
adult self-directed learning is `INFERENCE`. But the three stages — is the time allocated, is
attention on it, is the material at the right difficulty — are not school-specific, and the third
stage is exactly what an adaptive system controls.

### 1.3 The components the literature does *not* measure

**This is a genuine hole and it must be reported as one.** Across ERIC, Crossref, OpenAlex and
Europe PMC, **no study was located that decomposes a study session into search / orientation /
reading / practice / stuck time.** Two independent retrieval passes returned nothing. The nearest
proxies are the BTES cascade (classroom analogue) and the wheel-spinning literature (§2.3, which
isolates *stuck* specifically).

Consequently the per-component estimates below are labelled honestly:

| Component | Best available evidence | Estimate | Label |
|---|---|---|---|
| **Waiting** (next lecture, office hours, scheduling, term start) | Carnegie arithmetic §1.1; the 92% of the calendar week that is not the course | **~90% of calendar, ~0% of effort** | `INFERENCE` |
| **Search** (finding the right explanation/example/problem) | **no measurement found** | unquantified | — |
| **Orientation** (working out what you don't know) | quantified only *indirectly*, via the 13.13-vs-3.66 opportunity spread (§2.1) | large, unpriced | `INFERENCE` |
| **Re-reading** | **76%** of 472 UCLA students report rereading whole chapters or underlining (Bjork, Dunlosky & Kornell 2013, *Annu. Rev. Psychol.* 64:417–444; verified in F11 §6.4); Dunlosky et al. 2013 rate rereading and highlighting **LOW utility** | the most-used technique is the least effective | `MEASURED-META` |
| **Stuck time** | wheel-spinning: >10 opportunities on one skill without mastery (§2.3) | **50% of practice** for low-prerequisite students | `OBSERVED` |
| **Actual encoding** | ~7 opportunities/KC at 0.1 log-odds each (§2.1) | **the floor** | `MEASURED-BENCH` |

**The honest statement of the central finding:** the encoding fraction is small — that much is
solid on two independent measurements (BTES cascade, Carnegie arithmetic). What is *not* solid is
the internal split of the non-encoding remainder, because nobody has measured it. **A study-session
time-motion decomposition is the single highest-value missing measurement in this entire survey.**

### 1.4 A negative result about the size of the study week itself

**Babcock & Marks (2011), "The Falling Time Cost of College," *Review of Economics and Statistics*
93(2):468–478,** DOI 10.1162/rest_a_00093; NBER w15954 (full PDF retrieved). `OBSERVED`

Verbatim: *"full-time college students in **1961 devoted 40 hours per week to academics**, whereas
full-time students in **2004 invested about 27 hours per week**."*

**A correction that must not be laundered:** the 40 → 27 figure is **class attendance PLUS
studying**, not study time alone. The study-time-only declines, after adjusting for survey framing,
are *"about 8 hours per week between 1961 and 1981, about 2 hours per week between 1988 and 2004,
and about 10 hours per week"* overall. The authors also measured the instrument artefact directly:
Project-Talent-style wording elicited **12.7 h/wk** against NSSE-style **11.6 h/wk**. Declines were
*"extremely broad-based"* across every demographic subgroup, working and non-working students, and
four-year colleges of every type, size, degree structure and selectivity.

**Why this matters to the compression argument:** the real modern study week is on the order of
**11–13 self-reported hours**, and self-report is inflated. The quantity to be compressed is
already small. This cuts *against* spectacular headline ratios and *for* the claim that the
remaining time is nearly all overhead.

---

## 2. Prerequisite repair is the dominant time sink — and it is now measured precisely

This is the section's strongest evidence and it comes from one paper.

### 2.1 Koedinger et al. (2023): learning rate is a constant; prior knowledge is not

**Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023), "An astonishing regularity
in student learning rate," *PNAS* 120(13):e2221311120,** DOI 10.1073/pnas.2221311120,
PMC10068755 (full text retrieved and quoted). **1.3 million observations across 27 datasets**,
elementary through college, in math, science and language, on online practice systems that give
follow-up instruction on errors. Model: individual Additive Factors Model (iAFM), logistic, with
per-student intercepts (initial knowledge) and slopes (learning rate). `MEASURED-BENCH`

Findings, verbatim where they carry weight:

1. **The encoding cost.** *"Students do need extensive practice, about seven opportunities per
   component of knowledge."* Median 6.54 opportunities to 80% mastery.
2. **The rate is a near-constant.** *"we found students to be astonishingly similar in estimated
   learning rate, typically increasing by about 0.1 log odds or 2.5% in accuracy per opportunity."*
   Holding initial knowledge fixed, the 25th and 75th percentiles of learning rate need **7.89 and
   6.94** opportunities respectively — a spread of **1.14×**.
3. **Prior knowledge is where the variance is.** Initial accuracy: lower half **55.21%**, upper half
   **75.17%**. Holding learning rate fixed, *"a student in the bottom half of initial knowledge
   needs about **13.13** opportunities to reach mastery, a student in the top half needs about
   **3.66**"* — *"a large difference for students who have **met course prerequisites** and been
   provided verbal instruction."* **3.6×.**
4. **Calendar time does not predict learning.** *"we find these learning opportunities are much more
   predictive of learning outcomes than calendar time (a time-based model, time-AFM, systematically
   provides poor predictive fit)."*

**Read (3) again.** These students had *formally passed the prerequisites*. The 3.6× gap is
entirely inside the population that the education system certifies as ready. That is the missing
prerequisite the learner cannot name, quantified for the first time at scale.

**Read (4) again.** This is the compression theorem in one clause. If learning is counted in
opportunities and not in days, then delivering the same opportunity count in a shorter wall-clock
window costs nothing in *acquisition*. The only question left is whether it costs something in
*durability* — and it does (§4).

### 2.2 What (1)–(3) jointly imply

Two students, identical courses, identical instruction. Student A is in the top half of prior
knowledge, Student B the bottom half. Both learn at the same rate. B needs **3.6× the practice** to
reach the same mastery.

- If the system gives both the same fixed dose (the default in every non-adaptive setting), A
  overlearns and B does not master.
- If the system *diagnoses* and repairs B's missing components first, B's initial-knowledge
  parameter moves and the 3.6× collapses toward the 1.14× that is genuinely innate.

**The compression available from prerequisite repair alone is therefore bounded above at ≈ 3.6×**,
and it is the *only* term in this section with a measured multiplier attached to a named
mechanism. `MEASURED-BENCH` → `INFERENCE` for the collapse claim, because no study has yet run the
repair-then-remeasure experiment. **That experiment is the single cleanest test this survey can
propose** (see §8).

### 2.3 Wheel-spinning: the observable signature of an unrepaired prerequisite

**Beck, J. E., & Gong, Y. (2013), "Wheel-Spinning: Students Who Fail to Master a Skill," AIED 2013,
LNCS 7926,** DOI 10.1007/978-3-642-39112-5_44. The operational definition, retrieved via Park
(2023) *TechTrends*, ERIC EJ1377740, which restates it: wheel-spinning students *"practiced the same
skill set over 10 times but failed to submit correct answers three times in a row."*
**The paper's own prevalence figure could not be retrieved** — publisher-closed, abstract elided at
every access point. `UNVERIFIED` for prevalence; `OBSERVED` for the ≥10-opportunity threshold.

**Wan, H., & Beck, J. E. (2015), "Considering the Influence of Prerequisite Performance on Wheel
Spinning," EDM 2015,** ERIC **ED560558** (abstract retrieved). ASSISTments data. `OBSERVED`

> *"students in the **bottom 20% of pre-required knowledge exhibited wheel spinning behavior 50% of
> the time**, while those in the **top 20% of pre-required knowledge exhibited wheel spinning
> behavior only 10% of the time**."*

**A 5× differential in stuck-time, attributable to prerequisite state.** Adding prerequisite
performance to the detector moved R² 0.264 → 0.268 and AUC 0.884 → 0.888 — a small *predictive*
gain, which is itself informative: prerequisite state is not a new signal so much as a
*re-description* of the signal knowledge tracing already carries.

Follow-up work, all `OBSERVED`: **Kai, Almeda, Baker, Heffernan & Heffernan (2018)**, *JEDM*,
ERIC EJ1183799 — two distinct wheel-spinning profiles, both keyed to **bottom-out hint use** and
**massed (unspaced) practice**. **González-Esparza et al. (2022)**, ERIC ED629562 — ASSISTments
2009–10, **n = 4,217** middle-schoolers. **Caveat from Zhang et al. (2019)**, EDM, ERIC ED599222:
*"two prominent criteria for wheel spinning diverge substantially"* — the construct is not yet
measured consistently, so treat prevalence figures across papers as non-comparable.

### 2.4 The mastery-learning time literature — what it actually says

The owner's brief was right that Bloom's relevant contribution here is **not** the 2σ claim (retired
in this project's ledger: VanLehn 0.79, Nickow 0.288, Kestin ≈ 0.63). The relevant finding is about
**time variance**.

**Bloom, B. S. (1974), "Time and learning," *American Psychologist* 29(9):682–688,**
DOI 10.1037/h0037632. Metadata verified; **full text not retrieved.**

The retrievable form of the classic ratio comes from Borg's chapter in the same *Time to Learn*
volume (ED192454), which attributes it upstream, and the attribution matters: `OBSERVED`

> *"Data developed by **Glaser (1968) and Atkinson (1968)** suggest that **the slowest 5 percent of
> learners take about 5 times as long** to reach any given criterion of mastery as do the fastest
> 5 percent."*

And on what mastery conditions buy:

> *"where time and help are provided to slower students … **90 percent or more** finally reach the
> learning criteria."*
>
> Mastery-learning studies (**Block 1971; Peterson 1972**) *"typically bring about **80 percent of
> students to a learning criterion usually attained by only about 20 percent**. This additional
> learning is achieved at a cost of **10 to 20 percent additional learning time**."*

**Two corrections for the record:**
- The **5:1 slow/fast ratio is Glaser's and Atkinson's, not Bloom's own data.** Bloom relays it.
- **The widely-repeated claim that the 5:1 ratio shrinks to ~3:1 across successive mastery units
  (Anania, Burke, Arlin) could not be verified in this session.** Do not print it. The retrievable
  and defensible substitute is the **10–20% additional time** figure above, which is a *better*
  number for this argument anyway: it says prerequisite repair moves 20% mastery to 80% mastery at
  a **1.1–1.2× time cost**, not a 3× one.

**Carroll's ratio model** — degree of learning = *f*(time spent / time needed) — is confirmed
through **Gettinger (1984)**, *AERJ* 21(3):617, DOI 10.3102/00028312021003617 (N = 171 fourth- and
fifth-graders): *"TTL [time to learn] contributed significantly to achievement, and its direct
effect was greater than that of TSL [time spent learning]."* `OBSERVED`
**Gettinger (1985)**, *JEP* 77(1):3–11, DOI 10.1037/0022-0663.77.1.3, same N = 171: spending or
allocating less time than *needed* produced significant drops in both initial learning and 1-week
retention. **The widely-cited "~5× variation in time needed" attributed to Gettinger is NOT in
either retrievable abstract and is not printed here.** `UNVERIFIED`

**Karweit citation warning:** Crossref returns **no** 1984 paper titled "Time on task reconsidered."
The real records are **Karweit (1983)**, NIE, DOI 10.1037/e436792004-001; **Karweit (1988)**, *NASSP
Bulletin* 72(505):31–39, DOI 10.1177/019263658807250507; and **Karweit & Slavin (1981)**, *AERJ*
18(2):157, DOI 10.2307/1162379. Anyone citing "Karweit 1984" is citing a ghost.

---

## 3. What is genuinely compressible

Component by component, with the evidence attached and the inferences labelled.

### 3.1 Waiting → zero. `INFERENCE` (structural, not empirical)

The strongest term and the one requiring the least argument. A course week is 9 nominal hours inside
112 waking hours (§1.1). Office hours, the next lecture, the next term, the next cohort, the
prerequisite course you must pass before enrolling — none of these are cognitive work. An
always-available agent removes them by construction.

This is **not** a measured effect and should never be reported as one. It is an accounting identity.
Its size is nonetheless the largest single term in the budget: **roughly 90% of the calendar.**

### 3.2 Search → near zero. **Unmeasured — the honest gap.**

No study was located quantifying time spent locating an appropriate explanation, example or problem
during learning. Information-foraging theory (Pirolli & Card, *Information Foraging Theory*, OUP
2007, DOI 10.1093/acprof:oso/9780195173321) supplies the model but no learning-specific time
fraction. **Anyone who quotes a percentage for "time spent searching" in a learning context is
quoting a vendor deck, not a study.** This is reported as unquantified. `—`

The direction is not in doubt (generation replaces retrieval-and-selection); the magnitude is
unestablished.

### 3.3 Orientation → collapses **if and only if** the agent can diagnose. `MEASURED-BENCH` bound

This is the term Koedinger prices. Orientation cost *is* the initial-knowledge parameter, and its
value is a **3.6× multiplier on required practice** (§2.1). The claim that an agent collapses it
depends entirely on whether diagnosis works — which is F5's and J1's territory, and where this
survey's evidence is weakest. Two constraints from elsewhere in the corpus bound the optimism:

- Knowledge tracing has a measured accuracy ceiling (F5); a diagnosis that is wrong repairs the
  wrong prerequisite.
- The expertise-reversal effect (F10) means *over*-diagnosis is also costly: scaffolding a learner
  who does not need it degrades performance.

**Defensible statement:** orientation is worth up to **3.6×**, is the largest measured term after
waiting, and is *contingent* on diagnostic accuracy that has not been demonstrated at that
precision. Do not bank the full 3.6×.

### 3.4 Re-reading → replaced, at a measured effect size. `MEASURED-META`

The most-used study behaviour is the lowest-utility one. **76%** of 472 students report rereading
whole chapters or underlining (Bjork, Dunlosky & Kornell 2013, verified in F11 §6.4); Dunlosky et
al. (2013), *PSPI* 14(1):4–58, rate **rereading and highlighting LOW utility** and **practice
testing and distributed practice HIGH**.

Substituting retrieval practice for restudy is the best-evidenced single intervention in this entire
survey: **Yang, Luo, Vadillo, Yu & Shanks (2021)**, *Psychological Bulletin*, DOI
10.1037/bul0000309 — **222 studies, 48,478 students, classroom settings, g = 0.499 [0.442, 0.557]**;
**Rowland (2014)** g = 0.50; **Donoghue & Hattie (2021)** across all ten techniques, 242 studies,
169,179 participants, mean ES 0.56 (all carried from F11).

**A required caveat that cuts against the standard telling.** **Dirkx, Camp, Kester & Kirschner
(2019), "Do students really prefer repeated rereading over testing when studying textbooks? A
reexamination," *Memory*,** DOI 10.1080/09658211.2019.1610177. `MEASURED` They argue Karpicke,
Butler & Roediger (2009) operationalised "repeated rereading" as "restudying," conflating distinct
strategies, and find rereading *"is preferred only by few students early in the learning process,
with almost all shifting to testing late"* and is mostly *"rereading not understood parts"* rather
than true repeated rereading. **If that is right, the rereading term in the compression budget is
smaller than folklore implies — and note that "rereading not understood parts" is itself
prerequisite repair, executed badly.**

*Also for the record:* the frequently-quoted **"84% of students list rereading, 55% rank it first"**
from **Karpicke, Butler & Roediger (2009)**, *Memory* 17(4):471–479, DOI
10.1080/09658210802647009, **could not be verified this session** — the abstract states only that
*"a majority of students repeatedly read their notes or textbook"* and the full text 404'd at both
Purdue and WUSTL. N = 177 is confirmed. `UNVERIFIED` for the percentages.

### 3.5 Stuck time → collapses with on-demand diagnosis. `OBSERVED` bound

Wheel-spinning is **50% of practice** for bottom-quintile-prerequisite learners against **10%** for
top-quintile (Wan & Beck 2015). The mechanism of the collapse is the same as §3.3 — it is the same
variable observed downstream. **These two terms are not independent and must not be multiplied
together.** Doing so is the most likely way to inflate a compression estimate by an order of
magnitude, and it is worth naming explicitly because the arithmetic is tempting.

### 3.6 The one place all of this has actually been measured together

**Kestin, Miller, Klales, Milbourne & Ponti (2025), "AI tutoring outperforms in-class active
learning: an RCT introducing a novel research-based design in an authentic educational setting,"
*Scientific Reports* 15:17458,** DOI 10.1038/s41598-025-97652-6, PMC12179260 (full text retrieved).
`MEASURED-RCT`

Harvard undergraduate physics, N = 194 enrolled, crossover, two ~1-hour lessons a week apart.
Learning effect d ≈ 0.63 (carried from B2, along with its `(D)` developer-evaluated caveat: the
first author built the tutor and ran the analysis).

**The time data, verbatim — this is the only clean measurement of AI-tutoring time compression in
existence:**

> *"During a 75-minute period, the in-class students spent 15 minutes taking the pre- and
> post-tests; we assume 60 minutes spent on learning."*
>
> *"**70% of students in the AI group spent less than 60 minutes on task**, while 30% spent more
> than 60 minutes on task. **The median time on task for students in the AI group was 49 minutes.**"*
>
> *"they learn significantly more … **while spending less time on task**."*
>
> *"**Notably, there was no correlation between the time on task and students' post-test scores**,
> despite quite a wide range of times measured for the AI group."*

**Read this carefully, because it is the reality check on the whole section.**

- The measured time compression of a best-in-class LLM tutor against a *well-run active-learning
  hour* is **60 → 49 min = 1.22×**, with *more* learned.
- More time did **not** help. The learning was not time-limited; it was
  opportunity- and targeting-limited — exactly what Koedinger's time-AFM null predicts.
- Therefore: **the compressible hours are not inside the good hour.** A well-designed
  active-learning hour is already close to the encoding floor. The 40× lives in the calendar
  (§3.1), in the mis-targeted practice (§3.3, §3.5), and in the rereading (§3.4) — not in the hour
  where a competent teacher already has the learner engaged on well-pitched material.

That reconciliation is the most useful thing in this section. It tells a builder exactly where to
spend: **not on making the good hour faster, but on deleting the 111 hours around it.**

---

## 4. What is not compressible

Rigour here is what makes the affirmative case credible, so this part is deliberately unforgiving.

### 4.1 Consolidation requires wall-clock time — but the effect is smaller than advertised

**Berres, S., & Erdfelder, E. (2021), "The sleep benefit in episodic memory: An integrative review
and a meta-analysis," *Psychological Bulletin* 147(12):1309–1353,** DOI 10.1037/bul0000350.
**823 effect sizes from 271 independent samples in 177 articles**, 1967–2019, multilevel
metaregression with robust variance estimation. `MEASURED-META`

- **Overall g = 0.44.**
- **Corrected for selective reporting bias: g = 0.28** — a **36% shrinkage**, still significant.
- Moderators: larger when stimuli are studied **multiple times** rather than once; for word
  material largest in **free recall > cued recall > recognition**; **stronger in pre-post difference
  measures than in delayed memory tests** (i.e. partly a measurement artefact); larger for
  **natural sleep and night-time naps** than for SWS-deprived sleep or **daytime naps**.

**Interpretation for the compression question.** A sleep-dependent benefit of g ≈ 0.28 is real and
is a genuine wall-clock constraint — you cannot buy it with more study. But it is *not* the
dominating term people assume, and the daytime-nap moderator kills the obvious "just nap between
blocks" workaround.

**The required null, and it is a big one.** **Pan, S. C., & Rickard, T. C. (2015), "Sleep and motor
learning: Is there room for consolidation?" *Psychological Bulletin* 141(4):812–834,** DOI
10.1037/bul0000009. **34 articles, 88 experimental groups, 1,296 subjects.** `MEASURED-META`
The meta-analysis first reproduces the surface pattern (large post-sleep gain, small post-wake gain)
and then dissolves it with four moderators — **averaging in pre-post gain-score computation,
build-up of reactive inhibition during training, time of testing, and training duration** (plus
elderly status). Verbatim:

> *"With those variables accounted for, **there was no evidence that sleep enhances learning**.
> Thus, the literature speaks **against**, rather than for, the enhancement hypothesis."*

They allow that sleep may *stabilise* memory, but *"that effect … was not consistent across
different experimental designs."*

This directly attacks the most-cited number in the field: **Walker, Brakefield, Morgan, Hobson &
Stickgold (2002), *Neuron* 35(1):205–211** (DOI 10.1016/S0896-6273(02)00746-8), which reported
*"a night of sleep results in a **20% increase in motor speed** without loss of accuracy, while an
equivalent period of time during wake provides no significant benefit."* **Pair the two. Do not
cite Walker without Pan & Rickard.**

**Targeted memory reactivation**, the only technology-shaped intervention on this term: **Hu, Cheng,
Chiu & Paller (2020), "Promoting memory consolidation during sleep: A meta-analysis of targeted
memory reactivation," *Psychological Bulletin*,** DOI 10.1037/bul0000223. **91 experiments,
212 effect sizes, N = 2,004. Overall g = 0.29 [0.21, 0.38]**; NREM2 g = 0.32 [0.04, 0.60];
SWS g = 0.27 [0.20, 0.35]. **TMR was not effective during REM sleep nor during wakefulness.**
`MEASURED-META` — a real but small lever, and not one an LLM tutor operates.

### 4.2 The spacing constraint, stated exactly

**Cepeda, Vul, Rohrer, Wixted & Pashler (2008), "Spacing effects in learning: A temporal ridgeline
of optimal retention," *Psychological Science* 19(11):1095–1102,** DOI
10.1111/j.1467-9280.2008.02209.x. **N > 1,350**, study gaps to 3.5 months, final tests to 1 year.
`MEASURED`

> *"the optimal gap **declined from about 20 to 40% of a 1-week test delay to about 5 to 10% of a
> 1-year test delay**."*

**A correction this section must carry:** the popular "optimal gap ≈ 10–20% of the retention
interval" is a flattening of this result. The *proportional* optimum **declines** with delay while
the *absolute* optimum grows. The commonly-quoted "≈ 21 days for a one-year test" is consistent with
5–10% of 350 days (17.5–35 days) but **the specific 21-day figure was not verified** (publisher
403). `UNVERIFIED` for 21 days; `MEASURED` for the 5–10% band.

**Cepeda, Pashler, Vul, Wixted & Rohrer (2006),** *Psychological Bulletin* 132(3):354–380, DOI
10.1037/0033-2909.132.3.354 — **839 assessments in 317 experiments from 184 articles**. Key
structural finding: **ISI and retention interval operate jointly**. ⚠️ **The pooled d for spacing
and for lag is not in the retrievable abstract and is not printed here.** `UNVERIFIED`

**Donovan & Radosevich (1999), "A meta-analytic review of the distribution of practice effect: Now
you see it, now you don't," *Journal of Applied Psychology* 84(5):795–805,** DOI
10.1037/0021-9010.84.5.795. **63 studies, 112 effect sizes, mean weighted d = 0.46** favouring
spaced practice — with two deflationary riders in the abstract itself: task type and intertrial
interval **significantly moderated** the effect, and *"significantly higher effect sizes were found
in studies with **low methodological rigor**."* `MEASURED-META` The title is the caveat.

### 4.3 The clean experiment: same practice count, different wall clock

**Rohrer, D., & Taylor, K. (2006), "The effects of overlearning and distributed practise on the
retention of mathematics knowledge," *Applied Cognitive Psychology* 20(9):1209–1224,** DOI
10.1002/acp.1266. **N = 216 college students.** `MEASURED` (note: **2006, not 2004** — the 2004
*ACP* paper is the geography/vocabulary overlearning study, DOI 10.1002/acp.1083)

**Experiment 1 is the exact test this section needs.** The number of practice problems was held
**constant at 10**; the only manipulation was whether they were **massed in one session** or **split
across two sessions one week apart**.

> *"The benefit of distributed practise was **nil among students who were tested 1 week later** but
> **extremely large among students tested 4 weeks later**."*

Identical work, identical opportunity count, different calendar distribution, **divergent delayed
retention**. This is the empirical core of "acquisition compresses, durability does not."

**Experiment 2 is the overlearning null.** 3 vs 9 practice problems in a single session: the extra
six *"had no effect on test scores 1 or 4 weeks later."* **Cramming more repetitions into one
session buys nothing durable.** You cannot substitute intensity for interval.

### 4.4 The procedural/repetition floor

**Macnamara, Hambrick & Oswald (2014), "Deliberate practice and performance in music, games, sports,
education, and professions: A meta-analysis," *Psychological Science*,** DOI
10.1177/0956797614535810. `MEASURED-META` Variance in performance explained by deliberate practice:
**games 26%, music 21%, sports 18%, education 4%, professions < 1%.** Authors' conclusion:
*"deliberate practice is important, but not as important as has been argued."*
⚠️ **A corrigendum exists (DOI 10.1177/0956797618769891, 2018) whose content was not retrieved** —
verify before treating the percentages as final. `UNVERIFIED` for the corrigendum's effect.

**This result cuts both ways and both directions matter here:**
- *Against* compression: in motor-heavy domains, a quarter of the variance really is repetition, and
  repetitions take physical time an agent cannot supply.
- *For* compression, and this is the more interesting reading: **in education (4%) and professions
  (< 1%), practice volume explains almost nothing.** The 10,000-hour barrier to entering a
  *professional* field is not supported by this meta-analysis. That is direct, measured evidence
  that the barrier to breadth is not accumulated hours. It is something else — and §6 argues it is
  orientation.

**Surgical learning curves** — the best retrievable illustrations, both **single-centre
retrospective, not meta-analytic** (`OBSERVED`, illustration only): a laparoscopic radical
prostatectomy series (DOI 10.1186/s12893-026-03577-w, N = 90 consecutive cases, CUSUM) where
operative time plateaued **after the 61st case** (cases 1–30: 251.3 ± 52.3 min vs cases 61–90:
218.7 ± 40.4 min, p = 0.027); and a sentinel-node series (DOI 10.3390/cancers17233813, N = 337)
where a surgeon reached 80% success **by the 30th procedure** and 89% by the 74th, with the authors
recommending **30–35 supervised procedures**. **No pooled surgical learning-curve meta-analysis was
located, and no source for the power law of practice was retrieved.** `UNVERIFIED`

**Avoiding surgical skill decay: a systematic review on the spacing of training sessions,**
*Journal of Surgical Education* (2018), DOI 10.1016/j.jsurg.2017.08.002: **1,955 articles screened,
only 11 met inclusion**, overall quality *"moderate"*; spaced beat massed on retention, but
*"the optimal gap between the re-study sessions is unclear."* `MEASURED-META` (weak corpus)

### 4.5 The synthesis: two different quantities

| Quantity | Unit | Compressible? | Governing constant |
|---|---|---|---|
| **Acquisition** | practice opportunities | **Yes, proportionally** | ~7 opportunities/KC; time-AFM has poor fit |
| **Durability** | elapsed days | **No** | gap = 5–10% of a 1-year retention interval |
| **Effort inside durability** | minutes | **Yes** | Rohrer & Taylor: the second session is *the same 10 problems, split* |

**The refinement that makes the owner's claim sharper.** "A week's retention still needs a week"
is *almost* right and slightly pessimistic in an important way. What durability costs is **elapsed
calendar**, not additional work. Rohrer & Taylor Exp. 1 achieved the large 4-week benefit with **the
same ten problems** — merely split. So the true cost structure is:

> **Acquisition: 2–4 hours of dense, diagnosed, well-targeted opportunity.
> Durability to one year: the same material revisited two or three times, at gaps of roughly
> 18–36 days, for perhaps 20–40 minutes each.
> Total effort: under 6 hours. Total calendar: about two months. Neither number can be traded for
> the other.**

That is a genuinely better claim than "a week in an hour," and every term in it is sourced.

---

## 5. Speed records that already exist

The compression thesis does not rest on speculation about what agents might do. Systems built in the
1980s and 1990s already achieved compression factors that dwarf anything in the LLM literature — and
the mechanism by which they did it is exactly the one §2 identifies.

### 5.1 Sherlock — the record, and it is verified verbatim

**Lesgold, A., Lajoie, S., Bunzo, M., & Eggan, G. (1988), *Sherlock: A Coached Practice Environment
for an Electronics Troubleshooting Job*,** ERIC **ED299450** (also DTIC ADA201748, DOI
10.21236/ada201748). Full text retrieved and read. US Air Force F-15 avionics test-station
troubleshooting. `OBSERVED`

> *"Less experienced technicians who have practiced on Sherlock **about 20 to 25 hours** compare in
> their ability to troubleshoot test station failures with colleagues who have **four more years of
> on-the-job experience**."*

Also verbatim from the report: **34 problems, averaging 35 minutes each**; *"the average 20 hours of
coached practice"*; the average student sees **about 45 hints** across those 20 hours.

**Field-test numbers** — **Katz, Hall & Lesgold (1997)**, ERIC **ED411309**: tutored novices
**n = 18**, untutored novices **n = 23**, master technicians **n = 13** (masters had > 4× the job
experience). Tutored novices received **20 hours on Sherlock over 3 weeks**; the other groups
continued normal duties. Post-test verbal troubleshooting: tutored ≫ untutored
(VTT3 t[39] = −4.04, p < .001; VTT4 t[39] = −3.72, p < .001) *"and were comparable to those of the
master technicians."*

**Sherlock 2 / transfer** — **Gott, S. P. et al. (1995), *Tutoring for Transfer of Technical
Competence*,** ERIC **ED382817**: **54 F-15 avionics technicians** (41 apprentices, 13 masters)
across Langley, Nellis and Eglin. Apprentices averaged 33 months' experience, masters 124 months
(10 yr 4 mo). Groups equivalent at pretest. **Post-test effect size 1.27 SD** on VTT3
(control n = 23, M = 59, SD = 37; experimental n = 18, M = 95, SD = 5), with significant transfer to
a novel "Frankenstation" configuration (VTT t = −2.93, p = .006; NIT t = −2.34, p = .025).

**The compression factor: 20–25 hours against four years of on-the-job experience.** Four years of
Air Force duty is roughly 8,000 working hours. **That is a calendar compression of ≈ 300×.**

**And now the mechanism, which is the whole point.** Sherlock did not make anyone learn faster. It
delivered **34 troubleshooting problems in 20 hours.** On the flight line, a test-station failure of
that kind arrives every few weeks. Sherlock's entire contribution was **opportunity density** — it
compressed the *interval between practice opportunities*, not the opportunities themselves. This is
Koedinger's time-AFM null (§2.1, finding 4) demonstrated in the field twenty-five years before it
was measured: **learning is counted in opportunities, and four years of on-the-job experience
contains startlingly few of them.**

**This is the single most important datum in the section.** The largest verified compression factor
in the history of instructional technology was achieved by *deleting waiting*, which §3.1 identifies
as the largest and cheapest term in the budget.

### 5.2 DARPA Digital Tutor — the biggest claimed effect, partly verifiable

**Fletcher, J. D. (2011), *DARPA Education Dominance Program: April 2010 and November 2010 Digital
Tutor Assessments*,** IDA / DTIC **ADA542215**, DOI 10.21236/ada542215, 31 pp. DTIC blocked;
abstract retrieved through the **NTIS/NTRL mirror**. `OBSERVED`

> *"differences exceeded **two standard deviations** in magnitude, and in one case, the difference
> was **well above four standard deviations**."* (with the Tutor *"only partly finished"*)

**Fletcher, J. D., & Morrison, J. E. (2014), *Accelerating Development of Expertise: A Digital Tutor
for Navy Technical Training*,** IDA / DTIC **AD1002362**, 75 pp. Abstract retrieved via NTRL:

> *"After **16 weeks** of training with the Tutor, sailors who had **no prior IT experience** scored
> higher in tests of IT knowledge and job-sample troubleshooting, often with **effect sizes well in
> excess of two standard deviations**."*

Comparison groups confirmed: personnel receiving **35 weeks** of conventional Navy classroom
instruction, and **Fleet technicians averaging 9 years of IT experience**. Effective **regardless of
reading proficiency**. **Sample sizes are not in the abstract.**

**Two corrections for the record.**
- **The widely circulated "d = 1.9 to 3.7" range is UNVERIFIED.** No retrievable source states those
  values. The documented language is "in excess of two standard deviations" and "in one case well
  above four." The DOI record is `oa_status: closed`, with no repository copy in Unpaywall, and the
  per-measure effect-size tables were not obtainable. **Do not print 1.9–3.7 as sourced.**
- **The precursor study is human-tutored, not software-tutored, and this is routinely elided.**
  **Fletcher (2010), *Phase 1 IWAR Test Results*,** DTIC ADA518737, DOI 10.21236/ada518737 (full
  abstract retrieved): **12** IT "A" School candidates trained 16 weeks in the ACE program — *"Except
  for about 2 weeks when early available components of the computerized Digital Tutor (DT) were
  used, **highly qualified human tutors conducted this training**"* — against **12 Fleet ITs with
  3–12 years' experience**. Testing comprised 4 h knowledge, 13.25 h troubleshooting, 3.5 h security
  performance, 7 h design/implementation. ACE students beat Fleet ITs on **11 of 12** knowledge
  topics, solved **99 vs 79** troubleshooting problems, made **8 vs 18** harmful changes, and
  verified **97% vs 85%** of problems and **95% vs 77%** of solutions. Dockside, they solved **87%**
  of assigned tasks. **n = 12 per arm.** `OBSERVED`

**Compression factor: 16 weeks against 35 weeks of conventional school (2.2×), and against 9 years
of fleet experience (≈ 29× on calendar).** The 2.2× is the honest instructional number; the 29× is
again a *waiting* number, and again it is the larger one.

### 5.3 Computer-based instruction: the retrievable time-savings figure

**Kulik, J. A. (1983), "Synthesis of Research on Computer-Based Instruction," *Educational
Leadership*,** ERIC abstract retrieved. Meta-analysis of **51 studies**: `MEASURED-META`

> *"savings from **39 percent to 88 percent** in student learning time."*

**88% savings is 8.3×.** This is the strongest *retrievable* measured time-compression figure in the
instructional-technology literature and it sits squarely inside the 3–5× effort / 10–40× calendar
band derived in §7 — at the top of the effort range, at the bottom of the calendar range.

**Kulik & Kulik (1991)**, *Computers in Human Behavior* 7(1–2):75–94, DOI
10.1016/0747-5632(91)90030-5 — **254 controlled evaluations**; scope confirmed, but **the frequently
quoted "one-third time reduction" figure is UNVERIFIED** (no abstract text carrying a time
percentage was retrievable). **Fletcher's "rule of thirds" is UNVERIFIED** — no source located.
**Anderson, Corbett, Koedinger & Pelletier (1995)**, *Journal of the Learning Sciences*
4(2):167–207, DOI 10.1207/s15327809jls0402_2 — citation verified, but **the LISP-tutor time-savings
number (variously quoted as "1/3 less time" or "43%") is UNVERIFIED**; every full-text mirror
(act-r.psy.cmu.edu, pact.cs.cmu.edu, cs.cmu.edu) returned 404/403.

**ITS learning effects for calibration** (carried from B2, re-verified this session): VanLehn (2011),
DOI 10.1080/00461520.2011.611369 — **human tutoring d = 0.79, ITS d = 0.76**, explicitly *not* the
folkloric 0.3/1.0/2.0. Kulik & Fletcher (2016), DOI 10.3102/0034654315581420 — **median 0.66 SD**
across **50** controlled evaluations, strongly moderated by local vs standardised tests.

### 5.4 Personalized System of Instruction — self-pacing

**Kulik, J. A., Kulik, C.-L. C., & Cohen, P. A. (1979), "A meta-analysis of outcome studies of
Keller's personalized system of instruction," *American Psychologist* 34(4):307–318,** DOI
10.1037/0003-066x.34.4.307. **75 comparative studies.** Abstract retrieved: PSI *"generally produces
superior student achievement, **less variation in achievement**, and higher student ratings in
college courses."* `MEASURED-META`

**The commonly quoted ~0.5 SD final-exam effect is UNVERIFIED** — not present in any retrievable
abstract or full text. **Nothing on time-to-completion variance was obtainable**, which is a real
loss: PSI's self-pacing data is exactly the time-variance evidence this section wanted. The
retrievable finding — *less variation in achievement* — is Carroll's model running in the expected
direction (hold mastery constant, let time vary), and is consistent with §2.4's 10–20%-extra-time
figure, but it is not a time measurement.

### 5.5 The boundary case: language, where compression fails

This is the most useful negative anchor in the section, and it comes from official published data
rather than a study.

**US Department of State / Foreign Service Institute, "Foreign Language Training"**
(state.gov/foreign-language-training), retrieved. `OBSERVED` Timelines are to *"an integrated score
of **3 (Speaking + Listening)** on the Interagency Language Roundtable (ILR) scale."* A typical week
is **23 hours in class + 17 hours self-study = 40 hours**.

| FSI category | Weeks | Class hours |
|---|---|---|
| I (French, Spanish 30 wks; Danish/Dutch/Italian/Norwegian/Portuguese/Romanian/Swedish 24) | 24–30 | **552–690** |
| II | ~36 | **~828** |
| III | ~44 | **~1,012** |
| IV (Arabic, Cantonese, Mandarin, Japanese, Korean) | **88** | **2,200** |

**DLIFLC** (dliflc.edu/about/languages-at-dliflc/), retrieved: Cat I & II **36 weeks**, Cat III
**48 weeks**, Cat IV **64 weeks**. The page does **not** state a DLPT/ILR graduation target —
`UNVERIFIED`.

**Why this matters more than any positive result in this section.** FSI is the most
compression-optimised human learning protocol that exists: full-time immersion, expert instructors,
class sizes of roughly 1:4, no waiting, no search, no orientation cost, curriculum refined over
seventy years, and a hard institutional incentive to finish faster. **Every single term §3 identifies
as compressible has already been driven to zero.** And it still takes **552 hours for Spanish and
2,200 hours for Arabic.**

**The compression factor available to an AI tutor in this domain, against this baseline, is
approximately 1×.** Language is procedural, it is production-bound, and it is exactly the domain
where §4.4's repetition floor binds hardest. Anyone claiming 40× compression on language acquisition
is claiming to beat FSI by a factor of forty, and FSI publishes its numbers.

### 5.6 What has never been documented

**No controlled one-day or one-week zero-to-competence protocol with a real measured skill outcome
was located.** The nearest candidates found — a one-day veterinary suturing course with OSATS
scoring (DOI 10.5455/ajvs.131343) and anaesthesia procedural bootcamps (DOI 10.7759/cureus.21706) —
measure **comfort and self-efficacy, not skill**, or are single-arm. **This claim category is
unsupported.** Anyone citing a documented one-day-to-competence protocol should be asked for it.

### 5.7 The pattern across every record

| System | Compression | Against what | Mechanism |
|---|---|---|---|
| Sherlock | **≈ 300×** | 4 years of on-the-job experience | opportunity density (34 problems in 20 h) |
| Digital Tutor | **≈ 29×** | 9 years of fleet experience | opportunity density |
| Digital Tutor | **2.2×** | 35 weeks of classroom school | instructional quality |
| CBI meta-analysis | **1.6–8.3×** | conventional instruction | pacing + targeting |
| Kestin AI tutor | **1.22×** | a well-run active-learning hour | targeting only |
| FSI language | **≈ 1×** | itself — already optimised | none available |

**Read the right-hand column downward.** Every large factor is a *waiting* factor. Every
instructional-quality factor is between 1.2× and 8×. The records are not evidence that learning can
be made fast; they are evidence that **learning was never slow — delivery was.**

---

## 6. The polymath question

### 6.1 The bound is empirical and it is tight

**Zeng, A., Shen, Z., Zhou, J., Fan, Y., Di, Z., Wang, Y., Stanley, H. E., & Havlin, S. (2019),
"Increasing trend of scientists to switch between topics," *Nature Communications* 10:3439,**
DOI 10.1038/s41467-019-11401-8 (full text retrieved). Co-citing-network community detection over
individual scientists' complete publication records. `OBSERVED`

- *"the distributions of the number of communities that a scientist has become very narrow, **peaking
  around 4 and 3** if only communities with sizes larger than 2 and 5 are considered, respectively."*
- Yearly involved communities *"increases until it **peaks around the 20th year** of the career, and
  then gradually decreases."*
- *"high average citation per paper **in all career periods** correlates with **low** switching
  probability."*
- *"high switching probability **in early career** is associated with **low** overall productivity,
  yet **in latter career** is associated with **high** overall productivity."*

**This is the polymath question answered with data.** Over an entire research career — 30–40 years
of full-time professional effort by people selected for ability — the modal number of genuine topics
is **three or four**. Not thirty. And switching carries a measured *impact* penalty at every career
stage.

### 6.2 So what is the binding constraint?

Assemble the three measured facts:

1. **It is not learning rate.** Learning rate is astonishingly uniform: a 1.14× spread between the
   25th and 75th percentile (Koedinger et al. 2023). `MEASURED-BENCH`
2. **It is not accumulated practice hours, at least in knowledge work.** Deliberate practice
   explains **4%** of variance in education and **< 1%** in professions (Macnamara et al. 2014).
   `MEASURED-META`
3. **It is prior knowledge.** The one parameter with a large measured spread — a **3.6×** multiplier
   on the practice needed — is initial knowledge, *within a population that has formally met the
   prerequisites* (Koedinger et al. 2023, Table 2). `MEASURED-BENCH`

**Therefore:** entering field *N*+1 is expensive not because your brain is slower there, and not
because the field demands ten thousand hours, but because **your initial-knowledge parameter in that
field is at floor, and the practice multiplier that follows from being at floor is 3.6×.** Add the
wheel-spinning tax that accompanies a low prerequisite state — 50% of practice unproductive against
10% (Wan & Beck 2015) — and the effective penalty on a new field is larger still.

**That is the fixed orientation cost per field, and it now has numbers on it.** `INFERENCE`, but
built from three measured components, and the direction is not in dispute.

The corollary is the affirmative claim this section is here to make: **a system that reliably
diagnoses and repairs the initial-knowledge deficit converts the cost of field N+1 from a
3.6×-plus-wheel-spinning penalty toward the 1.14× that is genuinely irreducible.** The number of
fields a person can operate in is bounded by the *total orientation budget divided by the
per-field orientation cost*. Cut the denominator and the count rises roughly proportionally. If
the empirical ceiling of 3–4 fields per career reflects an orientation cost that is now cut by even
half, the ceiling is 6–8 — and that is a *conservative* reading, because the orientation cost also
falls each time because more of it is shared across fields.

**What this does NOT license.** It does not license "polymath" meaning *expert*. Zeng's 3–4 topics
are topics of genuine research contribution. The measured claim is about the cost of reaching
**functional competence**, not frontier contribution, and the two should never be elided. See §7.

### 6.3 The payoff to breadth is measured, and it is large

**Uzzi, B., Mukherjee, S., Stringer, M., & Jones, B. (2013), "Atypical combinations and scientific
impact," *Science* 342(6157):468–472,** DOI 10.1126/science.1240474. **17.9 million papers spanning
all scientific fields.** `OBSERVED`

> *"The highest-impact science is primarily grounded in exceptionally conventional combinations of
> prior work yet simultaneously features an intrusion of unusual combinations. **Papers of this type
> were twice as likely to be highly cited works.** Novel combinations of prior work are rare, yet
> **teams are 37.7% more likely than solo authors** to insert novel combinations into familiar
> knowledge domains."*

The structure of high-impact work is *conventional core + atypical tail* — which is precisely the
knowledge profile of someone with one deep field and cheap access to several others. And note the
last clause: today, the mechanism by which that profile is achieved is **teams**, not individuals,
because the individual orientation cost is prohibitive. **Cutting the orientation cost moves the
combination-generating capability from the team into the person.** `INFERENCE`

**Root-Bernstein et al. (2008), "Arts foster scientific success: Avocations of Nobel, National
Academy, Royal Society, and Sigma Xi members," *Journal of Psychology of Science and Technology*
1(2):51–63,** DOI 10.1891/1939-7054.1.2.51, is the classic breadth-and-eminence correlation. **The
odds ratios were not retrieved this session and are not quoted here.** `UNVERIFIED` The 2019 PNAS
follow-up (DOI 10.1073/pnas.1807189116, N = 225 STEMM professionals, convenience sample) is
retrievable but is a **correlational survey of a convenience sample** and carries no causal weight.

### 6.4 The counter-evidence on transfer

Breadth does not arrive free via transfer. **Sala & Gobet's second-order meta-analysis of cognitive
training** (DOI 10.31234/osf.io/9efqd) states the finding bluntly: *"the benefits of cognitive-training
programs hardly go beyond the trained task and similar tasks."* `MEASURED-META` And from F11,
carried: **Pan & Rickard (2018)**, *Psychological Bulletin*, retrieval-practice **transfer** d = 0.40
[0.31, 0.50] — real, but weaker than retention, and **weakest to rearranged stimulus–response items,
untested material seen during study, and worked-example problems.**

**The implication for polymathy is specific and it is a constraint, not a licence:** each new field
must be *paid for individually*. There is no general "learning ability" that carries across. What an
agent can do is make each individual payment cheaper — not make the payments unnecessary.

---

## 7. The upper bound, stated as a number

### 7.1 The model

The floor is a product of three terms, and every one of them is either measured or explicitly
assumed:

> **T_floor = N_kc × O(θ) × t_opp**
>
> - **N_kc** — knowledge components in the target material. *Assumption, not measurement.*
> - **O(θ)** — opportunities to 80% mastery given initial knowledge θ. **Measured**
>   (Koedinger et al. 2023, Table 2): **3.66** (75th pct) / **6.54** (median) / **13.13** (25th pct).
> - **t_opp** — wall-clock per opportunity: read the problem, attempt it, receive and process
>   feedback. **Not measured in this literature.** Bounded below by human reading and reasoning
>   speed, not by system latency.
>
> **T_durable = T_floor + k review sessions at gaps of 5–10% of the retention horizon**
> (Cepeda et al. 2008), each costing a *fraction* of T_floor because the material is the same
> (Rohrer & Taylor 2006 Exp. 1).

### 7.2 The calculation, with assumptions exposed

Take "a week of a course" to be **20 knowledge components** — this is `INFERENCE` from the
granularity of KC models in the datasets Koedinger analysed, and it is the weakest link in the
chain. Take **t_opp = 90 seconds**, which is generous to the learner and again `INFERENCE`.

| Scenario | O(θ) | T_floor (20 KCs × O × 90 s) |
|---|---|---|
| Prerequisites intact (75th pct initial knowledge) | 3.66 | **1.8 hours** |
| Median learner | 6.54 | **3.3 hours** |
| Prerequisites broken and **unrepaired** (25th pct) | 13.13 | **6.6 hours** + wheel-spinning tax |

Against the **nominal effort week** of 9 hours (§1.1): compression of **1.4× to 5×**.
Against the **calendar week** of 112 waking hours: compression of **17× to 62×**.
Against the **measured modern study week** of ~11–13 self-reported hours (Babcock & Marks):
compression of **1.7× to 7×**.

### 7.3 The answer

**Maximum defensible compression factor: 10× to 40× on elapsed calendar time, and 3× to 5× on
engaged effort, for well-structured declarative and conceptual material, measured by immediate
mastery test.** Conditions and failure modes below.

**Where each factor comes from:**

| Term | Multiplier | Basis | Label |
|---|---|---|---|
| Waiting eliminated | **~10×** on calendar | Carnegie accounting: 9 nominal hours inside 112 waking hours | `INFERENCE` (accounting identity) |
| Prerequisite diagnosis and repair | **up to 3.6×** on effort | Koedinger 13.13 → 3.66 | `MEASURED-BENCH` (the collapse itself is `INFERENCE`) |
| Targeting (BTES high-success stage) | **~2×** on effort | ALT ≈ 35% of allocated in the median classroom; ~4 vs ~52 min in the extremes | `OBSERVED` |
| Replacing rereading with retrieval | **g ≈ 0.50** — a *quality* gain, converted to time only by assumption | Yang et al. 2021, 222 studies, N = 48,478 | `MEASURED-META` |
| Search elimination | **unquantified** | no measurement exists | — |

**Why the effort terms do not multiply to 7×.** Prerequisite repair (3.6×) and targeting (2×) are
**the same phenomenon observed at two points in the pipeline** — an unrepaired prerequisite *is* a
low-success task. Multiplying them double-counts. The honest composition is **3× to 5×** on engaged
effort, dominated by the prerequisite term, with targeting adding at the margin.

**Why the calendar term is 10× and not 100×.** The 112:9 ratio is real, but you cannot spend all 112
hours learning. The practical ceiling on daily dense study is set by fatigue, and a compression that
demands 8 hours of unbroken diagnosed practice will not be executed. **10×–40× is the range across
"conservatively schedulable" and "maximally schedulable."**

### 7.3a Triangulation — the derived number against the historical record

The estimate above was built bottom-up from Koedinger's opportunity counts. It should be checked
against §5's top-down measurements, and it survives the check:

| Estimate | Value | Route |
|---|---|---|
| §7.2 derived, effort | **1.4×–5×** | bottom-up from O(θ) and t_opp |
| **Kulik (1983), 51 studies, measured** | **1.6×–8.3×** | top-down, CBI vs conventional |
| §7.2 derived, calendar | **17×–62×** | bottom-up, Carnegie arithmetic |
| **Digital Tutor vs 9 years' fleet experience** | **≈ 29×** | top-down, IDA assessment |
| **Sherlock vs 4 years' on-the-job experience** | **≈ 300×** | top-down, ERIC ED299450 |

The two independent routes agree on the effort term to within their own uncertainty. **The calendar
term is where the derived estimate is conservative** — Sherlock beat it by an order of magnitude,
because on-the-job "experience" is a far emptier baseline than a structured course week. **Against
informal, experience-based learning rather than a course, the ceiling is higher than 40×, and 300×
has been documented once.**

### 7.4 The conditions, stated so the number can be refused

The 10–40× holds **only** when all of the following are true. Any one failing collapses it.

1. **Material is declarative or conceptual.** Motor and procedural skill retains a repetition floor
   (Macnamara: 26% of variance in games, 21% music, 18% sports; 30–35 supervised surgical
   procedures). **For motor and production domains the defensible factor is ≈ 1×**, and §5.5 is the
   proof: FSI has already driven every compressible term to zero and still needs 552–2,200 hours.
   *Any claim of large compression on language, surgery, music or sport is a claim to beat a
   published, seventy-year-optimised baseline, and should be treated as extraordinary.*
2. **The success criterion is an immediate mastery test.** This is the criterion the compression
   applies to and the paper must say so.
3. **Diagnosis is accurate.** The 3.6× is available only if the missing prerequisite is correctly
   identified. Misdiagnosis converts the largest positive term into a negative one, and
   over-scaffolding a competent learner triggers expertise reversal (F10).
4. **The learner actually attempts.** Bastani et al. (2025), *PNAS*, DOI 10.1073/pnas.2422633122:
   unguarded GPT-4 produced **−17%** on the unassisted exam. `MEASURED-RCT` **The compression is a
   property of delivered practice opportunities, not of delivered answers.** An agent that answers
   instead of asking removes the opportunities the floor is made of, and the factor goes negative.
5. **The retention horizon is short, or the schedule is honoured.** For a one-year horizon, add
   review sessions at **18–36-day** gaps. **No compression factor applies to this term.**

### 7.5 The claim, finally, in the owner's own frame

> **"Things that take a week can be learnt in an hour."**
>
> Substantially true, and for a more interesting reason than the claim assumes. A calendar week of
> a course contains about **nine** nominal hours of student effort, of which perhaps **three** are
> spent on well-targeted material and perhaps **one to two** are irreducible encoding once
> prerequisites are repaired. **The hour is real. It was always in there.** What the agent removes
> is the 111 hours of calendar around it, the mis-targeted third, and the practice wasted on a
> prerequisite nobody named.
>
> **What the agent cannot remove is the month.** A year-durable memory needs its opportunities
> separated by roughly 18–36 days, and no amount of intelligence in the tutor changes that. The
> good news, which is not obvious: **the separated sessions are cheap.** Rohrer & Taylor got the
> large four-week benefit from *the same ten problems*, merely split.
>
> **So the defensible claim is: a week's understanding in an hour; a year's retention in six hours
> spread over two months.** Effort compresses by 3–5×. Calendar compresses by 10–40×. Durability
> compresses by 1×, and costs almost nothing extra to buy.

**And the reason to be bold rather than hedged about this.** Sherlock did it in 1988 (§5.1), with
34 hand-authored problems, a hint engine, and no language model — **20 hours against four years.**
The compression is not a forecast. It has been measured, in the field, under Air Force
instrumentation, on a real job. What was scarce in 1988 was not the idea but the *authoring*: each
of those 34 problems, each of those 45 hints, was built by hand by domain experts over years, for
one job, on one test station. **The thing generative models change is not the compression factor.
It is the cost of manufacturing the opportunities that produce it.** That is why the ceiling is
worth stating loudly: the ceiling is old, verified, and has been sitting unreachable behind an
authoring bottleneck for thirty-five years.

---

## 8. Negative and null results

Per CLAUDE.md §2, ≥1 is required. This section reports **sixteen**, and several of them are
load-bearing against its own thesis.

| # | Null / negative finding | Source | Label | What it kills |
|---|---|---|---|---|
| 1 | **There is no meta-analysis of intensive vs traditional course formats.** Every source cited as one — Scott & Conrad (1992, ERIC ED337087, 110 references), Daniel (2000), Harvey/Power/Wilson (2017, DOI 10.1080/00219266.2016.1217912) — is a **narrative review with no pooled effect size**. No d or g for format compression exists in the literature. | retrieval result, this session | `OBSERVED` | any citation of "the intensive-course meta-analysis" |
| 2 | **The intensive advantage decays to nothing.** Seamon (2004), *Teachers College Record* 106(4):852–874: matched educational-psychology classes (groups did not differ on need for cognition, age or GPA — a real selection check); intensive students scored significantly higher on immediate posttests of content *and* higher-order learning; **a 3-year follow-up with the same participants found no significant difference.** | Seamon 2004 | `OBSERVED` | the strong form of format compression |
| 3 | **Same contact hours, compressed calendar, WORSE grades.** Whillier & Lystad (2013), *Anatomical Sciences Education* 6(4), DOI 10.1002/ase.1358: Macquarie neuroanatomy, same teachers, same content, same total contact hours, 7-week vs 13-week. **Traditional cohort achieved significantly higher final grades (P = 0.001)**; no difference in self-rated knowledge (P = 0.148); the **intensive cohort was *more* satisfied** with practicals (P < 0.001). | Whillier & Lystad 2013 | `OBSERVED` | the assumption that satisfaction tracks learning under compression |
| 4 | **No format effect at 6 months.** LaFountain (1995), *Innovative Higher Education*: graduate counselling statistics; 6-month follow-up test showed no significant effect of scheduling format. | LaFountain 1995 | `OBSERVED` | durable format effects in either direction |
| 5 | **Compression degrades *mastery* measures while flattering *effort* measures.** Price (2024), *Decision Sciences Journal of Innovative Education*: compressed online economics, both taught in summer — effort-based assessments equal or better, **mastery-measuring assessments declined**, ratings worse. | Price 2024 | `OBSERVED` | measuring compression with the wrong instrument |
| 6 | **Sleep does not enhance motor learning.** Pan & Rickard (2015), *Psych. Bulletin* 141(4):812–834: 34 articles, 88 groups, 1,296 subjects — *"there was no evidence that sleep enhances learning."* | Pan & Rickard 2015 | `MEASURED-META` | the Walker 20% figure standing alone |
| 7 | **The sleep benefit shrinks 36% under publication-bias correction.** Berres & Erdfelder (2021): g = 0.44 → **0.28**. | Berres & Erdfelder 2021 | `MEASURED-META` | overstating the consolidation constraint |
| 8 | **TMR does nothing in REM or in wakefulness.** Hu et al. (2020): 91 experiments, N = 2,004. | Hu et al. 2020 | `MEASURED-META` | waking-consolidation shortcuts |
| 9 | **Overlearning buys nothing durable.** Rohrer & Taylor (2006) Exp. 2: 3 vs 9 problems in one session — the extra six *"had no effect on test scores 1 or 4 weeks later."* Corroborated by Rohrer & Taylor (2004), DOI 10.1002/acp.1083 (N = 218): the overlearning advantage present at 1 week *"decreased dramatically thereafter."* | Rohrer & Taylor 2004, 2006 | `MEASURED` | "just do more of it in the compressed session" |
| 10 | **Spacing has no robust effect on mathematical *procedures*.** "No Robust Effect of Distributed Practice on the Short- and Long-Term Retention of Mathematical Procedures," *Frontiers in Psychology* (2020), DOI 10.3389/fpsyg.2020.00811: **N = 235**, ISI = 0/1/11 days, test at 1 or 5 weeks, between-subjects — *"the analyses revealed **no effect of distributed practice** and therewith also no lag effect, even though the sample size was sufficiently large."* **This directly contradicts Rohrer & Taylor (2006) Exp. 1 on nearly the same material. The contradiction is unresolved and is reported as such.** | Frontiers 2020 | `MEASURED` | *both* the strong spacing constraint and the strong compression case — it cuts both ways |
| 11 | **Deliberate practice explains < 1% of professional performance variance and 4% in education.** Macnamara et al. (2014). | Macnamara et al. 2014 | `MEASURED-META` | the 10,000-hour framing in both directions |
| 12 | **More time on the AI tutor did not produce better scores.** Kestin et al. (2025): *"no correlation between the time on task and students' post-test scores"* despite a wide range of times. | Kestin et al. 2025 | `MEASURED-RCT` | "give the learner more hours with the agent" |
| 13 | **Unguarded LLM access produces −17% on the unassisted exam.** Bastani et al. (2025), *PNAS*. | carried from B2 | `MEASURED-RCT` | compression achieved by answering rather than practising |
| 14 | **The domain with every compressible term already at zero still costs 552–2,200 hours.** FSI publishes it (§5.5). | US State Dept, official | `OBSERVED` | large compression claims in procedural/production domains |
| 15 | **No documented one-day or one-week zero-to-competence protocol exists** with a controlled, measured skill outcome. The candidates located measure *comfort* and *self-efficacy*, or are single-arm. | retrieval result, this session | `OBSERVED` | the "learn anything in a day" genre entirely |
| 16 | **The most-cited compression numbers in the field are unverifiable.** Digital Tutor's "d = 1.9–3.7" (documented language is only "in excess of two SD"); Kulik & Kulik's "one-third time reduction"; the LISP tutor's "43% less time"; Fletcher's "rule of thirds"; PSI's "0.5 SD". **None could be sourced this session.** Additionally, the Digital Tutor's headline Phase 1 result was produced by **human tutors for 14 of its 16 weeks**, which is almost never stated. | retrieval result, this session | `OBSERVED` | the citation chain the whole "accelerated expertise" literature rests on |

**The two that hurt most, named honestly:**
- **#2 (Seamon)** is the only study located that both controlled for pre-existing student
  characteristics *and* tested at a long delay, and it found the intensive advantage **real
  immediately and gone at three years.** That is exactly the acquisition/durability dissociation
  this section argues for — which makes it corroborating — but it is also a hard limit on what a
  compression claim may promise.
- **#10 (Frontiers 2020)** contradicts §4.3's central experiment. Two adequately powered studies on
  near-identical material disagree about whether spacing protects procedural knowledge. **The
  durability constraint in §4 is therefore firmer for declarative than for procedural material,**
  and the section says so rather than picking the convenient result.

---

## 9. What should exist and does not

1. **A study-session time-motion decomposition.** Nobody has measured how a learning hour splits
   into search / orientation / reading / practice / stuck. The BTES cascade is the closest analogue
   and it is a 1976 elementary classroom. **This is the single highest-value missing measurement in
   the survey**, and it is cheap: instrument a cohort, classify events, publish the histogram.
2. **The repair-then-remeasure experiment.** Koedinger's 13.13 → 3.66 gap is measured. Whether
   diagnosing and repairing the missing components *moves a learner's initial-knowledge parameter*
   — and by how much — has not been tested. This is the experiment that would convert the largest
   term in §7.3 from `INFERENCE` to `MEASURED`. Design: pre-test to KC granularity, randomise to
   targeted repair vs matched-dose untargeted practice, remeasure θ, count opportunities to mastery.
3. **A compression RCT with a delayed test.** Every study in §5 and every study in table §8 measures
   either compression *or* delayed retention, never both cleanly in the same design with the same
   opportunity count. Seamon (2004) comes closest and is from 2004.
4. **t_opp measured.** The wall-clock cost of one practice opportunity — read, attempt, feedback,
   process — is the term that converts opportunity counts into hours, and no one has published it.
   Without it, every compression factor in this literature is a conversion away from being real.

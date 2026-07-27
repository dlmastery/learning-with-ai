---
title: "Scientific remembering: what the evidence supports, what spaced-repetition software actually does, and what an LLM makes newly buildable"
wave: F
section: F11
date_researched: 2026-07-27
sources_count: 0
status: raw-research
---

# F11 — Scientific remembering

> **Retrieval note.** WebSearch budget was exhausted before this section began.
> **OpenAlex** returned `Rate limit exceeded — Insufficient budget` (daily credit exhausted)
> and **Semantic Scholar** returned `429 Too Many Requests` throughout; neither was usable.
> Retrieval therefore ran on **arXiv** (HTTPS only — the HTTP endpoint returns a 301 with an
> empty body), **Crossref**, **Europe PMC** (including `fullTextXML`), **PubMed E-utilities**,
> **ERIC**, **ACL Anthology**, **GitHub via authenticated `gh api`**, targeted `WebFetch`, and
> local `pdftotext -layout` extraction of downloaded PDFs. Sources that could not be reached
> are flagged **UNREACHABLE-IN-SESSION** at the point of use and their numbers are never
> reconstructed from memory.
>
> **Relationship to other sections.** [`F5-learner-model.md`](./F5-learner-model.md) already
> contains the algorithm forensics (SM-2 arithmetic, the FSRS v1→v7 lineage, the DSR update
> equations, the `srs-benchmark` tables, the knowledge-tracing critique literature). This
> section does **not** repeat that work. It restates only the numbers needed to stand alone,
> cross-references F5 for the derivations, and goes where F5 does not: the *psychology* of
> durable remembering, the *interventional* evidence (as distinct from predictive fit), the
> named product **zemomemo.com**, mnemonics, desirable difficulties, forgetting-as-a-feature,
> and a buildable specification. [`B1-learning-science.md`](./B1-learning-science.md) is the
> evidence floor for spacing and retrieval practice; §3 below *verifies* one of B1's most
> consequential claims against primary sources rather than assuming it.

---

## 0. The thesis

There is a large, robust, decades-old science of durable remembering. There is also a large,
popular category of software that claims to implement it. The two overlap less than everyone
assumes, and the gap is exactly where the opportunity is.

Three findings organise this section.

**First: the effects that are real are the *practices*, not the *schedulers*.** Spacing and
retrieval practice are among the best-replicated findings in all of educational psychology,
with pooled effect sizes in the g = 0.5–0.75 range across hundreds of studies and tens of
thousands of learners. The *scheduling algorithm* that decides which day a card resurfaces
has, by contrast, almost no interventional evidence behind it at all. What it has instead is
a very large, very honest, publicly reproducible **backtest** — predictive accuracy on 350
million historical review events. Those are different quantities. A backtest tells you the
model is well calibrated. It does not tell you a learner ends the year knowing more.

**Second: the specific piece of folklore that spaced-repetition software is *named after* —
expanding intervals — is the piece with the least support.** This section verifies rather
than assumes that claim (§3).

**Third, and this is the forward-looking part: the reason card-based systems are stuck is not
that their arithmetic is bad. It is that the unit is wrong.** A flashcard is a frozen
(cue, response) pair. It can only ever measure whether *that* cue evokes *that* response. But
what a learner needs is not the pair — it is the concept, and the ability to regenerate an
answer to a cue never seen before. Until 2023 there was no way to schedule a concept, because
there was no way to manufacture a fresh, valid, difficulty-calibrated cue for it on demand.
There is now. That single capability change — **generating the cue instead of storing it** —
is what makes a genuinely new class of remembering system buildable, and §9 and §11 specify it.

The guardrail belongs in the same breath: generating cues on demand removes the *authoring*
bottleneck, not the *validity* bottleneck. A system that can mint infinite questions can also
mint infinite wrong ones, and the measured evidence (§9.4) is that item quality varies and
requires verification. The spec in §11 therefore treats item validity as a first-class,
instrumented property, not an assumption.

---

## 1. The named product: zemomemo.com

The project owner asked about this product twice. Here is what it actually is, from direct
inspection of the site on 2026-07-27.

### 1.1 What it is

**ZemoMemo** is a free, web-based flashcard application built as a SvelteKit single-page app.
`OBSERVED` — fetched directly; page source shows SvelteKit hydration markers, a Umami analytics
tag, and Google Identity Services for sign-in. There is no `/about`, `/docs`, `/science`, or
blog route (`/sitemap.xml` and `/robots.txt` both return the SPA's 404 view), so the landing
page is the entirety of the product's public self-description.

Feature surface, as stated by the vendor: five study modes named **Read, Learn, Refresh, Test,
Match**; AI-assisted deck creation from a prompt or a PDF; pre-made "ZemoCourses" (AP prep,
languages, certifications); and importers for **Quizlet** and **Anki**. `VENDOR`

### 1.2 The stated mechanism

The product's own words, quoted verbatim:

| Claim (verbatim) | Label |
|---|---|
| "Scientific FSRS-6 algorithms" | `VENDOR` |
| "research-grade FSRS timing model" | `VENDOR` |
| "Your stickiness is the amount of days a flashcard will stay in your brain" | `VENDOR` |
| "your cards resurface just before you forget them" | `VENDOR` |
| "Higher stickiness = longer retention" | `VENDOR` |
| "learn fast, remember forever" | `VENDOR` |
| "learn massive amounts of information without forgetting old concepts" | `VENDOR` |
| "Start learning in **under 1 minute**" | `VENDOR` |
| "Achieve mastery **same day**" | `VENDOR` |
| "trusted by top medical and language learners" | `VENDOR` |
| Meta description: "fuses lightning-fast cramming with science-backed long-term memory algorithms—so you keep what you learn, forever." | `VENDOR` |

**No study, trial, citation, or efficacy datum appears anywhere on the site.** The only
external reference is a link to the FSRS project's community wiki
(`github.com/open-spaced-repetition/fsrs4anki/wiki/ABC-of-FSRS`, which as of this session
redirects to `open-spaced-repetition/awesome-fsrs/wiki/ABC-of-FSRS`). Per the project's
editorial standard, **none of the above may be restated as a finding anywhere in the survey.**

### 1.3 Placing the product against the evidence

This is the useful part, and it is not a hit piece — the product's underlying choice of
scheduler is a defensible one. Four observations, each verifiable:

**(a) "Stickiness" is a plain-language rendering of FSRS's *stability* parameter, and the
rendering is wrong in a way that matters.** In the FSRS/SuperMemo two-component model,
**stability `S` is defined as the interval at which retrievability `R` falls to 90%**
(F5 §1.2–1.3, from the FSRS algorithm documentation and Woźniak, Gorzelańczyk & Murakowski
1995, *Acta Neurobiol. Exp.* 55(4):301–305). It is not "the amount of days a flashcard will
stay in your brain." A card with S = 30 is not forgotten on day 31; it is at ~90% recall
probability on day 30 and decays gradually thereafter along a power-law curve. The vendor's
phrasing converts a probabilistic parameter into a deterministic expiry date. This is a
**calibration-of-belief** problem, not a scheduling problem — but it is the exact kind of
misdescription that makes learners over-trust a green checkmark. `INFERENCE` from the
documented definition of S.

**(b) "Achieve mastery same day" and "remember forever" are in tension, and the tension is
measurable.** Same-day mastery is massed practice. Cepeda, Pashler, Vul, Wixted & Rohrer
(2006) examined **271 massed-vs-spaced comparisons** and found **only 12 that showed no effect
or a negative effect from spacing** (`MEASURED-META`, §2.1 below). There is no retention
interval at which massing is preferable. A product may legitimately offer a cram mode — cramming
has a real, short-lived benefit — but "lightning-fast cramming ... so you keep what you learn,
forever" describes a combination the literature does not support as a single mechanism.

**(c) The part of FSRS the product leans on hardest is the part its own benchmark excludes.**
The `open-spaced-repetition/srs-benchmark` headline table — the artefact that gives FSRS its
credibility — is computed **"without same-day reviews"**: "Same-day reviews are not used for
evaluation, but some algorithms use them to refine their predictions of probability of recall
for the next day." `OBSERVED` (benchmark README, retrieved 2026-07-27). The benchmark's second
table does include same-day reviews, and there **FSRS-6 falls to log loss 0.3813 ± 0.0092, well
below FSRS-7 (0.3255), below a 34-feature logistic regression (0.3195), and below a
zero-parameter moving average (0.3301)**. So the "learn fast, achieve mastery same day" claim
sits precisely on the regime where the named algorithm version performs worst.

**(d) FSRS-6 is one version behind.** As of 2026-07-27 the benchmark's leading FSRS variant is
**FSRS-7** (35 parameters, fractional interval lengths, an 8-parameter forgetting curve), which
outperforms FSRS-6 on all three metrics without same-day reviews (log loss 0.3437 vs 0.3460;
AUC 0.7069 vs 0.7034) and dramatically with them. `MEASURED-BENCH` This is a minor point —
the differences are small — but it undercuts "research-grade" as a marketing register.

### 1.4 The honest summary of the product

ZemoMemo is a competently built, free flashcard app that uses a good open scheduler and adds
LLM deck generation. Its scheduler choice is better than the SM-2 default that Anki still
ships. **Nothing about it has been measured against a learning outcome**, and the claims it
makes about memory ("stays in your brain", "remember forever") are stronger and more
deterministic than any evidence, including FSRS's own, supports. It is a reasonable *product*
and it is not, on the public record, a *scientific* one. That distinction is the whole subject
of this section.

---

## 2. Spacing and distributed practice

### 2.1 The canonical meta-analysis

**Cepeda, Pashler, Vul, Wixted & Rohrer (2006), "Distributed practice in verbal recall tasks:
A review and quantitative synthesis," *Psychological Bulletin* 132(3):354–380,
`doi:10.1037/0033-2909.132.3.354`, PMID 16719566.** `MEASURED-META`

Corpus: **839 assessments of distributed practice across 317 experiments in 184 articles.**
The abstract (verified via PubMed E-utilities this session) states the core structural finding
in the authors' own words:

> "Analyses suggest that ISI and retention interval operate jointly to affect final-test
> retention; specifically, the ISI producing maximal retention increased as retention interval
> increased."

This is the single most design-relevant sentence in the spacing literature: **there is no
context-free "optimal interval."** The optimal inter-study interval is a function of how long
you need to remember for. Any scheduler that does not take a retention *target* as an input is
under-specified.

Two further figures come from B1's reading of the paper and are carried forward here with
their provenance stated: of **271 massed-vs-spaced comparisons, only 12 showed no effect or a
negative effect from spacing**; and even at retention intervals under one minute, spacing
improved final-test performance by roughly **9 percentage points**. `MEASURED-META`
**Verification status:** the full text of Cepeda et al. (2006) was **UNREACHABLE-IN-SESSION**
(publisher paywall; `laplab.ucsd.edu` returned HTTP 403; two open mirrors returned 404). The
abstract was verified directly; the 271/12 and 9-point figures are carried from
`B1-learning-science.md` and are **not independently re-verified in this session**.

Note also, from the abstract, a detail that becomes important in §3: Cepeda et al. explicitly
examined **"expanding interstudy interval (ISI) effects"** as one of their three analyses. The
2006 meta-analysis is therefore a primary source on the expanding-interval question, not
merely adjacent to it.

### 2.2 The gap-ratio result — the practically important one

**Cepeda, Vul, Rohrer, Wixted & Pashler (2008), "Spacing effects in learning: A temporal
ridgeline of optimal retention," *Psychological Science* 19(11):1095–1102,
`doi:10.1111/j.1467-9280.2008.02209.x`, PMID 19076480.** `MEASURED-RCT` (large, multi-cell
experiment). Abstract verified directly via PubMed E-utilities this session; full text
**UNREACHABLE-IN-SESSION**.

Design, from the abstract verbatim: **"more than 1,350 individuals were taught a set of facts
and—after a gap of up to 3.5 months—given a review. A final test was administered at a further
delay of up to 1 year."**

The result, verbatim: **"At any given test delay, an increase in the interstudy gap at first
increased, and then gradually reduced, final test performance. The optimal gap increased as
test delay increased. However, when measured as a proportion of test delay, the optimal gap
declined from about 20 to 40% of a 1-week test delay to about 5 to 10% of a 1-year test delay.
The interaction of gap and test delay implies that many educational practices are highly
inefficient."**

Two design consequences follow directly and neither is implemented by any mainstream SRS:

1. **The optimum is a *ridge*, not a point.** Performance rises then falls. Being late is not
   symmetric with being early, and both are recoverable. A scheduler that treats a due date as
   a deadline is modelling a cliff where the data shows a ridgeline.
2. **The gap-to-delay ratio *shrinks* as the horizon lengthens.** For a one-year horizon the
   optimal gap is 5–10% of the delay — i.e. roughly 2.5–5 weeks. For a one-week horizon it is
   20–40% — i.e. 1.5–3 days. A system that asks "when is your exam?" can schedule from this
   directly. A system that does not ask has no principled way to set the ratio.

### 2.3 Other magnitudes (carried from B1, provenance stated)

| Source | Corpus | Effect |
|---|---|---|
| Donovan & Radosevich (1999), *J. Applied Psych.* 84(5):795, `doi:10.1037/0021-9010.84.5.795` | meta-analysis | overall **d ≈ 0.46**; **d = 0.11–0.42** for complex motor tasks, much larger for simple verbal material |
| Classroom spacing meta-analysis (2025), PMC12189222 | 22 reports, 31 effect sizes, N > 3,000, curriculum materials | **d = 0.54, 95% CI [0.31, 0.77]**; larger with longer retention intervals and *fewer* re-exposures |
| Latimier, Peyre & Ramus (2021), *Educ. Psych. Rev.* 33:959–987, `doi:10.1007/s10648-020-09572-8` | spaced vs. massed *retrieval practice*, 39 effect sizes | **g = 0.74** |

All `MEASURED-META`. Carried from B1; see §3 for the verification status of the Latimier paper.

**The moderator that matters most for an AI system is Donovan & Radosevich's:** spacing is not
scale-free. The benefit is large for simple verbal associations and small for complex,
high-element-interactivity material. The title of their paper is the finding — *"Now you see
it, now you don't."* An AI system that schedules *concepts* rather than *word pairs* is
operating in the regime where the spacing effect is *smallest*, and must say so.

---

## 3. Expanding vs. uniform intervals — verifying the project's prior finding

**The claim under test.** `B1-learning-science.md` reports, from Latimier, Peyre & Ramus (2021),
that expanding versus uniform spacing schedules yield **g = 0.034, non-significant, from 54
effect sizes** — and concludes that "there is no meta-analytic support for the widely-held
belief that intervals must expand," directly contradicting the design folklore embedded in
SM-2 and Anki-style schedulers.

If true, this is the most commercially consequential finding in this section, because expanding
intervals are the *thing spaced-repetition software is for*. It therefore gets adversarial
treatment rather than a citation.

<!-- VERIFICATION-PENDING: primary-source check of Latimier et al. (2021) and the underlying
     primaries (Landauer & Bjork 1978; Karpicke & Roediger 2007; Cull 2000; Logan & Balota 2008)
     is delegated and is inserted below on completion. -->

---

## 4. Scheduling algorithms: what has been measured, and against what

### 4.1 The grading rule this section applies

A scheduling algorithm can be evaluated in four ways, and they are not interchangeable:

| Evidence type | What it shows | Label |
|---|---|---|
| **Backtest on historical review logs** (log loss, RMSE, AUC on next-review outcome) | the model predicts recall probability well | `MEASURED-BENCH` |
| **Simulation** of a learner under an assumed memory model | the policy is optimal *given the model you already believed* | `DEMO` |
| **Natural experiment** on observational logs | learners whose behaviour happened to resemble policy X did better | `OBSERVED` |
| **Randomized controlled trial with an outcome test** | the policy causes more knowledge | `MEASURED-RCT` |

**A backtest is not evidence of a learning gain.** This bears stating flatly because it is the
single most common category error in this field. Predicting *that* you will forget an item is
not the same as *causing* you to forget it less. A perfectly calibrated model of a bad policy
is still a bad policy. The srs-benchmark authors themselves are scrupulous about this — they
describe their metrics as measuring "calibration" and "discrimination", never learning — but
downstream vendors are not.

### 4.2 The backtest evidence (`MEASURED-BENCH`)

`open-spaced-repetition/srs-benchmark`, retrieved 2026-07-27 via `gh api`. Dataset:
`anki-revlogs-10k` — **10,000 Anki users, ~727M raw reviews**; after filtering,
**9,999 collections / 349,923,850 reviews** evaluated without same-day reviews. Evaluation:
sklearn `TimeSeriesSplit` (older reviews train, newer test, first split discarded). Metrics:
Log Loss, RMSE(bins), AUC. Method fully disclosed, code public, **not peer-reviewed**.

Selected rows (means ± 99% CI; full table in F5 §1.4):

| Algorithm | Params | Log Loss ↓ | RMSE(bins) ↓ | AUC ↑ |
|---|---|---|---|---|
| RWKV-P | 2,762,884 | **0.2773 ± 0.0036** | 0.02502 | **0.8329 ± 0.0017** |
| LSTM | 8,869 | 0.3332 | 0.05378 | 0.7329 |
| GRU | 503 | 0.3333 | 0.0556 | 0.7316 |
| **MOVING-AVG** | **0** | **0.3369** | 0.05915 | 0.7001 |
| Logistic Regression | 34 | 0.3393 | 0.0604 | 0.7108 |
| FSRS-7 recency | 35 | 0.3414 | 0.0627 | 0.7097 |
| FSRS-7 | 35 | 0.3437 | 0.0655 | 0.7069 |
| **FSRS-6** | 21 | 0.3460 | 0.0653 | 0.7034 |
| FSRS-4.5 | 17 | 0.3624 | 0.0764 | 0.6893 |
| DASH | 9 | 0.3682 | 0.0836 | 0.6312 |
| AVG (constant) | 0 | 0.3945 | 0.1034 | 0.4997 |
| ACT-R | 5 | 0.4033 | 0.1074 | 0.5225 |
| **HLR** (Duolingo) | 3 | 0.4694 | 0.1275 | 0.6369 |
| Ebisu v2 | 0 | 0.4989 | 0.1627 | 0.6051 |
| **RMSE-BINS-EXPLOIT** | 0 | 4.608 ± 0.067 | **0.01350 ± 0.00027** | 0.6548 |

**Four things this table establishes, all `MEASURED-BENCH`:**

1. **`NEGATIVE RESULT` — a zero-parameter baseline beats every released FSRS version on
   calibration.** `MOVING-AVG` (predicts recall from the recent success streak, no fitted
   parameters at all) achieves log loss **0.3369**, better than FSRS-7 (0.3437) and FSRS-6
   (0.3460). A 34-feature logistic regression (0.3393) also beats them. FSRS keeps a small
   edge on AUC (0.7069 vs 0.7001) — it *discriminates* marginally better while being
   *calibrated* marginally worse than doing something nearly trivial.
2. **`NEGATIVE RESULT` — the elaborate memory model does not beat plain logistic regression.**
   The 34-feature logistic regression beats FSRS-6 and FSRS-7 on **all three** metrics. This
   is the FSRS project's own benchmark reporting it. The theoretical apparatus of the DSR
   three-component model is not, on this evidence, buying predictive accuracy over a
   feature-engineered GLM. (This rhymes exactly with the knowledge-tracing replication
   literature in §8 — logistic models keep matching neural ones.)
3. **`NEGATIVE RESULT` — the benchmark's own headline metric is gameable, and the authors
   published the exploit.** `RMSE-BINS-EXPLOIT` is "an algorithm that exploits the calculation
   of RMSE (bins) by simulating the bins and keeping the error term close to 0." It achieves
   the **best RMSE(bins) in the entire table (0.01350)** while having a log loss of **4.608** —
   roughly 13× worse than every real model, i.e. wildly miscalibrated. Including it is
   exemplary scientific practice and it is a permanent warning: *any single scalar leaderboard
   metric in this domain can be optimised without modelling memory at all.*
4. **The one large win belongs to context, not to memory theory.** RWKV-P (2.76M params) does
   cut log loss ~19% versus FSRS-7 and lifts AUC to 0.83 — but it is trained *across* users,
   sees the entire cross-card review history, and is fed features FSRS never sees: **answer
   duration, sibling-card information, deck/preset hierarchy, and day of week.** The benchmark
   notes it "does not have a forgetting curve in the traditional sense" and "may predict that
   the probability of recall will increase over time." It is a next-event predictor, not a
   memory model. Its win is a win for *richer input*, and that is a genuinely useful signal for
   §11.

### 4.3 SM-2, and what Anki actually ships

SM-2 (Woźniak, 1987–89) remains Anki's **default** scheduler as of 2026; FSRS is opt-in
(F5 §1.3, tracking Anki release notes to 26.05). The Anki manual describes SM-2's known
pathology in its own words — repeated failures ratchet the ease factor down to its 1.3 floor,
the community name being **"ease hell"** — and states that FSRS "doesn't experience" it.
`OBSERVED` The manual's own claim for FSRS is modest and correctly hedged: *"By more accurately
determining how much information you are likely to forget, it can help you remember more
material in the same amount of time."* It offers **no quantified efficiency gain**, which is
the correct posture given the evidence base.

The manual also documents a real limitation worth carrying into any design: *"FSRS can adapt to
almost any habit, except for one: pressing 'Hard' instead of 'Again' when you forget the
information."* `OBSERVED` The self-report grade is the algorithm's only input about difficulty,
and it is a channel the learner can silently corrupt. §11 treats this as a first-class design
problem.

The only benchmark generation that included SM-2 (19,990 collections, ~703M reviews, Aug 2024)
reported unweighted RMSE(bins) **FSRS-5 = 0.0712 vs SM-2 = 0.199**, with FSRS-5 lower for
**99.0%** of users — with the authors' own caveat that SM-2 emits no probabilities, so a
forgetting curve had to be bolted onto it to score it at all. `MEASURED-BENCH` (F5 §1.4)

### 4.4 Duolingo's Half-Life Regression — read the paper, not the abstract

**Settles & Meeder (2016), "A Trainable Spaced Repetition Model for Language Learning,"
*Proc. ACL 2016*, pp. 1848–1858, `doi:10.18653/v1/P16-1174`.** Full PDF retrieved and read
this session (ACL Anthology `P16-1174.pdf`).

The abstract's headline is: *"reducing error by 45%+ compared to several baselines at
predicting student recall ... and improving learner engagement by 12% in an operational user
study."*

**Both halves of that sentence need unpacking, and the second one is widely misread.**

**The 45% figure is a backtest.** 12.9M instances, first 90% train / last 10% test. Table 2:

| Model | MAE ↓ | AUC ↑ | CORh ↑ |
|---|---|---|---|
| **HLR** | **0.128** | 0.538 | **0.201** |
| HLR −lex | 0.128 | 0.537 | 0.160 |
| HLR −h | 0.350 | 0.528 | −0.143 |
| Leitner | 0.235 | **0.542** | −0.098 |
| Pimsleur | 0.445 | 0.510 | −0.132 |
| LR | 0.211 | 0.513 | n/a |
| **Constant p̄ = 0.859** | **0.175** | n/a | n/a |

`MEASURED-BENCH`. Note the two things the abstract does not say. **Leitner achieved the highest
AUC in the table (0.542), higher than HLR (0.538)** — the paper says so plainly: *"The Leitner
method did yield the highest AUC values among the other baselines."* And **a constant
prediction of 0.859 achieves MAE 0.175, beating every model in the table except HLR itself**
(and its −lex variant). The paper is honest about the range restriction causing this
(p̄ = 0.859, so "most words are recalled correctly"). The 45% error reduction is real but it is
a reduction in MAE relative to Leitner in a regime where predicting a constant is already close.

**The "12% engagement improvement" is not HLR versus Leitner.** This is the finding that
matters and it is buried in §4.3–4.4 of the paper. Two A/B tests were run. Table 4, verbatim,
reporting *change in daily student retention* (percentage change; `*` marks p < 0.001):

| Experiment | Any activity | Lesson | Practice |
|---|---|---|---|
| **I. HLR (v. Leitner)** | +0.3 | +0.3 | **−7.3\*** |
| **II. HLR −lex (v. HLR)** | **+12.0\*** | +1.7\* | +9.5\* |

**Experiment I is the one that tests the paper's actual thesis** — the new algorithm against
the incumbent — and it ran for **six weeks on "just under 1 million students."** Its result:
overall activity +0.3% (unmarked, i.e. not significant at p < 0.001), new lessons +0.3%
(likewise), and **practice sessions −7.3%, significantly *down***. `MEASURED-RCT` (large,
randomized, in production — but with an engagement outcome, not a learning outcome).

The +12.0% headline comes from **Experiment II**, which compares HLR *without* lexeme features
against HLR *with* them — an ablation of one feature set within the new model, run months later
to fix a documented overfitting problem where *"particular words or skills would decay rapidly,
regardless of how often they practiced."*

**`NEGATIVE RESULT`, stated precisely:** in the only randomized comparison of Duolingo's
trained scheduler against the heuristic it replaced, on ~1M students over six weeks, the
trained scheduler produced **no significant change in overall engagement and a significant
7.3% decrease in practice activity**. The authors deployed it anyway, on a stated basis of
*"positive anecdotal feedback about strength meter quality"* plus an interpretation that the
practice drop reflected students no longer needing to grind — a reasonable product judgement,
explicitly not a measurement. **And no learning outcome was measured in either experiment.**
Daily retention is an engagement metric.

Independently, HLR ranks **near the bottom of the Anki benchmark** — RMSE(bins) 0.1275, *worse
than the zero-parameter AVG baseline at 0.1034* (§4.2). `MEASURED-BENCH` Together these make
HLR the cleanest documented case in this survey of a heavily-cited industrial result whose
headline number does not mean what it is usually taken to mean.

### 4.5 MEMORIZE (PNAS 2019) — an excellent theory with an observational evaluation

**Tabibian, Upadhyay, De, Zarezade, Schölkopf & Gomez-Rodriguez (2019), "Enhancing human
learning via spaced repetition optimization," *PNAS* 116(10):3988–3993,
`doi:10.1073/pnas.1815156116`, PMC6410796.** Full text retrieved and read this session via
Europe PMC `fullTextXML`.

The theory is genuinely elegant and worth carrying: modelling review as a marked temporal point
process and solving the resulting stochastic optimal control problem yields (Theorem 3) an
optimal reviewing intensity **u\*(t) = q^(−1/2)·(1 − m(t))** — i.e. **review an item at a rate
proportional to how likely you are to have forgotten it.** That is a clean, closed-form,
implementable policy with a proof behind it, and it is a *different* policy from "review when
recall probability crosses a threshold."

**The evaluation, however, is observational, and the authors say so in the paper's own words:**

> "Although we cannot make actual interventions to evaluate the performance of each method, the
> following insight allows for a large-scale natural experiment: Duolingo uses hand-tuned spaced
> repetition algorithms, which propose reviewing times to the users; however, users often do not
> perform reviews exactly at the recommended times, and thus schedules for some (user, item)
> pairs will be closer to uniform than threshold or MEMORIZE and vice versa."

Design specifics, all verified from the full text: **two weeks** of Duolingo data (~12M
sessions, ~5.3M unique user-word pairs, ~5.2M after filtering to users with ≥30 review events
and words reviewed ≥30 times). Treatment and control groups are constructed **post hoc** by
taking the top 25% of (user, item) sequences by likelihood under each policy. Outcome:
"empirical forgetting rate" computed from the *last* review of each sequence. Reported result:
MEMORIZE beats uniform and threshold, Mann–Whitney U, p < 0.05, presented as box plots — **no
single pooled effect size is reported**. A secondary analysis correlates per-learner
log-likelihood with forgetting rate across **322 learners**.

**Label: `OBSERVED`.** Three limits the authors themselves flag: assignment is by revealed
behaviour, not randomization (they check only that *item difficulty* is balanced between
groups, SI §13 — not learner conscientiousness, motivation, or study volume); the dataset
"spans only 2 wk and that places a limitation on the range of time intervals between reviews
and retention intervals we can study"; and, verbatim, *"it would be interesting to perform
large-scale interventional experiments to assess the performance of our algorithm in comparison
with existing spaced repetition algorithms deployed by, e.g., Duolingo."* None was done in that
paper.

### 4.6 The two real RCTs

These are the only interventional trials of *algorithmic* scheduling with a retention outcome
that this session could locate. Both matter; both have limits that must be stated with them.

**(i) Lindsey, Shroyer, Pashler & Mozer (2014), "Improving students' long-term knowledge
retention through personalized review," *Psychological Science* 25(3):639–647,
`doi:10.1177/0956797613504302`, PMID 24444515.** `MEASURED-RCT` Abstract **verified directly
via PubMed E-utilities this session** (full text UNREACHABLE-IN-SESSION; two author-page PDF
mirrors returned 301/connection failure). The authors' own words:

> "The method was integrated into a semester-long middle-school foreign-language course via
> retrieval-practice software. Using a cumulative exam administered after the semester's end, we
> compared **time-matched** review strategies and found that personalized review yielded a
> **16.5% boost in course retention over current educational practice (massed study)** and a
> **10.0% improvement over a one-size-fits-all strategy for spaced study**."

This is the strongest result in the area and it is genuinely a scheduler result — the
**+10.0%** figure is personalized spacing versus generic spacing, i.e. the comparison that
isolates personalisation, holding *spacing itself* constant. It is the single best existing
counterweight to §4.7's "personalisation is worth ~2%" simulation, and the two should be
reported together rather than either alone.

Its scope limits, stated: middle-school foreign-language vocabulary; item-level cued recall;
one semester; one classroom context. And note what the 16.5%/10.0% split shows — **most of the
benefit comes from spacing at all (massed → spaced), with personalisation adding a further,
smaller increment on top.**

**(ii) Upadhyay, Lancashire, Moser & Gomez-Rodriguez (2021), "Large-scale randomized
experiments reveal that machine learning-based instruction helps people memorize more
effectively," *npj Science of Learning* 6:26, `doi:10.1038/s41539-021-00105-8`, PMC8421401.**
Full text retrieved and read this session.

This is the follow-up that MEMORIZE's authors said was needed, and it is a real RCT:

- **~50,700 consenting learners** aged 18+, studying for the German written driving permit,
  December 2019 – July 2020. **~16.75M answers to ~1,900 questions across ~628,000 sessions.**
- Three arms, randomized at install: **`select`** (ML algorithm chooses which questions enter
  each session; n = 10,151), **`difficulty`** (circular order, easiest first; n = 34,029),
  **`random`** (uniform with replacement; n = 13,600). Learners were blind to condition.
- The algorithm optimizes **which items to include**, not *when* to study — a deliberate design
  choice, since learners control their own study times. Optimal selection probability
  **p\*(t) = (1/q)(1 − m(t))**, the item-selection analogue of MEMORIZE's rate policy.
- **Result:** after controlling for review time and number of reviews, `select` had a lower
  median normalized empirical forgetting rate than the other two arms in **83.5%** of cells,
  significant (Bonferroni-corrected Mann–Whitney) in **66.7%** of cells. Median decrease in
  forgetting rate: **~48% vs. `random`, ~40% vs. `difficulty`**; corresponding median increase
  in half-life: **~92% vs. `random`, ~40% vs. `difficulty`**.
- Engagement: `select` learners were **50.6% more likely** (median) than `random` learners to
  return within 4–7 days — **but were also more likely to stop using the app in the first two
  days**. The authors report this explicitly.

**Four caveats that must travel with this result:**

1. **The abstract's "~69% longer" does not correspond to any single comparison in the paper.**
   The main text reports ~92% (vs `random`) and ~40% (vs `difficulty`) median half-life
   increases. The ~69% figure is not separately derived in the main text. Cite the body numbers.
2. **The baselines are weak, and the authors say so.** `random` and `difficulty` are not spaced
   repetition — they are "shuffle" and "easiest first". This trial shows ML selection beats
   *no scheduling policy at all*; it does **not** show ML selection beats a competent fixed
   spacing schedule. Verbatim from the paper: *"it would also be interesting to compare our
   algorithm with stronger baselines."*
3. **Heavy post-randomization exclusion.** 6,774 reinstallers and 32,445 learners who used the
   app fewer than two days were removed, leaving analysis sets of **1,564 / 7,582 / 2,335**
   learners — roughly 22% of those randomized. Post-randomization exclusion on a
   behaviour-correlated criterion (usage duration) breaks intention-to-treat, and it interacts
   badly with the finding that `select` learners were *more likely to quit in the first two
   days*: the arm with the higher early-dropout rate is also the arm whose survivors are being
   compared.
4. **The outcome is model-derived, not an independent post-test.** "Normalized empirical
   forgetting rate" is computed under the same exponential-forgetting / half-life-regression
   family used to build the treatment policy. This is not fatal — the metric uses only the final
   review — but it is not a held-out achievement test either. There was no driving-permit exam
   score in the analysis.

**(iii) A double-blind trial of an SRS tool — with an instructive confound.**
**Chukharev-Hudilainen & Klepikova (2016), "The effectiveness of computer-based spaced
repetition in foreign language vocabulary instruction: a double-blind study," *CALICO Journal*
33(3), `doi:10.1558/cj.v33i3.26055`, ERIC EJ1143520.** Full text retrieved and read this session
via ERIC.

Design — and it is unusually good for CALL research: **22 third-year EFL cadets** (native
Russian speakers, marine engineering, spring 2012), **112 target lexical units**. Randomization
is *per (student × lexical unit)*: for each unit, each student was independently assigned to
control (classroom presentation only) or experimental (classroom + the spaced-repetition tool),
yielding **596 control and 1,868 experimental participant-to-unit observations**. Both students
and the instructor were blind to which units were in which condition — the authors' explicit
methodological contribution, argued as an import from pharmacology.

Actual usage: **174 seconds per day** (learners were asked for 10 minutes). Mean time for a unit
to reach "learned" status: 107 s (SD = 159), median 71 s.

Result: proportion of units receiving partial or full credit on the posttest —
**experimental 49.9% vs. control 16.9%**, p < 0.001, one-tailed. "Almost threefold," in the
authors' words. `MEASURED-RCT`

**Three things must travel with that number.**
1. **It is confounded with time on task.** The control condition received *no additional
   practice at all*. So this measures "≈3 min/day of spaced retrieval practice vs. nothing," not
   "spaced vs. massed" and certainly not "algorithm A vs. algorithm B." It is a strong result for
   *the practice* and says nothing about *the scheduler*.
2. **The internal dose-response is the interesting part.** Broken down by how far a unit got in
   the system at posttest: still in active acquisition (P) **16.3%** — statistically
   indistinguishable from control's 16.9%; short-term (S) **28.7%**; long-term (L) **50.1%**. The
   benefit is entirely in the units that completed the schedule. `MEASURED-RCT`
3. **`NEGATIVE RESULT` inside a positive study.** Units that reached "long-term memory" status in
   the system scored **50.1%**, significantly *below* words the students already knew before the
   intervention began (**60.7%**, p < 0.001). The authors' own conclusion: *"the students may
   have failed to attain the level of vocabulary knowledge identical to the previously known
   lexical units."* The system's internal "learned" label overstates what the learner can do —
   which is precisely the calibration failure §1.3(a) identifies in ZemoMemo's "stickiness"
   framing, here measured rather than inferred.

**`NEGATIVE RESULT` / the honest bottom line for §4, and it is unchanged from F5 §1.8:** there
is **no controlled evidence that switching scheduling algorithm — SM-2 → FSRS, or Leitner → HLR
— improves any learning outcome.** There is good evidence that modern schedulers predict recall
better, and simulation evidence that they buy the same knowledge for less review time. Those are
three different claims and a survey must not merge them.

### 4.7 Memrise's fixed ladder, and the ceiling on personalisation

One simulation result deserves its own line because it bounds the whole enterprise. The
`SSP-MMC-FSRS` five-year simulation (10,000 cards, 10 new/day; assumes FSRS is perfectly
calibrated) reports cards-memorised-per-hour of study: FSRS at desired retention 0.70 = **18.9**;
FSRS at 0.90 = **13.7**; **Anki SM-2 = 15.0**; **Memrise's fixed 1→6→12→48→96→180-day ladder =
15.6.** `DEMO` (simulation, F5 §1.6)

**Memrise's hand-picked, non-adaptive, non-personalised ladder lands within ~2% of tuned FSRS
and above SM-2.** If that holds, the marginal value of per-user scheduling personalisation is
small compared with the value of *spacing at roughly the right order of magnitude at all*. This
is a `DEMO`-grade result — it is a simulation under FSRS's own memory model, which is a friendly
referee — but it points the same direction as everything else in this section: **the algorithm
is not where the remaining headroom is.**

---

## 5. Retrieval practice — the effect that actually carries the weight

The full treatment is in `B1-learning-science.md` §1. Restated compactly, with the numbers that
the spec in §11 depends on:

| Meta-analysis | Corpus | Effect |
|---|---|---|
| Rowland (2014), *Psych. Bulletin* 140(6):1432–1463, `doi:10.1037/a0037559` | lab-dominated | **g = 0.50, 95% CI [0.42, 0.58]**, I² = 84% |
| Adesope, Trevisan & Sundararajan (2017), *RER* 87(3):659–701, `doi:10.3102/0034654316689306` | practice testing | **g = 0.51 vs. restudy**; g = 0.61 overall; g = 0.93 vs. no activity |
| Yang, Luo, Vadillo, Yu & Shanks (2021), *Psych. Bulletin*, `doi:10.1037/bul0000309` | **222 studies, 48,478 students, classroom** | **g = 0.499, 95% CI [0.442, 0.557]**, I² = 88% |
| Pan & Rickard (2018), *Psych. Bulletin*, `doi:10.1037/bul0000151` | **transfer**: 192 effect sizes, N = 10,382 | **d = 0.40, 95% CI [0.31, 0.50]** |

All `MEASURED-META`. Yang et al. (2021) is the best applied estimate: **g ≈ 0.50 in real
classrooms across ~48,000 students.**

**The boundary conditions are the design brief** (all from B1 §1, verified there):

- **Delay is required.** At immediate test, restudy often wins (Roediger & Karpicke, 2006,
  Exp. 1). The benefit is *invisible or negative* at short delays. A system that shows a
  learner an immediate "you improved!" readout is measuring the wrong thing.
- **Feedback is near-mandatory when retrieval fails.** Rowland (2014); Fiechter & Benjamin
  (2018). Unsuccessful retrieval *without* corrective feedback produces little or negative
  benefit. This is the one place where an LLM is unambiguously, structurally better than a
  flashcard: a card can show you the back; it cannot diagnose *why* you missed it.
- **Recall beats recognition.** Rowland (2014) reports recall tests > recognition tests as a
  moderator. Multiple-choice review is the weak form.
- **Complexity is disputed and unresolved.** van Gog & Sweller (2015) argue the testing effect
  shrinks as element interactivity rises; Karpicke & Aue (2015) rebut. Pan & Rickard's finding
  that transfer is weakest to worked-example problems is partially consistent with van Gog &
  Sweller. **State this as unresolved; do not pick a side.**
- **Engagement is a hard prerequisite.** A 2026 pair of Prolific experiments (PMC12894256) with
  delayed post-tests, corrective feedback, attention checks and fair pay found **no testing
  effect at all**, attributing it to insufficient sustained engagement in crowdsourced settings.
  `MEASURED-RCT`, `NEGATIVE RESULT` This is directly relevant to AI-mediated self-study: the
  effect is contingent on effortful, attentive retrieval — not on the surface form of being
  quizzed.
- **`NEGATIVE RESULT` — a design confound in the founding study.** Soderstrom, Kerr & Bjork
  (2016), *Psych. Science* 27(2):223–230, `doi:10.1177/0956797615617778`, replicated Karpicke &
  Roediger (2008) but controlled the spacing differences inherent to its between-subjects
  design; within-subjects, **both repeated testing and repeated restudy improved learning**.
  The testing effect survives; the strong "restudy does literally nothing" claim does not.

### 5.1 The applied evidence: spacing + retrieval in professional education

Three 2026 sources — all located and read this session via Europe PMC — bring the applied
picture up to date, and together they make the section's central distinction unusually crisp.

**(a) The pooled applied effect is large.** **"The Effectiveness of Spaced Repetition in Medical
Education: A Systematic Review and Meta-Analysis," *The Clinical Teacher* (2026),
`doi:10.1111/tct.70353`.** PRISMA; searched Feb 2025; MERSQI quality assessment. 542 records
screened → 14 studies in the review, **13 in the meta-analysis, 21,415 learners**. Result,
verbatim: **"an overall significant effect in favour of spaced repetition study compared to
standard studying techniques (standardised mean difference = 0.78; 95% CI 0.56–0.99;
p < 0.0001)."** `MEASURED-META`

Note carefully what varied: the interventions were "faculty-created or third-party flash cards,
MCQs delivered via email or as part of a continuing medical education framework, and spaced
classroom quizzes." **The manipulation is spacing-plus-testing as a practice, not a scheduling
algorithm.** The authors' own conclusion asks for exactly the work that has not been done:
*"Further work is required to investigate the optimal design and delivery of spaced repetition
interventions."*

**(b) It transfers to a genuine skill, on a genuine transfer test.** **"Using spaced repetition
to teach histopathology significantly improves diagnostic skills: A randomized within-participant
evaluation," *Anatomical Sciences Education* (2026), `doi:10.1002/ase.70261`.**
`MEASURED-RCT` This is the most impressive design in the whole section: pathology trainees and
certified pathologists were randomized *within participant* to receive spaced-repetition material
for one set of diagnoses and not another, then evaluated **three months later on 20 previously
unseen cases**. Within-participant results (n = 42 paired): **mean 7.3/10 on SR-reviewed
diagnoses vs 5.4/10 on non-reviewed, paired difference +1.9 points, p < 0.001**, and the same
cases completed **1.4 minutes faster (median paired difference, p = 0.018)**.

This matters because it defeats the standard objection that SRS only produces vocabulary-shaped
recall: the outcome is diagnostic accuracy on cases never seen before, at a three-month delay,
in expert practitioners. **Caveat, stated with it:** 337 participants were recruited but only
**79 (23%)** completed the evaluation, and only 46 of those used the SR material. Within-participant
randomization protects the comparison from learner-level selection, but 77% non-completion is a
severe limit on generalizability.

**(c) The observational Anki literature is weaker than its reputation, and contains a null.**
**Frappa et al. (2026), "Anki Use and Academic Performance in Medical Education: A Systematic
Review of Evidence and Learning Theory," *Medical Science Educator*,
`doi:10.1007/s40670-026-02643-5`, PMC13197492.** Eleven studies, qualitatively synthesised.
Three found a consistent positive association between regular Anki use and USMLE Step 1
performance, with **high-frequency users outperforming minimal users by 4–13 points** and one
dose-response by total cards reviewed. `OBSERVED`

But: *"Evidence for university-administered exams was more mixed: some studies found significant
benefits with structured Anki programs, while others reported **no measurable difference despite
positive student perceptions**."* And — **`NEGATIVE RESULT`** — *"Only one study assessed Step 2
CK and **found no significant benefit**."* The authors' own summing-up: *"evidence is largely
observational."*

**The Step 1 / Step 2 CK split is the most diagnostic single fact in this subsection.** Step 1
is the foundational-knowledge exam; Step 2 CK is the clinical-reasoning exam. Anki use tracks
performance on the first and not the second. That is exactly the recognition-strength versus
generative-competence boundary (§9.3) showing up in the wild, in an outcome that costs a career.
It is observational and confounded — but it is the pattern a card-based system would predict.

### 5.2 The generation effect — the mechanism an LLM can actually manipulate

**Bertsch, Pesta, Wiscott & McDaniel (2007), "The generation effect: A meta-analytic review,"
*Memory & Cognition* 35(2):201–210, `doi:10.3758/BF03193441`.** Full PDF retrieved and read
this session. **445 effect sizes, 86 studies, N = 17,711.** `MEASURED-META`

Overall: **d = 0.40, 95% CI [0.38, 0.42]** for generating material versus reading it.

The moderator table is where the design guidance is, and it contains two of this section's
required null results:

| Moderator | Level | d | 95% CI |
|---|---|---|---|
| **Type of test** | Recognition | 0.46 | [0.44, 0.48] |
| | Cued recall | **0.55** | [0.53, 0.57] |
| | Free recall | 0.32 | [0.30, 0.34] |
| **Retention interval** | Immediate | 0.41 | [0.39, 0.43] |
| | Up to 1 min | 0.32 | [0.30, 0.34] |
| | 1 min – 1 day | 0.41 | [0.39, 0.43] |
| | **More than 1 day** | **0.64** | [0.62, 0.66] *(only 30 effects, n = 971 — thin)* |
| **Stimulus type** | Numbers | 0.87 | [0.85, 0.89] |
| | Words | 0.41 | [0.39, 0.43] |
| | **Nonwords** | **0.05** | **[0.03, 0.07]** |
| **Generate rule** | Calculation | 0.92 | [0.90, 0.94] |
| | Sentence completion | 0.60 | [0.58, 0.62] |
| | Word fragment | 0.37 | [0.35, 0.39] |
| | **Anagram** | **−0.05** | **[−0.07, −0.03]** |
| **Number of stimuli** | 25 or fewer | 0.60 | [0.58, 0.62] |
| | **More than 50** | **0.09** | [0.07, 0.11] |
| **Learning type** | Incidental | 0.65 | [0.63, 0.67] |
| | Intentional | 0.32 | [0.30, 0.34] |

**Three `NEGATIVE RESULT`s and one scaling law fall straight out of this table:**

1. **The generation effect is null for nonwords (d = 0.05) and *reverses* for anagrams
   (d = −0.05).** Generation only helps when there is pre-existing semantic structure for the
   act of generating to activate. Manufacturing difficulty *per se* does not help; manufacturing
   *semantically meaningful* difficulty does. This is the sharpest empirical statement of the
   desirable-difficulties boundary anywhere in this section, and it is a direct constraint on
   LLM-generated cues: a cleverly scrambled cue is an anagram, and anagrams do not work.
2. **The effect nearly vanishes with more than 50 items (d = 0.09) versus 25 or fewer
   (d = 0.60).** Generation is a *small-set* technique. This is a hard scaling constraint on
   any "generate everything" system.
3. **The effect *grows* with retention interval (d = 0.64 beyond one day, from 0.41 immediate)**
   — the same delayed-benefit signature as the testing effect, and the same warning against
   immediate-feedback evaluation. Note the thin cell (30 effects, n = 971).

The strongest single cell is **calculation, d = 0.92** — generating a numeric answer by
computing it. That is precisely the class of item a symbolic/executable backend can verify
(cross-reference `F3-executable-verifiable.md`), which is a useful coincidence for §11.

---

## 6. Desirable difficulties — and why the good stuff feels bad

<!-- PENDING: delegated. Inserted on completion. -->

---

## 7. Mnemonics and memory palaces

<!-- PENDING: delegated. Inserted on completion. -->

---

## 8. Knowledge tracing as the modern replacement for fixed schedules

<!-- PENDING: delegated. Inserted on completion. Cross-reference F5 §2. -->

---

## 9. What an LLM changes

This is the constructive core. The claim is specific: **four capabilities became available
essentially at once, and each of them removes a constraint that the flashcard paradigm was
built around.** Each is stated with the guardrail attached.

### 9.1 Generate the cue instead of storing it

**The old constraint.** A flashcard is a persisted (cue, response) pair. Every property of the
scheduler follows from that: you schedule *cards* because a card is the only thing that exists;
you model *card* difficulty because that is the only difficulty you can observe; a "leech" is a
card, not a misunderstanding. And the pair is frozen — the learner eventually learns the *cue*
rather than the *content*. Practitioners have a name for this ("pattern-matching the card") and
Anki's manual documents the adjacent failure mode where a learner's grading habit silently
corrupts the model (§4.3).

**What changed.** A competent model can now manufacture, on demand, a *fresh* cue for the same
underlying proposition — different surface form, different direction, different context,
different modality. The stored object stops being a card and becomes a **claim plus a generator
plus a verifier**.

This is not speculation; it has been built. **SRS-Stories** (arXiv:2512.18362, Dec 2025) takes
the set of words an SRS says are due, and generates a coherent short story that uses exactly
those words, constrained to vocabulary the learner already knows — "effectively replacing
flashcards with enjoyable stories." Evaluated in **English, Chinese and Polish** across three
generation methods and three constraint-enforcement strategies. `DEMO`

**The evidential status of the underlying mechanism — say this plainly.** I searched for, and
**did not find**, a meta-analysis or controlled trial directly comparing *repeated retrieval with
varied cues* against *repeated retrieval with an identical cue* for the same verbal content.
(Europe PMC and Crossref queries this session returned nothing on point; the motor-learning
"variability of practice" literature is a different construct and does not substitute.) The
nearest relevant evidence points in a **complicating** direction: **Pan & Rickard (2018)** find
that retrieval-practice transfer is *weakest* to **rearranged stimulus–response items**
(`MEASURED-META`, d = 0.40 overall for transfer). Read one way that undercuts naive cue
regeneration — practising cue form A may not automatically buy you cue form B. Read the other
way it is the *argument for* rotating cue forms deliberately rather than assuming transfer.
**Either way it is an open empirical question and §11.6's H1 exists to settle it.** I will not
assert the mechanism as established.

**The guardrail, stated with it:** SRS-Stories' evaluation is entirely of *text quality*
(grammaticality, coherence, interestingness, target-word usage) via automatic metrics, an LLM
judge (Qwen2.5-72B-Instruct), and a small human annotation. **No learner, no retention test, no
learning outcome.** The paper's own summary says the task "can be coupled with a Spaced
Repetition System" — the coupling is proposed, not measured. And its own human-vs-LLM-judge
correlations degrade sharply outside English: for coherence, Pearson r = 0.507 (English),
0.426 (Chinese), **−0.149 (Polish)**. `NEGATIVE RESULT` for LLM-as-judge in multilingual
evaluation of exactly this kind of content.

### 9.2 Schedule the concept, not the card

**The old constraint.** Item-level scheduling has no notion that two cards are about the same
thing. If a learner has ten cards derived from one misunderstood idea, an SRS shows all ten,
ten times, and never notices that one explanation would fix all of them.

**What changed.** A model can cluster items by the proposition they test, detect that failures
share a root cause, and schedule the *concept* — choosing at review time which of its many
possible surfaces to present. This inverts the relationship: the scheduler owns a knowledge
component; the item is a disposable sample from it.

**The guardrail:** this moves the system out of the regime where the spacing effect is
best-measured. Donovan & Radosevich (1999) found spacing effects shrink markedly for complex
material (d = 0.11–0.42 for complex motor tasks versus much larger for simple verbal material),
and Bertsch et al. (2007) found the generation effect nearly vanishes past 50 items. **Concept
scheduling is a bet that the mechanisms transfer up the complexity ladder, and that bet is not
yet backed by evidence.** §11 makes it falsifiable rather than assumed.

### 9.3 Distinguish recognition strength from generative competence

**The old constraint.** An SRS observes exactly one bit per review — "did the learner say they
got it." Anki's manual concedes the resulting fragility outright: FSRS "can adapt to almost any
habit, except for one: pressing 'Hard' instead of 'Again' when you forget the information."
`OBSERVED` A self-graded recognition judgement is the weakest possible evidence of knowing.

**Why the distinction is real and not a metaphor.** The measured moderators line up:
Rowland (2014) finds recall tests produce larger testing effects than recognition tests;
Bertsch et al. (2007) find the generation effect largest for **cued recall (d = 0.55)** and
smallest for **free recall (d = 0.32)**, with **recognition at 0.46** — i.e. the format changes
the effect by a factor of ~1.7. And Pan & Rickard (2018) find transfer at **d = 0.40**, robustly
weaker than retention, and *weakest to rearranged stimulus–response items* — which is precisely
the operational definition of "learned the card, not the content."

**What changed.** A model can now ask for a *free* production — "explain this", "derive it",
"apply it to a case you have not seen" — and grade it. That converts the one-bit channel into a
rich one: a system can observe that a learner reliably recognises a definition but cannot
produce an instance, and treat those as two different states of the same knowledge component
rather than one.

**The guardrail:** grading free production is exactly where LLM judging is least reliable and
where `C2-assessment-psychometrics.md` sets the constraints. Free-response grading must be
treated as a measurement with a known error rate, not as ground truth. See §11's storage schema,
which keeps the raw response so the grade can be re-derived when the grader improves.

### 9.4 Author retrieval practice at the speed it is consumed

The bottleneck on retrieval practice has never been the evidence — it has been that writing good
questions is slow. That constraint is gone, and there is now a direct (if imperfect) measurement.

**"Enhancing Student Learning with LLM-Generated Retrieval Practice Questions: An Empirical
Study in Data Science Courses"** (arXiv:2507.05629v2, Jul 2025). Full PDF read this session.
Two college-level data science courses, **~60 students**, weeks 6–9 of a quarter, run as
2-week cycles: in the practice week, 120-minute lectures were broken into 10–15-minute segments
with LLM-generated MCQs and immediate feedback at each segment boundary; in the control cycle,
none. Quiz accuracy: **89% with LLM-generated retrieval practice vs 73% without — a
16-percentage-point difference.**

**Label: `OBSERVED` (quasi-experimental), not `MEASURED-RCT`.** The authors are candid:
*"The absence of true random assignment means that unmeasured confounding variables could
potentially influence the observed effects, as pre-existing differences between sections cannot
be entirely ruled out."* Three further limits, two of which they state: small n; the two cycles
covered **different course material**, so the comparison is confounded with topic difficulty;
and the assessment window is ~1 week, so this measures short-term retention.

**And the interpretive point that matters most:** this study varied *retrieval practice vs. no
retrieval practice*. The LLM's role was **authoring**. It is therefore a (further) demonstration
of the testing effect plus a demonstration that LLM authoring is a viable production route — it
is **not** evidence that LLM-generated items are better than human-written ones. The authors'
own §5.1 is a list of quality failures they encountered, and their conclusion is explicit:
*"Instructors must still manually verify and revise the generated questions before releasing
them to students."*

A related capability result: **SmartPhone** (arXiv:2305.10436) auto-generates keyword-mnemonic
verbal and visual cues with an LLM and compares them to manually generated cues in a human
experiment — the first end-to-end pipeline for a mnemonic technique that previously required
manual authoring. See §7 for what the keyword-mnemonic evidence base actually supports.

### 9.5 What is *not* yet demonstrated — say it in the same breath

**LECTOR** (arXiv:2508.03275, Aug 2025) is instructive as a cautionary example. It proposes an
LLM-enhanced concept-based scheduler that uses semantic similarity to reduce interference
between confusable vocabulary items — a genuinely good idea, and one that §11 borrows. Its
reported result: **90.2% success rate vs 88.4% for the best baseline (SSP-MMC), a 2.0% relative
improvement**, evaluated "across six baseline algorithms (SSP-MMC, SM2, HLR, FSRS, ANKI,
THRESHOLD) across **100 simulated learners over 100 days**."

**Label: `DEMO`.** One hundred *simulated* learners. The simulator embodies a memory model; the
scheduler is optimised against that model; the result is that the scheduler is good at the
model. This is a legitimate way to explore a policy space and an illegitimate way to claim a
learning gain. The 2.0% figure must never be restated as a finding.

**Irec** (arXiv:2506.20156) is similarly a "conceptual framework and system prototype" for
context-triggered recall of a learner's own past insights via a knowledge graph plus LLM
similarity filtering — a good idea for the *retrieval-cue* problem, with no efficacy evaluation.
`DEMO`

### 9.6 Summary of §9

| Capability | Status | Best evidence found | Label |
|---|---|---|---|
| Generate a fresh cue for a stored claim | **built** | SRS-Stories (arXiv:2512.18362) | `DEMO` — text quality only |
| Author retrieval practice at scale | **built and partially measured** | arXiv:2507.05629, 89% vs 73%, ~60 students | `OBSERVED` (quasi-exp., confounded) |
| Auto-generate mnemonic cues | **built** | SmartPhone (arXiv:2305.10436) | `DEMO` (see §7 for the underlying technique's evidence) |
| Schedule concepts using semantic similarity | **prototyped** | LECTOR (arXiv:2508.03275) | `DEMO` — 100 *simulated* learners |
| Context-triggered recall of prior insights | **prototyped** | Irec (arXiv:2506.20156) | `DEMO` — no evaluation |
| Grade free production to separate recognition from competence | **buildable now** | no efficacy study located | — |
| Detect inert vs. merely unretrieved knowledge | **buildable now** | no efficacy study located | — |

**The pattern is stark and it is the section's central opportunity:** every LLM-native
remembering capability is at `DEMO` or confounded-`OBSERVED`. **Nobody has run the trial.** That
is not a reason for pessimism — it is an unusually clean, unclaimed empirical opening, and §11
is written so that entering it produces a falsifiable answer rather than another demo.

---

## 10. Forgetting as a feature

Every scheduler in §4 treats forgetting as the enemy. The memory literature does not.

**Richards & Frankland (2017), "The Persistence and Transience of Memory," *Neuron* 94(6),
`doi:10.1016/j.neuron.2017.04.037`.** `INFERENCE` from a theoretical review (verified via
Europe PMC this session; it is a review, not an experiment, and is labelled accordingly). Their
argument, verbatim from the abstract: transience *"(1) enhances flexibility, by reducing the
influence of outdated information on memory-guided decision-making, and (2) prevents overfitting
to specific past events, thereby promoting generalization. According to this view, the goal of
memory is not the transmission of information through time, per se. Rather, the goal of memory
is to optimize decision-making. As such, transience is as important as persistence in mnemonic
systems."*

**Retrieval-induced forgetting** is the mechanism that makes this operationally urgent for any
review system: retrieving a subset of items causes forgetting of *related, non-retrieved* items.
The meta-analysis is **Murayama, Miyatsu, Buchli & Storm (2014), "Forgetting as a consequence of
retrieval: A meta-analytic review of retrieval-induced forgetting," *Psychological Bulletin*
140(5):1383–1409, `doi:10.1037/a0037505`, PMID 25180807.** The abstract (verified this session)
concludes that results "largely supported inhibition accounts but also provided some challenging
evidence, with the nature of the results often varying as a function of how retrieval-induced
forgetting was assessed." **The pooled effect size is not stated in the abstract and the full
text was UNREACHABLE-IN-SESSION (paywalled). I could not verify a number and will not supply
one.** `MEASURED-META` (existence and direction only).

The design implication survives the missing number: **a review queue is a competition.** Drilling
card A does not leave card B where it was — if B is semantically related to A and not itself
retrieved, B can be actively suppressed. Item-level schedulers are structurally blind to this
because they model items as independent. (MEMORIZE's authors flag the same gap from the other
direction: *"we assumed that, by reviewing an item, one can influence only its recall probability
and forgetting rate. However, items may be dependent."*) A concept-level scheduler that knows
which items are semantically adjacent can, uniquely, schedule the *neighbourhood*.

### 10.1 When should a system let something go?

The honest answer is that no measured decision rule exists, so §11 specifies one that is
*falsifiable* rather than pretending one is established. The defensible components:

1. **When the goal has passed.** Cepeda et al. (2008) make retention interval a first-class
   input. If a learner's stated horizon for a topic has elapsed and no new goal references it,
   continued review is spending the learner's most finite resource on a settled question.
   `INFERENCE` from `MEASURED-RCT`.
2. **When the item is a leech and the *concept* is not.** Anki's leech mechanism suspends a
   card after N lapses. That is the right instinct at the wrong granularity: repeated failure on
   one surface form, while sibling items on the same concept succeed, is evidence about the
   *item* (bad cue, ambiguous phrasing, mis-scoped card), not about the learner. The correct
   action is to retire the item and re-sample the concept — which requires a generator (§9.1).
   `INFERENCE`
3. **When the knowledge has become externally available and non-load-bearing.** Not everything
   should be in a head. A remembering system that cannot distinguish "must be automatic" from
   "must be recognisable when encountered" from "must be findable" will schedule all three
   identically and waste the learner's life on the third. `INFERENCE`
4. **When retention is being bought at a ruinous exchange rate.** The DR-workload table (§4.7,
   `DEMO`) shows knowledge rising only **+8%** (6,676 → 7,218 cards) between desired retention
   0.85 and 0.99 while workload rises **4.9×**. Above ~0.90, the system is buying very little
   with a great deal. Anki's own manual concurs: above 97% "the workload can be overwhelming."
5. **When forgetting is the point.** Superseded knowledge — a deprecated API, a retracted
   result, a misconception the learner once held — should be *actively* scheduled out. No
   current system has an "unlearn" primitive. Retrieval-induced forgetting suggests one is
   mechanically available: retrieve the correct neighbour repeatedly and the competitor is
   suppressed.

---

## 11. Specification: a remembering subsystem

This is the deliverable. It is written to be built and to be *falsified*.

### 11.0 Design commitments, and the evidence each rests on

| Commitment | Rests on | Label |
|---|---|---|
| Space reviews; never mass them for durable goals | Cepeda 2006, 271 comparisons, 12 exceptions | `MEASURED-META` |
| Set the gap from a **stated retention horizon**, at 20–40% of a 1-week horizon down to 5–10% of a 1-year horizon | Cepeda 2008, N > 1,350 | `MEASURED-RCT` |
| Make every exposure a **retrieval**, not a re-read | Yang 2021, g = 0.499, 222 studies, 48,478 students | `MEASURED-META` |
| Always give **corrective feedback** on failure | Rowland 2014; Fiechter & Benjamin 2018 | `MEASURED-META` |
| Prefer **production** over recognition | Rowland 2014 moderator; Bertsch 2007 (cued recall 0.55 > recognition 0.46 > free recall 0.32) | `MEASURED-META` |
| Make the learner **generate**, but only over meaningful semantic structure | Bertsch 2007, d = 0.40 overall; **nonwords 0.05, anagrams −0.05** | `MEASURED-META` |
| Keep generation sets **small** | Bertsch 2007: >50 items → d = 0.09 | `MEASURED-META` |
| Do **not** assume expanding intervals are required | §3 | see §3 |
| Do **not** claim the scheduling algorithm is the source of the gain | §4.6 | `NEGATIVE RESULT` |
| Treat item validity as an instrumented property | arXiv:2507.05629 §5.1; C2 | `OBSERVED` |

### 11.1 What it stores

The unit is **not a card.** Three tables:

**`concept`** — the schedulable object.
- `id`, `statement` (the proposition, in prose), `prerequisites[]`, `domain`
- `provenance` — where in the source material this came from (required for grounding; see F3)
- `verification_mode` — one of `symbolic` | `executable` | `reference-text` | `rubric` | `none`.
  This determines how a free response can be graded and how much to trust the grade.
- `retention_horizon` — the learner's stated goal date, or `indefinite`. **Required.** Without
  it there is no principled gap ratio (Cepeda 2008).
- `criticality` — `automatic` | `recognisable` | `findable`. Governs whether the concept is
  scheduled at all (§10.1.3).

**`competence_state`** — per (learner, concept). This replaces the single "ease/stability" scalar
with the distinction §9.3 argues for:
- `recognition_strength` — updated from cued/recognition attempts
- `generative_strength` — updated from free-production attempts
- `last_retrieval_at`, `retrieval_count`, `lapse_count`
- `interference_set[]` — concepts whose items have been observed to be confused with this one
- `inert_flag` — set when `recognition_strength` is high and `generative_strength` is low across
  ≥3 distinct generated cue *forms* (see §11.3)

**`attempt`** — append-only, one row per retrieval event. Stores the **generated cue itself**,
the **raw learner response**, the grade, the grader identity and version, latency, and the cue's
`form` and `difficulty_estimate`. Storing the raw response is not optional: it is what allows a
grade to be re-derived when the grader improves, and it is what makes the falsification test in
§11.6 possible after the fact.

**No card table exists.** Items are generated, used, scored, and discarded. What persists is the
concept, the competence state, and the evidence trail.

### 11.2 What it schedules, and on what signal

**It schedules concepts. It generates items at review time.**

```
due_at(concept, learner) = last_retrieval_at + gap
gap                      = ratio(retention_horizon) × horizon_remaining
ratio                    = 0.30 for horizon ≲ 1 week,
                           declining to 0.075 for horizon ≳ 1 year   [Cepeda 2008]
```

...then modulated, in this priority order:

1. **Prerequisite gating.** A concept is not scheduled while its prerequisites are below
   threshold. Nothing in §4's algorithms does this; it is the single largest structural
   difference from an SRS.
2. **Interference spacing.** Concepts in the same `interference_set` are not co-scheduled in the
   same session. Motivation: retrieval-induced forgetting (§10) and LECTOR's semantic-confusion
   hypothesis (`DEMO`, §9.5). **This is a bet and it is listed in §11.6 as testable.**
3. **Modality/form rotation.** Consecutive reviews of a concept use *different* cue forms
   (recognition → cued production → free production → application). This is what prevents
   learning the cue.
4. **A calibrated recall-probability model as a *tiebreaker only*.** Given §4.2 — a zero-parameter
   moving average is competitive with FSRS-7 — the system uses the simplest model that is well
   calibrated and does **not** invest in scheduler sophistication. Start with FSRS-6/7 or a
   logistic regression over the `attempt` features; treat the choice as low-stakes, because the
   evidence says it is.

**The signal is not a self-report grade.** It is the graded outcome of a generated retrieval, plus
response latency, plus which cue form was used. This is exactly the "richer input" that RWKV-P's
benchmark win points at (§4.2, finding 4) — answer duration and cross-item context — obtained
here by design rather than by scraping it out of logs.

### 11.3 Detecting inert knowledge

**"Inert" means: reliably recognised, not usable.** Operationally:

> `inert_flag` is set when a concept's `recognition_strength` is above threshold while
> `generative_strength` remains below threshold across **≥3 distinct generated cue forms** on
> **≥2 separate days**.

The multi-form, multi-day requirement is what distinguishes *inert* (a stable state of the
knowledge) from *merely unretrieved* (a transient retrieval failure). A single failure on a
single cue is noise — the whole point of Bjork & Bjork's retrieval-strength/storage-strength
distinction is that momentary inaccessibility is not loss (§6).

**The response to `inert_flag` is not more review.** It is re-teaching in a different
representation — a worked example, a concrete instance, an application, a laddered explanation
(cross-reference `F10-explanation-laddering.md`). Scheduling more retrievals of knowledge that is
retrievable but unusable is the failure mode this whole specification exists to fix.

### 11.4 The item generator and its verifier

Every generated cue passes three gates before it reaches a learner:

1. **Groundedness** — the cue and its expected answer must be entailed by the concept's
   `provenance` source. (F3's grounding ladder.)
2. **Verifiability** — if `verification_mode` is `symbolic` or `executable`, the answer is
   checked by a CAS or an interpreter, not by a language model. Bertsch's strongest single cell
   is **calculation, d = 0.92** — the item type with the highest generation effect is also the
   item type a machine can verify exactly. Prefer it wherever the domain allows.
3. **Semantic legitimacy** — the difficulty must come from *meaning*, not from surface
   scrambling. Bertsch: **anagrams d = −0.05, nonwords d = 0.05.** A generated cue that is merely
   obfuscated is not a desirable difficulty; it is an anagram, and anagrams do not work. This gate
   is checkable: a cue whose answer can be recovered by string manipulation of the cue is rejected.

Item-quality telemetry is mandatory: per-item discrimination, per-generator acceptance rate,
and human-review sampling rate, reported to the learner-facing surface. Grounding: the one
measured LLM-generated-retrieval-practice study concludes *"Instructors must still manually
verify and revise the generated questions"* (§9.4). Building the verification loop into the
system is how that constraint is met at scale rather than waived.

### 11.5 What it lets go

Retirement rules, executed in this order, each with its evidence status:

| Rule | Action | Basis |
|---|---|---|
| `retention_horizon` elapsed and no live goal references the concept | stop scheduling; keep state | Cepeda 2008 `MEASURED-RCT` |
| `criticality = findable` | never schedule; index instead | `INFERENCE` |
| Item fails repeatedly while sibling items on the same concept succeed | retire the **item**, re-sample the concept | `INFERENCE` (corrects Anki's card-level leech) |
| Concept superseded / marked incorrect | schedule the **correct neighbour** to suppress the competitor | `INFERENCE` from retrieval-induced forgetting (§10) — effect size unverified |
| Desired retention would exceed ~0.90 | refuse; show the learner the workload curve | `DEMO` (simulation) + Anki manual `OBSERVED` |

### 11.6 The falsifiable claim that distinguishes this from Anki

Everything above is design. This is the part that makes it science.

> **H1 (the primary claim).** For conceptual material with a stated retention horizon of ≥ 8
> weeks, a **concept-scheduled, generated-cue, production-graded** system produces higher scores
> on a **held-out, human-authored, never-before-seen transfer test** than a card-scheduled system
> running FSRS over items generated once from the same source material, **at equal total learner
> time on task**.

Design that makes it a real test, not a demo:

- **Randomize learners, not items.** Two arms. Same source material, same total minutes, same
  corrective feedback, same LLM for authoring. The *only* difference is scheduling granularity
  and cue regeneration.
- **The outcome test is authored by humans who never saw either system's items, and is
  administered at ≥ 8 weeks.** Not a quiz drawn from the item pool. This is the specific
  methodological failure of §9.4's quasi-experiment (topic-confounded, ~1-week window) and of
  §4.5–4.6's forgetting-rate metrics (model-derived, not held-out).
- **Pre-register the exclusion rule and analyse intention-to-treat.** §4.6's RCT excluded ~78% of
  randomized learners post hoc on a behaviour-correlated criterion in the same paper that
  reported one arm having higher early dropout. Do not repeat that.
- **Pre-register the primary outcome as the transfer test.** Engagement, streaks, cards/day and
  review counts are secondary and may not be substituted. Settles & Meeder's headline number is
  an engagement metric; that is how a −7.3% practice result became a "+12% improvement" in
  citation.

**Falsification conditions, stated in advance:**

- **If H1 fails**, the honest conclusion is that concept scheduling adds nothing over item
  scheduling, and the right product is a *better-authored, better-fed-back* flashcard system —
  which the evidence in §5 says would still be worth building, because retrieval practice at
  g ≈ 0.50 is a real effect and most learners get none of it.
- **If H1 succeeds but the ablation** (concept scheduling **with** frozen items, versus concept
  scheduling **with** regenerated items) **shows no difference**, then cue regeneration is not the
  mechanism, and the gain is from grouping and prerequisite gating.
- **If both arms beat a no-review control by similar margins**, then the finding is the one this
  section has been converging on all along: **the gain is spacing and retrieval, and the
  scheduler is a rounding error.** That would be a genuinely useful negative result, and it is
  the outcome most consistent with §3, §4.2, §4.6 and §4.7.

**Three secondary, independently falsifiable claims:**

- **H2 (interference).** Co-scheduling semantically adjacent concepts in the same session
  produces *lower* retention of the non-retrieved neighbour than spacing them apart. Tests
  retrieval-induced forgetting as an engineering constraint. Currently `INFERENCE`.
- **H3 (inert detection).** Learners flagged `inert` benefit more from re-representation
  (worked example / laddered explanation) than from additional retrieval attempts, relative to
  non-flagged learners. Tests §11.3.
- **H4 (horizon).** Setting the gap ratio from a stated retention horizon (Cepeda 2008) beats a
  fixed ratio at equal review count. This is the one place where the *scheduling* literature
  makes a prediction that no shipped SRS implements — and it is a cheap experiment.

### 11.7 What this specification deliberately does not do

- **It does not invest in scheduler sophistication.** §4.2: a zero-parameter moving average
  matches FSRS-7 on calibration; a 34-feature logistic regression beats it. §4.7: Memrise's fixed
  ladder is within ~2% of tuned FSRS in simulation. Effort spent on the arithmetic has a
  measured near-zero return.
- **It does not claim mnemonic techniques as a core mechanism.** See §7.
- **It does not present felt fluency as evidence.** See §6.
- **It does not schedule everything.** `criticality = findable` means the system's most valuable
  act is often to decline.

---

## 12. Negative and null results register

<!-- Assembled after delegated sections land. -->

---

## 13. Bibliography

<!-- Assembled after delegated sections land. -->

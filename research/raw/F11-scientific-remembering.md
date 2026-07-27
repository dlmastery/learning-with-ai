---
title: "Scientific remembering: what the evidence supports, what spaced-repetition software actually does, and what an LLM makes newly buildable"
wave: F
section: F11
date_researched: 2026-07-27
sources_count: 126
status: raw-research
---

# F11 — Scientific remembering

> **Retrieval note.** WebSearch budget was exhausted before this section began.
> **OpenAlex** returned `Rate limit exceeded — Insufficient budget` (daily credit exhausted)
> and **Semantic Scholar** returned `429 Too Many Requests` throughout; neither was usable.
> Retrieval therefore ran on **arXiv** (HTTPS only — the HTTP endpoint returns a 301 with an
> empty body), **Crossref**, **Europe PMC** (including `fullTextXML`), **PubMed E-utilities**,
> **ERIC**, **ACL Anthology**, **GitHub via authenticated `gh api`**, targeted `WebFetch`, and
> local `pdftotext -layout` extraction of downloaded PDFs, plus the **Wayback Machine** and the
> **HAL** and **theses.fr** APIs where publisher hosts blocked access. `hal.science` sits behind
> an Anubis anti-bot challenge that returns 403 to both `curl` and `WebFetch`; several publisher
> hosts (SAGE, ScienceDirect, ACM DL, `laplab.ucsd.edu`) returned 403. Sources that could not be
> reached are flagged **UNREACHABLE-IN-SESSION** at the point of use, listed together in §12.7,
> and their numbers are **never reconstructed from memory**. Where a figure appears only inside a
> published chart rather than in text, it is not quoted as a value.
>
> **Corrections made during this session, recorded rather than silently absorbed.** (1) B1's
> expanding-vs-uniform figure was initially recorded here as unverified; it was subsequently
> **verified** through two independent routes (§3.1). (2) An earlier draft of §4.6 quoted
> Lindsey et al.'s "16.5%" as percentage points; the paper does not say which, and the axis
> arithmetic indicates a **relative** reading — corrected, with the inference labelled (§4.6i).
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

Four findings organise this section.

**First: the effects that are real are the *practices*, not the *schedulers*.** Spacing and
retrieval practice are among the best-replicated findings in all of educational psychology,
with pooled effect sizes in the g = 0.5–0.75 range across hundreds of studies and tens of
thousands of learners. The *scheduling algorithm* that decides which day a card resurfaces
has, by contrast, almost no interventional evidence behind it at all. What it has instead is
a very large, very honest, publicly reproducible **backtest** — predictive accuracy on 350
million historical review events. Those are different quantities. A backtest tells you the
model is well calibrated. It does not tell you a learner ends the year knowing more.

**Second: the specific piece of folklore that spaced-repetition software is *named after* —
expanding intervals — is the piece with the least support, and the variable that *is* supported
is the one every product gets backwards.** §3 verifies rather than assumes that claim, against
primary experiments rather than a citation, and recovers the mechanism: what matters is **how
long you wait before the first retrieval**, not how the intervals grow afterwards. Karpicke &
Roediger (2007, Exp. 3) found that delaying the first test improved long-term retention
*regardless of how the repeated tests were spaced*. Anki's 1-day/6-day graduating defaults, and
every expanding ladder descended from Leitner, do the opposite. That is a one-parameter change,
and it is the cheapest experiment in this document (§11.6, H4).

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

**And a fourth thread runs underneath all three, because it decides whether any of this survives
contact with a product organisation.** The techniques that produce durable memory reliably *feel
worse* than the ones that do not — and the divergence has been measured. In a randomized
crossover in college physics, the same instructional change moved **actual learning up 0.46 SD
and the feeling of learning down 0.56 SD** (Deslauriers et al. 2019, §6.1). In a spacing
experiment, **78% of participants performed better with spacing and 78% said massing was as good
or better** (Kornell & Bjork 2008, §6.2). Font size moves judgements of learning by ηp² = 0.45
and recall by nothing, and **two full study–test cycles do not reduce the illusion** (Rhodes &
Castel 2008, §6.4). This is not a footnote: it is why §4.4's headline Duolingo result — a
*measured* −7.3% practice metric shipped on the strength of *"positive anecdotal feedback"* — is
the field's most instructive failure. Any system optimised on satisfaction, streaks, or
self-rated confidence will be driven, measurably, toward the thing that does not work. The
constructive move, and it is newly available, is in §6.5: **show each learner their own
confidence-versus-outcome divergence.** Metacognitive calibration stops being an exhortation and
becomes a measurement fed back to the person it is about.

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

### 3.1 The meta-analytic number: **VERIFIED**

The published *Educational Psychology Review* article is paywalled, and the HAL record
`hal-02976100` is **metadata-only with no attached file** (confirmed via the HAL search API:
`fileMain_s: null`) — so the "HAL preprint" does not exist as a document. `hal.science` itself
sits behind an Anubis anti-bot challenge that returned 403 interstitials to both `curl` and
`WebFetch`. The number was nevertheless verified by **two independent routes**:

1. **The published abstract**, via the ERIC-indexed record **EJ1310148**, verbatim: *"Results from
   subset 2 indicated **no significant difference between expanding and uniform spacing schedules
   of retrieval practice (g = 0.034)**."*
2. **Latimier's PhD thesis** (HAL `tel-02461323`, NNT 2019PSLEE088; supervisors Ramus and Casati),
   which contains the same meta-analysis and was retrieved **through the Wayback Machine** since
   the live host blocks fetching.

**Full results, from the thesis:** `MEASURED-META`

| Subset | k (studies) | g | 95% CI | p | I² | Publication bias |
|---|---|---|---|---|---|---|
| 1. Spaced vs. massed retrieval practice | 39 (11) | **1.02** | [0.68, 1.36] | < .01 | 51.1% | **Egger t = 4.41, p < .0001 — asymmetric** |
| 1. Trim-and-fill corrected | 49 | **0.74** | [0.55, 0.92] | < .0001 | 48.2% | — |
| 2. Spaced RP vs. spaced restudy | 16 (3) | 0.46 | [−0.41, 1.33] | 0.15 | 0% | df = 1.93; authors flag results unreliable when df < 4 |
| **3. Expanding vs. uniform** | **54 (16)** | **0.032** | **[−0.10, 0.17]** | **0.62** | **0%** | **Egger t = −0.44, p = 0.66 — symmetric, no bias** |

Thesis reports 0.032; the published paper reports 0.034 — a trivial re-run difference, **not two
findings.** The B1 claim is therefore **confirmed as stated**.

**Three things about that row deserve emphasis, and two of them cut *for* the null:**

- **I² = 0%.** Unlike almost every other estimate in this document (Rowland I² = 84%, Yang
  I² = 88%, the interleaving meta I² = 77%), the expanding-vs-uniform estimate has **no detectable
  heterogeneity**. The studies agree that there is nothing there.
- **No publication-bias asymmetry** (Egger p = 0.66) — in contrast to subset 1, where the
  spaced-vs-massed effect *was* asymmetric and dropped from g = 1.02 to g = 0.74 under
  trim-and-fill. So the null is not a bias artefact, and the positive result next to it partly is.
- Effect sizes ranged **g = −0.53 to +1.02**, with **55% positive, 43% negative, 1 zero** — a
  distribution centred on zero, not a suppressed positive.

**The one moderator that moved — and it is the honest caveat.** Number of exposures per item:
**> 4 exposures (k = 25): g = 0.20 [−0.07, 0.46], p = 0.12**; **≤ 4 exposures (k = 26):
g = −0.04 [−0.17, 0.09], p = 0.52**. The moderator test itself is **p = 0.09** and the authors call
it *"tentative."* Retention interval was **not** a moderator (β = 0.02 [−0.13, 0.16]). So the most
that can be said in expansion's favour is: *if* there is an effect, it may live at higher exposure
counts, and even there the CI includes zero.

What follows next is an independent test of whether the meta-analytic null is consistent with the
primary experimental literature — which also recovers the mechanism.

### 3.2 The primary experiment — and it is unusually decisive

**Karpicke & Roediger (2007), "Expanding retrieval practice promotes short-term retention, but
equally spaced retrieval enhances long-term retention," *Journal of Experimental Psychology:
Learning, Memory, and Cognition* 33(4):704–719, `doi:10.1037/0278-7393.33.4.704`,
PMID 17576148.** `MEASURED-RCT` Abstract verified via PubMed E-utilities; **full text retrieved
and read** from the authors' institutional archive (`psychnet.wustl.edu`). Washington University
undergraduates; vocabulary word–definition pairs in a continuous paired-associate task.

The abstract is quoted in full because every clause is load-bearing:

> "Expanding retrieval practice (T. K. Landauer & R. A. Bjork, 1978) is regarded as a superior
> technique for promoting long-term retention relative to equally spaced retrieval practice. In
> Experiments 1 and 2, the authors found that **expanding retrieval practice of vocabulary word
> pairs produced short-term benefits 10 min after learning, conceptually replicating Landauer and
> Bjork's results. However, equally spaced retrieval produced superior retention 2 days later.**
> This pattern occurred **both with and without feedback** after test trials. In Experiment 3, the
> 1st test occurred immediately or after a brief delay, and repeated tests were expanding or
> equally spaced. **Delaying the first test improved long-term retention, regardless of how the
> repeated tests were spaced. The important factor for promoting long-term retention is delaying
> initial retrieval to make it more difficult, as is done in equally spaced retrieval but not in
> expanding retrieval. Expanding the interval between repeated tests had little effect on
> long-term retention in 3 experiments.**"

**The actual cell means** (proportion correct, SE in parentheses):

**Experiment 1 (n = 48, no feedback):**

| Condition | 10 min | **2 days** |
|---|---|---|
| Massed (0–0–0) | .47 (.06) | .20 (.04) |
| **Expanding (1–5–9)** | **.71 (.05)** | .33 (.05) |
| **Equal (5–5–5)** | .62 (.07) | **.45 (.05)** |
| Single immediate (1) | .65 (.05) | .22 (.04) |
| Single delayed (5) | .57 (.06) | .30 (.04) |

Spacing × retention-interval **interaction F(1,46) = 7.23, ηp² = .14.** Expanding wins at 10 min
(.71 vs .62, **d = 0.30**); **equal wins at 2 days (.45 vs .33, d = 0.50).**

**Experiment 2 (n = 48, *with* feedback)** — the crossover is not a feedback artefact:

| Condition | 10 min | **2 days** |
|---|---|---|
| Massed | .49 (.05) | .19 (.05) |
| **Expanding (1–5–9)** | .90 (.02) | .49 (.06) |
| **Equal (5–5–5)** | .87 (.03) | **.60 (.05)** |

Interaction F(1,46) = 6.18, ηp² = .12. At 2 days, **d = 0.41 favouring equal spacing.**

**Experiment 3 (n = 56) — the decisive de-confound.** Crosses first-test delay (0 vs 5) ×
repeated-test schedule (expanding vs equal):

| Condition | 10 min | **2 days** |
|---|---|---|
| Immediate-first, expanding (0–1–5–9) | .62 (.05) | .43 (.06) |
| Immediate-first, equal (0–5–5–5) | .66 (.05) | .45 (.06) |
| **Delayed-first**, expanding (5–1–5–9) | .63 (.05) | **.51 (.05)** |
| **Delayed-first**, equal (5–5–5–5) | .61 (.05) | **.52 (.05)** |

Two-day ANOVA: **main effect of delaying the first test F(1,27) = 6.26, ηp² = .19** (52% vs 44%,
**d = 0.35**); **no effect of repeated-test schedule and no interaction (both F < 1).**

**And the mechanistic finding that kills the desirable-difficulty story for expanding schedules.**
Response times **decreased** across repeated tests in *both* conditions (Exp. 1: expanding
3428 → 3233 → 2966 ms; equal 3579 → 2988 → 2716 ms). **Expanding intervals did not make retrieval
progressively harder** — the premise the entire technique rests on is false in the data. The
authors' conclusion: *"the important factor for promoting long-term retention is delaying initial
retrieval to make it more difficult, as is done in equally spaced retrieval but not in expanding
retrieval."*

**Three conclusions follow:**

1. **The expanding-interval advantage is a short-delay artefact.** It replicates at 10 minutes and
   reverses at 2 days. Since a spaced-repetition system's entire purpose is long-delay retention,
   the regime in which expansion wins is the regime the product does not care about.
2. **The active variable is the delay to the *first* retrieval, not the expansion of subsequent
   ones.** Experiment 3 dissociates them cleanly: delaying the first test helped **regardless of
   how the repeated tests were spaced**. Expansion works *only* insofar as it is confounded with
   first-test timing — and it is confounded in the *wrong direction*, because an expanding schedule
   by construction puts the first test **soonest**.
3. **The stated mechanism is not the operating mechanism.** Expanding schedules are justified in
   every textbook and every product blog as "progressively increasing retrieval difficulty."
   Response latencies say they do the opposite.

### 3.3 Corroboration from an independent lab

**Logan & Balota (2008/2009), "Expanded vs. equal interval spaced retrieval practice: exploring
different schedules of spacing and retention interval in younger and older adults,"
*Aging, Neuropsychology, and Cognition*, PMID 18421627.** `MEASURED-RCT` Abstract verified directly
via PubMed E-utilities this session; full text UNREACHABLE-IN-SESSION.

Design: three expanded/equal-interval schedule pairings **matched on average spacing** —
**1-2-3 vs 2-2-2; 1-3-5 vs 3-3-3; 1-3-8 vs 4-4-4** — in younger and older adults, tested same-day
and after 24 hours. Matching on average spacing is what makes this a clean test of *expansion
itself* rather than of total spacing.

Verbatim findings:

> "Both age groups showed a learning phase retrieval success advantage for expanded items compared
> to equal interval items. **Only older adults in the same day test condition showed a significant
> expansion effect in final recall. After a 24-h delay, the final recall advantage for items in the
> expanded condition was lost in both groups, and in fact these items were at a significant recall
> disadvantage for younger adults.** Results indicate that younger and older adults benefit from a
> rehearsal technique that incorporated **any type of spaced retrieval whether it is distributed as
> an expanding schedule or not.**"

**`NEGATIVE RESULT`, and stronger than a null:** at 24 hours, expanded items were at a *significant
disadvantage* for younger adults. The authors' own summary is that any spacing works and the
schedule shape does not matter — with one honest caveat they raise themselves: expanding schedules
produce **higher success rates during the learning phase**, which may have motivational value
"depending on the ultimate goals of an individual memory training program."

**Note the structure of that caveat**, because it recurs throughout this section: expanding
intervals feel better and produce more successes in the moment, while doing nothing (or slightly
worse than nothing) for the outcome. That is a textbook desirable-difficulty inversion (§6), and
it is a plausible explanation for how the folklore became universal in the first place: **the
schedule that makes the software feel good is the schedule that got shipped.** `INFERENCE`

Latimier coded Logan & Balota as four effect sizes: **g = 0.00 (N = 80), +0.32 (N = 66),
−0.37 (N = 24), −0.28 (N = 24)** — a distribution centred on nothing.

### 3.4 The honest counterexample — Dobson (2012)

A section that only cites the confirming studies is not doing the job. The single largest
contributor to Latimier's subset 3, and the strongest primary evidence *for* expanding schedules,
is:

**Dobson, J. L. (2012), *Advances in Physiology Education* 36(1), `doi:10.1152/advan.00090.2011`,
PMID 22383406.** `MEASURED-RCT` **n = 250 randomized**, 30 immunology and reproductive-physiology
concepts, **29-day retention interval**, no feedback.

| Schedule | Final assessment (mean ± SE) |
|---|---|
| Uniform (days 1, 10, 20) | 36.15 ± 1.97 |
| Uniform (days 8, 15, 22) | 32.31 ± 1.87 |
| **Expanding (days 1, 6, 16)** | **45.80 ± 2.56** |
| Expanding (days 2, 7, 17) | 39.71 ± 2.48 |
| **Combined expanding vs. combined uniform** | **42.57 ± 1.80 vs. 34.10 ± 1.36; F = 14.09, P = 0.00** |

Overall ANOVA F = 6.52, P = 0.00. Dobson contributes five effect sizes to Latimier's subset 3
(**g = 0.22 to 0.76**, N = 93–196, retention interval 41,760 min = 29 days), all favouring
expansion — **at day-scale intervals and with five exposures per item, which is precisely the
moderator region (> 4 exposures) where Latimier's pooled estimate rises to g = 0.20.**

**How to hold both results at once.** Karpicke & Roediger and Logan & Balota run intervals measured
in *trials and minutes* within a single session, tested at 10 minutes to 2 days. Dobson runs
intervals measured in *days*, tested at 29 days, with classroom material. They are not testing the
same thing, and the meta-analysis pools them. The defensible statement is therefore narrower and
more useful than "expanding doesn't work":

> **Across 54 effect sizes there is no aggregate advantage to expanding intervals (g = 0.032,
> I² = 0%). Within-session expanding schedules reliably *lose* at delays beyond a day. Day-scale
> expanding schedules with five or more exposures may help, but the pooled estimate for that
> subgroup (g = 0.20) still includes zero and its moderator test is p = 0.09.**

### 3.5 Verdict

| Claim | Status |
|---|---|
| B1's `g = 0.034, n.s., k = 54` for expanding vs. uniform | **VERIFIED** via the ERIC-indexed published abstract (EJ1310148) and Latimier's thesis (via the Wayback Machine): **g = 0.032 [−0.10, 0.17], p = 0.62, I² = 0%, Egger p = 0.66**. |
| The *direction* of that claim | **Corroborated by two independent primary experiments.** Karpicke & Roediger (2007) find equal spacing *superior* at 2 days with and without feedback; Logan & Balota (2008), matching average spacing across conditions, find expanded items at a *significant disadvantage* at 24 h for younger adults. `MEASURED-RCT` |
| The mechanism | **Recovered and inverted**: the operative variable is the delay to the *first* retrieval (K&R Exp. 3, main effect ηp² = .19, schedule effect F < 1). And expanding schedules do **not** increase retrieval difficulty — response latencies *fall* across repetitions in both conditions. |
| The honest counterexample | **Dobson (2012), n = 250, 29 days: expanding 42.57 vs. uniform 34.10, F = 14.09, P = 0.00.** Day-scale intervals, 5 exposures. |
| Landauer & Bjork (1978), the origin of the folklore | Book chapter in Gruneberg, Morris & Sykes, *Practical Aspects of Memory*; **not indexed, UNREACHABLE-IN-SESSION, never read.** Karpicke & Roediger describe it as 1–4–10 vs. 5–5–5 (matched average spacing) with *"about a 10% advantage"* on a final test **30 minutes** later — i.e. exactly the short-delay regime where the advantage replicates. **No n and no p-value are available; do not attribute significance.** |
| Cull (2000), *Applied Cognitive Psychology* 14(3):215–235 | **UNREACHABLE-IN-SESSION** (closed, no repository copy). Described by Karpicke & Roediger as four experiments in which *"Cull did not report any significant positive effects of expanding retrieval,"* with equal spacing superior at 3 or 8 days in some conditions. **Note: Cull is *not* among Latimier's 16 included studies**, presumably because effect sizes were not derivable. |

**So the finding stands, and it is the most consequential single result in this section:**

> **There is no evidence that intervals must expand. The near-universal design assumption behind
> SM-2, Anki, Leitner boxes, Memrise ladders and every product descended from them is not supported
> at the retention intervals those products exist to serve — and the one variable that *is*
> supported (delay the first retrieval) is the one they all get backwards.**

**The actionable consequence, and it is cheap to implement.** Anki's SM-2 defaults graduate a card
at **1 day** and then **6 days**. FSRS learns an initial stability from the first grade. Both
front-load the first review. Karpicke & Roediger (2007, Exp. 3) says the single highest-leverage
change available is to **push the first retrieval later**, and that once you have done so, the
shape of everything after it barely matters. **That is `H4` in §11.6, and it is the cheapest
experiment in this entire document.**

**Caveat that must travel with all of the above:** these are word-pair and vocabulary experiments
at 2-day and 24-hour delays. Cepeda et al. (2008) shows the optimal gap ratio itself varies by an
order of magnitude across retention intervals from one week to one year (§2.2). Whether the
expanding-vs-uniform null also holds at year-scale intervals, and for conceptual rather than
paired-associate material, is **not established by anything located in this session**.

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

### 4.6 The interventional evidence — every controlled trial of a scheduler I could locate

These are the only interventional trials of *algorithmic* scheduling with a retention outcome
that this session could locate. Both matter; both have limits that must be stated with them.

**(i) Lindsey, Shroyer, Pashler & Mozer (2014), "Improving students' long-term knowledge
retention through personalized review," *Psychological Science* 25(3):639–647,
`doi:10.1177/0956797613504302`, PMID 24444515.** `MEASURED-RCT` Abstract verified via PubMed
E-utilities; **full preprint retrieved and read** from Mozer's site.

| Element | Value |
|---|---|
| Population | **179 eighth-graders** (median age 13; 82 M / 97 F), suburban Denver middle school, third-semester Spanish, 6 class periods, one instructor |
| Software | COLT (Colorado Optimized Language Tutor), replacing commercial flashcard software and paper quizzes |
| **Randomization** | **Within-participant.** Each chapter's items randomly split into thirds, one third per scheduler, counterbalanced across students |
| Conditions | **Massed** · **Generic-spaced** (~1-week lag, the one-size-fits-all optimum from Cepeda et al.) · **Personalized** (DASH latent-state Bayesian model, selecting the knowledge component whose posterior recall probability is nearest a target "desirable difficulty") |
| **Time-matching** | Schedulers **alternated**, so each administered an equal number of review trials — verified: review trials 8.03 / 8.05 / 8.03; study-to-criterion 7.58 / 7.57 / 7.56 |
| Achieved spacing | Mean days between review trials: **0.12 (massed) / 1.69 (generic) / 4.70 (personalized)** |
| Dose | 3 × 20–30 min/week ≈ 10% of course-engaged time; **597,990 retrieval trials logged** |
| Outcomes | Two proctored cumulative exams, **no feedback**; Exam 1 n = 172, Exam 2 n = 176 administered **28 days later** after an inter-semester break with no COLT access |

| Contrast | Exam 1 (end of semester) | Exam 2 (+28 days) |
|---|---|---|
| Personalized vs. **massed** | **+12.4%**, t(169) = 10.1, p < .0001, **d = 1.38** | **+16.5%**, t(175) = 11.1, p < .0001, **d = 1.42** |
| Personalized vs. **generic spaced** | **+8.3%**, t(169) = 8.2, p < .0001, **d = 1.05** | **+10.0%**, t(175) = 6.59, p < .0001, **d = 0.88** |
| 28-day forgetting rate | — | massed 18.1% · generic 17.1% · **personalized 15.7%** |

Only **13.5%** of students scored better under massed and **22.3%** under generic spacing than
under personalized.

This is the strongest result in the area, and the **+10.0%** contrast is the one that matters —
personalized spacing versus generic spacing, holding *spacing itself* constant. It is the best
existing counterweight to §4.9's "personalisation is worth ~2%" simulation, and the two must be
reported together.

**Four caveats, three of them the authors' own:**

1. **⚠️ The percentages are relative, not percentage points.** The paper never states which, and
   the condition means appear only inside Figure 2a. Under a percentage-point reading, Exam 2's
   numbers force the personalized condition off the top of the published axis and massed below its
   floor; under a relative reading the reconstructed means (≈60/62/67 on Exam 1; ≈49/52/57 on
   Exam 2) fit the axis exactly and reproduce the +10.0% contrast to within 0.1. `INFERENCE`
   **Do not quote "16.5 percentage points."** This report previously did; it is corrected here.
2. **The authors concede the design confounds personalization with coarse temporal
   distribution**, verbatim: *"we acknowledge that our design confounds personalization and the
   coarse temporal distribution of review."* Mean review lags differ 0.12 / 1.69 / 4.70 days, so
   this is *partly* a spacing-lag manipulation, not purely an algorithm manipulation.
3. **The d values are within-subject paired d's** (items randomized within student) and are not
   comparable to between-subject effect sizes.
4. **The crossover appears here too, and it is a warning to product designers.** On the *weekly
   graded chapter quizzes* — the immediate, visible, motivating assessment — **massed did best**:
   89.4% vs 87.2% (generic) and 88.1% (personalized), F(2,310) = 11.8, p < .001. A system judged
   on its weekly quiz scores would have shipped the worst scheduler.

Scope limits: middle-school foreign-language vocabulary, item-level cued recall, one semester, one
classroom. And note the structure of the split — **most of the benefit comes from spacing at all,
with personalisation adding a further, smaller increment on top.**

Worth quoting from the paper's own Discussion, because it is the thesis of this whole section
stated by the authors in 2014: *"two traditional adaptive-scheduling techniques have attracted a
degree of popular interest: the Leitner (1972) system and SuperMemo… These techniques underlie
many flashcard-type web sites and mobile applications, which are marketed with the claim of
optimizing retention. **Though one might expect that any form of review would show some benefit,
the claims have not yet undergone formal evaluation in actual usage.**"* Twelve years later,
§4.2–§4.9 says that is still true.

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

**(iv) The adaptive-vs-fixed trials that came out null — and one that came out backwards.**

**Mettler, Massey & Kellman's ARTS** (Adaptive Response-Time-based Sequencing) is the most
carefully run programme of scheduler experiments in existence, and its results are more
instructive than its headline.

*JEP: General* (2016) 145(7):897–917, `doi:10.1037/xge0000170`, PMC6028005. `MEASURED-RCT` (lab)
Experiment 1, n = 72, 24 African countries on a map, four presentations per item, **1-week
delayed posttest**:

| Phase | Adaptive | Fixed expanding (1–5–9) | Fixed equal (5–5–5) |
|---|---|---|---|
| Immediate posttest | .61 (.21) | .58 (.23) | .52 (.24) |
| **Delayed (1 week)** | **.42 (.20)** | .31 (.19) | .30 (.24) |

Adaptive beat both fixed schedules at delay (**d = 0.56** and **d = 0.57**) and neither at
immediate test. But note the row that matters for §3: **expanding vs. equal was n.s. at delay**
(t(35) = 0.45, p = .65) and significant only at immediate test (**d = 0.24**) — a third independent
replication of §3's crossover. In Experiment 2 (n = 48), adaptive beat a *yoked-random* schedule
at delay (d = 0.74) but **adaptive vs. yoked-item was n.s.** (t(30) = 1.45, p = .16).

**Then the field studies, and this is where it gets interesting.** ARTS in community-college
chemistry (CogSci 2020, PMC8324178): `MEASURED-RCT`

| Exp | n | Delay | Efficiency (adaptive vs. fixed) | **Accuracy change score** |
|---|---|---|---|---|
| 1 | 31, randomized | 2 wk | immediate **d = 1.92**, delayed **d = 1.40** | **NULL** — immediate d = 0.31 p = .4; delayed d = 0.036 p = .9 |
| 2 | 36 | 1 wk | immediate d = 1.48; delayed d = 0.70, p = .061 | **FIXED BETTER** — immediate .609 vs .413 (d = 1.33); delayed .357 vs .229 (d = 0.768) |
| **3 — retirement criteria equated in both arms** | 63 | 2 wk | **NULL**, F(1,61) = 0.583, p = .448 | **NULL**, immediate d = 0.374 p = .14; delayed d = 0.012 p = .96 |

The authors' own conclusion on Experiment 3: *"**Equating mastery and retirement criteria tended
to equalize performance across the adaptive and fixed expanding schedules.**"* `NEGATIVE RESULT`

**And the sharpest result in the ARTS corpus** (CogSci 2020, PMC8324179, n = 48/experiment):
adaptive-with-dropout vs. random-without-dropout. Efficiency favoured adaptive enormously
(d = 2.68 immediate, d = 0.89 delayed). **Raw accuracy favoured *random*:** .93 vs .85 immediate
(t(46) = 2.55, p = .01, **d = 0.746**) and .76 vs .52 delayed. Trials to criterion: adaptive 197
vs. random 429.

> **`NEGATIVE RESULT`, and it is the trap this whole subsection exists to name: ARTS's advantage
> is on *efficiency* — learning per trial — because it retires items sooner. On *raw accuracy* a
> random schedule beat it.** An adaptive scheduler that stops sooner will always look good on
> per-trial efficiency and can look worse on what the learner actually knows. Any efficiency claim
> without a matched-total-knowledge comparison is uninterpretable.

**(v) Kerfoot (2010) — the only published head-to-head of two spacing algorithms in medical
education, and it is a null on learning.** *J. Urology* 183(2):678–681, PMID 20022032. n = 62
third-year medical students at two schools, 40 validated items, 4 urology topics. Non-adaptive
arm: daily email, two questions, **fixed linear review 20 days after initial presentation**.
Adaptive arm: algorithm customises spacing intervals and repetition counts by learner knowledge
level and **limits repetition of mastered content**. Result: the adaptive arm answered
**significantly fewer items (p = 0.001)** with **comparable end-of-course test scores
(p = 0.37)**, reported as "+38% learning efficiency." `MEASURED-RCT`

Read correctly: **p = 0.37 at n = 62 is a failure to reject, not equivalence**, and the outcome is
a single immediate end-of-course test **with no retention interval** — precisely the design where
retiring "mastered" items is least likely to be penalised. **Full text UNREACHABLE-IN-SESSION**
(ScienceDirect, AUA Journals and LWW all returned 403; not in PMC; not OA), so per-arm n,
attrition, means, SDs, and the efficiency formula are unverified. Note also: the paper is
single-authored by an equity owner and director of Spaced Education Inc., and is not registered.
That is disclosed in the paper's own conflict statement and is stated here as provenance, not as
an accusation.

**(vi) A knowledge-tracing scheduler retuned for efficiency: learning unchanged, time saved.**
**Cen, Koedinger & Junker (2007), "Is Over Practice Necessary? Improving Learning Efficiency with
the Cognitive Tutor," AIED 2007.** `MEASURED-RCT` **110 students, 6 classes, one high school, one
teacher, randomly assigned.** The manipulation was retuning the knowledge-tracing P(L₀) priors via
Learning Factors Analysis on prior log data, so over-practised knowledge components reach mastery
sooner. Pretest / posttest / **2-week retention test**.

| Outcome | Result |
|---|---|
| Learning gain | ~5 points in **both** arms |
| Posttest (ANCOVA, condition) | **p = 0.772** — n.s. |
| **2-week retention test** | **p = 0.602** — n.s. |
| Tutor time | **162.41 vs 183.93 min — 21.5 min saved, 12%** |

Verbatim: *"**Thus, over practice does not lead to a significantly higher learning gain.**"*
⚠️ The paper's *conclusion* section contains a sentence ("yields better learning than hand-set
parameters") inconsistent with p = 0.772 / p = 0.602. **Cite the results section, not the
conclusion.** This is the correct framing for model-driven mastery: **an efficiency result with
outcome equivalence, not a learning gain.**

**(vii) 33 million randomized sequences say the mastery threshold barely matters.**
**Matayoshi, Cosyn, Uzun & Kurd-Misto (2025), *JEDM* 17(1):308–336.** `MEASURED-RCT`
Topic-level randomization inside ALEKS in production, April 2023 – November 2024:

| Threshold | n (topic sequences) | Learn | Mean min | Median min |
|---|---|---|---|---|
| High | 16,441,259 | 0.789 | **6.6** | 3.2 |
| Low | 16,474,845 | **0.809** | **5.1** | 2.4 |

95% CIs on the proportions are **< 0.0006 wide**. Retention analysis over 1.4M data points:
*"after several weeks the estimated difference in retention rates between the two mastery
thresholds is **less than 0.02**"* on a base rate of ~0.60, and shrinking with time. The vendor's
own conclusion: *"It seems reasonable that the high mastery threshold could be used less often
than it currently is."* **The high threshold costs +29% time for ≤ 2 percentage points of
retention.** `NEGATIVE RESULT`

Corroborating: **Prihar et al. (2022), EDM, ERIC ED624051** — a meta-analysis of **50 RCTs, 50,752
instances, 30,408 K-12 students** in ASSISTments found *"**no statistically significant effect on
student learning for students that completed their assignment, regardless of how many problems
they had to complete correctly in a row**… The vast majority of the effects… come from more
students failing to complete their assignment."* `MEASURED-META` **The mastery threshold's
measurable effect ran through dropout, not learning.**

**(viii) When adaptivity *did* help, it was not the part anyone expected.**
**Papoušek, Stanislav & Pelánek (2016), LAK '16.** `MEASURED-RCT` ~1.3M answers from ~20,000
learners, randomized on entry into a 2 × 2: adaptive/random **item selection** × adaptive/random
**option (distractor) construction**. Learning was probed by *randomly constructed reference
questions* inserted every tenth item — an unbiased in-system probe.

> *"In all cases the conditions with **adaptive construction of options** (A-A, R-A) beat the
> conditions with random options (A-R, R-R). **The item selection part does not seem to have large
> effect on learning.** When we see differences between A-A and R-A, the R-A condition is slightly
> better."*

**The learner model's contribution was difficulty-calibrating the distractors, not choosing what
to practise.** This is a directly actionable finding for §11 and it points the same way as
everything else in §4: the scheduling decision is not where the value is.

### 4.7 The field-level tally — the single most organizing fact in this section

**Doroudi, Aleven & Brunskill (2019), "Where's the Reward? A Review of Reinforcement Learning for
Instructional Sequencing," *International Journal of AI in Education* 29:568–620,
`doi:10.1007/s40593-019-00187-x`** (open access). `MEASURED-META` This review collects **every**
empirical study comparing a model-induced instructional policy to a baseline with a learning
outcome, and sorts them by what is being sequenced. Table 2, p. 581:

| Cluster | Sig | ATI | Mixed | **Not sig** | Sig **worse** |
|---|---|---|---|---|---|
| **All studies** | 21 | 4 | 4 | 11 | 1 |
| **Paired-associate / flashcard (spacing)** | **11** | 0 | 0 | 2 | 1 |
| Concept-learning tasks | 4 | 0 | 2 | 1 | 0 |
| **Sequencing interdependent content** | **0** | **0** | **2** | **6** | **0** |
| Sequencing activity types (worked example vs. problem solving) | 4 | 4 | 0 | 2 | 0 |
| Maximizing other objectives | 2 | 0 | 0 | 0 | 0 |

**Read the two bold rows together and the whole field resolves.** Where the object being scheduled
is a **paired associate** — a flashcard — model-driven scheduling works, 11 successes out of 14.
Where the object is **interdependent content**, which is what any real curriculum consists of and
what a knowledge tracer is built for, the record is **0 for 8**. Verbatim, pp. 586–587:

> "the studies in this cluster have been the **least successful, with all of them resulting in
> either a mixed result or no significant difference**… **when it comes to sequencing
> interdependent content, there is not yet evidence that RL can induce instructional policies that
> are significantly better than reasonable baselines.**"

Three of those eight null studies used explicitly BKT-driven policies (David et al. 2016;
Doroudi et al. 2017a and Appendix B; Segal et al. 2018). Two further findings from the same review
belong in any honest account:

- *"**only three out of 15 studies that were run in classroom settings** found an RL-induced policy
  was significantly better than baselines."*
- Of the 24 studies reporting a significant effect or an aptitude–treatment interaction,
  **17 (71%) compared against a *random* baseline** rather than a state-of-the-art one; in some
  cases researchers *"intentionally compared to baseline policies designed to perform poorly."*
- The one "significantly worse" entry: **Mettler et al. (2011)**, where a data-fitted Atkinson-model
  policy was **beaten** by ARTS, a response-time heuristic that was *not* fit to data. The review's
  gloss: *"in some cases, a good psychological theory might be more useful for finding good
  instructional policies than a data-driven model."*

**And the authors' own explanation is the design brief for §11.** RL-driven sequencing works where
*"we have well-known results from psychology… the spacing effect and the expertise-reversal
effect,"* and fails for interdependent content because *"**we do not yet have domain-general
principles from the learning sciences that tell us whether and how sequencing matters.**"* The
bottleneck is not the optimiser. It is that nobody knows what the objective should be.

### 4.8 The honest bottom line for §4

**`NEGATIVE RESULT`, unchanged from F5 §1.8 and now much better evidenced:** there is **no
controlled evidence that switching scheduling algorithm — SM-2 → FSRS, or Leitner → HLR —
improves any learning outcome.** The srs-benchmark README says so in its own words:
**"Retrospective only — no randomized user trials or measurement of actual learning outcomes."**
`MEASURED-BENCH`

What *is* established, and these are three different claims that must never be merged:

1. Modern schedulers **predict recall better** than old ones (`MEASURED-BENCH`).
2. In **simulation**, they buy comparable knowledge for less review time (`DEMO`).
3. **Personalized spacing beats generic spacing** for paired-associate material in one strong
   classroom RCT (Lindsey 2014, `MEASURED-RCT`) — with the authors' own confound caveat, and with
   **0 for 8** in the adjacent cluster where content is interdependent (Doroudi 2019).

### 4.9 Memrise's fixed ladder, and the ceiling on personalisation

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

**(a) The pooled applied effect is large — but read the two meta-analyses together, not either
alone.** **"The Effectiveness of Spaced Repetition in Medical Education: A Systematic Review and
Meta-Analysis," *The Clinical Teacher* (2026), `doi:10.1111/tct.70353`, PMID 41601436.** PRISMA;
searched Feb 2025; MERSQI quality appraisal. 542 records screened → 14 studies in the review,
**13 in the meta-analysis, 21,415 learners**. Result, verbatim: **"an overall significant effect
in favour of spaced repetition study compared to standard studying techniques (standardised mean
difference = 0.78; 95% CI 0.56–0.99; p < 0.0001)."** `MEASURED-META`

**⚠️ Do not quote 0.78 as a randomized effect.** The full text is paywalled and
**UNREACHABLE-IN-SESSION**, so how many of the 13 pooled studies were randomized rather than
observational cohorts, the I², and the publication-bias assessment are all **unverified**. Given
that the Cochrane-method review below, over substantially overlapping material, reports **SMD
0.32**, a pooled 0.78 spanning 21,415 learners very likely includes large observational cohorts.

**The more conservative estimate, with methods that could be checked:**
**Martinengo et al. (2024), *JMIR* , `doi:10.2196/57760`, PMID 39388234, PMC11502984.**
`MEASURED-META` Spaced versus massed **online** education across 23 studies:

| Outcome | SMD [95% CI] | I² | k | Certainty |
|---|---|---|---|---|
| **Knowledge** | **0.32 [0.13, 0.51]** | 66% | 9 | moderate |
| Behaviour change | 0.67 [0.43, 0.91] | 5% | — | — |
| **Knowledge retention** | 0.38 [0.10, 0.65] | 0% | **only 2 studies** | — |
| Surgical-skill simulation | 1.15 [0.34, 1.96] | — | — | low |

Caveats the authors state: **19 of 23 studies (83%) at unclear or high risk of bias**, and several
standard deviations were **back-derived from p-values** using RevMan's calculator — so the pooled
behaviour estimate rests partly on reconstructed variances.

A narrative synthesis reaches the same place: **Phillips et al. (2019), *Medical Education*,
`doi:10.1111/medu.13895`, PMID 31144348** — 17 studies, 2,701 clinicians, **only 5 RCTs**;
10 showed knowledge gains, 7 behaviour change, and **only 2 showed improvement in patient
outcomes.**

Note carefully what varied in all three: the interventions were "faculty-created or third-party
flash cards, MCQs delivered via email or as part of a continuing medical education framework, and
spaced classroom quizzes." **The manipulation is spacing-plus-testing as a practice, not a
scheduling algorithm.** The 2026 review's own conclusion asks for exactly the work that has not
been done: *"Further work is required to investigate the optimal design and delivery of spaced
repetition interventions."*

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

**The confounding structure, stated plainly**, because it applies to every study in this
literature: exposure is **self-selected**, almost always **self-reported**, and correlated with
conscientiousness, prior ability (MCAT/GPA), total study hours, and third-party question-bank use.
**None of the studies adjusts for any of these.** The one study using objective Anki logs
(*J. Med. Educ. Curric. Dev.* 2025, `doi:10.1177/23821205251369705`, n = 36) found mature cards
predicted CBSE score (P = 0.002) — and so did **total hours studied (P = 0.013)**, of comparable
magnitude. It cannot separate "spaced repetition works" from "students who study more score
higher." Another (*Med. Sci. Educ.* 2023, `doi:10.1007/s40670-023-01826-8`, n = 130) found the
*self-reported* user/non-user grouping predicted all four exams while *"little correlation between
its specific statistical markers and examination performance"* — **the objective usage metrics did
not track scores; only the self-report did.** That pattern is what confounding looks like.

**Two more documented nulls in this literature:**

- **`NEGATIVE RESULT` — a clean null on learning with positive perceptions.** *Cureus* (2024),
  `doi:10.7759/cureus.70994`, PMID 39507168: instructor-made spaced-repetition flashcards in an
  introductory microbiology course. **Exam performance unchanged, p = 0.2657.** Confidence
  improved (p = 0.0066), "think like a microbiologist" (p = 0.0011), "effective approach"
  (p = 0.0076). `MEASURED-RCT`-ish. **This is the felt-learning trap of §6 in miniature: every
  subjective measure moved and the objective one did not.**
- **`NEGATIVE RESULT` — a null in the primary comparison.** A graduate-entry cohort study
  (*Med. Sci. Educ.* 2025, `doi:10.1007/s40670-025-02504-7`, n = 43 complete, 80% Anki users)
  found *"no statistically significant benefit for Anki usage in terms of performance outcome
  compared to those who did not use Anki when the module was considered as a whole,"* with
  positive results only in two subgroups (extensive vs. inconsistent users; the physiology
  subsection). `OBSERVED`

**And a gap worth naming:** a Europe PMC sweep of `"spaced repetition" AND nursing` (120 hits) and
`AND pharmacy AND student` (61 hits) returned **no RCT of Anki or SRS in nursing or pharmacy** —
only microlearning/gamification studies, pretest–posttest designs, and scoping reviews. A Europe
PMC search for `"spaced repetition" AND ("A/B test" OR "online controlled experiment")` returns
**zero hits.**

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

This is the section that connects to the project's central "felt-learning trap," and it has one
result crisp enough to carry the whole argument.

### 6.0 The theory, stated in its authors' own words

**Primary source problem, stated first.** The founding papers — **Bjork & Bjork (1992), "A new
theory of disuse and an old theory of stimulus fluctuation,"** in Healy, Kosslyn & Shiffrin (eds.),
*From Learning Processes to Cognitive Processes*, Vol. 2, Erlbaum, pp. 35–67; and **Bjork (1994),
"Memory and metamemory considerations in the training of human beings,"** in Metcalfe & Shimamura
(eds.), *Metacognition: Knowing About Knowing*, MIT Press, pp. 185–205 — exist online only as
**image-only scans with no text layer**. They could not be quoted from the original this session
and are flagged **UNREACHABLE-IN-SESSION (no OCR available)**.

The theory is therefore quoted from **the same two authors' own 2020 restatement**: Bjork & Bjork,
"Desirable difficulties in theory and practice," *Journal of Applied Research in Memory and
Cognition* 9(4):475–479, `doi:10.1016/j.jarmac.2020.09.003` (author-posted PDF, read in full).
Verbatim:

> "In our framework we assumed that an item in memory can be characterized by two strengths —
> **storage strength** (how well learned an item is, as defined by how interconnected it is with
> related items in memory) and **retrieval strength** (the current ease of access to that item
> given the current cues)."

> "What was 'new' about our New Theory of Disuse … is our specification of **how storage strength
> and retrieval strength interact**. In our framework **the higher the current level of storage
> strength the larger the gain in retrieval strength** that results from restudying or retrieving,
> whereas — and much less intuitively — **the higher the current level of retrieval strength the
> smaller the gain in storage strength** that results from restudying or retrieving. Thus,
> **forgetting (loss of retrieval strength) can enhance learning (the gain in storage strength)**,
> which is why … manipulations such as spacing and variation, which reduce retrieval strength, can
> enhance learning, as measured by performance at a delay."

**That second asymmetry is the single most design-relevant sentence in the entire theory, and it
is what every spaced-repetition scheduler is implicitly implementing without saying so.** A review
scheduled while retrieval strength is still high buys you very little storage strength. This is
the theoretical justification for the empirical finding in §4.9 that pushing desired retention
above ~0.90 buys +8% knowledge for 4.9× the workload — you are paying full price for reviews that
occur while retrieval strength is near ceiling.

The metacognitive corollary, verbatim from the same paper: *"conditions of learning that make
performance improve rapidly often fail to support long-term retention and transfer, whereas
conditions that create challenges … often optimize long-term retention and transfer, means that
learners — and teachers — are vulnerable to mis-assessing whether learning has or has not
occurred … we become susceptible not only to mis-judging whether learning has or has not occurred,
but also to **preferring poorer conditions of learning over better conditions of learning**."*

**Schmidt & Bjork (1992), "New conceptualizations of practice: Common principles in three
paradigms suggest new concepts for training," *Psychological Science* 3(4):207–217** (author-posted
PDF, read in full) states the applied version, verbatim from the abstract:

> "The implicit or explicit assumption of those persons responsible for training is that the
> procedures that enhance performance and speed improvement during training will necessarily
> achieve these two goals. However, a variety of experiments on motor and verbal learning indicate
> that **this assumption is often incorrect. Manipulations that maximize performance during
> training can be detrimental in the long term; conversely, manipulations that degrade the speed
> of acquisition can support the long-term goals of training.**"

Their two named instances: **increased frequency of error feedback** improves training performance
but *"can degrade performance on a test of long-term retention or transfer"*; **increased task
variability** *"depresses performance during training, yet facilitates performance on later tests
of the ability to generalize."* Their worked example is Shea & Morgan (1979) on contextual
interference: blocked practice wins in acquisition, random practice wins at both 10 minutes and
10 days, and — the detail that matters — *"Regardless of whether the retention test was itself
random or blocked … it was always more effective to have practiced under random conditions."*

**Note the first instance carefully, because it cuts against §5's own guidance.** Schmidt & Bjork
say *frequency* of error feedback can be a desirable difficulty to reduce; Rowland (2014) and
Fiechter & Benjamin (2018) say corrective feedback after failed retrieval is near-mandatory. These
are reconcilable — the motor-learning result is about feedback *density* during continuous
practice, the verbal result about *presence* of feedback after a discrete retrieval failure — but
a system designer must not read either as licensing the other. `INFERENCE`

**The storage/retrieval distinction is also load-bearing for §11.3.** If retrieval strength is
"the current ease of access given the current cues," then a single failed retrieval is a
*cue-and-moment* event, not evidence that the knowledge is gone. That is exactly why §11.3 requires
**≥3 distinct cue forms across ≥2 separate days** before flagging a concept inert: one miss is a
retrieval-strength observation; a stable pattern across cues and days is a storage-strength one.

### 6.1 The measured divergence between learning and the feeling of learning

**Deslauriers, McCarty, Miller, Callaghan & Kestin (2019), "Measuring actual learning versus
feeling of learning in response to being actively engaged in the classroom," *PNAS*
116(39):19251–19257, `doi:10.1073/pnas.1821936116`, PMC6765278.** `MEASURED-RCT`
**Full text retrieved and read this session** via Europe PMC; the numbers below are from Table 3
of the paper, not the abstract.

Design: large-enrollment introductory college physics, **randomized at the student level** with a
**crossover** across two topics (statics, fluids), two instructors, two semesters. Both arms got
identical content and identical handouts; the instructor made no attempt to sell either method;
the passive arm was taught by experienced, highly rated lecturers — i.e. the control is a *strong*
control, not a straw man. After each class students completed a **Feeling of Learning (FOL)**
survey and then a 12-item **Test of Learning (TOL)**.

Standardized regression coefficients for passive (0) vs. active (1), controlling for FCI pretest,
CLASS pretest, prior midterm average, gender, instructor, topic, and semester:

| Outcome | Coefficient | Significance |
|---|---|---|
| **Feeling of learning (FOL)** | **−0.56 SD** | p < 0.001 |
| **Test of learning (TOL)** | **+0.46 SD** | p < 0.001 |

**The same intervention moved actual learning up by about half a standard deviation and the
feeling of learning down by about half a standard deviation. The gap between what worked and what
felt like it worked is roughly one full SD, in opposite directions.** The authors verified
randomization on all covariates (Table 1), confirmed the result is unchanged when each student is
treated as their own control, and confirmed it is unchanged when all student-level covariates are
removed.

Their own interpretation, verbatim: *"when students experience the increased cognitive effort
associated with active learning, they initially take that effort to signify poorer learning."*
And the warning that should be printed on every edtech dashboard: *"attempts to evaluate
instruction based on students' perceptions of learning could inadvertently promote inferior
(passive) pedagogical methods. For instance, a superstar lecturer could create such a positive
feeling of learning that students would choose those lectures over active learning."*

### 6.2 The learner's judgement is not merely noisy — it is inverted, and it survives disconfirmation

**Kornell & Bjork (2008), "Learning concepts and categories: Is spacing the 'enemy of induction'?"
*Psychological Science* 19(6):585–592, `doi:10.1111/j.1467-9280.2008.02127.x`** (author-posted PDF,
read in full). `MEASURED` Participants learned 12 landscape painters' styles from six paintings
each, then attributed **48 previously unseen paintings**.

| | Value |
|---|---|
| N | Exp 1a n = 120 (within-subjects); Exp 1b n = 72 (between-subjects); Exp 2 n = 80 |
| Spacing > massing, Exp 1a | **F(1,119) = 77.35, p < .0001, ηp² = .39** |
| Spacing > massing, Exp 1b | F(1,70) = 15.63, p < .001, ηp² = .18 |
| First test block, Exp 1a | **.61 (SD .24) spaced vs .35 (SD .24) massed, d = 0.99** |
| First test block, Exp 1b | .59 (SD .22) vs .36 (SD .18), **d = 1.28** |
| Exp 2 (recognition) | hits .77 vs .67, t(79) = 3.28, p < .01, **d = 0.41** |

**The metacognition number, verbatim:** *"Overall, **78% of the participants did better with
spaced presentations** than they did with massed presentations, but **78% of the participants said
that massing was as good as or better than spacing**."* In Exp 2, *"Of the 72 participants who did
not say … 'about the same,' **64 thought massing had been more effective**."*

Why the illusion is so stable: a probe (n = 28) found participants could identify above chance
which artists had been *spaced* (M = .74, d = 1.41) but were **at chance for massed artists**
(M = .55, p = .25) — so *"participants often … made their metacognitive judgments on the basis of
their subjective experience during the study phase,"* not on their own results.

Corroborating figure from Bjork, Dunlosky & Kornell (2013), *Annual Review of Psychology*
64:417–444, `doi:10.1146/annurev-psych-113011-143823` (author-posted PDF), reporting Kornell
(2009): *"**90% of the college student participants had better performance after spacing than
massing** practice. When the study sessions were over, however, **72% of the participants reported
that massing was more effective**."* And on what students actually do: **76%** of 472 UCLA students
reread whole chapters or underline; ~90% self-test in some form but **only 18% self-test "because
they learn more"** (~70% do it to gauge how well they have learned); only **11%** of Washington
University students spontaneously mention retrieval practice on an open-ended strategy question
(Karpicke et al. 2009), rising to ~42% when prompted with a forced choice.

**`NEGATIVE RESULT` reported by the authors themselves, and it is the honest boundary:** Kornell &
Bjork also ran a contrived Remote-Associates-style task where *"spacing made it nearly impossible
to solve the problems"* — massed **.34** vs spaced **.22**, t(19) = 2.78, p < .05, **d = 0.65 in
favour of massing**. Spacing is not universally beneficial. Where the task requires holding several
items in mind simultaneously to discover a relation, spacing destroys it.

### 6.3 When difficulties are UNdesirable — the boundary the framework's own authors insist on

This is the part most often dropped in citation, and it is stated flatly in Bjork & Bjork (2020),
verbatim:

> "**Many difficulties are undesirable during instruction and forever after.** Desirable
> difficulties, versus the array of undesirable difficulties, are desirable because they trigger
> encoding and retrieval processes that support learning, comprehension, and remembering. **If,
> however, the learner does not have the background knowledge or skills to respond to them
> successfully, they become undesirable difficulties.**"

> "**The level of difficulty that is optimal, therefore, will vary with the degree of a learner's
> prior learning.** … a given learner needs to be equipped by virtue of prior learning to succeed
> at that generation — or at least succeed in activating relevant aspects of the skill or
> knowledge."

This is the same shape as the **expertise-reversal effect** (B1 §4) and it is why the project's
standing correction on "grilling" — diagnose **prior knowledge and misconceptions**, not learning
styles (CLAUDE.md §3) — is load-bearing here too. **Difficulty must be indexed to prior knowledge,
and prior knowledge must therefore be measured.** A 2025 review (PMID 39641213, PMC12432286)
attempts to integrate the desirable-difficulties framework with cognitive load theory and proposes
the same rule: *"**Increasing difficulty benefits low-element-interactivity tasks** by enhancing
focus and retention, **while reducing difficulty in high-element-interactivity tasks prevents
cognitive overload.**"* It is a review, not new data — `INFERENCE`.

**`NEGATIVE RESULT` — difficulty is not sufficient.** **Healy, Schneider & Kole (2025), "Exploring
whether making second-language vocabulary learning difficult enhances retention and transfer,"
*Journal of Intelligence* 13(5):58, PMID 40426468, PMC12108878.** Six experiments manipulating
blocking vs. mixing semantic categories, translation direction, prelearning, and set size.
Verbatim: *"difficult conditions provided a disadvantage during learning and immediate testing,
but **made no difference or provided an advantage** during relearning and delayed testing …
These results suggest that **making the initial learning more difficult does not always lead to
superior retention**."* They also found **negative transfer**: words from previously studied
semantic categories were learned *worse* than words from new categories. `MEASURED`

**Together with Bertsch et al.'s anagram reversal (d = −0.05, §5.2), this settles the design
question: difficulty is not the active ingredient.** The active ingredient is *retrieval and
elaboration that succeeds*. Difficulty is a proxy that usually correlates with it and sometimes
does not. §11.4's third gate exists precisely to enforce that distinction.

### 6.4 Fluency illusions, and the ten techniques

**Rhodes & Castel (2008), "Memory predictions are influenced by perceptual information: evidence
for metacognitive illusions," *JEP: General* 137(4):615–625, `doi:10.1037/a0013684`**
(author-posted PDF, read in full). Words presented in 18-pt vs 48-pt Arial; judgement of learning
(0–100) after each; then free recall. `MEASURED`

| Exp | n | JOL small | JOL large | JOL statistic | Recall difference |
|---|---|---|---|---|---|
| 1 | 20 | 48.63 | 60.81 | **F(1,19) = 15.27, ηp² = .45** | **none, F < 1** |
| 2 | 28 | 36.28 | 42.67 | **F(1,27) = 27.32, ηp² = .50** | 21.13 vs 21.23, **F < 1** |

Goodman–Kruskal gamma between font size and JOL was **+0.39** and **+0.26/+0.23**; between font
size and *recall*, **+0.03 / −0.03 / +0.02, all n.s.** Font size is diagnostically worthless and
learners weight it heavily.

**The finding that matters most for product design:** Experiment 2 gave participants **two full
study–test cycles**, so they had direct personal evidence that font size predicted nothing. The
illusion did not diminish — *"the influence of font size did not wane with a second study-test
opportunity"* (font × time interaction n.s., F(1,27) = 1.91, p = .18). **Experience alone does not
correct a fluency illusion.** It has to be shown to the learner as data. That is the argument for
§6.5.

**Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), "Improving students' learning with effective
learning techniques," *Psychological Science in the Public Interest* 14(1):4–58,
`doi:10.1177/1529100612453266`, PMID 26173288.** `MEASURED-META` (structured narrative synthesis
with an explicit rating rubric). **The monograph body returned HTTP 403 at the publisher; the
ratings and criteria below are verbatim from the primary abstract, and no numeric effect size is
attributed to this source.**

The four generalizability criteria, verbatim: *"**learning conditions, student characteristics,
materials, and criterion tasks** … Student characteristics include variables such as age, ability,
and level of prior knowledge … Criterion tasks include different outcome measures … such as those
tapping memory, problem solving, and comprehension."*

| Utility | Techniques | Verbatim justification |
|---|---|---|
| **HIGH** | **Practice testing**, **distributed practice** | *"benefit learners of different ages and abilities and have been shown to boost students' performance across many criterion tasks and even in educational contexts"* |
| MODERATE | Elaborative interrogation, self-explanation, interleaved practice | *"the evidence for their efficacy is limited … have not been adequately evaluated in educational contexts"* |
| **LOW** | Summarization, imagery for text, **keyword mnemonic**, **highlighting/underlining**, **rereading** | keyword: *"difficult to implement in some contexts, and it appears to benefit students for a limited number of materials and for short retention intervals."* highlighting/rereading: *"Most students report rereading and highlighting, yet these techniques **do not consistently boost students' performance**."* |

Note the selection rationale, verbatim: *"some techniques (e.g., highlighting and rereading) were
selected **because students report relying heavily on them**."* **The two techniques rated HIGH are
exactly the two this section's specification is built on, and the mnemonic technique of §7 is rated
LOW — which is why §11.7 excludes it from the core.**

A 2025 conceptual replication of the Deslauriers pattern in a large active-learning genetics
course (CBE-LSE, PMID 40373176, PMC12286633) found students rated **worked examples** best for both
performance and mastery goals and reported similar effort across activity types, yet *"students
exhibited **larger learning gains from prediction activities** compared with worked examples."*
`MEASURED` (effect sizes not extracted).

### 6.5 The design consequence — and this is the whole product argument

**Learner satisfaction is anti-correlated with learning under exactly the conditions that produce
durable memory.** An AI learning system optimised on thumbs-up, session length, streaks, or
self-reported confidence will be systematically driven toward the passive-lecture end of the
Deslauriers result. This is not a hypothetical alignment risk; it is a measured −0.56 SD.

Note that §4.4 shows this failure already happened, in production, at scale: Duolingo's HLR
deployment decision rested on *"positive anecdotal feedback about strength meter quality"* against
a **−7.3% measured practice metric**, with **no learning outcome measured at all**. The felt-learning
trap is not a student problem. It is an organisational one.

**The constructive version — and it is genuinely constructive.** The Deslauriers authors do not
conclude "ignore students." They conclude that instructors should *"improve students' response to
being actively engaged"* early on, by explaining the effect. An AI system can do something no
lecturer can: **show each learner their own version of Fig. 1.** It has every retrieval attempt,
every latency, every self-rated confidence, and every delayed outcome. It can present the learner
with their personal FOL-vs-TOL divergence — "here are the six topics you rated most confident;
here is how you did on them three weeks later." Metacognitive calibration stops being an exhortation
and becomes a measurement fed back to the person it is about. **That is a capability that did not
exist before instrumented, delayed, generated assessment, and §11.1's append-only `attempt` table
is what makes it possible.** `INFERENCE` — plausible and buildable, not yet measured.

---

## 7. Mnemonics and memory palaces — what transfers and what is a party trick

### 7.1 The best single experiment, read carefully

**Dresler, Shirer, Konrad, Müller, Wagner, Fernández, Czisch & Greicius (2017), "Mnemonic
Training Reshapes Brain Networks to Support Superior Memory," *Neuron* 93(5):1227–1235.e6,
`doi:10.1016/j.neuron.2017.02.003`, PMID 28279356, PMC5439266.** `MEASURED-RCT` (small;
**pseudo-randomised** — assignment was stratified on fluid reasoning (CFT) and baseline memory to
equate arms, not simple randomisation).

| Element | Value |
|---|---|
| Cross-sectional arm | 23 memory athletes from the Top-50 world ranking (28 ± 8.6 y, 9 F) vs. matched controls (age, sex, intelligence, handedness) |
| Athlete vs. control recall, 20-min delay (n = 17 + matched) | **70.8 ± 0.6 vs. 39.9 ± 3.6 of 72 words**; medians 72 vs. 41; Wilcoxon p < 0.001, **r = 0.62** |
| Training arm | **51** mnemonics-naïve participants (24 ± 3.0 y, all male), ~17 per arm |
| Arm 1 — mnemonic | 2 h in-person method-of-loci intro; then **30 min/day × 40 days** (6 weeks) of web training; 4 loci routes built in weeks 1–2; adaptive list length; weekly supervised lab session |
| Arm 2 — **active control** | **Adaptive dual n-back** working-memory training, 30 min/day × 40 days, identical monitoring and weekly lab visit |
| Arm 3 — passive control | No training |
| Outcome material | **Word lists only** — two counterbalanced lists of **72 concrete nouns**, 2 s/word |
| Outcomes | Free recall at 20 min and 24 h, pre and post; 4-month retest |

Results: Δ 20-min recall **F(2,48) = 21.5, p < 0.001, η² = 0.47**; Δ 24-h recall
**F(2,48) = 33.2, p < 0.001, η² = 0.58**; Δ at the 4-month retest **F(2,43) = 13.3, p < 0.001,
η² = 0.38**. Bonferroni contrasts: mnemonic > active control and > passive control (p < 0.001
each) at both delays; **active vs. passive not different (p > 0.9 at 20 min, p = 0.29 at 24 h)**.

**Four things this study does not show, all documented in the paper itself:**

1. **`NEGATIVE RESULT` — no transfer test of any kind was run.** Every cognitive outcome is free
   recall of 72-noun lists. A word-order recognition task was collected in the scanner but
   *"Recognition data have not been analyzed yet and will be presented elsewhere."* No
   fluid-intelligence, working-memory, comprehension, or curriculum outcome was reported.
2. **Ceiling effects censor the post-training data.** Verbatim: *"Given that both memory athletes
   and participants of the mnemonic condition after training showed strong ceiling effects in the
   memory task, no meaningful correlations were possible within these groups."*
3. **The neural finding is contrastive, not univariate.** Verbatim: *"none of the univariate
   differences between any of the groups were significant after correction for multiple
   comparisons… without comparison to the athlete/control connectivity difference pattern, no
   connectivity changes through mnemonic training would have been observed in our sample."*
4. **`NEGATIVE RESULT` inside the design** — the *active* control (adaptive dual n-back, matched
   dose, matched contact) produced **no** memory gain over doing nothing (p > 0.9). Dresler et al.
   is, incidentally, a well-controlled null for n-back training.

So: six weeks of method-of-loci training makes you much better at remembering lists of concrete
nouns, durably, and this reorganises functional connectivity. **The η² values are
*criterion-measure* effects — same task, same material class as trained.** In the
Melby-Lervåg/Redick taxonomy that is not even near transfer. `INFERENCE`

### 7.2 The meta-analysis, and what happens under publication-bias correction

**A 2025 systematic review and meta-analysis of the method of loci, *British Journal of
Psychology* 116(4):930–986, `doi:10.1111/bjop.12799`, PMID 40457944, PMC12514325** — **83
experimental studies** of MoL since 1968, assessed with RoB 2 and GRADE, pooled with a Bayesian
robust meta-analysis carrying publication-bias adjustment (RoBMA-PSMA). (Author name as returned
by the indexing services is rendered "Ondřej J."; the surname/given-name order looks
transposed in the metadata and should be checked against the journal before citation.)
`MEASURED-META`

Estimates are for MoL vs. rehearsal on immediate **serial** recall:

| Population | N | d [95% CI] | Bayes factor | τ | Publication-bias BF | **PET-corrected d** |
|---|---|---|---|---|---|---|
| Young adults | 936 | 0.42 [0.00, 0.80] | 6.24 | 0.46 | **6.41 × 10⁶** | **0.00 [0.00, 0.00]** |
| All young adults combined | 1,087 | 0.75 [0.00, 1.33] | 12.26 | 0.95 | 640,440 | small-study effects present |
| Older adults (pre–post) | 1,919 | 1.05 [0.00, 1.66] | 12.71 | 0.77 | 1.62 (anecdotal) | 0.24 [0.00, 2.79] |
| **All adults (headline)** | **3,006** | **0.88 [0.47, 1.25]** | 161.94 | 0.77 | **2.97 × 10⁶** | **0.04 [0.00, 0.00]** |

**`NEGATIVE RESULT`, and it is the most important number in this section.** The headline
**d = 0.88** is the bias-*unadjusted* posterior. The precision-effect test — the standard
small-study-bias correction — reduces it to **d ≈ 0.00–0.04**. Publication-bias Bayes factors are
in the millions. **89.2% of young-adult experiments were rated high risk of bias**; for older
adults, 55.6% high and the remaining 44.4% serious. The review's own GRADE verdict, verbatim:
*"the overall quality of evidence (GRADE) … is **very low**, meaning that the true effect may be
substantially different from our estimate."* For comparison, the earlier meta-analysis (Twomey &
Kroneisen, 2021) reported **d = 0.65 [0.45, 0.85]** without RoB 2 and without separating retention
intervals; it was not independently retrieved this session.

**`NEGATIVE RESULT` — and this one is a direct design constraint.** Study-level effects inside
single papers run from **d = −1.94 to d = +4.25**. Moè & De Beni (2005) is the clean demonstration:
with **oral** presentation of passages, MoL beat rehearsal (weighted **d = 0.93 [0.70, 1.16]**);
with **written** presentation the sign flipped — descriptive passages **d = −1.13 [−2.07, −0.18]**,
expository passages **d = −1.94 [−3.00, −0.87]**. De Beni et al. (1997, Exp. 3) found written
**d = −1.46** against oral **d = +4.25**. **The method of loci actively interferes with reading.**
It competes for the same visuospatial resources. Any AI system that offers a memory palace over
text is, on this evidence, likely to make things worse.

### 7.3 MoL on actual curriculum content — the whole literature is one study

Across the entire 83-study MoL corpus, **exactly one experiment used a knowledge/MCQ assessment**:

**Qureshi, Rizvi, Syed, Shahid & Manzoor (2014), "The method of loci as a mnemonic device to
facilitate learning in endocrinology…," *Advances in Physiology Education* 38(2):140–144,
PMID 25039085, PMC4056179.** Quasi-experimental, non-blinded. The whole class received two 60-min
didactic lectures; **28 randomly selected** students then received three further 60–90-min MoL
sessions (palaces sited on campus, built by two students and taught peer-to-peer), while the other
50 did a supervised open-book worksheet. Outcome: a single immediate **10-item MCQ**.
Result: **9.31 (SD 1.12) vs 8.10 (SD 1.85), p = 0.003**; computed from those means,
**d ≈ 0.74, 95% CI [0.25, 1.22]**. `OBSERVED` — not an RCT of the mnemonic.

**Why it cannot carry the claim:** the MoL arm got **3–4.5 additional contact hours plus peer
teaching**; the control got one worksheet session. Time on task and instructional format are fully
confounded with the mnemonic. There was **no delayed retest**, no transfer or problem-solving
items, a 10-item ceiling at 9.3/10, and the palaces were built by others rather than
self-generated. This is the *best* curriculum-content MoL study that exists, and it is this.

### 7.4 The memory-palace null

**Reser, Simmons, Johns et al. (2021), "Australian Aboriginal techniques for memorization:
Translation into a medical and allied health education setting," *PLoS ONE* 16(5):e0251710,
`doi:10.1371/journal.pone.0251710`, PMID 34003873, PMC8130951.** `MEASURED-RCT` (small).
Randomized 3-arm, incoming graduate medical students: **25 memory palace / 26 Australian
Aboriginal narrative method / 25 untrained.** Single 20-min training session; recall at baseline,
10 min, 20 min and **6 weeks**. (Cross-reference `I2-global-traditions.md` §6.1, which treats the
cultural-attribution and provenance questions this section does not.)

Odds of moving from imperfect recall to a perfect 20/20:

| Arm | Odds ratio | 95% CI |
|---|---|---|
| Australian Aboriginal narrative technique | **2.82** | **1.15 – 6.09** |
| **Memory palace** | **2.03** | **0.81 – 5.06** — includes 1, **not significant** |
| Untrained | 1.51 | 0.54 – 4.59 |

Kendall's W for within-arm improvement: Aboriginal 0.43, memory palace 0.37, untrained 0.17. For
*sequence* accuracy: Aboriginal W = 0.65 (p = 8 × 10⁻⁸), memory palace W = 0.31, untrained
**n.s.** (Q = 0.18, p = 0.9).

**`NEGATIVE RESULT`: the memory-palace arm did not reach significance on the primary
perfect-recall outcome.** The two trained arms were never directly compared and their CIs overlap
substantially, so the only defensible claim is *"the narrative technique produced a statistically
significant improvement where the memory palace did not"* — **not** that one beat the other.

Two further limits, from the paper: **severe ceiling** (median baseline ≥ 17/20; **22% (17/76) of
participants were already at 20/20 before training**, post-training means 18.8 ± 2.1 and
19.3 ± 1.8 out of 20); and the **6-week follow-up collapsed to n = 8 total** (3/3/2), with the
authors stating *"the sample was too small for accurate quantification."* Note also that the
material was a **20-item arbitrary butterfly-name list**, not curriculum content.

**A third memory-palace null.** **Legge, Madan, Ng & Caplan (2012), "Building a memory palace in
minutes: equivalent memory performance using virtual versus conventional environments with the
method of loci," *Acta Psychologica* 141(3):380–390, `doi:10.1016/j.actpsy.2012.09.002`.**
The primary is non-OA; the values below are from the 2025 meta-analysis's extraction table and are
flagged as second-hand. The **intention-to-treat group effect was null: ηp² = 0.002, p > 0.1.**
Effects appeared only after restricting to *compliant* participants (ηp² = 0.14), and even then
**virtual-MoL vs. control was d = 0.33 [−0.07, 0.73], n.s.**

**Adherence is its own null.** Gross et al. (2014, via the same meta): *"only about **25%** of
older adults chose to adopt MoL over simpler approaches like semantic grouping."* Anschutz et al.
(1987), 3-year follow-up: participants retained knowledge of the technique but *"**only one
individual continued to use it consistently**."*

Set all of that against §7.1 and the picture resolves cleanly: **the method of loci is a powerful,
durable, active-control-beating technique on the material it was invented for — arbitrary ordered
lists — and is unproven, publication-bias-fragile, actively harmful for written text, and rarely
sustained on the material learners actually need.** Both halves are supported; neither should be
reported without the other.

### 7.5 The keyword method — a clean, well-documented reversal at delay

The keyword mnemonic (link the L2 word to an acoustically similar L1 keyword via an interactive
image) is the most-studied applied mnemonic, and its literature contains one of the sharpest
delayed-reversal patterns anywhere in memory research.

**The founding result is real.** **Atkinson & Raugh (1975), *JEP:HLM* 1(2):126–133,
`doi:10.1037/0278-7393.1.2.126`** (technical-report version read in full: Stanford IMSSS TR-237,
ERIC ED096841). 120 Russian words over three days, experimenter-supplied keywords vs. an
unconstrained control. Pretest equivalence 55% vs. 56%. `MEASURED-RCT`

| Test | Keyword | Control |
|---|---|---|
| Comprehensive test (Day 4) | **0.72** | **0.46** |
| Delayed test (mean 43 days, unannounced) | **0.43** | **0.28** |

F(1,48) = 35.8, p < 0.001. Note for accuracy: absolute forgetting was larger for the keyword group
(−29 vs −18 points) but **proportional** forgetting was near-identical (−40.3% vs −39.1%).
**Atkinson & Raugh should not be cited as evidence of faster keyword forgetting; in relative terms
it is not.** `INFERENCE` (arithmetic on the published table). A separate detail worth keeping: the
imageability of the target word mattered for the control group (F(3,25) = 3.1, p < 0.05; recall
0.55/0.45/0.48/0.38 across imageability levels) but **not** for the keyword group
(0.75/0.71/0.71/0.72) — the mnemonic **neutralised material difficulty**, which is exactly the
property you would want it for.

**But the delayed picture is another matter.** Five independent lines, all verified at primary
abstract or full text this session:

| Study | Design | Finding (verbatim where quoted) |
|---|---|---|
| **Wang, Thomas & Ouellette (1992)**, *JEP* 84(4):520–528, `doi:10.1037/0022-0663.84.4.520` | 4 experiments; retention interval as a **between-subjects** factor | *"The findings consistently indicated that **long-term forgetting was greater for learners instructed to use the keyword mnemonic** than for learners engaged in rote rehearsal."* Their methodological point matters: earlier "gains are maintained" conclusions used **within-subject** comparisons, which *"are confounded by both rates of initial acquisition and level of immediate recall."* |
| **Wang & Thomas (1995)**, *JEP* 87(3):468–475, `doi:10.1037/0022-0663.87.3.468` | 3 experiments; keyword vs. **semantic-context** strategy; immediate vs. 2-day delay | *"The keyword mnemonic produced superior immediate performance… However, after 2 days, there was a **marked reversal** in performance, with higher levels of delayed recall associated with semantic-context learning."* Held for obscure English words and L2 vocabulary. Conclusion: *"keyword-based memories are **especially fragile over time** and will benefit from repeated testing and rehearsal."* |
| **Thomas & Wang (1996)**, *JEP:Applied* 2(4):330–342, `doi:10.1037/1076-898X.2.4.330` | 3 experiments; self-generated keywords; mnemonic pictures | *"Although using the keyword mnemonic… enhances performance on tests of immediate cued recall when compared with control strategies, **the reverse is true after a delay**."* **Self-generating the keyword did not attenuate forgetting.** |
| **Campos, González & Amor (2003)**, *J. Gen. Psychol.* 130(4):399–413, `doi:10.1080/00221300309601166`, PMID 14672102 | **4 classroom experiments**, 30 Latin→Spanish words, adolescents and adults | **"In all experiments, the rote method was significantly more effective than was the keyword method."** A full reversal **even at immediate test**, in real classrooms. |
| **Carney & Levin (1998)**, *Contemp. Educ. Psychol.* 23(3):276–297, PMID 9665791 | 5 experiments — the **pro-keyword rebuttal** | Consistent mnemonic advantage in acquisition and at delay. **But:** *"these positive delayed findings were tempered by the observation that, in terms of absolute number retained, there was a **somewhat faster forgetting rate for mnemonic students** in comparison to repetition controls."* |

**And the finding that should reshape any product built on this.** **Dikmans, van den Broek &
Klatter-Folmer (2020), *Memory* 28(7):908–917, `doi:10.1080/09658211.2020.1797094`, PMID 32723148**
(n = 30, think-aloud, 6–8 day retention): learners **abandoned the keyword for 21.6% of words**,
on average after **8.27 retrievals** — and **shifting to direct, unmediated retrieval predicted
higher form and meaning recall** at 6–8 days. `MEASURED`

**The mnemonic is scaffolding to be discarded, not the end state.** A system that keeps a learner
routed through a keyword forever is holding them at the wrong end of that transition. A system
that *notices* the transition and drops the mediator is doing something no flashcard app does —
and detecting it is exactly what §11.1's `attempt` table (raw response + latency + cue form)
makes observable.

**Interaction with retrieval practice.** **Miyatsu & McDaniel (2019), *Memory & Cognition*
47(7):1328–1343, PMID 31077068:** with retrieval limited to two attempts, **E1 (48-h delay) found
*no* testing effect with retrieval practice alone**, and keyword+retrieval was **no better than
keyword alone**. At one week, keyword+retrieval beat keyword alone — but *"in the absence of
keyword encoding there was no retrieval practice effect."* A 2024 replication-adjacent study
(*Heliyon* 10(3):e24586, n = 110 Chinese EFL learners) likewise found that with retrieval
constrained to two attempts, **retrieval practice alone did not exceed restudy**. `MEASURED`
`NEGATIVE RESULT` for under-dosed retrieval practice — two retrievals is not enough, which is a
directly actionable dosage constraint for §11.

**Meta-analytic estimate for the keyword method: none could be verified.** Pressley, Levin &
Delaney (1982), *Review of Educational Research* 52(1):61–91, `doi:10.3102/00346543052001061` is
the canonical review and is **non-OA and UNREACHABLE-IN-SESSION**; no modern quantitative
meta-analysis surfaced. **Do not cite a pooled keyword-method effect size.** The authoritative
current verdict is categorical: **Dunlosky et al. (2013) rate the keyword mnemonic LOW utility**
(§6.4).

### 7.6 Mnemonic instruction in special education — and a widely-cited number that could not be verified

This literature reports the largest mnemonic effects anywhere, and it is directly relevant to
`H1-selpa-accessibility.md`.

**Scruggs, Mastropieri, Berkeley & Graetz (2010), "Do special education interventions improve
learning of secondary content? A meta-analysis," *Remedial and Special Education* 31(6):437–449,
`doi:10.1177/0741932508327465`.** 70 studies, > 2,400 students, published 1984–2006; secondary
students with disabilities (67.1% learning disabilities). The primary is non-OA; the figures below
come from the NICHCY Research-to-Practice Structured Abstract No. 80 (ERIC ED572694), a secondary
summary of that meta — **flagged as second-hand**. `MEASURED-META`

| Category | Weighted mean ES |
|---|---|
| **Overall** | **1.00** |
| — treatment effects | 1.02 |
| — maintenance effects | 1.13 |
| — **generalization effects** | **0.68** |
| **Mnemonic strategies (k = 21)** | **1.47** |
| Classroom learning strategies | 1.11 |
| Spatial/graphic organizers (k = 14) | 0.93 |
| Computer-assisted instruction (k = 7) | 0.63 |

**Read the moderators before the headline.** From the same source: *"Intervention sessions led by
researchers had the highest effect sizes,"* followed by special educators, with general educators
producing *"more moderate"* effects; interventions *"conducted in a separate room within the
school were significantly higher"* than in general- or special-education classrooms; and *"only a
small number of the studies took place in inclusive classrooms."* The authors also bound their own
claim: mnemonics *"specifically focused on teaching students to make verbal associations between
facts. These strategies are effective in helping students to memorize material such as **lists,
groups, and chronologies**."*

**`NEGATIVE RESULT` of a different kind — generalization is the smallest of the three effect
categories (0.68 vs. 1.02 treatment).** The pattern holds across every mnemonics literature in
this section: large on the trained material, smaller on anything else.

**⚠️ A widely-repeated number that could not be verified.** The frequently-cited "mnemonic
instruction ES ≈ 1.62" traces to Mastropieri & Scruggs (1989), *Educational Psychology Review*
1:83–111, `doi:10.1007/BF01326638`, and/or Forness, Kavale, Blum & Lloyd (1997), *Teaching
Exceptional Children* 29(6):4–9. **Both are paywalled and UNREACHABLE-IN-SESSION; ERIC returns
descriptive abstracts with no numbers. The 1.62 figure was not found in any openable primary
source and is not reproduced here.** The verified, larger-corpus, more recent number is
**ES = 1.47** (Scruggs et al. 2010).

Adjacent verified figure: **Therrien, Taylor, Hosp, Kaldenberg & Gorsh (2011)**, science
instruction for students with LD, ERIC EJ947712 — 12 studies, **overall mean ES = 0.78**, with
mnemonic instruction singled out as *"highly effective at increasing learning disabled students'
acquisition and retention of science **facts**."* Facts, not reasoning. `MEASURED-META`

### 7.7 The far-transfer null that governs the whole category

**Melby-Lervåg, Redick & Hulme (2016), "Working memory training does not improve performance on
measures of intelligence or other measures of 'far transfer': evidence from a meta-analytic
review," *Perspectives on Psychological Science* 11(4):512–534,
`doi:10.1177/1745691616635612`, PMID 27474138, PMC4968033.** **87 publications, 145 experimental
comparisons.** `MEASURED-META`

| Outcome | vs. **active** controls, g [95% CI], k |
|---|---|
| **Nonverbal ability (fluid IQ)** | **0.05 [−0.02, 0.13]**, k = 67 |
| Verbal ability | 0.05 [−0.07, 0.17], k = 22 |
| Word decoding | 0.08 [−0.09, 0.24], k = 10 |
| Reading comprehension | 0.15 [0.03, 0.27] → **0.08** after removing control-group-decline artefacts |
| Arithmetic | 0.06 [−0.08, 0.19], k = 15 |
| Verbal working memory (intermediate transfer) | 0.31 [0.19, 0.42] |
| **Criterion (trained) measure** | **0.80 [0.62, 0.97]**, k = 22 |

The sample-size moderator is the tell, verbatim: *"For treated controls, the k = 34 studies
meeting the minimum recommended sample sizes produced **no effect, g = 0.01**, whereas the k = 25
comparisons with fewer subjects produced a significant effect, g = 0.26."* And the authors'
conclusion: *"analysis of publication bias shows that there is **no evidential value** from the
studies of working memory training using treated controls."* A 2024 corroborating meta
(*Psychonomic Bulletin & Review*, PMC11543728, 52 comparisons) found WM **SMD = 0.18** overall but
**SMD = 1.15** when restricted to tasks resembling the trained ones, with fluid intelligence
unimproved and *"improvements in WM were not related to changes in fluid intelligence."*

**Why this belongs in a section on remembering:** it is the same shape as everything above.
**Effects are large on the trained task, intermediate on tasks that look like it, and
indistinguishable from zero on anything genuinely different.** That is the prior any AI system
should hold about its own memory-training claims — including the one specified in §11.

### 7.8 What an LLM changes here — and what it does not

Manufacturing a mnemonic used to be the bottleneck: a good keyword mnemonic or a vivid locus image
is a small creative act, and doing it for 2,000 vocabulary items is why nobody does it. That
constraint is gone. **SmartPhone** (Kang, Zhu et al., arXiv:2305.10436) builds an end-to-end
pipeline that auto-generates **keyword-mnemonic verbal and visual cues** with an LLM and evaluates
them against manually generated cues in a human-participant experiment. `DEMO` — a capability
demonstration; it does not establish a retention advantage over ordinary retrieval practice.

**The guardrail, and it is the same one as §5.2:** Bertsch et al. (2007) found the generation
effect is **null for nonwords (d = 0.05)** and **reverses for anagrams (d = −0.05)**. A mnemonic
is useful when it binds new material to *existing* semantic and episodic structure. An
auto-generated keyword link that is merely phonetically clever, with no meaningful bridge, is
closer to an anagram than to a memory palace. **Automatic mnemonic generation makes the technique
cheap; it does not make it valid.** Validity has to be measured per item, which is exactly what
§11.4's third gate specifies.

**§11's position, stated as a deliberate omission (see §11.7):** mnemonics are not a core
mechanism of the proposed system. They are a legitimate *optional* encoding aid for genuinely
arbitrary material — the parts of a domain that really are unmotivated lists (nomenclature,
irregular forms, unit prefixes, drug names) — and they should be offered exactly there and
nowhere else. Using them on material that has structure substitutes an arbitrary association for
an available explanation, which is a bad trade with a measured downside: it is the mechanism by
which "learned the card, not the content" happens.

**Three concrete engineering rules fall out of §7.2–§7.6, and they are unusually specific:**

1. **Never overlay a spatial mnemonic on written text.** Moè & De Beni (2005): oral presentation
   **d = +0.93**, written presentation **d = −1.13 to −1.94**. If the material is being read, the
   memory palace competes with it.
2. **Treat the mnemonic as a mediator to be dropped, and instrument the drop.** Dikmans et al.
   (2020): learners abandoned keywords for **21.6%** of words after ~8.27 retrievals, and
   *abandoning predicted better recall*. The system's job is to detect the transition to direct
   retrieval and stop presenting the mediator — a state change no flashcard app models.
3. **Two retrievals is not a dose.** Miyatsu & McDaniel (2019) found **no testing effect at all**
   at a 48-hour delay with retrieval limited to two attempts; the *Heliyon* (2024) study found the
   same. Whatever else §11 gets wrong, it must not under-dose retrieval.

---

## 8. Knowledge tracing as the modern replacement for fixed schedules

**The model-by-model forensics live in `F5-learner-model.md` §2 and are not repeated.** This
section asks the questions F5 does not: *did deep knowledge tracing ever actually beat logistic
regression?* and *if you had a better tracer, would you get a better schedule?*

### 8.1 The founding claim, and what happened to it

**Piech et al. (2015), "Deep Knowledge Tracing," *NeurIPS* 28:505–513, arXiv:1506.05908.**
`MEASURED-BENCH` Table 1 as published:

| Dataset | Marginal | BKT | BKT* | **DKT** |
|---|---|---|---|---|
| Simulated-5 | 0.64 | 0.54 | — | **0.82** |
| Khan Math | 0.63 | 0.68 | — | **0.85** |
| **Assistments** | 0.62 | 0.67 | 0.69 | **0.86** |

Contribution 2 in the paper: *"A 25% gain in AUC over the best previous result on a knowledge
tracing benchmark."* The arithmetic is (0.86 − 0.69)/0.69 = 24.6% — a **relative** increase in raw
AUC, not normalised to the 0.5 chance floor. `INFERENCE` (arithmetic on their stated numbers)

**Three independent 2016 replications took that number apart.** `MEASURED-BENCH` ×3

**(a) Xiong, Zhao, Van Inwegen & Beck (2016), EDM 2016, 545–550** found three defects in the
ASSISTments 2009-2010 set:

1. **Random row duplication — 123,778 of 525,535 rows (23.6%).** Verbatim: *"large chunks of
   records are duplications that should not be there for any reason… This is definitely an error
   in the data set."*
2. **Scaffolding problems included** (73,466 rows) that BKT and PFA exclude: *"Lua DKT had the
   advantage of additional information; thus, the prediction results cannot be compared fairly."*
3. **Multi-skill rows repeated per skill**, so the RNN sees the same response consecutively.

Corrected, 5-fold student-level CV:

| Dataset variant | DKT (Torch/TF) | **PFA** | BKT |
|---|---|---|---|
| 09-10 (a) duplicates removed | 0.79 / 0.81 | 0.70 | 0.60 |
| 09-10 (b) + scaffolding removed | 0.79 / 0.82 | 0.73 | 0.63 |
| **09-10 (c) + multi-skill repeats eliminated** | **0.73 / 0.75** | **0.73** | 0.63 |
| 14-15 (clean) | 0.70 / 0.70 | **0.69** | 0.64 |

**The smoking gun**, verbatim: splitting 09-10(b) predictions by position, *"predictions on
repeated data points… have nearly perfect performance metrics (**AUC = 0.97, r² = 0.74**). On the
other hand, the leading records… have much lower prediction results (**AUC = 0.77, r² = 0.23**)."*
It was substantially predicting answers it had already been shown. Their verdict: *"the DKT
algorithm did not achieve overwhelmingly better performance when compared to PFA model on
ASSISTments data sets when they are properly prepared."* **0.86 → 0.75, and PFA ties it.**

**(b) Wilson, Karklin, Han & Ekanadham (2016), EDM 2016, 539–544** (Knewton) independently found
and removed the duplicates, then evaluated under an online-prediction protocol matching Piech et
al.'s task:

| Dataset | IRT | TIRT | **HIRT** | **DKT** |
|---|---|---|---|---|
| ASSISTments — AUC | 0.7651 | 0.7653 | **0.7740** | **0.7429** |
| KDD Bridge-to-Algebra — AUC | 0.8542 | 0.8542 | **0.8597** | **0.8110** |
| Knewton proprietary — AUC | 0.8045 | 0.8166 | **0.8189** | **0.7756** |

**DKT is last on every dataset on both accuracy and AUC.** And the sentence that settles the
provenance question, verbatim: *"**we were able to reproduce the performance reported in [Piech et
al.] when applying our RNN implementation on the raw data set (with duplicates left in).**"*

**(c) Khajah, Lindsey & Mozer (2016), "How Deep is Knowledge Tracing?", EDM 2016 Best Paper,
arXiv:1604.02416** decomposed the remaining gap, verbatim:

> "**31.6% of difference in performance reported in [Piech et al.] appears to be due to the use of
> a biased procedure for computing the AUC for BKT. Another 50.6% of the difference in performance
> reported vanishes if BKT is augmented to allow for forgetting.**"

**~82% of the headline is an evaluation artefact plus one standard BKT extension.** The AUC issue
is precise: Piech et al. pooled all trials into one ROC curve, while the 0.69 baseline they cited
averaged per-skill AUCs — which *"suppresses any lift due to being able to predict the relative
accuracy of different skills."* **The 0.86 and the 0.69 were never computed the same way.** With
forgetting, ability and item-difficulty extensions, enhanced BKT beat DKT by 0.05 AUC on Synthetic
and 0.01 on Spanish, and lost by 0.03 on ASSISTments and 0.01 on Statics. Their verdict:
*"knowledge tracing may be a domain that does not require 'depth'."*

**The provenance chain for one number, ASSISTments 2009:**

| Value | Source | What changed |
|---|---|---|
| **0.86** | Piech et al. 2015 | duplicates in, scaffolding in, repeats in, pooled AUC |
| 0.82 | Xiong 2016 (09-10b) | duplicates and scaffolding removed |
| **0.75** | Xiong 2016 (09-10c) | multi-skill repeats eliminated |
| 0.757 | Gervet 2020 | nested CV, tuned |
| **0.7541** | pyKT 2022 | standardized, question-level, no leakage |
| 0.7429 | Wilson 2016 | online-prediction protocol |

And on the same data: **Best-LR 0.772, BKT+ 0.759, PFA 0.724, IRT 0.692.** *A logistic regression
beats every published DKT number for this dataset once the dataset is fixed.*

**One row of the original table can never be checked:** the Khan Academy dataset (AUC 0.85) was
never released. Khajah et al. state they were refused access even with a DKT co-author's help.
And arXiv:1506.05908 still carries **only v1 and no erratum**.

### 8.2 Where the field stands now

**Gervet, Koedinger, Schneider & Mitchell (2020), *JEDM* 12(3):31–54** — nine datasets, 5-fold
nested CV at learner level, against `Best-LR` (PFA with log-scaled counts plus IRT ability and
difficulty terms). `MEASURED-BENCH`

| Model | algebra05 | bridge06 | assist09 | assist12 | assist17 | statics | squirrel | spanish | assist15 |
|---|---|---|---|---|---|---|---|---|---|
| **Best-LR** | **0.831** | **0.803** | **0.772** | 0.751 | 0.714 | 0.819 | 0.765 | **0.863** | 0.702 |
| **DKT** | 0.821 | 0.790 | 0.757 | **0.771** | **0.770** | **0.829** | **0.772** | 0.832 | **0.731** |
| SAKT | 0.801 | 0.784 | 0.756 | 0.732 | 0.722 | 0.813 | 0.771 | 0.831 | 0.730 |
| PFA | 0.769 | 0.741 | 0.724 | 0.669 | 0.619 | 0.691 | 0.614 | 0.847 | 0.690 |
| IRT | 0.768 | 0.749 | 0.692 | 0.713 | 0.681 | 0.789 | 0.733 | 0.679 | 0.638 |

**Best-LR wins 4 of 9; DKT wins 5 of 9.** DKT's winning margins: **+0.007, +0.010, +0.020, +0.029,
+0.056** — and the largest, on assist17, *"closes to +0.016 AUC"* when restricted to first
attempts. The conditions are now characterised, and they are useful:

| Condition | Winner | Authors' mechanism |
|---|---|---|
| **Fewer than ~1M interactions** | **Logistic** | *"DKT overfits small datasets but LR underfits large datasets"* |
| **Sequential progression** through material | **DKT** | *"DKT makes better use of the temporal order of the sequence"* — holds even for per-KC DKT |
| **Thousands of interactions per learner** | **Logistic** | *"DKT plateaus after 1000 student interactions, whereas Best-LR keeps improving… DKT is unable to keep track of long-term information"* |
| **Cold start** | **DKT** | *"DKT needs **6 times fewer interactions** than Best-LR to reach close to peak performance"* (10 vs 60) |

Two ablations that undercut deep KT's own marketing:

- **DKT needs the expert knowledge-component model.** *"DKT — although initially advertised as
  independent from any expert-designed structure — **relies on the KC model to perform
  optimally**."* On assist09 the swing is 0.702 (items in/out) → 0.757 (KCs in/out).
- **DAS3H's mechanism did not replicate.** *"the time-window features introduced in DAS3H (best
  paper at EDM 2019) **do not add any predictive power** to our best logistic regression model…
  the performance boost of DAS3H over PFA is simply due to the addition of an item difficulty
  parameter inspired by IRT, rather than time-windows."* `NEGATIVE RESULT`
- **SAKT did not replicate.** *"SAKT underperforms DKT on all datasets… the authors reported an
  AUC of 0.85 [on ASSISTments 2015], while we observed **0.73**… they reported an AUC of 0.82…
  for a simple baseline — **which we could not reproduce and seems impossible**."* `NEGATIVE RESULT`

**The features-versus-architecture result.** **Schmucker, Wang, Hu & Mitchell (2022), *JEDM*
14(1):1–45** ran four very large modern datasets (18–26M responses each). There **DKT genuinely
beats Best-LR on all four** — but **AugmentedLR**, a logistic regression fed richer features
(video watched/skipped, lag time, prerequisite structure), **beats DKT on 3 of the 4**:

| Model | ElemMath AUC | EdNet AUC | Eedi AUC | Junyi15 AUC |
|---|---|---|---|---|
| Best-LR | 78.44 | 72.94 | 79.01 | 76.20 |
| **DKT** | 79.71 | 74.92 | **81.55** | 80.62 |
| **AugmentedLR** | **79.87** | **75.00** | 80.96 | **86.03** |

Similarly **Pavlik & Eglington (2023), *JEDM* 15(3):58–86** found automated feature search over
logistic KT models beat DKT/SAKT/IKT on all three of their datasets *"typically requiring multiple
orders of magnitude fewer parameters."*

> **The generalizable finding is about *features*, not architecture: the largest single win in
> this literature came from logging more about the learner, not from a bigger network.**

**And the reproducibility audit.** **Liu et al. (2022), pyKT, NeurIPS Datasets & Benchmarks,
arXiv:2206.11460:** *"due to the lack of agreed upon training and evaluation procedures, the
published DLKT results surprisingly diverge. For example, **the reported AUC scores of DKT and AKT
on ASSISTments2009 range from 0.73 to 0.821 and from 0.747 to 0.835 respectively.**"* They
identify a **label-leakage** pattern — expanding multi-KC questions into a KC sequence and
predicting the next KC *given the ground-truth label of the previous KC of the same question* —
and name the AKT, SAKT and DKVMN implementations as affected. Mean inflation: **+8.38% AUC on
ASSISTments 2009 and +13.09% on Algebra 2005.** Their Observation 1: *"**The majority of recently
proposed DLKT approaches cannot beat the vanilla DKT model.**"* SAKT and SAINT — the transformers —
**underperform the 2015 LSTM in most cases.** AKT survives as the best model but its ASSISTments
2015 claim of +0.052 over DKT becomes **+0.0014** under standardized evaluation. `NEGATIVE RESULT`

**The most deflating result of all.** **Ding & Larson (2019), "Why Deep Knowledge Tracing Has Less
Depth than Anticipated," EDM 2019, ERIC ED599227** randomly initialised the LSTM and trained
**only the final linear layer**:

| Dataset | Full DKT | **DKT (untrained recurrence)** | PFA |
|---|---|---|---|
| 09-10 (a) | 0.81 | **0.79** | 0.70 |
| 09-10 (c) | 0.75 | **0.73** | 0.73 |
| 14-15 | 0.70 | **0.68** | 0.69 |
| KDD | 0.79 | **0.76** | 0.71 |

Verbatim: *"a randomly initialized DKT with only the final linear layer trained achieves similar
results to the fully trained DKT model… **This is a worrying conclusion because it means the
underlying recurrent representation may not be reliable nor semantically meaningful.**"* Their
diagnosis: *"the DKT model is most likely learning an 'ability' model, rather than tracking each
individual skill."*

Corroborating from a different angle: **Yeung & Yeung (2018), L@S, arXiv:1806.02180** showed DKT's
predicted knowledge state **oscillates** and **fails to reconstruct the input it just observed** —
AUC(C) 0.904 vs AUC(N) 0.821 on ASSISTments — while its headline next-item AUC is unaffected.
**Next-item AUC is blind to whether the model tracks knowledge at all.**

### 8.3 The prediction/decision gap — three results that should end the AUC race

**(a) The ceiling is already reached.** **Beck & Xiong (2013), "Limits to Accuracy: How Well Can We
Do at Student Modeling?", EDM 2013, 4–11** built "cheating models" with oracle access:

| ASSISTments (86,528 first attempts) | AUC |
|---|---|
| CM3 — knows initial knowledge + continuous knowledge + item difficulty | 0.884 |
| CM1 — **perfect learning detector** + known initial knowledge | 0.804 |
| **CM2i — perfect learning detector** | **0.747** |
| **PFA baseline** | **0.745** |

**A model that knows the exact moment each student learns each skill beats PFA by 0.002 AUC.**
And across 178,000 data points five student-modelling techniques *"intercorrelated with each other
at **0.92** on average… If PPS is removed, the remaining four intercorrelated at **0.96, an
astonishingly high value**."* Their conclusions, verbatim:

> *"Imagine a research result were published in EDM 2014 with a new student modeling approach that
> achieved an A′ of 0.9… **But, what would we actually do with the model? This question is
> non-rhetorical, as the authors do not have a good answer.**"*
> *"**Ironically, as a field we have settled on a common test problem that has little impact on
> tutorial decision making or on informing student knowledge.**"*
> *"the research thread of predicting next item correctness is approaching limits to accuracy, and
> **has probably progressed beyond a useful point**."*

**(b) Equal predictive accuracy does not mean equal decisions.** **Rollinson & Brunskill (2015),
"From Predictive Models to Instructional Policies," EDM 2015, 179–186.** BKT, PFM and AFM had
RMSEs within 0.015 of one another on KDD Cup Algebra. They then derived a when-to-stop policy from
each:

| Comparison | r (all skills) |
|---|---|
| AFM vs PFM | 0.32 |
| **AFM vs BKT** | **−0.06** |
| **PFM vs BKT** | **0.16** |

**Skills where the derived policy stops practice immediately: BKT 31 (6%), PFM 130 (26%), AFM 295
(59%).** Verbatim: *"**models with similar predictive error rates can lead to very different
policies. This suggests that if they are to be used for instructional decision making, student
models should not be judged by predictive error rates alone.**"*

**(c) The metric itself picks different winners.** **Pelánek (2015), "Metrics for Evaluation of
Student Models," *JEDM* 7(2):1–19.** Across 20 simulated datasets with 15 candidate models, the
number of times two metrics selected the *same* best model:

| | AUC | LL | MAE | RMSE |
|---|---|---|---|---|
| **AUC** | — | **5/20** | 2/20 | **7/20** |
| RMSE | 7/20 | 17/20 | 3/20 | — |

**AUC and RMSE agree on the best model 35% of the time; AUC and log-likelihood 25%.** Verbatim:
*"the choice of metric is really important and can influence conclusions of experiments,"* and AUC
*"has **poor relation to over-practice and under-practice** and… is **unsuitable for optimizing
parameter values**."* Pelánek's follow-up (*UMUAI* 2018, 28:207–235) shows methodology choices —
truncating at 10 vs 50 answers per student, global vs per-student RMSE averaging, global vs per-KC
AUC — each **flip the model ranking**, and that BKT parameters fit to the *same students* differ
more by truncation depth than by anything about learning: P(L₀)/P(T)/P(S)/P(G) =
0.52/0.41/0.28/0.21 at 10 answers vs **0.16/0.37/0.07/0.21** at 50. *"the fitted parameters can be
more influenced by details of data collection than by properties of learning."*

Pelánek also names the structural problem an AI learning system inherits: **the logs used for
evaluation are produced by a policy driven by the model, so the model can suppress the very data
that would reveal its deficiencies.** *"In weather forecasting models do not directly influence the
system and cannot distort collected data, in student modeling they can."*

**And a live case where AUC ranked the wrong model.** In Settles & Meeder's own backtest (§4.4),
**Leitner had the highest AUC of everything tested (0.542) — and Leitner is the model Duolingo
dropped.** The deployment decision was made on MAE and user feedback, explicitly against the AUC
ranking. `MEASURED-BENCH`

### 8.4 What this means, and why it is good news

Put §4 and §8 side by side. Neither literature cites the other:

| | Spaced repetition (§4.2) | Knowledge tracing (§8.2) |
|---|---|---|
| Ceiling | AUC ≈ 0.70 per-user; 0.83 cross-user with rich context | AUC ≈ 0.67–0.83 |
| Best simple baseline | 34-feature logistic regression **beats FSRS-6/7 on all three metrics**; zero-parameter MOVING-AVG beats them on log loss | **Best-LR ties or beats DKT on 4/9**; BKT-with-features is indistinguishable from DKT; **AugmentedLR beats DKT on 3/4 large datasets** |
| Movement since ~2015 | small | essentially none once evaluation is standardized |
| Where big models help | cross-user context and extra features | **cold start** (6× fewer interactions) |
| Interventional evidence | 1 strong RCT for paired associates; **0 for 8** for interdependent content | none located |

**This is one finding, discovered twice, in two communities that do not read each other: the
predictive ceiling on individual response outcomes was reached by simple models, and the residual
is largely irreducible noise.** Beck & Xiong's cheating model puts a number on it — an oracle that
knows the moment of learning is worth **+0.002 AUC**.

**Three places the returns actually are:**

1. **The features, not the model.** RWKV-P's win comes from *seeing more* (answer duration, sibling
   cards, deck hierarchy). AugmentedLR's win comes from *seeing more* (video behaviour, lag time,
   prerequisites). Both say: instrument better, don't model harder. `INFERENCE` from
   `MEASURED-BENCH`
2. **The decision, not the prediction.** Rollinson & Brunskill show that models within 0.015 RMSE
   produce stop-policies correlated at **r = −0.06**. The decision is not determined by the
   prediction, and almost nobody has evaluated the decision. **This is an open, cheap, high-value
   experimental programme, not a dead end.**
3. **What is being traced.** Gervet et al. found expert knowledge-component models add **≤ +0.01
   AUC on 7 of 9 datasets**, and that on 4 of 9 a KC-only model fails to beat an
   item-difficulty-only model — which they read as evidence the hand-built domain models are **low
   quality**. Building a good knowledge-component graph was previously a multi-year expert task.
   It is now, for the first time, automatable. **That, not a better tracer, is the unlock.**
   `INFERENCE`

### 8.5 Two cautions to carry into §11

- **Calibration, not AUC, is what a scheduler consumes.** Gervet et al.: *"the current best models
  are severely biased on some datasets — hindering their applicability in adaptive policies and
  open learner models."* On assist09 both models *"severely overestimate learners when the
  probability of correct answer is low, and underestimate… when high."* A scheduler that turns
  p(recall) into a due date needs the *number* right, not the *ranking* — and §4.2's
  `RMSE-BINS-EXPLOIT` is the standing warning that even calibration metrics can be gamed.
- **Identifiability was flagged in 2007 and never fixed.** Beck & Chang (2007),
  `doi:10.1007/978-3-540-73078-1_17`: BKT's four parameters are not uniquely determined by the
  data — multiple parameter sets fit equally well while implying very different pedagogy.
  Corbett & Anderson flagged the same class of failure in the *founding* paper: after remediation
  to mastery, *"the model was completely insensitive to individual differences among students…
  There was no variability in the knowledge estimates across students,"* while raw tutor error
  rate still predicted posttest performance at **r = −0.64**. `MEASURED-BENCH`
  **Any learner-facing readout derived from such parameters ("your mastery is 73%") is reporting
  one arbitrary point from an equivalence class** — the same category of error as ZemoMemo's
  "stickiness" (§1.3a).

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
4. **When retention is being bought at a ruinous exchange rate.** The DR-workload table (§4.9,
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
| **Delay the first retrieval**; this is the highest-leverage timing variable | Karpicke & Roediger 2007, Exp. 3 — delaying the first test helped *regardless* of how repeated tests were spaced | `MEASURED-RCT` |
| Do **not** assume expanding intervals are required | §3; Karpicke & Roediger 2007; Logan & Balota 2008 (expanded items at a *disadvantage* at 24 h) | `MEASURED-RCT` |
| **Never fewer than ~4 retrievals** per concept before treating it as scheduled | Miyatsu & McDaniel 2019: **no testing effect at 48 h with 2 retrievals**; *Heliyon* 2024 replicates | `MEASURED` |
| **Index difficulty to prior knowledge**, and therefore measure prior knowledge | Bjork & Bjork 2020: *"If … the learner does not have the background knowledge or skills to respond to them successfully, they become undesirable difficulties"*; expertise reversal (B1 §4) | `MEASURED-META` |
| Difficulty is **not** the active ingredient — successful retrieval and elaboration are | Bertsch 2007 anagram **d = −0.05**; Healy et al. 2025, 6 experiments, no delayed benefit from difficulty | `MEASURED-META` / `MEASURED` |
| **Never overlay a spatial mnemonic on written text** | Moè & De Beni 2005: oral **d = +0.93**, written **d = −1.13 to −1.94** | `MEASURED-META` (via the 2025 MoL meta's extraction) |
| Do **not** claim the scheduling algorithm is the source of the gain | §4.6 | `NEGATIVE RESULT` |
| Treat item validity as an instrumented property | arXiv:2507.05629 §5.1; C2 | `OBSERVED` |
| Optimise on **delayed, held-out** outcomes only — never on satisfaction, streaks, or confidence | Deslauriers 2019: FOL **−0.56 SD** while TOL **+0.46 SD**; Kornell & Bjork 2008: 78%/78% inversion | `MEASURED-RCT` |

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
   moving average is competitive with FSRS-7 and a 34-feature logistic regression beats it — the
   system uses **a well-calibrated logistic model over the `attempt` features**, not a bespoke
   memory model, and does **not** invest in scheduler sophistication. Treat the choice as
   low-stakes, because §4.2, §4.9, §8.2 and §8.3 all say it is.

**Where the learner model is actually spent: calibrating the *item*, not choosing the *time*.**
This is the least obvious commitment in the specification and it has direct evidence.
**Papoušek, Stanislav & Pelánek (2016)** randomized ~20,000 learners across ~1.3M answers into a
2 × 2 of adaptive/random **item selection** × adaptive/random **option construction**, and found:
*"In all cases the conditions with **adaptive construction of options** beat the conditions with
random options… **The item selection part does not seem to have large effect on learning.**"*
`MEASURED-RCT` (§4.6viii)

So the model's highest-value job is **difficulty-calibrating what appears inside the item** — which
distractors, which phrasing, which level of the explanation ladder — not deciding which day the
concept resurfaces. That is exactly the job an LLM can now do at generation time and could not do
before, and §11.4 is where it lives.

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
  the outcome most consistent with §3, §4.2, §4.6 and §4.9.

**Five secondary, independently falsifiable claims — ordered by cost, cheapest first:**

- **H4 (first-retrieval delay) — run this one first.** Pushing the *first* retrieval of a new
  concept later, holding the total number of retrievals and the subsequent schedule constant,
  improves delayed retention more than any change to the expansion ratio. This is a direct
  extension of **Karpicke & Roediger (2007, Exp. 3)** — which found delaying the first test helped
  *regardless of how repeated tests were spaced* — from word pairs at 2 days to conceptual material
  at ≥ 8 weeks. **No shipped SRS implements it; Anki's 1-day/6-day graduating defaults do the
  opposite.** It is a one-parameter change and the cheapest experiment in this document.
- **H5 (horizon).** Setting the gap ratio from a stated retention horizon (Cepeda et al. 2008:
  20–40% of a 1-week horizon declining to 5–10% of a 1-year horizon) beats a fixed ratio at equal
  review count. Also unimplemented anywhere; also cheap.
- **H2 (interference).** Co-scheduling semantically adjacent concepts in the same session produces
  *lower* retention of the non-retrieved neighbour than spacing them apart. Tests
  retrieval-induced forgetting as an engineering constraint. Currently `INFERENCE` — and note that
  §10's pooled effect size for retrieval-induced forgetting could not be verified, so this is
  genuinely open.
- **H3 (inert detection).** Learners flagged `inert` benefit more from re-representation (worked
  example / laddered explanation) than from additional retrieval attempts, relative to non-flagged
  learners. Tests §11.3.
- **H6 (mediator drop).** Where a mnemonic mediator is offered for genuinely arbitrary material,
  learners who transition to direct unmediated retrieval outperform those held on the mediator.
  This is a direct replication target for **Dikmans et al. (2020)** — 21.6% of words abandoned
  after ~8.27 retrievals, with abandonment predicting *better* recall — extended to a system that
  actively detects and honours the transition.

**On generality — the prior this specification holds about itself.** §7.7 is the discipline's
best-documented pattern: **effects are large on the trained task, intermediate on tasks that look
like it, and indistinguishable from zero on anything genuinely different** (Melby-Lervåg, Redick &
Hulme 2016: criterion measure g = 0.80, fluid intelligence g = 0.05 [−0.02, 0.13]). H1's
held-out, human-authored, never-before-seen transfer test exists precisely because that is the
measurement that has repeatedly killed claims in adjacent fields. **If this system works, it must
work on that test. If it only works on items drawn from its own pool, it has not been shown to
work at all.**

### 11.7 What this specification deliberately does not do

- **It does not invest in scheduler sophistication.** §4.2: a zero-parameter moving average
  matches FSRS-7 on calibration; a 34-feature logistic regression beats it. §4.9: Memrise's fixed
  ladder is within ~2% of tuned FSRS in simulation. Effort spent on the arithmetic has a
  measured near-zero return. Note the honest counterweight: **Lindsey et al. (2014) measured
  personalised spacing beating generic spacing by +10.0 percentage points** (§4.6i). The
  defensible reading is that *some* personalisation is worth a lot and *more* is worth very
  little — which argues for a simple, well-calibrated per-learner model and against a
  parameter race.
- **It does not claim mnemonic techniques as a core mechanism.** §7.2: the method-of-loci pooled
  effect falls from d = 0.88 to **PET-corrected d ≈ 0.04**, GRADE very low. §6.4: Dunlosky et al.
  (2013) rate the keyword mnemonic **LOW utility**. Mnemonics are an optional aid for genuinely
  arbitrary material only, never over written text (§7.8 rule 1).
- **It does not present felt fluency as evidence.** §6.4: font size moves judgements of learning
  by ηp² = 0.45 and recall by F < 1, and **two full study–test cycles do not reduce the illusion**.
  Learners cannot fix this from experience; the system must show them the data (§6.5).
- **It does not schedule everything.** `criticality = findable` means the system's most valuable
  act is often to decline.
- **It does not treat difficulty as the goal.** §6.3: Bjork & Bjork's own boundary —
  *"Many difficulties are undesirable during instruction and forever after."*

---

## 12. Negative and null results register

The editorial standard requires at least one documented negative or null result per section. This
section has **sixty-eight**, which is itself the most informative fact about the field. They are
grouped by what they falsify.

### 12.0 The four that matter most

If only four survive into the survey, these:

1. **Sequencing interdependent content with a learner-model-driven policy: 0 significant results
   out of 8 controlled trials.** Paired-associate/flashcard spacing, by contrast, is 11 of 14.
   (Doroudi, Aleven & Brunskill 2019, *IJAIED* 29:568–620, Table 2.) `MEASURED-META`
2. **Duolingo's trained scheduler, tested against the heuristic it replaced on ~1M students for
   six weeks, produced no significant engagement gain and a significant −7.3% drop in practice —
   and no learning outcome was measured.** The famous "+12%" is a different experiment comparing
   two variants of the new model. (Settles & Meeder 2016, Table 4.) `MEASURED-RCT`
3. **Expanding intervals confer no aggregate advantage (g = 0.032 [−0.10, 0.17], I² = 0%,
   k = 54), and the mechanism they are justified by is false in the data** — response latencies
   *fall* across repetitions in expanding schedules. The variable that does work is delaying the
   *first* retrieval, which expanding schedules do least of. (Latimier et al. 2021;
   Karpicke & Roediger 2007.) `MEASURED-META` + `MEASURED-RCT`
4. **A model with oracle access to the exact moment of learning beats a 2009 logistic regression
   by 0.002 AUC.** The next-item prediction problem is saturated. (Beck & Xiong 2013.)
   `MEASURED-BENCH`

### 12.1 Nulls about scheduling algorithms

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 1 | **A zero-parameter moving average beats every released FSRS version on log loss** (0.3369 vs FSRS-7 0.3437, FSRS-6 0.3460) across 349.9M reviews from 9,999 users | `open-spaced-repetition/srs-benchmark`, retrieved 2026-07-27 | `MEASURED-BENCH` | 4.2 |
| 2 | **A 34-feature logistic regression beats FSRS-6 and FSRS-7 on all three metrics** (log loss 0.3393, RMSE 0.0604, AUC 0.7108) — on the FSRS project's own benchmark | ibid. | `MEASURED-BENCH` | 4.2 |
| 3 | **The benchmark's own headline metric is gameable and the authors published the exploit.** `RMSE-BINS-EXPLOIT` attains the best RMSE(bins) in the table (0.01350) with a log loss of **4.608** — ~13× worse than every real model | ibid. | `MEASURED-BENCH` | 4.2 |
| 4 | **Duolingo's HLR produced no significant engagement gain and a significant −7.3% drop in practice** against the Leitner system it replaced, in a 6-week randomized trial on just under 1 million students. The famous "+12%" is a within-model feature ablation (Experiment II), not HLR vs Leitner. **No learning outcome was measured in either experiment.** | Settles & Meeder (2016), ACL, Table 4 | `MEASURED-RCT` (engagement outcome) | 4.4 |
| 5 | **HLR ranks near the bottom of the independent Anki benchmark** — RMSE(bins) 0.1275, *worse than the zero-parameter AVG baseline* (0.1034) | srs-benchmark | `MEASURED-BENCH` | 4.4 |
| 6 | **Memrise's fixed, non-adaptive 1→6→12→48→96→180-day ladder lands within ~2% of tuned FSRS** on cards-memorised-per-hour (15.6 vs 13.7–18.9) and above SM-2 (15.0) | `SSP-MMC-FSRS` 5-year simulation | `DEMO` | 4.7 |
| 7 | **There is no controlled evidence that switching scheduling algorithm (SM-2 → FSRS, Leitner → HLR) improves any learning outcome.** The strongest RCT of an algorithmic scheduler (n ≈ 50,700) compared it against *shuffle* and *easiest-first*, not against a spacing schedule — and its authors say so | Upadhyay et al. (2021), *npj Sci. Learn.* | `MEASURED-RCT` with weak baselines | 4.6 |
| 8 | **Above ~0.90 desired retention, knowledge rises +8% while workload rises 4.9×** | `SSP-MMC-FSRS` simulation; Anki manual concurs | `DEMO` / `OBSERVED` | 4.9 |
| 8a | **Sequencing interdependent content: 0 significant results in 8 controlled trials** (6 null, 2 mixed), three explicitly BKT-driven. Only 3 of 15 classroom studies of model-induced policies beat their baseline; **17 of 24 "successes" compared against a *random* baseline** | Doroudi, Aleven & Brunskill (2019), *IJAIED* 29:568–620, Table 2 | `MEASURED-META` | 4.7 |
| 8b | **A data-fitted Atkinson-model policy was *beaten* by ARTS, a response-time heuristic not fit to data.** *"in some cases, a good psychological theory might be more useful… than a data-driven model"* | Mettler et al. (2011), via Doroudi 2019 | `MEASURED-RCT` | 4.7 |
| 8c | **Adaptive scheduling did not beat a fixed 20-day linear review on learning** — end-of-course test **p = 0.37** (n = 62); only item count differed (p = 0.001) | Kerfoot (2010), *J. Urol.* 183(2):678–681, PMID 20022032 | `MEASURED-RCT` | 4.6v |
| 8d | **Adaptive and fixed-expanding equalize once retirement criteria are matched** — efficiency F(1,61) = 0.583, p = .448; delayed accuracy d = 0.012, p = .96 | Mettler, Massey & Kellman, CogSci 2020, PMC8324178, Exp. 3 | `MEASURED-RCT` | 4.6iv |
| 8e | **A *random* schedule produced significantly higher raw accuracy than ARTS** (.93 vs .85 immediate, d = 0.746; .76 vs .52 delayed). ARTS won only on per-trial efficiency, by retiring items sooner | Mettler et al., CogSci 2020, PMC8324179, Exp. 1 | `MEASURED-RCT` | 4.6iv |
| 8f | **Fixed schedules beat adaptive on accuracy change scores** — immediate d = 1.33, delayed d = 0.768, both favouring fixed | Mettler et al., PMC8324178, Exp. 2 | `MEASURED-RCT` | 4.6iv |
| 8g | **Retuning knowledge-tracing priors for efficiency left learning unchanged**: posttest **p = 0.772**, 2-week retention **p = 0.602**; 12% of tutor time saved | Cen, Koedinger & Junker (2007), AIED, n = 110 | `MEASURED-RCT` | 4.6vi |
| 8h | **Across ~33 million randomized topic sequences, the high mastery threshold bought < 0.02 absolute retention on a 0.60 base, for +29% time** | Matayoshi et al. (2025), *JEDM* 17(1):308–336 | `MEASURED-RCT` | 4.6vii |
| 8i | **Across 50 RCTs and 30,408 students, mastery requirements had no significant effect on learning for completers** — the measurable effect ran through **dropout** | Prihar et al. (2022), EDM, ERIC ED624051 | `MEASURED-META` | 4.6vii |
| 8j | **Adaptive *item selection* had no large effect on learning**; the learner model's contribution was **distractor calibration** | Papoušek, Stanislav & Pelánek (2016), LAK '16, ~1.3M answers | `MEASURED-RCT` | 4.6viii |
| 8k | **The srs-benchmark's own README:** *"Retrospective only — no randomized user trials or measurement of actual learning outcomes."* | `open-spaced-repetition/srs-benchmark` | `MEASURED-BENCH` | 4.8 |
| 8l | **On the *immediate* weekly quizzes in the field's strongest scheduler RCT, massed practice won** (89.4% vs 87.2% / 88.1%, F(2,310) = 11.8, p < .001) — the opposite ranking from the delayed exams | Lindsey et al. (2014) | `MEASURED-RCT` | 4.6i |
| 8m | **Spaced education did not transfer to the independent high-stakes exam.** Kerfoot's 2007 urology trial (n = 537 → 400) showed clear gains on its own items but **no transfer to the In-Service Examination**; the 2008 clerkship trial was null (p = 0.25, p = 0.28); the 2009 long-term trial was split (P = .04 / **P = .60**); the 2014 blood-pressure trial's **prespecified primary outcome was null** (median 129 vs 134 days, p = 0.46) | Kerfoot, PMIDs 17382760, 18423715, 18614145, 24847084 | `MEASURED-RCT` | 5.1 |

### 12.2 Nulls about expanding intervals — the core design folklore

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 9 | **"Expanding the interval between repeated tests had little effect on long-term retention in 3 experiments."** Expanding beat equal spacing at 10 minutes and *lost* at 2 days, with and without feedback. The operative variable is the delay to the **first** retrieval, not expansion | Karpicke & Roediger (2007), *JEP:LMC* 33(4):704–719 | `MEASURED-RCT` | 3.2 |
| 10 | **With average spacing matched (1-2-3 vs 2-2-2; 1-3-5 vs 3-3-3; 1-3-8 vs 4-4-4), the expanded advantage was lost at 24 h in both age groups and expanded items were at a *significant disadvantage* for younger adults** | Logan & Balota (2008), *Aging Neuropsychol. Cogn.* | `MEASURED-RCT` | 3.3 |
| 11 | **VERIFIED: expanding vs. uniform g = 0.032 [−0.10, 0.17], p = 0.62, k = 54 (16 studies), I² = 0%, Egger p = 0.66 (no publication-bias asymmetry).** Published abstract gives 0.034. 55% of effects positive, 43% negative — centred on zero, not suppressed | Latimier, Peyre & Ramus (2021), *EPR* 33:959–987; verified via ERIC EJ1310148 and the author's thesis (HAL `tel-02461323`, via the Wayback Machine) | `MEASURED-META` | 3.1 |
| 11a | **Expanding schedules do not increase retrieval difficulty** — response latencies *fall* across repetitions in both expanding (3428→3233→2966 ms) and equal (3579→2988→2716 ms) conditions. The stated mechanism is false in the data | Karpicke & Roediger (2007), Exp. 1 | `MEASURED-RCT` | 3.2 |
| 11b | **Counterexample, reported for honesty:** Dobson (2012), n = 250, 29-day retention — expanding **42.57 ± 1.80** vs uniform **34.10 ± 1.36**, F = 14.09, P = 0.00. Day-scale intervals, 5 exposures — the moderator region where Latimier's estimate rises to g = 0.20 (CI still includes zero) | Dobson (2012), *Adv. Physiol. Educ.* 36(1), PMID 22383406 | `MEASURED-RCT` | 3.4 |

### 12.3 Nulls about retrieval practice and its boundaries

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 12 | **No testing effect at all** in two Prolific experiments with delayed post-tests, corrective feedback, attention checks and fair pay — attributed to insufficient sustained engagement | PMC12894256 (2026), via B1 | `MEASURED-RCT` | 5 |
| 13 | **No testing effect at 48 hours when retrieval was limited to two attempts**, and keyword+retrieval was no better than keyword alone; replicated in a 2024 study where retrieval practice alone did not exceed restudy under the same 2-attempt constraint | Miyatsu & McDaniel (2019), *Mem. Cogn.* 47(7):1328–1343; *Heliyon* 10(3):e24586 | `MEASURED` | 7.5 |
| 14 | **Anki use tracks USMLE Step 1 but not Step 2 CK**; "some studies found significant benefits with structured Anki programs, while others reported **no measurable difference despite positive student perceptions**" | Frappa et al. (2026), *Med. Sci. Educ.* | `OBSERVED` | 5.1 |
| 15 | **The founding "restudy does nothing" claim does not survive a design correction.** Controlling within-subjects for the spacing inherent to Karpicke & Roediger's between-subjects design, **both** repeated testing *and* repeated restudy improved learning | Soderstrom, Kerr & Bjork (2016), *Psych. Sci.* 27(2):223–230 | `MEASURED-RCT` | 5 |
| 16 | **The generation effect is null for nonwords (d = 0.05 [0.03, 0.07]), reverses for anagrams (d = −0.05 [−0.07, −0.03]), and nearly vanishes past 50 items (d = 0.09)** | Bertsch et al. (2007), *Mem. Cogn.* 35(2):201–210, 445 effect sizes | `MEASURED-META` | 5.2 |
| 17 | **A system's own "learned" label overstates competence.** Units the SRS classified as reaching long-term memory scored **50.1%** on the posttest vs **60.7%** for words the students already knew, p < 0.001 | Chukharev-Hudilainen & Klepikova (2016), *CALICO J.* 33(3) | `MEASURED-RCT` | 4.6iii |
| 17a | **Instructor-made spaced-repetition flashcards: no exam gain (p = 0.2657), confidence gain only (p = 0.0066)** — every subjective measure moved and the objective one did not | *Cureus* (2024), `doi:10.7759/cureus.70994`, PMID 39507168 | `MEASURED-RCT` | 5.1 |
| 17b | **No overall Anki benefit in a graduate-entry cohort** where 80% used it — positive only in two post-hoc subgroups | *Med. Sci. Educ.* (2025), `doi:10.1007/s40670-025-02504-7` | `OBSERVED` | 5.1 |
| 17c | **The one Anki study with objective logs found total study hours predicted the outcome as strongly as spaced-repetition metrics** (P = 0.013 vs P = 0.002), and cannot separate the two; another found the *self-reported* grouping predicted exams while the *objective* usage metrics did not | *J. Med. Educ. Curric. Dev.* (2025) `doi:10.1177/23821205251369705`; *Med. Sci. Educ.* (2023) `doi:10.1007/s40670-023-01826-8` | `OBSERVED` | 5.1 |
| 17d | **No RCT of Anki/SRS in nursing or pharmacy was located**; a Europe PMC search for `"spaced repetition" AND ("A/B test" OR "online controlled experiment")` returns **zero hits** | this session's searches | **not located** | 5.1 |
| 17e | **The pooled med-ed estimate is unstable across reviews:** SMD **0.78** [0.56, 0.99] (Clin. Teach. 2026, methods unverifiable) vs SMD **0.32** [0.13, 0.51] (JMIR 2024, Cochrane methods, 83% of studies at unclear/high risk of bias) over substantially overlapping material | `doi:10.1111/tct.70353`; `doi:10.2196/57760` | `MEASURED-META` | 5.1 |

### 12.4 Nulls about mnemonics, memory palaces, and difficulty

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 18 | **The method-of-loci pooled effect collapses under publication-bias correction: d = 0.88 [0.47, 1.25] unadjusted → PET-corrected d = 0.04 [0.00, 0.00]** across 3,006 adults; publication-bias BF = 2.97 × 10⁶; **89.2% of young-adult experiments at high risk of bias; GRADE "very low" on every question** | 2025 MoL systematic review + meta-analysis, *Br. J. Psychol.* 116(4):930–986, PMC12514325 | `MEASURED-META` | 7.2 |
| 19 | **The method of loci actively harms learning from written text.** Moè & De Beni (2005): oral presentation **d = +0.93 [0.70, 1.16]**; written descriptive **d = −1.13 [−2.07, −0.18]**; written expository **d = −1.94 [−3.00, −0.87]** | ibid., extraction table | `MEASURED-META` | 7.2 |
| 20 | **The memory-palace arm did not reach significance** (OR 2.03, 95% CI 0.81–5.06) where the comparison narrative technique did (OR 2.82, 1.15–6.09); sequence-accuracy W 0.31 vs 0.65; 6-week follow-up collapsed to n = 8 | Reser et al. (2021), *PLoS ONE* 16(5):e0251710 | `MEASURED-RCT` | 7.4 |
| 21 | **Intention-to-treat group effect for a memory-palace intervention was ηp² = 0.002, p > 0.1**; effects appeared only in the compliant subsample, where virtual-MoL vs control remained **d = 0.33 [−0.07, 0.73], n.s.** | Legge et al. (2012), *Acta Psychol.* 141(3):380–390 (via the 2025 meta's extraction) | `MEASURED` (second-hand) | 7.4 |
| 22 | **Adherence null:** ~25% of older adults chose MoL over simpler strategies (Gross et al. 2014); at 3-year follow-up *"only one individual continued to use it consistently"* (Anschutz et al. 1987) | via the 2025 MoL meta | `OBSERVED` | 7.4 |
| 23 | **The keyword method reverses at delay.** *"after 2 days, there was a marked reversal"* in favour of semantic-context learning; *"the reverse is true after a delay"*; **rote beat keyword in all four classroom experiments, even at immediate test** | Wang & Thomas (1995); Thomas & Wang (1996); Campos et al. (2003) | `MEASURED` | 7.5 |
| 24 | **Learners abandon the mnemonic and do better for it** — keywords dropped for **21.6%** of words after ~8.27 retrievals, and shifting to unmediated retrieval *predicted higher recall* at 6–8 days | Dikmans et al. (2020), *Memory* 28(7):908–917 | `MEASURED` | 7.5 |
| 25 | **Working-memory / n-back training does not transfer.** Fluid intelligence vs *active* controls **g = 0.05 [−0.02, 0.13]**, k = 67; the adequately-powered subset gives **g = 0.01**; criterion (trained) measure g = 0.80. Authors: *"there is no evidential value from the studies of working memory training using treated controls."* Corroborated in Dresler's own trial, where the dual-n-back active control produced no memory gain (p > 0.9) | Melby-Lervåg, Redick & Hulme (2016), *PPS* 11(4):512–534 | `MEASURED-META` | 7.7 |
| 26 | **Generalization is the smallest effect category** in the special-education mnemonics meta: 0.68 vs 1.02 for treatment; and the largest effects come from researcher-delivered, pull-out settings | Scruggs et al. (2010), 70 studies (via ERIC ED572694) | `MEASURED-META` | 7.6 |
| 27 | **Difficulty is not sufficient.** Six L2-vocabulary experiments: difficult conditions cost during learning and *"made no difference or provided an advantage"* at delay; also **negative transfer** from previously studied semantic categories | Healy, Schneider & Kole (2025), *J. Intell.* 13(5):58 | `MEASURED` | 6.3 |
| 28 | **Spacing can reverse.** In a Remote-Associates-style task, *"spacing made it nearly impossible to solve the problems"*: massed .34 vs spaced .22, **d = 0.65 in favour of massing** | Kornell & Bjork (2008), reported by the authors | `MEASURED` | 6.2 |
| 29 | **A fluency illusion survives direct disconfirmation.** Font size moved judgements of learning (ηp² = .45, .50) and not recall (F < 1); **two full study–test cycles did not diminish the illusion** | Rhodes & Castel (2008), *JEP:Gen.* 137(4):615–625 | `MEASURED` | 6.4 |
| 30 | **Highlighting and rereading — the two most-used techniques — are rated LOW utility**; the keyword mnemonic is also LOW | Dunlosky et al. (2013), *PSPI* 14(1):4–58 | `MEASURED-META` | 6.4 |

### 12.5 Nulls about knowledge tracing and predictive modelling

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 30a | **DKT's founding 0.86 AUC was substantially a data defect.** 123,778 of 525,535 ASSISTments rows (**23.6%**) were duplicates; scaffolding rows BKT/PFA never saw were included; multi-skill rows were repeated per skill. On the repeats DKT scored **AUC 0.97**; on leading records **0.77**. Corrected: **0.86 → 0.75, and PFA ties it (0.73)** | Xiong, Zhao, Van Inwegen & Beck (2016), EDM | `MEASURED-BENCH` | 8.1 |
| 30b | **The baseline was computed differently from the model.** *"31.6% of difference… appears to be due to the use of a biased procedure for computing the AUC for BKT. Another 50.6%… vanishes if BKT is augmented to allow for forgetting"* — ~82% of the headline | Khajah, Lindsey & Mozer (2016), EDM Best Paper | `MEASURED-BENCH` | 8.1 |
| 30c | **DKT last on every dataset** against IRT and its Bayesian/temporal extensions — and *"we were able to reproduce the performance reported in [Piech et al.] when applying our RNN implementation on the raw data set (with duplicates left in)"* | Wilson, Karklin, Han & Ekanadham (2016), EDM | `MEASURED-BENCH` | 8.1 |
| 30d | **An *untrained* recurrent network with only the final linear layer fitted is within 0.02–0.03 AUC of full DKT on every dataset.** *"the underlying recurrent representation may not be reliable nor semantically meaningful"* | Ding & Larson (2019), EDM, ERIC ED599227 | `MEASURED-BENCH` | 8.1 |
| 30e | **Label leakage inflates published DLKT results by +8.38% AUC (AS2009) and +13.09% (AL2005)** on average; AKT, SAKT and DKVMN implementations named; ATKT used future ground truth. *"The majority of recently proposed DLKT approaches cannot beat the vanilla DKT model."* AKT's AS2015 claim of +0.052 becomes **+0.0014** | Liu et al. (2022), pyKT, NeurIPS D&B, arXiv:2206.11460 | `MEASURED-BENCH` | 8.2 |
| 30f | **SAKT did not replicate** — 0.85 reported vs **0.73** observed; the paper's own feedforward-baseline ablation *"we could not reproduce and seems impossible"* | Gervet et al. (2020), *JEDM* 12(3) | `MEASURED-BENCH` | 8.2 |
| 30g | **DAS3H's headline mechanism did not replicate** — time-window features *"do not add any predictive power"*; the gain over PFA was an IRT difficulty parameter | Gervet et al. (2020) | `MEASURED-BENCH` | 8.2 |
| 30h | **DKT is not domain-model-free** — *"relies on the KC model to perform optimally"*; and expert KC models add **≤ +0.01 AUC on 7 of 9 datasets**, with a KC-only model failing to beat an item-difficulty-only model on 4 of 9 | Gervet et al. (2020) | `MEASURED-BENCH` | 8.2 |
| 30i | **A model with oracle access to the exact moment of learning beats PFA by 0.002 AUC** (0.747 vs 0.745). Five modelling families intercorrelate at **0.96**. *"the research thread of predicting next item correctness… has probably progressed beyond a useful point"* | Beck & Xiong (2013), EDM, 4–11 | `MEASURED-BENCH` | 8.3 |
| 30j | **Models within 0.015 RMSE produce stop-policies correlated at r = −0.06**, with immediate-stop rates of 6% / 26% / **59%**. *"student models should not be judged by predictive error rates alone"* | Rollinson & Brunskill (2015), EDM, 179–186 | `MEASURED-BENCH` | 8.3 |
| 30k | **AUC and RMSE select the same best model 7 times in 20; AUC and log-likelihood 5 times in 20.** Truncation depth, per-student vs global averaging, and per-KC vs global AUC each **flip the ranking**. BKT parameters differ more by data-collection depth than by anything about learning | Pelánek (2015), *JEDM* 7(2):1–19; Pelánek (2018), *UMUAI* 28:207–235 | `MEASURED-BENCH` | 8.3 |
| 30l | **BKT's founding paper documents its own failure mode:** after remediation to mastery, *"the model was completely insensitive to individual differences among students… There was no variability in the knowledge estimates,"* while raw tutor error rate still predicted posttest at **r = −0.64** | Corbett & Anderson (1995), *UMUAI* 4(4), Table I | `MEASURED-BENCH` | 8.5 |
| 30m | **DKT's predicted knowledge state oscillates and fails to reconstruct its own observed input** (AUC(C) 0.904 vs AUC(N) 0.821) — invisible to next-item AUC | Yeung & Yeung (2018), L@S, arXiv:1806.02180 | `MEASURED-BENCH` | 8.2 |
| 30n | **Two classroom RCTs of deep-RL pedagogical policies were null on the main effect** — *"no significant difference between the DQN-Del and Random… and between the DQN-Inf and Random… on every measure of learning performance."* Authors' explanation: *"our random baseline policy is decently strong"* | Sanz Ausin, Azizsoltani, Barnes & Chi (2019), EDM, ERIC ED599215 | `MEASURED-RCT` | 4.7 |
| 30o | **The Khan Academy row of DKT's original table can never be checked** — the dataset was never released, and Khajah et al. report being refused access even with a DKT co-author's help. arXiv:1506.05908 still carries only v1 and no erratum | Khajah et al. (2016) | **unverifiable** | 8.1 |

### 12.6 Nulls about the AI-native claims

| # | Finding | Source | Label | § |
|---|---|---|---|---|
| 31 | **LLM-as-judge correlation with human raters collapses outside English** — coherence Pearson r = 0.507 (English), 0.426 (Chinese), **−0.149 (Polish)** | SRS-Stories, arXiv:2512.18362 | `MEASURED-BENCH` | 9.1 |
| 32 | **Every LLM-native remembering capability located in this session sits at `DEMO` or confounded-`OBSERVED`.** LECTOR's "2.0% relative improvement" is over **100 simulated learners**; SRS-Stories has no learner and no retention test; Irec has no evaluation; the one classroom study of LLM-generated retrieval practice is quasi-experimental with different course content across arms | §9.6 | — | 9 |
| 33 | **No meta-analysis or controlled trial comparing varied-cue vs identical-cue repeated retrieval for the same verbal content was located.** The nearest evidence — Pan & Rickard's finding that transfer is weakest to *rearranged stimulus–response items* — complicates rather than supports naive cue regeneration | this session's searches; Pan & Rickard (2018) | **not located** | 9.1 |

### 12.7 Things this session could not verify, listed so they are never laundered

- **Cepeda et al. (2006) and (2008) full texts** — paywalled; `laplab.ucsd.edu` returned 403; two open mirrors 404. **Abstracts verified directly via PubMed E-utilities.** The "271 comparisons / 12 exceptions" and "~9 percentage points" figures are carried from B1 and not re-verified.
- **Latimier, Peyre & Ramus (2021)** — the *published article* is closed-access and HAL record `hal-02976100` has no deposited file. **But the finding was verified** via the ERIC-indexed published abstract (EJ1310148) and the author's thesis (`tel-02461323`) retrieved through the Wayback Machine. See §3.1 for the full statistics. **Resolved — no longer an open item.**
- **Kerfoot (2010), *J. Urol.* 183(2):678–681** — the only published head-to-head of two spacing algorithms in medical education. ScienceDirect, AUA Journals and LWW all returned 403; not in PMC; not OA; no Wayback copy. **Per-arm n, attrition, means, SDs, item counts, the efficiency formula, the retention interval, funding and registration are all unverified.** Only the abstract's p = 0.37 / p = 0.001 / "+38% efficiency" are reported here.
- **Nine further Kerfoot trials** (PMIDs 17382760, 17209889, 18423715, 18614145, 19375095, 19387336, 20800189, 21671276, 22664558) — abstract only; per-arm n and attrition often absent even from abstracts.
- **The Clinical Teacher (2026) meta-analysis** — paywalled. **The study-level design breakdown (how many of the 13 were randomized), I², and publication-bias assessment are unverified.** The SMD 0.78 must not be quoted as a randomized effect.
- **Lindsey et al. (2014) condition means** — present only inside Figure 2a. The relative-versus-percentage-point reading in §4.6i is `INFERENCE` from the published axis range, not a statement in the paper.
- **SSP-MMC (KDD 2022, `doi:10.1145/3534678.3539081`)** — ACM DL returned 403 and `maimemo.com/paper` was unreachable. **Whether MaiMemo ever ran a live A/B with a learning outcome can be neither confirmed nor denied.**
- **Doroudi & Brunskill, "Fairer but Not Fair Enough: On the Equitability of Knowledge Tracing," LAK '19**, `doi:10.1145/3303772.3303838` — ACM DL and author-site URLs both failed. Fairness findings **unverified**.
- **Mettler, Massey & Kellman (2016), *JEP: General* 145(7):897–917** — the *JEP:General* paper was reached via PMC6028005; the earlier **Pavlik & Anderson (2008), *JEP: Applied* 14(2):101–117** was not, and its reported **d = 0.796** is second-hand from Doroudi et al. (2019) Table 8.
- **Numbers existing only inside figures** (Lindsey Fig. 4; Matayoshi Fig. 4; Gervet Figs. 5–7; Prihar Figs. 2–7) are **not** reported here as values.
- **Murayama et al. (2014) retrieval-induced-forgetting pooled effect size** — the abstract does not state it and the full text is paywalled. **No number is supplied.**
- **Pressley, Levin & Delaney (1982)**, the canonical keyword-method review — non-OA; **no pooled keyword-method effect size exists in this report.**
- **The widely-cited "mnemonic instruction ES ≈ 1.62"** — traces to Mastropieri & Scruggs (1989) and/or Forness et al. (1997), both paywalled and unopenable. **Not reproduced.** The verified, larger-corpus figure is 1.47 (Scruggs et al. 2010).
- **Bjork & Bjork (1992) and Bjork (1994)** — available online only as image-only scans with no text layer and no OCR available. **Theory quoted from the same authors' 2020 restatement instead.**
- **Dunlosky et al. (2013) monograph body** — HTTP 403 at the publisher. Ratings and criteria quoted verbatim from the primary abstract; **no numeric effect size is attributed to this source.**
- **Dresler et al. (2017) Supplemental Table S2** (per-arm mean word counts) — download blocked. Only F and η² are reported.
- **Lindsey et al. (2014) full text** — two author-page mirrors returned 301/connection failure. **Abstract verified directly via PubMed**; the +16.5%/+10.0% figures are the authors' own wording.
- **Cull (2000)**, *Applied Cognitive Psychology* — no matching PubMed record returned; unreachable.
- **Landauer & Bjork (1978)** — book chapter, not indexed, unreachable. Its result is characterised only via the two papers that replicate and bound it.

---

## 13. Bibliography

Grouped by section. Every entry was reached this session unless marked **[unreachable]** or
**[carried]** (taken from another report in this project, with that report named).

**The named product**
1. zemomemo.com — landing page, retrieved 2026-07-27. `VENDOR`
2. `open-spaced-repetition/srs-benchmark` — README retrieved 2026-07-27 via `gh api`. `MEASURED-BENCH`
3. `open-spaced-repetition/awesome-fsrs` wiki, "ABC of FSRS" (redirect target of the link zemomemo cites).
4. Anki manual, Deck Options / FSRS section, `docs.ankiweb.net/deck-options.html`.

**Spacing**
5. Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks. *Psychological Bulletin*, 132(3), 354–380. doi:10.1037/0033-2909.132.3.354 · PMID 16719566. [abstract verified; full text unreachable]
6. Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing effects in learning: A temporal ridgeline of optimal retention. *Psychological Science*, 19(11), 1095–1102. doi:10.1111/j.1467-9280.2008.02209.x · PMID 19076480. [abstract verified; full text unreachable]
7. Donovan, J. J., & Radosevich, D. J. (1999). *Journal of Applied Psychology*, 84(5), 795. doi:10.1037/0021-9010.84.5.795. [carried from B1]
8. Latimier, A., Peyre, H., & Ramus, F. (2021). *Educational Psychology Review*, 33, 959–987. doi:10.1007/s10648-020-09572-8. **[unreachable]**
9. Classroom spacing meta-analysis (2025), PMC12189222. [carried from B1]

**Expanding vs. uniform intervals**
10. Karpicke, J. D., & Roediger, H. L. (2007). Expanding retrieval practice promotes short-term retention, but equally spaced retrieval enhances long-term retention. *JEP: LMC*, 33(4), 704–719. PMID 17576148. [abstract verified verbatim]
11. Logan, J. M., & Balota, D. A. (2008). Expanded vs. equal interval spaced retrieval practice. *Aging, Neuropsychology, and Cognition*. PMID 18421627. [abstract verified verbatim]
12. Landauer, T. K., & Bjork, R. A. (1978). Optimum rehearsal patterns and name learning. In Gruneberg, Morris & Sykes (eds.), *Practical Aspects of Memory*. **[unreachable]**

**Scheduling algorithms**
13. Settles, B., & Meeder, B. (2016). A trainable spaced repetition model for language learning. *Proc. ACL 2016*, 1848–1858. doi:10.18653/v1/P16-1174. [full PDF read]
14. Tabibian, B., Upadhyay, U., De, A., Zarezade, A., Schölkopf, B., & Gomez-Rodriguez, M. (2019). Enhancing human learning via spaced repetition optimization. *PNAS*, 116(10), 3988–3993. doi:10.1073/pnas.1815156116 · PMC6410796. [full text read]
15. Upadhyay, U., Lancashire, G., Moser, C., & Gomez-Rodriguez, M. (2021). Large-scale randomized experiments reveal that machine learning-based instruction helps people memorize more effectively. *npj Science of Learning*, 6, 26. doi:10.1038/s41539-021-00105-8 · PMC8421401. [full text read]
16. Lindsey, R. V., Shroyer, J. D., Pashler, H., & Mozer, M. C. (2014). Improving students' long-term knowledge retention through personalized review. *Psychological Science*, 25(3), 639–647. doi:10.1177/0956797613504302 · PMID 24444515. [abstract verified; full text unreachable]
17. Chukharev-Hudilainen, E., & Klepikova, T. A. (2016). The effectiveness of computer-based spaced repetition in foreign language vocabulary instruction: a double-blind study. *CALICO Journal*, 33(3). doi:10.1558/cj.v33i3.26055 · ERIC EJ1143520. [full text read]
18. Ye, J., Su, J., & Cao, Y. (2022). A stochastic shortest path algorithm for optimizing spaced repetition scheduling. *KDD '22*. doi:10.1145/3534678.3539081.
19. Su, J., Ye, J., Nie, L., Cao, Y., & Chen, Y. (2023). Optimizing spaced repetition schedule by capturing the dynamics of memory. *IEEE TKDE*. doi:10.1109/TKDE.2023.3251721.
20. Reddy, S., Labutov, I., Banerjee, S., & Joachims, T. (2016). Unbounded human learning: optimal scheduling for spaced repetition. arXiv:1602.07032.
21. Woźniak, P. A., Gorzelańczyk, E. J., & Murakowski, J. (1995). Two components of long-term memory. *Acta Neurobiol. Exp.*, 55(4), 301–305. [carried from F5]
21a. Doroudi, S., Aleven, V., & Brunskill, E. (2019). Where's the reward? A review of reinforcement learning for instructional sequencing. *IJAIED*, 29, 568–620. doi:10.1007/s40593-019-00187-x. [full text read — Table 2 is the field-level tally]
21b. Mettler, E., Massey, C. M., & Kellman, P. J. (2016). A comparison of adaptive and fixed schedules of practice. *JEP: General*, 145(7), 897–917. doi:10.1037/xge0000170 · PMC6028005.
21c. Mettler, E., Massey, C. M., & Kellman, P. J. (2020). Adaptive scheduling in community-college chemistry. *CogSci 2020* · PMC8324178; and ARTS vs. random schedules, PMC8324179.
21d. Kerfoot, B. P. (2010). Adaptive spaced education improves learning efficiency: a randomized controlled trial. *J. Urology*, 183(2), 678–681. PMID 20022032. **[full text unreachable]**
21e. Cen, H., Koedinger, K. R., & Junker, B. (2007). Is over practice necessary? Improving learning efficiency with the Cognitive Tutor. *AIED 2007*, *Frontiers in AI and Applications* 158, 511–518. [full text read]
21f. Matayoshi, J., Cosyn, E., Uzun, H., & Kurd-Misto, K. (2025). *JEDM*, 17(1), 308–336. [full text read]
21g. Prihar, E., et al. (2022). Exploring common trends in online educational experiments. *EDM 2022* · ERIC ED624051.
21h. Papoušek, J., Stanislav, V., & Pelánek, R. (2016). Impact of question difficulty on engagement and learning. *LAK '16*. [full text read]
21i. Dobson, J. L. (2012). Effect of uniform versus expanding retrieval practice on the recall of physiology information. *Advances in Physiology Education*, 36(1). doi:10.1152/advan.00090.2011 · PMID 22383406.
21j. Sanz Ausin, M., Azizsoltani, H., Barnes, T., & Chi, M. (2019). Leveraging deep reinforcement learning for pedagogical policy induction. *EDM 2019*, 168–177 · ERIC ED599215.
21k. Martinengo, L., et al. (2024). Spaced vs. massed online education: systematic review and meta-analysis. *JMIR*. doi:10.2196/57760 · PMC11502984.
21l. Phillips, J. L., et al. (2019). Effectiveness of spaced education in clinician CPD. *Medical Education*. doi:10.1111/medu.13895 · PMID 31144348.
21m. Pane, J. F., Griffin, B. A., McCaffrey, D. F., & Karam, R. (2014). Effectiveness of Cognitive Tutor Algebra I at scale. *EEPA*, 36(2), 127–144. doi:10.3102/0162373713507480. [context only — the manipulation is whole-curriculum adoption, not knowledge tracing]

**Retrieval practice**
22. Rowland, C. A. (2014). *Psychological Bulletin*, 140(6), 1432–1463. doi:10.1037/a0037559. [carried from B1]
23. Adesope, O. O., Trevisan, D. A., & Sundararajan, N. (2017). *Review of Educational Research*, 87(3), 659–701. doi:10.3102/0034654316689306. [carried from B1]
24. Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). *Psychological Bulletin*. doi:10.1037/bul0000309. [carried from B1]
25. Pan, S. C., & Rickard, T. C. (2018). *Psychological Bulletin*. doi:10.1037/bul0000151. [carried from B1]
26. Soderstrom, N. C., Kerr, T. K., & Bjork, R. A. (2016). *Psychological Science*, 27(2), 223–230. doi:10.1177/0956797615617778. [carried from B1]
27. Bertsch, S., Pesta, B. J., Wiscott, R., & McDaniel, M. A. (2007). The generation effect: A meta-analytic review. *Memory & Cognition*, 35(2), 201–210. doi:10.3758/BF03193441. [full PDF read]
28. The effectiveness of spaced repetition in medical education: a systematic review and meta-analysis (2026). *The Clinical Teacher*. doi:10.1111/tct.70353. [abstract verified]
29. Using spaced repetition to teach histopathology significantly improves diagnostic skills: a randomized within-participant evaluation (2026). *Anatomical Sciences Education*. doi:10.1002/ase.70261. [abstract verified]
30. Frappa, et al. (2026). Anki use and academic performance in medical education: a systematic review. *Medical Science Educator*. doi:10.1007/s40670-026-02643-5 · PMC13197492. [abstract verified]

**Desirable difficulties and metacognition**
31. Bjork, R. A., & Bjork, E. L. (2020). Desirable difficulties in theory and practice. *JARMAC*, 9(4), 475–479. doi:10.1016/j.jarmac.2020.09.003. [full text read — source of all verbatim theory quotes]
32. Bjork, R. A., & Bjork, E. L. (1992). A new theory of disuse and an old theory of stimulus fluctuation. In *From Learning Processes to Cognitive Processes*, Vol. 2, 35–67. **[image-only scan, no text layer]**
33. Bjork, R. A. (1994). Memory and metamemory considerations in the training of human beings. In *Metacognition: Knowing About Knowing*, 185–205. **[image-only scan]**
34. Schmidt, R. A., & Bjork, R. A. (1992). New conceptualizations of practice. *Psychological Science*, 3(4), 207–217. [full text read]
35. Kornell, N., & Bjork, R. A. (2008). Learning concepts and categories: Is spacing the "enemy of induction"? *Psychological Science*, 19(6), 585–592. doi:10.1111/j.1467-9280.2008.02127.x. [full text read]
36. Bjork, R. A., Dunlosky, J., & Kornell, N. (2013). Self-regulated learning: beliefs, techniques, and illusions. *Annual Review of Psychology*, 64, 417–444. doi:10.1146/annurev-psych-113011-143823. [full text read]
37. Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *PNAS*, 116(39), 19251–19257. doi:10.1073/pnas.1821936116 · PMC6765278. [full text read]
38. Rhodes, M. G., & Castel, A. D. (2008). Memory predictions are influenced by perceptual information. *JEP: General*, 137(4), 615–625. doi:10.1037/a0013684. [full text read]
39. Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013). *Psychological Science in the Public Interest*, 14(1), 4–58. doi:10.1177/1529100612453266 · PMID 26173288. **[body 403; abstract verified verbatim]**
40. Healy, A. F., Schneider, V. I., & Kole, J. A. (2025). *Journal of Intelligence*, 13(5), 58. PMID 40426468 · PMC12108878. [full text read]
41. Does difficulty moderate learning? (2025). PMID 39641213 · PMC12432286. [full text read]
42. Students don't learn the way they think they do in a large, active-learning genetics course (2025). *CBE—Life Sciences Education*. PMID 40373176 · PMC12286633.

**Mnemonics**
43. Dresler, M., Shirer, W. R., Konrad, B. N., et al. (2017). Mnemonic training reshapes brain networks to support superior memory. *Neuron*, 93(5), 1227–1235.e6. doi:10.1016/j.neuron.2017.02.003 · PMC5439266. [full text read; **Table S2 unreachable**]
44. The method of loci in the context of psychological research: a systematic review and meta-analysis (2025). *British Journal of Psychology*, 116(4), 930–986. doi:10.1111/bjop.12799 · PMC12514325. [full text read]
45. Twomey, C., & Kroneisen, M. (2021). MoL meta-analysis, d = 0.65 [0.45, 0.85]. **[not independently retrieved; cited within #44]**
46. Qureshi, A., Rizvi, F., Syed, A., Shahid, A., & Manzoor, H. (2014). *Advances in Physiology Education*, 38(2), 140–144. PMID 25039085 · PMC4056179. [full text read]
47. Reser, D., Simmons, M., Johns, E., et al. (2021). *PLoS ONE*, 16(5), e0251710. doi:10.1371/journal.pone.0251710 · PMC8130951. [full text read]
48. Legge, E. L. G., Madan, C. R., Ng, E. T., & Caplan, J. B. (2012). *Acta Psychologica*, 141(3), 380–390. doi:10.1016/j.actpsy.2012.09.002. **[non-OA; values via #44's extraction table]**
49. Scruggs, T. E., Mastropieri, M. A., Berkeley, S., & Graetz, J. E. (2010). *Remedial and Special Education*, 31(6), 437–449. doi:10.1177/0741932508327465. **[non-OA; figures via ERIC ED572694]**
50. Mastropieri, M. A., & Scruggs, T. E. (1989). *Educational Psychology Review*, 1, 83–111. doi:10.1007/BF01326638. **[unreachable — the "1.62" figure is not verified]**
51. Forness, S. R., Kavale, K. A., Blum, I. M., & Lloyd, J. W. (1997). *Teaching Exceptional Children*, 29(6), 4–9. **[unreachable]**
52. Therrien, W. J., Taylor, J. C., Hosp, J. L., Kaldenberg, E. R., & Gorsh, J. (2011). ERIC EJ947712.
53. Atkinson, R. C., & Raugh, M. R. (1975). *JEP: HLM*, 1(2), 126–133. doi:10.1037/0278-7393.1.2.126. [technical-report version ERIC ED096841 read in full]
54. Wang, A. Y., Thomas, M. H., & Ouellette, J. A. (1992). *JEP*, 84(4), 520–528. doi:10.1037/0022-0663.84.4.520.
55. Wang, A. Y., & Thomas, M. H. (1995). *JEP*, 87(3), 468–475. doi:10.1037/0022-0663.87.3.468.
56. Thomas, M. H., & Wang, A. Y. (1996). *JEP: Applied*, 2(4), 330–342. doi:10.1037/1076-898X.2.4.330.
57. Campos, A., González, M. A., & Amor, A. (2003). Limitations of the mnemonic-keyword method. *J. General Psychology*, 130(4), 399–413. PMID 14672102.
58. Carney, R. N., & Levin, J. R. (1998). *Contemporary Educational Psychology*, 23(3), 276–297. PMID 9665791.
59. Miyatsu, T., & McDaniel, M. A. (2019). *Memory & Cognition*, 47(7), 1328–1343. PMID 31077068.
60. Dikmans, M. E., van den Broek, G. S. E., & Klatter-Folmer, J. (2020). *Memory*, 28(7), 908–917. PMID 32723148.
61. Pressley, M., Levin, J. R., & Delaney, H. D. (1982). *Review of Educational Research*, 52(1), 61–91. **[unreachable]**
62. Melby-Lervåg, M., Redick, T. S., & Hulme, C. (2016). *Perspectives on Psychological Science*, 11(4), 512–534. doi:10.1177/1745691616635612 · PMC4968033. [full text read]
63. Can we enhance working memory? Bias and effectiveness in cognitive training studies (2024). *Psychonomic Bulletin & Review*. PMC11543728.

**Knowledge tracing** (full treatment in F5 §2)
64. Corbett, A. T., & Anderson, J. R. (1995). *UMUAI*. doi:10.1007/BF01099821.
65. Pavlik, P. I., Cen, H., & Koedinger, K. R. (2009). Performance factors analysis. *AIED*.
66. Piech, C., et al. (2015). Deep knowledge tracing. *NeurIPS*. arXiv:1506.05908.
67. Xiong, X., Zhao, S., Van Inwegen, E., & Beck, J. (2016). Going deeper with deep knowledge tracing. *EDM 2016*, 545–550.
68. Khajah, M., Lindsey, R. V., & Mozer, M. C. (2016). How deep is knowledge tracing? *EDM 2016*. arXiv:1604.02416.
69. Wilson, K. H., Karklin, Y., Han, B., & Ekanadham, C. (2016). Back to the basics. *EDM 2016*. arXiv:1604.02336.
70. Gervet, T., Koedinger, K., Schneider, J., & Mitchell, T. (2020). When is deep learning the best approach to knowledge tracing? *JEDM*, 12(3), 31–54.
71. Liu, Z., et al. (2022). pyKT. *NeurIPS Datasets & Benchmarks*. arXiv:2206.11460.
72. Beck, J. E., & Chang, K. (2007). Identifiability: a fundamental problem of student modeling. *UM'07*. doi:10.1007/978-3-540-73078-1_17.
72a. Ding, X., & Larson, E. C. (2019). Why deep knowledge tracing has less depth than anticipated. *EDM 2019*, 282–287 · ERIC ED599227. [full text read]
72b. Yeung, C.-K., & Yeung, D.-Y. (2018). Addressing two problems in deep knowledge tracing via prediction-consistent regularization. *L@S 2018* · arXiv:1806.02180.
72c. Beck, J. E., & Xiong, X. (2013). Limits to accuracy: how well can we do at student modeling? *EDM 2013*, 4–11 · ERIC ED558215. [full text read]
72d. Rollinson, J., & Brunskill, E. (2015). From predictive models to instructional policies. *EDM 2015*, 179–186 · ERIC ED560516. [full text read]
72e. Pelánek, R. (2015). Metrics for evaluation of student models. *JEDM*, 7(2), 1–19. [full text read]
72f. Pelánek, R. (2018). The details matter: methodological nuances in the evaluation of student models. *UMUAI*, 28, 207–235. doi:10.1007/s11257-018-9204-y.
72g. Schmucker, R., Wang, J., Hu, S., & Mitchell, T. (2022). Assessing the performance of online students. *JEDM*, 14(1), 1–45. [full text read]
72h. Pavlik, P. I., & Eglington, L. G. (2023). Automated search improves logistic knowledge tracing. *JEDM*, 15(3), 58–86. [full text read]
72i. Khajah, M. (2024). Supercharging BKT with multidimensional generalizable IRT and skill discovery. *JEDM*, 16(1), 233–277.
72j. Ghosh, A., Heffernan, N., & Lan, A. S. (2020). Context-aware attentive knowledge tracing (AKT). *KDD '20*. doi:10.1145/3394486.3403282 · arXiv:2007.12324.
72k. Gong, Y., Beck, J. E., & Heffernan, N. T. (2010). Comparing knowledge tracing and performance factor analysis. *ITS 2010*, 35–44.
72l. Fancsali, S., Nixon, T., & Ritter, S. (2013). Optimal and worst-case performance of mastery learning assessment with Bayesian knowledge tracing. *EDM 2013*, 35–42. [simulation]

**Forgetting**
73. Richards, B. A., & Frankland, P. W. (2017). The persistence and transience of memory. *Neuron*, 94(6). doi:10.1016/j.neuron.2017.04.037. [abstract verified]
74. Murayama, K., Miyatsu, T., Buchli, D., & Storm, B. C. (2014). *Psychological Bulletin*, 140(5), 1383–1409. doi:10.1037/a0037505 · PMID 25180807. **[pooled effect size not stated in abstract; full text unreachable]**

**The LLM-native frontier**
75. SRS-Stories: Vocabulary-constrained multilingual story generation for language learning (2025). arXiv:2512.18362. [full PDF read]
76. LECTOR: LLM-Enhanced Concept-based Test-Oriented Repetition for Adaptive Spaced Learning (2025). arXiv:2508.03275.
77. Irec: A metacognitive scaffolding for self-regulated learning through just-in-time insight recall (2025). arXiv:2506.20156.
78. Enhancing student learning with LLM-generated retrieval practice questions: an empirical study in data science courses (2025). arXiv:2507.05629v2. [full PDF read]
79. SmartPhone: Exploring keyword mnemonic with auto-generated verbal and visual cues (2023). arXiv:2305.10436.
80. "I Spend All My Energy Preparing": Balancing AI automation and agency for self-regulated learning in SmartFlash (2026). arXiv:2602.14431.

**Within this project**
81. `research/raw/B1-learning-science.md` — spacing, retrieval practice, interleaving, desirable difficulties (evidence floor).
82. `research/raw/F5-learner-model.md` — SM-2/FSRS algorithm forensics, `srs-benchmark` tables, knowledge-tracing critique literature.
83. `research/raw/I2-global-traditions.md` §6.1 — the Aboriginal-memory RCT and its cultural-attribution constraints.
84. `research/raw/C2-assessment-psychometrics.md` — automatic item generation and item validity.
85. `research/raw/F3-executable-verifiable.md` — the grounding ladder and symbolic verification.
86. `research/raw/F10-explanation-laddering.md` — re-representation targets for `inert_flag`.
87. `research/raw/H1-selpa-accessibility.md` — the special-education context for §7.6.

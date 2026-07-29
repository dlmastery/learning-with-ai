---
title: "The Investment Case, Audited: market size, unit economics, defensibility and the risk register for an AI-native tutoring company with humans in the loop"
wave: M
section: M1
date_researched: 2026-07-29
sources_count: 58
status: raw-research
---

# M1 — Market and model

> **What this section is for.** Thirty-three sections of this corpus establish what
> works pedagogically. None of them contains a number an investment committee would
> recognise. This section is the missing half, held to the same standard: every claim
> labelled, no vendor claim restated as a finding, and every market figure either traced
> to a primary source or reported as **untraceable**.
>
> **Retrieval note.** WebSearch was exhausted before this section began. Everything
> below came from: **SEC EDGAR** (submissions JSON, XBRL `companyfacts`, full-text
> search `efts.sec.gov`, and direct retrieval of 10-K/10-Q primary documents);
> **BLS OEWS** national and state microdata files (May 2025, downloaded and parsed
> from the published `.xlsx`); **NBER** working-paper PDFs; **arXiv** PDFs;
> **Crossref**; **USAspending.gov** API; the **Hugging Face** dataset API; and
> `WebFetch`/`curl` on known URLs. Unreachable sources are listed in §11 with status
> codes and are never guessed around.
>
> **Evidence labels.** Project standard — `MEASURED-RCT` · `MEASURED-META` ·
> `MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE` — plus three used
> here and defined now:
> - **`FILING`** — an audited or regulator-submitted document carrying legal liability
>   (10-K, 10-Q, 20-F, Form C-AR, Form D, IRS 990). Form type and filing date given.
>   **`FILING` outranks every press figure in this section.**
> - **`GOV-STAT`** — an official government statistical product with published
>   methodology (BLS OEWS, NCES, Census, Statistics Korea).
> - **`UNTRACEABLE`** — a figure in wide circulation whose primary source could not be
>   reached, or which traces only to a paywalled report with no disclosed method. The
>   figure is named as untraceable and **is not restated**.
>
> **The rule this section is most at risk of breaking.** Investor-facing research is
> where numbers become unfalsifiable. A `VENDOR` claim is never restated as a finding.
> Where a company asserts an outcome, the finding is the *structure of the assertion*,
> not the number.

---

## 0. The eight findings that should change an investor's behaviour

Ordered by how much they should move a decision.

1. **In a human-in-the-loop tutoring model, AI inference is ~0.4% of delivered cost.**
   Two independent measurements agree to the second decimal: the LearnLM/Eedi trial's
   own cost model puts tokens at **0.43%** of a supervised session's cost, and Tutor
   CoPilot's measured API spend of **$20 per tutor per year** is **0.43%** of a tutor
   working 200 hours at the US mean tutor wage. **Inference price decline is
   economically irrelevant to this business model.** A 100× fall in token prices
   improves gross margin by less than half a point. `MEASURED` — §3.2.

2. **The only measurement of the AI-drafting leverage ratio puts it at +16.4%, not
   10×.** Eedi Appendix H: tutor throughput 35.38 → 41.18 sessions/hour, cost per
   session −13.6%. Concurrency rose 2.3 → 3.5 (+52%) but session duration rose 3.9 →
   5.1 minutes (+31%), which ate two thirds of the gain. And that number comes from a
   **six-tutor role-play simulation**, not the RCT — the authors say their design
   "precludes a rigorous measurement of throughput or efficiency." `MEASURED-RCT`
   (acceptance) + `DEMO` (throughput) — §3.3.

3. **The one public company running exactly this model saw gross margin fall from
   67.5% to 58.0% in the year it went AI-native.** Nerdy Inc. (Varsity Tutors), FY2025
   10-K: revenue −5.9% to $178.99M, gross profit $103.78M, expert costs *up* $5.24M on
   *falling* revenue. Ex the $7.76M software write-off the margin is 62.3% — still
   down 5 points. Q1 2026 recovered to 66.2%. `FILING` — §3.5.

4. **District contracts are not sticky, and the company says so in its 10-K.**
   "Contracts with Institutions are generally short-term in duration (one year or
   less)." Nerdy's Institutional revenue fell **22%** in FY2025 and a **$7.44M**
   state-funded programme "did not recur." That is the ESSER cliff arriving in audited
   numbers. `FILING` — §2.3, §8.3.

5. **The proprietary-data moat is empirically weak, because the field's data-richest
   organisations gave their data away.** Eedi — the company behind the 74.4% figure —
   publishes its own tutoring dialogues on Hugging Face under CC-BY-NC-4.0. ASSISTments
   publishes a 1–10M-row interaction corpus. Riiid published EdNet. `OBSERVED` — §5.1.

6. **A single regulatory act removed 62% of a tutoring company's revenue in one year,
   and it has not recovered profitability five years later.** Gaotu Techedu, 20-F:
   revenue CNY 6,561.7M (2021) → **CNY 2,498.2M (2022)** after China's July 2021
   "double reduction" policy; back to CNY 6,146.8M by 2025 but still an operating loss
   of CNY 503.2M. Regulatory risk in this sector is not theoretical and it is not
   gradual. `FILING` — §8.1.

7. **Nothing in this market's evidence base supports a claim that designed pedagogy
   beats an undesigned chatbot.** Fütterer et al. 2026 (*Educational Psychology
   Review*, n=371, Grades 7–9): two scaffolded GenAI conditions vs **plain ChatGPT**
   as control — null on domain knowledge, effort and elaboration strategy use. If the
   product thesis is "our pedagogy is the moat," this is the result that must be
   beaten. `MEASURED-RCT` — §5.2, §8.5.

8. **The category barely exists in the public markets, which cuts both ways.** EDGAR
   full-text search returns **47 filings ever** containing "AI tutor", **24**
   containing "AI tutoring", and **47** containing "high-dosage tutoring" — of which
   the high-dosage hits come from a single issuer. There is no public comparable set
   for an AI-native tutoring company, so every valuation multiple offered to an
   investor in this category is borrowed from an adjacent business. `OBSERVED` — §4.1.

---

## 1. Market size, honestly

*(§1 is completed below after the primary-source sweep; see §1.1 for the method that
governs every figure in it.)*

### 1.1 The method, stated first because it does most of the work

Three tiers, and an investor should refuse to mix them:

| Tier | What it is | How to grade it |
|---|---|---|
| **Reported TAM** | An analyst-house estimate of "the global tutoring market." | Almost always `UNTRACEABLE`. The number exists in a press release; the method is behind a paywall; the underlying survey, if any, is not published. |
| **Measured spend** | A government statistical product measuring what households or governments actually spent. | `GOV-STAT`. Real, narrow, and usually much smaller than the TAM. |
| **Addressable revenue** | The subset of measured spend that (a) is procurable by a company of this shape, (b) within a sales cycle it can survive, and (c) at a price it can charge. | `INFERENCE`, always. Must be derived in the open. |

**The discipline this section enforces: no figure moves up a tier.** A reported TAM is
never used as if it were measured spend, and measured spend is never used as if it were
addressable.

---

## 3. Unit economics of a human-in-the-loop tutoring model

This is the section the rest of the corpus could not write, and it is where the
investment case is actually decided. The model in question: **a human tutor remains the
delivery surface; an AI drafts, prepares, summarises, and sometimes converses; the
company's claim is that the AI raises the number of learners one tutor can serve without
lowering quality.**

That claim decomposes into exactly three measurable quantities. Everything else is
narrative.

1. **W** — the fully-loaded cost of a tutor-hour.
2. **L** — the leverage ratio: learners served per tutor-hour, with and without AI.
3. **a** — the AI cost per learner-hour.

Gross margin is then `GM = 1 − (W/L + a) / P`, where `P` is price per learner-hour.
The rest of §3 measures W, L and a, and then shows which of them the margin is actually
sensitive to. The answer is not the one the pitch deck assumes.

### 3.1 W — what a tutor-hour costs, measured

**Source: BLS Occupational Employment and Wage Statistics, May 2025, SOC 25-3041
"Tutors."** `GOV-STAT`. Retrieved as the published national and state `.xlsx`
microdata files (`oesm25nat.zip`, `oesm25st.zip`) and parsed directly, because the
per-occupation HTML pages now 301 to the tables index.

| Statistic | Value |
|---|---|
| National employment, occupation code 25-3041 | **175,070** |
| Hourly **mean** | **$23.10** |
| Hourly **median** | **$20.84** |
| Hourly 10th percentile | **$14.15** |
| Hourly 25th percentile | *see file* |
| Hourly 75th percentile | **$36.53** (90th) |
| Annual mean | **$48,050** |

Geographic spread, same file, state level (`GOV-STAT`):

| State | Employment | Hourly mean |
|---|---|---|
| Wyoming | 200 | **$36.81** |
| Rhode Island | 300 | $36.52 |
| Massachusetts | 4,610 | $31.35 |
| New York | 12,730 | $27.18 |
| **California** | **45,370** | **$23.54** |
| Florida | 12,220 | $21.57 |
| **Texas** | 10,690 | **$17.20** |
| Nevada | 1,070 | **$16.34** |

**The spread that matters is 2.25×** ($16.34 Nevada → $36.81 Wyoming), and the two
largest tutor labour markets — California (45,370 tutors) and Texas (10,690) — sit
$6.34/hour apart. A company that can hire nationally and deliver online captures that
spread; a company tied to a metro does not. This is a real and under-modelled source of
gross-margin variance, and it is measurable before a single line of code is written.

**Three cautions on W, all material:**

- **These are wages, not loaded cost.** Where tutors are W-2 employees, employer
  payroll taxes and benefits add materially. Where they are independent contractors —
  which is the marketplace norm and is Nerdy's disclosed structure — the platform pays
  the rate plus payment processing, and the burden sits with the tutor.
- **The occupation is small and probably undercounted.** 175,070 is the OEWS estimate
  for people whose *primary* job is coded "Tutor." Most tutoring in the US is done by
  teachers, graduate students and gig workers whose primary occupation is something
  else. Treat 175,070 as a floor on supply, not an estimate of it.
- **Tutor wage does not fall.** This is the whole point of the section. Between the
  2013–15 Saga study period and 2021, Saga's tutor stipend rose from **$16,000 plus
  benefits** to **$20,000 plus benefits** for a nine-month academic year (Guryan et al.,
  NBER w28531, footnote 12 and §II). `MEASURED-RCT` context. Over the same window
  inference cost per unit of capability fell by orders of magnitude (F4 §1.4, Epoch AI:
  median **50×/year**, post-2024 median **200×/year**). **The two cost curves point in
  opposite directions, and in this business model the one that matters is the flat
  one.**

**A useful triangulation.** LessonOrca's own public homepage derives its labour figure
from "**$25–30/hr**" tutor cost (`VENDOR`, and stated with its inputs shown, which is
more honest than the sector norm). That assumption sits between the BLS median ($20.84)
and the 90th percentile ($36.53), i.e. it is defensible but prices a somewhat
above-average tutor. An investor should ask which percentile the model assumes and
whether the company can actually hire there.

### 3.2 a — what the AI costs, and why it is the wrong thing to optimise

Two independent measurements exist. They are the most important numbers in this section
because they are the ones no pitch deck contains.

**Measurement 1 — Tutor CoPilot (Stanford), verbatim from the paper's appendix:**

> *"The total API cost for 429 treatment tutors over the 2-month study was $1,419.66,
> resulting in an estimated annual cost of $20 per tutor."*

`MEASURED` — Wang, Ribeiro, Robinson, Loeb & Demszky (2024), arXiv:2410.03017,
Appendix "Study Costs." That is **$1.65 per tutor per month** at 2024 GPT-4-class
prices, in a live deployment of 900 tutors / 1,800 students / 4,136 sessions.

**Measurement 2 — LearnLM/Eedi, from the trial's own cost model** (arXiv:2512.23633,
Appendix H.1): ~8 conversation turns per session, 1,650 input tokens and 200 output
tokens per query, priced at Gemini 2.0 Flash rates ($0.30/M in, $2.50/M out) →
**$0.005 (£0.0037) per session**, against a total supervised-session cost of **£0.861**.
`MEASURED-RCT` (platform data) + `INFERENCE` (the pricing arithmetic is the authors').

**The share of delivered cost, both ways:**

| Model | AI cost | Human cost basis | **AI as % of delivered cost** |
|---|---|---|---|
| Eedi supervised session | £0.0037 | £0.861/session | **0.43%** |
| Tutor CoPilot | $19.86/tutor/yr | 200 h × $23.10 = $4,620 | **0.43%** |
| Tutor CoPilot | $19.86/tutor/yr | 100 h × $23.10 = $2,310 | 0.86% |
| Tutor CoPilot | $19.86/tutor/yr | 500 h × $23.10 = $11,550 | 0.17% |

> **The finding, stated as bluntly as it deserves: in a human-in-the-loop tutoring
> model, the AI is between one-fifth and one-half of one percent of the cost of
> delivery. If inference went to zero tomorrow, gross margin would improve by less
> than half a point.**

This has three consequences an investor should hold onto.

1. **"Inference is getting cheaper" is not a thesis for this business.** It is a thesis
   for a pure-AI business, where inference *is* COGS. Here it is rounding error. The
   corpus's own reach arithmetic (F4 §1.3) prices a cached frontier tutoring hour at
   **$1.371** and a small-open-model hour with on-device voice at **$0.052** — both are
   dwarfed by one tutor-hour at $23.10. `INTERNAL-PRIOR`.
2. **Therefore the correct frame is capability-per-dollar, not affordability.** The
   question is not "can we afford the model?" — we can, trivially, at any tier. The
   question is "what does the extra capability buy in **L**?" Every dollar of extra
   inference must be justified by throughput or quality, never by cost.
3. **It also means a competitor can match your inference spend for nothing.** If your
   entire AI layer costs $20/tutor/year, no competitor is deterred by your compute
   budget. Compute is not a barrier to entry in this market at this scale. It is a
   barrier in pretraining; it is not a barrier here.

### 3.3 L — the leverage ratio, and the only number anyone has measured

This is where the business lives, and the evidence is much thinner than the sector
behaves as if it is.

**The acceptance figure, verified.** LearnLM Team Google & Eedi, "AI tutoring can safely
and effectively support students: An exploratory RCT in UK classrooms," arXiv:2512.23633,
trial May–June 2025, N=165 students, five UK secondary schools. From the paper, verbatim:

> *"Tutors accepted 𝑘 = 2,691 (74.4%) of its drafts without any modifications."*

2,691 / 3,617 = **74.40%**. `MEASURED-RCT`. The abstract's 76.4% is "zero or minimal
edits," where minimal means 1–2 characters — "virtually always … a tutor deleting or
changing an emoji." Median intervention altered **59 characters**. Post-hoc systematic
review found **zero** harmful or risky messages and **five** factual errors (**0.1%** of
3,617). The brief asked me to verify this figure and use it. It verifies exactly.

**And now the thing that matters: 74.4% acceptance is a quality statistic, not a
productivity statistic.** It says the model's drafts are usually good enough to send.
It says nothing about how much time the tutor saved, because reading and approving a
draft is not free. The authors are explicit, verbatim:

> *"our research design is poorly calibrated to compare the throughput of regular
> tutoring and supervised tutoring. In our trial, tutors fluidly mixed their activities
> within the same hour… As a result, we cannot cleanly attribute their time and thus
> cannot clearly assess the relative efficiency of the conditions."*

> *"[the design] precludes a rigorous measurement of throughput or efficiency for each
> condition."*

**The throughput number, and its provenance.** Because they could not measure it, they
simulated it: **six tutors** doing their normal job and **six tutors role-playing
students**, opening sessions at one-minute intervals until the working tutor pressed a
"HELP" button or left a student idle for a minute. `DEMO` — this is a staged capacity
test, not a trial arm, and it must never be reported as an RCT result.

| Metric | Human tutor alone | Supervised by LearnLM | Change |
|---|---|---|---|
| Average session duration | 3.9 min | **5.1 min** | **+31%** (worse) |
| Average concurrency | 2.3 sessions | **3.5 sessions** | **+52%** |
| **Estimated throughput** | 35.38 sessions/hr | **41.18 sessions/hr** | **+16.4%** |
| Tutor labour cost | £35.29/hr | £35.29/hr | — |
| Token cost | — | £0.0037/session | — |
| **Total cost per session** | **£0.997** | **£0.861** | **−13.6%** |

> **The measured leverage of AI drafting, in the only study that has ever estimated it,
> is +16.4% throughput and −13.6% cost per session.** Not 3×. Not 10×. Sixteen percent,
> from a six-person simulation.

**Four things about this table an investor must know before using any part of it.**

- **The concurrency gain is real but half-eaten.** Supervision let tutors hold 52% more
  simultaneous sessions, but each session took 31% longer. The net is +16.4%. Any model
  that takes the concurrency number without the duration number overstates leverage by
  a factor of three.
- **The £35.29/hour labour rate is a `VENDOR` figure inside a Google DeepMind paper.**
  Reference [43] is *"Hannah Coe. How much does a maths tutor cost in 2024/2025?"* —
  a **blog post on tutorful.co.uk**, a tutoring marketplace. The entire −13.6% cost
  saving is denominated in a rate published by a company that sells tutoring. This is
  exactly the laundering pattern this corpus exists to catch, and it appears inside the
  most rigorous AI-tutoring paper of the last two years.
- **The unit is a 4–5 minute chat intervention, not an hour of tutoring.** The Eedi
  intervention fires when a student gets the first question of a unit wrong. Extending
  +16.4% from 4-minute triage to 60-minute 1:1 instruction is an extrapolation with no
  supporting measurement. Do not do it, and be suspicious of any deck that has.
- **There is a small citation defect worth noting for calibration.** Appendix H.1 quotes
  Gemini 2.0 Flash prices but cites a Gemini 2.5 Flash page (reference [42]). Immaterial
  to the conclusion; material as a signal about how carefully cost appendices are read.

**The comparator that is *not* an AI story at all.** Saga Education's high-dosage
tutoring (Guryan, Ludwig, Bhatt, Cook, Davis, Dodge, Farkas, Fryer, Mayer, Pollack &
Steinberg — NBER w28531, published *AER* 2023, doi:10.1257/aer.20210434) `MEASURED-RCT`:

- Two RCTs, 2,633 and 2,710 students, Chicago public schools; **+0.16 SD** and
  **+0.37 SD** on maths.
- Delivery: **2:1**, up to **140 contact hours/year**, tutors were recent college
  graduates on **$16,000 + benefits** for nine months.
- Cost: **$3,500–$4,300 per participant per year**, ~$3,800 at study time — i.e.
  **$25.00–$30.71 per student-hour**, against Chicago per-pupil operating spend of
  ~$17,000/year.
- And then, verbatim from footnote 12: *"Saga has dropped its charge to districts from
  $3,800 per-pupil (2013-2015) to $3,100 per-pupil (2015-2019) to now $1,800 per-pupil
  … by obtaining an AmeriCorps subsidy of $15,000 per fellow and using a blended-learning
  model, in which the student:tutor ratio is 4:1 in lieu of 2:1 and students spend half
  their time on a learning platform, e.g. ALEKS."*

> **Read that footnote twice.** The 53% cost reduction from $3,800 to $1,800 was
> achieved by (a) halving tutor time per student, and (b) **a public subsidy of $15,000
> per tutor**. Neither is a technology gain. And the effect sizes — 0.16 and 0.37 SD —
> were measured at **2:1**, not at 4:1. **There is no RCT of the cheap version.** This
> is the single most instructive precedent in the sector for how "AI made tutoring
> cheaper" claims should be interrogated: ask what the ratio was, ask who paid the
> subsidy, and ask whether the efficacy was measured at the new ratio or the old one.

### 3.4 Putting W, L and a together

**Labour cost per learner-hour**, at BLS mean / p10 / p90 tutor wage:

| Leverage **L** | at mean $23.10 | at p10 $14.15 | at p90 $36.53 |
|---|---|---|---|
| 1.0 (pure 1:1) | **$23.10** | $14.15 | $36.53 |
| 2.0 (Saga's measured ratio) | $11.55 | $7.08 | $18.27 |
| **2.3 (Eedi, unassisted)** | **$10.04** | $6.15 | $15.88 |
| 3.0 | $7.70 | $4.72 | $12.18 |
| **3.5 (Eedi, AI-supervised)** | **$6.60** | $4.04 | $10.44 |
| 4.0 (Saga blended) | $5.78 | $3.54 | $9.13 |
| 6.0 | $3.85 | $2.36 | $6.09 |
| 8.0 | $2.89 | $1.77 | $4.57 |

**Gross margin** at `a = $0.08` per learner-hour (a generous AI allowance — an order of
magnitude above the Eedi-implied rate and comparable to a cheap-tier hosted model with
on-device voice from F4 §1.3):

| Price / learner-hour | L=1.0 | L=2.0 | L=3.5 | L=6.0 |
|---|---|---|---|---|
| $20 | **−16%** | 42% | 67% | 80% |
| $30 | 23% | 61% | 78% | 87% |
| $40 | 42% | 71% | 83% | 90% |
| $50 | 54% | 77% | 87% | 92% |
| $75 | 69% | 84% | 91% | 95% |

`INFERENCE` — this is my arithmetic on measured inputs, and every input is cited above.
Attack the inputs, not the model.

**What the table says, in plain words:**

- **At true 1:1 with a US tutor, there is no software business below $30/learner-hour.**
  Gross margin is negative at $20 and 23% at $30 — before sales, support, safeguarding
  or platform cost. Every consumer 1:1 tutoring business is therefore either priced
  above $40/hour, or offshore, or subsidised, or losing money.
- **Leverage is the only lever with real range.** Moving L from 1 to 2 buys ~19–29
  margin points at every price. Moving price from $30 to $50 buys ~13–20. Moving `a`
  from $0.08 to $0 buys **0.3**.
- **And the measured AI contribution to L is +16.4%** — which, from L=2.3 to L=3.5 in
  the Eedi setting, is worth about 6 margin points at $30/learner-hour. Real. Not
  transformative. **Not a moat.**

**Sensitivities, ranked by how much they move gross margin:**

| Sensitivity | Range observed | Margin impact | Controllable? |
|---|---|---|---|
| Leverage ratio **L** | 1.0 → 4.0 measured in the field | **~50 points** | Partly — pedagogy and format, not AI |
| Tutor wage geography | $16.34 → $36.81/hr (`GOV-STAT`) | **~15–25 points** | Yes, if delivery is online |
| Price point | $20 → $75/learner-hour | **~30 points** | Only where willingness-to-pay exists |
| Utilisation (paid hours ÷ available hours) | not disclosed by any filer | large, unmeasured | Yes |
| **AI inference cost** | $0.005/session → $0 | **0.4 points** | Irrelevant |

> **The one-line summary of §3: this is a labour-arbitrage and utilisation business
> wearing an AI costume. That is not a criticism — labour arbitrage with a real
> quality-preserving mechanism is a fine business. But it must be underwritten as one,
> and its defensibility must be argued on that basis, not on model quality.**

### 3.5 The audited comparison: what happened to the one public company doing this

**Nerdy Inc. (NYSE: NRDY), CIK 0001819404, Form 10-K for FY2025, filed 2026-02-26.**
`FILING`. Nerdy operates Varsity Tutors and describes itself, verbatim, as *"a
next-generation live tutoring and intervention platform that leverages the power of human
expertise with advanced artificial intelligence ('AI')."* It is the closest listed
comparable that exists for an AI-native, human-in-the-loop tutoring company.

| Line ($000) | FY2023 | FY2024 | **FY2025** |
|---|---|---|---|
| Revenue | 193,399 | 190,231 | **178,988** |
| Cost of revenue | 56,952 | 61,837 | **75,208** |
| **Gross profit** | 136,447 | 128,394 | **103,780** |
| **Gross margin** | **70.6%** | **67.5%** | **58.0%** |
| Sales & marketing | 68,448 | 71,623 | 60,123 |
| General & administrative | 125,570 | 126,879 | 105,521 |
| Operating loss | (57,571) | (70,108) | **(61,864)** |

Segment split FY2025: **Consumer $150,736k (84%)**, **Institutional $27,607k (15%)**,
Other $645k. Institutional revenue fell **22%**.

**Adjusting honestly.** FY2025 cost of revenue includes a **$7,757k** write-off from
*"the abandonment of certain components of our previously capitalized internal-use
software … rebuilt on entirely new, AI-native codebases"* plus **$6,429k** of software
amortisation. Excluding the abandonment charge, FY2025 gross margin is **62.3%** — still
5.2 points below FY2024. Excluding both amortisation and abandonment, the residual
"Expert cost and other" line is **$61,022k = 34.1% of revenue**, against **29.3%** in
FY2024.

**And the company states the cause, verbatim:**

> *"Excluding this impact, cost of revenue increased $5,614 thousand due to higher
> Expert costs of $5,243 thousand, primarily driven by investments in Expert pay and
> incentives."*

> **In the year Nerdy rebuilt its platform on AI-native codebases, its human cost line
> went *up* $5.2M while revenue went *down* $11.2M.** `FILING`. That is the opposite of
> the leverage story, and it is the only audited test of that story in existence.

**The counter-evidence, reported because it exists.** Form 10-Q for Q1 2026, filed
2026-05-07 `FILING`:

| Line ($000) | Q1 2026 | Q1 2025 |
|---|---|---|
| Revenue | 48,735 | 47,595 |
| Cost of revenue | 16,461 | 19,984 |
| **Gross margin** | **66.2%** | **58.0%** |
| Operating loss | (5,798) | (16,585) |
| Active Members (000) | 36.9 | 40.5 |
| **Active Experts (000)** | **8.3** | **10.8** |
| ARPM | $374 | $335 |

Gross margin recovered 8.2 points year-over-year and the operating loss narrowed 65%.
**Revenue per Active Expert rose from $4,407 to $5,872 — +33%.** That is genuine
operating leverage on the supply side, achieved with **23% fewer active experts**.

**But read the whole disclosure before calling it AI leverage.** The company attributes
the expert consolidation to *"our Expert incentives, which has promoted utilization of
the highest quality Experts by encouraging them to work with more Learners"* — an
incentive-design change, not an AI-drafting change. Revenue grew 2.4% while **Active
Members fell 8.9%**; the growth came from **price increases enacted in February 2025**
(ARPM +11.6%). And the company's own 10-K risk factor says, verbatim:

> *"There can be no assurance that our investments in AI will be beneficial to our
> business."*

**The honest read, and it is genuinely two-sided:** one year of margin compression
followed by one quarter of margin recovery, with the recovery driven by disclosed
non-AI mechanisms (price, incentives, headcount) and no disclosure of hours, utilisation
or draft-acceptance. **One quarter is not a trend, and the company does not claim it
is.** An investor evaluating any AI-tutoring company should ask for exactly the
disclosures Nerdy does not make: hours delivered, tutor utilisation, and learner-to-tutor
ratio over time.

**A derived structural datum, useful as a reference point.** At ARPM $364/month with
expert cost at ~34% of revenue, roughly **$124/member/month** flows to the expert; at
the BLS mean wage that is **~5.4 tutor-hours per member-month**. `INFERENCE` — from
`FILING` inputs. That is the shape of a US consumer tutoring membership: about five
hours of human time a month, sold for $364.

### 3.6 The three cost structures, side by side

| | **Pure human** | **Human-in-the-loop** | **Pure AI** |
|---|---|---|---|
| COGS driver | Tutor wage × hours | Tutor wage ÷ L, + tokens | Tokens + serving |
| Cost / learner-hour | $14–$37 (`GOV-STAT`) | $4–$18 at L=2–3.5 | $0.012–$1.41 (`INTERNAL-PRIOR`, F4 §1.3) |
| Structural gross margin | 40–70% | 55–85% | 85–95% |
| Marginal cost of the next learner | ≈ average cost | ≈ average cost ÷ L | ≈ 0 |
| What improves with the frontier | nothing | ~0.4 points of margin, plus L | COGS directly |
| Efficacy evidence | strongest in the field (Nickow et al. pooled **0.288 SD**) | one exploratory RCT, n=165 | contested; one large RCT shows **−17%** post-removal |
| Regulatory exposure | employment, safeguarding | both | AI Act Art. 50, COPPA, model liability |
| **Scaling constraint** | **hiring** | **hiring ÷ L** | **distribution** |

The row that decides the investment is the last one. **A pure-AI business is constrained
by distribution; a human-in-the-loop business is constrained by hiring.** Hiring
constraints do not fall with Moore's law, and they are the reason the human-in-the-loop
model cannot produce a software growth curve unless L rises a lot more than 16%.

**On the efficacy row, one correction that matters commercially.** The tutoring
meta-analysis everyone cites is Nickow, Oreopoulos & Quan. The widely quoted **0.37 SD**
is from the **2020 NBER working paper** (w27476). The peer-reviewed version — *American
Educational Research Journal*, doi:10.3102/00028312231208687 — reports a pooled
**0.288 SD**. `MEASURED-META`, `INTERNAL-PRIOR` (project standing correction). A deck
citing 0.37 is citing a superseded working paper, and that is a fast, cheap diligence
test.

---

## 4. The competitive map

**Method.** Company directories rot. This map is built from **filings first**: 10-K,
10-Q, 20-F, 40-F, Form D, Form C-AR and IRS Form 990. Where a company has no filed
number, that is reported as the finding. **No vendor claim below is restated as a
finding**; vendor language is quoted and labelled.

### 4.1 How small this category is in the public record

`OBSERVED` — EDGAR full-text search, retrieved 2026-07-29:

| Phrase | Filings containing it, all forms, all time |
|---|---|
| `"AI tutor"` | **47** |
| `"AI tutoring"` | **24** |
| `"high-dosage tutoring"` | **47** (dominated by a single issuer, Nerdy) |
| `"high-impact tutoring"` | **1** |
| `"intelligent tutoring system"` | **12** (most recent: 2006) |

The issuers who use "AI tutor" in a filing at all: Nerdy, Chegg, Pearson, Docebo,
Synthesis School, Classover Holdings, Youdao, NetEase, Gaotu Techedu, VEON, Nebius,
Adtalem, and one S-1 registrant. **There is no public comparable set for an AI-native
tutoring company.** Every revenue multiple offered to an investor in this category is
therefore borrowed from a company with a different cost structure — most often a
software company with 75–85% gross margins, which §3 shows this business does not have.

### 4.2 Segment 1 — AI-only / AI-first learning products

| Company | Filed financials | What it claims | What it can evidence | Business model |
|---|---|---|---|---|
| **Duolingo** (DUOL, CIK 1562088) `FILING` 10-K FY2025, filed 2026-02-27 | Revenue **$1,037.6M** (+39%); gross margin **72.2%** (72.8% FY2024); operating income **$135.6M**; MAU 133.1M, DAU 52.7M, paid subs 12.2M (9% of MAU) | Consumer language learning at scale | Scale, retention and margin — all filed. **No learning-outcome RCT is in the filing.** | B2C freemium subscription + Duolingo English Test |
| **Synthesis School** (CIK 1857145) `FILING` Form C-AR FY2025, filed 2026-04-10 | Revenue **$10.98M** (+6.5%); COGS $1.68M → **84.7% gross margin**; net loss **$(2.78)M** (was $(6.16)M); cash $0.96M (was $4.05M); short-term debt **$15.3M** against **$2.85M** total assets; **26 employees**. Filed **Form C-TR** the same day, ending its reporting obligation | AI maths tutor for children | The filings. Its marketing offers testimonials and a family count and **no outcome data**. | B2C subscription |
| **Khan Academy** (501(c)(3), EIN 26-1544963) `FILING` IRS Form 990 FY2023 | Total revenue **$98.27M**, of which **contributions $84.19M**; program service revenue **$12.06M** (flat for six years); total expenses **$68.13M** | Khanmigo, the largest AI-tutoring deployment in the world | Its own founder said in July 2026 the first Khanmigo *"did not change student learning as much as many of us hoped it would"* (`OBSERVED`, vendor statement against interest, E3 §2) | **Philanthropy.** Earned revenue is ~12% of income and has not grown |

**The Duolingo row is the most useful single comparison in this section**, because it is
the pure-AI cost structure with audited numbers. Verbatim from the 10-K:

> *"Cost of revenues predominantly consists of third-party payment processing fees
> charged by various distribution channels in addition to hosting fees and Artificial
> Intelligence ('AI') costs."*

> *"Total gross margin decreased to 72.2% from 72.8%… The decrease was primarily
> attributable to both a decline in subscription gross margin, **reflecting increased AI
> costs used in features like Video Call**, and a shift in revenue mix."*

`FILING`. **A generative-AI-heavy consumer learning product sustained ~72% gross margin
at $1.04B revenue, with AI cost contributing to at most 60 basis points of annual margin
compression.** That is the pure-AI structure: AI is a real but small COGS line, and the
margin is 10–14 points above the human-in-the-loop comparable (§3.5). Note the limit of
the claim: Duolingo does **not** separately quantify AI spend, so any specific
inference-cost figure attributed to Duolingo is an estimate, not a filed number.

**The Khan Academy row is the most misread.** It is routinely cited as evidence that AI
tutoring works at scale. What the 990 shows is a **philanthropically funded** programme:
FY2023 revenue rose 85% and the entire increase was contributions ($40.0M → $84.2M);
earned revenue is flat at ~$12M and has been for six years. **Comparing Khanmigo to a
commercial AI-tutoring P&L is a category error.** It also has no post-launch-scale
audited financials in the public record — FY2023 is the latest 990 available and it
captures only Khanmigo's first nine months.

### 4.3 Segment 2 — human tutoring marketplaces adding AI

| Company | Filed financials | Business model | The number that matters |
|---|---|---|---|
| **Nerdy / Varsity Tutors** (NRDY, CIK 1819404) `FILING` 10-K FY2025 + 10-Q Q1 2026 | Revenue **$178.99M** (−5.9%); GM **58.0%** (67.5% FY2024, 70.6% FY2023); operating loss **$(61.9)M**; Consumer $150.7M / Institutional $27.6M (−22%); Active Members 33.2k (−11.5%); Active Experts 15.8k (−22%); ARPM $364 | Two-sided marketplace; B2C membership + district ("Varsity Tutors for Schools") | See §3.5 in full. **Expert costs rose $5.24M while revenue fell $11.24M** |
| **Stride** (LRN, CIK 1157408) `FILING` FY2025 10-K + Q3 FY2026 10-Q | FY2025 revenue **$2,405.3M**, gross margin **39.2%** (35.2% FY2023); operating income $360.1M. Q3 FY2026: revenue +2.7%, **gross margin −384 bps** to 36.8% | Full-time virtual schooling under district/state contracts | The only profitable scaled operator here, at **39% gross margin** — the structural margin of a labour-delivered education business |

**The comparison an investor should hold in mind:** Duolingo 72%, Synthesis 85%, Nerdy
58%, Stride 39%. **Gross margin in this sector is a direct read-out of how much human
time is in the delivery.** No AI narrative has yet moved a company from the bottom of
that ladder to the top.

### 4.4 Segment 3 — content, curriculum and platform

| Company | Filed financials | Note |
|---|---|---|
| **Pearson plc** (PSO, CIK 938323) `FILING` 20-F FY2025, filed 2026-03-13 | Revenue **£3,577M**; gross profit **£1,860M (52.0%)**; operating profit £507M | Still an SEC registrant and still NYSE-listed. The incumbent that AI was supposed to kill has flat revenue and rising gross margin |
| **Coursera** (COUR, CIK 1651562) `FILING` 10-K FY2025 | Revenue **$757.5M** (+9%); GM **54.6%**; operating loss $(77.4)M. Two segments only — **Degrees is no longer reported** | Merger agreement with **Udemy** signed 2025-12-17, exchange ratio **0.800** Coursera shares per Udemy share; not closed at the 10-K. **Coursera makes no generative-AI revenue-decline attribution** — a material contrast with Chegg |
| **Docebo** (DCBO, CIK 1829959) `FILING` 40-F FY2025 | Revenue **$242.7M**; GM **80.3%**; operating income $23.2M | The software-margin comparison point |
| **Skillsoft** (SKIL) `FILING` 10-K FY2026 (to 31 Jan 2026) | Revenue **$512.7M** (−3.4%); GM ~73.7%; operating loss $(89.5)M | Corporate learning, declining |
| **Zearn** (501(c)(3), EIN 37-1665745) `FILING` Form 990 FY2023 | Revenue **$45.28M** (flat vs $46.02M FY2022); expenses **$40.53M**, up from $13.46M in FY2021 | **Expenses tripled in two years while revenue plateaued** — the textbook ESSER-funded expansion profile, visible in a tax return |
| **CommonLit** (501(c)(3)) `FILING` Form 990 FY2023 | Revenue $13.86M; expenses $17.21M → **$3.35M deficit** | Same pattern, smaller |

### 4.5 Segment 4 — teacher-productivity tools

The fastest-growing narrative segment and the one with the least filed evidence.

`OBSERVED` — EDGAR search for Form D filings: **MagicSchool AI, Speak (Speak Easy Labs)
and Ello have no EDGAR presence at all** — no Form D, no CIK. Absence of a Form D does
not prove no capital was raised (Rule 506 state-only filings and differently-named
holding entities both explain it), but it does mean **every circulating round size for
those three companies is press-only and untraceable to a filed source**, and this
section does not repeat those numbers.

What *is* filed, for calibration on what an edtech round actually looks like when a
company does file (`FILING`, Form D `totalAmountSold`):

| Issuer | CIK | Form D filings | **Cumulative amount sold** |
|---|---|---|---|
| **Amira Learning** | 1785128 | 2019-08-13, 2020-05-27 (D/A), 2021-05-21, 2022-04-22 | **$42.9M** (no Form D after 2022) |
| **Synthesis School** | 1857145 | 2021-04-15, 2021-06-02 | **$5.09M** Reg D + a Reg CF raise |

And the metric this segment sells on — "hours of teacher time saved" — is the sector's
substitute success criterion (E1 finding, `INTERNAL-PRIOR`). It fails the Null-Learner
Test in §7.1: a tool that generates unused lesson plans maximises it perfectly.

### 4.6 The graveyard and the current distress, with the filings

**Chegg — the only audited measurement of what generative AI does to an incumbent.**
`FILING`, Form 10-K FY2025 filed 2026-03-09 (CIK 1364954) and Form 10-Q Q1 2026 filed
2026-05-11.

| ($000) | FY2023 | FY2024 | **FY2025** |
|---|---|---|---|
| Total net revenues | 716,295 | 617,574 | **376,908** (−39%) |
| Academic Services | — | 543,615 | **308,254** (−43%) |
| Chegg Skilling | — | 73,959 | 68,654 (−7%) |
| Gross margin | 68.5% | 70.7% | **59.6%** |
| Operating income/(loss) | (67,725) | (737,108) | **(116,856)** |

Q1 2026 net revenues **$63,262k** vs $121,387k — an annualised run-rate of ~$253M
against $716M in FY2023, a **−65% peak-to-trough decline in two years**. The company's
own attribution, verbatim:

> *"Recent technological shifts, notably Google's AI Overviews search experience, or
> AIO, and continued increase in adoption of free and paid generative AI services by
> students, have created and are expected to continue to create headwinds for our
> industry and our business, most notably a reduction in traffic to our website and
> customers subscribing to our services."*

> *"students are increasingly turning to generative AI for academic support… students
> see generative AI products like ChatGPT and others as strong alternatives to
> vertically specialized solutions for education such as Chegg."*

And the operational consequence, verbatim: *"reductions of our global workforce of
approximately 640 employees, or approximately 56% of our then-current workforce."*
Chegg has also sued Google in the District of Columbia over AIO; Google's motion to
dismiss was pending as of the Q1 2026 10-Q.

**Two readings, and the distinction is the whole lesson.** The *distribution* channel
(search traffic) and the *product* substitute (free chatbots) are named in the same
sentence, and the filing does not separate them. `INFERENCE`: a company whose customer
acquisition depends on a channel controlled by a company that also ships the substitute
has a structural, not cyclical, problem. **An investor should ask every AI-tutoring
company what fraction of its acquisition comes from a channel owned by a model
provider.**

**A disclosure fact worth its own line:** Chegg discloses **no subscriber count** in the
FY2025, FY2024, FY2023 or FY2022 10-K, and the word "subscriber" does not appear at all
in the FY2025 earnings release. **Any Chegg subscriber figure in circulation for these
years is untraceable to a filed source.** `UNTRACEABLE`.

**2U / edX — died of unit economics.** `FILING`, CIK 1459417 (registrant now "2U, LLC").

| Item | Value | Source |
|---|---|---|
| Last audited revenue (FY2023) | **$945.95M** | 10-K filed 2024-03-06 |
| Net loss FY2023 | **$(317.6)M** | same |
| Marketing & sales | **$372.1M = 39.3% of revenue** | same |
| Long-term debt at 31 Dec 2023 | **$896.5M** | same |
| Total liabilities | $1,240.6M | same |
| Chapter 11 petition | **25 July 2024**, *In re: 2U, Inc.*, Case No. **24-11279 (MEW)**, Bankr. S.D.N.Y. | 8-K filed 2024-07-25 / 2024-09-10 |
| Emergence | 4 September 2024 | 8-K filed 2024-09-10 |
| Deregistration | Form 15-12G, 25 September 2024 | — |

**~$900M of debt against ~$946M of revenue, and Chapter 11 4.7 months after its final
10-K.** Note also: **2U never reported a gross profit line** — its costs are functional
(curriculum/teaching, servicing, technology, marketing). Any "2U gross margin" in
circulation is a third-party construction. `UNTRACEABLE`.

**Byju's — the negative finding, and it is important.** `UNTRACEABLE`.

EDGAR full-text search returns **zero** filings by Think & Learn Private Limited under
any name variant. It is an unlisted Indian private company; its only statutory accounts
sit with the Indian Ministry of Corporate Affairs (paywalled per document, no API), and
were filed years late. **Every Byju's figure in press circulation — the $22bn valuation,
the revenue claims, the 150M-user claim — is untraceable to an audited source and is not
repeated here as a number.**

The single SEC-traceable Byju's datapoint that exists: **Blackstone Private Credit Fund
(BCRED, CIK 1803498)** disclosed a position in **Byjus Alpha, Inc.** — the Delaware SPV
that issued Byju's Term Loan B — in its filed Schedule of Investments: par $50,000k,
cost $49,229k, **fair value $50,729k at 31 December 2021**, 0.39% of net assets
(10-Q filings 2022-05-13, 2022-08-12, 2022-11-14). `FILING`. A third-party mark at
approximately par at end-2021, and no reference in any filing after November 2022.

**Gaotu Techedu — the regulatory precedent, audited.** `FILING`, Form 20-F.

| CNY millions | 2020 | 2021 | **2022** | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|
| Revenue | 7,124.7 | 6,561.7 | **2,498.2** | 2,960.8 | 4,553.6 | 6,146.8 |
| Operating income | (1,755.0) | (3,180.3) | (118.1) | (149.0) | (1,181.8) | **(503.2)** |

**−62% revenue in one year** following China's July 2021 "double reduction" policy on
for-profit core-subject tutoring; revenue recovered by 2025 and the company is **still
loss-making at the operating line five years later**. This is §8.1's evidence.

**Youdao — the same shock, absorbed differently, and a margin trend worth noting.**
`FILING`, Form 20-F. Revenue grew through the policy (CNY 4,015.8M 2021 → 5,909.0M
2025) and operating income turned positive in 2024. But gross margin fell steadily:
**49.5% (2021) → 51.4% (2023) → 48.9% (2024) → 44.3% (2025)**. A learning company
growing revenue while gross margin declines is the same pattern as Nerdy's FY2025, in a
different market.

---

## 5. Defensibility — the question that decides the investment

Eight candidate moats. Each graded on two axes: **is it real today**, and **does it
survive the next frontier-model release**. The second axis is the one most edtech decks
never address.

| # | Candidate moat | Real today? | Survives a frontier release? | Grade |
|---|---|---|---|---|
| 1 | Proprietary learning data | Weakly | Mostly no | **D** |
| 2 | Model quality / prompt architecture | No | No | **F** |
| 3 | Distribution & procurement relationships | Yes | **Yes** | **B** |
| 4 | Brand / trust with parents | Partly | Yes | **C+** |
| 5 | Switching cost | Weak in K-12 | Yes, where it exists | **C−** |
| 6 | Network effects (two-sided) | Weak | Yes, if achieved | **C−** |
| 7 | Regulatory conformance as an asset | Yes, and rising | **Yes** | **B+** |
| 8 | **Verification capability** | Rare | **Yes** | **A−, and almost nobody has it** |

### 5.1 Proprietary data — **grade D**

The claim is that accumulated tutoring dialogues, misconception labels and learner
trajectories become a compounding asset. The empirical test is simple: *do the
organisations with the most of this data treat it as a crown jewel?* They do not.

`OBSERVED`, retrieved from the Hugging Face dataset API on 2026-07-29:

- **`Eedi/Question-Anchored-Tutoring-Dialogues-2k`** — published by **Eedi's own
  organisation account**, CC-BY-NC-4.0, 10K–100K rows, tutor–student chat dialogues with
  question and misconception metadata. This is the same company whose supervised-tutoring
  trial produced the 74.4% figure. **They gave the dialogues away.**
- **`ASSISTments/FoundationalASSIST`** — published by ASSISTments' own account,
  CC-BY-NC-4.0, **1M–10M rows**, accompanied by arXiv:2602.00070.
- **EdNet** (Riiid) and **ASSISTments 2009** are mirrored many times over by third
  parties. Riiid's successor company has removed the knowledge-tracing research identity
  from its corporate site entirely (`OBSERVED`, E3 §3.2) — the dataset outlived the
  institution.

**Why the data moat is weak here specifically.** Learning interaction data is (a)
narrow-domain, (b) heavily duplicated across vendors teaching the same curriculum, (c)
legally encumbered — under FERPA the vendor typically holds it as a "school official"
acting under the district's direct control, and under the 2025 COPPA amendments and
state statutes its use for model training is constrained — and (d) most valuable exactly
where it is most public (maths misconceptions).

**Where a data moat *is* real, and it is narrow:** longitudinal per-learner state that
the *learner* will not re-enter elsewhere, and **outcome-linked** data — dialogues paired
with a later, independent assessment result. Almost nobody has the second. It is
expensive, slow, and it is the only version of this asset a frontier model cannot
replicate by being better at language.

### 5.2 Model quality and prompt architecture — **grade F**

This is the moat most often claimed and it is the one this corpus has most thoroughly
falsified.

- **Prompt architecture is publishable and published.** The Eedi production system
  prompt is printed in full in Appendix D.1 of arXiv:2512.23633. `OBSERVED`. Anyone can
  copy it in an afternoon.
- **Designed pedagogy did not beat plain ChatGPT in a controlled trial.** Fütterer,
  Bardach, Kuhn, Keller & Gerjets (2026), *Educational Psychology Review*,
  doi:10.1007/s10648-026-10133-8, n=371, Grades 7–9, six 45-minute sessions in regular
  physics/English lessons. Two scaffolded GenAI conditions against a **plain ChatGPT
  control**. Verbatim: *"no statistically significant advantages of either intervention
  over the control condition were found for effort, domain-specific knowledge, or
  elaboration-based strategy use."* `MEASURED-RCT`.
- **Persona and role prompting buy no measured accuracy** (162 personas × 2,410
  questions; project standing correction). `INTERNAL-PRIOR`.
- **The frontier ships pedagogy for free.** No lab has shipped an education-positioned
  frontier model (`OBSERVED`, E3 §1), but every lab ships a study/tutor mode, and
  LearnLM's capabilities were folded into Gemini rather than sold separately.

**Test to apply to any company claiming this moat:** ask them to name the specific
capability their product has that the next frontier release cannot absorb. If the answer
is a prompt, a persona, a curriculum-shaped scaffold, or "our model is fine-tuned on
teaching," it is not a moat — it is a feature with a six-to-twelve-month half-life.

### 5.3 Distribution and procurement relationships — **grade B**

This is the moat most founders under-rate and the one most likely to survive. The reason
is arithmetic, not sentiment: a district relationship takes 9–18 months and a stack of
compliance artefacts to establish (§2), and a frontier model release does not shorten
that by a day. **The barrier that is annoying to you is also the barrier that protects
you**, and it is the only barrier in this list with that property.

Three qualifiers keep it at B rather than A:

- **It is expensive to build and does not compound cheaply.** Nerdy spends **33.6% of
  revenue on sales and marketing** and still lost 22% of Institutional revenue in a
  year `FILING`. 2U spent **39.3%** on marketing and sales and went bankrupt `FILING`.
  A distribution moat that costs a third of revenue to maintain is a cost centre with
  good PR.
- **It is bundleable away.** The incumbent with the SIS/LMS relationship can add a
  tutoring module and reach every one of your prospects at zero incremental sales cost.
- **It is not the same as a contract.** See §5.5.

### 5.4 Brand and parental trust — **grade C+**

Real, slow, and genuinely durable against model releases — a parent choosing who talks
to their child is not running an eval. Two limits: it is expensive to build in a
category where the salient news events are harms, and it is asymmetrically destructible
— one safeguarding incident does more damage than three years of accumulation. Chegg's
own encyclopedic record already carries the academic-integrity association
(`REFERENCE`, E1 §2.2); brand in this sector is a liability account as much as an asset
account.

### 5.5 Switching cost — **grade C−**

Weaker in K-12 than founders assume, and there is an audited number for it: **"Contracts
with Institutions are generally short-term in duration (one year or less)"** (Nerdy 10-K,
FY2025, critical-audit-matter disclosure) `FILING`, and Institutional revenue fell 22%
in a single year. Annual, re-competed, budget-cycle-dependent contracts are the norm for
supplemental services — genuine switching cost lives in the SIS/LMS layer (rostering,
gradebook, single sign-on), not in the tutoring layer.

Where switching cost *is* real: (a) deep LTI/OneRoster integration that a district's IT
team must re-do; (b) accumulated per-learner history that a parent or IEP team will not
recreate; (c) multi-year state contracts, which exist but are rare and are won on
procurement capability, not product.

### 5.6 Network effects — **grade C−**

The two-sided marketplace story is that more learners attract more tutors and vice
versa. The audited comparable is evidence *against* strong network effects on the
supply side: **Nerdy's Active Experts fell 22% (FY2025) and 23% (Q1 2026) with no
disclosed service failure**, and the company states it believes its remaining expert
count *"is sufficient to meet our near-term growth objectives"* `FILING`. A supply side
that can shrink by a fifth without breaking is elastic, not scarce — and elastic supply
is the opposite of a network effect.

Where network effects *are* plausible: within a single school or centre, where cohort
formation and peer interaction have measured pedagogical value (F2, `INTERNAL-PRIOR`).
That is a local, not a global, network effect, and it does not deter entry.

### 5.7 Regulatory conformance as an asset — **grade B+**

The unusual moat in this list: it is the only one that gets *stronger* as the technology
gets better, because capability growth is what drives the regulation. A company holding
SOC 2 Type II, signed state data-privacy agreements in the states that require them, a
current WCAG 2.1 AA conformance report, and an EU AI Act Article 50 compliance posture
holds a set of assets that (a) cost real time and money, (b) are checked by a
procurement officer before anyone looks at the product, and (c) are entirely unaffected
by a frontier release.

It is a **B+ rather than an A** for one reason: it is purchasable. Compliance is a
professional-services market. It buys you 6–12 months against a well-funded competitor,
not five years. The durable version is conformance *plus* the operating history that
proves it — an incident log with zero entries over years, which cannot be bought.

### 5.8 Verification capability — **grade A−, and it is the one almost nobody has**

This corpus's sharpest structural finding (K2 §0, `INTERNAL-PRIOR`) is that **the value
of an agentic loop is almost exactly the value of the external check it closes on** —
large replicated gains where a cheap verifier exists (test suites, proof kernels, exit
states), collapse to one-good-prompt performance where it does not. Teaching has no
cheap verifier. This is the field's central unsolved problem and therefore its most
durable commercial opportunity.

**Why it is the best moat available:** a company that can *demonstrate* that a learner
learned — cheaply, at scale, with delayed unannounced novel-item transfer assessment —
owns something that (a) a frontier model release does not obsolete, because it is a
measurement instrument rather than a generation capability; (b) is exactly what a
procurement officer needs to justify a renewal; (c) is the required evidence under ESSA
tiers and is what the corpus's whole efficacy literature is missing; and (d) compounds,
because outcome-linked data is the one data asset (§5.1) that is genuinely scarce.

**Why almost nobody has it:** it is expensive, it produces uncomfortable answers, and
the proximal/distal dissociation is the most reproducible finding in the literature —
Tutor CoPilot moved the exit ticket (+4 p.p., p<0.01) and **did not move the end-of-year
state test**; Nigeria +0.310 SD composite vs +0.206 SD school exam. `MEASURED-RCT`,
`INTERNAL-PRIOR` (B2 §4). A company that builds verification will find out that its
product works less well than it hoped. That is precisely why it is a moat: the cost is
psychological as well as financial, and most competitors will not pay it.

---

## 6. Why now, and why not three years ago

The honest version has three real changes and three false ones.

### 6.1 What genuinely changed

| # | Change | Evidence | Why it matters commercially |
|---|---|---|---|
| 1 | **Draft quality crossed the acceptance threshold.** A supervising human now approves ~3 in 4 AI-drafted tutoring messages unedited, with zero harmful messages and 0.1% factual errors in a 3,617-message audit. | `MEASURED-RCT` arXiv:2512.23633 | Below ~50% acceptance the human is rewriting, and the AI is a cost. Above ~75% the human is reviewing, and the AI is leverage. **This threshold was not demonstrably crossed before 2025.** |
| 2 | **Cost per unit of capability collapsed.** Constant-capability prices fell 9×–900×/year, median **50×/year**; post-2024 median **200×/year**. | `INTERNAL-PRIOR` F4 §1.4 (Epoch AI) | It makes the AI layer free *relative to labour* (§3.2) — which is what permits generous per-learner AI spend without touching gross margin. It does **not** improve the margin itself. |
| 3 | **Frontier-adjacent weights became legally deployable on-premises.** Gemma 4 ships Apache-2.0, ungated, with a 4.5B-effective-parameter variant. | `OBSERVED` E3 §1.3 | Removes the "we cannot send student data to a US cloud" procurement objection — a genuine gate, not a talking point (§2). |

### 6.2 What did *not* change, and this is where the overclaiming lives

| # | Non-change | Evidence |
|---|---|---|
| 1 | **Nobody shipped an education-positioned frontier model.** Not one lab, of eight surveyed. Education remains a prompt layer on a general model. | `OBSERVED` E3 §0 |
| 2 | **The efficacy evidence base is still thin and still proximal.** Best current AI-tutoring result vs a human tutor is +5.5 p.p. transfer with a credible interval spanning zero, n=165. Best human-tutoring meta-analytic pooled effect is 0.288 SD. | `MEASURED-RCT` / `MEASURED-META` |
| 3 | **Designed pedagogy still has not beaten plain ChatGPT in a controlled trial.** | `MEASURED-RCT` Fütterer 2026 |
| 4 | **Tutor wages did not fall.** Saga's stipend rose 25% ($16k → $20k) over the window in which inference fell by orders of magnitude. | `MEASURED-RCT` context, NBER w28531 |
| 5 | **Procurement cycles did not shorten.** District budget cycles, privacy review and accessibility conformance are unchanged by model capability. | §2 |
| 6 | **The measured throughput gain is +16.4% and comes from a six-person simulation.** | `DEMO` |
| 7 | **Full-duplex live voice — the pedagogically decisive modality — still is not shipped in a form a school can deploy.** | `INTERNAL-PRIOR` D1 §6 / E3 §1.4 |

> **The synthesis: what changed is that the AI became good enough for a human to
> approve its output, and cheap enough that approving it is worth doing. What did not
> change is anything about whether children learn more, or about how long it takes to
> sell to a school. A company whose "why now" rests on the first pair is credible; one
> whose "why now" rests on the second is not.**

---

## 7. The metrics a board should track, and the ones it should refuse

The corpus's governing test (F6 §7.3, `INTERNAL-PRIOR`):

> **The Null-Learner Test.** Simulate an agent that maximises the metric while learning
> nothing — the cheapest action sequence that satisfies the measurement. **If it scores
> well, the metric is invalid as a learning objective.**

### 7.1 The refuse list

| Metric | Null-learner verdict | Why a board is shown it anyway |
|---|---|---|
| DAU / MAU | **Maxed trivially** | It goes up |
| Streaks | **Maxed trivially** | It goes up fastest |
| Time-on-task / session length | **Maxed trivially**, and its measurement is methodologically fragile (Kovanović et al. 2016, doi:10.18608/jla.2015.23.6) | It looks like effort |
| XP / points / badges | **Maxed trivially** | Gamification vendors sell it |
| Messages exchanged with the AI | **Maxed trivially** | It scales with token spend |
| CSAT / NPS from learners | **Maxed by being agreeable** — F9 records learners rating understanding *higher* under conditions that produced *worse* learning | It is cheap to collect |
| "Hours of teacher time saved" | Not a learning metric at all; it is the sector's substitute success criterion (E1 finding) | It is the one number that reliably moves |
| Lessons/plans generated | **Maxed by a cron job** | It is the easiest thing to instrument |
| Draft-acceptance rate | **Maxed by drafting blandly.** A model that only ever writes "Great effort! What do you think the next step is?" is accepted 100% of the time | It is the industry's favourite new number, including in this section |

That last row deserves emphasis, because §3 leans on the 74.4% figure. **Acceptance rate
is a safety and quality floor, not a learning metric, and it fails the Null-Learner Test
outright.** Its correct use is as a *guardrail* — "did quality regress?" — never as a
board KPI.

### 7.2 The set a board should actually see, monthly

Designed so that a do-nothing product cannot fake it. Five tiers.

**Tier 1 — learning (cannot be faked; the only tier that justifies the company)**

| # | Metric | Definition | Why it survives |
|---|---|---|---|
| 1 | **Delayed novel-item transfer rate** | % correct on unannounced items ≥14 days after instruction, drawn from a held-out bank never seen in-product, on content *not* taught in the session | A null learner cannot answer novel delayed items. This is the corpus's one metric that passes cleanly |
| 2 | **Misconception resolution, verified later** | % of diagnosed misconceptions that remain resolved on a later, differently-worded probe | Distinguishes teaching from patching. Eedi measured the immediate version (95.4%); the *later* version is the one nobody reports |
| 3 | **Proximal-to-distal ratio** | (in-product mastery gain) ÷ (independent-assessment gain) on the same cohort | Directly instruments the field's most reproducible failure. A ratio drifting above ~2 means the product is training its own metric |
| 4 | **Learners on an independent assessment**, count and share | How many learners have *any* outcome measured outside the product | If this is near zero, tiers 2–5 are unfalsifiable |

**Tier 2 — the economic engine (the three quantities from §3)**

| # | Metric | Why |
|---|---|---|
| 5 | **Realised leverage ratio L** — learner-hours delivered ÷ paid tutor-hours, reported monthly as a time series | The entire margin thesis. If it is flat, the AI is decorative |
| 6 | **Fully-loaded cost per learner-hour**, split human / AI / platform | Makes §3.2 visible: if AI is <1% and L is flat, say so |
| 7 | **Tutor utilisation** — paid hours ÷ available hours | The silent margin killer in every marketplace; disclosed by nobody |
| 8 | **Gross margin ex-capitalised-software**, with the software line shown separately | Nerdy's FY2025 margin moved 4.3 points on a software write-off. Never let a capitalisation policy move a margin the board is judging |

**Tier 3 — the go-to-market reality**

| # | Metric | Why |
|---|---|---|
| 9 | **Days from first contact to signed contract**, by channel, as a full distribution not a mean | Procurement length is the #1 killer of B2B2C edtech cash plans (§2) |
| 10 | **Gross and net logo retention at the *contract* level**, and % of ARR on contracts ≤12 months | Because "generally short-term (one year or less)" is what the audited comparable discloses |
| 11 | **Share of revenue from expiring public programmes** | ESSER's successors will expire too. Nerdy disclosed a $7.44M state programme that did not recur |
| 12 | **Procurement-gate pass rate and time** — SOC 2, state DPA, VPAT/WCAG, per deal | These are the real barriers to entry; if they are also *your* barriers, they are not a moat |

**Tier 4 — safety and conformance (binary, not trending)**

| # | Metric | Why |
|---|---|---|
| 13 | **Harmful-content incidents** (count, not rate) and time-to-human-review | Eedi's audit found 0/3,617. That is the bar |
| 14 | **Factual-error rate on audited sample**, with sample size | Eedi: 5/3,617 = 0.1%. Any company reporting a rate without an n is reporting nothing |
| 15 | **Human-override rate and override *reasons*, taxonomised** | Eedi's edit taxonomy (44.3% pacing, 19.5% tone) is worth more than the acceptance rate |
| 16 | **Accessibility conformance status** against WCAG 2.1 AA, with the ACR date | A compliance date is a cliff, not a curve (§8.2) |

**Tier 5 — one metric the board should demand that no company publishes**

| # | Metric | Why |
|---|---|---|
| 17 | **The counterfactual arm.** % of learners in an ongoing holdout or stepped-wedge comparison against (a) no product, and (b) **plain ChatGPT** | Fütterer et al. is the reason. If the product has never been compared to a free chatbot, the board is funding an untested premium |

> **Adoption rule the board should write into the operating agreement:** *no metric
> enters an objective, a bonus plan, or an investor update until it has been run through
> the Null-Learner Test in writing, with the result recorded.* This costs nothing and
> would have prevented most of the failures in §4's graveyard, every one of which
> succeeded at the thing it measured.

---

## 8. What kills this company

An honest risk register, ordered by probability × severity, with the evidence attached
and — where possible — the leading indicator that would tell a board it is happening.

### 8.1 Regulatory shock — *severity extreme, probability moderate, warning time short*

**The precedent, audited.** China's July 2021 "double reduction" policy removed **62% of
Gaotu Techedu's revenue in twelve months** (CNY 6,561.7M → 2,498.2M), and the company is
still loss-making at the operating line in 2025 `FILING`. Tutoring is a politically
salient service delivered to children. It has been regulated to near-destruction once in
living memory, in the world's largest market for it, with roughly no notice.

**The live European deadlines** (`VERIFIED` from EUR-Lex, `INTERNAL-PRIOR` E3 §5 —
retrieved and quoted there against the primary text):

| Instrument | Date | What it does |
|---|---|---|
| **AI Act Article 50** transparency | **2 August 2026** — four days from this report | Chatbot-disclosure and synthetic-content marking. **Not** carved out by the Digital Omnibus; 50(1)–(6) untouched. For a conversational tutor in the EU this, not Annex III, is the live deadline |
| Article 111(4) relief | 2 December 2026 | Only for systems **already placed on the market before 2 Aug 2026**, and only for Art. 50(2) |
| **Annex III(3) education high-risk** | **2 December 2027** (was 2 Aug 2026) | Deferred by **Regulation (EU) 2026/1744** (Digital Omnibus on AI), in force 27 July 2026. Recital 40 gives the reason: delayed standards and national authorities. **Annex III point 3 itself is unamended — only the date moved** |
| Chapter III Section 5 (Arts. 40–49) | Apparently **2 August 2026** | `INFERENCE`: not in the carve-out list, so it appears to fall under the unamended general date. Looks like a drafting artefact. Wants a lawyer |
| Article 99 penalties | — | Fine ceilings apply |

**The commercial read of the deferral, which is not the obvious one.** Sixteen extra
months is not sixteen months of relief; it is sixteen months in which a competitor who
built for the original date holds a conformance asset nobody is checking yet, and it
compresses the eventual compliance scramble into a single quarter for everyone who
waited. It also means **the deadline can move again, in either direction** — the whole
episode is evidence that this regime's dates are political variables, not planning
constants.

**United States**: California SB 243 (companion chatbots) is enacted with **no education
carve-out** `VERIFIED`; the US Department of Education's AI priority (91 FR 18774,
effective 13 May 2026) is a **grant priority, not a vendor mandate**, and ED explicitly
**declined** to impose federal parental-consent requirements, pushing them to states
`VERIFIED`. That is a fragmentation risk, not a relief: fifty jurisdictions, thirty-eight
of which adopted around 100 AI measures in 2025 alone.

**Leading indicator for a board:** a rising count of state-specific contract riders per
deal, and legal spend per new district as a share of first-year contract value.

### 8.2 Efficacy-evidence risk — *severity high, probability high, and it is the risk this corpus is best placed to price*

The market currently does not require efficacy evidence. That is the risk, in both
directions.

- **If it never requires it**, the product competes on brand and distribution against
  free frontier chatbots, and §5 says most of those moats are weak.
- **If it starts requiring it** — via a state procurement rule, an ESSA-tier
  requirement, an FTC accuracy action, or a single well-publicised independent
  evaluation — a company with no measured outcome has no answer, and the answers
  available in the literature are uncomfortable: the strongest AI-tutoring result
  against a human tutor is **+5.5 p.p. transfer with a credible interval spanning zero,
  n=165**; the strongest human-tutoring meta-analytic pooled effect is **0.288 SD**; and
  the most reproducible finding in the field is that **proximal gains do not become
  distal gains** (Tutor CoPilot +4 p.p. exit ticket, **null on the end-of-year state
  test**). `MEASURED-RCT` / `MEASURED-META`.

**The specific landmine:** the FTC's *"Policy Statement Concerning the Suppression of
Accuracy in Artificial Intelligence Systems,"* published 7 July 2026. Retrieved as a
Federal Register listing only; **text not fetched, content `UNVERIFIED`** (E3 §5.4).
Flagged because an FTC accuracy policy statement three weeks old plausibly reaches
tutoring-product accuracy claims, and this section will not speculate about text it has
not read.

**Leading indicator:** the proximal-to-distal ratio in §7.2 metric #3. If it is drifting
above 2, the company is training its own metric and an independent evaluation will say so.

### 8.3 Procurement cycle length and the public-funding cliff — *severity high, probability high, already happening*

This is the risk with the most audited evidence behind it, and it is the one most
commonly modelled away.

- **"Contracts with Institutions are generally short-term in duration (one year or
  less)"** — Nerdy 10-K FY2025 `FILING`. Annual re-competition, every year, forever.
- **Institutional revenue −22% in FY2025**, and a **$7.44M state-funded programme "did
  not recur"** in Consumer revenue `FILING`. That is the post-ESSER contraction
  arriving in an audited income statement.
- **Zearn's Form 990** shows the same shape from the nonprofit side: expenses tripled
  from $13.46M (FY2021) to $40.53M (FY2023) while revenue plateaued at ~$45M `FILING`.
- Nerdy's own risk factor names the mechanism, verbatim: *"Our ability to generate
  revenue from Institutions such as schools and school districts may be adversely
  affected by decreased government funding of education… the government appropriations
  process is often slow and unpredictable."*

**The modelling error to avoid:** treating a district win as ARR. It is a one-year
contract that must be re-won inside a budget cycle whose timing you do not control, in a
market where the money that funded the category has expired.

**Leading indicator:** share of ARR on contracts of ≤12 months (§7.2 metric #10) and
share of revenue from expiring public programmes (metric #11).

### 8.4 Frontier-model commoditisation — *severity high, probability high, timing unknown*

The mechanism is not that a lab launches a tutoring product. It is that the free general
assistant becomes good enough that the incremental value of the vertical product falls
below its price.

Evidence that this is already in progress: **Chegg**, whose 10-K names it explicitly —
*"students see generative AI products like ChatGPT and others as strong alternatives to
vertically specialized solutions for education such as Chegg"* — alongside a **−39%**
revenue year and a **56% workforce reduction** `FILING`.

And the second mechanism, which Chegg's filing shows in the same sentence and which is
worse: **the distribution channel and the substitute can be the same company.** Google's
AI Overviews reduced Chegg's traffic while Google's models supplied the substitute.
Chegg has sued over it. `FILING`.

The human-in-the-loop model has partial protection here — a chatbot does not replace a
human tutor for a parent who wants a human — but §3 shows the protection is bought with
a 10–14 point gross-margin penalty. **The company is paying for its moat in margin, and
the board should see that trade priced explicitly.**

**Leading indicator:** the share of learner questions where the human's edit to the AI
draft is materially substantive. If that number falls toward zero, the human is a
liability line, not a differentiator. Eedi's taxonomy is the template: 44.3% of edits
were pacing, 19.5% persona/tone — *neither of which is subject-matter expertise.*

### 8.5 The counterfactual finding — *severity high, probability moderate, and it is specific*

**Fütterer et al. 2026** (*Educational Psychology Review*,
doi:10.1007/s10648-026-10133-8, n=371, Grades 7–9) randomised two pedagogically
scaffolded GenAI conditions against **plain ChatGPT** and found, verbatim: *"no
statistically significant advantages of either intervention over the control condition
were found for effort, domain-specific knowledge, or elaboration-based strategy use."*
`MEASURED-RCT`.

**This is the specific result that kills a "our pedagogy is the product" thesis**,
because the control arm is the free alternative every customer already has. It does not
say AI fails in classrooms — it says a designed scaffold bought nothing over an
undesigned chatbot on tested knowledge, in that implementation, with a teacher in the
room.

Read it with the other two anchors, as the corpus does (`INFERENCE`, E3 §7.3): Bastani
et al. showed unguarded AI produces **−17%** after removal and a guardrailed prompt
"largely mitigated" it; DeepMind's Sierra Leone trial showed **+0.258 SD** (unadjusted
+0.216, n.s.) where the counterfactual was very bad. The consistent reading is that
**the pedagogical layer's main job is removing harm, and its marginal benefit scales
with how bad the alternative was.** In a US or UK market where the alternative is a
competent free chatbot and a teacher, that marginal benefit is small.

### 8.6 Incumbent bundling — *severity moderate-high, probability high*

Pearson at **£3,577M revenue and 52.0% gross margin** `FILING`, Stride at **$2.41B**,
and the SIS/LMS layer (PowerSchool, Instructure — both now private-equity owned) each
already hold the district relationship, the rostering integration, the data-privacy
agreement and the procurement vehicle. Adding a tutoring or AI-assistant module costs
them a fraction of what customer acquisition costs a startup, and it arrives inside a
contract that is already signed. The consolidation pattern is visible in filings:
Coursera–Udemy (0.800 exchange ratio, signed 2025-12-17) `FILING`; Udacity into
Accenture; Riiid into Socra AI `OBSERVED`.

**The pattern worth naming, from E3 §3.2:** *the research identity is the first thing
discarded in a consolidation.* Riiid published the benchmark dataset the whole
knowledge-tracing field still uses, and its successor's website does not mention it.
Sector research capacity is not conserved through M&A — which means the evidence base
this company needs will not be built by the incumbents.

### 8.7 The four risks that are *not* on this list, and why

| Non-risk | Why it is not the threat it is sold as |
|---|---|
| **Rising inference costs** | AI is 0.43% of delivered cost (§3.2). A 10× price *increase* costs ~4 margin points |
| **Model provider deprecating an API** | Real operational nuisance; Gemma 4 ships Apache-2.0 and ungated, so a self-hosted fallback is legally and technically available (`OBSERVED`, E3 §1.3) |
| **Competitors with better prompts** | Prompt architecture is published (Eedi Appendix D.1) and pedagogical scaffolds did not beat plain ChatGPT (§8.5) |
| **Running out of learning data** | The field's richest corpora are publicly released by their own owners (§5.1) |

---

## 9. Negative results and documented failures

The section standard requires ≥4. There are ten.

| # | Negative result | Evidence | Label |
|---|---|---|---|
| N1 | **The AI-native rebuild coincided with a 9.5-point gross-margin fall.** Nerdy FY2025: 67.5% → 58.0%; expert costs +$5.24M on revenue −$11.24M; $7.76M of capitalised software abandoned. | Form 10-K, filed 2026-02-26 | `FILING` |
| N2 | **The measured leverage from AI drafting is +16.4%, and it comes from a 6-tutor role-play, not the trial.** Session duration got 31% *worse*. | arXiv:2512.23633 App. H | `DEMO` |
| N3 | **The trial that produced the 74.4% figure could not measure efficiency at all.** Verbatim: *"precludes a rigorous measurement of throughput or efficiency."* | arXiv:2512.23633 §5 | `MEASURED-RCT` (authors' own limitation) |
| N4 | **The cost saving in that appendix is denominated in a tutoring marketplace's blog post** (£35.29/hr, ref [43] → tutorful.co.uk). | arXiv:2512.23633 ref list | `VENDOR` inside a `MEASURED-RCT` paper |
| N5 | **Saga's 53% cost reduction was a public subsidy plus a halving of tutor time, and the efficacy was never re-measured at the cheaper ratio.** $3,800 → $1,800 via a $15,000/fellow AmeriCorps subsidy and 2:1 → 4:1. | NBER w28531 fn.12 | `MEASURED-RCT` context |
| N6 | **Designed pedagogy did not beat plain ChatGPT.** n=371, null on domain knowledge, effort, elaboration strategy. | doi:10.1007/s10648-026-10133-8 | `MEASURED-RCT` |
| N7 | **Institutional tutoring revenue fell 22% and a $7.44M state programme did not recur** — the public-funding cliff, audited. | Nerdy 10-K FY2025 | `FILING` |
| N8 | **District contracts are "generally short-term in duration (one year or less)."** The switching-cost moat is contradicted by the audited comparable's own disclosure. | Nerdy 10-K FY2025 | `FILING` |
| N9 | **The proprietary-data moat is contradicted by the data holders' own behaviour** — Eedi and ASSISTments publish their corpora under CC-BY-NC-4.0. | Hugging Face dataset API, 2026-07-29 | `OBSERVED` |
| N10 | **A single regulation removed 62% of a tutoring company's revenue in one year**, with no return to operating profit five years on. | Gaotu Techedu 20-F | `FILING` |

---

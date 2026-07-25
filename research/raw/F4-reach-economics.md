---
title: "The Reach Frontier — Economics, Access, Language, and What Becomes Possible at Near-Zero Marginal Cost"
wave: F
date_researched: 2026-07-25
sources_count: 0
---

# The Reach Frontier

**Thesis of this section.** "No child, no teen, no adult left behind" is an engineering and
economics claim. Tested against the numbers, it splits cleanly in two:

1. **The compute half is already won, or will be within ~2 years.** Delivering an hour of
   personalised tutoring to every school-age child on earth, every school day, is
   arithmetically fundable *today* at small-model prices and will be fundable at
   frontier-model quality shortly. The global silicon required is under one frontier
   training cluster.
2. **The compute half was never the binding constraint.** Devices, bandwidth, electricity,
   language coverage, and above all adult presence dominate the cost structure and the
   effect sizes. As marginal inference cost → 0, 100% of the remaining problem is the part
   AI does not address.

The rest of this section is the arithmetic behind those two claims, and an honest accounting
of the prior literature — which is mostly a record of expensive failure.

---

## 1. The cost curve

### 1.1 Current per-token pricing (July 2026)

Frontier and mid-tier, per million tokens (USD):

| Model | Input | Cached input | Output | Source |
|---|---|---|---|---|
| Claude Opus 5 | $5.00 | ~$0.50 (0.1×) | $25.00 | Anthropic pricing |
| Claude Sonnet 5 | $3.00 | ~$0.30 | $15.00 | Anthropic pricing |
| Claude Haiku 4.5 | $1.00 | ~$0.10 | $5.00 | Anthropic pricing |
| gpt-5.6-sol | $5.00 | $0.50 | $30.00 | OpenAI pricing |
| gpt-5.6-luna | $1.00 | $0.10 | $6.00 | OpenAI pricing |
| gpt-5.4-nano | $0.20 | $0.02 | $1.25 | OpenAI pricing |
| Gemini 3.5 Flash | $1.50 | — | $9.00 | Google AI pricing |
| Gemini 3.5 Flash-Lite | $0.30 | $0.15 | $2.50 | Google AI pricing |
| Gemini 3.1 Flash-Lite | $0.25 | — | $1.50 | Google AI pricing |

Batch/asynchronous processing is **–50%** across all three vendors. Prompt caching reads cost
**~0.1×** input price (Anthropic), 0.1× (OpenAI), 0.5× (Groq). This matters enormously — see §1.3.

Small and open-weights models, hosted (OpenRouter marketplace, cheapest provider, n=345 models):

| Model | Input | Output |
|---|---|---|
| Llama 3.2 1B Instruct | $0.027 | $0.201 |
| Gemma 3 4B IT | $0.050 | $0.100 |
| Llama 3.1 8B Instruct | $0.050 | $0.080 |
| Gemma 3 12B IT | $0.050 | $0.150 |
| Microsoft Phi-4 (14B) | $0.070 | $0.140 |
| Qwen 2.5 7B Instruct | $0.040 | $0.100 |
| Gemma 3n E4B IT | $0.060 | $0.120 |
| Gemma 4 26B-A4B / 31B | **$0.00** | **$0.00** (free tier) |
| Ling 2.6 Flash (cheapest paid) | $0.010 | $0.030 |

**The spread between frontier and small-open is ~185× on input and ~310× on output.**
Eighteen models on OpenRouter are served at zero marginal price.

Speech, the other half of a tutoring session:

| Service | Price |
|---|---|
| Whisper Large v3 Turbo (Groq) | **$0.04 per hour of audio** (228× realtime) |
| Whisper Large v3 (Groq) | $0.111/hr audio |
| gpt-4o-transcribe | ~$0.006/minute (≈$0.36/hr) |
| Orpheus TTS (Groq) | $22.00 per 1M characters |
| Google/commodity standard TTS | ~$4 per 1M characters |
| On-device TTS (Piper, Kokoro) | $0.00 |
| Gemini 3.1 Flash Live, native audio | $0.005/min in, $0.018/min out |

### 1.2 The session model — what an hour of tutoring actually consists of

Assumptions, stated so they can be attacked:

- 60-minute session, **120 conversational turns** (one exchange per 30 seconds)
- Tutor utterance 60 words → **78 output tokens** (1.3 tokens/word)
- Learner utterance 25 words → **33 input tokens**
- System prompt + curriculum + learner model: **2,000 tokens**
- **10 images** over the hour (learner photographs a worksheet) at 1,500 tokens each

Derived:

```
output tokens per hour       :      9,360
unique/cacheable tokens      :     30,260
naive input tokens per hour  :  1,925,370
context amplification factor :      63.6×
```

**This is the single most important engineering fact in the section.** Because the API is
stateless and the whole conversation is resent every turn, a session that *generates* 9,360
tokens *consumes* 1.93 million. Cost is dominated by re-reading context, not by producing
words. Naïve implementations pay 63× more than necessary.

### 1.3 What an hour costs today — the actual numbers

`LLM raw` = no caching. `LLM cached` = prompt caching (reads at 0.1×, writes at 1.25×).
Then three voice configurations added on top.

| Model | LLM raw | LLM cached | + premium voice | + standard voice | + on-device voice |
|---|---|---|---|---|---|
| Claude Opus 5 (frontier) | $9.861 | $1.371 | $2.282 | $1.569 | **$1.411** |
| Claude Sonnet 5 | $5.917 | $0.822 | $1.734 | $1.021 | $0.862 |
| Gemini 3.5 Flash-Lite | $0.601 | $0.092 | $1.003 | $0.290 | $0.132 |
| Gemini 3.1 Flash-Lite | $0.495 | $0.071 | $0.982 | $0.269 | $0.111 |
| Phi-4 14B (hosted) | $0.136 | $0.017 | $0.928 | $0.216 | $0.057 |
| Gemma 3 4B (hosted) | $0.097 | $0.012 | $0.924 | $0.211 | **$0.052** |
| Llama 3.1 8B (hosted) | $0.097 | $0.012 | $0.923 | $0.211 | $0.052 |
| Llama 3.2 1B (hosted) | $0.054 | $0.008 | $0.919 | $0.206 | $0.048 |

Voice add-ons per hour: ASR $0.040; premium TTS $0.871; standard TTS $0.158; on-device TTS $0.
Native end-to-end audio (Gemini Live) is **$0.750/hour**, competitive with a cascade using
premium TTS but ~14× the cost of a cascade with on-device speech.

**Three findings worth stating plainly:**

- **Prompt caching is worth more than model choice within a tier.** Caching alone takes
  frontier tutoring from $9.86 to $1.37/hour — a 7.2× saving, larger than the gap between
  Opus and Sonnet.
- **Below the frontier tier, text-to-speech becomes the dominant cost.** At Gemma 3 4B
  prices, inference is $0.012/hour and premium TTS is $0.871/hour — **speech synthesis is
  73× the cost of the intelligence.** Anyone optimising the model while paying $22/M
  characters for voice is optimising the wrong term.
- **The cheapest credible full-voice tutoring hour today is ~$0.05**, using a hosted 4–8B
  open model with on-device ASR/TTS.

### 1.4 At 1/10th and 1/100th

| Configuration | Today | ÷10 | ÷100 |
|---|---|---|---|
| Frontier, cached, on-device voice | $1.411 | $0.141 | $0.014 |
| Cheap-frontier tier | $0.111 | $0.011 | $0.0011 |
| Small open model | $0.052 | $0.005 | $0.0005 |

**How long is that?** Epoch AI's price-trend analysis measured the cost of reaching a fixed
capability level across six benchmarks (MMLU, GPQA Diamond, MATH-500, MATH Level 5,
HumanEval, Chatbot Arena ELO) over roughly three years. Prices for constant capability fell
**9× to 900× per year, median 50×/year**; restricting to post-January-2024 data raises the
median to **200×/year**. GPT-4-level performance on PhD-level science questions got 40×
cheaper per year.

Applying the observed rates:

| Decline rate | 10× cheaper in | 100× cheaper in |
|---|---|---|
| Slowest observed (9×/yr) | 12.6 months | 25.2 months |
| Median (50×/yr) | 7.1 months | 14.1 months |
| Post-2024 median (200×/yr) | 5.2 months | 10.4 months |

So the "1/100th" column is not a distant scenario. At the slowest rate ever observed it is
about **two years away**; at the median, **fourteen months**. This is the strongest single
argument for the survey's ambition — and, as §2 shows, also the reason the ambition will
still fail if nothing else changes.

### 1.5 At what price does 1:1 tutoring for every child become fundable?

Annual global bill, **180 hours per child per year** (one hour every school day), $ billions:

| Price/hour | All school-age (1.9B) | LMIC children (1.5B) | LIC children (300M) | Out-of-school (250M) |
|---|---|---|---|---|
| $9.86 (frontier, uncached) | 3,372 | 2,662 | 532 | 444 |
| $2.28 (frontier + premium voice) | 780 | 616 | 123 | 103 |
| $1.41 (frontier + on-device voice) | 482 | 381 | 76 | 64 |
| $0.27 (cheap tier + std voice) | 92 | 73 | 15 | 12 |
| **$0.052 (small open model)** | **17.8** | **14.0** | **2.8** | **2.3** |
| $0.001 (fully on-device) | 0.3 | 0.3 | 0.1 | 0.04 |

Inverting — the price that fits a given budget:

| Budget | Cohort & dose | Required price/hour |
|---|---|---|
| UNESCO SDG4 financing gap (~$100B/yr) | All children, 180 h | $0.29 |
| UNESCO SDG4 gap | LMIC children, 180 h | $0.37 |
| Total global aid to education (~$15B/yr) | All children, 180 h | $0.044 |
| Total global aid to education | LMIC children, 180 h | $0.056 |
| 1% of global education spending (~$50B) | All children, 180 h | $0.146 |
| 10% of LIC education budgets (~$3B) | LIC children, 180 h | $0.056 |

**The answer to the section's central question: ~$0.05 per hour.**

At $0.05/hour, universal daily 1:1 AI tutoring for every child in the developing world costs
about **$14 billion a year — roughly the size of existing global aid to education**, and it
is deliverable within the discretionary ICT fraction of existing national education budgets.

Per child per year at 180 hours:

| Configuration | $/child/year |
|---|---|
| Frontier, uncached | $1,774.80 |
| Frontier, cached + premium voice | $410.40 |
| Frontier, cached + on-device voice | $253.80 |
| Cheap tier + standard voice | $48.60 |
| **Small open model + on-device voice** | **$9.36** |
| Fully on-device | $0.18 |

**The benchmark that matters.** Government spending per primary pupil in low-income
countries runs **8–13% of GDP per capita** (World Bank SE.XPD.PRIM.PC.ZS: Malawi 8.2%,
Niger 13.3%), against LIC GDP per capita of **$809** (World Bank, 2024) — i.e. roughly
**$50–95 per pupil per year, total, for everything**: teacher salaries, buildings, books,
administration.

A 10% ICT allocation is $5–10/child/year. **The $9.36 small-model configuration fits inside
it today.** The $253.80 frontier configuration is 3–5× the *entire* per-pupil budget and will
not fit until the price falls ~30×, i.e. roughly 12–18 months at observed rates.

**Verdict on the cost curve: the economics claim survives contact with the arithmetic.**
Universal 1:1 tutoring is affordable now at small-model quality and affordable at frontier
quality within about two years. Every remaining objection in this section is about something
other than the price of tokens.

---

## 2. The costs that don't fall — total cost of ownership

Token prices are collapsing. Nothing else in the stack is. Full TCO per child per year at
180 hours (bandwidth priced at $3/GB, typical Sub-Saharan retail; devices amortised over 3
years):

| Scenario | Inference | Bandwidth | Device | Power | **Total** | Inference as % |
|---|---|---|---|---|---|---|
| A. Frontier cloud, voice, 1:1 device | $253.80 | $7.77 | $20.00 | $0.20 | **$281.77** | 90.1% |
| B. Cheap cloud model, voice, 1:1 | $48.60 | $7.77 | $20.00 | $0.20 | **$76.57** | 63.5% |
| C. Small open model, text, shared 1:5 | $2.16 | $0.03 | $4.00 | $0.05 | **$6.24** | 34.6% |
| D. On-device 4B, offline, 1:1 | $0.00 | $0.00 | $26.67 | $0.90 | **$27.57** | 0% |
| E. On-device, shared 1:5 school tablet | $0.00 | $0.00 | $5.33 | $0.20 | **$5.53** | 0% |
| F. SMS/IVR on existing feature phone | $0.20 | $1.50 | $0.00 | $0.05 | **$1.75** | 11.4% |

**The inversion.** In scenario A intelligence is 90% of cost; in scenario C it is 35%; in
D and E it is zero. **As inference approaches free, the problem becomes entirely a hardware
and connectivity problem** — and hardware and connectivity are exactly what forty years of
ICT4D failed to solve (§4).

### 2.1 Bandwidth is not free, and voice is expensive to move

| Channel | Per hour | Per child-year (180 h) |
|---|---|---|
| Opus voice, both directions (32 kbps) | 14.40 MB | 2.59 GB |
| Opus voice, learner only (16 kbps) | 7.20 MB | 1.30 GB |
| Low-rate codec (Lyra/Codec2, 6 kbps) | 2.70 MB | 0.49 GB |
| Text-only chat | 0.48 MB | 0.086 GB |
| SMS/IVR store-and-forward | ~0.02 MB | negligible |

At $3/GB, streamed voice costs **$7.78/child/year in data alone** — comparable to the entire
inference bill for a small model ($9.36), and 150× the cost of text-only ($0.26). **A voice
tutor delivered over a metered mobile connection spends nearly as much moving the audio as
thinking about it.** This is a decisive argument for on-device speech (ASR and TTS local,
only text over the wire) or for full on-device inference.

### 2.2 The supply side — how much silicon universal tutoring actually needs

Prefill is compute-bound; decode is memory-bandwidth-bound (batch 256). Against
3.42 × 10¹¹ global learner-hours/year (1.9B children × 180 h), in H100-equivalents:

| Model class | GPU-s per learner-hour | H100s needed | Power | TWh/yr | % of global DC electricity |
|---|---|---|---|---|---|
| 1B (on-device class) | 0.158 | 1,717 | 1.4 MW | 0.013 | 0.003% |
| 4B (Gemma 3 4B) | 0.634 | 6,868 | 5.8 MW | 0.051 | 0.012% |
| 8B (Llama 3.1 8B) | 1.268 | 13,735 | 11.5 MW | 0.101 | 0.024% |
| 30B MoE (~3B active) | 0.492 | 5,328 | 4.5 MW | 0.039 | 0.009% |
| **Frontier MoE (~50B active)** | **8.195** | **88,804** | **74.6 MW** | **0.654** | **0.158%** |

(Denominator: ~415 TWh/yr global data-centre electricity, IEA 2024.)

**~89,000 H100s — less than one current frontier training cluster — would serve every
school-age child on earth an hour of frontier-quality tutoring every school day, at 0.16% of
today's data-centre electricity.** At 4B-model quality it is under 7,000 GPUs and 0.012%.

Compute supply is *not* the constraint. Not remotely. Meanwhile:

- Devices at 1:1 — **1.9 billion units**, $38.0B/year at $60/device on a 3-year life
- Devices at 1:5 shared — 380 million units, **$7.6B/year**

**The silicon that runs the tutor costs ~$0.1–1B/year to operate. The silicon the child
holds costs $7.6–38B/year to keep in the field — a ratio of roughly 30–300:1 against the
thing that gets all the attention.**

---

## 3. Language — the cost model is regressive by construction

Tokenisation penalties multiply *every* number above. Non-Latin and low-resource scripts
fragment into far more tokens per word than English (Ahia et al., EMNLP 2023, "Do All
Languages Cost the Same?"; Petrov et al., NeurIPS 2023, "Language Model Tokenizers Introduce
Unfairness Between Languages"). Applying published multipliers to the $/hour figures:

| Language | × tokens vs English | Frontier $/h | Small model $/h | Small model $/yr |
|---|---|---|---|---|
| English | 1.0 | $1.41 | $0.052 | $9.36 |
| Spanish / French | 1.2 | $1.69 | $0.062 | $11.23 |
| Hindi (Devanagari) | 2.5 | $3.53 | $0.130 | $23.40 |
| Yoruba | 2.5 | $3.53 | $0.130 | $23.40 |
| Bengali | 3.0 | $4.23 | $0.156 | $28.08 |
| Telugu | 4.0 | $5.64 | $0.208 | $37.44 |
| Amharic (Ge'ez) | 5.0 | $7.05 | $0.260 | $46.80 |
| Burmese | 9.0 | $12.69 | $0.468 | $84.24 |
| Shan (worst observed) | 15.0 | $21.15 | $0.780 | $140.40 |

**The learner who most needs a free tutor pays the most per sentence.** A Telugu or Amharic
speaker pays 4–5× an English speaker for identical pedagogy; a Burmese speaker up to 9×. The
penalty correlates inversely with how much of the language was in the tokeniser's training
mix — it is regressive by construction, and it compounds with the quality gap (a worse tutor,
charged at a higher rate).

It also consumes the context window: a 1M-token window holds ~1M English tokens of curriculum
but only the equivalent of ~200–250k words in Amharic.

*[Measured benchmark performance by language — Global-MMLU, Belebele, IrokoBench/AfriMMLU,
MILU, Whisper/MMS WER — pending from the language research stream; see §6.]*

---

---

## 6. Evidence from deployed interventions

### 6.1 The two studies carrying the entire "AI tutoring works in poor countries" claim

**Nigeria — De Simone, Tiberti, Barron Rodriguez, Manolio, Mosuro & Dikoru (2025),
*From Chalkboards to Chatbots*, World Bank Policy Research WP 11125,
doi:10.1596/1813-9450-11125.** Nine public schools, Benin City, Edo State. Microsoft Copilot
(GPT-4) in school computer labs, twelve 90-minute after-school sessions over six weeks,
teacher-guided with prompt scaffolds. ITT effects: **English 0.238 SD (SE 0.068)**, total
weighted 0.31 SD, third-term curricular English exam 0.21 SD. Cost **$48/pupil** for the
pilot ($9 marginal; $124/pupil projected for a four-quarter version).

Caveats that matter:
- **Opt-in**: only 52% of eligible students entered the randomisation pool; no demographic
  data on non-participants.
- **Differential attrition**: 36% treatment vs 50% control failed to complete endline —
  statistically significant, and the analysed sample is 57% of those assigned. Lee bounds and
  IPW are applied and effects survive, which is the right response, but this is the study's
  largest threat.
- **Heterogeneity is regressive**: larger effects for higher-baseline and higher-SES students.
- **Not an AI-alone intervention**: teachers ran the sessions; students got extra
  instructional time, a computer lab, and structured curriculum-aligned activity. The
  counterfactual is *nothing*, not *the same 18 hours without a chatbot*. The active
  ingredient is unidentified.
- **The "nearly two years of learning in six weeks" headline is a units conversion, not a
  finding.** It is an Evans & Yuan (2019) EYOS transformation of 0.238 SD. It is a statement
  about how little a business-as-usual Nigerian school year adds, not how much the chatbot
  taught. The year-long extrapolation (1.2–2.23 SD) linearly projects a per-day dose-response
  estimated over ≤12 sessions out to 36 weeks and should not be quoted as a result.
- **No replication.** A full-text search of the World Bank corpus returns this paper and
  nothing else.

**Ghana — Henkel, Horne-Robinson, Kozhakhmetova & Lee (2024), *Effective and Scalable Math
Support: Experimental Evidence on the Impact of an AI-Math Tutor in Ghana*, AIED 2024,
doi:10.1007/978-3-031-64315-6_34 (arXiv:2402.09809).** Rori, a WhatsApp math tutor. Eleven
Rising Academies schools, **randomised at school level** (5T/6C), grades 3–8, two 30-minute
sessions/week, Feb–Aug 2023. 477 of 637 completed both tests. **Cohen's d = 0.36.** Marginal
cost **~$5/student/year**.

This is the most-cited LMIC AI-tutoring number and the **weakest-identified study of the set**:
- Assignment is at school level with **11 clusters**, but inference is an independent-samples
  t-test on 477 students — standard errors are not clustered, no school fixed effects. The
  reported p<0.001 is not credible as stated; the honest interval around 0.36 is very wide.
- Same 35-item instrument at all grades and both timepoints; authors concede **ceiling
  effects**; retest effects likely.
- 25% attrition, with dropouts substantially lower-scoring at baseline.
- Rising Academies **built the product, runs the schools, and authored the evaluation**. No
  pre-registration mentioned; authors call it "a preliminary evaluation."
- The $5 is *marginal* (API + device + 3G), excluding devices, content development, and
  teacher supervision — not comparable to Nigeria's all-in $48.

### 6.2 The near-empty evidence base

Searches across Crossref, ERIC, Europe PMC and the World Bank corpus produced **no rigorous
outcome evaluation** of Khanmigo (anywhere, including the US), ConveGenius/SwiftChat, Kidato,
M-Shule, Somanasi, Eneza Education, Pratham LLM pilots, or Central Square Foundation AI work.
Rocket Learning's public impact page carries testimonials only — no control group, N, effect
size, or cost. Youth Impact lists no AI/LLM programme with measured results.

**Two studies, neither replicated, one of them badly identified, is the entire base.**

### 6.3 The most rigorous trial finds zero

**Bastani, Bastani, Sungu, Ge, Kabakcı & Mariman (2025), *Generative AI without guardrails
can harm learning: Evidence from high school mathematics*, PNAS 122(26), e2422633122.**
~1,000 students, one Turkish high school, four 90-minute sessions, three arms.

| Arm | During assisted practice | On unassisted exam |
|---|---|---|
| GPT Base (no guardrails) | **+48%** | **−0.054 SD (SE 0.022), i.e. −17%** |
| GPT Tutor (guardrailed) | **+127%** | **−0.004 SD (SE 0.013) — a precise null** |

Two things are usually lost in citation. First, the harm comes from *unrestricted
answer-giving*, and a well-designed tutor removed it. Second, and less comfortably:
**the well-designed tutor also produced no detectable learning gain.** The best result in the
most careful negative-controlled AI-tutoring trial is "did no harm." (The 2025 PNAS
Correction, doi:10.1073/pnas.2518204122, is an author-affiliation fix only — no numbers
changed.)

For contrast, the strongest positive: **Kestin, Miller, Klales, Milbourne & Ponti (2025),
*AI tutoring outperforms in-class active learning*, Scientific Reports 15,
doi:10.1038/s41598-025-97652-6** — Harvard, 194 students, within-subject crossover, **0.63 SD**.
But: immediate researcher-designed multiple-choice post-test with **no delayed retention
measure**, two lessons, elite institution, expert-crafted prompts and bespoke instructional
video. An upper bound on a heavily engineered system, not on "students using ChatGPT."

### 6.4 The meta-analytic picture, including a retraction

- **VanLehn (2011)**, Educational Psychologist 46(4), doi:10.1080/00461520.2011.611369 —
  the field believed CAI/ITS/human tutoring were d = 0.3/1.0/2.0. Actual: **human tutoring
  0.79, ITS 0.76.** ITS essentially match human tutors, and **human tutors do not reach two
  sigma.**
- **Kulik & Fletcher (2016)**, RER 86(1), doi:10.3102/0034654315581420 — k=50, median 0.66 SD,
  but heavily dependent on local vs standardised outcome measures.
- **Steenbergen-Hu & Cooper (2013, 2014)** — college g = 0.32–0.37, ITS **less** effective
  than human tutoring; K-12 math "no negative and perhaps a small positive effect."
- **Liu, Zuo & Lu (2025)**, JCAL, doi:10.1111/jcal.70096 — k=37, g = 0.577 [0.395, 0.759].
  Its own moderators are the tell: largest effects at **samples of 21–40** and 5–10-week
  interventions. That is the signature of small-study bias.
- **⚠️ The headline LLM number has been retracted.** Wang & Fan (2025), *The effect of ChatGPT
  on students' learning performance…*, Humanities and Social Sciences Communications,
  doi:10.1057/s41599-025-04787-y, reported g = 0.867 across 51 studies and accumulated ~247
  citations. **Retracted 22 April 2026** (doi:10.1057/s41599-026-07310-z). Independently,
  **Bartoš, Martinková & Wagenmakers (2025)**, doi:10.31234/osf.io/8vs32_v1, show the effects
  "greatly diminish once publication bias is accounted for." **Anyone citing g ≈ 0.87 for LLM
  tutoring is citing a retracted paper.**
- **Bloom's two sigma has never been replicated.** Bloom (1984), doi:10.2307/1175554,
  dismantled by **von Hippel (2024), "Two-Sigma Tutoring: Separating Science Fiction from
  Science Fact," Education Next**: it rests on two dissertations, 3-week interventions,
  deliberately unfamiliar content, narrow researcher-made tests; the tutoring arm bundled
  mastery-learning retesting (roughly half the effect) and *replaced* rather than supplemented
  instruction. Cohen, Kulik & Kulik (1982): mean **0.33 SD** across 65 studies, 0.84 on local
  tests vs **0.27 on standardised tests**.
- **Human tutoring benchmark**: Nickow, Oreopoulos & Quan — the widely quoted 0.37 SD is the
  2020 working paper; the **published** version (AERJ 2023, doi:10.3102/00028312231208687)
  reports **0.288 SD (SE 0.029)**. Costs: Saga Education **$3,500–4,300/student/year**;
  US federally funded supplemental tutoring **$1,100–2,000/student** for **0.06 SD**.

### 6.5 What to expect at scale — the voltage drop

- **Muralidharan, Singh & Ganimian (2019)**, AER 109(4), doi:10.1257/aer.20171112 — Mindspark
  urban India, **0.37 SD math / 0.23 Hindi** over 4.5 months.
- **Muralidharan & Singh (2025)**, *Adapting for Scale*, NBER WP 34205 — same technology,
  adapted for scale, sample **20× larger**, **18 months**: **0.22 SD math / 0.20 Hindi**.
  Longer dose, bigger sample, smaller effect. This is the best-documented voltage drop in the
  technology-aided-instruction literature and the right prior for what happens to 0.31 and
  0.36 at scale.
- **Evans & Yuan (2022)**, EEPA, doi:10.3102/01623737221079646 — across 234 LMIC studies the
  **median RCT effect is 0.10 SD**, and effects are "larger and demonstrate higher variance
  for small-scale studies." Both AI studies above are small-scale.
- **Reich & Ruipérez-Valiente (2019)**, *The MOOC pivot*, Science 363(6423),
  doi:10.1126/science.aav7958 — six years of Harvard/MIT edX data: most learners never return
  after year one, growth concentrated in affluent countries, **completion rates did not
  improve over six years.** The closest well-measured analogue for unsupervised chatbot
  engagement over time — and the reason the Nigeria result matters *because* attendance was
  supervised (72% in a monitored lab), not despite it.

**No published measurement of week-by-week engagement decay in an LLM tutoring deployment
exists.** Rori's own evaluation names dosage–response and plateau as open questions. This is
a genuine hole.

### 6.6 Placing the measured points in the cost-effectiveness framework

Converting at ~0.30 SD per year of schooling (LAYS per $100; higher is better):

| Intervention | Cost/child/yr | d | LAYS per $100 |
|---|---|---|---|
| Ghana Rori (as claimed) | $5 | 0.36 | **24.00** |
| Ghana Rori (at Evans–Yuan median) | $5 | 0.10 | **6.67** |
| Botswana SMS + phone, human tutors | $13.50 | 0.12 | **2.96** |
| Nigeria Copilot, 6-week pilot as run | $48 | 0.238 | **1.65** |
| Mindspark urban | $100 | 0.37 | 1.23 |
| Mindspark at scale | $100 | 0.22 | 0.73 |
| Nigeria, projected 4-quarter version | $124 | 0.238 | 0.64 |
| Bastani GPT Tutor (guardrailed) | ~$50 | 0.00 | **0.00** |
| Saga human tutoring (US) | $3,900 | 0.26 | 0.02 |
| US supplemental private tutoring | $1,550 | 0.06 | 0.01 |

**Framework validation:** my conversion puts the Nigeria pilot at 1.65 LAYS/$100; the paper's
own reported range is **0.6–1.9**. The framework agrees with the primary source.

**The pattern is unambiguous and it is about cost, not about effect size.** The interventions
that win are the cheap ones. Rori wins not because 0.36 SD is large but because $5 is small.
Saga Education achieves a perfectly respectable 0.26 SD and scores 0.02 — a thousandth of
Rori — purely on price. **Buy AI tutoring for the cost, not the effect size.**

---

## 7. The uncomfortable counter-argument

### 7.1 The steelman

*Stated as strongly as it can be stated, because it is largely correct.*

**Premise 1 — Content availability has not been the binding constraint for decades.**
Every curriculum a child needs has been free on the open web since roughly 2010. Khan
Academy, Wikipedia, OpenStax, CK-12, and YouTube collectively solved "access to explanation"
years ago. Learning poverty nonetheless stands at roughly 70% of ten-year-olds in low- and
middle-income countries. If content were the constraint, that number would have moved. It
did not. AI does not add content; it adds *responsiveness* to content that was already free.
The burden of proof is on the claim that responsiveness is the missing ingredient, and that
burden has not been discharged.

**Premise 2 — The measured constraints are physiological, institutional, and custodial.**
A child who is stunted, anaemic, or hungry cannot consolidate what a tutor teaches, however
patient the tutor. A child who is not in school is not in front of the device. A child in a
classroom whose teacher is absent has no one to enforce the routine that makes any
instructional technology work. A girl who is unsafe walking to the learning centre does not
arrive. These are the variables with the largest documented effects on learning outcomes in
low-income settings, and **an AI tutor moves none of them.** It does not deworm, feed,
enrol, supervise, or protect.

**Premise 3 — The ICT4D record is a forty-year controlled experiment in exactly this
hypothesis, and it failed.** Every prior wave — radio, television, PCs, one-laptop-per-child,
tablets, MOOCs — arrived with the same structure of argument: the marginal cost of
distributing instruction has collapsed, therefore the learning gap will close. Each time,
rigorous evaluation found effects near zero on learning outcomes. The interventions that
*did* work were the ones that changed what an adult did with a child's time. AI is a better
technology than any of these, but "better technology" was never the failed variable — the
theory of change was.

**Premise 4 — Cost-effectiveness arithmetic actively disfavours the sophisticated version.**
This is the counter-argument's sharpest edge, and it comes from this section's own numbers.
Converting to the sector's standard currency (Learning-Adjusted Years of Schooling per $100,
at ~0.30 SD per year of schooling):

| Configuration | Full TCO/child/yr | LAYS/$100 at d=0.10 | at d=0.15 | at d=0.20 | Verdict vs 3-LAYS bar |
|---|---|---|---|---|---|
| Frontier cloud, voice, 1:1 | $281.77 | 0.12 | 0.18 | 0.24 | **FAILS** (needs 2.54 SD) |
| Cheap cloud model, voice, 1:1 | $76.57 | 0.44 | 0.65 | 0.87 | FAILS (needs 0.69 SD) |
| On-device 4B, 1:1 | $27.57 | 1.21 | 1.81 | 2.42 | marginal (needs 0.25 SD) |
| Small open model, text, shared 1:5 | $6.24 | 5.34 | 8.01 | 10.68 | **BEATS** (needs 0.06 SD) |
| On-device, shared 1:5 school tablet | $5.53 | 6.03 | 9.04 | 12.06 | **BEATS** (needs 0.05 SD) |
| SMS/IVR on an existing phone | $1.75 | 19.05 | 28.57 | 38.10 | **BEATS** (needs 0.02 SD) |

The d range is not hypothetical: **Evans & Yuan (2022) put the median LMIC RCT effect at
0.10 SD**, Mindspark fell from 0.37 to **0.22** on scaling, and the most rigorous AI-tutoring
trial (Bastani et al.) found **0.00** for a guardrailed tutor. d = 0.10–0.20 is the honest
planning range; 0.30+ requires believing the two unreplicated LMIC studies survive scaling.

Benchmarks in the same units: structured pedagogy ~2–3 LAYS/$100; teaching-at-the-right-level
~3–15; information on returns to schooling ~20+; **providing hardware alone <0.3, frequently
indistinguishable from zero.**

The implication is uncomfortable for the field's enthusiasms. **Frontier 1:1 voice tutoring
would need an effect size of ~2.5 SD to be cost-competitive with interventions that already
exist.** Bloom's 2-sigma is the theoretical ceiling of individual human tutoring and has
never been replicated under controlled conditions. So the most desirable configuration is
the one the arithmetic most clearly rejects — while an SMS bot on a phone the family already
owns needs only 0.02 SD to be a best buy.

**Conclusion of the steelman:** AI learning is a solution to a problem that was already
solved, priced above interventions that already work, deployed into infrastructure that does
not exist, in languages it does not speak, for children who are not in the room.

### 7.2 Response

The steelman is right about roughly 80% of the claim, and the honest response concedes that
rather than fighting it.

**Concede Premise 1 entirely.** Content was never scarce. Any version of this survey's
ambition that rests on "access to knowledge" is making a claim that was falsified fifteen
years ago. The defensible claim is narrower and different in kind: what has been scarce is
**contingent adult attention** — someone who notices *this* child is stuck at *this* step and
responds. That has always been supply-constrained because it is human time, and it is the
first thing in history to become manufacturable. Whether manufactured attention substitutes
for human attention is an empirical question, not a rhetorical one, and it is the question
the field should actually be running.

**Concede Premise 2 almost entirely.** Nutrition, enrolment, attendance, teacher presence,
and safety dominate. AI addresses none directly. The correct posture is **complementarity,
not substitution**: AI is a multiplier on instructional time that already exists, not a
substitute for a child being fed, enrolled, and supervised. A multiplier on zero is zero.
This means AI tutoring should be evaluated and funded *alongside* the interventions that put
children in seats — never as an alternative to them, and never in a budget line that competes
with them.

**Concede Premise 3, with one specific and important qualification.** The ICT4D record is
damning and the burden of proof sits with AI. But the failures were not undifferentiated.
The interventions that failed were those that shipped *hardware and content* and expected
learning to follow. The ones that worked — computer-assisted learning that adapted to the
child's actual level, and teaching-at-the-right-level programmes — worked because they
solved **heterogeneity**: the problem that a classroom of forty children spans six years of
attainment and a single-paced lesson serves almost none of them. That is a genuinely
different mechanism from "here is a laptop," and it is the one mechanism in the historical
record that AI is unusually well suited to. The prior is not "technology fails"; the prior is
"technology fails unless it targets instruction to the individual child's level, in which
case it sometimes works." AI's claim should be staked on that narrower ground, where the
evidence actually points.

**Partially reject Premise 4 — and note that its own logic points somewhere useful.**
The cost-effectiveness arithmetic is correct but is an argument about *configuration*, not
about AI. It rejects frontier voice tutoring on 1:1 devices; it strongly *endorses* shared
on-device small models and SMS/IVR delivery, which reach 12–38 LAYS/$100 at modest effect
sizes and outperform most things in the Smart Buys catalogue. The arithmetic is not a verdict
against AI learning. It is a verdict against the version of AI learning that demos well —
and a direction: **build for the feature phone and the shared tablet first, not the
frontier-model voice agent.**

Two further points the steelman understates:

- **The price trend is real and fast.** At Epoch AI's observed 9×–900×/year decline, the
  frontier configuration that fails the cost-effectiveness test today passes it in roughly
  12–24 months without anyone doing anything. Several premises above are true statements
  about 2026 that will be false statements about 2028. That does not rescue the enrolment,
  nutrition, or safety arguments — those do not move with token prices — but it does retire
  the affordability objection specifically.
- **Marginal cost near zero changes who can build.** The historical failures were centrally
  procured national programmes with multi-year cycles. Open-weights small models and on-device
  inference mean a national curriculum in Telugu or Hausa can be adapted by a local team on a
  budget of thousands, not tens of millions. That is a structural change in *who* gets to
  build for a linguistic community — and it is the most plausible route to the language
  problem in §3.

**Net position.** Marginal cost approaching zero makes universal AI tutoring *affordable*.
It does not make it *effective*, and affordability was not the binding constraint. The
correct claim for this survey is bounded: **AI removes the cost barrier to personalised
instruction, which is real and was never removed before — and leaves every other barrier
standing.** "No child left behind" is unachievable by AI alone and was never an AI-shaped
problem. What is achievable, and worth stating precisely, is that for children who are
already in school, already fed, and already supervised, the marginal cost of giving each of
them instruction targeted to their actual level has fallen to roughly five cents an hour and
is still falling. That is a smaller claim than the ambition. It is also, unlike the ambition,
true.

---

<!-- SECTIONS 4-5 PENDING RESEARCH STREAMS -->



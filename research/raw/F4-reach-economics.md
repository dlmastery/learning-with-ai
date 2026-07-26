---
title: "The Reach Frontier — Economics, Access, Language, and What Becomes Possible at Near-Zero Marginal Cost"
wave: F
date_researched: 2026-07-25
sources_count: 0
---

> **⚠️ PARTIAL — agent terminated by session limit mid-write (2026-07-25).**
> Sections 1–3 are complete and self-corrected (the agent explicitly replaced its
> own §3 after finding its published-multiplier estimates "wrong in both
> directions"). Sections 4+ (offline/low-bandwidth design, ICT4D failure history,
> the digital divide, deployed-intervention RCTs, and the steelman counter-argument)
> were **never written**. Re-run required — see CLAUDE.md §8.


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

| Price/hour | All school-age (1.9B) | LMIC children (1.5B) | LIC children (300M) | Out-of-school (272.9M) |
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
| UNESCO SDG4 financing gap ($97B/yr, verified) | All children, 180 h | $0.29 |
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
| A. Frontier cloud, voice, 1:1 device | $253.80 | $7.77 | $60.00 | $0.20 | **$321.77** | 78.9% |
| B. Cheap cloud model, voice, 1:1 | $48.60 | $7.77 | $60.00 | $0.20 | **$116.57** | 41.7% |
| C. Small open model, text, shared 1:5 | $2.16 | $0.26 | $12.00 | $0.05 | **$14.47** | 14.9% |
| D. On-device 4B, offline, 1:1 | $0.00 | $0.00 | $60.00 | $0.54 | **$60.54** | 0% |
| E. On-device 4B, shared 1:5 | $0.00 | $0.00 | $12.00 | $0.20 | **$12.20** | 0% |
| F. SMS/IVR on existing feature phone | $0.20 | $1.50 | $0.00 | $0.05 | **$1.75** | 11.4% |

Device prices here are deliberately **not** the $60 figure often quoted. §4.3 shows that a
4 GB, $100 handset cannot comfortably host even a 1B model; a device that genuinely runs a
4B model needs 6–8 GB and costs ~$180. Power uses MELT's measured 0.16–0.21 mWh/token
(Laskaridis et al., MobiCom 2024) rather than an assumed wattage.

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

## 3. Language — measured, not claimed

### 3.1 How many languages are genuinely served?

**Joshi, Santy, Budhiraja, Bali & Choudhury (2020), "The State and Fate of Linguistic
Diversity and Inclusion in the NLP World", ACL 2020, arXiv:2004.09095** — the taxonomy that
frames everything:

| Class | Name | # Languages | Speakers | % of langs | Examples |
|---|---|---|---|---|---|
| 0 | The Left-Behinds | **2,191** | 1.0B | 88.17% | Dahalo, Warlpiri, Bora |
| 1 | The Scraping-Bys | 222 | 1.0B | 8.93% | Cherokee, Bhojpuri, Fijian |
| 2 | The Hopefuls | 19 | 300M | 0.76% | Zulu, Konkani, Lao |
| 3 | The Rising Stars | 28 | 1.1B | 1.13% | Indonesian, Ukrainian, Hebrew |
| 4 | The Underdogs | 18 | 1.6B | 0.72% | Russian, Vietnamese, Korean |
| 5 | **The Winners** | **7** | 2.5B | 0.28% | English, Spanish, German, Japanese, French |

**Seven languages out of ~7,000 are genuinely resourced. Roughly one billion people speak a
Class 0 language.** Speaker population does not buy resources: Telugu has ~96M speakers —
more than German — and Bhojpuri ~50M sits in Class 1.

### 3.2 The measured quality gap

**Belebele** (Bandarkar et al., ACL 2024, arXiv:2308.16884), 122 language variants, reading
comprehension, random baseline = 25:

GPT-3.5-turbo 5-shot: English **87.7**, average across all 122 variants **50.6**. Amharic
**28.7**, Hausa 32.2, Lao 30.0, Khmer 30.4, Burmese 30.4, Bengali 43.6. **Roughly 30 of the
122 variants score below 30% — statistically indistinguishable from guessing.**

**The finding that should reframe procurement:** fine-tuned **XLM-R-large (550M parameters)**
beats GPT-3.5 badly on low-resource languages — Amharic **60.7 vs 28.7**, Telugu 61.1 vs
40.6, Bengali 63.7 vs 43.6. **Scale does not substitute for balanced pretraining data.** A
half-billion-parameter model with the right data beats a frontier model with the wrong data,
by 30+ points.

**IrokoBench** (Adelani et al., 2024, arXiv:2406.03368), 17 African languages:

| Model | AfriMMLU English | AfriMMLU African avg |
|---|---|---|
| GPT-4o | 86.9 | **59.0** |
| Gemini-1.5-Pro | 82.6 | 58.3 |
| Claude Opus | 73.3 | **42.3** |
| Gemma-2-27B (best open) | 76.3 | **37.1** |
| Llama-3.1-70B | 73.5 | **34.0** |
| Aya-101 | 39.3 | 28.6 |

**AfriMGSM (grade-school math word problems) is the starkest table in the literature.**
GPT-4o: English 58.4, **African average 29.3**. Open models, in-language African average:
**Aya-101 4.2, Llama-3-8B 2.9, mT0-XXL 2.6, BLOOMZ-7B 4.1, Gemma-7B 4.6, Llama-3-70B 8.2.**

**For a Yoruba- or Amharic-speaking learner, open models cannot do grade-school arithmetic
word problems at all.** This is the single most damaging fact for the "cheap open model
tutors the world" thesis in §1, and it is not visible in any English benchmark.

**MILU** (Verma et al., arXiv:2411.02538), 11 Indic languages: GPT-4o 74%; **language-specific
fine-tuned models "perform only slightly better than random baselines."** A direct rebuke to
"just fine-tune a small local model."

**INCLUDE** (Romanou et al., arXiv:2411.19799) — 1,926 *real local exams*, not translations,
44 languages. GPT-4o overall 77.1, but Telugu **68.2**, Armenian **53.6** vs Italian 90.0 — a
~39-point spread. **Global-MMLU** (Singh et al., arXiv:2412.03304) adds the methodological
warning: **28% of MMLU questions require culturally-sensitive knowledge**, and of
geography-dependent questions **84.9% concern North America or Europe.** Translated benchmarks
systematically mismeasure.

### 3.3 Tokenization — direct measurement on parallel text

Measured on the **same 300 parallel FLORES-200 devtest sentences** per language (identical
information content), relative to English:

| Language | cl100k (**Llama-3 inherits this**) | o200k (GPT-4o family) | mT5/Aya | Sarvam-1 |
|---|---|---|---|---|
| English | 1.00 | 1.00 | 1.00 | 1.00 |
| Swahili | 1.94 | **1.50** | 1.26 | 2.05 |
| Hausa | 1.95 | 1.53 | 1.34 | 2.00 |
| Hindi | 4.70 | **1.58** | 1.58 | **1.12** |
| Bengali | 5.84 | **1.73** | 1.57 | 1.29 |
| Zulu | 2.17 | 1.73 | 1.42 | 2.20 |
| **Telugu** | **8.22** | **1.92** | 1.42 | **1.16** |
| Tamil | 7.55 | 2.02 | 1.29 | 1.16 |
| Yoruba | 2.90 | **2.15** | 2.01 | 3.80 |
| Burmese | 11.54 | 3.18 | 1.59 | 13.63 |
| Odia | 12.42 | 4.96 | — | — |
| **Amharic** | 7.53 | **5.74** | 1.72 | 6.61 |
| Tigrinya | 7.79 | 5.99 | — | — |
| Shan | 14.48 | 7.66 | — | — |
| Lao | 9.43 | **8.13** | — | — |
| Santali | 12.44 | **13.40** | — | — |

**Four findings that overturn the received wisdom:**

1. **The 2023-era "Telugu costs 5–8× more" claim is now wrong for GPT-4o-family models.**
   o200k dropped Telugu from 8.22× to **1.92×**, Bengali 5.84 → 1.73, Tamil 7.55 → 2.02.
   Anyone citing Ahia et al. (2023) figures for a 2026 frontier model is citing stale data.
2. **Ge'ez and South-East Asian scripts were left behind entirely.** Amharic 5.74×, Tigrinya
   5.99×, Lao 8.13×, and **Santali 13.40× — where o200k is *worse* than cl100k.** Amharic at
   **9.02 tokens/word means 0.57 characters per token** — sub-byte fragmentation.
3. **Latin-script African languages are cheaper than assumed** — Swahili 1.50×, Hausa 1.53×,
   Yoruba 2.15×. Yoruba's premium is *diacritic/tone-driven*, not script-driven.
4. **⚠️ The inversion that matters most for §1: open small models inherit the old penalty.**
   Llama-3's 128k vocabulary extends cl100k — its Telugu token counts are **byte-identical**
   to cl100k's.

### 3.4 The cheap-model penalty — a direct hit on §1's economics

| Language | Small-open (cl100k) $/hr | $/child/yr | Frontier (o200k) $/hr | Cheap-model disadvantage |
|---|---|---|---|---|
| English | $0.052 | $9.36 | $1.411 | — |
| Swahili | $0.101 | $18.16 | $2.12 | 1.3× |
| Hindi | $0.244 | $43.99 | $2.23 | **3.0×** |
| Bengali | $0.304 | $54.66 | $2.44 | **3.4×** |
| Yoruba | $0.151 | $27.14 | $3.03 | 1.3× |
| **Telugu** | **$0.427** | **$76.94** | $2.71 | **4.3×** |
| Amharic | $0.392 | $70.48 | $8.10 | 1.3× |
| Burmese | $0.600 | $108.01 | $4.49 | 3.6× |

**The small-model cost advantage collapses exactly where it is most needed.** In English the
open model is 27× cheaper than frontier; in Telugu only 6×. And the absolute number is the
problem: **$76.94/child/year for Telugu on a small open model is above the entire ~$75
per-pupil budget of a low-income country** (§5.6), against $9.36 for English.

**The learner who most needs a free tutor pays the most per sentence — and the regression is
worse on the cheap infrastructure than on the expensive kind.**

**But the fix is cheap and known.** Sarvam-1's 68k Indic-specialised vocabulary gets Telugu to
**1.16×** — better than *either* mainstream tokenizer. **For Indic learners, tokenizer choice
is worth more than model choice.** This is the strongest argument in the section for regional
model-building: a tokenizer is a few thousand dollars of work that permanently divides the
serving cost of a language by four.

**Context-window erosion** compounds it (o200k tokens/word):

| Language | tok/word | A 1M-token window holds |
|---|---|---|
| English | 1.25 | 800k words |
| Swahili | 1.90 | 526k words |
| Telugu | 3.05 | 328k words |
| Amharic | 9.02 | **111k words** |
| Lao | 31.68 | **32k words** |

**Ahia et al. (EMNLP 2023, arXiv:2305.13707)** document the capability consequence, not just
cost: on XLSum, Telugu and Amharic **"struggle to fit even one in-context example for the
majority of their test set,"** forcing zero-shot-only evaluation. **Few-shot prompting is a
privilege of Latin-script users.** Petrov et al. (NeurIPS 2023, arXiv:2305.15425) find up to
**15×** length differences for identical content.

### 3.5 Speech — the only interface for a non-literate learner

This matters more than text for exactly the populations in question: a learner who cannot read
has speech as the *sole* channel.

- **Whisper** (Radford et al., arXiv:2212.04356): 680,000 training hours, of which **only
  117,000 (~17%) cover 96 non-English languages.** Two laws from the paper: log-WER vs
  log-training-data correlation **r² = 0.83**, and **WER halves for every 16× increase in
  data.** Named negative outliers include **Telugu**.
- **MMS** (Pratap et al., arXiv:2305.13516) gives the best available comparison: on the **54
  FLEURS languages both systems cover, Whisper large-v2 = 44.3 WER; MMS = 18.7 WER** — a 58%
  relative reduction while supporting 11× more languages. MMS covers **1,107 languages for
  ASR and 1,107 for TTS**. Average CER 2.1 overall but **Africa 2.9** vs Europe 1.7.
- **The caveat that should temper enthusiasm:** MMS trains on ~32 hours/language of **readings
  of religious texts**. Register, vocabulary, and speaker demographics are all badly mismatched
  to classroom dialogue.

**A 44% WER is not a usable tutoring interface.** For Yoruba, Amharic, and most African
languages, no openly-benchmarked ASR system is at usable WER for open-domain educational
dialogue. Whisper (44.3) and MMS (18.7) bracket the state of the art on the *easier*
54-language subset. This directly undermines the on-device voice architectures §2 and §4
otherwise favour.

### 3.6 Translation as a bridge — asymmetric, and that asymmetry is usable

NLLB-200 MoE-54B official FLORES-200 metrics (exact published numbers, 40,602 directions):

| Direction | eng→X chrF++ | X→eng chrF++ |
|---|---|---|
| French | 69.7 | 68.4 |
| Hindi | 57.3 | 66.5 |
| Swahili | 58.6 | 66.1 |
| Telugu | 55.9 | 65.5 |
| Bengali | 50.0 | 62.2 |
| Amharic | **39.4** | 59.9 |
| Tigrinya | **25.8** | 50.4 |
| **Yoruba** | **25.5** | 46.3 |

Distribution over all 201 directions: mean chrF++ **eng→X 45.3 vs X→eng 56.8**. Directions
below chrF++ 40: **66 (33%) for eng→X** but only 20 (10%) for X→eng.

**The asymmetry is the design insight.** Translating *into* English works far better than out
of it. **A pipeline that ingests learner speech in Yoruba, reasons in English, and generates
back into Yoruba will fail on the last step** — eng→Yoruba chrF++ 25.5 despite 53M speakers,
worse than Luganda.

**Translate-then-prompt is nonetheless the strongest actionable result in the literature**,
and it rescues exactly the models §1 wants to use:

| Model, AfriMGSM | In-language | Translate-test |
|---|---|---|
| Llama-3-70B | 8.2 | **45.3** |
| Llama-3-8B | 2.9 | **27.0** |
| GPT-4o | 29.3 | 32.4 (negligible gain) |
| BLOOMZ / mT0 | 4.1 | 2.1 (*degrades*) |

**The benefit is inversely proportional to native multilingual competence** — which means the
cheap open models §1 depends on are precisely the ones translate-test rescues most. Confirmed
by MGSM (Shi et al., arXiv:2210.03057): Swahili gains **+16 points** (35.2 → 51.2) from
reasoning in English.

### 3.7 What is actually being built

| Effort | Size | Languages | Measured result |
|---|---|---|---|
| Aya 101 | 13B | 101 | AfriMMLU 28.6, AfriMGSM 4.2 — coverage was never functional |
| Aya 23 / Expanse | 8B/35B | **23** | Beats Aya-101 on the 23 kept |
| Sarvam-1 | **2B** | 10 Indic | **Telugu tokenizer fertility 1.16×**; FLORES en→Indic chrF++ 39.83 |
| IndicTrans2 | — | 22 Indian | BPCC 230M pairs; first covering all 22 |
| InkubaLM | **0.4B** | 5 African | Comparable to much larger models on AfriMMLU/AfriXNLI |
| MMS | — | 1,107 ASR/TTS | See §3.5 |
| NLLB-200 | 54B MoE | 202 | **"not released for production deployment"** |

**The defining trend is a breadth-to-depth retreat.** Cohere went **101 → 23 languages
deliberately**, framing it as "depth vs breadth." It worked — but **Aya 23's language list
contains zero sub-Saharan African languages** and only Hindi from South Asia. Given
Aya-101's actual scores (AfriMMLU 28.6), this is arguably honesty rather than retreat. The
practical effect is that **the frontier of *serving* low-resource languages is now held by
benchmark-builders (Masakhane, AI4Bharat) rather than model-builders.**

**What this means for §1's ambition:** the cost curve says a Telugu or Yoruba speaker can be
served for cents. The measurement says that at those prices, in those languages, the model
cannot currently do grade-school word problems, the ASR is at 44% WER, and generating fluent
pedagogical Yoruba is beyond the best open translation system. **"No child left behind" is
not, at present, a claim that survives translation.**

---

## 4. Small and on-device models — what actually runs on what

### 4.1 The capability ladder

Instruction-tuned benchmark scores from vendor model cards:

| Model | Params | MMLU / MMLU-Pro | GSM8K | MATH | HumanEval |
|---|---|---|---|---|---|
| Gemma 3 1B | 1B | 14.7 (Pro) | 62.8 | 48.0 | 41.5 |
| Llama 3.2 1B | 1B | 49.3 | 44.4 | 30.6 | — |
| Llama 3.2 3B | 3B | 63.4 | 77.7 | 48.0 | — |
| Gemma 3 4B | 4B | 43.6 (Pro) | 89.2 | 75.6 | 71.3 |
| Phi-3-mini | 3.8B | 68.8 | 82.5 | 41.3 | 58.5 |
| Phi-4-mini | 3.8B | 67.3 | 88.6 | 64.0 | — |
| Llama 3.1 8B | 8B | 69.4 | 84.5 | 51.9 | — |
| Gemma 3n E4B | ~4B eff. | 64.9 | — | 37.7 (HiddenMath) | 75.0 |
| **Gemma 4 E2B** | **2.3B eff.** | **60.0 (Pro)** | — | 37.5 (AIME 2026) | 44.0 (LCB) |
| Gemma 4 E4B | 4.5B eff. | 69.4 (Pro) | — | 42.5 (AIME 2026) | 52.0 (LCB) |
| Gemma 3 27B | 27B | 67.5 (Pro) | 95.9 | 89.0 | 87.8 |

Sources: Gemma model cards (huggingface.co/google/gemma-*); Phi-3 technical report
(Abdin et al., arXiv:2404.14219); Llama 3.2 model cards; Qwen3 (qwenlm.github.io/blog/qwen3).

**Gemma 4 E2B at 2.3B effective parameters scoring MMLU-Pro 60.0 is the single most
important number here** — two generations earlier, Gemma 3 27B scored 67.5. Qwen reports a
similar ~2× parameter-efficiency gain per generation ("Qwen3-1.7B/4B/8B performs as well as
Qwen2.5-3B/7B/14B"). The floor is falling fast.

### 4.2 But capability ≠ pedagogy — the most important finding in this section

**Maurya, Srivatsa, Petukhova & Kochmar, "Unifying AI Tutor Evaluation: An Evaluation
Taxonomy for Pedagogical Ability Assessment", arXiv:2412.09416** (MRBench, 192 dialogues):

| Tutor | Mistake ID | Mistake Loc | **Guidance** | **Actionability** | Coherence | **Human-like** |
|---|---|---|---|---|---|---|
| Human expert | 76.04 | 63.02 | **67.19** | **76.04** | 79.17 | 87.50 |
| Phi-3 (3.8B) | 28.65 | 26.04 | **17.71** | 11.98 | 39.58 | 52.08 |
| Llama-3.1-8B | 80.21 | 54.69 | **45.31** | 42.71 | 80.73 | **93.75** |
| Mistral (7B) | 93.23 | 73.44 | 63.54 | 70.31 | 86.98 | **95.31** |
| GPT-4 | 94.27 | 84.38 | 76.04 | 46.35 | 90.17 | 89.62 |
| Llama-3.1-405B | 94.27 | 84.38 | 77.08 | 74.48 | 91.67 | 90.62 |

Read this carefully. Small models are **good at noticing something is wrong** (Llama-3.1-8B
80.2% mistake ID) and **better than human experts at sounding human** (93.8% and 95.3% vs
87.5%). They are **bad at the thing that constitutes tutoring**: guidance (45.3% vs 67.2%)
and actionability (42.7% vs 76.0%).

**The failure mode is precisely the dangerous one for education: fluent, human-sounding,
confidently non-actionable.** A model that sounds more like a teacher than a teacher does,
while giving guidance barely two-thirds as useful, is worse than an obviously-broken one —
it will not trigger the scepticism it should.

Note also that **Phi-3 scored worst of all models tested (17.71% guidance) despite MMLU 68.8
and GSM8K 82.5.** Raw benchmark capability and tutoring ability are close to decoupled at
this scale. Any procurement decision made on MMLU is being made on the wrong number.

Corroborating evidence:
- **TutorEval** (Chevalier et al., arXiv:2402.11111): GPT-4 85.5 vs **best 7B ≈ 50.9** — a
  35-point gap that *survived* domain fine-tuning.
- **BEA 2025 shared task** (Kochmar et al., arXiv:2507.10579): best macro-F1 58.34 (guidance)
  to 71.81 (mistake ID) — but **96.98 F1 on identifying which tutor produced a turn.**
  Machine tutoring style is trivially detectable while the pedagogical judgements stay hard.
- **Error diagnosis is unsolved even at the frontier**: Imran & Bulathwela, "Catching The
  Correct Answer Trap", arXiv:2605.23925 — when a student reaches a correct answer by flawed
  reasoning, **frontier** models detect the misconception only **57%** of the time. A 1–3B
  model is not a credible diagnostician.
- **LearnLM** (arXiv:2412.16429) shows pedagogical post-training is worth +31% expert
  preference over GPT-4o — but at Gemini scale, telling us nothing about 1–4B.

### 4.3 Quantization, thermals, and the cheap-phone reality

**Quantization.** Liu et al., "Quantization Hurts Reasoning?", arXiv:2504.04823 — W8A8 and
W4A16 are essentially lossless; **below 4 bits is a cliff, and the cliff is steeper for
smaller models.** DeepSeek-R1-Distill-Qwen-1.5B at W3A16 loses 18.6% average (MATH-500
84.7 → 48.1); the 32B model loses only 3.9%.

Meta's own Llama 3.2 numbers show *method* matters as much as bit-width:

| | 1B BF16 | 1B naive PTQ | 1B SpinQuant | 1B QLoRA |
|---|---|---|---|---|
| GSM8K | 44.4 | **33.1** | 40.6 | 46.5 |
| MATH | 30.6 | **20.5** | 25.3 | 31.0 |

**Naive 4-bit PTQ costs a 1B model a quarter to a third of its math ability.**
Quantization-aware training recovers it. QAT is not optional at this scale. (Apple ships a
~3B model at **2 bits per weight** via QAT with only ~4.6% MGSM regression — but nobody
outside Apple has reproduced this and the weights are not released.)

**On-device throughput** (Meta, OnePlus 12 / Snapdragon 8 Gen 3, ExecuTorch):

| | 1B SpinQuant | 3B SpinQuant |
|---|---|---|
| Decode | 50.2 tok/s | 19.7 tok/s |
| Time-to-first-token | 0.3 s | 0.7 s |
| **Resident memory (RSS)** | **1.92 GB** | **3.73 GB** |

**The independent measurement that undercuts the on-device story.** Laskaridis, Katevas,
Minto & Haddadi, **"MELTing Point: Mobile Evaluation of Language Transformers"**, MobiCom
2024, arXiv:2403.12844:
- TinyLlama-1.1B 4-bit on a Galaxy S23: **13.6 tok/s on CPU, 13.2 on GPU** — GPU offload gave
  *no* benefit.
- Energy **0.16–0.21 mWh per token**; **~490–591 prompts until battery depletion** on
  flagship hardware.
- Thermals: iPhone 14 Pro surface reached **47.9 °C**, 13.8 W sustained, >18 W instantaneous.
- Their conclusion: **"continuous execution of LLMs remains elusive"** on account of energy
  and thermal limits.

**A 60-minute tutoring dialogue is exactly the sustained-conversation workload MELT
identifies as infeasible.** At 120 turns per session, MELT's 490–591 prompt budget means
**~4–5 sessions per full battery charge — a daily hour drains 20–25% of a flagship
battery.** In a household without reliable power, that converts directly into charging-kiosk
trips.

**What a $50–100 Android phone actually is.** Samsung Galaxy A06 (Aug 2024, **$100.80**):
MediaTek Helio G85 (12 nm), 2×A75 @2.0 GHz + 6×A55, **4 GB RAM**. The Android 15 CDD still
permits compliant devices with under 1 GB available memory, and such devices are still sold.

Against Meta's measured **1.92 GB RSS for a quantized 1B**, on a 4 GB device where the OS
already consumes 1.5–2.5 GB: **marginal at 1B, impossible at 3B.** On throughput, a Helio
G85 has roughly a quarter to a third of an S23's memory bandwidth, implying **~3–6 tok/s**
(extrapolated from MELT, *not* measured) — a 150-token tutor turn would take **25–50
seconds**.

**Honest conclusion: the $50–100 phone is not currently a viable host for a conversational
on-device tutor.** Claims to the contrary should be checked for whether they were measured on
flagship hardware. This is why §2's revised TCO prices a workable on-device device at ~$180,
not $60 — and why shared devices, not 1:1, are the only configuration that clears the
cost-effectiveness bar.

### 4.4 The threshold question

**The evidence-based floor is ~3–4B, and the evidence for it is weak.**

Supporting: below 3B the math substrate itself breaks (Llama 3.2 1B: GSM8K 44.4, MATH 30.6,
falling to 33.1/20.5 under naive PTQ — a tutor wrong a third to half the time is not a
tutor); at 3–4B, GSM8K crosses 85% and MMLU crosses 65%; vendors have independently converged
on ~3B for on-device (Apple ~3B, Gemma 4 E2B 2.3B effective, Phi-4-mini 3.8B).

**Why the evidence is weak, stated plainly:** MRBench is 192 dialogues and tested exactly one
model under 7B — Phi-3, which was an outlier. TutorEval's small-model entries are 2024-era.
**No study systematically sweeps model size (0.5B → 1B → 3B → 8B → frontier) against a fixed
pedagogical benchmark.** That is the exact experiment the field needs and does not have. And
there is **no study measuring learning outcomes for students using a small on-device tutor at
all.** Every threshold claim here, including this one, is inference from adjacent evidence.

**Compounding risk no benchmark captures:** the deployment stack multiplies degradations —
quantization loss, then a pedagogical gap larger than the capability gap, then thermal
throttling mid-session. Benchmarks measure only the first.

### 4.5 Distillation — encouraging, but for the wrong task

- Llama 3.2 1B/3B were distilled from 8B/70B logits — production-scale existence proof.
- **Dang & Ngo, arXiv:2503.16219**: DeepSeek-R1-Distill-Qwen-1.5B improved AMC23 from 63% to
  80% and hit 46.7% on AIME24 (beating o1-preview) for **$42 of compute** on 4×A40 over 24
  hours. The strongest cost-effectiveness datapoint for narrow specialisation.
- **Qian et al., ICML 2026, arXiv:2606.16152**: high-reward distillation data actively
  *impairs* small-model math reasoning unless style-aligned — a real trap for naive
  GPT-4-distillation pipelines.

**The honest gap:** no study shows a small model fine-tuned on a narrow curriculum domain
matching a frontier model **at tutoring**. Everything above is math-*solving* specialisation
or tutor-*evaluation* distillation. Given that MRBench shows pedagogical and problem-solving
skill are close to decoupled, transferring these results to tutoring is an extrapolation the
field has not validated. **This is the most important open question in this section.**

---

## 5. The digital divide as it actually is

### 5.1 Connectivity (ITU *Facts and Figures 2025*)

| Metric | Value |
|---|---|
| Global internet users | **74%, ~6.0 billion** |
| **People offline** | **2.2 billion (26%)** |
| Africa | **36%** |
| LDCs / LLDCs | **34% / 38%** |
| Low-income vs high-income economies | **23% vs 94%** |
| Urban vs rural (global) | 85% vs 58% |
| Urban–rural ratio, Africa | **2.6** (Europe 1.1) |
| **Rural internet use, low-income countries** | **14%** |
| Gender | men 77% vs women 71%; **~280 million more men online** |
| Mobile phone ownership (10+) | 80% global; **Africa 66%**; low-income **56%** |

**The structural fact that reframes everything.** ITU 2025: **96%** of the world population
is covered by 3G or better, **93%** by 4G. Only **4% (~312 million)** live outside coverage.
But only 74% use the internet.

**→ The usage gap is ~22 percentage points, roughly 1.8–1.9 billion people who live under a
mobile broadband signal and do not use it — about 6× the size of the coverage gap.**

The binding constraint is **affordability, devices, skills and relevance — not towers.**
Building more network does not reach these people; they are already covered. This is the
single most important fact for anyone designing global AI-learning delivery, and it points
away from streaming-voice architectures and toward the cheapest possible channel.

Affordability (ITU 2025): entry-level mobile data = 1.4% of GNI per capita globally, but
low-income subscribers spend **~22×** the income share high-income subscribers do. Only
**~40% of low- and middle-income economies** meet the Broadband Commission 2% affordability
target for even one basket.

### 5.2 Electricity

| Metric | Value | Source |
|---|---|---|
| Access to electricity, world | 91.9% | WB `EG.ELC.ACCS.ZS` (2024) |
| Sub-Saharan Africa | **55.1%** | WB (2024) |
| Low-income countries | **48.8%** | WB (2024) |
| **People without electricity** | **666.4 million** | UN SDG Report 2025 (2023) |
| SSA share of that deficit | **565 million = 85%** | UN SDG Report 2025 |
| Projected still unserved in 2030 | 645 million | UN SDG Report 2025 |

(The widely quoted 685 million is the 2022 reference-year figure; **666.4 million is
current.**)

### 5.3 Schools — the sharpest data in this section (UNESCO UIS, 2024)

| Indicator | World | **Sub-Saharan Africa** | LDCs |
|---|---|---|---|
| Primary schools with **electricity** | 78.1% | **36.3%** | 43.1% |
| Lower secondary with electricity | 86.8% | 49.0% | 56.4% |
| Primary schools with **computers** | 48.5% | **19.0%** (2022) | 26.0% |
| Lower secondary with computers | 65.4% | 28.3% (2019) | 34.2% |
| Primary schools with **internet** | 48.0% | *no aggregate published* | 23.4% |
| Upper secondary with internet | 69.7% | 25.2% (2016) | 36.4% |

Comparator, primary level: Europe & North America 99.7% electricity / 98.8% computers /
95.9% internet.

**→ In Sub-Saharan Africa, at most ~6.9% of primary schools have both electricity and a
computer** (0.363 × 0.190, assuming independence — the true figure is higher if correlated,
but the ceiling is what matters).

**UIS publishes no recent regional aggregate for SSA primary computers or primary/lower
secondary internet. The most recent data points are 2016–2022. The absence of data is itself
a finding** — we are proposing to deliver AI tutoring into an infrastructure we have stopped
measuring.

### 5.4 Teachers — the human-capacity divide

| Metric | World | SSA | Low income |
|---|---|---|---|
| Pupil–teacher ratio, primary | 23.4 | **37.4** | **39.8** |
| Qualified teachers, primary | 88.9% | **73.4%** | — |
| Qualified teachers, secondary | 87.2% | **66.2%** | — |
| Trained teachers, secondary | 81.5% | **59.5%** | 55.6% |

**The 44 million gap** (UNESCO *Global Report on Teachers*): 44 million additional primary
and secondary teachers needed by 2030; **Sub-Saharan Africa alone needs ~15 million (34%)**.
Cost to close: **~US$120 billion/year** ($12.8bn primary + $106.8bn secondary). For scale,
the world had 34.1 million primary teachers in 2024 — **the gap is larger than today's entire
primary teaching force.** Primary teacher attrition nearly doubled, 4.62% (2015) → 9.06%
(2022).

**Teacher presence and knowledge — World Bank Service Delivery Indicators.** Bold, Filmer,
Martin, Molina, Stacy, Rockmore, Svensson & Wane, *"What Do Teachers Know and Do? Does It
Matter?"*, World Bank PRWP 7956 (2017) / *JEP* 31(4):185–204. Eight surveys, seven SSA
countries:

- **44% of teachers were absent from class.** In three of eight surveys, over half. Only
  Nigeria was below 30%.
- **One-third of classrooms were "orphaned"** — students present, no teacher.
- Scheduled teaching day **5h27m**; actual instruction received **2h49m — roughly half.**
  ~10% of schools provide no teaching at all on a given day.
- **Content knowledge: only 7% of language teachers** met the minimum threshold (80%
  correct); **zero** met it in Togo, Mozambique, Tanzania (2010) or Nigeria. In maths, **1 in
  10 could not add two double-digit numbers**; half could solve a simple story problem.
- **Pedagogical knowledge: only 10%** reached the minimum threshold; under 5% in four
  countries. Only **17%** could give feedback on strengths and weaknesses.
- **No improvement in two decades**: Uganda school absence 27% (2002–03, Chaudhury et al.) →
  30% (2013, SDI).

**The arithmetic that follows is uncomfortable for both sides of the argument.** The missing
2h38m of daily instruction × 180 days = **~473 hours per child per year of already-funded,
already-scheduled teaching that does not happen.** That is **2.6× the 180-hour AI dose modelled
in this section**, available at zero marginal compute cost if the adult simply shows up.

But note the other edge: where only 7% of teachers meet minimum subject knowledge and 10%
meet minimum pedagogical knowledge, "the adult shows up" is not sufficient either. **This is
the strongest available argument for AI as a complement — not because teachers are
replaceable, but because a teacher with a competent tutor in the room is a different
proposition from a teacher without one.**

### 5.5 Learning poverty, out-of-school children, and nutrition

- **Learning poverty**: **70%** of 10-year-olds in LMICs cannot read and understand a simple
  text (up from 57% pre-pandemic). **Sub-Saharan Africa 89%.** Latin America 80%, South Asia
  78%. Lifetime earnings loss for this cohort: **US$21 trillion**, 17% of global GDP.
  (World Bank/UNESCO/UNICEF, *State of Global Learning Poverty: 2022 Update*.)
- **Out-of-school (UIS, 2025): 272.9 million** — primary 78.6m, lower secondary 63.6m, upper
  secondary 130.7m. SSA 109.0 million. SSA out-of-school rates: primary 20%, lower secondary
  34%, upper secondary **46%**. (The commonly quoted "250 million" is the pre-revision
  figure — **use 272 million**.)
- **Foundational learning**: minimum proficiency is **58% in reading, 44% in mathematics**.
- **Stunting**: **149 million** under-5s (WHO/JME 2022); prevalence world 23.2%, **SSA 32.3%,
  low-income countries 35.8%**.
- **Deworming — the nuance that matters.** Miguel & Kremer (2004), *Econometrica* 72(1),
  doi:10.1111/j.1468-0262.2004.00481.x: mass deworming **"reduced school absenteeism by
  one-quarter"** and was far cheaper than alternatives — **but "we do not find evidence that
  deworming improved academic test scores."** The canonical "fix health first" intervention
  got children into seats and did not, by itself, raise learning. This cuts against a naive
  version of the counter-argument in §7 as much as it supports the sophisticated one.

### 5.6 Financing

- **SDG4 annual financing gap: US$97 billion/year** across 79 low- and lower-middle-income
  countries (UNESCO GEM, *Can countries afford their national SDG 4 benchmarks?*, 2024).
- Education spending as % of GDP: world 3.57%, **low income 2.98%**.
- **Low-income countries already allocate 16.7% of government budgets to education — a
  larger share than high-income countries' 12.0%, and at the top of the recommended 15–20%
  band. The gap is not political will at the margin; it is the size of the base.**
- Spending per primary pupil: **~US$75/year in low-income countries vs ~US$10,300 in
  high-income — a ratio of roughly 140:1.** (Derived: WB `SE.XPD.PRIM.PC.ZS` share applied to
  2024 GDP per capita; numerator years are stale (2012–2016), so treat as order-of-magnitude.)

This $75 figure is the denominator for everything in §1. **The $9.36/child/year small-model
configuration is 12% of a low-income country's entire per-pupil budget. The $253.80 frontier
configuration is 3.4× the whole budget.**

---



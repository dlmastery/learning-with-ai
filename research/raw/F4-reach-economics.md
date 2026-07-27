---
title: "The Reach Frontier — Economics, Access, Language, and What Becomes Possible at Near-Zero Marginal Cost"
wave: F
date_researched: 2026-07-25
date_completed: 2026-07-27
sources_count: 52  # distinct machine-checkable identifiers (DOI / arXiv / NBER-IZA-PRWP / URL / World Bank indicator code); a further ~60 works, datasets and agency reports are cited by title and venue
---

> **⚠️ PARTIAL — agent terminated by session limit mid-write (2026-07-25).**
> Sections 1–3 are complete and self-corrected (the agent explicitly replaced its
> own §3 after finding its published-multiplier estimates "wrong in both
> directions"). Sections 4+ (offline/low-bandwidth design, ICT4D failure history,
> the digital divide, deployed-intervention RCTs, and the steelman counter-argument)
> were **never written**. Re-run required — see CLAUDE.md §8.
>
> **✅ COMPLETED 2026-07-27.** The banner above is preserved as the record of the crash and is
> now superseded. Note that it undercounts what survived: the recovered file contains **five**
> complete sections, not three. §6–§12 were appended on 2026-07-27 under a reframe from
> *affordability* to *reach and capability* — see the completion note immediately after §5.


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



---

# ⟦ COMPLETION — appended 2026-07-27 ⟧

**Status of this file.** Sections 1–5 above were written on 2026-07-25 by an agent that was
terminated by a session limit. The warning banner at the top of the file says "Sections 1–3 are
complete"; that banner is itself a casualty of the crash — **the file as recovered contains five
complete sections** (§1 cost curve, §2 total cost of ownership, §3 language, §4 small/on-device
models, §5 the digital divide as it actually is). Everything below is new material appended on
**2026-07-27**, numbered **§6 onward** so that nothing above is renumbered, rewritten, or
contradicted by stealth.

**Two forward-references in the recovered text are now stale and are corrected here:**
§2 points to "§4" for the ICT4D failure history — that history is now **§7**. §5.5 points to
"§7" for the counter-argument — that is now **§10**. §2 and §4.3's cross-references to each other
are internally consistent and unchanged.

## The reframe, stated before it is executed

The project owner delivered a reframe after §1–5 were drafted, and it changes what this section
is arguing. It deserves to be stated plainly rather than smuggled in.

**§1 argues from price.** Its central question is "at what price does 1:1 tutoring for every
child become fundable?", its central answer is "~$0.05 per hour," and its verdict is "the
economics claim survives contact with the arithmetic." §1.4 extrapolates a 50×/year price decline.
§3.4 and §5.6 then price language and per-pupil budgets in the same currency.

**That framing is now retired for everything below.** Not because the arithmetic is wrong — it is
carefully done and it holds — but because **it answers a question that is not binding.** Inference
cost per unit of capability is falling on a curve that is well characterised, well capitalised, and
not in dispute. A constraint that dissolves on a known schedule without anyone doing anything is
not the interesting constraint. Optimising it is optimising a term that is already going to zero.

The recovered sections in fact make this argument against themselves, and the honest reading of
§1–5 is that **the section's own evidence overturns the section's own frame**:

| Recovered finding | What it says about price |
|---|---|
| §2's TCO inversion — inference is 79% of cost at frontier, **0%** on-device | As tokens approach free, 100% of the remaining problem is not tokens |
| §2.2 — **~89,000 H100s**, 0.16% of global data-centre electricity, serves every school-age child on earth | Compute supply is not scarce and never was |
| §2.2 — the silicon the child *holds* costs 30–300× more per year than the silicon that *thinks* | The device, not the model, is the expensive object |
| §5.1 — the **usage gap** (1.8–1.9B people under a signal who do not use it) is ~6× the **coverage gap** | The barrier is not the absence of infrastructure |
| §3.2/§3.5 — open models score **2.9–4.6** on AfriMGSM in-language; best-available ASR is at **44.3 WER** | Free tokens in a language the model cannot speak are worth nothing |
| §4.2 — Phi-3 scores **17.71** on pedagogical guidance against a human expert's 67.19 | Cheapness and tutoring ability are close to orthogonal |
| §5.4 — **44%** teacher absence, **7%** meeting minimum subject knowledge | The scarce resource is competent attention, not compute |

**So the question below is not "what does it cost?" It is: *who is currently unreached, what is
structurally in the way, and what becomes newly possible when competent attention is abundant?***

Where §1–5 measured dollars, §6–§11 measure **reach**: connectivity states, delivery channels,
languages, populations, and the barriers that a price of zero does not touch. Three of those
barriers — language, institutional permission, and evidence-of-efficacy-for-this-population — are
completely insensitive to the cost curve. One of them, language, is the one this section will argue
is the single highest-leverage engineering target in the entire survey.

**Evidence labels are unchanged** from the project standard: `MEASURED-RCT` · `MEASURED-META` ·
`MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`. The rule that a deployment count
or a vendor claim may **never** be restated as an efficacy finding is enforced aggressively below,
because the offline-education literature is almost entirely deployment counts and the temptation
to launder them is the field's characteristic failure.

---

## 6. Offline, low-bandwidth and intermittent — the real reach constraint

§5.1 produced the number that should govern this entire section: **96% of the world's population
is covered by 3G or better and 93% by 4G, but only 74% use the internet — a usage gap of roughly
1.8–1.9 billion people, about 6× the size of the coverage gap.** The barrier is not the tower.

But "covered" is not "connected," and "connected" is not "connected right now." **The reach
constraint is not the absence of a network. It is the assumption, baked into every cloud-first
architecture, that the network is there when the learner is.** That assumption is what excludes
people, and it is an engineering choice rather than an economic fact.

### 6.1 Four connectivity states, not two

The sector talks about "the offline" as a population. It is better modelled as **four states that
the same learner moves between during a single day**:

| State | Description | Who lives here | What the architecture must do |
|---|---|---|---|
| **Never connected** | No signal, or connection forbidden | ~312M outside coverage (§5.1); incarcerated learners; some pastoralist and conflict-affected populations | All inference local; content pre-loaded; **no round trip ever** |
| **Intermittent** | Signal available in bursts — a market day, a town trip, a charging kiosk | Rural low-income households; nomadic households; refugee settlements | **Store-and-forward**: queue work locally, reconcile opportunistically |
| **Narrowband / metered** | Signal present but 2G-class or priced per megabyte | The bulk of the 1.8–1.9B usage gap | **Text-only or voice-only over the wire**; local ASR/TTS; ruthless byte discipline |
| **Connected** | Broadband, unmetered enough | The 74% | Anything |

§2.1 already priced the third state: at $3/GB, streamed voice costs **$7.78/child/year in data
alone**, against **$0.26** for text-only — a **150×** difference for the same tutoring session,
which is why on-device speech (ASR and TTS local, only text over the wire) is not an optimisation
but the design. §2's scenario F — SMS/IVR on the feature phone the household already owns —
totals **$1.75/child/year including everything**, and requires no new device at all.

**The architectural point:** a system built for state 4 and "degraded gracefully" for states 1–3
is a system built for the people who were already reachable. **A system built for state 2 works in
all four.** Store-and-forward is a superset of streaming; the reverse is not true.

### 6.2 The offline-content lineage — what exists, and what is known about it

There is a twenty-year-old engineering tradition here, and it is genuinely good work: a small
server, often a Raspberry-Pi-class device, often solar-powered, holding a curated content library
and serving it over a local Wi-Fi hotspot to phones and tablets that never touch the internet.
The lineage runs KA Lite → **Kolibri** (Learning Equality), **RACHEL** (World Possible),
**Internet-in-a-Box**, **SolarSPELL**.

**What is documented is deployment. What is not documented is learning.** This distinction is the
entire point of this subsection and the project's editorial standard forbids blurring it.

| System | What it is | Evidence located |
|---|---|---|
| **Kolibri** | Offline-first learning platform + content library, local server | Kabugo (2020), *Journal of Learning for Development* — 10 government-aided secondary schools in Uganda during the COVID lockdown, 25 teachers and 100 students. **Method: "a Discourse Analysis (DA) of teachers' use of OER on Kolibri."** No control group, no learning outcome, no effect size. `OBSERVED` |
| **SolarSPELL** | Solar-powered offline digital library, Wi-Fi hotspot | Farrell, Hosman, Barrett & Nova (2024), *JITE:IIP*, doi:10.28945/5385 — mixed-methods case study in **South Sudan**. Findings framed as "offline digital solutions can effectively mitigate educational disruptions by providing an accessible means to continue education." **Continuity of access, not measured learning.** `OBSERVED` |
| **SolarSPELL (companion)** | Information-literacy tutorials for offline users | *JLD* (2024) — "report from the field" describing instructional videos created for novice users. `OBSERVED` / `DEMO` |
| **Offline micro-servers, generally** | Raspberry Pi / tablet / Chromebook as LMS host | Maro, Kondoro, Haßler, Mtebe & Proctor (2023), *JLD* — **Tanzania**, head-to-head benchmark. See §6.5. `MEASURED-BENCH` |
| **RACHEL, Internet-in-a-Box, Learning Passport, Giga** | Offline content servers; UNICEF/ITU connectivity programmes | **No controlled learning-outcome evaluation located.** `OBSERVED` (negative search result) |

**The finding, stated as plainly as it deserves:**

> **A targeted search of ERIC for controlled evaluations of the offline-server lineage returns
> case studies, discourse analyses, field reports and device benchmarks — and no randomised or
> quasi-experimental study measuring learning outcomes.** The best-documented deployment in the
> family (Kolibri in Uganda) is explicitly a discourse analysis. `OBSERVED` — search performed
> 2026-07-27; absence of evidence is reported as absence of evidence, not as absence of effect.

This is the third documented null-or-absent category in this section, and it is the one that
should most worry anyone about to build an offline AI tutor: **the lineage this design descends
from has never been shown to teach anybody anything.** It has been shown to *reach* people, which
is a real and non-trivial achievement, and which is not the same claim.

**A deployment count is not an efficacy finding.** Where vendor or project sites publish
installation totals, those are `OBSERVED` at best and `VENDOR` at worst, and they may not be
restated as evidence that the thing works. This section publishes none of them, because none was
retrievable from a primary source during this research and a number that cannot be checked is
worse than no number.

### 6.3 The narrowband channels — where the evidence actually is

Here the picture inverts completely. **The lowest-bandwidth channel in the entire stack has the
best evidence in the entire stack**, and §7.3 has the numbers:

| Channel | Bandwidth | Best measured effect |
|---|---|---|
| **Voice call + SMS** | A phone call | **+0.327 SD** pooled, five countries, N=8,902 (Angrist et al., NBER 31208); **+0.121 SD** ITT / **+0.167 SD** TOT in Botswana (*Nature Human Behaviour* 2022) |
| **SMS content alone** | ~140 bytes/message | **+0.083 SD** pooled — but **null in Kenya, null in Nepal**, and **+0.024 SD, p = 0.602** in Botswana |
| **IVR (interactive voice response)** | A phone call, no human | **Null.** Afoakwah et al., EdTech Hub Ghana (2021), 1,359 students: "**no significant effect was found on students' math skills**"; only place value moved, +5%, significant at 10% only |
| **Live tutoring calls, Sierra Leone** | A phone call | **Null.** Crawfurd et al., *J. Dev. Econ.* 164 (2023): maths **−0.008**, language **−0.027**; child-activity index **+0.29 SD** |
| Streamed voice tutoring | 16–32 kbps | **No learning-outcome trial located** |
| On-device conversational tutor | 0 | **No learning-outcome trial located** |

**Read the top two rows together and the whole section's thesis appears.** The channel is identical
— a mobile phone in a household. The content is broadly identical — foundational numeracy at the
child's level. **The difference between +0.083 SD and +0.327 SD is a live human being on the
call.** J-PAL's synthesis of thirty studies: "Mobile remote instruction works best when it
**supports human interaction rather than one-way content delivery**… **Making content available is
not enough.**" `OBSERVED`

**And read the top row against rows three and four and the qualification appears.** IVR — a phone
call with no human — is null. Live tutoring calls in Sierra Leone, with real humans, are also
null, while raising the child-activity index by 0.29 SD. **Neither the channel nor the human is
sufficient. Targeted instruction delivered conversationally is what works** (§7.5), and it is
transmissible over the narrowest channel in existence.

**A note on the SMS payload constraint, and an honest failure.** SMS is conventionally described
as 160 characters under the GSM 7-bit default alphabet, dropping to 70 characters when UCS-2
encoding is required — which it is for Devanagari, Ge'ez, Bengali, Telugu, Burmese, Khmer and most
non-Latin scripts. **I could not verify these figures against the primary specification: ETSI's
copy of 3GPP TS 23.038 returned HTTP 403.** They are therefore reported as widely-used engineering
constants requiring verification, not as established fact. If the 160/70 figures are right, the
consequence is worth stating because it rhymes exactly with §3.3's tokenizer finding: **the same
learner who pays a 5.7× tokenizer penalty in Amharic also pays a 2.3× SMS-payload penalty in
Amharic. The narrowband channel and the model both charge the same people extra for the same
scripts.** `INFERENCE`, conditional on the constants.

### 6.4 Store-and-forward, and why intermittency is the design centre

State 2 — intermittent — is the largest and least-served of the four states, and it has a mature
answer that predates all of this: queue work locally, reconcile when a connection appears. The
delay-tolerant-networking and "data mule" literature (Daknet, KioskNet, Wizzy Digital Courier) is
the canonical reference point. **No controlled educational evaluation of a store-and-forward
learning system was located in this research**, and the classical DTN papers could not be
retrieved through the available APIs. `OBSERVED` — flagged as a gap rather than filled with
assertion.

What can be said without a citation crutch is architectural, and it follows from §2's arithmetic:

- **Sync the learner model, not the media.** §5's TCO shows bandwidth is the second-largest
  recurring cost and the only one that scales with usage. A learner model — mastery estimates,
  misconception flags, item history — is kilobytes. A tutoring session's audio is megabytes.
- **The session must complete without the network.** Not degrade: complete. Any design in which a
  learner's turn blocks on a round trip has excluded states 1 and 2 by construction.
- **Content is pre-positioned; intelligence is local; only state reconciles.** This is the Kolibri
  architecture with a model added, and the reason it is the right shape is that the offline-content
  lineage already solved the hard logistics of getting bytes to a school without a connection.

### 6.5 What is actually measured about running a model at the edge

Four measured datapoints, all recent, none of them about learning:

**Micro-server capability.** Maro, Kondoro, Haßler, Mtebe & Proctor (2023), *JLD* — Raspberry Pi
vs Android tablet vs Chromebook as an offline LMS host in Tanzania. `MEASURED-BENCH`
> "**All devices had sufficient hardware resources to support the LMS**, however, software stacks,
> I/O performance, and platform optimisations affected the micro-servers' performance. The
> Chromebook had the best performance in terms of response time, followed by the Raspberry Pi and
> tablets. In terms of cost, the Raspberry Pi was the cheapest option."

**Offline LLM tutoring, deployed.** Walusimbi, Oguti, Ssentongo & Ainebyona, "Arapai: An
Offline-First LLM Architecture for Adaptive Learning in Low-Connectivity Environments,"
arXiv:2603.03339 (2026). Quantised models, hardware-aware model selection, CPU-only legacy
devices; adaptive response levels (Simple English / Lower Secondary / Upper Secondary /
Technical). Evaluated with **120 students and 9 instructors**.
> "Results indicate **stable operation on legacy hardware, acceptable response times of 1–3
> seconds** for typical queries, and **positive user perceptions** of its effectiveness in
> supporting self-directed learning."

`MEASURED-BENCH` for the latency; **`OBSERVED` for the perceptions — and perceptions are not
outcomes.** §7.1's Uruguay row is the cautionary precedent: **85.8% of Plan Ceibal principals
believed the programme had a positive impact on learning, and the measured effect was zero.**
Arapai is the most advanced offline-first educational LLM deployment located in this research and
it is, on its own evidence, at the same epistemic level as Plan Ceibal's principals.

**The energy–latency–quality frontier, measured.** Khemani, "Inference Energy and Latency in
AI-Mediated Education: A Learning-per-Watt Analysis of Edge and Cloud Models," arXiv:2603.20223
(2026). Phi-3 Mini (4k-instruct) on an NVIDIA T4, FP16 vs 4-bit NF4, 500 educational prompts
across five secondary subjects, 1,000 responses rated by **10 Cambridge International teachers and
three frontier AI systems** on a four-dimension rubric. `MEASURED-BENCH`

| Configuration | Energy per inference | Latency | Quality difference |
|---|---|---|---|
| FP16 | **369 J** | **9.2 s** | baseline |
| 4-bit NF4 | **329 J** | **13.4 s** | −0.19 points |

FP16 wins on the paper's Learning-per-Watt metric by **1.33×** under realistic (KV-cache-enabled)
inference. **The methodological finding is the important one:** with the cache disabled — "used in
offline evaluation but absent from real deployments" — the apparent gap widens to **7.4×**,
**overstating the FP16 advantage by more than fivefold.** `MEASURED-BENCH`

**This is a warning to every quantisation decision in §4.3.** Benchmarks run in the offline
evaluation regime systematically misrepresent the deployed trade-off, and the direction of the
error is toward *under*-valuing quantisation — i.e. toward telling you that the edge deployment is
worse than it is.

**And the negative result.** Hevia, Arredondo & Kumar, "Towards an Efficient, Customizable, and
Accessible AI Tutor," arXiv:2510.06255 (2025) — an offline RAG pipeline pairing a small language
model with retrieval, evaluated on biology coursework. `MEASURED-BENCH`
> "**Smaller models, such as SmolLM, struggle to effectively leverage extended contexts provided by
> the RAG pipeline, particularly when noisy or irrelevant chunks are included.**"

The obvious architecture for an offline tutor — small model plus a local retrieval corpus, since
the corpus is already sitting on the Kolibri server — **has a documented failure mode at exactly
the model scale the offline deployment requires.** The authors' own conclusion is a
recommendation to move "beyond traditional metrics like MMLU to a holistic evaluation framework,"
which is §4.2's finding arrived at independently.

For completeness: Ghorbani & Fattahi, arXiv:2506.12403 (2025), "Bridging the Digital Divide: Small
Language Models as a Pathway for Physics and Photonics Education in Underdeveloped Regions," is a
**position paper with no deployment and no data** — `DEMO`. It is cited here only to mark that the
enthusiasm is running well ahead of the measurement.

**The thermal and energy ceiling from §4.3 still binds and should be repeated here**, because it is
the constraint most often forgotten when someone says "just run it on the phone": MELT (Laskaridis
et al., MobiCom 2024) measured **0.16–0.21 mWh per token**, **~490–591 prompts until battery
depletion** on flagship hardware, iPhone 14 Pro surface temperature **47.9 °C**, and concluded that
"**continuous execution of LLMs remains elusive**." A 120-turn tutoring hour is **20–25% of a
flagship battery**, which in a household without reliable power converts directly into
charging-kiosk trips — a cost that appears in no TCO model.

### 6.6 What §6 establishes

1. **The reach constraint is architectural, not financial.** Nothing in §6 is made easier by a
   cheaper token. Everything in §6 is made easier by an inference that happens locally.
2. **The narrowest channel has the best evidence.** A voice call — the oldest, cheapest,
   lowest-bandwidth channel available, working on hardware households already own — delivers
   **+0.327 SD**, ranks in the **top 10 of 150 interventions** by cost-effectiveness, and works
   equally well delivered by government teachers as by NGOs.
3. **The offline-server lineage has reach without measured efficacy.** Twenty years of good
   engineering, real deployments, and — on this search — **not one controlled learning-outcome
   study.** `OBSERVED`
4. **Running a model at the edge is now measured, and the measurements are sobering but not
   disqualifying.** 1–3 second responses on CPU-only legacy hardware; 329–369 J and 9–13 s per
   inference at Phi-3-Mini scale; a documented small-model failure on long RAG contexts; a hard
   thermal and battery ceiling on continuous sessions.
5. **Perception is not outcome, and this literature runs on perception.** Arapai's "positive user
   perceptions" and Plan Ceibal's 85.8% of principals are the same evidence class, and one of them
   has already been checked against a measured zero.

---

## 7. ICT4D — the evidence, the graveyard, and the split that matters

Forty years of putting technology in front of poor children has produced a literature with an
unusually clear shape. It is not a story of uniform failure, which is how it is usually told, and
it is not a story of promise deferred, which is how it is usually sold. **It is bimodal, and the
line between the two modes is legible in advance from the design of the intervention.**

This section reports the graveyard first, at full strength, then the survivors, then the rule
that separates them.

### 7.1 The graveyard: hardware distribution

Every study below is a randomised or regression-discontinuity design with a real control group
and a real learning outcome. Point estimates are in standard deviations of the control-group
distribution unless noted.

#### One Laptop Per Child, rural Peru — the canonical trial

**Cristia, Ibarrarán, Cueto, Santiago & Severín, "Technology and Child Development: Evidence from
the One Laptop per Child Program," *AEJ: Applied Economics* 9(3), 2017, 295–320,
doi:10.1257/app.20150385.** 318–319 rural primary schools; 15 months. `MEASURED-RCT`

The programme *worked* as a logistics operation. Computers per student went from **0.118 to
1.178** (diff +1.046, SE 0.046). Students who had used a computer in the last week: 84.3% vs
31.9% (+0.518, SE 0.041). The laptops arrived, and the children used them.

| Outcome | Effect | SE |
|---|---|---|
| Math | +0.046 | (0.061) |
| **Language** | **−0.039** | (0.057) |
| **Average math + language** | **+0.003** | **(0.055)** |
| Raven's Progressive Matrices | +0.112 | (0.057), p≈.055 |
| Cognitive-skills index | +0.110 | (0.060), p≈.068 |
| Enrollment (students/school) | −1.754 | (2.514) |
| Attendance | +0.024 | (0.019) |
| Read a book last week | −0.017 | (0.027) |
| Self-perceived school competence | **−0.021** | (0.010), sig. at 5% |

> "No evidence is found of effects on enrollment and test scores in Math and Language."
>
> "The estimated effect on the average Math and Language score is **0.003 standard deviations**,
> and the associated standard error is 0.055."
>
> "Small standard errors allow ruling out modest effects. For example, for the average test score
> in Math and Language **we can rule out effects larger than 0.11 standard deviations at the five
> percent level**."

That last sentence is what makes this trial decisive rather than merely disappointing. **This is
not an underpowered null. It is a precisely estimated zero.** (Point estimates and SEs above are
from the IZA DP 6401 working-paper tables, since the published AEJ tables are paywalled; the
published abstract hedges the cognitive-skill result further, to "some evidence, though
inconclusive." Flagged rather than smoothed.)

#### The same programme, ten years later

**Cueto, Beuermann, Cristia, Malamud & Pardo, "Laptops in the Long Run: Evidence from the One
Laptop per Child Program in Rural Peru," NBER WP 34495, Nov 2025.** **531 rural primary schools**
(296 treatment) — a *complementary arm of the same original randomisation*, not a re-survey of
the 2017 schools — with administrative data 2007–2019. `MEASURED-RCT`

| Outcome | Effect | SE | N |
|---|---|---|---|
| Grade-2 math | −0.044 | (0.045) | 22,861 |
| Grade-4 reading | −0.133 | (0.073) | 3,207 |
| Grade-8 math | +0.026 | (0.045) | 6,024 |
| **Index of academic performance** | **−0.046** | (0.045) | 22,898 |
| Primary completion on time | −0.021 | (0.011) | 28,516 |
| Secondary completion on time | −0.022 | (0.015) | 7,749 |
| Applied to university on time | −0.022 | (0.013) | 3,750 |
| Completed years of education | −0.061 | (0.044) | 28,516 |
| **School-level grade progression, pooled 2009–16** | **−0.010** | (0.005), **p<0.05** | 4,234 school-yrs |

> "Following schools over time, we find no significant effects on academic performance but **some
> evidence of negative effects on grade progression**. Following students over time, we find no
> significant effects on primary and secondary completion, academic performance in secondary
> school, or university enrollment."
>
> "Pooling all the years together, **we can rule out, with 95 percent confidence, effects larger
> than 0.05 standard deviations**."
>
> "Overall, we conclude that there were **no long-term effects** of the OLPC program on either
> academic performance or educational attainment."

The mechanism data is the part a builder should read twice. XO-specific computer skills:
**+0.41 SD.** General PC skills: +0.17, marginal. Internet skills: null. Cognitive index:
insignificant. **The children learned to use the object. The object taught them nothing else.**

#### OLPC at home, Lima

**Beuermann, Cristia, Cueto, Malamud & Cruz-Aguayo, *AEJ: Applied Economics* 7(2), 2015, 53–80,
doi:10.1257/app.20130267** (NBER WP 18818). ~1,000 XO laptops lotteried to primary-school
children in Lima; N ≈ 2,700–2,850 in regressions. `MEASURED-RCT`

| Outcome | Effect | SE |
|---|---|---|
| **XO proficiency test** | **+0.88** | (0.07) |
| Objective PC & internet test | +0.02 | (0.01) |
| Raven's Progressive Matrices | +0.05 | (0.04) |
| **Teacher-rated "high academic effort in class"** | **−0.05** | (0.02), p<0.05 |
| **Time reading** | **−0.06** | (0.03), sig. |

> "Children randomized to receive laptops scored about 0.8 standard deviations higher in a test of
> XO proficiency **but showed lower academic effort as reported by teachers. There were no impacts
> on academic achievement or cognitive skills** as measured by the Raven's Progressive Matrices
> test."

**A child given a laptop read less and tried less.** The one skill that transferred was
proficiency with the specific machine, which is worth nothing once the machine is obsolete.
(The published math/reading achievement estimates could not be retrieved — AEJ paywalled, no OA
copy, and the NBER working paper measured achievement at baseline only. Flagged.)

#### Home computers, Romania — the clearest negative in the literature

**Malamud & Pop-Eleches, "Home Computer Use and the Development of Human Capital," *QJE* 126(2),
2011** (NBER WP 15814). Regression discontinuity on an income cutoff for a €200 computer voucher;
3,354 families. `MEASURED-RCT` (RD)

| Outcome | Nonparam. bw 60 | Nonparam. bw 30 | Parametric linear spline |
|---|---|---|---|
| **Math GPA** | −0.276 [0.118]** | −0.435 [0.171]** | −0.208 [0.100]** |
| **Romanian GPA** | −0.424 [0.126]*** | −0.562 [0.181]*** | −0.367 [0.104]*** |
| **English GPA** | −0.362 [0.153]** | −0.634 [0.225]*** | −0.321 [0.129]** |
| Raven's | +0.275 [0.092]*** | +0.320 [0.133]** | +0.146 [0.079]* |
| Computer-skills test | +0.329 [0.076]*** | +0.242 [0.108]** | +0.265 [0.066]*** |

> "Children who won a voucher had **significantly lower school grades in Math, English and
> Romanian** but significantly higher scores in a test of computer skills… with most estimates
> clustered around **an effect size of 1/3 of a standard deviation**."
>
> "…**few parents or children report having educational software installed**… Instead, **most
> computers had games installed** and children reported that most of the computer time was spent
> playing games."

Only **9%** of households had educational software; only **14%** had internet. This is not a story
about computers being bad. It is a story about **what an unstructured device actually gets used
for**, which is the single most transferable lesson in this section.

#### Classroom computers, Israel

**Angrist & Lavy, "New Evidence on Classroom Computers and Pupil Learning," *Economic Journal*
112, Oct 2002, 735–765, doi:10.1111/1468-0297.00068.** ~35,000 computers, ~$120,000/school —
"roughly four teachers' wages in Israel." `MEASURED-RCT` (IV/quasi-experimental)

4th-grade maths, reduced form: **−0.204 SD** (SE 0.089); with lagged score **−0.241** (0.088).
2SLS on CAI intensity: **−0.340** (0.214) to **−0.427** (0.252).

> "Although many of the estimates are imprecise, **CAI does not appear to have had educational
> benefits that translated into higher test scores**."
>
> "…pupils in the Tomorrow group scoring **0.2–0.25 standard deviations lower** than other pupils."
>
> "**On balance, it seems, money spent on CAI in Israel would have been better spent on other
> inputs**."

#### Computers for Education, Colombia

**Barrera-Osorio & Linden, World Bank PRWP 4836 (2009).** 97 schools, 5,201 students, two years.
`MEASURED-RCT`

Spanish **+0.077** (0.076); Math **+0.088** (0.109); Total +0.109 (0.104). All eight subject
competencies insignificant.

> "Overall, the program seems to have had little effect on students' test scores… **The main
> reason for these results seems to be the failure to incorporate the computers into the
> educational process.**"
>
> "Despite receiving computers, training, and technical assistance, **the teachers in the program
> simply failed to incorporate the new technology into their classroom teaching**."

#### Plan Ceibal, Uruguay

**de Melo, Machado & Miranda, IZA DP 8489 (2014).** 2,057–2,080 students, 90 primary schools,
2006→2009, individual fixed effects. `MEASURED-RCT` (quasi-experimental panel)

The naive specification finds math **+0.162** (0.061). The preferred specification, adding
school-time dummies to absorb a differential regional trend in teacher seniority, gives reading
**−0.003** (0.398) and math **−0.160** (0.353).

> "Our results suggest that **in the first two years of its implementation the program had no
> effects on math and reading scores**. The zero effect could be explained by the fact that the
> program **did not involve compulsory teacher training** and that laptops in class are mainly
> used to search for information on the internet."

68% of students said the most frequent classroom use was "looking for information on the net."
**85.8% of school principals said the programme had a positive impact on learning.** Set those two
numbers beside the measured nulls and you have the entire epistemology of this section in one
row: **perceived impact and measured impact are uncorrelated, and perceived impact is what gets
reported.**

*(Note: the brief for this research cited IZA DP 6519 for this study; that number is a different
paper entirely. The correct identifier is **8489**.)*

#### OLPC, Nepal

**Sharma, "Can Computers Increase Human Capital in Developing Countries? An Evaluation of Nepal's
One Laptop per Child Program," AAEA 2014.** 26 programme schools, 39 controls, six districts,
9,509 observations. `MEASURED-RCT` (quasi-experimental DiD)

Combined English+math **−0.32** (marginal); English alone **−0.41** (significant). Grade-4 English
**−0.513** (0.245); grade-5 English **−0.460** (0.175).

> "The exposure to computer-assisted learning in Nepal **had no impact or a negative impact** on
> student learning, non-cognitive skills and attendance."

The paper contains a section headed **"Possible Reasons for No Effect (or Negative Effects) on
Test Scores."**

#### The two authoritative syntheses

**Escueta, Quan, Nickow & Oreopoulos, "Education Technology: An Evidence-Based Review," NBER WP
23744 (2017).** `MEASURED-META`

> "We found that **simply providing students with access to technology yields largely mixed
> results**. At the K-12 level, much of the experimental evidence suggests that **giving a child a
> computer may have limited impacts on learning outcomes**, but generally improves computer
> proficiency…"
>
> "…**no significant impact—positive or negative—was found on homework time, grades, standardized
> test scores, attendance**, or several other outcomes."

**Bulman & Fairlie, "Technology and Education: Computers, Software, and the Internet," NBER WP
22237 / *Handbook of the Economics of Education* Vol. 5 (2016).** `MEASURED-META`

> "…much of the evidence in the schooling literature is based on interventions that provide
> **supplemental** funding for technology or additional class time, and thus **favor finding
> positive effects. Nonetheless, studies of ICT and CAI in schools produce mixed evidence with a
> pattern of null results.**"

Read that carefully. **The designs were biased toward finding an effect — extra money, extra time,
no substitution away from other inputs — and they still came back null.** Bulman & Fairlie add a
methodological observation that is bleaker than any single estimate: "relatively little attention
is given in the literature to heterogeneity in treatment effects by student characteristics,
**which is likely due in part to the finding of no effect overall in many studies**." The
literature is so null that subgroup analysis was never motivated.

#### The dissenting meta-analysis, and why it does not rescue the case

**Zheng, Warschauer, Lin & Chang, "Learning in One-to-One Laptop Environments: A Meta-Analysis and
Research Synthesis," *Review of Educational Research* 86(4), 2016, doi:10.3102/0034654316628645**
reviews 65 articles and 31 dissertations and reports "significantly positive average effect sizes
in English, writing, mathematics, and science." `MEASURED-META`

**The pooled effect sizes by subject could not be retrieved** — SAGE 403, no OA location in
Unpaywall, publisher-elided on Semantic Scholar, institutional repositories behind Cloudflare.
They are therefore **not quoted here, and should not be quoted by anyone who has not read them.**

Two things are worth saying about this paper anyway, because it is where the "1:1 laptops work"
claim usually traces to. First, the achievement meta-analysis pools **only 10 studies**, drawn
largely from education-research journals and dissertations. Second, its conclusion is in direct
opposition to the economics literature above, which applies much stricter causal-inclusion
criteria. **The divergence is itself the finding: whether 1:1 laptops "work" is almost entirely a
function of what you are willing to count as evidence.** `OBSERVED`

### 7.2 Counting the negatives

The project's editorial standard asks for at least one documented negative or null per section.
This section supplies, from primary sources with verbatim quotes:

| # | Study | Result |
|---|---|---|
| 1 | Cristia et al. 2017, Peru | **+0.003 SD** combined; effects >0.11 SD ruled out at 5% |
| 2 | Cueto et al. 2025, Peru 10-yr | Academic index **−0.046**; **grade progression −0.010, p<0.05** |
| 3 | Beuermann et al. 2015, Lima | **Academic effort −0.05**, reading time −0.06 |
| 4 | Malamud & Pop-Eleches 2011, Romania | **Grades −1/3 SD** across three subjects |
| 5 | Angrist & Lavy 2002, Israel | 4th-grade maths **−0.20 to −0.43 SD** |
| 6 | Barrera-Osorio & Linden 2009, Colombia | Null; >0.2 SD rejected at 10% |
| 7 | de Melo et al. 2014, Uruguay | Null under the preferred specification |
| 8 | Sharma 2014, Nepal | English **−0.41 SD**; grade-4/5 English −0.46 to −0.51 |
| 9 | Escueta et al. 2017 | Access-to-technology: null on grades, test scores, attendance |
| 10 | Bulman & Fairlie 2016 | "a pattern of null results" **despite designs biased toward effects** |

**Ten documented null-or-negative results, eight of them with control groups and point
estimates.** Any claim in this survey that AI extends reach must be made in the presence of this
table.

### 7.3 The survivors: instruction targeted to the learner's actual level

Against ten nulls, set the interventions that worked. Same countries, often the same children,
frequently the same hardware.

#### Teaching at the Right Level

**Banerjee, Cole, Duflo & Linden, "Remedying Education: Evidence from Two Randomized Experiments
in India," *QJE* 122(3), 2007, doi:10.1162/qjec.122.3.1235.** Vadodara and Mumbai, 2001–04;
122 + 77 primary schools. `MEASURED-RCT` (table values from NBER w11904; the QJE PDF is paywalled)

| Arm | Year 1 | Year 2 |
|---|---|---|
| **Balsakhi remedial tutor** (total score) | **+0.135** (0.047) | **+0.267** (0.062) |
| **Computer-assisted learning** (math, value-added) | **+0.394** (0.074) | **+0.347** (0.076) |
| CAL, language | — | **−0.040** (0.085) → **null** |

Treatment-on-treated for children who actually attended balsakhi classes: **0.6–1.0 SD**.
Cost: balsakhi **US$2.25/child/year**; CAL **US$15/child/year** — "the Balsakhi program is 5.9
times more cost-effective for math and 7.5 times more cost-effective for the total score."

**Two findings inside this trial that matter more than the headline:**

1. **Classmates who stayed in the now-smaller regular class posted no gains.** Reducing class size
   by removing the weakest children did nothing for the ones who remained. **The effect came from
   the targeted instruction, not from the resource.** This is the 2007 statement of the rule this
   whole section is about.
2. **Fade-out is real and it is fast.** One year after the programme ended: balsakhi effect on all
   children **+0.023 (0.045), insignificant.** For the bottom third it persisted at **+0.102
   (0.040)**. CAL math **+0.097 (0.053)**. "The gains erode relatively quickly over time."
   `MEASURED-RCT` — and a direct warning to every six-week AI trial in B2's scoreboard that never
   ran a delayed post-test.

#### Mindspark — adaptive software, Delhi

**Muralidharan, Singh & Ganimian, "Disrupting Education? Experimental Evidence on
Technology-Aided Instruction in India," *AER* 109(4), 2019, doi:10.1257/aer.20171112.**
619 students, individually randomised, 4.5 months. `MEASURED-RCT`

> "Lottery winners scored **0.37σ higher in math and 0.23σ higher in Hindi** over just a
> **4.5-month** period. IV estimates suggest that attending the program for 90 days would increase
> math and Hindi test scores by **0.6σ and 0.39σ** respectively."

Cost at pilot scale: ~US$15/student/month. **At scale above 1,000 schools, marginal cost falls to
~US$2 per pupil per year.**

#### Phone tutorials — the result that most directly bears on reach

**Angrist, Bergman & Matsheng, "Experimental evidence on learning using low-tech when school is
out," *Nature Human Behaviour* 6(7), 2022, doi:10.1038/s41562-022-01381-z.** 4,550 Botswanan
households, three arms. `MEASURED-RCT`

| Arm | Effect (SD) | SE | p |
|---|---|---|---|
| **SMS only** | **+0.024** | (0.046) | **0.602 — null** |
| **Phone call + SMS** | **+0.121** | (0.046) | **0.008** |
| Difference | +0.097 | | 0.033 |
| TOT (full participation) | **+0.167** | 95% CI [0.046, 0.289] | 0.007 |

Cost **US$5/child** (SMS) and **US$19/child** (phone+SMS) → **0.63–0.89 SD per US$100**, against a
literature average of "around **0.1 standard deviation per US$100**." Also a **31% reduction in
absolute innumeracy**.

**Replicated across five countries.** Angrist et al., NBER WP 31208 (2023, rev. 2025), India,
Kenya, Nepal, Philippines, Uganda, N = 8,902: `MEASURED-RCT`

| Arm | Pooled effect | SE |
|---|---|---|
| SMS messages | +0.083 | (0.027) — but **null in Kenya and Nepal** |
| **Phone call + SMS** | **+0.327** | (0.025) |

> "…average effects of **0.30–0.35 standard deviations**… **3.9 LAYS per $100, ranking among the
> top 10 out of 150 education interventions reviewed**."

And the delivery-model finding that closes the "but who runs it" objection: NGO-delivered
**0.26 SD**, **government-teacher-delivered 0.31 SD**, "similar and statistically
indistinguishable." Scale-up in Karnataka reached **>25,000 teachers** and ~100,000 students
(evaluated by difference-in-differences, not randomised — `OBSERVED`, not `MEASURED-RCT`).

#### Structured pedagogy

**Snilstveit et al., 3ie Systematic Review 24 (2015)**, 21 studies across 12 countries.
`MEASURED-META`

> "**Structured pedagogy programmes have the largest and most consistent positive average effects
> on learning outcomes**… an overall effect of **0.23 (95% CI [0.13, 0.34])**" for language arts;
> maths **0.14 [0.08, 0.20]**.

#### The adaptivity coefficient

**Evans & Popova, "What Really Works to Improve Learning in Developing Countries?", *World Bank
Research Observer* 31(2), 2016, doi:10.1093/wbro/lkv026**, reporting Conn (2014)'s Africa
meta-analysis: `MEASURED-META`

| | Pooled effect |
|---|---|
| **Adaptive instruction** | **0.42 SD** |
| **Non-adaptive instruction** | **0.12 SD** |

**A 3.5× difference, from the same delivery channel, distinguished only by whether the instruction
adapted to the learner.** McEwan (2015): CAL mean **0.15 SD**. Kenya ability-grouping (Kremer,
Duflo & Dupas 2011): **+0.17 SD language, +0.16 SD math**, "with results carrying over into the
next school year after the program had stopped."

### 7.4 The survivors have their own graveyard — and it is about delivery, not design

The most important thing in this section is that **Teaching at the Right Level itself fails when
the delivery model does not execute.** Banerjee, Banerji, Berry, Duflo, Kannan, Mukerji, Shotland
& Walton, *JEP* 31(4), 2017 / NBER w22746: `MEASURED-RCT`

| Experiment / arm | Language | Math |
|---|---|---|
| Bihar summer camp (govt teachers) | +0.087 (0.042)* | +0.074 (0.044)* |
| **Bihar — materials only** | **+0.017 (0.039) NULL** | **+0.041 (0.041) NULL** |
| **Bihar — training + materials** | **+0.043 (0.038) NULL** | **+0.015 (0.039) NULL** |
| Bihar — training + materials + volunteers | +0.125 (0.035)*** | +0.105 (0.037)*** |
| **Uttarakhand — training + materials** | **+0.064 (0.041) NULL** | **+0.059 (0.045) NULL** |
| **Uttarakhand — training + materials + volunteers** | **+0.012 (0.031) NULL** | **+0.025 (0.044) NULL** |
| Haryana TaRL (dedicated hour) | +0.154 (0.017)*** | **−0.006 (0.017) NULL** |
| **UP — 10-day learning camps** | **+0.701 (0.022)*** | **+0.694 (0.024)*** |

> "The materials-alone and materials-plus-training interventions had **no effect in either Bihar or
> Uttarakhand**. The materials-training-volunteers treatment in Uttarakhand had **no detectible
> impact either**."
>
> "In the first two instances (Bihar and Uttarakhand), the methodology was **not adopted by
> government schoolteachers**, despite well-received training sessions and Pratham support."

The process data explains it: in Haryana "over 90 percent of schools were grouped by learning
levels" and teachers used the materials in 81% of classes; grouping "largely failed in Bihar and
Uttarakhand." **The same intervention ranges from +0.70 SD to a precise zero depending entirely on
whether the adults in the room actually did it.**

J-PAL's own policy insight states the rule without hedging: `OBSERVED`

> "**Simply training teachers in the approach or providing the teaching materials alone does not
> improve learning outcomes.**"

Three further nulls from the low-tech literature, because the phone channel is not magic either:

| Study | Result |
|---|---|
| **Crawfurd, Evans, Hares & Sandefur, "Live tutoring calls did not improve learning during the COVID-19 pandemic in Sierra Leone," *J. Dev. Econ.* 164 (2023)**, 4,399 students | **Maths −0.008 (0.034), language −0.027 (0.034).** "We can rule out effects larger than **0.08 SD in mathematics and 0.05 SD in language**." Child educational-activity index rose **+0.29 SD** — **activity without learning.** `MEASURED-RCT` |
| **Afoakwah et al., IVR in Ghana (EdTech Hub, 2021)**, 1,359 students | "**No significant effect was found on students' math skills**… engagement was a significant challenge." Only place value moved, +5%, significant at 10% only. `MEASURED-RCT` |
| **Botswana / Kenya / Nepal, SMS-only arms** | Botswana +0.024 (0.046), p = 0.602; **null in Kenya and Nepal** in the five-country replication. `MEASURED-RCT` |

And the pooled CAL verdict that should be pinned above every AI-tutoring product roadmap
(Snilstveit et al. 2015, 18 studies, 9 countries): `MEASURED-META`

> "Based on the studies included in the review **it is not clear that the overall effect of CAL on
> children's learning is beneficial**. The overall average effect… range from **−0.01 SMD for
> language test scores (95% CI [−0.08, 0.05]) to 0.07 SMD for maths test scores (95% CI [0.02,
> 0.11])**."

**That is the field's honest pooled estimate for computer-assisted learning: between −0.01 and
+0.07 SD.** The 0.37s and 0.47s are the tail, not the mean.

#### The cleanest single test of "does the device tier matter?"

**Piper, Zuilkowski, Kwayumba & Strigel, "Kenya's ICT Policy in Practice: The Effectiveness of
Tablets and E-Readers in Improving Student Outcomes," *FIRE* (2015)** — an RCT inside the PRIMR
literacy programme that randomised **three different hardware tiers** on top of the same
instructional reform: tablets for instructional supervisors, tablets for teachers, and e-readers
for students. `MEASURED-RCT`

> "**All three showed significant impacts in English and Kiswahili above the results of the control
> group. The impacts of the three interventions were not statistically significantly different from
> each other.** … we recommend that Kenyan policy makers **embed ICT interventions in a larger
> instructional reform**, using ICT to support particular instructional improvement challenges."

**Three hardware tiers, one instructional reform, indistinguishable results.** Giving every child
an e-reader performed no better than giving a tablet to the person who supervises the teacher.
This is as close to a controlled dissection of "device versus instruction" as the literature
contains, and the device term is zero.

### 7.5 The rule, and the reason it is the most important paragraph in this section

The consensus panel states it as a purchasing decision. **GEEAP, "2023 Cost-Effective Approaches to
Improve Global Learning," World Bank (2023)** — a systematic search over 13,000+ studies, 550+
evaluations: `MEASURED-META`

> **Bad Buys, first item: "Investing in hardware like laptops, tablets and computers alone."**
>
> "As with other inputs, **investing in hardware alone is a bad buy**. When not accompanied by
> well-thought-out complementary measures—including personalized adaptive software and teacher
> training on how to use the software—**adding computers has had no impact at all in Peru,
> Colombia, and many other countries, or negative impacts on learning outcomes (Israel, Costa
> Rica)**."
>
> **Great Buys** include "**targeting teaching instruction by learning level, not grade (in or out
> of school)**" and "supporting teachers with structured pedagogy."

And Kremer, Brannen & Glennerster, *Science* 340(6130), 2013, doi:10.1126/science.1235350
(abstract via PubMed 23599477; full text unreachable, 403): `MEASURED-META`

> "…**among those in school, test scores are remarkably low and unresponsive to more-of-the-same
> inputs**, such as hiring additional teachers, buying more textbooks, or providing flexible
> grants. In contrast, **pedagogical reforms that match teaching to students' learning levels are
> highly cost effective at increasing learning**."

**The rule:**

> **Distributing capability produces null effects. Targeting instruction to the learner's measured
> level produces 0.14–0.70 SD. The device is not the variable. The targeting is the variable —
> and the delivery model is the thing that decides whether the targeting actually happens.**

### 7.6 The finding that answers the gap-widening objection

This is, I think, the single most useful result in this whole section, and it emerges only when
the two literatures are put side by side.

**§10's Premise 2 establishes that LLM tutoring widens gaps** — Sierra Leone +0.195 SD of effect
per SD of baseline, Nigeria +0.151, Lehmann's "LLMs widen the gap between students with low and
high prior knowledge." Three studies, same sign.

**Now look at the heterogeneity of the interventions that were designed around targeting:**

| Study | Who gained most? |
|---|---|
| **Balsakhi, year 2** (Banerjee et al. 2007) | **Bottom third +0.427** (0.084); middle +0.340; **top third +0.217** (0.081). Gains *decrease* with baseline. |
| **Balsakhi, one-year fade-out** | All children +0.023 **(ns)**; **bottom third +0.102 (0.040), still significant.** The only durable effect was on the weakest. |
| **TaRL, Haryana** (w22746, by baseline level) | Nothing **+0.167**; Letter **+0.169**; Word/Para +0.132; **Story +0.029 (ns)**. |
| **TaRL, UP 10-day camps** | Nothing **+0.771**; Letter **+0.792**; Word/Para +0.446; **Story +0.048**. |
| **Mindspark** (Muralidharan et al. 2019) | Similar *absolute* gains at every percentile — but **much larger relative gains for weak students**, because "we **cannot reject the null of no increase in test scores for the bottom-third of students in the control group**… lower-performing students appear to **make no academic progress under the status quo**." |
| **Pratham CAL** (Banerjee et al. 2007) | Bottom +0.417; middle +0.341; top +0.319 — "equally effective for all students." |
| **Botswana phone tutorials** (Angrist et al. 2022) | "**Limited evidence of heterogeneity**… the programme works equally well across these subpopulations." |
| **Kenya ability grouping** (Kremer, Duflo & Dupas 2011) | "**Even for low-performing students**… ability grouping improved student performance by **0.16 SD**." |

**Not one of the targeted interventions widens gaps. Several narrow them sharply. The
gap-widening finding is not a property of technology, and it is not a property of tutoring. It is
a property of *untargeted* delivery.** `INFERENCE` over `MEASURED-RCT` ×8 — and it is the
strongest available reconciliation of the two literatures.

The mechanism is not mysterious. TaRL's whole design is to *diagnose the child's actual level and
teach at it*, which by construction gives the most instruction to the child furthest behind. An
unconstrained chatbot does the opposite by construction: it answers the question it is asked, at
the level it is asked, and a strong student asks better questions. Bastani et al.'s guarded arm
(unassisted-exam effect **−0.004, ns**) versus its unguarded arm (**−17%, p<0.05**) is the same
mechanism observed inside a single trial.

**Design consequence, stated as a specification rather than an aspiration:** an AI tutor that does
not *measure the learner's level and constrain itself to it* is, on this evidence, expected to
widen gaps. An AI tutor that does is expected to narrow them. **This is the most falsifiable and
most testable claim in this section, and — per §10.3 — it has not yet been tested.**

---

## 8. The divide, stated precisely — and the one number nobody publishes

§5 measured the divide in the units the sector uses: connectivity, electricity, computers per
school, teachers per pupil, dollars per pupil. Those are the right units for a ministry of
education. They are the wrong units for this survey, because **they all describe the channel and
none of them describes whether the thing arriving down the channel can talk to the child.**

This section adds the missing axis. It is deliberately narrow: device access, electricity and
connectivity are done in §5 and are not repeated. What follows is about **language**, which is
the sharpest edge of the divide and the least discussed, and it ends with a number that, as far
as this research could determine, **has never been published**.

### 8.1 The question the field does not ask

Every multilingual benchmark reports a **per-language** score and, at best, an unweighted mean
across languages. Belebele reports "AVG 50.6" across 122 variants. IrokoBench reports an
"African average." AfriMGSM reports a mean over 17 languages.

**An unweighted mean over languages is a statement about linguistics. It is not a statement about
people.** It weights Santali and Mandarin identically. The question a builder actually needs
answered is the population-weighted one:

> **What fraction of the world's children live in a language a deployed model can actually read?**

Search across the multilingual-evaluation literature located **no benchmark that reports its
coverage weighted by learner population**, and no paper that joins per-language benchmark scores
to school-age demography. `OBSERVED` — this is a negative search result, and the absence is
itself the finding: **the field has optimised, published and celebrated a metric that is
structurally blind to how many humans each language represents.**

So the calculation is done here, from public data, with the method published so it can be
attacked.

### 8.2 Method

Three inputs, all public:

1. **Learner population.** World Bank `SP.POP.0014.TO`, population ages 0–14 by country, latest
   available (2025). World total **2,005,307,782**. `OBSERVED` — World Bank API, retrieved
   2026-07-27.
2. **The top 50 countries by child population**, which together hold **1,722,677,267 children =
   85.9% of the world's 0–14 population**. The tail of ~180 further countries is excluded and is
   discussed as a bias below.
3. **Per-language benchmark scores.** Belebele (Bandarkar et al., ACL 2024, arXiv:2308.16884),
   full per-language results table for 122 language variants, parsed directly from the paper's
   HTML. Two columns are used: **GPT-3.5-turbo, zero-shot** (the widely-deployed-LLM column) and
   **XLM-V-large, translate-train-all** (the fine-tuned 550M-parameter encoder column — the
   "what is achievable with balanced data" upper reference). Random baseline = 25.
   `MEASURED-BENCH`.

Each country is mapped to (a) its **official language(s) of instruction at primary level** and
(b) the **first language(s) its children actually speak at home**, with population weights. India
is split across twelve languages using Census-2011 mother-tongue shares; multilingual countries
are split proportionally; the full mapping is reproduced in §8.6 so that every judgement in it is
visible and correctable.

Scores are bucketed:

| Bucket | Belebele score | Interpretation |
|---|---|---|
| **Functional** | ≥ 70 | The model reads the language well enough to be reasoned with |
| **Marginal** | 50–69 | Usable with heavy scaffolding; error rate too high for unsupervised use |
| **Poor** | 35–49 | Materially above chance, materially below usable |
| **Near-chance** | < 35 | Statistically close to guessing (random = 25) |
| **Unmeasured** | — | Language absent from the benchmark entirely |

The join is `INFERENCE` — the inputs are measured, the combination is mine.

### 8.3 Result A — the official language of instruction

Widely-deployed-LLM column (GPT-3.5-turbo), weighted by children:

| Bucket | Children | % of top-50 | % of world 0–14 |
|---|---|---|---|
| **Functional (≥70)** | **956,981,625** | **55.6%** | 47.7% |
| Marginal (50–69) | 193,254,451 | 11.2% | 9.6% |
| Poor (35–49) | 396,597,037 | 23.0% | 19.8% |
| Near-chance (<35) | 144,619,349 | 8.4% | 7.2% |
| Unmeasured | 31,224,805 | 1.8% | 1.6% |
| **Learner-weighted mean Belebele** | **67.2** | | |

**Read on official language of instruction, the picture looks tolerable: 66.8% of children are in
a language scoring ≥50, and the learner-weighted mean (67.2) is 16.6 points above the benchmark's
own unweighted mean of 50.6.**

That gap is the whole story of this section, and it is not good news. **The population-weighted
average is higher than the language-weighted average precisely because the well-served languages
are the ones with hundreds of millions of speakers — and, in the postcolonial world, the ones
imposed as media of instruction.** English (87.7), French (83.1), Portuguese (83.0), Spanish
(79.2) and Modern Standard Arabic (69.3) are all functional or near-functional. They are also, for
a very large number of the children counted in that 55.6%, **languages the child does not speak.**

### 8.4 Result B — the language the child actually speaks

Same method, same benchmark, same weights; the only change is that each country's children are
mapped to their **home** language rather than the school's:

| Bucket | Children | % of top-50 | % of world 0–14 |
|---|---|---|---|
| **Functional (≥70)** | **529,463,904** | **30.7%** | **26.4%** |
| Marginal (50–69) | 171,067,107 | 9.9% | 8.5% |
| Poor (35–49) | 362,332,492 | 21.0% | 18.1% |
| Near-chance (<35) | 285,261,010 | 16.6% | 14.2% |
| **Unmeasured** | **374,552,754** | **21.7%** | 18.7% |
| **Learner-weighted mean Belebele** | **58.0** | | |

**The headline of this section:**

> **On the language a child actually speaks, fewer than one in three of the world's children
> (30.7%) live in a language a widely-deployed LLM reads at a functional level. More than one in
> five (21.7%, ≈375 million children) speak a language for which no score exists at all —
> the language is not in the benchmark.** `INFERENCE` over `MEASURED-BENCH` + `OBSERVED`.

Set the two results side by side:

| | Official language of instruction | Child's home language | Gap |
|---|---|---|---|
| Functional (≥70) | 55.6% | **30.7%** | **−24.9 pp** |
| ≥50 (usable-with-help) | 66.8% | 40.6% | −26.2 pp |
| Below 50 | 31.4% | 37.6% | +6.2 pp |
| **Unmeasured** | 1.8% | **21.7%** | **+19.9 pp** |
| Learner-weighted mean | 67.2 | 58.0 | −9.2 |

**The 24.9-point gap between the two columns is not a measurement artefact. It is the measured
size of the language-of-instruction problem, expressed in children.** Roughly **427 million
children** sit in the difference: children whose school runs in a language a model handles well
and whose life runs in a language it does not.

This has a consequence that reverses the naive procurement instinct. A ministry benchmarking
candidate models in the official medium of instruction — English in Nigeria, French in the DRC,
Portuguese in Mozambique — **will measure the model at its best and the child at their worst,
and will conclude the model is ready.** The evaluation will be technically valid and
substantively misleading. `INFERENCE`, and stated as a warning rather than a finding.

### 8.5 What the fine-tuned-encoder column proves

The same computation, run against Belebele's **XLM-V-large translate-train-all** column — a
**550-million-parameter** encoder fine-tuned with balanced multilingual data, i.e. roughly
1/300th the scale of a frontier model:

| Bucket | Home language, GPT-3.5 | Home language, XLM-V-large | Change |
|---|---|---|---|
| Functional (≥70) | 30.7% | **35.0%** | +4.3 pp |
| Marginal (50–69) | 9.9% | **39.5%** | **+29.6 pp** |
| Poor (35–49) | 21.0% | 3.1% | −17.9 pp |
| **Near-chance (<35)** | **16.6%** | **1.3%** | **−15.3 pp** |
| Unmeasured | 21.7% | 21.1% | −0.6 pp |
| Learner-weighted mean | 58.0 | **66.3** | **+8.3** |

**Three findings, in ascending order of importance:**

1. **The near-chance population collapses from 16.6% to 1.3% of children — from ~285 million to
   ~22 million.** A half-billion-parameter model with the right data pulls 263 million children
   out of the "the model is guessing" bucket that a frontier-scale system leaves them in. This is
   the §3.2 finding (XLM-R beats GPT-3.5 by 32 points on Amharic) restated in units of people.
   `INFERENCE` over `MEASURED-BENCH`.
2. **The combined below-50 population falls from 37.6% to 4.4%.** Whatever is wrong with model
   coverage of the world's languages, **it is not a capability ceiling.** It is a data-allocation
   choice, and it is reversible at a parameter scale that runs on the hardware §4.3 says a
   school can actually afford.
3. **The unmeasured 21.7% barely moves — 21.7% → 21.1%.** This is the part that scale cannot
   fix and fine-tuning cannot fix, because **you cannot fine-tune on a language that is not in
   your evaluation set and not in your corpus.** ~363 million children sit behind a wall that is
   made of missing data, not missing compute. That number is the single best answer this survey
   has to "what would you spend the next billion dollars on."

**The specific languages that hit the wall.** Of the languages of instruction or home languages
identified across the top-50 countries, **fifteen are absent from Belebele's 122 variants
entirely**: Dari, Kikongo, Tshiluba, Kirundi, Bemba, Mooré, Twi/Akan, Ewe, Kimbundu, Umbundu,
Kanuri, Venda, Southern Ndebele, Tumbuka, and the aggregate "other" categories for Côte d'Ivoire,
Cameroon and Chad. `OBSERVED` — direct check against the parsed benchmark table.

A further case deserves its own line because it is a pure reporting gap rather than a coverage
gap: **Odia (`ory_Orya`) — roughly 35 million speakers, an official language of an Indian state —
has a blank cell in Belebele's GPT-3.5 column.** The Llama-2 and XLM-V columns are populated;
the deployed-model column is not. `OBSERVED`. Thirty-five million people, no published number.

### 8.6 The mapping, published so it can be attacked

The country→language assignments are the weakest link in §8.3–§8.5 and are therefore given in
full. They are my coding, from standard census and official-language sources; they were **not**
retrieved from a machine-readable authority, because no open API supplying "language of
instruction by country, weighted" was located during this research. That absence is worth its own
line: **the denominator of the most important equity question in multilingual AI is not published
in machine-readable form anywhere this research could reach.** `OBSERVED`.

| Country | Children 0–14 | Coded language(s) of instruction | Coded home language(s) |
|---|---|---|---|
| India | 354.2M | 12 state languages + English, Census-2011 shares | same |
| China | 216.7M | Mandarin | same |
| Nigeria | 96.2M | English | Hausa .30 / Yoruba .21 / Igbo .18 / Fulfulde .07 / other .24 |
| Pakistan | 92.5M | Urdu .75 / English .25 | Punjabi .39 / Pashto .18 / Sindhi .15 / Urdu .08 / other .20 |
| Indonesia | 69.3M | Indonesian | Javanese .40 / Indonesian .20 / Sundanese .15 / other .25 |
| United States | 58.4M | English | same |
| Ethiopia | 52.5M | Amharic .35 / Oromo .34 / Somali .06 / Tigrinya .06 / other .19 | same |
| DR Congo | 51.8M | French | Swahili .25 / Lingala .25 / Kikongo .20 / Tshiluba .20 / other .10 |
| Bangladesh | 48.6M | Bengali | same |
| Brazil | 41.3M | Portuguese | same |
| Egypt | 37.4M | Modern Standard Arabic | Egyptian Arabic |
| … | … | *(full 50-row mapping in the analysis script)* | |

Script: `langreach.py`, three inputs (`SP.POP.0014.TO`, the World Bank country/aggregate filter,
and the parsed Belebele table), ~120 lines, deterministic, re-runnable.

**Four ways this estimate is wrong, stated before someone else states them:**

1. **The benchmark model is stale.** GPT-3.5-turbo is a 2023 system. Frontier 2026 models are
   materially better on low-resource languages — §3.3 shows o200k cut Telugu tokenizer fertility
   from 8.22× to 1.92×, and §3.2's IrokoBench numbers have GPT-4o at 59.0 on AfriMMLU against
   Claude Opus's 42.3. **But no 2026 frontier model publishes a per-language table at 122-language
   coverage.** The choice was: report a stale number with full coverage, or report no number.
   Reporting no number is what the field already does. **This is therefore a floor, and the more
   important finding is that a current ceiling cannot be computed from public data.** `OBSERVED`.
   A supporting check: an arXiv sweep of the most recent low-resource-language benchmark papers
   (submitted 2026-06-30 to 2026-07-24) returns almost entirely **single-language, narrow-task**
   datasets — Bangla form comprehension, Bangla hate speech, Sinhala aspect sentiment, Pharo code
   completion. **Not one broad-coverage per-language scoreboard for a current frontier model
   appears in the recent literature.** The field is producing depth on individual languages, which
   is valuable, and has stopped producing the breadth-wise scoreboard that would let anyone
   compute §8.4 against a 2026 system. `OBSERVED` — arXiv API, retrieved 2026-07-27.
2. **Belebele is reading comprehension, not tutoring.** §4.2 establishes that benchmark capability
   and pedagogical ability are close to decoupled — Phi-3 has MMLU 68.8 and pedagogical guidance
   17.71. A language scoring 70 on Belebele is *necessary* for tutoring in that language and
   nowhere near *sufficient*. Every number in §8.3–§8.5 is an upper bound on tutoring reach.
3. **The top-50 cutoff biases the estimate optimistically.** The 180 excluded countries are
   smaller, poorer and more linguistically fragmented on average. Including them would move
   children out of the functional bucket and into the unmeasured one.
4. **Home-language shares are coded, not measured.** Where a country's linguistic composition is
   contested or unenumerated I coded a residual "other" bucket into `unmeasured`, which is
   conservative in the direction of the section's own thesis. Readers who disagree should change
   the weights and re-run; the direction of the two headline results (B ≪ A; XLM-V ≫ GPT-3.5 at
   the bottom of the distribution) survives any plausible reweighting, because it is driven by
   the arithmetic difference between colonial and vernacular languages, not by the decimals.

### 8.7 Why this is the highest-leverage finding in the section

Line up what the recovered sections established against what §8 adds:

- §1: tokens are getting cheap on a schedule. **Insensitive to language.**
- §2: devices and bandwidth are the cost floor. **Insensitive to language.**
- §5: 2.2 billion people are offline; 1.8–1.9 billion of them are under a signal they do not use.
  **Insensitive to language.**
- §3 + §8: for 37.6% of the world's children, the model cannot read the language they think in —
  and for 21.7%, nobody has checked. **This one is not insensitive to anything. It is the only
  barrier in the list that a specific, bounded, fundable engineering programme removes.**

§3.7 observed that the frontier of *serving* low-resource languages has passed from model-builders
to benchmark-builders — Masakhane, AI4Bharat — and framed that as a retreat. §8 reframes it as an
**opportunity with a price tag attached**: Sarvam-1 (§3.7) is a **2B** model whose Indic tokenizer
gets Telugu fertility to 1.16×; InkubaLM is **0.4B** across five African languages; XLM-V-large is
**0.55B** and pulls 263 million children out of the guessing bucket. **The interventions that
close this gap are all two to three orders of magnitude smaller than a frontier training run.**

That is what it means to say the constraint is structural rather than financial. The money is not
the problem. **The problem is that the data for 363 million children's languages does not exist,
and nobody's benchmark scoreboard penalises them for that, because the scoreboard averages over
languages and not over people.**

---

## 9. Who is currently unreached — and what is actually in the way

The productive move is to stop asking "how many people are offline" and start asking, population
by population, **what specific thing stops this person learning, and does abundant attention
touch it?** Some barriers dissolve the moment a patient, competent, unlimited tutor exists. Some
are completely untouched by it. Confusing the two is how the sector has repeatedly spent a decade
solving the wrong term.

### 9.1 The populations, with the barrier named

#### Learners with disabilities — the empty chair

This survey's companion report H1 conducted a reproducible census of ERIC and Europe PMC on
2026-07-27 and found:

> **Zero randomised controlled trials of generative-AI tutoring on students with disabilities.**
> Of 30 GenAI-education RCTs indexed in Europe PMC that mention students, **0** mention
> disability, dyslexia, ADHD, autism, special education, or IEPs. The entire world literature on
> AI interventions for students with learning disabilities, 2022–2025, across seven databases, is
> **11 studies / 10 independent experiments / 3,033 participants**, of which **at most one is an
> RCT (n = 60)**, and **none** was rated low risk of bias. All 11 reported positive results — a
> publication-bias signature. `MEASURED-BENCH` (H1's own census) + `MEASURED-META`
> (Paglialunga & Melogno 2025).

H1 also full-text-audited the flagship AI-tutoring RCTs. In Kestin et al. (Harvard physics,
n = 194, effect 0.63 SD), every one of the six hits for `accessib*` means "available at low cost /
anywhere with an internet connection" — **the word *accessibility* never appears in its disability
sense.** In Tutor CoPilot, special-education status appears exactly once, as a covariate to adjust
*away*. `OBSERVED` (H1 full-text audit).

**Barrier: not price. Not connectivity. Not language.** It is (i) an **evidence vacuum** and
(ii) an **interface floor** — WCAG 2.2 AA, screen-reader compatibility, caption quality, latency
tolerance for switch access. Neither is affected by the cost of a token. And H1's F7 gives the
reason this population is the *most* exposed: unconstrained LLM use widens the gap between low-
and high-prior-knowledge learners, so **the expected direction of transfer from typical-learner
effect sizes to this population is negative, not neutral.** `MEASURED-RCT` ×2 (Lehmann et al.;
De Simone et al.).

*Note on prevalence:* the widely-quoted figure of ~240 million children with disabilities
(UNICEF, *Seen, Counted, Included*, 2021) **could not be verified through an accessible source in
this session** — data.unicef.org returned HTTP 403. Reported as unverified rather than restated.

#### Out-of-school children — 272.9 million

§5.5 establishes the number: **272.9 million** out of school (primary 78.6M, lower secondary
63.6M, upper secondary 130.7M), of whom **109.0 million are in Sub-Saharan Africa**, where the
upper-secondary out-of-school rate is **46%**. `OBSERVED` (UIS 2025).

**Barrier: the institution.** Every intervention in §7's evidence base — TaRL, structured
pedagogy, computer-assisted learning, Mindspark — is delivered *through a school*, to children who
are *in* the school. The 272.9 million are, by definition, outside the only delivery mechanism the
literature has ever evaluated. Their barrier is a compound of cost-of-attendance, child labour,
distance, conflict, gender norms, and disability — and for the upper-secondary majority, the
opportunity cost of a teenager's labour.

**This is the population where abundant attention has the most theoretical headroom and the least
evidence**, because a tutor that reaches a phone does not require a building, a timetable, or an
enrolment record. It is also the population where the §5.1 usage gap bites hardest: they are
mostly *under a signal*, and mostly not using it.

#### Refugee, displaced and stateless learners

Retrieved directly from the UNHCR population API, end-2024 reference year, aggregated over all
7 pages of country records on 2026-07-27:

| Category | Population |
|---|---|
| Refugees under UNHCR mandate | **30,958,200** |
| Asylum seekers | 8,352,712 |
| Internally displaced persons | **68,131,711** |
| Others of concern | 3,820,662 |
| Stateless persons | 4,360,087 |
| **Sum of the above** | **~115.6 million** |

`OBSERVED` — api.unhcr.org/population/v1, retrieved 2026-07-27. **Caveat, stated because it
matters:** this API aggregate (~111.3M excluding stateless) is *below* UNHCR's published headline
of ~123 million forcibly displaced for end-2024, because the API's mandate categories exclude
UNRWA-registered Palestine refugees (~6M) and use different inclusion rules. **The API figure is
reported as computed and is not reconciled to the headline.** UNHCR's own education pages, which
carry the enrolment-rate breakdown by level, returned HTTP 403 and **could not be retrieved** —
so no refugee gross-enrolment-rate figure is asserted here. `OBSERVED` (retrieval failure).

**Barrier: legal and documentary, then linguistic.** A displaced child's obstacles are the right
to enrol, a transcript that crosses a border, a curriculum that matches neither origin nor
destination, and **instruction in a host-country language they do not speak** — which lands them
precisely in §8.4's 37.6%. Price is not in the top five.

#### Adults without literacy — ~761 million, and two-thirds of them women

Derived from World Bank indicators, retrieved 2026-07-27:

| Quantity | Value | Source |
|---|---|---|
| World population 2025 | 8,215,424,893 | `SP.POP.TOTL` |
| Share aged 0–14 | 24.41% | `SP.POP.0014.TO.ZS` |
| ⇒ population aged 15+ | **6,210,113,615** | derived |
| Adult literacy rate, world | **87.74%** | `SE.ADT.LITR.ZS` (2024) |
| ⇒ **adults who cannot read** | **~761 million** | derived |
| Male / female literacy, world | 90.91% / 84.59% | `SE.ADT.LITR.MA/FE.ZS` |
| ⇒ **female share of the illiterate** | **~63%** (≈478M women) | derived |
| Adult literacy, low-income countries | **63.57%** (M 70.94 / F **56.42**) | `SE.ADT.LITR.ZS` |
| Adult literacy, Sub-Saharan Africa | **68.69%** (M 74.88 / F **62.66**) | `SE.ADT.LITR.ZS` |
| Youth (15–24) literacy, low-income | 75.39% | `SE.ADT.1524.LT.ZS` |

`OBSERVED` for the indicators, `INFERENCE` for the derived headcounts. (The commonly cited UIS
figure is ~739M for a 2023 reference year; ~761M here is the same quantity computed on 2024–25
data and is consistent with it.)

**In a low-income country, 43.6% of adult women cannot read.** The youth figure (75.4%) says the
pipeline is improving but that a quarter of the *next* cohort is still arriving at adulthood
without literacy.

**Barrier: the interface, and it is the one barrier abundant attention most directly removes.**
For a non-literate adult, **text is not a degraded channel — it is no channel at all.** Speech is
the sole interface. §3.5 is therefore not a footnote for this population; it is the whole story:
Whisper large-v2 sits at **44.3 WER** on the 54-language FLEURS subset it shares with MMS, MMS at
**18.7 WER** — and MMS's training data is ~32 hours per language of **readings of religious
texts**, which is a catastrophic register mismatch for adult-literacy dialogue. There is a second,
sharper barrier that is social rather than technical and that this population's literature is
unanimous on: **an adult will not practise reading in front of a person who can see them fail.**
A private, infinitely patient interlocutor is a mechanistically strong answer to that — and it is
`INFERENCE`, because no trial has tested it.

#### Rural, remote and nomadic learners

§5.1's number is the one to hold: **rural internet use in low-income countries is 14%**, against
an urban–rural ratio in Africa of **2.6** (Europe: 1.1). `OBSERVED` (ITU 2025).

Nomadic and pastoralist populations are the extreme case and are almost absent from the modern
literature. The most concrete figure located: Nigeria's National Commission for Nomadic Education
was established in 1989 to serve **an estimated 9.3 million nomads**, against reported literacy
rates of **0.28% among pastoral nomads and 20% among migrant fishermen** (Federal Ministry of
Education, 2005, as reported in *IRRODL* 2007), and "a critical appraisal of these approaches by
the commission … shows that very few of the schools were actually viable." `OBSERVED` — figures
are two decades old and no current replacement was located, which is itself the finding: **the
least-reached population is also the least-measured.**

**Barrier: physical mobility versus fixed infrastructure.** The school does not move; the
household does. This is the one population for which the store-and-forward and on-device
architectures of §6 are not an optimisation but the only possible design.

#### Incarcerated learners

**Barrier: institutional permission — a hard, deliberate, policy-level prohibition on
connectivity.** This population is the cleanest natural experiment in the whole taxonomy, because
price, coverage, electricity and device cost are all solved inside a prison and **the learner
still cannot reach anything**:

> "The contemporary digital university typically presupposes a level of mobility and access to
> mobile communication technologies which most Australian prisoners cannot access. This article
> examines the immobility of incarcerated students and their attempts to complete tertiary and
> pre-tertiary distance education courses **without direct internet access**." (Farley &
> Hopkins, *Critical Studies in Education*, 2017.) `OBSERVED`

A companion paper adds the verdict that matters for this survey: "**technology-centred approaches
alone will not adequately address the challenges**" faced by incarcerated students in a
digitising university (*Journal of Prison Education and Reentry*, 2014). `OBSERVED`

The prize is well-established even if this session could not verify its exact size. RAND's
congressionally-mandated meta-analysis (Davis, Bozick, Steele, Saunders & Miles, *Evaluating the
Effectiveness of Correctional Education*, RR-266, 2013) concluded that "receiving correctional
education while incarcerated **reduces an individual's risk of recidivating, and improves odds of
obtaining employment after release**." `MEASURED-META` — abstract verified via ERIC (ED558381);
**the report's exact odds ratios could not be retrieved** (rand.org returned HTTP 403; the 2018
*Journal of Experimental Criminology* update is paywalled). The commonly quoted "43% lower odds of
recidivating" is therefore **not asserted here**. An older, independently verified estimate:
Chappell (2003) found a **+0.31 correlation** between post-secondary correctional education and
recidivism reduction across 1990–1999 studies. `MEASURED-META` (ERIC EJ740020).

**An offline, on-device, air-gapped tutor is not a compromise for this population — it is the
only architecture the institution will ever permit.** That is a design specification, and §6's
lineage supplies it.

### 9.2 Ranking the barriers by what abundant attention actually removes

This is the table the reframe was asked for. Ranked from "attention dissolves it" to "attention
does nothing."

| Rank | Barrier | Does abundant attention remove it? | Why |
|---|---|---|---|
| **1** | **Scarcity of adult time and patience** | **Almost completely** | §5.4: 44% teacher absence, ~473 h/child/year of scheduled instruction that does not happen, 7% of teachers meeting minimum subject knowledge. This is *literally* a shortage of competent attention, and it is the one thing an unlimited tutor is. |
| **2** | **Per-learner dosage and diagnostic 1:1 time** | **Largely** | Pupil–teacher ratio 39.8 in low-income countries. Individual diagnosis is the thing that does not scale with staff and does scale with inference. |
| **3** | **Social cost of visible failure** | **Largely, mechanistically** | Adult literacy, disability, over-age learners. No trial has tested it — `INFERENCE` — but a private interlocutor removes the mechanism by construction. |
| **4** | **Language** | **Only if a specific data programme happens** | §8: 37.6% of children below Belebele 50 on their home language; 21.7% unmeasured. Falls to 4.4% with a 0.55B fine-tuned encoder. Zero relationship to inference price. **The highest-leverage tractable barrier.** |
| **5** | **Connectivity / bandwidth / intermittency** | **Partially — and only via a deliberate architecture** | Removable by on-device inference and store-and-forward (§6); *not* removable by cheaper cloud tokens. §5.1: the usage gap is 6× the coverage gap. |
| **6** | **Device access and electricity** | **No** | §2: the silicon the child holds costs 30–300× more per year than the silicon that thinks. §5.2/§5.3: 666M people without electricity; **≤6.9%** of SSA primary schools have both electricity and a computer. Falling token prices move none of this. |
| **7** | **Evidence that it works for *this* learner** | **No — it makes it worse** | H1: zero RCTs on students with disabilities. The gap-widening pattern (§10) means cheap deployment *ahead* of evidence is the specific way this goes wrong. |
| **8** | **Institutional permission** | **No** | Prisons, refugee legal status, ministry procurement, child-safety regimes. A free tutor that is not allowed through the door reaches nobody. |
| **9** | **Physical, sensory and cognitive access to the interface** | **No** | WCAG 2.2 AA, screen readers, switch access, caption quality. Engineering work, unrelated to model cost. |

**The single most important reading of this table:** every barrier a *cheaper model* removes sits
at ranks 1–3, and those are barriers of **quantity of attention**, which is exactly what the
reframe says is now abundant. Everything from rank 4 down is a barrier of **kind** — the wrong
language, the wrong channel, the wrong permission, the wrong evidence, the wrong interface. **The
next decade of reach is won at ranks 4 through 9, and none of it is bought with a price cut.**

---

## 10. The counter-argument, at full strength

This survey's editorial standard requires that the strongest case *against* its own thesis be
stated without softening. Here it is. I have written it as an opposing brief, with citations, and
I have not pulled any punches. The answer follows in §10.2, and it concedes more than it refutes.

### 10.1 The brief against "AI will extend reach"

**Premise 1 — Every prior technology promised exactly this, and the evidence base is a
graveyard.** Radio, television, film, the language lab, the microcomputer, the interactive
videodisc, the laptop, the tablet, the MOOC. Each arrived with the claim that marginal cost was
collapsing and reach was about to become universal. §7 documents what the randomised record says:
a ten-year follow-up of 531 Peruvian rural schools found **no significant effects on academic
performance and some evidence of *negative* effects on grade progression**, with **no effects on
primary completion, secondary completion, secondary academic performance, or university
enrolment** (Cueto, Beuermann, Cristia, Malamud & Pardo, NBER WP 34495, 2025). `MEASURED-RCT`
The same programme's home-laptop arm found beneficiaries "**less likely to read books**" and no
transfer of skill to a standard PC (Beuermann et al., NBER WP 18818, 2013). `MEASURED-RCT`
The prior is not neutral. **The prior is negative, and it is negative from large, well-run,
long-horizon randomised trials.**

**Premise 2 — Gap-widening is not a risk; it is the observed default.** Three independent
studies, three countries, three age bands, three different tools, same sign:

| Study | Heterogeneity finding |
|---|---|
| **Sierra Leone, Gemini Guided Learning** (DeepMind + Fab AI, 2026) | **+0.195 SD of treatment effect per SD of baseline maths** (95% CI [0.074, 0.315], **p = 0.002**) — an order of magnitude more statistically robust than the main effect (p = 0.029). Arithmetically, a student **one SD below the mean gains ≈0.055 SD — nothing.** `MEASURED-RCT` |
| **Nigeria, Copilot/GPT-4** (World Bank, 2025) | **+0.151 SD per SD of baseline**; "the largest effects are for female students, and **those with higher initial academic performance**." `MEASURED-RCT` |
| **Lehmann, Cornelius & Sting** (2024, two preregistered lab experiments) | "**We find no effect of LLMs on overall learning outcomes** … **We also observe that LLMs widen the gap between students with low and high prior knowledge**"; body text: LLMs "**harm** the learning of students with less prior knowledge." `MEASURED-RCT` |

**The populations this section is about — out-of-school children, over-age learners, learners with
disabilities, adults without literacy, children taught in a language they do not speak — are, by
construction, the *low-baseline* tail.** Extrapolating a +0.258 SD headline to them is
extrapolating along a gradient whose slope has been measured, and whose slope points the wrong
way. "Extending reach" and "widening gaps" are, on this evidence, **the same operation described
by an optimist and a pessimist.**

**Premise 3 — Without a teacher in the loop, the measured effect is approximately zero.** Gu & Yan
(2025), *JECR*, meta-analysis of 19 studies / 24 effect sizes: overall g = 0.683, but "students
with teacher support in the student–GenAI interaction have significantly larger gains
(**g = 1.426**) than those without teacher support (**g = 0.077**)." `MEASURED-META`
**g = 0.077 is nothing.** Every AI-tutoring result in the corpus that survives scrutiny is a
teacher-designed, teacher-supervised intervention with the model as one component. This is fatal
to the reach argument in its strong form, because **the populations with the least reach are
definitionally the ones with the fewest teachers** — §5.4: a 44-million-teacher gap, 39.8
pupil–teacher ratio in low-income countries, 44% teacher absence, 7% of teachers meeting minimum
subject knowledge.

**Premise 4 — Infrastructure and human capacity are the true binding constraints, and this
section's own data proves it.** §5.3: **at most ~6.9% of Sub-Saharan African primary schools have
both electricity and a computer.** §5.2: 666 million people without electricity, 85% of the
deficit in SSA, 645 million still projected unserved in 2030. §2: the device the child holds
costs 30–300× more per year to keep in the field than the silicon that runs the model. **None of
these curves is bending.** The one that is bending — token price — is the one that was never the
constraint.

**Premise 5 — The correlation runs the wrong way.** Reach is worst exactly where connectivity,
electricity, devices, teachers and language coverage are worst, and those five deficits are
strongly co-located. **The intervention arrives most easily where it is least needed.** §5.1: rural
internet use in low-income countries is 14%; low-income vs high-income internet use is 23% vs 94%.
§8.4: the unmeasured-language population is concentrated in exactly the countries with the lowest
enrolment and the highest learning poverty (SSA learning poverty **89%**).

**Premise 6 — The ceiling is lower than the discourse assumes.** Nickow, Oreopoulos & Quan (2024),
96 randomised studies: intensive in-person human tutoring — the most expensive, best-evidenced
intervention in education — buys **0.288 SD (SE 0.029)**, and the same team's estimate fell from
0.37 to 0.288 between working paper and peer review. VanLehn (2011): human tutoring d = 0.79 and
ITS d = 0.76 — Bloom's two sigma was never real. `MEASURED-META` ×2. **AI tutoring is not
competing against nothing; it is competing against a ceiling of about 0.3 SD, and the field's own
headline number — Wang & Fan's g = 0.867 — was retracted by the publisher in 2026.**

**Premise 7 — And it has never been tested on the people this section is about.** H1's census:
**zero RCTs of generative-AI tutoring on students with disabilities.** `MEASURED-BENCH` No RCT of
an offline or on-device tutor on learning outcomes was located anywhere in §6's search. **The
reach claim is, at this moment, entirely untested on the reach population.**

**Conclusion of the brief:** the honest summary of forty years of evidence is that *hardware
distribution produces null effects, instructional redesign produces effects, and AI is being sold
as hardware.* The reach argument is the OLPC argument with a language model where the laptop was.

### 10.2 The answer — what survives, and what does not

I am going to concede four of the seven premises outright, because they are correct.

**Conceded: Premise 1 is correct as stated, and it is the reason §7 exists.** Hardware
distribution alone produces null effects. This is not in dispute and should not be argued with.
The response is not to deny it but to **stop doing the thing that failed** — and to notice that
the ICT4D record is *not* uniformly null. It is bimodal, and the split is legible: **device
distribution → null; instructional redesign delivered through a device → 0.28–0.59 SD.** That is
the finding of §7 and it is the single most useful thing in this entire section, because it says
the failure mode is **identifiable in advance from the design of the intervention**, not
discoverable only after ten years.

**Conceded: Premise 3 is correct and is the strongest premise in the brief.** g = 0.077 without
teacher support is the number this survey should be most afraid of. **The correct response is
architectural, not rhetorical: build for the teacher-in-the-loop configuration, and treat
unsupervised deployment as the exception requiring justification.** §5.4's uncomfortable
arithmetic cuts both ways — 473 hours per child per year of already-funded instruction does not
happen, *and* only 7% of those teachers meet minimum subject knowledge. The configuration with
evidence behind it is neither "AI replaces teacher" nor "teacher alone." It is **an adult present
with a competent tool** — and Tutor CoPilot is the existence proof, with its **+9 p.p. gain for
students of the lowest-rated tutors**, an equity-positive heterogeneity result that runs opposite
to every other study in Premise 2.

**Conceded: Premise 6 is correct.** The realistic target is ~0.3 SD, not 2 SD. Anything above it,
measured on a researcher-built test over six weeks with no retention check, is a measurement
artefact until proven otherwise. This survey should stop quoting Bloom.

**Conceded: Premise 7 is correct, and it is unanswerable today.** There is no RCT of an AI tutor
with students on IEPs. There is no RCT of an offline or on-device tutor on learning outcomes.
**These are not gaps that argument closes. They are gaps that trials close, and the trials have
not been run.** Any claim about reach to these populations is, right now, mechanistic reasoning —
`INFERENCE` — and must be labelled as such every single time.

Now the three that do not survive intact.

**Premise 2 is real but proves less than it claims — and it contains its own remedy.** The
gap-widening finding is robust and must be designed against. But note *what* was measured in each
case: **unconstrained or lightly-constrained access to a general chatbot.** Bastani et al. is the
decisive datapoint, and it points the other way: the *guarded* configuration (GPT Tutor, with
pedagogical guardrails) produced an unassisted-exam effect of **−0.004 (ns)** while the *unguarded*
configuration (GPT Base) produced **−17%, p < 0.05**. `MEASURED-RCT` **The harm was a property of
the affordance, not of the technology.** Guardrails largely eliminated it. Gap-widening is
therefore a *design defect with a known mitigation*, not a law of nature — and the mitigation is
the same one §7's evidence base has been shouting for twenty years: **target the instruction to
the learner's actual level.**

**§7.6 makes this concrete, and it is the strongest single rebuttal in this section.** Across
eight targeted interventions, **not one widens gaps and several sharply narrow them**: Balsakhi
year 2 gave **+0.427 SD to the bottom third and +0.217 to the top**; the only effect that survived
one-year fade-out was the bottom third's (**+0.102, p<0.05**, against +0.023 ns for everyone);
TaRL in Uttar Pradesh gave **+0.771 SD to children who could recognise nothing and +0.048 (ns) to
children already reading stories**; Botswana's phone tutorials showed "limited evidence of
heterogeneity." **Gap-widening is a property of *untargeted* delivery, not of technology and not
of tutoring.** A system that widens gaps is a system that was not doing Teaching at the Right
Level. That is a fixable engineering specification, and it is *the* specification.

**Premise 4 is correct about the constraint and wrong about the conclusion.** Yes, infrastructure
binds. But the brief assumes the only delivery channel is a connected device in a school with
electricity, and §6 shows that assumption is a choice. The populations behind the infrastructure
wall are reachable by **channels that do not require the wall to fall**: on-device inference
(§4.4's ~3–4B floor, falling — Gemma 4 E2B at 2.3B effective parameters now scores MMLU-Pro 60.0,
where Gemma 3 27B scored 67.5 two generations ago), store-and-forward sync, SMS/USSD/IVR on the
feature phone that is already in the household (§2's scenario F: **$1.75/child/year total**,
requiring no new device at all), and solar-powered shared micro-servers. The right response to
"6.9% of SSA primary schools have electricity and a computer" is not to concede the population;
it is to **stop designing for the 6.9% configuration.**

**Premise 5 is the strongest empirical claim in the brief, and §5.1 refutes its mechanism.** The
correlation is real. But the ITU 2025 decomposition is decisive: **96% of the world's population
is covered by 3G or better and 93% by 4G, while only 74% use the internet.** The coverage gap is
~4% (~312 million people); the **usage gap is ~22 points, roughly 1.8–1.9 billion people who live
under a signal and do not use it — about 6× larger.** `OBSERVED` For 1.8 billion people, the
obstacle is not that the network is absent. It is device, cost-of-data, skills, and **relevance**
— and "relevance" is substantially a euphemism for *there is nothing here in my language that
answers my question*. §8 puts a number on that: 37.6% of the world's children below Belebele 50 in
their home language, 21.7% unmeasured. **The reach problem is more tractable than Premise 5
implies, but only if it is attacked as a content-and-language problem rather than a tower problem.**

### 10.3 What the honest position actually is

Stated as plainly as I can:

1. **The strong claim — "AI will reach everyone" — is not supported and should not be made.** It
   fails on Premises 1, 3, 6 and 7, and no amount of falling token price touches any of them.
2. **The weak claim is supported and is still large: the *channel* problem now has solutions it
   did not have in 2015.** A tutor that runs offline on a shared device, in the learner's own
   language, over a feature-phone voice call, is technically buildable today in a way it was not
   when OLPC shipped. Whether it *teaches* is unmeasured.
3. **The distinguishing variable between forty years of null results and the interventions that
   worked is not the device. It is whether the instruction was targeted to the learner's actual
   level.** §7 establishes this with effect sizes. Every design decision in this survey should be
   audited against it.
4. **The gap-widening default is the specific way this fails**, and it fails hardest on exactly
   the populations §9 names. It is mitigable (Bastani's guarded arm) and it is not mitigated by
   default.
5. **Four things cannot be answered yet, and saying so is not hedging — it is the finding.**
   (a) No trial has measured learning outcomes from an on-device or offline AI tutor. (b) No trial
   has measured AI tutoring on students with disabilities. (c) No trial has measured retention or
   transfer at more than a few weeks in *any* LLM tutoring study. (d) No public per-language
   benchmark exists for a current frontier model at the coverage needed to know whether §8's floor
   has moved. **Each of these is a specific, runnable study. The field's binding constraint is not
   compute or money — it is that nobody has run them.**

---

## 11. What becomes possible

The reframe asks for the forward-looking close: **with attention abundant, what reach problem is
now solvable that was not?** The answer has to be specific, technical, and falsifiable, or it is
just the OLPC press release with a different noun. So: five problems, each with the evidence that
defines it, the mechanism that newly addresses it, and the guardrail in the same breath.

### 11.1 The phone tutorial's human bottleneck — the strongest case, and it is an arithmetic case

This is the most important paragraph in the section, and it follows from §7 rather than from any
claim about AI.

**The single best-evidenced remote-learning intervention in the world is a live human voice on a
phone call.** Five countries, N = 8,902, pooled **+0.327 SD (SE 0.025)**; Botswana **+0.121 SD**
ITT and **+0.167 SD** TOT; **US$11/child**; **3.9 LAYS per $100, top 10 of 150 interventions
reviewed**. `MEASURED-RCT`

**And the decomposition tells you exactly where the effect lives.** In the same trials:

| Channel | Pooled effect |
|---|---|
| SMS content alone | **+0.083 SD** (null in Kenya and Nepal; null in Botswana at +0.024, p=0.602) |
| **SMS + a live human on the call** | **+0.327 SD** |
| **Delta attributable to the live human** | **≈ +0.24 SD** |

J-PAL's synthesis of thirty studies states the mechanism in one sentence: *"Mobile remote
instruction works best when it **supports human interaction rather than one-way content
delivery**… **Making content available is not enough**."* `OBSERVED`

**So the binding constraint on the best remote intervention in the literature is the supply of
people willing and able to have a competent twenty-minute conversation with a child.** §5.4 prices
that constraint: a **44-million-teacher gap**, **~US$120 billion/year** to close, **44% teacher
absence**, **7%** of teachers meeting minimum subject knowledge, **10%** meeting minimum
pedagogical knowledge. The intervention that works is bottlenecked on the input that is scarcest,
and the scarcity is not going to resolve.

**That bottleneck — competent conversational attention, at 20 minutes per child per week — is
precisely and only what abundant inference supplies.** This is not a claim that AI is a good
teacher. It is a claim that the *measured active ingredient* of the best-evidenced remote
intervention is a resource that was rationed and is no longer.

**Guardrail, in the same breath.** This has never been tested. The nearest datapoint is Rori, a
WhatsApp maths tutor in Ghana reporting **0.37 SD** — but with **only 11 school clusters**, no
retention measure, and the developer's own staff as authors (`(D)` on B2's independence scale).
The nearest *negative* datapoint is closer to home: **Crawfurd et al.'s Sierra Leone live tutoring
calls produced −0.008 SD in maths**, with the child-activity index up **+0.29 SD** — the calls
happened, the children engaged, and nothing was learned. **A voice on a call is not the active
ingredient. A competent, targeted voice on a call is.** The specification in §7.5 is not optional
decoration on this claim; it is the claim.

### 11.2 Diagnosis without grouping — the step TaRL fails on

**TaRL's failure mode is now fully characterised and it is administrative, not pedagogical.**
Bihar and Uttarakhand: materials-only, and training-plus-materials, both null; the full package
that produced +0.125 SD in Bihar produced **+0.012 SD in Uttarakhand**. The process data says why:
in Haryana "over 90 percent of schools were grouped by learning levels"; grouping "largely failed
in Bihar and Uttarakhand." `MEASURED-RCT`

**Grouping is the fragile step.** It requires assessing every child, sorting them, physically
reorganising classes, and holding that structure against a timetable, a curriculum, and a head
teacher. It is the step that a system either does or does not do, and when it does not, a 0.70 SD
intervention becomes a 0.01 SD intervention.

**A per-learner tutor removes the step entirely.** Not by being smarter — by making the grouping
cardinality one. There is no sorting to fail at, no class to reorganise, no timetable to defend.
The diagnosis is continuous and private, and the "group" is the learner. **This is the cleanest
example in the section of abundant attention removing a structural rather than financial barrier**,
and it is testable: the prediction is that an AI-delivered TaRL should show *less* implementation
variance across sites than teacher-delivered TaRL, which is exactly the quantity Bihar and
Uttarakhand measured.

**Guardrail.** §4.2's MRBench numbers say the diagnosis is the hard part and small models are bad
at it: guidance **17.71** for Phi-3 against a human expert's **67.19**; actionability **11.98**
against **76.04**. And frontier models detect a misconception behind a correct answer only **57%**
of the time (§4.2). **A system that mis-diagnoses level confidently and fluently is worse than no
grouping at all**, because at least a failed grouping is visible.

### 11.3 An in-language tutor at a parameter scale a school can host

Three measured facts, from three different sections, that only become interesting together:

1. **§8.5** — a **0.55B-parameter** encoder fine-tuned on balanced multilingual data moves the
   below-Belebele-50 child population from **37.6% to 4.4%**, pulling ~263 million children out of
   the near-chance bucket. `INFERENCE` over `MEASURED-BENCH`
2. **§4.1** — **Gemma 4 E2B, at 2.3B effective parameters, scores MMLU-Pro 60.0**, where two
   generations earlier Gemma 3 27B scored 67.5; Qwen reports a comparable ~2× parameter-efficiency
   gain per generation. `MEASURED-BENCH` (vendor model cards — capability only, never pedagogy)
3. **§3.7** — **Sarvam-1 is a 2B model whose Indic tokenizer gets Telugu fertility to 1.16×**,
   better than either mainstream tokenizer; **InkubaLM is 0.4B** across five African languages and
   is "comparable to much larger models" on AfriMMLU/AfriXNLI. `MEASURED-BENCH`

**The conclusion is a build order, not an aspiration.** The model that serves a Telugu- or
Amharic- or Yoruba-speaking learner well is **not** the frontier model rented over a metered
connection. It is a **1–4B model with a language-specific tokenizer and balanced data, resident on
a shared device**, whose serving cost is zero, whose latency is not a network round-trip, and
whose language competence — on the only benchmark with the coverage to check — is *better* than
the frontier model's in exactly the languages that matter most. §3.4 already showed the frontier
model's cost advantage inverts in these languages; §8.5 shows its *capability* advantage inverts
too.

**Guardrail, and it is severe.** §3.5: no openly-benchmarked ASR system is at usable WER for
open-domain educational dialogue in Yoruba, Amharic, or most African languages — Whisper 44.3 and
MMS 18.7 bracket the state of the art on the *easier* 54-language subset, and MMS is trained on
~32 hours/language of religious readings. §4.4: **no study measures learning outcomes for students
using a small on-device tutor at all**, and no study sweeps model size against a fixed pedagogical
benchmark. **Everything in this subsection is a capability claim. None of it is an efficacy
claim.**

### 11.4 Speech as a first-class channel — 761 million adults

For the ~761 million adults who cannot read (§9.1) — **63% of them women; 43.6% of adult women in
low-income countries** — text is not a degraded channel, it is no channel. Speech is the whole
interface. Two things changed: end-to-end speech models exist at a quality that did not, and the
social barrier — practising in front of someone who can see you fail — is dissolved by an
interlocutor that is not a person.

The measured precedent is real but thin: J-PAL's mobile-phone synthesis reports Niger adult
learners at **0.20–0.26 SD** and Zambia SMS short stories at **0.20–0.26 SD**. `OBSERVED` (J-PAL
policy insight, secondary to the underlying trials).

**The specification this implies is concrete and should be written down:** for a
conversational adult-literacy tutor, the binding requirement is not model capability but **ASR
word error rate in the learner's language, on spontaneous non-standard speech, from a
non-literate speaker, over a narrowband voice codec**. Nobody publishes that number. §3.5's 18.7
and 44.3 are read-aloud benchmarks on clean audio; the operational number will be worse. **"What
WER is required for an adult-literacy tutor to work?" is an unanswered, cheap, runnable
experiment**, and it gates everything else in this subsection.

### 11.5 The populations that only an offline architecture reaches

§6 established what runs without a connection. §9 established who is behind the connectivity wall
and *why* — and the important part is that for three of those populations the wall is not going to
come down:

- **Incarcerated learners** — connectivity is prohibited *by policy*, deliberately, and the
  prohibition is the point. §9.1: "attempts to complete tertiary and pre-tertiary distance
  education courses **without direct internet access**." An air-gapped, on-device, auditable tutor
  is not a degraded version of the product for this population. **It is the only version the
  institution will ever admit**, and the prize is a well-established one (RAND RR-266: correctional
  education "reduces an individual's risk of recidivating, and improves odds of obtaining
  employment after release").
- **Nomadic and pastoralist learners** — the household moves and the school does not. §9.1:
  Nigeria's nomadic-education commission, 9.3 million people, reported literacy of **0.28%** among
  pastoral nomads, and "very few of the schools were actually viable."
- **Learners in conflict and displacement** — ~115.6 million people in UNHCR's 2024 categories,
  where infrastructure is not merely absent but actively destroyed.

**For all three, intermittency is not an edge case to be handled gracefully. It is the
steady state**, and a system whose default assumption is a live connection has already excluded
them at the architecture-diagram stage.

### 11.6 What must be true for any of this to be more than a story

Five studies. Each is specific, each is affordable, none has been run, and until they are, every
claim in §11 is `INFERENCE`.

| # | The study | What it settles |
|---|---|---|
| 1 | **RCT of an AI voice tutor against a human phone tutor**, same curriculum, same dosage, same targeting protocol, powered against the 0.327 SD five-country benchmark | Whether the active ingredient of the best remote intervention survives substitution. The single highest-value trial in the field. |
| 2 | **RCT of an LLM tutor with students on IEPs**, with progress monitoring and a published decision rule (H1's recommendation) | Whether any of this transfers to the population the survey exists for. Currently n = 0. |
| 3 | **Learning-outcome trial of an on-device/offline tutor**, any language, any population | Whether §11.3's capability claim is an efficacy claim. Currently n = 0. |
| 4 | **A model-size sweep (0.5B → 1B → 3B → 8B → frontier) against a fixed pedagogical benchmark** (§4.4's stated missing experiment) | Where the tutoring floor actually is. Every threshold claim in §4 is currently inference from adjacent evidence. |
| 5 | **A learner-population-weighted multilingual benchmark for current frontier models**, at ≥100-language coverage, reporting per-language scores | Whether §8.4's floor has moved. No such table exists for any 2026 model. |

**Note what these five have in common.** None of them needs a new model, a new device, a cheaper
token, or a research breakthrough. **Four of the five are measurement.** The binding constraint on
knowing whether AI extends reach is not compute, capability, or money — it is that **the field has
built the instruments to measure languages and has not built the instruments to measure people.**

### 11.7 The close

The recovered §1 concluded that "the economics claim survives contact with the arithmetic."
It does. It is also, on the evidence assembled in §6–§10, **the least interesting true statement
in this section.**

Here is the replacement.

**What is now abundant is competent attention.** The measured active ingredient of the best
remote-learning intervention ever evaluated is twenty minutes of a person's focused, targeted
conversation, and the reason that intervention is not universal is that there are 44 million too
few people to have those conversations. That specific scarcity is over. Nothing else about
education is.

**What is now newly reachable** is the learner behind a barrier of *attention*: the child in a
class of forty, the child in one of the third of classrooms SDI found "orphaned," the child whose
teacher is one of the 44% absent, the child whose question is the
ninth in a row, the adult who will not practise in front of a witness, the learner on an IEP whose
required dosage of a known-good intervention has never been staffable. For every one of them the
obstacle was the cost of an adult's time, and it is not any more.

**What is not newly reachable, and will not be by any price curve**, is the learner behind a
barrier of *kind*: the 363 million children whose language has no data, the learner whose
institution forbids the connection, the learner whose interface cannot be operated, the learner for
whom no trial has ever been run. Those are the next decade's work, they are engineering and
measurement rather than scale, and **§8 says the largest of them — language — is addressable at a
parameter scale three orders of magnitude below the frontier.**

The honest headline of this section is therefore neither the optimist's nor the pessimist's:

> **The compute problem is solved and was never the problem. The attention problem is solved and
> was a real problem. The language, permission, interface and evidence problems are unsolved,
> unaffected by the cost curve, and — for the first time — the only things left.**

That is a better position than the field has been in for forty years. It is also, precisely, a
list of things to go and do.

---

## 12. Retrieval notes for the appended sections (§6–§11)

Recorded so that anyone re-running this can see what was and was not checked, per the project's
rule that unverifiable claims are reported as unverifiable rather than laundered or omitted.

**Worked:** Semantic Scholar graph API (intermittently rate-limited), Crossref, ERIC
(`api.ies.ed.gov`), arXiv export API, World Bank indicators API, UNHCR population API
(`api.unhcr.org`), NBER, World Bank documents repository, 3ie, J-PAL, IZA, Unpaywall,
`files.eric.ed.gov`, direct PDF retrieval from `docs.iza.org` and `nber.org`.

**Did not work, and the claims that depend on them are flagged in place:**

| Source | Failure | Consequence in the text |
|---|---|---|
| OpenAlex | HTTP 429, "Insufficient budget… Resets at midnight UTC" — unusable all session | Substituted Semantic Scholar + Crossref + ERIC throughout |
| ETSI / 3GPP TS 23.038 | HTTP 403 | §6.3 SMS payload constants reported as unverified engineering constants |
| RAND (`rand.org`), incl. RR-266 PDF | HTTP 403; ERIC has no full text | §9.1 correctional-education odds ratios **not asserted**; only the ERIC-verified qualitative conclusion is used |
| *J. Experimental Criminology* (Bozick et al. 2018) | Paywalled, Springer IDP redirect | Same as above |
| UNHCR education pages, `data.unicef.org` | HTTP 403 | §9.1 refugee enrolment rates and the 240M children-with-disabilities figure **not asserted** |
| ReliefWeb API | v1 decommissioned; v2 requires an approved appname | No substitute needed |
| `prisonstudies.org` (World Prison Brief) | 301/404 on the population list; homepage carries no headline figure | **No world prison population figure asserted** |
| *AEJ: Applied* (Cristia 2017; Beuermann 2015) | Paywalled | Point estimates cited to the IZA/NBER working papers, and the divergence from the published abstracts is flagged in §7.1 |
| *Review of Educational Research* (Zheng et al. 2016) | SAGE 403; no OA location in Unpaywall; repositories behind Cloudflare | **Pooled effect sizes not quoted** (§7.1) |
| *Science* (Kremer et al. 2013) | 403 everywhere | Abstract only, via PubMed 23599477 |
| *WBRO* (Rodriguez-Segura 2022) | Paywalled; no OA copy | Landing-page abstract only; contains no pooled effect size regardless |
| *JREE* (Schueler & Rodriguez-Segura 2022, Kenya) | Paywalled | Cited only as characterised by Crawfurd et al.; **its effect sizes are not reported** |
| Interactive Radio Instruction meta-analysis | None located in Crossref or ERIC | **No pooled IRI effect size asserted** |

**Original computation.** §8.3–§8.5 join World Bank `SP.POP.0014.TO` (2025) to the full
per-language Belebele results table (arXiv:2308.16884), via a published country→language mapping
(§8.6). Script: `langreach.py`. Inputs are `MEASURED-BENCH` and `OBSERVED`; the join is
`INFERENCE`; the mapping is my own coding and is reproduced so it can be corrected.

**Negative and null results reported in §6–§11:** ten hardware/ICT nulls with point estimates
(§7.2), six nulls from the TaRL and phone-tutoring literature including two scaling failures of a
proven intervention (§7.4), the pooled CAL estimate of −0.01 to +0.07 SD (§7.4), the absence of
any controlled learning-outcome evaluation of the offline-server lineage (§6.2), the small-model
long-context RAG failure (§6.5), and the zero-RCT census for students with disabilities (§9.1).

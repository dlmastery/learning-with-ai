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

<!-- SECTIONS 4-8 PENDING RESEARCH STREAMS -->

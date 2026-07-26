---
title: "Learner modeling, knowledge tracing, and the lifelong memory of a learner"
wave: F
section: F5
date_researched: 2026-07-25
sources_count: 88
status: superseded
superseded_by: "research/raw/C3-F5-learner-owned-state-2026.md"
---

# F5 — Learner modeling, knowledge tracing, and the lifelong memory of a learner

> **Superseded on 2026-07-25.** This exploratory report over-centered predictive
> leaderboard ceilings and constraint rhetoric. The current constructive,
> frontier-first architecture is
> [C3/F5 — The Learner-Owned State](C3-F5-learner-owned-state-2026.md). This file
> remains only as a source ledger and reproducibility trail.

> **Retrieval note.** WebSearch budget was exhausted before this section began. OpenAlex hit
> its daily credit limit mid-session; arXiv's API returned sustained `503 / Rate exceeded`.
> Retrieval therefore ran on **Crossref**, **Semantic Scholar (with backoff)**, targeted
> **WebFetch** of primary artefacts (GitHub READMEs, JEDM PDFs, W3C/1EdTech specs, EDM
> proceedings PDFs), and local `pdftotext` extraction. Three US federal sources
> (`ftc.gov`, `ecfr.gov`, `federalregister.gov`) returned **403/302-to-unblock** and could
> not be read; claims depending on them are labelled `UNVERIFIED-IN-SESSION` rather than
> guessed. Evidence labels follow PRD §3.

---

## 0. The thesis of this section

There are two literatures here that almost never cite each other, and both of them have
been telling the same uncomfortable story for a decade.

The **spaced repetition** literature has, in the last three years, acquired something no
other corner of learner modeling has: a public, adversarial, reproducible benchmark over
**~350 million real review events from 10,000 real users**. The **knowledge tracing**
literature has had ten years of deep-learning papers and a parallel, quieter stream of
replication papers demonstrating that the headline gains were substantially artefacts of
data preparation and evaluation protocol.

Put them side by side and the finding is the same in both: **learner modeling has a low
ceiling, that ceiling was reached by simple models, and almost all the reported progress
past that ceiling has been measurement error.** AUC in knowledge tracing sits in a band of
roughly **0.70–0.83** and has essentially not moved since 2015. In spaced repetition, a
**zero-parameter moving-average baseline beats every released version of FSRS on log
loss**.

That is not an argument for giving up on learner models. It is an argument that the
research frontier is *not* predictive accuracy. It is an argument that the value of a
learner model lies in **what it is made of, who owns it, how long it lives, and whether it
models error as well as knowledge** — none of which is measured by AUC. The deliverable in
§8 follows from exactly that.

---

## 1. Spaced repetition: SM-2, SuperMemo, Anki, FSRS

### 1.1 SM-2 — the algorithm the world actually runs on

Woźniak's **SM-2** (implemented Dec 1987 – Mar 1989; canonical spec at
`super-memory.com/english/ol/sm2.htm`) is still, in a modified form, the default scheduler
in Anki as of 2026. It is four lines of arithmetic. Grades `q ∈ [0,5]`; intervals
`I(1)=1`, `I(2)=6`, `I(n)=I(n−1)·EF`; and an ease-factor update

```
EF' := EF + (0.1 − (5−q)·(0.08 + (5−q)·0.02)),   clamped at EF ≥ 1.3,   EF₀ = 2.5
```

with repetitions restarting at `I(1)` when `q < 3` **without changing EF**.
`OBSERVED` — primary source is the author's own published spec.

The structural failure mode is well known to practitioners and is documented in the FSRS
project's own design rationale: EF is punished hard by sub-optimal grades (`q=3` costs
−0.14) and recovered feebly (`q=5` gains +0.10), so a card that a learner grades "Hard"
repeatedly ratchets EF down to the 1.3 floor and its interval stops growing. The community
name for this is **"ease hell."** `OBSERVED`

Anki's variant is not the original: 4 buttons rather than 6, a single fail option, user
-controlled learning steps, credit for late reviews, and no further ease decrease on
successive learning-phase failures. Defaults: starting ease 2.50, easy bonus 1.30,
interval modifier 1.00, hard interval 1.20. `OBSERVED` (Anki FAQ / manual)

### 1.2 SuperMemo and the two-component model

The peer-reviewed core of the SuperMemo lineage is small but real:

- Woźniak & Gorzelańczyk (1994), *Optimization of repetition spacing in the practice of
  learning*, **Acta Neurobiologiae Experimentalis** 54(1):59–62,
  `doi:10.55782/ane-1994-1003`. `MEASURED-BENCH`
- Woźniak, Gorzelańczyk & Murakowski (1995), *Two components of long-term memory*,
  **Acta Neurobiol. Exp.** 55(4):301–305, `doi:10.55782/ane-1995-1090`, PMID 8713361.
  `MEASURED-BENCH`

The model: **retrievability R** (probability of recall) and **stability S** (the interval
at which R = 90%), with stability increase `SInc = S′/S` declining as a negative power of S
and rising exponentially as R falls at review time. SM-15/16/17/18 fit `SInc` matrices per
user; the three-component version adds **difficulty D**.

Important caveat for the survey: the widely cited "Theoretical aspects of optimum review"
is part of Woźniak's 1990 MSc thesis / the `supermemo.guru` wiki — **not peer-reviewed** —
and SuperMemo has never released the evaluation code behind its "Universal Metric."
`INFERENCE` on comparability.

### 1.3 FSRS — the modern open scheduler

**FSRS (Free Spaced Repetition Scheduler)** descends from MaiMemo's DHP model. It is a
**DSR** model: Difficulty `D ∈ [1,10]`, Stability `S` (interval at which R = 90%),
Retrievability `R`, with grades `G ∈ {1 Again, 2 Hard, 3 Good, 4 Easy}`.

**The forgetting curve moved from exponential to power law.** This is the single most
consequential modelling decision in the family:

| Version | Forgetting curve |
|---|---|
| v1–v3 | `R(t,S) = 0.9^(t/S)` (exponential) |
| v4 | `R(t,S) = (1 + t/(9S))^(−1)` — power law, DECAY = −1, FACTOR = 1/9 |
| 4.5 | `R = (1 + FACTOR·t/S)^DECAY`, **DECAY = −0.5, FACTOR = 19/81** |
| 6 | decay is **trainable**: `R = (1 + factor·t/S)^(−w₂₀)`, `factor = 0.9^(−1/w₂₀) − 1` |
| 7 | **stability-weighted mixture of two power laws**, 8 trainable curve parameters (w₂₇–w₃₄) |

Parameter counts: **v1=7, v2=14, v3=13, v4=17, 4.5=17, 5=19, 6=21, 7=35.**
`OBSERVED` (`open-spaced-repetition/awesome-fsrs` wiki, "The Algorithm";
`srs-benchmark/models/fsrs_v7.py`) — community documentation, **not peer-reviewed**.

The difficulty update is where FSRS explicitly repairs SM-2:

```
D₀(G) = w₄ − (G−3)·w₅
D′    = w₇·D₀(3) + (1 − w₇)·(D − w₆(G−3))          ← mean reversion
```

The wiki states the mean-reversion term exists "to avoid ease hell." FSRS-5 shifts the
reversion target to `D₀(4)` and damps `ΔD` by `(10−D)/9`; FSRS-6 adds `S^(−w₁₉)` so `SInc`
converges. `OBSERVED`

Anki integration timeline (from release notes and merged PRs) `OBSERVED`:

| Anki version | Date | FSRS event |
|---|---|---|
| 23.10 | 2023-10-31 | FSRS integrated into core (PR ankitects/anki#2633, `fsrs-rs`); v2 scheduler dropped |
| 23.12 | 2023-12-25 | FSRS-4.5 |
| 24.11 | 2024-11-26 | FSRS-5 + FSRS simulator |
| 25.07 | 2025-07-04 | FSRS-6 (PR #3929) |
| 26.05 | 2026-06-16 | **FSRS still opt-in**; issue #3616 "Make FSRS the default?" open; PR #4391 not merged |

That last row matters for the survey's honesty standard: the best-validated open scheduler
in existence is *still not on by default* in the application that produced the data
validating it.

### 1.4 What ~350 million Anki reviews actually show

`open-spaced-repetition/srs-benchmark` is the important artefact. Dataset:
**`anki-revlogs-10k`** — 10,000 Anki users, ~727M raw reviews. Evaluation: sklearn
`TimeSeriesSplit` (older reviews train, newer test; first split discarded), three metrics
— **Log Loss**, **RMSE(bins)** (binned on interval length, review count, lapses), **AUC**.
After outlier and manual-reschedule filtering: **9,999 collections, 349,923,850 reviews**
(without same-day) / **10,000 collections, 519,296,315 reviews** (with).
`MEASURED-BENCH` — method fully disclosed, code public; **not peer-reviewed**.

Headline table (without same-day reviews; mean ± 99% CI):

| Algorithm | Params | Log Loss ↓ | RMSE(bins) ↓ | AUC ↑ |
|---|---|---|---|---|
| **RWKV-P** | 2,762,884 | **0.2773 ± 0.0036** | 0.02502 | **0.8329 ± 0.0017** |
| RWKV | 2,762,884 | 0.3193 | 0.0540 | 0.7683 |
| LSTM | 8,869 | 0.3332 | 0.05378 | 0.7329 |
| GRU | 503 | 0.3333 | 0.0556 | 0.7316 |
| **MOVING-AVG** | **0** | **0.3369** | 0.05915 | 0.7001 |
| Logistic Regression | 34 | 0.3393 | 0.0604 | 0.7108 |
| FSRS-7 recency | 35 | 0.3414 | 0.0627 | 0.7097 |
| FSRS-7 | 35 | 0.3437 | 0.0655 | 0.7069 |
| FSRS-rs | 21 | 0.3443 | 0.0635 | 0.7074 |
| FSRS-6 | 21 | 0.3460 | 0.0653 | 0.7034 |
| FSRS-5 | 19 | 0.3560 | 0.0741 | 0.7011 |
| FSRS-4.5 | 17 | 0.3624 | 0.0764 | 0.6893 |
| DASH | 9 | 0.3682 | 0.0836 | 0.6312 |
| FSRS v4 | 17 | 0.3726 | 0.0838 | 0.6853 |
| **AVG** (constant) | 0 | 0.3945 | 0.1034 | 0.4997 |
| ACT-R | 5 | 0.4033 | 0.1074 | 0.5225 |
| **HLR** (Duolingo) | 3 | 0.4694 | 0.1275 | 0.6369 |
| Ebisu v2 | 0 | 0.4989 | 0.1627 | 0.6051 |

**Four findings the survey should report:**

1. **`NEGATIVE RESULT` — a zero-parameter baseline beats FSRS.** `MOVING-AVG` (0 params;
   predicts recall from the recent success streak alone) achieves log loss **0.3369**,
   better than **every** released FSRS version including FSRS-7 (0.3437). A 34-feature
   logistic regression (0.3393) also beats it. FSRS retains a small edge on AUC
   (0.7069 vs 0.7001), i.e. it *discriminates* slightly better while being *calibrated*
   slightly worse than doing nothing clever.
2. **A large net does win — with an asterisk.** RWKV-P (2.76M params) cuts log loss ~19%
   vs FSRS-7 and lifts AUC 0.71 → 0.83. But RWKV-P is trained *across* users (not
   per-user), sees the whole cross-card review history, and gets extra features FSRS
   never sees: **answer duration, sibling-card information, deck/preset hierarchy, and
   day-of-week**. It also "does not have a forgetting curve in the traditional sense" and
   can predict recall probability *increasing* with time — i.e. it is not a memory model,
   it is a next-event predictor. Its win is a win for *context*, not for memory theory.
3. **Capacity is not the bottleneck.** A 503-parameter GRU ties an 8,869-parameter LSTM. A
   127-parameter Transformer in an earlier benchmark generation was worse than nearly
   everything (log loss 0.439–0.468). The marginal return to model capacity, holding
   features fixed, is close to zero. `INFERENCE`: individual review outcomes are close to
   irreducibly stochastic; the residual is aleatoric, not epistemic.
4. **FSRS does beat SM-2 decisively.** The only benchmark generation that included SM-2
   (19,990 collections, 702,721,850 reviews, Aug 2024) reported unweighted RMSE(bins)
   **FSRS-5 = 0.0712 vs SM-2 = 0.199**, with **99.0% superiority** (FSRS-5 had lower RMSE
   for 99% of users). Caveat published by the authors: SM-2 does not natively emit
   probabilities, so a forgetting curve had to be bolted on. `MEASURED-BENCH`

Against SuperMemo (small n, community-run): `fsrs-vs-sm15` — 16 users, 257,077 reps, FSRS
log loss 0.3812 / RMSE(bins) 0.0703 vs SM-15 0.4325 / 0.1174. `fsrs-vs-sm17` — 19 users,
687,662 reps, FSRS-6 Universal Metric 0.0287 vs SM-17 0.0435, SM-16 0.0547.
`MEASURED-BENCH` with a strong sample-size caveat.

### 1.5 Is the forgetting curve exponential or power-law?

The aggregate curve looks power-law; the mechanism is almost certainly a **superposition of
exponentials**. FSRS's own research notes state it directly: *"The stability of a group is
a distribution, so the forgetting curve is an average of multiple exponential functions,
whose shape is more similar to power function."* This is the stated justification for the
v3→v4 change. Supporting psychology: Wixted & Ebbesen (1991), *On the Form of Forgetting*,
Psychological Science, `doi:10.1111/j.1467-9280.1991.tb00175.x`; Wixted & Ebbesen (1997),
Memory & Cognition, `doi:10.3758/BF03211316`; Averell & Heathcote (2011), J. Math. Psych.
55:25–35, `doi:10.1016/j.jmp.2010.08.009`; Murre & Dros (2015), PLOS ONE,
`doi:10.1371/journal.pone.0120644`. `MEASURED-META` / `OBSERVED`

**`NEGATIVE RESULT` — the fitted decay is confounded with the retention regime.**
srs-benchmark issue #166 documents that the fitted DECAY drifts with the training data's
retention level, and that on *simulated* data with a known decay of 0.5 the optimiser never
recovers it, preferring flatter curves. The thread's conclusion: *"FSRS doesn't generalize
well between different levels of retention."* This is a serious limit on any claim that
large review corpora "prove" a power law: the corpus was generated by a scheduler
targeting ~90% retention, so the curve is only observed in a narrow band of R.
`OBSERVED` — community issue thread, not peer-reviewed.

Also worth stating plainly: FSRS's own tutorial concedes that *"unlike retrievability and
stability, both of which have precise definitions, difficulty is a hazy concept"* and
*"there is no standard method for the estimation of difficulty."* The D in DSR is the weak
leg. `OBSERVED`

### 1.6 Optimal desired retention

Theory (`E[SInc] = SInc·R`) puts the maximum *expected stability gain* at **R ≈ 30–40%**,
which is emphatically not the workload optimum. The `SSP-MMC-FSRS` 5-year simulation
(10,000 cards, 10 new/day) gives: `MEASURED-BENCH` (simulation; assumes FSRS is perfectly
calibrated, no fuzz, default parameters)

| Desired retention | Reviews/day | Min/day | Cards memorised | Memorised/hour |
|---|---|---|---|---|
| 0.70 | 49.3 | 18.8 | 5,946 | **18.9** |
| 0.90 | 116.0 | 30.5 | 6,881 | 13.7 |
| 0.99 | 425.1 | 88.1 | 7,218 | 4.6 |
| Anki SM-2 | 93.7 | — | 6,645 | 15.0 |
| Memrise fixed ladder | 98.7 | — | 6,753 | 15.6 |

Knowledge is nearly flat from DR 0.85 → 0.99 (6,676 → 7,218, **+8%**) while workload rises
**4.9×**. Anki's manual concurs: default 90%, "above 90% the workload increases very
quickly, and above 97% the workload can be overwhelming." Note also the embarrassment in
row 5: *Memrise's fixed 1→6→12→48→96→180-day ladder* is within 2% of FSRS on efficiency.
`NEGATIVE RESULT` for the marginal value of personalisation in scheduling.

Human data on the spacing gap: Cepeda, Vul, Rohrer, Wixted & Pashler (2008),
**Psychological Science** 19(11):1095–1102, `doi:10.1111/j.1467-9280.2008.02209.x`,
n > 1,350: the optimal inter-study gap falls from **20–40% of a one-week retention
interval to 5–10% of a one-year interval**. `MEASURED-RCT`. Meta-analysis: Cepeda,
Pashler, Vul & Wixted (2006), Psych. Bulletin 132(3):354–380,
`doi:10.1037/0033-2909.132.3.354`. `MEASURED-META`

### 1.7 Duolingo Half-Life Regression — a cautionary tale

Settles & Meeder (2016), *A Trainable Spaced Repetition Model for Language Learning*, ACL
2016, `doi:10.18653/v1/P16-1174`, 13M traces. Widely cited (~136). Three documented
problems, all confirmed in the project's own GitHub issues (including by Settles):
`NEGATIVE RESULT`

- The trained weights for **both** `right` and `wrong` are negative (−0.0125, −0.2245),
  implying that *more correct answers shorten the predicted half-life*.
- **>90% of predicted half-lives exceed 120 days.**
- A **constant baseline** `p̄ = 0.859` achieves MAE 0.175 on test — better than every model
  in the paper's Table 2 except HLR itself.

And on the independent Anki benchmark, HLR ranks near the bottom (RMSE(bins) 0.1275),
**worse than the zero-parameter AVG baseline (0.1034)**. This is the clearest single case
in the survey of a heavily cited industrial result that does not survive external
benchmarking.

### 1.8 Does better scheduling produce better learning?

This is where the literature thins dramatically.

- **Lindsey, Shroyer, Pashler & Mozer (2014)**, *Improving Students' Long-Term Knowledge
  Retention Through Personalized Review*, **Psychological Science** 25(3):639–647,
  `doi:10.1177/0956797613504302`. Semester-long middle-school Spanish, time-matched
  conditions, cumulative post-semester exam: personalised review beat massed study by
  **+16.5%** and one-size-fits-all spacing by **+10.0%**. `MEASURED-RCT` — the strongest
  result in the area. Still item-level cued recall.
- Tabibian et al. (2019), *Enhancing human learning via spaced repetition optimization*,
  PNAS 116(10):3988–3993, `doi:10.1073/pnas.1815156116` — MEMORIZE; large-scale but
  **observational**. `OBSERVED`
- Upadhyay, Lancashire, Moser & Gomez-Rodriguez (2021), npj Science of Learning 6,
  `doi:10.1038/s41539-021-00105-8` — an actual RCT; ~69% longer retention after
  controlling for study length and frequency. Very low citation count. `MEASURED-RCT`
- Frappa et al. (2026), *Anki Use and Academic Performance in Medical Education: A
  Systematic Review*, Medical Science Educator, `doi:10.1007/s40670-026-02643-5` — 11
  studies; high-frequency Anki users score **4–13 points** higher on USMLE Step 1, with one
  dose-response by total cards; evidence otherwise "limited and heterogeneous," **all
  observational**. `MEASURED-META` with `OBSERVED` inputs.

**`NEGATIVE RESULT` / the honest bottom line:** there is **no controlled evidence that
switching scheduling algorithm (SM-2 → FSRS) improves any learning outcome.** There is good
evidence that FSRS predicts recall probability better and, in simulation, buys the same
knowledge for less time. Those are different claims and the survey must not merge them.

---

## 2. Knowledge tracing — and the critique literature

### 2.1 The models

| Model | Citation | What it is |
|---|---|---|
| **BKT** | Corbett & Anderson (1995), UMUAI, `doi:10.1007/BF01099821` (1,547 cites) | 2-state HMM per skill; 4 params: p(L₀) init, p(T) transit, p(G) guess, p(S) slip |
| **AFM / LFA** | Cen, Koedinger & Junker (2006), `doi:10.1007/11774303_17` | Logistic; item difficulty + per-skill learning rate |
| **PFA** | Pavlik, Cen & Koedinger (2009), AIED, `doi:10.3233/978-1-60750-028-5-531` | Logistic; separate weights for prior correct / prior incorrect per skill; handles multi-skill items |
| **iBKT** | Yudelson, Koedinger & Gordon (2013), `doi:10.1007/978-3-642-39112-5_18` (323 cites) | Per-student parameters |
| **Elo** | Pelánek, Papoušek, Řihák & Stanislav (2016), UMUAI, `doi:10.1007/s11257-016-9185-7` | Online rating-style updates for adaptive fact practice |
| **DKT** | Piech et al. (2015), NeurIPS, arXiv:1506.05908 | LSTM over one-hot (skill × correctness) |
| **SAKT** | Pandey & Karypis (2019), EDM | Self-attention over the interaction sequence |
| **AKT** | Ghosh, Heffernan & Lan (2020), KDD, `doi:10.1145/3394486.3403282` (513 cites) | Monotonic attention + Rasch-based embeddings |
| **DAS3H** | Choffin et al. (2019), EDM best paper | Logistic + time-window features |
| **LKT** | Pavlik & Eglington (2021), CRAN `lkt` | A general logistic KT framework |

**Identifiability was flagged early and never fixed.** Beck & Chang (2007),
*Identifiability: A Fundamental Problem of Student Modeling*, UM'07,
`doi:10.1007/978-3-540-73078-1_17` — BKT's four parameters are not uniquely determined by
the data; multiple parameter sets fit equally well while implying very different pedagogy
(e.g. "guess = 0.6" degenerate fits). `MEASURED-BENCH`

### 2.2 The critique literature — report this honestly

This is the most important subsection in F5.

**(a) Xiong, Zhao, Van Inwegen & Beck (2016), *Going Deeper with Deep Knowledge Tracing*,
EDM 2016, pp. 545–550.** `MEASURED-BENCH` — read in full from the proceedings PDF.

The original DKT result on ASSISTments 2009-2010 was **AUC 0.86 for DKT vs 0.67 for BKT**.
Xiong et al. found *three* problems with that dataset:

1. **Duplicated records.** "large chunks of records are duplications that should not be
   there for any reason… We counted there are **123,778 rows of duplications out of
   525,535 in the data set (23.6%)**." The ASSISTments team acknowledged the error.
2. **Scaffolding problems mixed with main problems.** 73,466 rows of scaffolding records
   that BKT and PFA exclude but DKT was fed — an information advantage, not a modelling
   advantage.
3. **Repeated response sequences under different skill tags.** Multi-skill assignments were
   decomposed by repeating the *same* action log once per skill. An RNN over sequences sees
   the answer, then sees it again.

The effect, quantified: when multi-skill items are merged into joint skills to remove the
repeats, **DKT's average AUC drops from 0.81 to 0.74 and r² from 0.30 to 0.18.** Splitting
the predictions reveals why: on the *repeated* data points DKT scores **AUC 0.97, r² 0.74**;
on the *leading* records, **AUC 0.77, r² 0.23**. It was substantially predicting answers it
had already been shown.

The authors' verdict: *"On the 09-10 (c) dataset and 14-15 dataset where no repeated
response sequences and scaffolding problems, we notice that **PFA performs as well as
DKT**."* Meanwhile PFA's own AUC *improved* from 0.70 to 0.73 once scaffolding was removed.

**(b) Khajah, Lindsey & Mozer (2016), *How Deep is Knowledge Tracing?*, EDM 2016 /
arXiv:1604.02416.** `MEASURED-BENCH` Give BKT the same statistical regularities DKT
exploits — recency, contextualised trial sequences, inter-skill similarity, individual
ability — and *"BKT achieves a level of performance indistinguishable from that of DKT."*
DKT's advantage is not novel representation learning; it is access to regularities that
vanilla BKT was arbitrarily denied.

**(c) Wilson, Karklin, Han & Ekanadham (2016), *Back to the Basics: Bayesian extensions of
IRT outperform neural networks for proficiency estimation*, EDM 2016 / arXiv:1604.02336.**
`MEASURED-BENCH` Standard IRT, hierarchical IRT (item grouping) and temporal IRT
*"consistently matched or outperformed DKT across all data sets."*

**(d) Gervet, Koedinger, Schneider & Mitchell (2020), *When is Deep Learning the Best
Approach to Knowledge Tracing?*, JEDM 12(3):31–54.** `MEASURED-BENCH` — the definitive
study; read from the PDF. Nine datasets, three model families (Markov / logistic / deep).

- **Best-LR (logistic regression with good features) leads on 4 of 9 datasets; DKT on 5.**
  "Markov process methods lag behind other approaches."
- The margins are small: DKT's edge where it wins is **+0.007 (squirrel), +0.010 (statics),
  +0.020 (assistments12), +0.029 (assistments15)**, and +0.056 on assistments17 — but
  assistments17 is the only dataset recording *all* attempts rather than first attempts,
  and restricting it to first attempts closes the gap to **+0.016**.
- **The whole field lives in AUC ≈ 0.67–0.83.** Representative: algebra05 Best-LR 0.803;
  spanish DKT 0.831; assistments09 Best-LR ~0.771; BKT+ and PFA at 0.67–0.74.
- **`NEGATIVE RESULT` — SAKT fails to replicate.** *"In our experiments, SAKT underperforms
  DKT on all datasets."* On ASSISTments 2015 the original authors reported **AUC 0.85**;
  Gervet et al. observed **0.73**. They note the original ablation reported 0.82 for a
  trivial feedforward baseline, a figure they call one that "seems impossible."
- **`NEGATIVE RESULT` — DAS3H's time-windows add nothing.** The EDM 2019 best paper's
  headline feature adds **no** predictive power to a good logistic model; its gain over PFA
  "is simply due to the addition of an item difficulty parameter inspired by IRT."
- **`NEGATIVE RESULT` — expert knowledge-component models add ≤ +0.01 AUC on 7 of 9
  datasets.** Only the two KDD Cup 2010 datasets get +0.03. On 4 of 9 datasets a
  KC-only model (PFA) fails to beat an item-difficulty-only model (IRT), implying the
  hand-built domain models are low quality.
- **DKT is not domain-model-free.** The input/output representation dominates its
  performance; KC-inputs/item-outputs wins on most datasets. "DKT — although initially
  advertised as independent from any expert-designed structure — relies on the KC model to
  perform optimally."
- **Regime, not superiority:** LR wins on small/moderate data and on learners with
  thousands of interactions (DKT plateaus after ~1,000 interactions per learner — the RNN
  long-horizon problem). DKT wins on large data and where temporal order matters, and
  **reaches near-peak accuracy on a new learner ~6× faster** (10 interactions vs 60 on
  `squirrel`). That last point is the one genuinely useful thing deep KT buys, and it is a
  **cold-start** result, not an accuracy result.
- **Calibration is bad.** "the current best models are severely biased on some datasets —
  hindering their applicability in adaptive policies and open learner models."

**(e) Liu et al. (2022), *pyKT: A Python Library to Benchmark Deep Learning based Knowledge
Tracing Models*, NeurIPS 2022 Datasets & Benchmarks, arXiv:2206.11460.**
`MEASURED-BENCH` 7 datasets, 10 DLKT models, standardised preprocessing. Two conclusions
stated in the abstract: *"wrong evaluation setting may cause **label leakage** that
generally leads to performance inflation"*; and *"the improvement of many DLKT approaches
is **minimal** compared to the very first DLKT model proposed by Piech et al."*

**(f) Ding & Larson (2019), *Why Deep Knowledge Tracing has less Depth than Anticipated*,
EDM 2019 (paper #60).** Located in the proceedings index; full text is behind a Google
Drive link that could not be retrieved this session. `UNVERIFIED-IN-SESSION` beyond title
and authorship.

### 2.3 What the survey should conclude about knowledge tracing

1. **The AUC ceiling is ~0.82 and has not moved since 2015.** Every claimed jump above it
   has, on inspection, come from duplicated rows, leaked labels, non-standard splits, or
   information the baseline was denied.
2. **Simple baselines match deep KT on most real datasets.** Logistic regression with
   count features; BKT with recency and individualisation; IRT with hierarchy.
3. **AUC is the wrong metric anyway.** As Gervet et al. note (citing Pelánek 2015), AUC is
   invariant to monotone rescaling and therefore blind to calibration — and calibration is
   exactly what a downstream instructional policy or an open learner model needs. Note the
   parallel with §1.4: the SRS benchmark reports log loss *and* RMSE(bins) *and* AUC
   precisely because AUC alone is misleading. **KT should adopt the SRS benchmark's
   metric discipline.**
4. **The one real deep-learning win is burn-in speed, not asymptotic accuracy.** That is a
   cold-start result and should be filed under §4.
5. **The field has no equivalent of `srs-benchmark`:** no continuously-run, adversarial,
   open leaderboard over hundreds of millions of events with a zero-parameter baseline
   included by default. pyKT is the closest thing and is a one-shot paper. `INFERENCE` —
   this is the single highest-leverage missing artefact in learner modeling.

---

## 3. Open Learner Models — does showing the learner their model help?

### 3.1 The tradition

- Bull & Kay (2007), *Student Models that Invite the Learner In: The SMILI☺ Open Learner
  Modelling Framework*, IJAIED, `doi:10.3233/irg-2007-17(2)02`; and the 2016 revision,
  *SMILI☺: a Framework for Interfaces to Learning Data in Open Learner Models, Learning
  Analytics and Related Fields*, IJAIED, `doi:10.1007/s40593-015-0090-8` (118 cites).
- Bull & Kay (2010), *Open Learner Models*, Studies in Computational Intelligence,
  `doi:10.1007/978-3-642-14363-2_15` (104 cites).
- Bull (2020), *There are Open Learner Models About!*, IEEE TLT,
  `doi:10.1109/TLT.2020.2978473` (69 cites) — the field survey.
- Bull (2016), *Negotiated learner modelling to maintain today's learner models*, RPTEL,
  `doi:10.1186/s41039-016-0035-3` — the learner may *argue with* the model.
- Systems: **Mastery Grids** (Loboda, Guerra, Hosseini & Brusilovsky 2014,
  `doi:10.1007/978-3-319-11200-8_18`), open *social* learner models (Brusilovsky 2017,
  `doi:10.1145/3038535.3038545`), **Betty's Brain** teachable agent (Biswas, Leelawong,
  Schwartz & Vye 2005, `doi:10.1080/08839510590910200`; Biswas et al. 2010, RPTEL).

The SMILI☺ framework's contribution is a vocabulary: *what* is opened (knowledge,
misconceptions, affect), *to whom* (learner, peers, teacher, parent), *how* (skill meters,
concept maps, tree views), and *with what control* (view-only, editable, negotiated).

### 3.2 The evidence

- Bodily, Kay, Aleven, Jivet, Davis, Xhakaj & Verbert (2018), *Open learner models and
  learning analytics dashboards: a systematic review*, LAK'18,
  `doi:10.1145/3170358.3170409` (158 cites) — the field-defining review, unifying the OLM
  and LAD literatures which had developed in isolation. Full abstract could not be
  retrieved (`dl.acm.org` and the BYU mirror both 403 this session);
  `UNVERIFIED-IN-SESSION` for specific counts.
- Matcha, Uzir, Gašević & Pardo (2020), *A Systematic Review of Empirical Studies on
  Learning Analytics Dashboards: A Self-Regulated Learning Perspective*, IEEE TLT,
  `doi:10.1109/TLT.2019.2916802` (297 cites). Restricted to LAD studies "that report
  empirical findings to assess the impact on learning and teaching"; the paper's own
  framing of the gap: *"Several previous literature reviews identified self-regulated
  learning as a primary focus of LADs. However, there has been much less understanding how
  learning analytics are grounded in the literature…"* `MEASURED-META`
- Jivet, Scheffel, Specht & Drachsler (2018), *License to Evaluate: Preparing Learning
  Analytics Dashboards for Educational Practice*, LAK'18, `doi:10.1145/3170358.3170421`
  (211 cites); and Jivet, Scheffel, Drachsler & Specht (2017), ***Awareness Is Not Enough:
  Pitfalls of Learning Analytics Dashboards in the Educational Practice***, EC-TEL,
  `doi:10.1007/978-3-319-66610-5_7` (131 cites).
- Kaliisa, Jivet & Prinsloo (2023), *A checklist to guide the planning, designing,
  implementation, and evaluation of learning analytics dashboards*, IJETHE,
  `doi:10.1186/s41239-023-00394-6`.

**`NEGATIVE RESULT` — the recurring finding across all four reviews is the same, and it is
methodological.** The dashboard/OLM literature evaluates *perception* (usability,
satisfaction, self-reported usefulness) far more often than *learning*; the theoretical
grounding in self-regulated learning is thin or post-hoc; and comparison-to-peer-average
visualisations — the most common design — target *awareness*, which is the weakest link in
the SRL chain. The Jivet et al. 2017 title is the field's own summary: **awareness is not
enough.** `MEASURED-META`

A second, sharper worry appears in the same literature: **social-comparison designs can
demotivate.** Showing a struggling learner that they are below the class average is a
well-documented risk, and the reviews call for evaluation against motivational as well as
cognitive outcomes. `MEASURED-META` / `INFERENCE` on magnitude — the survey should report
this as a documented risk, not a quantified effect.

### 3.3 The under-appreciated blocker

Gervet et al.'s calibration finding lands directly here. An OLM shows the learner a
*number* — "you are at 62% mastery of quadratic factoring." If the underlying model is
"severely biased," the OLM is displaying a miscalibrated number with the authority of an
interface. **An open learner model inherits the calibration debt of the model it opens.**
Every OLM should therefore be required to publish reliability diagrams, not just AUC.
`INFERENCE`

The one design that is robust to this: **negotiated / editable** learner models (Bull
2016). If the learner can contest the estimate, miscalibration becomes a conversation
rather than a verdict. This is the design that the §8 schema adopts.

---

## 4. The cold start and the long game

### 4.1 What exists

**Cold start.** The only clean, replicated, positive deep-learning result in knowledge
tracing is a cold-start result: DKT reaches near-peak accuracy on a new learner in ~10
interactions where Best-LR needs ~60 — a **6× reduction in burn-in** (Gervet et al. 2020,
Fig. 7). `MEASURED-BENCH`. The classical answers are hierarchical/Bayesian pooling (a prior
over learners fitted from the population — this is what iBKT and hierarchical IRT do; see
Wilson et al. 2016) and Elo-style online updates that start every learner at the population
mean (Pelánek et al. 2016). In spaced repetition the analogue is FSRS's **default
parameters**, which the benchmark evaluates as a distinct row (log loss 0.3629 vs 0.3437
optimised — i.e. the population prior costs you ~0.02 log loss until you have your own
data). `MEASURED-BENCH`

**Lifelong / cross-domain.** Almost the entire body of work is one research group's:

- Kay & Kummerfeld (2012), *Creating personalized systems that people can scrutinize and
  control*, **ACM TiiS** 2(4), `doi:10.1145/2395123.2395129`.
- Kay & Kummerfeld (2019), *From data to personal user models for life-long, life-wide
  learners*, **BJET** 50(6), `doi:10.1111/bjet.12878` (44 cites) — the manifesto.
- Barua, Kay, Kummerfeld & Paris (2011), *Theoretical foundations for **user-controlled
  forgetting** in scrutable long term user models*, OzCHI, `doi:10.1145/2071536.2071541`;
  and Barua, Kay & Paris (2013), `doi:10.1145/2541016.2541034`.
- Kay (2021), *The Case for Scrutable, Personal, Long-Term User Models for Information
  Retrieval*, CHIIR, `doi:10.1145/3406522.3444755`.
- Personis / PersonisAD — a user-model *server* with per-component evidence lists and
  pluggable resolvers, i.e. the model stores *evidence*, and interpretation happens at
  query time.

That last architectural idea is the most important one in this section and is almost
entirely unexploited outside Kay's group. **A lifelong learner model should store evidence
and resolve it on demand, not store a fitted posterior.** Posteriors go stale, embed the
assumptions of whichever model was current in 2019, and cannot be re-derived. Evidence can
be re-interpreted by a better model in 2035. `INFERENCE`

### 4.2 What does not exist — and this is the point

**There is no public dataset of a single learner's traces across years and across
subjects.** The longest-horizon public educational datasets are all *platform* traces, not
*learner* traces:

| Dataset | Horizon | Scope |
|---|---|---|
| ASSISTments 2009-10 / 2012 / 2015 / 2017 | one school year each | middle-school maths, one platform |
| KDD Cup 2010 (algebra05, bridge06) | one course | one platform |
| EdNet (Choi et al. 2020, `doi:10.1007/978-3-030-52240-7_13`) | ~2 years | TOEIC prep, one platform |
| MaiMemo (Ye et al., 220M logs, `doi:10.7910/DVN/VAGUL0`) | multi-year | vocabulary only |
| Duolingo HLR (13M traces, `doi:10.7910/DVN/N8XJME`) | 2 weeks | vocabulary only |
| `anki-revlogs-10k` | up to ~10 years per user | **whatever the user chose to make cards about** |

`OBSERVED`. Note the last row: the Anki corpus is, almost by accident, the closest thing
the world has to a decade-long, cross-subject, per-learner record — because Anki is a
general-purpose tool that individuals own. That is not a coincidence; it is the argument of
§8 in empirical form. **Learner-owned tools produce longitudinal data; institution-owned
tools produce annual data, because institutions are annual.**

What is missing, concretely:

1. **No cross-subject transfer results.** Nobody has shown that knowing a learner's model
   in algebra improves the cold-start prior in chemistry, though the prior-knowledge
   literature (§5) says it should.
2. **No cross-provider identity.** A learner's Duolingo, Khan Academy, Anki and school-LMS
   models are four disjoint strangers.
3. **No decay model for the model itself.** Every KT model assumes knowledge is monotone or
   near-monotone within a session; none of them models what a mastery estimate from 2023
   is worth in 2026. The SRS literature has exactly this model (stability/retrievability)
   and the KT literature does not use it. **This is the most obvious unexploited join in
   the field.** `INFERENCE`
4. **No standard for "what I got wrong and why"** — see §6.

---

## 5. Prior knowledge is the dominant variable

### 5.1 The evidence

Dochy, Segers & Buehl (1999), *The Relation between Assessment Practices and Outcomes of
Studies: The Case of Research on Prior Knowledge*, **Review of Educational Research**
69(2):145–186, `doi:10.3102/00346543069002145` (270 cites). 183 articles reviewed; prior
knowledge shows positive effects on performance across the corpus, with the size of the
observed effect depending heavily on how prior knowledge was assessed. `MEASURED-META`

**The expertise reversal effect** is the mechanism that makes this actionable, not merely
predictive:

- Kalyuga, Ayres, Chandler & Sweller (2003), *The Expertise Reversal Effect*, **Educational
  Psychologist** 38(1):23–31, `doi:10.1207/S15326985EP3801_4` (1,333 cites).
  `MEASURED-META`
- Kalyuga & Sweller (2004), *Measuring Knowledge to Optimize Cognitive Load Factors During
  Instruction*, **J. Educational Psychology** 96(3):558–568,
  `doi:10.1037/0022-0663.96.3.558` (137 cites). `MEASURED-RCT`
- Kalyuga & Sweller (2005), *Rapid dynamic assessment of expertise to improve the
  efficiency of adaptive e-learning*, ETR&D, `doi:10.1007/BF02504800` (182 cites).
  `MEASURED-RCT`
- Tobias (2009), *The expertise reversal effect and aptitude treatment interaction
  research*, Instructional Science, `doi:10.1007/s11251-009-9103-z` — the connection back
  to Cronbach & Snow's ATI programme. Snow (1992), *Instructional Psychology: Aptitude,
  Adaptation, and Assessment*, Annual Review of Psychology,
  `doi:10.1146/annurev.psych.43.1.583`.

The core claim: **instructional techniques that help novices actively harm experts.**
Worked examples beat problem solving for novices and lose to it for experts; diagrammatic
support that prevents split attention becomes redundant and imposes extra load once the
learner has schemas. The *sign* of the treatment effect flips with prior knowledge. This is
why prior knowledge is not merely the best predictor — it is the variable that determines
which instruction is correct.

Kalyuga & Sweller's **rapid verification / first-step methods** matter for system design:
they showed you can get an actionable expertise estimate in *seconds* (present a
partially-solved problem, ask for the next step, or ask the learner to verify a proposed
step) rather than via a full diagnostic test. That is the right primitive for an AI-native
system's opening move.

### 5.2 Contrast: learning styles

- Pashler, McDaniel, Rohrer & Bjork (2008), *Learning Styles: Concepts and Evidence*,
  **Psychological Science in the Public Interest** 9(3):105–119,
  `doi:10.1111/j.1539-6053.2009.01038.x` (1,412 cites) — the meshing hypothesis requires a
  crossover interaction in a randomised design; virtually no study meets the standard, and
  those that do find no interaction. `MEASURED-META`
- Rohrer & Pashler (2012), *Learning styles: where's the evidence?*, Medical Education,
  `doi:10.1111/j.1365-2923.2012.04273.x`. `MEASURED-META`
- Newton & Salvi (2020), *How Common Is Belief in the Learning Styles Neuromyth, and Does
  It Matter? A Pragmatic Systematic Review*, **Frontiers in Education**,
  `doi:10.3389/feduc.2020.602451` (86 cites); Newton et al. (2021) for medical education
  specifically, `doi:10.3389/fnhum.2021.708540`. `MEASURED-META`
- A 2026 replication in J. Educational Psychology (`doi:10.1037/edu0001056`) again finds no
  effect of matching in primary-school students. `MEASURED-RCT`

**The design rule for the survey:** if a system can measure exactly one thing about a
learner before instruction, it should measure **prior knowledge in the specific domain of
the next task** — not a style, not a personality, not a modality preference. And it should
measure it with a rapid verification item, not a questionnaire. `INFERENCE` from
`MEASURED-META` inputs.

---

## 6. Misconception modeling — knowing what a learner believes *wrongly*

### 6.1 The oldest and best idea in the field

Brown & Burton (1978), *Diagnostic Models for Procedural Bugs in Basic Mathematical
Skills*, **Cognitive Science** 2(2):155–192, `doi:10.1207/s15516709cog0202_4` (647 cites).
BUGGY/DEBUGGY synthesised a "deep-structure model of a student's misconceptions or bugs"
that could **explain *why* a student is making a mistake as opposed to simply identifying
the mistake.** Brown & VanLehn's repair theory (`doi:10.1016/B978-1-4832-1446-7.50031-5`)
generalised it: bugs are not random, they are the outputs of *repairs* a learner applies
when a procedure reaches an impasse.

Read that against §2: forty-eight years later, the state-of-the-art model outputs a scalar
probability of a correct answer. **We replaced a theory of error with a number between 0
and 1.** `INFERENCE` — this is the strongest single argument in F5.

### 6.2 Concept inventories

- Hestenes, Wells & Swackhamer (1992), *Force Concept Inventory*, **The Physics Teacher**
  30:141–158, `doi:10.1119/1.2343497` (1,849 cites). The FCI's distractors were built from
  student interviews so that each wrong option corresponds to an identifiable Aristotelian
  or impetus-style belief. The instrument's diagnostic power is entirely in its
  distractors. `MEASURED-BENCH`
- Hake (1998), *Interactive-engagement versus traditional methods: A six-thousand-student
  survey of mechanics test data for introductory physics courses*, **Am. J. Physics**
  66:64–74, `doi:10.1119/1.18809` (3,279 cites). 62 courses, **N = 6,542**; normalised gain
  `g = (post − pre)/(100 − pre)` separates interactive-engagement courses (g ≈ 0.48 ± 0.14)
  from traditional lecture (g ≈ 0.23 ± 0.04). `MEASURED-BENCH` — one of the most
  consequential measurements in education, and it was possible *only* because the
  instrument measured misconceptions rather than performance.
- The FCI's interpretation was itself contested (Huffman & Heller 1995,
  `doi:10.1119/1.2344279`; Hestenes & Halloun's reply, `doi:10.1119/1.2344278`) — report as
  contested per PRD §3.2.

### 6.3 Distractor design and diagnostic psychometrics

- Briggs, Alonzo, Schwab & Wilson (2006), *Diagnostic Assessment With Ordered
  Multiple-Choice Items*, **Educational Assessment** 11(1):33–63,
  `doi:10.1207/s15326977ea1101_2` (194 cites). OMC items attach each option to a **level of
  a learning progression**, so a wrong answer is informative about *where* the learner is,
  not just *that* they are wrong. `MEASURED-BENCH`
- Cognitive diagnosis models: de la Torre (2009), *DINA Model and Parameter Estimation: A
  Didactic*, **JEBS** 34(1):115–130, `doi:10.3102/1076998607309474` (535 cites); de la
  Torre (2011), *The Generalized DINA Model Framework*, **Psychometrika** 76:179–199,
  `doi:10.1007/s11336-011-9207-7` (632 cites). These model a learner as a **binary
  attribute profile** against a Q-matrix — closer to "what components does this learner
  have" than to a scalar ability. The `GDINA` R package (`doi:10.32614/CRAN.package.GDINA`)
  is the practical entry point.

### 6.4 Modern, at scale

Wang, Lamb, Saveliev, Cameron, Zaykov, Hernández-Lobato, Turner, Baraniuk, Barton, Peyton
Jones, Woodhead & Zhang (2020), *Instructions and Guide for Diagnostic Questions: The
NeurIPS 2020 Education Challenge*, arXiv:2007.12061. **>20 million student answers** to
Eedi multiple-choice maths diagnostic questions, where *"the answers that the students give
to these questions reveal key information about the specific nature of misconceptions that
the students may hold."* `MEASURED-BENCH` This is the largest misconception-labelled
dataset in existence and it is the right shape: the label is *which wrong belief*, not
*wrong*.

### 6.5 Does confronting misconceptions work?

- Guzzetti, Snyder, Glass & Gamas (1993), *Promoting Conceptual Change in Science: A
  Comparative Meta-Analysis of Instructional Interventions from Reading Education and
  Science Education*, **Reading Research Quarterly** 28(2):117–159, `doi:10.2307/747886`
  (346 cites) — refutation texts (which state the misconception explicitly, refute it, then
  give the correct account) outperform expository text. `MEASURED-META`
- Tippett (2010), *Refutation Text in Science Education: A Review of Two Decades of
  Research*, **IJSME** 8:951–970, `doi:10.1007/s10763-010-9203-x` (250 cites).
  `MEASURED-META` — the effect is real but its durability and transfer are less well
  established than its immediate effect. Report as such.

### 6.6 The design claim

**Modeling what a learner believes wrongly is more useful than modeling what they know**,
for three reasons, and the survey should state them as a claim with this support:

1. **It is actionable.** "72% mastery" implies "practise more." "You are applying the
   subtraction-borrows-from-the-larger-digit bug" implies a specific refutation.
2. **It is stable and enumerable.** Misconceptions are a small, discrete, reusable
   vocabulary per domain (the FCI needs ~30 items to cover Newtonian mechanics). Mastery
   probabilities are continuous, per-learner, and non-transferable.
3. **It survives the model.** A misconception label written in 2026 is still meaningful in
   2036. A BKT posterior is not. This is exactly the property §8's schema needs.
   `INFERENCE`

---

## 7. Privacy and the permanent record

A lifelong learner model is lifelong surveillance. This must be treated as a design
constraint, not an ethics appendix.

### 7.1 The legal floor

**FERPA** (20 U.S.C. §1232g; 34 CFR Part 99). Protects "education records" held by
funded institutions. Two holes matter here: the **school official** exception (which the
2008/2011 rulemakings widened to cover contractors and "authorized representatives"), and
**directory information**, which may be disclosed without consent unless opted out. There
is **no private right of action** — *Gonzaga University v. Doe*, 536 U.S. 273 (2002) — so
enforcement runs through the Department of Education's funding-withdrawal power, which has
never been exercised. `OBSERVED` — statutory text and case citation verified; enforcement
history could not be re-verified this session (`ed.gov` unreachable): `UNVERIFIED-IN-SESSION`.

**COPPA** (15 U.S.C. §§6501–6506; 16 CFR Part 312). The FTC finalised significant
amendments to the COPPA Rule in 2025, reported to add **separate verifiable parental
consent for third-party disclosure and targeted advertising**, a **written data retention
policy** requirement, and an **express prohibition on indefinite retention**. All three
primary sources (`ftc.gov`, `ecfr.gov`, `federalregister.gov`) returned 403/302 this
session. **`UNVERIFIED-IN-SESSION` — the survey must re-verify effective and compliance
dates and the exact §312 subsection numbers before publication.** The FTC's May 2022 Policy
Statement on COPPA and ed tech is the relevant enforcement-posture document.

**GDPR** (Regulation (EU) 2016/679). The articles that bind a lifelong learner model:
Art. 4(4) profiling; **Art. 5(1)(c) data minimisation**; **Art. 5(1)(e) storage
limitation**; Art. 8 child consent (13–16 depending on member state); Art. 9 special
categories; Art. 15 access; **Art. 17 erasure**; **Art. 20 portability**; **Art. 22**
automated decisions producing legal or similarly significant effects; Art. 35 DPIA.
Storage limitation is the direct antagonist of "lifelong," and any lifelong model must
justify itself against it. `OBSERVED`

**EU AI Act** (Regulation (EU) 2024/1689). **Annex III point 3** makes four categories of
educational AI **high-risk**, verified verbatim: `OBSERVED`

> (a) AI systems intended to be used to determine access or admission or to assign natural
> persons to educational and vocational training institutions at all levels;
> (b) AI systems intended to be used to evaluate learning outcomes, including when those
> outcomes are used to steer the learning process of natural persons in educational and
> vocational training institutions at all levels;
> (c) AI systems intended to be used for the purpose of assessing the appropriate level of
> education that an individual will receive or will be able to access…;
> (d) AI systems intended to be used for monitoring and detecting prohibited behaviour of
> students during tests…

Read (b) carefully. **A knowledge tracing model that steers what the learner sees next is
explicitly a high-risk AI system under EU law.** That is the entire subject of §2. Art. 6(2)
performs the classification. Art. 5(1)(f) separately prohibits emotion-inference systems in
education. Applicability dates (entry into force 1 Aug 2024; prohibitions 2 Feb 2025;
GPAI 2 Aug 2025; Annex III high-risk 2 Aug 2026) are widely reported but were not
re-verified against the Official Journal this session: `UNVERIFIED-IN-SESSION`.

US state layer: California **SOPIPA** (Cal. B&P Code §22584) and AB 1584; Illinois SOPPA;
New York Ed. Law §2-d; the industry **Student Privacy Pledge**. `OBSERVED`

### 7.2 The empirical record — and the canonical failure

**inBloom** (2013–2014) is the cautionary tale for exactly the artefact this section
proposes. A Gates- and Carnegie-funded multi-state student data platform, it collapsed in
2014 under parent and legislative opposition. Bulger, McCormick & Pitcan (2017), *The
Legacy of inBloom*, Data & Society working paper (2 Feb 2017), `doi:10.69985/klul2611`,
records the consequence: **over 400 pieces of state-level student-data-privacy legislation**
followed, and the field moved from "a large-scale, open source platform that was a
multi-state collaboration" toward "closed, proprietary systems, adopted piecemeal."
`OBSERVED`

The lesson is precise and is the hinge of §8: **inBloom failed not because centralised
learner data is technically hard but because it was centralised in an entity that was not
the learner.** Every property people objected to — indefinite retention, third-party
access, no meaningful consent, no deletion — is a property of *custody*, not of *schema*.

**Human Rights Watch (25 May 2022), "How Dare They Peep into My Private Life?"** `OBSERVED`
— verified figures:

- **163 EdTech products** analysed across **49 countries**;
- **145 of 163 (89%)** engaged in data practices that risked, undermined, or infringed
  children's rights;
- those 145 products sent or granted access to children's data to **196 third-party
  companies**, overwhelmingly ad-tech;
- **56%** of 73 apps could collect advertising IDs; **29%** collected precise GPS;
  **25%** accessed contact lists; **8 of 124** websites used canvas fingerprinting;
- **39 of 42 governments** that built their own EdTech built systems that risked or
  infringed children's rights.

Breaches: Illuminate Education (Jan 2022, ~3 million students) and the FTC's 2022 action
against Chegg. `UNVERIFIED-IN-SESSION` on exact figures — not re-verified this session.

**And the de-identification result that should end the "just anonymise it" conversation:**
Daries, Reich, Waldo, Young, Whittinghill, Ho, Seaton & Chuang (2014), *Privacy, anonymity,
and big data in the social sciences*, **CACM** 57(9):56–63, `doi:10.1145/2643132` (82
cites). De-identifying the MITx/HarvardX dataset to a FERPA-defensible standard
(k-anonymity) **degraded the data enough to change the conclusions that could be drawn from
it**. The authors' framing: there is a genuine tension between open science and privacy in
human-subjects data, and the standard resolution — release an anonymised corpus — does not
work. `MEASURED-BENCH`

### 7.3 Technical mitigations, honestly rated

| Mitigation | What it buys | What it doesn't |
|---|---|---|
| **On-device / edge modeling** | Raw traces never leave the device; no custodian to breach or subpoena | Requires the model to be small — which §1.4 and §2.3 say is *fine*: a 21-parameter FSRS and a 34-feature logistic regression are the state of the art. **The accuracy ceiling is a privacy gift.** `INFERENCE` |
| **Federated learning** | Population priors without pooling raw traces | Gradient leakage; still needs a coordinator; education cohorts are small enough that per-round updates can be identifying |
| **Differential privacy** | Formal guarantee | Hard here: cohorts are small (a class of 25), traces are per-item and long, and the useful signal (this learner's specific misconception) *is* the outlier. DP budgets that protect a student destroy the diagnostic. `INFERENCE` |
| **Local-first architecture** | Kleppmann, Wiggins, van Hardenberg & McGranaghan (2019), *Local-first software: you own your data, in spite of the cloud*, Onward! 2019, `doi:10.1145/3359591.3359737` — seven ideals incl. ownership, longevity, privacy, user control | Sync/conflict complexity; no answer to institutional reporting needs |
| **User-controlled forgetting** | Barua, Kay, Kummerfeld & Paris (2011), `doi:10.1145/2071536.2071541` — a *theory* of what it means for a scrutable long-term model to forget on request | Almost never implemented |

The last row is the most under-used idea in the literature and belongs in the schema.

---

## 8. DELIVERABLE — the Portable Learner Model (PLM)

**Nobody has built this.** What exists is either (a) a *credential* format that records
outcomes (Open Badges 3.0, CLR 2.0, W3C VC 2.0, Europass/ELM), or (b) an *activity stream*
format that records events (xAPI / IEEE 9274.1.1, Caliper), or (c) a proprietary
per-vendor posterior that dies with the vendor. **None of them models what a learner knows,
has forgotten, or believes wrongly.**

Verified for this section: `OBSERVED`

- **W3C Verifiable Credentials Data Model 2.0** — W3C Recommendation, **15 May 2025**.
  Standardises "the extensible data model for verifiable credentials, how they can be
  secured from tampering, and a three-party ecosystem." Explicitly out of scope:
  *"Verifiability of a credential does not imply the truth of claims encoded therein"* —
  validation is left to the verifier's business rules. It is a **signature envelope**, not
  a knowledge model.
- **1EdTech Comprehensive Learner Record (CLR) Standard 2.0** (Final) — carries academic
  achievements, courses, competencies/skills, employer-based achievements. "An assertion is
  specific to one learner. It contains a claim that the learner has made a particular
  achievement and metadata about the achievement, the issuer, and the learner, including
  possible evidence supporting the claim." Built on **Open Badges 3.0** and compatible with
  W3C VC. It models **assertions by issuers**, not **beliefs of the learner**.
- **xAPI / Experience API** (ADL; IEEE 9274.1.1-2023) + Learning Record Store — an
  actor-verb-object statement stream. It is a *log format*. It defines no cognitive state.
- **DID Core 1.0** (W3C Rec, July 2022) — identifiers without a registry.

So the gap is specific and stateable: **we have standards for what a learner was *awarded*
and what a learner *did*, and no standard for what a learner *knows*.**

### 8.1 Design principles

1. **Evidence-first, posterior-second.** Store the observations; derive the estimates.
   (Personis, Kay & Kummerfeld.) Any model fitted today will be obsolete; the evidence
   won't be. Every derived quantity carries the model id and version that produced it, and
   is recomputable.
2. **Learner-custodied.** The record lives with the learner (device, personal pod, or a
   fiduciary of the learner's choosing). Providers get scoped, revocable, expiring reads.
   This is the direct lesson of inBloom: the objection was to custody, not schema.
3. **Small models, by design.** §1.4 and §2.3 show that a 21-parameter memory model and a
   ~34-feature logistic model are at the accuracy frontier. Therefore the whole model can
   run on-device. Privacy here costs approximately **zero accuracy**.
4. **Misconceptions are first-class.** Not a subtype of "incorrect." A named, referenceable
   belief with evidence and refutation history (§6).
5. **Everything decays.** Every knowledge claim carries a memory-model state
   (stability/retrievability), not just a timestamp. A mastery estimate without a decay
   model is a lie about the present (§4.2, item 3).
6. **Calibration is a published property.** Any estimate exposed to a learner or a policy
   must carry the reliability of the model that produced it (§3.3).
7. **Contestable and forgettable.** The learner can dispute an estimate (negotiated
   learner modeling, Bull 2016) and can compel forgetting with defined semantics (Barua et
   al. 2011). Erasure is a *feature*, and it is also GDPR Art. 17.
8. **Portable ≠ public.** Portability (Art. 20) and minimisation (Art. 5(1)(c)) both point
   at the same architecture: the learner can export everything; nobody else can read
   anything without a scoped grant.

### 8.2 The schema

Seven layers. `INFERENCE` throughout — this is the section's argued contribution.

```yaml
plm_version: "0.1"

# ── L0. IDENTITY ────────────────────────────────────────────────────
# Pseudonymous by default. A DID the learner controls; per-provider
# pairwise identifiers so providers cannot join records without consent.
identity:
  did: "did:key:z6Mk..."               # W3C DID Core 1.0
  pairwise_ids: { provider_id: local_pseudonym }
  guardianship:                         # COPPA / GDPR Art.8
    status: minor | adult | transitioning
    custodian_did: ...
    transition_at: <date>               # custody MUST transfer at majority

# ── L1. DOMAIN MAP ──────────────────────────────────────────────────
# Shared vocabulary. Without this, portability is a file format, not
# interoperability. Anchored to public identifiers, never to a vendor's
# internal skill ids.
domains:
  - kc_id: "wikidata:Q11473"           # or CASE/ELM/Credential Engine URI
    labels: { en: "quadratic factoring" }
    prerequisites: [kc_id, ...]
    provider_mappings: { khan: "...", openstax: "..." }

# ── L2. EVIDENCE LOG (append-only, the ONLY primary data) ───────────
# Every downstream number is recomputable from this. xAPI-compatible on
# the wire; richer than xAPI in what it requires.
evidence:
  - id: ulid
    ts: <iso8601>
    kc_ids: [...]
    item:
      item_id: <uri>
      item_hash: <sha256>              # so item drift is detectable
      format: mcq | free | code | proof | performance
      difficulty_prior: <float|null>
    response:
      correct: bool | partial<float>
      raw: <string|ref>                # what they actually said/did
      chosen_distractor: <distractor_id|null>   # ← the diagnostic bit
      latency_ms: int
      hints_used: int
      attempt_index: int
    context:
      modality: read|watch|practice|tutor_dialogue|exam|self_report
      assistance: none|hint|worked_example|ai_tutor|collaborator
      stakes: none|low|high
      provider: <did>
    provenance:
      attested_by: <did>
      signature: <vc-proof>            # W3C VC 2.0 securing mechanism
      confidence: observed|self_reported|inferred

# ── L3. MEMORY STATE (per KC, per item — the layer nobody ships) ────
# Borrowed wholesale from the SRS literature, which is the only part of
# learner modeling with a validated decay model.
memory:
  - kc_id: ...
    model: { name: "FSRS", version: "7", params_ref: <hash> }
    stability_days: 42.7               # interval at which R = 0.90
    difficulty: 5.2
    last_review: <iso8601>
    retrievability_now: 0.83           # DERIVED; recompute, never store stale
    curve: "power"                     # audit trail for the functional form

# ── L4. BELIEF STATE (knowledge AND error, symmetrically) ───────────
knowledge:
  - kc_id: ...
    estimate: 0.62
    interval: [0.48, 0.74]             # uncertainty is mandatory
    model: { name: "BestLR", version: "...", trained_on: <hash> }
    calibration_ref: <reliability-diagram-hash>   # §3.3
    evidence_refs: [ulid, ...]
    learner_annotation: "I think this is wrong — I only missed those
                         because I misread the sign"      # Bull 2016

misconceptions:                         # ← the first-class citizen
  - misconception_id: "fci:impetus-force-in-motion"
    kc_ids: [...]
    status: active | dormant | refuted
    strength: 0.7
    evidence_refs: [ulid, ...]          # which distractors, when
    refutation_history:
      - { ts: ..., intervention: "refutation_text", outcome: partial }
    last_observed: <iso8601>

# ── L5. INSTRUCTIONAL PRIORS (what to DO with the above) ────────────
# Deliberately short. This is where "learning styles" would go, and it
# is empty on purpose (§5.2).
instructional:
  expertise_level:                      # Kalyuga & Sweller rapid assessment
    - { domain: ..., level: novice|intermediate|expert,
        measured_by: "first_step_verification", ts: ... }
  guidance_policy: derived_from_expertise_level   # expertise reversal
  accommodations: [...]                 # accessibility; learner-declared
  # NO learning-style field. NO personality field. NO affect inference
  # (EU AI Act Art. 5(1)(f) prohibits emotion inference in education).

# ── L6. GOVERNANCE (co-equal with the data, not an appendix) ────────
governance:
  grants:
    - grantee: <did>
      scope: [kc_ids | domains | layers]
      purpose: instruction | assessment | research
      expires: <iso8601>                # MUST be finite
      revocable: true                   # MUST be true
      export_permitted: false           # onward transfer default-deny
      log_ref: <access-log-uri>         # learner-readable access log
  retention:
    evidence_ttl_days: <int>            # forces a §5(1)(e) answer
    derived_ttl_days: <int>
    forgetting_policy: user_controlled  # Barua et al. 2011
  erasure_receipts: [...]               # proof of deletion, GDPR Art.17
  high_risk_declaration:                # EU AI Act Annex III(3)(b)
    steers_learning: bool
    conformity_ref: <uri>
```

### 8.3 The guarantees the format must make

A PLM implementation is conformant only if it can demonstrate all nine:

| # | Guarantee | Enforced by |
|---|---|---|
| G1 | **Recomputability** — every derived number regenerates from L2 alone | model id + params hash on every estimate |
| G2 | **Decay-awareness** — no knowledge claim is served without a retrievability adjustment | L3 mandatory; `retrievability_now` is derived, never stored |
| G3 | **Calibration disclosure** — any estimate shown to a human or fed to a policy carries its reliability | `calibration_ref` required |
| G4 | **Error symmetry** — misconceptions are queryable exactly as knowledge is | L4 has two co-equal sections |
| G5 | **Learner custody** — no provider holds the authoritative copy | pairwise ids + scoped, expiring grants |
| G6 | **Finite grants** — no unbounded, irrevocable, or onward-transferable access | `expires` required; `export_permitted` default-deny |
| G7 | **Effective erasure** — deletion propagates to derived state and produces a receipt | `erasure_receipts` |
| G8 | **Contestability** — the learner can annotate or dispute any estimate, and the dispute travels with it | `learner_annotation` |
| G9 | **Majority transfer** — custody moves from guardian to learner on a fixed date, automatically | `guardianship.transition_at` |

### 8.4 What this deliberately does not do

- **It does not standardise the model.** FSRS-7 today, something else in 2030. The schema
  standardises the *evidence* and the *interface*, and versions the model.
- **It does not promise better predictions.** §1 and §2 say that ceiling is reached. The
  claim is better *portability, continuity, longevity, and diagnosis* — none of which AUC
  measures.
- **It does not centralise.** There is no PLM registry. That is the inBloom lesson.
- **It carries no affect or emotion inference.** EU AI Act Art. 5(1)(f) prohibits it in
  education, and the survey should treat that as good policy rather than a constraint.

### 8.5 The three hard unsolved problems

Stated as open problems for Wave G / F9, not hand-waved:

1. **The KC alignment problem.** L1 is the load-bearing layer and there is no adequate
   public knowledge-component vocabulary. Gervet et al. found expert KC models add ≤0.01
   AUC on 7 of 9 datasets and that 4 of 9 have KC models so poor a skill-only model loses
   to an item-difficulty-only model. **Portability across providers requires a shared
   domain map, and the evidence says our domain maps are bad.** This is the binding
   constraint on the whole proposal.
2. **The misconception vocabulary problem.** The FCI's ~30 items encode decades of physics
   -education interviews. Nothing comparable exists for most of the curriculum. The Eedi
   corpus (>20M answers) is the raw material; the labels are the missing work — and this is
   the most obvious high-value application of frontier models in learner modeling.
3. **The verification problem.** L2 requires `attested_by` and a signature. A learner-owned
   record that the learner can also forge is worthless for high-stakes use — but a record
   only institutions can write is not learner-owned. The resolution is probably that
   **self-attested evidence and issuer-attested evidence coexist with different
   `confidence` values and different downstream permissions**, which is what the
   `provenance.confidence` field encodes. This is unsolved.

---

## 9. Negative and null results in this section (PRD §8.2 compliance)

1. A **zero-parameter moving-average baseline beats every released FSRS version** on log
   loss over 350M reviews (§1.4).
2. **Duolingo's Half-Life Regression is worse than a constant baseline** on its own
   published metric, and worse than a zero-parameter baseline on independent benchmarks
   (§1.7).
3. **FSRS's fitted decay does not generalise across retention levels**, and cannot recover a
   known decay on simulated data (§1.5).
4. **Memrise's fixed interval ladder is within 2% of FSRS on simulated learning efficiency**
   (§1.6).
5. **No controlled evidence that FSRS improves learning outcomes vs SM-2** (§1.8).
6. **DKT's original 0.86 vs 0.67 result was inflated by 23.6% duplicated rows** plus
   scaffolding leakage plus repeated sequences; cleaned, **PFA matches DKT** (§2.2a).
7. **BKT with recency and individualisation is indistinguishable from DKT** (§2.2b).
8. **IRT variants match or beat DKT on all tested datasets** (§2.2c).
9. **SAKT fails independent replication on all nine datasets**; reported 0.85 vs observed
   0.73 (§2.2d).
10. **DAS3H's time-window features add no predictive power** (§2.2d).
11. **Expert-designed knowledge-component models add ≤0.01 AUC on 7 of 9 datasets** (§2.2d).
12. **pyKT: label leakage inflates results; most DLKT gains over 2015 DKT are minimal**
    (§2.2e).
13. **Best-in-class KT models are severely miscalibrated on some datasets** (§2.2d) —
    which undermines every open learner model built on them (§3.3).
14. **Learning-analytics dashboards / OLMs mostly evaluate perception, not learning**; the
    field's own title is "Awareness Is Not Enough" (§3.2).
15. **Learning styles: no crossover interaction, repeatedly** (§5.2).
16. **FERPA has no private right of action** and its only remedy has never been used
    (§7.1).
17. **FERPA-grade de-identification destroyed the research utility of the MITx/HarvardX
    corpus** (§7.2).
18. **89% of 163 EdTech products in 49 countries put children's rights at risk** (§7.2).
19. **inBloom collapsed despite ~$100M and multi-state backing** — centralised custody, not
    schema, was the failure (§7.2).
20. **No public dataset contains a single learner's traces across years and subjects**
    (§4.2).

---

## 10. Source ledger

**Spaced repetition (18).** Woźniak SM-2 spec; Woźniak & Gorzelańczyk 1994
`10.55782/ane-1994-1003`; Woźniak, Gorzelańczyk & Murakowski 1995 `10.55782/ane-1995-1090`;
`open-spaced-repetition/srs-benchmark`; `awesome-fsrs` wiki "The Algorithm"/"The Metric";
`srs-benchmark/models/fsrs_v7.py`; `SSP-MMC-FSRS`; `heterogeneous-memory-research`;
srs-benchmark issue #166; `fsrs-vs-sm15`; `fsrs-vs-sm17`; `anki-revlogs-10k` (HF); Anki
manual (deck options) + FAQ; ankitects/anki #2633, #3616, #3929, #4391; Ye, Su & Cao 2022
`10.1145/3534678.3539081`; Su, Ye, Nie, Cao & Chen 2023 `10.1109/TKDE.2023.3251721`;
Settles & Meeder 2016 `10.18653/v1/P16-1174` + `duolingo/halflife-regression` issues.

**Memory science (7).** Wixted & Ebbesen 1991 `10.1111/j.1467-9280.1991.tb00175.x`; Wixted
& Ebbesen 1997 `10.3758/BF03211316`; Averell & Heathcote 2011 `10.1016/j.jmp.2010.08.009`;
Murre & Dros 2015 `10.1371/journal.pone.0120644`; Cepeda et al. 2008
`10.1111/j.1467-9280.2008.02209.x`; Cepeda et al. 2006 `10.1037/0033-2909.132.3.354`;
Rohrer, Taylor, Pashler & Wixted 2004 `10.1002/acp.1083`.

**SRS outcomes (4).** Lindsey, Shroyer, Pashler & Mozer 2014 `10.1177/0956797613504302`;
Tabibian et al. 2019 `10.1073/pnas.1815156116`; Upadhyay et al. 2021
`10.1038/s41539-021-00105-8`; Frappa et al. 2026 `10.1007/s40670-026-02643-5`.

**Knowledge tracing models (10).** Corbett & Anderson 1995 `10.1007/BF01099821`; Cen,
Koedinger & Junker 2006 `10.1007/11774303_17`; Pavlik, Cen & Koedinger 2009
`10.3233/978-1-60750-028-5-531`; Beck & Chang 2007 `10.1007/978-3-540-73078-1_17`;
Yudelson, Koedinger & Gordon 2013 `10.1007/978-3-642-39112-5_18`; Pelánek et al. 2016
`10.1007/s11257-016-9185-7`; Piech et al. 2015 arXiv:1506.05908; Pandey & Karypis 2019
(EDM 2019 #87); Ghosh, Heffernan & Lan 2020 `10.1145/3394486.3403282`; Choi et al. 2020
(EdNet) `10.1007/978-3-030-52240-7_13`.

**Knowledge tracing critiques (6).** Xiong, Zhao, Van Inwegen & Beck 2016 (EDM 2016,
pp. 545–550); Khajah, Lindsey & Mozer 2016 arXiv:1604.02416; Wilson, Karklin, Han &
Ekanadham 2016 arXiv:1604.02336; Gervet, Koedinger, Schneider & Mitchell 2020 JEDM
12(3):31–54; Liu et al. 2022 arXiv:2206.11460; Ding & Larson 2019 (EDM 2019 #60,
`UNVERIFIED-IN-SESSION`).

**Open learner models (9).** Bull & Kay 2007 `10.3233/irg-2007-17(2)02`; Bull & Kay 2016
`10.1007/s40593-015-0090-8`; Bull & Kay 2010 `10.1007/978-3-642-14363-2_15`; Bull 2020
`10.1109/TLT.2020.2978473`; Bull 2016 `10.1186/s41039-016-0035-3`; Bodily et al. 2018
`10.1145/3170358.3170409`; Matcha et al. 2020 `10.1109/TLT.2019.2916802`; Jivet et al. 2018
`10.1145/3170358.3170421`; Jivet et al. 2017 `10.1007/978-3-319-66610-5_7`. Plus Loboda et
al. 2014 `10.1007/978-3-319-11200-8_18`; Brusilovsky 2017 `10.1145/3038535.3038545`; Biswas
et al. 2005 `10.1080/08839510590910200`.

**Lifelong / scrutable models (5).** Kay & Kummerfeld 2012 `10.1145/2395123.2395129`; Kay &
Kummerfeld 2019 `10.1111/bjet.12878`; Barua, Kay, Kummerfeld & Paris 2011
`10.1145/2071536.2071541`; Barua, Kay & Paris 2013 `10.1145/2541016.2541034`; Kay 2021
`10.1145/3406522.3444755`.

**Prior knowledge / expertise reversal / learning styles (9).** Dochy, Segers & Buehl 1999
`10.3102/00346543069002145`; Kalyuga, Ayres, Chandler & Sweller 2003
`10.1207/S15326985EP3801_4`; Kalyuga & Sweller 2004 `10.1037/0022-0663.96.3.558`; Kalyuga &
Sweller 2005 `10.1007/BF02504800`; Tobias 2009 `10.1007/s11251-009-9103-z`; Snow 1992
`10.1146/annurev.psych.43.1.583`; Pashler, McDaniel, Rohrer & Bjork 2008
`10.1111/j.1539-6053.2009.01038.x`; Rohrer & Pashler 2012
`10.1111/j.1365-2923.2012.04273.x`; Newton & Salvi 2020 `10.3389/feduc.2020.602451`.

**Misconceptions (9).** Brown & Burton 1978 `10.1207/s15516709cog0202_4`; Brown & VanLehn
`10.1016/B978-1-4832-1446-7.50031-5`; Hestenes, Wells & Swackhamer 1992
`10.1119/1.2343497`; Hake 1998 `10.1119/1.18809`; Huffman & Heller 1995
`10.1119/1.2344279`; Briggs, Alonzo, Schwab & Wilson 2006 `10.1207/s15326977ea1101_2`;
de la Torre 2009 `10.3102/1076998607309474`; de la Torre 2011 `10.1007/s11336-011-9207-7`;
Wang et al. 2020 arXiv:2007.12061. Plus Guzzetti et al. 1993 `10.2307/747886`; Tippett 2010
`10.1007/s10763-010-9203-x`.

**Privacy / law / standards (11).** 20 U.S.C. §1232g (FERPA); *Gonzaga Univ. v. Doe*, 536
U.S. 273 (2002); 15 U.S.C. §§6501–6506 / 16 CFR 312 (COPPA, `UNVERIFIED-IN-SESSION` on 2025
amendments); Regulation (EU) 2016/679 (GDPR); Regulation (EU) 2024/1689 (EU AI Act,
Annex III(3) verified verbatim); Cal. B&P §22584 (SOPIPA); Bulger, McCormick & Pitcan 2017
`10.69985/klul2611`; HRW 25 May 2022; Daries et al. 2014 `10.1145/2643132`; Kleppmann et
al. 2019 `10.1145/3359591.3359737`; W3C VC Data Model 2.0 (Rec, 15 May 2025); W3C DID Core
1.0 (Rec, July 2022); 1EdTech CLR Standard 2.0 / Open Badges 3.0; IEEE 9274.1.1-2023
(xAPI).

---

## 11. Handoff notes for the survey draft

- **Lead with the parallel.** Two independent literatures, two decades apart in maturity,
  both found that simple baselines match sophisticated models. That convergence is the
  section's strongest claim and it is fully sourced.
- **The strongest single sentence available:** in 1978 Brown & Burton built a system that
  could explain *why* a student made a mistake; in 2026 the state of the art outputs a
  scalar probability that they will get the next one right.
- **Re-verify before publication:** COPPA 2025 amendment dates and §312 subsections; EU AI
  Act applicability dates against the Official Journal; FERPA enforcement history; Bodily
  et al. 2018 review counts; Illuminate/Chegg breach figures; Ding & Larson 2019 content.
- **Cross-refs:** F1 (assessment) needs §6 on distractors as the assessment primitive; F8
  (safety/children) inherits §7 wholesale; F9 (open problems) should take §8.5's three hard
  problems verbatim; G2 (reference architecture) should take the §8.2 schema; B2 (tutoring
  efficacy) should note §1.8's absence of outcome evidence.
- **Buildable claim for `apps/`:** the §8.2 schema is small enough to implement as a
  SQLite-backed local store with an FSRS-7 memory layer and an Eedi-style misconception
  table — a natural reference-implementation candidate demonstrating G1, G2 and G4.

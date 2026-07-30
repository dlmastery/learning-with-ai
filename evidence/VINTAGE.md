# VINTAGE — what class of system produced each number, and when

**Scope.** Every effect size that appears in `survey/*.md`, `README.md`, `docs/index.html`,
`docs/deck.html`, `docs/thesis.html`. Each one is traced back to the report in `research/raw/`
that introduced it, and from there to the primary source the report names.

**Method.** No year is inferred. Where a report establishes the vintage, it is given with the
report and line that establishes it. Where the corpus does not establish it, the cell reads
**unestablished** — not a guess, not a decade, not "1980s". Several of the most-cited numbers in
this survey have unestablished constituent-study vintages, and that is itself a finding.

**System class.**

| Class | Means |
|---|---|
| `HUMAN` | a human tutor or human-delivered instruction |
| `ITS` | rule-based / pre-LLM adaptive system |
| `FRONTIER` | an LLM from 2023 onward |
| `TECHNIQUE` | an instructional manipulation, not a delivery system — no system class applies |
| `MIXED` | a pooled or constructed estimate spanning classes; composition given where the source reports it |

**Line numbers are as of this scan (2026-07-30).** Other agents are editing these files
concurrently. Each worklist entry in §5 carries the quoted string as well, so it stays findable
after the lines move.

---

## 1. The four anchors

### 1.1 Bloom's 2σ

| | |
|---|---|
| **Number** | 2.0 SD ("two sigma") |
| **Effect of** | a **bundle**: one-to-one tutoring **+** intensively coached tutors **+** mastery-style repeated quizzing with corrective feedback and retesting **+** tutoring that *replaced* rather than supplemented classroom instruction |
| **System class** | `HUMAN` |
| **Source** | Bloom, B. S. (1984), "The 2 Sigma Problem: The Search for Methods of Group Instruction as Effective as One-to-One Tutoring", *Educational Researcher* 13(6):4–16, `doi:10.3102/0013189X013006004` |
| **Underlying studies** | **Two University of Chicago doctoral dissertations — Joanne Anania and Arthur J. Burke — neither credited as co-author.** Grades 4, 5 and 8. Topics: probability (4–5) and cartography (8). Outcomes on narrow author-written tests of unfamiliar material. **Anania's experiment ran three weeks.** All the Chicago dissertations gave the mastery classes **20–33% more instructional time** than controls. |
| **Year of the underlying studies** | **Unestablished.** The corpus dates them only relatively: they precede Bloom 1984, are named by Slavin (1987) as "the Chicago dissertations", and are described by von Hippel (2024) as small short experiments. No fieldwork year is recorded anywhere in `research/raw/`. Record the claim's year (1984) and the constituent years as unestablished. |
| **Established by** | `research/raw/B1-learning-science.md` §7 lines 337–396 (via von Hippel 2024, *Education Next*); `research/raw/I1-pedagogical-systems.md` §4.3 lines 429–447; `research/raw/K1-compression.md` lines 271–295; `survey/45-sequencing-and-durability.md` §5 (Slavin 1987, *RER* 57(2):175–213) |
| **Why it does not survive** | Same experiments, narrow vs broad tests: **0.84 SD vs 0.27 SD**. Cohen, Kulik & Kulik (1982, *AERJ*, 65 studies): mean ≈ **0.33 SD**, and **only 1 of 65** reported a two-sigma effect. Nickow (96 RCTs): **none** produced a two-sigma effect. Slavin (1987), restricted to real schools running ≥4 weeks with equal time and standardised measures — 7 studies qualified, **median +0.04**; retention at 4–12 weeks **median ≈ zero**. von Hippel attributes roughly half the remaining effect to the quiz–feedback–retest loop, not the tutoring. |
| **Mentions** | 22 occurrences of "Bloom" (excluding inBloom) and 11 of "2σ / two sigma" across the five surfaces; 91 across the whole published corpus including `PAPER.md` and `docs/paper.html`. |
| **Used as a bound on frontier systems?** | **No — and this is the one anchor the corpus handles correctly.** It is explicitly retired in five places (`survey/24:212`, `survey/19:207`, `survey/19:331`, `survey/03:48`, `survey/45:176`) and is excluded by name from the dashboard chart (`docs/index.html:219`, "Bloom's 2σ does not appear, because it does not replicate"). **The residual defect is rhetorical, not evidential**: a 1984 human-tutor bundle is invoked 22 times as the thing being refuted, which keeps it as the corpus's reference point for what an AI tutor is measured against. `docs/index.html:222` still calibrates against it — *"Chasing 2σ inflates the target roughly 7× against the pooled estimate"* — where the pooled estimate is Nickow's **human** tutoring number. |

### 1.2 The 0.2–0.4 SD band — full provenance

This band anchors the survey's central claim and its concession conditions. Its provenance has
not previously been written down. Here it is.

**Where the string originates.** `research/raw/B2-ai-tutoring-efficacy.md`, §8 "THE ONE-PARAGRAPH
VERDICT", lines 696–698, verbatim:

> *"Well-designed, teacher-supervised LLM tutoring interventions produce immediate post-test
> gains of roughly **0.2–0.4 SD** — the same band as pre-LLM intelligent tutoring systems
> (0.32–0.42 g) and in-person human tutoring (0.288 SD), at much lower cost."*

**The band is `FRONTIER` by construction.** It is a rounding of three LLM-era field trials. It is
not a pooled estimate, it has no confidence interval, it is not from any meta-analysis, and it is
not a pre-LLM number. Its constituents, from `B2` §1a:

| Trial | Value | System | Fieldwork | Notes that the band conceals |
|---|---|---|---|---|
| Sierra Leone, Gemini Guided Learning | **+0.258 SD** adjusted | `FRONTIER` (Gemini 2.5 → 3.0 Pro) | 6 Oct – 5 Dec 2025; report 2026-05-15 | Unadjusted ITT **+0.216, SE 0.137, not significant**. Model swapped mid-trial. |
| Nigeria, Copilot/GPT-4 after-school English (World Bank) | **+0.23–0.31 SD** | `FRONTIER` (GPT-4) | 2025 | ~43% attrition (759 analysed of 1,328). Distal exam **+0.206**, i.e. it shrinks. |
| Rori, Ghana, WhatsApp maths | **0.37 SD** | `FRONTIER` | 2024 | **11 clusters.** Authors are Rising Academies staff — developer-run. |

Three trials. One headline is non-significant unadjusted, one loses a third of its effect on the
school's own exam, one has eleven clusters and is developer-authored. **That is the entire
empirical content of "the measured 0.2–0.4 SD band."**

**The comparators attached to it — this is where the classes get mixed.**

| Comparator as printed | What it actually is | Class | Year |
|---|---|---|---|
| "pre-LLM intelligent tutoring systems (0.32–0.42 g)" | **A constructed range that appears in no single source.** Spliced from Steenbergen-Hu & Cooper (2014, *JEP*, 39 studies, college): g = **0.32–0.37**; and Ma et al. (2014, *JEP*, 107 effect sizes, 14,321 participants): g = **0.42** for ITS vs teacher-led classroom. | `ITS` | Both metas published **2014**. **Constituent study years unestablished** in this corpus. |
| "in-person human tutoring (0.288 SD)" | Nickow, Oreopoulos & Quan pooled estimate — see §1.3 | `HUMAN` | AERJ 2024. **Constituent study years unestablished.** |

**Three different ITS ranges circulate in the corpus from the same two 2014 meta-analyses.**
`survey/09` prints the ITS row as **"d = 0.76; g = 0.32–0.57"** in its table and **"ITS
0.32–0.42"** in the prose two lines below; `survey/01` prints **"0.32–0.42"**. The 0.57 is Ma et
al.'s ITS-vs-*other-computer-based-instruction* figure — a third comparator again. No source
reports 0.32–0.42 or 0.32–0.57 as a range.

**What went wrong in transit.** The band starts as a description of what three frontier trials
measured. By `survey/09:277` it has become the reporting rule — *"Quote the band, not the
ceiling. 0.2–0.4 SD, the same band as ITS and human tutoring"* — and by `survey/20:255`,
`survey/21:288` and `README:130` it is the ceiling a frontier system must break to earn its
mechanisms. **A frontier-era measurement of n = 3 trials has been re-described as a shared
pre-LLM band and then used as a bound on frontier systems.** The one surface that states its
class correctly is `README:122` and `survey/03:171`, which say the band describes systems that
"answer freely, forget everything between sessions" — an accurate description of an LLM chatbot,
but neither says the band is three trials.

**What the band is NOT — three misreadings to avoid when rewriting.**

1. **It is not an average across three machines.** No averaging was performed anywhere. `B2`'s
   sentence attributes the band to the LLM interventions and names ITS and human tutoring as
   *coinciding with* it — *"the same band as"*. Writing that the band "is an average taken across
   human tutors, ITS and LLM deployments" invents a computation that no source performed, and it
   makes the frontier trials disappear into a pooled quantity that does not exist.
2. **It is not a pooled estimate and has no confidence interval.** It is a rounding, by one
   research agent, of three trial point-estimates. It has no k, no SE, no I², no CI.
3. **It is not a population parameter.** `survey/20`'s Premise 1 argues it might be one. That is
   a stated counter-case, correctly labelled as such, and it is not a finding.

**Mentions.** 14 across the five surfaces; 36 across the published corpus including `PAPER.md`.

### 1.3 Nickow, Oreopoulos & Quan

| | |
|---|---|
| **Number** | **0.288 SD (SE 0.029)**, 96 randomised studies |
| **Effect of** | intensive in-person one-to-one and small-group **human** tutoring — teacher, paraprofessional, non-professional and parent tutors. **Zero AI arms.** |
| **System class** | `HUMAN` |
| **Source** | *AERJ*, `doi:10.3102/00028312231208687`. Online-first 2023, issue 2024 — the corpus cites both years (`B1:369` says 2023, `B2:99` says 2024). Funded by J-PAL North America, independent. |
| **Superseded value** | NBER working paper **w27476 (2020): 0.37 SD**, same team. The estimate fell 0.37 → 0.288 between working paper and peer review. |
| **Sub-estimate** | ≈**0.25 SD** for studies with n > 400 — effects plateau with sample size, they do not vanish. |
| **Year of the underlying studies** | **Upper bound established; span unestablished.** `research/raw/B2-ai-tutoring-efficacy.md:100` records that the 2020 NBER working paper pooled **the same 96 studies**. Every constituent trial therefore predates 2020, and *a fortiori* predates GPT-4 (March 2023). That upper bound is safe to publish. **The lower bound and the span are unestablished** — no date range for the 96 trials appears in `B1`, `B2`, `I1` or anywhere in `research/raw/`. Safe: *"96 randomised trials, all of them run before 2020."* Not safe: any decade, median year, or span. |
| **Correction status** | **C-6** (Bloom's 2σ does not replicate; the replacement figures are VanLehn 0.79 / ITS 0.76 / Nickow 0.288). **C-12** (0.37 was published in five places including a chart bar labelled "the honest field-wide number"; caught by external review). The 0.37 may never appear without 0.288 nearby — `evidence/check-corrections.py` rule `C-6/C-12` enforces this. |
| **Mentions** | 8 across the five surfaces; 16 across the published corpus. |
| **Used as a bound on frontier systems?** | **Yes.** `docs/index.html:519` places it in the ladder as *"the honest field-wide number"* with no indication that the field in question is human tutoring. `survey/03:50` uses it, with VanLehn, as the frame inside which Kestin's frontier RCT is judged. `survey/09:277` makes it half of the standing reporting rule for AI claims. |

### 1.4 VanLehn

| | |
|---|---|
| **Numbers** | human tutoring **d = 0.79**; step-based/substep ITS **d = 0.76**. (Answer-based CAI d ≈ 0.3, ITS d ≈ 1.0 and human tutors d ≈ 2.0 were the *believed* values the review tested and **did not confirm**.) |
| **Effect of** | **two different classes in one paper.** The 0.79 is human tutors. The 0.76 is rule-based intelligent tutoring systems. |
| **System class** | `HUMAN` (0.79) and `ITS` (0.76) — never quote one without saying which |
| **Source** | VanLehn, K. (2011), "The Relative Effectiveness of Human Tutoring, Intelligent Tutoring Systems, and Other Tutoring Systems", *Educational Psychologist* 46(4), `doi:10.1080/00461520.2011.611369`. Funded ONR N00014-00-1-0600 and five NSF grants. |
| **Year of the review** | **2011.** |
| **Year of the underlying studies** | **Unestablished.** `B2:87` describes it only as a "review of controlled experiments"; `I1:221–227` and `B1:400–404` quote its conclusions without a date range. The upper bound is 2011 and the ONR grant number implies work from 2000 onward, but the corpus establishes neither the span nor the median year of the reviewed trials. **Do not write "1980s–2000s"** — that is not established here. |
| **Correction status** | Referenced by **C-6** as the replacement for Bloom's 2σ. No correction against VanLehn's own values. |
| **Mentions** | 6 across the five surfaces; 12 across the published corpus. |
| **Used as a bound on frontier systems?** | **Yes, and this is the single most direct category error in the corpus.** `docs/index.html:507` renders the row `{label:"Human tutoring", note:"VanLehn — the real ceiling, not 2σ", v:0.79}` at the top of a sorted ladder headed *"What actually works, and by how much"* — three rows above `{label:"Best AI tutor RCT", ... v:0.63}`. A 2011 human-tutoring synthesis is labelled **"the real ceiling"** and a 2024 frontier RCT is plotted beneath it. Neither row carries a year or a system class. |

---

## 2. Table 1 — every effect size, with vintage and class

Sorted by section of the corpus. `where` gives the surface that publishes it; `bound?` answers
"is this currently used as a bound on frontier systems?"

### 2.1 Tutoring and tutoring-system effects — the numbers where class matters most

| Number | Effect of | Class | Year of underlying studies | Where it appears | Bound on frontier? |
|---|---|---|---|---|---|
| **2.0 SD** | Bloom's tutoring+mastery bundle | `HUMAN` | Claim 1984; constituent Chicago dissertations **unestablished** | `survey/03`, `survey/19` ×2, `survey/24`, `survey/45` ×3, `docs/index.html:219,222` | No — retired by name, but retained as the calibration point |
| **0.84 / 0.27 SD** | same Bloom experiments, narrow vs broad tests | `HUMAN` | **unestablished** (pre-1984) | `survey/24:34` | Used to justify a general 2–3× test-alignment discount applied to modern trials |
| **1.00 SD** | Bloom's own mastery-learning claim "done systematically and well" | `HUMAN` | pre-1984, **unestablished** | `survey/45:164` | No |
| **0.52 / 0.54 SD** | Kulik et al. mastery learning | `HUMAN` | pre-1987, **unestablished** | `survey/45:163` | No |
| **0.81 SD** | Walberg, mastery learning | `HUMAN` | pre-1987, **unestablished** | `survey/45:164` | No |
| **+0.04 median** | Slavin 1987 best-evidence synthesis, 7 qualifying studies, real schools ≥4 weeks, standardised measures | `HUMAN` | studies pre-1987; **individual years unestablished** | `survey/45:169` | No |
| **≈0 median** | Slavin retention, 6 comparisons in 5 studies at 4–12 weeks | `HUMAN` | pre-1987, **unestablished** | `survey/45:183` | No |
| **0.79** | VanLehn human tutoring | `HUMAN` | review **2011**; constituents **unestablished** | `survey/03:48`, `survey/19:208`, `docs/index.html:219,507` | **Yes** — labelled "the real ceiling" |
| **0.76** | VanLehn ITS (step/substep) | `ITS` | review **2011**; constituents **unestablished** | `survey/03:48`, `survey/09:45`, `survey/19:209`, `docs/index.html:220,508` | **Yes** — plotted above the best frontier RCT |
| **0.288 SD (SE 0.029)** | Nickow pooled human tutoring, 96 RCTs | `HUMAN` | meta **2024** (online 2023); constituents **unestablished** | `survey/01:162`, `survey/03:50`, `survey/09:31,46,206`, `survey/19:210`, `docs/index.html:221,519` | **Yes** |
| **0.37 SD** | Nickow **2020 working paper** — superseded | `HUMAN` | 2020 | `survey/09:206`, `docs/index.html:451,519,547` — all as the superseded value | Ledger-quoted only (C-12) |
| **≈0.25 SD** | Nickow large-sample subset, n > 400 | `HUMAN` | **unestablished** | `research/raw/B2:101` only — not on a published surface | n/a |
| **0.33 SD** | Cohen, Kulik & Kulik 1982, 65 tutoring studies | `HUMAN` | meta **1982**; constituents **unestablished** | `research/raw/B1:368`, `C3:695` — not on a published surface | n/a |
| **g = 0.32–0.42** | **constructed splice**, ITS vs classroom | `ITS` | **two 2014 metas**; constituents **unestablished** | `survey/01:162`, `survey/09:49` | **Yes** — it is half the "same band" claim |
| **g = 0.32–0.57** | same splice, different endpoint (Ma's other-CBI comparator) | `ITS` | 2014 | `survey/09:45` | **Yes**, and it contradicts the line above |
| **g = 0.32–0.37** | Steenbergen-Hu & Cooper 2014, 39 studies, college; ITS **less** effective than human tutoring; **earlier studies significantly larger than recent** | `ITS` | meta **2014**; constituents **unestablished** | `research/raw/B2:89` — not published verbatim on a surface | n/a |
| **g = 0.42 / 0.57 / 0.35 / −0.11 / 0.05** | Ma et al. 2014, ITS vs teacher-led / other CBI / textbook / **individual human tutoring (ns)** / **small group (ns)**; 107 ES, 14,321 participants | `ITS` | meta **2014**; constituents **unestablished** | `research/raw/B2:88` — **the two null comparisons are never published on a surface** | n/a |
| **median 0.66** | Kulik & Fletcher 2016, 50 ITS evaluations — magnitude "depended to a great extent" on local vs standardised tests | `ITS` | meta **2016**; constituents **unestablished** | `survey/24:36` (the caveat only, not the 0.66) | No |
| **+0.21 SD (year 2); null (year 1)** | Pane et al., Cognitive Tutor Algebra I, 147 schools, 7 states | `ITS` | trial **2014** | `survey/09:269` | No — used correctly, as the shape an 8-week trial cannot see |
| **significant, largest for low prior achievers** | Roschelle et al., ASSISTments, end-of-year state test, 43 Maine schools | `ITS` | trial **2016/2020** | `survey/09:265` | No — used correctly |
| **positive but "mitigated"** | Létourneau et al. 2025, 28 studies, N = 4,597, mostly quasi-experimental, K-12 | `ITS` | meta **2025**; constituents **unestablished** | `research/raw/B2:91` — not on a surface | n/a |
| **+5 months, $1,625/pupil** | EEF/E4L one-to-one tuition, 123 studies | `HUMAN` | toolkit; constituents **unestablished** | `research/raw/I1:212` — not on a surface | n/a |

### 2.2 The frontier-era trials — see §3 for the full quotable forms

| Number | Effect of | Class | Year | Where | Bound? |
|---|---|---|---|---|---|
| **+0.258 / +0.216 SD** | Gemini Guided Learning, Sierra Leone | `FRONTIER` | fieldwork **Oct–Dec 2025** | `survey/01`, `survey/09:38,78`, `docs/index.html` | n/a — it *is* frontier evidence |
| **+0.310 / +0.206 SD** | Copilot/GPT-4, Nigeria | `FRONTIER` | **2025** | `survey/09:39` | n/a |
| **−17% / −0.004** | Bastani et al., unassisted exam | `FRONTIER` (GPT-4) | PNAS **2025** | `README:90`, `survey/01`, `survey/09:40,149`, `docs/index.html` | n/a |
| **+48% / +127%** | Bastani, assisted practice | `FRONTIER` | **2025** | `survey/09:148` | n/a — and never quotable alone (C-2) |
| **d ≈ 0.63** | Kestin, Harvard physics AI tutor | `FRONTIER` | Sci Rep **2025** | `survey/03:51`, `survey/09:41`, `docs/index.html:509` | n/a |
| **+4 p.p. proximal / null distal** | Tutor CoPilot | `FRONTIER` | **2024** | `survey/09:42,174` | n/a |
| **0.37 SD** | Rori, Ghana | `FRONTIER` | **2024** | `survey/09:43` | n/a |
| **+5.5 p.p.** | LearnLM + Eedi transfer vs human tutors | `FRONTIER` | Dec **2025** | `survey/09:44` | n/a |
| **g = 0.683 / 1.426 / 0.077** | Gu & Yan, LLM tutoring with / without teacher support | `FRONTIER` meta | **2025**, 19 studies | `README`, `survey/01:165`, `survey/09:186`, `docs/thesis.html:91,93,99` | n/a |
| **g = 0.867** | Wang & Fan — **RETRACTED 2026** | `FRONTIER` meta | 2025, retracted 2026 | `survey/01:160`, `survey/09:200,278` | Never quotable |
| **no better than chance** | TutorGym, 223 domains, 4 models | `FRONTIER` (**Aug–Oct 2024 snapshots**) | **2024** | `README:55`, `survey/32:64`, `survey/38:11`, `docs/deck.html:178`, `docs/thesis.html:157,249` | **Yes — a 2024 frontier measurement bounding 2026 frontier systems** |
| **79.2 / 83.8 / 21.0 / 4.6 %** | SWE-bench Verified / Terminal-Bench 2.1 / PaperBench / SciCode | `FRONTIER` bench | **2025** | `README:70`, `docs/thesis.html:150` | n/a |

### 2.3 Instructional techniques — no system class applies

These are `TECHNIQUE` effects. They are not measurements of any tutor, human or machine, and the
HUMAN/ITS/FRONTIER trichotomy does not apply to them. They are listed because they appear in the
published effect-size ladder alongside tutoring numbers, where a reader will read them as
comparable.

| Number | Effect of | Source and year | Constituent years | Where |
|---|---|---|---|---|
| **g = 0.56** | learning by teaching, prep + delivery | Kobayashi **2019**, k = 28 | **unestablished** | `docs/index.html:510` — C-7 requires "human learning-by-teaching"; the teachable-agent version is **untested** |
| **g = 0.55** | induced self-explanation, 69 ES / 64 reports | Bisra, Liu, Nesbit, Salimi & Winne **2018**, *EPR* | **unestablished** | `docs/index.html:511` |
| **d = 0.54 [0.31, 0.77]** | spacing on curriculum materials, 22 reports / 31 effects / N > 3,000 | **2025** classroom meta-analysis, PMC12189222 | **unestablished** | `docs/index.html:512`, `docs/thesis.html:74` — C-15: **not** "the Cepeda tradition" |
| **g = 0.50 (0.499 [0.442, 0.557])** | retrieval practice, 222 classroom studies / 48,478 students, **I² = 88%** | **unestablished** meta year | **unestablished** | `docs/index.html:513`, `docs/thesis.html:73` — C-16: I² must travel with it |
| **g = 0.48 (181 ES, 55 studies)** | worked examples on maths | Barbieri et al. **2023**, *EPR* | **unestablished** | `docs/index.html:514` |
| **+0.505 / −0.428** | expertise reversal, novices vs experts | Tetzlaff et al.; components imply ≈0.93 | **unestablished** | `docs/index.html:514`, `docs/thesis.html:75` — C-4: **d = 0.971 is not verifiable**; C-25 narrows the interaction to assistance/guidance |
| **g = 0.48 / −0.02** | teaching after prep, with / **without** teaching expectancy, k = 39 | Kobayashi **2024** | **unestablished** | `docs/index.html:515,524` |
| **g = 0.46** | computer-based scaffolding, 144 studies | Belland, Walker, Kim & Lefler **2017**, *RER* | **unestablished** | `docs/index.html:516` |
| **g = 0.42** | interleaving | Brunmair & Richter; lab effects 0.42–0.67 | **unestablished** | `docs/index.html:517` |
| **g = 0.38 (contiguity 0.74 [0.67,0.82], k=46; spatial 0.63 [0.55,0.71], k=58)** | Mayer design principles | Ginns **2006**; Schroeder & Cenkci **2018** | **unestablished** | `docs/index.html:518` |
| **g = 0.36 (0.87 bias-corrected)** | productive failure / PS-I, 53 studies / 166 comparisons | Sinha & Kapur **2021** | **unestablished** | `docs/index.html:520` |
| **+0.327 SD (pooled); +0.121 ITT / +0.167 ToT** | voice call + SMS, 5 countries, N = 8,902 | Angrist et al., NBER 31208; *Nat Hum Behav* **2022** | **unestablished** | `docs/index.html:521` |
| **ES = 0.24** | immersive VR (HMD) vs desktop/traditional, 35 RCT/quasi | Wu, Yu & Gu **2020**, *BJET* | **studies 2013–2019** — the one row where the corpus *does* establish the span | `docs/index.html:522` |
| **d = 0.23** | animation vs static | **unestablished** | **unestablished** | `docs/index.html:523` |
| **g = 0.22, p = .40** (2nd est. 0.14, p = .59) | Orton-Gillingham vs active comparison | **unestablished** | **unestablished** | `docs/index.html:524`, `survey/20:196` — C-3 |
| **d = 0.20; −0.06 when the robot replaces a teacher** | physical robot vs same content on screen, 78 controlled studies | de Winter et al. **2026** | **unestablished** | `docs/index.html:525` |
| **g = 0.19 [0.12, 0.27], k = 43** | pedagogical agents; 3D agents 0.11 n.s. | Schroeder et al. **2013**; Castro-Alonso et al. **2021** g = 0.20 | **unestablished** | `docs/index.html:526`, `docs/thesis.html:425` |
| **d = .85–1.01** | pedagogical avatars, affect, three field experiments — **learning did not move** | **2024** | 2024 | `docs/index.html` SLOPE, `docs/thesis.html:426` | |
| **0.067 [−0.103, 0.236]** | slides vs no slides | **unestablished** | **unestablished** | `docs/index.html:527` |
| **g = 0.032 / 0.034 n.s., k = 54, I² = 0%** | expanding vs uniform retrieval intervals | Latimier, Peyre & Ramus **2020/2021**, *EPR* | **unestablished** | `docs/index.html:528`, `survey/20:197`, `survey/21:277` |
| **ES 0.02 [−0.06, 0.09], p = .65** | EEF Lesson Study, 181 schools, n = 6,437 (12,747 pupils cited in `survey/21`) | Murphy, Weinhardt, Wyness & Rolfe **2017** | 2017 | `docs/index.html:529`, `survey/20:198`, `survey/21:275` |
| **0.0, moderate-strength evidence of no effect** | alternative seating on attention, 21 level-I/II studies | *Frontiers in Pediatrics* **2025** | **unestablished** | `docs/index.html:530` |
| **0.0** | learning styles meshing hypothesis | four decades of nulls; Rogowsky **2015**, Husmann & O'Loughlin **2019** (N=426), Melzner & Kappes **2024** (N=222) | 2015–2024 | `docs/index.html:531`, `survey/24` |
| **d ≈ 0.48 preference / 0 knowledge** | infographic vs plain-language Cochrane summary, **three RCTs, n = 334, adults, immediate quiz** | Buljan et al. **2018** | 2018 | `README:81`, `docs/deck.html:207`, `docs/index.html` SLOPE, `docs/thesis.html:264`, `survey/03:160` | **C-52 — published as a general law with the scope stripped** |
| **g = .034, p = .180 / none ≠ 0** | testing accommodations | Kieffer et al.; Rios et al. (N = 11,069); Elbaum **2007** reverses at secondary | **unestablished** | `survey/20`, `survey/04` — C-27 |
| **21 of 41 (51%)** | Doroudi et al., RL-induced instructional sequencing beating all baselines | **2019** | **unestablished** | `survey/13` — C-29, **C-61 unresolved** (21 of 41 vs the R6 report's 21 of 36) |
| **d = 0.72 / r = .12–.30 family** | teacher–student relationship | Hattie repackages Cornelius-White **2007**; Roorda **2011**; Emslander et al. **2025** (26 metas, 2.64M students) is the authoritative synthesis | **unestablished** | `survey/40` — C-55, C-56 (**nested, not independent**) |
| **d = 0.754 vs g = .25** | gamification, 2026 three-level meta (193 trials, 1,029 effects) vs the 2020 behavioural cell the survey leans on | **2026** vs **2020** | 2026 / 2020 | `docs/thesis.html:457` — C-53: the 2026 estimate is **not cited anywhere in the corpus** |

---

## 3. Table 2 — every frontier-era measurement in the corpus

This is the evidence that is actually about frontier systems. Each row is given in the form that
is safe to quote. Where a published correction applies, quoting the row without the stated
qualifier reproduces a corrected error.

| # | Measurement | Estimand | n | Interval / precision | Correction status | Safe-to-quote form |
|---|---|---|---|---|---|---|
| **F1** | **Sierra Leone**, Gemini Guided Learning (DeepMind + Fab AI; report 2026-05-15; AEARCTR-0016651) | ITT on an IRT-scaled, curriculum-aligned maths endline, built and blind-scored by Oxford MeasurEd | 1,423 analysed (1,763 enrolled); 48 classrooms, 12 schools; 8 weeks | Adjusted **+0.258 SD, 95% CI [0.027, 0.488], p = 0.029**. **Unadjusted +0.216, SE 0.137 — not significant.** ToT at 12 h +0.380. Treatment × baseline **+0.195 SD per baseline SD, 95% CI [0.074, 0.315], p = 0.002**. Grade 8 × treatment +0.429, p<0.01; Grade 7 main **−0.078, p<0.05** | **C-1** (never "the strongest evidence in the history of educational technology"; the unadjusted n.s. estimate must appear beside the adjusted one). **C-22** (**eight weeks**, not a school year) | *"+0.258 SD adjusted (95% CI [0.027, 0.488], p = 0.029) over eight weeks; the unadjusted estimate is +0.216, SE 0.137, not significant."* |
| **F2** | **Nigeria**, Copilot/GPT-4 after-school English (World Bank, 2025) | ITT on a composite and on the school's own third-term exam | 1,328 randomised; **759 analysed (~43% attrition)**; 6 weeks | **+0.310 SD composite (SE 0.068)**; +0.23–0.24 SD English; **+0.206 SD on the school's own exam (SE 0.067)** | None | *"+0.310 SD on the intervention-aligned composite and +0.206 SD on the school's own exam, with ~43% attrition."* Always publish both. |
| **F3** | **Bastani et al.**, Turkey (PNAS 2025) | assisted-practice performance, and a closed-book AI-removed exam on conceptually matched problems | ~1,000 students, ~50 classrooms; 4 × 90-min sessions | Practice: GPT Base **+0.137 (SE 0.031) = +48%**; GPT Tutor **+0.361 (SE 0.032) = +127%**. Unassisted exam: GPT Base **−0.054 (SE 0.022), p<0.05 = −17%**; GPT Tutor **−0.004 (SE 0.013), n.s.** | **C-2** (guardrails **remove harm**; they do not add benefit — the guardrailed coefficient is −0.004 n.s.). **C-11** (the PNAS notice `10.1073/pnas.2518204122` is an **author-affiliation erratum**; no datum or conclusion altered; the −17% stands). **C-54** (109 citing works in fourteen months contain **no replication with a withdrawal design** — state this wherever the −17% is load-bearing) | *"Unguarded GPT-4 left students 17% worse on a later unassisted exam (−0.054, SE 0.022, p<0.05); the guardrailed arm's unassisted coefficient is −0.004, not significant. No replication with a withdrawal design exists."* |
| **F4** | **Kestin et al.**, Harvard physics AI tutor (*Sci Rep* 2025, 15:17458) | post-test score vs an in-class active-learning hour | 194 enrolled; 142 AI / 174 in-class post-tests; two ~1-hour lessons a week apart | **d ≈ 0.63** (regression), p < 10⁻⁸. Separately, **0.73–1.3 ceiling-corrected** — a different estimand. Median 49 min vs an *assumed* 60. No time-on-task correlation with score | **C-13** (**"0.63–0.73" is a range that exists in no source** — the regression estimate spliced to a ceiling-corrected floor, then the midpoint plotted). Developer-built, developer-evaluated, **no funding statement** | *"d ≈ 0.63 on a researcher-built post-test, in a study whose first author built the tutor and ran the analysis and which declares no funding."* Do not write 0.63–0.73. |
| **F5** | **Tutor CoPilot** (Stanford, 2024) | exit-ticket mastery (proximal) **and** end-of-year state maths test (distal) | 900 tutors, 1,800 K-12 students, 4,136 sessions; ~2 months | **+4 p.p. exit-ticket, p < 0.01**; +9 p.p. for students of the lowest-rated tutors. Distal: **"we did not find statistically significant improvements in end-of-year math test scores"** | None. Independently funded (Smith Richardson; Arnold Ventures/Accelerate) | *"+4 p.p. on the in-platform exit ticket, p<0.01, and null on the end-of-year state test."* The null is not optional. |
| **F6** | **LearnLM + Eedi**, UK secondary (Google DeepMind + Eedi, Dec 2025) | accuracy on the first question of the *next* study unit — a transfer item — against **human tutors** | **165** students, 5 schools | LearnLM **66.2% [61.1, 71.2]** vs human tutors **60.7% [55.8, 65.4]** vs baseline 56.2% [54.2, 58.2]. **+5.5 p.p. with a credible interval spanning zero** | Developer-run. Related: **C-43** on the same trial's 74.4% figure | *"+5.5 p.p. on a transfer item against human tutors, n = 165, with a credible interval spanning zero."* |
| **F7** | **Eedi draft acceptance** (same trial) | proportion of LearnLM-drafted tutor messages accepted with no edits | 3,617 drafted messages | **74.4% (2,691/3,617)** — verifies exactly. The abstract's 76.4% is "zero or minimal edits". Five factual errors = 0.1%; zero harmful/risky | **C-43** (the authors state their design **"precludes a rigorous measurement of throughput or efficiency"**; the published throughput gain comes from a **six-tutor role-play simulation** with a labour rate cited to a marketplace blog post) | *"74.4% of drafts accepted unmodified (2,691/3,617) — a measured signal stream, not measured productivity."* |
| **F8** | **Rori**, Ghana (Rising Academies, 2024) | maths growth, on top of normal instruction | ~1,000 students, **11 clusters**; 8 months | **0.37 SD, p < 0.001** | None in the ledger. Developer-authored; **11 clusters**; year 1 only | *"0.37 SD across 11 clusters in a developer-authored study."* Never quote 0.37 without the cluster count. |
| **F9** | **Nie et al., "The GPT Surprise"** (L@S 2025) | ITT effect of *advertising* GPT-4 access on exam participation and score | **5,831** students, 146 countries | **Significant average decrease in exam participation.** The positive exam effect for adopters is selection, not a randomised contrast — peer review made the authors retitle | None | *"Randomised offer of GPT-4 access significantly reduced exam participation; the positive adopter effect is selection."* |
| **F10** | **Lehmann, Cornelius & Sting** | overall learning outcome, two preregistered incentivised lab experiments plus a field study | lab **107** and **69**; field 113 grad students / 6,775 observations | **No main effect in either preregistered experiment.** Substitutive use ↓ understanding; **"LLMs harm the learning of students with less prior knowledge"** | None | *"Two preregistered lab experiments, n = 107 and n = 69: no effect on overall learning outcomes, plus gap-widening."* |
| **F11** | **Gu & Yan (2025)**, *JECR* | pooled LLM effect on learning, moderated by teacher support | 19 studies, k = 24 | **g = 0.683 overall; with teacher support g = 1.426; without teacher support g = 0.077** | None | *"g = 0.077 without teacher support; g = 1.426 with it. The measured entity is teacher-plus-AI activity design."* |
| **F12** | **Wang & Fan (2025)**, *Hum Soc Sci Commun* | pooled ChatGPT effect on learning performance | 51 studies | g = **0.867** | **RETRACTED 2026** for "discrepancies in the meta-analysis"; authors did not respond; >250 citations accrued | **Not quotable as a finding in any form.** Quotable only as "the field's headline meta-analysis was retracted." |
| **F13** | **Liu, Guo, He & Hu (2025)**, *JECR* | pooled achievement and motivation | 49 articles | achievement **0.857**, motivation 0.803 | None — but flag: magnitude indistinguishable from the retracted F12 | Quote only with that flag. |
| **F14** | **(2025)** *JCAL* 70117 | pooled | 34 studies | g = **0.68** (cognitive 0.795 / competency 0.711 / affective 0.507) | None | Safe. |
| **F15** | **Wu & Yu (2023)**, *BJET* | pooled | 24 randomised studies | "large effect"; **short interventions > long**, which the authors attribute to novelty wearing off | None | Safe; the moderator is the useful part. |
| **F16** | **TutorGym** (arXiv:2505.01563, Weitekamp, Siddiqui & MacLellan) | labelling an incorrect student action, and next-step action correctness, inside a live ITS interface | 223 tutor domains; **four model snapshots**: `claude-3-5-sonnet-20241022`, `claude-3-5-haiku-20241022`, `gpt-4o-2024-08-06`, `deepseek-v2.5:236b` — **Aug–Oct 2024 vintage, zero-shot, no tool use** | **none better than chance** at labelling incorrect actions; next-step actions correct **~52–70%**. The authors call it an **"initial evaluation"** | **C-51** — "no LLM"/"no model" is superseded; the claim must be scoped to the models tested, and ProcessBench/BEA-2025 named as the adjacent positive literature. **LIVE VIOLATION on `docs/thesis.html`** (see §5) | *"Across 223 tutoring domains, the four models tested — an August–October 2024 snapshot set, in what the authors call an initial evaluation — did not beat chance at labelling an incorrect student action."* |
| **F17** | **ProcessBench** (arXiv:2412.06559, Qwen team, 9 Dec 2024) | identify the earliest step containing an error, or conclude all steps are correct | 3,400 human-annotated test cases | Prompted critic models **beat** trained PRMs. **QwQ-32B-Preview competitive with GPT-4o**; behind reasoning-specialised o1-mini | None | *"Open models are competitive with GPT-4o at identifying the earliest erroneous step; step-checking a model's own reasoning is not at chance."* |
| **F18** | **BEA 2025 Shared Task** (arXiv:2507.10579) on **MRBench** (arXiv:2412.09416) | mistake identification and guidance quality in tutor–student dialogue, against gold human annotations | over 50 international teams; MRBench = 192 conversations / 1,596 responses / 8 dimensions | Best **macro-F1 71.81** on Mistake Identification (3-class); **58.34** on providing guidance | None | **Currently absent from every published surface.** This is the frontier evidence on the exact operation the corpus says is unsolved. |
| **F19** | **LearnLM pedagogical evaluations** (Google, R1–R3) | a third-party expert's agreement with a statement about a transcript — pedagogical plausibility, **not learning** | not stated per evaluation | **+31% over GPT-4o; 73.2% overall win rate.** Rubric reliability, reported once: Krippendorff's **α = 0.359** overall; *inspires interest* **0.066**, *monitors motivation* **0.023**, *identifies goal* **0.031**. R2/R3 report no inter-rater statistic. Learners showed **"no substantial preference"** | None in the ledger, but Google's own text: *"it is unclear how well the results translate to improvements in learning outcomes"* | *"+31% over GPT-4o on expert-rated pedagogical plausibility, on a rubric whose overall Krippendorff's α is 0.359."* **Never as a learning effect.** |
| **F20** | **Agentic benchmarks** (`K2`, MEASURED-BENCH, 2025) | task solve rate under a strong vs weak external check | SWE-bench Verified 396/500 | **79.2%** SWE-bench Verified; **83.8% ± 1.2** Terminal-Bench 2.1; **21.0%** PaperBench replication score; **4.6%** SciCode main-problem solve rate | **C-37 / C-40** — the rule is a **bound**, not an equality, and **SciCode does have hand-written tests** | *"The value of an agentic loop is bounded by the value of the external check it closes on: 79.2% and 83.8% where the check is strong, 21.0% and 4.6% where it is weak — and SciCode has hand-written tests, which is why it is a bound."* |
| **F21** | **ERIC census**, run 2026-07-27 against `api.ies.ed.gov/eric/` | count of records | — | ChatGPT **1,668**; + "learning outcomes" **95**; + "delayed post-test" **2**; + "retention test" **0**; + "transfer test" **0**; + "preregistered" **0**; control "delayed post-test" any topic **273**. Seven randomised trials, **three** of them second-language learning | **C-58** (three, not four; EJ1415077 is a foundational chemistry course, EJ1484052 is VR with IoT tasks) | Safe in the corrected form. **Note an unreconciled inconsistency: `survey/09` publishes 1,668 ChatGPT records while `README`, `survey/23`, `survey/44` and `docs/thesis.html` publish 1,565.** Not in the ledger. |
| **F22** | **arXiv census**, 20 education-AI subfields | proportion of papers carrying any learning-outcome marker | 2,907 papers | at most **1.79%**; **eight subfields at exactly zero** | None | Safe. |
| **F23** | **Disability census** (ERIC + Europe PMC) | randomised trials of generative-AI tutoring mentioning students, vs mentioning disability | 30 trials | **30 mention students; zero mention disability, dyslexia, ADHD, autism, special education or an IEP** | None | Safe. |
| **F24** | **Inference cost share** (`M1`) | inference as a fraction of delivered session cost in a human-supervised model | two independent measurements | **0.43%** — £0.0037 of a £0.861 session; and $19.86/tutor/year measured API spend against a tutor at the US mean wage | **C-42** — "a $500/hour tutor at token cost" is the **wrong frame** for a human-in-the-loop model; falling token prices are economically irrelevant to this P&L | *"Inference is 0.43% of delivered session cost; the margin question is the leverage ratio, which nobody has measured."* |
| **F25** | **AI-native rebuild comparable** (`M1`) | gross margin and expert cost for a listed tutoring company that rebuilt on AI-native codebases | one audited company | gross margin **67.5% → 58.0%**; expert costs **up $5.2M** on revenue **down $11.2M** | **C-44** — the only audited comparable, and it is negative; omitting it was the failure this project exists to name | Safe, and required wherever the business case is made. |
| **F26** | **PaThA protocol** (`G1`, our own) | discrimination of a permutation-based fidelity check vs plain self-consistency | 768 generations, two models | **87.5%/87.5%** and **100%/100%** — exactly at chance both times; self-consistency wins by 18.8 and 43.8 points | **C-9** — our own hypothesis, benchmarked and falsified | Safe. |
| **F27** | **Rewind/replay density** (`N4`, our own) | whether replay peaks mark comprehension failure | 51 videos | median entropy **0.976** (1.0 = flat); enrichment **1.95×**; peaks closer to chapter boundaries than chance; **min–max normalised within video in 51 of 51 cases** | **C-49** — dead three ways, and LectureScape (UIST 2014) already built and nulled it | Safe. |
| **F28** | **Quantifier-prefix check** (`N4`, our own) | fire rate of a proposed decidable check on lecture transcripts | 1,524 sentences of MIT OCW transcripts | **fired zero times.** Overall lexical precision across the predicate set: **7 true positives from 30 flags (23%)** | **C-50** — not refuted, relocated: a check for authored prose, not transcript mining | Safe. |
| **F29** | **Adversary item space** (demo) | addressable distinct items | — | **14,929,920** addressable items; **99.66% distinctness measured** | **C-20** — the space is finite and measured, never "unbounded" | Safe. |
| **F30** | **Numeric grounding check** (demo) | recall and latency of a grounding harness | two harnesses | **99.1% recall at 0.38 ms and 0.61 ms** — both reported. A third implementation measures 170 ns on a smaller set and is not comparable | **C-21** — report both, not the flattering one | Safe. |
| **F31** | **Production mastery-threshold experiment** (`survey/08`) | retention difference from raising the mastery threshold | 32.9 million randomised topic sequences | **+29% time for a retention difference under 0.02** | None | Safe. |
| **F32** | **Learning-rate variation** (`README`) | spread in learning rate vs prior knowledge | 1.3 million observations | rate varies **1.14×** between the 25th and 75th percentile; prior knowledge varies **3.6×** | None | Safe. |

---

## 4. What the composition tables show

1. **The corpus contains 32 distinct frontier-era measurements.** It leads with none of them.
   It leads with a 2011 review (`docs/index.html`), a 1984 essay it is refuting (`survey/03`),
   and a three-trial band re-described as a pre-LLM ceiling (`survey/01`, `survey/09`,
   `survey/20`, `survey/21`, `README`).

2. **Six of the frontier rows are positive and independently funded** — F2, F5's proximal arm,
   F9's adopter contrast, F11's teacher-supported cell, F17, F18 — and two of those (F17, F18)
   appear on **no published surface at all**.

3. **The vintage of the constituent studies is unestablished for every pre-LLM anchor.** Bloom's
   dissertations, VanLehn's reviewed trials, Nickow's 96 RCTs, Ma et al.'s 107 effect sizes,
   Steenbergen-Hu's 39 studies — the corpus establishes the *publication* year of each synthesis
   and the *span* of none of them. Only one row in the entire audit carries an established
   constituent range: Wu, Yu & Gu 2020, **studies 2013–2019**. Any artifact that wants to say
   "these numbers are old" must say so from the synthesis year, not from an invented span.

4. **The one place a frontier vintage is disclosed is `survey/32`**, which names TutorGym's four
   model snapshots. `README`, `docs/deck.html` and `docs/thesis.html` restate the same result
   without them, and `docs/thesis.html` restates it in the superseded form.

---

## 5. The worklist — specific claims that are category errors

A category error here means: **a measurement of one class of system used as a bound on another**,
with the class not named in the surrounding text. File, line as of 2026-07-30, and the quoted
string so the entry survives renumbering.

### 5.1 Pre-LLM numbers bounding frontier systems

| # | File:line | Quoted string | What is wrong |
|---|---|---|---|
| **V1** | `docs/index.html:507` | `note:"VanLehn — the real ceiling, not 2σ", v:0.79` | A **2011 human-tutoring** synthesis is labelled **"the real ceiling"** at the top of a sorted ladder headed *"What actually works, and by how much"*, three rows above `"Best AI tutor RCT"` at 0.63. The row carries no year and no system class. This is the corpus's most-viewed artifact. |
| **V2** | `docs/index.html:508` | `note:"VanLehn — statistically indistinguishable from human", v:0.76` | A **2011 rule-based ITS** number, plotted above the best frontier RCT, with no year and no indication that it is pre-LLM. A reader ranks it as a current capability. |
| **V3** | `docs/index.html:509` | `{label:"Best AI tutor RCT", ... v:0.63}` | The *ordering itself* is the bound claim. Kestin's 2025 frontier RCT is rendered as sitting below two pre-2011 rows on one axis, with no note that the three measure different classes of system on different instruments. |
| **V4** | `docs/index.html:219–223` | *"VanLehn measured human tutoring at 0.79 and intelligent tutoring at 0.76; Nickow's pooled tutoring RCTs land at 0.288 … Chasing 2σ inflates the target roughly 7× against the pooled estimate"* | The figcaption calibrates the whole chart — including its frontier rows — against a 2011 review and a human-tutoring pooled estimate. Neither is dated in the caption; neither is identified as measuring something other than an AI system. |
| **V5** | `docs/index.html:519` | `note:"Nickow 2024 AERJ, 96 randomised studies — the honest field-wide number"` | **"The honest field-wide number"** does not say which field. On a dashboard about AI tutoring, a reader takes it as the field-wide number for AI tutoring. It is 96 human-tutoring RCTs. |
| **V6** | `survey/03-the-vision.md:48–54` | *"VanLehn measured human tutoring at d = 0.79 and intelligent tutoring systems at 0.76; Nickow et al. pooled 96 randomised tutoring studies at 0.288 SD … Kestin's Harvard AI-tutor RCT landed at d ≈ 0.63 … That is inside the human tutoring range, which is the honest claim"* | A frontier RCT is judged by whether it falls *inside* a range built from a 2011 review and a human-tutoring meta-analysis, neither dated. "Inside the human tutoring range" is offered as the ceiling a frontier system has reached, not as a comparison across classes. |
| **V7** | `survey/09-the-scoreboard.md:277` | *"**Quote the band, not the ceiling.** 0.2–0.4 SD, the same band as ITS and human tutoring."* | This is the survey's **standing reporting rule**. It instructs every future frontier claim to be quoted against ITS and human numbers whose vintage is never stated and whose constituent years are unestablished. It is the mechanism by which the category error propagates. |
| **V8** | `survey/09-the-scoreboard.md:45` | `| Pre-LLM ITS (VanLehn; Ma et al.; Steenbergen-Hu) | d = 0.76; g = 0.32–0.57 | meta | — | — | — |` | A row of 2011/2014 meta-analytic estimates is placed inside a table introduced as *"Now the AI results"*, with the same columns (n, duration, delayed test, distal outcome) all filled with em-dashes. It reads as a comparable arm of the same experiment. |
| **V9** | `survey/09-the-scoreboard.md:48–51` | *"The good LLM trials land in the same band as pre-LLM intelligent tutoring systems and as human tutors. … ITS 0.32–0.42"* | **0.32–0.42 appears in no source.** It is spliced from Steenbergen-Hu & Cooper 2014 (0.32–0.37) and Ma et al. 2014 (0.42). It also contradicts the table three lines above it, which prints 0.32–0.57. |
| **V10** | `survey/01-central-finding.md:162–164` | *"supervised LLM tutoring lands at **0.2–0.4 SD** — the same band as pre-LLM ITS (0.32–0.42) and in-person human tutoring (**0.288**, 96 RCTs)"* | Same splice, in the survey's central-finding section. No year for either comparator, and no statement that the 0.2–0.4 band is itself three frontier trials. |
| **V11** | `survey/19-the-canon.md:207–212` | *"Human tutoring is **d = 0.79** in VanLehn's synthesis, and intelligent tutoring systems were already at **0.76** before LLMs existed … Expert one-to-one is worth roughly eight tenths of a standard deviation under favourable synthesis and under three tenths when you pool the trials."* | Partially correct — *"before LLMs existed"* is the right instinct — but the passage then installs 0.79/0.288 as the standing benchmark without saying VanLehn's constituent trial years are unestablished, and without saying that the number being benchmarked against is not a measurement of any AI system. |
| **V12** | `README.md:122` and `:130` | *"The measured 0.2–0.4 SD band describes systems that answer freely, forget everything between sessions…"* and *"landing inside the 0.2–0.4 band rather than above it would mean the mechanisms are decorative and the band is the ceiling"* | The class attribution is **correct** (it does describe LLM chatbots), but the band is presented as *the measured band of the technology* when it is a rounding of **three field trials**, one non-significant unadjusted, one with 43% attrition, one with 11 clusters and developer-authored. The concession condition of the entire project is staked on a number whose n is 3. |
| **V13** | `survey/20-the-agenda.md:255` and `survey/21:288` | *"We would concede that 0.2–0.4 SD is a real ceiling and not a floor"* / *"landing inside the 0.2–0.4 band. Not below it. Inside it. That would mean … the band is the ceiling."* | Same defect as V12, in the two places where it is load-bearing for falsifiability. A concession condition must state what the band is a measurement of and how many trials it rests on, or it cannot be evaluated. |
| **V14** | `survey/24-the-floor.md:34` | *"Bloom's tutoring studies gave **0.84 SD** on the authors' own narrow tests versus **0.27 SD** on broad standardised tests"* | Correctly attributed to Bloom, but generalised into a rule — *"Any evaluation in which the system's designers also wrote the test should be discounted before you read the number"* — that is then applied to frontier trials. The 2–3× discount is derived from two early-1980s dissertations plus Kulik & Fletcher's ITS corpus. The rule may well be right; its evidential base is pre-LLM and is not stated as such. |

### 5.2 Frontier numbers bounding later frontier systems

| # | File:line | Quoted string | What is wrong |
|---|---|---|---|
| **V15** | `docs/thesis.html:157` | *"Across 223 real tutoring domains, **no model** beat chance at labelling an incorrect student action."* | **Live C-51 violation.** The corrected form is "the four models tested", in "what the authors call an initial evaluation". `evidence/check-corrections.py` does not catch it because `docs/thesis.html` **is not in its `SURFACES` list** — `SURFACES` covers `README.md`, `PAPER.md`, `process/CLAUDE.md`, `process/AUDIT.md`, `docs/index.html`, `docs/paper.html`, `survey/*.md`, `docs/demos/*.html`, and neither `docs/thesis.html` nor `docs/deck.html`. This is a hole in the propagation checker of exactly the shape C-30 and C-36 describe. |
| **V16** | `docs/thesis.html:249` | *"nowhere near solved by the labs, which sit at chance across 223 domains"* | Same measurement, restated as a claim about *"the labs"* in July 2026, from four **August–October 2024** model snapshots evaluated zero-shot with no tool use. |
| **V17** | `docs/deck.html:178` | *"Across 223 tutoring domains, the models tested did not beat chance"* | Correctly scoped by model set, but carries **no vintage**. A deck slide asserting a capability limit in 2026 from a 2024 snapshot must date it. |
| **V18** | `README.md:55` | *"Across **223 tutoring domains, the models tested did not beat chance** at labelling an incorrect student action"* | Scoped, undated. This is the README's headline finding — *"the finding the survey turns on"* — and it is a 2024 measurement. |
| **V19** | absent from every surface | — | **F18 (BEA 2025 Shared Task, macro-F1 71.81 on Mistake Identification across 50+ teams, on gold human annotations)** appears nowhere on a published surface. It measures the closest published construct to the one the corpus says is unsolved. Its absence is what makes V15–V18 read as settled. |

### 5.3 Non-system numbers published as general laws

| # | File:line | Quoted string | What is wrong |
|---|---|---|---|
| **V20** | `README.md:81`, `docs/deck.html:207`, `docs/thesis.html:264` | *"Preference shifts at **d ≈ 0.48** while knowledge stays flat"* / *"Preference moves at **d ≈ 0.48** while knowledge does not move"* | **C-52 is live on all three surfaces.** Buljan et al. 2018 is **three RCTs, n = 334, infographic vs plain-language Cochrane summary, adults, immediate quiz** — and it is published as a general law about learner preference, with no population, material or interval. C-52 also records that the evidence label was upgraded `MEASURED-RCT` → `MEASURED-META` in two reports, always in the direction of making the negative sturdier. |
| **V21** | `docs/thesis.html:457` | *"weakest and least stable cell in the table: behavioural **g = .25**"* | **C-53**: no gamification meta-analysis after 2020 is cited anywhere in the corpus, while a 2026 three-level meta-analysis (193 trials, 1,029 effect sizes) reports **d = 0.754**. The negative was frozen while positives were re-audited. |

### 5.4 Summary

**21 distinct category-error claims**, across 14 sites:

- **14 pre-LLM-bounds-frontier** (V1–V14), concentrated in `docs/index.html` (5) and `survey/09` (3);
- **5 frontier-bounds-later-frontier** (V15–V19), all traceable to one 2024 four-model snapshot;
- **2 non-system-published-as-law** (V20–V21).

Two of these are **live published corrections that no checker catches**: V15/V16 (C-51 on
`docs/thesis.html`) and V20 (C-52 on three surfaces). The immediate structural fix is to add
`docs/thesis.html` and `docs/deck.html` to `SURFACES` in `evidence/check-corrections.py`;
`evidence/check-vintage.py` scans them already.

---

## 6. The machine check

`evidence/check-vintage.py` encodes §5 as rules. Each rule fires when a legacy or
out-of-vintage number appears within a proximity window of a claim about what an AI or frontier
system can achieve, **unless** the nearby text names the class of system the number measured.

```bash
python3 evidence/check-vintage.py --self-test --strict
```

`--self-test` plants each rule's known-bad probe in a scratch copy of the tree and fails if the
rule does not fire. A scan that finds fewer than 20 surfaces fails rather than reporting OK. Both
requirements exist because of **C-30**: the first corrections checker printed *"0 violations"*
while every error it was built to catch was present in the tree.

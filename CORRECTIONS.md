# Corrections ledger

**This file is the single source of truth for every correction made to this project.**
The dashboard and README summarise it; they do not maintain their own copies. That rule
exists because they *did* maintain their own copies, and those copies were silently
edited — see C-12 and C-13, which are the reason this file exists.

## The rule

1. A correction is **added as a row**, never applied by rewriting the previous row.
   Rewriting a ledger entry to show the corrected value destroys the record of the error.
2. Every row names **who caught it**. A project that only lists errors it found itself is
   advertising, not accounting.
3. A correction is not complete until it reaches **the sentence that was wrong** — not a
   footnote below it, not a banner above it. Prepending a correction and leaving the
   error standing is the failure mode that produced C-12 through C-17.

## Provenance key

| Code | Meaning |
|---|---|
| **SELF-RESEARCH** | Our own research agent read a primary source and contradicted our draft |
| **SELF-VERIFY** | We checked a claim — including a claim made *to* us — and rejected it |
| **EXTERNAL-REVIEW** | An adversarial reviewer found it. We did not. |

---

## The ledger

| # | Date | We said | Actually | Caught by |
|---|---|---|---|---|
| **C-1** | 25 Jul | Sierra Leone +0.258 SD — "the strongest evidence in the history of educational technology" | Unadjusted estimate **+0.216, SE 0.137 — not significant.** Loads entirely on Grade 8 (Grade 7 main effect −0.078); gaps widened at +0.195 SD per SD of baseline; differential attrition favouring treatment; pre-registered subdomain analyses abandoned | SELF-RESEARCH (B2) |
| **C-2** | 25 Jul | Guardrails teach — "+127% with no retention penalty" | Guardrails **remove harm**. The guardrailed arm's unassisted coefficient is **−0.004, n.s.** Harm removed; benefit not demonstrated | SELF-RESEARCH (B2) |
| **C-3** | 26 Jul | Orton-Gillingham is decades-replicated | **g = 0.22, p = .40** against active comparison; second estimate g = 0.14, p = .59. The evidenced ingredient is explicit systematic decoding, not the multisensory branding | SELF-RESEARCH (H1) |
| **C-4** | 26 Jul | Expertise reversal interaction **d = 0.971** | Not verifiable in any retrievable source. Reported components (novices +0.505, experts −0.428) imply **≈0.93** | SELF-RESEARCH (F10) |
| **C-5** | 26 Jul | Concreteness fading has a pooled effect size | **Fyfe et al. 2014 is a systematic review, not a meta-analysis.** No pooled effect size for concreteness fading exists anywhere. Four documented nulls, including a computing replication that went 3-of-4 null | SELF-RESEARCH (F10) |
| **C-6** | 27 Jul | Bloom's 2σ as the target | Does not replicate. **VanLehn: human tutoring 0.79, ITS 0.76. Nickow et al. 2024 (AERJ): 0.288 across 96 RCTs.** Chasing 2σ inflates the target and makes real results look like failures | SELF-RESEARCH (I1) |
| **C-7** | 27 Jul | **g = 0.56** is the teachable-agent effect | It is **human** learning-by-teaching (Kobayashi 2019). g = 0.43 is peer tutoring's effect on the tutor. Self-explanation is g = 0.55. **The teachable-agent version is untested** | SELF-RESEARCH (C3) |
| **C-8** | 27 Jul | AI tutoring widens gaps, full stop | A property of **untargeted delivery**. Across **eight targeted interventions, none widened gaps** and several sharply narrowed them. Gap-widening is a design failure we know how to avoid | SELF-RESEARCH (F4) |
| **C-9** | 27 Jul | The pāṭha permutation protocol should beat self-consistency for fidelity checking | **Benchmarked and falsified.** 768 generations, two models, deterministic comparator: 87.5%/87.5% and 100%/100% — exactly at chance both times. Plain self-consistency wins discrimination by 18.8 and 43.8 points | SELF-RESEARCH (G1) |
| **C-10** | 27 Jul | Deixis is complete greenfield — zero repos, zero papers | The **substrate exists**: arXiv:2604.02893, a 200k-diagram geometry segmentation engine at 49% IoU fine-tuned (<1% zero-shot). The tutoring loop and its efficacy measurement do not | SELF-RESEARCH (F9) |
| **C-11** | 26 Jul | *(claim made to us)* Bastani's −17% now carries a PNAS correction and must not be cited as settled | **Rejected.** The correction (10.1073/pnas.2518204122) is an **author-affiliation production erratum**. No datum, estimate, figure or conclusion altered. The −17% stands | SELF-VERIFY |
| **C-12** | 28 Jul | Nickow pooled tutoring **0.37**, published in five places including a chart bar labelled "the honest field-wide number" | **0.288.** The 0.37 is the superseded 2020 working-paper figure — and `survey/09` states our own rule to discount working-paper effect sizes. We broke our own rule on the front page | **EXTERNAL-REVIEW** |
| **C-13** | 28 Jul | Kestin AI tutor **"0.63–0.73"** | **A range that exists in no source.** 0.63 is the regression estimate; 0.73–1.3 is *ceiling-corrected* — two different estimands spliced, then the midpoint plotted. Correct: **d ≈ 0.63**, and the study is developer-built and developer-evaluated with no funding statement | **EXTERNAL-REVIEW** |
| **C-14** | 28 Jul | **98.4%** recognition proves a tutor "sees" handwritten work | It is **answer-position recognition** on a 61-exam grading benchmark, and its 0.58% false-negative rate requires **supplying the reference solution**. Error-*correction* on handwriting tops out at **77%** | **EXTERNAL-REVIEW** |
| **C-15** | 28 Jul | Spacing d = 0.54, from "the Cepeda meta-analytic tradition" | Sourced to a **2025 classroom meta-analysis** — 22 reports, 31 effects, N > 3,000, CI [0.31, 0.77]. Cepeda et al. 2006 is the canonical *lab* meta-analysis and gives different figures | **EXTERNAL-REVIEW** |
| **C-16** | 28 Jul | Retrieval practice g = 0.50, presented as settled | **I² = 88%** was omitted while I² was reported three times for null results — selective reporting, and exactly the failure this survey exists to name. Boundary conditions also added: at immediate test restudy often wins; unsuccessful retrieval **without feedback** yields little | **EXTERNAL-REVIEW** |
| **C-17** | 28 Jul | *(process)* `survey/01`'s Sierra Leone correction was appended 100 lines below the error, leaving "the strongest evidence in the history of educational technology" standing in the body | Corrected **in place**. A correction that does not reach the wrong sentence is not a correction | **EXTERNAL-REVIEW** |
| **C-18** | 28 Jul | EU AI Act **Annex III** education obligations apply from 2 August 2026 | **Deferred to 2 December 2027** by Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026), verified against EUR-Lex primary text. **Article 50 — chatbot disclosure and synthetic-content marking — still applies from 2 August 2026** | SELF-RESEARCH (E3) |
| **C-19** | 28 Jul | The village is "a crew of seven" | G2 specifies a **registry of ten**, and the governing number is the **active set of 3–5 per learner-hour** — the economics permit ~40, the orchestration evidence permits 3–5 | SELF-RESEARCH (survey writers) |
| **C-20** | 28 Jul | The adversary demo offers "unbounded item generation" | The space is **finite and measured: 14,929,920 addressable items, 99.66% distinctness measured** rather than asserted. The page prints the number | SELF-RESEARCH (demo builder) |
| **C-21** | 28 Jul | Numeric grounding check "99.1% recall @ 0.61 ms" | Two harnesses measured **0.38 ms and 0.61 ms**; both are now reported rather than the flattering one. A third implementation in the demo measures 170 ns on a smaller set and is not directly comparable | SELF-RESEARCH (demo builder) |
| **C-22** | 28 Jul | The Sierra Leone trial "ran across a school year" | It ran **eight weeks.** The error made the field's time horizon look better than it is, in the very section arguing that the horizon is too short | **EXTERNAL-REVIEW** |
| **C-23** | 28 Jul | *(process)* Corrections were applied by **rewriting the ledger rows in place** — inside a table headed "each published rather than silently edited" — and the six corrections of 28 July appeared in no ledger at all | This file. Rows are append-only, carry provenance, and the count is generated from the filesystem | **EXTERNAL-REVIEW** |
| **C-24** | 28 Jul | *(process)* Warned three times that `research/raw/E1-E2-*.md` exposes LessonOrca's confidential operating data — "churn economics, pricing, funnel" — and asked the owner to decide on scrubbing git history | **Mostly wrong, and it should have been checked before being raised.** §6's figures ($1,600 per churned student, $15,000 wasted labour per tutor) are the company's **own public marketing copy**, retrieved verbatim from `lessonorca.com` and labelled `VENDOR` in the report's own header. Republishing a company's published claims is not a leak. **The genuinely internal material is narrower: §7's product telemetry** (n = 31 starts, 22% signup conversion, 6% reaching first real action) — sourced from the author's own analytics, not public. That is the only part where a scrub decision is real | SELF-VERIFY |
| **C-25** | 28 Jul | §22 framed expertise reversal as *the one aptitude-treatment interaction that survived*, without qualification | **Narrower than stated.** Noetel's meta-meta-analysis found prior knowledge **did not consistently moderate multimedia design effects (p = 0.14)**. The reversal is well established for **assistance and guidance** manipulations and is **not reliably detectable across the broad multimedia-design corpus**. The survivor is *prior knowledge moderates how much help to give* — not *prior knowledge moderates instruction*. Both sections now state the tension rather than picking a side | SELF-RESEARCH (survey writer, §24) |
| **C-26** | 28 Jul | "WCAG 2.2 AA is the accessibility floor", published in two survey sections | **The ADA Title II web rule incorporates WCAG 2.1**, not 2.2 — and the compliance dates moved twelve months in April 2026 (91 FR 20902), to **26 April 2027** and **26 April 2028**. Most published guidance still says 2.2 and April 2026 | SELF-RESEARCH (H2) |
| **C-27** | 28 Jul | §04 treated testing accommodations as part of the "known-good intervention" base being scaled | **Legally mandated and evidentially weak.** Kieffer et al.: overall **g = .034, p = .180**. Rios et al.: **none statistically different from zero** across N = 11,069. Elbaum 2007: the effect **reverses** at secondary level. And teachers assign them **at chance** (N = 1,218). Both halves must be held: required by law, not established by evidence | SELF-RESEARCH (H2) |
| **C-28** | 28 Jul | "An AI that changes a child's programme without generating prior written notice has created a procedural violation" | **Directionally right, wrong in three specifics.** The duty attaches to the **agency**, not the tool; it fires on identification, evaluation, placement and FAPE provision — **not on teaching methodology**, which §300.501(b)(3) places outside the meeting requirement; and a procedural violation denies FAPE only through §300.513(a)(2)'s three gates. ED's own line governs: *"placement refers to the provision of special education and related services rather than a specific place"* (71 FR 46588) | SELF-RESEARCH (H2) |
| **C-29** | 28 Jul | Cited Doroudi et al. (2019) as a negative review, publishing only its **0-of-8** sub-cut on interdependent content | **The review's overall finding is positive.** Verbatim: *"We find that over half of the studies found that RL-induced policies significantly outperform baselines."* **21 of 41 studies (51%) significantly beat all baselines**; 10 no significant difference; 1 baseline win. Publishing the pessimistic sub-cut without the headline is selective reporting — the exact failure this survey exists to name. The authors' qualifier also favours us: RL works best *"constrained with ideas and theories from cognitive psychology and the learning sciences"* | SELF-RESEARCH (K2) |
| **C-30** | 28 Jul | *(process)* Shipped a corrections-propagation checker and reported it green | **It did not work.** A reviewer copied the tree, planted the five superseded values in the exact form they had originally appeared — including the chart datum `v:0.37` — and it printed *0 violations* and exited 0. Two defects: `[^.]{0,80}` as a proximity window cannot cross the period in *"Nickow et al."*, the literal string that caused C-12; and the cure words were generic enough that an unrelated *"corrected"* nearby cleared a live error. Rewritten with a `--self-test` that plants each violation and fails if the rule does not fire | **EXTERNAL-REVIEW** |
| **C-31** | 28 Jul | *(process)* Every one of the paper's 29 contents links was dead, and the generator's own docstring claimed a sticky contents rail that did not exist | Two hand-matched slugging rules — `build()` slugged the bare title, python-markdown slugged the rendered heading with its number — and **no test**. The outline is now a single declarative record that the rail, the contents and the headings all render from, so an anchor cannot exist in one and be missing in another | **EXTERNAL-REVIEW** |
| **C-32** | 28 Jul | The dashboard's headline read "24 sections · 60,300 words · 23 corrections" | Against a 30-section, 75,352-word, 25-correction paper — **stale on the page whose entire pitch is that it publishes its own errors.** Counts are now written into `index.html` and `README.md` on every build | **EXTERNAL-REVIEW** |
| **C-33** | 28 Jul | The effect-size chart was captioned "ordered" | **It was not sorted.** Applying C-12 changed Nickow's value from 0.37 to 0.288 and left the row in position, so 0.288 sat above 0.36. A correction that fixed a number and broke the artifact around it | **EXTERNAL-REVIEW** |
| **C-34** | 28 Jul | The paper's internal cross-references | **83 of 87 pointed at the wrong section.** Sections are numbered 1–33 at build time; the prose carried source-file numbers, so *"a hostile reviewer read §04"* pointed at *Fifteen Hundred Papers*. Only four landed, by coincidence — and the commit that added 26 more cross-references made it worse. `build()` now assigns paper numbers in a first pass and rewrites both `§NN` and prose "Section NN" forms; unresolved refs are reported, never silently rewritten. **All 115 now resolve** | **EXTERNAL-REVIEW** |
| **C-35** | 28 Jul | The abstract said "32 research reports · ~2,100 citations"; the head said 34; the filesystem said 35. And "eight of the twenty-nine corrections" against a generated scoreboard reading twelve of thirty-three | **C-32 reproduced inside the abstract** — hardcoded counts sitting beside computed ones. Every count in the paper head and abstract is now derived from the filesystem and the ledger at build time | **EXTERNAL-REVIEW** |
| **C-36** | 28 Jul | *(process)* The hardened checker was reported as working | **Still defeatable: 17 evasions planted, 1 caught.** A `\| C-99 \|` row claimed the ledger exemption without the id needing to exist; `PAPER.md` was not a surface at all; C-16's regex could not match the plain `0.50` form; and deleting every surface printed *"OK, 0 violations"* and exited 0. Fixed: exemption now checks the id against the real ledger, PAPER.md and paper.html are surfaces, the regex is widened, and a scan finding fewer than 20 surfaces **fails** | **EXTERNAL-REVIEW** |
| **C-37** | 28 Jul | §32: *"the value of an agentic loop **equals** the value of the external check it closes on"*, with SciCode tabled as having no check | **Overstated, and the table was wrong.** SciCode has hand-written tests and still lands at 4.6%. The rule is a **bound**, not an equality: a weak check caps you low; a strong one does not guarantee you reach the bound | **EXTERNAL-REVIEW** |

---

## Scoreboard

*Generated from the rows above by `evidence/sync-ledger.py`. It drifted twice while
hand-maintained, which is the whole argument for generating it.*

| Source | Count |
|---|---|
| Caught by our own research | 15 |
| Caught by our own verification — including of our own warnings | 2 |
| Caught by our own builders, working against their own briefs | 4 |
| **Caught by an adversarial external reviewer** | **16** |
| **Total** | **37** |

16 of 37 were found by someone whose job was to fail us — including
the two most damaging (C-12, C-13), the one about this ledger itself (C-23), and the one
that proved the propagation checker did not work (C-30). That ratio is the honest measure
of what an internal review process is worth, and it is the argument for commissioning the
hostile read rather than trusting the self-audit.

---
title: "Coverage audit — what 45 reports and 40 sections never covered, and whether the negative findings were fairly selected"
wave: Z
section: Z1
date_researched: 2026-07-30
sources_count: 24
status: raw-research
---

# Z1 — The Coverage Audit

> **What this document is.** Two audits of the corpus itself, not of the field. Part 1 asks
> what a complete treatment of tutoring would contain and marks what is here. Part 2 tests
> whether the corpus's documented audit-bias (`process/ASSUMPTIONS.md` A5: *"That the null
> results were the interesting part — MINE, not the owner's"*) also distorted **evidence
> selection** for the five load-bearing negative findings.
>
> **Method.** Titles and executive framing of all 45 reports in `research/raw/` and all 40
> section titles in `survey/` were read. Coverage was then tested by term census across
> `research/raw/` + `survey/` (word-boundary matched; false positives from substrings —
> `tran-sla-te` matching `SLA`, `tran-sport` matching `sport` — were removed by re-running
> with `grep -ow`). For the skew audit, five primary sources were re-retrieved this session
> and their scope compared against the corpus's own sentences.
>
> **Retrieval note.** WebSearch exhausted per `process/CLAUDE.md` §5. Retrieval ran on
> **ERIC** (`api.ies.ed.gov`, the workhorse), **Crossref REST**, **OpenAlex** (working this
> session — 109 citing works for Bastani enumerated), **Europe PMC**, and the **arXiv API**
> (`export.arxiv.org`, working). `arxiv.org/abs` HTML returned empty bodies to `curl` for two
> targets; `arxiv.org/html/` worked and is the route used for TutorGym's method section.
>
> **Evidence labels** are the project standard — `MEASURED-RCT` · `MEASURED-META` ·
> `MEASURED-BENCH` · `OBSERVED` · `INFERENCE` — plus `OBSERVED — absence` for a gap
> established by a stated, reproducible query, which is never treated as proof of
> non-existence, and `[X]` for a census performed in this session.

---

## 0. The two findings, stated first

**1. The largest uncovered area is the relationship.** Not "rapport" as a UX property — the
*affective teacher–student relationship* as a measured moderator of achievement, with a
meta-analytic base of 189 studies and 249,198 students that this corpus does not cite once.
Fourteen mentions of the word "rapport" across 75,000 lines, five of which are the surname of
an ADHD researcher. There is no report, and no survey section, whose subject is what a tutor
does that is not instruction.

**2. The negative-finding skew is real, but it is a *search* skew and a *drift* skew, not a
reporting skew.** Every one of the five load-bearing negatives was **accurately reported and
correctly scoped at the point of first entry**. Four of five are correctly scoped everywhere.
What went wrong is downstream: a correctly-bounded null in a raw report becomes a universal
design law by the time it reaches the survey, sometimes with its evidence label *upgraded*;
and once a negative is entered it is declared settled and the literature around it stops
being searched, while positive claims are re-audited continuously. Section 2 gives four
specific instances with the corpus's sentence and the source's sentence side by side.

---

# PART 1 — THE COVERAGE MAP

**Quality key.** **Owned** = a report exists whose subject is this. **Load-bearing** = covered
substantively inside a report about something else. **Incidental** = mentioned, not
researched. **Absent** = not present as a research object.

| # | Area | Covered? | Where | Quality |
|---|---|---|---|---|
| 1 | **The relationship — alliance, trust, the tutor who believes in you** | **No** | — | **Absent.** `rapport` 14 hits / 6 files, 9 of them the surname *Rapport, M.D.* (N2, V5). `working alliance` 0 · `therapeutic alliance` 0 · `teacher-student relationship` 0 · `Pianta` 0 · `warmth` 1 `[X]` |
| 2 | Mentorship as distinct from instruction | Partial | I2 (guru–śiṣya, ustād–shāgird), I1 (Oxbridge tutorial) | Incidental. Treated as a *cost structure* and a *mechanism-survival* question, never as a relationship |
| 3 | **Diagnosis before instruction / the first ten minutes** | Partial | J1 (the 15-second measurement), F5 §cold-start, F10 (entry-rung selection) | Load-bearing but unowned. `placement test` 0 · `intake` 4 · `first session` 0 `[X]`. J1 specifies *which technique fires*, not *how the session opens* |
| 4 | Prerequisite / readiness diagnosis | Partial | F5, J1 | `prerequisite` 187 hits but `prerequisite structure` 4, `learning progression` 1, `learning trajector*` 1 |
| 5 | **The parent** | Partial | H2 (parent as legal party: consent, PWN, revocation), F8 (COPPA/FERPA) | Load-bearing *legally*, absent *pedagogically*. Parental homework involvement, home learning environment: absent |
| 6 | The teacher as co-user | Partial | H1/H2 (SELPA practitioner), D3 (Tutor CoPilot) | Load-bearing. `teacher professional development` 1 hit; `teacher workload` 1 |
| 7 | The school / district as adopter | Partial | E1-E2, M1, N3 | Load-bearing on economics and procurement |
| 8 | **Homework, revision, exam technique, cramming** | **No** | K1 (time budget), F11 (spacing vs massing) | **Absent as an object.** `exam technique` 0 · `study skills` 0 · `past paper` 0 · `test preparation` 1 · `homework` 26 hits, all incidental `[X]` |
| 9 | **Reading — decoding, fluency, comprehension** | Partial | H1 only (structured literacy, Orton-Gillingham null, Bowers/phonics dispute) | **Load-bearing inside a special-education report.** `phonics` in 4 files, 14 of 17 hits in H1. No report owns reading acquisition for the typical learner |
| 10 | **Writing as a distinct skill** | **No** | — | **Absent.** `writing instruction` 0 · `essay feedback` 0 `[X]`. F1 treats the essay as a *sampling instrument to be replaced*, never as a skill to be taught |
| 11 | **Maths anxiety, test anxiety, stereotype threat, self-concept** | **No** | — | **Absent.** `math anxiety` 2 hits · `mathematics anxiety` 0 · `test anxiety` 0 · `stereotype threat` 0 · `self-concept` 3 · `growth mindset` 0 · `belonging` 2 `[X]`. F6 owns motivation (SDT, gamification, MOOC attrition); the clinical-affective layer is a different literature and is not here |
| 12 | **Groups — most learning happens near other people** | Partial | I1 (chavruta, jigsaw, peer instruction as *systems*), F2 (AI-as-peer) | **Weak.** `collaborative learning` 7 hits / 2 files · `cooperative learning` 5 · `classroom discourse` 0 · `accountable talk` 0 · `socially shared regulation` 0 `[X]`. The CSCL evidence base is not represented at all |
| 13 | **Very young children (pre-K, early numeracy/literacy)** | **No** | I1 (Montessori RCTs, incidentally) | **Absent.** `early childhood` 0 · `toddler` 0 · `emergent literacy` 0 · `preschool` 7 hits, all inside Montessori or IDEA §619 budget lines `[X]` |
| 14 | **Adults returning to study; reskilling** | **No** | — | **Absent.** `andragogy` 0 · `adult education` 0 · `reskilling` 0 · `returning to study` 0 · `adult learner` 3 hits, all as a hypothetical trial population in F9 `[X]` |
| 15 | **Vocational / physical / musical / athletic skill** | Partial | F7 (embodiment, manipulatives, VR, surgical sim), I1 (apprenticeship, Suzuki) | Load-bearing on *manipulatives*; procedural/psychomotor acquisition (massed vs distributed motor practice, contextual interference, feedback scheduling) is absent. `motor skill` 3 · `psychomotor` 1 · `welding` 0 `[X]` |
| 16 | **Second-language learning** | **No** | F6 (Duolingo as an *attrition* case), F11 (vocabulary SRS) | **The most conspicuous gap given the brief.** `second language` 2 hits / 1 file · `SLA` 3 hits (2 in F8, unrelated) · `comprehensible input` 2 · `vocabulary acquisition` 0 `[X]`. Duolingo appears 89 times and never once as evidence about language acquisition |
| 17 | Note-taking, summarising, learner question-generation | Partial | F7/A3 quotes one note-taking null; C3, F2 cover self-explanation and teaching | **Weak.** `note-taking` 2 hits total, both in passing · `student-generated question` 0 · `summarising`/`summarizing` 5 `[X]`. `self-explanation` (81 hits) is well covered and is not the same construct |
| 18 | Metacognition / SRL | Yes | N2, V5, F6, B1 | Load-bearing and good |
| 19 | **Curriculum sequencing and prerequisite structure as a design object** | **No** | F10 explicitly *disclaims* it ("a ladder is not a curriculum"); J1 owns technique selection, not topic order | **Absent by explicit hand-off, and nobody caught it.** `curriculum sequencing` 2 · `scope and sequence` 1 · `backward design` 0 · `knowledge graph` 3 `[X]` |
| 20 | **What happens after — multi-year retention, transfer to work** | Partial | B2 owns *the absence* (nobody measures retention); F11 owns remembering | **The critique exists; the positive treatment does not.** `transfer to work` 0 · `labor/labour market` 2 · `fade-out` 3 `[X]`. F4 touches earnings; no report asks what a learner still has in three years |
| 21 | Assessment machinery | Yes | C2, F1 | Excellent |
| 22 | Explanation craft | Yes | V1, V2, N4, F10, C3 | Excellent, arguably over-served (5 reports) |
| 23 | Memory / spacing / retrieval | Yes | F11, F5, B1 | Excellent |
| 24 | Attention & executive function | Yes | N2, V5 | Excellent |
| 25 | Special education & accessibility | Yes | H1, H2 | Excellent — the deepest practitioner coverage in the corpus |
| 26 | Safety, privacy, regulation | Yes | F8, E3 | Excellent |
| 27 | Economics, reach, market | Yes | F4, M1, E1-E2 | Excellent |
| 28 | Verification / grounding | Yes | F3, G1, C1 | Excellent |
| 29 | Motivation & persistence | Yes | F6, V3 | Good; frozen at 2020 evidence (§2.5) |
| 30 | Non-Western traditions | Yes | I2 | Good, with its own stated Anglophone-index bias |

### 1.1 The shape of the gap

The corpus is organised around **the artifact and its verification**. Nine reports concern
how an explanation or a figure or an item is produced and checked. Zero reports concern the
learner's affect toward the subject, the learner's relationship with the teacher, or the
learner's ordinary week (homework, revision, the exam). It covers **what a system emits** in
extraordinary depth and **what a learner is** thinly outside of knowledge state and executive
function.

Two structural consequences:

- **The corpus is one-learner-one-system throughout.** Groups appear only as (a) historical
  pedagogical systems in I1 and (b) simulated peers in F2/G2. `INFERENCE`: this is inherited
  from the product frame, not from evidence — I1's own mechanism-survival test scores
  "genuine peers with real stakes" as one of exactly three costs AI does *not* collapse, and
  nothing follows up on it.
- **Age range is narrow.** Effectively 9–18 plus undergraduates. `[X]` The two ends —
  pre-readers and adults — are absent, and each has a distinct evidence base.

---

# PART 2 — THE SKEW AUDIT

Five load-bearing negatives, checked against primary sources retrieved this session.

## 2.1 The felt/real divergence — **correctly scoped where it is Deslauriers; over-generalised where it is Buljan**

Two different sources carry this claim in the corpus and they have been merged.

**Deslauriers et al. (2019), PNAS `10.1073/pnas.1821936116` — correctly reported.**
`MEASURED-RCT`. `survey/01` says *"active learning raises real learning while lowering felt
learning."* The abstract, retrieved via Europe PMC this session, supports this exactly.
`B1` §goes further and correctly records the *remedy* the authors describe. One line of
scope the survey drops: the paper says students *"can, on their own, discover the increased
value of being actively engaged during a semester-long course"* — i.e. the divergence is
described by its authors as **strongest early and self-correcting over a course**. The
survey states it as a standing law. Minor; worth one clause.

**Buljan et al. (2018), *J. Clin. Epidemiol.* `10.1016/j.jclinepi.2017.12.003` —
over-generalised, and its label upgraded.** This is the source of the corpus's most-repeated
number, `d ≈ 0.48`.

- **What the source says** (Europe PMC, verbatim): three parallel RCTs comparing an
  **infographic** against a **plain-language summary** and a **scientific abstract** of a
  **Cochrane systematic review**, in **university students (n = 171), consumers (n = 99) and
  doctors (n = 64)**. *"We found no difference in knowledge… All three participant groups
  preferred the infographic and gave it higher ratings for reading experience (d = 0.48 in
  the overall sample) and user-friendliness (d = 0.46)."*
- **`F10` scopes it correctly** — it names the three trials, the n's, and the comparison.
- **Downstream it becomes a universal law about learners choosing.** `survey/22` §3:
  *"Stated preference for difficulty | **ANTI-SIGNAL** — preference moves d ≈ 0.48 while
  knowledge moves 0 (§01)"*. Buljan measured **preference for a document format among adults
  reading health information**, not **preference for difficulty**, not children, not a
  tutoring interaction, and not repeated exposure. `survey/25` §: *"Entry is measured, never
  chosen. Preference moves d ≈ 0.48 while knowledge…"*.
- **The label was upgraded in transit.** `N4` line 30: *"§01 establishes moves at **d ≈ 0.48
  while knowledge moves zero**. `MEASURED-META`"*. `J1` line 1171: *"**preference d ≈ 0.48,
  knowledge = 0** `MEASURED-META`"*, and J1's reference list line 1370 repeats
  `MEASURED-META (via F10)`. It is three RCTs totalling **n = 334**, not a meta-analysis. Two
  reports carry a `MEASURED-META` label on an `MEASURED-RCT` source. `[X]`
- **The cross-reference is also wrong.** Both `N4` and `survey/22` attribute it to `§01`.
  `survey/01-central-finding.md` does not contain Buljan or the 0.48 figure.

**Adjacent positive literature not searched.** The metacognitive-illusion literature has a
substantial *remediation* arm — delayed judgments of learning, cue-only JOLs, generation
prompts — that raises calibration. `B1` §cites Koriat & Bjork (2006) for exactly this, and
**no downstream section carries it**. The corpus's design rule ("measure, never ask") is
stated as though asking is uninformative in principle, when the source literature says
stated preference is *biased*, not *null*, and that the bias is partly correctable.

**Verdict: reported correctly at entry, over-generalised and mislabelled downstream.**

## 2.2 "Measurement without a decision rule is inert" — **correctly reported; the bounding literature was never searched**

**Source.** Fuchs, Hamlett & Stecker (1991), *School Psychology Review* / the companion
*AERJ* paper — CBM alone produced more frequent program revisions but no achievement gain;
CBM plus expert-system advice produced superior achievement. `MEASURED-RCT`. `H1` F5 states
this accurately and names it as the load-bearing architectural finding. `J1`, `H2`,
`survey/04` §4.1 and `survey/22` all carry it correctly. **No over-generalisation found.**

**What was never searched: the meta-analysis of the architecture the corpus then builds on.**

> **Filderman, Toste, Didion, Peng & Clemens (2018)**, *Journal of Special Education* —
> "Data-Based Decision Making in Reading Interventions: A Synthesis and Meta-Analysis of the
> Effects for Struggling Readers." 15 studies, K–12. DBDM vs business-as-usual:
> **g = .24, 95% CI [0.01, 0.46]**. The six-study subset comparing the *same* intervention
> with and without DBDM: **g = 0.27, 95% CI [0.07, 0.47]**. The authors conclude:
> *"experimental investigation is necessary to establish DBDM as an evidence-based practice
> for struggling readers."* `MEASURED-META`, ERIC, retrieved verbatim this session.

This is the pooled value of the whole two-clock, decision-rule architecture that `H1` §1.4,
`J1` §, `survey/04` and `N3` are built on. It is a small effect with a CI whose lower bound
is 0.01, from a literature its own authors decline to call evidence-based. The corpus cites
`Fuchs & Fuchs 1986, ES = 0.70` (H1 §564) — a 1986 estimate from a related but narrower
formative-evaluation corpus — and never the 2018 meta-analysis that supersedes the design
claim.

**This is the clearest instance of a search failure that is *not* negativity bias.** The
un-searched literature would have made the corpus's position *more* cautious, not less. The
bias here is toward *the source that supports the architecture being specified*, whichever
direction it points.

**Verdict: correctly scoped; the bounding meta-analysis is missing and would change the
number the architecture is sold on.**

## 2.3 Bastani's −17% — **correctly reported and correctly scoped; one phrasing drifts**

**Source** (Crossref abstract, retrieved verbatim this session):
`10.1073/pnas.2422633122`, PNAS. *"nearly a thousand high school math students"*; two arms,
**GPT Base** and **GPT Tutor**; *"48% improvement in grades for GPT Base and 127% for GPT
Tutor"* during access; *"when access is subsequently taken away, students actually perform
worse than those who never had access (**17% reduction in grades for GPT Base**)"*; *"These
negative learning effects are largely mitigated by the safeguards in GPT Tutor."*

- `survey/01` reports this with exemplary precision, including the point most people get
  wrong: the guardrailed arm's unassisted coefficient is **−0.004, n.s.** — *"harm removed,
  not benefit added"*. That is the correct reading and it is more conservative than the
  paper's own framing.
- The **PNAS Correction** (`10.1073/pnas.2518204122`) was independently verified in
  `evidence/bastani-2025-correction-check.md` and is an author-affiliation erratum. Verified
  again this session via Crossref `update-to`. The finding stands. This was handled well and
  the standing rule it produced ("a subagent's characterisation of a source is a *lead*, not
  a finding") is the single best process artifact in the repository.
- **One drift.** `N4` line 1865: *"unguarded assistance leaves learners **17% worse on later
  unassisted work**"* — drops the arm, the population (Turkish high-school mathematics), and
  the fact that the "later unassisted work" is a topic exam on the same four practice
  sessions. Everywhere else the scope is stated.

**Replications/contradictions since.** OpenAlex reports **109 citing works** (queried
2026-07-30, `cites:W4411627694`). Enumerating the 45 most recent: none is a direct
replication with a withdrawal design. The nearest are *"Stage-specific generative AI use and
dependency in learning"* (*Interactive Learning Environments*, 2026-06-29), *"Learner-Stage-Aware
AI Tutor Improves Learning Processes: Initial Evidence from a Field Experiment"* (LNCS,
2026-06-26), and *"How AI-Generated Feedback Hinders or Helps Learning"* (*JCAL*, 2026-06-24).
`OBSERVED — absence`: **the single most load-bearing causal claim in this corpus has not been
replicated in fourteen months, and the corpus does not say so.** That is a statement the
corpus should make about its own foundation and does not.

**Verdict: fairly reported. One phrasing to tighten, and one absence to declare.**

## 2.4 The 223-domain chance result — **the scope failure, and the un-searched positive literature**

This is the corpus's worst evidence-selection problem, and it is load-bearing in at least
six places (`K2` ×5, `N1`, `V2` ×3, `G3` ×2, `survey/32`).

**What the source says.** TutorGym, arXiv:2505.01563 (Weitekamp, Siddiqui & MacLellan),
abstract retrieved verbatim via the arXiv API this session: *"Currently, TutorGym includes
223 different tutor domains. **In an initial evaluation**, we find that current LLMs are poor
at tutoring — none did better than chance at labeling incorrect actions, and next-step
actions were correct only ~52–70% of the time."*

**What §3.1 of the paper says, retrieved from `arxiv.org/html/2505.01563v1` this session and
not quoted anywhere in the corpus:**

> *"As an initial demonstration of using TutorGym to evaluate AI agents as interactive tutors,
> we tested several different LLMs, including **Sonnet-3.5, Haiku-3.5, GPT-4o, and
> DeepSeek-v2.5**… The snapshots were: `claude-3-5-sonnet-20241022`,
> `claude-3-5-haiku-20241022`, `gpt-4o-2024-08-06`, and `deepseek-v2.5:236b`. These
> commercial models offered the best performance vs. cost tradeoff at the time of writing."*

**Census `[X]`:** the strings `sonnet-3.5`, `gpt-4o-2024`, `haiku-3.5`, `deepseek-v2.5` return
**zero hits across all 45 reports and 40 sections**. The model set is never named. What the
corpus says instead, in July 2026:

> `survey/32` §: *"The single most basic operation a tutor performs — look at what a learner
> did and say what is wrong with it — is **currently** unverifiable by the systems being sold
> to do it."*
>
> `K2` §: *"a step-level verifier for student work — the missing `pytest` of pedagogy;
> **currently at chance**."*
>
> `V2` §: *"**Every** architecture that asks a model 'is this student action wrong, and why'
> is building on a chance-level primitive."*

The word **"currently"** is doing work the evidence cannot support. The measurement is of
four non-reasoning model snapshots from **August–October 2024**, zero-shot, with no
fine-tuning and no tool use, in a paper that calls it an *initial demonstration*. The corpus
was written after `D1` catalogued GPT-5.5, Gemini 3.5 and Gemma 4. **A 2024 capability
measurement is generalised to a 2026 capability claim, and the vintage is never disclosed to
the reader.**

**Adjacent positive literature, not searched.** Two bodies of work measure very close
constructs, well above chance, and appear nowhere:

1. **Step-level error identification in reasoning traces.** *ProcessBench: Identifying Process
   Errors in Mathematical Reasoning*, arXiv:2412.06559 (Qwen team, 9 Dec 2024) —
   3,400 human-annotated test cases; models must *"identify the earliest step that contains an
   error, or conclude that all steps are correct."* `MEASURED-BENCH`. Its headline comparison
   is directly damaging to the corpus's framing: prompted critic models **beat** trained PRMs,
   and *"the best open-source model, QwQ-32B-Preview, has demonstrated the critique capability
   competitive with the proprietary model GPT-4o, despite that it still lags behind the
   **reasoning-specialized o1-mini**."* That is the same GPT-4o vintage TutorGym tested,
   beaten by reasoning models on the same operation. Corpus census `[X]`: `ProcessBench` **0
   files**, `Math-Shepherd` **0 files**, `process reward` **1 file** — a single clause in `K2`
   §657 listing "Lightman's process reward models" among best-of-n techniques, never connected
   to the pedagogy claim.
2. **Mistake identification in tutor–student dialogue.** The **BEA 2025 Shared Task on
   Pedagogical Ability Assessment of AI-powered Tutors** (arXiv:2507.10579), *"over 50
   international teams"*, evaluated against gold human annotations: best **macro-F1 71.81 on
   Mistake Identification** (3-class), 58.34 on providing guidance. Built on **MRBench**
   (arXiv:2412.09416), 192 conversations / 1,596 responses / 8 pedagogical dimensions, with
   gold labels. Corpus census `[X]`: `MRBench` 1 file, `BEA 20` 1 file, `shared task` 2 files —
   none in a load-bearing position; `Prometheus` 0.

**The honest qualification, stated so this audit is not itself skewed:** ProcessBench and the
BEA task are **adjacent, not identical**. TutorGym asks a model to label a *student's* action
inside a live ITS interface across 223 curricular domains; ProcessBench asks it to find the
first bad step in a *model's own* mathematical chain; BEA asks whether a *tutor response*
correctly identified a student's error. They are three different tasks. But they are the three
closest measurements that exist, two of them are strongly positive, and a corpus that
concludes *"pedagogy has no `pytest`"* had an obligation to name and distinguish them. It does
not mention them.

**Verdict: over-generalised on two axes — model vintage silently generalised to "currently",
and one benchmark's initial evaluation generalised to "every architecture". The
positive adjacent literature was never searched.**

## 2.5 Gamification's weak behavioural cell — **correctly reported, correctly scoped, evidence frozen at 2020**

**Source** (ERIC, verbatim this session): Sailer & Homner (2020), *EPR*
`10.1007/s10648-019-09498-w` — cognitive **g = 0.49 [0.30, 0.69], k = 19**; motivational
**g = 0.36 [0.18, 0.54], k = 16**; behavioural **g = 0.25 [0.04, 0.46], k = 9**. *"the effect
of gamification on cognitive learning outcomes was stable in a subsplit analysis of studies
employing high methodological rigor, effects on motivational and behavioral outcomes were less
stable."* Significant moderators: game fiction, social interaction, competition-plus-collaboration.

`V3` §0 reproduces every number, leads with the *positive* cognitive cell, correctly names
the behavioural cell as the weak and unstable one, and correctly notes that **nothing in the
moderator analysis supports points, badges or leaderboards**. This is the corpus at its best
and it is fairly weighted. **No over-generalisation found.**

**The problem is the freeze.** `V3` opens: *"`F6-motivation-persistence.md` is taken as
settled and is not re-litigated."* The census confirms what that produced: `[X]` **the corpus
cites no gamification meta-analysis published after 2020**, and there are at least ten
2023–2026 candidates in Crossref. One is directly contradictory in magnitude:

> **"Exploring the Efficacy of Game-Based Pedagogy: A Three-Level Meta-Analysis of Game-Based
> Learning and Gamification"**, *Active Learning in Higher Education*, 2026,
> `10.1177/14697874261424519`. **1,029 effect sizes from 193 randomized or quasi-randomized
> trials**, three-level model. **Game-based learning d = 0.871; gamification d = 0.754**, with
> significant moderation by learning domain, stage and duration. `MEASURED-META`, Crossref
> abstract retrieved verbatim.

`INFERENCE`: d = 0.754 versus g = 0.25 is not a small disagreement, and the likely reconciliation
is exactly the one this corpus is expert at — outcome-measure alignment, publication venue,
quasi-randomised inclusion, higher-ed samples. **That reconciliation is the corpus's specialty
and it was never performed, because the negative finding had been marked settled.**

**Verdict: fairly reported; evidence frozen at 2020; a 193-trial 2026 meta-analysis reporting
a 3× larger effect is uncited.**

## 2.6 The pattern

| Finding | Reported accurately? | Scoped correctly? | Adjacent positive searched? | Post-publication check? |
|---|---|---|---|---|
| Deslauriers felt/real | Yes | Yes (drops "initially") | Partly — remedy in B1, lost downstream | n/a |
| Buljan d = 0.48 | Yes in F10 | **No downstream** — and label upgraded to `MEASURED-META` | No | No |
| Fuchs decision rule | Yes | Yes | **No** — 2018 DBDM meta missing | No |
| Bastani −17% | Yes | Yes (one drift in N4) | Yes (Kestin, guardrailed arm) | **Yes** — correction verified; but non-replication not declared |
| TutorGym 223 domains | Yes | **No** — vintage and "initial evaluation" both dropped | **No** — ProcessBench/PRM, BEA 2025, MRBench all absent | No |
| Sailer & Homner g = .25 | Yes | Yes | Partly | **No** — frozen at 2020 |

**The skew is real and it has a precise shape.** It is not that nulls were invented or
inflated. It is that:

1. **Negatives are entered once and then frozen**; positives are re-audited every session.
   `V3`'s *"taken as settled and is not re-litigated"* is the mechanism, stated in the corpus's
   own words. `ASSUMPTIONS.md` A4 diagnosed the review loop; nobody noticed the same asymmetry
   inside the *citation* loop.
2. **Scope decays downstream.** Every mis-scoping found is a *transfer* error: correct in the
   raw report, universal by the survey. Twice the evidence label was upgraded in transit
   (`MEASURED-RCT` → `MEASURED-META`), always in the direction of making the negative sturdier.
3. **The un-searched adjacent literature is un-searched in both directions.** The missing DBDM
   meta-analysis (§2.2) would have made the corpus *more* negative. So the bias is better
   described as *"whatever supports the design being specified goes in, and nothing is
   re-checked afterwards"* than as *"negatives preferred."* That is a subtler and more
   correctable failure than the one `ASSUMPTIONS.md` A5 confesses to.

---

# PART 3 — WHAT TO COMMISSION

Ranked by (harm to a real child if missing) × (evidence base actually exists).

### 1. The relationship, and what a tutor does that is not instruction

**Missing.** Any treatment of the affective teacher–student relationship, trust, credibility,
the alliance, and the tutor who believes in you. `[X]` Zero hits on every technical term for it.

**Why it matters to a system that tutors a real child.** A tutor that is right and cold loses
the child in week three, and this corpus has no vocabulary for that failure. `V5`'s entire
premise — supply the executive the learner lacks — is a *relational* act (someone holding the
plan for you) specified purely as a control loop. `H1`'s Direct Instruction base and `N2`'s
attention findings both assume a learner who shows up.

**What a report would have to establish.** (a) The measured association and its causal
status — Roorda, Koomen, Spilt & Oort (2011), *RER*, 99 studies / 88,417 students, and the
2017 update, 189 studies / 249,198 students, testing engagement as mediator; Cornelius-White
(2007), *RER*, 119 studies / 1,450 findings on learner-centred relationships. (b) The hard
question: how much of it survives when the other party is not a person — the corpus already
owns the right test (I1's *"if I remove the other human, is the thing the learner does still
the thing that caused the effect?"*) and has never applied it here. (c) The parasocial risk
register, which `F8` will constrain hard. (d) What the tutor's *first* obligation is when the
child is wrong and knows it.

**Does the evidence base exist?** **Yes, and it is large and meta-analytic.** Three RER-tier
meta-analyses confirmed in ERIC this session. The AI half is thin, which is the finding.

### 2. Second-language learning as the corpus's missing RCT density

**Missing.** `[X]` No report owns it. Duolingo appears 89 times, never as evidence about
acquisition.

**Why it matters.** L2 is where the field's best-powered intervention trials live, where
spaced retrieval was validated at industrial scale, and where "corrective feedback" — the
exact operation TutorGym says LLMs cannot do — has thirty years of meta-analysed RCTs with
real effect sizes. It is also the highest-volume commercial tutoring category on earth. `B2`'s
complaint that nobody measures retention is *false* for SLA, which measures delayed post-tests
as a discipline norm.

**What a report would have to establish.** Corrective-feedback effect sizes and their
moderators — *"The Effectiveness of Corrective Feedback in SLA: A Meta-Analysis"*,
*Language Learning* 2010, 33 primary studies; *"The Efficacy of Written Corrective Feedback
in Improving L2 Written Accuracy"*, *MLJ* 2015, 21 studies; the 2020 *TESL-EJ* written-CF
meta, 35 studies (all three located in ERIC this session, authors not resolved in-session
and to be confirmed before citation); comprehensible input vs. explicit instruction; whether delayed
post-test discipline transfers to the rest of the corpus; and whether Duolingo's published
half-life-regression work is evidence or vendor material under this corpus's own rule.

**Does the evidence base exist?** **Yes, and it is the densest in the corpus's reach.**
Four meta-analyses located in ERIC in a single query this session.

### 3. Reading and writing as skills, for the ordinary learner

**Missing.** Reading is covered only inside `H1` (special education). Writing instruction is
absent entirely; `F1` treats the essay as an instrument to be *replaced*.

**Why it matters.** Decoding and comprehension are the substrate every other subject runs on,
and a tutor for a nine-year-old that cannot tell a decoding failure from a comprehension
failure from a knowledge gap will mis-route every intervention. The corpus's own `J1`
selection policy has no branch for this.

**What a report would have to establish.** The simple view of reading and where it breaks;
the phonics dispute at the level `H1` already reached (Bowers 2020 vs the NRP consensus) but
for typical readers; fluency as a distinct target; why comprehension "strategies" have
weak transfer; and for writing, the genuinely strong finding the corpus is missing — that
*writing about content* is one of the better-evidenced content-learning interventions.

**Does the evidence base exist?** Yes, abundantly.

### 4. The affective layer that is not motivation — anxiety, self-concept, threat

**Missing.** `[X]` `math anxiety` 2 hits, `test anxiety` 0, `stereotype threat` 0,
`self-concept` 3.

**Why it matters.** `F6` owns *why learners quit* at the volitional level. It does not own
*why a specific child freezes on fractions*. These are different mechanisms with different
interventions, and the second is the one a tutoring system encounters hourly.

**What a report would have to establish.** The correlation and its size (Barroso et al.;
the 2022 *EPR* meta on 906,311 participants located in ERIC this session); which interventions
move it (the 2023 *J. Numerical Cognition* meta, 50 studies / 75 effect sizes); and — with
this corpus's characteristic honesty — the **replication status of stereotype threat**, which
is genuinely contested (Picho-Kiroga 2021 d = .28 vs the 2022 *JAA* reassessment finding
"no strong evidence" after correcting for inflating design features). That last item is a
case where the corpus's skepticism is *warranted* and would be a contribution.

**Does the evidence base exist?** Yes, including the contested parts.

### 5. Groups — the fact that learning happens near other people

**Missing.** `[X]` `collaborative learning` 7 hits; CSCL absent; no report owns it.

**Why it matters.** `I1` already scored "genuine peers with real stakes" as one of three costs
AI cannot collapse. That is a load-bearing negative the corpus states and never investigates.
If it is right, it bounds the entire single-tutor product thesis; if it is wrong, `G2`'s agent
village has a mechanism.

**What a report would have to establish.** Cooperative-learning effect sizes and the
conditions (positive interdependence, individual accountability) that carry them; the CSCL
meta-analyses; whether a simulated peer reproduces any of it — and here `F2`'s protégé-effect
material is the bridge that already exists.

**Does the evidence base exist?** Yes; several meta-analyses located this session.

### 6. Homework, revision, and the exam — what learners actually spend time on

**Missing.** `[X]` `exam technique` 0, `study skills` 0, `past paper` 0.

**Why it matters.** `K1` computes that most of a learning week is overhead, and then does not
ask what the learner is doing during the largest identifiable block of it. A system that
tutors a real child competes with, and should probably absorb, homework and revision.

**What a report would have to establish.** The homework–achievement effect and its strong age
moderation; parental homework involvement (a three-level meta exists, located this session);
what test preparation actually buys and on which construct; and the corpus's own `F11`
material re-aimed at the thing learners do the night before.

**Does the evidence base exist?** Yes, though noisier than the above.

### 7. Curriculum sequencing and the prerequisite graph as a design object

**Missing by explicit hand-off.** `F10` disclaims it; `J1` selects techniques, not topics.

**Why it matters.** Every generated curriculum in `A1` and every adaptive path in `J1`
presupposes an ordering, and no report specifies where the ordering comes from or how it is
validated. This is the largest **unowned** item rather than the largest absent one.

**What a report would have to establish.** Whether prerequisite structure is empirically
recoverable from response data (learning-curve analysis, Q-matrix refinement — `C2` and `F5`
have the machinery); what learning-progression research supports; and the falsifier — does
respecting a prerequisite graph beat a flat ordering on delayed transfer.

**Does the evidence base exist?** Partly. This is closer to `SPEC` than `MEASURED`, which
suits the corpus's post-`ASSUMPTIONS.md` direction.

### 8. Very young children, and adults returning to study

**Missing.** `[X]` Both ends of the age range.

**Why it matters.** "No child, no teen, no adult left behind" is quoted in `F4` as the
project's own goal. The corpus covers roughly ages 9–22.

**What a report would have to establish.** For pre-readers: what is even measurable, why
screen-based instruction has a poor record under 5, and the shared-reading evidence. For
adults: self-directed goal structures, prior-knowledge asymmetry (which `J1`'s expertise-reversal
law predicts is *larger*, not smaller), and the labour-market outcome question.

**Does the evidence base exist?** Yes for early childhood; thinner and more fragmented for
adults.

### 9. Procedural and physical skill

**Missing.** `F7` covers manipulatives; nothing covers motor-skill acquisition.

**Why it matters.** The corpus's compression claim (`K1`) is derived entirely from cognitive
encoding. Motor and procedural skill obey different laws — contextual interference, feedback
scheduling, massed vs distributed practice with *opposite* signs in places — and any claim
about "learning" that excludes them should say so.

**Does the evidence base exist?** Yes, and it is old and well-replicated.

### 10. Three corrections to file, not reports to commission

Cheap, and each removes a defect found above.

- **Fix the Buljan label and scope.** `MEASURED-META` → `MEASURED-RCT` in `N4` §0 and `J1`
  (two places); fix the `§01` cross-reference in `N4` and `survey/22`; and restate the design
  rule as *"stated preference is a biased signal on format, measured on adults reading health
  information"* rather than a universal law about learners choosing difficulty.
- **Date the TutorGym claim.** Every occurrence of "currently at chance" should read
  *"measured at chance on four non-reasoning model snapshots from August–October 2024, in what
  the authors call an initial evaluation,"* and should name ProcessBench and BEA 2025 as the
  adjacent measurements that point the other way. This affects `survey/32` — which is *titled*
  after the claim — plus `K2`, `V2`, `N1`, `G3`.
- **Declare the Bastani non-replication.** 109 citing works, no replication with a withdrawal
  design in fourteen months. The corpus's most load-bearing causal result rests on one trial in
  one country, and the corpus should say that in the same breath as the number.

---

## Appendix — reproducing the census

Every `[X]` figure above is a term census over `research/raw/` + `survey/`:

```
grep -rowi "<term>" research/raw survey | wc -l      # hits
grep -rlowi "<term>" research/raw survey | wc -l     # files
```

Word-boundary matching (`-w`) is required: an unbounded `SLA` matches `tran(sla)te`
(194 false hits) and an unbounded `sport` matches `tran(sport)`. Both were corrected before
the figures above were taken. Term censuses miss synonyms and inline-table mentions; every
"absent" row was re-checked with at least four synonyms before being marked. `OBSERVED — absence`
means *not found by the stated query*, never *does not exist*.

**Primary sources retrieved this session (24):** Bastani et al. PNAS `10.1073/pnas.2422633122`
+ correction `10.1073/pnas.2518204122` (Crossref) · TutorGym arXiv:2505.01563 abstract (arXiv
API) and §3.1 method (`arxiv.org/html/`) · ProcessBench arXiv:2412.06559 (arXiv API) ·
BEA 2025 findings arXiv:2507.10579 · MRBench arXiv:2412.09416 · GRADE arXiv:2605.27866 ·
NeuralNexus arXiv:2506.10627 · Team BD arXiv:2506.01817 · Buljan et al.
`10.1016/j.jclinepi.2017.12.003` (Europe PMC, verbatim) · Deslauriers et al.
`10.1073/pnas.1821936116` (Europe PMC, verbatim) · Sailer & Homner `10.1007/s10648-019-09498-w`
(ERIC, verbatim) · three-level GBP meta `10.1177/14697874261424519` (Crossref, verbatim) ·
Filderman et al. 2018 DBDM meta (ERIC, verbatim) · Roorda et al. 2011 and 2017 (ERIC) ·
Cornelius-White 2007 (ERIC) · 2022 *EPR* anxiety meta and 2023 *JNC* intervention meta (ERIC) ·
Picho-Kiroga reassessment, *JAA* 2022 (ERIC) · three corrective-feedback meta-analyses,
*Language Learning* 2010 / *MLJ* 2015 / *TESL-EJ* 2020 (ERIC, titles and study counts only) ·
cooperative-learning and CSCL metas, *JREE* 2013 / *IJEMST* 2021 (ERIC) · note-taking metas,
*JREE* 2016 / *SSLA* 2024 (ERIC) · homework metas, *IEJ* 2017 / AERA 2024 three-level
parental-involvement (ERIC) · Bastani citing-works enumeration, OpenAlex
`cites:W4411627694`, 109 works (2026-07-30).

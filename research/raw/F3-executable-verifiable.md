---
title: "Executable, Verifiable Knowledge — Making Generated Explanations Grounded Rather Than Merely Plausible"
wave: F
date_researched: 2026-07-27
sources_count: 76
---

# F3 · Executable, Verifiable Knowledge

> **Deliverable of this section:** a **grounding ladder** — five tiers of verification, each
> with measured cost, measured coverage, and a decision rule that maps a claim type to the
> tier it requires. Sections 1–7 are the evidence base; §8 is the ladder; §9 is the register
> of negative results; §10 is the handoff to G1.

---

## 0. The problem, stated precisely

A derivation is a sequence of claims. At the prose level, a *wrong* derivation and a *right*
derivation are drawn from nearly the same distribution: same connective vocabulary
("therefore", "substituting", "by symmetry"), same rhetorical shape, same confidence. The
generator that produces one produces the other with indistinguishable fluency. Fluency is not
evidence. **A learner cannot tell the difference, and neither can a fluency-trained grader.**

This is not a hypothetical failure mode. It is measurable in three independent places:

1. **End-to-end formal pipelines lose ~60 points of accuracy** relative to the components'
   individually reported numbers, and the loss traces to *statements that look right and are
   not* (§1.4).
2. **The single best-documented "executable knowledge" artefact in the world — the published
   Jupyter notebook — reproduces its own stated results 4.03% of the time** (§3.1).
3. **Citation-bearing generation gets the citation formatting right >94% of the time and the
   underlying fact right 39–77% of the time** (§6.2).

The gap between "looks grounded" and "is grounded" is the subject of this section. The
engineering response is not better prose. It is to route each claim to a *checker that can
say no*.

**The organising distinction.** Every mechanism below converts a claim into an artefact that
an adversarial, non-linguistic process can reject:

| Mechanism | Rejecting process | What "no" means |
|---|---|---|
| Formal proof | Lean/Isabelle/Coq kernel | The inference does not follow |
| Computer algebra | CAS normal form / zero test | The expressions are not equal |
| Execution | Interpreter, exit code, assertion | The code does not do what was claimed |
| Simulation | Numerical solver vs analytic form | The closed form does not match the dynamics |
| Dimensional analysis | Unit algebra | The equation is not even type-correct |
| Retrieval | Source text | The cited document does not say that |

Everything a learner values that is *not* on this list — intuition, analogy quality,
pedagogical sequencing, "why this matters" — is unverifiable by construction, and §7 draws
that boundary explicitly rather than pretending it away.

---

## 1. Formal verification: Lean 4 + mathlib, Isabelle, Coq

### 1.1 The infrastructure, sized

| Library | Scale | Date / source | Label |
|---|---|---|---|
| **mathlib4** (Lean 4) | **134,736 definitions + 283,310 theorems**, 772 contributors | leanprover-community.github.io/mathlib_stats.html | MEASURED-BENCH |
| mathlib4 (network study) | 308,129 declarations, 8.4M dependency edges, 7,563 modules | arXiv:2604.24797 (Apr 2026) | MEASURED-BENCH |
| mathlib4 repo | Apache-2.0, ~468 MB checkout, 828+ contributor pages, active daily (pushed 2026-07-27) | GitHub API, `leanprover-community/mathlib4` | OBSERVED |
| **Archive of Formal Proofs** (Isabelle) | **1,012 entries, 604 authors, ~5,342,200 LoC, ~323,000 lemmas** | isa-afp.org/statistics | MEASURED-BENCH |
| Lean CSLib (computer science) | New library, spun up 2026 | arXiv:2602.04846, arXiv:2602.15078 | OBSERVED |

Two structural facts from the network analysis (arXiv:2604.24797) matter for anyone planning
to *use* mathlib as a grounding substrate rather than admire it:

- **Human taxonomy diverges from logical structure: 50.9% coupling across namespaces.** The
  file you would guess a lemma lives in is the wrong file about half the time.
- **Developers use a median of 1.6% of the imported scope.** Import graphs are enormously
  over-broad; retrieval over mathlib is a genuine needle-in-haystack problem, which is
  precisely why LeanDojo's premise-selection contribution (arXiv:2306.15626) was the
  unlock it was.

`MEASURED-BENCH` · Maintenance is itself a research problem: mathlib's maintainers document
deprecation systems, linters, compile-time-driven library redesign, and custom triage tooling
purely to keep growth from collapsing under its own weight (arXiv:2508.21593).

### 1.2 The benchmark ladder, and where each rung actually sits

| Benchmark | What it is | Size | Source |
|---|---|---|---|
| **miniF2F** | Olympiad/competition, high-school level, cross-system (Lean, Isabelle, HOL, Metamath) | 488 problems (244 valid / 244 test) | arXiv:2109.00110 |
| **ProofNet** | **Undergraduate** pure maths from standard textbooks: real & complex analysis, linear algebra, abstract algebra, topology | 371 examples (NL statement + NL proof + formal statement) | arXiv:2302.12433 |
| **PutnamBench** | Putnam competition — undergraduate but *hard* | 1,692 formalizations of 640 theorems; Lean 4 + Isabelle, subset in Coq | arXiv:2407.11214 |
| **TaoBench** | Undergraduate analysis built from Tao's *Analysis I* **from scratch, not on mathlib definitions** | paired Tao / mathlib formulations | arXiv:2603.12744 |
| **LeanPhysBench** | **College physics** in Lean 4 + `PhysLib` unit/theorem repo | 200 hand-written, peer-reviewed statements | arXiv:2510.26094 |
| **FATE-H / FATE-X** | Graduate / PhD-level formal maths | — | via Seed-Prover 1.5, arXiv:2512.17260 |
| miniF2F-v2 | miniF2F with **all** formal/informal discrepancies corrected | 488 | arXiv:2511.03108 |

### 1.3 State of the art, July 2026 — and the Leanstral claim, verified

The brief asked us to verify a specific claim: *"Leanstral 1.5 saturates miniF2F at 100%,
Apache-2.0, July 2026."* Result: **the claim is real, is a vendor claim, and is not
independently reproduced.**

**What is verifiable:**

- `mistralai/Leanstral-1.5-119B-A6B` exists on Hugging Face, **Apache-2.0**, created
  **2026-07-01**, 119B MoE with **6.5B active params** (128 experts, 4 active), 256k context,
  multimodal input, built on `mistralai/Leanstral-2603`.
  (huggingface.co/mistralai/Leanstral-1.5-119B-A6B) `OBSERVED`
- The **model card contains no benchmark numbers at all** — only a benchmark comparison
  *image*. Every quantitative claim lives in the launch blog. `OBSERVED`
- The launch post (mistral.ai/news/leanstral-1-5, dated **2026-07-02**) reports:
  **miniF2F 100% (saturated, validation *and* test)**; **PutnamBench 587/672**; FATE-H 87%;
  FATE-X 34%; FLTEval pass@1 28.9%, pass@8 43.2%; and "5 previously unknown bugs" found
  across 57 tested repositories. `VENDOR`
- The same post reports the **test-time-scaling curve that is the real story**:
  PutnamBench pass@8 solves **44 problems at 50k tokens → 244 at 200k → 493 at 1M → 587 at
  4M tokens.** `VENDOR`

**What the independent evidence says.** The only independent evaluation located is
`MiaAI-Lab/Leanstral-1.5-119B-A6B_Review` (GitHub, July 2026), a 20-test two-tier local vLLM
evaluation at temperature 0.2. Its findings:

- 10/10 and 10/10 API success; mean latency 7.2 s (Tier 1) and 32 s (Tier 2), with one
  Fibonacci identity taking **194 s / ~3,900 tokens**.
- **"Scoring: API response quality + extracted Lean code (not compiler-verified)."**
- **"Not compiler-verified — estimated compile rate ~75–85%, not measured."**
- Grades: proof copilot **A**, agentic proof repair **A+**, autoformalization **A−**,
  **autonomous expert prover C+**.
- Verdict: *"It is not a hands-off expert prover — always verify output with `lake build`."*

`OBSERVED` · **Editorial ruling for the survey: report Leanstral's miniF2F 100% as a
`VENDOR` claim, never as a finding.** The independent reviewer did not compile a single proof.
Note also that the number is not implausible on its face — it is the endpoint of a trend, not
an outlier:

| System | miniF2F | PutnamBench | Date | Source |
|---|---|---|---|---|
| DeepSeek-Prover-V2-671B | 88.9% pass ratio | 49/658 | 2025-04 | arXiv:2504.21801 |
| Goedel-Prover-V2-8B | 84.6% pass@32 | — | 2025-08 | arXiv:2508.03613 |
| Goedel-Prover-V2-32B | 88.1% pass@32; **90.4% self-correction** | 86 @ pass@184 | 2025-08 | arXiv:2508.03613 |
| Seed-Prover | "saturates miniF2F"; 78.1% formalized past IMO | >50% | 2025-07 | arXiv:2507.23726 |
| Seed-Prover 1.5 | — | **88%**; FATE-H 80%, FATE-X 33% | 2025-12 | arXiv:2512.17260 |
| **Leanstral 1.5** | **100% (claimed)** | **587/672 = 87.4%** | 2026-07 | VENDOR |
| Gemini 3.1 Pro | 92% refine@32 (miniF2F subset) | — | 2026-06 | arXiv:2606.05632 |
| Claude Opus 4.7 | — (86% miniCTX refine@32) | — | 2026-06 | arXiv:2606.05632 |

**miniF2F is a saturated benchmark and should be retired from any 2026 argument about
capability.** Cite it only as a historical marker.

### 1.4 The negative result that matters most: the autoformalization gap

`MEASURED-BENCH` · **arXiv:2511.03108, "miniF2F-Lean Revisited" (Nov 2025).** The authors
evaluated the *whole* pipeline an actual learner needs — read an informal problem, formalize
it, prove it, and get credit only if the formal proof corresponds to the original informal
statement:

> **"The best accuracy of such pipeline can be about 36% using the SoTA models in the
> literature, considerably lower than the individual SoTA accuracies, 97% and 69% reported in
> the autoformalization and theorem proving literature."**

And the diagnosis:

> **"We trace back a considerable portion of this drop to discrepancies between the formal and
> informal statements for more than half of the problems in miniF2F."**

After correcting every error and simplification → **miniF2F-v2**, on which the end-to-end
pipeline reaches **70% (vs 40% on original miniF2F)** — an improvement that is *entirely a
benchmark-quality artefact*, and still leaves 30% failing.

**This is the single most important number in F3.** It says: *the kernel does not verify the
thing you care about.* It verifies that a formal statement follows from formal axioms. Whether
that formal statement *means* what the prose said is an unverified natural-language judgement
sitting upstream of the entire apparatus. **Formal verification moves the trust boundary; it
does not eliminate it.**

Three corroborating measurements:

- `MEASURED-BENCH` **Kernel acceptance overstates quality.** arXiv:2606.14000 built a
  three-dimensional audit (semantic correctness, mathlib reuse, cross-file reuse) over
  agent-formalized numerical analysis and over RepoProver's and M2F's released outputs. It
  found *"recurring unfaithful formalization patterns, including **incomplete multi-part
  statements, added weakening hypotheses, and parameter restrictions**, that kernel acceptance
  entirely obscures,"* concluding that *"compilation-based metrics substantially overstate
  formalization quality."*
- `MEASURED-BENCH` **Autoformalization is not robust to paraphrase.** arXiv:2511.12784
  paraphrased miniF2F and ProofNet statements while preserving semantics and found
  *"performance variability across paraphrased inputs, demonstrating that minor shifts in NL
  statements can significantly impact model outputs."* A learner who rephrases the question
  gets a different formalization.
- `MEASURED-BENCH` **Evaluating autoformalization is itself unsolved.** GTED
  (arXiv:2507.07399) exists because prior metrics *"lack semantic understanding, face
  challenges with high computational costs, and are constrained by the current progress of
  automated theorem proving."*

### 1.5 What fraction of ordinary textbook mathematics is formalizable today, and at what cost?

This is the brief's central question. The honest answer is a stratified one.

**Coverage, by stratum:**

| Stratum | Formalizable today (statement + proof, automated) | Evidence |
|---|---|---|
| Competition algebra / number theory (high-school) | **~90–100%** | miniF2F saturated (§1.3) |
| Undergraduate pure maths, *expressed in mathlib's definitions* | **~60–88%** | PutnamBench 88% (Seed-Prover 1.5); ProofNet |
| The **same** undergraduate maths in **non-mathlib definitions** | **−26 percentage points** | TaoBench, arXiv:2603.12744 |
| Graduate (FATE-H) | ~80–87% | arXiv:2512.17260; Leanstral VENDOR |
| PhD-level (FATE-X) | **~33–34%** | arXiv:2512.17260; Leanstral VENDOR |
| **College physics** | **16% (best expert Lean prover) – 35% (Claude Sonnet 4)** | LeanPhysBench, arXiv:2510.26094 |
| Numerical analysis / applied maths | *Library largely absent from mathlib* | arXiv:2606.14000 |
| **End-to-end from informal prose (the learner's actual task)** | **36% (original miniF2F) / 70% (cleaned)** | arXiv:2511.03108 |

`MEASURED-BENCH` · The TaoBench result deserves emphasis because it directly governs
pedagogy. Tao's *Analysis I* constructs the reals from scratch — exactly what a first analysis
course does. Provers drop **~26%** on definitionally-equivalent statements when the
definitions are the textbook's rather than mathlib's. **The system is good at mathematics as
mathlib has organised it, not at mathematics as your course has organised it.** For a tutor
that must follow *a specific textbook*, this is the binding constraint.

**Cost, four independent anchors:**

| Anchor | Cost | Source | Label |
|---|---|---|---|
| Cheapest measured per correct proof (miniF2F/miniCTX subsets, NVIDIA Nemotron 3 Super, GPT-OSS 120B) | **< $0.01 per correct proof** | arXiv:2606.05632 | MEASURED-BENCH |
| Leanstral 1.5 to reach 587/672 PutnamBench | **4,000,000 tokens per problem at pass@8** | mistral.ai/news/leanstral-1-5 | VENDOR |
| AlphaProof at IMO 2024 | *"up to three days"* per problem; problems **manually translated into Lean first** | deepmind.google blog | VENDOR |
| Seed-Prover 1.5 on Putnam 2025 | **11 of 12 problems in 9 hours** | arXiv:2512.17260 | VENDOR |
| Flyspeck (Kepler conjecture) | Started Jan 2003, completed **10 Aug 2014** — ~11 years, Hales's own estimate was 20; HOL Light + Isabelle | Wikipedia/Kepler conjecture | OBSERVED |

`MEASURED-BENCH` · Cost is now optimisable as an explicit objective: an action-routing agent
that predicts P(success) and cost-of-another-attempt from failed Lean trajectories cuts spend
**28.9%** on a PutnamBench subset with no performance loss (arXiv:2606.04883).

**The cost picture in one sentence.** For *routine* textbook mathematics that mathlib already
covers, formal verification now costs **sub-cent per claim** and is affordable at classroom
scale; for anything off the mathlib manifold it costs **megatokens to person-years** and is
affordable only for claims that will be reused thousands of times. This asymmetry is the
entire justification for a *ladder* rather than a *standard*.

### 1.6 Two further boundaries worth naming

- `MEASURED-BENCH` **Provers may be pattern-matching pre-training, not reasoning.** The
  Obfuscated Natural Number Game (arXiv:2605.00677) renames every identifier in Lean 4's
  Natural Number Game to create a zero-knowledge closed environment and tests "Architectural
  Reasoning" — proof synthesis from *only* local axioms. The framing is explicit: it is
  *"unclear whether these results stem from genuine logical reasoning or semantic pattern
  matching against pre-training data."*
- `MEASURED-BENCH` **Mode collapse under RL.** arXiv:2601.16172: with DeepSeek-Prover-V1.5-RL
  on miniF2F-test, **doubling the sampling budget from k=32 to k=64 produces zero additional
  solved theorems (42/244 in both cases)**. A fixed schedule of 15 tactic skeletons recovers
  **+45% relative at k=16**; paraphrase-based diversity matches baseline; irrelevant Lean
  comments actively degrade. Related: GRPO exhibits a *"degenerate rank bias"* that merely
  sharpens the base distribution (arXiv:2506.02355). **More compute at the same temperature
  buys nothing; structural diversity buys a lot.**
- `MEASURED-BENCH` **Compositional inequality reasoning fails.** Ineq-Comp
  (arXiv:2505.12680) builds compositions of elementary inequalities (variable duplication,
  algebraic rewriting) and shows provers do not recognise that a problem reduces to a known
  inequality such as AM/GM when it must be applied compositionally — *"beyond syntactic
  correctness, do these systems truly understand mathematical structure as humans do?"*
  This is exactly the skill a teacher is trying to instil.

---

## 2. Computer algebra as grounding

### 2.1 The Wester benchmark, and an original measurement

`OBSERVED` · Michael Wester's *"A Critique of the Mathematical Abilities of CA Systems"*
(1999, ~40 pp.) is the standard CAS correctness suite. It compares **seven systems** — Axiom,
Derive, Macsyma, Maple, Mathematica, MuPAD, Reduce — across **29 mathematical domains**, from
Boolean logic through PDEs. Source: math.unm.edu/~wester/cas_review.html and
math.unm.edu/~wester/cas/book/Wester.pdf. The per-problem results tables published on that
site are the reference point the CAS community still uses.

**Original measurement (this survey).** SymPy carries Wester's problems as a live test file,
`sympy/utilities/tests/test_wester.py`, whose docstring reads *"Tests from Michael Wester's
1999 paper 'Review of CAS mathematical capabilities'."* We pulled SymPy `master`
(2026-07-27) and counted.

`MEASURED-BENCH` — **SymPy vs the Wester suite, 2026-07-27** (3,108 lines, 397 test functions):

- **397** Wester problems implemented as tests
- **150** decorated `@XFAIL` (known-failing) + **3** `@SKIP` (2 open bugs, 1 hang)
- **⇒ 152 / 397 = 38.3% of the implemented Wester suite still fails in the world's most-used
  open-source CAS, 27 years after the benchmark was published.**
- Additionally **three entire Wester sections are unimplemented**: **A. Boolean Logic and
  Quantifier Elimination** (0 tests), **E. Statistics** (0 tests), and **Q. Tensors** (0
  tests — the file carries the literal comment `# Q1-Q6 Tensor tests missing`). So 38.3% is a
  *floor*: the true failure rate over Wester's full problem set is higher.

Failure rate by Wester section (section names read from the file's own headers):

| § | Domain | Tests | Failing | Rate |
|---|---|---:|---:|---:|
| A | Boolean logic & quantifier elimination | 0 | — | **not implemented** |
| B | Set theory | 4 | 0 | 0% |
| C | Numbers | 24 | 3 | 12% |
| D | Numerical analysis | 13 | 9 | **69%** |
| E | Statistics | 0 | — | **not implemented** |
| F | Combinatorial theory | 9 | 3 | 33% |
| G | Number theory | 10 | 4 | 40% |
| H | Algebra | 33 | 7 | 21% |
| I | Trigonometry | 12 | 8 | **67%** |
| J | Special functions | 18 | 4 | 22% |
| K | The complex domain | 10 | 1 | 10% |
| L | **Determining zero equivalence** | 9 | 4 | **44%** |
| M | Equations | 37 | 14 | 38% |
| N | Inequalities | 17 | 8 | 47% |
| O | Vector analysis | 6 | 2 | 33% |
| P | Matrix theory | 46 | 12 | 26% |
| Q | Tensors | 0 | — | **not implemented** |
| R | Sums | 23 | 16 | **70%** |
| S | Products | 10 | 5 | 50% |
| T | Limits | 14 | 3 | 21% |
| U | Differentiation | 17 | 8 | 47% |
| V | Indefinite integration | 16 | 7 | 44% |
| W | Definite integration | 28 | 16 | **57%** |
| X | Series | 22 | 9 | 41% |
| Y | Transforms (Laplace/Fourier/Z) | 13 | 6 | 46% |
| Z | Difference equations | 6 | 3 | 50% |

*(Reproduce: `curl -sL https://raw.githubusercontent.com/sympy/sympy/master/sympy/utilities/tests/test_wester.py`, then count `@XFAIL`/`@SKIP` decorators preceding `def test_*`.)*

**Reading of this table.** The high-failure regions are exactly the regions a physics or
engineering course lives in: **sums (70%), definite integration (57%), inequalities (47%),
indefinite integration (44%), transforms (46%), difference equations (50%)**. The low-failure
regions — set theory, complex numbers, numbers, algebra — are the regions where a numeric
check would have caught the error anyway. **CAS grounding is strongest where it is least
needed and weakest where it is most needed.** Any "L3 symbolic verification" tier must
therefore be built to *abstain loudly* rather than to answer.

### 2.2 Where CAS verification breaks: three mechanisms

**(a) Zero equivalence is undecidable.** Wester devotes section L to it; SymPy fails 44% of
it. The general problem — given an expression built from rationals, π, exponentials, logs,
absolute values, and sin, decide whether it is identically zero — is undecidable
(Richardson's theorem). A CAS's `simplify` is a heuristic pipeline, and *`simplify(e) != 0`
never means `e != 0`.* Treating a non-zero `simplify` result as a refutation is the single
most common misuse.

`MEASURED-BENCH` — **original measurement, this survey** (SymPy 1.14.0, see §4.2 harness):

| Candidate identity | `simplify(lhs − rhs)` | Verdict | Time |
|---|---|---|---|
| `sqrt(p)*sqrt(q) − sqrt(p*q)`, `p,q` unassumed | `sqrt(p)*sqrt(q) − sqrt(p*q)` | **cannot prove zero** | 5 ms |
| `log(exp(z)) − z`, `z` unassumed | `−z + log(exp(z))` | **cannot prove zero** | 9 ms |
| `sqrt(2+sqrt(3)) − (sqrt(6)+sqrt(2))/2` | `0` | proved | 14 ms |
| `((x+1)^(1/3))^3 − (x+1)`, `x>0` | `0` | proved | <1 ms |
| `exp(log(x)+log(y)) − x*y`, `x,y>0` | `0` | proved | <1 ms |

**(b) Assumption abuse — the pedagogically dominant failure.** The first two rows above are
not CAS bugs; they are the CAS being *correct* and the prose being *sloppy*. √x·√y = √(xy)
is false for negative reals; log(exp z) = z is false off the principal branch. A generated
explanation that writes these without stating x,y ≥ 0 is *wrong as written*, and the CAS
says so. But an unsophisticated grounding harness reads "CAS could not confirm" as "CAS
failed" and either suppresses the check or (worse) instructs the model to add
`positive=True` until it passes — laundering the error into the assumption set. **The
assumption declaration is part of the claim and must be checked, not chosen to make the check
pass.**

**(c) Notation abuse and the semantic gap.** CAS operates on expression trees, not on the
notation a textbook uses. `dy/dx` as a ratio, `∑` with an implied index range, `O(·)` in a
Taylor expansion, physicists' `d` vs `∂`, index-summation conventions — all of these are
notation the learner sees and the CAS never receives. Every translation from notation to
expression tree is an unverified step of exactly the same kind as autoformalization (§1.4),
with none of the tooling.

### 2.3 What CAS is genuinely excellent at

Do not over-correct. §4.2's measurement finds **100% recall and 0% false-alarm** for symbolic
checking over a corpus of 20 textbook identities × 6 mutation classes (113 wrong candidates)
and 37 semantically-equivalent rewrites, at **1.8 ms median / 10 ms p95**. Within its
competence, CAS verification is essentially free, essentially perfect, and grossly underused.
The engineering task is knowing the boundary, not avoiding the tool.

`MEASURED-BENCH` · **Step-wise symbolic verification generalises to physics.** On the TPBench
theoretical-physics dataset, a *symbolic weak-verifier* framework for parallel test-time
scaling *"significantly outperforms existing test-time scaling approaches"* and also
transfers to AIME — *"highlighting the power of step-wise symbolic verification for tackling
complex scientific problems"* (arXiv:2506.20729). This is direct evidence that L3 checking is
not merely a filter but a *capability amplifier*.

---

## 3. Executable documents

### 3.1 The Pimentel result — re-derived from the primary source

`MEASURED-BENCH` · **Pimentel, Murta, Braganholo & Freire, "A Large-scale Study about Quality
and Reproducibility of Jupyter Notebooks", MSR 2019.** Numbers below were read directly out of
the paper PDF (leomurta.github.io/papers/pimentel2019a.pdf), not from secondary summaries —
several widely-circulated restatements of this paper are wrong.

**Corpus construction**
- GitHub query (repos created 1 Jan 2013 – 16 Apr 2018, language "Jupyter Notebook"):
  **265,143 repositories, 1,450,071 notebooks**
- After excluding invalid/empty: 1,423,676 notebooks from 264,023 repositories
- After removing **264,510 (18.58%) duplicates** (SHA1 over cell sources and output formats):
  **1,159,166 notebooks**
- Python notebooks: 1,081,702 (93.32% of notebooks declare Python). Valid Python in all cells:
  **1,005,689 (86.76%)**
- Notebooks with **unambiguous execution order** (no repeated execution counters, no
  currently-executing cells): **863,878 (74.53%)** ← the reproducibility cohort

**The headline, verbatim from the abstract**

> **"As we discuss in Section IV, out of 863,878 attempted executions of valid notebooks
> (i.e., notebooks with defined Python version and execution order), only 24.11% executed
> without errors and only 4.03% produced the same results."**

**The breakdown**
- **208,323 notebooks (24.11%)** finished execution successfully
- **570,476** failed with an exception; **9,982** exceeded the 5-minute limit
- Of the 208,323 that finished, **173,487 produced *different* results** → **4.03% reproduced
  their own stored outputs**
- Top exception counts: **ImportError 178,919; ModuleNotFoundError 125,548; FileNotFoundError
  73,518; IOError 71,309; TypeError 35,458**
- **29.23%** of failures were ImportError/ModuleNotFoundError; **14.53%** NameError (hidden
  state / out-of-order); **12.59%** FileNotFoundError/IOError (data not in repo)
- Among notebooks that failed to reproduce, **50% differed in more than 53% of their cells**
- Of executed notebooks, only **24.9%** is the comparable reproducibility rate reported by
  Collberg et al. for general computer-systems research — i.e. notebooks are *not unusually
  bad*; the whole field is this bad

**The practice metrics that explain it**
- **Only 149,259** of 1.16M notebooks belong to a repository that declares dependencies at
  all. Within the 863,878 cohort, **118,483 (13.72%)** declared dependencies.
- **Dependency installation failure rates: `setup.py` 67.55%, `requirements.txt` 61.17%,
  `Pipfile` 65.20%.** Reasons: 35.04% require other unavailable files, 24.77% malformed,
  25.67% require a prior install step, 8.73% need external compilers/libraries.
- **36.36%** of unambiguous-execution-order notebooks have **out-of-order cells**;
  **76.90%** have at least one *skip*, averaging **12.82** skipped executions.
- **21.11%** of executed notebooks contain non-executed code cells; **62.08%** contain empty
  cells.
- **Only 1.54%** of valid Python notebooks import any testing module. **53.94%** define a
  function; **8.54%** define a class; **10.30%** import a local module.
- **30.93%** of notebooks contain **no markdown cell at all**. Median markdown cells: 4;
  median code cells: 13.

### 3.2 The negative result inside the negative result

`MEASURED-BENCH` · **Declaring dependencies made reproduction *worse* in Pimentel's data.**

> **"45.18% of the notebooks from repositories with declared dependencies failed with one of
> these errors [ImportError/ModuleNotFoundError], while only 31.24% of the notebooks from
> repositories without declared dependencies failed with these errors."**

The authors' own explanation is that undeclared-dependency notebooks were run in a *bloated
Anaconda environment* containing 100+ scientific packages, whereas declared-dependency
notebooks were run in a clean conda env built strictly from the declaration. **A 14-point
penalty for doing the "right thing."** Two lessons: (i) *declared dependencies are
systematically incomplete*, and (ii) **an environment that is permissive enough to run
everything is not an environment that has verified anything.** Any grounding harness that
executes generated code in a fat preinstalled image is measuring the image, not the code.

### 3.3 Containerisation helps and does not solve it

`MEASURED-BENCH` · arXiv:2604.01072 (Apr 2026), 443 notebooks from 116 GitHub repositories
referenced by PubMed Central publications, with automated dependency inference + container
generation + isolated execution:

- **Containerisation resolves 66.7% of prior dependency-related failures.**
- **53.7% of notebooks still exhibit low output fidelity**, from persistent runtime failures
  and stochastic non-determinism.
- Conclusion: *"standardized containerization is essential for computational stability but
  insufficient for full bit-wise reproducibility."*

`MEASURED-BENCH` · arXiv:2308.07333 (biomedical, PMC-indexed): of **27,271 notebooks** from
2,660 repositories across 3,467 articles, 22,578 Python, 15,817 with declared dependencies →
10,388 installable → **1,203 ran error-free, of which 879 produced identical results and 324
differed**. That is **879 / 15,817 = 5.6%** end-to-end, closely echoing Pimentel's 4.03%
across a completely different corpus and a two-year replication window.

**Two independent corpora, seven years apart, converge on ~4–6% self-reproduction. This is the
baseline any "executable textbook" claim must beat.**

### 3.4 marimo — investigated in detail

`marimo-team/marimo`: **Apache-2.0, 22,072 stars, 1,197 forks, created 2023-08-14, v0.23.15
released 2026-07-23, pushed daily.** (GitHub API, 2026-07-27) `OBSERVED`

**The mechanism.** marimo is a *reactive* notebook: it performs **static analysis** of each
cell to determine which global names it defines and which it reads, builds a **DAG** over
cells, and on running a cell automatically runs every cell that reads any name that cell
defines. The docs state the analysis *"incurs zero runtime overhead"* because it *"reads each
cell once"* and does not trace execution. Deleting a cell *"scrubs its variables from program
memory, eliminating hidden state."* Notebooks are stored as **pure Python `.py` files** (git-
diffable, script-executable, deployable as apps). Package requirements can be serialised
inline and run *sandboxed* in a temporary venv — *"reproducible down to the packages."*
(docs.marimo.io/faq, docs.marimo.io/guides/reactivity) `VENDOR` for the guarantees,
`OBSERVED` for the mechanism.

**The constraint that makes it work — and the one that limits it.**

> **"marimo requires that every global variable be defined by only one cell."**

This is the price of the guarantee: single-assignment across the notebook. Cycles are excluded
by the DAG. And crucially:

> **"marimo does not track mutations to objects."** Mutations like `my_list.append(42)` or
> `my_object.value = 42` *"don't trigger reactive re-runs of other cells."* If you assign
> `foo.bar = 10`, *"other cells referencing `foo.bar` will not be run."* Rationale given:
> *"Tracking mutations reliably is impossible in Python."*

The docs' own guidance — *"avoid defining a variable in one cell and mutating it in another"* —
is a **convention, not a guarantee.** `INFERENCE`: marimo eliminates the *ordering* class of
hidden state completely and the *mutation* class not at all. For a teaching artefact this is
a very good trade (teaching notebooks mutate little), but it must be stated: **a reactive
notebook is not a proof of reproducibility, it is the elimination of one dominant cause.**

Also: the runtime can be configured **lazy** — *"marking cells as stale instead of running
them"* — precisely for expensive or side-effecting cells. A lazily-configured marimo notebook
has the same staleness problem as Jupyter, by choice.

**A vendor-claim correction, and it is a load-bearing one.** marimo's FAQ says:

> *"[One study] analyzed 10 million Jupyter notebooks and found that 36% of them weren't
> reproducible"* — linking to the JetBrains Datalore blog (Dec 2020).

We checked the cited source. JetBrains downloaded **9,720,000 notebooks (Oct 2020)** and
classified **36%** as non-reproducible **on the basis of execution-count metadata alone** —
*"they examined execution order rather than actual re-execution"*, flagging notebooks whose
*"code cells were not originally executed in a linear order."* `MEASURED-BENCH`

**That 36% is a proxy for out-of-order execution, not a reproduction rate.** It is
near-identical to Pimentel's independently measured **36.36% out-of-order** figure. The number
that describes *reproduction* is Pimentel's **4.03%**. marimo's own supporting statistic is
therefore **9× more flattering to Jupyter than the truth**, which if anything understates
marimo's case. **The survey should quote 4.03% and cite Pimentel, not 36% and cite a vendor
FAQ quoting a vendor blog.**

### 3.5 The rest of the executable-document landscape

| Tool | Reproducibility mechanism | Hard limitation | Label |
|---|---|---|---|
| **Jupyter** | None. JSON file stores outputs decoupled from code; arbitrary execution order; deletion leaves variables in memory | 4.03% self-reproduction at scale (§3.1) | MEASURED-BENCH |
| **marimo** | Reactive DAG from static analysis; `.py` storage; single-definition rule; sandboxed inline deps | Mutations untracked; lazy mode opts out | VENDOR/OBSERVED |
| **Pluto.jl** | Reactive; *"at any instant, the program state is completely described by the code you see"*; *"no mutable workspace"*; **package environment with exact versions stored inside the notebook file** | Julia only; same mutation caveat as marimo | VENDOR (plutojl.org) |
| **Observable** | Reactive JS dataflow runtime; cells are a dependency graph, not a sequence | JavaScript-first; platform-coupled; documentation reviewed did not state runtime guarantees | OBSERVED (observablehq.com) |
| **Quarto** | `freeze: auto` (re-render only on source change) / `freeze: true` (never re-render in project renders); results cached in `_freeze/` and committed to VCS; `cache` via knitr/Jupyter Cache | **For `.ipynb` inputs, "Quarto will not execute the cells within the notebook by default (the presumption being that you have already executed them while editing)."** Freeze applies only to *project-wide* renders; an incremental single-document render always executes | OBSERVED (quarto.org) |
| **Jupyter Book / MyST-NB** | Build-time execution with `jupyter-cache`; execute modes off/force/cache/auto | Docs unreachable at time of research (HTTP 429); treat specifics as unverified | — |

`INFERENCE` — **the crucial and under-appreciated point about Quarto.** The most widely
adopted "executable document" toolchain in science *does not execute your notebook by
default*. `freeze` exists specifically so that published output need not be reproducible on
the publishing machine. This is a reasonable engineering choice for build-time cost and a
catastrophic one for a grounding guarantee. **"Built with an executable-document toolchain"
carries approximately zero evidential weight.** Only "executed in CI, in a clean environment,
with a non-zero exit code on failure" does.

**Design consequence for the reference implementation.** An executable document is a
*grounding delivery mechanism*, not a grounding *guarantee*. To convert it into one you need,
at minimum: (i) reactive or linear-enforced execution (marimo/Pluto class), (ii) pinned
environment *inside* the artefact (Pluto's model; marimo's sandbox; PEP 723 inline metadata),
(iii) execution in CI from a cold container, (iv) build failure on cell error, and (v)
assertions — not just outputs — because **only 1.54% of real notebooks contain any test at
all** and an output that is merely *printed* is not *checked*.

---

## 4. Numeric and simulation grounding: cheap, underused, and the best value on the ladder

### 4.1 The argument

A closed-form result is a claim about a function. A numerical evaluation of that function at
random points is a **Monte-Carlo test of the claim** that costs microseconds, needs no
library of formalised mathematics, needs no CAS competence in the relevant domain, and — the
key property — **degrades gracefully**: it cannot prove correctness, but it very rarely
misses an error, and it never gets *fooled* by notational sophistication.

The same logic runs one level up: an analytic solution to an ODE can be checked against a
numerical integration of the ODE; a derived closed-form partition function against a direct
sum; a claimed asymptotic against the exact quantity at large n; a probability formula against
a simulation. The check is *dumb by construction*, which is precisely why it is not correlated
with the generator's errors.

This principle is already the strongest empirical result in tool-augmented reasoning:

- `MEASURED-BENCH` **PAL (arXiv:2211.10435)**: offloading the *solving* step to a Python
  interpreter while the LLM only *decomposes* beats chain-of-thought across 13 benchmarks;
  PAL with Codex beat PaLM-540B CoT on GSM8K by **+15 points absolute top-1**.
- `MEASURED-BENCH` **Program-aided reasoners are better *calibrated*, not just more accurate**
  (arXiv:2311.09553): PAL improves calibration in **75% of instances** across 5 datasets and
  2 model families; lower-diversity prompting styles are better calibrated. For a tutor,
  calibration is worth as much as accuracy — a system that knows when it does not know can
  escalate.
- `MEASURED-BENCH` **AlphaEvolve** (arXiv:2511.02864) is the extreme case: an evolutionary
  coding agent with **automated evaluation** in the loop, run over **67 open problems** in
  analysis, combinatorics, geometry and number theory, rediscovering best-known constructions
  in most and improving several. The generative model proposes; a *program* disposes.

### 4.2 Original experiment: measured coverage and cost of the cheap tiers

Because the brief demands the ladder be *implementable*, we built and ran the checkers rather
than describing them. `MEASURED-BENCH` — **original, this survey.**

**Design.** 20 reference expressions: 10 pure calculus/algebra identities (binomial square,
geometric series, product rule, Gaussian integral, cos double angle, Taylor sin to O(x⁴),
cubic expansion, log product, Pythagorean identity, partial fractions) and 10 dimensioned
physics formulas (kinetic energy, pendulum period, spring energy, escape velocity, photon
energy, Lorentz factor, free-fall distance, momentum, centripetal acceleration, gravitational
PE). For each we generated:

- **37 semantically-equivalent rewrites** (e.g. `sqrt(pi/a)` vs `pi**(1/2) * a**(-1/2)`;
  `1 - 2sin²x` vs `cos 2x` vs `2cos²x − 1`; `2π√(L/g)` vs `√(4π²L/g)`) → any flag is a
  **false alarm**;
- **113 mutants** across six error classes that model real derivation slips: **sign flip,
  factor of 2, factor of ½, exponent off by one, dropped additive term, wrong variable
  substituted** → any pass is a **miss**.

Three checkers: **dimensional** (`pint` unit algebra), **numeric** (8 random substitutions,
relative tolerance 1e-9), **symbolic** (`sympy.simplify`, then a `trigsimp∘powsimp∘expand`
fallback). SymPy 1.14.0, pint 0.25.3, Python 3.12, single core.

**Result — recall on 113 wrong candidates:**

| Checker | Recall | Abstentions | False alarms on 37 equivalent rewrites |
|---|---|---|---|
| **Dimensional** | **28/55 = 50.9%** (of the dimensioned subset) | 58 (undimensioned formulas) | **0 / 14** |
| **Numeric** | **112/113 = 99.1%** | 0 | **0 / 37** |
| **Symbolic** | **113/113 = 100%** | 0 | **0 / 37** |

**Result — recall by error class (this is the whole point):**

| Error class | Dimensional | Numeric | Symbolic |
|---|---|---|---|
| sign flip | **0 / 9** | 20/20 | 20/20 |
| factor of 2 | **0 / 9** | 20/20 | 20/20 |
| factor of ½ | **0 / 9** | 20/20 | 20/20 |
| exponent off by one | **10 / 10** | 20/20 | 20/20 |
| dropped additive term | **9 / 9** | 20/20 | 20/20 |
| wrong variable | **9 / 9** | 12/13 | 13/13 |

**Result — cost (wall clock per check, n = 170):**

| Checker | median | mean | p95 | max |
|---|---|---|---|---|
| Dimensional | **0.07 ms** | 0.11 ms | 0.25 ms | 2.5 ms |
| Numeric | **0.61 ms** | 1.7 ms | 3.7 ms | 96 ms |
| Symbolic | **1.8 ms** | 3.3 ms | 10.8 ms | 35 ms |

**Findings.**

1. **The numeric tier is nearly as good as the symbolic tier at a third of the cost and with
   none of the domain gaps.** 99.1% vs 100% recall. Given that the symbolic tier fails 38.3%
   of the Wester suite (§2.1) in domains the numeric tier handles without noticing, *the
   numeric check should be the default and the symbolic check the escalation, not the
   reverse.* This inverts the usual instinct.
2. **Zero false alarms on 37 non-trivial equivalent rewrites for both numeric and symbolic.**
   The main practical fear about automated checking — that it will reject correct answers
   written differently — did not materialise on textbook-scale expressions.
3. **The single numeric miss is instructive.** For the Lorentz factor `1/√(1−v²/c²)`, the
   "wrong variable" mutant substitutes `v→c`, yielding `zoo` (complex infinity). The checker
   compared two degenerate values and reported agreement. **Numeric checking must treat
   non-finite results as abstention, not as agreement** — a one-line fix, and exactly the kind
   of thing that only surfaces by running the harness.
4. **Dimensional analysis has a perfectly clean signature**: **100% on all three structural
   error classes (exponent, dropped term, wrong variable), 0% on all three magnitude error
   classes (sign, ×2, ÷2).** It is not a weak version of the other checks; it is an
   *orthogonal* check that costs 0.07 ms.

*(Harness committed at `evidence/F3-grounding-ladder-harness.py`, ~240 lines, stdlib + sympy
+ pint. Reproducible in full: `pip install sympy pint && python
evidence/F3-grounding-ladder-harness.py`.)*

### 4.3 Why this is underused

`INFERENCE` · Three reasons, none of them good:

- **Prestige gradient.** Formal proof is glamorous and publishable; `assert abs(a-b) < tol`
  is not. The literature therefore over-invests in L4 and under-invests in L2.
- **It requires committing to a concrete instance**, which authors of general derivations
  resist. But a derivation that cannot be instantiated is a derivation that cannot be checked
  — and usually one the learner cannot use either.
- **It does not produce a certificate.** A numeric check produces confidence, not proof. In a
  culture that scores artefacts on their strongest guarantee, a probabilistic check reads as
  no check. **This is the error the ladder is designed to correct: 99% recall at 0.6 ms
  dominates 100% recall at 4 megatokens for every claim that will be read once.**

---

## 5. Dimensional analysis as a free correctness check

### 5.1 What it buys

Dimensional homogeneity (Fourier, 1822) is a *type system for physics*. Every equation must
have identical dimensions on both sides; every argument to a transcendental function must be
dimensionless; every additive term must match. Checking this is unit algebra — a few
multiplications over a rational exponent vector — and it is **decidable, total, and
instantaneous**.

Our measurement (§4.2): **0.07 ms median**, **100% detection of exponent errors, dropped
terms and wrong-variable substitutions**, **0 false alarms**, **0% detection of sign and
coefficient errors**. That signature is the whole specification. Buckingham Π extends the
same idea to *discovering* the dimensionless groups a relation must be a function of
(arXiv:2202.04643 shows this can be automated and used as a learning constraint).

### 5.2 The evidence that nobody runs it

`MEASURED-BENCH` · **arXiv:2512.00689** is the cleanest possible demonstration. The Size-Strain
Plot method for extracting crystallite size and microstrain from X-ray diffraction is a
workhorse of materials science. The paper shows that *"the equation most commonly applied in
SSP analysis is dimensionally inconsistent, a critical flaw that has gone largely unnoticed
and replicated across decades of materials research,"* raising *"concerns about the validity
of a significant body of published microstructural data."* It traces the historical origin of
the misformulated equation and provides a dimensionally consistent replacement.

**A check costing 0.07 ms, available since 1822, would have caught this in the first paper.**
It ran in none of them, for decades, across a literature. If human experts under peer review
do not run the free check, an automated pipeline certainly must.

### 5.3 The boundary — and the standard over-claim

`MEASURED-BENCH` · arXiv:1807.07643 ("Physical-type correctness in scientific Python") states
the limitation exactly:

> *"Since many physical quantities have the same units, it is possible for a block of code to
> be **unit-compatible, but still physically meaningless**."*

Torque and energy are both N·m. Entropy and heat capacity are both J/K. Frequency and angular
frequency are both s⁻¹ — and confusing them is a factor of 2π, which dimensional analysis is
constitutionally blind to. The paper's proposal — checking **kind-of-quantity**, not just
unit — is the correct fix and is *not* what off-the-shelf unit libraries do. It also
demonstrates *"the limitations of three Python unit-libraries."*

Also relevant: `PhysLib` (arXiv:2510.26094) exists because Lean 4's mathlib has no unit
system; adding one improved formal physics performance by **+11.75% average**. Dimensional
reasoning is not free inside a proof assistant — it is free only in a units-aware runtime.

**Ruling for the ladder: dimensional analysis is a mandatory gate, never a sufficient check.**
It is the cheapest tier and must run on 100% of dimensioned claims, but it may only ever
*reject*, never *accept*.

---

## 6. Retrieval grounding

### 6.1 What retrieval can and cannot ground

Retrieval attaches a claim to a document. That is a genuinely different guarantee from the
executable tiers: it establishes **provenance**, not **truth**. It is the only mechanism
available for the large fraction of educational content that is *conventional* rather than
*derivable* — notation, definitions, historical facts, disciplinary norms, syllabus scope,
"what this course means by 'stable'". For those, provenance *is* correctness. For anything
derivable, provenance is the weakest tier that is still above prose.

Retrieval is also the load-bearing mechanism *inside* formal verification: LeanDojo's ReProver
(arXiv:2306.15626) is retrieval-augmented precisely because **premise selection is "a key
bottleneck in theorem proving"** over a library where developers use a median 1.6% of imported
scope (§1.1).

### 6.2 The attribution numbers, and they are bad

`MEASURED-BENCH` · **"Cited but Not Verified" (arXiv:2605.06635, May 2026)** — the most
directly relevant measurement, benchmarking 14 closed- and open-source LLMs on inline
citations parsed from generated Markdown reports, scored on three axes:

| Axis | Frontier-model result |
|---|---|
| **Link Works** (URL resolves) | **> 94%** |
| **Relevant Content** (topical alignment) | **> 80%** |
| **Fact Check** (claim actually supported by the source) | **39 – 77%** |

And the finding that should govern system design:

> **"Fact Check accuracy drops by approximately 42% on average across two frontier models as
> tool calls scale from 2 to 150, demonstrating that more retrieval does not produce more
> accurate citations."**

Plus: *"fewer than half of open-source models successfully generate cited reports in a
one-shot setting."* The authors' framing — *"a critical disconnect between surface-level
citation quality and factual reliability"* — is the exact phenomenon this section exists to
address, transposed from mathematics to prose.

`MEASURED-BENCH` · **AttributionBench (arXiv:2402.15089)**: even *automatically evaluating*
attribution is unsolved — a fine-tuned GPT-3.5 reaches only **~80% macro-F1** on binary
supported/not-supported classification. `MEASURED-BENCH` · **CAQA (arXiv:2401.14640)**
benchmarks 25 automatic attribution evaluators against human evaluators using
knowledge-graph-generated fine-grained attribution categories, and finds prior evaluation
lacking on granularity, manual-annotation dependence, and subtle-difference discrimination.
`MEASURED-BENCH` · **Attributed QA (arXiv:2212.08037)** established the task and the human-
gold-standard evaluation framework.

**Reading.** Citation formatting is a solved problem; citation *truth* is not. A pipeline that
requires citations and checks only that they resolve has purchased **94%-grade theatre for
39–77%-grade truth.** The `L1` tier of the ladder must therefore be defined as *"cited **and**
the cited span entailment-checked"*, not *"cited."*

### 6.3 Where RAG fails *specifically for pedagogy*

This is the part of the literature that is genuinely surprising, and it is a null/negative
result of the first importance.

`MEASURED-RCT-adjacent` · **arXiv:2310.03184, "Retrieval-augmented Generation to Improve Math
Question-Answering: Trade-offs Between Groundedness and Human Preference."** Real middle-school
student questions in algebra and geometry; responses generated with retrieved content from a
high-quality open-source math textbook; multi-condition human survey. Finding:

> **"Humans prefer responses generated using RAG, but not when responses are too grounded in
> the textbook content."**

> *"Designers of math QA systems must consider trade-offs between generating responses
> preferred by students and responses closely matched to specific educational resources."*

**This is the pedagogical failure mode of retrieval grounding, and it is not a bug in the
retriever.** A textbook is written for a *reader who is already at the textbook's level*. A
student asking a question is, by definition, not at that level — that is why they are asking.
Faithful retrieval reproduces the register, vocabulary, notation and assumed prerequisites of
the source. **Groundedness and comprehensibility are in genuine tension**, and increasing one
decreases the other past an optimum. Any system that maximises groundedness maximises the
wrong thing.

`INFERENCE` · The five pedagogy-specific RAG failure modes, of which only the first is
generic:

1. **Unfaithful attribution.** Covered above: 39–77% fact-check accuracy (arXiv:2605.06635).
2. **Register mismatch / over-grounding.** Measured directly (arXiv:2310.03184). Faithful =
   at the source's difficulty, which is above the asker's.
3. **Curriculum misalignment.** The retrieved corpus encodes *a* pedagogical sequence. A
   student mid-course needs the explanation that uses only what they have already seen. A
   retriever ranked on semantic similarity has no representation of "prerequisites the learner
   has covered." Retrieval is topic-aware and *prerequisite-blind*.
4. **Absence of the negative.** Textbooks state what is true. The single highest-value
   pedagogical content — the *misconception*, the *common wrong turn*, the *why-this-obvious-
   approach-fails* — is largely absent from authoritative corpora. Retrieval cannot ground a
   claim about an error nobody wrote down.
5. **The gap between "supported" and "responsive."** A response can be perfectly entailed by
   the retrieved passage and not answer the question asked. Attribution metrics score
   entailment; nothing scores responsiveness.

`MEASURED-BENCH` · A confirming negative from an adjacent education domain: **arXiv:2409.15260**,
*"Generative AI Is Not Ready for Clinical Use in Patient Education for Lower Back Pain
Patients, Even With Retrieval-Augmented Generation."* Physical therapists rated model output
on redundancy, accuracy and completeness (Likert) plus Flesch Reading Ease. RAG-based LLMs
**did** beat non-RAG on all axes — *"and yet"* — *"our analysis reveals that the generated
materials are not yet ready for use in clinical practice,"* with the residual problems being
**clinical relevance and granularity**. Precisely the register/curriculum axis, not the
factuality axis.

**Contrast case (positive, but read the design).** *"Battling Botpoop"* (arXiv:2406.07796)
deployed a RAG chatbot at NTU Singapore with **97.1% of participants reporting positive
experiences** — a satisfaction measure, not a learning measure. `VENDOR`-adjacent. Do not
promote to a finding.

---

## 7. What cannot be verified — the boundary, stated explicitly

Every mechanism above shares a precondition: **the claim must have a truth condition that a
non-linguistic process can evaluate.** The following do not, and no amount of tooling will
change that. This list is not a caveat; it is a specification of where human judgement and
learning-science evidence (B1) must carry the load.

| Property | Why it is unverifiable | What can be measured instead |
|---|---|---|
| **Intuition quality** — does this *make sense* of the result? | No ground truth. Two correct intuitions can be incompatible in emphasis and both excellent. | Downstream transfer performance on novel items (B1/F1) |
| **Analogy quality** | Every analogy is false somewhere; the question is whether it breaks *where the learner will not step*. That depends on the learner's next 10 questions. | Whether the analogy's known failure points are *stated*; misconception rates in later assessment |
| **Pedagogical appropriateness** — is this the right explanation *for this learner now*? | Depends on prior knowledge, working-memory load, and the expertise-reversal effect. The *same* correct explanation is right for one learner and harmful for another. | Prior-knowledge diagnosis (F5), measured learning gain |
| **Sequencing / prerequisite ordering** | A DAG can be checked for cycles. Whether it is the *best* order is an empirical question about humans. | A/B on completion and gain |
| **"Why this matters"** | A claim about values and about a future the learner has not had yet. Not truth-apt. | Nothing. Declare it as authored opinion. |
| **Motivation, tone, encouragement** | Not truth-apt. | Persistence and return-rate (F6) |
| **Choice of what to omit** | The highest-leverage editorial act in teaching, and invisible to every checker in this section. A perfectly verified explanation of the wrong 20% is a failure no tier detects. | Expert review; coverage against a syllabus |
| **Whether the formalisation means what the prose meant** | §1.4: this is the autoformalization gap. It is a natural-language semantics judgement and it sits *upstream of* the kernel. | Human spot-audit; GTED-style semantic metrics (arXiv:2507.07399) |

**Two consequences the survey must not soften.**

1. **Verification is a floor, not a quality.** A fully L4-verified explanation can be
   pedagogically worthless — badly sequenced, pitched wrong, omitting the point. Grounding
   removes a failure mode; it does not add a virtue. Any product claim of the form "verified,
   therefore good" is a category error.
2. **The unverifiable layer is where the teaching is.** Everything in §1–6 is the part of
   teaching a machine can now do at near-zero marginal cost. The residue in the table above is
   the part that remains scarce. This is the same conclusion F4 reached from the economics
   side, arrived at independently: **as verification cost → 0, 100% of the remaining problem
   is the part verification does not address.**

---

## 8. THE GROUNDING LADDER

### 8.1 The tiers

Five tiers, ordered by strength of guarantee. **L2 splits into two orthogonal sub-checks**
because our measurement (§4.2) shows they catch disjoint error classes at comparable
(negligible) cost, and running only one is a mistake.

| Tier | Name | Artefact produced | Guarantee | Rejects |
|---|---|---|---|---|
| **L0** | **Unverified prose** | Text | None | Nothing |
| **L1** | **Cited + entailment-checked** | Claim ↔ source span, with an entailment verdict | The source says this | Fabricated support |
| **L2a** | **Dimensionally checked** | Unit-algebra trace | The equation is type-correct | Structural errors |
| **L2b** | **Numerically checked** | Executed check + seeds + tolerance | Agreement at sampled points | Nearly all value errors |
| **L3** | **Symbolically verified** | CAS normal-form certificate | Expressions are equal as symbolic objects | All value errors, in-domain |
| **L4** | **Formally proved** | Machine-checked proof term | The theorem follows from the axioms | Every logical error, modulo the statement |

### 8.2 Cost and coverage — the actual numbers

All figures measured or sourced above. "Coverage" = fraction of *claims of the relevant kind*
the tier can even be applied to. "Recall" = fraction of *wrong* claims it rejects, where
measured.

| Tier | Marginal cost / claim | Latency | Applicability (coverage) | Recall on wrong claims | False-alarm rate |
|---|---|---|---|---|---|
| **L0** | 0 | 0 | 100% | **0%** | 0 |
| **L1** | 1 retrieval + 1 NLI call ≈ **$10⁻⁴–10⁻³** | 0.3–3 s | ~100% of factual/conventional claims | **Fact-check accuracy 39–77%** (arXiv:2605.06635); auto-eval itself ~80% F1 (arXiv:2402.15089) | High; degrades **~42%** as retrieval depth 2→150 |
| **L2a** dimensional | **0.07 ms** (median, measured) | <1 ms | Only dimensioned claims — **50% of our corpus** | **100%** on exponent/dropped-term/wrong-variable; **0%** on sign/coefficient | **0 / 14** measured |
| **L2b** numeric | **0.61 ms** (median), 3.7 ms p95 | <5 ms | Any claim instantiable at a point — very high | **99.1%** (112/113 measured) | **0 / 37** measured |
| **L3** symbolic | **1.8 ms** median, 10.8 ms p95 | <50 ms typical; **unbounded worst case** | **~62% of the classical CAS problem space** (SymPy passes 245/397 Wester; 3 domains unimplemented) | **100%** in-domain (113/113 measured) | **0 / 37** measured |
| **L4** formal | **<$0.01/proof** (best case, mathlib-native) → **4M tokens/problem** → **3 days/problem** → **11 person-years** (Flyspeck) | seconds → years | **~90%** competition; **~60–88%** UG in mathlib idiom (**−26 pts** off-idiom); **16–35%** college physics; **~0** applied/numerical | ~100% of *proof* errors; **0%** of *statement* errors → end-to-end **36%** (arXiv:2511.03108) | Low, but abstention rate is the real cost |

**The five facts a reader should take from this table.**

1. **L2 costs about a millisecond and catches ~99% of derivation errors.** There is no
   economic argument for ever shipping an L0 formula.
2. **L2a and L2b are orthogonal, not redundant.** Dimensional catches 100%/0% by class;
   numeric catches ~99% overall. Run both; together they cost 0.7 ms.
3. **L3 is ~3× the cost of L2b for +0.9 points of recall on textbook material, and it has a
   38.3% hole** in exactly the applied domains (sums, definite integrals, transforms,
   inequalities) where teaching happens. **L3 is an escalation tier, not a default.**
4. **L4's cost spans nine orders of magnitude** depending on whether the claim lives inside
   mathlib's idiom. The routing decision is therefore not "how important is this claim" but
   **"is this claim already formalisable?"**
5. **L4's guarantee has a hole L1–L3 do not have**: it verifies the *formal statement*, and
   the informal→formal step is unverified. This is why L4 does not subsume L1 — a formally
   proved theorem still needs its statement checked against the prose, which is an L1-class
   entailment problem.

### 8.3 The decision rule

`INFERENCE` — this is the section's design contribution. Route by **claim type**, then apply
**cost-modulating** rules.

**Step 1 — classify the claim.**

| Claim type | Recogniser | **Required tier** | Rationale |
|---|---|---|---|
| **Convention / definition / notation** ("we write ∂ for…", "in this course, stable means…") | No truth condition beyond authority | **L1** | Provenance *is* correctness. Higher tiers are inapplicable. |
| **Empirical fact / historical / citation** | Named entity, date, quantity attributed to a source | **L1** | Only mechanism available. Must include entailment check, not just link-resolves. |
| **Numeric result** (a computed value) | Expression evaluates to a number | **L2b** | 0.6 ms, ~99% recall. Never ship unchecked. |
| **Dimensioned physical relation** | Any variable carries units | **L2a + L2b** | L2a is 0.07 ms and catches the class L2b's tolerance can mask. Both, always. |
| **Symbolic identity / closed-form derivation step** | Equation between expressions | **L2b, escalate to L3** | L2b first (cheaper, no domain holes); L3 only if L2b flags or if the claim is *reused* (see Step 2). |
| **Algorithm / code claim** ("this runs in O(n log n)", "this function returns…") | Executable | **L2b as executed tests + assertions** | Execution with assertions. Printed output is not a check. |
| **Statement about a model's behaviour / simulation** | Dynamical claim | **L2b via simulation cross-check** | Analytic vs numerical integration. |
| **General theorem asserted as universally true** ("for all n…", "always", "never") | Universal quantifier over an infinite domain | **L3 minimum; L4 if reused** | Numeric sampling cannot establish a universal. This is the one place L2b is *categorically* insufficient. |
| **Foundational result the rest of the artefact depends on** | In-degree ≥ k in the claim DAG | **L4 if formalisable, else L3 + human sign-off** | Amortise: cost per *reader* falls with reuse. |
| **Intuition, analogy, motivation, sequencing, "why this matters"** | §7 | **L0, explicitly labelled** | Verification is inapplicable. **Label it, do not launder it.** |

**Step 2 — cost-modulating rules (applied after Step 1).**

1. **Reuse rule.** Verification cost is one-time; reading is many-time. If a claim will be
   served to *N* learners, the per-learner cost of tier *T* is `cost(T)/N`. **Escalate one
   tier for every ~100× in expected N.** A claim in a shared curriculum spine at N=10⁶
   justifies L4 at 4M tokens (~$4 ⇒ $0.000004/learner); the same claim generated once for one
   learner does not.
2. **Blast-radius rule.** If a claim is a *premise* of ≥ 3 downstream claims in the artefact's
   dependency DAG, escalate one tier. Errors in premises are not local.
3. **Irreversibility rule.** If the claim will be *memorised* (a formula on a reference card, a
   spaced-repetition item — see F11), escalate one tier. Misremembered-correct is recoverable;
   remembered-wrong is expensive to unlearn.
4. **Abstention rule.** A tier that abstains has **not** verified. Abstention must propagate
   as `unverified`, never as `passed`. (§4.2's Lorentz-factor miss is exactly this failure:
   `zoo == zoo` must be abstention.) Non-finite values, timeouts, `simplify` returning
   non-zero, and missing units are all abstentions.
5. **Assumption rule.** Assumptions required to make a check pass are **part of the claim**.
   If `positive=True` was needed, the explanation must state the positivity hypothesis. A
   harness that adds assumptions to make checks pass is a laundering machine (§2.2b).
6. **Downgrade rule.** A claim that fails its required tier is **not** downgraded to prose.
   It is *withheld*, or shipped with an explicit failure annotation. Silent downgrade is how
   L0 content acquires L3 credibility.

**Step 3 — what ships.** Every claim carries a machine-readable tier badge and, for L1–L4, a
pointer to the artefact that justifies it (source span + entailment verdict; unit trace; seeds
and tolerances; CAS certificate; proof term hash). **The badge is the contract with the
learner.** F1's assessment reconstruction can then key off it; G1 can render it.

### 8.4 Reference implementation sketch

```
claim
  ├─ classify(claim) ──────────────────► required_tier          [Step 1]
  ├─ modulate(reuse, blast_radius, memorised) ► required_tier'  [Step 2]
  └─ verify(claim, required_tier'):
        L1: retrieve(k) → span; entail(claim, span) ∈ {sup, contra, neutral}
            PASS iff sup.   ⚠ do NOT scale k: fact-check accuracy fell ~42%
                            from k=2 to k=150 (arXiv:2605.06635)
        L2a: units(lhs) ≟ units(rhs); every additive term homogeneous;
             every transcendental argument dimensionless
            PASS iff equal.  ABSTAIN if any symbol lacks a declared unit.
        L2b: for i in 1..8: sample free vars; |lhs−rhs| ≤ rtol·(|lhs|+|rhs|)
            PASS iff all trials agree AND all values finite.
            ABSTAIN on non-finite, on domain error, on NaN.
        L3:  d = simplify(lhs − rhs); if d == 0 PASS
             else d2 = simplify(trigsimp(powsimp(expand(d), force=True)))
             if d2 == 0 PASS else ABSTAIN     ← never "FAIL": Richardson
        L4:  autoformalize → lake build → proof term
             PASS iff kernel accepts AND a separate L1 entailment check
                  confirms the formal statement matches the prose  ← §1.4
   ▸ result ∈ {PASS, FAIL, ABSTAIN} × tier;  ABSTAIN ≠ PASS  [Step 2, rule 4]
```

Delivery substrate: a **reactive notebook (marimo / Pluto class) executed in CI from a cold
container, with pinned dependencies serialised inside the artefact, failing the build on any
cell error and on any assertion failure.** Not Jupyter (§3.1), and not Quarto-with-`freeze`
over pre-executed `.ipynb` (§3.5).

### 8.5 Worked routing examples

| Claim | Type | Tier | Cost |
|---|---|---|---|
| "The pendulum period is T = 2π√(L/g)" | dimensioned relation | L2a+L2b | 0.7 ms |
| "Therefore ∫₀^∞ e^{−ax²}dx = ½√(π/a)" | symbolic identity, reused across a course | L2b → L3 (reuse rule) | ~2 ms |
| "For all n ≥ 1, Σᵢ₌₁ⁿ i³ = (n(n+1)/2)²" | universal quantifier | L3 minimum; L4 (mathlib-native, sub-cent) | <$0.01 |
| "Heat capacity has units J/K" | convention | L1 | ~$10⁻⁴ |
| "Newton published the *Principia* in 1687" | historical | L1 + entailment | ~$10⁻⁴ |
| "Think of entropy as the number of ways to arrange the microstates" | intuition | **L0, labelled** | 0 |
| "This sorting routine is O(n log n)" | algorithmic | L2b as executed benchmark + assertion | ms–s |
| "The Navier–Stokes similarity solution below satisfies the PDE" | analytic vs numeric | L2b via numerical PDE integration | s |
| "You should learn this before tensors" | sequencing | **L0, labelled** | 0 |

---

## 9. Negative and null results register

The editorial standard requires ≥1 documented negative or null result. This section has seven,
which is appropriate given that the subject *is* the gap between apparent and actual grounding.

1. **`MEASURED-BENCH` — Declaring dependencies made notebooks *less* reproducible.**
   Pimentel et al.: 45.18% of notebooks from repos *with* declared dependencies failed with
   ImportError/ModuleNotFoundError vs **31.24%** from repos *without*. A 14-point penalty for
   following best practice, because declarations are incomplete and the comparison environment
   was a fat Anaconda image. **Doing the documented right thing produced a worse outcome than
   doing nothing.**
2. **`MEASURED-BENCH` — Component benchmarks do not compose.** 97% autoformalization × 69%
   proving = **36% end-to-end** (arXiv:2511.03108), with the loss attributable to
   formal/informal discrepancies in **more than half** of miniF2F's problems.
3. **`MEASURED-BENCH` — More retrieval makes citations *less* factual.** Fact-check accuracy
   drops **~42%** as tool calls scale from 2 to 150 across two frontier models
   (arXiv:2605.06635). Scaling the obvious knob moves the metric backwards.
4. **`MEASURED-BENCH` — More sampling buys nothing.** DeepSeek-Prover-V1.5-RL on miniF2F-test:
   k=32 → k=64 yields **zero** additional theorems (42/244 both) (arXiv:2601.16172). The
   standard test-time-compute lever is inert under mode collapse.
5. **`MEASURED-BENCH` — Groundedness and student preference trade off.** *"Humans prefer
   responses generated using RAG, but not when responses are too grounded in the textbook
   content"* (arXiv:2310.03184). Maximising the grounding objective degrades the pedagogical
   objective.
6. **`MEASURED-BENCH` — RAG improved every measured axis and the output was still unusable.**
   Patient education for lower back pain: RAG beat non-RAG on accuracy, completeness,
   redundancy and readability, and PT reviewers judged the materials *"not yet ready for use
   in clinical practice"* (arXiv:2409.15260). **Beating the baseline on every metric is not
   the same as clearing the bar.**
7. **`MEASURED-BENCH` — Kernel acceptance overstates formalization quality.** Systematic audit
   found incomplete multi-part statements, added weakening hypotheses and parameter
   restrictions *"that kernel acceptance entirely obscures"* (arXiv:2606.14000). The strongest
   available guarantee has a systematic blind spot in the direction of over-reporting.

**Plus one original null result (this survey):** across 37 semantically-equivalent rewrites of
20 textbook formulas, **neither the numeric nor the symbolic checker produced a single false
alarm.** The most common objection to automated checking of student/model output — that it
will punish correct answers written differently — did **not** replicate at textbook scale.
Reported as a null because it is the absence of an expected effect.

---

## 10. Open problems and the handoff to G1

**What is solved.** Cheap grounding. A millisecond of dimensional + numeric checking catches
~99% of derivation errors with zero false alarms, and nobody runs it. This is the highest
return-on-effort intervention in the entire survey and it requires no research.

**What is not solved, in priority order.**

1. **The informal→formal semantic gap (§1.4).** The single largest source of unverified trust
   in the whole stack. Needs: cheap semantic-fidelity metrics (GTED is a start,
   arXiv:2507.07399), paraphrase-robust formalization (arXiv:2511.12784 shows current models
   are not), and audit methodology beyond kernel acceptance (arXiv:2606.14000).
2. **Off-manifold formalization.** −26 points when a textbook builds its own definitions
   (TaoBench). A tutor that must follow *a specific course* is exactly the off-manifold case.
3. **Applied and physical domains.** College physics 16–35% (LeanPhysBench); numerical
   analysis absent from mathlib; SymPy fails 57–70% of Wester's sums, definite integrals and
   transforms; statistics and tensors unimplemented. **The domains where formulas matter most
   to learners are the domains with the weakest grounding infrastructure.**
4. **Kind-of-quantity checking.** Unit-compatible-but-meaningless is a real and unaddressed
   class (arXiv:1807.07643). Torque vs energy, ω vs f.
5. **Curriculum-aware retrieval.** Every retriever ranks on semantic similarity; none ranks on
   "uses only prerequisites this learner has covered." This is the concrete, buildable fix for
   RAG failure mode 3 (§6.3) and it connects directly to F5's learner model.
6. **Verifying the omission.** No tier in this section detects a correct explanation of the
   wrong 20%. Open.

**Dependencies exported to G1.**

- The **tier badge** is a required field on every generated claim. G1's architecture must carry
  it end-to-end; it is the interface between generation and trust.
- **ABSTAIN is a first-class result** and must be representable in G1's data model. Collapsing
  `{PASS, FAIL, ABSTAIN}` to a boolean destroys the entire guarantee.
- The **executable substrate must be reactive and CI-executed**, not Jupyter, not
  freeze-cached. G1 should assume marimo/Pluto-class semantics.
- The **claim dependency DAG** must exist, because two of the three cost-modulating rules
  (blast radius, reuse) are functions of it.
- G1 must **not** treat L4 as the terminal goal. Per §8.2, L4's cost spans nine orders of
  magnitude and its guarantee has a hole L1 must patch. The ladder is a router, not a
  staircase to be climbed.

---

## Sources

**Formal verification — models, benchmarks, critiques**
1. miniF2F — arXiv:2109.00110 · http://arxiv.org/abs/2109.00110
2. miniF2F-Lean Revisited / miniF2F-v2 — arXiv:2511.03108 · http://arxiv.org/abs/2511.03108
3. ProofNet — arXiv:2302.12433 · http://arxiv.org/abs/2302.12433
4. PutnamBench — arXiv:2407.11214 · http://arxiv.org/abs/2407.11214
5. TaoBench — arXiv:2603.12744 · http://arxiv.org/abs/2603.12744
6. Lean4Physics / LeanPhysBench / PhysLib — arXiv:2510.26094 · http://arxiv.org/abs/2510.26094
7. DeepSeek-Prover — arXiv:2405.14333 · http://arxiv.org/abs/2405.14333
8. DeepSeek-Prover-V1.5 — arXiv:2408.08152 · http://arxiv.org/abs/2408.08152
9. DeepSeek-Prover-V2 — arXiv:2504.21801 · http://arxiv.org/abs/2504.21801
10. Goedel-Prover — arXiv:2502.07640 · http://arxiv.org/abs/2502.07640
11. Goedel-Prover-V2 — arXiv:2508.03613 · http://arxiv.org/abs/2508.03613
12. Seed-Prover — arXiv:2507.23726 · http://arxiv.org/abs/2507.23726
13. Seed-Prover 1.5 — arXiv:2512.17260 · http://arxiv.org/abs/2512.17260
14. LeanDojo / ReProver — arXiv:2306.15626 · http://arxiv.org/abs/2306.15626
15. Autoformalization with LLMs — arXiv:2205.12615 · http://arxiv.org/abs/2205.12615
16. GTED autoformalization metric — arXiv:2507.07399 · http://arxiv.org/abs/2507.07399
17. Autoformalization robustness to paraphrase — arXiv:2511.12784 · http://arxiv.org/abs/2511.12784
18. Formalizing Numerical Analysis: quality audit beyond kernel acceptance — arXiv:2606.14000 · http://arxiv.org/abs/2606.14000
19. Evaluation of LLMs for Mathematical Formalization in Lean (cost/refine@k) — arXiv:2606.05632 · http://arxiv.org/abs/2606.05632
20. Cost-quality tradeoff of agentic Lean provers — arXiv:2606.04883 · http://arxiv.org/abs/2606.04883
21. Obfuscated Natural Number Game (architectural reasoning) — arXiv:2605.00677 · http://arxiv.org/abs/2605.00677
22. Inference-time diversity / mode collapse in Lean provers — arXiv:2601.16172 · http://arxiv.org/abs/2601.16172
23. Rewarding the Unlikely (GRPO rank bias) — arXiv:2506.02355 · http://arxiv.org/abs/2506.02355
24. Ineq-Comp compositional inequality benchmark — arXiv:2505.12680 · http://arxiv.org/abs/2505.12680
25. ProofBridge (NL theorem+proof → Lean) — arXiv:2510.15681 · http://arxiv.org/abs/2510.15681
26. The Network Structure of Mathlib — arXiv:2604.24797 · http://arxiv.org/abs/2604.24797
27. Growing Mathlib: maintenance at scale — arXiv:2508.21593 · http://arxiv.org/abs/2508.21593
28. The Lean mathematical library — arXiv:1910.09336 · http://arxiv.org/abs/1910.09336
29. CSLib: The Lean Computer Science Library — arXiv:2602.04846 · http://arxiv.org/abs/2602.04846
30. Computer Science as Infrastructure (CSLib spine) — arXiv:2602.15078 · http://arxiv.org/abs/2602.15078
31. OpenProver (agentic + interactive Lean 4) — arXiv:2607.09217 · http://arxiv.org/abs/2607.09217
32. MiniF2F in Rocq (cross-assistant translation) — arXiv:2503.04763 · http://arxiv.org/abs/2503.04763
33. Mathematical exploration and discovery at scale (AlphaEvolve) — arXiv:2511.02864 · http://arxiv.org/abs/2511.02864
34. mathlib statistics — https://leanprover-community.github.io/mathlib_stats.html
35. mathlib4 repository — https://github.com/leanprover-community/mathlib4
36. Archive of Formal Proofs statistics — https://www.isa-afp.org/statistics/
37. Kepler conjecture / Flyspeck — https://en.wikipedia.org/wiki/Kepler_conjecture
38. AlphaProof & AlphaGeometry 2 at IMO 2024 — https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/

**Leanstral 1.5 (verification of the brief's claim)**
39. Model card — https://huggingface.co/mistralai/Leanstral-1.5-119B-A6B
40. Base model — https://huggingface.co/mistralai/Leanstral-2603
41. Launch post with benchmark claims — https://mistral.ai/news/leanstral-1-5
42. Independent evaluation (MiaAI-Lab) — https://github.com/MiaAI-Lab/Leanstral-1.5-119B-A6B_Review

**Computer algebra**
43. Wester, *A Critique of the Mathematical Abilities of CA Systems* (1999) — https://www.math.unm.edu/~wester/cas_review.html and https://www.math.unm.edu/~wester/cas/book/Wester.pdf
44. SymPy Wester test suite (measured 2026-07-27) — https://raw.githubusercontent.com/sympy/sympy/master/sympy/utilities/tests/test_wester.py
45. SymPy polys Wester examples doc — https://github.com/sympy/sympy/blob/master/doc/src/modules/polys/wester.rst
46. Test-time scaling in theoretical physics / symbolic weak verifier (TPBench) — arXiv:2506.20729 · http://arxiv.org/abs/2506.20729

**Executable documents & reproducibility**
47. Pimentel, Murta, Braganholo, Freire — *A Large-scale Study about Quality and Reproducibility of Jupyter Notebooks*, MSR 2019 — https://leomurta.github.io/papers/pimentel2019a.pdf
48. Pimentel et al., *Reproducible Research is more than Publishing Research Artefacts* — arXiv:1905.00092 · http://arxiv.org/abs/1905.00092
49. Computational reproducibility of Jupyter notebooks from biomedical publications — arXiv:2308.07333 · http://arxiv.org/abs/2308.07333
50. Earlier version, same study — arXiv:2209.04308 · http://arxiv.org/abs/2209.04308
51. Containing the Reproducibility Gap (automated containerization) — arXiv:2604.01072 · http://arxiv.org/abs/2604.01072
52. Similarity-Based Assessment of Computational Reproducibility (SRI) — arXiv:2509.23645 · http://arxiv.org/abs/2509.23645
53. Restoring Execution Environments of Jupyter Notebooks — arXiv:2103.02959 · http://arxiv.org/abs/2103.02959
54. JunoBench (crashes in ML notebooks) — arXiv:2510.18013 · http://arxiv.org/abs/2510.18013
55. marimo repository — https://github.com/marimo-team/marimo
56. marimo FAQ — https://docs.marimo.io/faq/
57. marimo reactivity guide — https://docs.marimo.io/guides/reactivity/
58. JetBrains Datalore, 10M notebooks (the study marimo cites) — https://blog.jetbrains.com/datalore/2020/12/17/we-downloaded-10-000-000-jupyter-notebooks-from-github-this-is-what-we-learned/
59. Pluto.jl — https://plutojl.org/
60. Quarto code execution / freeze & cache — https://quarto.org/docs/projects/code-execution.html
61. Quarto execution options — https://quarto.org/docs/computations/execution-options.html
62. Observable notebooks documentation — https://observablehq.com/documentation/notebooks/

**Retrieval grounding & attribution**
63. Cited but Not Verified (deep-research citation audit) — arXiv:2605.06635 · http://arxiv.org/abs/2605.06635
64. AttributionBench — arXiv:2402.15089 · http://arxiv.org/abs/2402.15089
65. CAQA: Can LLMs Evaluate Complex Attribution in QA? — arXiv:2401.14640 · http://arxiv.org/abs/2401.14640
66. Attributed QA: evaluation and modeling — arXiv:2212.08037 · http://arxiv.org/abs/2212.08037
67. RAG for math QA: groundedness vs human preference — arXiv:2310.03184 · http://arxiv.org/abs/2310.03184
68. GenAI not ready for patient education, even with RAG — arXiv:2409.15260 · http://arxiv.org/abs/2409.15260

**Program-aided reasoning, dimensional analysis**
69. PAL: Program-aided Language Models — arXiv:2211.10435 · http://arxiv.org/abs/2211.10435
70. Program-Aided Reasoners (better) Know What They Know — arXiv:2311.09553 · http://arxiv.org/abs/2311.09553
71. Physical-type correctness in scientific Python (kind-of-quantity) — arXiv:1807.07643 · http://arxiv.org/abs/1807.07643
72. Dimensionally Consistent Learning with Buckingham Pi — arXiv:2202.04643 · http://arxiv.org/abs/2202.04643
73. A Dimensionally Consistent Size-Strain Plot Method (decades of dimensionally inconsistent published results) — arXiv:2512.00689 · http://arxiv.org/abs/2512.00689
74. Battling Botpoop (RAG chatbot deployment, satisfaction measure) — arXiv:2406.07796 · http://arxiv.org/abs/2406.07796

**Original measurements (this survey, 2026-07-27)**
- SymPy `master` vs the Wester suite: 397 tests, 152 failing (38.3%), 3 domains unimplemented. Reproduce from source 44.
- Grounding-ladder coverage/cost harness `ladder2.py`: 20 formulas, 37 equivalent rewrites, 113 mutants, 3 checkers, 170 timed checks. SymPy 1.14.0, pint 0.25.3, Python 3.12.

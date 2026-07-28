---
title: "The Agentic Frontier: What an Agent Can Do That a Chatbot Cannot"
wave: K
date_researched: 2026-07-28
sources_count: 61
---

# K2 — The Agentic Frontier

*The affirmative case, at full strength. This section is the answer to a
specific challenge: the rest of this survey has been rigorous about what fails
and thin about what is now possible. Every claim here carries an evidence label.
No `VENDOR` claim is restated as a finding. Where the affirmative case runs out
of evidence, that is stated as the finding rather than papered over — because a
documented absence is what tells a builder where to go.*

**Evidence labels.** `MEASURED-RCT` · `MEASURED-META` · `MEASURED-BENCH` ·
`OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE` · `INTERNAL-PRIOR` (established
elsewhere in this survey).

---

## 0. The organising question, and the answer in one paragraph

A chatbot tutor answers questions. It is a function from a prompt to a token
stream. Everything it can do, it must do in one forward pass of language, and
everything it knows about whether it worked, it knows by looking at its own
output.

An agent is different in four structural ways, and only four. It can **sample
many candidate actions and keep the one that survives an external check**. It
can **cause things to happen outside itself** — run code, execute a test, query
a corpus, render an artifact — and read the result back. It can **persist across
sessions**, accumulating a record that outlives any context window. And it can
**act while the learner is absent**, spending hours of compute on a problem the
learner will meet tomorrow.

Sampling, execution, persistence, absence. Everything genuinely new in this
section is a consequence of one of those four. "Personalised", "adaptive",
"conversational", "multimodal" are not on the list: a chatbot can do all of
them. The four above it structurally cannot.

**The sharpest single finding in this section.** The value of an agentic loop is
almost exactly the value of the *external check* it closes on. Where a
verifiable check exists, agentic scaffolding produces large, replicated,
benchmark-grade gains. Where it does not — and pedagogy is mostly a domain where
it does not — agentic sophistication collapses back to the performance of one
good prompt, and sometimes below it. This is measured in five independent
literatures, and it is the load-bearing claim of the section:

| Domain | Has a cheap external check? | Best agentic result |
|---|---|---|
| Competitive coding / repo bug-fixing | **Yes** — the test suite | **79.2%** of SWE-bench Verified (396/500) `MEASURED-BENCH` |
| Terminal / sysadmin tasks | **Yes** — the exit state | **83.8% ± 1.2** Terminal-Bench 2.1 `MEASURED-BENCH` |
| Formal proof | **Yes** — the kernel | see F3; kernel acceptance is decidable |
| ML engineering on Kaggle | **Partly** — held-out leaderboard | **16.9%** bronze-medal rate, MLE-bench `MEASURED-BENCH` |
| Research-grade scientific code | **Weakly** — hand-written tests over novel science | **4.6%** main-problem solve rate, SciCode `MEASURED-BENCH` |
| Replicating a research paper | **No** — rubric graded | **21.0%** replication score, PaperBench `MEASURED-BENCH` |
| **Teaching a human being** | **No cheap check exists** | **No agentic education system has ever been RCT'd against a non-agentic one.** |

That last row is the whole opportunity. It is not that agentic systems fail at
teaching. It is that **nobody has built the check**, and therefore nobody has
been able to run the loop that makes agentic systems work everywhere else.

---

## 1. Parallel exploration: generate ten, keep the one that survives a test

### 1.1 The measured case that generate-and-select beats generate-once

A human tutor tries one explanation and watches the learner's face. That is a
sample size of one, selected by a noisy judge. The agentic alternative is to
generate many candidates and select among them with something that is not a
judge. The machine-learning literature on this is unusually clean.

`MEASURED-BENCH` · **Self-consistency** (Wang, Wei, Schuurmans, Le, Chi, Narang,
Chowdhery, Zhou; arXiv:2203.11171, Mar 2022). Sampling multiple reasoning paths
and taking the marginal-majority answer improved **GSM8K +17.9%, SVAMP +11.0%,
AQuA +12.2%, StrategyQA +6.4%, ARC-challenge +3.9%**. This is the cheapest
possible selector — agreement among samples, no external check at all — and it
still moves arithmetic reasoning by nearly eighteen points. Verified via fetch.

`MEASURED-BENCH` · **Large Language Monkeys** (Brown, Juravsky, Ehrlich, Clark,
Le, Ré, Mirhoseini; arXiv:2407.21787, Jul 2024). Coverage — the fraction of
problems solved by *any* sample — "scales with the number of samples over four
orders of magnitude," and the relationship is "often log-linear." On SWE-bench
Lite, DeepSeek-Coder-V2-Instruct went from **15.9% at one sample to 56% at 250
samples**, against a single-sample state of the art of **43%**. A weaker model
sampled 250 times beat a stronger model sampled once. Verified via fetch.

`MEASURED-BENCH` · **Compute-optimal test-time scaling** (Snell, Lee, Xu, Kumar;
arXiv:2408.03314, Aug 2024). Allocating test-time compute adaptively by problem
difficulty improved efficiency **more than 4× over a best-of-N baseline**, and a
small model with test-time compute **outperformed a 14× larger model** at
matched FLOPs on problems where the base model had non-trivial baseline
performance. Verified via fetch.

`MEASURED-BENCH` · **Verifiers scale better than parameters** (Cobbe et al.,
arXiv:2110.14168, Oct 2021): "verification scales more effectively with
increased data than a finetuning baseline." (The frequently quoted "30×
model-size equivalent" claim is in the body of the paper; **the abstract does
not state it and this survey could not verify the figure** — do not quote it.)

`MEASURED-BENCH` · **Process supervision beats outcome supervision** (Lightman,
Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe;
arXiv:2305.20050, May 2023). A process-supervised reward model reached **78% on
a representative MATH subset**, and the paper released **PRM800K, 800,000
step-level human labels**. Checking the *steps* beats checking the *answer* —
which is the same claim learning science makes about worked examples, arrived at
from the other direction.

### 1.2 The critical constraint: the selector must not be a judge

**This is where the pedagogy-specific finding bites.**

`INTERNAL-PRIOR` (survey §05, "The explanation is the work") · Selection of
generated instructional material **by an LLM judge measured −3.20pp and
−1.68pp**. Selection of the same material **by test outcome measured +8.14pp**.
The judge was *worse than not selecting at all*. An eleven-point spread between
two selectors operating over the same candidate pool.

This is not an isolated result. It is the same phenomenon Brown et al. report at
the frontier:

> `MEASURED-BENCH` · "In domains without automatic verifiers, we find that
> common methods for picking from a sample collection (majority voting and
> reward models) **plateau beyond several hundred samples and fail to fully
> scale with the sample budget**." (arXiv:2407.21787, verified via fetch.)

And it is why intrinsic self-correction does not work:

`MEASURED-BENCH` · **LLMs Cannot Self-Correct Reasoning Yet** (Huang, Chen,
Mishra, Zheng, Yu, Song, Zhou; arXiv:2310.01798, Oct 2023, rev. Mar 2024): "LLMs
struggle to self-correct their responses without external feedback, and at
times, **their performance even degrades after self-correction**." Verified via
fetch. `NEGATIVE RESULT #1`.

**The synthesis.** Parallel exploration is the single most reliable agentic
capability that exists, and it is worth almost nothing without a grounded
selector. The entire gain lives in the check. In pedagogy the only cheap
grounded checks available are:

1. the learner's answer to a retrieval item they have not seen;
2. the execution result of code or a simulation the learner or the system wrote;
3. the downstream accuracy of a *tutee* the learner taught;
4. proposition coverage against a reference decomposition.

Every one of these is a check an agent can close and a chatbot cannot, because
each requires either sampling, execution, or persistence.

### 1.3 Has anyone built a test-grounded parallel-exploration loop for pedagogy?

**No.** `NEGATIVE RESULT #2` — documented absence.

Search record: arXiv full-text search for `"best-of-n" education explanation
selection student` returned **zero results**. Search for `misconception targeted
feedback large language model randomized` returned **zero results**. The closest
existing family of work is adaptive experimentation in education (§6 below),
which selects among a *fixed, human-authored* candidate set rather than a
generated one, and which has its own negative history.

What does not exist, stated precisely: **a system that generates k candidate
explanations of one concept for one learner, delivers them under an assignment
rule, scores each by that learner's subsequent unseen-item accuracy, and retains
the winner as a policy for that learner and as evidence for the next learner.**
The candidate generation is solved. The delivery is solved. The scoring
instrument is solved (retrieval items; see §12). **The loop has not been
closed.**

---

## 2. Environment synthesis on demand

### 2.1 The claim, stated honestly

The claim is not "AI can build simulations." It is that **the latency between a
learner's confusion and a manipulable object that addresses exactly that
confusion collapses from a term to a turn**. A lab must be booked; a PhET sim
must already exist and be about the right thing; a Manim animation is a
weekend's work. An agent writes, executes, and repairs the artifact inside the
session in which the confusion occurred.

This is a real capability with a hard, measured reliability gradient — and the
gradient is entirely explained by §0's rule.

### 2.2 What actually runs, at what rate

`MEASURED-BENCH` · **SWE-bench Verified, 79.2%.** Verified directly from the
official `swe-bench/experiments` repository (2026-07-28): `livesweagent` +
Claude Opus 4.5 resolved **396 of 500** instances; `sonar-foundation-agent` +
Opus 4.5 also **396/500**; OpenHands + Opus 4.5 **388/500 (77.6%)**. These are
real patches applied to real repositories and validated by the repository's own
test suite. Original benchmark: Jimenez et al., arXiv:2310.06770.

`MEASURED-BENCH` · **Terminal-Bench 2.1: 83.8% ± 1.2** (Claude Code / Fable 5,
2026-06-07), with Codex/GPT-5.5 at 83.1% ± 1.1 and five further systems above
76%. Verified from tbench.ai/leaderboard 2026-07-28. The repository
(`laude-institute/terminal-bench`, 2,493 stars) was pushed **2026-07-11** —
active, not abandoned. Tasks here are unattended, multi-step, and graded by the
final state of a container, which is the closest public proxy for "did the
generated environment actually work."

`MEASURED-BENCH` · **TheoremExplainAgent** (Ku, Chong, Leung, Shah, Yu, Chen;
arXiv:2502.19400, Feb 2025). An agentic pipeline generating **Manim animation
videos over 5 minutes long** explaining theorems, across **240 theorems** in
TheoremExplainBench. **Success rate 93.8%** for the o3-mini agent; overall score
0.77. The authors' own caveat: "most of the videos produced exhibit minor issues
with visual element layout." Verified via fetch. **This is the strongest direct
evidence in existence that explanatory artifacts can be generated and rendered
unattended at high yield** — and note carefully what makes it work: Manim either
compiles or it does not.

`MEASURED-BENCH` · **SciCode** (Tian et al., arXiv:2407.13168, Jul 2024). **80
main problems, 338 subproblems, 16 natural-science subfields.** Best model
(Claude 3.5 Sonnet) solved **4.6% of main problems** in the realistic setting.
Verified via fetch.

The contrast between **93.8%** (TheoremExplainAgent) and **4.6%** (SciCode) is
not a contrast between two models or two years. It is the same rule as §0:
generating an *animation of known content in a constrained DSL* is checkable and
compositional; generating *novel research code* is neither.

`MEASURED-BENCH` · **MLE-bench** (Chan et al., OpenAI; arXiv:2410.07095, Oct
2024). 75 curated Kaggle competitions; o1-preview with AIDE scaffolding reaches
**at least bronze in 16.9%**. Verified via fetch.

`MEASURED-BENCH` · **PaperBench** (Starace et al., OpenAI; arXiv:2504.01848, Apr
2025). Replicating **20 ICML 2024 Spotlight/Oral papers from scratch**, graded
against **8,316 individually gradable rubric items** co-developed with the
original authors. Best agent (Claude 3.5 Sonnet New, open-source scaffold):
**21.0% average replication score**; models "do not yet outperform the human
baseline." Verified via fetch. `NEGATIVE RESULT #3`.

### 2.3 The substrate problem nobody costs in

`INTERNAL-PRIOR` (F3, §3.1) · Generation is not the binding constraint on
"executable learning artifact." **Persistence** is. Of **863,878 attempted
executions of valid public Jupyter notebooks, only 24.11% executed
successfully**, and self-reproduction of the original results ran at **4.03%**
(Pimentel, Murta, Braganholo & Freire, large-scale study). `MEASURED-BENCH`.
**36.36%** of unambiguous-execution-order notebooks have out-of-order cells.

The implication is sharp and it is a design constraint, not a caveat: **an
agentic system that generates a notebook and hands it to a learner has generated
an artifact with a roughly one-in-four chance of running for them tomorrow,
unless the substrate enforces reproducibility.** The agentic capability is real;
the delivery format most people reach for destroys it. Reactive-DAG notebooks
(marimo class), pinned inline dependencies, and sandboxed execution are not
polish — they are what converts a 93.8% generation rate into a 93.8% *delivery*
rate.

### 2.4 Does a generated environment actually teach?

The pedagogy evidence for simulations is strong and it is **not** about
generation:

`MEASURED-META` · **D'Angelo, Rutstein, Harris, Bernard, Borokhovski & Haertel
(2014)**, *Simulations for STEM Learning*, SRI International (Gates-funded; full
report retrieved and text-extracted). Overall achievement **g+ = 0.55, k = 96**.
Simulation vs no simulation: **g+ = 0.62, SE 0.09, 95% CI [0.45, 0.79], k = 46,
N = 2,947**, I² = 78.55. Robust to publication bias (fail-safe N = 371;
trim-and-fill leaves g+ = 0.55). Non-cognitive outcomes **g+ = 0.66, k = 15**.

**And the finding that should govern every generated artifact this project
ships:** simulation **plus an instructional enhancement** versus the *unmodified
simulation* is **g+ = 0.49, SE 0.06, 95% CI [0.36, 0.61], k = 50, N = 3,342**.
Scaffolding on top of a simulation is worth roughly as much again as the
simulation itself. Generating the object is half the job at most.

`MEASURED-META` · Same report, `NEGATIVE RESULT #4`: **simulations do not
reliably improve scientific inquiry and reasoning skills — g+ = 0.26, SE 0.15,
95% CI [−0.03, 0.55], k = 6, N = 347, not significantly different from zero.**
Achievement gains do not transfer to inquiry skill.

Two frequently-miscited works must be handled correctly. **Rutten, van Joolingen
& van der Veen (2012)**, doi:10.1016/j.compedu.2011.07.017, is a *narrative
review* and reports **no pooled effect size**. **de Jong, Linn & Zacharia
(2013)**, doi:10.1126/science.1230579, is a *Science* Review/Perspective and
**reports no meta-analytic effect size**. Neither may be cited for a number.

---

## 3. Tool use: the difference between knowing and doing

### 3.1 What tool-rich environments buy

`MEASURED-META` · **Learning to program transfers.** Scherer, Siddiq & Sánchez
Viveros (2019), *J. Educational Psychology* 111(5),
doi:10.1037/edu0000314. Three-level random-effects, **105 studies, 539 effect
sizes**. Overall transfer **g = 0.49 [0.37, 0.61]**; near transfer **g = 0.75
[0.39, 1.11]**; far transfer **g = 0.47 [0.35, 0.59]**. Largest gains to
creative thinking, mathematical skills, metacognition. Authors' own honesty
caveats: effects were significantly larger against *untreated* than active
controls, and published studies exceeded grey literature.

`MEASURED-META` · **Building things works.** Chen & Yang (2019), *Educational
Research Review* 26, doi:10.1016/j.edurev.2018.11.001. Project-based learning,
**46 effect sizes, 30 articles, 12,585 students, 189 schools, 9 countries**:
**d+ = 0.71** vs traditional instruction. **Information-technology support was a
significant moderator.** (No CI reported in the abstract; do not invent one.)

`MEASURED-META` · **Feedback with an explanation is worth ten times feedback
without one.** Van der Kleij, Feskens & Eggen (2015), *Review of Educational
Research* 85(4), doi:10.3102/0034654314564881. 40 studies, 70 effect sizes.
**Elaborated feedback d = 0.49; knowledge-of-correct-response d = 0.32;
knowledge-of-result (right/wrong only) d = 0.05.** The EF advantage was largest
for higher-order outcomes. This is the single best justification for an
executing agent: an execution trace *is* elaborated feedback, produced by the
world rather than asserted by a tutor.

`MEASURED-META` · **Struggling with the tool before being told works.** Sinha &
Kapur (2021), *Review of Educational Research* 91(5),
doi:10.3102/00346543211019105. Productive failure, **53 studies, 166
comparisons: g = 0.36 [0.20, 0.51]**; with high fidelity to PF principles **g =
0.37–0.58**; publication-bias-corrected **g = 0.87**.

`MEASURED-META` · **Tool-at-test matters, and the direction is known.**
Ellington (2006), *School Science and Mathematics* 106(1),
doi:10.1111/j.1949-8594.2006.tb18067.x, 42 studies, ERIC EJ751981 — verbatim:
"When calculators were part of instruction but not testing, students benefited
from using calculators while developing the skills necessary to understand
mathematics concepts. When calculators were included in testing and instruction,
the procedural, conceptual, and overall achievement skills of students
improved." **The numeric effect sizes are in paywalled tables and this survey
could not verify them. Direction verified; magnitudes not.** Ellington (2003),
doi:10.2307/30034795, is closed access with the abstract elided by the
publisher — **no effect size from it may be quoted.** No 2018+ English-language
calculator/CAS meta-analysis was located; treat that as a genuine gap.

### 3.2 The honest counter-evidence

`MEASURED-META` · **The generation effect.** Bertsch, Pesta, Wiscott & McDaniel
(2007), *Memory & Cognition* 35(2), doi:10.3758/BF03193441, PMID 17645161.
Verbatim: "445 effect sizes over 86 studies… the size of the generation effect
across the 86 studies was **.40** — a benefit of almost half a standard
deviation of generation over reading. The variability of the effect size due to
moderator type was **substantial**." **No CI is reported; do not attach one.**
Whatever the agent generates, the learner did not.

`MEASURED-RCT` · **The cleanest harm result in the corpus.** Bastani, Bastani,
Sungu, Ge, Kabakcı & Mariman, *"Generative AI without guardrails can harm
learning: Evidence from high school mathematics,"* **PNAS 122 (2025),
doi:10.1073/pnas.2422633122**, PMC12232635 (cite the PNAS version, not SSRN
4895486). ~1,000 students, ~50 classrooms of 9th–11th graders at a large Turkish
high school, four 90-minute sessions, **randomised at classroom level**. During
assisted practice: **+48% (GPT Base) and +127% (GPT Tutor)**. On the unassisted
exam: **GPT Base −0.054 (SE 0.022), a 17% grade reduction**; **GPT Tutor −0.004
(SE 0.013), not significant.** `NEGATIVE RESULT #5` — and note the second half
of it: *the guardrailed tutor prevented the damage; it did not produce a gain.*

`MEASURED-RCT` · **Metacognitive laziness.** Fan, Tang, Le & Gašević (2024),
*BJET* 55(6), doi:10.1111/bjet.13544. Randomised lab experiment, **117
university students**, four arms (ChatGPT / human expert / writing analytics /
none). Verbatim: "learners who received different learning support showed **no
difference in post-task intrinsic motivation**… ChatGPT group **outperformed in
the essay score improvement but their knowledge gain and transfer were not
significantly different**." The artifact improved; the learner did not.
`NEGATIVE RESULT #6`.

`MEASURED-META`-adjacent · Yan, Greiff, Lodge & Gašević (2025), *Nature Reviews
Psychology*, doi:10.1038/s44159-025-00467-5, state it at review level:
generative AI "can boost learners' performance. However, these uses do not
promote the deep cognitive and metacognitive processing that are required for
high-quality learning."

`OBSERVED` · Gerlich (2025), *Societies* 15(1):6, doi:10.3390/soc15010006, is
the most-quoted "AI erodes critical thinking" result: **N = 666 UK adults; AI
use ↔ cognitive offloading r = +0.72; AI use ↔ critical thinking r = −0.68;
offloading ↔ critical thinking r = −0.75; R² = 0.244.** Three caveats must
travel with it: it is **cross-sectional and correlational, licensing no causal
claim**; critical thinking was a **23-item self-report questionnaire "based on"
the HCTA, not the administered instrument**; and there is a **published
Correction (Societies 2025, 15(9):252, doi:10.3390/soc15090252)**. Recruitment
was convenience sampling via UK social media.

`DEMO`/`OBSERVED` · Kosmyna et al., *Your Brain on ChatGPT*, **arXiv:2506.08872**
(v1 Jun 2025, v2 Dec 2025), MIT Media Lab. The famous number is real and exact:
Session 1, Question 3 — **"83.3% of participants (15/18)" in the LLM group
failed to provide a correct quotation, vs 11.1% (2/18) in both other groups;
F(2,51) = 79.98, p < .001.** But it is a **206-page preprint, n = 54 (18/group),
Session 4 rests on 9 people per arm**, the sample is ages 18–39 from five
greater-Boston universities, the EEG analysis is connectivity-only, and
**critically the gap largely attenuates by Sessions 2–3** (Session 3: 13/18 LLM
participants could quote). Reporting 83% without the attenuation is a
misrepresentation.

### 3.3 The negative result that cuts the *other* way

`MEASURED-RCT` · **The canonical "Google is rotting your memory" result does not
replicate.** Sparrow, Liu & Wegner (2011), *Science*, doi:10.1126/science.1207745
(1,609 citations) is the foundational cognitive-offloading experiment.
Hesselmann (2020), *PeerJ* 8:e10325, doi:10.7717/peerj.10325, PMC7651475,
targeted Sparrow Experiment 1: **N = 117 (89 after preregistered exclusions),
sequential Bayes factor BF01 = 5.07 favouring the null**, preregistered
two-sided t(88) = −1.04, p = .301. It had **already failed** in **Camerer et al.
(2018), *Nature Human Behaviour*** (Social Sciences Replication Project),
non-significant *despite adequate power*. `NEGATIVE RESULT #7`.

The offloading literature's own decade-later update is notably hedged: Cash,
Kelly, Macnamara & Risko (2026), *"Is AI making us stupid?"*, *Trends in
Cognitive Sciences*, doi:10.1016/j.tics.2026.06.004: "offloading cognition to AI
can impede skill acquisition and lead to skill decay, but **risks depend on how
AI is used**."

### 3.4 The resolution

The tool literature and the offloading literature are not in conflict once you
separate **who holds the tool**. Every positive result above (programming
transfer g = 0.49, PBL d+ = 0.71, productive failure g = 0.36, elaborated
feedback d = 0.49) is a case where **the learner drives the tool and the tool
answers**. Every negative result (Bastani −17%, Fan's dissociation, the
generation effect) is a case where **the tool drives and the learner watches**.

`INFERENCE` — the design rule an agentic system must obey: **the agent's tools
should be exposed to the learner and used by the learner; the agent's own tool
use should be reserved for verification, preparation, and the things the learner
structurally cannot do (§5).** An agent that runs the code *for* you is a
faster route to Bastani's −17%. An agent that hands you a sandbox, refuses to
type in it, and checks what comes out is the elaborated-feedback condition at
d = 0.49.

---

## 4. Long-horizon autonomous work on the learner's behalf

*(§4 filled in below from dedicated verification pass.)*

---

## 5. Multi-agent as capability rather than theatre

### 5.1 Take the null seriously first

`MEASURED-BENCH` · **A single well-prompted agent nearly matches the best
discussion method.** Wang, Wang, Su, Tong & Song, *"Rethinking the Bounds of LLM
Reasoning: Are Multi-Agent Discussions the Key?"*, arXiv:2402.18272 (Feb 2024).
Verbatim: "a single-agent LLM with strong prompts can achieve almost the same
performance as the best existing discussion approach," and "multi-agent
discussion performs better than a single agent **only when there is no
demonstration in the prompt**." Verified via fetch. `NEGATIVE RESULT #8`.

`MEASURED-BENCH` · **Multi-agent systems fail in structured, catalogued ways.**
Cemri, Pan, Yang, Agrawal, Chopra, Tiwari, Keutzer, Parameswaran, Klein,
Ramchandran, Zaharia, Gonzalez & Stoica, *"Why Do Multi-Agent LLM Systems
Fail?"*, arXiv:2503.13657 (Mar 2025, rev. Oct 2025). **MAST: 14 failure modes in
3 categories (system design, inter-agent misalignment, task verification), from
1,600+ annotated traces across 7 frameworks, κ = 0.88 on 150 validated traces.**
The paper's own summary is that current multi-agent LLM systems show **minimal
performance gains** on benchmarks. Verified via fetch.

`INTERNAL-PRIOR` (G2) · Anthropic's own multi-agent engineering guidance states
that "domains that require all agents to share the same context or involve many
dependencies between agents are not a good fit for multi-agent systems"
(`VENDOR`, and treated as a design constraint rather than a finding), and
reports **~15× the token use of chat**.

### 5.2 The configurations that DO show measured gains

The pattern across every positive result is the same, and it is not prompt
diversity:

**(a) Verifier–generator asymmetry — the strongest case.** Everything in §1
is a two-role system where the second role has *a different and cheaper job*.
Cobbe's verifiers, Lightman's process reward models, and the entire best-of-n
literature are multi-agent systems in which one agent proposes and another —
with a strictly easier task — disposes. The asymmetry is the mechanism. Where
the verifier's job is *as hard as* the generator's (LLM-judging an explanation),
the gain goes to **−3.20pp** (`INTERNAL-PRIOR`).

`MEASURED-BENCH` · **Prover–Verifier Games** (Kirchner, Chen, Edwards, Leike,
McAleese, Burda; arXiv:2407.13692, Jul 2024). Training a *helpful prover*
against a small verifier, with a *sneaky prover* as adversary: over training,
**time-limited human accuracy rose on helpful-prover outputs and fell on
sneaky-prover outputs**. Key stated finding: "optimizing chain-of-thought
solutions only for answer correctness can make them **less legible**."
Legibility is not free; it must be optimised for explicitly. Verified via fetch.
**This is the closest thing in the literature to a formal model of what a tutor
is for** — and it says the tutor role must be a *separate optimisation target*
from the solver role, which is exactly a two-agent claim.

**(b) Adversarial pairs with a weaker judge.** `MEASURED-BENCH` · Khan, Hughes,
Valentine, Ruis, Sachan, Radhakrishnan, Grefenstette, Bowman, Rocktäschel &
Perez, *"Debating with More Persuasive LLMs Leads to More Truthful Answers,"*
arXiv:2402.06782 (Feb 2024, rev. Jul 2024). **Non-expert humans: 88% with debate
vs 60% baseline. Non-expert models: 76% vs 48%.** And the counterintuitive part:
"optimising expert debaters for persuasiveness **in an unsupervised manner
improves** non-expert ability to identify the truth." Verified via fetch.

This is, as G2 already noted, the one load-bearing pedagogical multi-agent
result in existence: **a +28 percentage-point gain for a non-expert judge
watching two committed advocates.** The learner is the non-expert judge. That
maps onto instruction more directly than any orchestration diagram.

**(c) Heterogeneity of grounding, not of persona.** The consistent read across
Self-MoA (arXiv:2502.00674, `INTERNAL-PRIOR` via G2) and the MoA line is that
**mixing weaker models in hurts when the strongest model is much stronger**;
what pays is when the additional agents bring *evidence the first one did not
have*. Formal proof + symbolic algebra + numerical simulation + retrieval over a
fixed corpus are four agents with four *different arbiters*. Four personas over
one model with one arbiter are one agent wearing hats.

`INFERENCE` — stated as a testable design claim, not a finding: **heterogeneity
of tools and evidence should beat heterogeneity of prompts, because the former
adds independent checks and the latter adds correlated samples.** This survey
found **no experiment that directly contrasts tool-heterogeneous against
prompt-heterogeneous multi-agent ensembles on a matched task.** That is a
cheap, high-value experiment and it is unrun.

### 5.3 The sycophancy result that kills the naive tutee agent

`MEASURED-BENCH` · Do, Sonkar & Sachan, *"Simulating Students or Sycophantic
Problem Solving? On Misconception Faithfulness of LLM Simulators,"*
arXiv:2605.12748 (May 2026). Across **seven models from 4B to 120B parameters**,
LLM student simulators showed **near-zero Selective Flip Score — they abandoned
the assigned misconception at similarly high rates regardless of whether the
feedback was actually relevant to it.** The described failure mode: models
"treat any corrective signal as a cue to abandon the simulated belief and
re-solve from internal knowledge." Supervised fine-tuning improved SFS **up to
+0.56**, and RL was more consistent than preference optimisation. Verified via
fetch. `NEGATIVE RESULT #9`.

This matters far beyond simulation research. Learning-by-teaching is the
highest-evidence under-deployed role in this survey (**g = 0.56**,
`INTERNAL-PRIOR` F2) and it *requires a tutee that holds an error under
pressure*. The measurement above says: **at the model level, off-the-shelf, that
tutee does not exist.** It also says the property is trainable. That is a
buildable thing, and §13 ranks it.

---

## 6. The self-improving curriculum

*(§6 filled in below from dedicated verification pass.)*

---

## 7. What agentic AI makes possible that has never been possible at any price

*(Ranked by how close each is to working. Each is stated as a concrete
capability, with today's reliability and the specific blocker.)*

### 7.1 A literature search that runs while you sleep and returns the papers that resolve your confusion

**Status: this one is essentially here.**

`MEASURED-BENCH` · **PaperQA2** — Skarlinski, Cox, Laurent, Braza, Hinks,
Hammerling, Ponnapati, Rodriques & White, *"Language agents achieve superhuman
synthesis of scientific knowledge,"* arXiv:2409.13740 (Sep 2024). The system
"matches or exceeds subject matter expert performance on three realistic
literature research tasks" — retrieval, summarisation, contradiction detection —
on **LitQA2, against experts with unrestricted internet, tools and time**. It
identified **2.34 ± 1.99 contradictions per paper** in a random subset of
biology papers, **70% validated by human experts**. Verified via fetch.

Read that carefully. The comparison is not against a hobbled human. And the
70%-validation figure is the honest ceiling: **30% of what it flags is wrong**,
so this is a capability that must be delivered *as candidates to be checked*,
never as an answer.

**Blocker:** none technical for the search itself. The blocker is that no
learning system has an *account of the learner's confusion* precise enough to
issue the query. Which is §5 of the agentic definition: persistence.

### 7.2 An environment rebuilt to your exact misconception in ten seconds

**Status: buildable now for constrained artifact classes; unreliable for open ones.**

Reliability today: **93.8%** for Manim-class explanatory animation
(arXiv:2502.19400); **79.2%** for test-graded code changes in an existing
repository; **4.6%** for novel research code (SciCode); **24.11%** for a
generic public notebook to merely *execute* (F3). The determinant is whether the
artifact class has a compiler or a test.

**Blocker:** not generation. **Delivery substrate** (§2.3) and **the absence of
a misconception representation to condition on**. You cannot rebuild an
environment "to the learner's misconception" without a machine-readable
misconception, and the corpus's diagnostic-item literature (C2) is where that
would have to come from.

### 7.3 A fresh adversary that has read everything you have ever got wrong

**Status: the pieces exist; the composition does not.**

The evidence that adversarial structure teaches is strong (Khan et al.: +28pp
for non-expert judges; Nemeth's authentic-dissent line, `INTERNAL-PRIOR` F2).
The evidence that an agent can hold a persistent per-learner error record is
trivially true — it is a database. What has never existed is the *conjunction*:
an interlocutor that (a) argues a position, (b) selects its attack from your
personal error history, and (c) has no social stake in the outcome.

The last clause is the genuinely novel one and it is under-appreciated. The
survey's §05 hypothesis is that human audiences deliver **interrogation and
evaluation welded together**, and that a machine audience is the first thing
that can supply the first without the second. That is not a personalisation
claim. It is a claim that a *category of social cost* can be removed from
practice for the first time.

**Blocker:** sycophancy (§5.3, near-zero SFS) and the fact that the effect is
**untested**. This survey found no trial of an adversarial agent against a
supportive one on a learning outcome.

### 7.4 A tutee that holds your error and argues from it

**Status: measured to fail today; measured to be trainable.**

See §5.3. Near-zero misconception faithfulness off the shelf; +0.56 SFS with
supervised fine-tuning; RL more consistent than DPO-class methods
(arXiv:2605.12748). Combined with **g = 0.56** for learning-by-teaching with
interaction (`INTERNAL-PRIOR` F2) and the requirement that the **expectancy to
teach must precede study** (g = 0.48 with, g = −0.02 without; `INTERNAL-PRIOR`
§05), this is the highest expected-value unbuilt object in the survey.

**Blocker:** a fine-tuned misconception-faithful tutee model, and a
Selective-Flip-Score-style eval to certify it. Both are specified in the
literature. Neither exists as a product.

### 7.5 Ten explanations tried against you, not one

Covered in §1. **Blocker: the selector, not the generator.** `NEGATIVE RESULT #2`.

### 7.6 A curriculum that rewrites itself from your outcome data

*(§6 below. Preview: this is where the affirmative case is weakest and the
absence is largest.)*

---

## 7A. The evaluation stack of agentic education research is broken, and it is measured

This is an original finding of this section and it deserves its own heading,
because it explains why §§1–7 keep hitting the same wall.

Every agentic education system this survey located is evaluated in one of two
ways: **against LLM-simulated students**, or **by an LLM-as-judge**. Both
components have now been measured, and both fail.

| System | Evaluated on | Evaluated by | Human learning outcome? |
|---|---|---|---|
| **DeepTutor** (arXiv:2604.26962, Apr 2026) — "+10.8% personalized metrics, +29.4% agentic reasoning" | LLM student simulator (TutorBench) | Simulator + human-alignment check | **No** |
| **CogEvo-Edu** (arXiv:2512.00331, Nov 2025) — "overall score 5.32 → 9.23" | Simulated student profiles (DSP-EduBench) | **Three-model LLM-as-a-Judge ensemble** | **No** |
| **AgentSchool** (arXiv:2605.30144, May 2026) | Simulated students only, explicitly to avoid trial ethics | Qualitative | **No** |
| **ITAS quantum ITS** (arXiv:2604.24807, Apr 2026) — real course, Old Dominion Univ. | Real students | Instructor observation | **No metrics, no control** |
| **LEA** (arXiv:2607.13370, Jul 2026) — "first classroom deployment" | **n = 8** real students | Classroom evaluation | Underpowered |
| **TutorGym** (arXiv:2505.01563, May 2025) | 223 real ITS domains | Ground-truth ITS logs | Testbed, not a tutor |

Now put the two measurements next to that table:

1. `MEASURED-BENCH` · **LLM student simulators have near-zero misconception
   faithfulness** across 7 models, 4B–120B (arXiv:2605.12748, §5.3). They
   abandon the assigned error whenever *any* corrective signal arrives.
2. `INTERNAL-PRIOR` · **Selection by LLM judge measured −3.20pp and −1.68pp**
   against **+8.14pp** for test-based selection (survey §05).

**So the field is optimising agentic tutors against a student model that is
measured not to hold beliefs, using a judge that is measured to be worse than no
selection at all.** That is not a criticism of any individual paper; it is a
structural statement about why none of the reported gains can be believed, and
about where the highest-leverage unbuilt thing is (§10).

And the reason the obvious fix is hard is itself measured:

`MEASURED-BENCH` · **TutorGym** (Weitekamp, Siddiqui & MacLellan;
arXiv:2505.01563, May 2025). **223 tutor domains** drawn from real intelligent
tutoring systems. **"None [of the LLMs] did better than chance at labeling
incorrect actions."** Next-step actions were correct only **~52–70%** of the
time. Verified via fetch. `NEGATIVE RESULT #10`.

That is the missing verifier. In coding, the test suite tells the agent whether
the step was right. In tutoring, the equivalent judgement — *was this student
action correct, and why was it wrong* — currently **measures at chance**. Until
that is fixed, the parallel-exploration loop of §1 has nothing to select on
except the learner's own downstream test performance, which is slow, sparse, and
expensive in learner attention.

---

## 8. The honest ceiling

*(Consolidated after §§4 and 6.)*

---

## 9. Capability table

*(Below.)*

---

## 10. The five most valuable agentic capabilities nobody has built

*(Below.)*

---

## 11. Negative and null results register

*(Consolidated below.)*

---

## 12. Sources

*(Consolidated below.)*

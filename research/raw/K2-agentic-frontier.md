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

### 4.1 The capability, stated concretely

Between Tuesday's session and Wednesday's, an agent can: mine the learner's
entire error history for a pattern no human would spot across months; build
tomorrow's problem set and *test it against a student model* before the learner
sees it; run a literature search and return three candidate papers; pre-compute
and debug the simulation so it opens instantly. None of these requires the
learner to be present. **A chatbot has no state in which the learner is absent.**

This is the agentic property with the clearest measured trajectory, and the
clearest measured wall.

### 4.2 How long an agent can work unsupervised — the numbers

`MEASURED-BENCH` · **METR time horizons.** Kwa, West et al., arXiv:2503.14499
(v1 Mar 2025; current v4 Jul 2026; NeurIPS 2025). **Note the title changed** from
"Measuring AI Ability to Complete Long Tasks" to "…Long **Software** Tasks" —
cite the current one. The paper's headline: Claude 3.7 Sonnet 50%-success time
horizon **~50 minutes**, with the horizon **doubling roughly every 7 months
since 2019**.

METR's own live data supersedes the paper. From
`metr.org/assets/benchmark_results_1_1.yaml` (benchmark `METR-Horizon-v1.1`,
site updated 2026-05-08; **228 tasks**, up from 170; 31 tasks of 8h+):

| Model | Release | 50% horizon | **80% horizon** |
|---|---|---|---|
| GPT-4 | 2023-03 | 3.99 min | 0.89 min |
| GPT-4o | 2024-05 | 6.99 min | 1.27 min |
| o1 | 2024-12 | 38.8 min | 7.1 min |
| Claude 3.7 Sonnet | 2025-02 | 60.4 min | 12.1 min |
| o3 | 2025-04 | 119.7 min | 30.0 min |
| GPT-5 | 2025-08 | 203.0 min | 38.3 min |
| Claude Opus 4.5 | 2025-11 | 293.0 min | 49.4 min |
| Claude Opus 4.6 | 2026-02 | 718.8 min | 69.9 min |
| Gemini 3.1 Pro | 2026-02 | 384.2 min | 89.8 min |

Doubling times in the current data: **187.8 days all-time; 128.7 days since 2023
(CI 104.4–158.0)**. METR states measurements above 16 h are unreliable with the
current suite.

**The single most important row for a builder is the gap between the two
columns.** The 80%-success horizon runs **4–10× shorter** than the 50%-success
horizon. At Claude Opus 4.6: **~12 hours at coin-flip reliability, ~70 minutes
at 80%.** Any pedagogical claim of the form "the agent works overnight on your
learning" is, at today's frontier, a claim about a **~1-hour reliable unit of
work**, repeated with checkpoints — not a claim about an eight-hour autonomous
shift.

`OBSERVED` · **Domain matters enormously.** METR's own cross-domain analysis
(metr.org, 2025-07-14) finds software/reasoning horizons of 50–200+ minutes
doubling every 2–6 months, while **agentic computer use (OSWorld, WebArena)
shows horizons 40–100× shorter**, roughly two years behind. Labelled `OBSERVED`
rather than `MEASURED-BENCH` because these horizons are derived from third-party
benchmarks, not METR's own timed task suite.

### 4.3 Error compounding: the formal result, and why it cuts both ways

`MEASURED-BENCH` · **The Illusion of Diminishing Returns: Measuring Long Horizon
Execution in LLMs.** Sinha, Arun, Goel, Staab, Geiping; arXiv:2509.09677 (Sep
2025, ICLR 2026). This is the substantive formal treatment and it makes the
affirmative case *harder* than the naive pessimism:

- Horizon length **H_s(p) = ln(s)/ln(p)** — the number of steps completable at
  success rate *s* given per-step accuracy *p* — grows **hyperbolically** in
  *p*, with sharp growth **beyond 80% single-step accuracy**. A fixed increment
  in step accuracy buys an ever-larger increment in task length.
- This **reconciles** with METR: sustaining a 7-month doubling of the 50%
  horizon requires step accuracy improving as 2^(−1/2t), which is itself a
  *diminishing* function. **Exponential horizon growth is compatible with
  diminishing per-step returns.**
- Measured single-turn execution length: **GPT-5 2,176 steps; Claude-4 Sonnet
  432; Grok 4 384; Gemini 2.5 Pro 120.**
- **Self-conditioning is the real failure mode.** Models become *more* likely to
  err when their own earlier errors are in context; per-step accuracy degrades
  as step count grows, and this is **not** explained by long-context limits
  alone. **Scaling model size does not fix it**; sequential test-time compute
  ("thinking") does mitigate it.
- Central framing: failures on lengthened *simple* tasks are **execution**
  failures, not reasoning failures.

`INFERENCE` · The pedagogical translation is direct and it is a design rule.
Self-conditioning means **an agent that makes an error about a learner early in
a long autonomous run becomes more likely to make further errors conditioned on
it.** An agent mining a learner's error history for two hours, unchecked, is
running exactly the regime this paper says degrades. The mitigation is not a
bigger model; it is checkpointing against an external check — §0's rule again.

`MEASURED-BENCH` · **Reliability across repeated trials collapses.** Yao, Shinn,
Razavi & Narasimhan, **τ-bench**, arXiv:2406.12045 (Jun 2024). The `pass^k`
metric — probability that **all** *k* independent trials succeed. gpt-4o:
**pass¹ = 61.2% on retail, but pass⁸ < 25%**; on airline, **pass¹ = 35.2%**.
A monotone collapse across k = 1, 2, 4, 8, 16, 32. (Exact per-k values are only
plotted, not tabulated — **unverified beyond pass¹ and the pass⁸ < 25% claim**.)

**And the ablation that should worry anyone building a rule-following tutor:**
removing the domain policy document cost gpt-4o only **−4.4 points in retail
(61.2 → 56.8)** but **−22.4 points in airline (33.2 → 10.8)**. The retail
successes largely came from commonsense tool use, not from actually following
the stated rules. A pedagogical agent instructed "never give the answer; ask a
question first" is in the same category — and this measurement says such
instructions may be substantially *not what is driving the behaviour*.

`MEASURED-BENCH` · **Multi-turn degradation.** Laban, Hayashi, Zhou & Neville,
*"LLMs Get Lost In Multi-Turn Conversation,"* arXiv:2505.06120 (May 2025).
**200,000+ simulated conversations, 15 LLMs across 8 families (8B–300B+), 6
generation tasks.** Average **39% performance drop** in multi-turn
underspecified settings vs single-turn fully-specified (≈90% → ≈65%), decomposed
into **16% aptitude loss and a 112% increase in unreliability**. Mechanism:
models assume early, commit prematurely, and over-rely on the commitment — "when
LLMs take a wrong turn in a conversation, they get lost and do not recover."
`NEGATIVE RESULT #13`.

This is the single most under-quoted result for anyone building a tutor. **A
tutoring dialogue is by construction multi-turn and underspecified** — the
learner does not know what they need, which is why they are learning. That is
precisely the regime in which unreliability more than doubles.

### 4.4 Where autonomy currently breaks — cross-benchmark audits

`MEASURED-BENCH` · **Holistic Agent Leaderboard (HAL).** Kapoor, Stroebl et al.,
arXiv:2510.11977 (Oct 2025, ICLR 2026). **21,730 agent rollouts, 9 models, 9
benchmarks, ~$40,000, 2.5B tokens of logs released.** Two findings that should
change how agentic products are built:

1. **Higher reasoning effort *reduced* accuracy in the majority of runs.**
   `NEGATIVE RESULT #14`.
2. LLM-aided log analysis caught agents taking **unexpected shortcuts — e.g.
   searching the web for the benchmark's own answers** rather than solving the
   task. `NEGATIVE RESULT #15`.

The live site (later than the paper, 26,597 rollouts) states agents can be
**"100× more expensive while only being 1% better."**

`MEASURED-BENCH` · **AI Agents That Matter.** Kapoor, Stroebl, Siegel, Nadgir &
Narayanan, arXiv:2407.01502 (Jul 2024). On HumanEval, cost-controlled:

| Agent | Accuracy | Cost |
|---|---|---|
| LDB (GPT-4) | 93.3% | $6.36 |
| **"Warming" — a trivial retry baseline** | **93.2%** | **$2.45** |
| **"Retry" — even simpler baseline** | 92.0% | $2.51 |
| GPT-4 zero-shot | 89.6% | $1.93 |
| **LATS (GPT-4)** | **88.0%** | **$134.50** |
| Reflexion (GPT-4) | 87.8% | $3.90 |

**A trivial retry loop matched the best published agent architecture, and the
most elaborate architecture was 50× the cost for lower accuracy.** The authors:
"the question of whether debugging, reflection, and other such 'System 2'
approaches are useful for code generation **remains open**." No prior paper had
compared against retry. `NEGATIVE RESULT #16`.

The same paper documents **benchmark-result artifacts**: WebArena's then-top
agent claimed 35.8% while marking 8 tasks unachievable; Reflexion and LATS
silently modified HumanEval. "These errors inflate accuracy estimates and lead
to overoptimism about agent capabilities."

`MEASURED-BENCH` · **Scaffold choice matters far less than model choice.**
Terminal-Bench 2.0 paper (arXiv:2601.11868, Jan 2026, **89 tasks**): swapping
GPT-5-Nano → GPT-5.2 inside Codex CLI gives **+52%** resolution; swapping
OpenHands → Terminus 2 with Gemini-2.5-Pro fixed gives **+17%**. And: **no
meaningful correlation between average turns per trial and success rate**;
higher token count does not correlate with better performance. `NEGATIVE RESULT
#17`. Orchestration complexity is not where the gains are.

### 4.5 The trajectory, stated without hype and without dismissal

Both things are true and both are measured:

- **WebArena** (arXiv:2307.13854): original best agent **14.41%** against a
  **78.24%** human baseline.
- **OSWorld** (arXiv:2404.07972): original best **12.24%** against a **72.36%**
  human baseline — and as of **2026-07-25 the top entry is 90.19%** (325.59/361,
  Intelligence-Indeed Agent; verified from the official
  `osworld_verified_results.xlsx`). **Human parity was crossed around late
  2025.** The top 15 entries range 72.1–90.2%.
- **SWE-bench**: 4.4% (Oct 2023) → 22.4% (Apr 2024) → **79.2%** (Dec 2025).
- **Terminal-Bench 2.0**: the paper (Jan 2026) reports frontier systems "less
  than 65%"; the live leaderboard tops **84.7%** four months later.

`INFERENCE` · The honest reading is not "agents are unreliable" and not "agents
are nearly there." It is that **the reliable autonomous unit of work is
currently on the order of an hour at 80% success, doubling every ~4–6 months,
and it is checkpoint-bound rather than capability-bound.** Design for one-hour
verified units with an external check at each boundary, and the capability is
already sufficient for everything in §7. Design for an unattended overnight
tutor and the measurements above predict exactly how it fails.

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

*The brief predicted "almost nothing" here and expected a documented absence to
be a major finding. The prediction is correct, and the absence is sharper and
more specific than expected — but the reason is not that the idea failed. It is
that **two literatures exist and they have never touched each other.***

### 6.1 Branch A — self-improvement works, on benchmarks

`MEASURED-BENCH` · Every one of these is verified, and every one is measured on
a static machine benchmark:

| System | Measured gain | Source |
|---|---|---|
| **OPRO** | "up to **8% on GSM8K**, up to **50% on Big-Bench Hard**" over human-designed prompts | arXiv:2309.03409 |
| **DSPy** | compiled pipelines beat standard few-shot by "**over 25%** (GPT-3.5) and **65%** (llama2-13b-chat)"; beat expert demonstrations by **5–46%** and **16–40%** | arXiv:2310.03714 |
| **MIPROv2** | beats baseline optimisers on **5 of 7** multi-stage programs, "**as high as 13% accuracy**" | arXiv:2406.11695 |
| **PromptBreeder** | PaLM 2-L zero-shot **GSM8K 83.9% vs 59.3%** (Plan-and-Solve+); SVAMP 90.2 vs 75.7; ETHOS 89 vs 80 | arXiv:2309.16797 (table via body text) |
| **GEPA** | beats GRPO by **6% average, up to 20%**, with **up to 35× fewer rollouts**; beats MIPROv2 by **>10%** (+12% on AIME-2025) | arXiv:2507.19457 |
| **TextGrad** | GPT-4o on GPQA **51% → 55%**; **20% relative** on LeetCode-Hard | arXiv:2406.07496 |
| **AlphaEvolve** | 4×4 complex matrix multiplication in **48 scalar multiplications** — first improvement on Strassen in this setting in **56 years**; recovers **0.7%** of Google fleet compute; on **>50 open maths problems**, ~75% matched and **~20% improved** the state of the art | arXiv:2506.13131 |
| **Darwin Gödel Machine** | self-modifying agent: **SWE-bench 20.0% → 50.0%**, Polyglot **14.2% → 30.7%** | arXiv:2505.22954 |

That is a real, replicated, cross-lab capability. An agent that reads its own
outcome data and rewrites its own instruction **works**, and the effect sizes
are large.

**And zero of these papers involves a single human participant, let alone a
learning outcome.**

Note also what several of the most-cited open-endedness systems do *not* report:
**ADAS** (arXiv:2408.08435) gives **no numeric gain in its abstract**; **OMNI**
(arXiv:2306.01711) reports **no numbers**; **OMNI-EPIC** (arXiv:2405.15568)
claims **no quantitative evaluation at all**; **POET** (arXiv:1901.01753) is
qualitative. The open-endedness cluster is the least quantified part of the
whole self-improvement literature. `NEGATIVE RESULT` — treat any "self-designing
curriculum" pitch citing these as `DEMO`.

### 6.2 Branch B — instructional-policy optimisation on human learners exists, and it is pre-LLM

**A correction this survey must make to its own prior.** It is often asserted
that reinforcement learning for instructional sequencing has largely failed.
That is **wrong**, and the correction matters:

`MEASURED-META` · **Doroudi, Aleven & Brunskill (2019)**, *"Where's the Reward?
A Review of Reinforcement Learning for Instructional Sequencing,"* IJAIED
29(4):568–620, doi:10.1007/s40593-019-00187-x. Verbatim: **"We find that over
half of the studies found that RL-induced policies significantly outperform
baselines."** Of **41 studies from 34 papers**: **21 (51%)** significantly beat
all baselines; 4 showed aptitude–treatment interactions favouring low
performers; 4 mixed; **10 no significant difference; 1 where the baseline won.**
The authors' qualifier is the load-bearing part: RL "has been most successful in
cases where it has been **constrained with ideas and theories from cognitive
psychology and the learning sciences**."

`MEASURED-RCT` · **The strongest single number in this literature.** Lindsey,
Shroyer, Pashler & Mozer (2014), *Psychological Science* 25(3):639–647,
doi:10.1177/0956797613504302. A model-based personalised review scheduler,
deployed for a **full semester in a middle-school foreign-language course**,
produced **+16.5% course retention over massed study and +10.0% over
one-size-fits-all spaced study** on a cumulative post-semester exam. A policy
optimised against a memory model, measured on real long-term human retention.

`MEASURED-RCT` · **Clement, Roy, Oudeyer & Lopes** — learning-progress bandits
(ZPDES) in schools. The 2024 follow-up (arXiv:2402.01669) is an **RCT with 265
children aged 7–8**: pre→post Predefined **6.83 → 8.36** vs ZPDES **6.74 →
9.38**; algorithm × time **η² = 0.034**; ordering ZPDES+Choice > ZPDES >
Predefined > Predefined+Choice. **Note the null-and-negative:** adding learner
choice to the *fixed* curriculum **hurt** learning. (One reported test statistic
in the retrieved body text appears mis-transcribed — **the F/p pair is
unverified**; the means and group sizes are reliable.)

`MEASURED-RCT` · **AXIS** — Williams, Kim, Rafferty, Maldonado, Gajos, Lasecki
& Heffernan, L@S 2016, doi:10.1145/2876034.2876042. Learners generate and revise
explanations; a bandit selects which to show next. **This is the closest thing
that has ever existed to §1's loop.** Result: AXIS explanations "objectively
enhanced learning… compared to the default practice," and their "rated quality
and learning benefit **did not differ from explanations generated by an
experienced instructor**." (No effect size in the abstract.) It is a decade old
and it used learnersourced human explanations, not generated ones.

`MEASURED-RCT` · **Rafferty, Brunskill, Griffiths & Shafto**, *Faster Teaching
via POMDP Planning*, *Cognitive Science* 40(6):1290–1332,
doi:10.1111/cogs.12290 — POMDP-planned teaching accelerated learning relative to
baseline in two human concept-learning tasks. Lab tasks; no effect size in the
abstract.

### 6.3 The null results inside Branch B

`MEASURED-RCT` · **Prihar, Haim, Sales & Heffernan (2022)**, L@S,
doi:10.1145/3491140.3528267. Verbatim: the first empirical study of their
Automatic Personalized Learning Service found Beta-Bernoulli Thompson Sampling
**"only slightly more capable of selecting helpful support than randomly
selecting from the relevant support options."** The frequently quoted **+10%
learning figure for their improved algorithm is simulation-only** and must be
labelled as such. `NEGATIVE RESULT #21`.

`MEASURED-RCT` · **Prihar, Sales & Heffernan (2023)**, UMAP (ERIC ED636016): the
bandit **"slightly increased students' learning compared to A/B testing"** — no
effect size; "slightly" is the authors' own word.

`MEASURED-BENCH` · **Better prediction is not better instruction.** Rollinson &
Brunskill, EDM 2015 (ERIC ED560516): **"student models with similar predictive
accuracies can suggest that substantially different amounts of practice are
necessary… predictive accuracy may not be a sufficient metric by itself when
choosing which student model to use."** `NEGATIVE RESULT #22`.

`MEASURED-BENCH` · **Khajah, Lindsey & Mozer**, *"How deep is knowledge
tracing?"*, arXiv:1604.02416 (EDM 2016): DKT's "stunning performance advantage"
over Bayesian Knowledge Tracing **disappears** once BKT is given comparable
flexibility — "BKT achieves a level of performance indistinguishable from that
of DKT… its gains do not come from the discovery of novel representations."
`NEGATIVE RESULT #23`.

`MEASURED-BENCH` · **Adaptive assignment costs you statistical power.**
Rafferty, Williams & Ying, JEDM 2019 (ERIC EJ1220507) — simulation study
documenting the false-positive-rate and power costs of bandit assignment in
educational experiments. Anyone proposing §1's loop must price this in.

### 6.4 Curriculum learning for machines is mostly null

`MEASURED-BENCH` · **Wu, Dyer & Neyshabur**, *"When Do Curricula Work?"*,
arXiv:2012.03107 (ICLR 2021), from thousands of orderings: **"for standard
benchmark datasets, curricula have only marginal benefits, and randomly ordered
samples perform as well or better than curricula and anti-curricula, suggesting
that any benefit is entirely due to the dynamic training set size."** Curricula
help only under limited training budget or noisy labels. `NEGATIVE RESULT #24`.

Saglietti, Mannelli & Saxe (arXiv:2106.08068) state it plainly: "in machine
learning, curricula are not widely used and empirically often yield only
moderate benefits."

**Do not cite** *Curriculum Learning: A Survey* (arXiv:2101.10382) as evidence
of gains — it is a taxonomy paper with a promotional abstract and **no aggregate
effect size**.

### 6.5 The failure modes of automatic prompt optimisation itself

`MEASURED-BENCH` · *Are Large Language Models Good Prompt Optimizers?*,
arXiv:2402.02101: LLM optimisers **"struggle to identify the true causes of
errors during reflection, tending to be biased by their own prior knowledge
rather than genuinely reflecting on the errors,"** and even when reflection is
semantically valid they "often fail to generate appropriate prompts for the
target models." `NEGATIVE RESULT #25`.

`MEASURED-BENCH` · *The Unreasonable Effectiveness of Eccentric Automatic
Prompts*, arXiv:2402.10949: 60 system-message combinations × 3 models (7B–70B)
on GSM8K — results **"do not universally generalize across models"**
(Llama2-70B's optimum was *no* system message at all), and the best
auto-optimised prompt "exhibits a degree of peculiarity far beyond
expectations." **Optimised prompts are search artifacts, not transferable
pedagogy.** `NEGATIVE RESULT #26`.

`MEASURED-BENCH` · **Optimiser gains do not compound, and can transfer below the
unoptimised baseline.** *Do Agent Optimizers Compound? A Continual-Learning
Evaluation on Terminal-Bench 2.0*, arXiv:2607.14004 (Jul 2026). Two-phase
continual-learning evaluation (Phase-1 / Transfer / Final / lifelong average):

| Optimiser | Phase 1 | **Transfer** | Final | Lifelong avg |
|---|---|---|---|---|
| Baseline (unoptimised) | 62.5 | 56.8 | 56.8 | 58.7% |
| **GEPA** | 70.8 | **54.5** | 72.7 | 66.0% |
| Meta Harness | 66.6 | 68.2 | 59.1 | 64.6% |
| RELAI-VCL (regression-aware) | 79.2 | 72.7 | 77.3 | **76.4%** |

**GEPA transfers below the unoptimised baseline (54.5% vs 56.8%)** — Phase-1
overfitting, measured. Gains compound only when regression control sits *inside*
the search loop. `NEGATIVE RESULT #27`. This is the closest thing found to a
demonstration that APO overfits; a targeted search for a paper explicitly
measuring an APO train/validation/test gap returned **nothing citable**, so
treat "APO overfits validation" as **currently unsupported by a direct
citation**.

### 6.6 The headline: the two branches have never met

> **Has any agentic self-improving instructional system — LLM prompt/program
> optimisation, evolutionary search over agent designs, automated agentic-system
> design — ever been evaluated on human learners with a learning outcome?**
>
> **No. Zero such papers.**

The absence is documented rather than assumed. Search record (all counts exact,
performed 2026-07-28):

| Database | Query | Hits | Relevant |
|---|---|---|---|
| arXiv | `abs:"prompt optimization" AND abs:students` | 6 | **0** (one English-teaching chatbot uses APO but reports no learning outcome; one uses 32 students as *annotators*) |
| arXiv | `abs:"prompt optimization" AND (abs:"learning outcomes" OR abs:"learning gains")` | 1 | **0** |
| arXiv | `abs:DSPy AND (abs:tutor OR abs:education OR abs:students)` | 1 | **0** |
| arXiv | `abs:"self-improving" AND (abs:"human learners" OR abs:"student learning")` | **0** | 0 |
| arXiv | `abs:"automatic curriculum" AND abs:students` | 7 | **0** — all seven are RL agents where "students" means the *learner network* |
| arXiv | `abs:GEPA OR abs:MIPROv2 OR abs:PromptBreeder AND abs:tutoring` | 64 | **0** with human learners |
| ERIC | `description:"prompt optimization"` | **0** | — |
| ERIC | `description:"automated prompt"` | **0** | — |
| ERIC | `title:DSPy` | **0** | — |
| ERIC | `"automatic prompt optimization"` | **0** | — |
| ERIC | `description:"evolutionary search" AND description:"instruction"` | **0** | — |
| ERIC | `description:"large language model" AND description:"instructional policy"` | **0** | — |
| ERIC | `description:"automated design" AND description:"tutoring"` | **0** | — |
| ERIC | `description:"self-improving" AND description:"tutoring system"` | 2 | **0** (1988, 1995) |
| ERIC | `description:"reinforcement learning" AND description:"instructional policy"` | 1 | Doroudi 2019 |
| ERIC | `description:"multi-armed bandit"` | 13 | the entire education-bandit literature — **all pre-LLM** |
| OpenAlex | full text: "adaptive experimentation MOOClet multi-armed bandit education" | **15 in all of OpenAlex** | the field is that small |

**The boundary case, and why it makes the absence worse.** Tutor CoPilot
(arXiv:2410.03017) is "the first randomized controlled trial of a Human-AI
system in live tutoring, involving 900 tutors and 1,800 K-12 students": **+4
p.p. topic mastery (p < 0.01), +9 p.p. for students of the lowest-rated tutors,
at $20 per tutor per year.** But Tutor CoPilot is **a fixed, hand-engineered
prompt.** No optimiser, no search, no self-improvement loop. It proves that
human-learner RCTs of LLM instruction are entirely feasible at scale — which
makes the total absence of *any* optimiser-in-the-loop trial the more striking.
(`INTERNAL-PRIOR`, B2 §3.5: Tutor CoPilot's own distal outcome was **null** —
"we did not find statistically significant improvements in end-of-year math test
scores.")

### 6.7 What this means

`INFERENCE` · The self-improvement literature has spent three years optimising
against proxies — benchmark accuracy — without once closing the loop on the only
reward signal that matters in education. The one place the loop *was* closed
(Lindsey's review scheduler, ZPDES, AXIS) used 2014-era machinery over tiny,
hand-authored action spaces, and produced the largest personalisation effect
anyone has measured on human learners (**+16.5% semester retention**).

The unbuilt object is the obvious composition: **Branch A's optimiser, Branch
B's reward signal.** A GEPA-class optimiser whose fitness function is not
benchmark accuracy but measured human retention at delay. Nobody has attempted
it. The two nearest obstacles are both measured: the reward is slow and sparse
(§8.3), and the optimiser overfits its training phase (arXiv:2607.14004).

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

**Status: both halves exist; they have never been joined.** The optimiser works
(GEPA, DGM, AlphaEvolve — §6.1). The reward signal has been closed on human
learners before, with the largest personalisation effect anyone has measured
(**+16.5% semester retention**, Lindsey et al. 2014) — but with 2014 machinery
over a hand-authored action space (§6.2).

**Blocker:** the reward is slow and sparse, and optimisers overfit their training
phase in a measured way (**GEPA transfers to 54.5% against a 56.8% unoptimised
baseline**, arXiv:2607.14004). `NEGATIVE RESULT #27`.

### 7.7 An adversary or environment that adapts *between* sessions rather than within them

**Status: the least-discussed and most available.** Everything in §7.1–7.6 is
about what happens while the learner is present. The genuinely unprecedented
thing is the interval. No human tutor has ever spent two hours between Tuesday
and Wednesday reading one student's entire error history. That is not a
sophistication claim; it is an availability claim, and the measured reliability
(§4.2: ~70 minutes of work at 80% success, doubling every ~4–6 months) is
already sufficient for it.

**Blocker:** nothing technical. **The learner model.** You cannot mine a
transcript for a pattern; you can mine a structured error record. Nobody stores
one.

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

### 8.1 The ceiling is the check, not the model

Everything in §§1–7 is one rule wearing seven costumes. **An agentic loop is
worth exactly as much as the external check it closes on, and pedagogy is the
domain where that check is hardest to build.** Not because learning is
mysterious, but because the signal is slow (retention is measured at delay),
sparse (a learner produces a few dozen scorable acts per hour, not a few
thousand), and confounded (the learner is also changing for other reasons).

Three concrete measurements pin the ceiling:

- **Chance-level step verification.** TutorGym: no LLM beat chance at labelling
  an incorrect student action across 223 domains (`MEASURED-BENCH`).
- **Judge-based selection is negative.** −3.20pp and −1.68pp
  (`INTERNAL-PRIOR`).
- **Selection methods without a verifier plateau.** Majority voting and reward
  models "plateau beyond several hundred samples" (`MEASURED-BENCH`,
  arXiv:2407.21787).

### 8.2 Error compounding is a hard wall on autonomy

*(See §4 for the measured numbers.)* The structural point: for a task of *n*
sequential steps each succeeding independently with probability *p*, end-to-end
success is *pⁿ*. At *p* = 0.95, a 20-step task succeeds 36% of the time; at 50
steps, 8%. Agentic pedagogy proposals routinely imply 50–500-step autonomous
sessions. `INFERENCE` from arithmetic — real agents are neither independent nor
memoryless, and recovery behaviour changes the exponent, which is precisely what
§4's measurements quantify.

### 8.3 Verification cost is paid by the learner, and the learner is the scarce resource

The PaperQA2 result is the model case: **superhuman on three literature tasks,
and 30% of its flagged contradictions are wrong** (arXiv:2409.13740). Every
capability in §7 is a candidate-generator whose output must be checked. If the
agent checks it, you are back to §8.1. If the learner checks it, you have spent
the learner's attention — the one input that does not scale, cannot be
parallelised, and is *already* the binding constraint on every intervention in
this survey.

The engagement evidence says this is not hypothetical:

`MEASURED-RCT` · Nie et al., *"The GPT Surprise"* (L@S 2025): randomised offer of
a GPT tutor to **5,831 students in 146 countries** produced a **statistically
significant average decrease in exam participation** (`INTERNAL-PRIOR`, B2 §3.6).
The positive exam effect was among *adopters* — selection, not ITT.
`NEGATIVE RESULT #11`.

`MEASURED-META` · Wu & Yu (2023), *BJET*, 24 randomised studies: **short
interventions outperform long ones**, which the authors attribute to novelty
wearing off (`INTERNAL-PRIOR`, B2). Sophistication that must be *used* to pay
off is competing against a decay curve.

### 8.4 Is agentic sophistication competing with, or complementing, the low-tech floor?

State it plainly. The largest measured effects in this survey are all universal
and low-tech:

| Intervention | Effect | Evidence base |
|---|---|---|
| Retrieval practice | **g = 0.499** [0.442, 0.557] | 222 studies, 48,478 students, classrooms; I² = 88% |
| Spaced practice | **d = 0.54** [0.31, 0.77] | classroom meta-analysis |
| Expectancy to teach, stated before study | **g = 0.48** [0.34, 0.63] vs **g = −0.02** without | meta-analysis |
| Learning by teaching, with interaction | **g = 0.56** | meta-analysis |
| Elaborated vs bare feedback | **d = 0.49** vs **d = 0.05** | 40 studies, 70 ES |
| Simulation + scaffolding vs bare simulation | **g+ = 0.49** [0.36, 0.61] | k = 50, N = 3,342 |

Against these, the best LLM-tutoring RCTs land in the same band as pre-LLM ITS
and human tutoring (`INTERNAL-PRIOR`, B2: Nickow, Oreopoulos & Quan pooled human
tutoring **0.288 SD**, 96 randomised studies).

**The honest answer is: complementing, and specifically in one direction.**
Every row of that table is a *policy* — do this thing, at this time, in this
framing. None of them is hard to know and all of them are hard to *execute
reliably for one learner over months*. Execution is exactly what sampling,
execution, persistence and absence buy.

The failure mode is precisely inverted from the usual fear. The risk is not that
agentic systems are too weak to add anything on top of retrieval and spacing. It
is that **they will be built to replace the floor rather than to enforce it** —
generating explanations instead of demanding retrieval, answering instead of
asking, producing the artifact instead of making the learner produce it. Bastani
et al.'s −17% is what that looks like when it is measured
(`MEASURED-RCT`, PNAS 2025).

The strongest version of the affirmative case is therefore *not* "agents will
outperform retrieval practice." It is:

> **An agent is the first technology that can guarantee the floor is actually
> delivered — the retrieval item asked at the right delay, the expectancy
> sentence said before study and not after, the tutee that holds the error, the
> spaced review that survives the learner's forgetting to come back — for every
> learner, without a human in the loop, indefinitely.**

That claim is worth more than any capability in §7, and unlike most of §7 it is
buildable today with measured components. It also has never been tested: this
survey found **no RCT of an agentic system against a non-agentic one**, and no
RCT of *floor-enforcement-by-agent* against ordinary AI tutoring.
`NEGATIVE RESULT #12`.

---

## 9. Capability table

*The deliverable. "Reliability today" is the best verified public number for the
nearest measurable proxy, with its label. Where no number exists, the cell says
so rather than guessing.*

| # | What an agentic system can do | What a chatbot tutor structurally cannot | Measured reliability today | The specific blocker | What it unlocks pedagogically |
|---|---|---|---|---|---|
| 1 | **Generate k candidate explanations / problems / analogies and keep the one that survives an external check** | Sampling + external check. A chatbot emits one stream and cannot re-enter the loop | Selection *by test*: **+8.14pp** vs LLM-judge **−3.20pp** (`INTERNAL-PRIOR`). Coverage scales log-linearly over 4 orders of magnitude (`MEASURED-BENCH`, 2407.21787). Self-consistency **+17.9 GSM8K** (`MEASURED-BENCH`) | **The selector.** In pedagogy the only grounded check is the learner's own unseen-item accuracy — slow and attention-expensive. LLM step-verification is at **chance** (TutorGym, `MEASURED-BENCH`) | The explanation that works for *this* learner is found empirically instead of guessed once |
| 2 | **Write, execute, and repair a runnable artifact inside the session** | Execution. A chatbot can emit code; it cannot know whether it ran | **93.8%** Manim explanatory video generation (2502.19400); **79.2%** SWE-bench Verified (396/500, verified from swe-bench/experiments); **83.8%** Terminal-Bench 2.1; **4.6%** SciCode novel research code; **21.0%** PaperBench (all `MEASURED-BENCH`) | **Artifact class.** Reliability tracks whether a compiler or test exists. Plus delivery: only **24.11%** of public notebooks execute at all, **4.03%** reproduce (`MEASURED-BENCH`, F3) | Simulation g+ = 0.62; sim + scaffold adds g+ = 0.49 (`MEASURED-META`). The lab arrives in the turn the confusion did |
| 3 | **Hand the learner a sandbox and check what comes out, without typing in it** | Verification of the learner's own product | Elaborated feedback **d = 0.49** vs bare correctness **d = 0.05** (`MEASURED-META`); programming transfer **g = 0.49** (`MEASURED-META`) | **Restraint, not capability.** Every measured harm (Bastani **−17%**, Fan's dissociation, generation effect d = 0.40) comes from the agent driving instead of the learner | Productive failure **g = 0.36–0.58** with a real object to fail against |
| 4 | **Work for hours between sessions on the learner's behalf** | Absence. A chatbot only exists when addressed | Reliable autonomous unit ≈ **70 min at 80% success** (Claude Opus 4.6, METR TH1.1); 50% horizon **~12 h**; doubling **~129 days since 2023** (`MEASURED-BENCH`) | **Self-conditioning** — early errors make later errors more likely, and model scale does not fix it (`MEASURED-BENCH`, 2509.09677). **τ-bench pass⁸ < 25%** where pass¹ = 61% | Mining months of error history, pre-building and pre-testing tomorrow's set, pre-computing the artifact — none possible for any human tutor at any price |
| 5 | **Persist a per-learner error record across months and condition every future act on it** | Persistence beyond the context window | Trivially reliable as storage; **no measured pedagogical effect** — this survey found no trial | **Nothing technical.** The blocker is that no one has defined *what to store* such that it is machine-actionable (a misconception representation, not a transcript) | An adversary/tutee/problem-setter that draws from your actual history rather than a generic bank |
| 6 | **Run a literature search overnight and return checked candidates** | Long-running tool use with no user present | PaperQA2 **matches or exceeds subject-matter experts** on retrieval, summarisation, contradiction detection vs experts with unrestricted tools; **2.34 ± 1.99 contradictions/paper, 70% expert-validated** (`MEASURED-BENCH`, 2409.13740) | **30% false-positive rate** → must be delivered as candidates. And no system knows the learner's confusion precisely enough to issue the query | The one paper that resolves your specific confusion, found while you slept |
| 7 | **Stage two committed advocates and let the learner judge** | Genuine adversarial structure — a single stream cannot hold two committed positions | Non-expert humans **88% vs 60%** baseline; non-expert models **76% vs 48%** (`MEASURED-BENCH`, 2402.06782). Optimising debaters for *persuasiveness* **improved** truth-finding | **Untested on learning outcomes.** Also requires answer sets pre-verified, or debate amplifies error | +28pp for the non-expert judge is the largest measured multi-agent pedagogical effect in existence |
| 8 | **Be taught by the learner, hold the error, and act on what it was taught** | Holding a false belief under corrective pressure | **Near-zero Selective Flip Score** across 7 models 4B–120B (`MEASURED-BENCH`, 2605.12748). SFT improves it **up to +0.56** | **Sycophancy at the model level.** Needs a fine-tuned tutee + an SFS-class certification eval | Learning by teaching **g = 0.56**, gated on expectancy stated *before* study (**g = 0.48 vs −0.02**) |
| 9 | **Optimise its own instruction against outcome data** | Reading its own results and rewriting its own policy | On benchmarks: **GEPA +6–20% over GRPO with 35× fewer rollouts**; **DGM SWE-bench 20% → 50%**; **AlphaEvolve improved ~20% of >50 open maths problems** (`MEASURED-BENCH`). On human learners: **zero systems, ever** | **The reward signal.** Human learning is slow, sparse, and measured at delay. Also **GEPA transfers *below* the unoptimised baseline** (54.5% vs 56.8%) — measured overfitting (`MEASURED-BENCH`, 2607.14004) | Branch B shows the prize: a policy optimised against a memory model gave **+16.5% semester retention** (Lindsey 2014). Branch A's optimiser on Branch B's signal is unbuilt |
| 10 | **Guarantee the low-tech floor is actually delivered, per learner, indefinitely** | Persistence + absence: it must act when the learner has forgotten to come back | Component effects are the largest in the survey (retrieval **g = 0.499**, spacing **d = 0.54**, expectancy **g = 0.48**). **The composed system has never been trialled** | Nothing technical. **Nobody has built it because it is unglamorous** | The highest expected value in this section, and the least researched |

---

## 10. The five most valuable agentic capabilities nobody has built

*Ranked by expected value = (size of the measured effect it would unlock) ×
(probability it works) ÷ (distance from existing components). Each is scoped so
a team could start on Monday.*

### 1. The misconception-faithful tutee, with a certification eval

**What it is.** A model fine-tuned to *hold* an assigned misconception under
corrective pressure, that the learner must teach; plus a public Selective Flip
Score benchmark that certifies faithfulness before deployment. The tutee then
attempts a downstream problem using only what it was taught, and its accuracy is
the learner's score.

**Why it is first.** It unlocks the largest under-deployed effect in the survey
(**g = 0.56**, learning by teaching with interaction), it supplies the *grounded
selector* §1 lacks (the tutee's downstream accuracy is an external check that
does not require an LLM judge), and it converts the expectancy result
(**g = 0.48 vs g = −0.02**) into an enforced product behaviour.

**What it would take.** SFT + RL on misconception-conditioned dialogue —
arXiv:2605.12748 shows **up to +0.56 SFS from SFT and better consistency from
RL**, so the recipe is published. The eval is the harder half and the more
valuable one. Estimated: one fine-tune, one benchmark, one RCT.

### 2. The test-grounded parallel-exploration loop

**What it is.** Generate *k* explanations of one concept; deliver under an
assignment rule; score by the learner's accuracy on unseen retrieval items;
retain the winner as this learner's policy and as a prior for the next learner.
Never let an LLM judge touch the selection.

**Why it is second.** It is the single most reliable agentic capability in
existence (§1) applied to the one domain where it has never been closed, and the
size of the prize is measured: **+8.14pp for test-based selection vs −3.20pp for
the judge**, an eleven-point spread on the same candidate pool.

**What it would take.** Nothing new in generation. It needs (a) an item bank the
learner has not seen, at the right grain — the psychometrics work in C2; (b) an
assignment rule that spends few enough items to be affordable in learner
attention; (c) honest handling of the fact that one learner supplies very little
signal, so the loop must pool across learners with per-learner shrinkage. That
last point is where the adaptive-experimentation literature (§6) should be
mined rather than reinvented.

### 3. The step-level verifier for student work

**What it is.** A model or ensemble that, given a domain and a student action,
says *correct / incorrect and why* at materially better than chance.

**Why it is third.** It is the missing component that blocks almost everything
else. TutorGym measured **no LLM better than chance at labelling incorrect
actions across 223 domains**, and next-step correctness at **~52–70%**. Coding
agents work because `pytest` exists. Tutoring agents do not because this does
not.

**What it would take.** The data exists — decades of ITS logs with ground-truth
step labels, which is precisely what TutorGym packaged. This is a supervised
learning problem with a public testbed and a published chance-level baseline. It
is the most tractable item on this list and the highest-leverage.

### 4. The floor-enforcement agent

**What it is.** An agent whose objective function is *not* to explain. Its job is
to guarantee that, for this learner, over months: the expectancy sentence
precedes study; retrieval is demanded at the right delay; spacing survives the
learner's absence; feedback is elaborated rather than bare; scaffolding fades on
measured evidence rather than schedule. It uses persistence and absence — the
two agentic properties nothing else in edtech uses — and it deliberately does
not use generation.

**Why it is fourth.** It composes the six largest effects in the survey
(g = 0.499, d = 0.54, g = 0.48, g = 0.56, d = 0.49, g+ = 0.49) and requires no
capability that is not already reliable. It ranks below 1–3 only because those
three create new evidence, whereas this one exploits existing evidence — but it
is the most likely of the five to work.

**What it would take.** A scheduler that is boring, a learner model that stores
policy rather than transcript, and an RCT against ordinary AI tutoring. This
survey found **no such trial**.

### 5. The heterogeneous-arbiter ensemble

**What it is.** Not four personas over one model. Four agents with four
*different arbiters*: a proof assistant, a computer algebra system, a numerical
simulation, and retrieval over a fixed corpus — each able to falsify the others,
with disagreement surfaced to the learner as the pedagogical event rather than
resolved silently.

**Why it is fifth.** The measured multi-agent literature is clear that
prompt-heterogeneity buys little (single strong prompt ≈ best discussion method,
arXiv:2402.18272) while evidence-heterogeneity is untested. Disagreement between
two *grounded* checkers is exactly the "authentic dissent" condition that
Khan et al.'s **+28pp** result and the conceptual-change literature both require,
and unlike debate between two prompted personas it cannot be faked.

**What it would take.** The arbiters all exist and F3 documents their reliability
individually. The unrun experiment is one line: **tool-heterogeneous vs
prompt-heterogeneous ensembles on a matched task, with a learning outcome.** No
one has run it.

---

### The five in one line each

1. **A tutee that will not fold** — unlocks g = 0.56, and supplies the selector everything else needs.
2. **Generate-and-select on the learner's own test, never on a judge** — an eleven-point spread is already measured.
3. **A step-level verifier for student work** — the missing `pytest` of pedagogy; currently at chance.
4. **An agent whose only job is to enforce the boring floor** — composes the six largest effects in the survey, needs no new capability.
5. **Four different arbiters, not four personas** — heterogeneity of evidence, with disagreement as the lesson.

---

## 11. Negative and null results register

*The brief asked for at least three. There are eighteen. They are the reason the
affirmative case above is load-bearing rather than decorative.*

| # | Result | Source | Label |
|---|---|---|---|
| 1 | LLMs cannot self-correct reasoning without external feedback; **performance sometimes degrades** after self-correction | arXiv:2310.01798 | `MEASURED-BENCH` |
| 2 | **No test-grounded parallel-exploration loop for pedagogy exists.** arXiv full-text searches for `"best-of-n" education explanation selection student` and `misconception targeted feedback LLM randomized` return **zero results** | this survey, 2026-07-28 | documented absence |
| 3 | Best agent replicates ICML papers at **21.0%**; does not beat the human baseline | arXiv:2504.01848 | `MEASURED-BENCH` |
| 4 | Simulations do **not** improve scientific inquiry/reasoning skill: **g+ = 0.26, 95% CI [−0.03, 0.55]**, k = 6 | D'Angelo et al. 2014 | `MEASURED-META` |
| 5 | AI tutor without guardrails: **+48%/+127% with the tool, −17% without it**; guardrailed version −0.004 (n.s.) — it prevented harm, it did not create learning | PNAS 2025, doi:10.1073/pnas.2422633122 | `MEASURED-RCT` |
| 6 | ChatGPT improved essay scores but **knowledge gain and transfer were not significantly different**, and no difference in intrinsic motivation | doi:10.1111/bjet.13544, N = 117 | `MEASURED-RCT` |
| 7 | The canonical "Google rots memory" experiment **fails to replicate** — BF01 = 5.07 for the null; already failed in Camerer et al. 2018 despite adequate power | doi:10.7717/peerj.10325 | `MEASURED-RCT` |
| 8 | **A single well-prompted agent nearly matches the best multi-agent discussion method**; discussion only helps when the prompt has no demonstrations | arXiv:2402.18272 | `MEASURED-BENCH` |
| 9 | LLM student simulators have **near-zero misconception faithfulness** across 7 models, 4B–120B | arXiv:2605.12748 | `MEASURED-BENCH` |
| 10 | **No LLM beat chance at labelling an incorrect student action** across 223 tutor domains; next-step correctness ~52–70% | arXiv:2505.01563 | `MEASURED-BENCH` |
| 11 | Randomised GPT-tutor offer to 5,831 students produced a **significant average decrease in exam participation** | Nie et al., L@S 2025 | `MEASURED-RCT` |
| 12 | **No RCT of an agentic system against a non-agentic one on a learning outcome exists**, anywhere in this survey's corpus | this survey | documented absence |
| 13 | **39% average performance drop** in multi-turn underspecified conversation; **unreliability +112%**; "when LLMs take a wrong turn… they get lost and do not recover" | arXiv:2505.06120, 200k+ conversations | `MEASURED-BENCH` |
| 14 | **Higher reasoning effort reduced accuracy in the majority of runs** across 21,730 rollouts | arXiv:2510.11977 | `MEASURED-BENCH` |
| 15 | Agents caught **searching the web for the benchmark's own answers** instead of solving tasks | arXiv:2510.11977 | `MEASURED-BENCH` |
| 16 | A **trivial retry baseline (93.2%, $2.45) matched the best published agent architecture (93.3%, $6.36)**; the most elaborate architecture cost **$134.50 for 88.0%** | arXiv:2407.01502 | `MEASURED-BENCH` |
| 17 | Scaffold choice matters far less than model choice (**+52% from model swap vs +17% from scaffold swap**); **no correlation between turns-per-trial and success** | arXiv:2601.11868 | `MEASURED-BENCH` |
| 18 | Published agent results contained **artifacts** — tasks silently marked unachievable, benchmarks silently modified — inflating accuracy estimates | arXiv:2407.01502 §6 | `MEASURED-BENCH` |
| 19 | ITS is **not** better than an individual human tutor (**g = −0.11 n.s.**) or small-group instruction (**g = 0.05 n.s.**) | Ma et al. 2014, doi:10.1037/a0037123 | `MEASURED-META` |
| 20 | Bare correctness feedback is worth almost nothing: **d = 0.05** | doi:10.3102/0034654314564881 | `MEASURED-META` |
| 21 | Thompson-sampling personalisation in ASSISTments was **"only slightly more capable of selecting helpful support than randomly selecting"**; the +10% figure is **simulation only** | doi:10.1145/3491140.3528267 | `MEASURED-RCT` |
| 22 | **Predictive accuracy is not a sufficient criterion for a student model** — models with similar AUC imply substantially different practice requirements | Rollinson & Brunskill, EDM 2015, ERIC ED560516 | `MEASURED-BENCH` |
| 23 | Deep Knowledge Tracing's advantage over BKT **disappears** when BKT is given comparable flexibility; "gains do not come from the discovery of novel representations" | arXiv:1604.02416 | `MEASURED-BENCH` |
| 24 | **Curricula have only marginal benefits** on standard benchmarks; **randomly ordered samples perform as well or better**; any benefit is attributable to dynamic training-set size | arXiv:2012.03107 (ICLR 2021) | `MEASURED-BENCH` |
| 25 | LLM prompt optimisers **"struggle to identify the true causes of errors… biased by their own prior knowledge rather than genuinely reflecting on the errors"** | arXiv:2402.02101 | `MEASURED-BENCH` |
| 26 | Auto-optimised prompts **do not generalise across models** (Llama2-70B's optimum was *no* system message) and are search artifacts — "peculiarity far beyond expectations" | arXiv:2402.10949 | `MEASURED-BENCH` |
| 27 | **GEPA transfers below the unoptimised baseline** (54.5% vs 56.8%) — measured Phase-1 overfitting; optimiser gains compound only with regression control inside the search loop | arXiv:2607.14004 | `MEASURED-BENCH` |
| 28 | Adding **learner choice to a fixed curriculum hurt learning** (Predefined+Choice was the worst of four arms), RCT, 265 children | arXiv:2402.01669 | `MEASURED-RCT` |
| 29 | The most-cited open-endedness systems report **no quantitative gain at all** — ADAS gives no number in its abstract, OMNI none, OMNI-EPIC claims no quantitative evaluation, POET is qualitative | arXiv:2408.08435 / 2306.01711 / 2405.15568 / 1901.01753 | `DEMO` |
| 30 | **Zero agentic self-improving instructional systems have ever been evaluated on human learners with a learning outcome.** 6 arXiv queries, 10 ERIC queries, OpenAlex full-text — search record in §6.6 | this survey, 2026-07-28 | documented absence |

---

## 12. Sources

**Verification note.** During this research pass the **arXiv API
(`export.arxiv.org`) returned "Rate exceeded" persistently** and **OpenAlex
exhausted its free daily budget**. Verification was therefore performed by
direct fetch of `arxiv.org/abs/…` pages, PDF download + `pdftotext`, Crossref,
ERIC, Europe PMC, HuggingFace datasets-server, `gh api`, and the projects' own
published data files. Every item below is marked verified or explicitly flagged.

### Test-time scaling, sampling and verification
1. Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou — *Self-Consistency Improves Chain of Thought Reasoning*, arXiv:2203.11171 — **verified via fetch**
2. Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini — *Large Language Monkeys*, arXiv:2407.21787 — **verified via fetch**
3. Snell, Lee, Xu, Kumar — *Scaling LLM Test-Time Compute Optimally…*, arXiv:2408.03314 — **verified via fetch**
4. Cobbe et al. — *Training Verifiers to Solve Math Word Problems*, arXiv:2110.14168 — **verified via fetch**; the "30× model size" figure is **unverified**
5. Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe — *Let's Verify Step by Step*, arXiv:2305.20050 — **verified via fetch**
6. Huang, Chen, Mishra, Zheng, Yu, Song, Zhou — *LLMs Cannot Self-Correct Reasoning Yet*, arXiv:2310.01798 — **verified via fetch**
7. Kirchner, Chen, Edwards, Leike, McAleese, Burda — *Prover-Verifier Games improve legibility*, arXiv:2407.13692 — **verified via fetch**

### Agentic generation, execution and long-horizon reliability
8. Jimenez et al. — *SWE-bench*, arXiv:2310.06770 — **verified**; original best 1.96% (Claude 2 + BM25)
9. SWE-bench Verified — 500 instances (HuggingFace datasets-server, `num_rows: 500`, created 2024-08-13) — **verified**. Top scores **79.2%** (`live-SWE-agent` + Claude Opus 4.5, 2025-12-15; `sonar-foundation-agent` + Opus 4.5, 2025-12-05 — 396/500 each, verified directly from `swe-bench/experiments` via `gh api`). OpenAI's Verified announcement is **unverified** (openai.com returns 403)
10. Terminal-Bench 2.0 — arXiv:2601.11868, **89 tasks** — **verified**; live 2.1 leaderboard top **83.8% ± 1.2** (Claude Code / Fable 5, 2026-06-07) — **verified via tbench.ai**; repo `laude-institute/terminal-bench` pushed **2026-07-11**, 2,493 stars (`gh api`)
11. Ku, Chong, Leung, Shah, Yu, Chen — *TheoremExplainAgent*, arXiv:2502.19400 — **93.8%** success, 240 theorems — **verified via fetch**
12. Tian et al. — *SciCode*, arXiv:2407.13168 — **4.6%** main-problem solve rate — **verified via fetch**
13. Chan et al. (OpenAI) — *MLE-bench*, arXiv:2410.07095 — **16.9%** bronze — **verified via fetch**
14. Starace et al. (OpenAI) — *PaperBench*, arXiv:2504.01848 — **21.0%** — **verified via fetch**
15. Kwa, West et al. (METR) — *Measuring AI Ability to Complete Long Software Tasks*, arXiv:2503.14499, NeurIPS 2025 — **verified**; live data `metr.org/assets/benchmark_results_1_1.yaml` (228 tasks) — **verified and parsed**
16. Sinha, Arun, Goel, Staab, Geiping — *The Illusion of Diminishing Returns*, arXiv:2509.09677, ICLR 2026 — **verified via PDF**
17. Yao, Shinn, Razavi, Narasimhan — *τ-bench*, arXiv:2406.12045 — **verified via PDF**; per-k values for k = 2,4,16,32 **unverified** (figure only)
18. Laban, Hayashi, Zhou, Neville — *LLMs Get Lost In Multi-Turn Conversation*, arXiv:2505.06120 — **verified**
19. Kapoor, Stroebl et al. — *Holistic Agent Leaderboard*, arXiv:2510.11977, ICLR 2026 — **verified**
20. Kapoor, Stroebl, Siegel, Nadgir, Narayanan — *AI Agents That Matter*, arXiv:2407.01502 — **verified via PDF Table A1**
21. Zhou et al. — *WebArena*, arXiv:2307.13854 — 14.41% vs 78.24% human — **verified via PDF**
22. Xie et al. — *OSWorld*, arXiv:2404.07972 — 12.24% vs 72.36% human; current top **90.19%** (2026-07-25, official `osworld_verified_results.xlsx`) — **verified**
23. Mialon, Fourrier, Swift, Wolf, LeCun, Scialom — *GAIA*, arXiv:2311.12983 — 92% human vs 15% GPT-4+plugins, 466 questions — **verified via fetch**; current leaderboard **unverified**
24. Liu et al. — *AgentBench*, arXiv:2308.03688 — **verified**
25. Drouin et al. — *BrowserGym/WorkArena*, arXiv:2412.05467 — WorkArena L3 at **0.0–0.4%** — **verified via PDF**
26. Wei et al. (OpenAI) — *BrowseComp*, arXiv:2504.12516, 1,266 questions — **verified**; success rates **not on the abs page**

### Multi-agent
27. Wang, Wang, Su, Tong, Song — *Rethinking the Bounds of LLM Reasoning*, arXiv:2402.18272 — **verified via fetch**
28. Cemri, Pan, Yang, Agrawal, Chopra, Tiwari, Keutzer, Parameswaran, Klein, Ramchandran, Zaharia, Gonzalez, Stoica — *Why Do Multi-Agent LLM Systems Fail?* (MAST), arXiv:2503.13657 — **verified via fetch**
29. Khan, Hughes, Valentine, Ruis, Sachan, Radhakrishnan, Grefenstette, Bowman, Rocktäschel, Perez — *Debating with More Persuasive LLMs*, arXiv:2402.06782 — **verified via fetch**
30. Self-MoA, arXiv:2502.00674 — `INTERNAL-PRIOR` via G2
31. Anthropic engineering, *How we built our multi-agent research system* — `VENDOR`, used only as a design constraint

### Agentic education systems (all evaluated on simulated learners or without controls)
32. Zhao, Zhang, Ren, Guo, Chu, Ma, Huang — *DeepTutor: Towards Agentic Personalized Tutoring*, arXiv:2604.26962 — **verified via fetch**; simulator-evaluated
33. Wu, Song, Zhao, Wu, Wan — *CogEvo-Edu*, arXiv:2512.00331 — **verified via fetch**; simulated students + three-model LLM-as-judge
34. Ye, Li et al. — *AgentSchool*, arXiv:2605.30144 — **verified via fetch**; simulated students only, no quantitative metrics
35. *ITAS — From Prototype to Classroom: An ITS for Quantum Education*, arXiv:2604.24807 — **verified via fetch**; real course (Old Dominion), **no metrics, no control**
36. *LEA — Learning Engagement Assistant*, arXiv:2607.13370 — first classroom deployment, **n = 8**
37. Weitekamp, Siddiqui, MacLellan — *TutorGym*, arXiv:2505.01563 — **verified via fetch**; 223 domains, chance-level error labelling
38. Do, Sonkar, Sachan — *Simulating Students or Sycophantic Problem Solving?*, arXiv:2605.12748 — **verified via fetch**
39. Li & Zheng — *A Scoping Review of LLM-Based Pedagogical Agents*, arXiv:2604.12253, 52 studies — **verified via fetch**
40. Skarlinski, Cox, Laurent, Braza, Hinks, Hammerling, Ponnapati, Rodriques, White — *Language agents achieve superhuman synthesis of scientific knowledge* (PaperQA2), arXiv:2409.13740 — **verified via fetch**
41. Wang, Ribeiro, Robinson, Loeb, Demszky — *Tutor CoPilot*, arXiv:2410.03017 — **verified via fetch**; +4 p.p. (+9 p.p. lowest-rated), 900 tutors / 1,800 students, **null on end-of-year test** (`INTERNAL-PRIOR` B2)

### Learning science (tools, feedback, offloading)
42. Scherer, Siddiq, Sánchez Viveros (2019), doi:10.1037/edu0000314 — g = 0.49 [0.37, 0.61], 105 studies — **verified via ERIC**
43. Chen & Yang (2019), doi:10.1016/j.edurev.2018.11.001 — d+ = 0.71, 12,585 students — **verified**; **no CI reported**
44. Van der Kleij, Feskens, Eggen (2015), doi:10.3102/0034654314564881 — EF d = 0.49, KR d = 0.05 — **verified via OpenAlex**
45. Sinha & Kapur (2021), doi:10.3102/00346543211019105 — g = 0.36 [0.20, 0.51] — **verified via ERIC**
46. Ma, Adesope, Nesbit, Liu (2014), doi:10.1037/a0037123 — **verified via OpenAlex**
47. D'Angelo, Rutstein, Harris, Bernard, Borokhovski, Haertel (2014), SRI International, *Simulations for STEM Learning* — **verified: full PDF retrieved and text-extracted**
48. Ellington (2006), doi:10.1111/j.1949-8594.2006.tb18067.x, ERIC EJ751981 — direction **verified**, **numeric effect sizes unverified (paywalled tables)**
49. Ellington (2003), doi:10.2307/30034795 — **effect sizes unverifiable; closed access, abstract elided. Do not quote.**
50. Bertsch, Pesta, Wiscott, McDaniel (2007), doi:10.3758/BF03193441, PMID 17645161 — generation effect **.40**, 445 ES / 86 studies — **verified via Europe PMC**; **no CI**
51. Bastani et al. (2025), *PNAS* 122, doi:10.1073/pnas.2422633122, PMC12232635 — **verified**; cite PNAS, not SSRN 4895486
52. Fan, Tang, Le, Gašević (2024), *BJET* 55(6), doi:10.1111/bjet.13544 — **verified via OpenAlex**
53. Gerlich (2025), *Societies* 15(1):6, doi:10.3390/soc15010006 — **verified from PDF**; **Correction: Societies 15(9):252, doi:10.3390/soc15090252**; correlational, self-report instrument
54. Lee, Sarkar, Tankelevitch, Drosos, Rintel, Banks, Wilson (2025), CHI, doi:10.1145/3706598.3713778 — **survey of 319 knowledge workers, self-report only, no effect sizes**
55. Kosmyna et al., *Your Brain on ChatGPT*, arXiv:2506.08872 — **83.3% (15/18) verified verbatim from PDF; n = 54; preprint; effect attenuates by Sessions 2–3**
56. Hesselmann (2020), *PeerJ* 8:e10325, doi:10.7717/peerj.10325 — **verified**; BF01 = 5.07
57. Sparrow, Liu, Wegner (2011), *Science*, doi:10.1126/science.1207745 — the original, **twice failed to replicate**
58. Camerer et al. (2018), *Nature Human Behaviour*, Social Sciences Replication Project — **verified via secondary**
59. Cash, Kelly, Macnamara, Risko (2026), *TiCS*, doi:10.1016/j.tics.2026.06.004 — **verified**
60. Yan, Greiff, Lodge, Gašević (2025), *Nature Reviews Psychology*, doi:10.1038/s44159-025-00467-5 — **verified**
61. Rutten, van Joolingen, van der Veen (2012), doi:10.1016/j.compedu.2011.07.017 — **narrative review, no pooled ES. Do not cite for a number.**
62. de Jong, Linn, Zacharia (2013), *Science*, doi:10.1126/science.1230579 — **Review/Perspective, no meta-analytic ES. Do not cite for a number.**

### Internal prior (this survey)
63. §05 *The explanation is the work* — test-based selection **+8.14pp** vs LLM-judge **−3.20pp / −1.68pp**; expectancy **g = 0.48 vs −0.02**; human code raters α ≈ 0.20
64. F2 *Beyond the tutor* — six roles; learning-by-teaching **g = 0.56**; the adversary role
65. F3 *Executable and verifiable* — notebook execution **24.11%**, self-reproduction **4.03%** of 863,878 attempted executions
66. B1 — retrieval **g = 0.499** [0.442, 0.557]; spacing **d = 0.54** [0.31, 0.77]
67. B2 — the seven LLM-tutoring RCTs; Nickow, Oreopoulos & Quan pooled human tutoring **0.288 SD**
68. G2 *Agent village* — multi-agent architecture, MAST, Self-MoA, the debate result
69. C2 — assessment psychometrics (the item bank capability #2 in §10 depends on)

---
title: "The G1 Grounding Ladder — One Verification Doctrine for Formulas, Figures, Items, and Agents"
wave: G
date_researched: 2026-07-27
sources_count: 58
---

# G1 · The Grounding Ladder

> **What this section is.** `survey/00-north-star-jarvis.md` already promises a tutor
> "grounded by verifiable code (**G1 ladder**)." Until now that was a dangling reference.
> This section makes it real: one ladder, one invariant, one routing table, one composition
> rule, and one honest statement of where the trust boundary ends up.
>
> **What it is not.** It is not a second literature sweep. F3 did the sweep for derivations
> (76 sources), C1 for figures, C2 for assessment, G2 for multi-agent claims, F10 for
> explanation ladders, I2 for the *pāṭha* protocol. Those four verification stories are
> currently four stories. G1's job is to notice that they are one mechanism seen from four
> angles, to say what the mechanism is, and to run the experiments that the separate sections
> left open. Four original measurements are reported here (§3.4, §8), three of them negative.

---

## 1. Lead with what this buys — and the guardrail in the same breath

Grounding is usually sold as a safety feature: *stop the tutor lying.* That framing
under-sells it by an order of magnitude, and it is also the framing that produces bad
products, because it makes verification a filter bolted onto the end of a generator. The
better framing is capability. **A tutor that can settle a factual dispute in 0.6 ms without
appealing to its own authority can do six things it cannot do today.** Each is stated with
the constraint that keeps it honest.

**1.1 It can contradict a confident learner without asserting authority.**
Today, when a tutor tells a learner they are wrong, it is staking status: *believe me, I am
the machine that knows.* That is exactly the epistemic posture education research spends its
time trying to dismantle, and it fails badly with the learner who is already right and the
learner who has learned not to argue. With a checker in the loop the move changes from
*assertion* to *experiment*: "I think that's off — let's evaluate both versions at x = 3 and
see." The tutor stops being the authority and becomes the person who knows how to settle it.
`INFERENCE`, but it is licensed by a measurement: G2 §2.2 permits the learner-as-judge tier
**only over answer sets already verified by executable ground truth**, and Khan et al.'s
debate result (non-expert human judges **88% vs 60% baseline**, arXiv:2402.06782,
`MEASURED-BENCH`) is what that tier is worth. Grounding is the precondition that makes
staging a disagreement safe rather than a way to teach a misconception with production value.
> **Guardrail.** The check settles *the claim*, never *the person*. And it settles only
> claims of the type it can decide (§4). A tutor that runs a numeric check and then
> generalises the win into "and therefore my explanation was better" has committed F3 §7's
> category error.

**1.2 Productive failure becomes bounded, and therefore affordable.**
The reason tutors interrupt is fear that a wrong model will set. A deterministic checker that
fires at the end of an exploration bounds that risk: you can let a learner build a wrong
model for twenty minutes *because you can show it is wrong in under a millisecond* and you
can show it with the learner's own numbers. **Grounding is what buys a tutor permission to
shut up.** `INFERENCE`.
> **Guardrail.** H1's finding governs: for anxiety and learned-helplessness archetypes and
> for working-memory-limited learners, unguided exploration is among the clearest measured
> harms. Bounded failure is a *policy setting on the learner model*, not a default.

**1.3 Disconfirmation can be delivered by the world instead of by an adult.**
Conceptual change wants cognitive conflict without ego threat, and has always needed
apparatus to get it. If the learner's prediction is falsified by a simulation they can rerun,
the source of the correction is the phenomenon. This has been unaffordable at scale for a
century; at L2b it costs a reactive-notebook cell. `INFERENCE`.
> **Guardrail.** A simulation is a *model*, and its assumptions are part of the claim
> (§7). "The simulation disagrees with you" is only honest if the simulation's declared
> domain contains the learner's case.

**1.4 The learner's own conjectures get the same ladder as the machine's.**
The badge is symmetric. A learner who writes "I think the sum is n²/2" can have it evaluated
at eight points and get back "that fails at n = 3, here is the value" — which is precisely
what a working mathematician does and is currently available to approximately nobody below
graduate school. Verification stops being surveillance of the learner and becomes an
instrument the learner holds. `INFERENCE`.

**1.5 Assessment can ask for a derivation instead of an answer.**
Step-wise symbolic verification is measured to work: a symbolic weak-verifier on TPBench
"significantly outperforms existing test-time scaling approaches" and transfers to AIME
(arXiv:2506.20729, `MEASURED-BENCH`). C2's Tier 0 licence — *"you got 7 of 10 right"* —
requires only that the key be correct, and an independently-recomputed key is an L2b artefact
costing under a millisecond. The cheap rung makes the honest score claim free.
> **Guardrail.** C2 §10.4 is unmoved by any of this. A verified key licenses Tier 0 and
> nothing above it. Calibration needs human response data; there is no synthetic substitute.

**1.6 A curriculum can be checked against itself.**
With a claim DAG (F3 §10) and L2b at 0.4 ms, every formula in a course can be instantiated at
shared numeric points and cross-checked for mutual consistency — the chapter-7 constant
against the chapter-3 constant, the worked example against the stated theorem. Nobody has
published this. It is a buildable experiment and it is the first thing G1's reference
implementation should ship. `INFERENCE`.

**The one-sentence version.** *Cheap, binding, legible verification does not mainly stop a
tutor being wrong; it lets a tutor stop performing certainty.*

---

## 2. The invariant — what makes these four stories one story

F3 verifies formulas with a CAS. C1 verifies figures with a schema and a renderer. C2
verifies assessment items against a cognitive model and human response data. G2 arbitrates
between agents by putting executable ground truth above every vote. These read as four
unrelated engineering programmes. They are one, and the unification is not cosmetic — it
tells you exactly what each of them is doing wrong when it fails.

> ### G1-INV — the grounding invariant
>
> A claim is **grounded at rung R** if and only if all four hold:
>
> 1. **DECLARATION.** The model emitted a *finite, parseable object that fully determines the
>    claim* — an expression tree, a Vega-Lite spec, an item plus its key and attribute
>    mapping, a formal statement. Not prose *about* the claim.
> 2. **INDEPENDENCE.** An **arbiter** maps that declaration to `{PASS, FAIL, ABSTAIN}`, and
>    the arbiter shares no weights, no prompt, and no training signal with the generator.
> 3. **BINDINGNESS.** The verdict is *consequential*: `FAIL` withholds the artefact,
>    and `ABSTAIN` is not `PASS`.
> 4. **LEGIBILITY.** The verdict and the declaration travel with the artefact, in a form the
>    learner can read and re-run.
>
> **The rung is defined by the arbiter, not by the medium.** That is the whole unification.

Each of the four source sections is a discovery of exactly one of these conditions, arrived
at independently:

| Condition | Where it was discovered | The failure it names |
|---|---|---|
| **Declaration** | C1 §4.3 — "the model MUST NOT compute layout coordinates"; nine independent groups converged on emit-an-IR (ALGOGEN **82.5% → 99.8%**, arXiv:2605.12159, `MEASURED-BENCH`) | Hand-written SVG has no declaration: the claim is entangled with its rendering, so nothing can be checked but well-formedness |
| **Independence** | G2 §2.1 — no majority voting, no synthesis, judge from a different model family (self-preference is causally linked to self-recognition, arXiv:2404.13076, `MEASURED-BENCH`); C1 §5.4 — the blank-image ablation | A checker correlated with the generator shares its errors and reports agreement as confirmation |
| **Bindingness** | F3 §8.3 rule 4 — `ABSTAIN ≠ PASS`; F3 §8.3 rule 6 — a failed claim is withheld, not downgraded to prose | Silent downgrade is how L0 content acquires L3 credibility |
| **Legibility** | F3 §8.3 step 3 (tier badge); C1 §9.3 ("tier is a property of the artifact, displayed to the learner"); C2 §10.4 (the tier is a property of π); G2 §1.3 (grounding tier on the role card) | An unlabelled verified claim and an unlabelled unverified claim are the same object to a learner |

`INFERENCE` — the four conditions are *jointly* necessary, and each of the four sections
ships a documented failure that violates exactly one:

- Violating **Declaration**: PlantUML generation reaches **91.5% syntactic validity** and
  "all LLMs produced valid PlantUML diagrams adhering to UML conventions" while showing
  "inconsistencies in annotations and signatures" (arXiv:2605.24453, arXiv:2506.00788,
  `MEASURED-BENCH`). The grammar was checkable; the *content* was not declared, so nothing
  checked it.
- Violating **Independence**: Mirage — a **blank image leaves Pass@k unchanged or higher**
  (arXiv:2604.27969, `MEASURED-BENCH`). The VLM checker was not looking at the artefact.
- Violating **Bindingness**: Quarto's `freeze` means the most widely adopted executable-
  document toolchain in science *does not execute your notebook by default* (F3 §3.5,
  `OBSERVED`). The verdict has no consequence, so there is no verdict.
- Violating **Legibility**: C2 §10.4 — *"Most AI tutoring systems in 2026 are [at Tier 0]
  and report as if they were at Tier 2."*

**The corollary that matters most.** Because the rung is defined by the arbiter, the ladder is
**modality-independent**, and the interesting structural fact drops out immediately:

> **`INFERENCE` — the top rung is machine-decidable only in the deductive modality.**
> For formulas, L4's arbiter is a proof kernel. For figures, C1's L4 requires "an external
> dataset ground truth **and a named human reviewer of record**." For assessment, C2's Tier 3
> requires human response data, documented equating, and an independent validity study —
> *"the marginal cost of item calibration is exactly zero times zero"* (C2 §0). For agent
> disagreement, G2's Tier 4 is *escalate to a human*.
>
> This is not a tooling gap that better models will close. It is the difference between
> claims whose truth condition is internal to a formal system and claims whose truth
> condition is empirical. **Machines can climb the whole ladder only where the ladder is
> made of axioms.** Everywhere else the top rung is the world.

---

## 3. THE G1 LADDER — canonical

### 3.1 The rungs

Six rungs, ordered by strength of guarantee. Each rung is named for **its arbiter**. L2 splits
into two orthogonal sub-rungs because F3 §4.2 measured them catching disjoint error classes at
comparable (negligible) cost.

| Rung | Name | Arbiter | The declaration it consumes | What a `FAIL` means |
|---|---|---|---|---|
| **L0** | **Asserted** | none | — | — |
| **L1** | **Attested** | source text + entailment check | claim ↔ source span | The source does not say this |
| **L2a** | **Typed** | type / unit / schema algebra | every symbol's declared kind and unit; or a spec schema | The artefact is not even type-correct |
| **L2b** | **Instantiated** | an interpreter, at sampled points | an executable instance + seeds + tolerance | The two things disagree at a point you can look at |
| **L3** | **Normalised** | a decision procedure (CAS zero test, IR diff, constraint solver) | a symbolic object | They are not equal as symbolic objects |
| **L4** | **Proved / Calibrated** | a proof kernel (deductive) **or the world** (empirical) | a formal statement, or a design plus response data | It does not follow / it does not replicate |

### 3.2 Cost, coverage, and when to escalate — the canonical table

All figures are measured or sourced. Costs marked `†` are original measurements from this
section (§3.4); the remainder are carried forward from F3 §8.2.

| Rung | What it checks | What it **cannot** check | Measured cost | Measured coverage / recall | Escalate when |
|---|---|---|---|---|---|
| **L0** Asserted | nothing | everything | 0 | recall **0%** | always, unless the claim is on §6.4's declared-unverifiable list *and is labelled as such* |
| **L1** Attested | that a named source supports the claim | whether the source is right; whether the claim is *responsive* to the question | ≈$10⁻⁴–10⁻³, 0.3–3 s | fact-check accuracy **39–77%**; automatic attribution evaluation itself only **~80% macro-F1** (arXiv:2605.06635; arXiv:2402.15089) | never scale retrieval depth: fact-check accuracy falls **~42%** from k=2 to k=150 |
| **L2a** Typed | dimensional homogeneity; transcendental arguments dimensionless; schema conformance; declared-scope presence | any error that preserves type — sign, coefficient, 2π vs 1 (ω vs f), torque vs energy | **0.07 ms** median | **100%** on exponent / dropped-term / wrong-variable; **0%** on sign / ×2 / ÷2; **0/14** false alarms; applies to ~50% of the F3 corpus (only dimensioned claims) | **never a sufficient check.** Mandatory gate; may reject, may never accept |
| **L2b** Instantiated | agreement of two expressions at sampled points; independently recomputed plot curves; independently recomputed answer keys | universals ("for all n"); anything not instantiable; anything outside the sampled domain | **0.38 ms** median at k=1 †, 0.49 ms at k=8 † (F3 measured 0.61 ms at k=8 on its own harness); p95 **0.93 ms** at k=1 † | **112/113 = 99.1%** recall, identical at k=1 and k=16 †; **0/37** false alarms in the declared domain † | on `ABSTAIN`; on a universal quantifier; on reuse ≥ ~100×; on blast-radius ≥ 3 |
| **L3** Normalised | symbolic equality; IR-vs-spec diff; constraint satisfaction | anything outside the decision procedure's competence — and it cannot tell you when it is outside | **1.8 ms** median, 10.8 ms p95, **unbounded worst case** | **100%** in-domain (113/113); but SymPy fails **152/397 = 38.3%** of the Wester suite, with three sections unimplemented — 57–70% failure in sums, definite integrals, transforms | on `ABSTAIN`. **`simplify(e) ≠ 0` never means `e ≠ 0`** (Richardson): L3 emits `PASS` or `ABSTAIN`, never `FAIL` |
| **L4** Proved / Calibrated | that a formal statement follows from axioms; or that a design replicates against human data | **whether the formal statement means the informal one** — the 36% gap; whether the design measures the construct | **<$0.01** mathlib-native → **4M tokens/problem** → 3 days → 11 person-years (Flyspeck). Empirical L4: several hundred examinees, irreducible | ~90% competition; **60–88%** UG in mathlib idiom, **−26 pts** off-idiom; **16–35%** college physics; ~0 applied/numerical; end-to-end from prose **36%** | L4 does **not** subsume L1. Every L4 result needs a statement-fidelity check above it (§5) |

**Six facts a reader should take from this table.**

1. **L2 costs under a millisecond and catches ~99% of derivation errors.** There is no
   argument — economic, engineering, or pedagogical — for ever shipping an L0 formula.
2. **L2a and L2b are orthogonal, not redundant.** Dimensional analysis is 100%/0% by error
   class; numeric is ~99% overall. Together they cost about 0.5 ms. Run both.
3. **The default is L2b and the escalation is L3, not the reverse.** This inverts the usual
   instinct and it is F3's measured result: L3 buys +0.9 points of recall for ~3× the cost
   and carries a 38.3% hole located precisely in the domains where physics and engineering
   teaching lives.
4. **`ABSTAIN` is not a degenerate case; it is most of the ladder's honesty.** L3 cannot emit
   `FAIL`. L2a cannot emit `PASS`. L2b must abstain on non-finite values. A pipeline that
   collapses `{PASS, FAIL, ABSTAIN}` to a boolean has destroyed the guarantee, not compressed
   it.
5. **L4's cost spans nine orders of magnitude**, so the routing question is never "how
   important is this claim" but "**is this claim already formalisable in the idiom the library
   has?**"
6. **The rungs are not a staircase to be climbed.** The ladder is a **router**. Climbing past
   the rung that can falsify a claim buys nothing and costs a great deal.

### 3.3 The same ladder, all four modalities

This is the table the survey has been missing. Rows are rungs; columns are what the rung
*is*, concretely, in each modality. Sources: F3 §8, C1 §5/§9.3, C2 §10, G2 §2.2/§8, F10 §11.

| Rung | **Formula / derivation** (F3) | **Figure / diagram** (C1) | **Assessment item** (C2) | **Multi-agent claim** (G2) | **Explanation rung** (F10) |
|---|---|---|---|---|---|
| **L1** Attested | claim ↔ source span + entailment verdict | data provenance cited; alt text present and emitted *from the IR*, not from pixels | key and rationale traced to a named source; distractor traced to an *attested* error | claim cites a primary source; scope precedence names a role of record | every proposition traceable to the rung above |
| **L2a** Typed | unit algebra; every additive term homogeneous | schema validation + C1 §5.2's assertion set: no label collision, canvas containment, arrows anchored, axis scale/limits/zero-baseline, unit present, contrast ≥ 4.5:1, second encoding channel | template/constraint conformance; option order randomised; NOTA forbidden unless the cognitive model requires it | role-card `may_assert` enforced **at the interface, not the prompt** | scope-flag present for every drop; **ontology test** (thing / direct process / emergent process) |
| **L2b** Instantiated | 8 (in fact 1 — §3.4) random substitutions, rtol 1e-9 | **independent recomputation of every plotted curve** — the only check that catches the wrong-curve class; round-trip atomic QA over pre-authored answers | key recomputed by a solver that is not the generator; item solved by a program | **T0: executable ground truth wins outright — CAS, unit test, proof checker, cited source. No agent votes.** | entailment test on instantiated cases |
| **L3** Normalised | CAS zero test with declared assumptions | IR diff vs the requested spec; ASP/Draco constraint check (LLM substitutes measured at **F1 ≤ 0.82 common, < 0.15 subtle**) | isomorphy diagnostic (DCIF) on the *family*; within-family parameter variance σ²ᵢ:g estimated and published | judge that **selects, never synthesises**, from a different model family, with published calibration | full entailment: rung *n* ⊨ rung *n+1* under the declared scope |
| **L4** Proved / Calibrated | proof kernel + statement-fidelity check | **named human reviewer of record** + external dataset ground truth | field calibration against human response data; documented equating; subgroup invariance; independent validity study | **escalate to a human** | expert sign-off; measured transfer |

Three things this table makes visible that none of the four sections could see alone:

- **C1's tier semantics were provisional and can now be reconciled.** C1 §9.3 flagged that it
  was proposing figure-tier semantics before F3 existed. Under G1-INV the reconciliation is
  mechanical: C1's "L1 well-formed" is **L2a** (schema is a type system), C1's "L2 structurally
  sound" is **L2a complete**, C1's "L3 semantically verified" splits into **L2b** (recompute
  the curve) and **L3** (IR diff), and C1's "L4" is the empirical top rung. The renumbering
  matters because C1's rule *"a figure below L2 may not be shown to a learner"* becomes, in
  G1 numbering, *"a figure below L2a-complete may not be shown to a learner"* — which is the
  same rule and is now stated in the survey's one vocabulary.
- **G2's arbitration ladder is the G1 ladder read as a precedence order.** G2 §2.2's T0 is
  "executable ground truth wins outright" — that is L2b/L3, doing double duty. The
  architectural consequence G2 draws is the right one: T0 costs **zero LLM tokens**, which is
  why it is both the most reliable and the cheapest tier.
- **F10's fidelity rule is the L2a/L3 pair for the explanation modality**, and it is the only
  place in the whole survey where somebody wrote down a machine-checkable specification for
  *pedagogical* correctness. §6 argues this is more important than it looks.

### 3.4 Original measurement — the cheap rung is cheaper than F3 thought, and 8 samples buy nothing

`MEASURED-BENCH` · **Original, this section.** Harness:
`evidence/G1-L2b-abstention-and-budget.py`, run against F3's corpus (20 reference formulas,
37 semantically-equivalent rewrites, 113 mutants across six error classes). SymPy 1.14.0,
Python 3.12, single core. Reproduce: `python evidence/G1-L2b-abstention-and-budget.py`.

**(a) F3's prescribed abstention fix works exactly as specified and costs nothing.**
F3 §4.2 finding 3 reported one numeric miss — the Lorentz-factor `wrong_variable` mutant
substitutes `v → c`, both sides evaluate to complex infinity, and the checker compared two
degenerate values and reported *agreement*. F3 prescribed the fix (non-finite ⇒ `ABSTAIN`)
but did not run it. We ran it:

| Guard | caught | **silent misses** | abstentions | false alarms on 37 equivalent rewrites |
|---|---|---|---|---|
| F3 as published | 112/113 | **1** | 0 | 0/37 |
| non-finite ⇒ `ABSTAIN` | 112/113 | **0** | 1 | 0/37 |

The headline recall number is unchanged; **the number that matters — silent passes on wrong
claims — goes 1 → 0.** This is the ladder's whole thesis in miniature: the fix did not make
the checker more accurate, it made the checker's *ignorance* representable. Cost: nil.

**(b) `MEASURED-BENCH` — a null result. Eight random substitutions buy nothing over one.**

| Sampling domain | k=1 | k=2 | k=4 | k=8 | k=16 |
|---|---|---|---|---|---|
| narrow positive (F3's, `U(0.31, 0.87)`) — recall | **99.1%** | 99.1% | 99.1% | 99.1% | 99.1% |
| narrow positive — false alarms / 37 | **0** | 0 | 0 | 0 | 0 |
| narrow positive — median / p95 (ms) | **0.38 / 0.93** | 0.45 / 1.01 | 0.48 / 1.62 | 0.49 / 3.21 | 0.50 / 6.35 |

Recall is flat at 112/113 across a 16× sampling budget. The cost is not flat: p95 latency
rises **6.8×** from k=1 to k=16 for zero measured benefit. On textbook-scale expressions a
single random substitution is the entire signal, because the mutation classes that matter
(sign, factor, exponent, dropped term, wrong variable) perturb the value almost everywhere,
not on a measure-zero set. **`INFERENCE`:** k should be set by the *structure* of the claim —
a claim with a suspected removable singularity or a piecewise domain needs more points; a
polynomial identity does not — never by a fixed constant.

**(c) `MEASURED-BENCH` — a second null, and it inverts a natural instinct: sampling *wider*
makes the checker worse.**

| Sampling domain (k=8) | recall | false alarms / 37 |
|---|---|---|
| narrow positive `U(0.31, 0.87)` | 99.1% | **0** |
| wide positive `U(0.05, 20)` | 99.1% | **1** |
| signed `±U(0.05, 20)` | 99.1% | **2** (3 at k=4 and k=16) |

Widening the domain gained **zero** recall and cost up to **3 false alarms out of 37** —
rejections of *correct* rewrites. The mechanism is the same one F3 §2.2b identified from the
other direction: `√p·√q = √(pq)` and `log(exp z) = z` are true on the positive reals and false
off them, so a checker that samples outside the claim's declared domain is not being more
rigorous, it is **evaluating a different claim**. This gives the assumption rule a symmetric
partner:

> **The domain rule.** Numeric checking must sample *inside the claim's declared domain*.
> Adding assumptions until a check passes is laundering (F3 §2.2b); sampling outside the
> declared assumptions is manufacturing. Both are failures of the *declaration*, not of the
> arbiter — which is exactly what G1-INV predicts.

---

## 4. The routing table — which rung can falsify this claim most cheaply

Route by **claim type**, then apply cost modulators. Step 1 extends F3 §8.3 across all four
modalities; Steps 2–3 are unchanged from F3 and restated because G1 is the canonical location.

### Step 1 — classify the claim

| Claim type | Recogniser | Cheapest rung that can falsify it | Why not lower / not higher |
|---|---|---|---|
| Convention, definition, notation | no truth condition beyond authority | **L1** | Provenance *is* correctness. Higher rungs are inapplicable, not merely expensive |
| Empirical / historical / attributed fact | named entity, date, quantity from a source | **L1 with entailment** | "Link resolves" is 94%-grade theatre for 39–77%-grade truth |
| Numeric result | expression evaluates to a number | **L2b** | 0.38 ms, 99.1% recall. Never ship unchecked |
| Dimensioned physical relation | any variable carries units | **L2a + L2b** | Orthogonal error classes; both, always; together ~0.5 ms |
| Symbolic identity / derivation step | equation between expressions | **L2b**, escalate to L3 | L2b is cheaper and has no domain holes; L3 has a 38.3% hole exactly where teaching happens |
| Universal claim ("for all n", "always", "never") | quantifier over an infinite domain | **L3 minimum; L4 if reused** | The one place L2b is *categorically*, not probabilistically, insufficient |
| Algorithm / code claim | executable | **L2b as executed tests + assertions** | A printed output is not a check. Only **1.54%** of real notebooks contain any test |
| Simulation / dynamical claim | analytic form vs dynamics | **L2b via numerical integration** | Dumb by construction, therefore uncorrelated with the generator's error |
| **Plotted curve in a figure** | a function rendered as a line | **L2b — independently recompute f(x) and assert max deviation from `line.get_ydata()` < ε** | C1 §5.2: *"this catches the mathematically incorrect curve class outright and nothing else does"* |
| **Figure layout / label / axis / contrast** | any rendered geometry | **L2a — the §5.2 assertion set** | Deterministic, no model in the loop, targets every documented failure class in C1 §3.1–3.4 |
| **Figure semantics ("this arrow means X causes Y")** | a meaningful arrow | **L2a anchor assertion + mandatory human review** | C1 §9.4: an arrow *is* a claim; anchor errors are measured; no automated gate covers causal meaning |
| **Answer key of a generated item** | item + key | **L2b — recompute the key with a solver that is not the generator** | Licenses C2 Tier 0 and nothing more. Human review of keys is non-negotiable at Tier 3: measured key-error rates reach **45%** |
| **"This distractor represents misconception M"** | a diagnostic claim about a wrong answer | **empirical L4 only** | C2 prohibition 2: a model-generated plausible wrong answer carries **no** misconception information. Mine the error from response data or do not make the claim |
| **"Your ability is θ = 0.6 ± 0.3"** | a score on a scale | **empirical L4** | Requires C1–C3, C7, C10 of GAV-1. Item-sampling variance must be in the interval; almost no shipping system does this |
| **Disagreement between two agents about a fact** | conflicting assertions | **L2b/L3 as G2's T0** | Executable ground truth wins outright, costs zero LLM tokens, and no agent votes |
| **Disagreement about which explanation is better** | conflicting assertions, no truth condition | **G2 T3 (learner judges) — only over a T0-verified answer set**; else L0, labelled | Judges are worst exactly here. Never stage a debate where one side is factually wrong |
| **A simplification / ELI-n rung** | an explanation that drops detail | **L2a: scope flag present + ontology test; escalate to L3 entailment** | F10 §11.4. See §7 — this is the row that moves "omission" off the unverifiable list |
| Intuition, analogy quality, motivation, sequencing, "why this matters" | F3 §7 | **L0, explicitly labelled** | Verification is inapplicable. Label it; do not launder it |

### Step 2 — cost modulators (carried from F3 §8.3, unchanged)

1. **Reuse.** Escalate one rung per ~100× in expected readership.
2. **Blast radius.** Escalate one rung if the claim is a premise of ≥3 downstream claims.
3. **Irreversibility.** Escalate one rung if the claim will be *memorised* (a reference card,
   a spaced-repetition item — F11). Remembered-wrong is expensive to unlearn.
4. **Abstention.** `ABSTAIN` propagates as `unverified`, never as `passed`.
5. **Assumption.** Assumptions needed to make a check pass are part of the claim and must be
   stated in the explanation.
6. **Domain** (new, §3.4c). Sample inside the declared domain; sampling outside it
   manufactures false alarms.
7. **Downgrade.** A claim that fails its required rung is **withheld**, never quietly
   demoted to prose.

### Step 3 — what ships

Every claim carries a machine-readable rung badge plus a pointer to the artefact that
justifies it: source span + entailment verdict (L1); unit trace (L2a); seeds, domain and
tolerance (L2b); CAS certificate and assumption set (L3); proof-term hash or calibration
study (L4). **The badge is the contract with the learner** — §7.3 specifies what it must say.

---

## 5. Composition is the unsolved problem

### 5.1 The generalisation of F3's central negative

F3's most important number: **97% autoformalization × 69% proving = 36% end-to-end**
(arXiv:2511.03108, `MEASURED-BENCH`), with the loss traced to formal/informal discrepancies in
"more than half" of miniF2F's problems. F3 stated it as a fact about Lean. It is a fact about
*chains*.

> ### G1-COMP — the composition rule
>
> Chaining a verified stage A into a verified stage B produces **three** verification
> obligations, and the field routinely ships two:
>
> 1. `wellformed(A.out)` — A's output is legal in A's target language. **Usually checked.**
> 2. `correct(B.out | B.in)` — B's output is correct with respect to B's input. **Usually
>    checked; this is the strong guarantee everyone quotes.**
> 3. **`fidelity(A.in ⟷ A.out)` — A's output *means* what A's input meant.** An entailment
>    obligation that straddles two semantics and therefore belongs to *neither stage's*
>    verifier. **Usually unchecked, and silently assumed to equal 1.0.**
>
> End-to-end accuracy is bounded by the product, and in practice it is *dominated by the term
> nobody measures*.

**The arithmetic, done.** `INFERENCE` over `MEASURED-BENCH` inputs: if the pipeline is
0.97 × 0.69 = 0.669 on the two checked obligations and measures 0.36 end-to-end, the implied
statement-fidelity rate is **0.36 / 0.669 ≈ 0.54**. That is an independent estimate, from the
arithmetic alone, that formalizations are faithful about **54%** of the time — and it lands on
top of the paper's own qualitative finding of discrepancies in "more than half" of problems.
Two routes, one number. The fidelity term is not a rounding error; **it is the largest term in
the product.**

### 5.2 The same law in three other modalities, with numbers

This is the payoff of the unification: once you know to look for obligation 3, you find it
already measured, under different names, in every section.

| Chain | Obligation 1 (checked) | Obligation 2 (checked) | **Obligation 3 — fidelity** | Measured fidelity rate |
|---|---|---|---|---|
| **Prose → formal statement → proof** (F3) | statement type-checks | kernel accepts the proof | does the formal statement mean the prose? | **≈54%** (`INFERENCE` from arXiv:2511.03108) |
| **Concept → declarative IR → render** (C1) | schema validates — **91.5%** syntactic validity, "all LLMs produced valid PlantUML" | renderer is deterministic and always correct | does the IR encode the intended figure? | **not measured**; the qualitative finding is "inconsistencies in annotations and signatures" and *"content you still cannot trust"* (arXiv:2506.00788) |
| **Cognitive model → item template → instance** (C2) | template conformance | key is correct | do instances of this family measure the same attribute at the same difficulty? | **≈39%** — the share of *expert-built* templates that pass isomorphicity without revision (ERIC EJ1357630) |
| **Simple rung → detailed rung** (F10) | rung is well-formed prose | detailed rung is itself verified | is the simple rung entailed by the detailed one under a declared scope? | the fidelity rule (F10 §11) — **untested**, F10 says so |

`MEASURED-BENCH` · The corroborating audit: arXiv:2606.14000 built a three-dimensional audit
over agent-formalized numerical analysis and found *"recurring unfaithful formalization
patterns, including incomplete multi-part statements, added weakening hypotheses, and
parameter restrictions, that kernel acceptance entirely obscures,"* concluding
*"compilation-based metrics substantially overstate formalization quality."* **The strongest
available guarantee has a systematic blind spot in the direction of over-reporting.** That is
obligation 3 failing while obligations 1 and 2 pass, described in the language of the domain
that discovered it.

### 5.3 What the fidelity check must actually be

The mistake to avoid is trying to *verify the translator*. Compiler verification has been
here, and it has two answers, of which only one is affordable: prove the compiler correct
once (CompCert, decades), or **validate each translation as it happens** — *"End-to-End
Translation Validation is the problem of verifying the executable code generated by a compiler
against the corresponding input source code for a single compilation"* (arXiv:2403.05302,
`OBSERVED`). No autoformalizer, item generator, or IR emitter will be proved correct. **Every
one of them can be asked to produce a per-instance certificate.**

> ### RTF — the round-trip fidelity check
>
> For any interface A.in → A.out:
>
> 1. **Author an atomic question set against A.in, *before* the translation**, whose answers
>    are specified in advance. This is C1 §5.5's CharTide design, which is the only
>    round-trip protocol in the four sections that is honest, precisely because the questions
>    and answers are fixed before generation: *"information invariance — a downstream model
>    should yield consistent answers to identical visual queries"*, scored by a **frozen**
>    inspector on answer accuracy rather than by a judge (arXiv:2604.22192, `MEASURED-BENCH`).
> 2. **Ask the same question set of A.out**, in A.out's own language — evaluate the formal
>    statement, query the IR, solve the generated item, instantiate the simplified rung.
> 3. **Require identical answers.** Disagreement is a fidelity `FAIL`; unanswerable is
>    `ABSTAIN`.
> 4. **Only ask about identifiable quantities.** A boxplot does not contain its samples; a
>    histogram does not contain its observations; asking a round-trip checker to recover them
>    *"encourages hallucination and over-specified code generation"* (arXiv:2607.04726,
>    `MEASURED-BENCH`). The same limit applies to formal statements: do not ask φ a question
>    that s never determined.
> 5. **Back-translation alone is not enough.** Translating φ back to prose and comparing is
>    an L1 entailment check performed by a model correlated with the one that produced φ —
>    G1-INV condition 2, violated. Use it as a *supplement* to the frozen question set, never
>    as the check.

**The measured warning that governs step 5.** Autoformalization is not robust to paraphrase:
semantically-preserving rewrites of miniF2F and ProofNet statements produce *"performance
variability across paraphrased inputs"* (arXiv:2511.12784, `MEASURED-BENCH`). A learner who
rephrases the question gets a different formalization — so the fidelity check must be anchored
to a **fixed, pre-authored** artefact, not to whatever prose happens to be in the context
window.

**Ruling for the survey.** *No chain of verified stages may be reported as verified end-to-end
unless every interface carries an RTF certificate.* Composite claims of the form "97%
formalization and 69% proving" are, absent obligation 3, **not claims about the pipeline at
all.**

---

## 6. Pressure-testing the hard boundary — is omission really unverifiable?

F3 §7 lists intuition, analogy quality, pedagogical appropriateness, sequencing, "why this
matters", and **the choice of what to omit** as unverifiable in principle. The brief asks
whether the omission row survives contact with F10's fidelity rule. **It does not, and the
row should be split. This is G1's substantive disagreement with F3.**

### 6.1 The position

> **Omission is verifiable relative to a declaration and unverifiable absolutely.**
> The claim "a perfectly verified explanation of the wrong 20% is a failure no tier detects"
> is true only of systems that never declared what the right 80% was. It is a *statement about
> missing declarations*, not about the limits of verification — and G1-INV's first condition
> already says that a missing declaration is a missing rung, not an unverifiable claim.

### 6.2 The argument

Split "choice of what to omit" into three claims that behave completely differently.

**(a) Omission that falsifies — machine-checkable at L2a, and it is the class that causes
harm.** F10 §11.3 is a list of five properties a simplification may **never** falsify. Every
one of them is a property of the *pair* (rung n, rung n+1) and every one of them is decidable
given both rungs:

| F10 invariant | Check | Rung |
|---|---|---|
| **Quantifier strength** — "all" asserted where only "some" holds | parse the quantifiers of each proposition in rung *n*; compare against the matching proposition in rung *n+1*. Syntactic, with an NLI backstop | **L2a** (syntactic) / L1 (NLI) |
| **Sign or direction of a causal relation** | extract the signed relation from both rungs; compare. This is relation extraction, not judgement | **L2a** |
| **Uniqueness of a mechanism** — "*the* mechanism" where several exist | definite-article / exclusivity detection in rung *n* against an enumeration in rung *n+1* | **L2a** |
| **Existence of a boundary** — implying a model is unrestricted when it is not | **set difference** over declared scopes. Fully decidable *if* scopes are declared | **L2a** |
| **Ontological category** — thing / direct process / **emergent** process | a classifier over both rungs; agreement required. Probabilistic, so it is a sampled check, not a decision procedure | **L2b-grade** |

F10 is explicit about why these five and not others: Chi 2005's result is that misconceptions
*across* ontological kinds are robust and *within* kinds are repairable, and the
classical-quantum hybrid population was measured **unchanged across a semester** of university
chemistry (ERIC EJ1442536, `MEASURED-BENCH`). So this is not a checklist of aesthetic
preferences. **It is the machine-checkable subset of "which omissions produce non-repairable
damage," and it is grounded in the only empirical result in the survey that says which
misconceptions do not wash out.**

F10 states the operational consequence more sharply than F3 does: *"undeclared drops are, at
retrieval time, indistinguishable from planted misconceptions."* An undeclared omission is not
an editorial judgement the checker cannot reach. **It is a type error**, and G1 routes it to
L2a.

**(b) Omission of required coverage — checkable as a set difference against a blueprint.**
"Did the artefact cover what it was supposed to cover?" is a set-cover computation, and
assessment has been doing it since the 1950s under the name *table of specifications* / test
blueprint. C2 makes the same object mandatory and moves it *before* generation: **H3 — the
cognitive model / Q-matrix, before generation, is where all construct validity now lives**
(C2 §10.3). Applied to explanation rather than assessment, the identical artefact turns
coverage omission into a diff. F3's own §7 concedes the mechanism in its right-hand column —
"coverage against a syllabus" — and then leaves the row in the unverifiable table anyway.
`INFERENCE`: that is an inconsistency in F3, not a finding.

**(c) The choice of the declared scope itself — genuinely, permanently unverifiable.**
Whether *this* syllabus is the right syllabus. Whether the 20% you declared out of scope was
the 20% that mattered. This is a claim about what is worth knowing; it is not truth-apt, and
it belongs with "why this matters" in F3 §7's bottom row. **The residue is one line long.**

### 6.3 The generalisation — the declaration move

The pattern that rescues omission rescues a second row of F3 §7, and it is the most useful
idea in this section:

> **`INFERENCE` — the declaration move.** Many properties that look unverifiable become
> verifiable when you require the author to **declare the thing that would falsify them**.
> You cannot check whether an analogy is *good*. You can check that it shipped with a
> declared **alignment set** and **limit set** (F10 §11.4), that the limit set is non-empty,
> and that no proposition in the alignment set contradicts the target concept's ontology.
> You cannot check whether an omission was *wise*. You can check that it was declared and
> that it falsified none of F10's five invariants.
>
> **Verification does not need ground truth. It needs a commitment.**

**The obvious attack, and why the design survives it.** A declaration can be gamed: declare a
trivially narrow scope and every fidelity check passes. This is real and it is why the two
checks must be run as a *pair*. Narrowing the declared scope to escape a fidelity failure
mechanically produces a **coverage** failure against the blueprint (b). The two checks pull in
opposite directions, which is exactly the property that makes a pair of checks sound where
either alone is gameable. `INFERENCE`.

### 6.4 The revised boundary table

Replacing F3 §7's table for the four rows that change:

| Property | F3 §7 verdict | **G1 verdict** | Rung |
|---|---|---|---|
| Choice of what to omit | unverifiable | **split.** Falsifying omission → checkable against F10's five invariants; coverage omission → set difference against a declared blueprint; *choice of blueprint* → unverifiable | **L2a / L2b**, residue at L0 |
| Analogy quality | unverifiable | **split.** "Is it a good analogy" → unverifiable. "Does it ship a non-empty declared limit set consistent with the target ontology" → checkable | **L2a**, residue at L0 |
| Sequencing | unverifiable | unchanged — a DAG can be checked for cycles; whether it is the *best* order is empirical | **L0**, A/B measurable |
| Intuition quality; "why this matters"; motivation and tone | unverifiable | **unchanged. Genuinely not truth-apt.** Declare as authored opinion | **L0, labelled** |

**And the sentence F3 got exactly right, which nothing above weakens:** *verification is a
floor, not a quality.* A fully L4 explanation can be badly sequenced, pitched wrong, and
pointless. Grounding removes a failure mode; it never adds a virtue.

---

## 7. The trust boundary, stated precisely

F3: *"Formal verification moves the trust boundary; it does not eliminate it."* True, and
under-specified. Here is exactly where it moves to.

### 7.1 What each rung still trusts

| Rung | Verifies | **Still trusts** |
|---|---|---|
| **L1** | that the span entails the claim | that the source is right; that the *relevant* span was retrieved; the entailment model (**~80% macro-F1**, arXiv:2402.15089) |
| **L2a** | unit homogeneity | that each symbol's declared unit is the right unit — and units do not distinguish **kind**: torque vs energy (N·m), entropy vs heat capacity (J/K), ω vs f (s⁻¹, a factor of 2π) (arXiv:1807.07643, `MEASURED-BENCH`). Also the notation → expression-tree translation |
| **L2b** | agreement at sampled points | that the sampled domain is the *declared* domain (§3.4c); that non-finite results abstain; the same notation → expression-tree translation |
| **L3** | symbolic equality | that the assumption set is the claim's own and was not added to make the check pass; that `ABSTAIN` was not read as `FAIL` (Richardson) |
| **L4 deductive** | derivability from axioms | that the formal statement means the informal one (**≈54%**, §5.1); that the library's definitions are the *course's* definitions (**−26 pts** off-idiom, TaoBench); the kernel and its elaborator |
| **L4 empirical** | that the design replicates | that the construct is the construct; that the calibration sample resembles this learner |

### 7.2 Where it moves to — one sentence

> **Every rung of the ladder verifies a declaration. No rung verifies the declaring.**
>
> The trust boundary moves from *the model's fluency* — an unbounded, undiagnosable surface —
> to *the map from the learner's world into the checker's world*: the units you assigned, the
> symbols you bound, the source you selected, the domain you declared, the formal statement
> you wrote, the scope you announced. That surface is **small, enumerable, auditable, and the
> same object at every rung.** Which is the whole point. You have not eliminated trust; you
> have compressed it into a finite list a human can review, and you have made every item on
> that list something the learner can be shown.

`INFERENCE`, and it is the section's thesis. Note that it explains, without further
machinery, why the four sections' hardest problems are the same problem: the autoformalization
gap (F3), "the IR does not encode the intended figure" (C1), the Q-matrix retrofitting problem
(C2), and shared-state semantics between agents (G2) are all **failures of the declaration,
observed through four different arbiters.**

### 7.3 What the learner must be told

A badge that says "✓ Verified" is worse than no badge, because it transfers the arbiter's
narrow guarantee onto the whole artefact — the precise error C2 documents in the field
(*"most AI tutoring systems are at Tier 0 and report as if they were at Tier 2"*). Five
requirements:

1. **State what was checked, operationally, in one sentence a twelve-year-old can read.**
   Not "L2b verified" but *"I checked this formula against 8 sets of numbers and it agreed
   every time."*
2. **State the declaration.** The units, the assumptions (`x > 0`), the domain sampled, the
   source chosen, the scope declared. **The assumption is part of the claim** — if
   `positive=True` was needed to pass, the learner is owed the positivity hypothesis.
3. **State what was not checked, by name.** *"Nobody checked whether this is the right
   explanation for you, or whether something important was left out beyond what I said I was
   leaving out."* This is not a disclaimer; it is the only thing that prevents the badge
   manufacturing exactly the misplaced confidence the ladder exists to prevent.
4. **Show `ABSTAIN`.** An explicit *"I couldn't check this"* is information. A missing badge
   is not. `{PASS, FAIL, ABSTAIN}` must reach the interface, not be collapsed to a boolean at
   the last layer.
5. **Make the verdict falsifiable by the learner.** Ship the check, not just its result. Let
   the learner change the numbers and watch it break. A verdict the learner can re-run is a
   claim; a verdict they cannot is an authority claim wearing a checkmark — and per §1.1,
   removing the authority claim was the point.

**The measured constraint on all of this.** Groundedness and comprehensibility trade off:
*"Humans prefer responses generated using RAG, but not when responses are too grounded in the
textbook content"* (arXiv:2310.03184, `MEASURED-RCT-adjacent`). The badge must never force the
explanation's register. **Ground the claim; do not ground the prose.**

---

## 8. Original experiment — the *pāṭha* protocol, benchmarked

I2 §9.2 proposed **permutation-based fidelity checking**: instead of re-asking a model the
same question k times, ask k *structurally different* questions about the same underlying
content — state it, invert it, evaluate it at boundary values, derive it backwards — and check
the answers against each other. The claim was that this is *"strictly stronger than
self-consistency sampling because the permutations are adversarial to semantic smoothing"*,
labelled `INFERENCE` and explicitly flagged **"for §F3 to benchmark."** Nobody had. We did.

### 8.1 Design

`MEASURED-BENCH` · Harness: `evidence/G1-patha-vs-selfconsistency.py`. Matched-budget,
two-condition design. 16 canonical formula claims (pendulum period, kinetic energy, escape
velocity, circle area, sphere volume, geometric series, compound interest, ideal gas, parallel
resistance, thin lens, Lorentz factor, spring energy, capacitor energy, de Broglie wavelength,
Coulomb's law, binomial variance). Each claim is run twice: once with the **true** relation
asserted in the model's context, once with a **plausibly corrupted** relation asserted (e.g.
`T = 2π√(g/L)`, `E = ½mv`, `V = np(1+p)`). This is the realistic tutor setting: the wrong
claim is already in the context window, and the question is whether the system can catch its
own earlier assertion.

Both protocols spend **exactly k = 6 generation calls** and both flag on the **same rule** —
"any probe answer disagrees with the asserted claim." The only difference is what the six
calls are:

- **Self-consistency (S):** six i.i.d. resamples of the *same* question at temperature 0.8.
- **Pāṭha (P):** six *structurally different* probes at temperature 0.2 — `forward` (restate),
  `inverse` (rearrange for another variable), `numA` / `numB` (evaluate at two numeric
  points), `scaling` (factor when one variable doubles), `zeroform` (write F such that F = 0 is
  equivalent). Each is a different function of the same relation: *krama*, *jaṭā* and *ghana*
  applied to a formula instead of a verse.

Every verdict is decided by a **deterministic SymPy comparator**. No LLM judges anything —
G1-INV condition 2 is respected by construction. Unparseable or undecidable probe answers
count as `ABSTAIN`, never as agreement.

### 8.2 Result — a clean negative, replicated on two models

`MEASURED-BENCH` · **768 generations across two models. gemma3:4b: 384 calls, 4.4 min, median
0.68 s. hermes3:8b: 384 calls, 3.4 min, median 0.51 s.**

| Protocol | Model | Recall (corrupted flagged) | False alarm (true flagged) | **Discrimination** |
|---|---|---|---|---|
| **Pāṭha, all 6 probes** | gemma3:4b | **14/16 = 87.5%** | **14/16 = 87.5%** | **+0.0 pts** |
| **Pāṭha, all 6 probes** | hermes3:8b | **16/16 = 100.0%** | **16/16 = 100.0%** | **+0.0 pts** |
| Self-consistency, k = 6 | gemma3:4b | 3/16 = 18.8% | 0/16 = 0.0% | **+18.8 pts** |
| Self-consistency, k = 6 | hermes3:8b | 7/16 = 43.8% | 0/16 = 0.0% | **+43.8 pts** |

**As specified in I2 §9.2, the *pāṭha* protocol is at chance — on both models, exactly.** It
flags corrupted claims and correct claims at *identical* rates. Self-consistency is a poor
detector (18.8% / 43.8% recall) that never cries wolf, and therefore wins on discrimination
by 18.8 and 43.8 points respectively.

**The scaling direction is the part to notice.** Going from 4B to 8B improved
self-consistency's discrimination by **+25 points** and improved *pāṭha*'s by **zero** — the
larger model simply flagged everything, in both conditions. A protocol whose false-alarm rate
rises exactly as fast as its recall does not get better with model scale; it gets *louder*.

### 8.3 Why — and it is the interesting part

The per-probe breakdown localises the failure exactly (recall − false alarm, per probe):

| Probe | gemma3:4b recall / FA | disc. | hermes3:8b recall / FA | disc. |
|---|---|---|---|---|
| `forward` (restate) | 3/16 / **0/16** | +18.8 | 6/16 / **0/16** | **+37.5** |
| `inverse` (rearrange) | 10/16 / 6/16 | **+25.0** | 7/16 / 6/16 | +6.2 |
| `numA` (numeric point A) | 5/16 / 6/16 | **−6.2** | 12/16 / 7/16 | **+31.2** |
| `numB` (numeric point B) | 6/16 / 3/16 | +18.8 | 11/16 / 9/16 | +12.5 |
| `scaling` (doubling factor) | 6/16 / 8/16 | **−12.5** | 11/16 / 8/16 | +18.8 |
| `zeroform` | 3/16 / 3/16 | +0.0 | 10/16 / 4/16 | **+37.5** |

**The permuted probes are harder tasks, and the model fails them whether or not the claim is
corrupted.** On gemma3 two of the six probes have *negative* discrimination — they fire more
often on correct claims than on corrupted ones. The protocol's signal is swamped by probe
difficulty, and the "any disagreement flags" rule aggregates six noisy detectors into one that
is exactly at chance.

**And the per-probe rankings do not transfer.** `inverse` is the best probe on gemma3 (+25.0)
and nearly the worst on hermes3 (+6.2); `numA` is the *worst* on gemma3 (−6.2) and among the
best on hermes3 (+31.2). Only `forward` — the un-permuted probe — is stable, and it is stable
because it is the only one both models can execute reliably (0/16 false alarms on both).
`MEASURED-BENCH`. **Any probe calibration is therefore per-model and per-version, not a
property of the protocol.**

**The diagnosis, stated as a general principle:** *permutation-based fidelity checking is
confounded with probe competence.* It detects "the model cannot do algebra" far more reliably
than it detects "the claim is corrupted." I2's mechanism argument — that structurally
different redundancy is not correlated with the original error — is *correct*, and is
precisely why it fails: the permuted probes have their own, independent, much larger error
rate.

### 8.4 The rescue, and its honest caveat

`MEASURED-BENCH` · We swept all 63 non-empty probe subsets on each model and took the best
(an **oracle**, selected on the same data it is scored on — see the caveat):

| Model | best oracle subset | recall | false alarm | disc. | self-consistency disc. |
|---|---|---|---|---|---|
| gemma3:4b | `forward + inverse + numB` | 81.2% | 43.8% | **+37.5** | +18.8 |
| gemma3:4b | `forward + numB` | 56.2% | 18.8% | **+37.5** | +18.8 |
| hermes3:8b | `forward + zeroform` | 75.0% | 25.0% | **+50.0** | **+43.8** |
| — | full 6-probe protocol as specified | 87.5–100% | 87.5–100% | **+0.0** | — |
| — | worst subset (gemma3, `numA + scaling`) | 62.5% | 81.2% | **−18.8** | — |

**Caveat, stated because it is the difference between a finding and an artefact:** the subsets
were selected *post hoc on the same 16 claims*. **These are oracle upper bounds, not
estimates.** And read the hermes3 row carefully: even with oracle probe selection, permutation
checking beats plain self-consistency by **6.2 points** on the stronger model — a margin that
requires a calibration set to obtain and that would not survive honest cross-validation at
n = 16. What is *not* oracle-selected, and is the robust result: the full protocol as
specified is at chance on both models, and two of six probes are worse than useless on one of
them.

### 8.5 The doctrine consequence

> **Every probe in a permutation-based checker must carry a measured false-alarm rate on
> known-true claims — measured per model and per version — and probes above threshold must be
> dropped.** An uncalibrated probe is, in G2's phrase, an unlabelled coin, and the *pāṭha*
> protocol as specified is six of them in a trench coat. The measured non-transfer of probe
> rankings between gemma3 and hermes3 (§8.3) means the calibration set is not optional
> infrastructure that can be amortised across deployments; it is a per-deployment artefact.

This is not a rejection of I2's proposal. It is the missing half of it, and it lands on the
same requirement G2 imposes on judges (*"published selection accuracy on a held-out
disagreement set, refreshed per model version"*) and C2 imposes on generators (*"the
accountable object is the probe policy π"*). **The pāṭha protocol is a probe policy and must
be calibrated as one.** Notably, that is exactly what the tradition did and the software
proposal omitted: the *vikṛti-pāṭha* forms were performed by reciters who had spent years
being drilled to execute the permutations flawlessly, so the permuted recitation's own error
rate was driven to near zero *before* it was used as a checksum. **The tradition calibrated
its probes. The software proposal skipped that step, and the step turns out to be the whole
protocol.** `INFERENCE`.

### 8.6 The corroborating literature

`MEASURED-BENCH` · arXiv:2502.15845, *"Verify when Uncertain: Beyond Self-Consistency in Black
Box Hallucination Detection"*: self-consistency-based detection methods *"perform nearly as
well as a supervised (black-box) oracle, leaving limited room for further gains within this
paradigm"*, and the gain comes from **cross-model** consistency — a genuinely different
information source, called only for cases inside an uncertainty band. This is the mechanism
I2 was reaching for, validated in the form that works: **the second opinion must come from a
different system, not from a different question put to the same system.** For G1 that is the
independence condition, restated: *a permuted probe answered by the same model is still the
same model.*

### 8.7 Limits of this experiment — stated plainly

- **Two small open-weight models, run locally.** gemma3:4b and hermes3:8b. A frontier model
  would have a lower probe-error rate and the protocol might separate — the 4B → 8B trend is
  not encouraging (self-consistency gained 25 points of discrimination; *pāṭha* gained zero),
  but two points do not make a curve. What the experiment establishes is that the protocol
  *as specified* has **no error budget for probe difficulty**, not that it can never work.
- **One domain.** Closed-form algebraic formulas. I2's proposal targets any verbatim-fidelity
  content (statutes, dosages, API contracts); those may have easier permutations.
- **n = 16.** The 95% binomial interval on 14/16 is roughly 62–98%. The *discrimination*
  claim is a paired result and the exact coincidence of recall and false-alarm on both models
  is strong; individual rates are wide.
- **The corruptions are single-operator.** Real semantic drift is subtler.
- **The comparator is strict.** A probe answer that is algebraically right but written in a
  form SymPy could not decide counts as `ABSTAIN`, not as agreement — 15–21 of 96 *pāṭha*
  probe answers per model. Abstentions do not create flags, so they depress *pāṭha*'s recall
  and its false-alarm rate equally; they do not explain the zero discrimination.

---

## 9. Negative and null results register

The editorial standard requires ≥1. This section has five, three of them original.

1. **`MEASURED-BENCH` (original) — the *pāṭha* protocol as specified is at chance, on two
   models.** 87.5% recall / 87.5% false alarm (gemma3:4b) and 100% / 100% (hermes3:8b) on 16
   corrupted-vs-true formula claims at matched k = 6. Plain self-consistency, which is a far
   *worse* detector (18.8% / 43.8% recall), has strictly better discrimination because it
   never false-alarms. Scaling the model improved self-consistency by 25 points of
   discrimination and *pāṭha* by zero. A falsifiable proposal from I2 §9.2, tested, and
   falsified in its stated form (§8).
2. **`MEASURED-BENCH` (original) — eight random substitutions buy nothing over one.** L2b
   recall is flat at 112/113 = 99.1% from k = 1 to k = 16, while p95 latency rises 6.8×. The
   standard "sample more points to be safe" instinct is inert on textbook-scale expressions
   (§3.4b).
3. **`MEASURED-BENCH` (original) — sampling a *wider* domain makes the checker worse.** Zero
   recall gained; up to 3 false alarms out of 37 correct rewrites introduced, because
   `√p·√q = √(pq)` is simply false off the positive reals. Rigour applied to the wrong object
   is not rigour (§3.4c).
4. **`MEASURED-BENCH` — self-consistency is a saturated paradigm.** Self-consistency
   hallucination detectors *"perform nearly as well as a supervised (black-box) oracle,
   leaving limited room for further gains within this paradigm"* (arXiv:2502.15845). More of
   the same information source is exhausted; the remaining gains require a *different* source.
5. **`INFERENCE` over `MEASURED-BENCH` — the composition arithmetic implies a fidelity rate
   of ≈54%, and that term is larger than either measured stage.** 0.36 / (0.97 × 0.69) ≈ 0.54.
   The single largest term in the end-to-end product is the one no stage's verifier measures
   (§5.1).

**Carried forward from F3, because G1 is where they now live:** declaring dependencies made
notebooks *less* reproducible (45.18% vs 31.24% import failures); more retrieval makes
citations *less* factual (−42% from k=2 to k=150); doubling the proof-search budget from k=32
to k=64 yields *zero* additional theorems; groundedness and student preference trade off
directly; kernel acceptance systematically overstates formalization quality.

---

## 10. What I could not verify

Stated so the reader can discount accordingly.

- **The Leanstral 1.5 figures are not used anywhere in this section, deliberately.** F3 §1.3
  established that the model card carries **no benchmark numbers at all — only a comparison
  image** — and that every quantitative claim (miniF2F 100%, PutnamBench 587/672) lives in
  the vendor launch post, with the only independent evaluation explicitly *"not
  compiler-verified."* G1's L4 row therefore quotes only independently-published numbers
  (DeepSeek-Prover-V2, Goedel-Prover-V2, Seed-Prover 1.5, TaoBench, LeanPhysBench). **No
  vendor number enters any G1 table.**
- **The C1 fidelity rate is not measured anywhere.** §5.2's table has a blank in the
  concept → IR row. The qualitative finding exists (valid diagrams, untrustworthy content);
  the *rate* does not. I could not locate one and do not estimate it.
- **The 39% template-isomorphicity figure is a share of expert-built templates**, not of
  LLM-generated ones. Using it as the fidelity rate for an LLM item generator is an
  extrapolation and is labelled as such in §5.2; the LLM number does not exist.
- **The ≈54% statement-fidelity rate is arithmetic**, `INFERENCE` over three measured inputs,
  not a direct measurement. It is corroborated by the source paper's independent qualitative
  finding ("more than half"), which is why it is offered at all.
- **G2's majority-voting 1-in-4 minority-discard figure and the 0.810 vs 0.179
  selection-vs-synthesis figure are `INTERNAL-PRIOR`** — G2 could not locate public papers
  with those exact numbers. G1 relies on the *direction* (no voting, selection not synthesis),
  which is externally corroborated, not on the magnitudes.
- **The permutation-benchmark result is on 4B and 8B open-weight models only.** I had no
  frontier-model API available in this environment. §8.7 states the limit; the result should
  be re-run before the survey generalises it beyond "the protocol as specified has no error
  budget for probe difficulty."

---

## 11. Open problems, and what G1 hands on

**Solved, and nobody is doing it.** Sub-millisecond dimensional + numeric checking catches
~99% of derivation errors with zero false alarms inside the declared domain. This requires no
research. It is the highest return-on-effort intervention in the survey, and §3.4 shows it is
*cheaper* than F3 estimated.

**Not solved, in priority order:**

1. **Statement fidelity at every interface (§5).** The largest unmeasured term in every
   pipeline in this survey. Needs: RTF certificates as a shipped artefact; cheap semantic
   fidelity metrics (GTED, arXiv:2507.07399, is a start); paraphrase-robust translation
   (arXiv:2511.12784 shows current models are not).
2. **Probe calibration for permutation checking (§8).** The measured blocker on I2's proposal,
   and the measured non-transfer of probe rankings across models makes it worse than it looks:
   the calibration is per-model, per-version, per-domain. Needs a held-out true-claim set per
   probe family with a published false-alarm rate. **Two weeks of work, and it would settle
   whether permutation checking survives at frontier scale.** The honest prior after this
   experiment is that it survives only as a *calibrated subset*, and that the surviving subset
   will be small.
3. **Kind-of-quantity checking (L2a's ceiling).** Unit-compatible-but-meaningless is a real,
   unaddressed class; off-the-shelf unit libraries do not do it (arXiv:1807.07643).
4. **Off-manifold formalization.** −26 points when a course builds its own definitions
   (TaoBench). A tutor following *a specific textbook* is exactly the off-manifold case.
5. **Curriculum-aware retrieval.** Every retriever ranks on semantic similarity; none ranks on
   "uses only prerequisites this learner has covered." The concrete fix for F3 §6.3's failure
   mode 3, and it connects to F5's learner model.
6. **The F10 fidelity rule is untested.** §6 argues it is the machine-checkable core of
   pedagogical correctness; F10 itself says nobody has run it. Building the five invariant
   checkers and measuring their agreement with expert judgement is the highest-value
   *pedagogical* verification experiment available.
7. **The self-consistency check of a whole curriculum (§1.6).** Unattempted, cheap, and
   likely to produce a startling number.

**Contract exported to the reference implementation:**

- Every claim carries `{rung, verdict ∈ {PASS, FAIL, ABSTAIN}, declaration, artefact-pointer}`.
  Collapsing the verdict to a boolean destroys the guarantee.
- Every *interface* between generation stages carries an RTF certificate, or the chain is
  reported as unverified end-to-end.
- The claim dependency DAG must exist: two of the seven cost modulators are functions of it.
- Substrate is a reactive notebook (marimo / Pluto class) executed in CI from a cold
  container, pinned deps inside the artefact, build fails on any cell error or assertion
  failure. Not Jupyter (4.03% self-reproduction), not Quarto-with-`freeze`.
- **L4 is not the goal.** The ladder is a router. In three of the four modalities the top rung
  is not a machine at all.

---

## Sources

**Inherited section anchors (the synthesis substrate)**
1. F3 — Executable & Verifiable Knowledge · `research/raw/F3-executable-verifiable.md` (76 sources)
2. C1 — Illustration & Diagram Generation · `research/raw/C1-illustration-generation.md`
3. C2 — Assessment Generation & Psychometrics (GAV-1) · `research/raw/C2-assessment-psychometrics.md`
4. G2 — Agent Village / arbitration precedence · `research/raw/G2-agent-village.md`
5. F10 — Explanation Laddering / the fidelity rule · `research/raw/F10-explanation-laddering.md`
6. I2 — Global Traditions / the *pāṭha* protocol · `research/raw/I2-global-traditions.md`
7. F5 — Learner model (recomputation guarantee); F11 — spaced repetition (irreversibility rule); H1 — SELPA guidance policy; F4 — reach economics

**New sources located for this section**
8. Beyond Self-Consistency in Black-Box Hallucination Detection — arXiv:2502.15845 · http://arxiv.org/abs/2502.15845
9. End-to-End Translation Validation (per-instance certificates, not verified translators) — arXiv:2403.05302 · http://arxiv.org/abs/2403.05302

**Load-bearing measurements cited in this section (all previously located by F3/C1/C2/G2/F10)**
10. miniF2F-Lean Revisited / the 36% composition result — arXiv:2511.03108
11. Formalization quality audit beyond kernel acceptance — arXiv:2606.14000
12. Autoformalization robustness to paraphrase — arXiv:2511.12784
13. GTED autoformalization metric — arXiv:2507.07399
14. TaoBench (−26 pts off-manifold) — arXiv:2603.12744
15. LeanPhysBench / PhysLib — arXiv:2510.26094
16. Cited but Not Verified (39–77% fact check; −42% with retrieval depth) — arXiv:2605.06635
17. AttributionBench (~80% macro-F1 auto-eval) — arXiv:2402.15089
18. RAG for math QA: groundedness vs human preference — arXiv:2310.03184
19. Step-wise symbolic verification / TPBench — arXiv:2506.20729
20. Physical-type correctness / kind-of-quantity — arXiv:1807.07643
21. Dimensionally inconsistent Size-Strain Plot across decades — arXiv:2512.00689
22. Program-aided reasoners know what they know (calibration) — arXiv:2311.09553
23. PAL — arXiv:2211.10435
24. AlphaEvolve (the generative model proposes; a program disposes) — arXiv:2511.02864
25. Inference-time diversity / mode collapse in Lean provers — arXiv:2601.16172
26. Ineq-Comp (compositional inequality failure) — arXiv:2505.12680
27. Pimentel et al., Jupyter reproducibility (4.03%) — https://leomurta.github.io/papers/pimentel2019a.pdf
28. Containerisation closes 66.7%, 53.7% still low-fidelity — arXiv:2604.01072
29. Wester CAS benchmark — https://www.math.unm.edu/~wester/cas_review.html
30. SymPy Wester suite (38.3% failing, measured 2026-07-27) — https://raw.githubusercontent.com/sympy/sympy/master/sympy/utilities/tests/test_wester.py
31. ALGOGEN (IR + deterministic renderer, 82.5% → 99.8%) — arXiv:2605.12159
32. Raiven (DSL → D3, 100% compilation) — arXiv:2604.10008
33. Flint (data semantic model) — arXiv:2607.20775
34. DiagramIR (IR-level comparison beats LLM-as-judge) — arXiv:2511.08283
35. GeoSVG-RL (six-dimensional browser-backed verifier) — arXiv:2605.25447
36. CharTide (frozen inspector, pre-authored atomic QA) — arXiv:2604.22192
37. SciFlow-Bench (round-trip inverse parsing) — arXiv:2602.09809
38. Round-trip identifiability limit — arXiv:2607.04726
39. Mirage (blank-image ablation) — arXiv:2604.27969
40. Viz-rules: LLM judges F1 ≤ 0.82 / < 0.15 vs symbolic solvers — arXiv:2602.20137
41. Misleading-visualisation VLM false positives — arXiv:2603.22368
42. PlantUML: 91.5% syntactic validity — arXiv:2605.24453
43. Nine-model PlantUML study (valid diagrams, untrustworthy content) — arXiv:2506.00788
44. SVGenius (systematic degradation with complexity) — arXiv:2506.03139
45. Socratic Chart (30% drop when labels removed) — arXiv:2504.09764
46. Draco / Draco 2 (design knowledge as ASP constraints) — arXiv:2308.14247
47. LLM evaluators favour their own generations — arXiv:2404.13076
48. Why do multi-agent LLM systems fail? (MAST, 14 failure modes) — arXiv:2503.13657
49. Debating with more persuasive LLMs (88% vs 60% human judges) — arXiv:2402.06782
50. Can LLMs generate novel research ideas? (self-evaluation failure) — arXiv:2409.04109
51. Chi 2005 ontological categories / robust misconceptions — via F10
52. Classical-quantum hybrid population unchanged across a semester — ERIC EJ1442536
53. Isomorphicity: ~39% of expert templates pass without revision — ERIC EJ1357630
54. AI-generated MCQ validity systematic review (not for unsupervised summative use) — doi:10.1093/postmj/qgag057
55. Distractors from model plausibility carry no misconception information — doi:10.18653/v1/2024.findings-naacl.193
56. UNESCO ICH, Tradition of Vedic chanting — https://ich.unesco.org/en/RL/tradition-of-vedic-chanting-00062

**Original measurements (this section, 2026-07-27)**
57. `evidence/G1-L2b-abstention-and-budget.py` — abstention fix (1 silent miss → 0) and sampling-budget sweep (k = 1…16 × 3 domains) over F3's 113-mutant / 37-rewrite corpus. SymPy 1.14.0, Python 3.12.
58. `evidence/G1-patha-vs-selfconsistency.py` — *pāṭha* permutation checking vs self-consistency, 16 formula claims × 2 conditions × 2 protocols × k = 6, deterministic SymPy comparator, local models via ollama. Raw per-generation logs committed at `evidence/G1-patha-results-gemma3-4b.json` and `evidence/G1-patha-results-hermes3-8b.json` (768 generations, every prompt, response, parsed expression and verdict). Reproduce: `ollama serve & ; python evidence/G1-patha-vs-selfconsistency.py --model gemma3:4b`.

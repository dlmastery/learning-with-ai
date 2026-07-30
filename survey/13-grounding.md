---
title: "Grounding — correctness that lives in the verifier"
section: grounding
status: draft
date: 2026-07-28
source_report: research/raw/G1-grounding-synthesis.md
---

# Grounding

Substituting one random set of numbers into two expressions and comparing the
results takes **0.38–0.61 ms** (two harnesses in this project measured each, and
both are reported rather than the flattering one) and catches **112 of 113** seeded
derivation errors: 99.1% recall, with **zero** false alarms across 37
semantically-equivalent rewrites. (A third, independent implementation in
`docs/demos/grounding-ladder.html` measures 170 ns on a smaller formula set; the
figures are not directly comparable and the demo says so.)

That is the whole economic argument, over before it starts. **There is no
engineering, pedagogical, or performance reason to ever ship an unchecked formula.**

What follows is more interesting than that, because grounding is usually sold as a
safety feature (*stop the tutor lying*), and that framing produces bad products. It
makes verification a filter bolted onto the end of a generator. The better framing
is capability.

---

## 1. What a checker in the loop makes possible

**A tutor can contradict a confident learner without asserting authority.** Today,
when a tutor says you are wrong, it is staking status: *believe me, I am the machine
that knows*, the posture that fails with the learner who is already right and
the learner who has learned not to argue. With a checker, the move changes from
*assertion* to *experiment*: "I think that's off — let's evaluate both versions at
x = 3 and see." The tutor stops being the authority and becomes the person who knows
how to settle it.

> *Guardrail, in the same breath:* the check settles **the claim**, never the person,
> and only claims of the type it can decide. A tutor that runs a numeric check and
> then generalises the win into "and therefore my explanation was better" has
> committed a category error.

**Productive failure becomes bounded, and therefore usable.** The reason tutors
interrupt is fear that a wrong model will set. A deterministic checker that fires at
the end of an exploration bounds that risk: you can let a learner build a wrong model
for twenty minutes *because you can show it is wrong in under a millisecond, with the
learner's own numbers*. **Grounding is what buys a tutor permission to shut up.**

> *Guardrail:* for anxiety and learned-helplessness archetypes, and for
> working-memory-limited learners, unguided exploration is among the clearest measured
> harms in this survey. Bounded failure is a policy setting on the learner model, not
> a default.

Two more that follow directly. The learner's own conjectures get the same ladder —
a learner who writes "I think the sum is n²/2" gets back "that fails at n = 3, here is
the value," which is what a working mathematician does and is available to
approximately nobody below graduate school. And **a curriculum can be checked against
itself**: every formula in a course instantiated at shared numeric points and
cross-checked for mutual consistency, the chapter-7 constant against the chapter-3
constant. Nobody has published that. It is buildable today.

The one-sentence version: **cheap, binding, legible verification does not mainly stop
a tutor being wrong; it lets a tutor stop performing certainty.**

---

## 2. The invariant

Verifying formulas with a computer algebra system, verifying figures with a schema and
a renderer, verifying assessment items against a cognitive model, and arbitrating
between agents by putting executable truth above every vote are one mechanism seen from
four angles.

> A claim is **grounded at rung R** if and only if:
>
> 1. **DECLARATION.** The model emitted a finite, parseable object that *fully
>    determines* the claim — an expression tree, a chart spec, an item plus key and
>    attribute mapping, a formal statement. Not prose *about* the claim.
> 2. **INDEPENDENCE.** An arbiter maps that declaration to `{PASS, FAIL, ABSTAIN}`,
>    and shares no weights, no prompt, and no training signal with the generator.
> 3. **BINDINGNESS.** The verdict is consequential. `FAIL` withholds the artefact,
>    and `ABSTAIN` is not `PASS`.
> 4. **LEGIBILITY.** The verdict and the declaration travel with the artefact, in a
>    form the learner can read and re-run.
>
> The rung is defined by the arbiter, not by the medium.

Each condition was discovered independently, and each has a documented failure that
violates exactly one of them:

| Violated | Documented failure |
|---|---|
| **Declaration** | PlantUML generation reaches **91.5% syntactic validity** — "all LLMs produced valid PlantUML adhering to UML conventions" — while showing "inconsistencies in annotations and signatures." The grammar was checkable; the content was never declared, so nothing checked it |
| **Independence** | Mirage: a **blank image leaves Pass@k unchanged or higher.** The vision-model checker was not looking at the artefact |
| **Bindingness** | Quarto's `freeze` means the most widely adopted executable-document toolchain in science **does not execute your notebook by default.** The verdict has no consequence, so there is no verdict |
| **Legibility** | "Most AI tutoring systems in 2026 are at Tier 0 and report as if they were at Tier 2" |

And the structural fact that drops out immediately: **the top rung is machine-decidable
only in the deductive modality.** For formulas, the top arbiter is a proof kernel. For
figures it requires an external dataset and a named human reviewer of record. For
assessment it requires human response data, documented equating, and an independent
validity study. For agent disagreement it is *escalate to a human*. This is not a
tooling gap that better models will close. **Machines can climb the whole ladder only
where the ladder is made of axioms. Everywhere else the top rung is the world.**

---

## 3. The six rungs

Named for their arbiters. L2 splits into two orthogonal sub-rungs because they catch
disjoint error classes at comparable and negligible cost.

| Rung | Arbiter | Measured cost | Measured coverage | Cannot check |
|---|---|---|---|---|
| **L0** Asserted | none | 0 | recall **0%** | everything |
| **L1** Attested | source span + entailment | 0.3–3 s | fact-check accuracy **39–77%**; attribution evaluation itself only ~80% macro-F1 | whether the source is right |
| **L2a** Typed | unit / schema algebra | **0.07 ms** | **100%** on exponent, dropped-term, wrong-variable; **0%** on sign, ×2, ÷2; 0/14 false alarms | anything type-preserving — sign, coefficient, ω vs f |
| **L2b** Instantiated | an interpreter, at sampled points | **0.38 ms** median, p95 0.93 ms | **112/113 = 99.1%**; 0/37 false alarms | universals; anything outside the sampled domain |
| **L3** Normalised | a decision procedure (CAS zero test, IR diff) | **1.8 ms** median, 10.8 ms p95, **unbounded worst case** | 100% in-domain — but SymPy fails **152/397 = 38.3%** of the Wester suite | anything outside its competence, *and it cannot tell you when it is outside* |
| **L4** Proved / Calibrated | a proof kernel, **or the world** | <$0.01 in-idiom → 4M tokens → 3 days → 11 person-years | ~90% competition maths; 60–88% undergraduate in-idiom, **−26 pts off-idiom**; 16–35% college physics; **36% end-to-end from prose** | whether the formal statement means the informal one |

Two things about `ABSTAIN`, because it carries most of the ladder's honesty. **L3 can
never emit `FAIL`** — `simplify(e) ≠ 0` does not mean `e ≠ 0`, by Richardson's
theorem, so the symbolic rung emits `PASS` or `ABSTAIN` and nothing else. And **L2a
can never emit `PASS`**: dimensional homogeneity is a mandatory gate that may reject
and may never accept. A pipeline that collapses `{PASS, FAIL, ABSTAIN}` to a boolean
has destroyed the guarantee; it has not compressed it.

And the rungs are not a staircase. The ladder is a *router*. Climbing past the
rung that can falsify a claim buys nothing and costs a great deal.

---

## 4. The measured inversion

The instinct is that numeric checking is the cheap approximation and symbolic checking
is the real thing you escalate to when it matters. **The measurement says the
opposite: the default is numeric and the escalation is symbolic.** L3 buys about +0.9
points of recall over L2b for roughly 3× the median cost, an unbounded worst case —
and a **38.3% hole** in the domains where physics and engineering teaching lives:

| Wester section | Tests | Failing | Rate |
|---|---|---:|---:|
| **R. Sums** | 23 | 16 | **70%** |
| **D. Numerical analysis** | 13 | 9 | **69%** |
| **I. Trigonometry** | 12 | 8 | **67%** |
| **W. Definite integration** | 28 | 16 | **57%** |
| **S. Products** | 10 | 5 | 50% |
| **N. Inequalities** | 17 | 8 | 47% |
| **Y. Transforms (Laplace/Fourier/Z)** | 13 | 6 | 46% |
| **L. Determining zero equivalence** | 9 | 4 | **44%** |
| A. Boolean logic · E. Statistics · Q. Tensors | 0 | — | **not implemented** |

38.3% is a *floor*, because three entire sections carry no tests at all. Meanwhile the
dumb numeric checker handles those same domains without noticing there was supposed to
be a problem — precisely because it is dumb by construction, and therefore uncorrelated
with the generator's errors.

**Run L2a and L2b together, always.** They are orthogonal: dimensional analysis is
100% on some error classes and 0% on others; numeric sampling is ~99% overall.
Together they cost about half a millisecond. Escalate to L3 only on `ABSTAIN`, on a
universal quantifier, or when the claim is reused enough that the tail risk matters.

---

## 5. Four measurements that went the other way

Four, and three of them contradict something a reasonable engineer would have assumed.

Eight random substitutions buy nothing over one. Recall is flat at 112/113 across
a 16× sampling budget. The cost is not flat: p95 latency rises **6.8×** for zero
measured benefit. On textbook-scale expressions a single substitution is the entire
signal, because the mutation classes that matter (sign, factor, exponent, dropped
term, wrong variable) perturb the value almost everywhere, and never merely on a
measure-zero set. So k should be set by the *structure* of the claim (a suspected
removable singularity or a piecewise domain needs more points; a polynomial identity
does not) and never by a fixed constant.

Sampling wider makes the checker worse. This inverts a natural instinct.

| Sampling domain (k=8) | Recall | False alarms / 37 |
|---|---|---|
| narrow positive `U(0.31, 0.87)` | 99.1% | **0** |
| wide positive `U(0.05, 20)` | 99.1% | **1** |
| signed `±U(0.05, 20)` | 99.1% | **2** (3 at k=4 and k=16) |

Widening gained zero recall and cost up to three rejections of *correct* rewrites.
The mechanism: `√p·√q = √(pq)` and `log(exp z) = z` are true on the positive reals and
false off them, so a checker sampling outside the claim's declared domain is not being
more rigorous — it is evaluating a different claim. Adding assumptions until a
check passes is laundering; sampling outside the declared assumptions is manufacturing.
Both are failures of the declaration and never of the arbiter, which is what the
invariant predicts.

And a proposal from this project's own corpus was benchmarked and falsified. An
earlier section proposed permutation-based fidelity checking, modelled on the Vedic
*pāṭha* recitation protocols: instead of re-asking a model the same question k times,
ask k structurally *different* questions about the same content: state it, invert it,
evaluate it at two points, ask the scaling factor, write it in zero form. The claim
was that this is "strictly stronger than self-consistency sampling because the
permutations are adversarial to semantic smoothing," and it was flagged for
benchmarking. It was
benchmarked: 768 generations, two models, matched budget of six calls each, every
verdict decided by a deterministic comparator so no model judges anything.

| Protocol | Model | Recall | False alarm | **Discrimination** |
|---|---|---|---|---|
| Pāṭha, all 6 probes | gemma3:4b | 87.5% | 87.5% | **+0.0 pts** |
| Pāṭha, all 6 probes | hermes3:8b | 100.0% | 100.0% | **+0.0 pts** |
| Self-consistency, k=6 | gemma3:4b | 18.8% | 0.0% | +18.8 pts |
| Self-consistency, k=6 | hermes3:8b | 43.8% | 0.0% | +43.8 pts |

Exactly at chance, on both models. It flags corrupted and correct claims at
identical rates. Self-consistency is a poor detector that never cries wolf, and
therefore wins. And going from 4B to 8B improved self-consistency's discrimination by
+25 points and improved pāṭha's by zero — the larger model simply flagged
everything, in both conditions. **A protocol whose false-alarm rate rises exactly as
fast as its recall does not get better with scale; it gets louder.**

The diagnosis generalises: **permutation-based fidelity checking is confounded with
probe competence.** It detects "the model cannot do algebra" far more reliably than "the
claim is corrupted." The original mechanism argument, that structurally different
redundancy is uncorrelated with the original error, is *correct*, and is why
it fails: the permuted probes have their own, independent, much larger error rate. On
one model two of six probes have *negative* discrimination, and probe rankings do not
transfer between models.

Sweeping all 63 non-empty probe subsets and taking the best gives +37.5 and +50.0 points
— but those subsets were selected post hoc on the same 16 claims, so **they are oracle
upper bounds, not estimates.** What is robust is the negative. The doctrine that
follows: **every probe in a permutation-based checker must carry a measured false-alarm
rate on known-true claims, per model and per version, and probes above threshold must be
dropped.** The calibration set is not amortisable infrastructure; it is a per-deployment
artefact.

One more null, about the substrate: only **1.54%** of valid public Python notebooks
import any testing module. A printed output is not a check.

---

## 6. Composition is the unsolved problem

The single most important number in this area:

> **97% autoformalization × 69% proving = 36% end-to-end.**

That was stated as a fact about Lean. It is a fact about *chains*.

> The composition rule. Chaining a verified stage A into a verified stage B
> produces **three** verification obligations, and the field routinely ships two:
>
> 1. `wellformed(A.out)` — A's output is legal in A's target language. *Usually
>    checked.*
> 2. `correct(B.out | B.in)` — B's output is correct given its input. *Usually
>    checked; this is the strong guarantee everyone quotes.*
> 3. **`fidelity(A.in ⟷ A.out)` — A's output *means* what A's input meant.** An
>    entailment obligation straddling two semantics, belonging to *neither stage's*
>    verifier. **Usually unchecked, and silently assumed to equal 1.0.**

Do the arithmetic. If the two checked obligations give 0.97 × 0.69 = 0.669 and the
pipeline measures 0.36 end-to-end, the implied statement-fidelity rate is
**0.36 / 0.669 ≈ 0.54** — which lands on top of the source paper's own qualitative
finding of formal/informal discrepancies in "more than half" of the problems. Two
routes, one number. **The fidelity term is not a rounding error; it is the largest term
in the product.**

Once you know to look for obligation 3, it is already measured under other names:

| Chain | Obligation 3 | Measured fidelity |
|---|---|---|
| Prose → formal statement → proof | does the formal statement mean the prose? | **≈54%** |
| Cognitive model → item template → instance | do instances of this family measure the same attribute at the same difficulty? | **≈39%** — the share of *expert-built* templates passing isomorphicity without revision |
| Concept → declarative IR → render | does the IR encode the intended figure? | **not measured**; the qualitative finding is "content you still cannot trust" |
| Simple explanation rung → detailed rung | is the simple rung entailed by the detailed one? | **untested** |

An independent audit of agent-formalized numerical analysis found "recurring unfaithful
formalization patterns, including incomplete multi-part statements, added weakening
hypotheses, and parameter restrictions, that kernel acceptance entirely obscures,"
concluding that "compilation-based metrics substantially overstate formalization
quality." That is obligation 3 failing while 1 and 2 pass. **The strongest available
guarantee has a systematic blind spot in the direction of over-reporting.**

The fix is not to verify the translator. Compiler verification has been here: prove the
compiler correct once, or validate each translation as it happens. No
autoformalizer, item generator or IR emitter will be proved correct; every one can be
asked for a per-instance certificate.

Concretely: author an atomic question set against the *input*, before the
translation, with answers fixed in advance; ask the same questions of the output in the
output's own language; require identical answers, disagreement a `FAIL` and
unanswerability an `ABSTAIN`. Only ask about identifiable quantities — a boxplot does not
contain its samples, and asking a checker to recover them "encourages hallucination and
over-specified code generation." And back-translation alone is not enough: comparing
the formal statement's prose rendering to the original is an entailment check performed
by a model correlated with the one that produced it, which violates the independence
condition outright.

The ruling: **no chain of verified stages may be reported as verified end-to-end unless
every interface carries a round-trip certificate.** "97% formalization and 69% proving"
is, absent obligation 3, no claim about the pipeline at all.

---

## 7. The disagreement about omission

This project publishes its internal disagreements rather than smoothing them, and there
is one here worth stating plainly.

An earlier report listed "the choice of what to omit" as unverifiable in principle,
alongside intuition, analogy quality, and "why this matters," on the grounds that "a
perfectly verified explanation of the wrong 20% is a failure no tier detects."

That row does not survive, and it should be split into three.

**(a) Omission that *falsifies* is machine-checkable, and this is the class that causes
harm.** Five properties a simplification may never falsify, each a property of the *pair*
(simple rung, detailed rung), each decidable given both:

| Invariant | Check | Rung |
|---|---|---|
| **Quantifier strength** — "all" asserted where only "some" holds | parse quantifiers in each rung, compare matching propositions | L2a, NLI backstop |
| **Sign or direction of a causal relation** | extract the signed relation from both rungs, compare | L2a |
| **Uniqueness of a mechanism** — "*the* mechanism" where several exist | definite-article / exclusivity detection against an enumeration | L2a |
| **Existence of a boundary** — implying a model is unrestricted when it is not | **set difference over declared scopes.** Fully decidable *if* scopes are declared | L2a |
| **Ontological category** — thing / direct process / **emergent** process | classifier over both rungs, agreement required | L2b-grade |

Those five and not others, for a reason with a measurement behind it: misconceptions
*across* ontological kinds are robust and *within* kinds are repairable, and a
classical–quantum hybrid conception was measured unchanged across a full semester of
university chemistry. An undeclared drop is, at retrieval time, indistinguishable from a
planted misconception. **It is a type error, not an editorial judgement the checker
cannot reach.**

(b) Omission of required coverage is a set difference against a blueprint. "Did the
artefact cover what it was supposed to cover?" is a set-cover computation, and assessment
has done it since the 1950s under the name *table of specifications*. The earlier report's
own right-hand column concedes the mechanism, "coverage against a syllabus", and then
leaves the row in the unverifiable table anyway. That is an inconsistency and not a finding.

(c) The choice of the declared scope itself is genuinely, permanently unverifiable.
Whether *this* syllabus is the right syllabus; whether the 20% you declared out of scope
was the 20% that mattered. Not truth-apt. The residue is one line long.

The general move:

> The declaration move. Many properties that look unverifiable become verifiable when
> you require the author to declare the thing that would falsify them. You cannot check
> whether an analogy is *good*. You can check that it shipped with a declared alignment set
> and limit set, that the limit set is non-empty, and that nothing in the alignment set
> contradicts the target concept's ontology. You cannot check whether an omission was
> *wise*. You can check that it was declared and falsified none of the five invariants.
>
> Verification does not need ground truth. It needs a commitment.

The obvious attack: declare a trivially narrow scope and every fidelity check passes.
Real, and it is why the two checks run as a *pair*. Narrowing the scope to escape a
fidelity failure mechanically produces a coverage failure against the blueprint. They
pull in opposite directions, which is what makes a pair sound where either alone is
gameable.

And the sentence the earlier report got right, which nothing above weakens:
verification is a floor, not a quality. A fully verified explanation can be badly
sequenced, pitched wrong, and pointless. Grounding removes a failure mode; it never adds a
virtue.

---

## 8. Where the trust boundary ends up

> **Every rung verifies a declaration. No rung verifies the declaring.**

The boundary moves from the model's fluency, an unbounded and undiagnosable surface, to the
map from the learner's world into the checker's world: the units you assigned, the symbols
you bound, the source you selected, the domain you declared, the scope you announced. That
surface is small, enumerable, auditable, and the same object at every rung. You have
not eliminated trust; you have compressed it into a finite list a human can review and a
learner can be shown. It also explains why four sections' hardest problems are one
problem: the autoformalization gap, "the IR does not encode the intended figure," the
Q-matrix retrofitting problem, and shared-state semantics between agents are all failures
of the declaration, seen through four different arbiters.

Which makes the badge the contract. A badge that says "✓ Verified" is **worse than no
badge**, because it transfers the arbiter's narrow guarantee onto the whole artefact.
State what was checked, operationally, in one sentence a twelve-year-old can read ("I
checked this formula against 8 sets of numbers and it agreed every time"). State the
declaration, including any assumption needed to make it pass, because **the assumption is
part of the claim**. State what was *not* checked, by name. Show `ABSTAIN` — an
explicit "I couldn't check this" is information and a missing badge is not. And make the
verdict falsifiable: ship the check, not just its result, so the learner can change the
numbers and watch it break.

One measured constraint: groundedness and comprehensibility trade off, since "humans
prefer responses generated using RAG, but not when responses are too grounded in the
textbook content." Ground the claim; do not ground the prose.

---

## 9. Correctness was never the hard part

*You have built an elaborate apparatus around the part of teaching that was never the hard
part. Nobody's tutor fails because it got a sign wrong in a derivation; it fails because
it explained the wrong thing at the wrong moment to the wrong learner.*

That is right. As verification cost approaches zero, **100% of the remaining problem is
the part verification does not address**, and the unverifiable layer (intuition,
appropriateness, sequencing, why this matters) is where the teaching is.

But §1 is not a safety argument at all. The checker is what lets a tutor wait, let a wrong
model run, hand the instrument to the learner, and settle a disagreement by experiment
rather than by status. **The apparatus is not there to make the tutor correct. It is there
to make the tutor able to stop performing.**

---

## 10. The verification we owe every claim

- **Never ship an L0 formula.** 0.38 ms, 99.1% recall. There is no argument on the other
  side.
- **Run L2a and L2b together; escalate to L3 only on `ABSTAIN` or a universal.** The
  symbolic rung has a 38.3% hole located where physics and engineering teaching
  lives.
- **`{PASS, FAIL, ABSTAIN}` reaches the interface.** L3 never emits `FAIL`; L2a never
  emits `PASS`; a boolean at the last layer destroys the guarantee.
- **Sample inside the declared domain, and set k by the structure of the claim.** k=8 buys
  nothing over k=1; widening the domain costs false alarms and gains no recall.
- **Every interface in a chain carries a round-trip certificate**, authored before the
  translation, scored by a frozen inspector. Back-translation by a correlated model is not
  a check.
- **Every probe in a permutation checker publishes a per-model, per-version false-alarm
  rate.** The pāṭha protocol as specified is at chance; we ran it and we are publishing
  that.
- **Declare the scope, then check the omission against it.** Falsifying omission is L2a;
  coverage omission is a set difference; only the choice of blueprint is unverifiable, and
  the residue is one line.
- **The badge states what was checked, what was assumed, and what was not checked** — and
  ships the check so the learner can re-run it.

A verifier does not make an explanation better. It makes wrongness **discoverable by the
learner instead of assertable by the tutor**, which is the only kind of correction
that does not require them to believe you. Which is why the rung that matters most is the
one the learner can run themselves.

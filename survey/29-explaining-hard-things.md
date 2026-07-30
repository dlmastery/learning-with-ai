---
title: "Explaining Hard Things — the fidelity invariants, instantiated"
section: explanation-invariants
status: draft
date: 2026-07-28
source_report: derived — see provenance note in §1
---

# Explaining Hard Things

Section 25 established a rule for when a simplification is legal: **monotone
refinement.** A rung may drop precision, formalism, or mechanism-depth. It may never
falsify **ontology, causal sign, quantifier strength, or uniqueness of mechanism**.

That rule is correct and, as stated, nearly unusable. Four abstract invariants do not
tell an author what to check on a Tuesday. This section instantiates them: which one
breaks in which domain, what the breakage looks like, and what a machine can check.

**Provenance, stated because this section's evidential status differs from the rest.**
What follows was derived by applying §25's rule to two live cases: graduate
mathematics, and a specific published explanation of energy-based models. It was not
retrieved from a literature. The invariants themselves carry the evidence of §25. The
instantiations are `INFERENCE`. Where a claim below is measured, it is labelled and
sourced; where it is derived, it says so. We flag this so the section does not
borrow §25's authority.

---

## 1. Which invariant breaks, by domain

The four invariants are not equally at risk. In each field, one of them is where
almost all bad explanation dies.

| Domain | The invariant most at risk | What the failure looks like |
|---|---|---|
| **Mathematics** | **Quantifier strength** | ∀∃ silently reordered |
| **Physics / engineering** | **Uniqueness of mechanism** | A determined quantity presented as a tunable choice |
| **Computer science** | **Ontology** | Process and object conflated — a function as *a rule you run* versus *a value you pass* |
| **Biology / medicine** | **Causal sign** | Correlational mechanism narrated as causal, direction unmarked |
| **Statistics** | **Quantifier strength** again | "The probability the hypothesis is true", which reverses the conditional |

This is a design table and not a finding. Its use is that it tells an author *what to
check first*, and it tells a verifier which predicate to spend its budget on.

---

## 2. Mathematics: quantifier strength is the whole game

> "For every ε there is a δ" and "there is a δ that works for every ε" are the
> difference between continuity and **uniform** continuity, and the entire second
> half of a real-analysis course.

Nearly every "intuitive" explanation of a limit, a convergence, or a bound quietly
reorders those quantifiers, because the reordered version is easier to say. The
student computes correctly for two years and then cannot understand uniform
convergence, and the trace goes back to a sentence nobody flagged.

**This is mechanically checkable on written statements**, with a scope limit we
established by testing it. Implemented and run against 1,524 sentences of lecture
transcript, the check **fired zero times**: speech *elides* quantifiers rather than
reordering them, so there is no prefix to compare. It is a check for **authored
technical prose and generated output**, and not for transcript mining (C-50). Within that
scope: an explanation is legal iff **its quantifier prefix is entailed by the formal
statement's, under the declared scope.** That is a predicate and not a matter of taste,
decidable at the cheap rung of the grounding ladder given both statements.

### The ontological crossing that follows it

Chi's test says errors *within* an ontological category are repairable and errors
*across* categories are robust. The Bohr-model hybrid population was **unchanged
across a full semester** of university chemistry (§25).

Mathematics has its own canonical crossing: process versus object. A limit as
*something you do* versus *a number that exists*. A function as *a rule you apply*
versus *a point in a space*.

A student holding "limit" in the process category can compute limits indefinitely and
cannot understand uniform convergence, because uniform convergence quantifies over a
space of functions, which requires functions to be objects first. The
misconception survives instruction exactly as Chi's test predicts, because the repair
is a category change and not a correction. `INFERENCE`, from Chi's mechanism plus
the process/object literature in mathematics education.

---

## 3. Two failure modes worth naming

These are the section's original contributions, and both are checkable.

### 3.1 Machinery before obstacle, and the experiment that narrows it

**An explanation that presents machinery before the obstacle the machinery exists to
dodge makes the machinery look arbitrary.**

**Corrected 2026-07-29, and the correction is more useful than the original claim.**
Muller's doctoral work (Sydney, 2008) ran the nearest thing to a controlled test of
this, and it points somewhere else. His Refutation condition is the Exposition
script verbatim, plus explicit statements of the misconception, in the same
definitions-first order, with no reordering at all. It scored d = 0.79 against the
Exposition.

So in the one experiment that isolates it, the load-bearing variable is **naming the
wrong idea**, not the order in which the machinery arrives. Ordering may still help;
it has not been shown to be what does the work, and this section originally implied
it was. See §3.3.

The original argument was mechanistic. Machinery before obstacle leaves the reader
with no slot to put it in. They remember it as a list of tricks, cannot
reconstruct it, and cannot tell which parts are essential and which are incidental —
which is precisely the failure that makes an explanation feel clear and leave nothing
behind. It is a fluency illusion with a specific cause.

The rule, narrowed by the correction above: name the wrong idea explicitly. The
obstacle-first *ordering* is a plausible way to do that and is not what the evidence
isolates. Muller's Refutation condition kept the original order and simply stated the
misconception aloud. So: say what does not work, out loud, before or after the
machinery. The naming is the mechanism; the position is a preference.

This is checkable in a weak but useful sense — for a technical explanation, does the
obstacle appear before the first piece of machinery it motivates? That is a structural
predicate over an outline and not a judgement about prose.

### 3.2 A determined quantity presented as tunable

This falsifies uniqueness of mechanism, and it is endemic in engineering
explanation.

When a quantity is *determined* by a conservation law, a stationarity condition or a
dimensional constraint, and the explanation presents it as a knob someone chose, the
reader concludes the design is taste. They will then tune it, and be confused when it
breaks, because they were told it was theirs to set.

The check: for each numeric constant in an explanation, is it (a) determined by a
stated condition, (b) empirically fitted, or (c) arbitrary? All three are fine. Not
saying which is the violation.

### 3.3 Name the misconception

Three experiments, one thesis, and it is the closest thing the field has to a direct
test of what makes an explanation teach.

| Condition | Content | Gain |
|---|---|---|
| Exposition | Clear, correct, 7:02 | 1.77 |
| Extended | Same, longer, 11:22 | 2.41 |
| **Refutation** | Exposition **verbatim + the misconception named**, 9:33 | **4.41** |
| **Dialogue** | Two speakers, one holding the misconception, 11:22 | **4.77** |

N = 364, F(3,461) = 13.625, p < .001; **d = 0.83** for Dialogue, **d = 0.79** for
Refutation. Replicated at n = 73 on quantum tunnelling (d = 0.71).

And the same thesis contains the felt/real dissociation, measured. On the opinion
form, *"I learned something from the video"* scored **5.7 for Dialogue against 5.6 for
Exposition — flat**, while actual learning differed by d = 0.71. Perceived clarity did
not differ either. What *did* differ: students found the better format more dull
(p < .01) and said they would rather see the worse one in lectures (p < .05).

The author's own conclusion is the sentence this survey has been circling for eighty
thousand words:

> *"They believed they learned the same amount as students with double their learning
> gains. Thus the expositions actually strengthened misconceptions."*

**A clear explanation of a concept the learner has a wrong model of does not overwrite
the wrong model. It sits alongside it, and raises confidence.** That is why clarity is
not the goal, and why "was it well explained?" is the wrong question.

One further result from the same work, on the prediction step this survey recommends
elsewhere: *"students who witness demonstrations without being asked to make a
prediction perform as well on follow-up tests as those who don't see the demonstration
at all."* The demonstration is worth nothing without the commitment that precedes it.

---

## 4. Worked example: energy-based models

A test of whether any of this improves an explanation that is already good. The
subject is a published walkthrough of energy-based generative models: energy
landscape, a particle in a fluid, rolling downhill while wandering, a persistent
replay buffer. The physics framing is the right instinct. Three things sharpen it.

### 4.1 Lead with the uncomputable constant

Every piece of machinery in an energy-based model exists to dodge one fact:

> **You can write the probability of any image up to a constant you cannot compute.**

*p(x) = e^(−E(x)) / Z*, where *Z* integrates over every possible image. In 784
dimensions that integral is not hard; it is hopeless.

Introduce *Z* as the antagonist first and every later step is *forced* rather than
clever. Introduce the landscape first and the reader meets Langevin dynamics,
contrastive divergence and replay buffers as three unrelated tricks. Same content,
different retention — §3.1.

### 4.2 The one line the method turns on

∇ₓ log p(x) = −∇ₓ E(x), because *Z* is constant in *x* and vanishes under the
gradient.

You cannot evaluate the probability. You can always compute *which direction makes it
go up* — and sampling only ever needs the direction. Most treatments bury this in the
derivation. It is the hinge, and it belongs at the top of rung 2.

### 4.3 The noise scale is not a knob

"Rolling downhill while wandering" is the right picture with the *why* missing.
Gradient descent finds a mode. You do not want the most likely image; you want a
*sample*. So Langevin adds noise:

*x*ₜ₊₁ = *x*ₜ − (ε/2)∇E(*x*ₜ) + √ε · *z*ₜ

The √ε is not a hyperparameter. It is the unique scale at which the stationary
distribution equals *p*. Present it as tunable and you have falsified uniqueness of
mechanism — §3.2, exactly.

And the persistent replay buffer stops being a hack once the tug-of-war is visible:
training pushes energy *down* on real data and *up* on model samples, and the "up"
push lands wherever the negative samples happen to be. Unconverged samples mean
pushing up in the wrong places — teaching the model to distrust regions it should
like. The buffer maintains a population near equilibrium so that after the landscape
shifts, the samples are still approximately right.

Note what that is: continuity of state across steps, because recomputing from
scratch each time is biased and slow. The same argument this survey makes for
persistent learner state (§11), in a different domain.

### 4.4 The three rungs

Three rungs, because five did not beat three at **p = 0.738** (§25).

| Rung | The claim |
|---|---|
| **1** | A network scores images. Real ones score low, everything else high. To make an image, start from noise and walk downhill while jittering. |
| **2** | The score is an unnormalised log-probability. The normaliser is uncomputable, but its gradient is zero — so sampling works where evaluating does not. The noise scale is fixed by requiring the correct stationary distribution. |
| **3** | Maximum likelihood on −E − log Z; ∇_θ log Z = −𝔼_{p_θ}[∇_θ E], estimated by MCMC. Persistent contrastive divergence approximates that expectation with a maintained chain, because a fresh chain per step is both biased and slow. |

Every rung is entailed by the one below it. Rung 1 drops the normaliser entirely,
which is legal because it drops precision. It does not claim the score *is* a
probability, which would falsify ontology.

---

## 5. What the probe should ask

§22 established that entry must be measured, never preferred. The sharpest single
measurement behind that rule is narrow. Buljan et al. 2018 ran three randomised
comparisons, n = 334 adults, an infographic against a plain-language Cochrane
summary, scored on an immediate quiz: preference moved d ≈ 0.48 and knowledge moved
zero. Read that as one format contrast in one adult population and the rule still
holds, because the felt/real split recurs in trials built quite differently (§09,
§43), and because rapid dynamic assessment recovers an actionable estimate from 1–3
items in 15–40 seconds at r = 0.66–0.92 against full diagnostics. A real measurement
is available, so there is no reason to ask.

This section adds *what the probe should ask*. **Probe on the obstacle, not the
definition.**

- Weak probe: *"What is an energy-based model?"* — separates people who have read a
  definition from people who have not.
- Strong probe: *"Why can't we just compute the probability directly?"*

The second sorts by whether the reader holds the *constraint that generates the
field*. Someone who can answer it belongs at rung 2 whatever their credentials;
someone who cannot will not understand rung 2 however much they have read.
`INFERENCE`. This follows from §3.1 and not from a trial, and testing it is cheap.

---

## 6. Graduate level: the tutor's job inverts

Guidance measures **d = −0.428 for experts**. Worked examples, scaffolding and
explicit instruction — the strongest interventions that exist for a novice — are an
*active harm* here. A tutor that explains beautifully to a graduate student is doing
the wrong job well.

What remains, in order of value:

1. **Numeric falsification before symbolic proof.** A numeric check catches 99.1% of
   seeded derivation errors in **0.38–0.61 ms** with zero false alarms; symbolic costs
   roughly 3× for +0.9 points and carries a **38.3% XFAIL/SKIP hole** in SymPy,
   concentrated in sums (70%), definite integrals (57%) and inequalities (47%) — the
   areas graduate work lives in. Substitute random values before proving. Most wrong
   conjectures die in a millisecond.
2. **The adversary, unannounced.** The referee who supplies the case the proof forgot.
   *Announced* devil's advocacy measurably produces bolstering of the original view
  (§26), so the objection must be owned, not performed.
3. **Explaining it back, with the expectancy set first** — g = 0.48 with, **g = −0.02**
   without (§05). This is why seminars work and "any questions?" does not.
4. **Formal verification where it earns its cost**, and honestly: 97% autoformalisation
   × 69% proving yields **36% end-to-end**, because the formal statement stops matching
   the informal one (§13). The kernel moves the trust boundary; it does not remove it.

Explanation is fourth at best, and the explanation that counts is the learner's.

---

## 7. What an author must check first

- **Instantiate the invariant before authoring.** Name which of the four is at risk in
  this domain, and check that one first.
- **In mathematics, check the quantifier prefix.** It is decidable, it is cheap, and it
  is where the damage is.
- **Obstacle before machinery**, always. If the reader does not know what fails, every
  fix looks arbitrary.
- **Label every constant** as determined, fitted, or arbitrary. Silence on this point
  is a falsification of mechanism.
- **Probe on the obstacle.** A definition question measures reading. An obstacle
  question measures understanding.
- **At expert level, stop explaining.** Falsify, object, and let them teach it back.

A simplification is legal when the reader can still tell what would break. Everything
above is that sentence made checkable, one domain at a time.

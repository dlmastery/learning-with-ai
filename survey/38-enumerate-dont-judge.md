---
title: "Enumerate, Don't Judge — the belief object, and how it routes around the verifier gap"
section: architecture
status: draft
date: 2026-07-29
source_report: research/raw/V2-responsive-explanation.md
---

# Enumerate, Don't Judge

Earlier sections establish a wall. Across **223 real tutoring domains, no model beat
chance at labelling an incorrect student action** — and since every agentic capability
is bounded by the check it closes on, the whole architecture appeared to be waiting on
a model good enough to judge student work.

It is not. The wall is an artifact of the question being asked.

**Every system in the field asks a model: *is this wrong, and why?*** That is an
open-ended judgement over an unbounded space, which is exactly what models are bad at
and exactly what the 223-domain result measures.

There is a different question, and it is a lookup.

---

## 1. The belief object

A misconception is not a label with a strength attached. That is what every shipping
system stores, and it is why nothing can be done with it. Model a belief instead as an
**object with three methods**:

```
Belief {
  predict(item)         → distribution over responses
  discriminate(rival)   → an item that separates this belief from that one
  break(case_space)     → trace | SCOPE_LIMITED | EQUIVALENT | ⊥
}
```

Every other component of a responsive tutor falls out of those three.

- **`discriminate()` is the probe generator.** You do not author diagnostic items; you
  ask two candidate beliefs for the item on which they disagree.
- **`predict()` is what the explanation is compiled against**, and what a mid-stream
  revision re-evaluates.
- **`break()` is the run-it-forward move** — instantiate the learner's own wrong rule
  and execute it until the world contradicts it.
- **Divergence between `predict()` and observed behaviour is the retirement
  criterion.** A belief that stops predicting is a belief the learner no longer holds.

---

## 2. Why this walks around the wall

Here is the whole argument in one line:

> **The belief object never asks whether an answer is wrong. It asks which of its
> enumerated beliefs predicted that answer** — an argmax over precomputed
> distributions.

Chance-level open-ended judgement becomes a **table lookup over a bounded set.** The
belief library *is* the verifier. Not a model that has learned to judge — a structure
that makes judging unnecessary.

And the consequence for latency is not incidental. A posterior update over **≤40
enumerated beliefs is closed-form Bayes**, which means **no language model anywhere on
the real-time path.** The 200 ms budget stops being aspirational.

This is the difference between waiting for a capability and designing so the capability
is not required.

---

## 3. Decay has been modelled backwards

A finding that falls out of taking beliefs seriously as objects, and it inverts standard
practice.

Every spaced-repetition and learner-model system decays belief strength toward zero.
For misconceptions this is **wrong in the case that matters most**. Cross-ontological
errors — a limit held as a process, an electron held as an orbiting particle — do
not decay. The Bohr-model hybrid population was unchanged across a full semester of
university chemistry.

What decays is our confidence that the learner still holds it.

So the parameter must not fall toward zero. The **credible interval widens toward the
population prior**, and a belief last seen six months ago returns as *probably still
there, poorly localised* rather than *probably gone*. Systems that decay misconception
strength are quietly deciding that untested errors have been repaired.

---

## 4. The explanation IR, and the compiler that refuses

An explanation is compiled, not written. Three layers:

| Layer | Holds | Checkable |
|---|---|---|
| **Claim graph** | The propositions and their dependencies | Fully |
| **Discourse plan** | Order, emphasis, what is named aloud | Structurally |
| **Surface bindings** | Words, marks, animation parameters | At the boundary |

The four fidelity invariants — a rung may drop precision but never falsify **ontology,
causal sign, quantifier strength, or uniqueness of mechanism — become compiler
passes that block a render.** Not review guidance. A build failure.

Two passes are worth naming because they come from measured results rather than
principle. One enforces that the misconception is named explicitly, from the finding
that a Refutation condition scoring **d = 0.79** was the exposition script *verbatim
plus explicit statements of the wrong idea* — same order, nothing rearranged. The other
enforces referential-status ordering, from the result that referential status, not
persistence, decides whether an added element helps or harms.

---

## 5. Latency is a schema property

The naive framing treats mid-stream revision as a performance problem — make the model
faster. It is a type problem.

Of the available patch operations, **`annotate` is the only one that falsifies no
invariant.** Adding a label, a pointer, a highlight cannot make a true claim false. So
`annotate` is the only operation that may legally land inside 200 ms.

Everything else — substituting a claim, reordering, changing a rung — **must branch at a
beat boundary**, from a patch cache pre-verified during the previous beat. The system
does not race; it prepares.

That is a cleaner answer than optimisation, and it is enforced by the schema rather than
by discipline.

---

## 6. What the system may watch, and why the legal answer is the better one

Emotion inference in education is prohibited under EU AI Act Article 5(1)(f) — not
high-risk, banned. Gaze-based frustration detection is out.

The replacement is better on the merits. Legal triggers reduce to voluntary acts:
a committed answer, a deictic act (pointing, selecting, circling), a produced artifact.
Each is unambiguous, learner-initiated, and carries far more information than an
inferred affective state — which, on this survey's own evidence, would optimise the
felt axis rather than the real one.

One tempting signal is explicitly rejected: rewind and replay density, which was
measured null and opposite-signed. The obvious proxy for confusion is not one.

---

## 7. Deixis stops being a research problem

Pointing at the thing was earlier described as the cleanest greenfield, with a substrate
at **49% IoU** fine-tuned against under 1% zero-shot.

That number is the cost of grounding references in images you did not author. Once
an explanation is compiled from an IR, every object in the scene has a **compile-time
identifier**, and pointing is exact by construction. The hard version of the problem
only exists for systems that generate pixels first and try to understand them
afterwards.

---

## 8. The hole, and the experiment nobody will want to run

`break()` cannot address ontological crossings. Running a wrong rule forward
requires the rule to have dynamics. "A limit is a process" has no dynamics to execute —
there is nothing to run until it contradicts itself. And that class is precisely the one
the literature shows to be most robust and least repairable by instruction.

So the strongest move in this architecture does not reach the strongest misconception.
Ontological repair needs a different mechanism, and this document does not have one.

And the falsifier that matters is not the obvious one. Comparing a responsive system
against a fixed explanation confounds targeting with timing. The arm that settles it is
A′: identical targeting, revision deferred to the end.

> If A ≈ A′, then mid-stream revision is theatre and the entire latency argument was
> decoration on a targeting result.

That is the experiment we owe, and it is the one least likely to be run by anyone
selling this.

---

## 9. What this section commits us to

- **Enumerate beliefs; never ask a model to judge.** The 223-domain result bounds
  open-ended judgement, not bounded lookup.
- **No language model on the real-time path.** Closed-form Bayes over a bounded belief
  set, or the latency claim is fiction.
- **Widen the interval; do not decay the strength.** An untested misconception is
  poorly localised, not repaired.
- **Fidelity invariants are compiler passes, not review notes.** A render that would
  falsify ontology does not build.
- **Only `annotate` lands inside 200 ms.** Everything else branches at a prepared beat
  boundary.
- **Watch voluntary acts only.** Committed answers, deictic acts, produced artifacts —
  and not gaze, which is prohibited, nor replay density, which was measured null.
- **Run arm A′.** If deferred revision matches live revision, we were wrong about the
  interesting part.

The general form, and the reason this section exists: **a capability gap can be walked
around as well as waited out.** The field is waiting for models to become good judges.
The structure that makes judgement unnecessary is buildable now.

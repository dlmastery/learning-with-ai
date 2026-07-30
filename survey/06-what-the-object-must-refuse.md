---
title: "What the Object Must Refuse — embodiment, manipulatives, and executable material"
section: embodiment
status: draft
date: 2026-07-27
source_report: research/raw/F7-A3-embodiment-and-notebooks.md
---

# What the Object Must Refuse

Every experienced teacher of young children believes the same thing, and they are
not being sentimental about it: some concepts do not go in through a screen. You
need the blocks. You need to *move the thing*. Fractions become real when a child
cuts a circle, not when a circle is cut for them.

This section set out to establish what that intuition is worth and where the
boundary sits — because if physical manipulation is load-bearing, there is a hard
ceiling on what an AI reaches, and honesty requires naming it.

The measurement says the intuition is pointing at something real and **has
misidentified what it is.**

---

## 1. Presence is worth about 0.2, and three literatures agree

The first question is narrower than "does the physical matter": does adding
*presence* — a face, a body, a room — to otherwise identical content help?

Three independent literatures converge on the same number:

| Comparison | Effect |
|---|---|
| On-screen pedagogical agent vs none (43 studies) | **g ≈ 0.19** |
| Physical robot vs the same content on a tablet (78 controlled studies) | **d = 0.20** |
| Immersive VR vs desktop (35 RCTs) | **ES = 0.24** |

A real premium, and a modest one. But the number that should govern any decision
built on it is a different one: **the effect is dwarfed by the control condition you
choose.** The robot meta-analysis spans **+0.75** (robot versus nothing) to
**−0.06** (robot *replacing* the teacher). And its Europe/non-Europe reporting gap
is **0.36 SD — larger than the effect being estimated.**

When the moderator is bigger than the main effect, the main effect is not a
property of the technology. It is a property of what you took away to make room
for it.

---

## 2. The result that reverses the premise

Novack and Goldin-Meadow ran the clean experiment. Same mathematical strategy,
taught three ways: **physical action on objects**, **concrete gesture**, and
**abstract gesture**.

> "Gesture promotes transfer of knowledge better than direct action on objects."

Only gesture transferred. Acting on the actual objects — the thing the intuition
insists on — produced learning that stayed stuck to the objects. Replicated
neurally in 2026 with fNIRS.

The reading is counterintuitive and, once seen, obvious. **Physicality is not the
active ingredient. Representational compression is.** A gesture is already a
*symbol* of the action; it has thrown away the specific blocks and kept the
structure. That discarding is the learning. Handling the real blocks does the
opposite — it binds the idea to the instance.

Consistent with this: physical versus virtual manipulatives comes out null in
both randomised, fidelity-documented head-to-heads (N = 350, within-class
randomisation, Welch t = 1.015, p = 0.316). The one pooled estimate favouring
virtual (d = 1.603) has **I² = 97.95%** and is uninterpretable — we report it
because omitting an inconvenient number is worse than discounting a bad one.

---

## 3. So what *is* load-bearing

If not the medium, then what makes a good manipulative good? Two properties, and
both are implementable in software:

> **The object must refuse illegal states, and it must link representations.**

A Montessori pink tower cannot be built wrong and stay standing. A number line
will not let you put 7 to the left of 3. The correction comes from the object, not
from an adult — which is why the child can be wrong in private, repeatedly, at
their own pace, without anyone's face changing.

That is *self-correction*, and it is the mechanism. It is also, precisely, a
constraint solver with a rendering layer.

This resolves an apparent conflict in our own corpus. An earlier section scored
Montessori's materials as not surviving substitution — remove the physical
object and the mechanism goes with it. That verdict is right *about Montessori*
and does not generalise, because what fails to survive is the wood. What survives
is the refusal.

A well-built simulation refuses illegal states more thoroughly than wood does. It
also links representations — symbol, picture, graph, equation, animation — updating
together, which no physical object has ever done.

---

## 4. The inversion that matters most here

Physical manipulation is an access barrier, and virtual is the accessible
option.

In the head-to-head comparisons the virtual arm showed **fewer demographic
predictors of performance**. Fine motor control, grip, tremor, visual tracking,
and the sheer physical availability of a materials kit are all requirements the
physical version quietly imposes and the virtual version does not.

And the adjacent literature on sensory accommodations does not support the folk
consensus. Sensory-integration treatment effects decline from **0.60 to 0.03**
across study eras and sit at **0.09, non-significant, against active controls**.
Alternative seating — the wobble stools and therapy balls that appear in every
classroom that is trying — has moderate-strength evidence of **no effect on
attention**.

These are not reasons to withhold anything a child finds comfortable. They are
reasons not to *count on it* as an intervention, and not to spend the budget of
attention there instead of on explicit instruction.

---

## 5. The bridge, and the failure mode that must be fixed first

None of this means the physical world is out of reach. Camera-in changes the
boundary: a tutor can now *watch* a child work on paper and comment on it.

State the capability precisely, because the headline number is narrower than it
sounds. The **98.4%** figure is *answer-position recognition* on a 61-exam grading
benchmark, and its **0.58%** false-negative rate is achieved **with the reference
solution supplied**. The best measured rate for reading *error-correction* on
handwritten work is **77%**. So: the system can reliably find and read what a child
wrote. Diagnosing where the reasoning went wrong is a different and harder task
that is not yet at that accuracy.

One failure mode disqualifies naive deployment, and it is the most important
sentence in this section for anyone building:

> **Vision-language models silently "fix" student errors while transcribing them.**

Asked to read a page of student work, the model returns the *corrected* work. It
repairs the sign, closes the parenthesis, completes the step — because that is
what its training rewards. The mistakes are the entire reason for looking at the
page, and they are the thing being erased.

So transcription is not a neutral read. It must be constrained to a verbatim,
error-preserving task with an explicit instruction that mistakes are the payload,
and it must be checked against exactly that.

---

## 6. Executable material: reactivity is a hazard reduction, not a guarantee

The same theme carries into how teaching material itself is built. A reactive
notebook — one whose cells form a dependency graph and recompute on change —
promises that a learner cannot produce an inconsistent state. That is the "refuses
illegal states" property applied to a document.

Measured across eight hazard classes, the promise is **substantially but not
entirely kept. Reactive execution refuses to load** duplicate definitions and
cycles, and eliminates use-before-define and deleted-cell residue. But the same
three cells with identical dependencies produce `total = 106` or `total = 6`
purely by source position.

Hazard reduction, not a guarantee. Worth having, and not worth trusting blindly.

And the honest gap: **zero empirical evaluations of reactive notebooks as an
instructional medium exist.** The claim that a consistent-by-construction document
prevents misconception formation is a design hypothesis, not a finding. It is
stated here as the former.

What *is* verified is the recipe. Applying a nine-rule conformance checker to
teaching scripts — ~38 ms per script, non-zero exit on violation — an injected
sign flip in an entropy definition **failed loudly and named the claim it
violated.** That is the thing byte-identical reproduction alone cannot do:
reproducing a wrong answer perfectly is still reproducing a wrong answer.

---

## 7. What to build teaching material *on*

Substrate matters more than it looks, because a chapter that takes five seconds to
become interactive is a chapter most learners never see interact.

| Substrate | Cost | Use |
|---|---|---|
| **Reactive JavaScript** | **27 KB** | **The default.** Simulations, constraint objects, linked representations |
| **MicroPython** | 0.53 MB | When Python source must be *read* by the learner |
| **Pyodide** | **21.89 MB + 4.5 s CPU per cold visit** | Real scientific stack. 293 packages, no threads or sockets, torch impossible. **Cap at ≤3 chapters** |

The 27 KB default is not a compromise. Almost everything this survey wants a
mini-app to do — refuse an illegal state, link four representations, let a wrong
idea run to its visible consequence — is a constraint solver and a renderer, which
is exactly what small JavaScript is good at.

A note worth keeping: Observable's own team, asked whether to run computation in
the browser, shipped a static site generator.

---

## 8. What this section commits us to

- **Build for representational compression, not physical fidelity.** Gesture beat
  action on objects. The goal is to help a learner *discard* the instance, not to
  make the instance more vivid.
- **Every manipulative must refuse illegal states and link representations.** If
  it does neither, it is a picture.
- **Virtual is the accessibility default**, because it removes requirements the
  physical version imposes silently.
- **Never let a model transcribe student work unconstrained.** The errors are the
  payload.
- **Reactive documents reduce hazards; conformance checks catch what reactivity
  misses.** Ship both.
- **27 KB of JavaScript, not 21.89 MB of Python**, unless the learner needs to read
  the Python.

The through-line, which is the same one the grounding sections reached from the
other direction: what teaches is not the richness of what the learner is given. It
is the precision of what they are not allowed to do wrong without noticing.

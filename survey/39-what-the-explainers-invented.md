---
title: "What the Explainers Invented — 104 techniques, and the one nobody has ported"
section: craft
status: draft
date: 2026-07-29
source_report: research/raw/V1-explainer-techniques.md
---

# What the Explainers Invented

Over roughly fifteen years, a few dozen people built a craft of explanation that
has no textbook and almost no research literature. This section is the first
inventory of it — **104 named techniques** from 3Blue1Brown, Veritasium, Primer,
Ben Eater, Sebastian Lague, Mark Rober, Steve Mould, Numberphile, Kurzgesagt,
Vsauce, Applied Science, CGP Grey, Welch Labs, Karpathy, Ciechanowski, Nicky Case,
Bret Victor, Distill, Khan, Physics Wallah, Unacademy, and the Chinese dual-teacher
classroom.

It was commissioned to test a hypothesis. The hypothesis was wrong, and the way it
was wrong is the most useful thing here.

---

## 1. The hypothesis, and its refutation

**The claim under test:** every technique these people invented is *craft
compensating for the absence of a listener.* They cannot see you, cannot ask, cannot
re-render when you frown — so the anticipated objection, the "you might be thinking…",
the deliberate false start, the misconception voiced on the viewer's behalf, all of it
is scar tissue from one-way transmission. Strip the constraint and most of the craft
dissolves.

Classified across all 104:

| Bucket | Count | Meaning |
|---|---|---|
| **A — Compensation** | 16 | Exists only because the explainer cannot see the learner |
| **B — Intrinsic** | **63** | Still the right move with a perfectly responsive tutor |
| **C — Medium constraint** | 11 | Dissolves in an interactive substrate |
| **D — Authored invariant** | 5 | Cannot be derived from a learner model at all |

**Sixteen of 104.** The hypothesis is not merely wrong; it is wrong by a factor of
four in the other direction. **Most of what these people invented is not scar
tissue — it is discovery**, and almost none of it has been built into a responsive
system.

That matters commercially and strategically. A system that assumes responsiveness
supersedes craft will rebuild the 16 and discard the 63.

---

## 2. Bucket D, which the brief did not anticipate

The fourth category came back unrequested and it constrains the whole architecture.

Sanderson holding **one 2×2 transformation on screen for four minutes** is not
derivable from any learner model. There is no signal that says *this particular
matrix, this long*. It is an authored decision by someone who understood the concept
deeply enough to know which single object carries it — and no amount of diagnosis
produces it.

> **Curate a library. Do not only generate.**

This is a correction to the instinct running through the rest of this survey, which
has consistently favoured generation over authorship. Generation handles the
learner-specific; authorship handles the concept-specific. A system that generates
everything will be responsive and shallow.

---

## 3. The technique nobody has ported

Reading the raw HTML of Ciechanowski's *Gears* exposes an ordering that is invisible
when you read the page normally:

> *"In the demonstration below you can control the fan's speed using a slider:"* →
> **the widget** → and only in the paragraph *after* does the concept arrive.

That is **prediction before reveal**, executed **30 times in a single article and
120 times in *Moon*** — and executed without ever asking the reader to pause.

Compare the video version of the same idea. Sanderson says the prediction is where
the learning happens, says it across 34 videos, and concedes that people are
*"a little bit more passive in that moment."* The pause is a request, and requests
are declined.

**Ciechanowski solved it by deleting the thing that would have to be paused.** An
article has no clock. The widget simply sits there, unresolved, and the reader
manipulates it because there is nothing else to do.

### The spec, in one sentence

> For every load-bearing claim, emit a **manipulable figure that instantiates it**,
> render it **before** the prose that resolves it, introduce **one new degree of
> freedom** per figure, and **do not advance** until the learner has moved something.

Four constraints, each doing work. The figure must instantiate the claim rather than
illustrate it. The order is non-negotiable — after the prose, it is a demonstration
rather than a prediction. One degree of freedom keeps the search space small enough
to reason about. And the gate makes the prediction compulsory without ever asking.

---

## 4. The measured warrant, which is narrower than the folklore

Prediction-before-reveal is widely believed to work. The measurement says something
more precise and more useful:

**Prediction has no main effect.** The entire effect is carried by the
expectancy-violation interaction — *p* = .002. Predicting and being right does
approximately nothing. Predicting and being wrong is where the whole result lives.

Which is the measured warrant for the strongest move in this survey: taking a
learner's stated rule and running it until it breaks. The mechanism is not that
they predicted. It is that the prediction failed, visibly, on something they
committed to.

It also disciplines the design. A prediction step that mostly confirms is a cost with
no benefit, so the figure must be chosen to discriminate — set at the parameter
values where a common wrong model and the correct one disagree.

---

## 5. Three places the report disagrees with this survey

Recorded because they are unresolved, not because they are settled.

Responsiveness is a hazard for productive failure. Productive failure measures
**g = 0.36–0.58**, and the finding is blunt: *adding help to the struggle does not
help.* A system optimised to notice you are stuck and intervene is optimised to
destroy the mechanism. This survey has argued hard for unprompted intervention;
those two commitments are in tension and the resolution — intervening on the
*wrong kind* of stuck — is asserted here rather than measured.

The street interview does not port. Veritasium's misconception reveal works
because a stranger commits publicly and is then shown to be wrong. The cost is
affective, not technical — the confession is what makes the correction land. A
private system can elicit the same commitment and cannot reproduce the stake.

**Personalisation destroys the shared artifact, and nothing in this survey has
costed that.** A 3Blue1Brown video is a thing millions of people have *in common* —
it can be discussed, referenced, argued over, taught from. A perfectly personalised
explanation is seen by one person and can be discussed with nobody. This survey has
treated personalisation as strictly good. It has a price and we have never named it.

---

## 6. And one finding from the largest-scale case

The Chinese dual-teacher classroom — a remote expert paired with a local facilitator,
at enormous scale — returns exactly one record in ERIC.

What that record says is the useful part: the failure mode is **emotional, not
informational.** The remote expert delivered the content adequately; what broke was
the relationship in the room.

Read against everything else here: **the layer AI would most naturally replace was
already the weak one.** The instruction was never the scarce good.

---

## 7. What this section commits us to

- **Build the 63 before rebuilding the 16.** Most of this craft is invention, not
  compensation, and a responsive system does not supersede it.
- **Curate as well as generate.** Bucket D cannot be derived from a learner model,
  and a system that only generates will be responsive and shallow.
- **Ship manipulate-before-explain as a hard ordering rule.** Widget, then prose,
  one degree of freedom, no advance until something moves.
- **Choose figures that discriminate.** Prediction has no main effect; the
  expectancy violation carries all of it, so a confirming prediction is wasted cost.
- **Hold the productive-failure tension open.** Intervening on the wrong kind of
  stuck is a design claim we have not measured, and the honest position is that it
  is unresolved.
- **Name the price of personalisation.** An explanation nobody else has seen cannot
  be discussed with anybody.

The general form: **a decade of craft was developed by people who could not see their
learners, and most of it turns out not to depend on that.** They were not working
around the constraint. They were discovering how explanation works, and the
constraint was incidental.

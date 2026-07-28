---
title: "The One Interaction That Survived — personalisation as a measurement problem"
section: personalisation
status: draft
date: 2026-07-28
source_report: research/raw/J1-personalisation-engine.md
---

# The One Interaction That Survived

Every section before this one asks *which techniques work*. This one asks the
harder question, and the one everybody actually wants answered: **for this learner,
on this concept, at this moment — which technique fires?**

The answer is not an algorithm. It is a fifteen-second measurement that was
impractical until about eighteen months ago.

---

## 1. Start with the failure, because it is fifty years long

Personalisation has a research programme behind it and the programme mostly
failed. This is not a minor caveat; it is the single most important thing to know
before building anything in this space, and it is routinely omitted.

Cronbach and Snow spent two decades hunting **aptitude–treatment interactions** —
the idea that different learners need different instruction, and that you can
predict which from measurable traits. Read Cronbach's own 1975 summary rather than
anyone's characterisation of it:

> *"The interactions did not turn out as we had anticipated."*

On the direct ancestor of every modality-matching claim ever sold — high spatial
ability paired with diagrams:

> *"No interaction of this sort was found, in our shop or elsewhere."*

On the programme's *best* results, the ones that did reach significance:

> *"Strangely inconsistent from year to year and from course to course."*

And the structural warning, which is the sentence anyone proposing a
personalisation engine should have to write out by hand first:

> *"Once we attend to interactions, we enter a hall of mirrors that extends to
> infinity."* … *"Generalizations decay."*

Fifty years of looking. **Exactly one interaction survived** — and it survived in
two forms that turn out to be the same law.

---

## 2. The survivor

Snow's *ability × information-processing load*, and **expertise reversal**:
**d = +0.505** for novices, **d = −0.428** for experts. Chen, Kalyuga and Sweller
show both reduce to **element interactivity** — how many things a learner must hold
simultaneously to make sense of the material.

Three properties of this interaction decide the entire architecture:

- **It is per-topic, not per-person.** The same learner is a novice in one chapter
  and an expert in the next. Any system that stores "this student needs
  scaffolding" as a trait has already made the mistake Cronbach warned about.
- **It is asymmetric.** Under-assisting a novice is a missed gain. Over-assisting
  an expert is an *active harm* at −0.428.
- **It is heterogeneous.** I² ≈ 90%. It is a real law with noisy boundaries, not a
  dial.

Everything else on the personalisation menu — learning styles, modality
preference, personality type, demographic tailoring — is either debunked or
unevidenced. The honest table is very short:

| Dimension | Status |
|---|---|
| Prior knowledge / expertise on **this** concept | **EVIDENCED** — the one survivor |
| Working-memory load imposed by **this** material | **EVIDENCED** — same law, other face |
| Pace and dosage | **PLAUSIBLE** — evidenced for mastery, weak for micro-adaptation |
| Interest and context of examples | **PLAUSIBLE** — small, real, easily oversold |
| Learning styles / modality matching | **DEBUNKED** |
| Personality or demographic tailoring | **DEBUNKED or unevidenced** |
| Stated preference for difficulty | **ANTI-SIGNAL** — preference moves d ≈ 0.48 while knowledge moves 0 |

---

## 3. What actually changed, and it is not the model

Here is the reframe that makes this section worth writing.

The blocker on real personalisation was **never compute, and never the algorithm.**
It was that knowing where a learner sits on the one interaction that matters —
*on this concept, right now* — required a pretest that cost more attention than the
lesson it was meant to configure. So every system fell back on the two signals that
are free: **stated preference** and **demographic label**. Both are documented dead
ends, and the field's fifty-year record of failure is substantially a record of
optimising against free but worthless signals.

Two things changed.

**First, the measurement got cheap.** Kalyuga and Sweller's *rapid dynamic
assessment* recovers an actionable expertise estimate from **1–3 items in 15–40
seconds**, correlating **r = 0.66–0.92** with full diagnostic instruments that take
**2.5–4.9× longer**. Four validation studies. The learner states a first step, or
completes a partial solution, and that is enough.

**Second, the probe can now be written on demand.** The reason rapid assessment
stayed a laboratory curiosity is that someone had to author a valid, calibrated,
concept-specific probe for every concept in a curriculum. A frontier model authors
it fresh, at the moment of need, for a concept nobody anticipated.

> **Personalisation was never an algorithm problem. It was a measurement-cost
> problem, and the measurement just became affordable.**

That is a much smaller claim than "AI enables personalised learning," and it is the
one with evidence under it.

---

## 4. Four results that should stop most adaptive-learning projects

The field's dominant approach is to treat instruction as a sequential decision
problem — bandits, reinforcement learning, policy optimisation. Four findings, all
from primary sources read in full:

**Most of the literature contains no test.** Of 89 reinforcement-learning-in-
education papers, **54 ran no statistical test at all** — and **45 of those 54 are
content-sequencing papers**, precisely the cluster that measured **0 for 8** in
earlier work. Only **14 of 89** included a non-adaptive control condition.

**The wins are not where people think.** Of 18 documented wins, **14 are
guidance-related and 4 are content-related.** Adaptivity helps by adjusting *how
much help*, not by resequencing *what comes next*. That replicates the split
exactly.

**Bandits are statistically hostile in a classroom.** They need **≥2× the
participants** for equivalent power. And under *temporal entry bias* — students
joining across a term, which is the normal shape of a school year rather than an
edge case — **Type I error reaches 95%, and gets worse as the sample grows.** A
system that adapts as learners arrive can manufacture a significant result from
nothing, more reliably the longer it runs.

**And the flagship comparison is a tie.** MathBot's contextual bandit **matched but
did not beat** a randomised A/B assignment.

There is a fifth finding that is not statistical and matters as much. Across 16
studies and 5,873 participants, people object to being **experimented on** even
when they find either arm individually acceptable — and the effect is
**undiminished among professionals**. Exploration is not a free parameter when the
exploration cost is borne by a specific child in a specific year of their
education.

---

## 5. The controller

What survives all of that is narrower than an adaptive-learning platform and more
useful.

### 5.1 The substrate is never selected

Retrieval practice (**g = 0.499**, 48,478 students), spacing (**d = 0.54**), and the
teaching-expectancy framing (**g = 0.48** vs **−0.02** without) run for everyone,
always. They are not personalisation candidates and they are not A/B tested against
nothing.

This concedes the strongest form of the counter-argument **structurally rather than
rhetorically**: the largest measured effects in this entire survey are *universal*,
not personalised. If a system does only the substrate and no adaptation at all, it
captures most of the available gain. Anything the controller adds must be argued
for on top of that, against that baseline.

### 5.2 The fast loop — seconds, and forbidden to change method

| | |
|---|---|
| **Signals** | Error *type*, latency, help-seeking, partial-solution state, disengagement |
| **May change** | Assistance level · explanation rung · problem granularity · worked-vs-completion-vs-independent |
| **May never change** | **The method.** Not once. |
| **Latency** | Seconds |

The fast loop is where the one surviving interaction lives. It moves *how much
support*, which is exactly the axis the 14-of-18 wins sit on.

### 5.3 The slow loop — four probe points minimum, and it must prescribe

| | |
|---|---|
| **Signals** | Graphed probe scores against a goal line |
| **Minimum evidence** | **≥4 points**; trend judgements need 7–10 weeks |
| **Action** | Fire **one** item from a **closed, ordered** menu — with the reason logged |
| **Latency** | Weeks |

The closed ordered menu is not bureaucracy. Fuchs 1991 is unambiguous: measurement
*without* a named decision rule moved nothing, and both arms revised instruction
more often. **A pivot that is not drawn from a stated menu and logged with a reason
is the arm that failed.**

### 5.4 Log the propensity, always

Every action records the probability with which it was selected. That single
discipline turns the entire deployment into an off-policy evaluation dataset — so
the policy improves **offline, on logs**, rather than online, on children. Given
the 95% Type I error under temporal entry bias and the documented objection to
being experimented on, this is the only ethically and statistically defensible way
to improve a policy in a school.

---

## 6. Bidirectional, and what may never enter the model

The learner learns the topic; the system learns the learner. That second half needs
hard boundaries, because a learner model is **profiling** under GDPR Article 4(4),
which means no adaptive tutor can self-exempt from high-risk classification.

What the model holds: per-concept expertise estimates with timestamps and decay,
misconception flags with the evidence that raised them, retrieval history, and the
log of every pivot with its reason.

What it may **never** hold: inferred emotional state (emotion inference in
education is **prohibited**, not merely high-risk), inferred disability or
diagnosis, personality inference, or any trait-level claim about the person rather
than a state-level claim about a concept.

And it is inspectable and correctable **by the learner and the parent**, decays by
default, and requires stronger evidence to *restrict* what is offered than to
expand it — because the failure mode of a confident learner model is automated
tracking, and we know what that does.

---

## 7. The falsifiable claim, and the condition for deleting this whole section

> With the universal substrate identical in both arms, **probe-assigned entry
> assistance beats the best expert-chosen *fixed* level on delayed transfer** — run
> as a crossover.

Three details carry the weight. **Transfer, not retention**, because Rey and
Fischer found the reversal appears on transfer and not on retention — measuring
retention would look like a null even if the effect is real. **The comparison is a
well-chosen fixed level**, not no-instruction, because against nothing everything
works. And **crossover**, so each learner is their own control, which is the only
design that fits an interaction this heterogeneous.

The concession is stated in advance:

> **If the advantage sits only in the low-prior-knowledge tail, delete the probe and
> always assist.** The measurement would have earned nothing that a default could
> not.

That would be a good outcome. It would mean the answer to "how do we personalise?"
is "mostly, you don't — you run the substrate, you assist by default, and you spend
the saved complexity on getting the universal things right."

---

## 8. What this section commits us to

- **Lead with Cronbach.** Anyone proposing a personalisation dimension states which
  of the seven rows in §2 it belongs to, and defends it there.
- **Measure, never ask.** Preference moves d ≈ 0.48 while knowledge moves zero.
  Stated preference is an anti-signal and is not an input.
- **Per-topic, never per-person.** No trait-level storage. The expertise estimate
  is attached to a concept and decays.
- **The fast loop may not change the method.** Assistance level, rung, granularity —
  that is the whole permitted range.
- **No pivot without a menu item and a logged reason.** The unprescribed arm moved
  nothing.
- **Log propensity on every action** and improve the policy offline. Do not run
  bandits on children in a term.
- **Ship the crossover trial**, on transfer, and publish it if it says the probe was
  unnecessary.

The most valuable thing personalisation research produced in fifty years is a
warning about itself. We are proposing to try again — with one interaction instead
of a hall of mirrors, a fifteen-second measurement instead of a battery, and a
pre-registered condition under which we delete the feature.

---
title: "The Technique Inventory — what the world's best explainers invented, which half of it is scar tissue from not being able to see the learner, and what replaces it"
wave: V
date_researched: 2026-07-29
sources_count: 0
---

# V1 — The Technique Inventory

> **The document this repo has not written.** `N4` graded four explainers against a fidelity
> standard and reported, correctly, that the outcome data does not exist. That is an audit.
> This is the other half: a **named, mechanised, buildable inventory** of the craft itself,
> classified by whether each technique is a real invention or a workaround for a missing
> listener.

---

## §0 — The thesis, stated once, before any evidence

Over roughly fifteen years, a few hundred people — most of them unaffiliated with any
educational institution — invented a craft of explanation that had no prior art. They did it
under a constraint so total that it became invisible to them and to everyone studying them:

> **One artifact. Millions of learners. No return channel.**

They cannot branch. They cannot ask. They cannot see that you did not get it. They cannot
re-render when you frown. Every technique in this document was invented inside that box, and
a large fraction of the craft — larger than anyone has admitted — is not explanation at all.
It is **prosthesis for an absent listener**.

The street interview that surfaces a wrong model before teaching is a proxy for asking *you*.
The interviewer on Numberphile asking the dumb question is a **stand-in for you**. "You might
be thinking…" is a guess at *your* objection. "Pause and ponder" is a **request** because it
cannot be a **gate**. The whole apparatus of anticipated objection, voiced misconception,
deliberate false start, and rhetorical question is one thing wearing many costumes: an
explainer modelling a learner they will never meet, in their head, at authoring time, once,
for everybody.

So the organising question of this document is not *"how do we make videos like theirs?"* It
is:

> **Which of these techniques exist only because the explainer could not see the learner —
> and what replaces each one when the system can?**

Three buckets, and the classification is the deliverable's spine:

| Bucket | Definition | Disposition |
|---|---|---|
| **A — Compensation** | Exists because the explainer cannot see or hear this learner. | **Port the job, discard the form.** The technique's *purpose* survives; its *implementation* is a workaround. |
| **B — Intrinsic** | Would still be the right move with a perfectly responsive tutor sitting beside the learner. | **Build as-is.** These are the real inventions. Do not "improve" them with responsiveness. |
| **C — Constraint-of-medium** | Exists because video is linear, clocked, and non-interactive. | **Dissolves.** Nothing to port. Deleting it is free. |

And a fourth, which the brief did not ask for and which the evidence forced (§2.6):

| **D — Authored-invariant** | Exists because a specific person with taste made a choice no learner model could have derived. | **Curate, do not generate.** The system needs a library, not only a generator. |

The document's ranking of its own findings, stated up front so nothing hides in the middle:

1. **The single most valuable unported technique is 3Blue1Brown's `pause and ponder`, and it
   is unported because in video it is unenforceable.** Sanderson says the prediction is where
   the learning happens; he says it in 34 videos; and he concedes in the same breath that
   *"realistically, a lot of people are a little bit more passive in that moment."* The
   compliance is not observable from the artifact and not required by it. In a responsive
   substrate it becomes a **gate**: the reveal does not render until a prediction is
   committed. The underlying effect is already measured (productive failure `g = 0.36`,
   rising to `0.58` at high implementation fidelity, §01; pretesting/errorful generation,
   §01). Converting an unenforceable *request* into an enforced *precondition* is the highest
   value-per-unit-engineering move in this entire inventory, and it needs no new model
   capability.
2. **The Chinese dual-teacher classroom (双师课堂) is the existing human proof-of-concept for
   this project's entire architecture** — a world-class authored explanation streamed to
   scale, plus a local agent whose only job is to watch one room and intervene. It has been
   running at national scale. Nobody in the English-language discussion of AI tutoring cites
   it. §1.13, §3.9.
3. **Responsiveness is a hazard for at least one bucket-B technique, not an asset.**
   Productive failure requires the failure to complete. A system that can see you struggling
   will be tempted to rescue you, and rescue destroys the effect it was built to produce.
   §2.5.
4. **The misconception street interview does not port cleanly, and the reason is affective,
   not technical.** Watching a stranger be confidently wrong is socially free. Being told
   *you* are wrong is not. §2.4 — "the confession cost."

---

## §1 — The inventory: techniques, by name, with mechanism and example

**Reading the labels.** This section keeps the repo's evidence labels (`MEASURED-RCT`,
`MEASURED-META`, `OBSERVED`, `VENDOR`, `DEMO`, `INFERENCE`) and adds one, per the brief:

> **`CRAFT`** — observed practice by an elite practitioner, described mechanistically,
> **unmeasured**. Craft ahead of evidence is still craft. A `CRAFT` label is not a hedge and
> not an apology; it is a statement that the technique is real, the mechanism is specified,
> and nobody has run the trial. Roughly two-thirds of this inventory is `CRAFT`. That is the
> honest state of the field and it is not a reason to omit anything.

Bucket assignments (**A**/**B**/**C**/**D**) appear inline and are argued in §2. The full
table is §4.

---

### 1.1 — 3Blue1Brown (Grant Sanderson)

8.51M subscribers · 241 videos · 761,430,994 total views · channel opened 2015-03-03.
`OBSERVED` (scraped 2026-07-29). Per the repo's standing rule, **reach is evidence about reach
and nothing else** — the numbers are here so the reader knows the case is not marginal.

Sanderson is the most-studied case in the repo (`N4` §5.1–5.2) and the most misread. The
public discussion is about *animation quality*. The animation quality is the least of it — and
he says so himself, in the one methodology statement that should anchor this entire section:

> *"the thing that I try to make the channel do more than anything else is look visually
> distinctive and **put animations first in the explanation rather than making them a
> supplement to the explanation**. Like if I'm thinking of a topic it's better if I think this
> is the core visual around which the narrative will revolve. Rather than writing a script and
> then later thinking, hmm what visuals will I put to this? I am definitely a big advocate
> also of while I'm animating things **letting what I discover while creating the visuals
> change what the words will be**."*
> — Numberphile Podcast, *"The Hope Diamond – with 3blue1brown"*, 2018-12-12
> (transcript PDF: `https://www.numberphile.com/s/The-Hope-Diamond-with-3blue1brown.pdf`)

Read the second half twice. **The visual is not the output of the explanation; it is the
instrument he uses to find the explanation, and what he learns from building it rewrites the
script.** That is a claim about animation as an epistemic tool, from the person with the
strongest track record in the medium, and it is the deepest thing anyone in this inventory has
said about their own craft. It also has a direct measured correlate — see T1.

**T1 · Continuous transformation preserves referential identity** — **B** · `CRAFT`

The signature move, and the one nobody names. In a 3Blue1Brown video, when a representation
changes, **it is never cut to; it is morphed into.** A vector is dragged into its transformed
position; a grid is deformed rather than replaced; a sum is *pushed* into an integral sign.
The mechanism is precise: a cut forces the learner to re-establish the binding between the
new object on screen and the old one in memory — a working-memory operation whose cost scales
with how many objects are in play. A continuous morph performs that binding **in the
perceptual system**, for free, using the same object-permanence machinery that tracks a
thrown ball. The learner never has to ask "is that the same thing?" because their visual
system already answered.

*Example:* the four-minute unbroken 2×2 linear transformation in *Eigenvectors and
eigenvalues* (`https://www.youtube.com/watch?v=PFDu9oVAE-g`, 2016, 6,213,617 views, 1:20–5:27) — the grid deforms
continuously, and the eigenvector is identified as *the arrow that stayed on its own span*
during the deformation. That identification is not narrated. It is **seen**, and it is only
seeable because nothing cut.

*Cognitive job:* eliminates the referent-rebinding cost of representational change.

**And this is the one place where "animation as argument rather than decoration" is not a
slogan but a measured distinction.** Berney & Bétrancourt (2016): animation overall
**g = 0.23 [0.12, 0.33]**; **representational animation g = 0.40 [0.34, 0.46], k = 59**;
**decorative animation g = −0.05 [−0.17, 0.07], k = 17 — a null.** `MEASURED-META` (§B1).
The entire value of animation sits in whether the motion *carries the referent's state
change*. Continuous morphing is the strongest possible form of representational: the motion
**is** the state change. Nothing measures continuity-of-identity-through-change specifically —
the multimedia literature measures *co-location*, not *continuity* — so the specific mechanism
stays `CRAFT` while the representational/decorative split behind it is `MEASURED-META`.

**T2 · Colour as a persistent variable binding** — **B** · `CRAFT`

A symbol and its geometric referent share a colour, and that colour is stable across the
entire video and often across the entire series. `i-hat` is green in every frame it appears
in, in every video in *Essence of Linear Algebra*. The binding between notation and meaning is
therefore offloaded from working memory to a perceptual channel that has essentially unlimited
capacity for a handful of hues.

*Cognitive job:* removes the symbol-lookup step that split-attention costs are made of.
Nearest measured relatives (§B1): **signaling g = 0.43 [0.35, 0.50], k = 209** (Schneider
et al. 2018) and **spatial contiguity / split attention g = 0.63 [0.55, 0.71], k = 58**
(Schroeder & Cenkci 2018). `MEASURED-META`. Two caveats the repo insists on: signaling is
**subject to expertise reversal** (Richter et al. 2016 — the effect concentrates in
low-prior-knowledge learners, r = 0.17), and nobody has tested a *persistent* binding
maintained across hours of runtime, which is what 3b1b actually does. `CRAFT` for the
persistence. **Expertise reversal here is a direct argument for responsiveness: the colour
scaffold should decay as the learner's fluency with the notation rises, and only a system that
can see the learner knows when.**

**T3 · Obstacle before machinery / concrete-to-abstract descent** — **B** · `OBSERVED`,
effect **not isolated**

Named machinery arrives late — 31–83% of runtime in the sampled corpus (`N4` §5.2). Sanderson
states it as a *first-draft failure mode he corrects against*, which is better evidence than
stating it as a virtue: *"almost always when you understand something the natural inclination
is to go the other way around. I find myself doing this in pretty much any first draft."*
(SoME1 announcement, `ojjzXyQCzso`, 9:58.)

> ⚠️ **Keep `N4`'s correction.** Muller's *Refutation* condition was the *Exposition* script
> **verbatim** — identical definitions-first ordering — plus explicit misconception statements,
> and scored `d = 0.79`. Ordering and misconception-naming are separable; Muller separated
> them; **the effect loaded on the naming.** Ordering is a plausible, untested predicate.
> `MEASURED-RCT` for the naming, `CRAFT` for the ordering.

**T4 · The naive-but-flawed first solution, then progressive refinement** — **B** · `CRAFT`

*"Start with a naive but flawed solution, and then progressively refine it"* (`cDofhN-RJqg`,
9:52). The learner is handed a model that *almost* works, allowed to see exactly where it
fails, and the real machinery arrives as the *repair for a failure they have already felt*.

*Cognitive job:* manufactures a knowledge gap and then fills it — the structural core of
productive failure (`g = 0.36`, `0.58` at high fidelity, §01) delivered **vicariously**,
without the learner having to generate the failed solution themselves. That vicariousness is
exactly what makes it weaker than the real thing, and exactly what a responsive system fixes
(§3.7). `MEASURED-META` for the underlying mechanism, `CRAFT` for the vicarious form.

**T5 · Reinventing the notation rather than presenting it** — **B** · `CRAFT`

Titles like *Reinventing Entropy* (`l6DKRf-fAAM`) are the technique stated in the title. The
definition is not given; it is **derived as the thing you would have had to invent** given the
constraints. Entropy is defined at ~75% of runtime because the preceding 75% is the argument
that something with those properties has to exist.

*Cognitive job:* converts an arbitrary-seeming definition into a forced one. Nearest measured
relative: none. The instructional-explanation literature has an established null on
"instructional explanations" generally (`N4` §1.6), and nothing that isolates *derived* versus
*given* definitions. `CRAFT`.

**T6 · The spared-pain callback** — **A** · `CRAFT`

At 9:16 of the eigenvector video: *"an expression like this would feel completely out of the
blue."* He tells the learner **what they were spared**. This is pure compensation: he cannot
observe whether the structure worked, so he narrates its purpose, inviting the learner to
audit their own experience. A tutor who can see the learner's answer never has to do this —
the check is empirical instead of rhetorical.

**T7 · "Pause and ponder"** — **A** · `OBSERVED` (marker), compliance unobservable

The phrase appears in **34 of his videos** (`N4` §5.2). It is a *request* for the learner to
predict before the reveal. Sanderson grounds it in Kapur explicitly (JMM 2023, `UOuxo6SA8Uc`)
and concedes the limit in the same talk: *"realistically, a lot of people are a little bit
more passive in that moment."*

**This is the flagship A.** The job — force generation before the answer — is intrinsic and
measured. The *form* — an unenforceable spoken request — exists only because the medium cannot
gate. §3.1 specifies the replacement.

**Three measured facts constrain how it must be ported, and every one of them narrows the
design:**

1. **The prequestion effect is specific, not general.** St. Hilaire, Chan & Ahn (2024,
   preregistered): questioned content **g = 0.54 [0.42, 0.66], k = 97, p < .001**; everything
   *else* in the lesson **g = 0.04 [−0.04, 0.11], k = 91, p = .349**. `MEASURED-META` (§N2).
   A prediction gate buys you the step you gated and nothing around it. **Gate the load-bearing
   step; gating everywhere costs attention and returns 0.04.**
2. **Guessing is the moderator.** **g = 0.65 when learners guess vs g = 0.22 when they do
   not**, p < .001. `MEASURED-META`. The gate must accept a wrong answer, not require a right
   one — "I don't know" must not be an accepted token.
3. **Prediction only pays when the prediction is violated.** Theobald & Brod (2022): no main
   effect of predicting before a reveal (**b = −0.090, p = .330**); the **condition ×
   expectancy-violation interaction was b = 0.195, SE = .062, p = .002**. `MEASURED-RCT`.
   **Predicting correctly buys nothing. Being surprised is the whole effect.** This single
   result is the strongest argument in the document for §3.2 — an animation parameterised by
   the learner's own wrong model, run until it visibly breaks, is *engineered expectancy
   violation*, and it is the only technique here whose mechanism has a measured interaction
   term behind it.

And one age boundary that governs deployment: **adults g = 0.62 vs grade-school children
g = 0.22**, p = .020. `MEASURED-META`.

**T8 · Manim as an authored language, and the parameterisation that gets thrown away** —
**C** · `OBSERVED`

Manim (`github.com/3b1b/manim` — 88,991 ★, MIT, created 2015-03-22; community fork
`github.com/ManimCommunity/manim` — 39,784 ★, created 2020-05-19; `gh api`, 2026-07-29) is
not a rendering tool; it is a **language in which explanations are programs**. This matters far
more than the aesthetic. Every 3Blue1Brown scene is a *function of parameters* — the matrix
entries, the number of terms, the sample size — and the published video is **one evaluation of
that function, collapsed to a fixed rendering and then discarded**.

The parameterisation already exists, in source, in public. The medium throws it away.
**This is the single largest C in the inventory**, and the highest-value one: the substrate
that keeps the parameters open is not a research problem, it is a deployment decision.

Sanderson's own framing of the tool is a warning against treating it as a rendering pipeline:
*"A good litmus test for whether it's the right tool is whether the idea of writing code to
create visuals feels inhibiting or liberating"* (`https://www.3blue1brown.com/about`). And on
the codebase itself: *"It began as a scrappy playground of code for my own use cases… The
version I use is probably best viewed as a testing ground."* `OBSERVED`.

> ⚠️ **Rights, from `N4` §7.4, because it governs what can actually be shipped.** `manim` is
> MIT; the `videos` repo is CC BY-NC-SA 4.0 but contains **scene source only, no transcripts**;
> **the videos themselves are all rights reserved.** He permits clips under 60 seconds with
> on-screen attribution. Veritasium is all-rights-reserved (© Electrify US LLC) with no
> licence. **The technique inventory is portable; the artifacts are not.** Build from the
> techniques.

**T9 · The example-density floor** — **B** · `OBSERVED`

One example held for four minutes, against The Organic Chemistry Tutor's ~52 seconds per
worked problem (`N4` §5.2, `5yw1YH7YA7c`). Sanderson's evidence for this is his review of
thousands of SoME entries — an observation over a corpus he did not author, which makes it
better evidence than a self-report: *"entries that struck me as especially clear would often
keep one or two examples front and center… giving the viewer a chance to build their own
intuitions before general rules are presented"* (`cDofhN-RJqg`, 11:14).

**T9a · The explorable he built when video would not do it** — **C, demonstrated** ·
`OBSERVED`

`https://eater.net/quaternions` — an interactive explorable on quaternions, built by Sanderson
**with Ben Eater**. Two of the strongest video explainers in the world, collaborating, chose a
manipulable web artifact rather than a video for the one topic where the rotation group has to
be *turned by hand*. This is the field's own admission of where its medium stops, and it is
the most direct existing evidence for this document's bucket C. `OBSERVED`.

**T10 · SoME as a technique-discovery engine** — **D** · `OBSERVED`

The Summer of Math Exposition is a competition that generates thousands of independent
explanation attempts at the same concepts, judged, ranked, and published. It is the closest
thing the field has to a **combinatorial search over explanation designs** — and it is
entirely human-in-the-loop. A system that can generate and evaluate explanations has an
obvious analogue and nobody has built it (§3.12).

---

### 1.2 — Veritasium (Derek Muller)

The only person in this inventory who ran a randomised controlled trial **before** adopting
the format he built a career on. His PhD (University of Sydney, 2008, *Designing Effective
Multimedia for Physics Education*) is the strongest single result in the literature on
explanation quality and it is his own channel's design document.

21M subscribers · 523 videos · 4,443,828,399 total views · opened 2010-07-21. `OBSERVED`.

**The primary sources, since `N4` cites the thesis second-hand.** Muller's peer-reviewed
papers are retrievable and the key one carries the N = 364 result in its abstract:

| Year | Paper | Venue | DOI |
|---|---|---|---|
| 2008 | **Saying the wrong thing: improving learning with multimedia by including misconceptions** (Muller, Bewes, Sharma, Reimann) | *J. Computer Assisted Learning* 24(2):144–155 | `10.1111/j.1365-2729.2007.00248.x` |
| 2008 | Raising cognitive load with linear multimedia to promote conceptual change (Muller, Sharma, Reimann) | *Science Education* 92(2):278–296 | `10.1002/sce.20244` |
| 2007 | Conceptual change through vicarious learning in an authentic physics setting | *Instructional Science* 35(6):519–533 | `10.1007/s11251-007-9017-6` |
| 2008 | Coherence or interest: which is most important in online multimedia learning? | *AJET* 24(2):211–221 | `10.14742/ajet.1223` |

The thesis (*Designing Effective Multimedia for Physics Education*, Univ. Sydney, 2008) is
linked from `https://www.veritasium.com/publications`; the USyd repository handle
(`hdl.handle.net/2123/3526`) **returns 403 to non-interactive clients** and could not be
retrieved directly.

**A fact in the abstract that `N4` does not carry and that changes the design conclusion:**

> *"**Students with low prior knowledge benefited most, however high prior knowledge learners
> were not disadvantaged.**"* — Muller et al. 2008, `10.1111/j.1365-2729.2007.00248.x`,
> Crossref abstract, verbatim. `MEASURED-RCT`.

**Refutation does not show expertise reversal.** Almost every other technique in this
inventory does — signaling (Richter 2016), worked examples (Tetzlaff 2025: novices **+0.505**,
experts **−0.428**), scaffolding generally. Misconception-naming is the rare intervention that
is safe to apply without knowing the learner's level, which makes it **the correct default for
a cold start** and the first thing a responsive system should do before it knows anything.

**T11 · Misconception-first elicitation by street interview** — **A** · `CRAFT` (the form),
`MEASURED-RCT` (the job)

Stop strangers, ask the question, let them be confidently wrong on camera, *then* teach. The
mechanism has two halves that must be separated because they port differently:

- **The elicitation half** is pure **A**. He cannot ask *you*, so he samples a proxy
  population and shows you the modal wrong answer, betting that it is yours.
- **The activation half** is **B**. Hearing a wrong model stated out loud *activates* the
  learner's own version of it, which is a precondition for displacing it — you cannot
  restructure a belief that is not currently in working memory.

*Example:* *The Most Common Cognitive Bias*
(`https://www.youtube.com/watch?v=vKA4w2O61Xo`, 2014-02-24, 16,703,768 views) is the tightest
instance — viewers are made to commit to a rule (the 2-4-6 task) before the rule is named. The
origin artifact is *Khan Academy and the Effectiveness of Science Videos*
(`https://www.youtube.com/watch?v=eVtCO84MDj8`, 2011-03-17, 1,677,772 views), in which he
explains his own thesis result on camera three months after finishing it — **the only case in
this inventory of a creator publishing the trial that justifies their format before building
the format.**

*Cognitive job:* pre-activation of the to-be-displaced conception; refutation-text structure.
`MEASURED-RCT` — see T12.

**T12 · Refutation: name the wrong belief and mark it wrong** — **B** · `MEASURED-RCT`

Muller's four-condition experiment, N = 364, F(3,461) = 13.625, p < .001 (`N4` §5.2, §29 §3.3):

| Condition | Content | Length | Gain |
|---|---|---|---|
| Exposition | Clear, correct | 7:02 | 1.77 |
| Extended Exposition | Same, longer | 11:22 | 2.41 |
| **Refutation** | **Exposition verbatim + the misconception named** | 9:33 | **4.41** |
| **Dialogue** | Two speakers, one holding the misconception | 11:22 | **4.77** |

`d = 0.79` (Refutation) and `d = 0.83` (Dialogue) against Exposition; replicated at n = 73 on
quantum tunnelling, `d = 0.71`. **This is the only technique in the entire inventory with a
direct randomised effect size attached to the technique itself rather than to a distant
cousin.** Note the design: Refutation was Exposition **verbatim plus one feature**. That
ablation design is the template for every test proposed in §3.

**The meta-analytic picture is smaller and the repo mandates the smaller number.**
Schroeder & Kucera (2022): refutation texts **g = 0.41 [0.30, 0.51], k = 44, n = 3,869** raw,
**trim-and-fill adjusted to g = 0.28 [0.16, 0.39]**. `MEASURED-META`. *Quote 0.28, and say
which.* Against a *published* document (an IDA dyslexia fact sheet) the refutation version
gave **η² = 0.33** at posttest and **η² = 0.175** delayed (Peltier et al. 2020, n = 75) —
one of only two head-to-head tests of real published explanations that exist anywhere.

**And two well-powered replications found nothing.** Mason, Zaccoletti & Carretti (2019,
N = 85) and Mason, Borella & Diakidoy (2020, N = 110): students improved *"regardless of text
read."* `MEASURED-RCT`. The strongest technique in the inventory has a live null attached and
the inventory says so.

> ⚠️ **The adjacent finding that constrains every "show the wrong model" design in §3.**
> Barbieri et al. (2023) on worked examples (**g = 0.48**, 55 studies, 181 effect sizes):
> **correct examples alone outperformed incorrect-only and correct+incorrect combinations.**
> `MEASURED-META`. Showing learners *someone else's* wrong work is measured to be worse than
> showing them right work. Refutation is not the same operation — it names a belief **the
> learner already holds** and marks it wrong — and the distinction between those two things is
> load-bearing for §3.2 and §3.3. Get it wrong and you have built the losing condition.

**T13 · The dialogue form — a confederate who holds the misconception** — **A** · `MEASURED-RCT`

The highest-scoring condition (`d = 0.83`). Two speakers; one is wrong; the wrongness is
argued rather than asserted. The confederate is a **manufactured listener**: someone in the
artifact who does not understand, so that the learner has a proxy for their own confusion.

**This is the purest A in the document.** The entire technique is the construction of a fake
interlocutor because a real one is unavailable. When a real one is available, the confederate
is not needed — *and* (§2.4) something is lost with it that must be replaced deliberately.

**T14 · The felt/real dissociation, and what Muller measured about his own format** —
`MEASURED-RCT`

The same thesis contains the most important table in this repo's argument (7-point opinion
form, quantum tunnelling replication):

| Item | Dialogue | Exposition | |
|---|---|---|---|
| I learned something from the video | 5.7 | 5.6 | n.s. |
| I could follow the explanations | 5.4 | 5.6 | n.s. |
| **I found the video dull** | **3.4** | **2.6** | **p < .01** |
| **The video was too long** | **3.2** | **2.4** | **p < .01** |
| **I'd enjoy seeing stuff like this in lectures** | **4.8** | **5.5** | **p < .05** |

Perceived learning was **flat** while actual learning differed by `d = 0.71`. The better
explanation felt **duller**, felt **too long**, and students **preferred the worse one**.
Every one of those three significant rows is a signal a recommender system reads and acts on.
`MEASURED-RCT`.

**The consequence for this inventory:** a technique's popularity among creators is not
evidence of its efficacy, and may be *inverse* evidence. This is why the inventory keeps
`CRAFT` techniques on mechanism rather than on reach.

**T15 · The engineered adjudication at absurd scale** — **B** · `CRAFT`

When a dispute cannot be settled by argument, build the apparatus. A kilometre of cable to
test how fast electricity "flows"; a vehicle with a wheel-driven propeller to settle whether
it can outrun the wind (*Blackbird*, and the public wager with Alexander Kusenko that
followed). The technique is: **make the physical world the referee, at whatever cost, on
camera.**

*Cognitive job:* converts a belief conflict into an observation. This is conceptual-change
instruction's "dissatisfaction with the existing conception" step (Posner et al.), implemented
as engineering rather than as text. `CRAFT`.

**T16 · Public self-refutation** — **B** · `CRAFT`

The follow-up video that says *the previous video was wrong*, or *incomplete*, or *right for
the wrong reason*. Veritasium has done this repeatedly and has had it done to him (§1.14,
AlphaPhoenix). The technique models epistemic revision as a normal operation rather than a
humiliation — which is exactly the disposition a learner needs and almost never sees
demonstrated by an authority.

*Cognitive job:* epistemic norm-setting; reduces the affective cost of the learner's own
future error. Nearest measured relative: none directly. `CRAFT`.

---

### 1.3 — Primer (Justin Helps)

**T17 · The simulation *is* the argument** — **B** · `CRAFT`

Most explainers narrate a claim and illustrate it. Primer states a rule, encodes it as an
agent behaviour, presses run, and **reports what came out**. The distinction is total: in a
3Blue1Brown video the animation is authored to be correct; in a Primer video the animation is
*generated* and could have come out otherwise. The explainer has given up control of the
conclusion — and the viewer can tell.

*Example:* *Simulating the Evolution of Aggression*
(`https://www.youtube.com/watch?v=YNMkADpvO4w`, 2019-07-27, 24,858,944 views) and *Simulating
Natural Selection* (`https://www.youtube.com/watch?v=0ZGbIKd0XrM`, 2018-11-14, 15,596,157
views) — hawk/dove dynamics emerge from the encoded payoff rules rather than being asserted
from them. The channel has **24 videos and 98.2M views**; the views-per-video ratio is the
highest in this inventory by a wide margin, which is what a technique with no substitutes looks
like. `OBSERVED`.

**The lineage is documented and it matters.** Helps's first engine,
`github.com/Helpsypoo/primerpython` (★1,364, 2018, now archived), says in its own README:
*"This is a library of tools that lets you write high-level functions to build and animate
objects in **Blender**… **Much of the structure comes from manim, 3blue1brown's animation
engine.**"* He has since moved to C#/Godot (`github.com/Primer-Learning/PrimerTools`, ★119,
active 2026). **Manim's real contribution was not the renderer; it was establishing that an
explanation should be a program.** T8's parameterisation argument applies to Primer with more
force, because in Primer the program is a *model* and not only a *drawing*.

*Cognitive job:* transfers the warrant from the narrator's authority to the model's mechanics.
This is the *executable-and-verifiable* property this repo argues for in §F3, arrived at
independently by a YouTuber. `CRAFT`.

**T18 · Generations as the exposition's timeline** — **B** · `CRAFT`

The video's clock **is** the model's clock. There is no separate narrative structure imposed
on top; the story is "generation 1 … generation 200," and the pedagogical beats are wherever
the dynamics change regime. This is why the videos feel like watching an experiment rather
than a lecture.

**T19 · Ablate one parameter, re-run, show the regime change** — **B** · `CRAFT`

Change the mutation rate, or the food density, or the cost of aggression, and run it again.
The learner sees the *family* of outcomes rather than one outcome. This is Bret Victor's
ladder of abstraction (T48) implemented in a linear medium — and it is exactly the technique
that becomes trivial and continuous once the learner holds the slider (§3.2, §3.5).

**T20 · The minimally-anthropomorphic agent ("blobs")** — **B** · `CRAFT`

The agents are simple rounded shapes with no faces and no expressed intent. This is a
*discipline*, not a style choice: a face would smuggle in intention, and the entire lesson of
evolutionary simulation is that the outcome requires no intention. The visual design is
constrained by the epistemics of the claim.

*Cognitive job:* prevents the teleological misconception that is the single most common error
in learning natural selection. Nearest measured relative: the misconception literature on
evolution (teleology/essentialism) is large; the *design constraint* is unmeasured. `CRAFT`.

---

### 1.4 — Ben Eater

**T21 · Build it from nothing, in real time, with nothing hidden** — **B** · `CRAFT`

An 8-bit computer on breadboards, one component at a time, over dozens of hours. Every wire is
visible. There is no "and now we add the ALU" — you watch the ALU get wired, and it is a pile
of 74LS181s and jumper cable, and it works. The technique's claim is: **the abstraction you
find intimidating is made of things you can see**.

*Example:* the *Building an 8-bit breadboard computer* series — 44 videos, hub at
`https://eater.net/8bit` — and the *world's worst video card* series
(`https://www.youtube.com/watch?v=l7rce6IQDWs`, 2019-07-05, 6,961,306 views, plus three
sequels). Channel: 1.38M subscribers, 130 videos, 107.6M views. `OBSERVED`.

Two biographical facts that are not decoration. Eater states on `https://eater.net/about` that
he **has no degree** — *"I went to school for computer science, but failed out after the first
year"* — and that he spent seven years at **Khan Academy**, joining in 2011 as lead exercise
developer. The person who built the most rigorous build-it-from-nothing corpus in existence
came out of the largest exercise-generation system in existence, and left it to do this.

*Cognitive job:* collapses the felt distance between the learner's competence and the target
system. Nearest measured relative: none. Grounding/embodiment work in this repo (§F7) is the
closest, and it does not measure this. `CRAFT`.

**T22 · The instrument as ground truth** — **B** · `CRAFT`

Eater does not tell you the signal is there. He puts a scope probe on the trace and you see
it. The warrant for every claim is an **external, non-narrating instrument**. When the trace
looks wrong, the claim is wrong, and the video says so.

*Cognitive job:* separates "the teacher said so" from "the world said so." Structurally
identical to T15 (Veritasium's engineered adjudication) at a thousandth of the budget.
`CRAFT`.

**T23 · Debug on camera; the diagnosis is the content** — **B** · `CRAFT`

The circuit does not work. Eater does not cut. He reasons out loud through the fault tree —
*is the clock running? is the enable line asserted? is that pin actually connected?* — and the
**diagnostic procedure is the transferable skill**, more than the circuit is.

*Cognitive job:* models expert troubleshooting, which is otherwise invisible because experts
do it fast and silently. Nearest measured relative: worked-example effect (§B1) extended to
*process* rather than *solution* — a "worked debugging example." Unmeasured in that form.
`CRAFT`.

**T24 · Physical instantiation of an abstraction** — **B** · `CRAFT`

A bus is literally eight wires. A register is literally a chip that holds. Address decoding is
literally a NAND gate whose output you can probe. The abstraction and its implementation are
in the same frame at the same time.

---

### 1.5 — Sebastian Lague

**T24a · Demand-ranked topic selection** — **A** · `OBSERVED`

Eater's FAQ documents that he takes topic requests **only via a Reddit thread, ranked by
upvotes**: *"Requests I get through email/twitter/etc. are much more likely to be ignored,
since the Reddit thread is what I look at when considering what people want."* This is a
deliberately-built, low-bandwidth, aggregate return channel — a creator constructing the
crudest possible instrument for seeing his audience, because none is supplied. Pure **A**, and
the honesty of the design is instructive: he does not pretend it tells him about any
individual.

**T25 · The visible iteration loop** — **B** · `CRAFT`

The *Coding Adventures* series shows v1, which looks bad; v2, which looks bad differently;
and v5, which looks good — with the reasoning for each change. Channel: 1.4M subscribers, 296
videos, 114.7M views; exemplars include *Coding Adventure: Chess*
(`https://www.youtube.com/watch?v=U4ogK0MIzqk`, 2021, 4.26M views), *Simulating Fluids*
(`rSKMYc1CQHE`, 2.57M), *Simulating an Ecosystem* (`r_It_X7v-1E`, 2.34M), *Ant and Slime
Simulations* (`X-iSQQgOd1A`, 2.18M). The learner sees that the
polished result is the *end* of a process, not a property of the author.

*Cognitive job:* corrects the "expert produces finished work in one pass" misconception,
which is a load-bearing demotivator (§F6). Also functions as a **vicarious productive-failure**
sequence (T4). `CRAFT`.

**T26 · Failure retained as content, not as blooper** — **B** · `CRAFT`

Approaches that did not work are kept in the main narrative with their diagnosis, not exiled
to an outtake. The distinction matters: a blooper frames failure as entertainment; a retained
failure frames it as method.

**T27 · The executable artifact, and the tournament** — **B** · `OBSERVED`

The code is published, one repo per episode, matched 1:1 (`Fluid-Sim` ★1,276, `Boids` ★945,
`Ant-Simulation` ★260 — whose entire description is the video URL; `Digital-Logic-Sim` ★4,627).
The explanation is therefore **runnable and modifiable by the learner** after the video ends.
This is the one technique in the video-native set that already carries its own interactivity —
smuggled in through a GitHub link because the medium would not carry it.

And once, it went further: `Chess-Challenge` (★1,779, 2023) — *"Create your own tiny chess
bot!"* — turned the explanation into **an entry condition for a public tournament**, which he
then ran and published as a video. The explanation's terminal state was not "you understood
it" but "you submitted an agent that competed." That is T70 (hand over authorship) achieved
inside the video ecosystem, and it required leaving the video to do it.

---

### 1.6 — Mark Rober

**T28 · Spectacle → principle** — **B** · `CRAFT`

Engineer a set-piece so extreme that the target concept is **the only available explanation**
of what the viewer just watched. A backyard-sized elephant-toothpaste eruption, a glitter bomb
with six cameras, a world's-largest Nerf gun. The spectacle is not decoration and not a hook —
it is a **constructed situation in which the principle is forced**.

*Cognitive job:* creates a need-to-know that precedes the content. This is the "motivating
question" of T3/T7 built out of physical materials at a five-figure budget.

> ⚠️ **The nearest measured relative points the other way, and it has numbers.** The
> **coherence principle**: removing seductive detail is worth **g = 0.33 [0.18, 0.48], k = 68**
> (Sundararajan & Adesope 2020); a 2026 MASEM (Cheng et al., 177 effect sizes / 50 studies)
> puts seductive details at **g = −0.16** overall (comprehension −0.19, recall −0.17, transfer
> −0.12), **mediated by extraneous load only** — intrinsic and germane load do not mediate.
> `MEASURED-META` (§B1, §N2).
>
> **But the moderator rescues Rober specifically, and this is worth knowing.** The coherence
> effect splits hard by persistence: **persistent on-screen seductive detail g = 0.43 [0.29,
> 0.57], k = 47** versus **transient g = 0.12 [−0.33, 0.57], k = 18 — not significant.** A
> spectacle that happens, resolves, and gets out of the way is in the transient class. A
> decorative element that sits on screen during the explanation is in the expensive one.
>
> The technique is therefore defensible exactly when the spectacle is (a) **transient** and
> (b) **non-tangential** — the concept is genuinely load-bearing for the outcome. Where it is
> neither, this is a seductive detail with a five-figure budget. `MEASURED-META` for the
> boundary, `CRAFT` for the load-bearing case.

**T29 · Stakes-first cold open** — **A/C** · `CRAFT`

You see the payoff — the squirrel on the obstacle course, the package about to be stolen —
before you learn any mechanism. Partly **A** (a bid for attention from a viewer who has not
committed) and partly **C** (a retention-curve optimisation for a recommender system). Almost
none of it is **B**.

**T30 · The consequence-bearing test** — **B** · `CRAFT`

The glitter bomb is deployed against actual package thieves. The squirrel course is run by
actual squirrels. The demonstration has a **real target that can defeat it**, which is what
distinguishes it from a rigged demo. The possibility of public failure is what makes the
success informative.

---

### 1.7 — Steve Mould

**T31 · The apparatus that refuses to behave** — **B** · `CRAFT`

A chain of beads in a beaker leaps *upward* out of the container before falling — the
self-siphoning bead chain, or "chain fountain." The demonstration is chosen precisely because
the learner's model predicts something else and the apparatus does not care.

*Cognitive job:* this is **cognitive conflict** in the Posner/Strike sense — dissatisfaction
with the existing conception — delivered by an object rather than by an argument. Related
measured effect: refutation-text and conceptual-change instruction (T12, `d = 0.79`). The
physical-demonstration form is unmeasured against the textual form. `CRAFT`.

**T32 · The two-explanation shootout and the discriminating experiment** — **B** · `CRAFT`

Two mechanisms are proposed for the chain fountain. Rather than picking, Mould specifies **an
observation that would differ between them** and goes and makes it. The *design of the
discriminating test* is the content.

*Cognitive job:* teaches the structure of hypothesis discrimination, which is the actual
transferable skill and is almost never modelled in instruction. Nearest measured relative:
none. `CRAFT`.

**T33 · Self-refutation across videos, against his own prior explanation** — **B** · `CRAFT`

Mould's chain-fountain explanation was revised in public — including against work by others
(Biggins & Warner) — over multiple videos, and the thread has now run **thirteen years**:
2013 demonstration → *World Record Chain Fountain? The Mould Effect Explained* (2.72M views) →
*NASA tested my chain theory in space* (`NtZaP8VMv0c`, 14.3M views, his best-performing video
on the thread). The effect is now called the **Mould effect** in the physics literature.

**This is the longest-running single explanation in the inventory and it is a correction
sequence, not a lesson.** An artifact that improves for thirteen years under public
adversarial pressure is a thing no curriculum produces and no LLM currently produces either.
Same structure as T16, iterated. `OBSERVED`.

---

### 1.8 — Numberphile / Computerphile (Brady Haran)

**T34 · The interviewer as designated novice** — **A** · `CRAFT`

Haran is not a mathematician and does not pretend to be. He asks the question the viewer
would ask — *"but why does that matter?"*, *"hang on, what's a group?"* — and the expert
answers **a person**, not a camera.

**This is a manufactured listener, hired.** It is the same A as Muller's dialogue confederate
(T13) with the roles reversed: instead of a wrong model being voiced, an *absence of model* is
voiced. The technique exists entirely because the actual learner cannot interrupt.

*Example, and it is the cleanest possible demonstration:* **OEIS A247698 is named "Brady
numbers"** (`https://oeis.org/A247698`) — a sequence that exists because Haran, who is not a
mathematician, asked a naive question on camera and the mathematician present found it was
worth answering. The designated-novice role produced a citable mathematical object. Combined
scale: Numberphile 4.76M subs / 812 videos / 725.9M views; Computerphile 2.63M / 915 / 238.5M.
`OBSERVED`. Haran's own account of the method is in his Zeeman Medal lecture *Treasure Trove*
(`https://www.youtube.com/watch?v=tsZkzxEhpHk`, 2025-07-27) and the Numberphile Podcast Q&A
(`https://www.numberphile.com/podcast/brady-haran-qa`); **no verbatim "I ask the dumb
questions" sentence was retrievable** and none is invented here.

*Cognitive job:* supplies the questions the learner cannot ask; forces the expert out of
expert register. Related measured effect: the **expert blind spot** literature (`N4` §1.5) —
which, note, does not measure learning.

**T35 · Brown paper, and the rate-limiting of the expert** — **B** · `CRAFT`

The medium is a sheet of butcher paper and a marker. It is deliberately low-bandwidth and
high-latency: the expert can only go as fast as they can write, and writing is far slower than
speaking, which is far slower than thinking. **The medium enforces a pace the learner can
follow.**

*Cognitive job:* pacing control by material constraint rather than by discipline. Nearest
measured relative: **segmenting principle** (§B1) — but segmenting chunks *content*, whereas
this throttles *rate*. Unmeasured in that form. `CRAFT`. Identical in mechanism to Khan's
real-time handwriting (T74) and to Alakh Pandey's board derivations (T77) — three
independent inventions of the same constraint.

**T36 · Unscripted generation, hesitation retained** — **B** · `CRAFT`

The expert is thinking on camera. The false starts, the *"no wait, that's not right"*, the
pause before the right word — all kept. What the learner sees is not a polished result but
**mathematics being done**, including at the speed it is actually done.

**T37 · One expert, one concept, no institutional frame** — **B/D** · `CRAFT`

No curriculum, no learning objectives, no assessment. The unit of publication is *a thing a
person finds interesting*, which is why the corpus covers Graham's number and the parker
square and not the AP syllabus. This is a **D** as much as a B: what is being transmitted is
partly the person's taste, which is not derivable from a learner model.

---

### 1.9 — Kurzgesagt

**T38 · The scale ladder** — **B** · `CRAFT`

A magnitude too large to grasp is reached by a **chain of familiar anchors**, each one used to
build the next: a grain of sand → a beach → the sand on Earth → stars in the galaxy. No step
in the chain exceeds the learner's intuitive range; the composition does.

*Cognitive job:* makes an incomprehensible quantity representable by decomposing the
incomprehension into steps that are individually comprehensible. Nearest measured relative:
the analogy/comparison literature (structure mapping); no measured effect on *chained* anchors
specifically. `CRAFT`.

**T39 · The metaphor with a published, per-claim source graph** — **B** · `OBSERVED`

Every Kurzgesagt video ships a **public sources document** at a predictable URL
(`sites.google.com/view/sources-<slug>`; e.g. the *Loneliness* video `n3Xv_g3g-mA` →
`https://sites.google.com/view/sourcesloneliness/startseite`). This is not a citation ritual.
The document is organised **line by line against the script**, mapping individual spoken
sentences to citations with `Quote:` and `Summary:` fields:

> *"– In the UK 60% of 18 to 34 year olds say that they often feel lonely. (source displayed in
> video) #The lonely society?, 2010"* — `OBSERVED`, verbatim from the live document.

**That per-claim granularity is a provenance graph, hand-built, for a general audience,
by an animation studio.** It is the artifact this repo's grounding work (§F3, §G1) argues for,
and the fact that a YouTube channel ships it and academic publishing does not is worth sitting
with.

Their published process (`https://kurzgesagt.org/what-we-do`) states the mechanism in the
research phase: *"The last step is **preparing a sourcesheet for each video to prove our claims
and make our process transparent**."* The script phase: *"**This can take about a dozen
drafts**… The ultimate goal is to offer a new perspective on a topic and leave viewers with new
insights – **without them really noticing**."* The illustration phase: *"After **deliberating
over the best visual metaphors** and ideas for each scene…"*

> ⚠️ Note the exception that proves it: *Optimistic Nihilism* (`MBRqu0YOH14`), described in one
> line as *"The philosophy of Kurzgesagt"*, ships **no sources document**. The boundary is
> enforced by the presence or absence of the artifact, which is a cleaner signal than any
> hedging language could be.

*Cognitive job:* lets an explanation take metaphorical risk without the learner acquiring a
false model — **provided the learner reads the document, which is a `C` problem** (§2.7). The
depth is one click and one context-switch away, which is one too many. In an interactive
substrate the boundary is inline and reachable at the exact sentence it qualifies.

**T40 · Aesthetic constancy as a retrieval cue** — **B/C** · `CRAFT`, with a warning

A single unmistakable visual language across hundreds of videos, plus recurring characters
(the birds). Argument for: consistent surface features act as a retrieval cue and reduce the
per-video cost of learning a new visual grammar. Argument against: **this is exactly what the
seductive-details literature warns about** (§B1) — decorative elements that consume attention
without carrying content. The birds are load-bearing for *engagement* and, as far as anyone
has measured, not for *learning*. Kept in the inventory with the tension stated.

**T41 · Emotional frame wrapped around a factual payload** — **A** · `CRAFT`

*Optimistic Nihilism*, *The Egg*, the loneliness videos. The affective frame does motivational
work that a linear artifact cannot do adaptively — it must be baked in at authoring time,
pitched at a modal emotional state. **A**: a responsive system knows whether this learner is
currently discouraged and can supply the frame *when it is needed* instead of always.

---

### 1.10 — The rest of the video-native field

**T42 · Vsauce (Michael Stevens) · Definitional destabilisation** — **B** · `CRAFT`

Take a word the learner believes is settled — *"how much of the Earth is in the way?"*,
*"what is the shortest path?"*, *"is anything real?"* — and demonstrate that the definition
they hold does not survive contact with edge cases. The video is a *sustained attack on a
concept boundary*.

*Cognitive job:* converts an inert, over-confident concept into a live problem. Structurally,
it is refutation (T12) applied to a **definition** rather than to a causal belief. Unmeasured
in that form. `CRAFT`.

**T43 · Vsauce · The tangent chain** — **A/C** · `CRAFT`

The digression that returns. Functions as an attention-maintenance device for a viewer who
might leave, and as a curiosity-preservation mechanism. Almost entirely compensation and
medium-constraint: a system that can detect disengagement does not need a *scheduled* tangent,
and a learner who can ask does not need the tangent taken *for* them.

**T44 · SmarterEveryDay (Destin Sandlin) · The host fails publicly at a motor task** —
**B** · `CRAFT`

The *Backwards Brain Bicycle*: Sandlin, who understands exactly how the bicycle works, cannot
ride it, and it takes him eight months to learn. The technique is to make a
**knowledge-versus-ability dissociation** unarguable by demonstrating it on the presenter's own
body, over months, on camera.

*Cognitive job:* directly attacks the "I understood the explanation, therefore I can do it"
illusion — this repo's felt/real gap expressed in a form nobody can argue with. The canonical
measurement of that gap is Buljan et al. (2018, *J Clin Epi*, three parallel RCTs, n = 171 /
99 / 64): infographic versus plain-language summary produced **no difference in knowledge**
while **preference moved d = 0.48** and user-friendliness **d = 0.46**. `MEASURED-RCT`.
Sandlin's bicycle is that dissociation staged on a human body for eight months. It is the
best existing *intervention* against illusion-of-competence in the entire corpus, and a
responsive system can run it continuously and cheaply (§3.11). `CRAFT`.

**T45 · SmarterEveryDay · The instrument that changes the timebase** — **B** · `CRAFT`

The high-speed camera. A phenomenon that is invisible because it is fast becomes ordinary
perception at 10,000 fps. The technique is: **move the phenomenon into the learner's
perceptual band** rather than describing it.

**T46 · Applied Science (Ben Krasnow) · Reproduce the canonical apparatus in a garage** —
**B** · `CRAFT`

Scanning electron microscope (`https://www.youtube.com/watch?v=VdjYVF4a6iU`, 616K views),
X-ray backscatter imaging, thermoacoustic engines — built at home from purchasable parts. The
signature is the companion video *DIY SEM – Sources, Costs and References*
(`L6HxTk9tfQk`, 94,552 views): **a tenth of the audience, and it is the bill of materials.**
The 522,000-view gap between the demonstration and its reproducibility appendix is the
clearest measurement in this document of how much of an audience actually wants to build the
thing — and a system that can ask *which learner you are* does not have to choose. The claim is not "here is how an SEM works"; it is **"an SEM is a
thing a person can build, and here is the actual bill of materials."**

*Cognitive job:* converts institutional knowledge into reachable knowledge; kills the belief
that the frontier is behind a door you do not have a key to.

**T47 · Applied Science · Instrument before claim** — **B** · `CRAFT`

Build the measurement rig first, validate it against a known quantity, *then* measure the
unknown. The epistemics are visible in the ordering. Same family as T22 and T15.

**T48 · CGP Grey · The useful lie, declared** — **B** · `CRAFT`

State a clean model, use it, and then explicitly announce that it was a simplification and
what it hides. Grey does this structurally — *"this is a lie, but a useful one"* — rather than
burying the caveat.

*Cognitive job:* this is **explicit level-of-abstraction signalling**, and it is the single
most underrated technique in the inventory. The learner is told which rung of the ladder they
are standing on. Without it, every simplification silently becomes a misconception the next
teacher has to refute. Maps onto this repo's `F10` explanation-laddering work (ELI10/15/20/25)
— and note that **Grey's version supplies the metadata that makes the ladder navigable**,
which the ELI-n framing alone does not. `CRAFT`.

**T48a · CGP Grey · Retroactive A/B retitling of the back catalogue** — **C** · `OBSERVED`

Grey systematically re-titles published videos to test performance: *Humans Need Not Apply*
(2014-08-13, 19.3M views) now displays as *"What Happened to Horses Is Happening to Us"*;
*The Trouble With Tumbleweed* (14.2M) now displays as *"Tumbleweeds Kill Themselves on
Purpose"*. `OBSERVED` (verified by upload date + description, 2026-07-29).

Keep this in the inventory as the **reductio of bucket C**. The artifact's *name* — the handle
by which a learner and a citation and a syllabus refer to it — is now a mutable field optimised
against a click-through metric. There is no pedagogical variable here at all. It is a pure
distribution artifact, and it has the practical consequence that **any explanation atlas
keyed on titles will silently break.** Key on video ID.

**T49 · CGP Grey · The footnote video** — **A/C** · `OBSERVED`

A second artifact (*"Footnote: …"*) holding the qualifications, the corrections, and the
edge cases, so the primary artifact can stay clean. This is a **bimodal-audience workaround**:
he cannot serve the pedant and the newcomer in one linear stream, so he ships two streams and
lets the audience self-sort. In an interactive substrate this is an expansion in place, and
the technique disappears entirely.

**T50 · CGP Grey · Invented concrete referents for abstract systems** — **B** · `CRAFT`

*Rules for Rulers* has "keys to power" as named, countable objects. The Hexagon islands.
"Grey's law." An abstract system is given a **fictional but internally consistent physical
instantiation** that the learner can then reason about concretely and transfer back.

**T51 · Tom Scott · Standing where it happened** — **B** · `CRAFT`

The *Things You Might Not Know* / *Amazing Places* form: single take, on location, presenter
physically at the referent. The claim is grounded by co-presence — the thing being explained
is behind him and can be pointed at.

**T52 · Stand-up Maths (Matt Parker) · Do it the stupid way, at scale** — **B** · `CRAFT`

Calculate π by rolling 500 dice; measure it with pies; build a domino computer. A concept is
demonstrated by **executing its most naive possible implementation at absurd cost**, so that
the concept's structure is visible in the labour.

*Cognitive job:* makes an algorithm's cost and structure physically felt. Related: T21
(build-from-nothing). `CRAFT`.

**T53 · Vihart · Explanation at the speed of thought, against the pacing norm** — **B/D** ·
`CRAFT`

*Doodling in Math Class*: narration far faster than any pedagogical guideline permits, drawn
in real time, framed as boredom and rebellion rather than instruction. It works, and it works
by **rejecting the modal-learner pacing compromise** in favour of a specific register that a
specific audience finds electric. This is a **D**: the value is in the authored voice, and no
learner model produces it.

**T54 · Welch Labs · History as the scaffold** — **B** · `CRAFT`

*Imaginary Numbers Are Real*: the concept is introduced through the actual historical sequence
of people who needed it and did not have it. The learner's confusion is legitimised by being
**the same confusion the field had**, for two centuries, with names attached.

*Cognitive job:* de-pathologises the learner's difficulty and supplies the motivating problem
for free (the historical actors had a real problem). `CRAFT`.

**T55 · The Coding Train (Daniel Shiffman) · Live coding with errors retained** — **B** ·
`CRAFT`

Type it, run it, watch it break, read the actual error message, fix it. The **error message is
read out loud** — a small thing that turns the most feared object in programming into a
routine information source. Same family as T23 (Eater) and T26 (Lague).

**T56 · Andrej Karpathy · Build the whole thing from zero, in one sitting, in a notebook** —
**B** · `CRAFT`

*Let's build GPT from scratch* / *Neural Networks: Zero to Hero*. Nothing imported that has
not been built; the notebook runs top to bottom; every abstraction is opened before it is
used. This is Ben Eater's technique (T21) in software, and it is the closest existing
artifact to what this repo's `F3` (executable/verifiable) section argues for.

**T57 · AlphaPhoenix · Empirical adjudication *between* explainers** — **B** · `CRAFT`

Build the measurement rig to settle a dispute that two other explainers are having in public —
most visibly the "how fast does electricity actually travel down the wire" exchange following
Veritasium's video. The technique is new and it is a genuine invention: **the explanation
corpus becomes self-correcting because a third party can run the experiment.**

*Cognitive job:* demonstrates that the resolution procedure for a factual dispute is
measurement, not authority or popularity. Nothing in the instructional literature covers this.
`CRAFT`.

**T58 · Practical Engineering (Grady Hillhouse) · Scale-model failure** — **B** · `CRAFT`

Build a small dam in the garage and break it. Build a small levee and undermine it. The
failure mode of a system too large and too dangerous to fail on camera is reproduced at 1:50
and destroyed.

**T59 · The Organic Chemistry Tutor · The reference work that is not an explanation** —
**B (different job)** · `OBSERVED`

10.8M subscribers, 3,106 videos, 1.76B total views; machinery first, no chapter structure,
~52 s per worked problem; **lowest first-decile replay mass in `N4`'s 51-video sample (0.081
vs. 0.291 mean)** — nobody replays the opening because there is nothing there to replay
(`N4` §5.3). This is a *lookup surface*, and it is the largest channel in the class.

**Keep it in the inventory, because the classification exercise is incomplete without it.**
The mistake would be to grade it as a bad explanation. It is a good index. A responsive system
needs both, and needs to know which one the learner is currently asking for — a **query-intent
classification** that no video platform performs and that is trivial when the learner can
speak (§3.13).

---

### 1.11 — Bartosz Ciechanowski — the closest existing thing to the target

If one practitioner's work should be read end-to-end before building anything, it is
`ciechanow.ski`. The articles are, structurally, **the design this repo is trying to reach,
built by one person with no adaptivity at all.**

**The density, measured from the served HTML rather than estimated** (`OBSERVED`, 2026-07-29 —
counting `div.drawer_container` placeholders, which is exactly one per interactive figure):

| Article | Date | Interactive figures | Sections | ~words | JS bundle |
|---|---|---|---|---|---|
| *Gears* | 2020-02-12 | **30** | 10 | ~5.0k | `gears.js`, 117 KB |
| *Lights and Shadows* | 2020-07-01 | **44** | 14 | ~5.0k | `light.js`, 264 KB |
| *Internal Combustion Engine* | 2021-04-29 | **69** | 8 | ~6.0k | `ice.js`, 282 KB |
| *Curves and Surfaces* | 2021-11-02 | **90** | 13 | ~8.2k | `curves.js`, 337 KB |
| *Mechanical Watch* | 2022-05-04 | **93** | 13 | ~8.2k | `watch.js`, 327 KB |
| *Moon* | 2024-12-17 | **120** | 10 | — | `moon.js` |

*Gears* has **30 figures, 26 dedicated slider controls, and 108 paragraphs — one manipulable
figure per 3.6 paragraphs.** *Moon* has 120. For comparison, a well-regarded interactive
article in a mainstream publication ships two or three.

**The stack is hand-rolled and has no dependencies.** A shared `base.js` (34 KB) supplies
matrix math, a Canvas2D wrapper, a pointer/slider input layer, and a `requestAnimationFrame`
tick; the richer articles add raw WebGL with inline GLSL (14 fragment shaders in `curves.js`,
11 in `ice.js`, 10 in `light.js`) and *Sound* adds Web Audio. No React, no D3, no Three.js, no
lazy instantiation. **The article source is closed** — his GitHub (`github.com/Ciechan`, 1,352
followers) holds only pre-2018 iOS work. `OBSERVED`.

**T60 · One manipulable figure per claim, adjacent to the claim** — **B** · `CRAFT`

Not "an interactive at the end of the section." Every 3.6 paragraphs there is a widget, and
the widget instantiates **exactly the sentence above it**. The reader never holds a claim in
memory while scrolling to find its illustration.

*Cognitive job:* contiguity taken past the limit the literature has tested. Measured
relatives (§B1): **contiguity overall g = 0.74 [0.67, 0.82], k = 46** (Ginns 2006);
**temporal contiguity g = 0.78 [0.64, 0.92], k = 13**; **spatial contiguity / split attention
g = 0.63 [0.55, 0.71], k = 58, n = 2,426** (Schroeder & Cenkci 2018), validated by
eye-tracking and the most mechanically checkable principle in the set. `MEASURED-META`.
Ciechanowski's version is past all of them: the illustration is not merely *near* the text, it
is *the text's referent, live, under the reader's hand*. `CRAFT` for that density.

**T61 · Progressive degrees of freedom** — **B** · `CRAFT`

The figures build the complete system **one control at a time**. The first figure has one
slider. The tenth has six, and the reader has met each of the six individually, in order, with
the others held fixed. By the end the reader is manipulating a full model they could not have
understood if handed it at the start.

*Cognitive job:* this is **cognitive-load management via degrees-of-freedom sequencing** and it
is a better-specified version of "scaffolding" than anything in the instructional literature.
It is also the exact mechanism a generated interactive most often gets wrong — generated
widgets tend to expose all parameters at once. `CRAFT`. **High priority to port.**

**T61a · Manipulate first, explain second — and this is the finding that should change the
build** — **B** · `CRAFT`

Reading the raw HTML of *Gears* exposes an ordering that is invisible when you read the page
normally, and it is consistent:

> *"In the demonstration below you can control the fan's speed using a slider:"*
> `<div class="drawer_container" id="gears_angular_velocity"></div>`
> `<div id="gears_angular_velocity_slider_container"></div>`
> *"The speed of a rotating fan is a different kind of speed than that of a car…"*

**The invitation to manipulate precedes the concept. The conceptual payoff arrives in the
paragraph *after* the reader has already played.** That is prediction-before-reveal (T7),
explore-then-explain, and productive failure — implemented **thirty to a hundred and twenty
times per article**, silently, without ever asking the reader to pause, because the artifact
has no clock to pause.

Ciechanowski has, in other words, solved the exact problem Sanderson names and concedes he
cannot solve. Sanderson says the prediction is where the learning happens and that *"a lot of
people are a little bit more passive in that moment."* Ciechanowski never asks for the pause;
he removes the thing that would have to be paused. `CRAFT` — and it is the single most
transferable structural pattern in this document.

**T62 · The reader generates the counterexample** — **B** · `CRAFT`

Because the parameters are open, the reader can drive the model to its breaking point
themselves. Nobody has to *tell* them the small-angle approximation fails; they slide the
angle up and watch it fail. **The refutation is self-administered**, which removes the
confession cost (§2.4) entirely.

This is the single most important structural property in the document. A refutation the
learner performs on their own model, against an unarguable simulation, with no other person
present, is *strictly better* than Muller's `d = 0.79` dialogue on every dimension except that
nobody has measured it. `CRAFT` — and §3.2 and §3.3 are built on it.

**T63 · No clock** — **C-dissolving-into-B** · `OBSERVED`

There is no runtime. The reader's dwell time on any figure is unbounded and unmeasured. A
paragraph that takes one reader four seconds takes another four minutes and neither is
penalised. Every pacing technique in the video half of this inventory (T35, T43, T64, the
10-minute chunk, the retention cold open) exists to solve a problem that **does not exist
here**.

**T64 · Absurd authoring cost, and what it implies** — **OBSERVED**

In his own words, from the Patreon campaign page (`https://www.patreon.com/ciechanowski`,
868 patrons at retrieval):

> *"I write interactive articles about physics, math, and engineering. **It's a weekend hobby
> of mine, so I only end up making a few articles per year.** I want to keep the content of my
> website accessible to everyone without annoying ads or paywalls."*

`OBSERVED`. (The widely-quoted "months per article" figure is **not** a claim he has made
publicly — his process commentary lives in patron-gated *"On '\<Title>'"* posts. Do not
attribute a number to him.)

**Twenty-two articles in eleven years, from a weekend hobby, and they are the best interactive
explanations that exist.** That is the argument for generation in one sentence — not because
generation would match the quality, but because the quality demonstrably exists at ~2–3
artifacts per year against a demand of every concept in every syllabus. The gap is five orders
of magnitude and hiring will not close it.

**Distill's hiatus is the same finding arriving from the research side, and it is more
precise.** From the hiatus notice (2021-07-02, `10.23915/distill.00031`), verbatim:

> *"we don't believe that having a venue is the primary bottleneck… Instead, we believe **the
> primary bottleneck is the amount of effort it takes to produce these articles and the
> unusual combination of scientific and design expertise required**."*
> *"For some of our early articles, **we provided more than 50 hours of help** with designing
> diagrams, improving writing style, and shaping scientific communication."*
> *"Distill is volunteer run and these frictions have caused our team to **struggle with
> burnout**."*

**Two independent efforts, one solo and one institutional, both stopped for the same reason:
the labour.** `OBSERVED`. And the tooling picture confirms it — see T72a.

---

### 1.12 — Explorable explanations: Bret Victor, Nick Case, Distill

**T65 · Bret Victor · The reactive document** — **B** · `OBSERVED`

From *Explorable Explanations* (worrydream.com, 2011): prose in which **the numbers are
live**. The reader changes a value in a sentence and every dependent value in the surrounding
text updates. The reader is not reading a claim; they are reading a *model* rendered as
English.

He defines all three of his coined techniques in one place, and they should be kept verbatim
because everyone paraphrases them into mush:

> **"A *reactive document* allows the reader to play with the author's assumptions and
> analyses, and see the consquences."** [sic]
> **"An *explorable example* makes the abstract concrete, and allows the reader to develop an
> intuition for how a system works."**
> **"*Contextual information* allows the reader to learn related material just-in-time, and
> cross-check the author's claims."**

And the design constraint that most implementations violate:

> *"There are no UI elements screaming for attention. The reader is not transported off to a
> separate 'interactive' context. **Most interactive widgets dump the user in a sandbox and
> say 'figure it out for yourself'. Those are not explanations.** … an essential aspect of the
> 'explorable explanation' concept is that **the author holds up their end of the
> conversation**."*

*Cognitive job:* collapses the gap between a stated result and the parameter regime that
produced it. The reactive document is *"like a spreadsheet without the spreadsheet"*, readable
at four depths from one artifact: *"The hurried reader can skim it. The casual reader can read
it as-is. The curious reader can adjust the author's scenarios. The engaged reader can explore
scenarios of their own devising."* **That is a four-level ladder served by a single artifact
with no branching and no learner model — the cheapest possible answer to T86's modal-learner
problem, and it predates every system in this repo by fifteen years.**

**T65a · Victor's own 2024 retraction of what the term came to mean** — `OBSERVED`

The postscript he added to the 2011 essay in **February 2024** is the most important paragraph
in the explorable-explanations literature and is almost never cited:

> *"Since this was written, the term 'explorable explanation' has gained some currency… **It
> has now been applied so broadly that it seems to mean 'any article with interactive
> pictures'.** … almost all of these articles are pedagogical, and that's not really what I
> was going for here. **What I meant by 'explorable explanation' was more like, 'a written
> argument whose assertions are backed by explorable computational models, whose facts,
> assumptions, and calculations are all visible and editable'.** The author's role here is not
> just to teach, but to convince. The reader's role is not to believe, but to critically
> evaluate, rebut, and come to a broad understanding. **The reader rebuts by modifying the
> models.**"*

**Take this as a design requirement rather than as a quibble about terminology.** An
explanation whose parameters are open is not merely easier to follow; it is *falsifiable by
its reader*. The interactivity is not a comprehension aid — it is the **rebuttal channel**.
That reframing changes what §3 should build: not "explanations the learner can play with," but
**explanations the learner can attack, with the attack surface being the model's own
assumptions.** He also notes he has *"given up on the computer screen as a medium for
model-grounded discussion"* and points at Dynamicland instead, which is a disagreement worth
recording and not resolving here.

**T66 · Bret Victor · Up and down the ladder of abstraction** — **B** · `OBSERVED`

The reader is given an explicit control that moves between **one concrete instance** and
**the parameterised family of all instances**, with a visible representation at every rung —
one trajectory, then all trajectories, then the space of trajectories coloured by outcome.

*Cognitive job:* makes abstraction a **navigable direction** rather than a cliff. This is the
missing operator in almost all instruction: learners are asked to abstract without ever being
shown the movement. Directly relevant to this repo's `F10` laddering: **Victor's ladder is
vertical over abstraction; ELI10→ELI25 is vertical over prerequisite load. They are different
axes and a system needs both.** `CRAFT` for the pedagogical claim.

**T67 · Bret Victor · Contextual information on demand** — **B** · `OBSERVED`

Every term carries its definition, its provenance, and its concrete instantiation **one hover
away, in place**, without navigation. The learner never leaves the sentence to resolve a
reference.

**T68 · Nick Case · The mechanic carries the argument** — **B** · `CRAFT`

*Parable of the Polygons* (with Vi Hart): the reader **personally enacts** mild individual bias
by dragging shapes, and personally produces severe collective segregation. Schelling's result
is not stated and believed; it is **committed by the reader and then measured**.

*Cognitive job:* an argument the learner cannot dismiss as the author's, because the learner
produced the data. There is no rhetorical technique in the linear corpus that does this.
`CRAFT`.

**T69 · Nick Case · Lose first, then learn why** — **B** · `CRAFT`

*The Evolution of Trust*: the reader plays iterated prisoner's dilemma, adopts a strategy, and
**gets beaten by a strategy they had not considered**. The explanation of why arrives *after*
the defeat and lands on a prepared surface.

*Cognitive job:* productive failure (`g = 0.36`/`0.58`, §01) with the failure *actually
experienced* rather than watched. This is what T4 and T25 are proxies for.

**T69a · Nick Case · Invisible scaffolding, and the public retraction that produced it** —
**B** · `OBSERVED`

The most valuable single document by any practitioner in this inventory is Case's *"Curse of
the Chocolate-Covered Broccoli (or: Emotion in Learning)"* (2019-12-05,
`https://blog.ncase.me/curse-of-the-chocolate-covered-broccoli-or-emotion-in-learning/`).
It opens:

> *"So earlier this year, I learnt my whole career was based on a lie. As one does. I make
> games to help folks learn by doing. … Of course beginners learn better from pure
> exploration, rather than being railroaded through step-by-step instructions. Anyway, this
> idea's been experimentally tested, and it's **replicatably false**."*

He then names what he redesigned around: **the expertise reversal effect** (*"'active'
learning-by-exploring is ineffective for beginner students, but very effective for advanced
students"*), **cognitive load theory**, **the zone of proximal development**,
**Yerkes–Dodson**, and **Mayer's multimedia principles**. And the technique that came out of
it, verbatim:

> *"it turns out the designers add tons of hand-holding guidance – **they just keep it
> invisible so you can feel smart**."*

**That is the technique: guidance whose presence the learner cannot detect.** The learner
experiences discovery; the designer has constrained the space so that discovery is nearly
forced. It is the resolution of the "learner control measures worse than system control"
finding (§2.9): **you do not choose between guidance and agency — you deliver guidance in a
form indistinguishable from agency.**

`OBSERVED` for the practice, `MEASURED-META` for every mechanism he cites, and note the rarity:
**a leading practitioner publicly retracting his field's founding premise on the basis of
replication evidence.** Nobody in the video half of this inventory has done that.

Case also runs his own randomised experiments on his own pedagogy —
`https://ncase.me/experiment-stats/results/`, *"Does guessing first improve memory? — a
randomized-controlled web experiment"* — which is the T7 question, asked by the person best
placed to answer it. `OBSERVED`.

**T69b · Nick Case · Manipulate the rules, not the sliders** — **B** · `CRAFT`

From his *Explorables Jam* write-up (2018-08-28, `https://blog.ncase.me/the-explorables-jam/`),
as a self-criticism:

> *"you can change the simulation's rules by **directly manipulating the simulation itself**!
> (In contrast, **almost all my sims have you change rules with sliders & buttons**) I wanna
> see more sims designed this way!"*

A slider varies a parameter inside a fixed model. **Direct manipulation of the rules lets the
learner change the model.** The distinction is the difference between exploring a family of
answers and questioning the question, and it is the more valuable of the two and the rarer.
Victor's 2024 postscript (T65a) is asking for the same thing from the other direction.

**T69c · Nick Case · Expandable explanations (Nutshell)** — **B/C** · `OBSERVED`

`ncase.me/nutshell` (620 ★) — inline, in-place expansion of any phrase into its explanation,
recursively, without navigation. **This is the mechanical replacement for CGP Grey's footnote
video (T49) and for Kurzgesagt's external sources document (T39), and it already exists as a
shipped, public-domain library.** Victor's *contextual information* (T67), built.

**T70 · Nick Case · Hand over authorship at the end** — **B** · `CRAFT`

*Loopy* ends by letting you build and share your own causal-loop model; *Explorable
Explanations* (explorabl.es) is a curated commons; the works are CC0 and remixable. The last
move of the explanation is **"now make one."**

*Cognitive job:* learning-by-teaching / generation — one of the largest effects in the corpus,
and the technique the entire video field structurally cannot use.

The numbers, with the repo's standing correction attached (Kobayashi 2019/2024, §C3):
preparing to teach **g = 0.35**; preparing **and delivering g = 0.56**; and the decisive
moderator — **with teaching expectancy g = 0.48 [0.34, 0.63]; without it g = −0.02 [−0.14,
0.11], k = 39.** `MEASURED-META`. **The effect is entirely carried by the learner believing
they will have to teach it.** Peer tutoring's gain to the *tutor* is **0.43** (Leung 2018).

> ⚠️ Standing correction C-7: *g = 0.56 is human learning-by-teaching, not teachable agents.*
> **The teachable-agent version is untested** — arXiv returns 18 results total for the term and
> Europe PMC returns **zero** for `"teachable agent" AND "randomized"`. Do not launder the
> human number onto an AI agent that plays dumb.

**T71 · Distill · "Research debt" as the named target** — **OBSERVED**

*Research Debt* (Olah & Carter, `10.23915/distill.00005`) names the thing the whole field of
explanation is paying down, by analogy to technical debt, and decomposes it into five
components that are individually actionable: **poor exposition**; **bad definitions,
abstractions, and notation** — *"Formalisms like abstractions and notation are **the user
interface of research**"*; **undigested ideas**; **unavailable tools**; and **noise** —
*"When hundreds of papers are published each day, with no easy way to filter or summarize
them, the energy needed to keep up with a field is too high… we think noise is the main way
experts experience research debt."*

The framing sentence, which is the best one-line statement of this project's premise written
by anyone: *"Achieving a research-level understanding of most topics is like climbing a
mountain. … **The climb isn't progress: the climb is a mountain of debt.**"* And: *"The
insidious thing about research debt is that **it's normal**."*

**T72 · Distill · The diagram as the paper's argument, publicly peer-reviewed** — **B** ·
`OBSERVED`

Interactive figures were peer-reviewed artifacts, not supplements — and the **review itself was
public, conducted as GitHub issues on a per-article repository** (e.g.
`github.com/distillpub/post--activation-atlas`, `label:peer-review`). The claim, its
manipulable demonstration, and the argument about whether it was right were **one versioned
object**. Nothing in education publishing works this way. Their masthead named the goal
directly: *"Machine Learning Research Should Be Clear, Dynamic and Vivid"*, with **$10,000
prizes** attached — an explicit attempt to price a form of labour the academy does not pay for.
ISSN 2476-0757; operated 2016–2021; 32 articles.

**T72a · The tooling asymmetry, which is the most damning number in this document** —
`OBSERVED`

`gh api`, 2026-07-29:

| Repo | Purpose | ★ | Last push |
|---|---|---|---|
| `3b1b/manim` | **linear video** animation engine | **88,991** | 2026-07-28 |
| `ManimCommunity/manim` | linear video | **39,784** | 2026-07-29 |
| `observablehq/plot` | data viz | 5,331 | 2026-07-13 |
| `observablehq/framework` | data apps | 3,559 | 2026-05-15 |
| **`idyll-lang/idyll`** | **"Create explorable explanations and interactive essays"** | **2,036** | **2023-02-04 — stale** |
| `distillpub/template` | interactive article framework | 990 | — |
| `ncase/nutshell` | expandable explanations | 620 | — |
| `mathigon/textbooks` | interactive textbooks | 392 | 2025-02-25 |

**The single tool built explicitly for explorable explanations has been dead since February
2023, and the tool for making linear videos has forty-four times its stars and shipped
yesterday.** `explorabl.es` curates 180 explorables, of which **10 are tools**, several of them
now unmaintained (Tangle, Apparatus, dat.gui, g9, Kinetic Graphs, LOOPY, Joy.js, Emoji
Simulator, Idyll, Observable).

Read that as an opportunity rather than as a verdict. The *demand* for explanation is
enormous and demonstrably met by video. The *superior substrate* has been identified, prototyped
by the best practitioners in the field, and abandoned at the tooling layer **because authoring
in it costs 30–120 hand-built figures per article.** That authoring cost is precisely what
generation attacks. **This is the clearest statement of the opportunity in the entire
document.**

---

### 1.13 — Mass-scale exam preparation: Khan, India, China

This is the largest body of explanation practice on Earth and it is almost entirely unstudied
in English-language sources. The constraints are different — a fixed, high-stakes, timed exam;
an audience of millions who did not choose the subject; teachers who are regional celebrities
— and the craft that grew under those constraints is different craft, not worse craft.

**T73 · Khan Academy · Remove the observer** — **A** · `OBSERVED`

No face. No stage. A digital blackboard and a voice slightly off-mic. Khan's own stated
rationale, verbatim, is not about production cost:

> *"That way, it doesn't seem like I'm up on a stage lecturing down at you. It's intimate,
> like we're both sitting at a table and we're working through something together."*
> *"The worst time to learn something is when someone is standing over your shoulder going,
> 'Do you get it?'"* (*WIRED*, 2011-07-15)
>
> *"Probably the least-appreciated aspect of this is the notion that the very first time that
> you're trying to get your brain around a new concept, the very last thing you need is
> another human being saying, 'Do you understand this?'"* (TED 2011)

**This is the most consequential warning in the document for anyone building a responsive
tutor**, and it comes from the person with the most learner-hours in history. The absence of
an observer is not a limitation Khan worked around — it is a **feature he chose**, and it is in
direct tension with the thesis of Part 3. §2.8 takes this seriously rather than dismissing it.
Classified **A** because it is compensation for an absence, but it is the one A whose
replacement must be built with great care.

**T74 · Khan Academy · Real-time handwriting; production pace equals thinking pace** —
**B** · `OBSERVED`

The writing happens at writing speed. The learner's processing has the same clock as the
teacher's production. Same mechanism as Numberphile's brown paper (T35) and Alakh Pandey's
board work (T77) — **three independent inventions of pace-limiting by material constraint.**
That convergence is the strongest `CRAFT`-level evidence in the document.

> ⚠️ Two widely-repeated Khan claims are wrong and must not propagate (`N4` §5.2): the
> "never edits, single take" line is **Clive Thompson's paraphrase in *WIRED*, not Khan's
> words** (`UNVERIFIED`); and the ten-minute length was **not** chosen for attention span —
> Khan Academy's own 2010 FAQ says it was chosen for *"viewing on the computer"* and for
> **standards-mapping granularity** (`HISTORICAL`). A format constraint has been rationalised
> as a cognitive finding for fifteen years.

**T75 · Khan Academy · Granular decomposition to a mappable unit** — **C** · `HISTORICAL`

*"Because of the granular nature of the 10 minute videos, the content can be mapped to almost
any state's or nation's standards."* The atomisation exists to satisfy **an institutional
indexing requirement**, not a cognitive one. In a system that can compose an explanation on
demand at any granularity, the fixed unit dissolves — although the *mapping* requirement does
not, and any real deployment still has to satisfy it.

**T76 · Physics Wallah (Alakh Pandey) · The one-shot** — **C, with a B residue** · `OBSERVED`

An entire chapter — sometimes an entire subject — taught in a single unbroken multi-hour
video. This is the format that took a teacher from a Kanpur classroom to a company valued in
the billions, and it is the exact opposite of every Western guideline about segmenting.

Mostly **C**: the bundling is a distribution decision — one upload, one URL, one thing to
share in a WhatsApp group, one artifact a student can commit an evening to. But there is a
**B residue** that the segmenting literature misses: a chapter taught continuously preserves
**cross-topic dependency structure inside a single working context**. Segmented delivery
forces the learner to reload the context at every boundary, and the reload cost is real and
unmeasured.

The literature points the other way and the disagreement is genuine, so here is the other
side in full: **segmenting g = 0.34 [0.30, 0.38], k = 123** (Rey et al. 2019) — but
**system-segmented g = 0.41 beats learner-segmented g = 0.20**, and segmenting carries a
**time-on-task cost of g = 0.92 [0.82, 1.02]**. `MEASURED-META` (§B1).

> **Read that middle row again, because it is the sharpest evidence against this whole
> document's thesis.** When the *system* chooses the segment boundaries the effect roughly
> doubles relative to when the *learner* does. Handing control to the learner measured worse.
> §2.9 takes this seriously; the short version is that **"responsive" and "learner-controlled"
> are different things, and the evidence favours the first and not the second.**

**T77 · Physics Wallah · Derivation at board speed, uncut, with the algebra shown** —
**B** · `OBSERVED`

The full derivation, every line, in real time, on a physical or digital board. Nothing is
"left as an exercise" and nothing is pre-rendered. See T74.

**T78 · Physics Wallah · Direct affective address as a persistence mechanism** — **A** ·
`CRAFT`

*"Bacho"* — "children." The register is not neutral-instructional; it is a specific adult
speaking to specific young people about their futures, with anger at their circumstances and
open belief in their capacity. Mid-lecture the content stops and a two-minute address about
effort, family, and the exam takes its place.

**This is scheduled motivational intervention, delivered blind.** He cannot see who is
discouraged, so he addresses everyone, periodically, at a rate tuned to the modal aspirant.
Classified **A** — and it is a large A, because in a market where the alternative was a
coaching centre nobody could afford, the parasocial bond is a substantial part of what the
product *is*.

*Cognitive job:* persistence and belonging (§F6). Note the direction of the evidence on
pedagogical-agent persona effects, which is weak (§B1/§F6) — but those studies measure a
cartoon on a slide, not a person whose life story the learner knows. The comparison is not
close and the literature does not cover this case.

**T79 · Indian exam prep · The previous-year question as the unit of explanation** —
**B** · `CRAFT`

A concept is not finished when it has been explained; it is finished when it has been **cashed
out against an actual item from an actual past exam**. The transfer target is stated,
concrete, and public. Every concept arrives pre-attached to the form in which it will be
tested.

*Cognitive job:* this is **transfer-appropriate processing made explicit**, and it is the
technique the Western explainer corpus most conspicuously lacks. `N4` §5.6 records that
Kozyrkov's five-hour series contains **no quiz, exercise, or assessment anywhere**. The Indian
format has the opposite failure mode — item-drilling that never reaches the concept — and the
right design takes one from each. `CRAFT`.

**T80 · Indian exam prep · The shortcut economy** — **B/negative** · `CRAFT`

"Tricks" — procedural compressions that produce the right answer faster than the principled
method (options-elimination heuristics, dimensional shortcuts, memorised special cases). Real
craft, honestly optimised for a timed multiple-choice exam, and **actively harmful to
conceptual understanding**, which is a trade the students are making knowingly.

Kept in the inventory because a system serving these learners must decide explicitly whether
to teach the trick, and pretending the trick does not work is not an option. `CRAFT`.

**T81 · Live batch teaching at scale with a doubt channel** — **A, partially resolved** ·
`OBSERVED`

Unacademy, Vedantu, PW Live, and the Byju's-era live formats: a teacher streams to tens or
hundreds of thousands of concurrent learners, with a chat and a "doubt" queue. **This is the
field's own attempt to build the return channel**, and it is instructive precisely because it
half-works: the channel exists, but it is one-to-N with N in the tens of thousands, so what
comes back is a *sample of the distribution*, not this learner's state. The teacher answers
the modal doubt. Everyone else watches someone else's question get answered.

**T82 · The dual-teacher classroom (双师课堂) — the human proof-of-concept** — **B** ·
`OBSERVED`

The most important entry in this section. In the Chinese model (Xueersi/TAL, Yuanfudao,
Zuoyebang, and the wider sector before the July 2021 "double reduction" policy largely
dismantled private tutoring), **a star teacher delivers the explanation by live stream to many
classrooms, and in each room a local tutor watches the actual students** — checks work, flags
confusion, re-explains locally, manages attention, and reports back.

That is exactly the architecture this repo is arguing for, implemented with humans, at
national scale, for years:

| Layer | Chinese dual-teacher | This project |
|---|---|---|
| Authored explanation | star teacher, streamed | curated/generated artifact |
| Per-learner observation | local tutor, one room | model, one learner |
| Repair | local re-explanation | re-render / branch |
| Feedback to the author | tutor reports | telemetry to the atlas |

**The design insight it delivers for free:** the two layers are *separable*, and the expensive
one (world-class explanation) can be amortised across everyone while the cheap-per-unit one
(watching) is what has to be local. Nobody in the English-language AI-tutoring discussion
cites this, and it is the single strongest existing argument that the architecture works.
`OBSERVED` for the practice; the outcome literature is thin and mostly Chinese-language.

**T83 · Shadow education generally · Extreme dosage as the actual mechanism** — `OBSERVED`

The uncomfortable finding lurking behind every one of these systems: a substantial part of
their measured effect is plausibly **time-on-task at a dosage no school can match** — six-hour
days, seven-day weeks, for two years. Any comparison of a technique against "the Indian
coaching result" must control for dosage or it is measuring hours, not craft. Flagged here so
that no technique in this section gets credit that belongs to the clock.

---

### 1.14 — Techniques nobody attributes to one person

**T84 · The anticipated objection ("you might be thinking…")** — **A** · `CRAFT`

Universal across the corpus. The explainer voices the learner's likely objection and answers
it. This is **the single most common compensation technique in existence** and it is entirely
guesswork: the explainer guesses the modal objection at the modal point, and every learner
whose objection differs gets an answer to a question they did not have — which is *worse than
silence*, because it introduces a doubt they were not carrying.

**T85 · The deliberate false start** — **A** · `CRAFT`

*"So you might try to solve it like this… and that doesn't work, and here's why."* Related to
T4 but distinct: T4 is a genuine simplification-then-refinement; this is a **staged error**,
performed so the learner sees the error corrected without having made it.

**T86 · Modal-learner targeting** — **A** · `INFERENCE`

**The invisible master-technique of the entire field, and the one nobody names.** Every choice
in every artifact — vocabulary, assumed prerequisites, pace, how much algebra to show, whether
to define "eigenvalue" — is a **point estimate of a distribution the explainer cannot see**.
The artifact is pitched at an imagined median learner and is therefore, by construction, too
fast for the bottom half and too slow for the top half, on every axis, simultaneously.

Everything else in bucket A is downstream of this. The anticipated objection, the recap, the
caveat aside, the footnote video, the "if you already know X, skip to 4:20" — all are patches
on a single unavoidable lossy compression: **one artifact, one pitch, a distribution of
learners.**

This is what a responsive system actually removes. Not the animation. Not the voice. **The
point estimate.**

**T87 · The recap after the break; the "as we saw earlier"** — **C** · `CRAFT`

Re-statement inserted at fixed intervals because the explainer cannot know whether this
learner still has the earlier material active. A system that can ask — or that can infer from
a two-second probe — restates only for the learners who need it.

**T88 · Chapter timestamps as the navigation affordance** — **C** · `OBSERVED`

The state of the art in explanation navigation is a list of labelled time offsets in a
description box. `N4` §5.3 records that the largest channel in the class does not even provide
those. Replaced entirely by query.

**T89 · The retention-engineered cold open** — **C** · `OBSERVED`

The first fifteen seconds are designed against an algorithmic retention curve, not against
comprehension. Per T14, that curve is measuring *dull* and *too long* — the two axes on which
the `d = 0.79` format lost. **This technique is optimising against learning and there is a
measured trial saying so.** It dissolves the moment the artifact is not competing for a click.

**T90 · Rewind as the sole repair mechanism** — **C** · `OBSERVED`

When comprehension fails, the only available action is to replay the same words. `N4` §3.7
records that when rewinding was finally tested against an outcome, **the sign was backwards**.
The repair affordance the medium offers is not a repair.

**T91 · The comment section as the return channel** — **A/C** · `OBSERVED`

The listener does exist — asynchronously, self-selected, and with a latency of days to years,
aggregated across millions, and reaching the author rather than the learner. Corrections
surface in pinned comments and in follow-up videos (T16, T33). It is a real feedback loop
operating at approximately 10⁻⁷ of the bandwidth of a person in a room.

---

---
title: "The Ladder of Explanation — ELI10 to ELI25, and the rule that makes a simplification legal"
section: laddering
status: draft
date: 2026-07-28
source_report: research/raw/F10-explanation-laddering.md
---

# The Ladder of Explanation

"Electrons orbit the nucleus like planets orbit the sun."

That sentence is the most successful explanation in the history of chemistry
teaching, and it is a false one. Cunha, Dias & Streit (2023, *Journal of Chemical
Education*) put structured questionnaires to Brazilian university chemistry students
across three majors at the start and the end of a semester. The number of students
able to hold a quantum mental model of the atom went up. And **the number holding
the Bohr hybrid — classical orbits with quantum ideas grafted on — stayed the
same.**

An entire semester of instruction aimed at that misconception did not shrink the
population holding it. The simplification did not fade. It fused.

This section is about the question the project asked for directly: render one
concept at ELI10, ELI15, ELI20 and ELI25, so a learner can enter at their own level
and climb. The literature says the idea is right, the number of rungs is wrong, the
entry mechanism everybody ships is backwards, and there is one constraint that
separates a productive simplification from a planted misconception.

---

## 1. Three rungs, not five

The most useful single result for this design is a mostly-null replication.

Trory, Howland, Good & du Boulay (2026, ACM *Transactions on Computing Education*)
ran three between-groups pre/post experiments with **166 pupils aged 9–10** on
computer network structure and routing. Four hypotheses:

| Hypothesis | Result |
|---|---|
| H1: fading beats abstract, concrete and concreteness-introduction | **Not supported.** ANCOVA F(3,54) = 2.413, **p = 0.077**, ηp² = 0.118 |
| H2: physical concrete beats virtual concrete | **Not supported.** Welch t(41.7) = 1.015, p = 0.316 |
| **H3: three-step beats two-step** | **Supported.** F(2,56) = 3.670, **p = 0.032**, ηp² = 0.116; Mdiff = 0.99 |
| **H4: five-step beats three-step** | **Not supported.** Mdiff = 0.16 [−0.78, 1.09], **p = 0.738** |

Three of four hypotheses null. But H3 and H4 together are a quantitative constraint
on the brief: **three rungs beat two, and five rungs bought nothing over three.**
The return diminishes, and it diminishes early.

That does not kill ELI10/15/20/25. It changes what the four levels are *for*.

> **The ladder is a library the learner enters, not a staircase they climb.** Five
> rungs exist so that different learners start at different points. Any given
> learner traverses two or three of them.

The distinction is the whole design. A system that walks every learner from ELI10
to ELI25 is running the arm that measured p = 0.738. A system that measures where
someone is, drops them one rung below it, and moves them up two is running the arm
that measured p = 0.032.

---

## 2. Entry is measured, never preferred

Here is the mechanism everybody gets wrong, and it has its own clean evidence.

Buljan et al. (2018, *Journal of Clinical Epidemiology*) ran **three parallel
randomised trials** — students n = 171, consumers n = 99, doctors n = 64 —
comparing an infographic, a plain-language summary and a scientific abstract of the
same Cochrane review.

> "We found **no difference in knowledge** between the infographic and the
> text-based PLS in any of the trials or in the whole participant sample. **All
> three participant groups preferred the infographic**" — reading experience
> **d = 0.48**, user-friendliness **d = 0.46**.

**Preference moved by about half a standard deviation while knowledge moved by
zero.** This is the same anti-signal that §22 establishes as the governing rule for
personalisation; what the laddering literature adds is the direction of the drift.

Scharrer, Rupieper, Stadtler & Bromme (2017) found that after reading popularised
articles, laypeople **agreed more** with the knowledge claims and were **more
confident** in their own judgements than after reading the expert-addressed
versions — the *easiness effect of science popularisation*. Salzmann, Walther &
Kaspar (2025, N = 179) tested the obvious fix: a debiasing video before the plain-
language summary. **The easiness effect persisted anyway.** Warning people does not
remove it.

Put those together and you get a structural failure, not a preference:

> **A learner who has just read an ELI10 is more confident, and therefore less
> likely to ask for the ELI15. Preference-driven laddering has a built-in downward
> ratchet.**

Expert intuition is inadmissible for the same reason from the other side. Hansen &
Richland (2020, *CBE—Life Sciences Education*) found that people's beliefs about
how to sequence representations *for others* were systematically different from
their beliefs about how they themselves learn — and the students' results favoured
simultaneous presentation **only when paired with self-explanation prompts**,
matching neither belief cleanly.

So the entry rung comes from a probe, not a dropdown. The validated instrument is
Kalyuga & Sweller's rapid dynamic assessment, which §22 works through in detail. Two
details belong here rather than there. **The type of prior-knowledge assessment is
itself a significant moderator** of the expertise-reversal effect (Tetzlaff et al.
2025) — the probe is the largest tunable parameter in the system, not an incidental.
And the selection is per prerequisite: compute the mastery vector over the concept's
transitive prerequisite closure and **enter at the weakest link**, laddering that
prerequisite separately rather than dragging the whole explanation down.

---

## 3. The fidelity rule

Everything above concerns *which* rung. This concerns whether a rung is allowed to
exist.

> **Monotone refinement.** A rung at level *n* is legal if and only if every
> proposition it asserts is entailed by the level-*n+1* account under an explicitly
> stated domain restriction. Climbing may add detail and may narrow scope. Climbing
> may never require negating something already asserted.

The ladder is a refinement chain, not five independent texts. Level *n* is level
*n+1* minus declared drops. One engineering consequence follows immediately and is
not negotiable: **ladders must be generated top-down.** You cannot check a
non-falsification constraint against an account you have not written yet. Writing
the ELI10 first and "adding detail" is structurally incapable of passing the test.

What a rung **may** drop: numeric precision; higher-order corrections; formal
machinery — derivation, notation, proof; mechanism depth, by black-boxing a
subcomponent *provided the box is named as a box*; edge cases outside a declared
scope; historical provenance; one of several equivalent formulations, provided it is
not asserted as *the* formulation.

What a rung may **never** falsify:

| Never | Why it is unrepairable |
|---|---|
| **Ontological category** — thing vs. process vs. *emergent* process | Chi (2005): misconceptions **across** ontological kinds are robust; within-kind ones are not |
| **Sign or direction of a causal relation** | Fixing it requires literal negation |
| **Deterministic vs. stochastic vs. emergent character** | The most common ontological error in practice |
| **Quantifier strength** — "all" where only "some" holds | Cannot be narrowed later without retraction |
| **Conservation, invariance, impossibility claims** | These *are* the structure |
| **Uniqueness of a mechanism** — one of several presented as *the* one | Reductive collapse (Spiro et al. 1989) |
| **Existence of a boundary** — implying an unrestricted model | Undeclared drops are indistinguishable from planted misconceptions at retrieval |

Now re-read the opening. "Electrons orbit the nucleus like planets orbit the sun"
places a quantum stationary state in the ontological category *object following a
trajectory*. It is a category error, and Chi's account predicts exactly what the
*Journal of Chemical Education* measured: instruction produces a **synthetic
hybrid** rather than a replacement, and the hybrid is stable.

The legal ELI10 for the same subject is a sentence away: *"An electron in an atom
can only have certain specific amounts of energy — not anything in between. Light
is given off when it drops from a higher one to a lower one."* Every proposition
there survives verbatim into the full quantum account. It drops the wavefunction,
the orbital, the selection rules and the entire mechanism. **It falsifies nothing.**

Two more tests complete the rule. Every drop leaves a **named, retrievable marker** —
not "it's more complicated than that" but a token the learner can carry upward:
*"this assumes no friction; the friction case is rung 3."* And every analogy ships a
declared **alignment set** (which relations map) and **limit set** (which do not);
for concepts with high reductive-bias risk, Spiro's prescription is two mutually
*dis*analogous sources rather than one good one.

A vocabulary corollary follows. Replacing "eigenvalue" with "stretchiness number"
creates a term the learner must later unlearn and cannot look up. **Simplify the
explanation; keep the name.**

---

## 4. Chi's test replaces threshold concepts

The natural framework for "which ideas cannot be simplified" is threshold concepts
— transformative, irreversible, integrative, bounded, troublesome. It is heavily
cited and it does not survive as a classifier.

Salwén (2019) argues the framework is "beset with severe definitional and empirical
problems," that the definitions "fail," and that even if particular threshold
concepts could be identified their "scientific importance would be limited if not
nil." Stopford (2020) is more precise about the operational gap: the framework "is
without a methodology for identifying threshold concepts."

And the one study that tried to measure a crossing found the measurement itself
unreliable. Walck-Shannon, Batzli, Pultorak & Boehmer (2019, *CBE—Life Sciences
Education*) interviewed 29 students about biological variation in a cross-sectional
design — Pre, Current, Post, and a postbaccalaureate outgroup — coding on four
dimensions. **Liminality appeared in Pre, Post and Outgroup explanations alike,
"with discomfort and uncertainty regardless of accuracy."** Even the advanced group
felt unsure. Feeling uncertain does not identify not having crossed.

So a generator that asks "is this a threshold concept?" and branches on the answer
is branching on an unreliable label. **Chi's ontology test is the replacement**:
does this rung place the concept in the correct ontological category? That question
is domain-general, answerable, and grounded in conceptual-change research with
measurement behind it.

For concepts where no simplification passes the ontology test, the move is not a
false model but a **pre-concept rung**: state the phenomenology, decline to assert
a mechanism. *"When you cool helium enough, it flows up the walls of its container.
Nothing in everyday physics explains that."* That is honest, it has a real
assessment ceiling — recognise and predict — and it plants nothing. It is Clement's
anchoring-intuition strategy, whose measured version (21 students, matched groups)
produced significant gains on target **and transfer** problems.

---

## 5. What the evidence does not support

This section's foundations have more holes than its confident tone would suggest,
and they need naming.

**Concreteness fading has no pooled effect size.** Fyfe, McNeil, Son & Goldstone
(2014) is the empirical backbone of this whole area and it is a **systematic
review, not a meta-analysis**. No pooled estimate for concreteness fading exists
anywhere in the retrievable record. Anyone quoting "the effect size of concreteness
fading" is quoting something that does not exist.

**And it does not beat its main alternative.** Lichtenberger, Kokkonen & Schalk
(2024, *JRST*), N = 187 high-school students, Faraday's law: no significant
difference between concreteness fading and simultaneous presentation, and an
**equivalence test with pre-specified bounds d = ±0.5 showed the two approaches
performed equally.** The authors' conclusion is the one that matters here:
facilitating understanding "may involve more than determining the optimal order."
Ordering is not the mechanism.

**Variety of surface actively harms.** Bennett, Inglis & Gilmore (2019, *JEP*),
three experiments: children who learned novel numerical symbols paired with a
single abstract representation outperformed those given multiple concrete ones —
and the harm was attributable to **the multiplicity itself**, not to concreteness.
Day, Motz & Goldstone (2015) found the same shape in two classroom experiments:
**greater contextualisation, poorer transfer**, in undergraduates and
middle-schoolers alike. An ELI10 rendered as "here are four fun everyday analogies"
reproduces both results at once.

**A well-motivated analogy manipulation produced nothing.** Sota (2012) randomly
assigned participants to refutational contrasting analogies, non-refutational
contrasting analogies, or none, for natural selection: "**no differences among
groups** on either understanding of or reasoning about natural selection" — though
the groups engaged differently with the analogy materials. Different experience,
identical learning.

**The Feynman technique has essentially no research base.** An ERIC search across
the entire corpus returns **two records**, both 2025–2026, both small, both from
the same ESL niche, and both confounding the technique with analogical reasoning so
that it cannot be isolated. The *mechanism* — generating an explanation, finding the
gap, iterating — is self-explanation, which carries **g ≈ 0.55 across 69 effect
sizes** (Bisra et al. 2018) and is the subject of §05. The branded four-step
protocol carries nothing. Cite the mechanism; do not cite the brand.

**One number in our own brief was unverifiable.** The expertise-reversal interaction
was given to this project as **d = 0.971**. It could not be verified in any
retrievable source; the publisher abstract supports only the two marginals
(novices +0.505, experts −0.428), which imply an interaction of **≈ 0.93** by simple
difference. We report the marginals and the ≈0.93, and we do not assert 0.971.

**And the composite has never been tested.** No study in the retrieved literature
tests laddering as such — the same concept authored at N levels under a fidelity
constraint, entry chosen by measurement. Every component is evidenced. The assembly
is not. That is simultaneously the contribution and the risk, and it is the
honest label for everything in §3.

---

## 6. The objection worth answering

*If ordering is not the mechanism and fading is statistically equivalent to
simultaneous presentation, why build a ladder at all?*

Because the ladder is not making an ordering claim. The robust finding underneath
concreteness fading is not concrete-then-abstract; it is **multiple instantiation of
the same relational structure**. Goldstone & Son (2005) found that switching
representation in *either* direction beat not switching. Gentner's analogical-
encoding studies found that comparing two examples beats studying them serially.
Bennett's harm was unaligned multiplicity. The active ingredient across all of them
is **aligned comparison of two instantiations of one structure** — which is what a
refinement chain is, expressed as text.

So the design does not claim a fading benefit. It claims that a learner who has an
entailment-preserving pair of accounts at two adjacent depths can compare them, and
that comparison is the evidenced act. When transfer succeeds but load is high, the
move is not to climb — it is a **second aligned instantiation at the same rung**.

One instrumentation warning makes or breaks this. Rey & Fischer (2013) tested
expertise reversal specifically on *instructional explanations*: it replicated on
**transfer** and **not on retention**. A ladder that evaluates itself with recall
questions is instrumented to be blind to its own primary failure mode. **Probe with
a transfer item.**

And support must actually be withdrawn. Nückles et al. (2010) ran two term-long
journal-writing studies: by the end of term the **permanent-prompt group scored
substantially lower** than the faded-prompt group, because internalised strategies
turn external support into "a redundant stimulus that interfered." A system that
leaves a learner on ELI15 because they never asked to move is harming them by
week six.

---

## 7. What this section commits us to

- **Four rungs exist as a library; a learner traverses two or three.** Three-step
  beat two-step at p = 0.032; five-step did not beat three-step at p = 0.738.
- **Entry is measured, never chosen.** Preference moves d ≈ 0.48 while knowledge
  moves zero, and the easiness effect survives explicit debiasing. The dropdown may
  exist as an override; it may never be the default input.
- **Per prerequisite, take the weakest link.** No single global level per learner.
- **Generate top-down.** A refinement chain cannot be checked against an account
  that does not exist yet.
- **A rung may drop precision, formalism and mechanism depth. It may never falsify
  ontology, causal sign, quantifier strength, or uniqueness of mechanism.**
- **Every drop leaves a named marker; every analogy ships a limit set.**
- **Ask the ontology question, not the threshold question.** The threshold
  framework has no identification methodology and its own measurement study found
  liminality regardless of accuracy.
- **Probe with transfer items and force the fade.** Retention testing cannot see
  the damage; permanent prompts cause it.
- **Quote no effect size for concreteness fading**, because none exists.

The highest-value use of a ladder may not be serving one at all. If explaining
simply is itself a learning act — and at g ≈ 0.55 it is — then the strongest move
available is to ask the learner to write the ELI10 and **diff it against the
system's**. The diff localises the defect by class: a missing relation, an
over-extended analogy, or a wrong ontological category. That is `INFERENCE`, not a
measured design. It is also the cheapest experiment in this section, and the one
that would turn the ladder from an output into an instrument.

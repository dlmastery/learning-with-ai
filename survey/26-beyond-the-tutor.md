---
title: "Beyond the Tutor — the five roles nobody is building"
section: roles
status: draft
date: 2026-07-28
source_report: research/raw/F2-beyond-the-tutor.md
---

# Beyond the Tutor

Say "I'm going to play devil's advocate for a moment" and you have just made your
interlocutor harder to move.

Nemeth, Brown & Rogers (2001, *European Journal of Social Psychology*) compared
role-played devil's advocacy against authentic dissent. Authentic dissent produced
divergent thinking — more solutions, considered from more angles. The assigned
devil's advocate produced "thinking that was primarily aimed at **cognitive
bolstering of the initial viewpoint** rather than stimulating divergent thought."

Announced opposition makes people defend harder. It does not make them think wider.

That result governs the most obvious way to build an AI that argues with a learner,
and as far as this project's search could determine it appears nowhere in the
AI-education literature. It is one of six roles an AI can occupy in learning, five
of which are essentially unbuilt.

---

## 1. The design space has one point in it

"AI tutor" is the default not because the evidence favours it but because it is the
shape an instruction-tuned assistant already has: knowledgeable, helpful, agreeable,
responsive. **That shape is a training artifact, not a pedagogical finding.**

Distinguish the roles by three questions — who holds the knowledge, who holds the
goal, and who bears the cognitive load. The last one decides everything, because
transfer follows load.

| Role | AI's stance | Who bears the load | Evidence |
|---|---|---|---|
| **Tutor** | Knows more, dispenses | The AI, at the limit | Strong for constrained tutors; **strong for harm** when unconstrained |
| **Student** | Knows less, asks, errs | The learner, fully | Strong for human tutees; thin for AI tutees — §02 |
| **Peer** | Knows comparably, commits | Shared, symmetric | Strong for human peers; **theoretical only** for AI |
| **Adversary** | Knows, withholds, attacks | The learner, fully | Strong for the human analogues; almost no AI outcome data |
| **Environment** | No stance; holds consequences | The learner | Strong in principle, barely instrumented |
| **Instrument** | Extends a human's capability | The human who owns the task | Best evidence-to-deployment ratio of the six |

The tutor role is the only one that requires the AI to be knowledgeable and
agreeable. It is also the only one with documented harm at scale: **§01 and §09
carry the −17% unassisted-exam result and the guardrail correction, and this
section does not re-argue them.** What it argues is that four of the other five
roles are available now and nobody is building them.

The student role is the exception, and it already has a section: **§02** works
through the protégé effect, the knowledge-telling failure, capability leakage, and
the Betty's Brain architecture. **§05** works through the learner as explainer.
Everything below is what is left.

---

## 2. The adversary

### 2.1 Why dissent works, and why it does not need to be right

Nemeth's core asymmetry (1986/1987) is that exposure to opposing views from a
**minority** produces divergent thinking — the problem gets considered from multiple
angles, and performance improves. Exposure to opposing **majority** views produces
convergent thinking — narrowing onto the proposed view, which does not help and can
impair.

**The dissenter's value does not depend on the dissenter being right.** It depends
on the dissent being real.

That is a remarkable licence for an AI adversary, because it means the objection
does not have to be correct to be useful — and it is immediately revoked by the
2001 result above, because it also means the objection cannot be performed.

### 2.2 The dilemma, stated fully

- If the AI announces "I'll argue the other side," it is a *known* devil's advocate.
  Nemeth's condition. It produces cognitive bolstering — **the learner ends more
  confident in the view they started with.** Worse than doing nothing.
- If the AI dissents without announcing, it is authentically dissenting from the
  learner's standpoint and produces divergence — but it may assert things it does
  not hold, and it is in some sense misrepresenting its own epistemic state.

The resolution this project proposes is a design hypothesis and is labelled as one.
**Do not have the model perform opposition. Have it stop suppressing the objections
it already computes.** Not "I'll take the other side" but "I actually don't find
that convincing, and here is specifically why" — where the *why* is the model's own.

That reframes anti-sycophancy work usefully. We do not need models that pretend to
disagree. We need models that stop suppressing disagreements they have already
generated. **That is a far more tractable engineering target**, and it is directly
testable: divergent-thinking and learning outcomes under (a) announced devil's
advocate, (b) unannounced authentic objection, (c) agreeable baseline. The template
exists — Marvel & Ju (2026) ran a pre-registered **N = 1,492** study crossing a
sycophantic against a challenger model with disclosure conditions. The educational
version has not been run.

### 2.3 What the adversary costs

Two boundary results keep this honest.

**Children experience persistent questioning as pushy.** A 2024 study of elementary
students with a Socratic chatbot is titled "This Chatbot is Kind of Pushing It!" and
the title is the finding. Satisfaction and pedagogical value diverge — which is
exactly what desirable-difficulty theory predicts, and exactly what a five-star
rating loop will destroy. An adversary role cannot be tuned on satisfaction.

**And adding help to the struggle does not help.** Sinha & Kapur (2021) compared
problem-solving-before-instruction, *scaffolded* problem-solving-before-instruction,
and alternative sensemaking activities across **118 comparisons**: scaffolding
showed a small descriptive advantage and **no significant difference, g = −0.08
[−0.20, 0.04].** Bolting a helpful assistant onto the exploration phase adds
nothing measurable. The struggle phase does not want a co-pilot.

One more constraint, because "let them struggle" is as over-claimable as "give them
a tutor": **the instruction phase is mandatory.** Productive failure is problem
solving *followed by* instruction, and consolidation must contrast the learner's own
failed attempts against the canonical solution. An AI that only obstructs is as
wrong as one that only helps.

---

## 3. The simulated peer, and the one thing AI cannot fake

The strongest result in the peer literature is also the strangest.

Smith et al. (2009, *Science*) ran the decisive experiment on peer instruction.
Students answer a concept question alone, discuss with neighbours, revote —
correctness rises. Is that learning, or social copying from whoever knew? They
followed with a second, isomorphic question answered individually:

> **"Peer discussion enhances understanding, even when none of the students in a
> discussion group originally knows the correct answer."**

The mechanism is not transmission. It is articulation, commitment, and the
reconciliation of conflicting commitments. **Two wrong students arguing produce
understanding neither had.**

Smith et al. (2011) added the sequencing: peer discussion **followed by** instructor
explanation beat either alone, substantially. Peer first, expert second — structurally
identical to problem-solving-before-instruction.

So can an AI hold the peer position? Three obstacles, and they are not equally
tractable.

**Known asymmetry.** The learner knows the model has read everything. A model
asserting a wrong answer is either deferred to or dismissed as roleplaying. Neither
is peer engagement.

**No stakes symmetry.** A human peer is embarrassed to be wrong. That embarrassment
is what makes the commitment real and the reconciliation effortful.

**Capitulation.** A peer who abandons their position the moment you push back
supplies no resistance and therefore nothing to reconcile. Measured capitulation
rates sit around **58%**, with **78.5% [77.2, 79.8]** persistence once it happens —
figures §02 works through in the sycophancy context.

And one collaborative structure is flatly unavailable. Jigsaw works by **positive
interdependence under genuine information asymmetry**: each learner holds a unique,
necessary fragment and the group cannot succeed without every member. An AI cannot
supply this. Any asymmetry is simulated, and the learner knows the model could
produce the other fragments on request. **Jigsaw requires scarcity of knowledge, and
AI is defined by its abundance.**

The honest verdict: **the peer role is the weakest of the six for AI**, and "AI
study buddy" is the least defensible product framing in the category. The salvage
is not to fake symmetry. It is to be a committed adversary, or one voice among
several — both of which preserve the conflicting-committed-positions mechanism
without requiring a symmetry that does not exist.

---

## 4. The audience, and the environment that cannot flatter

### 4.1 Why an audience matters at all

Two findings from independent literatures converge on a single mechanism.

Rosenshine, Meister & Chapman (1996) meta-analysed teaching students to **generate
questions**: median ES **0.36** on standardised tests, **0.86** on
experimenter-developed ones. Their most useful sentence is the deflating one — "the
traditional skill-based instructional approach and the reciprocal teaching approach
yielded similar results." The *format* was not the intervention. The
question-generation skill was.

That matters for role design in a way builders consistently miss. **What transfers
is the learner's acquired disposition to interrogate material.** Any AI that
performs the questioning *for* the learner captures the performance and destroys the
disposition — which is exactly the shape of Mousazadeh's (2023) null: explainable
ChatGPT improved performance on the specific tasks it explained and produced **no
generalised gains in metacognitive knowledge or writing.** Targeted transfer, no
metacognitive transfer, precisely as you would predict if the AI is doing the
monitoring.

### 4.2 The environment role

The environment holds no epistemic stance toward the learner. It holds
**consequences**. A simulation that diverges, a failing test suite, a patient that
deteriorates, a quiz that the agent you taught then fails.

This is the only role where **disconfirmation is structural rather than social**,
and that single property does more work than any amount of model tuning. A unit
test cannot be sycophantic. A simulation cannot be talked round. The learner's error
surfaces as a consequence rather than as a correction from an authority, which also
preserves the ego-protection property that makes teaching-an-agent work for
low-confidence learners.

> **If agreeableness is the master obstacle, the environment is the master
> mitigation — and it is a systems-architecture choice, not a model-alignment
> problem.**

§02 describes the architecture in its teachable-agent form. The generalisation is
broader: for any role, prefer a design where being wrong has a visible non-social
consequence over a design where being wrong requires the model to say so.

---

## 5. The coach

The instrument role — AI extending a human's capability on a task that human still
owns — has the best evidence-to-deployment ratio of the six and receives the least
attention, because "AI helps a teacher be better" is a worse pitch than "AI replaces
the teacher."

Tutor CoPilot supplies real-time suggestions to *human* tutors during live sessions.
The AI never faces the learner. Its distributional signature is the interesting
part: **the largest gains went to the least experienced tutors** — the inverse of
the pattern where unstructured AI access widens the gap between low- and
high-prior-knowledge students.

The result is also honestly limited, and §09 carries the numbers: a proximal exit-
ticket gain alongside a distal null. Treat it as the cleanest demonstration that the
instrument role is real and that its distal effects are unproven, not as a headline.

---

## 6. The nulls this section has to carry

**Announced adversarialism backfires.** Nemeth, Brown & Rogers (2001). The obvious
implementation of "AI adversary" — tell the learner you are about to argue the other
side — is the one that produces bolstering rather than divergence. This is the most
consequential negative result in the section and it is why §2.2 exists.

**Fluency raises confidence and ratings with no effect on learning.** Carpenter and
colleagues, across **five studies from 2013 to 2020**, found that a fluent
instructor produced higher judgments of learning and higher instructor ratings with
**zero** gain in actual learning. An LLM is a maximally fluent instructor by
construction. This is the most directly transferable warning in educational
psychology and it is essentially absent from AI-education discourse. The felt/real
dissociation itself is established in **§14** and **§17**; the transferable part
here is that *fluency of delivery* is one of its cheapest triggers.

**Perceptual disfluency failed to replicate.** Bjork & Yue (2016), from the
originators of desirable difficulties: hard-to-read fonts largely do not work.
Difficulty per se is not the mechanism; retrieval and generation are. **Do not build
an AI that is gratuitously hard to read. Build one that makes you generate.**

**LLMs had no main effect on overall learning.** Lehmann, Cornelius & Sting
(2024/2025), pre-registered lab experiments plus a field study. The effects were
entirely in the *usage pattern*: substitution use — generate the solution — broadened
coverage while reducing depth; complementation use — ask for an explanation —
deepened understanding without broadening. And LLM access widened the gap between
low- and high-prior-knowledge students, a property §07 establishes belongs to
untargeted delivery rather than to the technology.

**The socially engaging agent is not a universal win.** Tärning, Haake & Gulz (2011)
added a social chat module to a teachable-agent maths game. High- and mid-achievers
improved. **Low-achievers disliked it, chatted more, and went off-task more** — the
learners who most need the ego-protection property were the ones the social framing
cost. An aptitude–treatment interaction, not a feature.

**And one paper must be flagged rather than cited.** A 2025 quasi-experimental study
titled "AI as a Socratic Dialogue Partner," with a critical-thinking instrument as
its outcome, describes its own findings as **hypothetical**. It is unverifiable as
evidence and it will be cited by others as though it were not. We name it here so
that nobody, including us, launders it later.

---

## 7. The counter-argument, and the sequence

The strongest objection is that the tutor role is not empty. Kestin et al. (2025)
is a genuine randomised result in an authentic course, at **d ≈ 0.63**, and it
belongs in the ledger — with the caveats §09 records, including that the tutor was
built and evaluated by its developers and was **explicitly pedagogically
constrained** rather than a helpful assistant. The comparison was
AI-with-pedagogy against classroom-with-pedagogy.

So the claim is not that the tutor role is worthless. It is that the tutor role is
over-used relative to its evidence, and — more precisely — that it is being deployed
*out of order*.

The same ordering appears in three independent literatures:

| Phase | Role | Warrant |
|---|---|---|
| 1. Encounter | **Environment / adversary** — struggle before instruction | Problem-solving-before-instruction, **g = 0.36 [0.20, 0.51]**, rising to 0.37–0.58 at high fidelity |
| 2. Reconcile | **Society** — conflicting committed positions, learner arbitrates | Smith 2009: peer discussion works with no expert in the group |
| 3. Consolidate | **Tutor** — canonical instruction, contrasted against the learner's own attempts | Smith 2011: peer *then* instructor beats either; the instruction phase is mandatory |
| 4. Test | **Student** — teach an agent that then acts on what you taught | §02 |
| 5. Grill | **Adversary** — authentic, unannounced objection to the learner's own explanation | Nemeth 2001; question generation ES 0.36–0.86 |

**The field has built step 3, and only step 3.** It is the one step that requires the
AI to be knowledgeable and agreeable, and by Smith (2011) it is the step that works
only when steps 1 and 2 come first. Deployed alone, it is the condition that
produced the unassisted-exam penalty.

That is also the answer to the "grilling" requirement this project started with.
Grilling — sustained, escalating, unsympathetic interrogation of a claim the learner
has just made — is the union of four validated mechanisms: retrieval practice,
question generation, illusion-puncturing through attempted explanation, and authentic
dissent. **No study evaluates grilling as a named construct with an AI.** Given four
converging literatures and zero direct evidence, it is the highest-expected-value
untested intervention in this report, and it should be run before it is sold.

---

## 8. What this section commits us to

- **Never announce the adversary.** Performed opposition produces bolstering. The
  objection must be the model's own, and unannounced.
- **Do not build an AI peer.** No stakes symmetry, no real commitment, and jigsaw's
  information scarcity is unfakeable. Build a committed adversary or a society of
  voices instead.
- **Prefer structural disconfirmation to social correction.** Where the learner can
  be shown wrong by a consequence, do not have a model say so.
- **Never let the AI do the questioning the learner should learn to do.** The
  transferable asset is the disposition to interrogate; performing it for the learner
  captures the performance and loses the disposition.
- **Do not tune any of this on satisfaction.** Children call persistent questioning
  pushy, and they are describing the intervention working.
- **Do not scaffold the struggle phase.** g = −0.08 across 118 comparisons.
- **Report calibration, not just performance.** Five instructor-fluency studies say
  a fluent teacher moves confidence and not learning; an AI condition can look
  neutral on performance while being badly worse on the confidence–performance gap,
  and it is the gap that decides when a learner stops studying.
- **Sequence the roles.** Encounter, reconcile, consolidate, test, grill. The
  consolidation step is the only one anyone has built, and it is the one that
  requires the other four to precede it.

Six roles, one deployed. The interesting thing is not that the tutor is bad. It is
that the field does not appear to know there was a choice — and therefore has never
sequenced them.

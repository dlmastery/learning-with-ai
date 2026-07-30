---
title: "The Agenda — ten experiments, and what would falsify this survey"
section: agenda
status: draft
date: 2026-07-30
source_report: research/raw/F9-open-problems.md
---

# The Agenda

Two ERIC queries, run 2026-07-27:

| Query | Records |
|---|---|
| `"retention test" AND "ChatGPT"` | **0** |
| `"transfer test" AND "ChatGPT"` | **0** |

A third, `"artificial intelligence" AND "delayed posttest"`, returns seven, and
the recent entries are EFL vocabulary studies and not conceptual transfer.

So: **no adequately powered trial of an LLM tutor has measured what a learner can
do, without the AI, on novel items, four or more weeks after the intervention
ended.** Every procurement decision, every scaling decision, every roadmap in
this field is currently made on assisted or immediate outcomes.

The one study that separated them found the sign flips. In a randomised trial of
roughly 1,000 students across ~50 classrooms, assisted practice performance rose
by **+48%** for an unguarded GPT assistant and **+127%** for a hint-only tutor.
On the closed-book exam with the AI removed, the unguarded arm was **−0.054
(SE 0.022), p < .05, a 17% deficit relative to never having had access**, and
the guardrailed arm was **−0.004 (SE 0.013), not significant.**

That is the whole problem in one study. **A variable that moves an outcome from
−17% to zero is not near a ceiling; it is near a decision.** And nobody has
measured what happens six weeks later (§01).

Ten experiments follow, ranked, each with a runnable design and a pre-registered
falsifier, and then the case that this survey is wrong, stated at full strength.

Three of the ten were ranked in July 2026 against nineteen open problems. The
other seven landed on 2026-07-30 with the domain reports behind §40, §41, §42,
§43, §44, §45 and §46, each closing with a specified trial and a power
calculation. **Two of the seven put a specification this survey publishes on
trial**, which is a category the original nineteen did not contain, and one of
those two enters at second and moves the standing order.

| # | Experiment | The quantity that decides it | Learners | |
|---|---|---|---|---|
| 1 | The delayed, unassisted, novel-item outcome | Immediate-to-delayed rank correlation across arms | 900 | standing |
| 2 | Randomise the graph, not the policy (§45) | Equivalence within δ = 0.10 SD | 857 × 8 topic pairs | **new — enters at 2** |
| 3 | Persistent learner state against a stateless baseline | C − A on prerequisite-dependent transfer | 600 | was 2 |
| 4 | Does the guardrail that removes harm ever add benefit? | A − C on 6-week unassisted transfer | 900 | was 3 |
| 5 | The guardrail where the machine can write the essay (§43) | B − C on a delayed cold-prompt composition | 636 | **new** |
| 6 | Relational standing × correction stance, dosage fixed (§40) | Correction acceptance, then 14-day transfer | 1,000 | **new** |
| 7 | Randomise revision allocation, with an off-board audit paper (§41) | Whether the marks gain reproduces on the audit paper | ~630 | **new** |
| 8 | Skill only, affect only, both (§42) | Arm B on the 6-week unassisted outcome | 645 | **new** |
| 9 | Does speaking to a machine transfer to speaking to a person? (§44) | Comprehensibility with an unmet human at 4 weeks | 465 | **new** |
| 10 | The peer mechanism, and the cheap question inside it (§46) | C − B at d = 0.15; collaboration skill at g ≈ 0.7 | 4,600 / 99 | **new** |

The ordering is expected information gain against feasibility, with one tie-break
that has changed. Where two experiments score alike, the one that can retire a
specification this survey already publishes goes first, and the one that can only
retire a mechanism this survey proposed goes second. On that rule the graph trial
displaces the memory ablation from second to third and the guardrail trial from
third to fourth. Nothing else is reordered; experiments 5 to 10 are additions
below the standing three.

---

## Experiment 1. The delayed, unassisted, novel-item outcome

**Why first.** It is the measurement precondition for everything else.
Seventeen of the nineteen open problems in the underlying research name a
delayed unassisted transfer test as their primary outcome, and six of the seven
new trials name one too. If that instrument is not built, validated, and shown
to be administrable at scale, none of the rest can be run credibly. It is also
cheap: no novel system to build.

| | |
|---|---|
| **Population** | 900 students, grades 8–10, one school system with a stable roll, one curricular unit (e.g. linear functions) not revisited for a full term |
| **Arms** (individually randomised within class, 300 each) | **A** — guardrailed LLM tutor, hint-only · **B** — unguarded LLM assistant · **C** — matched-time supervised study with worked examples, no AI |
| **Power** | 300/arm detects d = 0.23 at 80%; with ANCOVA on a pre-test (r ≈ .6), **d ≈ 0.18**. At 25% attrition it still detects d = 0.21 |
| **Primary outcome** | **Unannounced, unassisted, closed-device test at 6 weeks**, on items never seen, from the same construct specification but a disjoint item family. Blind-scored |
| **Secondary** | Immediate assisted score; immediate unassisted score; procedural vs conceptual retention separately; and the **immediate-to-delayed rank correlation across arms** |

**Pre-registered prediction.** A > C at delay by 0.15–0.30 SD; B ≤ C at delay;
and **the arm ordering at six weeks differs from the arm ordering on the
immediate assisted test.**

That last clause is the finding that matters, because it invalidates the
measurement practice of the entire field rather than one product.

> Falsifier. If immediate assisted performance and 6-week unassisted
> performance rank the arms identically, with **r > .8** across a range of
> systems, then immediate measurement is a valid proxy, this problem dissolves,
> and the field's existing evidence base is worth far more than this survey
> credits it for.

The falsifier here is *good news for everyone else*. We should want to run it
precisely because it can rescue a decade of published effect sizes.

Why it has not been run is not an intellectual difficulty. A delayed unannounced
test costs learner goodwill, requires re-contacting a dispersed cohort, and
produces attrition that is almost certainly non-random — the students who show up
are the ones who learned. It is also commercially unattractive: it is the one
measurement that can turn a shipped product's headline number negative, and every
party positioned to fund it has an interest in the immediate number.

---

## Experiment 2. Randomise the graph, not the policy

**Why second, and why it displaces the memory ablation.** §25 tells a builder to
compute the mastery vector over a concept's transitive prerequisite closure and
enter at the weakest link. §18 takes a prerequisite graph as an input to a
textbook that writes itself. Four reports assume the architecture. But the one
tally that separates between-topic sequencing from within-topic sequencing puts
the between-topic cluster at **zero of eight** against its baselines, while both
clusters that did work are decisions inside a topic (§45). This survey publishes
a rule whose warrant comes from a different question's evidence, and the rule is
live in code. Every study in that literature randomises which traversal policy
walks a fixed graph. Nobody has randomised the graph.

| | |
|---|---|
| **Population** | 900 learners in a mid-sized deployment, each contributing at least eight eligible topics over roughly two terms — about 7,200 topic sequences |
| **Randomisation** | **Within learner, at topic level.** Each eligible topic is assigned to **graph-respecting entry** (verify the prerequisite closure, remediate any gap, then teach the target) or **demand-driven entry** (teach the requested target immediately, repair prerequisites reactively when an error names a missing component). Total instructional time is capped identically in both arms, so neither condition can win by being given more teaching |
| **Power** | An **equivalence trial**, not a superiority trial. Two one-sided tests at **δ = 0.10 SD**, α = .05, 90% power, paired within learner at a between-condition correlation of 0.5 gives σ_d ≈ 1.0 SD and **n ≈ 857 learners**. At a correlation of 0.7, σ_d falls to ≈ 0.77 and n to ≈ 510 |
| **Primary outcome** | **Delayed transfer at 28 days** on freshly generated items for the target topic, scored blind |
| **Secondary** | Time to criterion; a 90-day retention probe; and **the proportion of graph-respecting sessions in which the verified prerequisite gap turned out to be real** — a diagnostic number nobody has ever published |

The margin is the design. What is at stake is not whether an ordering makes any
difference but whether the difference is large enough to pay for building the
graph and keeping it correct, so 0.10 SD is registered in advance as the point
below which the answer is no. Within-learner randomisation is what makes the
sample affordable: one learner supplies eight paired observations, and the paired
correlation does the rest.

> Falsifier. Equivalence within 0.10 SD withdraws the weakest-link entry rule
> from §25, collapses §18's problem from *construct a validated ordering* to
> *answer the question that was asked*, and takes the traversal layer out of the
> learner model. A win above 0.10 SD gives this project its first direct warrant
> for an architecture four of its own reports already assume, and pays for a gate
> it has been using on credit. Both answers change a build, which is why it goes
> second.

---

## Experiment 3. Persistent learner state against a stateless baseline

**Why third.** Memory is the headline feature of the current product
generation and the organising premise of every lifelong-learner-model
architecture, **including this survey's own**. It is being built at real schema
cost, real privacy exposure, and the entire regulatory surface described earlier
in this survey — on zero evidence that it changes a learning outcome. No
trial has compared a tutor that remembers a learner across sessions against the
identical tutor that does not. It moved down one place for a single reason: it
tests a mechanism this survey proposes, and the trial above tests a rule this
survey already publishes and instructs builders to implement.

The census is stark. arXiv `"open learner model"` → 0. `"long-term learner
model"` → 0. `abs:"long-term memory" AND abs:"tutor"` → 0. Six results for
memory + tutoring system + LLM, all system papers, **none containing a
memory-ablation arm.** GitHub `learner model knowledge tracing memory LLM tutor`
→ 0 repositories.

| | |
|---|---|
| **Population** | 600 learners, 12 sessions over 8 weeks, one multi-topic curriculum (introductory statistics — many interlocking prerequisites, high misconception density) |
| **Arms** (200 each) — identical model, prompt, and UI, **differing only in what crosses the session boundary** | **A** — stateless, no carryover · **B** — transcript carryover, prior session summaries in context (what most "memory" products actually are) · **C** — structured learner state: typed per-KC mastery, an explicit misconception register, channel constraints, and pivot history, inspectable and correctable by the learner |
| **Power** | 200/arm detects d = 0.28; with ANCOVA, **d ≈ 0.22**. This matters — the honest prior is *small*, and a study powered only for d = 0.5 produces an uninterpretable null |
| **Primary outcome** | **4-week unassisted transfer on items requiring a prerequisite established in an early session and applied in a late one** — the only place a memory effect can mechanistically appear |
| **Secondary** | Redundant re-explanations of mastered material; time-to-first-correct on prerequisite-dependent items; **learner corrections of the visible state**; and a pre-registered ablation of arm C into **C-typed vs C-untyped** |

Pre-registered prediction. C > B > A, with **C − A ≈ 0.25 SD on the
prerequisite-dependent subscale and ≈ 0 on the topic-local subscale.** The
*localisation* is the real prediction; a uniform gain would indicate a confound.

Two design details carry most of the value. The control must be
summary-carryover and not a true amnesiac, or the comparison measures
politeness instead of memory. And the typed/untyped sub-ablation converts a null
into a diagnosis — because the deep obstacle is knowledge-component
alignment, and nobody has yet demonstrated a domain map that survives transfer
between two systems (§11). **A memory whose contents are badly typed may be worth
exactly nothing**, and no experiment has yet separated that case from the case
where typing is what makes memory pay.

The case for memory also cannot be "better next-item prediction." A zero-parameter
moving average beats every released FSRS version on log loss over 350 million
reviews, so the quantity that layer optimises is not where a memory system would
earn its cost. The case has to be continuity, diagnosis and pivoting — none of
which any released benchmark measures, and none of which anyone has measured
either.

> Falsifier. C = B = A on prerequisite-dependent transfer, with no advantage
> even on redundant-re-explanation counts, would mean persistent state is an
> engineering preference rather than a pedagogical mechanism. Given its
> privacy cost, **that finding should stop people building it.**

---

## Experiment 4. Does the guardrail that removes harm ever add benefit?

Why fourth, and why it is this survey's own thesis on trial. The central
design claim running through these sections is that **restraint is the active
ingredient**. The evidence for that claim is currently *entirely* about harm
removal. The guardrail took the unassisted effect from −17% to exactly zero (§01). **No
study has ever shown a constrained tutor beating a no-AI control on a delayed
unassisted outcome.** Europe PMC, `"guardrails" AND "learning" AND "randomized"`:
**0 hits**. The one relevant trial has not been replicated.

| | |
|---|---|
| **Population** | 900 students, matched-time design, one curricular unit, single school system |
| **Arms** (300 each, **all receiving identical total instructional time**) | **A** — guardrailed AI tutor: hint-only, withholds solutions, requires a reasoning attempt before help · **B** — unguarded AI assistant · **C** — matched-time worked examples plus retrieval practice, no AI — *the best cheap thing we already know works* |
| **Power** | 300/arm detects d = 0.23; the decisive contrast is **A vs C**, with a pre-registered smallest effect of interest of **d = 0.20** |
| **Primary outcome** | 6-week unassisted novel-item transfer |
| **Secondary** | Help-seeking after AI removal; a **dependency probe** (does arm A attempt fewer unaided problems in a later, unrelated unit?); gap-widening by prior-knowledge quartile |

The matched-time constraint is the whole design. Almost every deployment trial in
the corpus adds the AI *on top of* normal instruction, which makes the AI arm
strictly advantaged and the resulting effect uninterpretable as evidence about
the AI.

Pre-registered prediction. A > C by 0.15–0.25 SD, so the constrained system
beats the best cheap alternative but only modestly, and B < C. **Honest
confidence in A > C: about 55%.** That is the confidence level at which an
experiment is worth running.

> Falsifier. **A ≈ C at adequate power is the result that should change this
> survey's posture most.** It would mean the guardrailed tutor's contribution is
> the *scalability of a known-good intervention*, not a new mechanism — still
> valuable, and a completely different claim, which should then be stated in
> those words.

---

## Experiment 5. The guardrail where the machine can write the essay

**Why fifth.** Experiment 4 puts restraint on trial in mathematics practice,
where an unguarded assistant hands over the answer to part of a task. Writing is
the domain where it hands over the artifact, and where a fifteen-year automated
feedback transfer null is still ambiguous between two readings: weak automated
feedback, or automated feedback as such. Across ERIC, Crossref and OpenAlex, §43
could not locate a single randomised trial of generative-AI writing support with
a delayed, unassisted post-test on a new composition. That result set is
dominated by pre/post designs with no control and n between 30 and 120.

| | |
|---|---|
| **Population** | 636 learners, one term, randomised **at learner level within class** |
| **Arms** (212 each) | **A** — unguarded AI writing assistance: drafting, rewriting and feedback without restriction · **B** — guarded assistance: task-level feedback only, no generated prose, no holistic score, structured to prescribe the next move · **C** — no AI, ordinary instruction with teacher feedback. All three write the same number of compositions on the same prompts |
| **Power** | Smallest difference that would change a build decision: **d = 0.30**. 15.7/d² gives **175 per arm**; two pairwise comparisons at Bonferroni α = .025 raise it to **212 per arm, 636 total**. Class-level randomisation would multiply by a design effect of 1 + 24(0.15) = **4.6**, or **≈ 2,930 learners across 117 classes** |
| **Primary outcome** | A **delayed, unassisted, cold-prompt composition** written four weeks after the last session, on a new topic, scored by blinded human raters on the standard rubric |
| **Secondary** | The assisted compositions during the term, which is what every existing study measures; and a content-knowledge test on the topics written about |

That design effect is why the assistance condition has to be enforced in
software instead of by instruction. A learner told not to ask for generated prose
will ask for generated prose, and assigning whole classes to condition costs
2,294 additional learners. A trial half this size can still rule out large harm;
it cannot rule out the harm that matters, which is a quarter of a standard
deviation on what the child can do alone.

> Falsifier. B ≈ C at 212 per arm means the guardrail adds nothing where the
> machine can do the whole task, and the restraint claim running through these
> sections is a finding about mathematics practice. B ≈ A means the guardrail is
> theatre. And if A < C reproduces the withdrawal effect in writing, the harm
> belongs to unguarded assistance in general and not to one subject (§01).

---

## Experiment 6. Relational standing, with dosage designed out

**Why sixth.** Every relationship finding bundles two mechanisms. One is dosage:
a learner who likes the tutor comes back more, and more of everything happens.
The other is a licence to correct, the standing that lets a tutor say *that is
wrong* without the learner disengaging. They imply opposite products, and no
trial in any literature has told them apart, because the manipulation that raises
standing also raises attendance. A tutor can cap items and wall-clock time
identically across arms. A classroom cannot, which is why this became answerable
only once the tutor was software (§40).

| | |
|---|---|
| **Population** | 1,000 learners aged 10–13, one topic with a clean transfer test, including a pre-specified stratum of **≥ 250 students with an active IEP** |
| **Design** (2 × 2, four cells of 250) | **Factor A — standing.** *Continuous*: the tutor carries a visible record of prior sessions, cites it by name when correcting, and frames each correction with the standard plus an assertion of reachability · *Neutral*: identical content and identical corrections, no record cited, competent and impersonal. **Factor B — correction stance.** *Assertive*: states that the answer is wrong and says why · *Accommodating*: hedges, asks the learner to reconsider, accepts the second assertion |
| **Dosage** | **Fixed by construction.** Every arm gets the same number of items and the same wall-clock cap, which designs the attendance mechanism out and leaves the correction mechanism alone in the model. Session length is a manipulation check and never an outcome |
| **Power** | Correction acceptance at a conservative 0.50 vs 0.35 split: **167 per cell**. Delayed transfer at d = 0.25: **251 per arm**. Four cells of 250 give 80% power for a 14-point difference in correction acceptance, d = 0.25 on transfer as a main effect, and **d = 0.35 inside the IEP stratum**. The trial is deliberately not powered for the β = .07 direct relationship-to-achievement path |
| **Primary outcome** | **Correction acceptance** — the proportion of corrections after which the learner's next attempt adopts the corrected procedure |
| **Co-primary** | **Delayed transfer at 14 days**, on unseen items requiring the same procedure in a new surface form |
| **Secondary** | Unprompted admissions of not understanding per 100 turns; and satisfaction, collected last, which is expected to move in the Continuous arm regardless and is the falsification trap |

The IEP stratum earns this trial a place it would not otherwise hold. It is the
only pre-specified disability stratum anywhere in this agenda, and while one topic
and one manipulation is not the empty chair (§04), it is the first design here
that returns disability-stratified randomised evidence at all.

> Falsifier. Written in advance by the report that proposed it: the relationship
> thesis for an AI tutor is dead if, with dosage fixed, the Continuous arm's
> satisfaction advantage is positive and significant while the delayed transfer
> contrast has a 95% CI whose upper bound falls below d = 0.20 and the correction
> acceptance contrast crosses zero. Six studies with weaker manipulations have
> already landed there, so the interpretation has to be pre-registered.

---

## Experiment 7. Randomise revision allocation, and score it on an off-board paper

**Why seventh.** Every measured intervention in test preparation manipulates a
technique. Allocation, meaning what the learner works on next, is the one degree
of freedom that is large, unmeasured, and structurally unavailable to a coaching
centre, which teaches a cohort. Everything else in the category is either
established (retrieval, spacing) or already null (nudging). And no
test-preparation study in that literature has ever carried an instrument capable
of separating learning from score inflation (§41).

| | |
|---|---|
| **Population** | ~630 candidates for a public examination with published past papers and granular mark schemes; GCSE or A-level mathematics is cleanest because the specification is stable |
| **Arms** (individually randomised) | **Control** — full access to the same past-paper library, the same generated items and the same marking, with the learner choosing what to work on · **Treatment** — identical resources, with the system allocating each session's topics by expected-marks maximisation over the learner's per-topic posterior and the specification's historical topic weights. Both arms get closed-book retrieval and the same spacing defaults |
| **Power** | Effects worth detecting are 0.10–0.20 SD. d = 0.15 needs **700 per arm, 1,400 total**; ANCOVA at a deliberately conservative ρ = 0.80 multiplies by (1 − ρ²) = 0.36, giving **252 per arm, ~505 total**; 20% attrition between consent and the sitting gives **~630 candidates** |
| **Primary outcome** | Marks on the real public examination — externally scored, publicly documented, and outside the reach of the LLM-as-judge failure §32 describes |
| **Audit instrument** | A held-out paper from a **different examination board** covering the same specification, which the system never trained or allocated against |
| **Secondary** | Per-topic marks, to test whether any gain is concentrated where the optimiser reallocated |

The audit paper is the contribution. No test-preparation study in that
literature has ever included one, and every one of them should have. It is also
why a school district can run this in a year: 630 candidates, one specification,
and a primary outcome nobody in this project scores.

> Falsifier. If the treatment arm's gain reproduces on the off-board paper at the
> same magnitude, allocation is teaching, and the score-inflation objection to
> this whole product category is answered. If the gain appears on the primary
> paper and is absent on the audit paper, the system is a score-inflation engine
> and should be described as one. Only one of those results is commercially
> convenient, which is most of the argument for registering both.

---

## Experiment 8. Skill only, affect only, both

**Why eighth.** No trial in the anxiety literature can hold anxiety constant
while moving skill, or the reverse, because every classroom intervention moves
both at once. That is why the direction question is still open after decades, and
it is what a system with item-level control can do that a classroom cannot (§42).

| | |
|---|---|
| **Population** | 645 learners, two school terms, one district partnership, stratified on a baseline maths-anxiety screen |
| **Arms** (215 each) | **A — skill only**: adaptive remediation of the prerequisite gap, every affective feature disabled · **B — affect only**: the affective features at full strength, with item selection held to the learner's existing level so that no new skill is taught · **C — both** |
| **Power** | Smallest difference worth detecting between two arms: **d = 0.25**. Three pairwise contrasts at Bonferroni α = .0167 two-sided, 80% power: **335 per arm, 1,005 total**. ANCOVA on a baseline unassisted pre-test at r = 0.6 gives **215 per arm, 645 total**. Enriching to the top tercile of the screen brings it below 500 and narrows the population the answer applies to |
| **Primary outcome** | **Delayed unassisted performance on transfer items at 6 weeks**, administered without the tutor, blind-scored |
| **Secondary** | Anxiety on the same instrument at 6 weeks, and the avoidance-signature rate from the logs |

Three theories make three different predictions here and the trial separates
them. Deficit Theory predicts A ≈ C > B on both outcomes. The Debilitating
Anxiety Model predicts B > A on anxiety and B ≈ A on performance in the short
run, with B's advantage appearing only at follow-up. Reciprocal Theory predicts
C > A ≈ B on performance with a super-additive gap.

> Falsifier. Registered before the trial runs: arm B moves the anxiety instrument
> and does not move the 6-week unassisted outcome. That would make the affective
> layer a comfort feature, and it should then be costed as one and sold as one.

---

## Experiment 9. Does speaking to a machine transfer to speaking to a person?

**Why ninth.** Unlimited low-stakes practice with a partner who cannot be
embarrassed is the one capability advantage in this field that is not merely
economic. It is also what the whole consumer segment is sold on. Every trial in
the domain scores the material it trained. The nearest quantitative estimate runs
against the hypothesis: cross-modality contrasts of 0.29 [−0.21, 0.79] and
0.19 [−0.31, 0.70], against same-modality contrasts of 0.65–0.84 (§44).

| | |
|---|---|
| **Population** | 465 learners across three arms with a hierarchical testing order, or **310 for the two-arm A-versus-B version**, which is the question a builder actually faces |
| **Arms** | **A** — 12 weeks of AI conversational practice · **B** — 12 weeks of human conversation partners matched on **speaking minutes** · **C** — matched-time non-speaking study |
| **Power** | Plan against **d = 0.35** on A vs C, a control-adjusted estimate against business-as-usual and not a trained-item effect: **129 per arm** at 80% power, α = .05 two-sided. Three arms with hierarchical testing (A vs C, then A vs B) and 20% attrition gives **n ≈ 465** |
| **Primary outcome** | Collected **four weeks after the last session**, in an unscripted conversation with a human interlocutor the participant has never met, scored for **comprehensibility** on a nine-point scale by two raters blind to condition |
| **Co-primary** | **Intelligibility** — orthographic transcription accuracy by naive listeners |
| **Secondary** | Minutes of L2 speech produced, turns initiated, and self-reported willingness to communicate, so that the self-report and the behavioural measure can be compared in the same sample |

The outcome instrument is a human being, which is most of why nobody has run it.
It cannot be automated without reintroducing the machine whose effect is under
measurement.

> Falsifier. A ≈ B on delayed comprehensibility is the best available outcome for
> this category and should be reported as one: machine practice substitutes for
> scarce human practice at a fraction of the cost. A ≈ C retires the central
> marketing claim of the largest consumer segment in the field, and would be worth
> more than another significant result on trained items.

---

## Experiment 10. The peer mechanism, and the cheap question inside it

**Why last, and why it is here at all.** One part of a group cannot be supplied
by an AI tutor: being disagreed with by someone who is genuinely uncertain. A
model that knows the answer and performs uncertainty is not in that state. The
residual is worth on the order of 0.1–0.2 SD (§46), and detecting it takes a
multi-school trial nobody will fund. The cheap question rides in the same three
arms and needs 99 learners.

| | |
|---|---|
| **Population** | Three arms, learner-level randomisation within classrooms, one term, one subject with a validated concept inventory — introductory mechanics, because the FCI exists |
| **Arms** | **A** — AI tutor alone: full personalisation, individual-accountability scoring, no peers · **B** — AI tutor plus an AI peer that commits to a possibly-wrong position and defends it · **C** — AI tutor plus brokered human pairing on disagreement items |
| **Power, the expensive half** | The contrast is **C − B**. At the low end of the residual, **d = 0.15** needs **699 per arm**, about 2,100 across three arms; an ICC of 0.05 and cluster size 25 give a design effect of 1 + 24(0.05) = **2.2**, raising it to roughly **4,600**. At d = 0.25 it is 252 per arm before the design effect and about 1,700 after it |
| **Power, the cheap half** | The **collaboration-skill** secondary outcome is where the CSCL syntheses predict **g ≈ 0.7**, and at that magnitude **33 per arm** suffices before the design effect — **99 learners** |
| **Primary outcome** | Delayed concept-inventory score at eight weeks, scored blind |
| **Secondary, and the one worth running first** | A collaboration-skill measure, because that is where the group's distinctive effect lives and no arm-A system can produce it |

The 46-fold gap between those two rows is the entry, and not a footnote to it.
Same three arms, same term, same instrument set, and the question you pick
decides whether the study costs 4,600 learners or 99. It also sets a floor under
what counts as evidence here: any study in this space with fewer than 500 per arm
reporting a null on peers has not tested the hypothesis, and a 60-learner pilot
has 80% power only for d ≈ 0.51, which is larger than the whole cooperative
learning effect.

> Falsifier. C ≈ B at 699 per arm means simulated commitment is as good as real
> commitment, and the last principled objection to a pure one-to-one architecture
> goes with it. A ≈ B ≈ C on collaboration skill at 33 per arm means an
> AI-mediated group does not teach a learner to work with a person, and the
> single-tutor thesis carries a cost it currently does not price.

---

## What would falsify this survey

This survey argues that the frontier deployment results on record are a floor with
the brakes on; that constrained, grounded, pivoting, remembering systems would do
better; and that nobody has built the good version and measured it.

Say first what that record actually is, because the argument turns on it and on
nothing else. **Sierra Leone** +0.258 SD adjusted, and +0.216 SD (SE 0.137) unadjusted
and not significant, across 48 classrooms in eight weeks. **Nigeria** +0.23 to +0.31.
**Rori** 0.37, across eleven clusters, developer-authored. **Kestin** d ≈ 0.63,
developer-built and developer-evaluated, in a median 49 minutes. **Tutor CoPilot**
+4 percentage points on exit tickets and +9 for students of the lowest-rated tutors,
with **no significant movement on the end-of-year state test**. **Bastani** +127% on
assisted practice, −17% unassisted for the unguarded arm and −0.004 (n.s.) for the
guardrailed one (§09, §01). That is the whole frontier record, and it is measured
almost entirely on immediate or assisted outcomes over eight weeks or less.

One clause belongs with every one of those numbers and this survey previously
dropped it: those gains arrive **at much lower cost**. Tutor CoPilot ran at about
$20 per tutor per year. A result of that size delivered at that price is a different
proposition from the same result delivered by hiring people, and the source that
produced the summary called the cost the genuinely important finding.

Here is the strongest case against the survey's reading, stated properly and not
as a strawman. Anyone who cannot state it in this form has not earned the right to the
survey's conclusion.

**Premise 1. The frontier record is the only reference class, and it is not a floor.
It is the measurement.** Every trial listed above ran a real frontier model, in a
real classroom, with real teachers, and none of them was a deliberately degraded
version of what a good system would be. Sierra Leone had tablets, a 2:1 device
ratio and supervision (§09); Tutor CoPilot had trained human tutors in the loop; Kestin's
tutor was purpose-built by a physics-education group and still needed a developer to
evaluate it. On this premise the survey's move — *these results are what bad systems
do* — is unfalsifiable special pleading: any result below expectation gets attributed
to a mechanism nobody has built, and any result above it gets attributed to the
mechanisms the survey favours. **A thesis that can absorb every outcome has not
predicted any of them.** The premise's demand is concrete and fair: name in advance
the property that separates the good version from the systems already trialled, and
name the trial that would show it missing.

**Premise 2. The nulls already on record are the honest prior, and they are the
most rigorous studies in their respective literatures.**

| Result | Effect | What it measured |
|---|---|---|
| Orton-Gillingham vs comparison instruction | **g = 0.22, p = .40**; g = 0.14, p = .59 | HUMAN — teacher-delivered reading instruction (Stevens et al. 2021) |
| Expanding retrieval intervals | **g = 0.034, n.s.** | HUMAN — schedule manipulation, lab and classroom (Latimier 2020) |
| Lesson Study (EEF) | **ES 0.02 [−0.06, 0.09], p = .65**; n = 6,437; 181 schools; **very high** security; null in every subject and subgroup; no dose–response; good fidelity | HUMAN — teacher professional development |
| Ruffle&Riley (LLM learning-by-teaching) | **null twice**, N = 100 and N = 200, with high subjective ratings and users needing *more* time | **FRONTIER** — LLM, 2023–2024 |
| Lehmann et al. | **no main effect**, two preregistered experiments — plus gap-widening | **FRONTIER** — LLM, 2024 |
| RTI at federal scale | **negative** Grade-1 impacts, regression discontinuity | HUMAN — a schooling framework (Balu et al. 2015) |
| Working-memory training | **no transfer** | HUMAN — cognitive training (Melby-Lervåg et al. 2016) |
| UDL | outcomes **not demonstrated** | HUMAN — a curriculum-design framework |

Two of the eight rows measured a language model, and those two carry the premise:
both are preregistered, both are frontier, and both are null. The other six are
evidence about *instruction* — they are the reason to expect rigour to shrink an
effect, and they are not evidence about what an AI tutor can do. The survey has not
always drawn that line where it belongs, and the line is drawn here.

**Premise 3. Added mechanism adds load, and the load is real while the benefit
is speculative. This is the sharpest version, and this survey's own evidence
supplies it.** Multiple concrete representations *harmed* symbol learning, with
the harm attributable to multiplicity. Five ladder rungs did not beat three
(Mdiff = 0.16 [−0.78, 1.09], p = .738). Persistent decorative detail carries
**g = 0.43 of harm**. Mixing models *reduced* ensemble quality — a single-model
Mixture-of-Agents beat the mixed version by 6.6%. Debate does not reliably beat
self-consistency. Declaring dependencies made notebook reproduction *worse*.
**Every one of those is a case where the elaborated version lost to the plain
one**, and "a village of agents with persistent state, deixis, laddering,
error-holding tutees and a pivot engine" is the most elaborate system anyone has
proposed. The base rate for elaboration in this literature is not good.

**Premise 4. The mechanism the survey most relies on has a moderator that dwarfs
it. AI tutoring with teacher support: g = 1.426. Without teacher support:
g = 0.077** — approximately null. If the human is doing the work, every
architectural refinement is optimising the small term.

**Premise 5. The field's positive results degrade under scrutiny in one
direction only. Sierra Leone's unadjusted estimate (+0.216 SD, SE 0.137**) is
not significant (§09). The largest positive LLM-tutoring meta-analysis (g = 0.867) was
**retracted in 2026**. One prominent tutor was built and analysed by its first
author with no funding statement. One trial has 11 clusters. Another lost 43% of
its sample. **Where independence and rigour increase, effects shrink. That is the
signature of a literature whose true effect is smaller than its published mean.**

### What the survey says back, as reasons to test and not refutations

One: the nulls are mostly about branding and not about mechanism. Orton-Gillingham
nulls while its active ingredient, explicit systematic decoding instruction,
carries d = 0.41 to 0.55. Expanding intervals null while *scheduling retrieval at
all* carries classroom d = 0.54, with only 12 of 271 massed-versus-spaced
comparisons failing. Lesson Study nulls as a *process* while content-bearing
interventions do not. The pattern is that **the wrapper fails and the mechanism
holds**, and this survey's programme is explicitly mechanism-level.

Two: the dissociation results are sign results, not ceiling results. A
ceiling story predicts small positive effects everywhere. It does not predict
−17%, and it does not predict the same model with a different interaction policy
landing at zero in the same study (§01).

Three: the empty chair. Zero randomised trials of AI tutoring on learners
with disabilities is not a verdict. The ceiling argument cannot even be assessed
for the population where prior-knowledge, dosage and fidelity constraints bind
hardest, which is where the mechanism-level case is strongest.

---

## The concession conditions, stated in advance

We would concede that the frontier results already on record are what this
technology does, and not a floor set by unfinished systems, and that added
mechanism does not pay, if:

1. **Experiment 4 returns A ≈ C** at n = 300/arm. The single most decisive test:
   the flagship design against the best cheap known-good alternative on our own
   preferred outcome.
2. **Experiment 3 returns C = B = A** on prerequisite-dependent transfer *and*
   the typed-vs-untyped ablation shows no difference — persistent state buys
   nothing even when correctly typed.
3. **The village-vs-single-agent comparison returns parity at matched compute** —
   architectural elaboration is compute in a costume.
4. **A teachable agent that can genuinely stay wrong returns parity with one that
   cannot**, despite a clean separation in belief persistence — the most
   distinctive mechanism in the design is inert.
5. **Any two of deixis, pivot latency, and laddering return flat.** Those are the
   three "add a mechanism" bets; two of three null puts the elaboration thesis in
   serious trouble regardless of the others.
6. **A well-powered, independent, preregistered trial of a system implementing
   several of these mechanisms together shows no advantage over a matched-time
   no-AI control** on a delayed unassisted outcome, against a pre-registered
   smallest effect of interest of d = 0.20. This is the cleanest trigger and the
   one we should most want run, because it tests the conjunction instead of the
   parts.
7. **Experiment 2 returns equivalence within δ = 0.10 SD.** The transitive
   prerequisite closure §25 publishes and §18 assumes is then an architecture we
   pay for and cannot detect, and the weakest-link entry rule comes out of §25.
   This is the first concession condition in this survey that would retire a
   specification we wrote, which is why it belongs at the top of the list and not
   at the bottom.
8. **Experiment 5 returns B ≈ C at 212 per arm.** Restraint would then be a
   finding about mathematics practice, and the design claim running through these
   sections would have to be restated at that width.

**If (1) and (6) both land, the correct revision is not a hedge.** It is to
rewrite the thesis as: *AI's contribution to learning is the scalable,
high-fidelity, high-dosage delivery of interventions we already knew worked, and
the design space of novel mechanisms is a distraction.*

That would still be an important and actionable finding. It would redirect the
field toward fidelity and dosage, which is what the section on
designing for the margin already argues for special education, where the
known-good intervention base is two orders of magnitude larger than the AI base.
**We say this now, in advance, so that conceding costs us nothing but a
hypothesis.**

---

## How this agenda gets run

- **Run the outcome instrument first.** Delayed, unassisted, novel-item,
  blind-scored. Report the immediate-to-delayed rank correlation as a headline
  number, because it tells everyone whether their existing evidence base means
  anything.
- **Randomise the graph before building another one.** Within learner, at topic
  level, time capped identically, registered as an equivalence trial at 0.10 SD.
  A specification we publish should be the first thing we put at risk.
- **Ablate memory before building more of it.** Same model, same prompt, same
  UI, differing only in what crosses the session boundary. Split typed from
  untyped so a null is a diagnosis.
- **Put restraint on trial against worked examples plus retrieval practice, at
  matched time**, in mathematics and again in writing, where the machine can
  produce the artifact. Not against business as usual. Pre-register d = 0.20 as
  the smallest effect worth claiming.
- **Report gap-widening by prior-knowledge quartile as a pre-registered
  moderator on every trial**, because the sign of the effect depends on the
  learner.
- **Enforce the arm in software.** Experiments 5 and 6 both fail if the condition
  is a request: a learner told not to ask for prose asks for prose, and a warm
  tutor that also runs longer sessions has measured dosage instead of standing.
- **Publish the falsifier before the result.** Each of the ten experiments above
  has one written down, and none of them is a formality.
- **Three of these are runnable inside one instrumented product** with a few
  hundred consented users and no new modelling work: the memory ablation, the
  gap-widening moderator, and the collaboration-skill arm of Experiment 10, which
  needs 33 learners per arm. A shared delayed-assessment panel is the
  infrastructure that makes the rest reportable. The
  permutation-vs-self-consistency check that used to occupy that third slot has
  been run, and its own falsifier fired: 768 generations, two models, a
  deterministic comparator, at chance both times (C-9). It is a result now and
  no longer an item on this list.

The measurement gap is the widest one in applied AI: dozens of benchmarks for
whether a model is smart, roughly one field trial per organisation per year for
whether it teaches. Anyone building in this space is building without a ruler.
Waiting for someone else to supply one is not a posture this project can afford.
Build the ruler, publish the falsifier alongside the design, and be the kind of
project that would notice if it were wrong.

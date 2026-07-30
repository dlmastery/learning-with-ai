---
title: "The Canon — what the history of pedagogy already settled"
section: canon
status: draft
date: 2026-07-28
source_report: research/raw/I1-pedagogical-systems.md, research/raw/I2-global-traditions.md
---

# The Canon

There is a single question that sorts every pedagogical tradition humanity has
produced into things worth rebuilding and things worth admiring from a distance:

> **Remove the other human and remove the physical objects. Is the thing the
> learner does still the thing that caused the effect?**

For the Keller Plan, yes. For chavruta, no. That one question does more work than
any amount of enthusiasm about AI tutors, and this section is an attempt to run
it across the catalogue honestly — including where it returns an answer the
field would rather not hear.

The thesis under test is the seductive one: *most great pedagogical systems were
abandoned for cost, not efficacy; if AI changes the cost structure, the question
is not what new pedagogy AI enables but which known-good pedagogy just became
affordable.* It is roughly two-thirds right, and the third that is wrong is the
third most likely to be repeated uncritically.

---

## 1. Where the cost actually sat

Start mechanically. A pedagogy's per-learner cost decomposes into seven
components, and AI does not touch them equally.

| Cost component | Does AI reduce it? |
|---|---|
| **Expert attention-minutes** (tutorial, mastery correctives, coaching) | **Yes — this is the big one.** |
| **Assessment and regrading labour** (unit tests, unlimited retakes) | **Yes, near-totally.** |
| Curriculum authoring and sequencing | Partly — generation is cheap; *validation* is not |
| Record-keeping and progress tracking | Yes; this was a first-order killer and is now solved |
| **Physical materials and space** | **No** |
| **Genuine peers with real stakes** | **No** |
| **Institutional and political permission** | **No — and this killed several systems outright** |

AI collapses two of seven components to near zero, substantially reduces two
more, and does nothing at all for three. **The thesis is therefore true precisely
for pedagogies whose costs sat in the first two buckets** — and one system sat
almost entirely there.

---

## 2. The flagship vindication: PSI

Fred Keller's Personalized System of Instruction has five defining features:
written materials as the primary vehicle, chosen because text maximises learner
control; content divided into separable units with stated objectives and
prerequisite structure; **self-pacing**; **unit mastery** at roughly 90% before
progression, with multiple equivalent test forms so a retake is not a retake of
the same items; and **proctors** who administer and mark unit tests immediately,
certify mastery, and supply social reinforcement.

A meta-analysis of **75 comparative studies** concluded that PSI "generally
produces **superior student achievement, less variation in achievement, and
higher student ratings** in college courses."

Read the middle clause, because it is almost never quoted. **Mastery designs
compress the bottom tail.** That is a distributional claim, and it is exactly
what a system designed for the margin should want.

PSI died of administrative labour and proctor cost — item generation, immediate
marking, unlimited fresh retests, and record-keeping. Those are precisely the two
components AI zeroes and the two it substantially reduces. Nothing in the
mechanism requires a human: the proctor's function is certification and
immediacy, not relationship. **PSI is the clean case, and it is the one that
should be built first.**

With one measured caveat carried in the same breath. Self-pacing is a documented
failure mode of PSI *and* of AI tutors, and the policy toolkits state that
mastery learning is "much less effective when students work at their own pace."
Rebuild the spine; add external pacing pressure.

---

## 3. The flagship refutation: Direct Instruction

Engelmann's Direct Instruction is not "the teacher talks a lot." It is a
faultless-communication engineering discipline: sequences designed so the
examples presented logically permit only the intended generalisation, scripted
wording to eliminate ambiguity, placement by assessment into skill-homogeneous
groups, signals and rapid response to maximise responses per minute, mastery
gating, and — the load-bearing part — **sequences that were empirically debugged
over decades. If children misgeneralise, the script is what gets fixed.**

The evidence base is the strongest in this catalogue:

- **328 studies, 413 study designs, nearly 4,000 effect estimates**, 1966–2016.
  "All of the estimated effects were positive and all were statistically
  significant except results from metaregressions involving affective outcomes."
- **Characteristics of the publications, methodology and sample were not
  systematically related to effect estimates** — the absence of the small-study
  and publication-bias signature that discredits most of this literature.
- Effects showed little decline during maintenance and grew with exposure.
  Reported magnitude ≈ 0.6 SD. In special education: 25 studies, **none**
  favouring comparison groups.
- Project Follow Through — roughly **352,000 children, 178 projects, 20 sponsored
  models** — found DI strongest on basic skills and, contrary to the standard
  objection, found the structured models beat the unstructured ones on affective
  and self-concept outcomes too.

And DI is cheap: student workbooks around $20, teacher guides $180–232.

It won the largest educational experiment ever run and was then sidelined — for
teacher resistance to scripting framed as a constraint on creativity, for
ideological mismatch with constructivist orthodoxy, and for a dissemination
apparatus that went on to recommend programmes that had *not* been validated. A
former US Education Commissioner called endorsing all models when "only one of
the sponsors (Direct Instruction) was found to produce positive results more
consistently" "inappropriate and irresponsible."

**Cost was never the binding constraint. Professional identity and institutional
politics were, and AI has no purchase on those.** Attributing DI's fate to
economics is a factual error and this survey will not make it.

There is one genuine and underrated twist, and it is not a cost argument: **an AI
tutor has no professional identity to protect and cannot resent a script.** The
one thing that blocked the best-evidenced curriculum in education is exactly the
thing a machine does not have.

Which makes the failure mode obvious and worth naming loudly. DI's effect size
comes from *validated* sequences. **An LLM generating "DI-style" scripts on the
fly produces the form without the validation that is the entire source of the
effect.** That is the most likely route by which a product claims DI's evidence
base without inheriting any of it.

---

## 4. Four classes, and where each tradition lands

Class A — survives fully. The mechanism is a property of the learner's
cognitive activity; the human was only the delivery vehicle. Mastery gating and
unlimited fresh retesting; scaffolding with contingency and fading (the only
mechanism whose *computer-based* version is directly meta-analytically validated,
ḡ = 0.46 across 144 studies); worked-example modelling; precision-teaching rate
measurement; productive-failure sequencing; DI's sequences *if validated*.

Class B — survives with a named casualty. The tutorial keeps unlimited
"defend your work" sessions and loses **the fallible expert whose regard you earn
and whom you can argue into changing their mind.** Cognitive apprenticeship loses
the community of practice. The case method loses seventy-nine peers publicly
disagreeing with you. The Socratic method keeps questioning-instead-of-answering
and loses refutation and *aporia* — a model trained to be agreeable and resolve
tension will not leave a learner in productive puzzlement, and cannot honestly
occupy Socrates' position of not knowing the answer.

Class C — does not survive. Chavruta needs a genuine equal with stakes who
cannot be dismissed by closing a tab. Jigsaw needs real interdependence. Peer
instruction needs a real distribution of peer misconceptions and real persuasion.
Harkness needs twelve prepared peers — and note that the expensive input there is
not the teacher's attention but the ratio itself, which is precisely what elite
private schooling purchases. Guild apprenticeship needs real production with real
consequences.

**Class D — there was no mechanism to port, because there was never a
measurement.** Waldorf, Reggio (except its documentation practice), Sudbury,
unschooling, Kumon's own evidence base, the Harvard case method specifically, and
the Oxbridge tutorial as such. **Building an AI version of an unmeasured
tradition does not create an evidence base. It creates an unevidenced product
with a prestigious name.**

A refinement this survey owes itself. An earlier section scored Montessori as not
surviving substitution, and a later one narrowed that: what fails to survive is
the wood, and what survives is the *refusal* — the property that a well-made
material cannot be assembled wrongly and stay standing. Both are right at
different granularities. Montessori-as-a-system is Class C; refusal-of-illegal-
states is Class A. Port the mechanism, not the tradition.

---

## 5. The nulls, at full strength

AI cannot make a null result affordable. Eleven documented, all meta-analytic or
randomised:

| Finding | Effect |
|---|---|
| **Group-based mastery learning** on standardized achievement | **"essentially no evidence"**; positive only on experimenter-made measures |
| **Unassisted discovery learning** | **d = −0.38 [−0.44, −0.31]**, *favouring explicit instruction*, 580 comparisons |
| **Problem-based learning** | "tendency to a negative effect on student knowledge"; pooled **d_w = 0.13** with **Q ≈ 954** — uninterpretable heterogeneity |
| **Reciprocal teaching** | non-significant on standardized tests; non-significant for below-average students |
| **Montessori RCT** (preregistered, French public schools) | **null on maths, executive function and social skills**; reading only, d = 0.68 |
| **Lesson Study** (EEF) | **ES = 0.02 (−0.06 to 0.09), p = 0.65**, n = 6,437, 181 schools, **very high** evidence security; no dose–response; fidelity was good |
| **Singapore Math®** | after adding seven studies, **no studies meet WWC design standards; "no conclusions can be made"** |
| **Mathematics Mastery** | pooled +0.073, both individual trials' CIs cross zero |
| **Deliberate practice** | 18% of variance in sports, **1% among elite performers** |
| **Technology-mediated collaborative learning** | **+3 months against +5** for the in-person version |
| **Multi-agent debate** | does not reliably beat self-consistency; a single agent with strong prompts ≈ the best discussion method |

Three of these deserve a sentence each. The Lesson Study null is the most
uncomfortable finding in the section: very high security, good fidelity, 181
schools, and a flat zero — which is what a well-run trial of a beloved method
looks like when the method does not work at scale. The Singapore Math result
means that using the brand while the evidence base is empty is a vendor claim
restated as a finding, which this project's editorial standard forbids outright.
And **technology-mediated collaboration at +3 versus +5** is a measured price for
digitising a social mechanism — not a hypothesis, a number.

The correction already on this project's record belongs here too, because it is
the same species of error: Bloom's two-sigma claim did not replicate. Human
tutoring is **d = 0.79** in VanLehn's synthesis, and intelligent tutoring systems
were already at **0.76** before LLMs existed. But the figure that should be quoted
alongside it — and which an earlier version of this paragraph omitted — is the pooled
randomised estimate: **0.288 SD across 96 RCTs**. Expert one-to-one is worth roughly
eight tenths of a standard deviation under favourable synthesis and **under three
tenths** when you pool the trials. Not two.

And a correction this survey must publish about its own work. The research
behind this section proposed a *pāṭha* protocol — permutation-based fidelity
checking, derived from Vedic recitation's *krama*/*jaṭā*/*ghana* schemes — as a
concrete, falsifiable alternative to self-consistency sampling. It was
explicitly offered for benchmarking. It was benchmarked, and it was falsified.
The idea was good, the mechanism was clearly stated, and the measurement said no.
That is how this is supposed to work.

---

## 6. The exclusion ledger

This is the deepest thing the historical record has to say, and it is almost
never said.

| Tradition | Who was excluded | Constitutive or incidental? |
|---|---|---|
| Vedic study / gurukula | śūdras and those outside varṇa; women, progressively | **Constitutive** — *upanayana* eligibility *is* the admissions rule |
| Nyāya / śāstric education | the same gate, plus Sanskrit literacy | Constitutive |
| The 64 *kalās* | the propertied urban elite | Constitutive |
| Yeshiva / chavruta | women — study "never forbidden, but discouraged"; in practice male | Near-constitutive; changing |
| Madrasa / *ḥifẓ* | heavily gendered access; large opportunity cost | Incidental to method, structural in practice |
| ***Keju*** (Chinese imperial examination) | **all women, for roughly 1,300 years, without exception**; poorer households by cost | **Constitutive** |
| Songlines | initiation status, gender, kin and country; secret-sacred material | **Constitutive, and still actively enforced — respect it** |
| Age-set systems | typically male; advancement capped by age regardless of merit | Constitutive |
| Griot / *jeli* | **hereditary and endogamous** — you cannot become one, or stop | Constitutive |

> **Almost every high-fidelity, low-ratio, high-intensity learning system in the
> historical record achieved its quality partly by rationing access.**

Small cohorts, long apprenticeships and lineage-based trust are cheap when you
have decided in advance that most of the population is ineligible. This reframes
the entire cost thesis. The traditional mechanisms are not expensive because they
are good; **they are good, and they were affordable because they were
exclusive.**

AI changes exactly one variable — the marginal cost of attention — and that is
precisely the variable the exclusions were rationing. Which yields the selection
rule for everything in this catalogue: **port the mechanisms whose quality did
not depend on the exclusion.**

The tradition that names the correct design commitment is a story rather than a
system. Ekalavya learned archery from a teacher who refused to admit him, by
building the teacher's image and practising before it, and surpassed the
teacher's own students. The pedagogical content of the story is that **the
admission gate was the only thing that had ever been scarce.** The design
consequence is a default of *yes*: no prerequisite locks, no grade-level gating
of content (only of framing), never "you're not ready" but "here is the shortest
path from where you are," and explicit design for the learner nobody would admit
— the adult with gaps, the disabled learner, the out-of-sequence child.

The honest limit ships with the feature. Ekalavya lost his thumb *after*
succeeding. Removing the teacher's veto does not remove the guild's, and any
product making this claim without a story about credential recognition is telling
half of it.

---

## 7. What is under-built and survives

Four mechanisms that pass the survival test, are implementable today, and almost
nobody has built.

A named, citable feedback taxonomy. Nyāya's *nigrahasthāna* enumerates
twenty-two grounds for defeat in argument. The list matters less than the
property: a fixed, published, learner-visible taxonomy makes feedback
learnable (the learner acquires the categories and self-diagnoses),
auditable (a wrong category assignment is visibly wrong, unlike a wrong
vibe), and symmetric (the learner can apply it back to the AI). Current
tutors give fluent, hedged, unnamed feedback, which is none of those things.

**Variation-theoretic example generation, gated by *shu–ha–ri*.** Enumerate a
concept's critical aspects; vary exactly one while holding the rest invariant;
present differences against a background of sameness. Adaptive systems today vary
*difficulty* and *quantity* — randomly generated problems vary many dimensions at
once and thereby make the critical aspect *harder* to discern. The gate is the
other half: shu, one canonical method enforced with deviation corrected;
ha, alternatives introduced deliberately; ri, the learner adapts and the
system shifts to critique. Current tutors are stuck permanently in *ha* —
maximally accommodating, always offering another way to look at it, including at
the stage where a beginner most needs to be told to do it exactly this way.

Precision-teaching rate measurement as telemetry. Pinpoint a behaviour, time
short trials, chart rate per minute, let the slope drive the decision. Thin
evidence base (11 studies, 170 participants), pure measurement labour, free for
software. Highest ratio of neglect to feasibility in the catalogue.

AI-brokered human pairing. For everything in Class C the correct role is
orchestrator, not participant: matching chavruta partners with compatible level
and incompatible blind spots, authoring ConcepTests, partitioning jigsaw groups
and detecting free-riding, guaranteeing every seminar participant arrives having
engaged the text. AI supplies the objections; it does not supply the partner.

---

## 8. What this section commits us to

- **Run the survival test before building anything.** Remove the other human and
  the objects; if what remains is not the mechanism, the correct role is
  orchestration.
- **Build PSI's spine first** — prerequisite graph, 80–90% mastery bar, unlimited
  retests on *freshly generated* equivalent items, immediate certification, full
  records — and add pacing pressure, because self-pacing is a documented
  failure mode.
- **Take DI's discipline and never claim its evidence.** Generated sequences are
  not validated sequences. Faultless communication, placement, high response rate
  and mastery gating transfer; four thousand effect estimates do not come along
  with them.
- **Never argue from cost where the constraint was permission.** DI lost to
  ideology; competency-based education is blocked by credit hours and
  accreditation; standards-based grading is blocked by transcripts.
- **Evaluate on assessments the system did not author.** Every effect size in
  this literature roughly halves when it moves from a researcher-made test to a
  standardized one.
- **Port only what did not depend on the exclusion**, and default to yes on
  admission.
- **Publish the corrections.** Bloom's two sigma did not replicate. Our own
  *pāṭha* protocol was falsified. Say so and move on.

The historical record is not a museum of things we can now afford. It is a
partially validated engineering catalogue with a very uneven evidence base, an
uncomfortable access history, and a small number of mechanisms that were only
ever gated by the price of attention. Those are the ones to build. The rest are
worth knowing so that we do not mistake a tradition for a finding.

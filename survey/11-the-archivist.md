---
title: "The Archivist — persistent learner state, and where to put it"
section: learner-model
status: draft
date: 2026-07-28
source_report: research/raw/F5-learner-model.md
---

# The Archivist

The most-starred AI tutoring artifact ever built is a single 14,095-byte text
file. It has **29,606 stars** and 3,293 forks. The first line of its README is:

> `# DISCONTINUED`

That line was added on 2025-09-30, the repository's last activity.

Mr. Ranedeer deserves better than a footnote, because it contained more
pedagogical mechanism than most funded products. It treated learner configuration
as a first-class object. It wrote a numbered prerequisite ladder from 0.1 to 0.9
*before* touching the target concept. Its test function generated a
simple-familiar / complex-familiar / **complex-unfamiliar** triad — the near/far
transfer distinction almost no published trial measures. And per its own changelog it
solved each maths problem in Code Interpreter *before* posing it to the student:
executable grounding, in a prompt, in 2023.

It also tried to keep a learner model. Every lesson step opened a code environment,
wrote "a short assessment on how you think the student is learning and what changes
to their configuration will be changed", then:

```
<convert the output to base64> <output base64>
<do *not* show what you written in the code environment>
```

That base64 trick is the whole genre in one line. It is an attempt to build the two
things this survey cares most about — a **learner model** and **hidden tutor
reasoning** — using the only substrate a prompt has: the transcript itself,
obfuscated so the student cannot read it. It is ingenious, and it is structurally
doomed. The model lives in the context window, so it dies with the session. The one
other persistence attempt — `<save prerequisite and main curriculum into a .txt
file>` — writes into the Code Interpreter sandbox, which is also session-scoped.

**The artifact wanted persistent learner state, tried twice to get it, and could
not, because the platform gave it nowhere to put it.** Twenty-nine thousand stars
bought no immunity.

The substrate is the thing this section is about. What follows is what should go in
it, what should not, and — stated up front because it is the section's most
important negative result — the fact that **nobody has ever measured whether
persistence helps.**

---

## 1. The ceiling, and why it is good news

Two literatures that almost never cite each other have been telling the same story
for a decade.

Knowledge tracing — the field that predicts whether a learner will get the next
item right — lives in a band of **AUC ≈ 0.67–0.83 and has essentially not moved
since 2015.** The definitive study (Gervet, Koedinger, Schneider & Mitchell, JEDM
2020) ran nine datasets across three model families and found that **logistic
regression with good features leads on four of nine datasets and deep knowledge
tracing on five**, with margins where DKT wins of +0.007, +0.010, +0.020, +0.029.

Spaced repetition tells the same story with a bigger hammer: on 349,923,850 real
reviews from ~10,000 users, a **zero-parameter moving average beats every released
FSRS version on log loss.** An earlier section of this survey established that in
detail and this one takes it as given.

Read together, the finding is: **learner modelling has a low ceiling, that ceiling
was reached by simple models, and much of the reported progress past it was
measurement error.**

The reason that is good news arrives in §4. First, the errors, because they are
instructive.

---

## 2. The nulls, given their own space

Deep knowledge tracing announced itself in 2015 with **AUC 0.86 for DKT against
0.67 for BKT** on ASSISTments 2009-2010. Xiong, Zhao, Van Inwegen & Beck (EDM 2016)
took the dataset apart and found **123,778 duplicated rows out of 525,535 — 23.6%**
(acknowledged by the ASSISTments team), **73,466 rows of scaffolding records** that
BKT and PFA excluded and DKT was fed, and multi-skill items decomposed by repeating
the same action log once per skill, so the network saw each answer and then saw it
again.

Quantified: merging multi-skill items to remove the repeats drops **DKT's average
AUC from 0.81 to 0.74** and r² from 0.30 to 0.18. Split the predictions and the
mechanism is naked — on the *repeated* data points DKT scores AUC 0.97; on the
*leading* records, 0.77. Their verdict: on the clean datasets, **PFA performs as
well as DKT.**

The rest of the replication record, compressed:

| Claim | What replication found |
|---|---|
| DKT's representational advantage | Give BKT recency, contextualised trials, inter-skill similarity and individual ability, and **BKT is indistinguishable from DKT** (Khajah et al. 2016) |
| Neural nets beat psychometrics | Standard, hierarchical and temporal **IRT matched or outperformed DKT across all datasets** (Wilson et al. 2016) |
| SAKT, AUC 0.85 on ASSISTments 2015 | **Observed 0.73.** "SAKT underperforms DKT on all datasets" (Gervet et al.) |
| DAS3H's time-window features (EDM 2019 best paper) | **No predictive power added**; the gain over PFA "is simply due to the addition of an item difficulty parameter" |
| Expert-designed knowledge-component models | **≤ +0.01 AUC on 7 of 9 datasets**; on 4 of 9 a skill-only model loses to an item-difficulty-only model |
| The DLKT literature since 2015 | pyKT (NeurIPS 2022): "wrong evaluation setting may cause **label leakage**"; improvements over the original DKT are "**minimal**" |
| Duolingo's Half-Life Regression (~136 citations) | Trained weights for **both** `right` and `wrong` are negative; >90% of predicted half-lives exceed 120 days; a **constant baseline beats it** on its own metric, and it ranks near the bottom of the independent Anki benchmark |

One more, because it is the one that should make anyone building personalisation
uncomfortable: in a five-year simulation, **Memrise's fixed 1→6→12→48→96→180-day
ladder comes within 2% of FSRS on learning efficiency.** A hard-coded ladder, no
personalisation at all.

And the deep-learning result that *does* survive is not an accuracy result. DKT
reaches near-peak accuracy on a new learner in about **10 interactions where good
logistic regression needs 60** — a 6× reduction in burn-in. That is a **cold-start**
win, and it is the honest thing to claim.

---

## 3. The null this section exists to state

Every number above is about prediction. Here is the one about persistence.

> **No study anywhere in this project's learner-modelling corpus — 88 sources —
> compares a system that remembers a learner across sessions, subjects and years
> against the same system starting fresh, on a human learning outcome.**

The closest adjacent facts make the gap sharper rather than softer:

- There is **no controlled evidence that switching scheduling algorithm improves
  any learning outcome.** There is good evidence that FSRS predicts recall better
  and, in simulation, buys the same knowledge for less time. Those are different
  claims and must not be merged.
- There are **no cross-subject transfer results.** Nobody has shown that knowing a
  learner's model in algebra improves the cold-start prior in chemistry, though the
  prior-knowledge literature says it should.
- There is **no public dataset of a single learner's traces across years and across
  subjects.** ASSISTments is one school year. KDD Cup 2010 is one course. EdNet is
  ~2 years of TOEIC prep. Duolingo's release is two weeks of vocabulary.

The one exception is instructive. The `anki-revlogs-10k` corpus contains up to ten
years per user, across whatever the user chose to make cards about — the closest
thing the world has to a decade-long, cross-subject, per-learner record. It exists
by accident, because Anki is a general-purpose tool that individuals own.

> **Learner-owned tools produce longitudinal data. Institution-owned tools produce
> annual data, because institutions are annual.**

That is the strongest empirical argument in this section, and it is an argument
about custody rather than about modelling.

A second, softer null. The open-learner-model and learning-analytics-dashboard
literature — four systematic reviews — converges on a methodological finding: these
systems overwhelmingly evaluate **perception** rather than learning; the grounding in
self-regulated learning theory is thin or post-hoc; and the most common design,
comparison against a peer average, targets *awareness*, the weakest link in the chain.
The field's own title for this is **"Awareness Is Not Enough."** Social-comparison
designs are additionally a documented demotivation risk.

And an under-appreciated compounding problem: the best knowledge-tracing models are
"severely biased on some datasets." **An open learner model inherits the calibration
debt of the model it opens**, and shows a learner a number with the authority of an
interface. Every OLM should publish reliability diagrams, not AUC.

---

## 4. The inversion: the ceiling is a privacy gift

Now the good news, and it is structural.

A 21-parameter memory model and a ~34-feature logistic regression sit at the
accuracy frontier for this task. Capacity is demonstrably not the bottleneck — a
503-parameter GRU ties an 8,869-parameter LSTM. The residual appears to be
aleatoric: individual review outcomes are close to irreducibly stochastic.

Which means the entire learner model runs on the learner's device. Privacy here
costs approximately zero accuracy.

That inverts the usual trade. Normally, keeping data local means accepting a weaker
model. Here, the strong model *is* small. The custodial architecture this section
argues for is not a sacrifice made for ethics; it is what the measurement record
permits at no cost.

Compare the alternatives honestly. Federated learning buys population priors
without pooling raw traces, but leaks through gradients and still needs a
coordinator. Differential privacy gives a formal guarantee and is a poor fit here:
cohorts are a class of twenty-five, traces are per-item and long, and *the useful
signal is the outlier* — this learner's specific misconception. A DP budget that
protects the student destroys the diagnostic. And the "just anonymise it" move is
settled: de-identifying the MITx/HarvardX dataset to a FERPA-defensible k-anonymity
standard **degraded the data enough to change the conclusions that could be drawn from
it.**

---

## 5. What to store: evidence, not posteriors

The single most important architectural idea in this literature comes from Judy
Kay's group and is almost entirely unexploited outside it. The Personis user-model
server stores per-component evidence lists with pluggable resolvers — the model
stores evidence, and interpretation happens at query time.

**A lifelong learner model should store evidence and resolve it on demand, not
store a fitted posterior.** Posteriors go stale. They embed the assumptions of
whichever model was current in 2019 and cannot be re-derived. Evidence can be
re-interpreted by a better model in 2035.

Three consequences follow, and each is a design commitment.

Misconceptions are first-class, not a subtype of "incorrect." In 1978, Brown &
Burton's BUGGY built a deep-structure model of a student's bugs that could explain
*why* a student was making a mistake, not merely identify it. Forty-eight years
later, the state of the art outputs a scalar probability that they will get the next
one right. **We replaced a theory of error with a number between 0 and 1.**

Modelling wrong belief beats modelling right belief for three reasons. It is
*actionable*: "72% mastery" implies "practise more," while "you are applying the
subtraction-borrows-from-the-larger-digit bug" implies a specific refutation. It is
*enumerable*: the Force Concept Inventory covers Newtonian mechanics with about
thirty items whose distractors each encode an identifiable Aristotelian or impetus
belief — and Hake's 6,542-student result separating interactive engagement
(g ≈ 0.48) from lecture (g ≈ 0.23) was possible only because the instrument
measured misconceptions rather than performance. And it *survives the model*: a
misconception label written in 2026 still means something in 2036; a BKT posterior
does not. The raw material exists — Eedi's diagnostic-question corpus is **over 20
million student answers** where the label is *which wrong belief*, not *wrong*. The
vocabulary is the missing work.

Everything decays, and the two literatures have never been joined. Every
knowledge-tracing model assumes knowledge is monotone or near-monotone within a
session. None models what a mastery estimate from 2023 is worth in 2026. The spaced
repetition literature has exactly that model — stability and retrievability — and
the knowledge tracing literature does not use it. **This is the most obvious
unexploited join in the field**, and it is why the schema below makes memory state a
mandatory layer: a mastery estimate without a decay model is a lie about the
present.

And prior knowledge is the variable that matters. Not style. If a system can
measure exactly one thing before instruction, it measures prior knowledge in the
domain of the next task — because the expertise reversal effect means the *sign* of
a treatment effect flips with it. Worked examples beat problem-solving for novices
and lose to it for experts. Kalyuga & Sweller showed you can get an actionable
expertise estimate in seconds with a first-step verification item rather than a full
diagnostic. Learning styles get no field, because the meshing hypothesis requires a
crossover interaction in a randomised design and does not get one, replicated again
in 2026 in primary-school students.

---

## 6. Custody is the design, and inBloom is the proof

inBloom was a Gates- and Carnegie-funded multi-state student data platform. It
collapsed in 2014, and **over 400 pieces of state-level student-data-privacy
legislation followed**; the field moved from a large-scale open-source multi-state
collaboration toward closed proprietary systems adopted piecemeal.

The lesson is precise: **inBloom failed not because centralised learner data is
technically hard but because it was centralised in an entity that was not the
learner.** Every property people objected to — indefinite retention, third-party
access, no meaningful consent, no deletion — is a property of *custody*, not of
*schema*.

The empirical record since has not improved. Human Rights Watch analysed **163
EdTech products across 49 countries: 145 of 163 (89%)** engaged in data
practices that risked, undermined, or infringed children's rights, sending or
granting access to children's data to **196 third-party companies**, overwhelmingly
ad-tech. **39 of 42 governments** that built their own EdTech built systems with the
same problem.

The legal floor has holes worth knowing. FERPA's school-official exception was
widened by rulemaking to cover contractors, directory information may be disclosed
without consent unless opted out, and there is no private right of action —
enforcement runs through a funding-withdrawal power that has never been exercised.

Two provisions cut the other way and should be treated as design requirements rather
than compliance costs. GDPR Art. 17 (erasure) and Art. 20 (portability) point at the
same architecture: the learner can export everything, and nobody else can read
anything without a scoped grant. And the EU AI Act, Annex III point 3(b), makes
high-risk any system "intended to be used to evaluate learning outcomes, **including
when those outcomes are used to steer the learning process**." Read that carefully:
**a knowledge-tracing model that decides what the learner sees next is explicitly a
high-risk AI system under EU law.** Art. 5(1)(f) separately prohibits emotion
inference in education, which is why the schema has no affect field.

*A verification caveat this project owes its readers: the 2025 COPPA amendments and
the EU AI Act applicability dates were not reachable from primary sources during the
research session and are flagged `UNVERIFIED-IN-SESSION`. They must be re-verified
against the Federal Register and the Official Journal before publication.*

---

## 7. The Portable Learner Model, in brief

Nobody has built this. What exists is either a *credential* format recording
outcomes (Open Badges 3.0, CLR 2.0, W3C VC 2.0), or an *activity stream* format
recording events (xAPI / IEEE 9274.1.1, Caliper), or a proprietary per-vendor
posterior that dies with the vendor.

> **We have standards for what a learner was awarded and what a learner did, and no
> standard for what a learner knows.**

Seven layers: **L0** identity (a DID the learner controls, pairwise per-provider
pseudonyms, and a guardianship record with an automatic transition date). **L1** a
domain map anchored to public identifiers, never a vendor's internal skill ids.
**L2** an append-only evidence log — the only primary data — where every response
record carries the chosen distractor, because that is the diagnostic bit. **L3**
memory state per knowledge component, borrowed wholesale from the spaced-repetition
literature. **L4** belief state with knowledge *and* misconceptions as co-equal
sections, every estimate carrying an uncertainty interval, a calibration reference,
and a `learner_annotation` field so a learner can say *"I only missed those because I
misread the sign."* **L5** instructional priors, deliberately short — expertise
level, guidance policy, accommodations, and no learning-style field. **L6**
governance, co-equal with the data: grants with mandatory expiry, default-deny onward
transfer, a learner-readable access log, and erasure receipts.

Nine conformance guarantees, of which four carry most of the weight:
recomputability (every derived number regenerates from L2 alone, given the
recorded model id and parameter hash); decay-awareness (no knowledge claim is
served without a retrievability adjustment); error symmetry (misconceptions are
queryable exactly as knowledge is); and contestability (the learner can dispute
any estimate, and the dispute travels with it).

Three problems remain genuinely unsolved and are stated as such. KC alignment:
portability requires a shared domain map and the evidence says our domain maps are
bad — the binding constraint on the whole proposal. The misconception vocabulary:
the FCI's thirty items encode decades of physics-education interviews and nothing
comparable exists for most of the curriculum. Verification: a learner-owned
record the learner can forge is worthless for high stakes, but a record only
institutions can write is not learner-owned. The likely resolution — self-attested
and issuer-attested evidence coexisting with different confidence values and
different downstream permissions — is a proposal, not a solution.

---

## 8. The strongest counter-argument

*If simple models are already at the ceiling, and persistence has never been shown
to help, why build the archivist at all? Keep the session, throw it away, and ship.*

The answer is that **the claim for persistence is not an accuracy claim, and AUC
does not measure anything this section wants.** It does not measure whether a
learner's misconception from March is still active in September. It does not measure
whether a tutor in chemistry can start from what the learner already proved in
algebra. It does not measure whether a parent can trace a disputed number back to
the evidence that produced it, or whether a family can compel deletion and get a
receipt.

But the counter-argument lands hard on one point, and this section concedes it: the
value of persistence is currently a design hypothesis, not a finding. It should
be labelled that way everywhere, including by us. And it is testable, cheaply: the
cold-start result gives a ready-made design — measure whether a warm prior from
another subject reduces burn-in the way a within-subject history does. That is one
experiment, and no one has run it.

---

## 9. What this section commits us to

- **Store evidence, resolve on demand.** Never store a posterior as primary data.
  Every derived number carries the model id and version that produced it and
  regenerates from the evidence log alone.
- **Misconceptions are first-class.** The chosen distractor is recorded, always. A
  theory of error beats a number between 0 and 1.
- **Every knowledge claim carries a decay model.** A mastery estimate without one is
  a lie about the present.
- **The model runs on the learner's device**, because a 21-parameter memory model and
  a 34-feature logistic regression are the frontier. Privacy costs approximately zero
  accuracy here.
- **Custody sits with the learner.** Scoped, expiring, revocable, default-deny onward
  transfer, with a learner-readable access log and erasure receipts. inBloom failed on
  custody, not schema.
- **Any estimate shown to a human publishes its calibration.** No reliability diagram,
  no number.
- **No learning-style field. No personality field. No affect inference.** Measure prior
  knowledge with a first-step verification item instead.
- **Label persistence as an unmeasured hypothesis** until someone runs the stateless
  baseline — and run it ourselves.

Mr. Ranedeer's author built a prerequisite ladder, a transfer-graded test, executable
verification of every problem before posing it, and a hidden learner model — in a
prompt, in 2023, before most of the funded products in this space existed. Then the
platform moved and all of it became probabilistic. **The mechanisms were not the
weak part. The place to put them was.**

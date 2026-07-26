---
title: "Scientific remembering and adaptive retrieval at the July 2026 frontier"
wave: F
section: F11
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 21
---

# F11 — Scientific Remembering and Adaptive Retrieval

## Executive finding

Understanding does not automatically persist. A world-class explanation can be
fully understood today and unavailable when a learner needs it next month.

The scientific-remembering primitive is therefore:

> **Select durable targets, encode them into a connected model, require effortful
> retrieval, repair quickly, vary the retrieval form, and schedule the next
> encounter from observed memory—not a fixed calendar.**

FSRS‑6 is the July 2026 open scheduling substrate to beat. It models each item’s
difficulty, stability, and retrievability, uses 21 fitted parameters, incorporates
all reviews, and lets a learner choose a target recall probability that trades
workload against retention. `OBSERVED`

But a scheduler answers only **when**. The AI mentor must also decide:

- what deserves durable memory;
- what the memory unit is;
- how the learner should retrieve it;
- when to use a mnemonic;
- when to vary context;
- when recall is insufficient without application or transfer;
- when an item should merge, split, or retire.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized or within-participant learner comparison |
| `MEASURED-BENCH` | Dataset, scheduler, or deployed-system evaluation |
| `OBSERVED` | Inspectable open implementation or current documentation |
| `INFERENCE` | Design implication from the evidence |

## 1. The current scheduling frontier

### 1.1 FSRS‑6

The current [FSRS technical overview](https://github.com/open-spaced-repetition/fsrs4anki/wiki/ABC-of-FSRS)
defines:

- **Retrievability (R):** estimated probability of successful recall now;
- **Stability (S):** time for retrievability to fall from 100% to 90%;
- **Difficulty (D):** resistance to stability growth after a review.

FSRS‑6 uses 21 parameters, learns from a person’s review history when sufficient,
and otherwise uses defaults fit on several hundred million reviews from roughly
10,000 users. The project says it uses all reviews, including same-day reviews,
unlike earlier versions. `OBSERVED`; project-reported benchmark provenance.

FSRS is:

- open source under the [FSRS4Anki repository](https://github.com/open-spaced-repetition/fsrs4anki);
- integrated into current [Anki](https://github.com/ankitects/anki/releases);
- available through multiple-language implementations maintained by
  [Open Spaced Repetition](https://github.com/open-spaced-repetition);
- evaluated through an open
  [scheduler benchmark](https://github.com/open-spaced-repetition/srs-benchmark).

The underlying optimization line includes a 2022 KDD
[stochastic-shortest-path scheduler](https://doi.org/10.1145/3534678.3539081)
and a 2023 IEEE
[memory-dynamics framework](https://doi.org/10.1109/TKDE.2023.3251721).
The latter reports a 220-million-row dataset and reductions of 64% in recall
prediction error and 17% in scheduling cost against its selected baselines.
`MEASURED-BENCH`

### 1.2 Desired retention is a learner choice

The FSRS documentation treats desired retention as a control over the workload–
recall trade. The current practical range is approximately 70–97%, with higher
targets requiring more reviews. `OBSERVED`

For a universal mentor, target retention depends on use:

| Memory | Example | Scheduling policy |
|---|---|---|
| Safety-critical | medication contraindication, electrical procedure | high retention + simulation + human standard |
| Generative foundation | number facts, syntax, vocabulary, anatomy | high enough for fluent reasoning |
| Navigational | recognize a theorem and know where to retrieve it | moderate retention + source access |
| Temporary project state | a short-lived API detail | low retention or externalize |
| Personally meaningful | name, story, commitment | learner-controlled, context-sensitive |

Not everything belongs in biological memory. Expertise includes knowing what to
retrieve from tools.

## 2. Recent real-world evidence

### 2.1 Practice spread across days

[Counting Days](https://doi.org/10.1038/s41539-025-00322-5) tested a simple
incentive that rewarded the number of days students practiced instead of the
number of questions completed. It used two RCTs—143 students within a course and
71 instructors—and was designed to increase spacing and retrieval practice.
`MEASURED-RCT`

The architectural lesson is positive: the mentor can make a powerful memory
intervention through tiny scheduling and incentive choices rather than demanding
more total study time.

### 2.2 Authentic retrieval forms

- A 2025 primary-school study found
  [retrieval practice improved learning in real classrooms](https://pubmed.ncbi.nlm.nih.gov/40861368/)
  in both distributed and nondistributed conditions. `MEASURED-RCT`
- A 2026 stratified RCT compared
  [re-solving virtual patients, MCQs, and short answers](https://pubmed.ncbi.nlm.nih.gov/41503782/)
  for medical-student long-term retention. `MEASURED-RCT`
- A 2026 within-participant evaluation found
  [spaced histopathology cases](https://pubmed.ncbi.nlm.nih.gov/42130248/)
  improved diagnostic scores by 1.9 points on a ten-point measure and reduced
  median case time by 1.4 minutes among 42 participants. `MEASURED-RCT`
- A 2026 medical-education
  [systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/41601436/)
  evaluates spaced repetition across the field. `MEASURED-BENCH`
- A 2025
  [mathematics meta-analysis](https://aidanhorner.org/papers/Murrayetal_EdPsychReview_2025.pdf)
  focuses specifically on spacing and retrieval for mathematics learning.
  `MEASURED-BENCH`

`INFERENCE`: a review does not need to be a flashcard. It can be a diagnosis,
worked derivation, oral explanation, reconstruction, physical procedure, code
repair, or application.

### 2.3 Retrieval can be scaffolded without becoming restudy

A 2026 study of
[diminishing-cues retrieval](https://pubmed.ncbi.nlm.nih.gov/42322471/)
compares gradually reduced cues against standard retrieval and restudy for
difficult English–Chinese vocabulary. `MEASURED-RCT`

The mentor can therefore preserve retrieval effort while preventing an
unproductive dead end:

```text
free recall
  → structural cue
  → first step
  → contrasting example
  → partial answer
  → full feedback
```

The schedule records the cue level, not merely “correct/incorrect.”

## 3. The memory object

A flashcard front/back pair is one possible interface. The durable object is a
**memory contract**:

```yaml
target:
  id: newtons-second-law
  kind: relationship
  durable_claim: "net force equals rate of change of momentum"
  conditions: ["inertial frame"]
  connections: [momentum, mass, acceleration, vectors]
retrieval_forms:
  - explain
  - draw_free_body_diagram
  - solve
  - diagnose_error
  - predict_motion
  - transfer_to_variable_mass_case
cues:
  ladder: [none, structure, first_step, contrast, answer]
evidence:
  accuracy: ...
  latency: ...
  cue_level: ...
  representation: ...
  transfer_distance: ...
state:
  difficulty: ...
  stability: ...
  retrievability: ...
```

### Memory kinds

| Kind | Retrieval form |
|---|---|
| Fact | free recall in context |
| Vocabulary | produce, recognize, use, distinguish |
| Relationship | reconstruct graph/equation and explain direction |
| Procedure | perform steps with faded support |
| Perceptual pattern | classify and justify from varied exemplars |
| Motor skill | demonstrate, sense, and correct |
| Concept | generate examples/nonexamples and transfer |
| Source location | find and evaluate the authoritative artifact |
| Personal commitment | recall in the situation where action matters |

The scheduler maintains separate evidence by form. Recognizing a word is not the
same memory as producing it in speech.

## 4. The memory-compounding loop

### Step 1 — Select

Ask whether the target should be:

- memorized for fluent use;
- understood and regenerated from first principles;
- indexed for external retrieval;
- practiced as a skill;
- discarded when the project ends.

### Step 2 — Encode meaningfully

Before scheduling recall, connect the target to:

- a causal model;
- prior knowledge;
- an example and nonexample;
- a sensory or spatial cue where useful;
- a personally meaningful use;
- an executable artifact.

The 2025
[method-of-loci systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/40457944/)
supports immediate and sustained recall benefits across a large literature.
`MEASURED-BENCH`

Mnemonics are encoding tools. They are valuable for arbitrary mappings, ordered
lists, and initially weak cues; they do not replace understanding or transfer.

### Step 3 — Retrieve before exposure

The learner attempts recall, reconstruction, or performance before seeing the
answer. The mentor captures:

- correctness and partial correctness;
- latency;
- confidence;
- cue level;
- error type;
- representation and context;
- emotional cost when volunteered.

### Step 4 — Repair with grounded feedback

Feedback arrives quickly enough to prevent an error from becoming the remembered
answer. It explains the misconception, reconnects to the model, and produces a
new cue only when necessary.

### Step 5 — Vary and transfer

Success in one format schedules a different form:

```text
recognize → produce → explain → apply → transfer → teach
```

This prevents the scheduler from optimizing repeated familiarity with one card.

### Step 6 — Space adaptively

Update the memory state and schedule the least costly future retrieval consistent
with the target retention and use. Batch reviews into humane sessions, honor
deadlines, and smooth workload.

### Step 7 — Integrate, merge, and retire

As knowledge grows:

- merge atomized items into chunks;
- replace memorized outputs with generative rules;
- retain boundary cases;
- suspend obsolete details;
- preserve provenance;
- schedule a far-transfer or creation task instead of another identical prompt.

## 5. Remembering and reasoning are separate, connected loops

Pure recall can produce inert knowledge. Pure explanation can produce insight
that disappears.

The mentor runs both:

```text
retention loop: retrieve → repair → space
reasoning loop: model → vary → apply → transfer
```

Every important concept eventually crosses between them:

- facts become inputs to reasoning;
- reasoning produces compressed, memorable structure;
- retrieval reveals which parts of the model remain available;
- transfer decides whether recall supports capability.

The 2011
[retrieval-practice experiment](https://pubmed.ncbi.nlm.nih.gov/21252317/)
found more learning from retrieval than elaborative concept mapping in its
studied science-text conditions. This does not make elaboration unnecessary; it
shows that a beautiful concept map is not a substitute for later retrieval.
`MEASURED-RCT`

## 6. AI-native memory policy

The AI mentor can do what a static deck cannot:

1. derive memory targets from the learner’s actual goals and work;
2. generate multiple valid retrieval forms;
3. detect whether an answer was recalled, derived, guessed, or externally found;
4. explain an error in context;
5. preserve a concept across languages and modalities;
6. reschedule from detailed evidence;
7. reconnect a due item to the current project;
8. ask for transfer when simple recall saturates;
9. help the learner delete low-value memory obligations.

[IntelliCode](https://aclanthology.org/2026.eacl-demo.10/) demonstrates a 2026
agent architecture in which learner profiling, assessment, curriculum selection,
graduated hints, spaced repetition, and engagement monitoring transform one
shared state under a single-writer policy. `OBSERVED`

[TASA](https://arxiv.org/abs/2511.15163) explicitly combines persona, memory, and
forgetting dynamics for mathematics tutoring. `MEASURED-BENCH`

[Planning-Guided Tutoring with Assessment-Driven Memory](https://aclanthology.org/2026.acl-long.325.pdf)
adds an assessment-driven tutoring memory to real-time pedagogical planning.
`MEASURED-BENCH`

These are early systems, but they show the primitive moving into complete tutors.

## 7. Universal-access consequences

- Scheduling and the learner’s memory state run locally.
- Reviews are tiny, cacheable objects that work offline and sync as event logs.
- Speech permits retrieval without literacy or typing barriers.
- A shared device can protect separate encrypted learner states.
- Local examples and languages change the cue surface, not the durable claim.
- Teachers can assign community practice and see aggregate due-load, never a
  permanent intelligence ranking.
- Target retention adapts to workload realities; missed days trigger
  rescheduling, not punishment.
- A print packet can carry QR-less identifiers and sync later through a teacher
  or community hub.

## 8. Acceptance tests

- [ ] Every target declares why it deserves biological memory.
- [ ] Memory kind and required retrieval forms are explicit.
- [ ] First exposure builds meaning before scheduling repetition.
- [ ] Retrieval precedes answer exposure.
- [ ] Cue level, latency, error type, and context are recorded.
- [ ] Feedback is source-grounded and repairs the model.
- [ ] Success varies form and eventually tests transfer.
- [ ] Scheduler parameters and desired retention are inspectable.
- [ ] Missed reviews reschedule without shame, loss, or streak punishment.
- [ ] Items merge, split, suspend, and retire as expertise changes.
- [ ] Learners can export/delete schedules and correct evidence.
- [ ] Offline review and delayed sync preserve full event provenance.

## Source index

1. FSRS‑6 overview — [ABC of FSRS](https://github.com/open-spaced-repetition/fsrs4anki/wiki/ABC-of-FSRS)
2. FSRS4Anki — [source](https://github.com/open-spaced-repetition/fsrs4anki)
3. Open Spaced Repetition — [implementations](https://github.com/open-spaced-repetition)
4. SRS Benchmark — [source](https://github.com/open-spaced-repetition/srs-benchmark)
5. Current Anki releases — [GitHub](https://github.com/ankitects/anki/releases)
6. Stochastic shortest-path scheduling — [KDD 2022](https://doi.org/10.1145/3534678.3539081)
7. Memory-dynamics scheduling — [IEEE TKDE 2023](https://doi.org/10.1109/TKDE.2023.3251721)
8. Counting Days — [npj Science of Learning 2025](https://doi.org/10.1038/s41539-025-00322-5)
9. Primary-school retrieval — [2025](https://pubmed.ncbi.nlm.nih.gov/40861368/)
10. Virtual-patient retrieval RCT — [2026](https://pubmed.ncbi.nlm.nih.gov/41503782/)
11. Histopathology spaced practice — [2026](https://pubmed.ncbi.nlm.nih.gov/42130248/)
12. Medical spaced-repetition meta-analysis — [2026](https://pubmed.ncbi.nlm.nih.gov/41601436/)
13. Mathematics spacing/retrieval meta-analysis — [2025](https://aidanhorner.org/papers/Murrayetal_EdPsychReview_2025.pdf)
14. Diminishing-cues retrieval — [2026](https://pubmed.ncbi.nlm.nih.gov/42322471/)
15. Method-of-loci meta-analysis — [2025](https://pubmed.ncbi.nlm.nih.gov/40457944/)
16. IntelliCode — [EACL 2026](https://aclanthology.org/2026.eacl-demo.10/)
17. TASA — [arXiv:2511.15163](https://arxiv.org/abs/2511.15163)
18. Planning-guided tutoring memory — [ACL 2026](https://aclanthology.org/2026.acl-long.325.pdf)
19. Retrieval vs concept mapping — [Science 2011](https://pubmed.ncbi.nlm.nih.gov/21252317/)
20. Test-enhanced learning — [Psychological Science 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)
21. Spacing meta-analysis — [Psychological Bulletin 2006](https://doi.org/10.1037/0033-2909.132.3.354)

## Decision

**Adopt FSRS‑6 as an open scheduling baseline, then build the larger memory
compiler around it.** Schedule concepts, relationships, procedures, perceptual
patterns, and transfer—not only cards. Make retention a learner-controlled
service that quietly compounds capability across years.

---
title: "Learner-owned state at the July 2026 frontier"
wave: C/F
sections: [C3, F5]
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 22
supersedes: "research/raw/F5-learner-model.md"
---

# C3/F5 — The Learner-Owned State

## Executive finding

The learner model has become the continuity layer of the universal mentor.

Frontier agents can now maintain multi-resolution memory, reason over long
interaction histories, update learner profiles, generate difficulty-calibrated
questions, and coordinate specialists around shared state. July 2026 work
connects conversational knowledge tracing, explicit question difficulty,
curriculum-grounded retrieval, agent memory benchmarks, and open educational
data standards. `MEASURED-BENCH`; `STANDARD`

The correct architecture is not a hidden score predicting whether a child will
answer the next question correctly. It is a **learner-owned evidence ledger**
from which transparent, uncertain, expiring hypotheses are recomputed.

It separates:

1. **observations** — what the learner said, did, built, recalled, or corrected;
2. **estimates** — current hypotheses about mastery, misconceptions, retention,
   transfer, confidence, language, and access;
3. **decisions** — the proposed next teaching action and why it was chosen;
4. **authority** — what learners, teachers, and families can inspect, contest,
   share, export, and delete.

The frontier claim is:

> A child should be able to carry a rich, trustworthy learning history from a
> shared village phone to a school server to a frontier mentor—without any
> vendor owning the authoritative copy and without any estimate becoming a
> permanent label.

This refreshed report supersedes the earlier F5 draft, which over-centered
prediction ceilings and null-result rhetoric. Predictive accuracy remains a
component metric; the design center is now continuity, evidence, agency, and the
quality of the teaching decisions state enables.

---

## 1. What changed by July 2026

### 1.1 Dialogue itself became diagnostic evidence

Knowledge tracing traditionally consumed a sequence of item IDs and binary
responses. A spoken or written mentor conversation now exposes richer evidence:

- the learner’s explanation;
- intermediate steps and revisions;
- the location and type of an error;
- latency and hint use;
- which representation resolved confusion;
- whether the idea transfers to a fresh context;
- self-reported confidence and goals.

[Interpretable Difficulty-Aware Knowledge Tracing in Tutor-Student
Dialogues](https://arxiv.org/abs/2605.01097) explicitly models both learner
ability and the difficulty of the tutor’s next task, mapping LLM outputs into
interpretable item-response parameters. It outperformed the reported dialogue-KT
baselines on two datasets while producing cognitively interpretable estimates.
`MEASURED-BENCH`

The important shift is from “predict the next click” to “choose the next probe
that reduces uncertainty and helps the learner.”

### 1.2 Memory became a shared agent substrate

[DeepTutor](https://arxiv.org/abs/2604.26962) uses dynamic multi-resolution
memory to distill interaction history into an evolving learner profile shared
across grounded solving, question generation, writing, research, and proactive
tutor skills. [IntelliCode](https://arxiv.org/abs/2512.18669) demonstrates a
multi-agent tutor with centralized learner modeling, mastery updates, and
personalized review intervals. `MEASURED-BENCH`

This supports one state ledger behind many specialists. The language mentor,
subject expert, practice coach, and teacher cockpit should not each maintain a
contradictory private profile.

### 1.3 Agent memory became independently evaluable

[MemoryAgentBench](https://mlanthology.org/iclr/2026/hu2026iclr-evaluating/)
evaluates long-term agent memory through incremental multi-turn interactions.
The benchmark separates retrieval, updating, and use rather than treating the
presence of a long context window as memory. `MEASURED-BENCH`

For education, the unit test is stricter: can the system preserve the right
learner fact, update it when new evidence arrives, forget or expire it when
appropriate, and cite the event that justifies using it?

### 1.4 Learner-state-aware tutoring can improve expert-rated pedagogy

A July 2026 peer-reviewed comparison held the foundation model constant and
compared a prompt-only algebra tutor with a curated, learner-state-aware
pedagogical RAG workflow. Across 24 two-turn episodes and eight expert reviewers,
the integrated condition received higher ratings for conceptual support,
instructional quality, and helpfulness (composite **4.65 vs 4.33**, Wilcoxon
`p=.00024`, rank-biserial `r=.86`). It measured expert ratings, not learner
outcomes. `MEASURED-BENCH`

Source: [Frontiers in Education, July 2026](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1896839/abstract)

The design implication is positive and specific: learner state adds value when
it is combined with a bounded teaching policy and curated knowledge—not when it
is merely pasted into a prompt.

---

## 2. The state is a hypothesis graph, not a report card

For each curriculum goal, the mentor should represent several dimensions:

| Dimension | Example state | Evidence |
|---|---|---|
| Concept | understands proportional equivalence | explanation plus varied problems |
| Representation | strong with tables, emerging with equations | cross-representation probes |
| Procedure | executes cross-multiplication accurately | worked steps |
| Misconception | may treat additive and multiplicative change alike | error cluster and diagnostic distractor |
| Retention | likely retrievable for seven days | spaced retrieval history |
| Transfer | applies ratio reasoning to maps but not mixtures | novel contexts |
| Independence | succeeds after one cue; full scaffold no longer needed | hint/fading trace |
| Confidence | self-rating aligned or misaligned with performance | self-report plus outcome |
| Language | prefers spoken Tamil for concepts, English notation | explicit preference and successful use |
| Access | needs low-reading-load, high-contrast presentation | learner/teacher preference |

Each cell stores:

- current estimate;
- confidence or interval;
- supporting event IDs;
- model and parameter version;
- last updated time;
- decay or expiry rule;
- next discriminating probe;
- learner or teacher annotation.

No estimate is served without its evidence and uncertainty.

---

## 3. Four stores, kept deliberately separate

### 3.1 Event ledger

An append-only local-first stream:

```yaml
event_id: evt_...
time: 2026-07-25T14:04:31-07:00
actor: learner_...
goal: case:...
task: task_...
modality: speech
observation:
  transcript_ref: local://...
  claim: "A ratio stays equal when both sides use the same multiplier."
  assistance: one_targeted_question
grounding:
  claim_records: [clm_...]
consent_scope: learner_and_current_teacher
```

Events are observations, not verdicts. They remain stable so any later model can
recompute state.

### 3.2 Derived learner state

Recomputable hypotheses linked to events:

```yaml
estimate_id: est_...
goal: case:...
dimension: transfer
value: emerging
confidence: 0.67
evidence_for: [evt_a, evt_b]
evidence_against: [evt_c]
model: transfer-rubric-v3
updated_at: ...
expires_or_decays_at: ...
next_probe: "novel mixture problem without table"
learner_annotation: "I understood the ratio; the units confused me."
```

The learner annotation travels with the estimate. It may change the next probe
without rewriting the original event.

### 3.3 Curriculum and misconception graph

The state references stable competency identifiers, prerequisites,
representations, common misconceptions, and transfer contexts. [1EdTech CASE
1.1](https://standards.1edtech.org/case/) already provides machine-readable
competency frameworks, associations, rubrics, and identifiers. `STANDARD`

This lets a state move between systems without mapping “fractions-7” by string
guessing.

### 3.4 Teaching-decision log

The router records:

- alternatives considered;
- selected teaching mode;
- evidence used;
- expected learning signal;
- stopping or pivot rule;
- outcome and human override.

This is how the system learns which actions work for this learner without
inventing a fixed “learning style.”

---

## 4. State resolution across time

The mentor needs four memory horizons:

| Horizon | Contents | Typical lifetime |
|---|---|---|
| Turn | current problem, visible work, immediate error | minutes |
| Session | active goal, successful explanation, unresolved question | hours to days |
| Course | concept graph, misconceptions, transfer, review schedule | months |
| Lifelong | learner-owned goals, achievements, portfolios, access preferences | years, explicitly permissioned |

Compression must preserve provenance. A session summary does not replace events;
it points to them. A course-level estimate can be recomputed when the tracing
model improves. A lifelong record stores achievements and learner-chosen
continuity, not every private conversation.

The [Comprehensive Learner Record 2.0](https://standards.1edtech.org/clr/)
provides a current standard for verifiable learning experiences and
achievements. CASE identifies the competency; the learner ledger contains the
evidence and estimates; CLR packages achievements a learner chooses to carry.
`STANDARD`

---

## 5. Retention is one dimension, not the whole model

The open [SRS benchmark](https://github.com/open-spaced-repetition/srs-benchmark)
currently evaluates approximately **349.9 million** filtered reviews from 9,999
Anki collections. It includes FSRS-7 and large sequence models, with disclosed
time-split evaluation. `MEASURED-BENCH`

That scale makes retention scheduling one of the most empirically instrumented
parts of learner state. The mentor should store retrievability and stability for
facts and procedures that benefit from scheduled recall.

But recall is not transfer. The same goal may be:

- remembered;
- poorly explained;
- successfully applied in a familiar form;
- not yet transferable to a new context.

F11 owns the scheduling mechanism. C3/F5 ensures that retention evidence sits
beside conceptual, representational, and transfer evidence.

---

## 6. Misconceptions become actionable hypotheses

A wrong answer is not merely “mastery = 0.” It can distinguish:

- a calculation slip;
- a language misunderstanding;
- a missing prerequisite;
- a stable alternative conception;
- correct reasoning with an incorrect unit;
- a correct concept applied outside its conditions.

The state stores a misconception **hypothesis**, evidence for and against it,
and the cheapest discriminating probe. The mentor can then choose a contrast
case, counterexample, visual model, worked example, or teacher escalation.

[A New Domain-Informed Learner Model with Uncertainty-Aware Knowledge Mastery
Propagation](https://educationaldatamining.org/edm2026/proceedings/2026.EDM.full-papers.153/index.html)
is part of a 2026 movement toward explicit domain structure and uncertainty
rather than opaque scalar mastery. `MEASURED-BENCH`

The universal mentor should publish calibration: when it says 70% confident,
that confidence should mean something across goals and learner groups.

---

## 7. Cold start becomes a useful first conversation

The system does not need months of surveillance before it can help.

An initial ten-minute loop can gather:

1. learner-selected goal and urgency;
2. local curriculum or project context;
3. one broad diagnostic task;
4. a think-aloud or spoken explanation;
5. one prerequisite probe;
6. language and access preferences;
7. a first teach-practice-transfer cycle.

The output is a sparse state with wide uncertainty, not a personality profile.
The mentor immediately begins helping and tightens estimates through normal
learning.

Prior school records, if the learner chooses to import them, are evidence—not
ground truth. A quick fresh probe can reveal what is usable today.

---

## 8. Learner custody and open standards

The authoritative record belongs to the learner, with age-appropriate guardian
and school roles.

Interoperability uses existing standards where they fit:

| Need | Standard or mechanism |
|---|---|
| Competency graph | [CASE 1.1](https://standards.1edtech.org/case/) |
| Learning events | [Caliper Analytics](https://standards.1edtech.org/caliper/) or xAPI profiles |
| Achievements | [CLR 2.0](https://standards.1edtech.org/clr/) |
| Classes and official results | [OneRoster 1.2](https://standards.1edtech.org/oneroster/) |
| Provenance | [W3C PROV-O](https://www.w3.org/TR/prov-o/) |
| Local format | signed JSON/SQLite bundle with content-addressed attachments |

The portable bundle contains:

- raw events selected for export;
- derived estimates plus model metadata;
- competency identifiers;
- achievements and projects;
- annotations and disputes;
- permission grants with expiry;
- erasure and synchronization receipts.

A receiving system can use the estimates immediately or recompute them from
events. No provider-specific embedding is the only representation of the child.

---

## 9. Privacy through architecture, not policy text

### Data minimization

Record what improves a learning decision. Do not infer protected or intimate
traits because a model can.

### Separate identity from learning evidence

Use pairwise identifiers and local key mapping. A regional research dataset does
not need the learner’s civil identity.

### Scoped views

A subject agent sees the minimum relevant state. A teacher sees learning
evidence for their class. A parent or guardian receives an age-appropriate
overview. A research export contains only consented fields.

### Finite retention

Turn transcripts can expire quickly. Derived estimates can persist while their
raw sensitive inputs are deleted where policy permits. Achievements the learner
chooses to preserve may last.

### Contestability

The learner can say “that estimate is wrong,” attach context, request a fresh
probe, and see who used it.

### Majority transition

Guardian permissions automatically transition to the learner at the relevant
age. The architecture does not leave childhood data under perpetual adult or
vendor control.

These are implementation requirements of the L4 human-authorization boundary,
not reasons to abandon personalization.

---

## 10. Offline synchronization

The authoritative state can live on the learner device or trusted school node:

- new events receive device-scoped IDs;
- append-only events merge without destructive conflict;
- estimates recompute after merge;
- competing human annotations coexist until resolved;
- large media remains local unless explicitly shared;
- curriculum identifiers map through signed CASE bundles;
- permissions travel with every exported field;
- sync receipts show what moved.

A shared device keeps encrypted learner partitions and rapid profile switching.
If no personal device exists, a printed or spoken learner code plus local
guardian recovery can preserve continuity.

The system may use a frontier cloud model one day and a local small model the
next. The learning history remains the same.

---

## 11. The teaching router

State exists to improve action. For each candidate next step, the router asks:

1. What goal does the learner care about?
2. What prerequisite is most uncertain?
3. Which misconception hypothesis is worth testing?
4. Which representation has and has not worked?
5. Is this a learning moment, a review moment, or a transfer moment?
6. How much scaffold is currently necessary?
7. Which language and modality fit the situation?
8. What evidence would show the action worked?
9. When should the system pivot or call a person?

The decision log makes the policy inspectable. Teachers can edit the goal,
reject a hypothesis, or choose a group activity. The learner can choose among
several valid next steps.

---

## 12. Acceptance tests

The learner-state architecture passes when:

1. observations never silently become facts about ability;
2. every estimate names evidence, uncertainty, model version, and expiry;
3. events can recompute state under a new model;
4. mastery is multidimensional, including retention and transfer;
5. misconception hypotheses include a discriminating next probe;
6. one shared state serves all mentor specialists;
7. the teaching router explains its action;
8. learners and trusted adults can inspect and correct state;
9. corrections do not erase provenance;
10. a standards-based export works across two independent implementations;
11. the core ledger and routing loop work offline;
12. shared-device identities remain isolated;
13. permissions are scoped and expire;
14. distributional calibration is reported by language and learner group;
15. use of state improves delayed unaided learning, not only expert-rated text;
16. a learner can leave the provider with their usable history.

---

## Conclusion

The learner model is no longer a score hidden inside one tutor. It is the shared,
portable memory of an expert mentor mesh.

Built correctly, it makes personalization cumulative:

- each explanation teaches the learner and the mentor;
- each error becomes a testable hypothesis;
- each successful representation becomes reusable;
- each retrieval updates a retention plan;
- each project adds transfer evidence;
- each teacher correction improves the next decision;
- each year begins with continuity rather than a blank slate.

The child owns that continuity. Models and institutions compete to serve it.

---

## Source index

1. [Interpretable difficulty-aware conversational knowledge tracing](https://arxiv.org/abs/2605.01097)
2. [DeepTutor](https://arxiv.org/abs/2604.26962)
3. [MemoryAgentBench](https://mlanthology.org/iclr/2026/hu2026iclr-evaluating/)
4. [Learner-state-aware pedagogical RAG](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2026.1896839/abstract)
5. [IntelliCode centralized learner modeling](https://arxiv.org/abs/2512.18669)
6. [TASA memory- and forgetting-aware tutoring](https://arxiv.org/abs/2511.15163)
7. [EDM 2026 uncertainty-aware learner model](https://educationaldatamining.org/edm2026/proceedings/2026.EDM.full-papers.153/index.html)
8. [Open spaced-repetition benchmark](https://github.com/open-spaced-repetition/srs-benchmark)
9. [FSRS reference implementation](https://github.com/open-spaced-repetition/fsrs4anki)
10. [CASE 1.1](https://standards.1edtech.org/case/)
11. [Caliper Analytics](https://standards.1edtech.org/caliper/)
12. [Comprehensive Learner Record 2.0](https://standards.1edtech.org/clr/)
13. [OneRoster 1.2](https://standards.1edtech.org/oneroster/)
14. [W3C PROV-O](https://www.w3.org/TR/prov-o/)
15. [xAPI specification](https://github.com/adlnet/xAPI-Spec)
16. [OECD Digital Education Outlook 2026](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/01/oecd-digital-education-outlook-2026_940e0dd8/062a7394-en.pdf)
17. [DeepTutor TutorBench](https://arxiv.org/abs/2604.26962)
18. [EduAgentBench](https://arxiv.org/abs/2605.14322)
19. [FATE evaluator](https://arxiv.org/abs/2607.10647)
20. [CSTutorBench](https://arxiv.org/abs/2607.05571)
21. [JSON Schema](https://json-schema.org/specification)
22. [C2PA specifications](https://spec.c2pa.org/specifications/)

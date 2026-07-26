---
title: "The Universal Mentor Reference Architecture"
section: G2-reference-architecture
status: draft
date: 2026-07-25
---

# The Universal Mentor Reference Architecture

![The universal mentor connects the learner through multimodal access to a conductor, role-certified expert mesh, verified knowledge compiler, learner-owned state, human network, action surfaces, and evidence engine across device, community-hub, and cloud tiers](../assets/diagrams/universal-mentor-reference-architecture.svg)

*One coherent relationship in front; replaceable intelligence, verified
knowledge, trusted humans, and local infrastructure behind it.*

The universal mentor is not one giant model. It is a protocol and a control
system.

Its commitments are:

1. the learner owns the longitudinal state;
2. the active teaching action is explicit;
3. every generated object comes from verified knowledge;
4. specialists are selected by role evidence, latency, privacy, and cost;
5. teachers, families, peers, tutors, and experts are first-class nodes;
6. delayed independent transfer is the north-star outcome;
7. the useful core survives network interruption;
8. knowledge remains broad while consequential actions are gated;
9. models and vendors are replaceable;
10. every layer exposes uncertainty and fallback.

## Seven planes, one experience

### 1. Learner interface and perception

The learner can speak, interrupt, type, use AAC, show a page or object, share a
screen, draw, write, manipulate a simulation, and work with other people.

Language, depth, modality, and pace can change without starting over. Temporary
sensory observations carry confidence and provenance; raw audio and video do not
become permanent memory by default.

### 2. Mentor conductor

One conductor keeps the relationship coherent. It reads only permitted state,
identifies the goal and uncertainty, chooses a teaching action, calls
specialists or humans, assembles the response, records evidence, and schedules
continuation.

The conductor is accountable orchestration, not necessarily the largest model.

### 3. Expert mentor mesh

Behind the conductor can sit a whole faculty:

- subject expert;
- curriculum architect;
- diagnostician;
- teaching router;
- language and local-culture mentor;
- accessibility specialist;
- visual and simulation teacher;
- memory scheduler;
- assessment and psychometrics agent;
- peer facilitator;
- human-network coordinator;
- consequence and safeguarding gate.

“Expert” means passed a role-specific evaluation, not assigned a persuasive
persona.

The 2026
[Beyond the AI Tutor](https://arxiv.org/abs/2604.02677) experiment found its
highest observed unaided math accuracy in the tutor-plus-peers condition. Its
two-model writing condition improved quality while preserving idea diversity
near the no-AI baseline. `MEASURED-RCT`

[DeepTutor](https://arxiv.org/abs/2604.26962) demonstrates that grounding,
multi-resolution memory, problem solving, calibrated questions, writing,
research, and proactive skills can share an agentic substrate.
`MEASURED-BENCH`

### 4. Verified knowledge compiler

One `ConceptSpec` contains:

- authorized sources;
- prerequisites and invariants;
- allowed simplifications by depth;
- misconceptions;
- examples and counterexamples;
- diagram and simulation rules;
- practice and transfer generators;
- scoring and escalation rules.

From that shared truth, the compiler can emit a layered explanation, micro-
chapter, visual, simulation, reactive notebook, practice set, assessment,
project, or reusable learner skill.

If representations contradict one another, the build fails or the uncertainty is
shown.

### 5. Learner-owned state

The learner’s vault contains:

- chosen goals and opportunity targets;
- probabilistic concept state;
- memory strength and scheduled retrieval;
- evidence pointers and support conditions;
- successful and unsuccessful teaching actions;
- language and access preferences;
- interests and local context;
- trusted human relationships and permissions;
- resumable work;
- credential candidates.

The learner can inspect, correct, export, share selectively, and delete it.
Specialists receive only the fields needed for their role.

### 6. Action surfaces and humans

The mentor can teach through:

- conversation;
- AI-native text;
- reactive notebook;
- verified visual;
- simulation or generated world;
- code, laboratory, craft, fieldwork, or physical project;
- peer collaboration;
- tutor or teacher session;
- family or community participation.

The human network is not a fallback after AI fails. It is one of the mentor’s
normal teaching actions.

### 7. Evidence and outcomes

Every meaningful action can produce:

- the capability claim;
- task and novelty;
- learner response;
- AI, human, reference, and accessibility support;
- evaluator and score uncertainty;
- state change;
- next teaching action;
- delayed-transfer schedule;
- learner disclosure permission.

The engine turns this evidence into feedback, sequencing, a longitudinal
portfolio, and selective credentials.

## The contracts make every component replaceable

| Contract | Purpose |
|---|---|
| `ConceptSpec` | Shared verified truth for every representation |
| `LearnerState` | Learner-owned goals, uncertainty, memory, access, evidence, and permissions |
| `TeachingAction` | Explicit mode, reason, expected learner action, success signal, and fallback |
| `LearningEvidence` | Claim, task, response, support, evaluator, provenance, uncertainty, and disclosure |
| `MentorTool` | Certified model/tool role, schemas, data scope, consequence class, latency, cost, and tier |
| `SyncEnvelope` | Encrypted, purpose-bound state and content deltas |
| `HumanHandoff` | Reason, urgency, role, minimum context, authority, and continuity |

With these boundaries, a model can be replaced, a local curriculum authority can
change the source layer, a specialist speech system can replace generic ASR, and
a school can hold state locally without breaking the learner relationship.

## The runtime loop

```text
learner goal or action
  → temporary multimodal observation
  → minimum necessary state
  → explicit teaching action
  → checked knowledge + certified specialists
  → conversation, learning object, tool, or human
  → learner solves, explains, builds, or collaborates
  → evidence with uncertainty
  → state and memory update
  → scheduled retrieval or transfer
  → learner-visible summary and control
```

That loop can finish in a live voice turn or continue across years.

## Device, community hub, and cloud

### Device

The device handles identity on a shared-phone-safe profile, interface, cached
curriculum, compact state, common teaching actions, practice, evidence append,
and encrypted sync.

### School or community hub

The hub supplies a stronger local model and speech stack, full local curriculum,
simulations, group learning, teacher views, updates, local-language terminology,
and local custody of child data.

### Regional or cloud specialists

The regional tier handles the hardest reasoning, multi-agent verification,
specialized language and access support, rich media, large source indexes,
credential verification, model updates, and authorized human escalation.

The scheduler spends bandwidth, energy, latency, and money only when the
expected learning value justifies it.

## Freedom, consequence, and data

Explaining, debating, simulating, creating, and exploring remain available by
default.

Actions affecting another person, money, physical systems, public posting,
location, identity, credentials, or institutional records require explicit
authority.

Raw sensory streams expire unless deliberately saved. Longitudinal memory stores
claims and evidence pointers, not total surveillance. Every handoff explains why
a human is joining, what will be shared, what they can decide, and how learning
will resume.

## Graceful degradation is part of the design

| When this fails | Continue with |
|---|---|
| Cloud | Local voice/text, cached sources, practice, evidence |
| Hub | Device cache and deferred sync |
| Speech confidence | Repeat, text, visual choice, AAC, or human |
| Source authority | Show uncertainty, teach verification, defer the claim |
| Generated visual | Verified static representation |
| State consistency | Show evidence and preserve competing hypotheses |
| Specialist agreement | Run checks, show alternatives, request human judgment |
| Human availability | Continue low-stakes learning and queue continuity |

Degraded mode means reduced media or specialization—not no learning.

## Build one complete concept first

Release 0 needs:

- one verified concept;
- text and voice;
- direct explanation, worked example, hint, retrieval, and teach-back;
- learner-owned state;
- local append-only evidence;
- a seven-day independent-transfer task;
- offline operation after install.

Then expand:

1. one dependency-linked domain;
2. language and accessibility specialists;
3. verified diagrams and simulations;
4. teacher and tutor views;
5. adaptive teaching-policy trials;
6. community-hub deployment;
7. human handoff and consequence gates;
8. cross-provider state and credentials.

## Acceptance means the learner can leave

The reference system passes when:

- a learner begins in a home language and changes modes without losing state;
- evidence changes the next teaching action;
- the action and its reason are visible;
- every representation shares checked invariants;
- learner corrections change future behavior;
- a lesson continues through an outage;
- human handoff uses minimum context;
- delayed independent transfer succeeds;
- evidence exports to another implementation;
- the model or vendor can be replaced without losing the learner.

The last test is the philosophy of the whole architecture.

The mentor is universal not because one company reaches everyone, but because
the learner can carry the relationship, knowledge, evidence, and ability to
continue—anywhere.

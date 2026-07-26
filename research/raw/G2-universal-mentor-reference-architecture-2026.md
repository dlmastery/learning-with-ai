---
title: "Universal mentor reference architecture"
wave: G
section: G2
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 24
---

# G2 — The Universal Mentor Reference Architecture

## Executive specification

The July 2026 universal mentor is one coherent learner relationship backed by a
replaceable society of models, tools, verified knowledge, trusted humans, and
local infrastructure.

Its architectural commitments are:

1. **The learner owns the longitudinal state.**
2. **The active teaching action is explicit and inspectable.**
3. **Every generated object comes from a verified concept specification.**
4. **Specialists are selected by role evidence, not model prestige.**
5. **Human relationships are first-class nodes, not escalation afterthoughts.**
6. **Delayed independent transfer is the north-star outcome.**
7. **The useful core works through connectivity interruptions.**
8. **Knowledge remains broad; consequential actions are permission-gated.**
9. **Models and vendors are replaceable; learner evidence is portable.**
10. **Every layer exposes uncertainty and graceful fallback.**

The architecture is not a single giant tutor model. It is a protocol and a
control system.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner outcome |
| `MEASURED-BENCH` | Disclosed benchmark or structured evaluation |
| `OBSERVED` | Current standard, product, deployment, or open implementation |
| `VENDOR` | Provider-reported capability |
| `RESEARCH` | Current proposed research system |
| `INFERENCE` | Reference-architecture decision |

## 1. System boundary

### In scope

- learning goals and local curriculum;
- text, voice, image, screen, handwriting, AAC, and physical-action interfaces;
- verified source and concept compilation;
- pedagogical routing and specialist-agent orchestration;
- learner-owned state, memory, and evidence;
- interactive documents, simulations, generated worlds, projects, and practice;
- teacher, family, peer, tutor, specialist, and community participation;
- assessment, delayed transfer, and portable credentials;
- device, school/community, and cloud deployment;
- child safety, privacy, provenance, audit, and permissions.

### Outside the automatic authority boundary

- irreversible real-world action without authorization;
- sole automated decisions for discipline, admission, grading, diagnosis, or
  safeguarding;
- hidden commercial recommendation;
- permanent trait classification;
- emotional dependency optimization;
- disclosure beyond minimum necessary context.

The mentor may explain anything age-appropriately. Power over the child remains
constrained.

## 2. The seven functional planes

### Plane 1 — Learner interface and perception

The learner can:

- speak and interrupt naturally;
- type or use AAC;
- show a page, object, diagram, screen, or physical setup;
- draw and write;
- manipulate a simulation;
- work alone or with others;
- change language, depth, modality, and pace;
- inspect what the mentor believes and why.

The perception layer converts raw streams into temporary, consented observations
with confidence and provenance. Raw audio/video is not longitudinal memory by
default.

### Plane 2 — Mentor conductor and teaching router

One conductor owns conversational coherence. It:

1. reads only permitted learner state;
2. identifies the current goal and uncertainty;
3. selects a `TeachingAction`;
4. requests knowledge, specialists, tools, or humans;
5. compiles the learner-facing turn;
6. records evidence and next state;
7. schedules continuation or transfer.

The conductor is not assumed to be the smartest model. It is the accountable
orchestrator.

### Plane 3 — Expert mentor mesh

Role-certified specialists may include:

- subject expert;
- curriculum architect;
- diagnostician;
- pedagogy router;
- language and local-culture mentor;
- accessibility specialist;
- visual and simulation teacher;
- memory and practice scheduler;
- assessment and psychometrics agent;
- motivation and return coach;
- peer-panel facilitator;
- human-network coordinator;
- safeguarding and consequence gate.

Most specialists remain invisible. The learner sees one calm mentor, with
provenance when a specialist’s contribution matters.

The 2026
[Beyond the AI Tutor](https://arxiv.org/abs/2604.02677) study found the highest
observed unaided math accuracy in the tutor-plus-peers condition and showed that
a two-model writing condition preserved idea diversity near the no-AI baseline
while improving quality. `MEASURED-RCT`

[DeepTutor](https://arxiv.org/abs/2604.26962) demonstrates a shared agentic
substrate for grounding, memory, problem solving, questions, writing, research,
proactive skills, and multichannel access. `MEASURED-BENCH`

### Plane 4 — Verified knowledge compiler

The compiler accepts:

- authorized sources;
- concept prerequisites and invariants;
- allowed simplifications by depth;
- known misconceptions;
- examples and counterexamples;
- diagram and simulation specifications;
- practice and transfer generators;
- scoring and escalation rules.

It emits:

- layered explanation;
- source-grounded micro-chapter;
- diagram or visual;
- executable simulation;
- reactive notebook;
- practice;
- assessment;
- project or real-world activity;
- reusable learner skill.

All outputs share one `ConceptSpec`. Contradictory representations fail the
build or are explicitly marked uncertain.

### Plane 5 — Learner-owned state and memory

The state includes:

- learner-chosen goals and identity claims;
- local curriculum and opportunity targets;
- probabilistic concept mastery;
- memory strength and next retrieval;
- evidence pointers and support conditions;
- successful and unsuccessful teaching actions;
- language and accessibility preferences;
- interests and local context;
- human relationships and permissions;
- open questions and resumable work;
- credential candidates.

The learner can inspect, correct, export, selectively share, and delete it.
Models receive role-scoped views.

### Plane 6 — Action surfaces and human network

Action surfaces include:

- conversational explanation;
- AI-native textbook;
- reactive notebook;
- verified visual;
- simulation and generated world;
- code, lab, craft, fieldwork, or physical project;
- peer collaboration;
- tutor/teacher session;
- family or community participation.

The human network is not downstream from AI. It is a parallel action surface.
The mentor can invite a peer explanation, prepare a tutor, notify a teacher of a
misconception pattern, give a family member a simple supporting role, or route a
high-stakes judgment to an authorized specialist.

### Plane 7 — Evidence, outcomes, and credentials

Every meaningful action can emit `LearningEvidence`:

- concept and claim;
- task and novelty;
- learner response or performance;
- AI, human, reference, and accessibility support;
- evaluator and scoring method;
- uncertainty;
- state change;
- next teaching action;
- delayed-transfer schedule;
- learner permissions.

The evidence engine supports immediate feedback, adaptive sequencing,
longitudinal portfolios, and selective credentials. The primary outcome is
delayed independent transfer.

## 3. The six core contracts plus human handoff

### 3.1 `ConceptSpec`

```ts
interface ConceptSpec {
  id: string;
  version: string;
  authority: SourceRef[];
  prerequisites: ConceptRef[];
  invariants: CheckableClaim[];
  depthLevels: SimplificationContract[];
  misconceptions: Misconception[];
  representations: RepresentationRecipe[];
  practiceGenerators: GeneratorPolicy[];
  transferPolicy: TransferPolicy;
  verification: VerificationSuite;
}
```

### 3.2 `LearnerState`

```ts
interface LearnerState {
  ownerId: string;
  goals: Goal[];
  conceptState: ProbabilisticConceptState[];
  memory: MemorySchedule[];
  evidenceRefs: EvidenceRef[];
  access: AccessPreference[];
  language: LanguageContext[];
  interests: LearnerAuthoredContext[];
  humanNetwork: PermissionedRelationship[];
  openLoops: ResumableWork[];
  corrections: StateCorrection[];
  permissions: FieldPermission[];
}
```

### 3.3 `TeachingAction`

```ts
type TeachingMode =
  | "explain" | "worked_example" | "hint" | "socratic"
  | "retrieve" | "contrast" | "simulate" | "teach_back"
  | "collaborate" | "human_handoff";

interface TeachingAction {
  mode: TeachingMode;
  targetConcept: string;
  reason: string;
  evidenceUsed: EvidenceRef[];
  supportLevel: number;
  expectedLearnerAction: string;
  successSignal: string;
  fallback: TeachingActionRef;
}
```

### 3.4 `LearningEvidence`

```ts
interface LearningEvidence {
  claim: CapabilityClaim;
  task: TaskDescriptor;
  responseRef: EncryptedArtifactRef;
  support: SupportConditions;
  evaluator: EvaluatorRef;
  score: ScoreWithUncertainty;
  provenance: ProvenanceEvent[];
  nextProbe?: ProbeSchedule;
  learnerPermission: DisclosurePolicy;
}
```

### 3.5 `MentorTool`

```ts
interface MentorTool {
  role: string;
  inputSchema: JSONSchema;
  outputSchema: JSONSchema;
  dataScope: FieldSelector[];
  consequenceClass: "learning" | "external";
  certification: EvaluationResult[];
  latencyBudgetMs: number;
  costBudget: number;
  offlineCapability: "device" | "hub" | "cloud";
}
```

### 3.6 `SyncEnvelope`

```ts
interface SyncEnvelope {
  ownerId: string;
  encryptedDeltas: EncryptedDelta[];
  vectorClock: Clock;
  purpose: string;
  expiry?: string;
  recipientScope: string[];
  signature: string;
}
```

### 3.7 `HumanHandoff`

```ts
interface HumanHandoff {
  reason: string;
  urgency: "routine" | "priority" | "urgent";
  requestedRole: "peer" | "family" | "teacher" | "tutor" | "specialist";
  minimumContext: EvidenceRef[];
  learnerVisibleSummary: string;
  authorityBoundary: string;
  continuityPlan: string;
}
```

## 4. The runtime loop

```text
1. learner expresses a goal or acts in the world
2. perception produces temporary observations
3. conductor reads minimum necessary state
4. teaching router proposes an action
5. knowledge compiler and specialists produce checked inputs
6. consequence gate separates learning from external action
7. mentor acts through conversation, object, tool, or human
8. learner responds, builds, explains, or collaborates
9. evidence engine scores with uncertainty
10. learner state and memory update
11. next retrieval or transfer is scheduled
12. learner receives an inspectable summary and control
```

The loop can execute in seconds during a live turn or across months.

## 5. Physical deployment: device, community, cloud

### Tier 1 — Learner device

Default local responsibilities:

- wake and identity under a shared-device-safe profile;
- text, speech, and AAC interface;
- cached curriculum and source retrieval;
- compact learner state;
- common teaching actions and practice;
- state/evidence append;
- encrypted sync queue;
- emergency offline contact instructions.

### Tier 2 — School or community hub

Responsibilities:

- stronger local model and speech stack;
- complete local curriculum;
- shared simulations and media;
- teacher and facilitator views;
- group learning orchestration;
- device updates and local model cache;
- local-language terminology;
- custody of locally governed child data;
- opportunistic regional synchronization.

### Tier 3 — Regional or cloud specialists

Responsibilities:

- hardest reasoning and multimodal generation;
- multi-agent verification;
- rare language or accessibility specialists;
- large source indexes;
- cross-site evaluation;
- credential verification;
- authorized human escalation;
- model and content updates.

The device does not block on the cloud for every turn. The scheduler spends
latency, bandwidth, energy, and money only when the expected learning value
justifies it.

## 6. Trust, safety, and freedom architecture

### Learning remains open

Explaining, simulating, debating, creating, and exploring are available by
default, adapted to age and context.

### Consequence is gated

Actions affecting another person, money, physical systems, public posting,
location, identity, credentials, or institutional records require explicit
authority.

### Data is minimized

- raw sensory streams expire unless the learner deliberately saves an artifact;
- longitudinal state stores claims and evidence pointers, not total surveillance;
- specialists receive field-scoped context;
- humans receive the minimum necessary summary;
- permissions and retention are inspectable;
- the learner can correct and export.

### Escalation preserves continuity

A handoff explains:

- why a human is joining;
- what context will be shared;
- what the human can decide;
- how the learning episode will resume.

## 7. Model and specialist certification

“Expert” means passed an evaluation for a declared role.

| Role | Required evaluation |
|---|---|
| Conductor | coherence, correct routing, privacy scope, graceful fallback |
| Subject expert | domain truth, source quality, calibration, tool use |
| Teaching router | delayed-transfer uplift over fixed policies |
| Language mentor | local-speaker review, curriculum terms, code-switching |
| Accessibility specialist | goal preservation across modalities and profiles |
| Visual/simulation teacher | structural truth, accessibility, learner action |
| Assessment agent | validity, calibration, subgroup performance, uncertainty |
| Memory scheduler | retention and transfer per learner burden |
| Human coordinator | handoff precision, minimum context, continuity |
| Consequence gate | high recall for consequential action with low learning friction |

A small local model can beat a frontier model for a narrow role. The router uses
certification, latency, privacy, cost, and offline availability.

## 8. Graceful degradation

| Failure | Continue with |
|---|---|
| Cloud unavailable | local text/voice, cached sources, practice, state append |
| Hub unavailable | device cache and deferred sync |
| Voice confidence low | text, repeat, visual choice, human support |
| Source authority uncertain | label uncertainty, teach verification, defer claim |
| Generated visual fails checks | use verified static representation |
| Learner state conflict | show evidence, ask learner, preserve both hypotheses |
| Specialist disagreement | surface alternatives, run checks, request human judgment |
| Human unavailable | continue low-stakes learning, queue handoff, never invent authority |
| Device shared | session-scoped local identity and encrypted owner state |

Degraded mode means reduced latency, media, or specialization—not no learning.

## 9. Minimum viable reference implementation

### Release 0 — One concept, complete loop

- one verified `ConceptSpec`;
- text and voice;
- direct explanation, worked example, hint, retrieval, and teach-back;
- learner-owned state;
- local append-only evidence;
- 7-day independent transfer;
- offline operation after initial install.

### Release 1 — One domain

- 100 dependency-linked concepts;
- language and accessibility specialists;
- verified diagrams and simulations;
- teacher/tutor view;
- adaptive teaching-policy trial;
- device/hub synchronization.

### Release 2 — Community deployment

- shared low-cost hub;
- local curriculum-authority workflow;
- family, peer, and community-expert roles;
- human handoff and consequence gate;
- 30- and 90-day transfer;
- cost and energy telemetry.

### Release 3 — Open ecosystem

- cross-provider conformance;
- learner-state wallet;
- specialist certification registry;
- selective verifiable credentials;
- deployment playbooks across regions and languages.

## 10. Acceptance tests

The reference system is not complete until:

1. a learner can begin in a home language and switch modes without losing state;
2. the tutor’s next action changes when evidence changes;
3. every teaching action exposes its reason;
4. generated text, diagram, simulation, and assessment share verified invariants;
5. the learner corrects state and the correction changes future behavior;
6. the core lesson continues through a network outage;
7. a human receives only minimum context and the learner sees the handoff;
8. the learner completes a delayed independent transfer task;
9. evidence exports to a second implementation;
10. a model, specialist, or vendor can be replaced without losing learner state.

## 11. Architecture conclusion

Every major component has a 2026 existence proof:

- frontier models supply multilingual multimodal intelligence;
- Study Mode and Guided Learning expose teaching policies;
- DeepTutor and AgentTutor expose agentic orchestration;
- Tutor CoPilot and LessonOrca connect human continuity;
- Learn Your Way and reactive systems compile learning objects;
- E2V-Bench and EduIllustrate make generated visuals testable;
- Kolibri supplies offline-first distribution;
- xAPI, CLR, Open Badges, and verifiable credentials supply portability
  primitives;
- Sierra Leone and Nigeria show measured gains in public-school contexts.

The universal mentor is the disciplined composition:

```text
one learner-owned relationship
+ a role-certified expert mesh
+ verified executable knowledge
+ an explicit teaching control loop
+ trusted humans
+ three-tier delivery
+ delayed-transfer evidence
```

This is buildable now.

## Sources

1. Project synthesis, [Expert mentor mesh](../../survey/03-expert-mentor-mesh.md), 2026.
2. Project research, [Universal reach](F4-reach-economics.md), 2026.
3. Project synthesis, [Learning science control loop](../../survey/25-learning-science-becomes-a-control-system.md), 2026.
4. Project synthesis, [Learner-owned state](../../survey/06-learner-owned-state.md), 2026.
5. Project synthesis, [Executable knowledge](../../survey/07-executable-knowledge.md), 2026.
6. Project synthesis, [Live multimodal mentor](../../survey/10-live-multimodal-mentor.md), 2026.
7. Project synthesis, [Assessment evidence architecture](../../survey/26-assessment-becomes-an-evidence-architecture.md), 2026.
8. Project synthesis, [Designed from the margin](../../survey/19-designed-from-the-margin.md), 2026.
9. Project synthesis, [Safe enough to be free](../../survey/20-safe-enough-to-be-free.md), 2026.
10. [Beyond the AI Tutor](https://arxiv.org/abs/2604.02677), 2026.
11. [DeepTutor](https://arxiv.org/abs/2604.26962), 2026.
12. [AgentTutor](https://arxiv.org/abs/2601.04219), 2026.
13. [EduAgentBench](https://arxiv.org/abs/2605.14322), 2026.
14. Wang et al., [Tutor CoPilot](https://arxiv.org/abs/2410.03017).
15. Google DeepMind/Eedi, [Human-supervised AI tutoring](https://arxiv.org/abs/2512.23633), 2025.
16. Google, [Gemini study notebooks](https://blog.google/products-and-platforms/products/education/iste-students-2026/), 2026.
17. Google, [Learn Your Way](https://blog.google/products-and-platforms/products/education/learn-your-way/), 2025.
18. [E2V-Bench](https://arxiv.org/abs/2605.31212), 2026.
19. [EduIllustrate](https://arxiv.org/abs/2604.05005), 2026.
20. Learning Equality, [Kolibri](https://learningequality.org/kolibri/about-kolibri/), current 2026.
21. Ed-Fi Alliance, [Data Standard in the Age of AI](https://docs.ed-fi.org/getting-started/provider-playbook/implementation/ed-fi-data-standard-in-the-age-of-ai/), 2026.
22. [I2IDL](https://www.i2idl.org/), current 2026.
23. World Bank, [Nigeria tutoring RCT](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324), 2025.
24. Google DeepMind, [Sierra Leone Guided Learning RCT](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/), 2026.

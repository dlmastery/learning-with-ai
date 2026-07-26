---
title: "Portfolio validation and comparative learning systems"
wave: D-G
sections: [D2, G3]
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 19
---

# D2 + G3 — From a Portfolio of Projects to a Universal Mentor

## Executive finding

The reference standard developed in this survey survives contact with real
systems.

The `dlmastery` portfolio, an external AI-native machine-learning book, and seven
current learning platforms each demonstrate valuable pieces of the universal
mentor:

- high-volume first-principles curriculum authoring;
- executable skills and evaluation harnesses;
- live multimodal tutoring;
- curriculum-grounded mastery support;
- persistent personalized agent memory;
- teacher and human-tutor continuity;
- open self-hosting;
- offline distribution;
- measured learning gains.

No inspected system exposes the entire composition. That comparison does not
invalidate any project. It shows that the next product can be assembled from
demonstrated parts.

The strongest portfolio conclusion is:

> **Do not build another isolated tutor. Connect the existing authoring,
> real-time, memory, verification, human, and measurement assets through one
> learner-owned state and one evidence loop.**

## Evidence labels

| Label | Meaning |
|---|---|
| `INSPECTED` | Code, built artifacts, or public files directly examined |
| `OBSERVED` | Public product or open implementation |
| `VENDOR` | Provider-reported capability or metric |
| `MEASURED-RCT` | Randomized learner outcome |
| `RESEARCH` | Current research implementation |
| `NOT-PUBLIC` | Not visible in the inspected public surface; not proof of absence |
| `INFERENCE` | Synthesis or build consequence |

## 1. Why the comparison occurs late

The project’s future standard was written before this validation. That
quarantine matters: prior artifacts can now test the standard without silently
shrinking it to whatever happened to be built already.

The comparison asks seven questions:

1. Is knowledge grounded, executable, and verifiable?
2. Does teaching adapt by state and goal rather than by one fixed style?
3. Can the system see, hear, show, and act with low latency?
4. Does memory compound across sessions under learner control?
5. Are teachers, families, peers, tutors, and specialists part of the system?
6. Can it work on low-cost devices and interrupted networks?
7. Does it measure delayed independent transfer?

This is a capability comparison, not a leaderboard.

## 2. The `dlmastery` portfolio: the missing system is already latent

The earlier
[forensic source audit](D2-portfolio-case-studies.md) inspected approximately 60
repositories, 35+ active projects, nine deployed applications, 128 notebooks,
production bundles, prompts, schemas, real-time audio paths, and automated
research harnesses. `INSPECTED`

### 2.1 Demonstrated assets

The portfolio has already demonstrated:

1. **A mechanized zero-to-hero authoring method.** A fixed educational arc,
   builder utilities, validation, coverage audit, dependency ordering, and
   repeatable notebook generation exist at corpus scale. `INSPECTED`
2. **Live multimodal tutoring.** The applications implement voice input/output,
   interruption, transcripts, language switching, persona, structured tool
   calls, visual generation, and homework-image flows. `INSPECTED`
3. **A schema-constrained curriculum compiler.** Learner grade, location,
   language, interests, and goal can produce a structured learning path.
   `INSPECTED`
4. **Verified content production.** Notebook pipelines execute cells, check
   structure, enforce grounding conventions, audit coverage, and preserve
   regenerable drivers. `INSPECTED`
5. **Persistent memory patterns.** `meditationguru` carries cross-session context;
   the autonomous-research projects use append-only ledgers and compact
   checkpoints so a new agent can resume. `INSPECTED`
6. **Autonomous improvement loops.** Hypotheses, experiments, hard evaluation
   gates, objective fingerprints, adversarial audit, and champion promotion have
   run at large scale. `INSPECTED`
7. **Progressive media delivery.** The media projects implement storyboard,
   still, video, narration, continuity, streaming, and export pipelines.
   `INSPECTED`
8. **A rural-first product specification.** The Sokrates design specifies
   on-device operation, low-cost Android, intermittent sync, and village sharing.
   `INSPECTED`

Those are not superficial prototypes. Together they cover authoring, delivery,
memory, experimentation, and access design.

### 2.2 The integration seam

The live tutors, content builders, memory systems, and research harnesses do not
currently share one learner-state or evidence contract. `INSPECTED`

That seam can be stated positively:

```text
zero-to-hero authoring
        +
runtime concept verification
        +
Ekalavya live tutor tools
        +
meditationguru continuity
        +
autoresearch experiment ledger
        +
Sokrates local-first target
        =
first coherent universal-mentor prototype
```

The portfolio therefore needs less invention than consolidation. `INFERENCE`

## 3. The external harness-engineering book: learning leaves systems behind

The April 2026 repository
[`xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning`](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning)
is a complete AI-native machine-learning book organized around skills, project
memory, evaluation loops, and harness engineering. `INSPECTED`

Its core sequence is:

```text
prompt once
  → repeat a workflow
  → package a reusable skill
  → design a reliable harness around the human and model
```

The
[outline](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning/blob/main/OUTLINE.md)
defines a beginner-to-specialist ladder, recurring real-world cases, chapter
Harness Labs, evidence trails, reflection artifacts, and system-design
extensions. `INSPECTED`

The
[reader-skill workflow](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning/blob/main/src/how-to-use-reader-skills.md)
asks the learner to:

1. state the judgment in their own words;
2. work a concrete case;
3. invoke a reusable skill;
4. compare its output with their reasoning;
5. save accepted and rejected output plus the next experiment.

That is a powerful bridge between reading and professional action. It makes the
skill inspectable and makes each chapter leave a durable evidence artifact.

Its public repository does not expose a live adaptive learner model,
full-duplex tutor, family/teacher network, or offline runtime. `NOT-PUBLIC`
Those are natural composition opportunities, not defects in a book.

## 4. Comparative systems: each one proves a different layer

### 4.1 Google Learn Your Way and study notebooks — content becomes adaptive

[Learn Your Way](https://blog.google/products-and-platforms/products/education/learn-your-way/)
turns static textbook material into personalized representations and reported an
11-percentage-point advantage on a long-term recall test relative to a standard
digital reader. `VENDOR`

Gemini
[study notebooks](https://blog.google/products-and-platforms/products/education/iste-students-2026/)
diagnose gaps, generate a lesson plan, update it from quizzes, and share source
context with NotebookLM. `VENDOR`

Together they demonstrate the AI-native textbook and adaptive study loop. Their
public surfaces do not provide a portable learner-owned state or offline
frontier-inference layer. `NOT-PUBLIC`

### 4.2 Khanmigo — curriculum and mastery shape the dialogue

[Khanmigo’s 2026 redesign](https://blog.khanacademy.org/learning-in-the-open-what-ai-is-and-isnt-changing/)
uses whether a learner is first learning or reviewing a skill, plus mastery and
prerequisite information, to select support. Khan Academy reports a
six-percentage-point improvement in next-item learning in its 2025–2026 product
tests. `VENDOR`

This demonstrates the value of connecting conversation to an explicit content
graph and practice history.

### 4.3 LessonOrca and Tutor CoPilot — humans become more continuous

[LessonOrca](../../survey/21-lessonorca-evidence-loop.md) connects session
history, tutor plans and notes, between-session support, parent visibility, and
organization policies. `VENDOR`

[Tutor CoPilot](https://arxiv.org/abs/2410.03017) found four percentage points of
overall mastery gain and nine points for learners served by lower-rated tutors
when tutors had real-time AI guidance. `MEASURED-RCT`

These systems prove that AI can distribute expert teaching moves through a human
relationship rather than requiring an either/or choice.

### 4.4 Flint — one teacher can author multimodal learning activities

[Flint](https://flintk12.com/teachers) publicly demonstrates a broad student
activity surface: voice practice, historical roleplay, guided science labs,
whiteboards, diagram annotation, graphing, coding, writing feedback, leveled
reading, and teacher analytics. `VENDOR`

Its distinct contribution is the teacher as author of an interactive learning
experience, not merely a consumer of generated text.

### 4.5 DeepTutor — agentic personalization has a coherent substrate

[DeepTutor](https://arxiv.org/abs/2604.26962) unifies source grounding,
multi-resolution memory, problem solving, calibrated question generation,
collaborative writing, deep research, proactive skills, multichannel access, and
a student-centric TutorBench. `RESEARCH`

It is the clearest current research expression of the mentor as an agentic
system rather than a chat window.

### 4.6 Open TutorAI — the tutor can be self-hosted and shared

[Open TutorAI](https://opentutorai.com/) exposes classrooms, source-grounded
support, student-configured tutors, analytics, and learner/teacher/parent roles
in an open self-hosted platform. Its avatar mode adds voice and video.
`RESEARCH`

Its contribution is institutional and local control of the runtime.

### 4.7 Kolibri — universal reach starts before continuous broadband

[Kolibri](https://learningequality.org/kolibri/about-kolibri/) is an open,
offline-first platform for curriculum and progress on low-cost and legacy
devices. `OBSERVED`

It does not need to be replaced by an AI tutor. It can become the local content,
identity, and synchronization substrate under one.

## 5. Coverage matrix

`●` demonstrated in the inspected public surface;
`◐` partial, emerging, or provider-bound;
`○` not visible publicly; not proof of absence

| System | Verified knowledge / artifacts | Adaptive teaching / state | Multimodal action | Human network | Offline / local control | Transfer evidence |
|---|---:|---:|---:|---:|---:|---:|
| `dlmastery` portfolio | ● | ◐ | ● | ◐ | ◐ | ○ |
| Harness-engineering book | ● | ◐ | ◐ | ○ | ● static | ◐ artifacts |
| Google Learn Your Way / notebooks | ● | ● | ● | ◐ teacher | ○ | ◐ |
| Khanmigo | ● | ● | ◐ | ● teacher | ○ | ◐ next-item |
| LessonOrca / Tutor CoPilot | ◐ | ◐ | ◐ | ● | ○ | ● trial / planned |
| Flint | ◐ | ◐ | ● | ● teacher | ○ | ○ public |
| DeepTutor | ● | ● | ● | ◐ | ● open | ◐ benchmark |
| Open TutorAI | ● | ◐ | ● | ● | ● self-host | ◐ analytics |
| Kolibri | ● static | ◐ progress | ◐ HTML5 | ● facilitator | ● | ◐ progress |

No row is the universal mentor. Every column has at least one demonstrated
implementation. `INFERENCE`

## 6. What the comparison adds to the reference standard

### 6.1 A chapter should ship a skill

The harness-engineering book makes an important advance over a conventional
textbook: each chapter can leave behind a reusable decision procedure.

The AI-native textbook should therefore compile:

- the explanation;
- executable examples;
- practice;
- assessment;
- a reusable learner skill;
- an evidence artifact;
- a memory update.

### 6.2 A tutor should expose its teaching policy

The compared systems use different policies—Socratic guidance, prerequisite
review, direct instruction, teacher-authored activities, expert suggestions,
and learner-created supports. The universal mentor should make the active mode
visible and permit an authorized learner or educator to change it.

### 6.3 Project memory and learner memory can share a pattern

The `dlmastery` research harness uses a compact checkpoint and append-only
ledger. The harness-engineering book asks readers to save accepted decisions,
rejected output, and next experiments. DeepTutor uses multi-resolution memory.

These converge on a learner-memory architecture:

```text
compact current state
+ append-only evidence pointers
+ learner-authored reflections
+ scheduled retrieval
+ explicit uncertainty
```

### 6.4 Local-first does not mean model-last

Kolibri supplies a local delivery substrate; Open TutorAI supplies
self-hostability; compact models supply increasing local intelligence; cloud
specialists can be intermittent. The comparison strengthens the three-tier
delivery architecture rather than treating offline use as a reduced static
edition.

## 7. The portfolio’s next integration release

A credible first release can be bounded to six shared contracts.

### Contract 1 — `ConceptSpec`

One checked representation of prerequisites, invariants, misconceptions,
examples, diagrams, simulations, practice generators, and source authority.

### Contract 2 — `LearnerState`

Learner-owned goals, mastery distributions, evidence pointers, memory strength,
access preferences, language, interests, and human permissions.

### Contract 3 — `TeachingAction`

An explicit choice among direct explanation, worked example, hint, Socratic
question, retrieval, simulation, teach-back, peer work, or human escalation.

### Contract 4 — `LearningEvidence`

Attempt, context, support level, concept, response, evaluator, confidence, next
probe, delayed transfer, and credential export.

### Contract 5 — `MentorTool`

Model-independent tools for source retrieval, diagram generation, simulation,
voice, learner-state read/write, assignment, scheduling, and human handoff.

### Contract 6 — `SyncEnvelope`

Encrypted learner-controlled state and content deltas that work across personal
device, school/community hub, and cloud specialist.

These contracts turn the portfolio’s strongest existing projects into modules
of one system.

## 8. Suggested build sequence

1. **Shared core package.** Extract the six contracts plus model adapters from
   one live tutor instead of forking another application.
2. **Instrument independent transfer.** Add a new-problem, delayed, changed-
   context assessment event before optimizing engagement.
3. **Connect memory.** Adapt the existing cross-session and ledger patterns to
   learner-owned state with evidence pointers.
4. **Compile content at runtime.** Bring the notebook validation and grounding
   gates into live generated lessons and visuals.
5. **Expose teaching actions.** Let the mentor and teacher see which pedagogical
   mode is active and why.
6. **Add the human mesh.** Connect tutor, family, peer, teacher, and specialist
   views through minimum-necessary permissions.
7. **Ship the local tier.** Run core retrieval, state, voice, and common teaching
   moves on device or community hub, with opportunistic specialist calls.

## 9. Final comparative judgment

The late comparison reveals convergence:

- the `dlmastery` portfolio knows how to generate, verify, speak, stream,
  remember, and run experiments;
- the harness-engineering book knows how learning becomes a reusable skill and
  an evidence artifact;
- Google and Khan Academy connect material, diagnosis, practice, and adaptation;
- LessonOrca and Tutor CoPilot connect AI expertise to human continuity;
- Flint turns teachers into authors of multimodal experiences;
- DeepTutor and Open TutorAI show agentic and open architectures;
- Kolibri shows how learning reaches beyond continuous connectivity.

The future standard is larger than any one project but smaller than the union of
what already works.

That is the optimistic conclusion of portfolio validation: **the universal
mentor is not waiting for a singular invention. It is waiting for disciplined
integration.**

## Sources

1. Internal first-hand audit, [D2 portfolio case studies](D2-portfolio-case-studies.md), 2026.
2. Project standard, [expert mentor mesh](../../survey/03-expert-mentor-mesh.md), 2026.
3. Project standard, [learner-owned state](../../survey/06-learner-owned-state.md), 2026.
4. Project standard, [executable knowledge](../../survey/07-executable-knowledge.md), 2026.
5. Project standard, [live multimodal mentor](../../survey/10-live-multimodal-mentor.md), 2026.
6. `xiaol`, [Harnessing LLM Skills to Master Machine Learning](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning), inspected 2026-07-25.
7. `xiaol`, [Book outline](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning/blob/main/OUTLINE.md), 2026.
8. `xiaol`, [Reader-skill workflow](https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning/blob/main/src/how-to-use-reader-skills.md), 2026.
9. Google, [Learn Your Way](https://blog.google/products-and-platforms/products/education/learn-your-way/), 2025.
10. Google, [Study notebooks and connected learning tools](https://blog.google/products-and-platforms/products/education/iste-students-2026/), 2026.
11. Khan Academy, [Learning in the Open](https://blog.khanacademy.org/learning-in-the-open-what-ai-is-and-isnt-changing/), 2026.
12. Khan Academy, [Building a better AI tutor](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/), 2026.
13. LessonOrca, [product evidence program](../../survey/21-lessonorca-evidence-loop.md), 2026.
14. Wang et al., [Tutor CoPilot](https://arxiv.org/abs/2410.03017), field trial.
15. Flint, [teacher activity platform](https://flintk12.com/teachers), current 2026.
16. Zhao et al., [DeepTutor](https://arxiv.org/abs/2604.26962), 2026.
17. El Hajji et al., [Open TutorAI](https://arxiv.org/abs/2602.07176), 2026.
18. Learning Equality, [Kolibri](https://learningequality.org/kolibri/about-kolibri/), current 2026.
19. 1EdTech, [CLR and Open Badges horizon](https://www.1edtech.org/sites/default/files/media/docs/2025/Wellspring_Phase_I_Report.pdf), 2025.

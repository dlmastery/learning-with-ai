---
title: "The Next Problems Are System Problems"
section: F9-G4-research-frontier
status: draft
date: 2026-07-25
---

# The Next Problems Are System Problems

![A ranked research map places delayed transfer, learner-owned state, verified generated knowledge, and offline full-duplex tutoring in the prove-before-scaling tier; teaching policy, multimodal observation, accessibility, and human networks in the composition tier; and credentials plus global deployment laboratories in the ecosystem tier](../assets/diagrams/research-frontier-priority-map.svg)

*The field has enough intelligence to begin. The highest-value work now turns
that intelligence into durable, portable human growth.*

The old frontier asked whether a language model could explain a concept, answer
a question, or generate a lesson.

By July 2026, those capabilities are abundant. The next research problems are
about the system around the model:

- what the learner can do later without help;
- who owns the learner’s history;
- which teaching action should happen now;
- whether every generated representation is true;
- how intelligence works through network outages;
- how speech, handwriting, tools, disability, and group work are understood;
- how humans remain connected;
- how learning evidence opens opportunity without becoming a permanent dossier.

These are not reasons to slow deployment. They are a blueprint for making rapid
deployment worth trusting.

## P0: prove before scaling

### 1. Delayed independent transfer

The north-star outcome is:

```text
new task + later date + changed context + no tutor
```

[LongTutor](https://aclanthology.org/2026.acl-long.1371/) now evaluates
long-term personalized tutoring against longitudinal learner histories.
[EduAgentBench](https://arxiv.org/abs/2605.14322) evaluates diagnosis,
pedagogical justification, adaptation over time, and action inside realistic
teaching workflows. `MEASURED-BENCH`

The next step is a real cohort assessed at 7, 30, 90, and 365 days. Every product
claim should end in independent transfer, not turns or minutes.

### 2. Learner-owned state

The mentor needs memory, but the provider should not own the learner.

An open state must represent goals, concept uncertainty, memory strength,
evidence pointers, access preferences, language, and human permissions. It must
be readable, correctable, selectively shareable, and portable across models and
schools.

The [Ed-Fi Alliance’s 2026 AI work](https://docs.ed-fi.org/getting-started/provider-playbook/implementation/ed-fi-data-standard-in-the-age-of-ai/)
and [I2IDL](https://www.i2idl.org/) identify the needed interoperability and
conformance layer. `OBSERVED`

The milestone is concrete: two model providers, two learning platforms, and one
offline community hub import and export the same learner-controlled state—and a
learner correction changes the next teaching action.

### 3. Verified generated knowledge

A generated diagram can be beautiful and numerically wrong. A simulation can be
engaging and obey the wrong law. A quiz can test something different from the
lesson.

Current research is beginning to make educational generation testable:

- [E2V-Bench](https://arxiv.org/abs/2605.31212) evaluates whether early-
  arithmetic visuals preserve numerical and relational structure;
- [EduIllustrate](https://arxiv.org/abs/2604.05005) evaluates 230 multimodal
  education problems across subjects, grades, consistency, and learning-theory
  criteria;
- [MagicGeo](https://doi.org/10.1016/j.gmod.2026.101331) uses a symbolic geometry
  representation and computational verification before rendering.

The breakthrough is one `ConceptSpec` compiling prose, diagram, simulation,
practice, and assessment—with contradictions failing the build.

### 4. Offline full-duplex tutoring

[Kolibri](https://learningequality.org/kolibri/about-kolibri/) proves that
offline-first learning content and progress can work on low-cost and legacy
devices. A 2026
[offline-first LLM architecture](https://scale.stanford.edu/ai/repository/offline-first-llm-architecture-adaptive-learning-low-connectivity-environments)
reports the feasibility of adaptive AI assistance in low-connectivity settings.
`OBSERVED` / `RESEARCH`

The next reference runtime must publish—not hide—its device, energy, latency,
network, and cost budgets. Common voice, retrieval, memory, and teaching moves
should run on the device or community hub; hard problems should route to an
intermittent specialist.

## P1: compose the learning experience

### 5. A causal teaching-action router

The relevant choice is not “Socratic or direct.” It is:

```text
explain · worked example · hint · question · retrieve
· simulate · peer · human
```

A randomized 2026 study of 334 university learners found AI tutoring improved
exam performance by 0.23 standard deviations and that unrestricted access
outperformed a forced-pre-reading policy by 0.21 standard deviations.
[`MEASURED-RCT`](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5992341)

The proper response is not to turn one policy into doctrine. It is to
sequentially randomize teaching actions, learn by state and goal, and test the
router against delayed transfer.

### 6. Real multimodal observation

A mentor should see the child’s diagram, hear uncertainty, follow a physical
experiment, and understand group participation—not merely parse a typed prompt.

[SciIBI](https://researchdiscovery.drexel.edu/esploro/outputs/preprint/Can-Multimodal-LLMs-See-Science-Instruction/991022163435104721)
benchmarks science-classroom video and discourse.
[ChildVox](https://arxiv.org/abs/2605.29257) evaluates childhood audio and speech
understanding. The
[Pasketti challenge](https://www.drivendata.org/competitions/group/childrens-asr-competition/)
provides 560,000 child utterances and 515+ hours across read, prompted, and
spontaneous speech. `MEASURED-BENCH`

The needed dataset includes consented speech, handwriting, diagrams,
manipulatives, experiments, individual work, and group work—with teacher labels
for when intervention should, should not, or must happen.

### 7. Disability and language as the design center

[Special-R1](https://arxiv.org/abs/2605.30670) evaluates disability-adaptive
tutoring across five profiles and 690 multi-turn dialogues, improving
persona-aware fit from 6.75 to 8.40 in its disclosed test. `MEASURED-BENCH`

[Shiksha Copilot](https://doi.org/10.1145/3788074) shows human-in-the-loop,
curriculum-aligned lesson adaptation in English and local Indian languages.
`OBSERVED`

The success condition is not easier content. It is the same rigorous goal
reached through a representation, language, pace, and response channel the
learner can use.

### 8. The human mesh

[Tutor CoPilot](https://arxiv.org/abs/2410.03017) increased topic mastery by four
percentage points overall and nine points for learners served by lower-rated
tutors. `MEASURED-RCT`

The next study should compare AI-only, human-only, AI-assisted human, and
learner-group-plus-AI conditions. It should measure transfer, belonging,
equitable participation, continuity, escalation precision, and learning per
scarce human hour.

The goal is abundant expert support that strengthens human relationships.

## P2: build the ecosystem

### 9. Evidence to opportunity

Open Badges, Comprehensive Learner Records, xAPI, and verifiable credentials
provide containers. The missing protocol states exactly:

- which capability is claimed;
- what task supports it;
- which help was available;
- how recently;
- with what uncertainty;
- what the learner chooses to reveal.

The milestone is a real project credential accepted by a second institution
without transferring the learner’s raw history.

### 10. Global deployment laboratories

The Sierra Leone and Nigeria trials show that large gains are possible in
African public-school contexts. They should seed a locally led research network
across rural and urban Africa, India’s multilingual systems, China’s adaptive-
learning ecosystem, Latin America, island and displaced communities, indigenous
languages, and disability-serving schools.

Each site should publish:

- a common minimum outcome set;
- locally defined learning goals;
- device, power, and network conditions;
- model and human-support configuration;
- cost per learner and per transferred concept;
- reusable implementation materials.

Success means every deployment makes the next community faster and cheaper.

## The program has dates and tests

| Horizon | Deliverable | Proof |
|---|---|---|
| 6 months | Open mentor contracts | Cross-provider + offline-hub conformance |
| 6 months | Delayed-transfer kit | 7- and 30-day tasks in a deployed tutor |
| 9 months | Concept compiler | Text, visual, simulation, and assessment agree or fail |
| 12 months | Local full-duplex runtime | Published device, energy, latency, network, cost, and outcome budgets |
| 18 months | Teaching-router trial | Beats the best fixed policy on transfer |
| 18 months | Access-first multimodal cohort | Equivalent rigor and improved participation |
| 24 months | Human-mesh trial | More learning per scarce human hour and stronger continuity |
| 36 months | Learner wallet pilot | Selective evidence accepted across institutions |
| 36 months | Deployment-lab network | Open costed playbooks across contexts |
| 60 months | Longitudinal independence result | 90- and 365-day transfer and opportunity outcomes |

## What no longer defines the frontier

The field does not need another undifferentiated chat wrapper, summary generator,
closed activity dashboard, isolated textbook-answer benchmark, or “offline”
demo without hardware and learning measurements.

Those can be useful features. They are not the work that unlocks the next
billion learners.

The frontier is a mentor that remembers without owning, adapts without labeling,
generates without inventing, observes without surveilling, works through
outages, amplifies humans, and makes itself progressively less necessary as the
learner grows.

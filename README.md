# Learning with AI

Excellent personal instruction is scarce. The models, media systems and agent
runtimes needed to change that are arriving quickly. The missing piece is a learning
system.

This project develops the evidence and product architecture for one: a persistent
personal faculty that can observe the work, choose a useful next move, change the
representation, remember what happened, withdraw help, and verify that the learner
can act independently.

It is meant to work across ages and fields—from early reading to graduate
mathematics—and to treat accessibility as part of instruction. The founding design
case is an eleven-year-old served under a SELPA plan who may understand a concept
while a reading-heavy worksheet measures something else.

## The thesis

A frontier model is a component, not a learning system.

Current systems can converse through voice and vision, generate diagrams and
software, execute tools, and maintain state across sessions. Those capabilities
become instruction only when a control loop connects them to learner evidence:

1. resume the learner's goal and unresolved question;
2. elicit a prediction, explanation, drawing or action;
3. maintain competing explanations for what the action means;
4. select or generate the smallest useful representation;
5. fade assistance and test a new case;
6. revisit the idea after a delay;
7. update an inspectable, portable learner record.

The primary outcome is delayed, unassisted performance on novel work. Engagement,
assisted completion and conversation quality are useful observations; they are not
substitutes for learning.

## Public artifacts

| Artifact | What it is |
|---|---|
| [Research dashboard](https://dlmastery.github.io/learning-with-ai/) | Product thesis, frontier capability map, access requirements and research program |
| [Pitch deck](https://dlmastery.github.io/learning-with-ai/deck.html) | A 15-slide venture narrative, including the decisions that still belong to the founder |
| [Paper](PAPER.md) | A concise evidence synthesis and reference architecture |
| [Web paper](https://dlmastery.github.io/learning-with-ai/paper.html) | Reading edition of the paper |
| [Living Evidence Atlas](ATLAS.md) | The long research record and extended argument; intentionally separate from the paper |
| [Mechanism gallery](https://dlmastery.github.io/learning-with-ai/demos/) | Browser implementations of individual ideas, each scoped to what it demonstrates |
| [Corrections](CORRECTIONS.md) | Append-only record of factual and editorial corrections |

The demos are research instruments and mechanism prototypes. They are not presented
as an end-to-end product. A previous scripted “University in a Box” walkthrough was
removed because it simulated the interface without implementing the learning system.

## What the evidence currently supports

- Purpose-built and human-supervised generative systems can improve proximal
  instructional outcomes.
- Unguarded assistance can improve practice performance while harming later
  unassisted performance.
- Ease, preference and engagement can move independently of learning.
- Prior knowledge varies enough that a fixed starting point is a major design error.
- Progress measurement needs an explicit rule for changing instruction.
- Retrieval, spacing, active attempts and faded support remain load-bearing.
- Evidence about durable transfer, integrated multimodal systems, and learners with
  disabilities remains inadequate.

The project therefore tests whether persistent, multimodal orchestration grounded in
learner evidence produces stronger independent capability than conversational use of
a general model.

## System requirements

The proposed architecture includes:

- a portable learner state that separates declared, observed and inferred data;
- bounded diagnostic hypotheses and discriminating probes;
- checked renderers for speech, diagrams, notebooks, animation, applications and
  simulations;
- specialist functions for diagnosis, domain knowledge, representation, access and
  evaluation, coordinated by one accountable orchestrator;
- support fading, delayed retrieval and independent graduation tasks;
- multiple input and response modes, learner control and data minimization;
- an interchange for authors and educators to contribute attributable instructional
  techniques;
- outcome evaluation against a strong general-model baseline, including subgroup
  gap change.

## Repository map

| Path | Purpose |
|---|---|
| [`research/raw/`](research/raw/) | Research reports covering evidence, systems, media, access, agents and markets |
| [`survey/`](survey/) | Thematic source chapters used by the evidence-atlas build |
| [`PAPER.md`](PAPER.md) | Edited manuscript |
| [`ATLAS.md`](ATLAS.md) | Generated living evidence atlas |
| [`docs/`](docs/) | Public dashboard, deck, paper, atlas and demos |
| [`evidence/`](evidence/) | Builds, validation, reviews and reproducible experiments |
| [`process/TASK-TRACEABILITY.md`](process/TASK-TRACEABILITY.md) | Vision-to-artifact gap audit |
| [`TASK.md`](TASK.md) | Owner requests, status and unresolved owner decisions |

## Build and validation

Render the edited paper:

```bash
python3 evidence/build-manuscript.py
```

Rebuild the long evidence atlas:

```bash
python3 evidence/build-paper.py --html
```

Run the public-artifact checks:

```bash
python3 evidence/check-voice.py --strict
python3 evidence/check-stance.py --strict
node evidence/check-links.mjs
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH=/snap/bin/chromium node evidence/test-pages.mjs
```

## Current boundary

The research, architecture and public narrative now describe the same product. The
integrated learning system has not been built or validated. Before fundraising or a
trial, the owner must confirm the first learner, buyer, domain, geography and external
outcome; name the founding team; and supply the operating plan and raise.

Contributions are most useful when they add a primary source, expose a reproducible
failure, improve an access requirement, or propose an experiment that distinguishes
the architecture from an excellent general-model baseline.

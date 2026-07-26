---
title: "Assessment Becomes an Evidence Architecture"
section: F1-assessment-reconstruction
status: draft
date: 2026-07-25
---

# Assessment Becomes an Evidence Architecture

![An assessment assurance ladder rises from activity through immediate response, interactive explanation, executable performance, delayed independent transfer, and a longitudinal learner-owned portfolio, while every rung records support conditions and feeds the next teaching action](../assets/diagrams/assessment-assurance-ladder.svg)

*AI makes artifacts abundant. It can also make evidence abundant.*

An essay, solution, presentation, program, image, or report used to stand in for
several claims at once. Frontier generation pulls them apart:

| Claim | What the assessor wants to know |
|---|---|
| Product | Is this artifact good, correct, useful, or beautiful? |
| Process | What did the learner do, delegate, verify, and revise? |
| Capability | What can the learner do again under declared support conditions? |
| Learning | What changed between two points in time? |

The old [85-source assessment reconstruction](../research/raw/F1-assessment-reconstruction.md)
established that distinction and documented the detector era. It is now a source
archive.

The July 2026 opportunity is positive: build a different instrument for each
claim and connect them into one living evidence graph.

## Declare the claim before the task

Every assessment event should name:

```yaml
construct: "causal reasoning about feedback loops"
claim: product | process | capability | learning
support:
  ai: none | retrieval | hints | tutor | full collaborator
  human:
  references:
  accessibility:
evidence:
  response:
  evaluator:
  uncertainty:
```

“Unaided” remains an important condition, especially for a foundational core.
It is not the only authentic condition. Future capability also includes
directing tools, checking sources, testing output, recovering from failure, and
knowing what not to delegate.

The credential should make that boundary visible.

A July 2026 paper on
[cognitive stewardship](https://arxiv.org/abs/2607.19988) audits public guidance
from 30 universities and reaches the same frontier: AI-use categories are
insufficient unless the institution states what may be delegated, what the
learner must demonstrate, and which evidence protects the credential’s meaning.
`RESEARCH`

## The assurance ladder

### Level 0: activity

Opened, watched, clicked, completed, spent time.

This shows opportunity to learn, not capability.

### Level 1: immediate response

The learner selects, recalls, solves, labels, or corrects a fresh item. This
updates state quickly but is sensitive to guessing, cues, and surface similarity.

### Level 2: interactive explanation

The learner explains a choice, repairs an error, responds to a counterexample,
or changes an assumption.

Full-duplex voice and multimodal models make short adaptive oral assessment
cheap and multilingual. Equivalent modes—typed viva, AAC, asynchronous video,
visual selection, physical demonstration, or human-supported response—must have
equal authority when speech is not the construct.

A 2026
[AI-resilient assessment framework](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1841682/full)
includes structured oral defenses, scoring examples, AI-use disclosure, and
alternative modes for communication disabilities. `RESEARCH`

### Level 3: executable or observable performance

A proof compiles. Code passes public and withheld tests. An experiment’s
measurements fit the claimed model. A circuit works. A learner teaches a concept
and handles a misconception. A team coordinates around a real artifact.

Here the performance carries part of its own warrant.

### Level 4: delayed independent transfer

The learner receives a new problem, later, in a changed context, without tutor
support.

This is the strongest routine learning claim.

### Level 5: longitudinal portfolio

Projects, transfer probes, explanations, collaborations, reflections, and human
validations accumulate into a program-level claim. No single artifact is
load-bearing. The learner controls what becomes a credential.

## Generated probes make low-stakes assessment abundant

One checked concept specification can create fresh:

- recall and application items;
- misconception-targeted distractors;
- counterexamples;
- oral follow-up questions;
- role-play situations;
- simulation perturbations;
- parallel forms across language and modality.

A 2026
[large-scale study of AI-generated exams](https://doi.org/10.1609/aaai.v40i45.41205)
used iterative generation, critique, and revision. Item-response analysis found
the generated questions performed comparably to expert-created standardized-
exam questions for the studied sample. `MEASURED-BENCH`

[AI-GENIE](https://facultyprofiles.vanderbilt.edu/esploro/outputs/journalArticle/Generative-psychometrics-via-AI-GENIE-Automatic-item/991044886709303276)
connects item generation to psychometric evaluation, while its
[open implementation](https://arxiv.org/abs/2603.28643) makes the workflow
reproducible. `RESEARCH`

The operational rule is generous and rigorous:

> Generate freely for low-stakes teaching. Promote an item or scoring policy
> only after grounding, answerability, executable checks, access review,
> adversarial review, calibration, and subgroup evidence justify its load.

## Adaptive assessment should stop when the decision is precise

A 2026 IRT-based adaptive test over 38 language models correlated 0.988 with
full-bank proficiency estimates while using 1.3% of the items.
[`MEASURED-BENCH`](https://arxiv.org/abs/2603.23506)

The examinees were models, but the efficiency principle transfers: do not make
every learner answer the same long test. Choose the next probe that most reduces
uncertainty or distinguishes plausible misconceptions, then send the result
directly to the teaching router.

Assessment and teaching become one loop.

## Assessment can hide inside meaningful work

The mentor can produce evidence without stopping a project for an artificial
exam:

- ask for a prediction before a simulation;
- request a rationale before a design choice;
- insert a counterexample during debugging;
- ask the learner to compare their solution with an AI proposal;
- change one constraint and observe adaptation;
- invite a peer to challenge the explanation;
- revisit the concept weeks later in a different project.

The work remains meaningful. The probes make the underlying capability visible.

## AI collaboration is itself assessable

A learner can demonstrate:

- defining the intended result;
- supplying the right context;
- decomposing and delegating;
- checking evidence and assumptions;
- testing generated output;
- recognizing limits of authority;
- revising the artifact and workflow;
- defending the final decision;
- performing a declared independent core.

The compact process record is:

```text
goal → delegation → evidence checked → change made
→ rejected output → remaining uncertainty → independent defense
```

That is enough to support a capability claim. A raw, permanent prompt transcript
is unnecessary.

## Human judgment moves upward

AI can generate, administer, adapt, score structured elements, summarize
evidence, and route uncertain cases.

Humans retain authority over:

- which capability deserves certification;
- local and cultural validity;
- accommodations and equivalent modes;
- high-stakes edge cases;
- conflicting evidence;
- professional and ethical judgment;
- credential issuance.

This allocation expands the reach of expert judgment instead of automating it
away.

## Evidence should travel without the dossier

Open Badges, Comprehensive Learner Records, xAPI, and verifiable credentials
provide containers. A July 2026
[privacy-preserving credential architecture](https://doi.org/10.1016/j.jisa.2026.104465)
demonstrates granular selective disclosure. `RESEARCH`

A learner should be able to share:

```yaml
capability: "models nonlinear systems with justified assumptions"
evidence:
  - verified project
  - independent defense
  - 30-day transfer probe
support:
  project: "AI collaborator disclosed"
  defense: "references allowed; no tutor"
  transfer: "no AI or human help"
uncertainty:
```

The receiving institution does not need the raw learning history.

## The universal-access payoff

Assessment becomes more equitable when it is:

- available in the learner’s language;
- usable through voice and low-cost shared devices;
- runnable offline with later synchronization;
- generated from local curriculum authority;
- available through equivalent response modes;
- low stakes until calibrated;
- followed immediately by useful teaching;
- exportable as learner-owned evidence.

This reduces dependence on scarce item writers, testing centers, graders, and
one-shot gatekeeping events.

The new evidence graph is:

```text
meaningful action
  → generated micro-probe
  → response + support conditions
  → adaptive explanation or defense
  → executable / observable performance
  → delayed independent transfer
  → longitudinal human-reviewed portfolio
  → selectively disclosed credential
  → next teaching action
```

The rebuilt system does not chase an AI-free past. It observes real capability
more often, through more modalities, across more contexts, with clearer support
conditions—and puts the resulting evidence in the learner’s hands.

---
title: "Assessment after abundant artifact generation"
wave: F
section: F1
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 25
---

# F1 — Assessment Becomes an Evidence Architecture

## Executive finding

When AI can cheaply generate an essay, solution, presentation, program, image,
or report, the submitted artifact no longer answers every question educators
used to ask of it.

That is not the collapse of assessment. It is the separation of four claims:

| Claim | Question |
|---|---|
| Product | Is this artifact good, correct, useful, or beautiful? |
| Process | What work did the learner perform, delegate, verify, and revise? |
| Capability | What can the learner produce or decide again under declared support conditions? |
| Learning | What changed in the learner between two points in time? |

The July 2026 opportunity is to build a different instrument for each claim and
connect them in a continuous evidence graph.

The strongest design is not an “AI-proof assignment.” It is:

> **A sequence of generated probes, live explanations, executable checks, real
> performances, delayed transfer, and human judgments whose support conditions
> are explicit and whose evidence belongs to the learner.**

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner outcome |
| `MEASURED-BENCH` | Disclosed benchmark or psychometric evaluation |
| `OBSERVED` | Field study, standard, or public implementation |
| `VENDOR` | Provider-reported capability |
| `RESEARCH` | Current research system or proposal |
| `INFERENCE` | Assessment architecture consequence |

## 1. Preserve the useful insight, leave the detector era behind

The original 85-source
[assessment reconstruction](F1-assessment-reconstruction.md) established three
durable ideas:

1. an assessment is an inference from evidence to a claim;
2. product, process, capability, and learning are different claims;
3. AI-text detection does not establish capability or learning.

That document is retained as a source archive. The main 2026 story is what can
now be built, not institutional panic about text provenance.

A July 2026 paper on
[cognitive stewardship](https://arxiv.org/abs/2607.19988) reaches a compatible
frontier conclusion after auditing public guidance from 30 universities:
permissions are not enough; assessment must state what can be delegated, what
the learner must demonstrate, and which evidence preserves credential validity.
`RESEARCH`

## 2. Start by declaring the claim and support condition

Every assessment event should state:

```yaml
claim:
  construct: "causal reasoning about feedback loops"
  type: product | process | capability | learning
task:
  context:
  novelty:
  modality:
support:
  ai: none | retrieval | hints | tutor | full collaborator
  human:
  references:
  accessibility:
evidence:
  response:
  trace:
  evaluator:
  uncertainty:
```

“Unaided” is one useful condition, not the only authentic one. A future
engineer’s capability includes directing tools, checking output, recovering from
failure, and knowing what not to delegate. A foundational mathematics claim may
still require an independent core.

The credential must make that boundary visible.

## 3. The assessment assurance ladder

### Level 0 — Activity

Examples: opened, watched, clicked, completed, spent time.

Use only to explain whether the learner had an opportunity to learn. Activity is
not capability.

### Level 1 — Immediate response

Examples: selected, recalled, solved, labeled, or corrected a fresh item.

This provides a quick state update. It is vulnerable to guessing, cueing, and
surface similarity, so it should not carry a high-stakes claim alone.

### Level 2 — Interactive explanation and defense

The assessor asks the learner to explain a choice, compare alternatives, repair
an error, respond to a counterexample, or change an assumption.

Frontier voice and multimodal models make adaptive oral assessment inexpensive
and multilingual. The goal is not a theatrical viva. It is a short, responsive
sample of reasoning.

A current
[AI-resilient assessment framework](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1841682/full)
includes structured oral-defense protocols, worked scoring examples, AI-use
disclosure, and alternative verification modes for communication disabilities.
`RESEARCH`

### Level 3 — Executable or observable performance

Examples:

- a proof compiles;
- code passes public and withheld tests;
- an experiment’s measurements agree with the claimed model;
- a circuit, design, or repair works;
- a simulation obeys declared invariants;
- a learner teaches a concept and handles a misconception;
- a team coordinates around a real shared artifact.

The product carries part of its own warrant.

### Level 4 — Delayed independent transfer

The learner receives a new problem, later, in a changed context, without the
tutor. This is the strongest routine learning claim.

### Level 5 — Longitudinal capability portfolio

Multiple low-stakes observations, projects, transfer probes, reflections,
collaborations, and human validations form a program-level claim. No single
artifact is load-bearing.

The learner controls selective disclosure into a verifiable credential.

## 4. Generation makes assessment abundant and adaptive

Generative systems can produce parallel probes, explanations, distractors,
counterexamples, role-play situations, simulations, and oral follow-ups from a
concept specification. This makes frequent, low-stakes measurement possible
without a teacher authoring every item.

It also creates an assurance obligation.

The 2026
[large-scale field study of AI-generated exams](https://doi.org/10.1609/aaai.v40i45.41205)
used iterative generation, critique, and revision; item-response analysis found
the generated questions performed comparably to expert-created standardized-
exam questions for the studied sample. `MEASURED-BENCH`

[AI-GENIE](https://facultyprofiles.vanderbilt.edu/esploro/outputs/journalArticle/Generative-psychometrics-via-AI-GENIE-Automatic-item/991044886709303276)
connects automatic item generation with network-integrated psychometric
evaluation. Its open
[AIGENIE implementation](https://arxiv.org/abs/2603.28643) makes early scale
development reproducible. `RESEARCH`

A 2026 comparison of
[ChatGPT-generated reading tests and CET-4](https://doi.org/10.1177/07342829261444828)
supports low-stakes supplementary use while still requiring refinement before
high-stakes use. `MEASURED-BENCH`

The rule is:

> Generate freely for low-stakes teaching; promote an item or scoring policy
> only after content, bias, difficulty, discrimination, reliability, and
> transfer evidence justify its load.

## 5. The generated-item assurance pipeline

Every generated probe should pass:

1. **construct specification** — which knowledge or reasoning is sampled;
2. **source grounding** — which facts and authorities are allowed;
3. **answerability** — enough information, one defensible scoring interpretation;
4. **executable checks** — units, equations, code, geometry, simulations, or
   reference calculations where available;
5. **access review** — language and modality do not introduce irrelevant
   difficulty;
6. **adversarial review** — no formatting, wording, length, or cultural shortcut;
7. **synthetic prior** — estimated difficulty and likely misconception coverage;
8. **human calibration** — real response data updates difficulty,
   discrimination, scoring, and subgroup performance;
9. **exposure control** — freshness and leakage tracking;
10. **retirement or repair** — failed items leave the active pool.

The existing
[generated-assessment validity chapter](../../survey/12-assessment-as-evidence-stream.md)
specifies this pipeline in detail.

## 6. Adaptive testing becomes continuous formative measurement

Adaptive assessment should stop when the decision is precise enough—not when
every learner has answered the same number of questions.

A 2026 CAT study over 38 language models found that an IRT-based adaptive test
correlated 0.988 with full-bank proficiency estimates while using 1.3% of the
items. Although the examinees were models, the result demonstrates the
efficiency available from calibrated adaptive selection.
[`MEASURED-BENCH`](https://arxiv.org/abs/2603.23506)

The current
[PBAT framework](https://www.ijiet.org/show-242-3318-1.html) combines retrieval
grounding, item-response theory, and adaptive sequencing. Its reported retention
result is promising but remains one study rather than a universal estimate.
`MEASURED-BENCH`

For learners, the adaptive engine should choose the next probe that most reduces
uncertainty or discriminates between plausible misconceptions—and then hand the
result directly to the teaching router.

## 7. Assessment can occur inside real work

The mentor can create evidence without interrupting a project with a separate
test:

- ask for a prediction before a simulation runs;
- request a verbal rationale before a design choice;
- insert a counterexample into a debugging session;
- ask the learner to compare their output with an AI proposal;
- change one constraint and observe adaptation;
- invite a peer to challenge the explanation;
- revisit the same concept weeks later in a different project.

This is assessment as a living evidence stream.

The activity remains meaningful; the probes make the underlying capability
visible.

## 8. AI collaboration should be assessed as a real capability

Learners should be able to demonstrate:

- defining what outcome is wanted;
- supplying the right context;
- decomposing and delegating work;
- inspecting sources and assumptions;
- testing generated output;
- recognizing when the model is outside its authority;
- revising the artifact and the workflow;
- explaining the final decision;
- performing a declared independent core.

The relevant record is not a raw prompt transcript. It is a compact decision
trace:

```text
goal → delegation → evidence checked → change made
→ rejected output → remaining uncertainty → independent defense
```

This respects privacy while preserving the capability claim.

## 9. Full-duplex assessment can be brief, multilingual, and accessible

Voice, screen, camera, handwriting, diagram, and tool observation let assessment
sample how a learner thinks and acts.

For a mathematical solution, the mentor can:

1. ask what the learner predicts;
2. observe the next step;
3. point to a specific transformation;
4. change a coefficient;
5. ask whether the method still works;
6. request a short explanation;
7. schedule a new transfer problem.

Alternative modes—typed viva, asynchronous video, AAC, visual choice, physical
demonstration, human-supported response—must carry equivalent authority when
speech is not an appropriate construct.

Assessment should remove construct-irrelevant barriers, not reward conformity to
one response channel.

## 10. Human judgment moves upward

AI can generate probes, administer conversations, score structured components,
summarize evidence, surface uncertainty, and identify where expert review adds
the most value.

Humans retain authority over:

- the capability worth certifying;
- local and cultural validity;
- high-stakes edge cases;
- consequential accommodations;
- interpretation across conflicting evidence;
- professional and ethical judgment;
- credential issuance.

A June 2026 system for
[AI assessment of human tutors](https://arxiv.org/abs/2606.18617) analyzes
authentic tutoring transcripts to connect training performance with real
practice. `RESEARCH`

This illustrates the right allocation: machines expand observation and
consistency; humans own the consequential interpretation.

## 11. Portable evidence without permanent surveillance

Open Badges 3.0, Comprehensive Learner Records, xAPI, and verifiable credentials
provide an interoperability base.

A July 2026
[privacy-preserving credential architecture](https://doi.org/10.1016/j.jisa.2026.104465)
combines verifiable credentials with granular selective disclosure.
`RESEARCH`

The learner should be able to share:

```yaml
capability: "models nonlinear relationships with justified assumptions"
evidence:
  - verified project
  - independent oral defense
  - 30-day transfer probe
support_conditions:
  project: "AI collaborator disclosed"
  defense: "references allowed; no tutor"
  transfer: "no AI or human help"
issuer:
validity_window:
uncertainty:
```

The receiving institution does not need the raw conversation history.

## 12. Universal access consequence

Abundant assessment changes opportunity when it is:

- available in the learner’s language;
- runnable through voice or low-cost shared devices;
- usable offline with later synchronization;
- composed from local curriculum authority;
- accessible through equivalent response modes;
- low stakes until calibrated;
- connected immediately to another teaching action;
- exportable as learner-owned evidence.

This reduces dependence on scarce item writers, testing centers, graders, and
one-shot gatekeeping events.

## 13. The reference evidence graph

```text
meaningful learner action
  → generated micro-probe
  → scored response + support conditions
  → short adaptive explanation or defense
  → executable / observable performance
  → delayed independent transfer
  → longitudinal human-reviewed portfolio
  → selectively disclosed credential
  → next teaching action
```

Each edge keeps provenance, evaluator, uncertainty, accessibility conditions,
and learner permissions.

## 14. Final synthesis

AI makes artifacts abundant. It can also make evidence abundant.

The rebuilt assessment system does not chase an impossible AI-free past. It
samples real capability more often, in more modalities, across more contexts,
and with clearer support conditions than the old essay-or-exam binary.

It helps the learner answer:

- What can I do now?
- What can I do with tools?
- What can I do independently?
- What changed?
- What should I learn next?
- Which evidence do I want to carry forward?

That is assessment worthy of a universal mentor.

## Sources

1. Source archive, [The Collapse and Reconstruction of Assessment](F1-assessment-reconstruction.md), 85-source evidence spine.
2. Yao, [What Does the Credential Still Certify?](https://arxiv.org/abs/2607.19988), 2026.
3. [AI-resilient assessment framework](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1841682/full), 2026.
4. [Large-scale field study of AI-generated exams](https://doi.org/10.1609/aaai.v40i45.41205), AAAI 2026.
5. [AI-GENIE](https://facultyprofiles.vanderbilt.edu/esploro/outputs/journalArticle/Generative-psychometrics-via-AI-GENIE-Automatic-item/991044886709303276), 2026.
6. [AIGENIE R package and tutorial](https://arxiv.org/abs/2603.28643), 2026.
7. [Generated reading-test psychometrics](https://doi.org/10.1177/07342829261444828), 2026.
8. [CAT for cost-effective proficiency estimation](https://arxiv.org/abs/2603.23506), 2026.
9. [PBAT](https://www.ijiet.org/show-242-3318-1.html), 2026.
10. [AI assessment of authentic tutor practice](https://arxiv.org/abs/2606.18617), 2026.
11. [Privacy-preserving credential architecture](https://doi.org/10.1016/j.jisa.2026.104465), 2026.
12. 1EdTech, [Wellspring / CLR horizon](https://www.1edtech.org/sites/default/files/media/docs/2025/Wellspring_Phase_I_Report.pdf), 2025.
13. [I2IDL](https://www.i2idl.org/), current 2026.
14. Project research, [Generated assessment validity](C2-generated-assessment-validity-2026.md), 2026.
15. Project synthesis, [Assessment as an evidence stream](../../survey/12-assessment-as-evidence-stream.md), 2026.
16. Google, [Study notebooks and no-cost practice tests](https://blog.google/products-and-platforms/products/education/iste-students-2026/), 2026.
17. Khan Academy, [Building a better AI tutor](https://blog.khanacademy.org/how-khan-academy-is-building-a-better-ai-tutor-our-most-recent-learnings/), 2026.
18. [LongTutor](https://aclanthology.org/2026.acl-long.1371/), 2026.
19. [EduAgentBench](https://arxiv.org/abs/2605.14322), 2026.
20. [Strategies for creating uncertainty to trigger critical thinking](https://arxiv.org/abs/2602.00026), 2026.
21. [E2V-Bench](https://arxiv.org/abs/2605.31212), 2026.
22. [EduIllustrate](https://arxiv.org/abs/2604.05005), 2026.
23. Ed-Fi Alliance, [Data Standard in the Age of AI](https://docs.ed-fi.org/getting-started/provider-playbook/implementation/ed-fi-data-standard-in-the-age-of-ai/), 2026.
24. [Learning Analytics by Design](https://publica.fraunhofer.de/entities/publication/0890e6a7-df86-4001-a2f6-c270bc3e7398), 2026.
25. World Bank, [From Chalkboards to Chatbots](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324), 2025.

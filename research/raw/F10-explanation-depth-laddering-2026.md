---
title: "Explanation depth laddering without conceptual debt"
wave: F
section: F10
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
---

# F10 — Explanation Depth Laddering Without Conceptual Debt

## Executive finding

Frontier models can generate many explanations. The unsolved design problem is
how to make four explanations of the **same concept** differ in prerequisite
load, representation, formalism, and edge cases while preserving a common truth.

This section defines the missing primitive:

> **A depth ladder is a versioned family of explanations connected by explicit
> invariants, declared omissions, prerequisite tests, and transfer checks.**

“ELI10/15/20/25” names sophistication bands, not ages or identities. A
ten-year-old expert may enter at ELI20. An adult new to a field may begin at
ELI10. Entry comes from demonstrated prior knowledge and current purpose, never
from demographics or a style preference.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-RCT` | Randomized learner-outcome comparison |
| `MEASURED-BENCH` | Human-rated, deployed, or benchmarked system |
| `OBSERVED` | Inspectable system or standard |
| `INFERENCE` | Proposed design derived from evidence |

## 1. Why July 2026 changes the opportunity

### 1.1 Adaptation is now operational at useful scale

[PathBuilder](https://aclanthology.org/2026.acl-demo.50/) combines
curriculum-aligned diagnostics, retrieval-grounded generation, and automated
validation. It reports a 17,758-item bank, including 1,018 expert-approved
generated items, and a real deployment with 75 matched learners: 37.9 percentage
points mean gain, normalized gain 0.760, and Cohen’s d = 0.98.
`MEASURED-BENCH`, not randomized.

[TeachCraft](https://aclanthology.org/2026.acl-long.1328/) decomposes lesson
authoring into source-role classification, objective sequencing, and schema-bound
generation. On 40 expert lessons with heterogeneous sources, it reports a 67.8%
human-evaluation win rate and 79.6% model-evaluation win rate against eight
baselines. `MEASURED-BENCH`

[Adaptive educational readings](https://aclanthology.org/2026.bea-1.63/) now
have a theory-grounded simulation framework connecting open content, a shared
ontology, one-objective reading–assessment pairs, Bayesian knowledge tracing,
encoding, integration, memory, and misconception revision. `MEASURED-BENCH`

The new capability is not simply personalization of tone. It is a closed loop:

```text
measured prerequisite state
    → select explanation contract
    → generate from grounded sources
    → ask learner to act
    → update state
    → move up, down, or sideways
```

### 1.2 Explanation diversity can improve performance

A 2026 randomized study of
[971 introductory-programming students](https://arxiv.org/abs/2606.28882)
compared generic model explanations with multiple explanations emphasizing
different aspects. Open-ended response accuracy was about 7.7% higher in the
diverse-explanation condition, without a reported difference in perceived
cognitive load. `MEASURED-RCT`

[ELI-Why](https://aclanthology.org/2025.findings-acl.1306/) evaluates pedagogical
utility against differing learner information needs rather than treating one
reference explanation as universally correct. `MEASURED-BENCH`

A July 2026 study generated
[1,072 code explanations](https://arxiv.org/abs/2607.17022) from six open models
against five inclusive problem-solving styles and identified 13 linguistic
adaptations. `MEASURED-BENCH`

`INFERENCE`: variation is useful when each representation exposes a different
structure and the learner compares or selects based on a task. Random stylistic
variation is not a depth ladder.

## 2. The operational level taxonomy

The four levels are defined along six axes. They are not word-count targets.

| Axis | ELI10 — enter | ELI15 — connect | ELI20 — formalize | ELI25 — extend |
|---|---|---|---|---|
| Prerequisites | everyday causal knowledge | named prior concepts | algebraic/domain foundations | field conventions and proof maturity |
| Vocabulary | concrete verbs; essential terms introduced in place | standard terms with plain paraphrase | canonical technical vocabulary | compressed expert language plus ambiguity notes |
| Representation | manipulable object, story, sketch | two linked representations | formal notation + derivation + executable model | multiple formalisms and research artifacts |
| Abstraction | one mechanism in one case | invariant across contrasting cases | general model with assumptions | model class, proof obligations, competing abstractions |
| Edge cases | one carefully chosen boundary if load permits | canonical counterexample | domain limits and failure case | adversarial cases, exceptions, unresolved frontier |
| Learner action | predict, sort, manipulate, explain | translate, compare, vary | derive, prove, implement, diagnose | critique, generalize, design, research |

### ELI10 — enter through causal structure

Goal: the learner can *act on* the concept before mastering its formal language.

Required:

- one causally coherent mechanism;
- familiar or locally available objects;
- visible contrasts;
- one action and one prediction;
- names for only the terms needed to continue;
- no statement the later model must reverse.

May omit:

- general proof;
- rare cases;
- formal notation;
- competing definitions.

May never imply:

- correlation is causation;
- a metaphorical entity literally exists;
- a drawing’s accidental scale is a law;
- a default case is universal.

### ELI15 — connect representations

Goal: the learner recognizes the same invariant in words, diagrams, examples,
tables, and light notation.

Required:

- explicit mapping between at least two representations;
- a contrast case;
- conditions under which the rule applies;
- an invitation to translate or reconstruct.

### ELI20 — formalize and derive

Goal: the learner can generate results from the model rather than recall a
description.

Required:

- definitions and notation;
- assumptions;
- derivation or proof;
- executable example where possible;
- canonical counterexample;
- relationship to the ELI10/15 model.

### ELI25 — extend and contest

Goal: the learner can choose, criticize, and extend models.

Required:

- competing formulations;
- proof obligations and boundary conditions;
- historical or disciplinary disagreements when material;
- unresolved questions;
- transfer to unfamiliar or research-level cases;
- primary artifacts: paper, dataset, code, specification, or experiment.

## 3. The fidelity contract

A rung is valid only when it declares four things.

### 3.1 Invariants

Statements preserved at every level.

Example for natural selection:

```yaml
invariants:
  - individuals in a population vary
  - some variation affects reproduction in an environment
  - heritable variants can change in frequency across generations
  - populations evolve; individuals do not evolve by need
```

### 3.2 Declared omissions

Details intentionally deferred:

```yaml
omitted_at_ELI10:
  - population-genetic equations
  - drift and gene flow
  - genotype-phenotype mapping
  - frequency-dependent selection
```

An omission is not a false statement. The learner can see what lies beyond the
current view.

### 3.3 Marked approximations

An approximation includes its condition and exit ramp:

```yaml
approximation:
  statement: "Treat the surface as frictionless for this first model."
  valid_when: "friction is small relative to the applied forces"
  breaks_when: "dissipation materially changes acceleration or energy"
  next_rung: "add kinetic friction and compare trajectories"
```

### 3.4 Forbidden implications

The generator and verifier test for misconceptions a simple representation might
plant:

```yaml
must_not_imply:
  - heavier objects fall faster in a vacuum
  - force is required to maintain constant velocity
  - the drawn force arrows are literal objects attached to the body
```

This is the rule:

> **A simpler explanation may reduce resolution; it may not change the sign,
> direction, ontology, causality, or domain of the underlying relationship.**

## 4. Why representation must fade and connect

[Goldstone and Son](https://doi.org/10.1037/0096-3445.134.1.69) studied transfer
from concrete to idealized simulations. [Fyfe et al.](https://doi.org/10.1007/s10648-014-9249-3)
synthesize the concreteness-fading approach. `MEASURED-RCT` / synthesis

The ladder implements a concrete → connected → idealized → formal progression
when the learner needs it, while allowing experts to enter at the formal level.

[Gentner’s structure-mapping theory](https://doi.org/10.1207/s15516709cog0702_3)
explains why a useful analogy preserves relations rather than superficial
attributes. [Ainsworth’s DeFT framework](https://doi.org/10.1016/j.learninstruc.2006.03.001)
organizes multiple representations around complementary information,
constraining interpretation, and deeper understanding.

`INFERENCE`: every analogy and representation gets an explicit mapping table:

| Source element | Target element | Preserved relation | Where analogy breaks |
|---|---|---|---|

[Teaching Through Analogies](https://aclanthology.org/2026.bea-1.59/) provides a
current modular retrieval and generation pipeline; the fidelity contract adds
the break-condition needed for laddered instruction. `MEASURED-BENCH`

## 5. Adaptive entry and the expertise-reversal rule

[Kalyuga et al.](https://doi.org/10.1207/S15326985EP3801_4) describe the
expertise-reversal effect: supports useful to novices can become redundant and
counterproductive as knowledge grows. The rule is not “simple is safe.”

Entry selection uses:

1. a brief reconstruction or prediction task;
2. prerequisite evidence from the learner-owned state;
3. the learner’s current goal and time horizon;
4. confidence and a reversible probe.

Policy:

```text
if prerequisite evidence is strong:
    enter at the highest rung whose transfer probe passes
elif evidence is uncertain:
    offer a compact contrast task, not a long beginner explanation
else:
    enter where the first meaningful action succeeds
```

The learner can always say:

- “show the formal version”;
- “give me the missing rung”;
- “use a physical example”;
- “tell me what this simplification hides”;
- “test whether I am ready to skip ahead.”

Preference selects among valid representations at a rung. Evidence selects depth.

## 6. Climbing requires learner generation

[Chi et al.](https://doi.org/10.1207/s15516709cog1302_1) connect
self-explanation to learning from examples. Current 2026
[knowledge-component generation](https://aclanthology.org/2026.bea-1.18/) uses
LLMs to process classroom self-explanations and surface misconceptions in real
time. `MEASURED-RCT` / `MEASURED-BENCH`

A rung is passed when the learner can:

1. reconstruct its model;
2. translate it to another representation;
3. predict a new case;
4. explain the approximation and its break condition;
5. connect it to the next rung’s added structure.

Reading a harder explanation is not climbing.

## 7. The compiler

An explanation ladder is generated from:

```yaml
concept_contract:
  canonical_claims: [...]
  prerequisites: [...]
  invariants: [...]
  misconceptions: [...]
  representations: [...]
  executable_checks: [...]
  source_spans: [...]
levels:
  ELI10: {max_prerequisites: 2, formalism: none, action: predict}
  ELI15: {representations: 2, action: translate}
  ELI20: {derivation: required, action: derive}
  ELI25: {competing_models: required, action: critique}
```

The generation pipeline:

1. grounds canonical claims and prerequisites;
2. creates the full formal model first;
3. extracts invariant relationships;
4. compiles lower-resolution representations;
5. labels omissions and approximations;
6. adversarially checks forbidden implications;
7. produces bridge tasks between adjacent rungs;
8. renders accessible and local-language forms;
9. field-tests entry and transfer.

Creating the formal source first is important: simplification is a controlled
projection of a known structure, not a model improvising from a child-directed
tone prompt.

## 8. Universal-access consequences

- A community server caches the concept contract and four compact text/vector
  rungs, generating rich media only when available.
- The same invariant graph supports local-language labels and culturally familiar
  examples without localizing the science away.
- Speech, sign, tactile, visual, and physical forms share the same fidelity
  checks.
- Teachers can inspect exactly what each rung omits and override entry.
- A learner who has expertise from work, family, or community practice is not
  forced through school-grade assumptions.

## 9. Acceptance tests

- [ ] Each rung states prerequisites, vocabulary, representation, formalism,
      edge cases, and learner action.
- [ ] Invariants are identical across rungs.
- [ ] Omissions are visible and linked forward.
- [ ] Every approximation includes validity and break conditions.
- [ ] Named misconceptions are tested as forbidden implications.
- [ ] Analogy mappings include where the analogy breaks.
- [ ] Entry comes from demonstrated evidence, with a reversible probe.
- [ ] Each bridge requires reconstruction, translation, prediction, or transfer.
- [ ] Source claims and executable checks survive localization.
- [ ] The learner can inspect and choose to move.

## Source index

1. PathBuilder — [ACL 2026](https://aclanthology.org/2026.acl-demo.50/)
2. TeachCraft — [ACL 2026](https://aclanthology.org/2026.acl-long.1328/)
3. Adaptive readings — [BEA 2026](https://aclanthology.org/2026.bea-1.63/)
4. Diverse programming explanations — [arXiv:2606.28882](https://arxiv.org/abs/2606.28882)
5. Problem-solving-style adaptation — [arXiv:2607.17022](https://arxiv.org/abs/2607.17022)
6. ELI-Why — [ACL 2025](https://aclanthology.org/2025.findings-acl.1306/)
7. Teaching Through Analogies — [BEA 2026](https://aclanthology.org/2026.bea-1.59/)
8. Knowledge-component generation — [BEA 2026](https://aclanthology.org/2026.bea-1.18/)
9. IntelliCode learner model — [EACL 2026](https://aclanthology.org/2026.eacl-demo.10/)
10. Prompt-optimized tutors — [arXiv:2605.27088](https://arxiv.org/abs/2605.27088)
11. Goldstone & Son — [concreteness and transfer](https://doi.org/10.1037/0096-3445.134.1.69)
12. Fyfe et al. — [concreteness fading](https://doi.org/10.1007/s10648-014-9249-3)
13. Gentner — [structure mapping](https://doi.org/10.1207/s15516709cog0702_3)
14. Ainsworth — [DeFT](https://doi.org/10.1016/j.learninstruc.2006.03.001)
15. Kalyuga et al. — [expertise reversal](https://doi.org/10.1207/S15326985EP3801_4)
16. Chi et al. — [self-explanation](https://doi.org/10.1207/s15516709cog1302_1)
17. Posner et al. — [conceptual change](https://doi.org/10.1002/sce.3730660207)
18. diSessa — [knowledge in pieces](https://doi.org/10.1207/s15327809jls0202_2)
19. Meyer & Land — [threshold concepts](https://www.ee.ucl.ac.uk/~mflanaga/thresholds.html)
20. Bruner — [The Process of Education](https://books.google.com/books?id=S6FKW90QY40C)

## Decision

**Implement explanation depth as a compiler target, not a tone setting.** Every
important concept gets a formal source, a fidelity thread, four operational
rungs, bridge tasks, and adaptive entry. Frontier models make the variants cheap;
the contract makes them cumulative.

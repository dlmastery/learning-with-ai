---
title: "Reactive computational learning documents at the July 2026 frontier"
wave: A
section: A3
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
---

# A3 — Reactive Computational Learning Documents

## Executive finding

The notebook should no longer be a sequential transcript of code cells with
invisible session state.

The correct substrate for an AI-native book is a **reactive semantic graph**:
sources, definitions, parameters, computations, visualizations, explanations,
tests, and practice objects declare their dependencies. Change one assumption
and every affected view updates automatically. Unaffected work stays cached.
The visible document always corresponds to the executable state.

This is already technically possible:

- Pluto 1.0 and marimo construct dependency graphs and re-evaluate affected
  cells;
- JupyterLite, Pyodide, and marimo WASM run notebooks in a browser;
- Observable and Vega-Lite provide reactive, declarative views;
- frontier AI generates code and applications, executes Python, reads results,
  and edits artifacts;
- tests, units, schemas, sources, and grounding records can be nodes in the same
  graph.

The learning primitive is:

> The learner changes a meaningful input, predicts which downstream claims
> should change, runs the graph, explains the result, and transfers the model.

The mentor watches declared learning events rather than scraping an opaque UI.

---

## 1. Why reactive structure matters

A traditional notebook allows:

- cells to run out of order;
- a deleted definition to remain in memory;
- plots to show results from code that is no longer visible;
- hidden mutations to change later cells;
- “restart and run all” to fail after a long authoring session.

Those are reproducibility problems and teaching problems. A learner cannot
reason about causality when the document’s causal structure is hidden.

[Pluto’s reactivity model](https://plutojl.org/en/docs/reactivity/) analyzes
assignments and references, builds a dependency graph, deletes variables whose
definitions disappear, and re-runs downstream cells automatically. Its stated
goals are exactly right for learning: reproducibility, no stale hidden state,
and easy exploration. `STANDARD`, shipping open source

[marimo](https://docs.marimo.io/guides/reactivity/) similarly treats notebooks
as reactive Python programs, with deterministic execution, composable UI
elements, SQL, testing, app export, and browser/WASM operation. `STANDARD`,
shipping open source

The 2025 Rex paper introduced a fine-grained test suite for assessing whether
notebook systems actually maintain reactive semantics across edge cases.
`MEASURED-BENCH`

Source:

- [When Are Reactive Notebooks Not Reactive?](https://arxiv.org/abs/2511.21994)

The July 2026 standard should therefore test reactivity rather than trusting a
product label.

---

## 2. The semantic cell types

An AI-native learning document distinguishes roles:

| Cell type | Contains | Verification |
|---|---|---|
| Source | exact curriculum, paper, manual, or local knowledge span | existence, authority, version, entailment |
| Definition | term, symbol, unit, assumption | schema, uniqueness, dependency |
| Parameter | learner-controlled value or scenario | bounds, unit, accessible label |
| Data | observation or dataset reference | provenance, shape, checksum |
| Compute | code, formula, proof, transformation | tests, types, units, sandbox |
| View | text, table, plot, diagram, simulation | semantic and accessibility checks |
| Explanation | dynamic narrative tied to graph state | claim records and scope |
| Practice | prediction, probe, creation, transfer task | rubric and learner evidence |
| Reflection | learner explanation or annotation | learner-owned provenance |

Cell roles make the document legible to the mentor. The AI can modify a
visualization without overwriting the source or practice contract.

---

## 3. One change updates every representation

Consider an energy notebook. The learner switches friction from zero to a
positive coefficient.

The graph should update:

- governing equation;
- energy table;
- position-speed plot;
- animation;
- prose explanation;
- invariant tests;
- example solution;
- transfer question;
- verification status.

It should *not* silently retain “total mechanical energy is constant” from the
frictionless edition.

The learner predicts which nodes will change before running. This makes the
dependency graph a conceptual model, not just software plumbing.

---

## 4. AI acts through the graph

The mentor receives structured actions:

```text
inspect_node(node_id)
explain_dependency(source_id, target_id)
propose_patch(node_id, diff)
run_affected(node_id)
show_verification(node_id)
fork_scenario(parameter_changes)
create_probe(goal_id, graph_state)
record_learner_explanation(event)
```

Every AI edit appears as a patch. The learner can accept, modify, reject, or
revert it. The graph records which model, source, and tool produced the change.

This is better than a side-panel chatbot whose explanation may refer to a
different state than the notebook.

Current frontier products provide the components:

- [Gemini code execution](https://ai.google.dev/gemini-api/docs/code-execution)
  iteratively generates Python, reads output, and can combine execution with
  search and tools. `VENDOR`
- [Claude Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
  creates editable applications and maintains versions. `VENDOR`
- NotebookLM’s June 2026 upgrade added advanced reasoning and a secure cloud
  computer for running code and generating charts, spreadsheets, and slides.
  `VENDOR`

Source:

- [Google’s June 2026 AI update](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-june-2026/)

---

## 5. Proactive help without interruption spam

A graph exposes meaningful events:

- repeated test failure;
- a changed parameter;
- prediction submitted;
- invariant broken;
- explanation inconsistent with graph;
- long pause at a declared step;
- transfer attempt completed.

The mentor can act only at pedagogically useful boundaries. It may ask for a
prediction before execution, offer one hint after a repeated error, or invite
explanation after a surprising result.

The July 2026 SCALA deployment in an online Python course with more than 1,500
students generated likely questions before lectures. Students frequently
selected the predictive questions, and their content substantially overlapped
real learner questions. Students preferred SCALA’s answers to their own queries
over compared alternatives. `OBSERVED`

Source:

- [SCALA, ACL Industry 2026](https://aclanthology.org/2026.acl-industry.107/)

Reactive documents make proactive help more precise because intervention
triggers are declared and inspectable.

---

## 6. Browser-local and offline execution

[JupyterLite](https://jupyterlite.readthedocs.io/) runs a JupyterLab-like
environment in the browser. [Pyodide](https://pyodide.org/) provides CPython and
scientific packages through WebAssembly. [marimo
WASM](https://docs.marimo.io/guides/wasm/) exports reactive Python applications
for static hosting. `STANDARD`, shipping open source

The offline bundle includes:

```text
semantic graph
source excerpts
Python/JavaScript/WASM runtime
data and dependency hashes
tests and verification records
accessible static views
learner event queue
```

A shared phone may receive a lightweight JavaScript graph and static fallbacks.
A school laptop can run local Python. A regional sandbox handles packages or
compute unavailable locally.

The graph and learner evidence remain portable across tiers.

---

## 7. Reproducibility as a learner-facing feature

Every notebook exposes:

- “what changed”;
- “what reran”;
- “which outputs are now stale or invalid”;
- “which test supports this claim”;
- “which source defines this quantity”;
- “how to reproduce this result”;
- “what is cached and from when.”

The learner can select any visual statement and trace it upstream to code,
parameters, data, definitions, and sources.

This implements the project’s L0–L4 grounding ladder inside the document.

---

## 8. Narrative and graph coexist

Reactive does not mean the learner sees a programming IDE.

The same graph can render:

- a guided story with one control at a time;
- a traditional notebook;
- a dashboard;
- a simulation;
- a spoken lesson;
- an editable expert view;
- a printed static path.

The mentor progressively reveals the machinery. A beginner manipulates. An
intermediate learner inspects formulas. An advanced learner edits code, tests,
and source mappings.

[Quarto](https://quarto.org/) provides multi-format scientific publishing.
[Observable Framework](https://observablehq.com/framework/) and
[Vega-Lite](https://vega.github.io/vega-lite/) provide reactive data
presentation. The AI-native layer adds generation, verification, learner state,
and mentor orchestration.

---

## 9. Collaborative state

Teachers and learners can fork a scenario rather than overwrite one another.

- learner branch: predictions, edits, and explanations;
- teacher branch: verified base, hints, and feedback;
- peer branch: alternative model or solution;
- mentor proposal: a visible patch;
- published branch: signed, tested artifact.

Merging is semantic:

- independent cells merge automatically;
- competing definitions require resolution;
- source changes invalidate dependent claims;
- learner reflections are never overwritten;
- verification reruns after a merge.

The learner-owned state ledger references notebook event and version IDs.

---

## 10. Physical and unplugged extensions

The graph can connect a digital model to a local experiment:

- measure a pendulum with a phone camera;
- record water temperature;
- build a paper circuit;
- use bottle caps as manipulatives;
- simulate a sorting network with people;
- compare sensor data with the model.

A July 2026 primary-school study using the mechanical Turing Tumble found that
9–10-year-olds relied heavily on iterative testing and debugging, making
observable action and strategy central evidence. `OBSERVED`

Source:

- [Unplugged but Connected](https://link.springer.com/article/10.1007/s10763-026-10698-4)

An April 2026 ACM study designed four physical simulations of machine-learning
reasoning for young adolescents, supporting low-resource and embodied AI
learning. `OBSERVED`

Source:

- [AI Unplugged](https://doi.org/10.1145/3786761)

The notebook records real measurements and physical actions as L3 evidence.

---

## 11. Acceptance tests

A reactive learning document passes when:

1. visible outputs always match visible code and parameters;
2. deleted definitions do not linger;
3. each node has one semantic role and stable ID;
4. dependencies are inspectable;
5. a change reruns only the affected graph;
6. stale outputs cannot appear verified;
7. sources, units, tests, and accessibility checks are graph nodes;
8. AI edits are visible, reversible patches;
9. learner prediction precedes at least one important run;
10. explanation and transfer return to learner state;
11. the notebook restarts reproducibly from a clean environment;
12. browser-local core operation works offline;
13. static and accessible fallbacks preserve the goal;
14. branches and merges preserve learner authorship;
15. proactive mentor interventions use declared events;
16. a learner can trace a claim to its dependencies.

---

## Conclusion

The reactive notebook is the executable page of the AI-native textbook.

It keeps explanation, code, data, visualization, verification, and practice in
one causal structure. It lets a learner see what depends on what, change the
model, predict the consequences, and understand why a result moved.

The AI mentor does not hover beside the document. It acts through the same
inspectable graph, and every useful interaction becomes portable learning
evidence.

---

## Source index

1. [Pluto reactivity](https://plutojl.org/en/docs/reactivity/)
2. [Pluto FAQ](https://plutojl.org/en/docs/faq/)
3. [Rex reactive-notebook test suite](https://arxiv.org/abs/2511.21994)
4. [marimo reactivity](https://docs.marimo.io/guides/reactivity/)
5. [marimo WASM](https://docs.marimo.io/guides/wasm/)
6. [JupyterLite](https://jupyterlite.readthedocs.io/)
7. [Pyodide](https://pyodide.org/)
8. [Jupyter Notebook format](https://nbformat.readthedocs.io/)
9. [Quarto](https://quarto.org/)
10. [Observable Framework](https://observablehq.com/framework/)
11. [Vega-Lite](https://vega.github.io/vega-lite/)
12. [Gemini code execution](https://ai.google.dev/gemini-api/docs/code-execution)
13. [Google June 2026 AI updates](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-june-2026/)
14. [Claude Artifacts](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
15. [SCALA proactive tutor](https://aclanthology.org/2026.acl-industry.107/)
16. [AI-supported problem-based learning in Nigeria](https://doi.org/10.1016/j.chbah.2026.100263)
17. [Unplugged but Connected](https://link.springer.com/article/10.1007/s10763-026-10698-4)
18. [AI Unplugged](https://doi.org/10.1145/3786761)
19. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
20. [WebAssembly core specification](https://webassembly.github.io/spec/core/)

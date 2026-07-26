---
title: "Executable and verifiable knowledge at the July 2026 frontier"
wave: F
section: F3
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
---

# F3 — Executable and Verifiable Knowledge

## Executive finding

The static explanation is no longer the natural unit of digital learning.

By July 2026, mainstream AI products can generate and run code, produce
interactive React applications and SVG diagrams, build manipulatives from a
conversation, combine search with computation, and expose editable versions.
Browser runtimes can execute Python and notebooks offline. Formal proof systems,
test suites, schemas, unit checkers, and data-validation tools can verify
declared properties. `VENDOR`; `STANDARD`

This enables **executable knowledge**:

> A grounded concept specification compiles into coordinated text, diagram,
> simulation, code, proof, data, and practice views that the learner can change.
> Each checkable claim carries a verifier and every learner action returns
> evidence to the learner-owned state.

The learning object is not a polished animation to watch. It is an inspectable
system in which the learner predicts, changes an assumption, runs the model,
explains the result, and transfers the idea.

---

## 1. The capability threshold has crossed

### Interactive visual explanations are a product primitive

ChatGPT’s March 2026 release notes describe interactive math and science modules
whose formulas and variables can be manipulated in real time. Claude Artifacts
currently creates shareable HTML, SVG, React, code, diagrams, and AI-powered
applications from conversation, with version history and forking. Anthropic
reported more than half a billion artifacts by June 2025 and has documented
educators creating simulations, games, quizzes, and visualizations. `VENDOR`

Sources:

- [ChatGPT release notes: interactive math and science](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
- [Claude Artifacts overview](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Anthropic: AI-powered artifacts](https://www.anthropic.com/news/build-artifacts)
- [Anthropic education report](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude)

### Code execution is an iterative reasoning tool

Gemini’s Interactions API documentation, updated 21 July 2026, exposes Python
execution with scientific, document, geospatial, image, data, and plotting
libraries. The model can generate code, inspect its output, and iterate; search
grounding and custom function tools can be combined with execution.
`VENDOR`

Source:

- [Gemini code execution](https://ai.google.dev/gemini-api/docs/code-execution)

### The browser can be the lab

[JupyterLite](https://jupyterlite.readthedocs.io/) runs a Jupyter environment
entirely in the browser. [Pyodide](https://pyodide.org/) ports CPython and the
scientific Python stack to WebAssembly.
[marimo](https://docs.marimo.io/guides/wasm/) can export reactive notebooks to
WASM. [Observable Framework](https://observablehq.com/framework/) and
[Vega-Lite](https://vega.github.io/vega-lite/) provide reproducible,
declarative data views. `STANDARD`; shipping open source

These runtimes support a low-cost learning package that works from local files,
a school server, or a cached progressive web app.

---

## 2. The executable lesson contract

Generation begins from a versioned concept specification:

```yaml
concept: "conservation of energy on a frictionless track"
learner_goal: "predict speed from height"
prerequisites:
  - "gravitational potential energy"
  - "kinetic energy"
definitions:
  - symbol: m
    meaning: mass
    unit: kg
sources: [...]
assumptions:
  - "no friction"
  - "constant gravitational field"
invariants:
  - "m*g*h + 0.5*m*v^2 is constant"
controls:
  - mass
  - initial_height
learner_actions:
  - predict
  - vary
  - explain
  - transfer
verification:
  units: true
  numerical_invariant_tolerance: 1e-9
access:
  keyboard: true
  screen_reader_summary: true
  reduced_motion: true
```

The specification is the semantic source of truth. Text, visual, code, and
assessment renderers consume it. When one assumption changes, all views
regenerate together.

---

## 3. The representation compiler

One concept can produce:

- a short spoken explanation;
- an annotated diagram;
- an interactive manipulative;
- executable equations;
- a table and graph;
- a formal derivation;
- a physical activity using local objects;
- guided practice;
- a transfer challenge;
- accessible text, audio, high-contrast, and reduced-motion variants.

The representations are coordinated, not independently hallucinated. Shared
symbols, units, sources, assumptions, and invariants come from the concept
specification.

For a learner on a basic phone, the compiler may choose a static SVG plus numeric
inputs. On a school laptop, it may add a local Python simulation. In a lab, it
may connect to a sensor. The learning goal remains stable while the execution
tier adapts.

---

## 4. Verification is attached to the claim

The [grounding ladder](G1-grounding-ladder-2026.md) maps generated material to
the right check:

| Claim | Tier | Verifier |
|---|---|---|
| “Imagine a frictionless planet” | L0 | visible generation label |
| “The local curriculum defines this objective” | L1 | exact source span |
| “The equation conserves energy under these assumptions” | L2 | symbolic, unit, and numeric checks |
| “This model predicts our measured cart” | L3 | experiment, calibration, residuals |
| “This result satisfies the course credential” | L4 | authorized educator decision |

The verification bundle records tool version, source, input, output, parameters,
random seed, environment, tests, and validity scope.

Current implementation components include:

- [SymPy](https://docs.sympy.org/) for symbolic computation;
- [Pint](https://pint.readthedocs.io/) for units;
- [JSON Schema](https://json-schema.org/specification) for structured lesson
  contracts;
- [Lean 4](https://lean-lang.org/doc/reference/latest/) for formal proof terms;
- test frameworks and property-based testing for code and invariants.

A pass means only what the predicate says. A simulation that conserves energy
does not prove the world is frictionless. A test suite does not prove the
learner understands. The interface shows the boundary.

---

## 5. The learner action loop

The highest-value interaction sequence is:

1. **Predict** what will happen before execution.
2. **Change** a variable, assumption, representation, or piece of code.
3. **Run** the artifact and see the consequences.
4. **Explain** the result in the learner’s own words or notation.
5. **Verify** the claim with the attached tool or source.
6. **Compare** prediction with result.
7. **Transfer** to a fresh situation where surface features differ.

The mentor records the learner’s prediction, edits, explanation, help used, and
transfer—not merely whether they clicked “run.”

The loop supports productive creation. A learner can build a model, improve it,
teach it to an AI student, defend it before a peer panel, and publish it with
provenance.

---

## 6. Verification-first does not mean answer-first

Executable objects create two kinds of truth:

- **artifact truth:** the program, proof, or model satisfies a declared check;
- **learner capability:** the learner can explain, adapt, and transfer it.

Artifact truth can be established cheaply and continuously. That frees the
mentor to spend interaction on understanding:

- Why is this invariant the right one?
- What assumption did the test leave out?
- Which input would break the model?
- Can you predict the graph before running?
- How would this change with friction?
- Can you rebuild the relationship in another representation?

The verified artifact becomes the starting point for a richer oral or project,
not the end of assessment.

---

## 7. Sandboxing and reproducibility

Generated execution belongs in a constrained environment:

- explicit CPU, memory, and wall-time budgets;
- no ambient network or secrets;
- allowlisted libraries and system calls;
- immutable base environment;
- ephemeral working directory;
- deterministic seed where possible;
- captured stdout, stderr, files, and plots;
- content hash for every dependency;
- reset button and learner-visible execution status.

WebAssembly provides a portable runtime boundary. Local execution reduces cloud
cost and keeps exploratory learner data on the device. More demanding or
specialized work can escalate to a school node or regional sandbox.

Source:

- [WebAssembly core specification](https://webassembly.github.io/spec/core/)

---

## 8. Visual and interaction verification

Code correctness does not guarantee a correct diagram or usable manipulative.
The pipeline also checks:

- labels match the concept specification;
- axes, units, scales, and legends are present;
- constraints remain true across the control range;
- color is not the only carrier of meaning;
- keyboard, screen-reader, touch, and voice paths reach the same goal;
- focus order and reduced motion work;
- text remains readable on low-resolution screens;
- a static explanation exists when execution is unavailable.

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) supplies the accessibility floor.
[C2PA 2.4](https://spec.c2pa.org/specifications/) can preserve generated-media
provenance. `STANDARD`

The July 2026 [ShadowAI](https://doi.org/10.1145/3803784.3816815) project
demonstrates how tangible making, generated stories, images, and visualized AI
reasoning can support children’s critical AI understanding in an informal
museum experience. `OBSERVED`

---

## 9. Offline delivery

An executable lesson bundle can contain:

```text
manifest.json
concept.yaml
sources/
views/
  explanation.html
  diagram.svg
  manipulative.js
  notebook.ipynb
checks/
  tests.json
  unit_rules.json
access/
  transcript.txt
  alt_explanation.html
provenance/
  claims.json
  c2pa/
```

The bundle is signed, cached, and runnable from a browser. A school node can
generate or update bundles overnight. A learner on a shared phone can interact
with the lightweight view and synchronize evidence later.

The verification status travels with the artifact. Offline does not mean
opaque.

---

## 10. Acceptance tests

An executable learning object passes when:

1. every representation is generated from the same versioned concept spec;
2. factual claims have claim-level sources;
3. calculations, units, schemas, and declared invariants pass reproducibly;
4. simulation assumptions and validity domain are visible;
5. the learner predicts before running at least one key result;
6. controls expose a meaningful relationship rather than decorative motion;
7. learner edits and explanations return to the state ledger;
8. transfer is tested in a fresh representation or context;
9. the artifact runs in a constrained sandbox;
10. dependencies, inputs, outputs, and seeds are preserved;
11. keyboard, screen reader, touch, voice, and reduced-motion paths are tested;
12. a useful static fallback works offline;
13. the same package runs on a learner device and school node;
14. generation and edit provenance is visible;
15. learning outcomes are measured separately from artifact validity.

---

## Conclusion

Frontier AI makes custom learning software cheap enough to generate for one
learner and one moment. Verification tools make its checkable core trustworthy.
Local browser runtimes make distribution global.

The design standard is therefore higher than “AI created an animation”:

- one grounded semantic specification;
- many coordinated representations;
- declared assumptions and invariants;
- tool-backed verification;
- learner prediction and manipulation;
- explanation and transfer;
- portable evidence and provenance;
- offline-capable execution.

The textbook page becomes a live laboratory, proof assistant, studio, and
practice partner—created on demand and owned by the learner.

---

## Source index

1. [ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)
2. [Claude Artifacts overview](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
3. [Anthropic: AI-powered artifacts](https://www.anthropic.com/news/build-artifacts)
4. [Anthropic education report](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude)
5. [Gemini code execution](https://ai.google.dev/gemini-api/docs/code-execution)
6. [Gemini tools](https://ai.google.dev/gemini-api/docs/tools)
7. [JupyterLite](https://jupyterlite.readthedocs.io/)
8. [Pyodide](https://pyodide.org/)
9. [marimo WASM](https://docs.marimo.io/guides/wasm/)
10. [Observable Framework](https://observablehq.com/framework/)
11. [Vega-Lite](https://vega.github.io/vega-lite/)
12. [SymPy](https://docs.sympy.org/)
13. [Pint](https://pint.readthedocs.io/)
14. [JSON Schema](https://json-schema.org/specification)
15. [Lean 4 reference](https://lean-lang.org/doc/reference/latest/)
16. [WebAssembly core specification](https://webassembly.github.io/spec/core/)
17. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
18. [C2PA specifications](https://spec.c2pa.org/specifications/)
19. [ShadowAI](https://doi.org/10.1145/3803784.3816815)
20. [OECD: Empowering Learners for the Age of AI](https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/06/empowering-learners-for-the-age-of-ai_2f8315e7/65cd27d4-en.pdf)

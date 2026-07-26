---
title: "Verified educational illustration and diagram generation at the July 2026 frontier"
wave: C
section: C1
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 20
---

# C1 — Verified Educational Illustration and Diagram Generation

## Executive finding

The frontier has moved from *text-to-image* to **multimodal visual production**:
research a subject, reason about the requested structure, generate or edit an
asset, inspect it, and repair it across turns. In April 2026, ChatGPT Images 2.0
made thinking-with-search, source transformation, dense text, and controlled
editing part of a single production surface. Google’s July 2026 image family
offers grounded generation, multi-reference consistency, reliable text rendering,
and output up to 4K. `VENDOR`

That is enough to make bespoke illustration abundant. It is not, by itself,
enough to make a visual *instructionally true*.

The correct architectural response is not to suppress generation. It is to
separate:

1. **the semantic object** — entities, relationships, values, units, learning
   objective, and source claims;
2. **the rendered object** — pixels, SVG, canvas, video, or print;
3. **the verification object** — assertions that can fail; and
4. **the access object** — alt text, reading order, contrast, localization, and
   nonvisual equivalents.

An expert AI mentor can therefore draw a new explanation for one learner in
seconds, while a verification harness prevents a persuasive drawing from silently
changing the lesson.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-BENCH` | Quantitative evaluation on a stated benchmark or human-rated set |
| `OBSERVED` | Directly inspectable API, artifact, specification, or behavior |
| `VENDOR` | Provider-reported capability, not independent educational evidence |
| `INFERENCE` | Design conclusion drawn from the evidence |

## 1. What became newly possible

### 1.1 One model can now be visual researcher, editor, and renderer

- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)
  combines a thinking mode with web research, source-image transformation,
  complex layout, dense text, and iterative editing. The launch examples include
  an academic poster derived from the GPT-1 paper. `VENDOR`
- [GPT-Image-1.5](https://openai.com/index/new-chatgpt-images-is-here/)
  brought stronger instruction following, more precise edits, improved dense
  text, better consistency, and up to 4× faster generation to the API in
  December 2025. `VENDOR`
- Google’s current [Nano Banana model guide](https://ai.google.dev/gemini-api/docs/image-generation)
  identifies Gemini 3.1 Flash Image as the default generalist, Gemini 3 Pro Image
  for complex professional work with search grounding and thinking, and Gemini
  3.1 Flash Lite Image for low-cost, low-latency production. `VENDOR`
- The same guide states that the current family supports interleaved text/image
  work, multi-reference input, conversational editing, text rendering, and up to
  4K generation on selected models. `VENDOR`
- Google plans to shut down the older Imagen API models on 17 August 2026 and
  recommends migration to its native multimodal image family. This is a concrete
  reason not to anchor an implementation to a static 2024–25 model taxonomy.
  `OBSERVED`

The educational consequence is profound: a learner no longer needs to search for
the one diagram that happens to match a misconception. The mentor can construct
a new diagram around the learner’s exact words, language, scale, notation, and
current artifact.

### 1.2 Visual code is becoming a first-class generation target

For exact educational figures, the important development is not only better
pixels. Models increasingly generate **renderable structure**:

- [VectorGym](https://arxiv.org/abs/2603.29852) evaluates text-to-SVG,
  sketch-to-SVG, complex editing, and captioning using expert-authored
  annotations; its multitask 8B method matches GPT-4o on the reported benchmark.
  `MEASURED-BENCH`
- [DiagramIR](https://arxiv.org/abs/2511.08283) evaluates educational geometry
  diagrams through an intermediate representation extracted from TikZ. Its
  structural evaluation agrees with humans better than LLM-as-judge baselines;
  the authors report that a small model can match a larger model at roughly one
  tenth the inference cost when the representation does the checking.
  `MEASURED-BENCH`
- [ChartCoder](https://arxiv.org/abs/2501.06598) treats chart code as a lossless
  representation and trains against a 160k chart-to-code dataset. `MEASURED-BENCH`
- [Chart2Code](https://arxiv.org/abs/2510.17932) spans 2,023 tasks and 22 chart
  types across reproduction, editing, and long-table generation. The reported
  2025 frontier result—0.57 on code evaluation and 0.22 on chart quality for
  editing—shows why compilation alone is insufficient. `MEASURED-BENCH`

`INFERENCE`: educational visuals should default to code or structured scene
graphs when the visual asserts exact relationships. Raster generation remains
ideal for stories, environments, historical reconstruction, motivation, and
conceptual analogy.

## 2. What the 2026 evaluations actually say

### 2.1 Scientific figures are now plausible, not automatically correct

[SciFig](https://arxiv.org/abs/2601.04390) generates paper pipeline figures by
parsing research into components, grouping modules, laying out relationships,
then iterating with visual feedback. It reports 70.1% overall quality on
dataset-level evaluation and 66.2% on paper-specific evaluation.
`MEASURED-BENCH`

[SridBench](https://arxiv.org/abs/2505.22126) contains 1,120 scientific figure
tasks across 13 disciplines and evaluates six dimensions including semantic
fidelity and structural accuracy. Its experiments found a remaining
human–frontier-model gap in text/visual clarity and scientific correctness.
`MEASURED-BENCH`

These results are not an argument against generated figures. They specify the
missing production layer: **measure semantic fidelity separately from aesthetic
quality, and repair before publication.**

### 2.2 July 2026 educational work converges on agentic repair

[Exploring Agentic Workflows for Generating High Quality Math Visual Aids](https://arxiv.org/abs/2607.09839),
released 10 July 2026, asks one agent to derive visual quality questions and
another vision-language model to inspect and iteratively improve K–12 math
visuals. The exploratory results support the repair loop while identifying
spatial reasoning and QA-question coverage as the main remaining gaps.
`MEASURED-BENCH`

[Can We Improve Educational Diagram Generation with In-Context Examples?](https://arxiv.org/abs/2601.20476)
uses 150 diagrams rated by computer-science educators for organization,
connectivity, aesthetics, and hallucination. Structured in-context examples
reduced factual hallucination and improved faithfulness, but model self-detection
of errors remained unreliable. `MEASURED-BENCH`

`INFERENCE`: the same model may propose and revise, but the acceptance decision
must be grounded in explicit assertions, independent rendering checks, or a
second verifier with access to the source contract.

## 3. The visual-verification pipeline

### Stage 1 — Write a concept contract

Before prompting for appearance, encode:

- the learning objective;
- learner age, language, prior knowledge, and access mode;
- entities that must appear;
- relationships, directions, quantities, labels, units, and invariants;
- what may be simplified;
- what may never be falsified;
- required source excerpts or executable derivations;
- likely misconceptions the visual must not reinforce.

Example contract:

```yaml
concept: net force
learner_state: understands vectors, confuses velocity with force
must_show:
  - object: cart
  - force: {label: F_push, direction: right, magnitude: 8 N}
  - force: {label: F_friction, direction: left, magnitude: 3 N}
invariants:
  - net_force == 5 N right
  - arrow_length_ratio == 8/3 within tolerance
must_not_imply:
  - motion direction equals net-force direction in every instant
nonvisual_equivalent: ordered force list plus signed sum
```

### Stage 2 — Choose the representation by claim type

| Claim type | Preferred representation | Reason |
|---|---|---|
| Exact geometry, circuit, causal graph | SVG/TikZ/diagram code + IR | Relationships can be inspected |
| Data chart | Vega-Lite/Matplotlib/Plotly + source table | Values and encodings can be tested |
| Dynamic process | Executable simulation + state trace | Motion derives from a model |
| Spatial story or analogy | Raster image + semantic checklist | Expressiveness matters most |
| Manipulable object | 3D scene graph + constraints | Learner can change parameters |
| Print/offline | SVG/PDF plus text equivalent | Portable and accessible |

### Stage 3 — Generate both source and render

The production result is a bundle:

```text
visual/
  concept.yaml          # source claims and invariants
  figure.svg            # editable semantic representation
  figure.png            # preview / low-bandwidth derivative
  figure.alt.md         # nonvisual explanation
  assertions.json       # machine checks and results
  provenance.json       # sources, model, prompt, version, timestamp
```

### Stage 4 — Verify four independent dimensions

1. **Semantic truth**
   - Are every required entity and relationship present?
   - Do values, units, signs, arrows, labels, and causal directions agree with
     the source?
   - Does the visual avoid the named misconception?
2. **Render integrity**
   - Does the source compile?
   - Are labels clipped, overlapped, illegible, or outside the viewport?
   - Does it survive mobile, print, grayscale, and localization expansion?
3. **Accessibility**
   - Is there meaningful alt text or a structured equivalent?
   - Is reading order explicit?
   - Is color redundant with shape, texture, or text?
4. **Provenance**
   - Which claims and sources does the figure encode?
   - Which model, prompt, code, and revision produced it?
   - Is synthetic-media provenance retained? Google documents
     [SynthID](https://deepmind.google/technologies/synthid/) for generated
     media; OpenAI documents C2PA metadata for its
     [image API](https://openai.com/index/image-generation-api/). `OBSERVED`

### Stage 5 — Repair only the failed layer

If arrow direction is wrong, rewrite the semantic source and rerender. If text
overlaps, preserve the approved semantic graph and change layout. If alt text
omits a relationship, repair the access object without regenerating the visual.

This makes iteration cheap without reopening every settled decision.

## 4. An AI-mentor visual policy

The mentor chooses the least expensive representation that makes the learner’s
next inference visible:

1. **Point** to the learner’s own work before generating anything.
2. **Annotate** the existing artifact when one mark resolves the confusion.
3. **Sketch** when speed and conversational flow matter.
4. **Render structured code** for exact relationships.
5. **Simulate** when change under intervention is the lesson.
6. **Generate imagery** when scene, culture, affect, or analogy is central.
7. **Print or cache** the smallest derivative that preserves the learning action.

The visual is not the explanation. The learner’s act—predicting, manipulating,
labeling, comparing, reconstructing—is the explanation.

## 5. Universal-access consequences

### Low bandwidth and offline

- Store the concept contract and vector source before large raster derivatives.
- Generate thumbnails and print-ready monochrome variants.
- Precompute high-frequency diagrams in regional language packs.
- Allow a local small model to change labels/layout while reserving cloud calls
  for new semantic generation.
- Send deltas for edits instead of whole images.

### Language

- Keep labels outside pixels whenever possible.
- Permit right-to-left and vertical writing systems.
- Validate layout after translation; a correct English diagram can become
  unusable when labels expand.
- Generate the nonvisual equivalent in the learner’s strongest language.

### Disability

The [W3C Images tutorial](https://www.w3.org/WAI/tutorials/images/) distinguishes
informative, decorative, functional, and complex images and requires alternatives
appropriate to purpose. The [WCAG 2.2 recommendation](https://www.w3.org/TR/WCAG22/)
is the baseline, not a post-launch feature. `OBSERVED`

An accessible AI mentor can also transform the same concept contract into:

- tactile-print instructions;
- ordered verbal description;
- sonification;
- high-contrast or low-visual-complexity variants;
- sign-supported video;
- a physical construction recipe using local materials.

## 6. Acceptance tests

A generated educational visual is publishable only if:

- [ ] every factual claim maps to a source, derivation, or executable state;
- [ ] all contract invariants pass;
- [ ] a second pass checks labels, units, arrows, counts, topology, and scale;
- [ ] the learner can perform an action with the visual;
- [ ] the asset remains legible at its delivery size;
- [ ] color is not the sole information channel;
- [ ] useful alt text or a structured equivalent exists;
- [ ] localization has been rendered, not merely translated;
- [ ] low-bandwidth and print derivatives exist where relevant;
- [ ] source, render, prompt, model/version, and verification results are retained.

## 7. Research agenda

1. Build curriculum-specific semantic IRs for geometry, chemistry, circuits,
   timelines, maps, and causal systems.
2. Measure learning from verified dynamic visuals against generic generated
   images, holding tutor policy constant.
3. Benchmark whether verifier diversity—symbolic test + VLM + human sampling—
   reduces correlated error.
4. Measure accessibility transformations as learning experiences, not compliance
   artifacts.
5. Price the pipeline on local, regional, and frontier tiers.

## Source index

1. OpenAI — [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)
2. OpenAI — [GPT-Image-1.5](https://openai.com/index/new-chatgpt-images-is-here/)
3. OpenAI Academy — [Creating images with ChatGPT](https://openai.com/academy/image-generation/)
4. OpenAI — [Image generation API](https://openai.com/index/image-generation-api/)
5. OpenAI — [Images 2.0 system card](https://deploymentsafety.openai.com/chatgpt-images-2-0/chatgpt-images-2-0.pdf)
6. Google — [Gemini image generation](https://ai.google.dev/gemini-api/docs/image-generation)
7. Google — [Gemini models](https://ai.google.dev/gemini-api/docs/models)
8. Google DeepMind — [SynthID](https://deepmind.google/technologies/synthid/)
9. SciFig — [arXiv:2601.04390](https://arxiv.org/abs/2601.04390)
10. Math visual-aid agents — [arXiv:2607.09839](https://arxiv.org/abs/2607.09839)
11. Educational diagram ICL — [arXiv:2601.20476](https://arxiv.org/abs/2601.20476)
12. DiagramIR — [arXiv:2511.08283](https://arxiv.org/abs/2511.08283)
13. SridBench — [arXiv:2505.22126](https://arxiv.org/abs/2505.22126)
14. VectorGym — [arXiv:2603.29852](https://arxiv.org/abs/2603.29852)
15. Chart2Code — [arXiv:2510.17932](https://arxiv.org/abs/2510.17932)
16. ChartCoder — [arXiv:2501.06598](https://arxiv.org/abs/2501.06598)
17. Mermaid — [diagram syntax](https://mermaid.js.org/intro/)
18. W3C — [SVG 2](https://www.w3.org/TR/SVG2/)
19. W3C WAI — [Images tutorial](https://www.w3.org/WAI/tutorials/images/)
20. W3C — [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

## Decision

**Adopt visual generation as a core tutor tool, with semantic source, automated
verification, accessibility transformation, and provenance as one indivisible
pipeline.** The goal is not fewer generated visuals. It is a new visual for every
learner whenever one helps—produced cheaply enough for universal access and
verified strongly enough to teach from.

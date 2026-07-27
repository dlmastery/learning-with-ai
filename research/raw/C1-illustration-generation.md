---
title: "Illustration and diagram generation: can a machine draw a CORRECT figure?"
wave: C
section: C1
date_researched: 2026-07-27
sources_count: 64
status: raw-research
---

# C1 — Illustration and diagram generation: can a machine draw a *correct* figure?

> **Scope boundary.** Section A2 owns animation *pedagogy* (does motion help?), Manim, Remotion, and the
> LLM→video toolchains. This section owns **static and interactive figure generation and its correctness**:
> what target language to emit, what can be mechanically checked, what fails, and what a
> figure-generation standard looks like. Where A2 and C1 touch the same paper (ALGOGEN, PairCoder++,
> ScImage, the SVG benchmarks), C1 goes to the *verification* argument rather than the pedagogy argument.

> **Retrieval note.** WebSearch budget exhausted. The arXiv **API** (`export.arxiv.org`) returned sustained
> `HTTP 429` from this host for the entire session; Semantic Scholar and OpenAlex returned `429` as well.
> Retrieval therefore ran on (a) the arXiv **API** during a short window before rate-limiting bit — this
> produced verbatim abstracts for 11 anchor papers; (b) **WebFetch** against `arxiv.org/abs/…` and
> `arxiv.org/search/…`, which returns a model-summarised rendering of the page rather than raw text; and
> (c) the authenticated **GitHub API**. Papers retrieved by route (a) are marked `[verbatim]`. Papers
> retrieved by route (b) are marked `[fetched-summary]` — quoted fragments are quoted as they appeared in
> the fetched abstract text, but a fragment not enclosed in quotation marks is a paraphrase and should be
> re-verified before it enters the survey. Nothing here is reported from memory.

**Evidence labels** (PRD §2): `MEASURED-BENCH` · `MEASURED-META` · `MEASURED-RCT` · `OBSERVED` ·
`VENDOR` · `DEMO` · `INFERENCE`.

---

## 0. The thesis

Three findings organise everything below.

**First: the field solved the wrong problem and knows it.** Execution success for generated figures is
essentially done. Ford & Rios take text-to-chart generation from ~15% script failure to **4.5%** with a
four-role agent loop on GPT-4o-mini, and title the paper *"Does It Run and Is That Enough?"* — because
manual review of the surviving charts found **6 of 100 contained hallucinations** and only **33.3%
(Text2Chart31) / 7.2% (ChartX)** of them satisfied basic colourblindness guidance
(arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH` `[verbatim]`). A compile gate
buys you the existence of the artifact and nothing else.

**Second: the dangerous output class is the legible-but-wrong figure, and it is now measured.**
SciFlow-Bench states it flatly: text-to-image models "often produce visually plausible but structurally
incorrect results" (arXiv:[2602.09809](https://arxiv.org/abs/2602.09809), `MEASURED-BENCH`
`[fetched-summary]`). GeoR-Bench states the same thing from the other side — "the visual consistency and
image quality of the outputs frequently surpass their scientific accuracy"
(arXiv:[2605.11541](https://arxiv.org/abs/2605.11541), `MEASURED-BENCH` `[fetched-summary]`). For a
teaching system this class is worse than a crash, because a crash teaches nothing and a confident wrong
diagram teaches a misconception that the learner will then defend.

**Third: the architecture is settled and the field has stopped arguing about it.** At least eight
independent groups, across chart code, algorithm animation, technical illustration, geometry, and
diagram evaluation, converged on the same shape: **the LLM emits a small, verifiable, declarative
intermediate representation; a deterministic renderer does the drawing.** The cleanest measurement is
ALGOGEN's: decoupling algorithm simulation from rendering moved success from **82.5% → 99.8%**
(arXiv:[2605.12159](https://arxiv.org/abs/2605.12159), `MEASURED-BENCH` `[verbatim]`). This section
argues that this is no longer a research direction — it is the standard, and generating raw SVG or raw
D3 for an educational figure is now a defect.

---

## 1. Generation targets, ranked by how checkable the output is

### 1.1 The ranking criterion

"Checkable" is not one property. It decomposes into four independent gates, and a target's rank is how
many of them it gives you *for free*:

| Gate | Question | Who answers it |
|---|---|---|
| **G1 — Parses** | Is the emitted string well-formed in its grammar? | parser / schema validator |
| **G2 — Renders** | Does it produce an artifact at all? | compiler / renderer / interpreter |
| **G3 — Layout is not the model's job** | Does an engine own positioning, so label collision and overflow are *impossible by construction* rather than *hopefully absent*? | layout engine |
| **G4 — Semantics are recoverable** | Can the figure's claims be read back out of the source (or the render) and compared to the intended spec? | IR diff / round-trip / solver |

G3 is the gate the literature under-weights and the one that decides whether an educational figure is
usable. Every documented label-collision, text-overflow, and arrow-pointing-at-nothing failure in §3 is
a G3 failure, and every one of them occurs in a target where the model is asked to compute coordinates.

### 1.2 The ranking

**Tier A — Declarative spec + deterministic renderer (all four gates).**

- **Vega-Lite** (`vega/vega-lite`, 5,421★, BSD-3, created 2014-11-20, `OBSERVED` via GitHub API
  2026-07-27). A JSON grammar of graphics: the model names data fields and encodings; scales, axes,
  legends and layout are derived. Schema-validatable (G1), compiles (G2), engine owns layout (G3), and
  the spec *is* the semantics (G4) — you can diff a generated spec against a required spec field by
  field.
- **A project-defined trace/spec IR** — ALGOGEN's VTA-JSON, Flint's semantic model, Raiven's DSL. See §4.
- **Desmos expression lists / GeoGebra constructions.** State is a short list of expressions or
  constrained objects; the engine solves geometry and draws. GeoBuildBench formalises exactly this as a
  benchmark: "executable geometric constructions" from natural language, 489 Chinese textbook-style
  problems (arXiv:[2605.13167](https://arxiv.org/abs/2605.13167), `MEASURED-BENCH` `[fetched-summary]`).

**Tier B — Structural DSLs with an automatic layout engine (G1, G2, G3; G4 partial).**

- **Graphviz / DOT.** The model writes nodes and edges; `dot`/`neato` computes positions. Node overlap
  and edge routing are the layout engine's problem, and it is a good one. LegalViz built a 7,010-pair
  legal-document→DOT dataset across 23 languages precisely because DOT is a tractable target
  (arXiv:[2502.06147](https://arxiv.org/abs/2502.06147), `MEASURED-BENCH` `[fetched-summary]`).
  *(Note: `graphviz/graphviz` on GitHub is a 4-star stub; development is on GitLab — `OBSERVED`, GitHub
  API 2026-07-27. Do not cite GitHub stars as evidence of Graphviz's adoption.)*
- **Mermaid** (`mermaid-js/mermaid`, **89,429★**, MIT, created 2014-11-01, pushed 2026-07-27,
  `OBSERVED`). Smallest grammar in the set, renders natively in Markdown and on GitHub. MermaidSeqBench
  (132 samples, hybrid human-verified + LLM-augmented + rule-expanded) reports "significant capability
  gaps across models and evaluation modes" (arXiv:[2511.14967](https://arxiv.org/abs/2511.14967),
  `MEASURED-BENCH` `[fetched-summary]`) — i.e. even the smallest grammar is not free.
- **PlantUML** (`plantuml/plantuml`, 13,200★, LGPL-3.0, `OBSERVED`). Two results worth the survey:
  Code2UML reports **91.5% mean syntactic validity, 0.858 relationship precision, 81.7/100 structural
  quality** over 12 repositories × 4 languages × 7 diagram types
  (arXiv:[2605.24453](https://arxiv.org/abs/2605.24453), `MEASURED-BENCH` `[fetched-summary]`); and a
  nine-model study that generated **90 diagrams containing 3,373 methods** found that "all LLMs produced
  valid PlantUML diagrams adhering to UML conventions" while showing "inconsistencies in annotations and
  signatures," concluding "human oversight is essential to ensure accuracy"
  (arXiv:[2506.00788](https://arxiv.org/abs/2506.00788), `MEASURED-BENCH` `[fetched-summary]`).
  **This is the cleanest available statement of the G1/G2-pass, G4-fail pattern: 100% syntactic validity
  and content you still cannot trust.**

**Tier C — Compiled coordinate languages (G1, G2; no G3; G4 via IR parsing).**

- **TikZ / PGF.** The best-studied target because it compiles pass/fail and because DaTikZv2 supplies
  >360k human-written examples (A2 §3.4). PairCoder++ moves **TikZ compile rate up 10–30 points on every
  model tested** (arXiv:[2607.01883](https://arxiv.org/abs/2607.01883), `MEASURED-BENCH` `[verbatim]`).
  But TikZ has no layout engine: the model computes every coordinate, so G3 is entirely on the model.
  Recovering G4 requires a purpose-built parser — which is exactly what **DiagramIR** is: parse the
  LaTeX/TikZ into an intermediate representation and evaluate *that*, reporting "higher agreement with
  human raters" than LLM-as-a-Judge and letting **GPT-4.1-Mini perform comparably to GPT-5 at 10× lower
  inference cost** (arXiv:[2511.08283](https://arxiv.org/abs/2511.08283), `MEASURED-BENCH` `[verbatim]`).
- **matplotlib** (`matplotlib/matplotlib`, 23,034★, `OBSERVED`). Executes, and — crucially — the *data*
  in a matplotlib figure comes from real Python arrays, so the figure's numeric content is auditable at
  the source rather than inferred from pixels. Its live `Axes` object is directly assertable
  (`get_xlim`, `get_ylim`, `get_lines()[i].get_ydata()`, `get_xscale`), which makes it the best target
  in the whole set for *programmatic* axis and unit checks (§5.2). No layout engine for annotations,
  though: `text()` placement is manual, so label collision remains a model responsibility.
- **Asymptote.** Same class as TikZ. **`OBSERVED — absence`:** an arXiv full-text search for Asymptote +
  vector graphics returns only a 2023 Asymptote-animation paper and a 2010 Bézier-parametrisation paper;
  **there is no LLM-generation or benchmark literature for Asymptote.** Using it means operating with
  zero measured base rate. Prefer TikZ, which has one.

**Tier D — Hand-computed vector output (G1 only; the worst realistic option).**

- **SVG written directly by the model.** Well-formedness is checkable and nothing else is. This is where
  the benchmark literature is most consistent and most negative:
  - **VGBench** — 4,279 understanding + 5,845 generation samples; LLMs show "less desirable performance
    on low-level formats (SVG)" (arXiv:[2407.10972](https://arxiv.org/abs/2407.10972), `MEASURED-BENCH`
    `[verbatim]`).
  - **SVGenius** — 2,377 queries, 24 domains, **8 task categories, 18 metrics, 22 models**, with
    deliberate complexity stratification: "**all models exhibit systematic performance degradation with
    increasing complexity, indicating fundamental limitations in current approaches**"; also
    "reasoning-enhanced training proves more effective than pure scaling"
    (arXiv:[2506.03139](https://arxiv.org/abs/2506.03139), `MEASURED-BENCH` `[verbatim]`).
  - **VCode** — "frontier VLMs struggle to generate faithful SVGs, revealing a persistent gap between
    language-centric and visual-centric coding" (arXiv:[2511.02778](https://arxiv.org/abs/2511.02778),
    `MEASURED-BENCH` `[verbatim]`).
  - **SGP-GenBench** — decomposes the failure into **attribute binding, spatial relations, and
    numeracy**, the same three axes that fail in text-to-image
    (arXiv:[2509.05208](https://arxiv.org/abs/2509.05208), `MEASURED-BENCH` `[verbatim]`).
  - **VectorEdits** — 270k+ SVG edit pairs; "current methods struggle to produce accurate and valid
    edits" (arXiv:[2506.15903](https://arxiv.org/abs/2506.15903), `MEASURED-BENCH` `[verbatim]`).

  **The distinction the survey must draw: SVG is an excellent *output format* and a bad *generation
  target*.** You want SVG on the page (it is text, it scales, it can carry ARIA structure — §6.3). You
  do not want an LLM computing its path coordinates. Emit Tier A/B and let a renderer produce the SVG.

- **D3.js** (`d3/d3`, 113,293★, ISC, `OBSERVED`) and **p5.js** (`processing/p5.js`, 23,823★, LGPL-2.1,
  `OBSERVED`). Imperative, no layout engine, no scene graph. Raiven's measured conclusion — a mediating
  DSL that compiles to D3 reaching **100% compilation** and 6× cheaper than direct generation
  (arXiv:[2604.10008](https://arxiv.org/abs/2604.10008), `MEASURED-BENCH`, via A2) — is the field's
  verdict on direct D3.

**Tier E — Raster text-to-image (no gates at all).**

- Diffusion / native image models. **SciDraw-Bench** ("Can AI Draw Science?") built 32 structured tasks
  over 8 figure types across 10 disciplines, each with a "machine-checkable specification of required
  labels, relations, components, conventions," and found domain-specific systems substantially beat
  general text-to-image models, with "**text fidelity remains the hardest dimension for all systems**"
  (arXiv:[2606.28406](https://arxiv.org/abs/2606.28406), `MEASURED-BENCH` `[fetched-summary]`).
  **ScImage** — 11 scientist raters over spatial, numeric and attribute comprehension in English,
  German, Farsi and Chinese — found GPT-4o acceptable on single-dimension prompts but that "all models
  face challenges in this task, especially for more complex prompts"
  (arXiv:[2412.02368](https://arxiv.org/abs/2412.02368), `MEASURED-BENCH` `[verbatim]`).
  A raster figure cannot be parsed, diffed, edited, or made screen-reader-navigable. For a teaching
  figure with any text in it, **Tier E is disqualified**, not merely discouraged.

### 1.3 The one-line rule

> **Rank = how much of the drawing the model is *not* asked to do.** Every coordinate the model computes
> is a coordinate that can be silently wrong, and there is no gate that catches it.

---

## 2. Measured LLM performance and the degradation curve

### 2.1 Degradation with complexity is the universal finding

| Benchmark | Scale | Degradation finding |
|---|---|---|
| **SVGenius** (arXiv:[2506.03139](https://arxiv.org/abs/2506.03139)) | 2,377 queries, 24 domains, 22 models, 18 metrics | "**all models exhibit systematic performance degradation with increasing complexity**"; style transfer hardest capability across all model types `[verbatim]` |
| **VGBench** (arXiv:[2407.10972](https://arxiv.org/abs/2407.10972)) | 4,279 + 5,845 samples | strong overall, "less desirable performance on **low-level formats (SVG)**" `[verbatim]` |
| **ScImage** (arXiv:[2412.02368](https://arxiv.org/abs/2412.02368)) | 5 models, 11 human raters, 4 languages | fine on one comprehension dimension at a time; degrades sharply when spatial + numeric + attribute must combine `[verbatim]` |
| **FeynmanBench** (arXiv:[2604.03893](https://arxiv.org/abs/2604.03893)) | 2,000+ tasks, 19 MLLMs | "models achieve **70–95% on local recognition** (vertex and propagator identification) but **collapse to 13–17% on topological reconstruction**" `[fetched-summary]` |
| **GeoR-Bench** (arXiv:[2605.11541](https://arxiv.org/abs/2605.11541)) | 440 samples, 6 categories, 24 task types, 21 models | best model **42.7%** strict accuracy; best open-source **10.3%** `[fetched-summary]` |
| **ChartMimic** (arXiv:[2406.09961](https://arxiv.org/abs/2406.09961)) | 4,800 human-curated triplets, 18+4 chart types, 201 subcategories, 17 models | GPT-4o / InternVL2-Llama3-76B average **82.2** on Direct Mimic but **61.6** on Customized Mimic `[verbatim]` — a 20-point drop for adding a *requirement* |
| **Plot2Code** (arXiv:[2405.07990](https://arxiv.org/abs/2405.07990)) | 132 matplotlib plots, 14 MLLMs | "most existing MLLMs struggle with visual coding for **text-dense plots**, heavily relying on textual instruction" `[verbatim]` |

The shape is the same everywhere: **near-ceiling on the atomic sub-task, collapse on the composition.**
FeynmanBench's 70–95% → 13–17% is the most vivid single instance in the literature, and it is the
correct mental model for what happens when a figure has to be right *as a whole* rather than right in
each glyph.

### 2.2 The Socratic Chart result — models read text, not geometry

**Socratic Chart** (arXiv:[2504.09764](https://arxiv.org/abs/2504.09764), `MEASURED-BENCH` `[verbatim]`)
constructs a harder test scenario by **removing textual labels from ChartQA charts and applying
perturbations**. Under those conditions, "models like **GPT-4o and Gemini-2.0 Pro experience up to a 30%
performance drop**." The paper's framing is that existing benchmarks "reveal significant reliance on
text-based shortcuts and probabilistic pattern-matching rather than genuine visual reasoning."

**Why this is load-bearing for C1**, in three steps:

1. It bounds every render-and-inspect verification loop. If the checker's accuracy is carried by OCR of
   the labels, then a figure whose *geometry* is wrong but whose *labels* are right will pass. That is
   precisely the legible-but-wrong class we are trying to catch. **The VLM is blindest exactly where we
   need it to see.**
2. It bounds every "AI grades the student's diagram" feature. A student's hand-drawn diagram is
   label-sparse and geometry-dense — the worst case.
3. It explains why the field's answer is symbolic: Socratic Chart's own fix is to convert the chart
   image into **SVG** and reason over the symbolic primitives (bar heights, line coordinates) with an
   agent-critic validating them. Same architecture as §4.

Two corroborations of the same shortcut, in different domains:

- **The "Mirage" phenomenon** (arXiv:[2604.27969](https://arxiv.org/abs/2604.27969), `MEASURED-BENCH`
  `[fetched-summary]`): in circuit-diagram→Verilog generation, "replacing a circuit diagram with a
  **blank image** leaves Pass@k **unchanged or even higher**" because models read identifier names in
  the module header instead of the picture. Gaps between normal and identifier-anonymised modes across
  eight MLLMs confirmed that "high Normal-mode accuracy is largely a Mirage." **The blank-image ablation
  is the single cheapest diagnostic in this entire section and every figure-checking pipeline should run
  it.** If your VLM checker scores the same on a blank canvas, it is not looking.
- **GPT-Vision on scientific images** (arXiv:[2311.02069](https://arxiv.org/abs/2311.02069),
  Hwang, Head & Callison-Burch, `MEASURED-BENCH` `[fetched-summary]`): documented sensitivity to
  prompting, to **counterfactual text in the image**, and to **spatial relationships**. The
  counterfactual-text sensitivity is the Socratic Chart finding stated as a qualitative failure mode:
  when the text disagrees with the picture, the model follows the text.

### 2.3 The execution-success ceiling has been reached, and it did not deliver correctness

- Ford & Rios: ~15% → **4.5%** execution errors in 3 repair iterations on Text2Chart31; **4.6%** on
  ChartX. "Under current benchmarks, execution success appears largely solved." Then:
  **6/100 sampled charts contain hallucinations**; colourblind-safe rate **33.3% / 7.2%**
  (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH` `[verbatim]`).
- PairCoder++, across **17 public benchmarks and 7 models from 3 vendors**, improves "essentially every
  benchmark whose artifact is verifiable" — Blender scene executability **0.20 → 0.78**, TikZ compile
  rate **+10–30 points** — at **2.9–9.2× single-model cost (~7× overall)**
  (arXiv:[2607.01883](https://arxiv.org/abs/2607.01883), `MEASURED-BENCH` `[verbatim]`).

**The number pair to carry into the survey: 4.5% execution failure and 6% hallucination rate on the
charts that ran.** After all that engineering, the probability that a delivered figure is *wrong* now
exceeds the probability that it fails to *exist*.

### 2.4 Negative and null results (PRD §2 requirement — five of them)

1. **`MEASURED-BENCH` — execution repair does not buy correctness.** Ford & Rios,
   arXiv:[2506.06175](https://arxiv.org/abs/2506.06175): errors 15%→4.5%, hallucinations still 6/100,
   accessibility 33.3%/7.2%. *The paper's own title is the null result.*
2. **`MEASURED-BENCH` — visual/constraint feedback does not reliably enable self-correction.**
   GeoBuildBench: state-of-the-art multimodal models "frequently exhibit **structural hallucinations,
   missing objects, and failures to satisfy geometric constraints**, with **limited ability to exploit
   visual and constraint-based feedback for self-correction**"
   (arXiv:[2605.13167](https://arxiv.org/abs/2605.13167) `[fetched-summary]`). This is a direct null on
   the render-and-inspect loop that the rest of the field assumes works.
3. **`MEASURED-BENCH` — the toolchain-review method admits where it fails.** PairCoder++: improvements
   "concentrate where the toolchain provides an informative oracle and the baseline leaves headroom, and
   the method **ties or mildly regresses where the oracle is weak**"
   (arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) `[verbatim]`). Verification-in-the-loop is not
   free and is not universal.
4. **`MEASURED-BENCH` — grammar constraints fix syntax and not meaning.** An empirical study of
   structured-output control in software engineering finds "TTMG nearly eliminates syntax errors, yet
   **substantial structural and semantic errors persist**"
   (arXiv:[2606.09395](https://arxiv.org/abs/2606.09395) `[fetched-summary]`). Grammar-Aligned Decoding
   further shows constrained decoding "**distorts the LLM's distribution**," producing outputs that are
   grammatical but improperly weighted (arXiv:[2405.21047](https://arxiv.org/abs/2405.21047)
   `[fetched-summary]`), and a 2026 study identifies a "**constraint tax**" in open-weight models where
   grammar constraints suppress tool use (arXiv:[2606.25605](https://arxiv.org/abs/2606.25605)
   `[fetched-summary]`). **Constrained decoding is a G1 device only. Budget for it as such.**
5. **`MEASURED-BENCH` — 100% syntactic validity, unreliable content.** Nine LLMs, 90 PlantUML diagrams,
   3,373 methods: all valid, all conforming, still inconsistent in annotations and signatures, authors
   conclude "human oversight is essential"
   (arXiv:[2506.00788](https://arxiv.org/abs/2506.00788) `[fetched-summary]`).
6. **`OBSERVED — absence`.** No LLM-generation literature exists for **Asymptote**; none was found for
   **Excalidraw** scene JSON or **Observable** (A2 §3.7 concurs). Choosing these targets means choosing
   an unmeasured base rate.

---

## 3. The documented failure taxonomy

Seven classes. Each has a citation and each maps to a check in §5.

### 3.1 Label collision, text overflow, clipping, and canvas escape

The single most-reported defect, and now precisely enumerated. **Visual-SDPO** names the recurring set
verbatim — "otherwise executable code often yields artifacts with visually salient defects, including
**overlapping elements, clipped text, broken alignment, low contrast, and overflow**" — and builds
Visual-Grounded Code Credit Weighting to trace each detected defect back to the responsible code
statements (arXiv:[2606.10334](https://arxiv.org/abs/2606.10334), `MEASURED-BENCH` `[fetched-summary]`;
>10 absolute points over zero-shot base on ChartMimic/Design2Code/AeSlides).

**GeoSVG-RL** gives the same list from the diagram side: "minor errors such as **misaligned connector
endpoints, text labels overlapping borders, or complex layouts drifting beyond the canvas boundaries**
render the resulting SVG files functionally unusable for professional applications"
(arXiv:[2605.25447](https://arxiv.org/abs/2605.25447), `MEASURED-BENCH` `[verbatim from fetched abs]`).

ALGOGEN independently names **element overlap** as one of three core failures of end-to-end generation
(arXiv:[2605.12159](https://arxiv.org/abs/2605.12159) `[verbatim]`).

**This class is a Tier-C/D-only disease.** In Vega-Lite, Mermaid, DOT or PlantUML it is structurally
impossible because a layout engine places things.

### 3.2 Arrows that point at nothing

Not a joke failure — a named, measured metric. GeoSVG-RL's six reward dimensions include **precise
anchor placement** and reports gains specifically in "**arrow-anchor accuracy**"
(arXiv:[2605.25447](https://arxiv.org/abs/2605.25447) `[verbatim from fetched abs]`). SciDraw-Bench
evaluates "components, arrows, and text" as separate structural axes, and SciForma-9B is claimed to
exceed all open-source baselines and GPT-Image-1.5 on exactly that decomposition
(arXiv:[2607.18091](https://arxiv.org/abs/2607.18091), `MEASURED-BENCH` `[fetched-summary]`).

Pedagogically this is the worst layout defect, because an arrow *is* the claim: an arrow from the wrong
box asserts a causal or structural relation that does not hold, and the learner has no way to know.

### 3.3 Spatial-relation errors and occlusion

- ScImage evaluates **spatial** comprehension as a first-class axis and reports failure under
  composition (arXiv:[2412.02368](https://arxiv.org/abs/2412.02368) `[verbatim]`).
- SGP-GenBench isolates **spatial relations** alongside attribute binding and numeracy
  (arXiv:[2509.05208](https://arxiv.org/abs/2509.05208) `[verbatim]`).
- GPT-Vision on scientific images: documented difficulty with "relative positions of elements"
  (arXiv:[2311.02069](https://arxiv.org/abs/2311.02069) `[fetched-summary]`).
- Vision2Code: leading models "perform well on charts/graphs but remain weak on **spatial scenes**,
  chemistry, documents, and circuit diagrams"
  (arXiv:[2605.11307](https://arxiv.org/abs/2605.11307), `MEASURED-BENCH` `[fetched-summary]`).

### 3.4 Wrong axes, wrong scales, misleading encodings

The finding that matters here is not that models *produce* bad axes — it is that they cannot reliably
*detect* them.

- **"When Visuals Aren't the Problem"** (arXiv:[2603.22368](https://arxiv.org/abs/2603.22368),
  `MEASURED-BENCH` `[fetched-summary]`): taxonomy split into **design errors** (truncated axes, dual
  axes, inappropriate encodings) and **reasoning errors** (cherry-picking, causal inference). VLMs
  "detect visual design errors substantially more reliably than reasoning-based misinformation, **and
  frequently misclassify non-misleading visualizations as deceptive**." Both error directions, with the
  false-positive direction being the one that makes an automated gate unusable without calibration.
- **"Do LLMs Understand Data Visualization Rules?"** (arXiv:[2602.20137](https://arxiv.org/abs/2602.20137),
  `MEASURED-BENCH` `[fetched-summary]`): ~2,000 Vega-Lite specs with annotated violations derived from
  the **Draco** constraint system. **F1 up to 0.82 on common violations, below 0.15 on subtle perceptual
  rules.** Translating Draco's Answer Set Programming constraints into natural language boosted small
  models by **up to 150%**. Conclusion: LLMs "underperform compared to symbolic solvers — particularly on
  nuanced visual perception tasks."
- Companion paper (arXiv:[2602.20084](https://arxiv.org/abs/2602.20084) `[fetched-summary]`): "frontier
  models tend to be **more effective at correcting violations than at detecting them reliably**."
  **This asymmetry is an architectural instruction: use a symbolic checker to detect, and the LLM to
  repair.** Do not use the LLM as the detector.

### 3.5 Mathematically or structurally incorrect content

- SciFlow-Bench: "visually plausible but structurally incorrect"
  (arXiv:[2602.09809](https://arxiv.org/abs/2602.09809) `[fetched-summary]`).
- GeoR-Bench: visual consistency "frequently surpass[es] their scientific accuracy"
  (arXiv:[2605.11541](https://arxiv.org/abs/2605.11541) `[fetched-summary]`).
- GeoBuildBench: "structural hallucinations, missing objects, and failures to satisfy geometric
  constraints" (arXiv:[2605.13167](https://arxiv.org/abs/2605.13167) `[fetched-summary]`).
- FeynmanBench: topological reconstruction collapses to 13–17%
  (arXiv:[2604.03893](https://arxiv.org/abs/2604.03893) `[fetched-summary]`).
- ALGOGEN's diagnosis of the mechanism: requiring the model to "simultaneously simulate algorithm flow
  and satisfy video rendering constraints" is what "induces LLM hallucinations"
  (arXiv:[2605.12159](https://arxiv.org/abs/2605.12159) `[verbatim]`). **The cause is capacity
  contention between semantics and layout, not a knowledge gap.** That is why decoupling works.

### 3.6 Silent data errors — the chart that renders beautifully and encodes the wrong column

Raiven's term (arXiv:[2604.10008](https://arxiv.org/abs/2604.10008), via A2). Two 2026 papers add
mechanism:

- **Chart Specification** (arXiv:[2602.10880](https://arxiv.org/abs/2602.10880), `MEASURED-BENCH`
  `[fetched-summary]`) attributes hallucination to training that "encourage[s] surface-level token
  imitation rather than faithful modeling of underlying chart structure," and fixes it with structured
  intermediate representations (up to **61.7%** over baselines on complex benchmarks with 3k samples).
- **Observation-Aligned supervision** (arXiv:[2607.04726](https://arxiv.org/abs/2607.04726),
  `MEASURED-BENCH` `[verbatim]`) identifies a *theoretical* limit that everyone doing round-trip
  verification must internalise: "many chart programs contain **latent raw variables that cannot be
  uniquely recovered from the rendered image**. For example, a boxplot exposes summary statistics rather
  than original samples, a pie chart reveals proportions rather than arbitrary raw values, and a
  histogram shows bin-level mass rather than individual observations. Supervising models to reproduce
  such **non-identifiable** quantities encourages hallucination and over-specified code generation."
  **Corollary for §5.5: a round-trip check can only assert what is identifiable from the artifact.**
  Asking a checker to recover a histogram's raw samples *manufactures* hallucination.

### 3.7 Legible but factually wrong — the class that teaches misconceptions

This is 3.4 + 3.5 + 3.6 seen from the learner's chair, and it deserves its own name because its
remediation is different. The other classes are *ugly*; this one is *beautiful*. A learner has no
signal that anything is wrong, no reason to re-check, and the figure's polish functions as a
credibility claim.

The empirical anchor is Ford & Rios's **6/100** post-repair hallucination rate on charts that all ran
(arXiv:[2506.06175](https://arxiv.org/abs/2506.06175) `[verbatim]`), and the mechanism anchor is the
Mirage ablation (arXiv:[2604.27969](https://arxiv.org/abs/2604.27969) `[fetched-summary]`) showing that
apparent visual competence can be entirely text-mediated.

**`INFERENCE` (flagged as inference, and as a research gap):** no study in this literature measures
whether a learner exposed to a legible-but-wrong generated figure acquires the corresponding
misconception, nor how durable it is. The misconceptions literature (B1) says misconceptions are
sticky and resistant to correction; the figure-generation literature says ~6% of delivered figures are
wrong. Nobody has multiplied those two facts together. **See §8.**

---

## 4. The convergent architecture: constrain the LLM to a verifiable IR, let a deterministic renderer draw

### 4.1 The independent rediscoveries

| # | System | The IR | The renderer / checker | Measured result |
|---|---|---|---|---|
| 1 | **ALGOGEN** (arXiv:[2605.12159](https://arxiv.org/abs/2605.12159)) `[verbatim]` | **VTA** — "Visualization Trace Algebra, a monoid over algorithm visual states and operations," emitted as **VTA-JSON** by an LLM-written Python tracker; layout templated separately in **RSL** (Rendering Style Language) | deterministic compiler → Manim, LaTeX/TikZ, or Three.js | **82.5% → 99.8%** success on a 200-task LeetCode AV benchmark (**+17.3 pts avg**) |
| 2 | **Raiven** (arXiv:[2604.10008](https://arxiv.org/abs/2604.10008)) via A2 | RaivenDSL | compiles to D3 / VTK.js | **100% compilation**, up to **6× faster and 6× cheaper**, 100-task benchmark |
| 3 | **Flint** (arXiv:[2607.20775](https://arxiv.org/abs/2607.20775)) `[verbatim from fetched abs]` | "hierarchical **data semantic model**" — the author declares field *meanings*; scales/axes/formatting are derived, not specified | compiles to **Vega-Lite, Apache ECharts, and Chart.js** | explicitly positioned as "an effective intermediate language for both humans **and AI agents** to create visualizations" |
| 4 | **Chart Specification** (arXiv:[2602.10880](https://arxiv.org/abs/2602.10880)) `[fetched-summary]` | structural chart spec | chart code | up to **+61.7%** on complex benchmarks with 3k training samples |
| 5 | **GeoSVG-RL** (arXiv:[2605.25447](https://arxiv.org/abs/2605.25447)) `[verbatim from fetched abs]` | "a structured **layout plan** that serves as a **geometric contract** for the subsequent generation of the SVG code" | browser-backed verifier computing six-dimensional rewards | gains in arrow-anchor accuracy and text-in-box rates |
| 6 | **DiagramIR** (arXiv:[2511.08283](https://arxiv.org/abs/2511.08283)) `[verbatim]` | IR parsed *out of* TikZ | IR-level comparison instead of image comparison | higher human agreement than LLM-as-a-Judge; **GPT-4.1-Mini ≈ GPT-5 at 10× lower cost** |
| 7 | **Socratic Chart** (arXiv:[2504.09764](https://arxiv.org/abs/2504.09764)) `[verbatim]` | SVG primitives (bar heights, line coordinates) extracted by agent-generators | agent-critic validates the symbolic representation | surpasses SOTA at capturing chart primitives |
| 8 | **SciFlow-Bench** (arXiv:[2602.09809](https://arxiv.org/abs/2602.09809)) `[fetched-summary]` | structured graph | "closed-loop, **round-trip protocol** that inverse-parses generated diagram images back into structured graphs for comparison" | structure-aware evaluation beats visual-similarity metrics |
| 9 | **GeoBuildBench** (arXiv:[2605.13167](https://arxiv.org/abs/2605.13167)) `[fetched-summary]` | geometric-construction DSL | executable construction + constraint satisfaction | frames geometry as executable grounding, not plausibility |

Plus the *review*-side variant, which is the same principle applied to the loop rather than the
representation: **PairCoder++** grounds a Driver/Navigator pair in "diagnostics, execution results, and
renderings of the current artifact beside the target," across 17 benchmarks and 7 models
(arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) `[verbatim]`).

### 4.2 Why it works — stated as a mechanism, not a vibe

ALGOGEN gives the causal claim in one sentence: end-to-end generation "requires the system to
simultaneously simulate algorithm flow and satisfy video rendering constraints, such as element layout
and color schemes. **This complex task induces LLM hallucinations**"
(arXiv:[2605.12159](https://arxiv.org/abs/2605.12159) `[verbatim]`). The failure is **capacity
contention**. The model has finite reasoning budget per token and is being asked to hold the semantics
of the concept and the geometry of the page in the same forward pass. Splitting them:

- makes the semantic output **small** (a JSON trace, a Vega-Lite spec, a DOT graph) — fewer tokens,
  fewer opportunities to drift;
- makes the semantic output **checkable** — a schema, a monoid law, a constraint set;
- makes the geometry **exact** — a renderer never miscomputes a bounding box;
- makes the artifact **re-targetable** — ALGOGEN's one trace renders to Manim *or* TikZ *or* Three.js;
  Flint's one spec renders to Vega-Lite *or* ECharts *or* Chart.js. For an education system that must
  serve a static PDF, a screen-reader page, and an interactive widget from the same idea, this is not a
  convenience — it is the only affordable way to hit H1's multi-modal requirement.

### 4.3 Therefore: the standard

> **A generated educational figure MUST be produced by rendering a declarative specification that the
> model emitted and that a machine validated. The model MUST NOT compute layout coordinates for any
> figure that ships to a learner.**

Nine independent groups, five different domains, one architecture, with the only clean ablation
(ALGOGEN's 82.5%→99.8%) pointing the same way. This is as close to a settled engineering result as this
literature has. Treating it as optional is the position that now requires evidence.

---

## 5. Can you test a diagram? Yes — six mechanisms, ranked by trustworthiness

### 5.1 Compile / execute gate — cheap, necessary, weakest

Free, deterministic, high recall for the class it covers, zero coverage of everything else. Measured
gains: PairCoder++ TikZ **+10–30 points**, Blender executability **0.20→0.78**
(arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) `[verbatim]`); agentic repair **15%→4.5%**
(arXiv:[2506.06175](https://arxiv.org/abs/2506.06175) `[verbatim]`). Cost: PairCoder++ runs at
**2.9–9.2× single-model cost, ~7× overall** — a real number for F4's arithmetic.

Grammar-constrained decoding sits here too and only here (§2.4 item 4).

### 5.2 Programmatic assertions on layout and axes — the highest value-per-unit-cost check

This is deterministic, cheap, has no model in the loop, and directly targets §3.1–3.4. GeoSVG-RL's six
verifier dimensions are the best published starting checklist
(arXiv:[2605.25447](https://arxiv.org/abs/2605.25447) `[verbatim from fetched abs]`):

1. **rendering validity** 2. **canvas fitting** 3. **precise anchor placement**
4. **text containment** 5. **graph consistency** 6. **code cleanliness**

Concretely implementable assertions, per target:

| Check | Implementation |
|---|---|
| **No label collision** | render → extract text bounding boxes (SVG DOM `getBBox()`, or `matplotlib` `Text.get_window_extent`) → assert pairwise IoU = 0 |
| **Text containment / canvas fit** | assert every element bbox ⊆ viewBox; assert every label bbox ⊆ its container shape |
| **Arrow anchors** | assert each arrow endpoint lies within ε of a named node's boundary; **assert no arrow endpoint is unattached** |
| **Axis sanity** | assert `get_xscale`/`get_yscale` matches the declared scale; assert axis limits contain the data range; **assert a bar chart's y-axis includes 0** (the truncated-axis check from arXiv:[2603.22368](https://arxiv.org/abs/2603.22368)); assert tick label count ≤ N |
| **Unit sanity** | assert axis label carries a unit string; assert declared unit matches the spec's unit; range-check magnitudes against the domain spec |
| **Curve correctness** | for a plotted function, recompute `f(x)` independently (SymPy / numpy) and assert max abs deviation from `line.get_ydata()` < ε — **this catches the "mathematically incorrect curve" class outright and nothing else does** |
| **Spatial contiguity (§7)** | assert distance(label bbox, referent bbox) < threshold; assert legend-only encoding is absent |
| **Colour-only encoding (§6)** | assert every series carries a second channel (marker/dash/pattern); run a deuteranopia/protanopia simulation and assert pairwise ΔE above threshold |
| **Contrast** | WCAG 2.2 contrast ratio ≥ 4.5:1 for text, ≥ 3:1 for non-text |

The symbolic-solver path generalises this: **Draco / Draco 2** encode visualization design knowledge as
Answer Set Programming constraints (arXiv:[2308.14247](https://arxiv.org/abs/2308.14247),
`OBSERVED` `[fetched-summary]`; the knowledge base itself derived from ~30 graphical-perception papers,
arXiv:[2308.14241](https://arxiv.org/abs/2308.14241)). And the measured verdict on using an LLM instead
of the solver is unambiguous: **F1 ≤ 0.82 common / < 0.15 subtle, "underperform compared to symbolic
solvers"** (arXiv:[2602.20137](https://arxiv.org/abs/2602.20137) `[fetched-summary]`).

### 5.3 IR-level comparison — best correlated with human judgement

**DiagramIR** is the only education-specific figure-evaluation pipeline in the literature: parse the
generated TikZ into an IR and compare IRs rather than images; reports **higher agreement with human
raters than LLM-as-a-Judge**, and enables a 10×-cheaper model to match GPT-5
(arXiv:[2511.08283](https://arxiv.org/abs/2511.08283) `[verbatim]`). If the figure was generated *from*
an IR (§4), this check is nearly free: diff the emitted IR against the requested spec.

### 5.4 Render-and-inspect with a VLM — use it, distrust it, and calibrate it

The evidence against relying on a VLM checker, assembled:

| Result | Implication for the checker |
|---|---|
| Socratic Chart: **up to 30% drop** when labels removed (arXiv:[2504.09764](https://arxiv.org/abs/2504.09764)) `[verbatim]` | the checker is reading text, not geometry — blind to geometric error |
| Mirage: **blank image leaves Pass@k unchanged or higher** (arXiv:[2604.27969](https://arxiv.org/abs/2604.27969)) `[fetched-summary]` | the checker may not be looking at the image at all |
| Misleading-viz benchmark: VLMs "**frequently misclassify non-misleading visualizations as deceptive**" (arXiv:[2603.22368](https://arxiv.org/abs/2603.22368)) `[fetched-summary]` | high false-positive rate ⇒ unusable as a hard gate without calibration |
| Viz-rules benchmark: **F1 < 0.15** on subtle perceptual rules (arXiv:[2602.20137](https://arxiv.org/abs/2602.20137)) `[fetched-summary]` | near-chance exactly where human designers add value |
| GeoBuildBench: "**limited ability to exploit visual and constraint-based feedback for self-correction**" (arXiv:[2605.13167](https://arxiv.org/abs/2605.13167)) `[fetched-summary]` | the *loop* fails, not just the judgement |
| Text-to-Automata: VLM descriptions of student diagrams "often incorrect," human correction substantially improves quality (arXiv:[2603.07936](https://arxiv.org/abs/2603.07936), via A2) `[B]` | VLM diagram *reading* bounds any grade-my-diagram feature |

And the evidence *for* keeping it: it is the only mechanism that catches aesthetic and gestalt defects a
solver has no predicate for, and Visual-SDPO shows visual feedback is a usable *training* signal when
grounded to code statements (arXiv:[2606.10334](https://arxiv.org/abs/2606.10334) `[fetched-summary]`).
And note the asymmetry from arXiv:[2602.20084](https://arxiv.org/abs/2602.20084): models "are more
effective at **correcting** violations than at **detecting** them reliably."

> **Rule: symbolic checks detect; the VLM repairs; the VLM never gates alone.**
> **Mandatory calibration: run the blank-image ablation on your own checker.** If the score does not
> drop, the checker is not looking at the figure. This is one line of code and it is the highest-value
> diagnostic in §5.

### 5.5 Round-tripping — generate → describe back → compare

Three instantiations, all 2025–2026, all independent:

- **SciFlow-Bench**: "closed-loop, round-trip protocol that inverse-parses generated diagram images back
  into structured graphs for comparison" (arXiv:[2602.09809](https://arxiv.org/abs/2602.09809))
  `[fetched-summary]`.
- **VCode / CodeVQA**: "a policy model answers questions over rendered SVGs; correct answers indicate
  faithful symbolic preservation" (arXiv:[2511.02778](https://arxiv.org/abs/2511.02778)) `[verbatim]`.
- **CharTide's Inspector**: "information invariance — a downstream model should yield consistent answers
  to identical visual queries across both original and generated charts," verified by a **frozen**
  Inspector over atomic QA tasks, giving verifiable reward from answer accuracy rather than VLM scoring
  (arXiv:[2604.22192](https://arxiv.org/abs/2604.22192), `MEASURED-BENCH` `[verbatim]`).

**The design that makes round-tripping honest** is CharTide's: don't ask "describe this figure and see
if it matches"; ask a **fixed set of atomic questions whose answers were specified in advance**, and
score answer accuracy. That converts a fuzzy similarity judgement into a pass/fail assertion, and it
composes directly with §7's "one idea per figure" — if the figure carries one idea, the atomic question
set is small and can be authored alongside the figure.

**The hard limit, from arXiv:[2607.04726](https://arxiv.org/abs/2607.04726) `[verbatim]`:** round-trip
checks can only assert **identifiable** quantities. A boxplot does not contain its samples; a histogram
does not contain its observations. Asking a round-trip checker to recover them "encourages hallucination
and over-specified code generation." **Write the question set against what the figure can actually
answer.**

Two further cautions on VLM judges generally: MLLM-as-a-judge shows calibration and orientation failures
under ambiguity, with cross-pool human agreement itself weak (r = −0.12 on one dimension) even where
within-pool reliability was strong (α = 0.86 / 0.74) — arXiv:[2606.20676](https://arxiv.org/abs/2606.20676)
`[fetched-summary]`. Where automated judging *does* validate well, it is on ranking, not absolute
correctness: ArtifactsBench reports **94.4% ranking consistency with WebDev Arena** and **>90% pairwise
agreement with human experts** (arXiv:[2507.04952](https://arxiv.org/abs/2507.04952) `[fetched-summary]`).
**Judges rank; solvers verify.**

### 5.6 Human review — what cannot be delegated

See §9.4. Non-negotiably human: **the first instance of any new figure template**, any figure asserting
a **causal** claim, any figure in a **high-stakes or assessed** context, and any figure whose subject the
system cannot check symbolically. ScImage used **11 scientists**; the PlantUML study's conclusion was
"human oversight is essential"; DiagramIR exists specifically to *reduce* — not remove — human raters.

---

## 6. Accessibility as correctness, not as a feature

Per H1, WCAG 2.2 AA is a **floor**. This section's contribution is that accessibility failures in
generated figures are *measured*, *severe*, and *fixable* — which removes every excuse.

### 6.1 The measured baseline is bad

- **Colour-only encoding is the default output.** Only **33.3%** (Text2Chart31) and **7.2%** (ChartX) of
  generated charts satisfied basic colourblindness guidelines *after* the execution problem was solved
  (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175), `MEASURED-BENCH` `[verbatim]`). A 7.2% pass
  rate is not a long tail; it is the modal output being inaccessible.
- **Default generated web code is non-compliant.** "ChatGPT can effectively address accessibility issues
  when prompted, [but] its default code often lacks compliance"
  (arXiv:[2501.03572](https://arxiv.org/abs/2501.03572), `OBSERVED` case study `[fetched-summary]`).

### 6.2 It is fixable, and the fix is measured — which makes it mandatory

**A11yn** is the first method to optimise a code-generating LLM for WCAG compliance, using a reward that
penalises violations by severity from automated testing; trained on **UIReq-6.8K**, evaluated on
**RealUIReq-300**, it achieves a **60% reduction in Inaccessibility Rate over the base model while
maintaining semantic accuracy and visual quality** (arXiv:[2510.13914](https://arxiv.org/abs/2510.13914),
`MEASURED-BENCH` `[fetched-summary]`). A related result on UI principle violations moves a VLM detector
from **36% → 84% micro-F1**, with 13 of 19 principles above 80% F1
(arXiv:[2607.20690](https://arxiv.org/abs/2607.20690), `MEASURED-BENCH` `[fetched-summary]`).

**`INFERENCE`:** given a 60% reduction is achievable with a reward signal, and given that the checks in
§5.2 (contrast ratio, colour-difference under CVD simulation, second-channel encoding) are all
deterministic and free at inference time, shipping a colour-only figure is a choice, not a limitation.

### 6.3 Screen-reader-navigable structure — why the target choice in §1 is an accessibility decision

A raster figure has exactly one accessibility affordance: a caption. A rendered **SVG** has a DOM: it can
carry `<title>`, `<desc>`, `role="img"`/`role="graphics-document"`, `aria-labelledby`, and a
structural hierarchy a screen reader can walk. **Chart4Blind** demonstrates the target state —
converting bitmap line charts into "end-to-end accessible SVGs suitable for assistive technologies such
as embossed prints (papers and laser cut), 2D tactile displays, and screen readers," plus CSV and alt
text; SUS **90%**, ~4 minutes per chart for a sighted user
(arXiv:[2403.06693](https://arxiv.org/abs/2403.06693), `MEASURED-BENCH` `[fetched-summary]`).

This is the accessibility argument for §1's ranking, and it is decisive: **Tier A/B targets render to
structured SVG carrying the semantic hierarchy for free; Tier E raster cannot ever.** Choosing the
generation target *is* choosing whether a blind learner can use the figure.

Beyond alt text, the multimodal layer: **Py maidr** encodes tactile, auditory and conversational
representations from Matplotlib/Seaborn with "minimal performance overhead," explicitly framed as
"design *for us*" rather than "design for them"
(arXiv:[2509.13532](https://arxiv.org/abs/2509.13532), `OBSERVED` `[fetched-summary]`);
**tactile charts** with 12 BLV participants found 3D-printed templates "support chart type
understanding" and were the preferred learning method for complex chart types (UpSet, violin, clustered
heatmap, faceted line) (arXiv:[2507.21462](https://arxiv.org/abs/2507.21462), `MEASURED-BENCH`
`[fetched-summary]`); and **conversational tactile data interfaces** found users "reserved the
conversational agent for tasks touch couldn't resolve"
(arXiv:[2607.14588](https://arxiv.org/abs/2607.14588), `OBSERVED` `[fetched-summary]`) — a useful
correction to the assumption that a chatbot replaces a tactile display.

### 6.4 Is there work on *generated alt-text quality for scientific figures*? — Yes, and it is a warning

**The direct answer to the brief's question.** There is a 2026 PRISMA systematic survey with a
ROBIS risk-of-bias assessment: **"A Systematic Survey on Image Description Techniques for STEM Domains"**
(Cardia, Angileri, Buzzi, Galesi & Leporini, arXiv:[2607.21611](https://arxiv.org/abs/2607.21611),
`MEASURED-META` `[verbatim from fetched abs]`), covering **20 peer-reviewed studies**. Its findings,
quoted:

> "The analysis reveals a shift from static, one-shot alt text toward interactive and multimodal systems
> that integrate conversational interfaces, keyboard navigation, and audio or haptic feedback. However,
> critical challenges persist, including **factual inaccuracies and hallucinations**, the **scarcity of
> accessibility-first datasets co-designed with blind and low-vision users**, and a **heavy reliance on
> automatic text-overlap metrics that poorly capture perceived usefulness and trust**."

Its recommended directions — "user-controlled verbosity, explainable and **verifiable** AI pipelines,
and integration into mainstream STEM authoring and learning environments" — are the same architecture as
§4, arrived at from the accessibility side.

Corroborating primary results:

- **MatplotAlt** (Nylund, Mankoff & Potluri, EuroVis 2025, arXiv:[2503.20089](https://arxiv.org/abs/2503.20089),
  `MEASURED-BENCH` `[fetched-summary]`): a one-line Python package for alt text on Matplotlib figures.
  Key finding: "**state-of-the-art LLMs still struggle with factual errors when describing charts**,"
  and accuracy improved by "prompting GPT4-turbo with **heuristic-based alt text or data tables parsed
  from the Matplotlib figure**." **This is the design rule in one sentence: describe the figure from its
  source specification, never from its pixels.** It is the §4 architecture applied to alt text — and it
  is the reason alt text should be generated *at the same time as the figure, from the same IR*, not
  bolted on afterwards by a VLM looking at a PNG.
- **Grounded Intuition of GPT-Vision** (Hwang, Head & Callison-Burch,
  arXiv:[2311.02069](https://arxiv.org/abs/2311.02069), `MEASURED-BENCH` `[fetched-summary]`): GPT-Vision
  alt text for scientific figures is sensitive to prompting, to **counterfactual text in the image**, and
  to **spatial relationships**.
- **Context Matters** (Kreiss, Bennett, Hooshmand, Zelikman, Morris & Potts, EMNLP 2022,
  arXiv:[2205.10646](https://arxiv.org/abs/2205.10646), `MEASURED-BENCH` `[fetched-summary]`): BLV
  participants rated descriptions; **referenceless metrics do not take context into account, "whereas
  contextual information is highly valued by BLV users."** So the *evaluation* of generated alt text is
  itself broken — you cannot score alt text without knowing what the surrounding text already said.
  **For an education system this is a gift, not a problem: the surrounding lesson text is known, so
  context-aware description is available by construction.**
- **BLV scientists in practice** (arXiv:[2607.18514](https://arxiv.org/abs/2607.18514), `OBSERVED`,
  interviews with **10 scientists (5 with vision disabilities, 5 sighted)**, 115 logged queries):
  scientists reported **abandoning AI workflows** when they hit "vague or incomplete image descriptions,
  as well as incorrect AI outputs." **This is the cost of a wrong description stated as user behaviour:
  not a lower score, but abandonment of the tool.**
- **Alt4Blind** (arXiv:[2405.19111](https://arxiv.org/abs/2405.19111), `MEASURED-BENCH`
  `[fetched-summary]`): benchmark of **5,000 real chart images** with labelled descriptions —
  the closest thing to an evaluation substrate for this task.
- **University disability-services professionals writing HCI figure descriptions with generative AI**
  (arXiv:[2602.08937](https://arxiv.org/abs/2602.08937), `OBSERVED` `[fetched-summary]`): professionals
  "can struggle to write high-quality alt text if they lack subject expertise"; generative AI assistance
  improved both quality and speed. **The honest framing: AI alt text is a strong assistive draft for a
  human who lacks domain expertise, and is not yet an unsupervised producer of record.**

### 6.5 Accessibility checks are correctness checks

Every item in §6 is machine-checkable at generation time, and every one of them belongs in the same
gate as the geometry checks. There is no principled distinction between "this arrow points at nothing"
and "this series is distinguishable only by hue" — both are figures that fail to communicate to some
learner. Per H1 (curb-cut), the second one fails to communicate to roughly 8% of male learners and to
every learner viewing a greyscale printout.

---

## 7. Figure design for the H1 archetypes — and which principles are mechanically checkable

B1's meta-analytic effect sizes, re-read as a *specification* rather than as advice:

| Principle | Effect size (B1) | Checkable? | The check |
|---|---|---|---|
| **Spatial contiguity / split attention** | **g = 0.63 [0.55, 0.71]**, k = 58, n = 2,426 (Schroeder & Cenkci 2018, [10.1007/s10648-018-9435-9](https://doi.org/10.1007/s10648-018-9435-9)) — `MEASURED-META` | **Yes, fully** | assert `distance(label_bbox, referent_bbox) < τ`; assert no legend-only mapping for ≤ 6 series; assert no callout crosses another element |
| **Contiguity, overall** | **g = 0.74 [0.67, 0.82]**, k = 46 (Ginns 2006) — `MEASURED-META` | partly | as above, plus temporal alignment for interactive figures |
| **Signalling** | **g = 0.43 [0.35, 0.50]**, k = 209 (Schneider et al. 2018); **r = 0.17**, benefit concentrated in **low-prior-knowledge** learners (Richter, Scheiter & Eitel 2016, [10.1016/j.edurev.2015.12.003](https://doi.org/10.1016/j.edurev.2015.12.003)) — `MEASURED-META` | partly | assert exactly one salient emphasis channel per figure; assert emphasis targets the element named in the caption; **gate signalling on the learner model's prior-knowledge estimate (F5), because signalling is subject to expertise reversal** |
| **Coherence / seductive-detail removal** | **g = 0.33 [0.18, 0.48]**, k = 68; **persistent on-screen details g = 0.43**, transient details **g = 0.12 n.s.** (Sundararajan & Adesope 2020, [10.1007/s10648-020-09522-4](https://doi.org/10.1007/s10648-020-09522-4)) — `MEASURED-META` | weakly | assert element count ≤ budget; assert no decorative element lacks a referent in the caption; otherwise human review |

**Two consequences worth putting in the survey.**

**(1) The strongest multimedia principle is the most mechanically checkable one.** Spatial contiguity
(g = 0.63–0.74) reduces to a distance predicate on two bounding boxes. Coherence (g = 0.33) requires
judgement. So the automated gate should spend its budget on contiguity, and reserve human review for
coherence. That is a rare case where the evidence and the engineering point the same way.

**(2) The persistence moderator indicts static figures specifically.** Sundararajan & Adesope find
seductive details harm at **g = 0.43 when persistent** and **g = 0.12, n.s. when transient**. A static
diagram is maximally persistent — the decoration sits on the page for the entire study episode. **A
decorative element that would be harmless in a 2-second animation is harmful in a printed figure.**
Generation systems tuned for appeal (and RLHF'd toward it — A2 §5.3) are therefore optimising against
the coherence principle precisely in the medium where it bites hardest.

**Design rules for the C1 standard, derived:**

1. **One idea per figure.** Also the enabling condition for §5.5 round-tripping: one idea ⇒ a small,
   authorable atomic-question set.
2. **Labels adjacent to referents; legends are a last resort.** Directly checkable, largest effect size.
3. **Signal one thing, and only for novices.** Expertise reversal is measured; do not signal for
   high-prior-knowledge learners.
4. **Every element must be referenced.** An element with no referent in the caption or lesson text is
   either decoration (delete: coherence) or an unstated claim (label it: contiguity).
5. **Two channels for every distinction.** Colour + shape/dash/pattern/position. Accessibility *and*
   coherence agree here.
6. **Reduced extraneous detail, especially in static media**, per the persistence moderator.
7. **Alt text is authored from the spec, at generation time**, in the same pass — never reverse-engineered
   from the raster later (§6.4, MatplotAlt).

---

## 8. What is not known (state plainly; do not fill with plausible answers)

1. **`INFERENCE` — nobody has measured misconception acquisition from a wrong generated figure.** ~6% of
   post-repair charts are hallucinated (arXiv:[2506.06175](https://arxiv.org/abs/2506.06175)). Nobody has
   run: learner studies a legible-but-wrong generated figure → measure misconception formation and
   durability. **This is the highest-value missing experiment in C1 and it is cheap to run.**
2. **`OBSERVED — absence` — no benchmark measures learning from a generated figure.** Every metric in §2
   measures artifact existence, structural fidelity, or VLM answerability. The A2 finding ("no paper
   measures whether a human learns anything") holds identically for static figures.
3. **`OBSERVED — absence` — the informational-equivalence control is unrun for figures.** Generated
   figure vs. generated prose of equal information content, on transfer. Tversky's control, in the AI
   era.
4. **`OBSERVED — absence` — no measured base rate for Asymptote, Excalidraw scene JSON, or Observable as
   generation targets.**
5. **Unknown: the reliability of §5.2's checklist itself.** GeoSVG-RL's six dimensions are used as an RL
   reward, not validated as an evaluation instrument against human raters. DiagramIR is the only pipeline
   validated that way, and only for TikZ geometry.
6. **Unknown: whether generated alt text is *safe* unsupervised.** The STEM survey
   (arXiv:[2607.21611](https://arxiv.org/abs/2607.21611)) reports persistent factual inaccuracies and
   notes evaluation relies on text-overlap metrics that "poorly capture perceived usefulness and trust."
   There is no accuracy figure that would license unsupervised deployment to a BLV learner.

---

## 9. DELIVERABLE — the C1 figure-generation standard

### 9.1 Target selection: which target for which purpose

| Purpose | Target | Why | Forbidden alternative |
|---|---|---|---|
| Quantitative data / any chart | **Vega-Lite** (or a project IR compiling to it, per Flint) | engine owns scales, axes, legends, layout; spec is diffable | direct D3; raster |
| Structure, process, systems, taxonomy | **Mermaid** (small/lesson-embedded) or **Graphviz DOT** (larger graphs) | automatic layout ⇒ §3.1 and §3.2 impossible by construction | hand-placed SVG boxes |
| Software / systems modelling | **PlantUML** | conventions built in; 91.5% syntactic validity measured | prose description |
| Geometry, constructions, proofs | **GeoGebra construction** or **executable construction DSL** (GeoBuildBench class) | constraints are solved, not guessed; construction is interactive | TikZ coordinates typed by the model |
| Function plots, parameter exploration | **Desmos expression list** / **matplotlib with asserted axes** | tiny declarative state; curve independently recomputable (§5.2) | p5.js redrawing the curve by hand |
| Algorithm / data-structure trace | **Trace IR + deterministic renderer** (ALGOGEN VTA-JSON pattern) | 82.5%→99.8%; retargets to TikZ / Manim / Three.js | end-to-end code generation |
| Print-quality static math figure | **TikZ**, gated by a DiagramIR-style IR check | compiles; best-studied; 360k-example corpus | Asymptote (no measured base rate) |
| Conceptual/schematic scientific figure | **TikZ or SVG emitted by a renderer from a spec** | SciDraw-Bench: text fidelity is the hardest dimension for raster | any text-to-image model |
| Anything decorative with no claim | reconsider generating it at all | coherence, persistent-detail **g = 0.43** harm | — |

**Hard prohibitions:**
- **No raster text-to-image for any figure containing text, numbers, arrows, or a spatial claim.**
  (ScImage; SciDraw-Bench "text fidelity remains the hardest dimension for all systems.")
- **No model-computed layout coordinates in a shipped figure.** (§3.1, §4.3.)
- **No hand-written SVG paths as the generation target.** (SVGenius / VCode / VGBench / SGP-GenBench.)
- **No colour-only encoding.** (§6.1: 7.2% pass rate is the status quo being rejected.)

### 9.2 The pipeline (normative)

```
spec (concept + claims + atomic question set + prior-knowledge level)
  │
  ├─► [LLM]  emit DECLARATIVE IR only              ← the model's entire job
  │
  ├─► [schema/grammar validator]                    G1  — hard gate
  ├─► [deterministic renderer]                      G2  — hard gate
  ├─► [programmatic assertions §5.2]                G3  — hard gate (layout, axis, unit, a11y)
  │        incl. blank-image ablation on any VLM in the loop
  ├─► [IR diff vs. requested spec §5.3]             G4  — hard gate
  ├─► [round-trip atomic QA §5.5]                   G4' — hard gate at tier ≥ L3
  ├─► [alt text generated FROM THE IR §6.4]         — emitted, not inferred
  ├─► [VLM critique §5.4]                           advisory only; may propose repairs, may not gate
  └─► [human review §9.4]                           per tier
```

### 9.3 Which checks are mandatory at which grounding tier

Mapping onto the F3/G1 L0–L4 ladder. **`INFERENCE` — F3 was not written when C1 ran, so the tier
semantics below are C1's proposal for the figure axis and must be reconciled with F3/G1 before the
survey states them.**

| Tier | Meaning for a figure | Mandatory checks | Permitted use |
|---|---|---|---|
| **L0** — asserted | Raster or hand-coded output; no gate passed | none | **never shipped to a learner.** Scratch/ideation only |
| **L1** — well-formed | Parses / compiles | G1 parse + G2 render; alt text present | throwaway in-chat sketch, explicitly labelled provisional |
| **L2** — structurally sound | Renders and survives deterministic layout + accessibility assertions | L1 + **all of §5.2**: no label collision, canvas containment, arrow anchors attached, axis scale/limits/zero-baseline, unit present, contrast ≥ 4.5:1, second encoding channel, contiguity distance | **the floor for any figure shown to a learner** |
| **L3** — semantically verified | The figure's claims were checked against the spec, not just its geometry | L2 + IR diff vs. requested spec + round-trip atomic QA (CharTide-style, on identifiable quantities only) + independent recomputation of every plotted function/curve | course content, reusable lesson assets, anything persisted |
| **L4** — externally grounded + human-signed | Content verified against an external authority and a human expert signed it | L3 + CAS/simulation/dataset ground truth + **named human reviewer of record** | assessment items, credential-bearing material, safety-critical or clinical content, SELPA/IEP-adjacent material, anything a learner will be graded on |

**Tier rules:**
- **A figure below L2 may not be shown to a learner.** Not "should not" — the §3 failure rates make L1
  output a misconception generator.
- **Interactive figures are held to the same tier as static ones, evaluated over their parameter range**,
  not at default settings. A widget correct at `a=1` and wrong at `a=−1` is an L1 artifact.
- **Tier is a property of the artifact, displayed to the learner**, per the project's grounding-ladder
  convention. A learner should be able to see that a figure is L2 and not L4.
- **Regeneration resets the tier.** vTikZ's finding that models "struggle to reliably modify code in
  alignment with visual intent" (arXiv:[2505.04670](https://arxiv.org/abs/2505.04670), via A2) means an
  *edited* figure is a new figure and must re-clear every gate. **Edits are more dangerous than
  first drafts**, and this is the least-appreciated result in the area.

### 9.4 What must be human-reviewed (non-delegable)

1. **The first instance of every figure template.** Template-level review amortises; per-instance review
   does not scale. Once a template's IR→render path is human-verified, instances ride the automated gates.
2. **Every figure that asserts a causal or mechanistic relation** — i.e. every figure with a meaningful
   arrow. §3.2: an arrow *is* a claim, and anchor errors are measured.
3. **Every L4 artifact**, with a named reviewer of record.
4. **Every figure whose subject the system cannot check symbolically** (qualitative schematics,
   conceptual/metaphorical diagrams, anything with no ground-truth computation).
5. **Alt text for any figure delivered to a BLV learner**, until an accuracy figure exists that licenses
   otherwise (§8.6). Basis: STEM description survey reports persistent factual inaccuracies and
   hallucinations (arXiv:[2607.21611](https://arxiv.org/abs/2607.21611)); BLV scientists *abandon* tools
   after incorrect descriptions (arXiv:[2607.18514](https://arxiv.org/abs/2607.18514)); the
   disability-services study positions genAI as an aid to a human author, not a replacement
   (arXiv:[2602.08937](https://arxiv.org/abs/2602.08937)).
6. **Any figure a VLM critique flagged and an automated check cleared, or vice versa** — disagreement
   between gates is a human-review trigger, given the measured false-positive rate of VLM detectors
   (arXiv:[2603.22368](https://arxiv.org/abs/2603.22368)).

### 9.5 Cost discipline (feeds F4)

- Verification-in-the-loop costs **2.9–9.2× single-model inference, ~7× overall**
  (arXiv:[2607.01883](https://arxiv.org/abs/2607.01883) `[verbatim]`).
- The IR architecture pushes the other way: ALGOGEN's decoupling and Raiven's DSL report **up to 6×
  cheaper** than direct generation, and DiagramIR lets **GPT-4.1-Mini match GPT-5 at 10× lower cost**
  when the *evaluation* is IR-based rather than judge-based.
- **`INFERENCE`:** the combination — small IR from a small model, deterministic rendering, deterministic
  checks, and a large model reserved for repair only — is plausibly *cheaper* than single-pass frontier
  generation at equal quality. Nobody has published that end-to-end comparison; it is a concrete
  experiment for the reference implementation.

### 9.6 The one-paragraph version

> Emit a spec, not a picture. Let a renderer draw. Gate on parse, render, and a fixed list of
> deterministic layout, axis, unit, and accessibility assertions before any learner sees it. Verify
> semantics by diffing the spec and by asking the rendered figure a pre-authored set of atomic questions
> whose answers you already know — and only ask about quantities the figure could actually contain.
> Use a VLM to repair, never to approve, and prove your VLM is looking by checking that it scores worse
> on a blank canvas. Write the alt text from the spec in the same pass, not from the pixels afterwards.
> Put the labels next to the things they label, because that is the biggest measured effect and the
> easiest thing to check. Have a human sign the template once, and the artifact every time it will be
> graded.

---

## 10. Source index

**Retrieved verbatim via arXiv API (11):**
2506.03139 SVGenius · 2511.02778 VCode · 2407.10972 VGBench · 2412.02368 ScImage ·
2504.09764 Socratic Chart · 2605.12159 ALGOGEN · 2607.01883 PairCoder++ · 2511.08283 DiagramIR ·
2506.15903 VectorEdits · 2509.05208 SGP-GenBench · 2312.11556 StarVector

**Retrieved verbatim via arXiv API (chart-generation batch, 10):**
2406.09961 ChartMimic · 2410.04064 Text2Chart31 · 2405.07990 Plot2Code · 2402.11453 MatPlotAgent ·
2604.22192 CharTide · 2506.06175 "Does It Run and Is That Enough?" · 2607.04726 Observation-Aligned
supervision · 2606.31732 UniCoder · 2508.13587 MSRL · 2606.10334 Visual-SDPO

**Retrieved as fetched abstract summaries via WebFetch on `arxiv.org/abs/` (16):**
2607.21611 STEM image-description survey · 2605.25447 GeoSVG-RL · 2607.20775 Flint ·
2606.28406 SciDraw-Bench · 2604.03893 FeynmanBench · 2604.27969 Mirage/VeriGround ·
2607.18514 BLV scientists · 2602.09809 SciFlow-Bench · 2605.13167 GeoBuildBench ·
2605.11541 GeoR-Bench · 2205.10646 Context Matters · 2603.22368 misleading visualizations ·
2602.20137 viz rules · 2602.20084 viz principles · 2510.13914 A11yn · 2411.11916 DiagramAgent ·
2503.20089 MatplotAlt · 2311.02069 Grounded Intuition of GPT-Vision

**Identified via arXiv search listings, abstract not individually fetched — verify before quoting (17):**
2502.06147 LegalViz · 2605.24453 Code2UML · 2506.00788 UML behavioural augmentation ·
2603.09100 class models from requirements · 2511.14967 MermaidSeqBench · 2603.17067 ill-defined tasks ·
2607.18091 SciForma · 2605.11307 Vision2Code · 2602.10880 Chart Specification ·
2604.14941 Text2Arch · 2604.17206 SciDraw-6K · 2308.14247 Draco 2 · 2308.14241 "Too Many Cooks" ·
2408.06845 DracoGPT · 2405.21047 Grammar-Aligned Decoding · 2606.09395 structured-output control ·
2606.25605 constraint tax · 2607.20690 UI principle violations via RL · 2501.03572 ChatGPT a11y case
study · 2403.06693 Chart4Blind · 2509.13532 Py maidr · 2507.21462 tactile charts ·
2607.14588 conversational tactile interfaces · 2405.19111 Alt4Blind · 2602.08937 disability services
professionals · 2606.20676 MLLM-judge calibration · 2507.04952 ArtifactsBench

**Carried from A2 (already verified there):**
2604.10008 Raiven · 2505.04670 vTikZ · 2603.07936 Text-to-Automata · 2310.00367 AutomaTikZ ·
2405.15306 DeTikZify · 2607.18116 SGA · 2502.19400 TheoremExplainAgent · 2603.13251 ManiBench

**Learning-science (via B1, peer-reviewed meta-analyses):**
Schroeder & Cenkci (2018) 10.1007/s10648-018-9435-9 · Ginns (2006) · Schneider et al. (2018) ·
Richter, Scheiter & Eitel (2016) 10.1016/j.edurev.2015.12.003 ·
Sundararajan & Adesope (2020) 10.1007/s10648-020-09522-4

**GitHub API, observed 2026-07-27:**
`mermaid-js/mermaid` 89,429★ MIT · `plantuml/plantuml` 13,200★ LGPL-3.0 ·
`matplotlib/matplotlib` 23,034★ · `vega/vega-lite` 5,421★ BSD-3 · `d3/d3` 113,293★ ISC ·
`processing/p5.js` 23,823★ LGPL-2.1 · `excalidraw/excalidraw` 128,412★ MIT ·
`graphviz/graphviz` 4★ (GitHub mirror stub; development is off-GitHub)

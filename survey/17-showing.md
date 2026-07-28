---
title: "Showing — illustration, animation, and the arithmetic of a wrong picture"
section: showing
status: draft
date: 2026-07-28
source_report: research/raw/C1-illustration-generation.md, research/raw/A2-interactive-animation.md
---

# Showing

Two numbers from the same paper. An agentic repair loop took text-to-chart
generation from roughly **15% execution failure down to 4.5%**. Manual review of
the charts that survived found **6 of 100 contained hallucinations**, and only
**33.3%** (on one benchmark) and **7.2%** (on another) satisfied basic
colourblindness guidance. The paper is titled *"Does It Run and Is That
Enough?"*, which is the null result stated in the title.

Put those together and you get the fact that should govern every figure a
learning system ships:

> **The probability that a delivered figure is *wrong* now exceeds the
> probability that it fails to *exist*.**

A crash teaches nothing. A confident, beautiful, incorrect diagram teaches a
misconception the learner will then defend. This section is about the
engineering that closes that gap, and it is unusually good news, because the
architecture is settled and it is cheap.

---

## 1. Rank the target by how little drawing the model does

"Checkable" is not one property. It decomposes into four gates, and a generation
target's rank is how many of them you get for free.

| Gate | Question | Answered by |
|---|---|---|
| **G1 — parses** | Is the emitted string well-formed? | schema / grammar validator |
| **G2 — renders** | Does an artifact exist? | compiler / renderer |
| **G3 — layout is not the model's job** | Does an engine own positioning, so collision and overflow are *impossible* rather than *hopefully absent*? | layout engine |
| **G4 — semantics recoverable** | Can the figure's claims be read back and compared to the spec? | IR diff / round-trip / solver |

G3 is the gate the literature under-weights and the one that decides whether an
educational figure is usable. Every documented label collision, text overflow,
and arrow-pointing-at-nothing failure is a G3 failure, and every one occurs in a
target where the model was asked to compute coordinates.

| Tier | Targets | Gates |
|---|---|---|
| **A** — declarative spec + deterministic renderer | Vega-Lite; a project trace/spec IR; Desmos expression lists; GeoGebra constructions | G1–G4 |
| **B** — structural DSL with automatic layout | Graphviz DOT; Mermaid; PlantUML | G1–G3, partial G4 |
| **C** — compiled coordinate languages | TikZ/PGF; matplotlib; Asymptote | G1, G2; no G3 |
| **D** — hand-computed vector output | **model-written SVG**; direct D3; p5.js | G1 only |
| **E** — raster text-to-image | diffusion / native image models | none |

**The one-line rule: rank equals how much of the drawing the model is *not*
asked to do.** Every coordinate the model computes is a coordinate that can be
silently wrong, and no gate catches it.

**Why hand-written SVG is Tier D, specifically.** The benchmark literature is
unusually consistent and unusually negative. VGBench (4,279 understanding + 5,845
generation samples): models show "less desirable performance on low-level formats
(SVG)." SVGenius (2,377 queries, 24 domains, 22 models): "**all models exhibit
systematic performance degradation with increasing complexity, indicating
fundamental limitations in current approaches.**" VCode: "frontier VLMs struggle
to generate faithful SVGs." SGP-GenBench decomposes the failure into attribute
binding, spatial relations and numeracy — the same three axes that fail in
text-to-image. VectorEdits, on 270k+ edit pairs: "current methods struggle to
produce accurate and valid edits."

The distinction that resolves the paradox: **SVG is an excellent output format
and a bad generation target.** You want SVG on the page — it is text, it scales,
and it carries a DOM a screen reader can walk. You do not want a language model
computing its path coordinates. Emit Tier A or B; let a renderer produce the SVG.

*(A self-application: this project's own documentation dashboard shipped
hand-written SVG charts. By its own standard those are Tier D artifacts and are
being replaced.)*

Tier E is disqualified rather than discouraged for any figure containing text.
SciDraw-Bench, across 32 structured tasks over 8 figure types and 10 disciplines,
found domain-specific systems substantially beating general text-to-image models,
with "**text fidelity remains the hardest dimension for all systems.**" A raster
figure cannot be parsed, diffed, edited, or made screen-reader-navigable.

---

## 2. Nine groups, one architecture, one clean ablation

The single cleanest measurement in this literature comes from ALGOGEN, on a
200-task algorithm-visualisation benchmark. End-to-end LLM generation:
**82.5%** success. Decoupling algorithm simulation from rendering — the model
emits a JSON trace, a deterministic compiler draws it to Manim, TikZ, or
Three.js — **99.8%**.

The mechanism is stated causally, not as a vibe. End-to-end generation "requires
the system to simultaneously simulate algorithm flow and satisfy video rendering
constraints, such as element layout and color schemes. **This complex task
induces LLM hallucinations.**" The failure is **capacity contention**: the model
is holding the semantics of the concept and the geometry of the page in the same
forward pass.

At least nine independent groups, across chart code, algorithm animation,
technical illustration, geometry, and diagram evaluation, converged on the same
shape — Raiven (a DSL compiling to D3, 100% compilation, up to 6× cheaper),
Flint (a hierarchical data-semantic model compiling to Vega-Lite, ECharts, or
Chart.js), GeoSVG-RL (a layout plan as "geometric contract"), DiagramIR (parse
the TikZ back into an IR and compare IRs, not images), SciFlow-Bench (round-trip
inverse-parsing), Socratic Chart, GeoBuildBench, Chart Specification.

> **A generated educational figure must be produced by rendering a declarative
> specification that the model emitted and a machine validated. The model must
> not compute layout coordinates for any figure that ships to a learner.**

Splitting also buys re-targeting for free: one trace renders to Manim *or* TikZ
*or* Three.js; one spec renders to three chart libraries. For a system that must
serve a static PDF, a screen-reader page, and an interactive widget from the
same idea, that is not a convenience. It is the only affordable way to do it.

---

## 3. Animation: g = 0.23, and the moderator that survives

Now the pedagogy, and it does not flatter the medium.

Berney & Bétrancourt's meta-analysis — **61 studies, N = 7,036, 140 pairwise
comparisons** of animated versus static graphics — reports **Hedges's
g = 0.226, 95% CI [0.12, 0.33]**. Small. The authors of one of the three
meta-analyses in this area summarise the field in their own words:

> "The results of three meta-analyses show that the effectiveness of learning
> from animations, when compared to learning from static pictures, is **rather
> limited**."

That sentence is written by researchers sympathetic to animation, which makes it
more credible, not less. The subgroup moderators are larger — system-paced
animation g = 0.309, animation with auditory commentary g = 0.336, instruction
without accompanying text g = 0.883 — and the last one is exactly the kind of
subgroup-of-a-subgroup result a replication-minded reader should discount.
Report the 0.226; treat the moderators as hypotheses.

Behind the meta-analytic average sits the canonical negative result: a review
that found **no case in which animation outperformed an informationally
equivalent static graphic.** Apparent wins were confounded — the animated
condition usually contained *more information*, or added interactivity and
self-pacing. The finding is not "animation is bad." It is "**the
informational-equivalence control is almost never run, and when you run it,
motion adds nothing.**" In the AI-generated-video boom, that control is not run
at all.

**The moderator that does survive is directly actionable: animate what changes.**
A systematic review of 194 studies found the field assessing *conceptual* mental
models while neglecting *kinematic* ones, and the follow-up experiment argues
animation earns its keep specifically when the specifics of the displayed change
are the learning target. Kinematics, procedures, human movement, mechanism
dynamics: animate. Static structure, a relation, a proof step: a well-designed
static diagram is at least as good and far cheaper to verify.

And the result that should be printed on the wall of every generation-pipeline
team. Fourth and sixth graders learned the operation of a bicycle pump from
graphics presented simultaneously, successively, self-paced, or animated:

> "The presentation mode affected evaluation of **perceived comprehensibility,
> interestingness, enjoyment and motivation, but not comprehension test score.**"

Animation moves *liking* without moving *learning*. Set that beside the
randomised active-learning result where students in the active classroom
**learned more but felt they learned less**, and the dissociation runs in both
directions: subjective fluency is anti-correlated with effortful learning, and
animation is a fluency machine.

**Every LLM→video pipeline in this literature is scored by VLM judges or human
preference. Those metrics measure precisely the axis that dissociates from
comprehension.** A pipeline optimised on preference is optimising the illusion.

One more, and it belongs to the author of the multimedia principles himself:
across experiments on lightning formation, brakes, ocean waves, and toilet
tanks, **static, learner-paced, annotated illustrations equalled or beat
narrated animations on transfer.** The cheapest artifact was often the best one.

---

## 4. The field-wide pattern: resemblance, not effect

Line up the success rates this literature reports. TheoremExplainAgent: **93.8%
success rate** — alongside the authors' own note that "most of the videos
produced exhibit minor issues with visual element layout." A renderer-in-the-loop
system: 94% render success rate, 85.7% visual similarity. ALGOGEN: 99.8%. Raiven:
100% compilation.

**Every one of those is a measure of artifact existence or resemblance to a
reference artifact. None is a measure of effect on a mind.** The 93.8%-success /
most-videos-have-layout-defects pair is the field's own admission that its
success metric is measuring compilation, not legibility.

The two metrics that reach further are still proxies. DiagramIR compares
intermediate representations and reports higher agreement with human raters than
LLM-as-a-judge — genuinely better, and still a judgement about the figure.
TeachQuiz, the most inventive metric in the area, measures how well a
**vision-language model, after unlearning, can recover knowledge by watching the
generated video**. It is a machine analogue of a learning-gain measure, and it is
not evidence about humans.

> **No study in the LLM-generated-explanatory-video literature measures whether a
> human learns anything from the generated video.** The identical gap holds for
> static figure generation: every benchmark measures existence, structural
> fidelity, or VLM answerability.

Two consequences follow, and they are the reason this is a section rather than a
footnote. First, the highest-value missing experiment here is cheap: expose
learners to a legible-but-wrong generated figure and measure misconception
formation and durability. We know roughly 6% of post-repair charts are
hallucinated; we know from the conceptual-change literature that misconceptions
are sticky. **Nobody has multiplied those two facts together.** Second, the
informational-equivalence control — generated figure versus generated prose of
equal information content, on transfer — has never been run in the AI era.

---

## 5. What is checkable, and the happy coincidence

Re-read the multimedia meta-analyses as a *specification* rather than as advice.

| Principle | Effect | Checkable? | The check |
|---|---|---|---|
| **Spatial contiguity** | **g = 0.63 [0.55, 0.71]**, k = 58 | **Fully** | assert `distance(label_bbox, referent_bbox) < τ`; no legend-only mapping for ≤ 6 series |
| **Contiguity overall** | **g = 0.74 [0.67, 0.82]**, k = 46 | Mostly | as above, plus temporal alignment |
| **Signalling** | **g = 0.43**, k = 209; benefit concentrated in **low-prior-knowledge** learners | Partly | one salient emphasis channel; gate on the prior-knowledge estimate — signalling is subject to expertise reversal |
| **Coherence** | **g = 0.33**, k = 68; persistent details **g = 0.43**, transient **g = 0.12 n.s.** | Weakly | element budget; every element referenced in the caption; otherwise human review |

**The strongest multimedia principle is also the most mechanically checkable
one.** Spatial contiguity, the largest effect in the table, reduces to a distance
predicate on two bounding boxes. Coherence, the smallest, requires judgement.
Spend the automated gate's budget on contiguity and reserve humans for coherence.
Evidence and engineering rarely agree this cleanly.

The persistence moderator carries a specific indictment of static figures.
Seductive details harm at g = 0.43 when persistent and g = 0.12, not significant,
when transient. A static diagram is maximally persistent — the decoration sits on
the page for the whole study episode. **A decorative element that would be
harmless in a two-second animation is harmful in a printed figure**, and
generation systems tuned for appeal are optimising against coherence precisely
where it bites hardest.

---

## 6. Verification: symbolic detects, the model repairs, and prove the checker is looking

The tempting architecture is render-and-inspect: draw the figure, show it to a
vision-language model, ask if it is right. The evidence against relying on that
is specific and it is the second major null in this section.

- **Socratic Chart:** remove textual labels from charts and apply perturbations,
  and frontier models drop **up to 30%**. The checker is reading text, not
  geometry — blind exactly where geometric error lives.
- **The "Mirage" ablation:** in circuit-diagram→Verilog generation, replacing the
  diagram with a **blank image leaves Pass@k unchanged or even higher**, because
  models read identifier names in the module header instead of the picture.
- **Misleading-visualisation benchmark:** VLMs detect design errors more reliably
  than reasoning-based misinformation, and **"frequently misclassify
  non-misleading visualizations as deceptive"** — a false-positive rate that
  makes them unusable as a hard gate.
- **Visualisation-rules benchmark:** **F1 up to 0.82 on common violations, below
  0.15 on subtle perceptual rules**; the authors conclude LLMs "underperform
  compared to symbolic solvers." Translating a symbolic constraint system's rules
  into natural language boosted small models by up to 150%.
- **GeoBuildBench:** state-of-the-art multimodal models show "**limited ability to
  exploit visual and constraint-based feedback for self-correction**." That is a
  direct null on the self-repair loop the rest of the field assumes works.

But there is an asymmetry worth exploiting: models are **more effective at
correcting violations than at detecting them reliably.**

> **Rule: symbolic checks detect; the model repairs; the model never gates
> alone.** And run the blank-image ablation on your own checker. If the score
> does not drop, the checker is not looking. One line of code, highest-value
> diagnostic in the stack.

Round-tripping — generate, describe back, compare — works when it is made
concrete: ask a **fixed set of atomic questions whose answers were specified in
advance** and score answer accuracy. That converts a fuzzy similarity judgement
into pass/fail, and it composes with "one idea per figure," because one idea
means a small authorable question set. The hard limit is identifiability: **a
boxplot does not contain its samples and a histogram does not contain its
observations.** Asking a round-trip checker to recover non-identifiable
quantities "encourages hallucination and over-specified code generation."

---

## 7. Accessibility is a correctness gate, not a feature

Only **33.3%** and **7.2%** of generated charts satisfied basic colourblindness
guidance after the execution problem was solved. A 7.2% pass rate is not a long
tail; it is the modal output being inaccessible.

It is fixable and the fix is measured: optimising a code-generating model against
a severity-weighted WCAG reward produced a **60% reduction in inaccessibility
rate** while maintaining semantic accuracy and visual quality. Given that
contrast ratio, colour-difference under CVD simulation, and second-channel
encoding are all deterministic and free at inference time, **shipping a
colour-only figure is a choice, not a limitation.**

There is no principled distinction between "this arrow points at nothing" and
"this series is distinguishable only by hue." Both are figures that fail to
communicate to some learner. They belong in the same gate.

And one design rule with a measurement behind it: **generate alt text from the
specification, in the same pass, never from the pixels afterwards.** Alt-text
accuracy improved when the model was prompted with heuristic alt text or data
tables parsed from the figure source rather than shown the image. A 2026 PRISMA
survey of 20 studies on STEM image description reports persistent "factual
inaccuracies and hallucinations" plus "heavy reliance on automatic text-overlap
metrics that poorly capture perceived usefulness and trust." Interviews with
blind and low-vision scientists record the cost in behaviour rather than score:
they **abandoned AI workflows** after vague or incorrect descriptions. Until an
accuracy figure exists that licenses otherwise, alt text delivered to a BLV
learner is human-reviewed.

---

## 8. What this section commits us to

- **Emit a spec, not a picture.** No model-computed layout coordinates in any
  figure a learner sees. 82.5% → 99.8% is the ablation; nine groups is the
  consensus.
- **No hand-written SVG as a generation target, and no raster text-to-image for
  anything containing text, numbers, arrows, or a spatial claim.**
- **Gate deterministically before a learner sees it:** parse, render, then
  layout, axis, unit, contrast, and second-channel assertions. Independently
  recompute every plotted function — nothing else catches a wrong curve.
- **Animate only what changes.** g = 0.226 overall; the surviving moderator is
  kinematic and procedural content. Otherwise ship the static, learner-paced,
  annotated illustration that beat narrated animation in Mayer's own
  experiments.
- **Never optimise a generation pipeline on preference.** Animation raises
  perceived comprehensibility, interest, enjoyment and motivation and not
  comprehension. Active learning does the reverse.
- **Symbolic detects, the model repairs, and the blank-image ablation is
  mandatory** on any vision checker in the loop.
- **Report compile rate and correctness as two numbers**, always.
- **Alt text from the spec, at generation time.** Accessibility failures are
  correctness failures.

The through-line is the same one the rest of this survey keeps arriving at from
other directions. The generation literature has become very good at producing
something that *resembles* a good figure, and has not yet measured whether a
person understood anything. Resemblance to an artifact is not effect on a mind,
and only one of those is the job.

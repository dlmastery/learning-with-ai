---
title: "Generative animation, video, and interactive explanation at the July 2026 frontier"
wave: A
section: A2
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 19
supersedes: "research/raw/A2-interactive-animation.md (removed)"
---

# A2 — Generative Animation, Video, and Interactive Explanation

## Executive finding

By July 2026, an AI mentor can:

- generate synchronized video and audio from text, image, audio, and video;
- edit video conversationally across turns;
- preserve characters and scenes across revisions;
- generate controlled eight-second 4K clips with native audio;
- create exact programmatic STEM animations with render-feedback repair;
- synthesize interactive web courseware;
- turn a formal model into a manipulable simulation;
- inspect the learner’s own artifact and annotate it live.

The design question has changed from “does animation beat a static picture?” to:

> **Which medium lets this learner perform the next epistemic action with the
> least cost and the strongest truth guarantee?**

The mentor chooses among annotation, controlled animation, executable simulation,
generated situated video, and physical activity. Motion is not the intervention;
prediction, intervention, reconstruction, and transfer are.

This report replaces the previous A2 draft, which led with old static-versus-
animation averages and a negative content-medium frame. Those passages were
removed from the active repository.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-BENCH` | Benchmark, render evaluation, or human/expert rating |
| `OBSERVED` | Inspectable API, artifact, code, or system |
| `VENDOR` | Provider-reported model capability |
| `INFERENCE` | Design conclusion |

## 1. The July 2026 media frontier

### 1.1 Multimodal generation and conversational editing

Google’s current [video-generation guide](https://ai.google.dev/gemini-api/docs/video)
names Gemini Omni Flash as its default: text, images, audio, and video can be
combined as inputs; the model supports conversational editing, character
consistency, factual grounding, and high-coherence video. Veo 3.1 remains the
route for first/last-frame control, scene extension, and legacy production
workflows. `VENDOR`

[Gemini Omni Flash](https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/)
became available to developers on 30 June 2026 at a reported $0.10 per generated
second. `VENDOR`

[Veo 3.1](https://ai.google.dev/gemini-api/docs/veo) produces eight-second clips
at 720p, 1080p, or 4K with native audio and supports image-based direction and
frame control. `VENDOR`

The [Gemini changelog](https://ai.google.dev/gemini-api/docs/changelog) records
the shutdown of Veo 2 and 3.0 endpoints on 30 June 2026. `OBSERVED` This rapid
turnover is an architecture requirement: use a media abstraction and preserve
semantic shot specifications rather than model-specific prompts.

[Sora 2](https://openai.com/index/sora-2/) launched in September 2025 as a video
and audio generation model and is available through an
[API production surface](https://openai.com/solutions/use-case/content-creation/)
with length, aspect-ratio, resolution, and remix controls. `VENDOR`

The implication for learning is not longer generated lectures. It is a new,
specific visual example on demand:

- show one molecular collision from the learner’s chosen frame;
- animate the exact code trace where their mental model diverged;
- reconstruct a historical street from local photographs and sources;
- compare two camera perspectives of a mechanical procedure;
- turn a child’s drawing into a short motion prediction, then test it.

### 1.2 Programmatic animation is the exactness layer

[OmniManim](https://arxiv.org/html/2605.15585v1) frames animation generation as
render-feedback-aware constrained code generation. A shared scene state, explicit
visual plan, post-render diagnostics, and localized repair make errors
addressable rather than forcing full regeneration. `MEASURED-BENCH`

[Pedagogy-Aware AI Generation of STEM Animations](https://arxiv.org/html/2604.05266)
uses programmatic animation and pedagogical planning for STEM. `MEASURED-BENCH`

[LASEV](https://arxiv.org/html/2602.11790v2) decomposes instructional-video
generation into a hierarchical multi-agent pipeline to preserve logical and
knowledge structure. `MEASURED-BENCH`

[Training and Agentic Inference Strategies for LLM-based
Animation](https://arxiv.org/html/2604.18364v1) reports that programmatic
animations can serve as reliable mediators for educational video generation.
`MEASURED-BENCH`

For an exact claim, the animation source should be:

```text
concept contract
  → state machine / equations / data
  → scene graph and timeline
  → rendered frames
  → automated checks
```

Not:

```text
plausible prose prompt → opaque video → trust the pixels
```

### 1.3 Interactive courseware can be generated as software

[MAIC-UI](https://arxiv.org/html/2604.25806) investigates generative UI for
interactive courseware. `MEASURED-BENCH`

[AnimatedLLM](https://arxiv.org/html/2601.04213v2) runs in the browser and uses
precomputed traces of open models to show transformer operations step by step.
`OBSERVED`

This points to the preferred medium for causal learning: not a video of a model
running, but a stateful object the learner can pause, change, and interrogate.

## 2. The modality decision map

### Route 1 — Annotate the learner’s artifact

Use when one mark resolves attention or relationship:

- circle the mistaken sign;
- trace data flow;
- align two lines;
- label a joint;
- overlay a force vector.

This is fastest, cheapest, and most personal. It also preserves authorship.

### Route 2 — Controlled step animation

Use when order, transformation, or hidden state is the concept:

- algorithm trace;
- mitosis;
- derivation;
- grammar transformation;
- mechanism assembly.

Required controls:

- pause;
- scrub;
- step forward/back;
- change speed;
- hide/reveal layers;
- predict before the next state;
- compare two traces.

### Route 3 — Executable simulation

Use when the learner must change a variable and observe consequences:

- force and motion;
- population dynamics;
- circuit behavior;
- probability;
- chemical equilibrium;
- resource allocation.

The state transition comes from code, equations, data, or a validated simulator.
The learner’s interventions and predictions become assessment evidence.

### Route 4 — Generated situated video

Use when scene, viewpoint, culture, affect, or visual analogy is essential:

- show a procedure in the learner’s environment;
- generate multiple perspectives;
- dramatize a historical choice;
- make an invisible scale imaginable;
- demonstrate a conversation or social scenario.

The video carries a shot contract:

```yaml
claim: ...
required_events: [...]
forbidden_implications: [...]
continuity_constraints: [...]
spoken_claims_and_sources: [...]
camera_purpose: ...
learner_pause_points: [...]
```

### Route 5 — Physical or human activity

Use when the learning target is embodied, social, tacit, safety-critical, or
available through local materials:

- build;
- measure;
- role-play;
- interview;
- observe;
- repair;
- practice with an expert.

The AI supplies preparation, checklist, just-in-time support, reflection, and
handoff. It does not replace the world.

## 3. Generate the action, not only the media

Every asset includes:

1. a pre-view prediction;
2. learner-controlled pacing;
3. one intervention or reconstruction;
4. a contrast or counterfactual;
5. a transfer task;
6. a nonvisual equivalent;
7. a low-bandwidth derivative;
8. evidence returned to the learner-owned state.

Example:

```text
Before: “Which part of this sorting algorithm will move next?”
During: learner advances one state and drags the selected element
After: learner reconstructs the invariant and predicts a new input
Transfer: diagnose a different algorithm with the same invariant
```

If the learner only watches, the mentor has not finished authoring.

## 4. Verification by medium

| Medium | Authority | Checks |
|---|---|---|
| Annotation | original artifact + concept contract | target, alignment, label |
| Programmatic animation | state machine/equations/code | state order, values, geometry, labels |
| Simulation | executable model | invariants, units, boundaries, reproducibility |
| Generated video | shot contract + source claims | event coverage, continuity, narration, prohibited implications |
| Physical activity | procedure + human/sensor evidence | safety, materials, observation, reflection |

[EduAIGV‑1k](https://arxiv.org/html/2603.03066v1) contains 1,130 videos from ten
text-to-video models against 113 expert-curated early-math prompts. It evaluates
educational video quality rather than generic aesthetics. `MEASURED-BENCH`

[DataReel](https://arxiv.org/abs/2604.25220) provides 328 data-driven video
stories pairing structured data, charts, and narration and proposes planning,
generation, and verification stages. `MEASURED-BENCH`

The reusable rule is to verify the semantic layer and the render separately.

## 5. Universal-access media

### Delivery ladder

```text
text description
  → still keyframes
  → low-frame-rate vector animation
  → interactive code cached locally
  → compressed generated video
  → frontier multimodal regeneration
```

The learning action survives every tier.

### Localization

- Keep labels and narration as separate tracks.
- Generate culturally situated examples from a fixed concept contract.
- Re-render translated layouts.
- Preserve source terms where translation would erase a distinction.
- Invite local teachers to publish approved scene packs.

### Accessibility

- Description exposes state changes, not only appearance.
- Keyboard and switch controls cover pause, step, reset, and parameter change.
- Motion can be disabled.
- Color is redundant.
- Narration, captions, transcript, sign, tactile build, and static sequence are
  generated from the same semantic timeline.

## 6. Cost routing

At July 2026 provider pricing, continuous bespoke 4K video is not the universal
default. The mentor routes:

1. annotation and vector/code locally;
2. cached programmatic animation on a community server;
3. compressed generic clips regionally;
4. expensive generated video only for high-value scene-specific needs;
5. share and reuse verified assets across learners.

Once generated, a source-grounded animation becomes an open learning object,
localizable at low marginal cost.

## 7. Acceptance tests

- [ ] The medium is chosen from the learner action and truth requirement.
- [ ] The concept and shot/state contracts are versioned.
- [ ] Exact relationships derive from inspectable structure.
- [ ] The learner predicts before motion reveals the answer.
- [ ] The learner controls pacing and can intervene.
- [ ] A reconstruction or transfer task follows.
- [ ] Narration and labels are source-grounded.
- [ ] Render continuity, clipping, overlap, units, and state order pass.
- [ ] A nonvisual and reduced-motion equivalent exists.
- [ ] A low-bandwidth/offline tier preserves the action.
- [ ] The artifact returns evidence to learner-owned state.
- [ ] Model/API turnover does not destroy the semantic source.

## Source index

1. Gemini video generation — [current guide](https://ai.google.dev/gemini-api/docs/video)
2. Gemini Omni Flash — [June 2026 launch](https://deepmind.google/blog/start-building-with-nano-banana-2-lite-and-gemini-omni-flash/)
3. Gemini Omni — [model introduction](https://deepmind.google/blog/introducing-gemini-omni/)
4. Veo 3.1 — [API guide](https://ai.google.dev/gemini-api/docs/veo)
5. Veo — [model page](https://deepmind.google/models/veo/)
6. Gemini API changelog — [deprecations](https://ai.google.dev/gemini-api/docs/changelog)
7. Gemini API pricing — [video](https://ai.google.dev/gemini-api/docs/pricing)
8. Sora 2 — [OpenAI](https://openai.com/index/sora-2/)
9. Sora 2 API — [OpenAI](https://openai.com/solutions/use-case/content-creation/)
10. OmniManim — [arXiv:2605.15585](https://arxiv.org/html/2605.15585v1)
11. Pedagogy-aware STEM animation — [arXiv:2604.05266](https://arxiv.org/html/2604.05266)
12. LASEV — [arXiv:2602.11790](https://arxiv.org/html/2602.11790v2)
13. Agentic animation generation — [arXiv:2604.18364](https://arxiv.org/html/2604.18364v1)
14. AnimatedLLM — [arXiv:2601.04213](https://arxiv.org/html/2601.04213v2)
15. MAIC-UI — [arXiv:2604.25806](https://arxiv.org/html/2604.25806)
16. EduAIGV‑1k — [arXiv:2603.03066](https://arxiv.org/html/2603.03066v1)
17. DataReel — [arXiv:2604.25220](https://arxiv.org/abs/2604.25220)
18. Manim — [community source](https://github.com/ManimCommunity/manim)
19. PhET — [research and design](https://phet.colorado.edu/en/research)

## Decision

**Treat generated motion as a routed, verifiable teaching tool.** Annotate first,
animate state when sequence matters, simulate when intervention matters, generate
video when situation and viewpoint matter, and send the learner into the physical
world when reality is the medium. Always generate the learner action with the
asset.

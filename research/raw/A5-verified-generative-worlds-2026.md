---
title: "Verified generative worlds as learning substrates at the July 2026 frontier"
wave: A
section: A5
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 21
supersedes: "research/raw/A5-world-models.md (removed)"
---

# A5 — Verified Generative Worlds as Learning Substrates

## Executive finding

Generated worlds crossed from research clips to usable creation surfaces in
2025–26:

- Project Genie lets people create, explore, remix, and ground interactive
  worlds in Street View imagery;
- Marble exposes explorable 3D-world generation from text, images, video,
  panoramas, and layouts through a public API;
- Agora‑1 enables multiple humans or agents to share and change one generated
  world in real time;
- Oasis 3 exposes an interactive world model through an API;
- SIMA 2 reasons, converses, acts, and learns across virtual worlds, including
  generated Genie environments;
- research systems now sustain learned visual interaction for more than ten
  minutes at 15 FPS and transfer generated experience into real robot policies.

The educational primitive is ready:

> **Use a generated world to create presence, possibility, perspective, and
> practice. Bind exact claims to executable models, grounded sources, and real
> observations.**

This avoids a false choice between exuberant exploration and scientific rigor.
The world model does not need to be the physics engine. It can be the adaptive
experience layer around a verified simulation.

This report replaces the prior A5 draft, which organized the field mainly around
warnings and capability gaps. Current limits are represented here only where they
change the verification stack or permitted use.

## Evidence labels

| Label | Meaning |
|---|---|
| `MEASURED-BENCH` | Quantitative world, agent, or real-world transfer evaluation |
| `OBSERVED` | Public product, API, code, or inspectable artifact |
| `VENDOR` | Provider-reported capability |
| `INFERENCE` | Educational design conclusion |

## 1. The July 2026 world frontier

### 1.1 Genie becomes a product surface

[Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
generates real-time interactive environments from text and images. Google reports
720p, 24 FPS, minutes of continuous interaction, and promptable world events.
`VENDOR`

On 29 January 2026,
[Project Genie](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/)
opened world creation, exploration, and remixing to U.S. adult AI Ultra
subscribers. `OBSERVED`

On 19 May 2026, Google added
[Street View grounding](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/),
using real-world starting imagery and expanding access. `OBSERVED`

For education, these three actions map directly:

- **create:** compile a learning environment around one concept or story;
- **explore:** let the learner choose path and perspective;
- **remix:** change a condition and compare consequences.

### 1.2 Explorable 3D worlds become API objects

[Marble](https://www.worldlabs.ai/blog/marble-world-model) creates persistent 3D
worlds from text, images, video, panoramas, or coarse layouts, supports editing,
expansion, and combination, and exports splats, meshes, or video. `VENDOR`

The January 2026
[World API](https://www.worldlabs.ai/blog/announcing-the-world-api) turns those
worlds into developer objects renderable on the web or exportable into downstream
simulations. `OBSERVED`

World Labs’ open-source [Spark renderer](https://github.com/worldlabsai/spark)
renders Gaussian splats in Three.js across desktop, laptop, mobile, and VR
targets. `OBSERVED`

This separation—generated spatial scene plus downstream engine—is precisely what
education needs.

### 1.3 Generated worlds become shared

[Agora‑1](https://odyssey.ml/introducing-agora-1), released in May 2026, enables
multiple humans or AI agents to share and act in the same real-time generated
world. `VENDOR`

[Oasis 3](https://decart.ai/oasis) is available as an interactive-world API and
explicitly describes itself as a world-generation model, not a physics engine.
`VENDOR`

The educational consequence is larger than solo simulation:

- two learners solve from different roles;
- a learner and expert enter the same procedure;
- specialist agents play patient, customer, historical actor, critic, or
  teammate;
- a class negotiates a shared resource system;
- different hypotheses unfold in parallel worlds.

### 1.4 Agents can learn inside generated worlds

[SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
uses a Gemini core to reason about high-level goals, converse, describe plans,
execute actions, and improve through self-directed play. DeepMind reports using
SIMA 2 in previously unseen Genie 3 environments. `VENDOR`

A 2026
[Interactive World Simulator](https://arxiv.org/abs/2603.08546) reports stable
interactions beyond ten minutes at 15 FPS on one RTX 4090. Policies trained using
world-model-generated interaction data performed comparably to those trained on
the same quantity of real data across the studied rigid, deformable, and piled
object tasks; simulated and real policy performance correlated strongly.
`MEASURED-BENCH`

This is a crucial positive result: learned visual worlds can already provide
useful practice data when anchored to a real evaluation loop.

## 2. The verified-world stack

### Layer 1 — Experience

The generated world supplies:

- spatial presence;
- visual continuity;
- local and historical context;
- characters and role-play;
- rapid alternative scenarios;
- perspective change;
- shared exploration;
- emotionally memorable setting.

Truth-mode badge: **GENERATED EXPERIENCE**.

### Layer 2 — Executable law

Exact dynamics come from:

- equations;
- game/simulation engine;
- constraint solver;
- state machine;
- geographic model;
- economic or ecological model;
- verified code;
- teacher-authored rule set.

Truth-mode badge: **MODELLED — assumptions available**.

The generated renderer receives state from this layer. It does not invent the
state transition.

### Layer 3 — Grounded source and data

Claims bind to:

- primary historical records;
- maps and Street View;
- measured datasets;
- scientific references;
- local expert testimony;
- sensor records;
- provenance and uncertainty.

Truth-mode badge: **GROUNDED — source available**.

### Layer 4 — Reality

The learner:

- builds;
- measures;
- visits;
- observes;
- interviews;
- practices with a person;
- compares predicted and real outcomes.

Truth-mode badge: **OBSERVED — context recorded**.

The stack makes all four modes visible. Generated scenery is not disguised as
measurement, and simulation is not described as reality without conditions.

## 3. Learning patterns now unlocked

### 3.1 Counterfactual laboratory

The learner changes one assumption, explores both worlds, and identifies which
observations distinguish them.

Examples:

- high/low gravity around an engine-driven projectile model;
- different epidemic policies around a transparent compartment model;
- two city layouts around a mobility dataset;
- alternate historical constraints around cited primary records.

The world creates intuition. The model creates consequences. The sources create
the boundary between history and speculation.

### 3.2 Perspective exchange

One event is entered from multiple positions:

- engineer, resident, regulator, and ecosystem;
- patient, nurse, family, and clinic;
- buyer, seller, transporter, and producer;
- historical actors with different information.

The mentor asks the learner to reconstruct what each actor can know, then compare
against the record.

### 3.3 Procedure rehearsal

The learner practices sequence, decision points, communication, and recovery:

- laboratory protocol;
- equipment maintenance;
- emergency response;
- clinical interview;
- public speaking;
- conflict mediation.

The world supplies context; a verified checklist and human authority govern
safety-critical steps.

### 3.4 Agent society

The [expert mentor mesh](../../survey/03-expert-mentor-mesh.md) can inhabit the
same world:

- domain agent checks correctness;
- simulation agent controls dynamics;
- role agent presents a perspective;
- assessment agent watches decisions;
- accessibility agent changes navigation and representation;
- human teacher can enter or review the trace.

### 3.5 Learner-built worlds

Creation is more powerful than tourism. The learner:

1. writes the world contract;
2. chooses laws and assumptions;
3. generates a scene;
4. predicts behavior;
5. instruments the environment;
6. runs a peer or agent through it;
7. compares the trace with the model and reality;
8. revises.

The world becomes an executable argument.

## 4. Benchmarks and the acceptance boundary

[iWorld‑Bench](https://arxiv.org/abs/2605.03941) evaluates interactive world
models across visual generation, trajectory following, and memory.
`MEASURED-BENCH`

A June 2026
[interactive-world-model survey](https://arxiv.org/abs/2606.01164) organizes
frontiers, challenges, benchmarks, and research directions. `MEASURED-BENCH`

These evaluations support a layered release policy:

| Use | Required authority |
|---|---|
| imagination, narrative, perspective | world contract + source labels |
| navigation and spatial planning | scene geometry + task checks |
| conceptual simulation | executable law layer |
| quantitative prediction | validated simulator + units + bounds |
| safety-critical rehearsal | certified procedure + human supervision |
| claim about real world | measurement/source + uncertainty |

The model’s capability does not set the educational boundary alone; the source of
authority does.

## 5. Universal access

### Delivery ladder

```text
verbal scenario
  → illustrated map
  → pre-rendered path
  → lightweight web 3D
  → community-server simulation
  → streamed generative world
  → immersive display
```

The hypothesis, decision, and evidence loop survives every tier.

### Local world kits

A community can contribute:

- photographs and panoramas;
- oral histories;
- maps;
- common tools and materials;
- locally verified procedures;
- language, signage, and narration;
- accessibility landmarks.

The system builds from local authority instead of treating every environment as
generic.

### Shared infrastructure

One community workstation can generate and cache a world. Phones receive
pre-rendered paths or lightweight scene geometry. Printed maps and role cards
preserve multi-perspective decision tasks without a GPU.

## 6. Acceptance tests

- [ ] The world states whether it is imagined, modelled, grounded, or observed.
- [ ] Exact dynamics come from an executable, versioned law layer.
- [ ] Historical/scientific claims link to sources and uncertainty.
- [ ] The learner predicts or decides before seeing consequences.
- [ ] Alternative worlds vary named assumptions.
- [ ] The learner can inspect assumptions and state.
- [ ] Quantitative tasks validate units, boundaries, and invariants.
- [ ] Safety-critical tasks use certified procedures and human authority.
- [ ] Real observation calibrates the world where practical.
- [ ] A nonimmersive and low-bandwidth equivalent preserves the decision task.
- [ ] Local contributors control local data and representation.
- [ ] Traces return evidence to learner-owned state.

## Source index

1. Genie 3 — [Google DeepMind](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/)
2. Project Genie — [Google, January 2026](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/)
3. Street View grounding — [Google, May 2026](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/)
4. Genie 1 — [arXiv:2402.15391](https://arxiv.org/abs/2402.15391)
5. Genie 2 — [Google DeepMind](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)
6. SIMA 2 — [Google DeepMind](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/)
7. Marble — [World Labs](https://www.worldlabs.ai/blog/marble-world-model)
8. World API — [World Labs](https://www.worldlabs.ai/blog/announcing-the-world-api)
9. Spark — [open renderer](https://github.com/worldlabsai/spark)
10. Agora‑1 — [Odyssey](https://odyssey.ml/introducing-agora-1)
11. Oasis 3 — [Decart](https://decart.ai/oasis)
12. iWorld‑Bench — [arXiv:2605.03941](https://arxiv.org/abs/2605.03941)
13. Interactive-world survey — [arXiv:2606.01164](https://arxiv.org/abs/2606.01164)
14. Interactive World Simulator — [arXiv:2603.08546](https://arxiv.org/abs/2603.08546)
15. Interactive World Simulator project — [demo and results](https://www.yixuanwang.me/interactive_world_sim/)
16. OASIS robot simulation — [arXiv:2606.08548](https://arxiv.org/abs/2606.08548)
17. World-model benchmark collection — [GitHub](https://github.com/liujiuming123/Awesome-Interactive-World-Model)
18. MuJoCo — [open physics engine](https://github.com/google-deepmind/mujoco)
19. OpenUSD — [scene standard](https://openusd.org/release/index.html)
20. glTF — [Khronos specification](https://www.khronos.org/gltf/)
21. PhET — [simulation research and design](https://phet.colorado.edu/en/research)

## Decision

**Build generated worlds as an experience layer around verifiable laws, sources,
and reality.** Invite every learner to explore and create worlds now. Make the
truth mode visible, require an intervention, and compare the generated experience
with an executable model and the world outside the screen.

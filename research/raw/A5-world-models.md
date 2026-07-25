---
title: "World Models and Generative Interactive Environments as Learning Substrates"
wave: A
section: A5
date_researched: 2026-07-25
sources_count: 47
---

# A5 — World Models and Generative Interactive Environments as Learning Substrates

## Evidence strength key

Every claim below is tagged.

| Tag | Meaning |
|---|---|
| **[A]** | Peer-reviewed / arXiv technical paper with quantitative results, independently checkable |
| **[B]** | Official vendor documentation or model card with *specific numbers* — self-reported, not independently audited |
| **[C]** | Vendor marketing page or curated demo video — no numbers, no independent verification. Treat as a claim about a best case, not a capability |
| **[D]** | Could not verify from any primary source; stated here as unconfirmed |

Two structural warnings apply to this whole section:

1. **Almost every world-model capability claim in 2025–2026 is [B] or [C].** Genie 3, Odyssey-2, Oasis 3 and Project Genie have no technical papers. What we know comes from blog posts and hand-picked demo reels. No one outside the labs has published a reproducible measurement of Genie 3's consistency horizon.
2. **The evaluation literature and the capability claims point in opposite directions.** Vendors describe "world simulators"; every benchmark that has actually measured physical correctness finds it poor (§5). This gap is the single most important fact in this section for anyone thinking about education.

---

## 1. Google DeepMind Genie (1 → 2 → 3)

### Genie 1 (Feb 2024)

- Paper: **"Genie: Generative Interactive Environments"**, Bruce, Dennis, Edwards, Parker-Holder, Shi, Hughes, Lai, Mavalankar, Steigerwald, Apps, Aytar, Bechtle, Behbahani, Chan, Heess, Gonzalez, Osindero, Ozair, Reed, Zhang, Zolna, Clune, de Freitas, Singh, Rocktäschel. arXiv:2402.15391, submitted 2024-02-23. https://arxiv.org/abs/2402.15391 **[A]**
- **11B parameters.** Trained unsupervised on internet video. Can be "prompted to generate an endless variety of action-controllable virtual worlds described through text, synthetic images, photographs, and even sketches." **[A]**
- The architecturally interesting move: a **learned latent action space** inferred without action labels. This is what makes it possible to train a controllable environment from passive video — no instrumented gameplay logs required. **[A]**
- Genie 1 was 2D platformer-grade, low resolution, not real-time. It was a research result, never a product.

### Genie 2 (Dec 2024)

Blog: https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ **[B/C]** — no arXiv paper exists.

- Input: **a single prompt image** (can come from Imagen 3, or a real photograph). **[B]**
- Consistency: "can generate consistent worlds for **up to a minute**, with the **majority of examples shown lasting 10–20s**." **[B]** — note the honest hedge in DeepMind's own wording. The headline number and the typical number differ by 3–6×.
- Modelled phenomena claimed: water effects, gravity, object interaction (bursting balloons, opening doors, shooting barrels), point/directional lighting, reflections, bloom, character animation, other agents. **[C]** — demonstrated in curated clips only.
- A **distilled real-time version** exists with an explicitly acknowledged "reduction in quality of the outputs." **[B]** This is the recurring trade in this field: real-time *or* good, not both.

### Genie 3 (Aug 2025)

Blog: https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/ **[B]**
Model page: https://deepmind.google/models/genie/ **[B]**

Verified numbers from DeepMind's own pages:

| Property | Claim | Source |
|---|---|---|
| Resolution | **720p** | both pages **[B]** |
| Frame rate | **24 fps** (blog) / **"20–24 fps"** (model page) | **[B]** |
| Interaction horizon | "a **few minutes** of continuous interaction, rather than extended hours" | **[B]** |
| Visual memory | "extending as far back as **one minute** ago"; "memory recalling changes from specific interactions for **up to a minute**" | **[B]** |
| Consistency | environments "remain largely consistent for **several minutes**" | **[B]** |
| Prompt | text description (not just image, unlike Genie 2) | **[B]** |
| Promptable world events | text mid-session to "alter weather conditions or introduce new objects and characters" | **[B]** |
| Grounding | "grounded in Street View data from Google Maps" | **[B]** |

DeepMind's own stated limitations — these matter more than the capabilities for our purposes: **[B]**

- **"Limited range of actions agents can carry out."**
- Cannot accurately model **"complex interactions between multiple independent agents."**
- **"Currently unable to simulate real-world locations with perfect geographic accuracy."**
- **"Clear and legible text is often only generated when it's in the input world description."** — this is a hard blocker for most instructional content, which is labelled.

**No technical report exists for Genie 2 or Genie 3.** As of 2026-07-25 there is no arXiv paper, no model card with training details, no reproducible eval. Genie 3 remains the newest world model on DeepMind's model index (https://deepmind.google/models/ — Genie 3 listed under world models; no successor). **[B]**

### Project Genie — actual availability (Jul 2026)

https://labs.google/projectgenie **[B]**

- "Project Genie is available to **Google AI Ultra subscribers in the US (18+)**."
- Capabilities described: prompt-based world creation from text or images, environmental editing, first-person exploration with "walking to riding, flying to driving," and environmental memory shown via footprints and paint trails.
- **Not disclosed anywhere on the page**: session time limits, output resolution, world persistence, whether worlds can be saved or shared, whether there is an API. There is no API. **[B]**

**Practical verdict:** Genie 3 is real, is genuinely a step change (real-time interactive is qualitatively different from clip generation), and is **effectively inaccessible** — one country, one paid consumer tier, no API, no export, no persistence guarantee. You cannot build an educational product on it today.

### SIMA 2 — agents inside generated worlds

https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/ **[B/C]**

- Gemini-powered agent that "can think about its goals, converse with users, and improve itself over time."
- **Runs inside Genie-generated worlds.** In newly generated environments SIMA 2 "was able to sensibly orient itself, understand user instructions, and take meaningful actions toward goals, despite never having seen such environments before." **[C]** — no numbers given for the Genie-world condition specifically.
- Quantitative claims are relative to SIMA 1 on games (ASKA, MineDojo), "closing a significant portion of the gap to human performance." **[C]** — no absolute numbers in the blog.
- Availability: **"a limited research preview" with "early access to a small cohort of academics and game developers."** **[B]**

This pairing (generated world + agent that can act and *talk* in it) is the architecture that would matter for tutoring — a co-inhabitant that can explain what's happening. It is not available.

---

## 2. Kimi K3 — what is actually documented

This required careful separation of a real release from a misleading framing.

### What is confirmed

- **Kimi K3 exists.** Released **2026-07-16** by Moonshot AI. Listed on https://www.moonshot.ai/ as the flagship model. **[B]**
- Release blog: **https://www.kimi.com/blog/kimi-k3** **[B]**
- Specs from the blog: **2.8 trillion parameters** ("world's first open 3T-class model"), MoE with **16 of 896 experts** activated, built on **Kimi Delta Attention (KDA)** and **Attention Residuals (AttnRes)**, **1M-token native context**, native vision, quantization-aware training from the SFT stage (MXFP4 weights / MXFP8 activations). **[B]**
- API pricing: **$0.30/MTok cache-hit input, $3.00/MTok cache-miss input, $15.00/MTok output.** Model ID `kimi-k3`. **[B]** (https://platform.kimi.ai/docs/introduction — "Kimi's flagship model, built for long-horizon coding and end-to-end knowledge work, with native visual understanding," up to 1M tokens.)
- **Full weights announced for release 2026-07-27** (two days after this research date). **[B]**
- Corroborating third-party evidence of a real, widely-adopted release: 5,808 GitHub issues mentioning "kimi-k3" as of 2026-07-25, including model-support requests filed against microsoft/vscode (#326684), ollama/ollama (#17235), and kirodotdev/Kiro (#10278). **[A]** (via `gh api search/issues`)

### What is NOT confirmed — the "interactive worlds" claim

**The claim that Kimi K3 creates interactive worlds in the world-model sense is not supported by any Moonshot source.** Specifically:

- The K3 release blog **never uses the words "world model," "simulation," "physics," or "environment."** (Verified by targeted re-read of the blog.) **[A — direct negative observation on the primary source]**
- What the blog *does* say, verbatim: **"Kimi K3 combines strong 3D reasoning, coding, and vision capabilities to turn concepts, images, and videos into fully playable interactive experiences."** **[B]**
- And: K3 achieves **"true 'vision in the loop'"** by "seamlessly iterating between code and live screenshots — instantly seeing and refining outputs." **[B]**

Read carefully, this is a claim about **code generation**: K3 writes a playable game/app (presumably Three.js/WebGL/canvas), screenshots the running result, and iterates. That is a completely different mechanism from Genie: the "world" is *programmed*, not *dreamed frame by frame*. The physics in such a world is whatever physics engine or hand-written update loop the model emitted — inspectable, deterministic, and debuggable.

- **No world model appears in Moonshot's model catalogue.** https://huggingface.co/moonshotai lists Kimi-K2.7-Code (Jun 15 2026), Kimi-K2.6 (May 19), Kimi-K2.5 (Apr 30), Kimi-K2-Instruct, Kimi-VL variants, Moonlight, Kimi-K2-Base. **No K3 entry yet, no world/video/environment model of any kind.** **[A — direct observation]**
- **No K3 repository on GitHub.** `gh api search/repositories?q=org:MoonshotAI+K3` returns **0** results. The MoonshotAI org (~40 repos) contains Kimi-K2, Kimi-K2.5, Kimi-VL, Kimi-Audio, Kimi-Linear, Kimi-Dev, MoBA, Moonlight, kimi-code, and **WorldVQA** — but nothing generative-environment. **[A]**
- **"WorldVQA" is a trap for the unwary.** https://github.com/MoonshotAI/WorldVQA (created 2026-01-26) is a *world-knowledge* benchmark: "3,500 VQA pairs across 9 categories" measuring "atomic vision-centric world knowledge," i.e. whether an MLLM can name and ground visual entities. Paper: arXiv:2602.02537. It has nothing to do with world *models*. Anyone skimming the Moonshot repo list could easily misreport this. **[A]**

### Independent corroboration of the code-generation reading

https://github.com/keunwoochoi/beetbox-eval **[A]** — an independent researcher (@keunwoochoi, July 2026) built an arena around a demo from the K3 release post:

> "I saw a short screen recording of Beetbox in the Kimi K3 release post, but without any interactive demo. Well… If they could prompt, I can prompt it too."

He fed several coding agents the same 19-second screen recording plus 1-fps frames and one prompt ("Recreate the Beetbox web app... as faithfully as possible"), and compared the resulting web apps. Two things follow: (a) K3's showcased "interactive experience" was a **web app built from code**, and (b) Moonshot published it as a video with **no playable artifact**, which is exactly the demo-vs-availability gap this section is meant to police.

### Verdict on Kimi K3

> **Kimi K3 is a frontier LLM that writes interactive software, not a generative world model.** It belongs in the same category as Claude/GPT/Gemini "vibe-coded simulation" workflows, not in the same category as Genie 3, Odyssey-2, or Oasis. Any survey text that lists K3 alongside Genie 3 as a world model is making a category error.
>
> This distinction is *good news* for education, not bad — see §6. Generated **code** is auditable; generated **pixels** are not.

Also noted, unverified relevance: Moonshot released **PerceptionBench** the same day (2026-07-16, per moonshot.ai). A repo `perceptionbench2026/PerceptionBench` was created 2026-07-22 but had no readable README at time of access. **[D]**

---

## 3. The broader world-model landscape, sorted by what you can actually use

### Tier 1 — usable by a developer today, self-serve

| System | What it is | Access | Evidence |
|---|---|---|---|
| **World Labs Marble** (Fei-Fei Li) | "Frontier multimodal world model" that reconstructs/generates 3D worlds from text, single image, multi-image, video, or coarse 3D layout ("Chisel"). Exports **Gaussian splats, triangle meshes (collider + visual), and camera-controlled video**. | **Generally available since 2025-11-12**, marble.worldlabs.ai; API at platform.worldlabs.ai (both live, HTTP 200) | **[B]** https://www.worldlabs.ai/blog/marble-world-model |
| **Decart** | Lucy 2.5 (real-time video editing/restyling, **30 fps**), **Oasis 3** ("interactive world model", real-time), Lucy Image. | Self-serve API keys at platform.decart.ai; free "Try Oasis 3" demo | **[B/C]** https://decart.ai/, https://platform.decart.ai/ |
| **Odyssey** | Odyssey-2 ("dreams in video", "**multi-minute simulations, not 10 second clips**", ~**50 ms** generation, instant streaming); Agora-1 (multi-participant shared world simulation); Starchild-1 (multimodal interaction learning). | Public demos at experience.odyssey.ml and agora.odyssey.ml (both HTTP 200). **No API, no pricing disclosed.** | **[C]** https://odyssey.ml/ — the page itself concedes "Odyssey-2 is early" |
| **NVIDIA Cosmos** | World foundation model platform: Reason (VLM), World Simulation ("controllable physics-grounded simulator"), Action Generation. Paper: arXiv:2501.03575 (77 NVIDIA authors, 2025-01-07). | **Open weights on HuggingFace**, post-training scripts on GitHub, **OpenMDW 1.1 (Linux Foundation)** license per nvidia.com; CC-BY-4.0 per the paper | **[A/B]** https://arxiv.org/abs/2501.03575, https://www.nvidia.com/en-us/ai/cosmos/ |
| **Microsoft WHAM / Muse** | Autoregressive model over (observation, action) pairs. **300×180 px, 10 Hz, context of 10 (obs, action) pairs**, 200M (3.7 GB) and 1.6B (18.9 GB) checkpoints. Trained on ~500,000 games of *Bleeding Edge* (>1B obs-action pairs). | **Downloadable by anyone on HuggingFace**, Microsoft Research License (academic research only), confined to the one game | **[A/B]** Nature 638 (2025), doi:10.1038/s41586-025-08600-3; https://huggingface.co/microsoft/wham |

**Important:** Cosmos is explicitly aimed at **robotics and autonomous vehicles**, not games or education — its stated use cases are robot policy learning, AV synthetic sensor data, industrial video analytics. Marble produces **static 3D scenes**, not interactive simulation; the World Labs page itself flags interactivity as future work. WHAM is 300×180 pixels of one Xbox game. None of these is a general educational world engine.

### Tier 2 — real but gated

- **Genie 3 / Project Genie** — Google AI Ultra, US only, 18+, no API. **[B]**
- **SIMA 2** — limited research preview, small cohort. **[B]**

### Tier 3 — repositioned or absent

- **Runway.** The Dec 2023 "General World Models" post (https://runway.com/research/introducing-general-world-models) was a research *position*, not a product; it shipped nothing and described Gen-2 as only "very early and limited forms of general world models." **[B]** As of 2026-07, https://runway.com/research lists **GWM-1** ("a state-of-the-art General World Model built to interact with the real world"), Gen-4.5, a **Robotics Suite**, and "Accelerating Robot Policy Evaluation with General World Models." **There is no "Game Worlds" product listed** — Runway's world-model effort has been repositioned toward robotics policy evaluation. **[B]** Any survey text citing "Runway GameGen" should be checked; I found no such product.
- **Sora / Veo as world simulators.** OpenAI's pages (openai.com/index/sora-2/, openai.com/index/video-generation-models-as-world-simulators/) returned **HTTP 403** to automated fetch, so OpenAI's own claims could not be verified directly in this pass. **[D — vendor claims unverified here]** However, Sora *was* independently tested and found wanting on physics (§5), which is the more useful evidence anyway. For Veo, the relevant primary source is arXiv:2509.20328 (§5).

### Playable-video research lineage (for the survey's technical narrative)

- **GameNGen** — "Diffusion Models Are Real-Time Game Engines," Valevski, Leviathan, Arar, Fruchter, arXiv:2408.14837 (2024-08-27, ICLR 2025). **DOOM at 20 fps on a single TPU, PSNR 29.4** (comparable to lossy JPEG). Human raters distinguishing real from generated gameplay performed **"only slightly better than random chance"** on short clips. **[A]** This is the proof-of-concept that a neural net can *be* a game engine.
- **DIAMOND** (diffusion world models for RL, arXiv:2405.12399) and **Decart/Etched Oasis** (open Minecraft-like) are the other well-known nodes; Oasis has **no technical paper** — blog and demo only. **[D]**

---

## 4. Why this matters for learning: the hand-built simulation baseline

If generated worlds are going to be a learning substrate, they must beat or complement something that already works extremely well and is free.

### PhET (University of Colorado Boulder) is the benchmark

https://phet.colorado.edu/en/research **[B]**

PhET's own research page describes their process: **4–6 think-aloud interviews per simulation** with individual students, plus classroom observation, driving iterative redesign. Design principles include "encourage scientific inquiry" and "make the invisible visible." The publication list runs to 100+ items. **[B]**

Key efficacy results, with citation counts as a proxy for standing in the field:

| Study | Finding | Evidence |
|---|---|---|
| **Finkelstein, Adams, Keller et al. (2005)**, "When learning about the real world is better done virtually," *Phys. Rev. ST PER* 1, 010103, doi:10.1103/PhysRevSTPER.1.010103, ~358–617 citations | In an intro DC-circuits lab, students using a **simulation outperformed students using real light bulbs, meters and wires** — both on a conceptual survey **and** on the coordinated task of assembling a *real* circuit and explaining it. | **[A]** (full abstract retrieved) |
| **Wieman, Adams, Perkins (2008)**, "PhET: Simulations That Enhance Learning," *Science* 322, doi:10.1126/science.1161948, ~272–373 citations | The canonical statement of the PhET design philosophy and its learning claims. | **[A]** existence + venue verified via Crossref/S2; abstract paywalled |
| **de Jong, Linn, Zacharia (2013)**, "Physical and Virtual Laboratories in Science and Engineering Education," *Science* 340:305, doi:10.1126/science.1230579, **~671–920 citations** | The field's authoritative review of virtual vs physical labs. | **[A]** verified via Crossref + S2; abstract elided by publisher |
| **Rutten, van Joolingen, van der Veen (2012)**, *Computers & Education*, doi:10.1016/j.compedu.2011.07.017, **~658–955 citations** | Review of learning effects of computer simulations in science education. | **[A]** verified |
| **Smetana & Bell (2012)**, *Int. J. Sci. Educ.*, doi:10.1080/09500693.2011.605182, **~425–600 citations** | Critical review; the consistent conclusion across this literature is that simulations work **when paired with guidance/scaffolding**, and are weak when used as unguided free exploration. | **[A]** verified |
| **Meta-analysis of PhET specifically**: Fadillah, Alawyah, Syafrijon (2026), *iJOE* 22(2), doi:10.3991/ijoe.v22i02.59007; also de Medeiros Jr. et al. (2024), *Rev. Bras. Ens. Fis.*, doi:10.1590/1806-9126-rbef-2024-0186 | Recent quantitative syntheses of PhET effectiveness exist. | **[A]** existence verified; effect sizes not retrieved |
| **Implicit scaffolding**: Paul, Podolefsky, Perkins (2013), "Guiding without feeling guided," doi:10.1063/1.4789712; Podolefsky, Rehn, Perkins (2013), doi:10.1063/1.4789713 | PhET's distinctive design contribution: the *constraints of the sim itself* do the pedagogical steering, so students feel they are playing while being channelled toward the target concept. | **[A]** |

**The thing a generated world does not get for free.** Every PhET sim embodies (a) a *correct* physical model, (b) a *deliberately simplified* model — the right lie for the learner's level, (c) *implicit scaffolding* — affordances chosen so that the natural exploration path is the productive one, and (d) years of iterative interview-driven refinement. A Genie-style model reproduces only the *surface* of (a) and none of (b)–(d). Implicit scaffolding is arguably the hardest to replicate: it is not "physics," it is *pedagogical* design encoded in what the sim will and will not let you do.

Adjacent tools: **GeoGebra** and **Desmos** are the math analogues — hand-built, deterministic, symbolically exact. The literature on them is large but thin in quality (many small quasi-experiments; e.g. Anajihah et al. 2025 meta-analysis, doi:10.30738/indomath.v8i1.140; Bhatia & Chakraborty 2024, doi:10.1080/09747338.2024.2341068). Their real argument is not effect size — it is that a *computer algebra system cannot be wrong about algebra*, which is precisely the property a generative model lacks.

### The one direct empirical study of generated simulations in a real course

**Ben-Zion, Carroll, West, Wong, Finkelstein (2026)**, "Leveraging generative artificial intelligence for simulation-based physics experiments: A new approach to virtual learning about the real world," *Phys. Rev. Physics Education Research*, doi:10.1103/s8dy-kqy5, published 2025-12-22 / Jan 2026 issue. Open access. **[A — full abstract retrieved via DOAJ API]**

Note the last author: **Noah Finkelstein**, the same CU Boulder group behind the 2005 study and PhET itself. The title is a deliberate echo of Finkelstein 2005.

Design: second-semester physics for life-science majors, electric potentials lab, **three conditions**: (i) physical equipment, (ii) prebuilt simulator, (iii) **students using AI to generate a simulation**.

Findings:
- Significant differences on conceptual assessment, **η² = 0.359** (a large effect).
- Post hoc: **both the AI-generated and prebuilt simulation conditions scored significantly higher than the physical-equipment condition.** AI-generated was not distinguishable from prebuilt in the reported post hoc.
- Both simulation groups reported more favourable perceptions of the experience.
- The authors highlight a *different* affordance from the one usually advertised: "opportunities for developing students' modeling skills through the processes of **designing, refining, and validating** AI-generated simulations."

**This is the most important single result for our section.** Three consequences:

1. Generated simulations can match hand-built ones on conceptual outcomes — **in a curated classroom setting with an instructor and a well-specified topic.**
2. The mechanism is **LLM-generated simulation code**, not generated video. The pedagogy that made it work is *students validating the AI's simulation against physics they are learning* — the AI's fallibility was converted into the learning objective.
3. It is a **single preliminary study, n unreported here, one topic, one course.** Do not generalise it into "generated worlds teach as well as PhET."

---

## 5. The correctness problem — treat this as the central risk

A generated world that gets physics wrong is not a neutral failure. It is an *active teaching instrument for a misconception*, delivered with the persuasive force of high-fidelity video, in a medium where learners have no way to tell simulation from hallucination. Everything in the benchmark literature says this risk is currently high.

### The measurements

| Benchmark | Finding | Source |
|---|---|---|
| **VideoPhy** — Bansal, Lin, Xie, Zong, Yarom, Bitton, Jiang, Sun, Chang, Grover (2024-06-05) | Text-to-video models on material-interaction prompts (e.g. marbles on inclines). **Best model (CogVideoX-5B) satisfied both the prompt and physical law in only 39.6% of instances.** Conclusion: models "are far from accurately simulating the physical world." | arXiv:2406.03520 **[A]** |
| **VideoPhy-2** — Bansal, Peng, Bitton, Goldenberg, Grover, Chang (2025-03-09) | Action-centric, 200 actions. **Best joint (semantic + physical) performance on the hard subset: 22%.** Models "particularly struggle with **conservation laws like mass and momentum**." | arXiv:2503.06800 **[A]** |
| **PhyGenBench** — Meng, Liao, Tan, Shao, Lu, Zhang, Cheng, Li, Qiao, Luo (2024-10-07) | **160 prompts across 27 distinct physical laws in 4 domains.** Current models "struggle to generate videos that comply with physical commonsense," and critically: **"simply scaling up models or employing prompt engineering techniques is insufficient."** | arXiv:2410.05363 **[A]** |
| **Physics-IQ** — Motamed, Culp, Swersky, Jaini, Geirhos (Google DeepMind, 2025-01-14) | Tested Sora, Runway, Pika, Lumiere, Stable Video Diffusion, VideoPoet. Headline: **"physical understanding is severely limited, and unrelated to visual realism."** | arXiv:2501.09038 **[A]** |
| **WorldModelBench** — Li, Fang, Chen, Yang, Cao, Wong, Luo, Wang, Yin, Gonzalez, Stoica, Han, Lu (2025-02-28) | 14 frontier video models, **67K human labels**. Explicitly detects violations such as "irregular changes in object size that breach the mass conservation law." | arXiv:2502.20694 **[A]** |
| **WorldScore** — Duan, Yu, Chen, Fei-Fei, Wu (ICCV 2025) | Unified world-generation benchmark: **controllability, quality, dynamics**; 3,000 test examples, **19 models** across video-gen, 3D-gen and 4D approaches. | arXiv:2504.00983 **[A]** |
| **Show, Don't Tell / ProVisE + SpatialGen-Bench** — Wang, Yao, Pan, Zhou, Liu, Zhang, Zhang (2026-07-23) | 470 samples, 14 spatial subtasks. Image-generation models compete when spatial answers are expressed in pixels, but **text-output VLMs retain the advantage in compositional spatial reasoning.** Recent evidence that pixel-space "understanding" and symbolic spatial reasoning are still dissociated. | arXiv:2607.21072 **[A]** |

### The counter-argument, stated fairly

**"Video models are zero-shot learners and reasoners"** — Wiedemer, Li, Vicol, Gu, Matarese, Swersky, Kim, Jaini, Geirhos (2025-09-24), arXiv:2509.20328. **[A]** Claims Veo 3 shows emergent zero-shot segmentation, edge detection, image editing, "understanding physical properties," affordance recognition, tool-use simulation, and "early forms of visual reasoning like maze and symmetry solving," arguing video models are "on a path to becoming unified, generalist vision foundation models."

Note that Geirhos and Jaini are authors on *both* this and Physics-IQ. The same group that found "physical understanding is severely limited" also finds emergent capability. The honest reading: capability is rising fast and is real, but the paper's own hedge is **"early forms"** and **"emergent"** — which is not the same as reliable, and reliability is what teaching requires.

### Why this is worse for education than for entertainment

1. **The failure modes are exactly the concepts we teach.** Conservation of mass and momentum (VideoPhy-2), object permanence, cause and effect. These are not cosmetic glitches; they are the *curriculum*.
2. **Fidelity decouples from correctness** (Physics-IQ). A photoreal 720p world that violates momentum conservation is *more* dangerous than a crude one, because realism is the cue learners use to decide whether to trust what they see.
3. **Scaling does not fix it** (PhyGenBench). The "wait for the next model" argument has been directly tested and failed.
4. **There is no error signal.** In a PhET sim, an incorrect behaviour is a bug someone can file. In a generated world, there is no ground truth, no reference implementation, no test suite, and no way for a 14-year-old to know that the pendulum they just watched had the wrong period.
5. **Text illegibility** (Genie 3's own stated limitation) removes the one channel by which a world could label or correct itself.
6. **Misconceptions are famously persistent.** The whole conceptual-change literature (and PhET's own design philosophy) exists because misconceptions, once installed, resist instruction. A generative world is a high-throughput misconception factory if unsupervised.

### The mitigations that follow

- **Prefer generated *code* to generated *pixels*.** Code can be read, unit-tested, executed against known analytic solutions, and version-controlled. This is what the Ben-Zion 2026 study actually did, and what Kimi K3 / Claude / GPT-class models actually do. Generated pixels are unauditable by construction.
- **Constrain the generated world to a verified engine.** Let the model author scene, narrative and task; let a real physics engine (or a symbolic CAS) own the dynamics.
- **Make validation the learning objective.** Ben-Zion et al.'s "designing, refining, and validating" framing turns the correctness problem into a modelling curriculum. This is the only design pattern found in this pass that is *robust to* model error rather than dependent on its absence.
- **Restrict generated worlds to domains where correctness is not the point** — historical settings, language immersion, narrative, procedural/design practice, social scenario rehearsal.
- **Never use a generative world model as the authority on a physical law.**

---

## 6. Interactive fiction and text worlds — the cheap, correct substrate

Text worlds are the underrated option. They are orders of magnitude cheaper, run anywhere, and — crucially — a text world's state can be maintained by a **symbolic simulator** rather than a neural one, which makes it *correct by construction*.

- **TextWorld** — Côté et al. (Microsoft Research), arXiv:1806.11532 (2018-06-29, Computer Games Workshop @ IJCAI). A Python sandbox that "handles interactive play-through of text games, as well as backend functions like state tracking and reward assignment," and lets you "handcraft **or automatically generate** new games" with controlled difficulty, scope and language. **[A]** The generation is *grammar/planner-driven*, not neural — so the world model is guaranteed consistent.
- **ScienceWorld** — Wang, Jansen, Côté, Ammanabrolu, "ScienceWorld: Is your Agent Smarter than a 5th Grader?", arXiv:2203.07540 (2022). An interactive text environment at **standard elementary (5th-grade) science curriculum level.** Headline result: **a 1.5M-parameter agent trained interactively for 100k steps outperforms an 11B model statically trained on millions of expert demonstrations** for scientific QA. And the diagnosis is directly educational: models "can answer factual questions (like material conductivity) but cannot **reason about or explain learned science concepts in novel contexts**, such as designing experiments to test unknown materials." **[A]**

  ScienceWorld is the single most relevant artefact in this whole section: an *interactive, curriculum-aligned, symbolically correct* world where learning-by-doing measurably beats learning-by-reading. It was built for agents, but the pedagogy it demonstrates is the human one.

- **Jericho** (Hausknecht et al.) and **BALROG** are the standard interactive-fiction agent suites; **ALFWorld** aligns text and embodied versions of the same tasks. *(IDs not re-verified in this pass — **[D]** on exact arXiv numbers.)*
- Education-side literature is thin but exists: Wright & Weible (2024), "Current attitudes on digital interactive fiction and text adventure games within learning contexts: A systematic literature review," *J. Res. Sci. Math. Tech. Educ.*, doi:10.31756/jrsmte.713 **[A]**; Dickey (2006), "Game Design Narrative for Learning," *ETR&D*, doi:10.1007/s11423-006-8806-y, 211 citations **[A]**; Pereira (2014) on interactive fiction for game-based language learning, doi:10.1057/9781137023315_11 **[A]**.

**The architectural point for the survey:** an LLM narrating over a symbolic state machine gets you generative *variety* with simulated *correctness*. The LLM handles language, character and improvisation — where hallucination is a feature. The state machine handles physics, inventory, causality and progression — where hallucination is fatal. This hybrid is available today, at chat-model prices, and is the most defensible generative learning substrate that currently exists.

---

## 7. Synthesis: what a generated world buys, and what it costs

**Buys:**
- **Variety and personalisation at zero marginal cost.** PhET has a few hundred sims built over 20+ years; a generative model has a combinatorial space. A world set in the learner's own town, or matched to their interest, is free.
- **The long tail.** Nobody will hand-build a sim for every niche topic. Generation covers the tail that hand-building never reaches.
- **Speed of iteration.** Minutes instead of months.
- **Learner authorship.** The learner can *make* the world, which is a different and possibly better activity than exploring someone else's — this is the affordance Ben-Zion et al. (2026) actually found value in.

**Costs:**
- **Correctness** — measured at 22–40% physical-commonsense adherence on the hardest benchmarks (§5), with no ground truth, no error reporting, and no evidence that scale fixes it.
- **Pedagogical design.** Implicit scaffolding, deliberate simplification, and the choice of what *not* to model are the actual intellectual content of a good sim. Generation gives none of this.
- **Persistence and reproducibility.** Genie 3 forgets after ~1 minute and stays consistent for "a few minutes." A curriculum needs a world that is the same next Tuesday, for every student, and can be assessed against.
- **Text.** Genie 3 admits it can't render legible text unless it was in the prompt. Most instructional content is labelled.
- **Access and cost.** The good stuff (Genie 3, SIMA 2) is a US-only consumer subscription or a research preview. Real-time neural world generation is expensive per learner-minute in a way PhET's static JavaScript is not.

**The defensible position for the survey:**

> Generated *pixel* worlds are, as of mid-2026, a **demo-grade** technology for education: genuinely impressive, genuinely inaccessible, and measurably unreliable on exactly the physical facts that science education is about. Generated *code* simulations — an LLM writing an auditable, executable model that a student then validates — already have positive experimental evidence from the PhET group's own institution and can be deployed today. And LLM-narrated symbolic text worlds are the cheapest correct substrate available.
>
> The direction of travel is clear and the capability curve is steep. But "Genie 3 will teach physics" is currently a claim supported by curated demo videos, contradicted by every published measurement of physical plausibility, and blocked in practice by a US-only Ultra subscription with no API.

---

## Appendix: source inventory (47)

**Primary technical papers [A]** — arXiv:2402.15391 (Genie), 2406.03520 (VideoPhy), 2503.06800 (VideoPhy-2), 2410.05363 (PhyGenBench), 2501.09038 (Physics-IQ), 2502.20694 (WorldModelBench), 2504.00983 (WorldScore), 2509.20328 (Veo3 zero-shot), 2607.21072 (ProVisE/SpatialGen-Bench), 2408.14837 (GameNGen), 2501.03575 (Cosmos), 1806.11532 (TextWorld), 2203.07540 (ScienceWorld), 2602.02537 (WorldVQA), 2405.12399 (DIAMOND, id unverified).

**Peer-reviewed education [A]** — doi:10.1103/PhysRevSTPER.1.010103; 10.1126/science.1161948; 10.1126/science.1230579; 10.1016/j.compedu.2011.07.017; 10.1080/09500693.2011.605182; 10.1103/s8dy-kqy5; 10.3991/ijoe.v22i02.59007; 10.1590/1806-9126-rbef-2024-0186; 10.1063/1.4789712; 10.1063/1.4789713; 10.1063/1.3680053; 10.1119/1.2150754; 10.1119/1.3361987; 10.31756/jrsmte.713; 10.1007/s11423-006-8806-y; 10.1057/9781137023315_11; 10.30738/indomath.v8i1.140; 10.1080/09747338.2024.2341068; 10.1038/s41586-025-08600-3 (WHAM, Nature).

**Vendor pages [B/C]** — deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/; deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/; deepmind.google/models/genie/; deepmind.google/models/; deepmind.google/blog/sima-2-…/; labs.google/projectgenie; worldlabs.ai/blog/marble-world-model; decart.ai; platform.decart.ai; odyssey.ml; nvidia.com/en-us/ai/cosmos/; runway.com/research; runway.com/research/introducing-general-world-models; kimi.com/blog/kimi-k3; moonshot.ai; platform.kimi.ai/docs/introduction; huggingface.co/moonshotai; huggingface.co/microsoft/wham; phet.colorado.edu/en/research; phet.colorado.edu/en/about.

**Repository / API evidence [A]** — github.com/MoonshotAI (org listing, 0 K3 repos); github.com/MoonshotAI/WorldVQA; github.com/MoonshotAI/Kimi-K2.5; github.com/keunwoochoi/beetbox-eval; `gh api search/issues?q="kimi-k3"` (5,808 results).

**Inaccessible in this pass [D]** — openai.com/index/sora-2/ (403); openai.com/index/video-generation-models-as-world-simulators/ (403); link.aps.org (403); no technical report exists for Genie 2, Genie 3, Odyssey-2, or Decart Oasis.

**Tooling note:** arXiv API, Semantic Scholar and OpenAlex were all rate-limited or budget-exhausted during this pass; Crossref, DOAJ, Unpaywall, `gh api` and direct WebFetch on arxiv.org abstract pages were used instead. Where an abstract was elided by a publisher, existence, venue, year and citation count were still verified and the claim is tagged accordingly.

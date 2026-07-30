# Z2 — Frontier capability gap audit

**Date:** 2026-07-30  
**Brief audited:** `TASK.md`, Part A and founding ask 1  
**Purpose:** identify what the raw corpus failed to research, not what the survey
failed to summarize.

## 0. Method

The existing raw corpus was searched clause by clause against the founding brief.
Presence was not counted as coverage. A named product in a landscape table, a link in
a bibliography, or a paragraph saying a capability exists is **mention-only**.
Coverage requires:

1. the current capability and its constraints;
2. the learning action it makes possible;
3. the verification or measurement problem it creates;
4. a comparison against the best alternative representation;
5. an executable prototype or experiment.

This is a gap audit, not a source-count exercise. The corpus contains hundreds of
thousands of words and still leaves central clauses thin.

---

## 1. Correction: term counts overstated the gaps

The first pass of this audit used file-level term counts to identify candidates. That
method produced false gaps and is rejected here. A4 already contains a detailed July
2026 comparison of Gemini Live, OpenAI Realtime, session resumption, semantic VAD,
camera limits, cost and Wan2.2. A5 already distinguishes Kimi-generated interactive
software from neural world models. A1 and D3 already treat generated textbooks, with
D3 carrying Learn Your Way's delayed RCT. K2 already researches agentic tutoring as
sampling, execution, persistence and absence. D1 already includes Claude for Teachers.

The corpus did the research in those areas. The failure was **propagation and
integration**: those findings did not become the main survey, dashboard, deck or an
end-to-end demonstration. A grep count cannot distinguish that from absence.

## 2. The remaining research gaps

| ID | Founding requirement | Raw-corpus state | Verdict |
|---|---|---|---|
| Z2-1 | Agent-native / agent-first education | K2 deeply covers agentic capability and G2 covers orchestration; no report defines a two-sided interface that lets learners and agents operate the same educational state | **Narrow technical gap** |
| Z2-2 | One coherent school/university in a box | Components are distributed across reports | **Missing as a system** |
| Z2-3 | On-the-fly personalised textbook | A1 and D3 are strong, including Learn Your Way; the corpus has no live book runtime, shared schema or longitudinal mutation model | **Runtime/schema gap** |
| Z2-4 | Frontier live audio-in/video-in/audio-out/video-out | A4 is current and detailed; V4 covers live formats | **Researched; failed to propagate** |
| Z2-5 | Generated interactive worlds | A5 is current, careful and correctly separates generated software from generated pixels | **Researched; renderer policy missing** |
| Z2-6 | Kimi-style generation of interactive artifacts | A5 and E3 cover Kimi K3 capabilities and category boundaries | **Benchmark gap** |
| Z2-7 | Live generated avatar mentor / Wan streamer | A4 contains the stack, hardware burden, latency and evidence analysis | **Researched; target-specific trial missing** |
| Z2-8 | Dynamic mini-app per concept | K2 researches on-demand environment synthesis; A1/A2/F7 cover content and notebooks | **Compiler/CI gap** |
| Z2-9 | Manim, Remotion, notebooks and slides as interchangeable renderers | A2, C3 and F7 cover the tools and formats | **Common intermediate representation missing** |
| Z2-10 | Learn elite creators' craft by domain | V1 contains 104 techniques; no automated observation/coding pipeline or licensing/attribution model turns new creator work into policies | **Inventory strong, ingestion loop missing** |
| Z2-11 | Scientific remembering as a product loop | F11 is deep; connection to session memory, curriculum compilation and withdrawal testing is incomplete | **Integration gap** |
| Z2-12 | “Grill me” diagnosis of mode, level and misconceptions | J1/F5/F9 cover diagnosis; no multimodal first-session protocol compares speech, drawing, manipulation and reading without reifying “learning styles” | **Experiment specified only in pieces** |
| Z2-13 | Zero-to-hero across any field | K1 covers compression; no cross-domain goal compiler, prerequisite acquisition benchmark or portfolio credential | **Claim bounded, system missing** |
| Z2-14 | Publisher/author/site ecosystem | M1 and thesis are strong commercially; no technical interchange format for concept packages, rights, author intent, item telemetry and royalties | **Business case strong, protocol missing** |
| Z2-15 | SELPA-first frontier experience | H1/H2 are unusually deep; the frontier modalities in A4/A5 are not evaluated as accommodations and the integrated demos do not begin with an access profile | **Cross-report integration gap** |

---

## 3. What the 2026 capability baseline changes

### 3.1 Live multimodality is now substrate, not a speculative feature

Google's Live API accepts continuous audio, images and text and returns spoken audio
over a stateful low-latency connection. Its current documentation lists native audio,
97 languages, proactive audio, affective dialogue, tool use and configurable media
resolution. It also publishes constraints the corpus did not carry together:
audio-only sessions are limited to 15 minutes, audio-plus-video sessions to two
minutes, with session-management patterns required to extend them.

OpenAI's Realtime API natively supports speech-to-speech plus text, image and audio
input over WebRTC, WebSocket and SIP. Its semantic voice-activity detection estimates
whether a speaker has finished rather than relying only on silence. That matters for a
learner who pauses to reason or retrieve a word: turn-taking is now a pedagogical
parameter, not only a transport detail.

**Sources:**  
Google, Live API overview and capabilities:
https://ai.google.dev/gemini-api/docs/live-api and
https://ai.google.dev/gemini-api/docs/live-api/capabilities  
OpenAI, Realtime API:
https://platform.openai.com/docs/api-reference/realtime

**New research question.** Compare semantic end-of-turn, learner-controlled
push-to-talk and patient fixed-delay turn-taking for learners with language,
processing-speed and attention accommodations. Primary outcome: completed reasoning
units and self-corrections, not conversational smoothness.

### 3.2 A world can now be generated while the learner moves through it

DeepMind describes Genie 3 as a text-prompted world model producing navigable,
interactive 720p environments at 20–24 fps with consistency over minutes and
promptable world events. It explicitly names learning through historical exploration
as an application. The published limitations are as important: limited agent action
space, weak multi-agent interaction and inaccurate representation of real locations.

This changes the question from “can AI make a visual?” to “which concepts require
counterfactual action inside a world?” A generated Roman street is not evidence about
Rome. It may be an orientation or spatial-causality instrument, provided historical
claims are supplied by a separate verified layer.

**Source:** Google DeepMind, Genie 3:
https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

**Prototype.** One concept, three renderers: static causal diagram, deterministic
simulation and generated world. Hold target claims and practice time constant.
Measure delayed causal prediction and transfer to a non-visual item. The world earns
its cost only if it beats both cheaper renderers.

### 3.3 Generated mini-apps have crossed from demo to distribution surface

Anthropic reports that educators use Artifacts for chemistry simulations, educational
games, automated rubrics and data visualisation. Its product now permits shareable
AI-powered apps that generate new content inside the artifact. Anthropic reports over
half a billion artifacts created; that is a vendor count, not learning evidence.

The missed research object is the **artifact compiler**:

`concept contract → generated app → executable tests → accessibility checks →
learner event schema → publish → outcome-linked revision`

Current artifact products largely stop at “it runs and looks right.” Education needs
tests for invariant preservation, misconception handling, keyboard/screen-reader
access, and whether the emitted event can update the learner model.

**Sources:**  
Anthropic, AI-powered Artifacts:
https://www.anthropic.com/news/build-artifacts  
Anthropic education usage report:
https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude

### 3.4 Open avatar generation is not the same thing as a live mentor

Wan2.2 publishes weights and inference code for text-to-video, image-to-video,
speech-to-video and character animation. The speech-to-video model accepts audio plus
a reference image and optional pose video; the documented 14B path expects at least
80 GB of GPU memory. This is an offline generation substrate, not evidence of a
low-latency bidirectional tutor.

The raw corpus repeatedly groups “avatar” systems that solve different problems:
offline presenter rendering, low-latency lip sync, conversational turn-taking,
persistent identity and pedagogical action. They must be separated.

**Source:** Wan2.2 official repository:
https://github.com/Wan-Video/Wan2.2

**Decision rule.** A face is selected only for a measured function: joint attention,
gesture, articulation modelling, signed communication, social rehearsal or presence.
If voice plus shared workspace produces the same learning and persistence, the avatar
is decoration and loses on cost and bandwidth.

### 3.5 The education ecosystem is becoming callable

Anthropic's July 2026 teacher product connects standards and fine-grained learning
components to OpenSciEd and Illustrative Mathematics, then exposes tools including
ASSISTments, Eedi, Coteach, Snorkl and TeachFX. It can schedule recurring analysis of
exit tickets and adapt a following day's plan. This is teacher-facing and explicitly
not a child-facing autonomous university, but it demonstrates that curriculum,
diagnosis, content generation and classroom telemetry can be connected as tools.

The corpus's ecosystem thesis therefore needs a protocol, not another partnership
list. The competitive question is who owns the portable learner state and the
concept-level interchange contract across those tools.

**Source:** Anthropic, Claude for Teachers:
https://www.anthropic.com/news/claude-for-teachers

### 3.6 The products named in the brief need mechanism-level comparison

The corpus named Paradigm, Vizuara and Brilliant but did not extract their different
product theses.

**Paradigm** presents a learner-supplied source—a PDF, link or text—as the seed for a
course that is “rewritten as you go.” Its public examples combine generated units,
interactive elements, build-along cloud environments and a persistent companion that
tracks deadlines, reminders and learner context. The important product move is not
course generation; it is combining curriculum mutation with executive-function
support in one relationship. Public product copy is `VENDOR`, not outcome evidence.

**Vizuara's Vizz-AI** combines synchronized voice and text, multilingual real-time
conversation, interruption, questions anchored to a video's current visual timeline,
and live vision of the learner's workspace. That is a concrete reference design for
joint attention over authored video: the tutor and learner share both a timestamp and
a work surface.

**Brilliant** is the opposite architectural choice: authored, constrained interactive
problem solving with custom feedback, progressive difficulty and next-step
recommendations. It gives the generative system a control condition. A generated
concept app should not be compared with prose; it should be compared with the best
authored interactive.

**Kimi's current product documentation** now names K3, a general agent that produces
websites and slides, and an agent swarm. Kimi K2.6's product page demonstrates
full-stack app generation from a natural-language description. This is evidence that
the generation substrate exists, not that it produces instructionally correct apps.
The missing benchmark is a fixed set of concept contracts with seeded invariants,
misconceptions and accessibility requirements, scored after generation and after a
learner uses the app.

**Sources:**  
Paradigm: https://www.paradigm.study/  
Vizz-AI: https://vizz.vizuara.ai/  
Brilliant AI: https://brilliant.org/ai/  
Kimi product overview: https://www.kimi.com/help/getting-started/overview  
Kimi K2.6: https://www.kimi.com/ai-models/kimi-k2-6

**Comparison to run.** One difficult concept, the same 45-minute budget and four arms:
authored interactive, generated mini-app, live joint-attention tutor over authored
material, and adaptive generated course. Primary outcome is delayed novel-item
transfer; secondary outcomes are time to first correct mental model, accessibility
failures, authoring cost and factual/invariant violations.

### 3.7 Generated textbooks and generated media now have a measured starting point

D3 already carries the result this audit initially missed. Google's Learn Your Way
study randomised 60 learners aged 15–18 to an AI-transformed textbook experience or a
standard PDF reader on the same chapter. The generated experience included multiple
representations and formative quizzes and performed better on immediate and
three-day-delayed tests (`p = 0.03` for each); the paper does not isolate which
component caused the difference and reports no effect size in its text. Google's
public summary describes the delayed difference as 11 percentage points. This is a
small developer-run lab study and the most direct measured precedent for the founding
brief's personalised textbook.

NotebookLM's March 2026 Cinematic Video Overviews combine Gemini 3, image generation
and Veo 3 to create source-grounded animated videos, with Gemini making narrative,
visual and structural choices. The feature is 18+, English-only at launch and a vendor
capability claim; no learning comparison is published. Together the two products
create a clean next experiment: hold source, learner, time and retrieval items fixed;
compare adaptive interactive text, narrated slides, cinematic video and a
learner-routed combination.

**Sources:**  
Learn Your Way product and study summary:
https://blog.google/products-and-platforms/products/education/learn-your-way/  
NotebookLM Cinematic Video Overviews:
https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/

---

## 4. The missing technical architecture

The raw reports never define a common intermediate representation. Without one,
“generate a textbook, slide deck, animation, notebook, podcast, game or world” means
seven unrelated prompts with seven opportunities for semantic drift.

The missing object is a versioned **Learning Experience Graph**:

```text
Goal
 ├─ concepts and prerequisite edges
 ├─ target claims with source/rights provenance
 ├─ misconception hypotheses and discriminating actions
 ├─ representations
 │   ├─ prose / dialogue / slide
 │   ├─ diagram / Manim scene / Remotion sequence
 │   ├─ executable notebook / deterministic simulation
 │   └─ generated world / avatar encounter
 ├─ accessibility alternatives and response modes
 ├─ assistance ledger
 ├─ unassisted transfer items
 └─ future retrieval events
```

Renderers consume the same claims and learning objective. Validators check the output
against that graph. Learner events return to it. This is what makes a dynamic textbook
different from a collection of generated pages.

`DESIGN`. It fails if independently prompted renderers are equally faithful, equally
cheap to update and equally effective, or if the graph cannot represent a domain such
as dance, clinical communication, historical argument or graduate proof.

### 4.1 Agent-native changes the application boundary

Builder.io's Agent-Native framework states a precise invariant: define an action once
and expose it through the human UI, an agent, HTTP, MCP, A2A and CLI. Its runtime
bundles tools, memory, scheduled jobs, observability and handoffs. The education
corpus discusses agents extensively and never applies this application contract.

For a learning system, every consequential action needs one typed implementation:

| Action | Learner surface | Agent surface | Audit event |
|---|---|---|---|
| submit an explanation | voice, drawing, text, artifact | structured `submit_evidence` call | assistance level, source artifact, timestamp |
| change representation | visible choice or tutor suggestion | `render(concept, obstacle, mode)` | reason, cost, prior renderer and predicted benefit |
| update learner state | learner confirms or corrects | `propose_state_patch` | old value, uncertainty, evidence and author |
| schedule retrieval | calendar/timeline | persistent job | due rule, completion and unassisted score |
| request a specialist | faculty view | A2A handoff | trigger, context boundary, token budget and result |
| escalate to a person | help control | permissioned handoff | reason, shared fields and response |

The benefit is larger than developer convenience. Hidden agent-only mutations become
impossible; the learner can inspect and invoke the same actions. A human coordinator
can take over without screen-scraping state from a chat transcript. Tests can exercise
the actual production action without driving pixels.

**Source:** Builder.io, Agent-Native repository:
https://github.com/BuilderIO/agent-native

`DESIGN`. This boundary fails if separate learner and agent workflows produce fewer
errors or if a shared action schema cannot express multimodal evidence and
permissioned school records without leaking them.

---

## 5. New work packages

| Work package | Deliverable | Prototype | Kill condition |
|---|---|---|---|
| WP-1 Frontier interaction matrix | Current model/API comparison across live audio, image/video input, interruption, tools, session limits, languages, cost and deployment | Two live tutors behind one interface | No learning-relevant difference after transport is controlled |
| WP-2 Experience graph | Open schema plus three domain fixtures: fractions, photosynthesis, integration by parts | Render each fixture as dialogue, diagram, notebook and mini-app | Semantic drift is not reduced relative to independent prompts |
| WP-3 Artifact compiler | Generate, test, accessibility-audit and instrument one concept app | CI pipeline with deliberate seeded errors | Tests miss seeded conceptual or access failures |
| WP-4 World router | Decision policy for static, deterministic and generative environments | Three-renderer trial | Generated world does not improve transfer |
| WP-5 Agent-native learning runtime | State, permissions, tools, events and human/agent-readable UI | The same learner goal completed by human UI and agent API | Agent needs hidden UI-only state or learner cannot inspect agent action |
| WP-6 Multimodal access trial | First-session probes across speaking, pointing, drawing, manipulation and reading | SELPA-first onboarding | Modality routing worsens calibration or stigmatizes |
| WP-7 Creator-technique ingestion | Consent, coding, attribution, licensing and outcome loop for elite explainers | One creator, one domain, five techniques | Technique cannot be isolated or rights cannot be made legible |
| WP-8 Ecosystem protocol | Concept package schema, portable learner-state boundary, rights and royalty events | Author + open curriculum + item bank | Partner must surrender source or learner data to participate |
| WP-9 Zero-to-hero compiler | Goal decomposition, prerequisite acquisition and portfolio proof | One 20-hour cross-domain sprint | Learner cannot pass delayed novel-item and authentic-project checks |
| WP-10 Avatar function trial | Face/gesture vs voice+workspace at matched content | articulation, geometry deixis, social rehearsal | No target-specific benefit justifies video cost |

---

## 6. Correction to the project posture

The earlier corpus often asked, “has this improved a delayed learning outcome?” That
is necessary for efficacy claims and insufficient for frontier mapping. A capability
survey must also ask:

- What became technically possible this quarter?
- Which learning action was previously impossible or unaffordable?
- What is the smallest prototype that exposes the new capability?
- What external check makes an agent loop trustworthy?
- Which substrate can be replaced and which learner-state asset compounds?

Absence of an RCT does not make a frontier capability unimportant. It changes its
label from `MEASURED` to `CAPABILITY`, `DESIGN` or `OPEN`. The old posture allowed
unmeasured future systems to disappear from a survey explicitly commissioned to map
the future. This report restores them without promoting them to findings.

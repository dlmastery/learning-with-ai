---
title: "The Substrate — what the frontier actually supplies"
section: substrate
status: draft
date: 2026-07-28
source_report: research/raw/A4-live-multimodal.md, research/raw/A5-world-models.md, research/raw/D1-frontier-quarter.md
---

# The Substrate

Humans take the floor in conversation with a modal gap of **100–200 ms**, and
51–55% of all turn transitions across corpora happen in under 200 ms. That is
faster than language production: encoding a single word takes about 600 ms from
stimulus to speech onset, and a complex sentence roughly 1,500 ms. The arithmetic
only works if the listener predicts the end of your turn and plans their reply
*while you are still talking*.

Moshi, the open full-duplex speech model, reports **160 ms theoretical latency,
200 ms in practice**, which is inside the human window. It gets there the same
way people do, by modelling its own stream and the user's in parallel instead of
waiting for a silence timer.

That is the shape of the whole section. The frontier now supplies pieces that are
genuinely new: a conversation that can be interrupted, a camera that can see a
page of homework, a face that renders at video rate on one consumer GPU, and a
world conjured from a sentence. Each arrives with a hard edge, and in every case
the edge is somewhere other than the marketing suggests.

---

## 1. The duplex layer is real, and the good version is not for sale

Two vendors ship a managed real-time speech-to-speech loop. The differences that
matter for teaching are not the model quality.

| | Gemini Live | OpenAI Realtime |
|---|---|---|
| Transport | WebSocket only | **WebRTC**, WebSocket, SIP |
| Vision in | JPEG/PNG frames, **≤ 1 FPS** | `input_image` items; no documented native video |
| Session limit | **15 min audio-only; 2 min audio+video**; connection ≈ 10 min | not documented |
| End-of-turn | tunable VAD, 500–800 ms recommended | server VAD **or `semantic_vad`** (eagerness caps 8/4/2 s) |
| Barge-in bookkeeping | discarded generation dropped from history | auto-truncate on WebRTC; **manual on WebSocket** |
| In-session tools | function calling, Search. **No code execution** | function calling + **MCP** |
| Silent side-channel | — | **out-of-band responses** (`conversation: "none"`) |

Two of these decide whether you have a tutor.

**Barge-in bookkeeping.** Gemini's rule is that on interruption "only the
information already sent to the client is retained in the session history", so
the model's memory of what it said matches what the student actually heard. OpenAI's
WebRTC path matches this; the WebSocket path pushes truncation to the client, and
their own docs concede the model "doesn't have enough information to precisely
align transcript and audio." Get this wrong and the tutor believes it explained
step 3 when the learner only heard step 2 — a correctness bug that looks like a
student being obtuse.

**Endpointing is the latency budget.** Default server VAD is a 500 ms silence
timer plus 300 ms prefix padding. **That configuration alone exceeds the human
modal gap by 2.5–5× before the model has done any work.** Neither vendor
publishes an end-to-end latency figure anywhere in their documentation. Any
millisecond number in this survey comes from an academic system or a local
measurement, never from a vendor page. `semantic_vad`, a model-based
turn-*prediction* in place of a silence timer, is the closest shipped analogue
of what the turn-taking data says humans do.

**And the pedagogically correct target is not minimal latency.** Silence beyond
about 700 ms is socially marked, but in tutoring marked silence is often exactly
right; wait time is an instructional variable. The design goal is
**controllable** latency: fast for acknowledgement, deliberately slow for "think
about it." Human parity (≤ 250 ms) needs Moshi-class full duplex and is not
reachable on hosted APIs with default VAD; 300–800 ms feels natural on WebRTC
with aggressive semantic VAD and no avatar; 800–1500 ms is a comfortable tutor
including a real-time face; beyond 2 s — where open avatar stacks currently sit
at a self-reported 2.2 s — is annoying, and cascaded VAD→ASR→LLM→TTS pipelines
land past 3 s, which is broken.

The genuinely new architecture arrived in July 2026 and you cannot build on it.
GPT-Live listens and speaks simultaneously, backchannels, stays silent while you
think, and delegates a hard sub-problem to a frontier model *in the background
while continuing to talk*. That is the shape of a tutor saying "hold on, let me
think about that" without dropping rapport. It is ChatGPT-only. The API is a
sign-up form. **The highest-value capability of the quarter is, for builders,
unavailable**, and anyone planning a build this year should plan around its
absence.

---

## 2. What the camera can and cannot see

Vision into a live session is stills at one frame per second. It is not video,
and that single constraint sorts the use cases cleanly.

- **Camera on paper: works, today, on both platforms.** A worked problem is a
  static artifact; 1 FPS is more than enough. This is the strongest live-vision
  use case in education and it is available now.
- **Screen share of code: works,** and is well matched — code changes slowly.
- **Watching a *process* does not work.** A pen moving, a lab technique, a
  physics demo, sign language. 1 FPS discards the information that makes
  procedural feedback possible. Anyone claiming "the AI watches how you
  solve it" is over-claiming: it watches snapshots of the result.

There is no code execution inside a live session on Gemini Live at all, and
neither API has any output channel other than audio, transcript, and tool calls.
No cursor, no overlay, no highlight primitive.
Deixis, the "*this* term, *that* bracket" that is among the most powerful moves a
human tutor makes, has to be reconstructed by your own client from a model
reasoning about coordinates in an image it saw at ≤ 1 FPS.

A correction the project owes its readers here. The research behind this
section concluded flatly that "the pointing layer does not exist" and that
nobody had built a shared-pointing surface. The project's own correction ledger
subsequently records a deixis substrate in the literature (arXiv:2604.02893).
The revised claim is narrower and still true: **no vendor exposes deixis as a
primitive in a live session.** The design space is open without being empty.

---

## 3. The face: 25 FPS on one GPU, and no measured learning effect

The avatar layer has a sharp architectural dividing line where you would expect
a gradient.

Implicit-keypoint and warping models run at video rates on consumer hardware:
LivePortrait at **12.8 ms per frame on an RTX 4090**; MuseTalk at 30 FPS at
256×256 on a V100; SoulX-FlashHead-Lite at 96 FPS, or **three concurrent
real-time streams at 25+ FPS on a single 4090**. Diffusion-video models do not
and, so far, cannot: Wan 2.2 S2V requires ≥ 80 GB VRAM for single-GPU
inference, and the *fast* member of that family generates a 5-second 720p clip
in under 9 minutes on a consumer GPU. **That is roughly 108× slower than real
time.** Those are pre-render tools for canned lesson segments, not live-loop
renderers, and no local hardware short of a multi-GPU node changes the category.

So a locally-rendered talking tutor at 25 FPS is buildable today. The question
is whether it should be, and here the evidence is unusually clean and unusually
deflationary.

The null, stated at full strength. Three field experiments in real
university courses, using exam-relevant videos over 30 minutes taught by a
personally known instructor, compared a visible instructor with no visible
instructor:

> "positive effects of a visible instructor... on **some affective measures**:
> social presence in Study 1 (n = 18, d = .85) and well-being in Study 3
> (n = 38, d = 1.01)... They also show **no effects on extraneous processing or
> learning outcomes** (Studies 1–3). Thus, **no general effect of instructor
> presence can be shown**... but there are also no detrimental effects."

**A face reliably makes learners feel better and does not reliably make them
learn more.** The meta-analytic base agrees on
magnitude — pedagogical agents at **g ≈ 0.19** across 43 studies and 3,088
participants, **g ≈ 0.20** in an independent multimedia synthesis. (Both figures
were recovered from citation contexts and not from the paywalled originals;
re-verify before publication.) And in the same analysis, **agents communicating
via on-screen text outperformed agents communicating by narration**, the
opposite of the voice-first, face-first product thesis. The larger 2025
GenAI-agent effects (g ≈ 0.36–0.40) compare an AI tutor to *no tutor* and never
an agent with a face to the same agent without one: they measure the model, not
the avatar.

Two things the evidence does support. Embodiment helps *relative to a static
agent*. Gestures, gaze and expression beat their absence on a transfer test,
which is an argument about how to animate rather than whether to show a face.
And reducing consistency in human realism increases the uncanny effect, so a
photoreal face with slightly-off mouth motion is worse than a stylised face with
the same motion. Cartoon-quality avatars are an engineering choice and not a
compromise.

**Build the face for social presence and willingness to keep going, and say
exactly that.** Persistence is a learning input. It is not a learning gain.

---

## 4. Generated worlds: the measurement everyone skips

Genie 3, on DeepMind's own numbers: 720p, 24 fps, "a few minutes of continuous
interaction," visual memory "extending as far back as one minute ago," promptable
mid-session world events that alter weather or introduce objects. A real step
change — real-time interactive is qualitatively different from clip generation.
It is also a US-only, 18+, $200/month consumer tier with no API, no export and no
persistence guarantee, and **no technical report exists for Genie 2 or Genie 3.**
Every capability claim in that lineage is a vendor blog post plus curated demo
reels.

Now the benchmarks, which point the other way.

| Benchmark | Result |
|---|---|
| **VideoPhy** | Best model satisfied prompt *and* physical law in only **39.6%** of instances |
| **VideoPhy-2** | Best joint semantic + physical performance on the hard subset: **22%**. Models "particularly struggle with conservation laws like mass and momentum" |
| **PhyGenBench** | 160 prompts, 27 physical laws. "Simply scaling up models or employing prompt engineering techniques is **insufficient**" |
| **Physics-IQ** | "Physical understanding is severely limited, and **unrelated to visual realism**" |
| **WorldModelBench** | 14 frontier video models, 67K human labels; explicitly detects "irregular changes in object size that breach the mass conservation law" |

Five consequences make this worse for education than for entertainment.

1. **The failure modes are the curriculum.** Conservation of mass and momentum,
   object permanence, cause and effect. Not cosmetic glitches.
2. **Fidelity decouples from correctness.** A photoreal world that violates
   momentum conservation is *more* dangerous than a crude one, because realism is
   the cue learners use to decide whether to trust what they see.
3. **Scale does not fix it.** Tested directly, and failed. "Wait for the next
   model" is not an available argument.
4. **There is no error signal.** In a hand-built simulation an incorrect
   behaviour is a bug someone can file. In a generated world there is no ground
   truth, no reference implementation, no test suite, and no way for a
   fourteen-year-old to know the pendulum they just watched had the wrong period.
   Genie 3's own stated inability to render legible text unless it was in the
   prompt removes the one channel by which a world could label itself.
5. **Misconceptions persist.** The entire conceptual-change literature exists
   because they resist instruction once installed.

The counter-argument deserves its space. A 2025 paper argues video models are
zero-shot learners and reasoners, reporting emergent segmentation, physical-
property understanding, affordance recognition and "early forms of visual
reasoning" in Veo 3. Two of its authors are also authors on Physics-IQ, the paper
that found physical understanding "severely limited." Both are true: capability
is rising fast and is real, and the paper's own hedges are "early forms" and
"emergent," which is not the same as reliable. Teaching requires reliable.

---

## 5. The decomposition: generative world, symbolic physics

The design that follows splits the substrate in two.

> **Let the model author the world. Let a verified engine own the event
> stream.**

The *world* is scene, setting, narrative, character, task framing, the language
of the thing. Variety is the point there, and a generative model is unbeatable
at it. The *event stream* is physics, causality, inventory, state transitions,
progression, anything a learner might generalise from. There a single wrong
frame teaches a misconception, so it belongs to a physics engine, a computer
algebra system, or a plain symbolic state machine.

Three lines of evidence converge on this.

**Generated code beats generated pixels, and it has been tested in a real
course.** The CU Boulder group behind PhET ran a three-condition study in
second-semester physics for life-science majors: physical equipment, a prebuilt
simulator, and students generating their own simulation with AI. Conceptual
assessment showed **η² = 0.359**, a large effect, and post hoc **both simulation
conditions scored significantly higher than the physical-equipment condition**,
with AI-generated not distinguishable from prebuilt. The mechanism was
LLM-generated simulation *code*, and the pedagogy the authors highlight is
"designing, refining, and validating" — students checking the AI's simulation
against the physics they were learning. The model's fallibility became the
learning objective. **This is the only pattern found anywhere in this research
that is robust to model error rather than dependent on its absence.** It is also
a single preliminary study, one topic, one course; do not inflate it into
"generated worlds teach as well as PhET."

Symbolic worlds already work and are almost free. ScienceWorld is an
interactive text environment at fifth-grade science curriculum level, with state
maintained by a symbolic simulator and therefore correct by construction. Its
headline result belongs in any argument about substrate: **a 1.5M-parameter agent
trained interactively for 100k steps outperforms an 11B model statically trained
on millions of expert demonstrations.** Learning by doing beat learning by
reading, in a world that could not be wrong about itself.

And the category error worth correcting explicitly. Kimi K3 circulates in
summaries as a world model that creates interactive worlds. Moonshot's own
release blog **never uses the words "world model," "simulation," "physics," or
"environment."** What it says is that K3 "combines strong 3D reasoning, coding,
and vision capabilities to turn concepts, images, and videos into fully playable
interactive experiences," achieving "vision in the loop" by iterating between
code and live screenshots. That is code generation. There is no world model in
Moonshot's catalogue, no K3 repository, and the one repo with a suggestive
name, WorldVQA, is a *world-knowledge* visual-QA benchmark. **K3 writes
interactive software; Genie dreams pixels. Listing them together is a category
error.**

And this is good news. A programmed world's physics is whatever engine or update
loop was emitted. That is inspectable, deterministic, debuggable, unit-testable
against analytic solutions, version-controlled. Generated pixels are unauditable
by construction.

---

## 6. The nulls that should change what you build

Long context is a non-event for learning. A whole textbook has fit
comfortably in context for over a year; 1M tokens is now the default across an
entire commodity vendor's services. Yet a targeted arXiv query for
long-context / whole-textbook educational grounding returned **literally zero
results**, while curriculum-RAG is one of the healthiest clusters in the same
sweep. The field looked at "put the textbook in the window" and chose retrieval.
That is not inertia — the binding constraint was never capacity, it was
attribution. A teacher needs to know which page the claim came from, and a
stuffed context window destroys that affordance while adding cost and latency.

**Model capability does not transfer to tutoring capability, and there is now a
number. Solving ability and pedagogical ability correlate at r = 0.421** on
public benchmarks. The maths a learner needs help with is not Putnam; it is
fractions, and the specific fraction misconception this specific child holds.
Every current model solves that perfectly. The unsolved problem is diagnosing the
misconception and choosing *not* to solve it, and no maths benchmark measures
that — note that two frontier labs published no maths claims at all in their most
recent flagship posts.

And the pedagogy layer is permanently yours. LearnLM no longer exists as a
model family; Google's own documentation states its capabilities were "integrated
into Gemini starting with the 2.5 model series." There is no model ID that
returns a tutor. What survives is a product surface built from system
instructions, and OpenAI's Study Mode is described the same way; independently,
training-free prompt optimisation was found to beat RL-trained pedagogical
baselines. Pedagogy is a prompt-and-product layer and not a weights layer. That
is simultaneously the largest opportunity here and the reason most frontier model
releases are irrelevant to this work.

---

## 7. The build rules this substrate forces

- **Full duplex is the target and endpointing is the budget.** 200 ms is the
  human number; a 500 ms silence timer plus 300 ms padding already blows it.
  Build for *controllable* latency. Minimum latency is the wrong target,
  because wait time is a pedagogical variable.
- **Camera on paper and screen, not on process.** 1 FPS stills are excellent
  for a worked page and useless for a moving pen. Say which one you built.
- **Barge-in must be bookkeeping-correct.** The model's memory of what it said
  must equal what the learner heard.
- **Render the face at 25 FPS locally if you want one. Claim affect; do not
  claim learning.** d ≈ 0.85–1.01 on social presence and well-being; no learning
  effect in real courses; g ≈ 0.19–0.20 overall. Stylised beats
  almost-photoreal.
- **Generative world, symbolic event stream.** 39.6% best-case and 22% on the
  hard subset are not numbers you teach conservation laws with. Let the model
  write the scene; let an engine own the dynamics.
- **Prefer generated code to generated pixels**, and where possible make
  *validating the generated model* the assignment.
- **Never use a generative world model as the authority on a physical law.**

The frontier supplied a great deal this quarter and moved learning very little.
The one exception in these seven subsections was a field trial in a real physics
course; no model release came close. A dozen new benchmarks arrived to test
whether a model is smart, and roughly one trial a year tests whether it teaches.
That ratio is the widest measurement gap in applied AI, and closing it is the
subject of the last section of this survey.

---
title: "The JARVIS Inversion — an ambient tutor is not an ambient assistant"
section: north-star
status: draft
date: 2026-07-25
---

# The JARVIS Inversion

The target is an ambient, always-present, sees-what-you-see, remembers-everything
tutor. JARVIS is the right image and the wrong specification, and the difference
is the most important design decision in this document.

## 1. The inversion

**JARVIS assists an expert. A tutor must build one.**

Tony Stark already knows the physics. JARVIS's job is to *minimise* his cognitive
load: answer instantly, compute silently, never withhold, never quiz him. Every
one of those behaviours is correct for an expert operator and **wrong for a
learner**.

| JARVIS behaviour | Effect on an expert | Effect on a learner |
|---|---|---|
| Answers instantly | Removes friction | Destroys retrieval practice — the best-evidenced retention intervention |
| Never withholds | Maximises throughput | Produces dependence; the learner offloads instead of encoding |
| Explains fluently on demand | Efficient | **Fluency illusion** — feels understood, isn't retained |
| Agrees and complies | Correct for a tool | Sycophancy; blocks productive failure and error correction |
| Does the work in parallel | Force multiplier | Does the learning too |

So the pedagogical JARVIS is defined by a capability the fictional one never
needs: **the judgment to refuse.** Its highest-value act is deciding *not* to
answer — to ask instead, to wait, to let a struggle run, to withhold the formula
until the learner has tried.

This is not a softening of the vision. It is a harder engineering problem than
the original.

## 2. What JARVIS actually requires, decomposed

Seven capabilities, each independently assessable against 2026 reality.

| # | Capability | Status | Blocker |
|---|---|---|---|
| J1 | **Ambient / always-on** | ⛔ Blocked | Gemini Live: 15 min audio, **2 min with video**, ~10 min connection life. Escape hatch: `contextWindowCompression` + `sessionResumption` (2 h handles). OpenAI max session undocumented. |
| J2 | **Sees what you see** | ⚠️ Degraded | Video is **≤1 FPS**. Static artifacts (paper, code on screen) work. *Watching a process does not survive 1 FPS* — and process is exactly what the pivot rule needs. |
| J3 | **Points, draws, annotates** | ⛔ Absent | Neither Gemini Live nor OpenAI Realtime can point. Deixis must be rebuilt: function calling → your own canvas. **Largest unexploited design space in the stack.** |
| J4 | **Remembers everything** | ⛔ The core gap | Portfolio audit finding: *"The bottleneck is not generation — generation is solved to a startling degree. It is state."* |
| J5 | **Proactive, interrupts, volunteers** | ✅ Available | OpenAI Realtime **out-of-band responses** (`conversation: "none"`) is a silent side-channel — the model can evaluate "is this learner stuck?" without speaking. This is the proactivity primitive and it is under-used. |
| J6 | **Has judgment, pushes back** | ⛔ Trained against | RLHF optimises agreeableness. "Sir, I would not advise that" is exactly what current models will not say. See §4. |
| J7 | **Runs work in parallel** | ✅ Available | Agent village (G2): background probe generation, misconception analysis, next-session planning. |

Two of seven are available today. One is degraded. Four are blocked — and the
blockers are *architectural*, not capability. They will not be fixed by a better
model.

## 3. Latency: the budget is spent before the model runs

Human conversational turn gaps are modally **100–200 ms**; 51–55% land under
200 ms (Levinson & Torreira 2015). Humans achieve this by *predicting* the end of
your sentence — word encoding alone takes ~600 ms, so listening-then-responding
cannot produce it.

Default server VAD is **500 ms silence + 300 ms padding = 800 ms before
inference begins.** The budget is blown before the model is invoked. Moshi
demonstrates the alternative: 160 ms theoretical, ~200 ms practical, full duplex.

For an ADHD learner this is not a polish issue. An 800 ms dead gap after every
utterance is an attention leak on every turn.

## 4. The refusal engine — the component that does not exist

Everything above is infrastructure. This is the pedagogy, and no vendor ships it.

The tutor must continuously decide **answer / ask / wait / pivot / escalate**, and
default to *not answering*. Inputs it must weigh:

- Has the learner attempted? (no attempt ⇒ never answer)
- Is this struggle productive or is it failure? (**mode-dependent — see H1.3: for
  SELPA archetypes this inverts toward explicit instruction**)
- Is this a retrieval opportunity? (recently taught ⇒ ask, don't tell)
- Is frustration approaching the point of harm? (escalate, don't persist)
- Is the current *method* failing, versus the learner failing? (⇒ pivot)

The last one is the bidirectional loop (H1.2) and it is the difference between a
tutor and a search engine. Most AI tutors re-explain the same way with more
words. This one must change **approach**, not volume — and know the difference
between "not yet" and "not this way."

Against this, RLHF-trained agreeableness is an active adversary. The refusal
engine has to be built *over* the model's disposition, not delegated to it.

## 5. What to build first

Ranked by (impact for the target learner) ÷ (blocker difficulty):

1. **State (J4).** Nothing else compounds without it. A single learner model
   every agent reads and writes; inspectable and correctable by learner and
   parent.
2. **The refusal engine (§4).** Pure logic over an existing model. No new
   capability required. Highest pedagogical yield per line of code.
3. **Deixis (J3).** A shared canvas the tutor can point at and annotate via tool
   calls. Removes working-memory load directly — the highest-value accommodation
   in the archetype table.
4. **Proactive probing (J5).** Out-of-band evaluation → the CBM probe loop.
   Available now, nobody uses it.
5. **Session continuity (J1).** Compression + resumption to defeat the 2-minute
   video cap.
6. **Process vision (J2).** Blocked at 1 FPS upstream; work around it with event
   capture (keystrokes, edits, canvas strokes) rather than video.
7. **The face.** Last, and honestly labelled: pedagogical agents measure
   **g ≈ 0.19–0.20**; three 2024 field experiments improved affect (d = .85–1.01)
   while learning *did not move*. Build it for engagement — a real and necessary
   win for an ADHD learner — but do not claim it teaches.

## 6. The one-line spec

> An ambient tutor that sees the work, remembers everything, points at the thing,
> notices you are stuck before you say so, changes its approach when its approach
> is failing — and, most of the time, declines to give you the answer.

---

## 7. Addendum — Wan Streamer changes three of the seven blockers

*Added 2026-07-25 after direct source review. Supersedes the latency and avatar
analysis above where they conflict.*

Sources. Wan-Streamer v0.2, arXiv:2607.04443 (Huang et al., 5 Jul 2026);
Wan Streamer v0.3, https://wan-streamer.com/v0.3/ (16 Jul 2026). Local install
present at `~/wan-streamer` — note this directory is actually **StreamDiffusionV2**
(arXiv:2511.07399, MLSys 2026 Best Paper), a *different* real-time V2V system with
Blackwell support added 2026-05-17. Both are relevant; they are not the same
project.

**Measured figures (v0.2/v0.3):** 640×368 @ **25 FPS**, **~200 ms model-side
signal-to-signal latency**, ~550 ms total remote including 350 ms network.
Architecture: single-GPU *thinker* (perception) + multi-GPU *performer*
(Ulysses-style context parallelism). `MEASURED-BENCH`, author-reported.

### Revisions to §2 and §3

| | Previous finding | Revised |
|---|---|---|
| **Latency** | "Budget blown before the model runs" (800 ms default VAD) | **~200 ms model-side is inside the human turn-gap budget** (modal 100–200 ms; Levinson & Torreira). The 800 ms figure describes *default VAD configuration*, not the achievable floor. |
| **J2 — sees what you see** | Degraded, ≤1 FPS | Applies to Gemini Live / OpenAI Realtime. A dedicated real-time audio-visual stack operates at 25 FPS. |
| **J1 — ambient** | Blocked by 2-min video cap | Vendor-API constraint, not a physical one. A self-hosted stream has no such cap. |

### The v0.3 contribution: world / event-stream decomposition

v0.3 separates the world (scene, characters, appearance, sound — must stay
coherent) from the event stream (speech, motion, camera movement,
environmental change — varies moment to moment). *"Establish the world once,
follow the timeline, and learn what happens next."*

This is the sharpest architectural fit for tutoring in the entire survey:

- **The world is the lesson context** — a lab bench, a workshop, a circuit, a
  kitchen, a farm. Established once, persistent across the session.
- **The event stream is the teaching** — the tutor's speech, gesture, object
  manipulation, and attention shifts, time-aligned within that world.

It also addresses Genie 3's two disqualifying limits for education directly:
persistent world state (vs ~1 minute of visual memory) and legible on-screen text
(v0.2's stated goal is "readable details during real-time conversation").
One of v0.3's own demo categories is "instructional activity."

### What this does *not* fix

Physical correctness is unchanged. VideoPhy (39.6% best case) and VideoPhy-2
(22% on the hard subset) measure generated-video physics adherence, and nothing
in v0.2/v0.3 claims to improve it. **A generated world may be real-time,
persistent, legible, and still wrong about physics** — and photorealism makes
the error more persuasive, not less.

Therefore the A5 conclusion is narrowed rather than withdrawn:

> Generated pixel worlds remain unsuitable as the *authority* for physical law.
> They are now suitable as the *stage* — a persistent, legible, real-time
> environment in which a tutor grounded by verifiable code (G1 ladder) teaches.
> Keep the world generative; keep the physics symbolic.

### Revised build order (supersedes §5)

Deixis (J3) rises to first. In a persistent world at 25 FPS, "point at *this*"
becomes tractable in a way it never was over a 1 FPS still-frame channel — and it
is the highest-value accommodation in the H1 archetype table.

1. **Deixis in a persistent world** — the tutor indicates, annotates, manipulates.
2. **State (J4)** — one learner model beneath it.
3. **The refusal engine (§4)** — unchanged; still the pedagogy.
4. **Proactive probing (J5)** — out-of-band evaluation → CBM loop.
5. **The face** — now cheap to render, still `g ≈ 0.19–0.20`. Build for
   engagement; do not claim it teaches.

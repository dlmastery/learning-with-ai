---
title: "Live, full-duplex multimodal tutoring: video-in/audio-in → video-out/audio-out"
wave: A
section: A4
date_researched: 2026-07-25
sources_count: 48
status: superseded
superseded_by: "research/raw/A4-live-multimodal-frontier-2026-07-25.md"
---

# A4 — Live, full-duplex multimodal tutoring

> **Superseded on 2026-07-25.** This first pass over-centered avatar rendering
> and point-in-time API limits. Use
> [A4 — Live Multimodal Mentorship](A4-live-multimodal-frontier-2026-07-25.md),
> which incorporates GPT-Live full duplex, Gemini 3.5 Live Translate, scoped
> perception, shared artifacts, local continuity, and a complete interaction
> policy. This file remains as a detailed technical source ledger.

**Scope.** What it actually takes, today, to build a tutor that a student can *talk to* while
*showing it something* (paper, screen, whiteboard) and that talks back with a face. Three
layers: (1) the realtime conversational model, (2) the perception channel (camera / screen),
(3) the output channel (voice, and optionally a rendered face). Plus the two questions that
decide whether any of this matters: **latency** and **evidence**.

**Evidence-strength tags used throughout:**
- `[MEASURED]` — a number from a peer-reviewed paper, benchmark, or reproducible artifact
- `[DOCUMENTED]` — a hard spec published in vendor API documentation (verifiable, but vendor-authored)
- `[VENDOR]` — a marketing or blog claim with no independent verification
- `[UNVERIFIED]` — I could not retrieve the source (paywall/403); flagged so it is not treated as fact

---

## 1. The shape of the problem

A "live multimodal tutor" is not one model. It is a loop:

```
student mic ──┐                                    ┌──> synthesized voice
student cam ──┼──> realtime model ──> tool calls ──┤
screen share ─┘      (S2S)                         └──> [optional] avatar renderer ──> video
                          ↑                                        ↑
                    barge-in / VAD                          the expensive part
```

Two vendors ship the middle box as a managed service (Gemini Live, OpenAI Realtime). Nobody
ships the *right-hand* box in a way that is simultaneously local, real-time, and good. That
asymmetry is the central finding of this section.

---

## 2. Gemini Live API

Primary source: <https://ai.google.dev/gemini-api/docs/live>,
<https://ai.google.dev/gemini-api/docs/live-guide>,
<https://ai.google.dev/gemini-api/docs/live-session>,
<https://ai.google.dev/gemini-api/docs/live-tools>,
<https://ai.google.dev/gemini-api/docs/live-api/capabilities>,
<https://ai.google.dev/gemini-api/docs/ephemeral-tokens>

### 2.1 Transport and I/O
- Stateful **WebSocket (WSS)** connection. `[DOCUMENTED]`
- **Input:** "Audio (raw 16-bit PCM audio, 16kHz, little-endian), images (JPEG <= 1FPS), text". `[DOCUMENTED]`
- **Output:** "Audio (raw 16-bit PCM audio, 24kHz, little-endian)". `[DOCUMENTED]`
- Native-audio models **only support the `AUDIO` response modality** — you cannot get text and
  audio out simultaneously; you use the input/output *transcription* feature to get text.
  `[DOCUMENTED]` (<https://ai.google.dev/gemini-api/docs/live-guide>)
- Video is sent as **individual JPEG or PNG frames at a maximum of 1 frame per second**.
  `[DOCUMENTED]` — this is the single most important constraint for teaching (see §4).
- `mediaResolution` low/high setting trades tokens for image detail. `[DOCUMENTED]`

### 2.2 Models (as of 2026-07)
| Model ID | Notes |
|---|---|
| `gemini-3.1-flash-live-preview` | native audio; `thinkingLevel` (minimal/low/medium/high); **sequential (synchronous) function calling only**; turn coverage defaults to audio activity **and all video frames** |
| `gemini-2.5-flash-native-audio-preview-12-2025` | native audio; `thinkingBudget` (token count); **asynchronous function calling** with `NON_BLOCKING`; **proactive audio** (model may decline to respond); **affective dialog** (adapts to user tone) |

`[DOCUMENTED]` — <https://ai.google.dev/gemini-api/docs/live-api/capabilities>

### 2.3 Session limits — the tutoring blocker
- **Audio-only sessions: limited to 15 minutes.** `[DOCUMENTED]`
- **Audio + video sessions: limited to 2 minutes.** `[DOCUMENTED]`
- Underlying **connection lifetime ≈ 10 minutes** before termination. `[DOCUMENTED]`
- **Context window:** 128k tokens for native-audio output models; 32k for other Live models. `[DOCUMENTED]`
- **`contextWindowCompression`** (sliding window) "allows sessions to run indefinitely by
  compressing the context when token thresholds are reached". `[DOCUMENTED]`
- **`sessionResumption`** issues `SessionResumptionUpdate` handles "valid for 2 hr after the
  last session's termination", letting one logical session span many connections. `[DOCUMENTED]`
- **`GoAway`** message with `timeLeft` warns before disconnection; `generationComplete` marks
  end of a model turn. `[DOCUMENTED]`

> **Implication:** a 45-minute tutoring session with the camera on is *not* a supported
> primitive. It is something you build out of compression + resumption + reconnect glue.
> Any product claim of "hour-long live video tutoring" on raw Gemini Live is an
> engineering claim about the wrapper, not the API.

### 2.4 Turn-taking, VAD and barge-in
- "Users can interrupt the model at any time for responsive interactions." `[DOCUMENTED]`
- On interruption, "the ongoing generation is canceled and discarded. **Only the information
  already sent to the client is retained in the session history.**" `[DOCUMENTED]` — i.e. the
  model's memory of what it said matches what the student actually heard. This is correct
  behaviour and non-trivial; it is what makes barge-in pedagogically safe.
- Automatic VAD is configurable: `start_of_speech_sensitivity`, `end_of_speech_sensitivity`,
  `prefix_padding_ms`, `silence_duration_ms`. Docs recommend **500–800 ms** thresholds "for
  balanced latency and quality". `[DOCUMENTED]`
- Manual mode: set `automaticActivityDetection.disabled = true` and send explicit
  `activityStart` / `activityEnd` — i.e. push-to-talk, useful in noisy classrooms. `[DOCUMENTED]`
- Gemini 3.1 changes the streaming contract: `send_client_content` only works for initial
  context (with `initial_history_in_client_content`); ongoing updates must use
  `send_realtime_input`. `[DOCUMENTED]`

### 2.5 Tools during a live session
| Tool | 3.1 Flash Live | 2.5 Flash Live |
|---|---|---|
| Google Search grounding | ✅ | ✅ |
| Function calling | ✅ (synchronous only) | ✅ (sync + async / `NON_BLOCKING`) |
| Google Maps | ❌ | ❌ |
| **Code execution** | ❌ | ❌ |
| URL context | ❌ | ❌ |

`[DOCUMENTED]` — <https://ai.google.dev/gemini-api/docs/live-tools>. Also: "unlike the
`generateContent` API, the Live API doesn't support automatic tool response handling" — you
must marshal tool results yourself.

> **Implication for teaching:** *no code execution inside the live session.* A tutor that
> wants to run the student's Python must call out to your own sandbox via function calling.
> That is fine, but it means the "watch me run your code" affordance is your problem.

### 2.6 Voices, languages, auth
- **97 supported languages** with BCP-47 codes. `[DOCUMENTED]`
- Native audio output models "support any of the voices available for our Text-to-Speech (TTS)
  models" (e.g. `Kore`). `[DOCUMENTED]`
- "Live Translation: real-time voice-to-voice translation in 70+ languages." `[VENDOR]`
- **Ephemeral tokens** for browser-direct connections: `expireTime` default 30 min,
  `newSessionExpireTime` default 1 min, `uses` default 1 (single session). Recommended
  architecture is client→your backend→token→client connects directly to Live API,
  "avoiding backend proxy overhead for real-time data". `[DOCUMENTED]`

### 2.7 Pricing (paid tier)
From <https://ai.google.dev/gemini-api/docs/pricing> `[DOCUMENTED]`:

| Model | Input | Output |
|---|---|---|
| Gemini 3.1 Flash Live Preview | $0.75 /M text; **$3.00 /M audio (≈$0.005/min)** | $4.50 /M text; **$12.00 /M audio (≈$0.018/min)** |
| Gemini 2.5 Flash Native Audio | $0.50 /M text; $3.00 /M audio **or video** | $2.00 /M text; $12.00 /M audio |
| Gemini 3.5 Live Translate | $3.50 /M audio (≈$0.0053/min) | $21.00 /M audio (≈$0.0315/min) |

Audio is billed at **25 tokens per second of audio**. Free tier exists for preview access.

**Rough tutoring economics (Gemini 3.1 Flash Live):** ~$0.005/min in + ~$0.018/min out. If the
tutor talks ~40% of the time, a 45-minute session ≈ $0.22 in + ~$0.32 out ≈ **$0.55/session**
before video frames. Video frames at 1 FPS on the 2.5 native-audio model bill at the $3.00/M
"audio/video" input rate — non-trivial but not dominant.

*Not found:* published concurrent-session / QPS limits for Live models. The rate-limits page
defers to the AI Studio dashboard. `[UNVERIFIED]`

---

## 3. OpenAI Realtime API

Primary source: <https://developers.openai.com/api/docs/guides/realtime> (the
`platform.openai.com/docs/guides/realtime` URL 301s here),
<https://developers.openai.com/api/docs/guides/realtime-conversations>,
<https://developers.openai.com/api/docs/guides/realtime-webrtc>,
<https://developers.openai.com/api/docs/api-reference/realtime-sessions>,
<https://developers.openai.com/api/docs/pricing>

### 3.1 Transports — three, not one
- **WebRTC** — "Use for browser and mobile clients that capture or play audio directly."
  Explicitly recommended over WebSockets from the client "for more consistent performance". `[DOCUMENTED]`
- **WebSocket** — "Use when your server already receives raw audio from a media pipeline." `[DOCUMENTED]`
- **SIP** — telephony. `[DOCUMENTED]`

This is a real architectural advantage over Gemini Live (WSS only): WebRTC brings jitter
buffering, packet loss concealment, echo cancellation and adaptive bitrate for free, which is
exactly what a kid on a phone on school wifi needs.

Connection flow: either the unified interface (browser SDP → your server → `POST
https://api.openai.com/v1/realtime/calls` with a standard key → SDP answer), or ephemeral
tokens from `POST /v1/realtime/client_secrets`. An `OpenAI-Safety-Identifier` header is
recommended for per-user attribution. `[DOCUMENTED]`

### 3.2 Models
| Model ID | Context | Notes |
|---|---|---|
| `gpt-realtime-2` / `gpt-realtime-2.1` | **128k** | "think before it speaks"; `reasoning.effort` ∈ {minimal, low, medium, high, xhigh}; docs advise starting at `low` |
| `gpt-realtime-1.5` | **32k** | fast non-reasoning S2S |
| `gpt-realtime-2.1-mini` | — | cheap tier |
| `gpt-realtime-translate` | — | dedicated translation endpoint, continuous (no `response.create` needed) |
| `gpt-realtime-whisper` | — | transcription only, "controllable latency" |

`[DOCUMENTED]`. Note the docs pages and the pricing page disagree slightly on suffixes
(`gpt-realtime-2` vs `gpt-realtime-2.1`); treat the exact string as version-churny.

### 3.3 Turn detection — more knobs than Gemini
From the session API reference `[DOCUMENTED]`:
- `server_vad`: `threshold` 0.0–1.0 (**default 0.5**), `prefix_padding_ms` (**default 300**),
  `silence_duration_ms` (**default 500**), `create_response`, `interrupt_response`,
  `idle_timeout_ms` (5000–30000).
- `semantic_vad` (**enabled by default** per the conversations guide): `eagerness` ∈
  {low, medium, high, auto} with **max timeouts of 8 s, 4 s, 2 s** respectively. This is a
  *model-based* end-of-turn predictor rather than a silence timer — meaningfully better for
  learners who pause mid-thought.
- `turn_detection: null` → manual: `input_audio_buffer.commit` + `response.create`.
- Keep VAD but suppress auto-response: set `turn_detection.create_response` and
  `interrupt_response` to `false`.
- `max_output_tokens`: 1–4096 per response (inclusive of tool calls), default `"inf"`.

### 3.4 Interruption
- **WebRTC/SIP:** "the server automatically truncates unplayed audio upon detecting new speech"
  via `input_audio_buffer.speech_started`. `[DOCUMENTED]`
- **WebSocket:** the *client* must stop playback and send `conversation.item.truncate` with the
  item ID and `audio_end_ms`. The docs concede: "The realtime model doesn't have enough
  information to precisely align transcript and audio." `[DOCUMENTED]`

> This is a subtle correctness bug factory for tutoring: if truncation is sloppy, the model
> believes it explained step 3 when the student only heard step 2. Gemini's "only information
> already sent to the client is retained" rule is cleaner; OpenAI's WebRTC path matches it,
> the WebSocket path does not.

### 3.5 Vision in a realtime session
- **Images: yes.** `conversation.item.create` with content type `input_image` and a base64
  data URL (`"image_url": "data:image/{format};base64,{base64Image}"`). `[DOCUMENTED]`
- **Video: not documented as a native input.** You send frames as images at whatever rate you
  can afford. `[DOCUMENTED]` (absence-of-spec, so treat as "roll your own").
- Image tokens are separately priced ($5.00/M for `gpt-realtime-2.1`), confirming vision is a
  first-class billed input. `[DOCUMENTED]`

### 3.6 Other
- **MCP server integration is supported** in realtime sessions, plus ordinary function calling. `[DOCUMENTED]`
- **Out-of-band responses:** `response.create` with `"conversation": "none"` runs a generation
  that does *not* enter the conversation, with a `metadata` field to correlate. This is a
  genuinely useful teaching primitive — you can run a silent "is the student stuck?" classifier
  off the same audio stream without polluting the dialogue. `[DOCUMENTED]`
- Audio formats: PCM (24 kHz shown in examples; transcription sessions state "Only a 24kHz
  sample rate is supported"), plus PCMU (μ-law) for telephony. `[DOCUMENTED]`
- **Max session duration is not documented** on any page I could retrieve. `[UNVERIFIED]`

### 3.7 Pricing (per 1M tokens)
`[DOCUMENTED]` — <https://developers.openai.com/api/docs/pricing>

| Model | Audio in | Audio cached | Audio out | Text in | Text out | Image in |
|---|---|---|---|---|---|---|
| `gpt-realtime-2.1` | $32.00 | $0.40 | $64.00 | $4.00 | $24.00 | $5.00 |
| `gpt-realtime-2.1-mini` | $10.00 | $0.30 | $20.00 | $0.60 | $2.40 | $0.80 |
| `gpt-realtime-translate` | $0.034/min | — | — | — | — | — |
| `gpt-realtime-whisper` | $0.017/min | — | — | — | — | — |

---

## 4. Head-to-head

| | **Gemini Live API** | **OpenAI Realtime API** |
|---|---|---|
| Transport | WebSocket (WSS) only | **WebRTC**, WebSocket, SIP |
| Audio in | 16-bit PCM, **16 kHz** | PCM (24 kHz), PCMU |
| Audio out | 16-bit PCM, **24 kHz** | PCM 24 kHz |
| Video/vision in | **JPEG/PNG frames, ≤ 1 FPS**, `mediaResolution` low/high | `input_image` items (base64 data URL); no documented native video |
| Text + audio out together | ❌ (audio-only modality; use transcription) | ✅ modalities configurable |
| Context window | 128k (native audio) / 32k | 128k (`gpt-realtime-2`) / 32k (`1.5`) |
| **Session limit** | **15 min audio-only; 2 min audio+video**; conn ≈10 min | not documented |
| Long sessions | `contextWindowCompression` (indefinite) + `sessionResumption` (2 h handles) | truncation config; auto-drops oldest items |
| End-of-turn | configurable VAD (sensitivity, `prefix_padding_ms`, `silence_duration_ms`; 500–800 ms recommended); manual `activityStart/End` | `server_vad` (thr 0.5, pad 300 ms, silence 500 ms, idle 5–30 s) **or `semantic_vad`** (eagerness low/med/high → 8/4/2 s caps) |
| Barge-in | yes; discarded generation is dropped from history | yes; auto-truncate on WebRTC, **manual `conversation.item.truncate` on WebSocket** |
| Tools in-session | function calling (3.1 sync-only, 2.5 async), Google Search. **No code exec, no URL context, no Maps** | function calling + **MCP servers** |
| Silent side-channel | — | **out-of-band responses** (`conversation: "none"`) |
| Reasoning control | `thinkingLevel` (3.1) / `thinkingBudget` (2.5) | `reasoning.effort` minimal→xhigh |
| Affect | **affective dialog**, **proactive audio** (2.5) | not documented as a named feature |
| Languages | **97** | not enumerated in fetched docs |
| Client auth | ephemeral tokens (30 min, 1 use) | ephemeral client secrets |
| Audio out price | **$12/M (~$0.018/min)** | $64/M (`2.1`), $20/M (`mini`) |

**Blunt read.** Gemini Live is ~3–5× cheaper on audio and has the better language coverage and
the more explicit affect features. OpenAI Realtime has the better *transport* story (WebRTC),
the better *turn-taking* story (semantic VAD), MCP, and out-of-band responses. Gemini's 2-minute
audio+video session cap is the sharpest single constraint in this whole section; OpenAI's lack
of documented video makes "show me your homework" a client-side frame-sampling exercise on
either platform.

---

## 5. What each can actually do *for teaching*

### 5.1 Can it see the student's work?
**Yes, but at 1 frame per second or slower, and as stills, not video.** `[DOCUMENTED]`

Practical consequences:
- **Camera on paper:** works. A worked math problem is a static artifact; 1 FPS is plenty.
  This is the strongest live-vision use case in education and it is available *today* on both
  platforms.
- **Screen share of code:** works, and is well matched to 1 FPS — code changes slowly.
  Gemini's consumer app explicitly supports screen sharing ("share and get help with what's on
  your device's screen… your full screen is shared with Gemini") and camera with front/rear
  switching; both auto-disable when Live is on hold or the screen locks.
  `[DOCUMENTED]` — <https://support.google.com/gemini/answer/15274899>
- **Watching a *process*** — a student's pen moving, a physics demo, a lab technique, a
  gymnastic movement, sign language — **does not work.** 1 FPS discards exactly the
  information that makes procedural feedback possible. Anyone claiming "the AI watches how you
  solve it" is over-claiming; it watches *snapshots* of the result.
- Gemini 3.1's turn coverage defaults to "audio activity **and all video frames**" while 2.5
  defaults to "detected activity only" `[DOCUMENTED]` — meaning 3.1 keeps looking even during
  silence. For a tutor watching a student work quietly, 3.1 is the right default (and the more
  expensive one).

### 5.2 Can it be interrupted?
**Yes on both, and this is the single most important pedagogical affordance.** A tutor that
cannot be stopped mid-explanation is a lecture. Both APIs cancel generation on detected user
speech. Gemini additionally guarantees the model's transcript matches what was actually heard;
OpenAI guarantees this on WebRTC but pushes the burden to the client on WebSocket. `[DOCUMENTED]`

### 5.3 Can it interrupt *the student*?
**Not really, and no vendor exposes it as a primitive.** Gemini 2.5's *proactive audio* — the
model "can decline to respond" — is the inverse capability (restraint, not initiative).
`[DOCUMENTED]` A tutor that catches an error the moment it appears would need to (a) run
continuous vision, (b) decide to barge in, (c) emit audio over the student. You can approximate
this with OpenAI out-of-band responses driving a client-side `response.create`, but it is a
build, not a feature. **This is a genuine product gap.**

### 5.4 Can it point at things or draw?
**No.** Neither API has any output channel other than audio (+ optional text transcript) and
tool calls. There is no cursor, no annotation, no overlay, no "highlight line 12" primitive.

The only route is: model calls *your* function (`highlight(region)`, `draw_arrow(x,y)`), and
your client renders it. That works and is the correct architecture, but it means:
- The model must reason about **coordinates in an image it saw at ≤1 FPS**, which is brittle.
- Deixis ("*this* term", "*that* bracket") — one of the most powerful things a human tutor does
  — is entirely on you to reconstruct.

This is, in my view, the largest unexploited design space in live AI tutoring: the models can
already see and talk; nobody has built a good shared-pointing surface.

### 5.5 Can it run the student's code?
Gemini Live: **no code execution tool in-session** `[DOCUMENTED]`. OpenAI Realtime: no built-in
interpreter either, but **MCP support** means you can wire a sandbox in with much less glue.
Advantage OpenAI.

---

## 6. Avatar / talking-head generation for tutors

### 6.1 The hosted vendors
I was **unable to retrieve technical specs from HeyGen, D-ID or Synthesia** — their doc sites
returned 403/404 to automated fetches, and `heygen.com/interactive-avatar` now **301-redirects
to `liveavatar.com`**, which also 403s. `[UNVERIFIED]` Everything I can honestly report:

- **HeyGen** has repositioned its interactive-avatar product onto a separate `liveavatar.com`
  property and is mid-migration to a v3 API (docs.heygen.com now serves mainly a v3 migration
  notice pointing at developers.heygen.com). `[DOCUMENTED]` (the redirect and migration notice
  are directly observable)
- **D-ID** lists "Agents" as "Interactive, realtime avatars with knowledge and skills for
  customer engagement" on its API docs landing page. `[VENDOR]`
  <https://docs.d-id.com/reference/get-started>
- **Synthesia** — no interactive-avatar page retrievable at the obvious URL. `[UNVERIFIED]`

**Do not put vendor latency numbers in the survey without re-verifying them from a live page.**
Every "sub-second avatar" claim I have seen in this space is marketing copy. Treat as `[VENDOR]`
until measured.

### 6.2 The open stack — what actually exists

| System | Year | Speed claim | Hardware | License / stars |
|---|---|---|---|---|
| **SadTalker** (arXiv:2211.12194) | CVPR'23 | not real-time | — | 13,971★, last push 2024-06 (**dormant**) |
| **LivePortrait** (arXiv:2407.03168) | 2024 | **"12.8 ms on an RTX 4090 GPU with PyTorch"** `[MEASURED]` | RTX 4090 | 18,808★ (repo now `KlingAIResearch/LivePortrait`) |
| **MuseTalk** (arXiv:2410.10122) | 2024 | **"30 FPS output at 256×256 on an NVIDIA V100"** `[MEASURED]` | V100 | 6,237★ |
| **Hallo** (arXiv:2406.08801) / **Hallo2** | 2024/ICLR'25 | diffusion; not real-time | — | 8,660★ / 3,726★, MIT |
| **EchoMimic** (arXiv:2407.08136) / **v2** | AAAI'25 / CVPR'25 | not real-time | — | 4,273★ / 4,621★, Apache-2.0 |
| **Ditto** (arXiv:2411.19509) | ACM MM'25 | "streaming processing, real-time inference, and **low first-frame delay**" `[MEASURED]` | A100 + TensorRT 8.6 | 842★, Apache-2.0 |
| **VASA-1** (arXiv:2404.10667) | 2024 | **"512×512 at up to 40 FPS with negligible starting latency"** `[MEASURED]` | — | **no code released** |
| **FLOAT** (arXiv:2412.01064) | 2024 | flow matching, fast sampling | — | — |
| **Loopy** (arXiv:2409.02634), **Sonic** (arXiv:2411.16331), **EMO** (arXiv:2402.17485), **OmniHuman-1** (arXiv:2502.01061) | 2024–25 | quality-first, offline | — | mostly closed |
| **SoulX-FlashHead** | 2026 | **Lite: 96 FPS, or 3 concurrent real-time (25+ FPS) streams on a single RTX 4090. Pro: 10.8 FPS on one 4090; real-time on two RTX 5090 (with SageAttention)** `[MEASURED]` | 4090 / 2×5090 | 925★, 1.3B params |
| **LiveTalking** | active (push 2026-07-19) | integration layer: ernerf/musetalk/wav2lip/Ultralight; **WebRTC, RTMP, virtual-camera out; supports interruption; multi-concurrency** `[DOCUMENTED]` | — | 8,499★, Apache-2.0 |
| **OpenAvatarChat** | v0.6.0, 2026-04 | **"平均响应时间仅 2.2 秒" — average response time 2.2 s** `[VENDOR]` (project self-report) | — | 3,646★, Apache-2.0 |

**The dividing line is architectural, not incremental.** Implicit-keypoint / warping models
(LivePortrait) and latent-inpainting models (MuseTalk) run at video rates on one consumer GPU.
Diffusion-video models (Hallo, EchoMimic, EMO, OmniHuman, Wan-S2V) do not, and no amount of
optimization has closed that gap for full-frame generation — the 2026 answer (SoulX-FlashHead,
Ditto) is to shrink to ~1.3B params and stream in motion space, not pixel space.

### 6.3 Wan-family and LTX — where the user's own tooling sits

**Wan 2.2 S2V** (`Wan2.2-S2V-14B`, arXiv:2508.18621 "Wan-S2V: Audio-Driven Cinematic Video
Generation"): supports 480P & 720P, audio-driven, optional `--pose_video` for pose-driven
generation, and CosyVoice TTS integration since 2025-09-05. `[DOCUMENTED]`

The decisive number from the official repo: **"This command can run on a GPU with at least
80GB VRAM"** for single-GPU S2V inference (even *with* `--offload_model True
--convert_model_dtype`). `[DOCUMENTED]` And for context on the *fast* member of the family:
**TI2V-5B "can generate a 5-second 720P video in under 9 minutes on a single consumer-grade
GPU"** `[DOCUMENTED]`.

> **9 minutes for 5 seconds is ~108× slower than real time.** Wan 2.2 S2V is a *production*
> tool for pre-rendered lesson video. It is categorically not a live-tutor renderer, and no
> local hardware short of a multi-GPU H100 node changes that.

**LTX-2 / LTX-2.3** (`Lightricks/LTX-2`, 10,747★ on the predecessor repo): a 22B DiT
audio-video foundation model, native 4K, up to 50 fps, synchronized audio, clips up to 10 s.
`[VENDOR]`/`[DOCUMENTED]` Relevant pieces for tutoring avatars:
- **`A2VidPipelineTwoStage`** — audio-to-video generation conditioned on an input audio file. `[DOCUMENTED]`
- **`LTX-2.3-22b-IC-LoRA-LipDub`** — a lip-dubbing IC-LoRA. `[DOCUMENTED]`
- The *predecessor* LTX-Video shipped distilled checkpoints described as **"real time on H100
  with the distilled model"** at 1216×704 / 30 FPS, and a 2B distilled variant "15× faster,
  real-time capable". `[VENDOR]` (repo README)

So LTX's real-time claims are (a) about the older, smaller models and (b) anchored on H100.
LTX-2.3's 22B model is a quality play. **The LipDub IC-LoRA is the interesting artifact**: it
is the one piece of the Wan/LTX world that plausibly slots into a tutoring pipeline, as a
post-hoc lip-sync pass over pre-rendered instructor footage — not as a live renderer.

### 6.4 The user's `face-swap-streamer` — an underrated asset

`gh api repos/dlmastery/face-swap-streamer` `[MEASURED]` (direct inspection):
- Flask web app + **HLS live streaming with synchronized audio** + TensorRT-accelerated
  InsightFace `inswapper_128_fp16`, GFPGAN restoration, 1- or 2-source face matching.
- **4-stage thread pipeline** (reader → detect → swap → ffmpeg writer), `Q_DEPTH=128`.
- Measured throughput: **"RTX 4090 hits 8–13 fps on 1080p, 18–25 fps on 480p with TensorRT"**;
  the `webapp_mp.py` multiprocess variant reaches **33 fps at 1080p** with 6 workers at
  `FACESWAP_DET_SIZE=480`, saturating the GPU at 87–95% SM utilisation (10 GB VRAM vs 3 GB
  single-process).
- Streams **while processing** — the viewer sees HLS segments before the job finishes — then
  remuxes `.ts` → faststart MP4 in a ~5 s second pass.
- Also contains a **C++ CLI reimplementation** (`cli/` with ONNX Runtime session, face
  analyser, pipeline) and a Next.js `web/` front end.

**Why this matters for the survey.** The hard parts of a live avatar tutor are not the face
model — they are (1) a frame pipeline that keeps a GPU saturated, (2) muxing generated frames
to a live transport with audio in sync, (3) a viewer that starts playing before generation
finishes. This repo already solves all three at 33 fps/1080p on a 4090. Swapping the
`inswapper` stage for a **LivePortrait (12.8 ms/frame) or SoulX-FlashHead-Lite (96 FPS)** stage
is a plausible path to a genuinely local real-time tutor avatar. The main change needed is
**transport**: HLS carries multi-second latency by design; a real tutor needs WebRTC (which is
exactly what LiveTalking and OpenAvatarChat use).

---

## 7. Latency budgets

### 7.1 What humans actually do

The canonical numbers, from Levinson & Torreira (2015), *Frontiers in Psychology* 6:731,
doi:10.3389/fpsyg.2015.00731 `[MEASURED]`
(<https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.00731/full>):

- **Modal floor-transfer offset (FTO): 100–200 ms.**
- **"The majority (51–55%) of all turn transitions across corpora take place in under 200 ms."**
- Mean gap **236–468 ms** across languages; median **264–347 ms** in telephone corpora.
- Cross-linguistic range of average FTOs: **−78 ms (Dutch) to 468 ms (Danish)** — "mean values
  vary… roughly a quarter of a second either side of the cross-linguistic mean."
- Modal overlap **< 50 ms**; simultaneous speech is "less than 5% of the spoken signal."
- **This is faster than language production.** Encoding a single word takes ~**600 ms** from
  stimulus to speech onset; two nouns **740–800 ms**; three words **900 ms**; a complex
  sentence "**about 1500 ms** before speech output begins." Inhalation alone is "typically over
  500 ms" plus 140–320 ms neural transmission.

The inescapable conclusion — and the one that should anchor any engineering target — is that
**humans hit 200 ms gaps by predicting the end of your turn and pre-planning their response
during your speech, not by responding fast after you stop.**

Corroborating cross-linguistic work: Stivers et al. (2009), *PNAS* 106(26),
doi:10.1073/pnas.0903616106 `[MEASURED]` — 10 languages; "robust human universals in this
domain, where local variations are quantitative only."

### 7.2 What that means for a tutor's latency budget

Decompose the round trip:

```
student stops speaking
  → endpoint detection        [server_vad silence_duration_ms = 500 ms by DEFAULT]
  → network to model          [50–150 ms typical]
  → model first audio token   [??? — not published by either vendor]
  → network back              [50–150 ms]
  → jitter buffer + playout   [50–200 ms]
  [→ avatar render + encode]  [+16–120 ms if a face is in the loop]
```

**Key finding: the default VAD configuration alone (500 ms silence timer + 300 ms prefix
padding) already exceeds the human modal gap by 2.5–5× before the model has done any work.**
`[DOCUMENTED]` This is why every good voice-AI system is really a *turn-prediction* system.
OpenAI's `semantic_vad` with `eagerness: high` (2 s cap) is the closest thing to Levinson's
"predict the turn end" mechanism that either vendor ships; Gemini's tunable
`end_of_speech_sensitivity` is the analogue.

**Neither vendor publishes an end-to-end latency number.** I found no ms figure in any Gemini
Live or OpenAI Realtime doc page fetched for this section. `[UNVERIFIED]` Any latency figure in
the survey must therefore come from an academic system or your own measurement.

### 7.3 What systems achieve

- **Moshi** (arXiv:2410.00037, Kyutai; 10,722★ Apache-2.0): "the first real-time full-duplex
  spoken large language model, with a **theoretical latency of 160 ms, 200 ms in practice**."
  `[MEASURED]` This is the reference point — it lands squarely inside the human modal gap, and
  it does so by modelling the user's stream and its own stream *in parallel*, "allowing for the
  removal of explicit speaker turns, and the modeling of arbitrary conversational dynamics."
  Moshi is the architectural answer to the endpointing problem, not a faster pipeline.
- Moshi's own framing of the alternative: cascaded VAD→ASR→LLM→TTS pipelines have "a latency of
  several seconds between interactions." `[MEASURED]`
- **OpenAvatarChat** (avatar in the loop): **"average response time 2.2 s"**. `[VENDOR]`
- Open full-duplex/omni line of work for the survey's related-work: **LLaMA-Omni**
  (arXiv:2409.06666), **Mini-Omni** (arXiv:2408.16725), **Mini-Omni2** (arXiv:2410.11190,
  vision+speech+duplex), **Qwen2.5-Omni** (arXiv:2503.20215, block-wise streaming encoders,
  TMRoPE time-aligned multimodal position embedding for audio/video sync).

### 7.4 Proposed budget for a live tutor

| Target | Budget | Verdict |
|---|---|---|
| Human-parity | ≤ 250 ms | Only Moshi-class full-duplex architectures. Not achievable on current hosted APIs with default VAD. |
| "Feels natural" | 300–800 ms | Achievable: WebRTC transport + aggressive semantic VAD + no avatar. |
| "Acceptable tutor" | 800–1500 ms | Comfortably achievable, incl. a real-time avatar (LivePortrait/SoulX-Lite class). |
| "Annoying" | > 2 s | Where the current open avatar stacks (OpenAvatarChat 2.2 s) sit. |
| Broken | > 3 s | Cascaded pipelines + diffusion avatars. |

Note the pedagogical wrinkle: **a tutor is one context where a longer gap is defensible.**
Levinson's data says >700 ms silence is socially marked — but in tutoring, marked silence is
often *correct* (wait time). The literature on teacher wait-time suggests deliberate pauses aid
thinking. The design goal is therefore **controllable** latency, not minimal latency: fast for
acknowledgement, slow for "think about it."

---

## 8. The evidence question: does a face help?

This is where the vendor story and the literature diverge most sharply. Report honestly.

### 8.1 Meta-analytic effect sizes

| Study | Scope | Effect |
|---|---|---|
| **Schroeder, Adesope & Gilbert (2013)**, *J. Educ. Computing Research* 49(1), doi:10.2190/EC.49.1.a | 43 studies, 3,088 participants | "a **small but significant** effect on learning" — **g = 0.19** |
| **Castro-Alonso, Wong, Adesope & Paas (2021)**, *Educ. Psychol. Rev.*, doi:10.1007/s10648-020-09587-1 | multimedia pedagogical agents | **g = 0.20**; "students may be able to learn **similarly from different types of agents**" |
| **Do Generative AI-Powered Pedagogical Agents Improve Learners' Academic Performance?** (2025), *JECR*, doi:10.1177/07356331251400540 | 27 studies, 2015–2025 | **g = 0.401**; multimodal dialogue moderated highest; **no moderation** by grade level, gender, domain, duration, or agent role |
| **GAICA systematic review + meta-analysis** (2025 preprint), doi:10.31124/advance.175136285.53256239/v1 | 27 studies 2022–2025 | cognitive **g = 0.357**, non-cognitive **g = 0.519** |

`[MEASURED]` for the two 2025 items (abstracts retrieved via Crossref).
`[MEASURED, secondary]` for Schroeder 2013 (g = 0.19) and Castro-Alonso 2021 (g = 0.20) — I
recovered these figures from a citation context in a citing paper via the Semantic Scholar
citations API, not from the paywalled originals. Verify before publication.

**Read carefully.** g ≈ 0.2 is a *small* effect — roughly the size you would get from a modestly
better worked example. And Schroeder's own moderator analysis is awkward for the avatar
industry: agents helped **K-12 more than post-secondary** students, and — critically — **agents
that communicated via on-screen text facilitated learning more effectively than agents that
communicated using narration**. `[MEASURED, via S2 tldr]` That is the opposite of the
voice-first, face-first product direction.

The 2025 GenAI-agent numbers are larger (g ≈ 0.4), but note the confound: those studies compare
*a GenAI tutor* to *no tutor / business as usual*, not *an agent with a face* to *the same agent
without a face*. **They measure the value of the LLM, not the value of the avatar.**

### 8.2 The strongest pro-embodiment result

**Mayer & DaPra (2012)**, "An embodiment effect in computer-based learning with animated
pedagogical agents," *J. Exp. Psychol.: Applied*, doi:10.1037/a0028616 `[MEASURED]`, 296 cites.
Three experiments; students viewed a 4-min narrated presentation on solar cells with an agent
beside 11 slides. **"Learners performed better on a transfer test when a human-voiced agent
displayed human-like gestures, facial expression, eye gaze, and body movement than when the
agent did not, yielding an embodiment effect."**

This is the real result, and it is important — but read what it says: **the contrast is
gesturing agent vs. static agent, not agent vs. no agent.** It supports "if you show a face,
make it move and gesture." It does not establish that showing a face beats voice alone.

### 8.3 The evidence *against* — instructor presence

**Instructor presence in instructional videos in higher education: three field experiments in
university courses** (2024), *ETR&D*, doi:10.1007/s11423-024-10391-9 `[MEASURED]` — abstract
retrieved in full. Three field studies with real, exam-relevant, >30-min videos taught by a
personally known instructor:

> "The results of these studies show positive effects of a visible instructor compared to no
> visible instructor on **some affective measures**: social presence in Study 1 (n = 18, d = .85)
> and well-being in Study 3 (n = 38, d = 1.01), but not on others… **They also show no effects
> on extraneous processing or learning outcomes (Studies 1–3).** Thus, **no general effect of
> instructor presence can be shown** for instructional videos embedded in university courses…
> but there are also no detrimental effects."

This is the cleanest statement of the honest position: **a face reliably makes learners feel
better and does not reliably make them learn more.** Related reviews: Henderson & Schroeder
(2021), "A Systematic Review of Instructor Presence in Instructional Videos: Effects on
Learning and Affect," *Computers and Education Open*, doi:10.1016/j.caeo.2021.100059 (69 cites,
gold OA — **I could not retrieve the abstract; do not cite specifics** `[UNVERIFIED]`); and
"Instructors' presence in instructional videos: A systematic review" (2022), *Educ. Inf.
Technol.*, doi:10.1007/s10639-022-11532-4.

### 8.4 The voice question, and the uncanny valley

- **Craig & Schroeder (2017)**, "Reconsidering the voice effect when learning from a virtual
  human," *Computers & Education*, doi:10.1016/j.compedu.2017.07.003, 133 cites `[MEASURED —
  metadata only, abstract not retrieved]`. The paper is the standard citation for the claim
  that Mayer's classic *voice principle* (human voice > machine voice) does not survive contact
  with modern TTS. Given 2026 native-audio models, this matters: **synthetic voice is no longer
  a penalty**, which removes one historical argument for recording a real human.
- **Uncanny valley** remains a live risk as avatar realism rises. Seyama & Nagayama (2007),
  "The Uncanny Valley: Effect of Realism on the Impression of Artificial Human Faces,"
  *Presence* 16(4), doi:10.1162/pres.16.4.337 (476 cites) `[MEASURED]`; MacDorman & Chattopadhyay
  (2016), doi:10.1016/j.cognition.2015.09.019 (228 cites) — **"reducing consistency in human
  realism increases the uncanny valley effect"** `[MEASURED]`. That last finding is directly
  actionable for lip-sync avatars: a photoreal face with slightly-off mouth motion is
  *consistency-inconsistent* and therefore worse than a stylized face with the same mouth
  motion. **Cartoon-quality avatars may be the correct engineering choice, not a compromise.**
- Also: "How Human is Too Human? Uncanny Valley Effects of Pedagogical Agents in STEM Learning
  Environments" (2025 preprint), doi:10.31124/advance.175671765.54967058/v1.

### 8.5 Honest bottom line

1. Pedagogical agents produce **small** average learning gains (**g ≈ 0.19–0.20** across two
   independent pre-GenAI meta-analyses).
2. Where agents help, the effect is largest for **K-12**, and (Schroeder 2013) **text-based**
   agent communication outperformed **narrated** agent communication — a direct contradiction
   of the voice-and-face product thesis.
3. Embodiment/gesture helps **relative to a static agent** (Mayer & DaPra 2012), which is an
   argument about *how* to animate, not *whether* to show a face.
4. Realistic field experiments with real courses find **affective benefits (d ≈ 0.85–1.01 on
   social presence and well-being) and no learning benefit.**
5. The large 2025 GenAI-agent effects (g ≈ 0.36–0.40) are **about the tutor, not the avatar.**
6. Therefore: **build the face for engagement, retention and rapport — and say so.** Do not
   claim it improves learning. The defensible claim is that a face improves *social presence
   and willingness to keep going*, and that persistence is itself a learning input.

---

## 9. Synthesis — what I'd tell someone building this

**The realtime layer is solved and cheap.** Gemini Live at ~$0.018/min of model speech makes a
45-min tutoring session cost under a dollar. Use OpenAI Realtime if you need WebRTC robustness,
MCP tools, or semantic VAD; use Gemini Live if you need cost, 97 languages, or affective
dialog. Both.

**The vision layer is the honest constraint.** 1 FPS stills. Excellent for paper and code,
useless for process. Gemini's 2-minute audio+video session cap is the sharpest edge in the
whole stack and requires `contextWindowCompression` + `sessionResumption` plumbing to hide.

**The pointing layer does not exist.** No vendor gives you deixis. Everyone who builds a good
one will have an advantage, and it is buildable today with function calling + a client canvas.

**The avatar layer is a fork in the road.**
- *Real-time local, today:* LivePortrait (12.8 ms/frame, 4090), SoulX-FlashHead-Lite (96 FPS or
  3 concurrent 25-FPS streams on one 4090), MuseTalk (30 FPS @ 256² on V100), Ditto
  (streaming, low first-frame delay). Wire through LiveTalking (WebRTC/RTMP, supports
  interruption, multi-concurrency) or the user's own `face-swap-streamer` pipeline with the
  swap stage replaced and HLS swapped for WebRTC.
- *Not real-time, ever, locally:* Wan 2.2 S2V (≥80 GB VRAM), LTX-2.3 22B, and the whole
  diffusion-video family. These are **pre-render** tools. Use them for canned lesson segments
  and for the LipDub IC-LoRA pass, not for the live loop.

**And the honest caveat.** The evidence that the face improves *learning* is weak. The evidence
that it improves *affect* is solid. Build it for the second reason.

---

## 10. Sources

**Gemini Live API** (all `[DOCUMENTED]`)
1. https://ai.google.dev/gemini-api/docs/live — overview, modalities, transport
2. https://ai.google.dev/gemini-api/docs/live-guide — models, VAD params, interruption semantics, 97 languages, 1 FPS video
3. https://ai.google.dev/gemini-api/docs/live-session — 15 min / 2 min limits, compression, resumption, GoAway
4. https://ai.google.dev/gemini-api/docs/live-tools — tool support matrix
5. https://ai.google.dev/gemini-api/docs/live-api/capabilities — context windows, thinking, proactive audio, affective dialog
6. https://ai.google.dev/gemini-api/docs/live-api — Live API landing
7. https://ai.google.dev/gemini-api/docs/ephemeral-tokens — 30 min / 1 min / 1 use
8. https://ai.google.dev/gemini-api/docs/pricing — Live pricing, 25 tokens/sec audio
9. https://ai.google.dev/gemini-api/docs/rate-limits — no Live-specific numbers published
10. https://support.google.com/gemini/answer/15274899 — consumer camera + screen share behaviour

**OpenAI Realtime API** (all `[DOCUMENTED]`)
11. https://developers.openai.com/api/docs/guides/realtime — transports, models, MCP
12. https://developers.openai.com/api/docs/guides/realtime-models-prompting — gpt-realtime-2 (128k) / 1.5 (32k), reasoning effort
13. https://developers.openai.com/api/docs/guides/realtime-conversations — semantic VAD default, truncation, out-of-band, input_image
14. https://developers.openai.com/api/docs/guides/realtime-webrtc — connection flow, ephemeral secrets
15. https://developers.openai.com/api/docs/api-reference/realtime-sessions — VAD defaults (0.5 / 300 ms / 500 ms), eagerness caps 8/4/2 s, max_output_tokens 1–4096
16. https://developers.openai.com/api/docs/pricing — realtime token prices

**Turn-taking / latency** (`[MEASURED]`)
17. Levinson & Torreira (2015), *Front. Psychol.* 6:731 — doi:10.3389/fpsyg.2015.00731 — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.00731/full
18. Stivers et al. (2009), *PNAS* 106(26) — doi:10.1073/pnas.0903616106
19. Levinson (2016), "Turn-taking in Human Communication," *TiCS* — doi:10.1016/j.tics.2015.10.010
20. Wilson & Wilson (2005), "An oscillator model of the timing of turn-taking" — doi:10.3758/bf03206432
21. Moshi (2024), arXiv:2410.00037 — 160 ms theoretical / 200 ms practical full-duplex — https://arxiv.org/abs/2410.00037
22. Qwen2.5-Omni (2025), arXiv:2503.20215 — https://arxiv.org/abs/2503.20215
23. Mini-Omni (2024), arXiv:2408.16725; 24. Mini-Omni2, arXiv:2410.11190; 25. LLaMA-Omni, arXiv:2409.06666

**Talking heads / avatars**
26. SadTalker, arXiv:2211.12194 — https://arxiv.org/abs/2211.12194 `[MEASURED]`
27. LivePortrait, arXiv:2407.03168 — 12.8 ms on RTX 4090 `[MEASURED]`
28. MuseTalk, arXiv:2410.10122 — 30 FPS @ 256² on V100 `[MEASURED]`
29. Hallo, arXiv:2406.08801; 30. EchoMimic, arXiv:2407.08136
31. VASA-1, arXiv:2404.10667 — 512² @ 40 FPS, no code released `[MEASURED]`
32. EMO, arXiv:2402.17485; 33. Loopy, arXiv:2409.02634; 34. Sonic, arXiv:2411.16331; 35. FLOAT, arXiv:2412.01064
36. OmniHuman-1, arXiv:2502.01061
37. Ditto, arXiv:2411.19509 + https://github.com/antgroup/ditto-talkinghead `[MEASURED]`
38. Wan-S2V, arXiv:2508.18621 + https://github.com/Wan-Video/Wan2.2 (≥80 GB VRAM; TI2V-5B 5 s/720P in <9 min) `[DOCUMENTED]`
39. LTX-Video, arXiv:2501.00103 + https://github.com/Lightricks/LTX-Video + https://github.com/Lightricks/LTX-2 (LTX-2.3, A2Vid pipeline, LipDub IC-LoRA) `[DOCUMENTED]`/`[VENDOR]`
40. SoulX-FlashHead — https://github.com/Soul-AILab/SoulX-FlashHead — 96 FPS Lite / 3 concurrent real-time on one 4090 `[MEASURED]`
41. LiveTalking — https://github.com/lipku/LiveTalking — WebRTC/RTMP, interruption, multi-concurrency `[DOCUMENTED]`
42. OpenAvatarChat — https://github.com/HumanAIGC-Engineering/OpenAvatarChat — 2.2 s average response `[VENDOR]`
43. face-swap-streamer — https://github.com/dlmastery/face-swap-streamer — 8–13 fps 1080p / 33 fps multiproc on 4090 `[MEASURED]`
44. https://docs.d-id.com/reference/get-started — "Agents: interactive, realtime avatars" `[VENDOR]`; HeyGen/Synthesia specs `[UNVERIFIED]` (403/404)

**Pedagogical agent evidence**
45. Schroeder, Adesope & Gilbert (2013), *JECR* 49(1) — doi:10.2190/EC.49.1.a — g = 0.19 `[MEASURED, secondary]`
46. Castro-Alonso, Wong, Adesope & Paas (2021), *Educ. Psychol. Rev.* — doi:10.1007/s10648-020-09587-1 — g = 0.20 `[MEASURED, secondary]`
47. Mayer & DaPra (2012), *JEP: Applied* — doi:10.1037/a0028616 — embodiment effect `[MEASURED]`
48. Instructor presence field experiments (2024), *ETR&D* — doi:10.1007/s11423-024-10391-9 — affect yes (d = .85, 1.01), learning no `[MEASURED]`
49. GenAI-PA meta-analysis (2025), *JECR* — doi:10.1177/07356331251400540 — g = 0.401 `[MEASURED]`
50. GAICA meta-analysis (2025 preprint) — doi:10.31124/advance.175136285.53256239/v1 — g = 0.357 / 0.519 `[MEASURED]`
51. Henderson & Schroeder (2021), *Computers and Education Open* — doi:10.1016/j.caeo.2021.100059 `[UNVERIFIED — abstract not retrieved]`
52. Craig & Schroeder (2017), *Computers & Education* — doi:10.1016/j.compedu.2017.07.003 `[MEASURED — metadata only]`
53. Seyama & Nagayama (2007), *Presence* 16(4) — doi:10.1162/pres.16.4.337 `[MEASURED]`
54. MacDorman & Chattopadhyay (2016), *Cognition* — doi:10.1016/j.cognition.2015.09.019 `[MEASURED]`

**Known gaps for a follow-up pass**
- End-to-end latency in ms for either hosted API — **no vendor figure exists in the docs.** Must be measured locally.
- Gemini Live concurrent-session / QPS quotas.
- OpenAI Realtime maximum session duration.
- HeyGen / Synthesia / liveavatar.com specs and latency claims (all sites blocked automated fetch).
- Verified originals for Schroeder (2013) and Castro-Alonso (2021) effect sizes.
- Henderson & Schroeder (2021) full abstract.

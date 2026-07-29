---
title: "Live formats after the constraint dies: podcasts that hear you, sessions with no schedule, video that stops where you are stuck, figures with a thirty-second life"
wave: V
section: V4
date_researched: 2026-07-29
sources_count: 42
---

# V4 — Live formats after the constraint dies

**What this document is.** A build specification for six formats that do not exist. It is not a
review. Where the literature is silent I have marked the design `SPEC` and specified it anyway;
an absent citation is not a reason to leave a decision unmade. Every number carried in from
another section of this repo is re-labelled with its original evidence tag.

**Evidence labels**
- `MEASURED-META` / `MEASURED-RCT` / `MEASURED` — a number from a meta-analysis, a randomised
  trial, or a reproducible artifact.
- `DOCUMENTED` — a hard spec published by a vendor or a paper's own claim about its system.
- `OBSERVED` — directly inspected this session (repo state, API response, page text).
- `CRAFT` — observed elite practice, unmeasured.
- `SPEC` — designed here. Not evidence. A commitment about what to build.
- `INFERENCE` — a step of reasoning over labelled evidence.

---

## 0. The one thing to read if you read nothing else

The brief's organising insight is right and incomplete. Sharpened:

> **Every format we have was shaped by an economic constraint. But each constraint was also
> silently supplying a service nobody paid for. Strip the constraint and the service falls out
> with it. The design work is not imitating the format better — it is enumerating what the
> constraint was quietly doing and re-supplying each service on purpose.**

Three services, and the evidence that they are real:

| Constraint | Its stated job | The service it was also supplying, unpriced | Does the service dissolve too? |
|---|---|---|---|
| The lecturer's time is scarce | ration expert attention | **a commitment device and a task-initiation cue** | **No.** It has to be rebuilt, by the learner, against themselves |
| Producing a video/figure is expensive | limit how many get made | **someone checked it before it shipped** | **No.** Verification does not get cheaper when generation does |
| A podcast is recorded in advance | the host cannot hear you | **it was edited — the boring parts were cut** | **No.** Live speech is less dense than produced speech |
| A class is synchronous | buy attention in bulk | **the turn comes to you; you cannot silently substitute rereading for retrieval** | **No.** But it needs minutes, not fifty of them |

The failure mode this predicts is specific and is what the market is currently doing: build the
always-available tutor, remove the schedule, and discover that completion collapses — then try to
fix it with notifications, which is the intervention with four large nulls behind it
(§2.2). The constraint was load-bearing in a way nobody documented because nobody was paying for
it.

And the second-order consequence, which sets the build order in §9: **all six formats consume the
same authoring asset** — a decomposition of a topic into claim units, each with a proposition, a
dependency set, and one attemptable check. Build that once. Everything else is a traversal policy
over it.

---

## 1. Substrate check — what is actually true as of 2026-07-29

### 1.1 A correction the repo needs: open full-duplex speech exists and shipped

The repo's earlier sweep concluded there was **no maintained open full-duplex voice
implementation**, on the evidence that Moshi's last release was 2024-09-22. Checking commit
activity rather than release tags, per the brief:

| Repo | Stars | Last commit | Last release | License | `OBSERVED` 2026-07-29 |
|---|---:|---|---|---|---|
| `kyutai-labs/moshi` | 10,755 | **2026-05-16** | rustymimi-0.2.2, 2024-09-22 | Apache-2.0 | commits are 20 months newer than the release tag |
| **`NVIDIA/personaplex`** | **10,274** | 2026-03-02 | *none* | **MIT** | **created 2026-01-05; 7B full-duplex S2S; weights on HF** |
| `xcc-zach/xtalk` | 233 | 2026-07-06 | — | Apache-2.0 | cascaded full-duplex, pure Python, WebSocket, active |
| `DanielLin94144/Full-Duplex-Bench` | 246 | 2026-05-20 | — | — | v1→v3; WebRTC orchestrator; evaluates Gemini 3.1 Live & PersonaPlex |
| `pipecat-ai/pipecat` | 13,793 | 2026-07-28 | v1.6.0, 2026-07-21 | BSD-2 | orchestration, actively released |
| `livekit/agents` | 11,559 | 2026-07-29 | 1.6.7, 2026-07-25 | Apache-2.0 | orchestration, actively released |

**PersonaPlex** (Roy, Raiman, Lee, Ene, Kirby, Kim, Kim, Catanzaro; arXiv:2602.06053, submitted
2026-01-14) is *"a duplex conversational speech model that incorporates hybrid system prompts,
combining role conditioning with text prompts and voice cloning with speech samples… based on the
Moshi architecture and weights"*, MIT-licensed, `pip install moshi/.`, `python -m moshi.server`.
`DOCUMENTED` It claims to surpass prior duplex models *"in role adherence, speaker similarity,
latency, and naturalness"* on an extended Full-Duplex-Bench; the abstract publishes **no latency
number**, so Moshi's 160 ms theoretical / **200 ms practical** remains the reference figure.
`MEASURED` (arXiv:2410.00037)

Honest caveat: PersonaPlex's last *code* commit is 2026-01-24 and the only later commits are
README edits. It is **shipped and installable, not actively developed upstream**. The
maintenance is being carried by the ecosystem — an MLX port for Apple Silicon (76★, 2026-02),
a 4-bit/8-bit quantisation fork for 16 GB consumer GPUs (18★), and several one-click launchers.
`OBSERVED`

**What changes because of this.** The "you cannot self-host duplex" line is retired. A
locally-hosted, MIT-licensed, role-conditioned, voice-cloned full-duplex tutor is a weekend of
integration, on a 4090. That matters most for children's audio, where F8's COPPA analysis makes
sending a child's voice to a third party the expensive path.

**And a warning.** X-Talk advertises that *"paralinguistic information (e.g. environment noise,
emotion) is encoded in parallel to support in-depth understanding and empathy."* `DOCUMENTED`
That feature, used in an EU education deployment, is a direct collision with AI Act Art. 5(1)(f).
See §2.4. An otherwise excellent framework ships a component you must disable.

### 1.2 The vendor limits are configuration, not physics

| | Gemini Live | Wan-Streamer v0.3 | Vidu S1 |
|---|---|---|---|
| Video in | JPEG frames **≤ 1 FPS** `DOCUMENTED` | 640×368 @ **25 FPS** in *and out* `DOCUMENTED` | — |
| Video out | none | 640×368 @ 25 FPS | **540p @ up to 42 FPS on consumer GPUs** `DOCUMENTED` |
| Streaming unit | — | **160 ms** | — |
| Model-side latency | not published anywhere `UNVERIFIED` | **~200 ms** | "real-time" |
| Total interaction latency | not published | **~550 ms** (with 350 ms network) | — |
| Session cap, audio+video | **2 minutes** `DOCUMENTED` | none stated | "infinite-length" |

(Wan-Streamer: arXiv:2606.25041 v0.1 and arXiv:2607.15038 v0.3 *"Video = World + Event Stream"*;
Vidu S1: arXiv:2607.03118. Both `DOCUMENTED` — vendor-authored papers, not independently
replicated.)

The gap is 25× on frame rate and unbounded on session length, between what a hosted API permits
and what a research system demonstrates on hardware the user already owns. **Design against the
physics, not the quota.** Every format below assumes 25 FPS bidirectional video and sub-second
turns are achievable, because they have been achieved, and treats the 2-minute cap as a
temporary billing decision.

The counterweight — and it is decisive for Format 3 — is **VideoFDB** (arXiv:2605.30256): the
first full-duplex audio-visual-to-audio-visual benchmark finds *"systematic failure modes:
captioning collapse and visual-stream ignorance,"* that current systems *"exploit vision for
explicit visual question answering but not for the streaming joint audiovisual grounding required
in natural conversation,"* and that cascaded speech-to-avatar architectures *"fundamentally
preclude the production of full-duplex nonverbal cues."* `DOCUMENTED` So the pixels are fast
enough and the grounding is not. That asymmetry is why every format below puts generation on the
*overlay* and keeps assertions on *authored* assets.

### 1.3 The human clock everything is measured against

Levinson & Torreira (2015), *Front. Psychol.* 6:731: modal floor-transfer offset **100–200 ms**;
**51–55%** of all turn transitions under 200 ms; modal overlap < 50 ms. And the finding that
governs the architecture: humans hit 200 ms by **predicting** turn ends, because producing even a
single word takes ~600 ms and a complex sentence ~1500 ms. `MEASURED-META`

Against which: the *default* VAD configuration on both hosted APIs (500 ms silence + 300 ms
prefix padding) exceeds the human modal gap **by 2.5–5× before the model has done any work**.
`DOCUMENTED` (A4 §7.2)

**Design consequence, used in three formats below:** navigation commands must not travel through
VAD. Route "wait", "go back", "again", "slower", "stop" through a separate always-on keyword
spotter with a ≤ 150 ms budget, and let VAD own only the conversational path. This is a
~200-line component and it is the highest-leverage single decision in this document.

---

## 2 · Format 1 — The podcast that can hear you

### 2.1 The constraint, and what actually dissolves

**Dead constraint:** the recording finishes before you hear it, so the host cannot hear you.

**What dissolves:** one-directionality. Fully. §1.1 shows the model exists, open and local.

**What does NOT dissolve — and this is where the naive answer loses.** A produced 20-minute audio
piece has been *cut*. Every hesitation, dead end, and restatement was removed by someone. Live
speech is not merely rougher; it is substantially less dense per minute of listening. The format
with "the best claim on time nobody else can use" earns that claim through density. A live tutor
in your headphones while you drive is not a better podcast — it is a worse one that answers
questions. `INFERENCE`, and I have no measurement of the density ratio; that is a gap worth
closing.

**Therefore what it becomes:** not a live show. **A produced, edited, pre-rendered audio programme
with interruption seams.** Default state is playback of a verified artifact. The learner's voice
preempts playback at any sample. On resolution, playback resumes at a *recomputed* position, not
where it stopped.

Call it a **seamed monologue**. `SPEC`

### 2.2 The prior art obeys the dead constraint

NotebookLM ships an interactive Audio Overview. From Google's own support page, retrieved
2026-07-29, verbatim `DOCUMENTED`:

> "join a conversation and interact with the AI hosts in Audio Overview. With your voice, you can
> ask the hosts for more details or to explain a concept differently."

and, decisively:

> "**When the hosts call on you, ask your questions.**"

The floor is granted by the hosts. That is a raise-hand queue — a half-duplex politeness protocol
wrapped around a broadcast. It is the dead constraint, preserved as an interaction pattern after
the technology that required it went away. Also documented: English only; new overviews only;
interactions are not shared; *"your voice and transcribed interactions with the hosts won't be
stored or shared"*; known issues include *"a slight delay in starting to play the initial
content"* and *"random speaker switches, third voice, or voice glitches."*

**The format nobody has built is the one where the learner takes the floor without being offered
it.** That is the whole product.

### 2.3 The interruption model

Three classes, disjoint, resolved client-side before any model is consulted. `SPEC`

| Class | Trigger | Behaviour | Budget |
|---|---|---|---|
| **Backchannel** | vocalisation < 600 ms, no content word, matches an open backchannel set ("mhm", "yeah", "huh", "wow", laughter) | **Do not pause.** Log a marker at the current claim unit. Never respond. | — |
| **Navigation** | matches the closed command grammar | Do not enter dialogue. Execute a deterministic transport action. | **≤ 150 ms** |
| **Barge-in** | any speech > 600 ms, or containing a wh-word, at any position | Duck programme audio to −18 dB within **120 ms**; hard-stop by **300 ms**; open a live segment | ≤ 300 ms to silence |

Notes that matter:

- **Ducking before stopping.** A hard cut at 0 ms is startling and produces false positives on
  ambient speech; a 120 ms duck is perceptible as "it heard me" and is recoverable if the trigger
  was spurious. `SPEC`, borrowed from broadcast practice `CRAFT`.
- **Backchannels must not stop playback**, and this is the single most common failure in shipped
  voice systems. Full-Duplex-Bench v1.0 assesses exactly this as one of its four dimensions
  (pause handling, backchanneling, smooth turn-taking, user interruption) `DOCUMENTED` — use it
  as the acceptance test, do not invent one.
- **Acoustic echo cancellation is mandatory and is not optional plumbing**: the microphone is
  hearing the programme. `libwebrtc` AEC, in-browser or native. Without it, every class above
  fires on the programme's own voice.
- **The listener is not the speaker.** The always-on component consumes (mic − programme via AEC)
  and emits a *class label*, not a reply. It needs no LLM. The live-segment model is only
  instantiated on a barge-in, which is also what makes the cost model work.

### 2.4 "Wait, go back"

The naive implementation rewinds N seconds. It is wrong, because **audio time is not idea time**.

The programme is not a waveform. It is a **`ProgrammeIR`**: `SPEC`

```yaml
programme:
  id: str
  claim_units:                 # ordered
    - id: str
      audio: {start_ms, end_ms}
      proposition: str         # the one thing this unit asserts
      depends_on: [unit_id]    # units whose propositions this one presumes
      rung: int                # position on the explanation ladder (F10/N4)
      check:                   # REQUIRED. A unit with no check may not ship.
        prompt: str
        answer_spec: {...}
        distractors: [{option, misconception_id}]   # each names a misconception
      exempt_strings: [str]    # formulae, code, numerals — never spoken-only
```

Resolution of `BACK`:

1. If the learner is **> 2 s into** the current unit → seek to the **head of the current unit**.
2. Else → seek to the head of the **nearest unresolved dependency** of the current unit, where
   "unresolved" means its `check` was never attempted or was attempted wrongly.
3. **Second consecutive `BACK` on the same unit does not replay.** It re-renders that unit one
   rung *down* the explanation ladder and resumes. Replaying identical audio is the auditory
   equivalent of re-reading, and this repo has the number: retrieval practice **g = 0.51 vs
   restudy** `MEASURED-META` (corpus B1, Adesope, Trevisan & Sundararajan 2017). Replay is
   restudy.
4. **Third `BACK`** abandons playback and hands off to dialogue, opening with the unit's `check`
   as a prequestion — the learner must attempt before the explanation resumes. Prequestions carry
   **g = 0.54 [0.42, 0.66], k = 97** on the material they ask about `MEASURED-META` (St. Hilaire,
   Chan & Ahn 2024, preregistered), and the work is done by **the attempt** — guessing **g = 0.65**
   vs not-guessing **g = 0.22**.

Companion commands, same grammar, same 150 ms budget: `AGAIN` (replay current unit verbatim —
the one case where verbatim replay is what was asked for), `SLOWER` (playback rate, not
re-render), `SKIP` (advance to next unit, mark check as skipped), `STOP`, `HOLD`.

Note what §2.4 buys that a live tutor does not: **the produced artifact is the thing that carries
density, and the graph is the thing that makes it navigable by idea.** Neither is available if you
just stream a model into headphones.

### 2.5 Knowing they stopped listening — what is legal, stated as architecture

**Prohibited.** EU AI Act **Art. 5(1)(f)** prohibits *"the placing on the market, the putting into
service for this specific purpose, or the use of AI systems to infer emotions of a natural person
in the areas of workplace and education institutions"* `DOCUMENTED` (verbatim, via F8 §1.1),
read with Art. 3(39) (biometric-based inference of emotions or intentions) and Art. 3(34)
(biometric data includes *"behavioural characteristics"*). Applicable since 2 February 2025.
F8 further flags that **sensor-free affect detection from clickstream and response latency sits
in a genuine grey zone** — clickstream is arguably a "behavioural characteristic" — and that no
authoritative construction of that boundary was found. `INFERENCE`

So do not build a design whose legality depends on winning that argument. The rule below is
stricter than the statute and does not need the grey zone resolved:

**Do not infer whether they are listening. Make listening produce an observable act on the
artifact, and observe the act.** `SPEC`

Legal signals, all of which are records of what the learner *did to a media object* — the same
category as turning a page:

1. **Solicited response latency.** Each claim unit carries a `check`. No response within
   **T = 6 s** is an event about *the check*, not about the person. The unit is marked
   unattempted; the responder decides what to do.
2. **Transport events.** Pause, seek, rate change, volume, skip, device disconnect, headphone
   removal, app backgrounded. User actions on a media object.
3. **Explicit declaration.** One utterance, told to the learner up front: "hold on" suspends the
   programme. This is autonomy-supporting rather than autonomy-spending — the one SDT need a
   machine supplies best-in-class (F6 §2.1).
4. **Absence of 1–3 for 90 s.** The system does **not** diagnose the learner. It **pauses itself,
   ends the session, and writes a resumption item.** Silence means "the session ended", not "the
   learner is bored."

That fourth move is the whole design: **replace state inference with a default-off policy.** You
never need to know they stopped listening if the artifact stops when unattended.

The resumption item is not a summary screen. N2's finding: resumption is a **re-entry item**, not
a screen — one retrieval question about the last thing done, answerable in seconds
(N2 §4.4 row 9, warranted by prequestion **g = 0.54** and retrieval **g = 0.51**). `MEASURED-META`

**Prohibited by construction, not by policy** (see §6.2): no classifier over voice acoustics,
prosody, face, or gaze whose output is a state of the person — bored, frustrated, confused,
engaged, distracted. This includes any use of X-Talk's paralinguistic emotion channel (§1.1) and
Gemini 2.5's *affective dialog* feature in an EU education deployment. `DOCUMENTED` + `INFERENCE`

**Data minimisation.** A child's voice is personal information under COPPA (voiceprints,
16 CFR 312.2) `DOCUMENTED` (F8). Therefore: AEC and class detection on-device; live-segment audio
retained only in the streaming buffer; learner utterance transcripts retained only within the
session unless the learner saves them; persisted state is claim-unit outcomes only. Google's own
posture on NotebookLM interactive mode is identical and is a usable public benchmark.

### 2.6 What has to exist · what to build first

Must exist: the `ProgrammeIR` authoring format; a concurrent listener (AEC + streaming VAD +
closed command grammar) that runs *during playback*, which neither hosted API contemplates
because both assume the model is the only speaker; a live-segment model (hosted Realtime, or
PersonaPlex locally).

**Buildable today: yes**, entirely. Nothing here waits on a model that doesn't exist.

**Build first:** the `ProgrammeIR` graph and the transport layer — three interruption classes,
hardcoded command grammar, `BACK` resolving to claim units — over a **pre-recorded programme with
no LLM anywhere in the loop.** Two weeks. If "wait, go back" does not land on the right idea, no
amount of duplex rescues it.

---

## 3 · Format 2 — The live session with one attendee and no schedule

### 3.1 The constraint, and the service nobody priced

**Dead constraint:** expert time is scarce and indivisible, so it is sold in bulk and in advance.

**What dissolves:** the expert's scarcity; the bulk; the schedule as a *rationing* device; the
50-minute period, which was the lecturer's calendar granularity and never a learning quantity.

**What does NOT dissolve — the answer the brief says to find.** The schedule was never only
rationing. It was also the learner's **commitment device** and their **task-initiation cue**,
supplied free as a side effect of someone else's scarcity. The evidence that this is the
load-bearing part:

| Intervention | Result | Source |
|---|---|---|
| **Commitment device** — learner pre-commits a time budget | **+24% time on course, +0.29 SD grades, +40% more likely to complete** | Patterson 2018, *JEBO* `MEASURED-RCT` |
| Alert tool, same study | **indistinguishable from control** | ibid. `MEASURED-RCT` **null** |
| Distraction-blocking tool, same study | **indistinguishable from control** | ibid. `MEASURED-RCT` **null** |
| Self-regulation + affirmation nudges, 250k students / 247 courses | *"Scaling behavioral science interventions across various online learning contexts can reduce their average effectiveness by an order-of-magnitude"*; engagement up early, **completion not** | Kizilcec et al. 2020, *PNAS* `MEASURED-RCT` |
| Nudge campaigns, **>800,000 students** | *"no impacts… overall or for any subgroups"*; no framing, delivery, or timing variant helped | Bird et al. 2021, *JEBO* `MEASURED-RCT` **null** |
| Virtual coaching, 5 years, ~20,000 students | study time up, **no effect on academic outcomes** | Oreopoulos & Petronijevic 2023, *EJ* `MEASURED-RCT` **null** |
| **Implementation intentions in children**, 52 ES / 42 studies / **N = 12,957** | **Hedges' g = 0.31 [0.21, 0.41]**; stronger in younger children and **in ADHD** — *"particularly effective when self-regulation abilities are limited"* | Breitwieser & Reinelt 2026, *BJP*, registered report `MEASURED-META` |

**Being told does nothing. Being reminded does nothing. Being blocked does nothing. Binding your
own future self does a lot.** The structural reason (F6 §1.4): the commitment device is the only
intervention on that list that *transfers* autonomy to the learner rather than spending it.

So the product that removes the schedule and replaces it with push notifications has swapped the
one thing that worked for the thing with four large nulls behind it.

### 3.2 What "live" means when the other party is always available

Availability is not a schedule. A schedule is a **constraint the learner accepted in advance**.
When the expert stops supplying it, the learner must, and the system's job is to make that binding
possible and then honour it — including honouring it against the system's own engagement interest.

Three mechanisms. `SPEC`, each anchored to a measured result.

**(1) The learner-authored appointment, fired by an if-then cue.**
Not "when shall I remind you?" — that is a reminder, and reminders are the null column. The
learner declares an if-then cue bound to an existing routine ("after I put my bag down", "after
the second coffee") plus a duration. At the cue, **the session opens itself with the first item
already on screen and answerable in one action.** It does not ask permission; asking is a decision
point, and decision points are exactly where an initiation deficit bites. Warrant: implementation
intentions **g = 0.31**, strongest where self-regulation is weakest.

*Platform reality, stated because it changes the design:* on iOS you cannot programmatically open
an app. The best available is a local notification that **renders the first item inside the
notification**, so the first attempt happens before the app opens. On Android, a full-screen
intent; on desktop, a systemd/launchd timer. `OBSERVED` (platform constraint, not measured here.)

**(2) Manufactured scarcity with teeth.**
The tutor is *not* always-available in the UI. It is present inside the window the learner bound.
Outside it, the tutor is reachable but the learner must spend an explicit override, which is
logged and shown back at the next review. Ariely & Wertenbroch (2002): self-imposed deadlines
improve performance `MEASURED-RCT`. The override log is the learner's, not the system's; it is
never used to nag.

**(3) A witness.**
F6 §2.3 is unambiguous that relatedness is the need a machine cannot supply the load-bearing part
of, and that *"a companion that never notices your absence cannot underwrite a commitment."*
`INFERENCE` Minimum viable witness: an opt-in weekly one-line digest to a **named human** — parent,
peer, coordinator — showing kept/missed commitments only, no content, no transcripts, no scores.
The human need never attend. They need only be capable of noticing.

### 3.3 Why anything should be synchronous at all

Three functions survive the death of scarcity, and only three:

**(a) Only a time is bindable.** "Do it sometime" is not a commitment. Synchrony is the substrate
that makes §3.2(1) enforceable at all.

**(b) The turn comes to you.** In a live segment the learner cannot silently substitute rereading
for retrieval. This is the same mechanism as the expectancy result: teaching *with* a prior
expectancy is **g = 0.48 [0.34, 0.63]**; teaching *without* it is **g = −0.02 [−0.14, 0.11]**
(Kobayashi 2024, k = 39) `MEASURED-META`. What is different is not the activity; it is that
something was committed to beforehand.

**(c) A loop that must close inside working memory.** Real-time is genuinely required only where a
wrong step must be corrected before the next step is built on it. Everywhere else, asynchronous is
equal or better — and this repo has the direct evidence that an audience is a *net cost*: teaching
**to a camera** beat teaching to one student and to seven on transfer, with **lower social
presence, lower pulse rate, lower anxiety, lower cognitive load, and more idea units produced**
(Wang, Cheng & Mayer 2023) `MEASURED-RCT`; written teaching scripts equalled spoken at one week,
and mode is a **null moderator** in the meta-analysis.

**Conclusion, stated plainly because it will be unpopular: most of what is currently synchronous
should not be.** The correct residue of "live" is a short, bounded, learner-committed window in
which one feedback loop closes fast. `SPEC`: default 12 minutes, learner-settable, hard-stopped
by the system. A tutor that runs long is spending the learner's commitment budget without asking.

### 3.4 What has to exist · what to build first

The **commitment object**, first-class, learner-owned:

```yaml
commitment:
  cue: {type: routine_anchor | clock, spec: str}
  window: {duration_min: int, hard_stop: bool}
  declared_goal: str            # the learner's words, not a curriculum node
  witness: {contact_id, digest: weekly} | null
  overrides: [{t, reason?}]     # append-only, learner-visible, never used to prompt
  # The system may READ this. The system may never WRITE it.
```

Plus a cue-fired opener that pre-loads the first attemptable item, and one hard product rule:
**no notification that is not a learner-authored cue.** Every other notification is in the null
column, and under AI Act Art. 5(1)(b) — exploiting *"vulnerabilities of a natural person… due to
their age, disability"* `DOCUMENTED` — engagement mechanics tuned to a child's known impulsivity
are prohibited outright, not merely unwise (F8).

**Buildable today: yes.** It requires no AI whatsoever. That is the point and the embarrassment.

**Build first:** the commitment object and the cue-fired opener, shipped **with no tutor behind
it**, measured on F6's **Unprompted Return Rate** — sessions initiated with no notification,
email, or reminder in the preceding 24 h — against a reminder-based control.

---

## 4 · Format 3 — The tutorial video that stops where you are stuck

### 4.1 The constraint, and the one that replaces it

**Dead constraint:** rendering was expensive, so a video is authored once, linearly, for the median
viewer.

**What dissolves:** the marginal cost of a path. §1.2: 540p at 42 FPS on a consumer GPU;
640×368 at 25 FPS with 200 ms model-side latency. This is measured, in 2026, on hardware in the
building.

**What does NOT dissolve: verification.** A video made once was also *checked* once. Generated
video is unchecked at every frame. C1's tier rules are not advisory:

- *"A figure below L2 may not be shown to a learner."* Not "should not" — the measured failure
  rates make L1 output *a misconception generator*.
- **"Regeneration resets the tier."** vTikZ (arXiv:2505.04670) finds models *"struggle to reliably
  modify code in alignment with visual intent"*; an edited artifact is a **new** artifact and must
  re-clear every gate. **"Edits are more dangerous than first drafts"** — C1 calls this the
  least-appreciated result in the area. `MEASURED-BENCH` / `INFERENCE`

And VideoFDB (§1.2) says the streaming visual grounding required to know *what to draw next* is
precisely what current systems fail at. `DOCUMENTED`

So "generate the branch" is prohibited by this repo's own gate, and by the only benchmark that
tests the capability it would require.

### 4.2 What it becomes: three layers with different verification duties

**The video is not a file and not a generator. It is a rendered traversal of an authored,
pre-verified segment graph, with a generated overlay layer that never carries a claim.** `SPEC`

| Layer | Content | Verified | Generated at runtime? |
|---|---|---|---|
| **Base** | One authored segment per knowledge component, L3+ signed | once, offline, human of record | no — retrieved |
| **Branch** | Authored alternates: one per known misconception, one per lower ladder rung (F10/N4) | once, offline, L3 | no — retrieved |
| **Overlay** | Deixis only: pointer, highlight, arrow, freeze-frame, a re-drawn figure, a spoken aside | **L2 gate at runtime** (schema + deterministic render + assertions) | **yes** |

The overlay may **point at, emphasise, or re-draw**. It may **not assert a new fact**. Any new
fact requires a branch, and a branch must already exist. **If no branch exists for the detected
misconception, the video stops and hands off to dialogue.** Stopping is a legitimate output and
should be designed as one, not treated as a failure.

This answers "re-render or overlay" directly: **overlay, always, for anything inside the latency
budget. Re-render only offline, into new authored branches, as a batch job informed by where
learners actually stopped.** A4 makes the pixel-space argument; C1 makes the verification
argument; VideoFDB makes the grounding argument. All three agree.

A note on the largest unexploited affordance, which lives in this layer: A4 §5.4 observes that no
vendor exposes deixis at all — no cursor, no annotation, no "highlight line 12" — and concludes
that *"nobody has built a good shared-pointing surface."* The overlay layer **is** that surface,
and its gate is what makes it safe. Deixis is the cheapest thing on this list and the most
distinctive.

### 4.3 How it knows where you are

Same legal rule as §2.5: observe acts, never states. Three sources, and the asymmetry between them
is the design.

1. **Transport behaviour tells you *where*.** Rewind on segment k; **second rewind on segment k**;
   pause > 20 s; playback-rate reduction. The double-rewind on the same segment is the single
   strongest free signal in the system and nobody uses it.
2. **The interposed attempt tells you *what*.** Each knowledge component ends with one attemptable
   check whose distractors each name a `misconception_id`. A wrong answer *identifies* the
   confusion rather than merely detecting one. Warrant: prequestion **g = 0.54** specific,
   **g = 0.04** general `MEASURED-META` — the effect is proposition-local, so a system that
   doesn't know *which* proposition failed can only respond generically, and generic response is
   the 0.04 column.
3. **Volunteered speech.** Handled by Format 1's interruption model, unchanged.

You need both 1 and 2. The attempt is the one every product skips because it interrupts the
video. **It has to interrupt the video. That is the mechanism, not the cost.**

### 4.4 What a branch costs

Two costs, and only one of them is compute.

- **Compute.** Retrieving an authored segment: ≈ 0 (a seek in a prefetched buffer). Overlay
  render for a Tier-A declarative figure: target **≤ 400 ms p95 to first pixel**, `SPEC` — freeze
  the frame while it renders and the perceived cost is zero. **This repo contains no measured
  figure-render latency anywhere.** That is a one-day measurement and it should be the first
  number produced by this workstream.
- **Authoring.** Each branch is a human-verified asset. **This is the real cost, and it is linear
  in misconceptions, not in learners.** A course with 40 knowledge components and 3 authored
  misconception branches each is 160 verified segments. That is a production plan, not a research
  problem — and the same 160 assets serve Formats 4 and 6 (§9).

### 4.5 The latency budget

Against Levinson & Torreira's modal 100–200 ms gap `MEASURED-META`:

| Event | Budget | Why it is achievable |
|---|---|---|
| Navigation command → audio-visual response | **≤ 150 ms** | keyword spotter + local seek; **no VAD, no model** |
| Barge-in → programme ducked | **≤ 120 ms**; hard stop ≤ 300 ms | client-side |
| Wrong answer → branch segment begins | **≤ 700 ms** | retrieval + decode; A4's "feels natural" band is 300–800 ms |
| Overlay figure appears | **≤ 400 ms** p95 | `SPEC` — unmeasured, measure it first |
| Dialogue turn in a live segment | **300–800 ms** | A4 §7.4; Moshi-class 200 ms model-side is the ceiling of the possible |
| Deliberate wait time after a question | **1500–3000 ms**, deliberate | A4 §7.4: in tutoring, marked silence is often correct. **The goal is controllable latency, not minimal latency.** |

The last row is the one that separates a tutor from a voice assistant, and it is a *policy on the
responder*, not a property of the stack.

### 4.6 Buildable · build first

**Buildable today: partial.** Base + branch + transport + attempt: **yes, today, with no
generative video at all.** Gated overlay figures: **yes** (C1 pipeline, §5). Generated video
branches: **no — and should not be built.** Not because they are impossible (Vidu S1 and
Wan-Streamer show they are not) but because **nothing gates them**, and C1's tier rule forbids
shipping ungated artifacts to a learner.

**Build first:** the double-rewind detector and the interposed attempt, over an **existing linear
video**, with authored branches for the top 3 misconceptions in **one** topic. Zero generation.
If branch selection does not beat linear playback at equal total content, the generative version
will not save it.

---

## 5 · Format 4 — Illustration on the fly

### 5.1 The constraint

**Dead constraint:** a bespoke figure for one confusion in one head is uneconomical to draw by
hand. Survey/05 §4 names this exactly: *"Nobody makes that by hand, because it is uneconomical to
make a bespoke figure for one confusion in one head. That constraint is the one that lifts."*

**What dissolves:** the marginal cost of the drawing.

**What does NOT dissolve:** the figure was correct because a person drew it. So: **the model does
not draw. The model emits a declarative spec; a deterministic renderer draws it; a gate checks the
spec before it renders.** C1's convergent architecture, unchanged.

**What it becomes:** a **disposable L2 artifact with a thirty-second provenance** — generated
against a *named* misconception, satisfying a checkable contract, shown once, discarded.

With one addition C1 does not make: **retain the spec, not the image.** Two reasons. An image is
not auditable; a spec is. And if the same `misconception_id` recurs across learners, the spec is
the unit that gets promoted to L3 and becomes an authored branch in Format 3. **The on-the-fly
figure is the R&D pipeline for the authored asset.** That loop is what makes the whole system get
cheaper over time instead of more expensive. `SPEC`

### 5.2 The pipeline

```
[t−30s … t]  dialogue / attempt window
   │
   ├─ 1. MISCONCEPTION IDENTIFICATION — never inference from behaviour.
   │     Named by (a) a distractor the learner selected, or (b) a proposition
   │     the learner asserted that contradicts a reference proposition.
   │     Output: misconception_id ∈ N4 atlas, or NULL.
   │     NULL → NO FIGURE.                                    ← HARD GATE
   │
   ├─ 2. FIGURE CONTRACT — deterministic lookup, not generation:
   │     misconception_id → { figure_archetype,
   │                          required_propositions: [...],
   │                          contrast_pair,           # the wrong and right model
   │                          atomic_question_set }
   │     A figure with no atomic question set may not be generated. ← HARD GATE
   │
   ├─ 3. LLM emits DECLARATIVE IR ONLY, inside the archetype's closed grammar.
   │     No coordinates. No hand-written SVG paths. No raster. (C1 Tier D: prohibited)
   │
   ├─ 4. G1  schema / grammar validation                        HARD
   ├─ 5. G2  deterministic render                               HARD
   ├─ 6. G3  programmatic assertions                            HARD
   │        no label collision · canvas containment · arrow anchors attached ·
   │        axis scale/limits/zero-baseline · unit present · contrast ≥ 4.5:1 ·
   │        second encoding channel (never colour alone) · contiguity distance
   ├─ 7. G4  IR-diff vs required_propositions                   HARD
   ├─ 8.     alt text emitted FROM THE IR, not inferred from pixels
   ├─ 9.     VLM critique — ADVISORY ONLY. May propose a repair. May never pass.
   │
   ├─ FAIL at any hard gate → fall back to the archetype's authored template
   │     instance, or to no figure. NEVER ship a failed render.
   │     At most ONE repair attempt: an edited figure is a new figure and must
   │     re-clear every gate.
   │
   └─ 10. SHOW. Then discard the raster; retain
          { misconception_id, IR, gate results, next-attempt outcome }.
```

**The gate in one sentence:** *a figure ships only if a machine can state, from the source, which
propositions it asserts, and those propositions are exactly the ones the contract required.*
Everything else — beauty, style, "does it look right" — is advisory. Warrant: the VLM critique
path cannot gate, because misleading-visualisation detectors *"frequently misclassify
non-misleading visualizations as deceptive"* `MEASURED-BENCH` (C1 §5.4); C1's rule is
**"symbolic checks detect; the VLM repairs; the VLM never gates alone."**

### 5.3 The hard part nobody specifies: step 1

"A misconception detected in the last thirty seconds" is doing enormous work. Detecting a
misconception from free speech is unreliable, and routing it through prosody is legally adjacent
to the prohibited zone (§2.5). So:

**Misconceptions are detected by attempts, not by listening.** `SPEC`

Which means the format's real requirement is that the preceding thirty seconds contained an
*attemptable* thing. This is N2's central finding transposed: a question holds attention because
it can be attempted (**g = 0.54** vs an exhortation's **g = 0.04**), and — the part usually
missed — the attempt is also what **localises** the confusion. No attempt → no named misconception
→ no figure. That is a hard product rule and it will feel restrictive to everyone who has to
implement it.

### 5.4 The runtime switch, twice

C3's redundancy rule is *"a runtime switch per learner, not a style rule"* — evaluated on language
status, pacing control, reading support, and hearing access, with hard exemptions for formulae,
code, and numerals (C3 §2.4) `INFERENCE` over `MEASURED-META` (verbal redundancy **g = 0.15**;
text→audio **g = 0.29**; audio→text **g = −0.04 n.s.**).

The same architectural move applies a second time, and it should be named: **signalling is also a
runtime switch.** Signalling is **g = 0.43 [0.35, 0.50], k = 209** `MEASURED-META` (Schneider et
al. 2018) but the benefit is concentrated in **low-prior-knowledge** learners (**r = 0.17**,
Richter, Scheiter & Eitel 2016) and is subject to expertise reversal — so the emphasis channel
must be gated on the learner model's prior-knowledge estimate, per learner, at generation time.
`INFERENCE` (C1 §7)

Two independent principles, same shape: **the generator's real advantage over a human author is
not speed, it is per-learner evaluation of a conditional whose correct setting varies.** That is
the actual case for generative media, and it is much better than "figures on demand."

### 5.5 Latency and fallback

`SPEC`: **≤ 2.5 s** from named misconception to shown figure. Contract lookup ≈ 0; IR emission
400–1200 ms (C1's `INFERENCE` is that a *small* model suffices for a *small* IR); gates + render
≤ 400 ms; show.

If 2.5 s cannot be met: **show the archetype's authored template instance immediately and swap.**
Never make a learner wait for a figure. A generic correct figure now beats a bespoke correct
figure in four seconds.

**Buildable today: yes** — every component is off the shelf. The missing piece is the
misconception → contract table, which is an authoring job, sourced from N4.

**Build first:** the contract table for one topic (~20 misconceptions) and the gate, with figures
produced by **template instantiation rather than an LLM.** Then measure how often the template is
adequate. `SPEC` prediction: for a large majority it is, and the LLM's marginal contribution is
small — in which case the expensive part of this feature never has to be built.

---

## 6 · Format 5 — Bidirectional as the default

### 6.1 The primitive

What does a system need so that *every* format is two-way, including the broadcast ones? Two
things, one authoring and one runtime, and every format above is a specialisation of them.
`SPEC`

1. **Every broadcast artifact is compiled into a segment graph** whose nodes carry (i) a
   proposition, (ii) a dependency set, (iii) at least one attemptable check. (§2.4's
   `ProgrammeIR` generalised across media.)
2. **Every playback surface exposes one uniform in-band event channel.**

**The minimum signal that makes a monologue responsive is not the learner's voice.** It is:

> **one attemptable act per proposition, and one uniform way to say *no*.**

- *One attemptable act*, because the effect is proposition-local: **g = 0.54** on what the
  question asked, **g = 0.04** on everything else, k = 91, p = .349, with 46% of studies at or
  below zero `MEASURED-META`. A system that cannot tell which proposition failed can only respond
  generically, and generic response is the 0.04 column.
- *One uniform "no"*, because a menu is a decision and decisions are where executive function is
  spent. Spoken ("wait"), tapped (one button), or typed (one key) — **the same event, the same
  handler**, in the podcast, the video, the slide, and the live session.

### 6.2 The event channel — and the legal architecture expressed as a type

```
LearnerEvent {
  t_wall, t_artifact          // wall clock; position within the artifact
  node_id                     // which claim unit / knowledge component
  kind: ATTEMPT | NAVIGATE | BARGE_IN | BACKCHANNEL | DECLARE | TRANSPORT | ABSENT
  payload:
    ATTEMPT     -> {option_id | proposition_set, latency_ms}
    NAVIGATE    -> {BACK | AGAIN | SLOWER | SKIP | STOP}
    BARGE_IN    -> {utterance_text}
    BACKCHANNEL -> {}
    DECLARE     -> {HOLD | RESUME | DONE}
    TRANSPORT   -> {PAUSE | SEEK | RATE | VOLUME | DISCONNECT | BACKGROUND}
    ABSENT      -> {window_ms}
  // NOTHING ELSE. No affect. No confidence. No engagement score. No attention score.
}
```

That final comment is the compliance architecture. **If the event type cannot carry an emotional
or attentional state, no downstream component can infer one, and the Art. 5(1)(f) question never
arises** — including the unresolved grey zone over whether clickstream counts as a "behavioural
characteristic" under Art. 3(34), which F8 identifies as *"the sharpest open legal question in the
whole area"* and which determines the legality of a large body of AIED work in the EU.
`INFERENCE`

**Enforce the prohibition in the type system, not the policy document.** This is the most
transferable idea in this file and it costs nothing.

### 6.3 The responder contract

```
Responder(node, event, learner_model) -> Action

Action ∈ {
  CONTINUE,                    // do nothing; the broadcast case
  REPLAY(node),                // verbatim; only on explicit AGAIN
  DESCEND(node, rung),         // re-render one rung down the explanation ladder
  BRANCH(misconception_id),    // an authored alternate must exist
  OVERLAY(figure_contract),    // gated, non-assertive
  ATTEMPT(check),              // demand an attempt before proceeding
  HANDOFF_TO_DIALOGUE,         // live segment
  STOP                         // end the session; write a resumption item
}
```

Eight actions. Closed set. **A broadcast format is one whose responder returns `CONTINUE` for
every event. A fully interactive one uses all eight.** So:

> **Bidirectionality is not a property of the medium. It is the size of the responder's range.**

That is the sharpened form of the brief's insight, and it makes the property measurable: report
the action-mix histogram per format, and a "two-way" claim becomes falsifiable.

### 6.4 What is missing, and what to build first

Nothing is missing at the model layer. The gap is entirely **an artifact format and an event bus**
— which is unglamorous, which is why nobody has built it, and which is why every vendor SDK
assumes the model is the sole speaker and the sole author. Neither hosted API has any concept of
"the artifact currently playing."

**Buildable today: yes.**

**Build first:** `LearnerEvent` and the responder contract, implemented for exactly one format
(the podcast), with the other three stubbed to `CONTINUE`. Then port to video. **The porting cost
is the test of the abstraction** — if video needs a ninth action, the abstraction is wrong.

---

## 7 · Format 6 — The format nobody has: **the Standing Explanation**

### 7.1 The swing

Strip the reproduction constraint and the obvious move is one artifact per person. That is what
everyone is building and it is boring.

The non-obvious move is to strip it in the other direction. Every format above is **the system
explaining to the learner, with a return channel bolted on.** What has never been economically
possible is the inverse as a *primary medium*: **an artifact produced by the learner and consumed
by the system, at scale, persistently.**

Three measured things in this repo, which have never been combined:

1. Teaching **to a camera** beat teaching to one student and to seven, on **transfer**, with lower
   social presence, lower pulse rate, lower anxiety, lower cognitive load, and **more idea units
   produced** — mediated by exactly those paths (Wang, Cheng & Mayer 2023) `MEASURED-RCT`.
2. Learning-by-teaching is **g = 0.48 [0.34, 0.63]** *with* a prior expectancy to teach and
   **g = −0.02 [−0.14, 0.11]** *without* (Kobayashi 2024, k = 39) `MEASURED-META`. The fix is the
   ordering of one sentence.
3. **No study compares an AI audience to a human audience** (survey/05 §8; four independent search
   routes empty). The hypothesis: *the gain comes from being **interrogated**; the loss comes from
   being **evaluated**; every human audience welds them together; a machine audience is the first
   thing that can separate them.*

### 7.2 The format

**The Standing Explanation.** Not a session and not a lesson. A **persistent, versioned,
learner-authored explanation of one thing, which the system keeps and periodically attacks.**
`SPEC`

- **Declaration, before study.** The learner names a target — *"I will be able to explain why the
  water doesn't fall out of the bucket."* The expectancy sentence is delivered **before** study,
  always. It is free and it is the difference between g = 0.48 and g = −0.02.
- **Production, to no one.** The learner records to a camera or writes. **Never to a room.**
  Written equals spoken at one week, and mode is a null moderator. Presenting to humans is
  available, never required, never framed as the real version.
- **Scoring, without a judge.** Four checkable channels (survey/05 §9):
  1. **Proposition coverage** against a reference decomposition, in a stated scope.
  2. **Elaboration and monitoring counts** — the behaviours that actually *mediated* the effect in
     Mayer's studies. Count the mechanism, not the impression.
  3. **Executable prediction checks** — instantiate the learner's model and run it. If their
     account of the circuit says the bulb lights, simulate it. **The world disagrees, not the
     tutor.**
  4. **The protégé's downstream accuracy, capped** — taught only this, did it get the next problem
     right?

  Explicitly **not** an LLM judge: selection by LLM judge alone measured **−3.20pp and −1.68pp**
  against **+8.14pp** for test-based selection `MEASURED`. Explicitly **not** a human holistic
  rater: human graders of code reach **Krippendorff's α ≈ 0.20** `MEASURED`. The gold standard is
  noise.
- **Persistence.** The explanation is versioned and owned by the learner. It is an artifact, not a
  transcript.
- **Attack, on the learner's own schedule.** At spaced intervals set by the Format 2 commitment
  object, a **confused protégé** asks a question — *"wait, but then why doesn't X?"* — targeting
  exactly the propositions that coverage found missing or execution found wrong. The learner
  patches the explanation.
- **Assessment is the diff.** What changed, when, and in response to which attack. Not a test.

### 7.3 Why it is a format and not a feature

It inverts the direction of the medium. Every other format puts the generative act on the
system's side and gives the learner a return channel. This one puts the generative act on the
learner's side and makes the system's questions the return channel. Both are two-way; only one
of them locates the effortful production in the person who needs to do it.

And it exploits the one thing a machine is uniquely good at and every human audience is
structurally incapable of: **interrogating without evaluating.** This repo's own numbers say the
audience is where the loss is. Remove the evaluation, keep the interrogation.

### 7.4 What has to exist

- **Reference decompositions per target** — the N4 explanation atlas. *The same asset that supplies
  Format 3's branches and Format 4's contracts.* This is the strongest single argument for the
  build order in §9.
- **A protégé that asks genuinely dependent follow-ups.** The success criterion is checkable —
  *does answering this question require proposition p?* — so the generator can be gated the same
  way a figure is. This is the genuinely novel component.
- **Executable instantiation** where the domain permits (F3).
- **Learner-owned version storage**, exportable and deletable. Under IDEA, disability records are
  destroyable on parental demand (F8); an explanation archive is exactly the kind of thing that
  becomes a record.

**Buildable today: partial.** Coverage, elaboration counts, versioning, attack scheduling: yes.
Executable checks: yes in F3's domains, no elsewhere. The dependency-gated protégé generator:
partial — this is where the research risk sits.

**Build first:** the expectancy sentence and the persistent versioned explanation, with attacks
drawn from a **hand-written bank**. No generation. If the diff over eight weeks shows no growth,
no generator will fix it.

---

## 8 · The table

| Format | The dead constraint | What it becomes | Required capability | Buildable today | Build first |
|---|---|---|---|---|---|
| **1 · Podcast that hears you** | The recording finishes before you hear it | **Seamed monologue** — produced, edited audio over a claim-unit graph, preemptible at any sample, resuming at a *recomputed* position | `ProgrammeIR`; AEC + streaming VAD + closed command grammar running *concurrently with playback*; a live-segment model (hosted, or PersonaPlex local) | **Yes** | Claim-unit graph + 3 interruption classes + `BACK` resolution, over pre-recorded audio, **no LLM** |
| **2 · Session, one attendee, no schedule** | Expert time is scarce, indivisible, sold in bulk | **A window the learner binds themselves to**, cue-fired, ~12 min, hard-stopped, witnessed by a named human | Learner-owned commitment object; cue-fired opener that pre-loads the first attemptable item; a ban on all non-learner-authored notifications | **Yes** (needs no AI at all) | Commitment object + cue-fired opener, **with no tutor behind it**, measured on Unprompted Return Rate |
| **3 · Video that stops where you're stuck** | Rendering was expensive; author once, linearly, for the median | **A traversal of an authored, pre-verified segment graph** with a generated overlay that never asserts | Base/branch/overlay separation; double-rewind detector; interposed attempts with misconception-naming distractors; keyword spotter outside the VAD path | **Partial** — base+branch+transport yes; **generated video branches no, and should not be built** | Double-rewind + interposed attempt over an **existing linear video**, 3 authored branches, one topic |
| **4 · Illustration on the fly** | A bespoke figure for one confusion in one head is uneconomical | **A disposable L2 artifact with a 30-second provenance** — and the retained *spec* becomes tomorrow's authored branch | misconception→contract table; declarative IR + deterministic renderer + 4 hard gates; template fallback within 2.5 s | **Yes** | Contract table for ~20 misconceptions + the gate, figures by **template instantiation**, LLM second |
| **5 · Bidirectional by default** | Broadcast media had no return path, so none was designed | **A closed 8-action responder over a uniform event channel** — two-way becomes a measurable range, not a medium | `LearnerEvent` (which structurally cannot carry affect); responder contract; segment-graph compilation of every artifact | **Yes** | `LearnerEvent` + responder for the podcast only; others stubbed to `CONTINUE`; then port |
| **6 · The Standing Explanation** | An explanation could only be delivered to an audience, once, and the audience both interrogated and judged | **A persistent, versioned learner-authored explanation the system periodically attacks** — assessment is the diff | Reference decompositions (N4); dependency-gated protégé questions; executable instantiation; learner-owned version store | **Partial** | Expectancy sentence + versioned explanation + **hand-written** attack bank |

---

## 9 · Build order

The ordering is set by one fact: **Formats 1, 3, 4, 5 and 6 all consume the same authoring asset**
— a topic decomposed into claim units, each with a proposition, a dependency set, one attemptable
check, and distractors that name misconceptions. Build it once, for one topic, before anything
else. Every later phase is a traversal policy over it. `SPEC`

**Phase 0 — the substrate. Nothing ships without it.**
`ProgrammeIR` / segment-graph schema · `LearnerEvent` · the 8-action responder contract · one
topic fully decomposed (target: 40 knowledge components, 3 misconception branches each, ~120
distractors that name a `misconception_id`). No AI in this phase. The deliverable is a data
format and a hand-authored corpus.

**Phase 1 — Format 2, in parallel with Phase 0.** No dependency on the substrate; largest measured
prior of anything here (+40% completion, +0.29 SD); needs no AI. Ship the commitment object and
the cue-fired opener against a reminder-based control. Doing this early also protects every later
phase: if the commitment layer doesn't hold, nothing downstream gets used.

**Phase 2 — Format 1, over pre-recorded audio.** Transport, three interruption classes, command
grammar, `BACK` resolution. The live segment is added **last**, deliberately, so that the graph
is proven before the model is introduced and cannot be credited for the graph's effect.

**Phase 3 — Format 5, extracted from Phase 2.** Once the responder works for one format, extract
it, port it to video, and report the porting cost. Do not design the abstraction in advance;
extract it from a working instance.

**Phase 4 — Format 3, over an existing linear video.** Double-rewind detector, interposed
attempts, authored branches. Overlay layer added only after §4.4's render-latency number exists.

**Phase 5 — Format 4.** Contract table and gate, templates first. The LLM IR path is added only
if the template-adequacy measurement says it is needed.

**Phase 6 — Format 6.** Runs on the Phase 0 decompositions, the Phase 1 commitment object, and the
Phase 5 gate. It is last because it is the only one with genuine research risk in a required
component, and because by then the three assets it needs already exist.

**Never build:** generated video branches (ungatable); ungated figures shown to learners (below
C1 L2); any classifier whose output is a state of the person; any notification the learner did not
author.

---

## 10 · One falsifiable claim per format

Each is stated so that a specific result would kill it, with the prior that sets the expected
effect size.

**1 · Podcast.** On a 20-minute audio programme with matched total content, learners who can
interrupt score higher on *delayed transfer* than learners with pause/rewind only — **and the
effect is carried by claim-unit `BACK` navigation, not by the dialogue segments.**
*Kill condition:* the effect sits entirely in the dialogue segments. Then the segment graph is
unnecessary complexity and you should ship a live tutor and delete `ProgrammeIR`.

**2 · Live session.** Learners who author an if-then commitment with a named witness show higher
session completion and higher Unprompted Return Rate at 8 weeks than learners on identical content
with system-initiated reminders — **and the gap does not close when the reminder arm is given a
better tutor.** *Prior:* Patterson's +40% completion, attenuated by Kizilcec's order-of-magnitude
scaling penalty ⇒ **expect +5 to +10pp, and plan for it.** *Kill condition:* the reminder arm
matches. Then commitment devices do not survive contact with an always-available tutor.

**3 · Video.** On a fixed topic, learners on the branch-graph version reach criterion on delayed
transfer in **less total video time** than learners on the linear version with unlimited rewind —
**and the effect is carried by attempt-triggered branches, not transport-triggered ones.**
*Kill condition:* transport-triggered branching carries it. Then the interposed checks are
unnecessary and a far cheaper product is available.

**4 · Illustration.** A gated, contract-driven figure delivered within 2.5 s of a *named*
misconception produces higher correct-response rates on the *next* item targeting that
misconception than (a) no figure and (b) an ungated model-drawn figure — **and the ungated arm
underperforms the no-figure arm.** That third comparison is the one worth running, because it is
the one nobody believes. *Kill condition:* the ungated arm matches the gated arm. Then C1's entire
gate architecture is over-engineering and should be relaxed to G1+G2.

**5 · Bidirectional.** The same eight-action responder, ported **unchanged** across podcast,
video, slide and live session, produces the same direction of effect in all four. *Kill
condition:* any format requires a ninth action. Then the abstraction is wrong and these are
genuinely different objects that should not share a runtime.

**6 · Standing Explanation.** An AI protégé that interrogates without evaluating produces higher
transfer and lower state anxiety than a human audience, **and the gap is largest for learners who
currently avoid presenting.** *Prior:* teaching to a camera already beat 1 and 7 humans; an
*interrogating* camera should beat a *silent* one. *Kill condition:* the interrogating protégé
does not beat the silent camera. Then the entire gain was audience-removal — which is a far
cheaper product, and you should ship that instead.

---

## 11 · Limitations

1. **Five of the six latency budgets are `SPEC`.** The 120/150/400/700/2500 ms figures are
   designed here, anchored to Levinson's measured 100–200 ms human gap and A4's measured
   Moshi/Wan-Streamer numbers, but not measured for these components. The **figure-render latency
   in particular has never been measured anywhere in this repo** and should be the first number
   produced.
2. **Wan-Streamer and Vidu S1 are vendor-authored papers.** 25 FPS, 200 ms, 42 FPS, "infinite
   length" — all `DOCUMENTED`, none independently replicated. VideoFDB's finding of *visual-stream
   ignorance* in current systems is the counterweight and is the reason no format here lets
   generated video assert anything.
3. **The density claim in §2.1 is unmeasured.** That produced audio is substantially denser than
   live speech is `INFERENCE`. It is load-bearing for the whole seamed-monologue design and I
   found no measurement of the ratio.
4. **PersonaPlex's "maintained" status is arguable.** Shipped, installable, MIT, 10k stars — but
   the last *code* commit is 2026-01-24, with the ecosystem carrying the ports. Treat it as a
   working artifact, not a supported dependency.
5. **The Art. 5(1)(f) grey zone is unresolved.** F8 could find no authoritative construction of
   whether clickstream and response-latency signals count as "behavioural characteristics" under
   Art. 3(34). The §6.2 design is deliberately stricter than the statute so the answer does not
   matter; a laxer reading would permit more, and I have not specified for it.
6. **arXiv's API rate-limited mid-session** (HTTP 429 after ~30 queries) and Semantic Scholar
   returned 401/429 throughout. Several searches — conversational podcast generation, adaptive
   educational video, turn-end prediction — could not be run. WebSearch was exhausted before this
   section began.
7. **Format 6 has no direct evidence.** It is a composition of three measured results plus one
   documented absence. The composition is `SPEC` and the protégé-generator component is the only
   place in this document with genuine research risk in a required part.

---

## 12 · Sources

**Retrieved or inspected this session (`OBSERVED` / `DOCUMENTED`)**
1. NVIDIA/personaplex — github.com/NVIDIA/personaplex — 10,274★, MIT, created 2026-01-05, last commit 2026-03-02, no releases
2. PersonaPlex paper — arXiv:2602.06053 — Roy, Raiman, Lee, Ene, Kirby, Kim, Kim, Catanzaro; 2026-01-14; abstract verbatim
3. kyutai-labs/moshi — 10,755★, commits to 2026-05-16, last release 2024-09-22
4. Moshi — arXiv:2410.00037 — 160 ms theoretical / **200 ms practical** full-duplex `MEASURED`
5. xcc-zach/xtalk — 233★, Apache-2.0, last commit 2026-07-06; arXiv:2512.18706; paralinguistic-emotion channel
6. DanielLin94144/Full-Duplex-Bench — 246★, v1→v3; v1 dimensions: pause handling, backchanneling, smooth turn-taking, user interruption; arXiv:2503.04721 / 2507.23159 / 2510.07838 / 2604.04847; Gemini 3.1 Live and PersonaPlex added 2026-02/2026-05
7. Full-Duplex-Bench (published) — doi:10.1109/asru65441.2025.11433838
8. pipecat-ai/pipecat — 13,793★, v1.6.0 2026-07-21; livekit/agents — 11,559★, 1.6.7 2026-07-25
9. Wan-Streamer v0.1 — arXiv:2606.25041 — 160 ms streaming unit, ~200 ms model-side, ~550 ms total
10. Wan-Streamer v0.3, *"Video = World + Event Stream"* — arXiv:2607.15038 — 640×368 @ 25 FPS
11. Vidu S1 — arXiv:2607.03118 — 540p @ up to 42 FPS on consumer GPUs, infinite-length, voice-controllable
12. MiniCPM-o 4.5 — arXiv:2604.27393 — Omni-Flow; full-duplex omni on edge with < 12 GB RAM
13. DuplexOmni — arXiv:2606.09186 — split interaction / thinking layers, asynchronous
14. VideoFDB — arXiv:2605.30256 — first AV2AV full-duplex benchmark; captioning collapse, visual-stream ignorance; cascaded avatar systems structurally preclude full-duplex nonverbal cues
15. NotebookLM Interactive mode — support.google.com/notebooklm/answer/16212820 — *"When the hosts call on you, ask your questions"*; English only; voice not stored
16. mu-hashmi/personaplex-mlx (76★), cookertron/personaplex-7b-quantized (18★) — ecosystem ports
17. BayLing-Duplex — arXiv:2606.14528; FacePlex — arXiv:2606.30145; DuplexChat — arXiv:2607.04941 (surveyed, not load-bearing)

**Carried from this repo, with original labels**
18. `research/raw/A4-live-multimodal.md` — Gemini Live 1 FPS / 2-min video cap / 15-min audio `DOCUMENTED`; VAD defaults 500 ms + 300 ms `DOCUMENTED`; latency bands `INFERENCE`; no vendor end-to-end latency published `UNVERIFIED`; deixis absent from every API `DOCUMENTED`
19. Levinson & Torreira 2015, *Front. Psychol.* 6:731, doi:10.3389/fpsyg.2015.00731 — modal FTO 100–200 ms; 51–55% under 200 ms `MEASURED-META` (title/date re-verified via Crossref this session)
20. Stivers et al. 2009, *PNAS* 106(26), doi:10.1073/pnas.0903616106 `MEASURED`
21. `research/raw/N2-executive-function-and-attention.md` — prequestions **g = 0.54 [0.42, 0.66]** specific / **g = 0.04 [−0.04, 0.11]** general, k = 97/91 (St. Hilaire, Chan & Ahn 2024, preregistered) `MEASURED-META`; guessing **0.65** vs not-guessing **0.22**; resumption as a re-entry item
22. Breitwieser & Reinelt 2026, *Br. J. Psychol.*, doi:10.1111/bjop.70065 — implementation intentions **g = 0.31 [0.21, 0.41]**, 52 ES / 42 studies / N = 12,957, stronger in ADHD `MEASURED-META`
23. Retrieval practice vs restudy **g = 0.51** — Adesope, Trevisan & Sundararajan 2017, via corpus B1 `MEASURED-META`
24. `research/raw/F6-motivation-persistence.md` — Patterson 2018, *JEBO*, doi:10.1016/j.jebo.2018.06.017 — commitment device **+24% time, +0.29 SD, +40% completion**; alert tool null; blocker null `MEASURED-RCT`
25. Kizilcec, Reich, Yeomans et al. 2020, *PNAS*, doi:10.1073/pnas.1921417117 — order-of-magnitude attenuation at scale `MEASURED-RCT`
26. Bird, Castleman, Denning et al. 2021, *JEBO*, doi:10.1016/j.jebo.2020.12.022 — >800,000 students, null `MEASURED-RCT`
27. Oreopoulos & Petronijevic 2023, *Economic Journal*, doi:10.1093/ej/uead064 — ~20,000 students, null on outcomes `MEASURED-RCT`
28. Kizilcec, Pérez-Sanagustín & Maldonado 2016, doi:10.1145/2876034.2893378 — null `MEASURED-RCT`
29. Ariely & Wertenbroch 2002, *Psych. Science*, doi:10.1111/1467-9280.00441 `MEASURED-RCT`
30. F6 §2 — SDT: autonomy best-in-class, competence conditional, **relatedness not suppliable** in the load-bearing part; §9 — Unprompted Return Rate
31. `survey/05-the-explanation-is-the-work.md` — Wang, Cheng & Mayer 2023: camera > 1 > 7 on transfer, lower pulse/anxiety/load, more idea units `MEASURED-RCT`
32. Kobayashi 2024, k = 39 — **g = 0.48 [0.34, 0.63]** with prior expectancy, **g = −0.02 [−0.14, 0.11]** without `MEASURED-META`; delivery adds g = 0.38
33. survey/05 §8 — no study compares an AI audience to a human audience; four search routes empty `OBSERVED`
34. survey/05 §9 — LLM-judge selection **−3.20pp / −1.68pp** vs test-based **+8.14pp** `MEASURED`; human code graders **Krippendorff's α ≈ 0.20** `MEASURED`
35. `research/raw/C3-slides-and-presentations.md` — deck vs chalk-and-talk **g = 0.067, 95% CI [−0.103, 0.236], k = 48** (Baker et al. 2018, doi:10.1016/j.compedu.2018.08.003) `MEASURED-META`
36. C3 §2.3–2.4 — verbal redundancy **g = 0.15 [0.08, 0.22]**, k = 57; text→audio **g = 0.29**; audio→text **g = −0.04 n.s.** (Adesope & Nesbit 2012, doi:10.1037/a0026147) `MEASURED-META`; the redundancy switch as a runtime decision procedure with three retrieved nulls against it
37. `research/raw/C1-illustration-generation.md` — the four gates G1–G4; L0–L4 tier ladder; **L2 is the floor for any figure shown to a learner**; **regeneration resets the tier**; Tier D prohibited
38. vTikZ — arXiv:2505.04670 — models *"struggle to reliably modify code in alignment with visual intent"*; edits more dangerous than first drafts `MEASURED-BENCH`
39. ALGOGEN — arXiv:2605.12159 — declarative IR + deterministic compiler, **82.5% → 99.8%** task success `MEASURED-BENCH`
40. Signalling **g = 0.43 [0.35, 0.50], k = 209** (Schneider et al. 2018); **r = 0.17**, concentrated in low-prior-knowledge learners (Richter, Scheiter & Eitel 2016, doi:10.1016/j.edurev.2015.12.003) `MEASURED-META`
41. `research/raw/F8-safety-privacy-children.md` — AI Act **Art. 5(1)(f)** verbatim; Art. 3(39)/3(34); **Art. 5(1)(b)** on age/disability vulnerability; Art. 26(11) disclosure; COPPA 16 CFR 312.2 voiceprints; the unresolved clickstream/"behavioural characteristics" question
42. `research/raw/N4-explanation-atlas.md` and `F10-explanation-laddering.md` — the misconception inventory and ladder rungs that Formats 3, 4 and 6 all consume

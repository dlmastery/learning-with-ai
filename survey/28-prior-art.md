---
title: "Prior Art — what thirty-five builds reveal, read as evidence and not as inspiration"
section: portfolio
status: draft
date: 2026-07-28
source_report: research/raw/D2-portfolio-case-studies.md
---

# Prior Art

One hundred and twenty-eight notebooks. Zero exercises.

That is not an impression. It is a programmatic scan of every markdown cell in three
sampled zero-to-hero notebooks, counting the strings a practice item would have to
contain:

| String | logreg | tabular_sota | stats_sota |
|---|---|---|---|
| "Exercise" | **0** | **0** | **0** |
| "Your Turn" | **0** | **0** | **0** |
| "Try it" | **0** | **0** | **0** |
| "Solution" | **0** | **0** | **0** |
| "Quiz" | **0** | **0** | **0** |
| "🧠 Intuition" | 12 | 13 | 5 |
| "✅ " | 46 | 14 | 36 |

The corpus is explanation, demonstration, and verification-by-the-author. The
learner reads and runs. **The learner is never asked to produce anything.** And the
method's own stated success criterion says so out loud: *"a student can narrate
every cell in a 1-hour video."*

Narrating is not retrieving. §24 and §08 establish what that distinction costs: the
two largest replicated effects in learning science are retrieval practice and
distributed practice, and this corpus contains neither. It is optimised, with real
craft and enormous discipline, for the felt sense of understanding.

---

## 1. What this section is, and what it may not be

This survey has a standing rule about this material and it is worth stating before
anything else.

The portfolio examined here belongs to this project's owner: roughly 35 active
repositories, nine live deployed apps and 128 notebooks, all inspected first-hand
by downloading the production JavaScript bundles and reading the shipped system
prompts. It arrives **last**, as validation, and it is **never** the seed
for what should be built.

The reason is measured and not stylistic. Research within this project found that
seeding a generator with examples produced **zero diversity gain** (p = .95, .89
and .49 across three comparisons) while anchoring moved **57–77% of
correct answers to wrong ones**. A portfolio shown to a generator before the
literature does not expand the design space. It collapses it, and it does so most
strongly on the items the generator would otherwise have got right.

So the question here is not "what should we build." It is the narrower and more
interesting one: **when a capable practitioner is handed frontier models and no
constraints, what actually gets built, and what reliably does not?**

---

## 2. What gets built: generation, six times over

Six of the nine deployed apps are the same machine with different prompts: a
single-page React app, the model called directly from the browser, structured JSON
out through a response schema, live bidirectional audio over a WebSocket, search and
URL grounding, text-to-speech, embeddings.

What that machine demonstrably does, in production, today:

- **Bidirectional live voice with a persona**, in six shipped apps, with barge-in
  handled through `interrupted` / `turnComplete` events, a hand-rolled client audio
  pipeline down to 16 kHz Int16 PCM, and playback scheduled at 24 kHz against a
  running cursor to avoid gaps.
- **Live bilingual transcripts**, with both input and output transcription enabled.
- **Mid-session language switching**, injected into the live stream as an
  instruction.
- **Tool calls that drive the interface mid-sentence.** The model narrates by voice
  while mutating application state.
- **Curriculum synthesis on demand**: any topic to a schema-constrained ten-chapter
  path in one call, conditioned on grade, location, culture, interests, dialect and
  stated goal.

The technical substrate §16 describes as newly available is not a research problem
for this practitioner. It is shipped, six times over. That is the first thing
the portfolio reveals that the literature does not: the field's discourse treats
multimodal tutoring as a frontier, and at the level of plumbing it is a solved
weekend.

Three design patterns recur and are worth naming because they were arrived at
independently.

Make generation legible. Every app narrates the model's work during a 10–40
second wait: "Architecting Learning Path…", "Clustering 50 Mastery Paths…",
"Validating Narrative Integrity…". Nothing hides behind a spinner. It is
genuinely good interface design for a latency that is not going away.

The schema is the pedagogical commitment. The flagship app's curriculum
generator enforces a JSON schema with `globalGifts[]`, provocation questions, a
peer collaborative challenge, showcase-based assessment, and a journaling prompt,
recognisably Froebel plus Reggio Emilia plus Socratic method, encoded as a type
rather than as an aspiration. A schema is a pedagogy you cannot quietly drop.

Personas are swapped at the system-instruction layer and nowhere else. The same
codebase ships as a Spanish course, a Telugu course, a Bhagavad Gita app, a Sanatana
Dharma app and an Ayurveda app, differing in one string.

---

## 3. What does not get built

### 3.1 The mode switch with no policy

The flagship app ships three distinct live-session personas as separate system
instructions: Lecturer ("start with a 2–3 minute comprehensive discourse…"),
Socratic ("answer questions by asking leading questions"), and Examiner
("conduct an interactive oral quiz… evaluate the student's response and provide
feedback").

Mode-switching between lecture, dialogue and assessment is already implemented.
What is missing is any policy for when to switch. The learner picks. No mastery
estimate drives the choice.

That is §22's central argument, rediscovered from the other end by someone building
rather than reading. The hard part was never generating the three modes. It was
knowing which one fires, and that requires a measurement nobody took.

### 3.2 The signal that is emitted and discarded

The language portals declare function calls as their assessment channel during live
voice sessions:

```
provide_feedback(score, feedback, suggestion)   → "Accuracy score from 1 to 10."
mark_word_practiced(word)                       → "Mark a vocabulary word as
                                                   successfully practiced and mastered."
```

This is **the only place in the entire portfolio where the model emits structured
evidence of learner state.** `mark_word_practiced` is a one-bit mastery signal and
it is exactly the right primitive.

It is written to nothing. There is no persistence layer in those bundles. The
mastery signal is discarded at page reload.

And the sharpest version of the same gap: cross-session memory exists in this
portfolio. A meditation app injects *"CONTEXT FROM PREVIOUS SESSIONS"* into every
live session from a Firestore-backed store, alongside affect-conditioned pacing that
slows down when the user sounds anxious. A separate research-agent codebase solves
the memoryless-collaborator problem again, with an explicit thesis that *"the
repository is the memory."*

The same author solved cross-session memory twice, once for meditation and once for
a machine-learning agent, and shipped it in neither of the tutors.

§11 argues that persistent learner state is the load-bearing component of an AI-native
learning system. This is what its absence looks like in built artefacts, from
someone who demonstrably knew how to build it.

### 3.3 Assessment lives in a different repository

The one instrument in the corpus with real practice structure is **one notebook out
of 128**: an interview gauntlet with 29 trap markers and 31 follow-ups, structured
*question → intuition → rigorous answer → code check → follow-ups*. The
exam-prep notebook contains 36 problems in a strict four-beat format, mapped to
textbook exercises and cross-checked against the official solutions manual, and
the solution sits immediately below every problem. No hidden answer, no attempt
gate, no self-grading.

Meanwhile a companion repository carries graded rubrics and reflection prompts for
all 197 lectures of a full curriculum. **The assessment layer was written. It was
never wired to an artefact.**

---

## 4. The finding that generalises: enforcement beats intention

This is the most transferable result in the portfolio, and it comes from comparing
two bodies of work by the same author under the same standards.

The teaching corpus states its quality rules. Sixteen non-negotiables, including
some that this survey would endorse verbatim: *"no jargon before it's grounded"*,
with a term-grounding verifier that flags every term whose first use precedes its
plain-language explanation; *"no formula verbatim — a formula stated with no
build-up is a defect"*; *"prove it AND verify it"*, every derivation shown in LaTeX
and confirmed numerically.

The research corpus compiles its rules into regexes, word floors, SHA-256
fingerprints, and independent audit agents that exit non-zero with no bypass flag.

Then look at what happened to each.

Where the rule is a norm, it drifted. Hiding code cells is declared "non-negotiable"
by the governing method and is set on no code cell in any notebook sampled,
including the ones the rule specifically governs. Two deployed apps ship the wrong
page title — a Spanish course and a Bhagavad Gita app both serve
`<title>Sanatana Dharma AI Portal</title>`. Five apps share a byte-identical
stylesheet, so a Spanish learning portal ships with saffron, gold and mandala
styling. One repository disagrees with itself about which model it uses across the
README, the agent instructions, and two source files.

And the drift reached production. **Six of seven bundles ship a literal placeholder
API key string**, one of them at six call sites covering the lesson generator, the
live teacher, TTS, speech and the writing lab — which means that app's **core lesson
generation is non-functional in production**. The parent app had the fix. The fork
did not receive it.

Where the rule is a gate, it held: **112/112 forensic audit passes**, and 82 of 112
tasks beating a published benchmark, in the corpus whose rules exit non-zero.

> **A survey advocating AI-generated curricula must advocate gates, not guidelines.**

That is the sentence this section contributes, and a natural experiment earned it.

---

## 5. The nulls

The specified constraint set was abandoned wholesale. The flagship app's own
product requirements document targets rural learners on low-end Android devices,
on-device inference offline the great majority of the time, a small initial download,
solar-friendly operation, and a hundred low-resource languages. What shipped is an
online-only single-page web app whose voice path requires a persistent WebSocket and
whose audio capture uses a deprecated main-thread API, in *every* app in the
portfolio, that will glitch on precisely the target device. The design research
document runs to 78.5 KB. **Every hard constraint was dropped and the easy 20% was
built.** That gap is more useful to this survey than a success story would be, and it
is the single most honest datum in the report.

**Local generative video is not viable as a tutor avatar, and the code says so
itself.** The locally written streaming demo carries this note in its own source:

> *"HONESTY: this is NOT a real-time interactive avatar. It is a low-FPS (~1.8 FPS
> on this GB10, arm64, no flash-attn/TensorRT) video-to-video style transfer
> stream."*

That is a model of calibrated claiming, and the verdict follows from it:
asynchronous generated lesson media, streamed progressively, is available now; a
live generated avatar is not.

Nothing was evaluated. No A/B test, no learning-outcome measurement, no user
study, no telemetry beyond a token counter, across nine deployed apps and 128
notebooks. An analytics project exists in the same environment and is unused for
this purpose. §27 records the same pathology in the same owner's commercial product,
independently.

Grounding is applied uniformly where it should be applied selectively. Web-search
grounding is switched on identically for logistic regression and for Ayurvedic health
guidance delivered in the voice of a deity. No source allowlist, no provenance
display, no medical disclaimer in the extracted strings. One app in the set asserts
uncited clinical statistics as fact — *"diagnostic simulation benchmarks outperform
junior residents in 8/10 categories"* — with no citation mechanism anywhere in the
bundle. §13 argues that correctness must live in a verifier and not in the
generator; this is what the alternative ships as. **The same portfolio contains a
codified "citation rigor" discipline. It is not applied to the consumer apps.**

---

## 6. The objection

*If the portfolio's gaps are the same gaps the literature already identified, what
did reading it add?*

Three things the literature does not supply.

A measured asymmetry in agentic content production. Independent artefacts
parallelise freely — "the 5 above were built by 5 concurrent agents." Enhancement
passes on a *single* artefact are constrained to at most two agents on
non-overlapping regions, with the orchestrator performing the inserts sequentially,
because two agents editing one notebook corrupts it. That is an operational finding
you only get by doing it, and it governs how any of this survey's proposals would
actually be produced.

A working closed loop over curriculum coverage. A programmatic keyword audit of
every notebook against every subsection of the reference textbook produced a
pass/warn/fail verdict per chapter, found a real gap (a named list of clustering
algorithms entirely missing), generated an action item, and the gap-fill notebook was
then built. **Audit → gap → targeted build → re-audit is the one place in the whole
portfolio where an automated signal changed the curriculum**, and it is a template
anyone can copy.

A typed contract for what an AI tutor should expose. One repository enumerates
32 features as a typed interface — onboarding, streaming chat, levelled hints, mode
switching, image generation, speech in and out, multi-agent classroom and debate,
whiteboard construction, learner-model read and write, progress and achievements,
group mode — with a mock implementation proving the shape is coherent. The deployed
app implements roughly eight of the thirty-two. A specification written before
the implementation, with the implementation gap visible in the same repository, is a
more useful artefact than either half alone.

---

## 7. What thirty-five builds oblige us to do

- **The portfolio is evidence, never a seed.** Zero measured diversity gain from
  example-seeding; 57–77% correct→wrong movement under anchoring. It arrives after
  the literature, or it does not arrive.
- **Generation is not the bottleneck.** Six shipped live multimodal tutors say so.
  State is the bottleneck: knowing what the learner knows, keeping it, acting on it.
  Every gap in this portfolio reduces to that one.
- **Ship gates, not guidelines.** Where rules were norms they drifted into production
  breakage; where rules were executable and exited non-zero, they held at 112/112.
- **A schema is a pedagogy that cannot be quietly dropped.** Prefer encoding a
  commitment as a type over stating it in a prompt.
- **Emit the learner-state signal into a store, not into the void.**
  `mark_word_practiced` is the right primitive and it was written to nothing.
- **Ground selectively, and display provenance.** Uniform web grounding across a
  maths lesson and a health claim is not a grounding strategy.
- **Instrument before you narrate.** Nine apps, 128 notebooks, zero outcome
  measurements — and the same absence appears independently in §27.
- **Publish the gap between the requirements document and the deployment.** Ours is
  large, it is in this section, and stating it is the only thing that makes the rest
  of the section credible.

The portfolio's most valuable property is that it was built by someone who knew the
right answers. The rules were written down. The verifier was coded. The memory layer
was shipped — for meditation. The assessment rubrics exist — in another repository.
Every component of the system this survey describes is present somewhere in these
thirty-five repositories, and none of them are wired together.

That is the finding. Not that builders do not know what to build, but that under
no external gate, the parts that get finished are the parts that demo — and the parts
that measure whether anyone learned are the parts that are always about to be built
next.

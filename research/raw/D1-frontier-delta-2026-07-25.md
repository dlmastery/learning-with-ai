---
title: "Frontier delta, 25 July 2026: the universal AI mentor is now a deployment problem"
wave: D
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 44
supplements: "research/raw/D1-frontier-quarter.md"
---

# D1 supplement — the universal AI mentor frontier

## Executive finding

The interrupted D1 pass found a fast-moving model frontier but concluded that it
had moved learning very little. That conclusion is now too pessimistic. It
underweighted several developments that were either missed, newly indexed, or
released while the earlier pass was being assembled:

1. **The learning outcome evidence is no longer a single isolated result.**
   A pre-registered Gemini Guided Learning trial in Sierra Leone found a
   **+0.258 SD** intent-to-treat mathematics effect across 1,763 students
   (`MEASURED-RCT`). A World Bank randomized trial in Nigeria found
   **+0.31 SD** after six weeks of teacher-supported generative-AI tutoring
   (`MEASURED-RCT`). A July 2026 experiment found **+0.27 SD** on an immediate
   unaided knowledge test and persistence one week later (`MEASURED-RCT`).
   These are not engagement metrics and they are not model benchmarks.
2. **A general-purpose consumer product now implements much of the adaptive
   loop.** Gemini Study Notebooks diagnoses a learner, decomposes a goal into
   more than 100 objectives, generates short lessons and quizzes, updates a
   skill dashboard, and syncs with source-grounded NotebookLM
   (`VENDOR`, shipping product). This is much closer to a tutor than a chatbot.
3. **Natural, multilingual conversation is now a real model capability.**
   GPT-Live is full-duplex and can listen while speaking; Gemini Live Translate
   supports more than 70 spoken languages and 2,000 language pairs; open models
   now cover local audio, vision, and reasoning on consumer hardware
   (`VENDOR` and `MEASURED-BENCH`, not learning-outcome evidence).
4. **The price floor collapsed further than the original report captured.**
   DeepSeek V4 Flash lists **$0.14/M uncached input and $0.28/M output**, with
   1M context; a cache hit is $0.0028/M input. Gemini 3.5 Flash-Lite is
   $0.30/$2.50 and half that in batch. Open-weight Gemma 4 E2B/E4B targets
   phones and laptops. Sarvam Edge runs a sub-1GB speech/translation stack for
   all 22 scheduled Indian languages locally (`VENDOR`; prices are current
   first-party price sheets).
5. **The newest tutoring research rejects one universal interaction style.**
   Pure answer withholding is not the whole answer. A July field deployment
   with Chinese junior-high students found that learners under exam pressure
   resisted conventional Socratic dialogue and used answer-first worked
   examples as diagnostic checkpoints (`OBSERVED`, n=12). Across 16,851
   programming-tutor interactions, verification feedback produced the highest
   productive continuation, but the association was small and context
   dependent (`OBSERVED`). The product needs a *policy router*, not a slogan.

The revised thesis is therefore:

> **As of 25 July 2026, an excellent AI mentor is technically buildable and
> economically deployable. The unsolved problem is not whether a language model
> can explain school material. It is the systems work required to give every
> learner a persistent, source-grounded, multilingual, multimodal mentor that
> selects the right teaching mode, works on weak connectivity, and escalates
> difficult cases intelligently.**

This is a capability-positive conclusion. It does not depend on incumbent
education-industry claims, and it does not treat the failure modes of early
chatbots as a ceiling on current models.

---

## 1. Corrections to the interrupted frontier pass

### 1.1 Claims that remain valid

- `MEASURED-BENCH`: general solving ability and measured tutoring behavior are
  only partially aligned. On eight public MathTutorBench models the reported
  correlation was **r = 0.421**. A strong solver is not automatically a strong
  tutor.
- `INFERENCE`: the pedagogy layer remains a product/control-plane responsibility.
  A raw model endpoint does not supply curriculum, learner state, source
  provenance, age policy, progress measurement, or a teaching-mode controller.
- `VENDOR`: full-duplex voice, low-cost inference, open multimodal models, and
  long context are real enabling capabilities. Vendor benchmarks do not prove
  that any one of them causes learning.
- `MEASURED-RCT`: delayed, unaided learner performance remains the important
  outcome. Immediate task completion alone cannot distinguish learning from
  delegation.

### 1.2 Claims that this supplement rescinds or narrows

**“No vendor will sell you a tutor.” — Rescinded.** Google now ships Study
Notebooks as an “interactive, adaptive learning platform.” The product performs
diagnosis, objective decomposition, lesson generation, quizzes, progress
tracking, and next-lesson recommendation. Its efficacy as an integrated product
has not been published, so it is `VENDOR`, but it is plainly a tutor-shaped
consumer product rather than an empty chat surface.

**“The frontier moved learning very little.” — Rescinded.** In the April–July
window, the Sierra Leone result, Study Notebooks, full-duplex GPT-Live, 70+
language live translation, cheap/open multimodal models, and new evidence about
mode selection collectively change what can be built and where it can be
deployed.

**“Long context does not matter.” — Narrowed.** Long context is not a substitute
for retrieval, citations, or a learner model. It does matter operationally for
maintaining a live lesson, a curriculum graph, source excerpts, accommodations,
and recent learner history without repeatedly compressing away decisive
details. The correct conclusion is: *long context is useful capacity, but not a
grounding or memory architecture*.

**“Better mathematics is near-zero for learning.” — Rescinded.** Better formal
reasoning does not select a pedagogy, but it raises the correctness ceiling for
advanced mathematics, proof checking, synthetic practice generation, and
verification. Leanstral 1.5 cannot diagnose a child's misconception by virtue of
solving Putnam problems; it can serve as a specialist verifier inside the
mentor. In a routed system, specialist capability matters without pretending it
is pedagogy.

**“Teaching mode is the active ingredient.” — Updated.** Requiring learner
thought is important, and the July 2026 Zhongkao field study shows that
strategically exposing a worked answer can enable inspection and local repair.
The active ingredient is **adaptive control over when to ask, hint, model,
reveal, verify, retrieve, or escalate**.

---

## 2. What is actually buildable on 25 July 2026

### 2.1 Frontier reasoning and agents

| Capability | Current evidence | Learning consequence |
|---|---|---|
| GPT-5.6 Sol/Terra/Luna | `VENDOR` — global API availability; 1.05M context on Luna; multi-agent beta; explicit cache breakpoints; $5/$30, $2.50/$15, $1/$6 | Use Sol only for difficult synthesis or verification; Terra/Luna can run routine mentor-agent work. |
| Claude Opus 5 | `VENDOR` / vendor-run benchmarks — $5/$25, 1M context, interactive artifact generation, stronger self-verification and long-horizon execution | Generates and iterates interactive learning objects; useful as high-capability author/verifier. |
| Claude Sonnet 5 | `VENDOR` — $2/$10 introductory, then $3/$15; agentic tool use; Free-plan default | A practical mid-tier orchestration and artifact model. |
| Gemini 3.6 Flash | `VENDOR` / vendor-run benchmarks — production model emphasizing token efficiency, coding, and planning | Low-latency control plane and dynamic-content engine. |
| Gemini 3.5 Flash-Lite | `VENDOR` — $0.30/$2.50 standard, $0.15/$1.25 batch; free tier | High-volume question generation, classification, routing, translation, and feedback. |
| DeepSeek V4 Flash | `VENDOR` — open weights, 13B active, 1M context, $0.14/$0.28; $0.0028 cached input | The current price disruption: cloud reasoning can be cheaper than premium speech. |
| Qwen3.6-35B-A3B | `VENDOR` / vendor-run benchmarks — open model, 3B active, multimodal, thinking/non-thinking | A small-active-parameter regional/edge specialist with Chinese ecosystem support. |
| Gemma 4 E2B/E4B/12B | `VENDOR` / vendor-run benchmarks — open, 140+ pretraining languages, image/audio input, 128K–256K context; phone-to-laptop targets | A viable local mentor core when privacy, connectivity, or sovereignty forbids a cloud-only product. |
| Sarvam 30B/105B | `VENDOR` / vendor-run benchmarks — open weights, Indian-language reasoning and agentic use, trained in India | Sovereign high-quality Indian-language model tier rather than translation through English. |

No row in this table is a learning outcome. The architecture uses these models
as interchangeable cognitive components beneath a stable learner experience.
The learner should not have to know or care which model handled a turn.

### 2.2 Conversation is no longer a turn-taking text box

**GPT-Live** (`VENDOR`) listens and speaks at the same time, can backchannel,
pause, remain silent while the learner thinks, invoke tools many times per
second, and delegate hard reasoning to a frontier model without ending the
conversation. More than 150 million people already use ChatGPT voice or
dictation weekly. The free tier receives GPT-Live-1 mini. At launch the API is
still “soon,” and GPT-Live does not combine voice with video or screen sharing.
Those are shipping constraints, not evidence that full-duplex tutoring is
impossible.

**Gemini 3.1 Flash Live** (`VENDOR`) is available through the API for real-time
audio dialogue. Published pricing is $0.005 per input audio minute and $0.018
per output audio minute. **Gemini 3.5 Live Translate** (`VENDOR`) automatically
detects and translates more than 70 languages across 2,000+ pairs while
preserving intonation, pacing, and pitch.

**Sarvam Edge** (`VENDOR`) reports a fully local, sub-1GB recognition,
translation, and synthesis stack across all 22 scheduled Indian languages, with
a 128 ms example end-to-end pipeline. **Meta Omnilingual ASR** (`VENDOR` /
vendor-run benchmarks) open-sources recognition for 1,600+ languages, including
500 low-resource languages not previously transcribed by AI. **Voxtral Mini**
(`VENDOR` / vendor-run benchmarks) is a 3B model intended for local and edge
speech understanding; Voxtral TTS is a 4B multilingual, low-latency voice model
with open weights for a non-commercial reference-voice version.

`INFERENCE`: Voice is not a cosmetic layer. It is the primary access interface
for young learners, people with limited literacy, phone-first users, and
languages for which typing is cumbersome or poorly supported. A universal
mentor that starts with English text and “adds localization later” is not
universal.

### 2.3 The mentor can see, read, draw, and build

- **Mistral OCR 4** supports 170 languages, returns bounding boxes, block types
  and confidence, and can be self-hosted in one container (`VENDOR` /
  vendor-run benchmark). This converts a photographed local worksheet or
  textbook page into citation-ready source blocks.
- **Gemma 4** accepts text, image, audio, and—in documented usage—video frames.
  E2B and E4B target mobile devices and laptops (`VENDOR`).
- **Qwen-Image 3.0** can render dense layouts, exam papers, storyboards,
  infographics, small text, and 12 scripts (`VENDOR`). This is relevant to
  instant localized worksheets and visual explanations, not proof of their
  correctness.
- **Claude Opus 5** demonstrates generated interactive artifacts including a
  wind tunnel and an explorable cell (`DEMO`). The significance is not the two
  demos themselves; it is that an agent can now author, inspect, run, and
  revise a manipulable explanation in one workflow.
- **ChatGPT dynamic visual explanations** cover more than 70 core mathematics
  and science concepts (`VENDOR`, shipping product), making variables and
  formula relationships manipulable rather than merely described.
- **Gemini Study Notebooks** says interactive visualizations will enter lessons
  later in summer 2026 (`VENDOR`, announced rather than shipped at the cutoff).

`INFERENCE`: The best 2026 tutoring surface is generated on demand. It can
switch from speech to a number line, from a number line to a simulation, from a
simulation to a worked example, and then to an unassisted probe. A static course
catalog is a source library, not the learner experience.

---

## 3. The latest outcome evidence is capability-positive

### 3.1 Sierra Leone: a frontier tutor produced measured mathematics gains

The strongest current direct result is Google's pre-registered classroom trial
(`MEASURED-RCT`):

- **N = 1,763**, grades 7 and 8, 48 classrooms in 12 government-supported
  schools in Port Loko District.
- Guided Learning versus regular classwork, with local teachers leading the
  intervention.
- **Intent-to-treat effect: +0.258 SD** on an externally validated mathematics
  assessment. The technical report gives a wide 95% confidence interval of
  approximately **[0.027, 0.488]**.
- More than 113,000 interactions were analyzed; 91.4% were classified as
  conceptual learning, model responses used scaffolding questions 76% of the
  time, and direct solutions 2%.
- 69% of treatment students met the intended usage target.

This is not “AI replaces school.” Teachers set objectives, designed lessons,
managed paired device use, and facilitated the class. It is evidence that
frontier AI can expand the amount of individualized guided practice a teacher
can deliver.

**Equity warning, not a dismissal.** The technical report found larger gains
for students who entered with stronger mathematics scores. A universal mentor
must therefore optimize *gain among initially behind learners*, not merely
average gain. The fact that an intervention worked and distributed benefits
unequally is a design target, not a reason to retreat to a system that already
leaves those learners behind.

### 3.2 Nigeria: a cheap general model worked in a resource-constrained setting

The World Bank trial in Edo State (`MEASURED-RCT`) used Microsoft Copilot
powered by GPT-4 in a six-week, teacher-supported after-school program. It found
**+0.31 SD** on a combined assessment containing English, AI knowledge, and
digital skills, with positive effects on the primary English outcome and on
regular end-of-year curricular exams. The intervention involved about 800
first-year senior-secondary students.

The authors explicitly state that the study cannot isolate the chatbot from the
teacher, structured prompts, scheduled sessions, and implementation support.
That is not a flaw in the universal-mentor vision. It is evidence that the
*deployable unit is a system*, not a naked model.

### 3.3 July 2026: learning persisted after the model was removed

Contractor and Reyes (`MEASURED-RCT`, preprint) randomized undergraduates
learning an unfamiliar topic with or without off-the-shelf generative AI:

- AI access raised immediate unaided knowledge-test scores by **0.27 SD**.
- Gains persisted one week later.
- Learners who used AI for explanation (“augmentation”) showed stronger delayed
  gains than those who used it to generate text (“automation”).
- Students shifted time from drafting to reading/search and reported greater
  enjoyment.

This directly shows that access to a general generative model can produce
retained learning. The usage policy and learner behavior shape the size of the
gain.

### 3.4 AI can narrow expertise gaps rather than merely amplify advantage

Cruces et al. (`MEASURED-RCT`, NBER working paper, N=1,174 adults) found that a
generative-AI assistant increased performance at every education level and
reduced the higher- versus lower-education performance gap from **0.548 SD to
0.139 SD**—about three quarters. Treated participants did not perform worse
when AI was removed, and lower-education participants retained part of the
gain. High performance plus later retention was strongest when intensive AI
use was paired with sustained human effort.

This is not a school tutoring trial, but it is highly relevant to the “no child
left behind” mechanism: capable assistance can disproportionately help those
who begin with less formal preparation.

### 3.5 Other 2026 evidence points in the same direction

- LearnLM + Eedi (`MEASURED-RCT`, exploratory, N=165, five UK schools) reported
  that AI-supported learners were **5.5 percentage points** more likely than
  human-tutor-only learners to solve novel subsequent-topic problems.
- Khan Academy implementation support in 83 residential government middle
  schools in Uttar Pradesh (`MEASURED-RCT`, not generative AI) increased weekly
  use from 7.2 to 47.4 minutes and mathematics achievement by almost
  **0.5 SD**. The result says deployment fidelity can dominate nominal software
  availability.
- The World Bank's July 2026 Peru program (`OBSERVED` deployment plus a
  separate teacher-training RCT) has reached about 4,500 students in 85 public
  schools with an AI mathematics tutor and career coach. Outcome estimates for
  the student tutor were not published on the results page.

The accumulated evidence does not prove that every chatbot teaches. It is now
enough to reject the claim that excellent, scalable AI tutoring is speculative.

---

## 4. The 2026 pedagogical frontier: a mode router

Current research supports neither “always answer” nor “always be Socratic.”
The tutor needs a controller that chooses among modes.

### 4.1 What the newest interaction data says

| Study | Current result | Design implication |
|---|---|---|
| Yao et al., *Teach or Solve* | `MEASURED-BENCH`: solving/pedagogy correlation **r=.421** across eight models | Evaluate the deployed teaching policy separately from model intelligence. |
| Abrar et al., 16,851 programming interactions | `OBSERVED`: verification feedback had 82.4% productive continuation; direct answers 62.7%; associations small (Cramér's V .078/.087) | Verification is a strong default, but response policy must use context. |
| Neagu et al., 9,490 chats | `OBSERVED`: real learners often bypass scaffold scripts; uptake differs from benchmark assumptions | Treat learner direction as signal, not disobedience. |
| Feng et al., Zhongkao deployment | `OBSERVED`, n=12: students resisted slow Socratic dialogue under pressure and used answer-first worked examples diagnostically | Reveal can be pedagogical when followed by inspection, local repair, and delayed retrieval. |
| CSTutorBench | `MEASURED-BENCH`: family/instruction tuning predicted tutor quality better than size in a small 11-model sample; a prompt revision improved 10/11 | Cheap/local models can tutor well with a tested control prompt. |
| DeepTutor | `MEASURED-BENCH`: agentic open-source architecture couples source grounding, learner memory, calibrated question generation, and proactive skills | Personalization is a system substrate shared by agents, not a style adjective. |

### 4.2 Proposed control policy

`INFERENCE` — each turn should be routed among these actions:

1. **Diagnose** — ask for the learner's attempt, confidence, or explanation.
2. **Hint** — provide the smallest cue likely to unlock the next step.
3. **Model** — show a complete worked example when the learner lacks a usable
   schema or when time pressure makes unguided discovery counterproductive.
4. **Inspect** — require the learner to label or explain the worked example.
5. **Repair** — isolate the exact incorrect step, then retry only that step.
6. **Verify** — use tools, sources, a calculator, code, or a specialist model.
7. **Retrieve** — later, remove the support and ask for unassisted performance.
8. **Transfer** — change surface features and require use in a new context.
9. **Escalate** — hand to a stronger model, teacher, parent, or specialist.

The controller optimizes for the learner doing progressively more of the work,
not for the tutor saying progressively less. That distinction reconciles the
positive Guided Learning results with the newest field evidence against rigid
Socratic scripts.

---

## 5. Architecture for an expert mentor for every learner

The universal system is a **mentor mesh**, not one enormous model assigned to
every child.

### Tier 0 — device-resident continuity

Runs without a network connection:

- learner profile, consent state, skill graph, prior attempts, and review queue;
- a small multilingual model where hardware permits (Gemma 4 E2B/E4B,
  Qwen3.6 A3B-class, or a regionally tuned model);
- local speech, translation, and synthesis (Sarvam Edge in India; open ASR/TTS
  equivalents elsewhere);
- downloadable national/local curriculum packs with signed provenance;
- calculator, code runner, interactive canvas, and deterministic simulations;
- encrypted event log that syncs when connectivity returns.

This tier makes “offline” a degraded intelligence state, not a no-learning
state.

### Tier 1 — commodity cloud mentor

Handles most live turns:

- DeepSeek V4 Flash, Gemini Flash-Lite, GPT-5.6 Luna, a hosted open model, or a
  sovereign regional equivalent;
- curriculum retrieval and citation;
- question/hint generation, feedback, translation, OCR, and mode selection;
- continuous updates to the learner hypothesis;
- asynchronous preparation of the next lesson and spaced review.

This is where near-zero marginal cost becomes practical. A universal system
must route routine classification and generation away from frontier models.

### Tier 2 — frontier specialist

Invoked for the minority of turns requiring:

- hard mathematical or scientific reasoning;
- deep source synthesis;
- generation and verification of a new interactive explanation;
- resolving disagreement among cheaper models;
- novel misconceptions or exceptional learner needs.

GPT-5.6 Sol, Claude Opus 5/Fable-class models, top Gemini models, Leanstral for
formal proof, and discipline-specific agents belong here. The learner experiences
one mentor; the system silently assembles expertise.

### Tier 3 — human relationship and accountability

Reserved for decisions that should not be automated:

- safeguarding, suspected abuse, self-harm, and acute distress;
- medical, disability, or psychological diagnosis;
- legally consequential accommodations or placement;
- persistent non-response to multiple instructional pivots;
- conflict involving family, school, or local cultural context;
- the relationship, encouragement, and community that a child needs from people.

Humans are not a throughput bottleneck in this design. AI absorbs routine
explanation, practice, translation, planning, and feedback so scarce human time
is spent where human authority or relationship is uniquely valuable.

### One state, many specialists

All tiers read and write one inspectable learner state:

```yaml
learner:
  goals: []
  language:
    preferred_spoken: null
    preferred_written: null
    code_switch_patterns: []
  access:
    device_class: null
    connectivity: offline|intermittent|online
    modalities_available: []
  concept_state:
    - concept_id: null
      evidence:
        independent_accuracy: null
        explanation_quality: null
        transfer_accuracy: null
        last_unassisted_at: null
      misconceptions: []
      support_level: model|hint|prompt|independent
      next_review_at: null
  accommodations: []
  provenance_preferences: []
  corrections_by_learner_or_guardian: []
```

The state is a hypothesis that the learner and guardian can inspect and correct,
not a hidden permanent score.

---

## 6. The global deployment evidence already spans continents

### Africa

- Nigeria: +0.31 SD in a six-week teacher-supported generative-AI trial
  (`MEASURED-RCT`).
- Sierra Leone: +0.258 SD mathematics with Guided Learning across 12 schools
  (`MEASURED-RCT`).
- UNESCO reports an offline-first Ethiopian learning deployment reaching more
  than 200,000 learners across 200 towns (`OBSERVED`, program report).

### India

- Google's ATL Saathi begins with a 100-school pilot inside the Atal Tinkering
  Lab network, which reaches 11 million students; eight languages launch first
  (`VENDOR`; pilot, no outcomes yet).
- The Uttar Pradesh Khan Academy experiment found almost +0.5 SD when schools
  received dedicated implementation support (`MEASURED-RCT`).
- Sarvam has released sovereign 30B/105B open models, 22-language speech and
  translation, and a fully local edge stack (`VENDOR` / vendor-run benchmarks).
- India's NITI Frontier Tech portal reports a low-bandwidth, 2G-compatible
  human-AI tutoring service reaching 285,000 students (`OBSERVED`; the portal's
  pass-rate claims are not randomized and must not be read as causal effects).

### China

- China's five-ministry “AI + Education” action plan makes AI integration a
  national system priority (`GOVERNMENT-POLICY`).
- Daxing'anling's 2026–2028 implementation plan explicitly targets remote
  schools, personalized learning, AI lesson planning, assessment, tutoring,
  teacher training, and rural/urban resource sharing (`GOVERNMENT-POLICY`).
- Qwen3.6-35B-A3B supplies an open, 3B-active multimodal reasoning model;
  Qwen-Image 3.0 supplies dense, multilingual educational artifact generation
  (`VENDOR`).
- The July Zhongkao field study provides direct learner-interaction evidence
  from a Chinese high-stakes context (`OBSERVED`).

### Latin America

- The World Bank reports deployment of an AI mathematics tutor and career coach
  to 4,500 students in 85 public schools in Lima, plus AI-supported school
  leadership work across several countries (`OBSERVED`; student outcome estimate
  pending).

The universal-mentor program should therefore not be framed as a US product
exported after it matures. Model, speech, curriculum, device, and governance
layers should be co-built regionally from the start.

---

## 7. Economics: intelligence is becoming the cheap component

Current first-party prices, per million tokens:

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| DeepSeek V4 Flash | $0.14 | **$0.0028** | $0.28 |
| Gemini 3.5 Flash-Lite | $0.30 | $0.03 | $2.50 |
| GPT-5.6 Luna | $1.00 | $0.10 | $6.00 |
| Claude Sonnet 5 (introductory) | $2.00 | not verified here | $10.00 |
| GPT-5.6 Sol | $5.00 | $0.50 | $30.00 |
| Claude Opus 5 | $5.00 | not verified here | $25.00 |

Batch Gemini Flash-Lite is $0.15/$1.25. Groq lists Whisper Large v3 Turbo
transcription at **$0.04 per audio hour**. Gemini 3.1 Flash Live lists audio at
$0.005/minute input and $0.018/minute output. Fully local speech has no per-use
API cost.

The detailed tutoring-hour arithmetic remains in F4. This supplement changes
the model mix: the newest DeepSeek price is substantially below the cheap-cloud
tier used there. `INFERENCE`: with an on-device continuity layer, a commodity
model for most turns, cache reuse, and frontier escalation for a small fraction,
the intelligence cost of a high-quality mentor can fall below the costs of
device amortization, connectivity, electricity, teacher training, and local
implementation.

That is the opportunity. “AI is cheaper than a teacher” is the wrong comparison.
The relevant question is whether AI can give a teacher responsible for 40–80
learners the individualized explanation, practice, translation, and diagnostic
capacity that previously required dozens of additional experts. Current
evidence says yes, provided the system is deliberately implemented.

---

## 8. Negative findings and open falsification tests

A capability-positive report still has to identify what would prove its claims
wrong.

1. **Sierra Leone confidence interval is wide**, the trial was short, and
   stronger entrants benefited more. Replication must show gains for initially
   behind learners and persistence after months, not only weeks.
2. **Nigeria is a system treatment.** It does not isolate model, teacher,
   schedule, prompt, or digital-literacy components.
3. **Study Notebooks has no published product-level RCT.** Its adaptive UI is a
   capability claim, not efficacy evidence.
4. **No direct RCT found here tests full-duplex voice against text or
   turn-based voice on delayed learning.**
5. **No direct RCT tests the full mentor mesh**—local model, cheap router,
   frontier specialist, persistent learner state, and human escalation.
6. **Low-resource language coverage is not language quality.** “1,600
   languages supported” must be followed by native-speaker comprehension,
   pedagogy, accent, code-switching, and cultural evaluations.
7. **A mode router can be wrong.** Too much scaffolding frustrates goal-directed
   learners; too little support strands novices. Its decisions need randomized
   evaluation against delayed independent performance.
8. **A generated interactive explanation can be persuasive and false.**
   Executable simulations must expose equations/assumptions and be verified
   against deterministic tests or authoritative sources.
9. **Connectivity remains unequal.** ITU estimates 2.2 billion people remained
   offline in 2025 even though mobile-broadband coverage was nearly universal.
   A cloud-only mentor excludes many of the learners in the north star.
10. **Deployment can reproduce inequality.** The universal claim fails if
    initially advanced learners compound faster while lower-attaining learners
    receive a cheaper, less capable tier.

Pre-registered outcome tests for a reference implementation:

- delayed unaided mastery by concept;
- novel transfer, not repeated-question accuracy;
- gain by initial attainment, gender, language, disability, and rurality;
- false-teaching rate per learner-hour;
- time from misconception detection to verified repair;
- hours of useful tutoring per dollar, watt-hour, and gigabyte;
- completion and return without coercive engagement design;
- teacher time shifted from routine production to human judgment/relationship;
- percentage of sessions that remain useful during total network loss.

The universal-mentor thesis should be rejected if the routed system cannot beat
a strong classroom/control condition on delayed independent performance, or if
its gains systematically concentrate among learners already ahead.

---

## 9. Immediate project implications

1. **Make the north star explicit:** an expert AI mentor for every learner, in
   the learner's spoken language, on the device and network they actually have.
2. **Adopt a teaching-mode router.** Asking, hinting, worked-example reveal,
   verification, retrieval, and escalation are all legitimate actions selected
   for the learner and moment.
3. **Build an offline-first learner-state and curriculum core.** Cloud accounts
   are optional accelerators, not the identity system.
4. **Separate model certification by role.** Evaluate cheap models for routine
   tutoring actions, specialist models for subject correctness, voice models
   for language access, and the router for learning outcomes.
5. **Treat multilingual speech as core architecture.** Start with African,
   Indic, Chinese, and code-mixed use cases, not translated English demos.
6. **Generate learning objects dynamically.** Explanations should be able to
   become diagrams, manipulatives, simulations, worked examples, stories, or
   local analogies, each source-grounded and testable.
7. **Measure distributional gain.** “Average +0.26 SD” is insufficient if the
   lowest baseline group gains least.
8. **Use frontier models sparingly but unapologetically.** The system exists to
   deliver expert help. Cost routing should make the best available reasoning
   accessible at the moment it is genuinely needed.

---

## Source ledger

All links were accessed on 25 July 2026. Vendor/model pages support capability
and pricing claims only unless a separate human-outcome study is named.

1. OpenAI, [GPT-5.6](https://openai.com/index/gpt-5-6/) — model tiers,
   multi-agent API, availability, official pricing.
2. OpenAI, [GPT-5.6 Luna model card](https://developers.openai.com/api/docs/models/gpt-5.6-luna)
   — 1.05M context, cache and token pricing.
3. OpenAI, [Introducing GPT-Live](https://openai.com/index/introducing-gpt-live/)
   — full-duplex architecture, delegation, rollout and launch limits.
4. OpenAI Help, [Using Study Mode in ChatGPT](https://help.openai.com/en/articles/11780217-study-mode)
   — current global availability, voice/files/memory and limitations.
5. OpenAI, [New ways to learn math and science](https://openai.com/index/new-ways-to-learn-math-and-science-in-chatgpt/)
   — dynamic visual explanations for 70+ concepts.
6. Anthropic, [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)
   — capabilities, interactive artifacts, availability and pricing.
7. Anthropic, [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
   — agentic capability and introductory pricing.
8. Anthropic, [Claude for Teachers](https://www.anthropic.com/news/claude-for-teachers)
   — teacher product, curriculum connectors, skills and US scope.
9. Google, [Gemini Study Notebooks](https://blog.google/innovation-and-ai/products/gemini-app/gemini-study-notebooks/)
   — diagnostic, 100+ objectives, adaptive lessons/quizzes and dashboard.
10. Google for Education, [Connected AI tools for students](https://blog.google/products-and-platforms/products/education/iste-students-2026/)
    — product rollout, school accounts and standardized-test plans.
11. Google DeepMind, [Guided Learning RCT in Sierra Leone](https://deepmind.google/blog/measuring-the-impact-of-learning-with-ai-in-sierra-leone-and-beyond/)
    — public trial summary and interaction analysis.
12. Google DeepMind/Fab AI, [Sierra Leone technical report](https://storage.googleapis.com/deepmind-media/LearnLM/learnLM_sierraleone_may26.pdf)
    — design, preregistration and detailed results.
13. Google, [Gemini 3.5 Live Translate](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/)
    — 70+ languages and 2,000+ pairs.
14. Google AI, [Gemini API release notes](https://ai.google.dev/gemini-api/docs/changelog)
    — July 21 model availability and live-audio model.
15. Google AI, [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
    — Flash-Lite, Flash Live, batch, cache and free-tier pricing.
16. Google AI, [Gemma models overview](https://ai.google.dev/gemma/docs)
    — sizes, languages, modalities and device targets.
17. Google, [Gemma 4 12B developer guide](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)
    — unified multimodality and 16GB local target.
18. Mistral, [OCR 4](https://mistral.ai/news/ocr-4/) — 170 languages,
    confidence, bounding boxes and self-hosting.
19. Mistral, [Voxtral](https://mistral.ai/news/voxtral/) — 3B edge ASR,
    multilingual speech understanding and API price.
20. Mistral, [Voxtral TTS](https://mistral.ai/news/voxtral-tts/) — 4B model,
    multilingual voice, latency and open-weight variant.
21. DeepSeek, [V4 release](https://api-docs.deepseek.com/news/news260424/)
    — parameter counts, open weights and 1M context.
22. DeepSeek, [models and pricing](https://api-docs.deepseek.com/quick_start/pricing/)
    — current V4 Flash/Pro first-party prices.
23. Qwen, [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b)
    — open multimodal 3B-active model.
24. Qwen, [Qwen-Image 3.0](https://qwen.ai/blog?id=qwen-image-3.0)
    — dense layout, small-text, 12-language generation.
25. Sarvam, [open-sourcing 30B and 105B](https://www.sarvam.ai/blogs/sarvam-30b-105b)
    — Indian sovereign open models and evaluations.
26. Sarvam, [Sarvam Edge](https://www.sarvam.ai/products/edge) — sub-1GB,
    22-language local speech/translation stack.
27. Sarvam, [Saaras v3 speech recognition](https://www.sarvam.ai/speech-to-text)
    — 22 Indian languages plus English, code-mixing and price.
28. Meta, [Omnilingual ASR](https://ai.meta.com/blog/omnilingual-asr-advancing-automatic-speech-recognition/)
    — 1,600+ languages and open release.
29. World Bank, [From Chalkboards to Chatbots](https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099548105192529324)
    — Nigeria randomized trial and +0.31 SD result.
30. World Bank, [AI in Latin America's schools](https://www.worldbank.org/en/results/2026/07/02/artificial-intelligence-in-action-in-latin-america-s-schools-evidence-from-peru)
    — Peru deployment and teacher-training trial.
31. Contractor & Reyes, [Experimental Evidence on the Learning Impact of
    Generative AI](https://arxiv.org/abs/2607.08849) — immediate and delayed
    unaided learning.
32. Cruces et al., [Does Generative AI Narrow Education-Based Productivity
    Gaps?](https://www.nber.org/papers/w34851) — randomized gap and retention
    evidence.
33. LearnLM Team & Eedi, [AI tutoring can safely and effectively support
    students](https://arxiv.org/abs/2512.23633) — exploratory UK RCT.
34. Oreopoulos et al., [Khan Academy field experiment in India](https://www.nber.org/papers/w34683)
    — implementation support and mathematics gains.
35. Yao et al., [Measuring Whether LLM Tutors Teach or Solve](https://arxiv.org/abs/2606.16206)
    — public benchmark diagnostic.
36. Abrar et al., [When LLM Tutoring Responses Work](https://arxiv.org/abs/2607.09919)
    — 16,851 programming interactions.
37. Neagu et al., [Rethinking Scaffolding in LLM Tutors](https://arxiv.org/abs/2606.15766)
    — 9,490 benchmark and deployment chats.
38. Feng et al., [From Answer Generators to Reasoning Facilitators](https://arxiv.org/abs/2607.01692)
    — Zhongkao field deployment.
39. Lane & Kageler, [CSTutorBench](https://arxiv.org/abs/2607.05571) — small
    model tutoring benchmark and prompt intervention.
40. Zhao et al., [DeepTutor](https://arxiv.org/abs/2604.26962) — agent-native,
    open personalized tutoring architecture.
41. Google DeepMind, [ATL Saathi](https://deepmind.google/blog/empowering-indias-next-generation-of-innovators-with-atl-saathi/)
    — India pilot, scope and languages.
42. Daxing'anling Education Bureau, [2026–2028 AI-assisted education plan](https://dxal.gov.cn/dxal/c100131/202603/c13_330128.shtml)
    — rural/regional Chinese implementation policy.
43. ITU, [Facts and Figures 2025](https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/)
    — global connectivity and 2.2B offline estimate.
44. UNESCO, [Resilient education systems: 2026 practices](https://www.unesco.org/sdg4education2030/en/articles/building-resilient-education-systems-global-lessons-good-practices)
    — offline-first Ethiopia deployment and current global practices.

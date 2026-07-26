---
title: "Case Studies from an Existing Practitioner Portfolio (dlmastery)"
wave: D
date_researched: 2026-07-25
sources_count: 78
---

# Case Studies from an Existing Practitioner Portfolio

**Subject:** GitHub user `dlmastery` (eranti@gmail.com), ~60 repositories (35+ active), 9 live deployed
apps inspected. All evidence below is first-hand: authenticated `gh api` reads (including private repos),
`curl` of the deployed production bundles, and local filesystem reads. No claim here is second-hand or
inferred from a README alone unless explicitly labelled.

**Method note.** Every deployed app is a client-rendered React SPA whose HTML shell contains no content.
Rendering-based inspection (WebFetch) returns only a `<title>`. All behavioural findings below were
obtained by downloading the production JavaScript bundles (588 KB – 1.0 MB each) and extracting system
prompts, model IDs, response schemas, tool declarations, and UI strings directly from the shipped code.
This is why the findings include defects that a screenshot review would never surface.

---

## 0. Executive summary of findings

The portfolio is a large, genuinely impressive body of *content generation* and *interface* work with a
consistent, repeatable architecture. Its strengths are exactly the things the survey wants to advocate:
a codified, agent-executable "zero-to-hero" curriculum method; a real-time multimodal tutoring stack;
and an autonomous research loop that could be repurposed for curriculum improvement.

Its weaknesses are equally clear and equally instructive, and the survey should treat them as the
research agenda rather than as embarrassments:

1. **No learner model, no memory, no assessment loop.** Across 128 notebooks and 7 deployed learning
   apps there is effectively **zero formative assessment**. The zero-to-hero notebooks contain literally
   zero cells matching `Exercise`, `Your Turn`, `Try it`, or `Solution`. Nothing measures whether
   learning occurred.
2. **Generation is not persistence.** Content is regenerated per session from a prompt. Only Ekalavya
   persists anything (Firestore `users/{uid}/curriculums/{id}`), and even that persists the *artifact*,
   not the *learner state*.
3. **Fork-and-rename is the reuse mechanism**, and it has already produced measurable drift and
   production breakage (§A.3, §A.4). Five apps share a byte-identical CSS block; two ship the wrong
   `<title>`; six ship a literal placeholder API key at up to six call sites.
4. **BYOK is a hard adoption wall.** Six of seven AI-Studio-lineage apps call
   `window.aistudio.openSelectKey()` — they demand the *end user's* Gemini API key. Only Ekalavya has a
   server-side proxy. A learning platform for "the next billion minds" cannot require the learner to hold
   a paid API key.
5. **The two capabilities the tutors most need were built elsewhere in the same portfolio.**
   Cross-session memory and affect-conditioned pacing exist in `meditationguru`; a formal, gated,
   ledger-backed improvement loop with a "the repository is the memory" thesis exists in `autoresearch*`.
   Neither has been applied to teaching.
6. **Enforcement vs intention is the portfolio's defining split.** The teaching corpus *states* quality
   rules; the research corpus *compiles them into regexes, word floors, SHA-256 fingerprints and
   independent audit agents that exit non-zero with no bypass flag*. Where rules are norms they have
   already drifted; where rules are gates they hold at 112/112.

---

## A. The learning-specific apps

### A.1 Provenance: two distinct app lineages

All nine URLs resolved HTTP 200 (no cold-start failure, no auth wall). They fall into two clearly
separable families:

| Lineage | Apps | Auth model | Backend | Tell-tale |
|---|---|---|---|---|
| **AI Studio "Build" export** | Spanish, Telugu, Bhagavad Gita, Sanatana Dharma, Ayurveda, PsycheForge, (Akka) | BYOK — `window.aistudio.openSelectKey()` | none; browser calls Gemini directly | `esm.sh` importmap, `cdn.tailwindcss.com`, `@google/genai` in-browser |
| **Hand-built app w/ server** | Ekalavya AI | Firebase Auth | Cloud Run server proxy: `/api/gemini/generate`, `/api/gemini/tts`, `/api/live` (WebSocket) | Firestore SDK, 9 server-proxy call sites, 0 BYOK for core paths |

Architecture markers extracted from the shipped bundles:

```
app        openSelectKey  googleSearch  firebase  server-proxy  bundle bytes
spanish         1             32           0           0          680,494
telugu          1             32           0           0          643,787
gita            1             32           0           0          743,853
sanatana        1             32           0           0          767,977
ayurveda        1             32           0           0          644,417
psycheforge     1             32           0           0          588,341
ekalavya        1              0           2           9        1,016,019
```

### A.2 Ekalavya AI — the flagship learning app

**URL:** `https://ekalavya-ai-262451841611.us-west1.run.app` (live, HTTP 200)
**Repo:** `dlmastery/ekalavya-ai` (public, TypeScript, 226 KB)
**Tagline shipped on the landing page:**
> "Infrastructure takes decades. AI takes seconds. The self-teaching platform for the next billion minds."
> "Connecting the next billion minds to world-class mastery. Deeply personalized. Cinematic. Infinite."

**The framing device** (from the shipped copy) is the Mahabharata story of Ekalavya, who was refused
instruction by Drona and taught himself before a clay statue of the master:
> "In the ancient epic Mahabharata, Ekalavya was a young prince of a forest tribe who sought to learn
> archery from the great master Drona. When rejected because of his social standing, he did not give up.
> Instead, he retreated into the forest, created a clay statue of Drona, and began practicing with
> unwavering focus, treating the statue as his living guru."

This is a *precise* and deliberate metaphor for the survey's thesis: the AI is the clay Drona. It is
worth stealing as framing.

#### Interaction model

1. **Profile** — name, grade, location, language, optional interests ("E.g. Space, History, Farming,
   Robotics…"; "Type any topic. Our AI understands your context and environment.").
2. **Curriculum synthesis** — a single `gemini-3.1-flash-lite` call with a strict `responseSchema`
   producing exactly 10 chapters. UI narrates the generation with staged copy: *"Architecting Learning
   Path…" → "Clustering 50 Mastery Paths…" → "Synthesizing Academy Blueprint…" → "Validating Narrative
   Integrity…"*.
3. **Live voice tutor ("Drona Live")** — WebSocket to `/api/live`, mic captured via `getUserMedia` →
   `ScriptProcessorNode(4096,1,1)` → manual decimation to 16 kHz → Int16 PCM → base64 over WS; model
   audio returned and played at 24 kHz with barge-in handled by `interrupted` / `turnComplete` messages.
4. **Visualization / video** — "Neural Visualization Inbound…", "Preparing video engine…", and a
   `"Video generation complete (Mock)."` string (i.e. the video path is stubbed).
5. **Homework capture** — "Upload homework photos here"; "Analyze books and the world instantly."
6. **Export** — "Print as Tome (PDF)".

#### Pedagogy, quoted from the shipped system prompts

The curriculum generator (verbatim from the production bundle):

```
You are an expert curriculum designer specializing in deep, engaging, evidence-based education
inspired by self-directed, play-based learning.

CORE PHILOSOPHY:
- Self-directed exploration and play as the primary engine of learning.
- "Gifts": hands-on materials, tools, simulations, or digital analogs that make abstract
  concepts tangible.
- Learner agency: learners choose projects based on curiosity.
- Teacher/Facilitator (Drona): uses open-ended "provocations" and questions instead of lecturing.
- Interdisciplinary connections and rich projects.

TASK: Create a concentrated 10-chapter intensive mastery path for ${name} (Grade ${grade},
${location}) on ${topic}.
... Ensure the content deeply caters to a Grade ${grade} student and integrates the local
environment, history, and culture of ${location}.
STRICT CONSTRAINT: The difficulty, vocabulary, and conceptual depth MUST perfectly match a
Grade ${grade} cognitive level. DO NOT OVERCOMPLICATE topics beyond what a Grade ${grade}
student can understand.
Each chapter must be a distinct, high-impact module that increases learner autonomy.
```

The JSON schema it enforces is a genuine pedagogical commitment, not decoration:
`curriculumTitle`, `goal`, `pedagogicalApproach`, `globalGifts[]`, `hours[{hourNumber, theme}]`
with `minItems: 10, maxItems: 10`. Other schema fields surfaced in UI strings include
`"Hands-on Simulation: Name (Description)"`, `"Provocation Question 1"`, `"Peer shared activity or
collaborative challenge"`, `"Showcase-based assessment description (Portfolios, Peer Review)"`,
`"Method for documenting learning (e.g. Journaling prompt)"`, `"Scenario to apply the gift"`.

This is recognisably **Froebel + Reggio Emilia + Socratic**: "gifts", "provocations", learner agency,
portfolio assessment, reflective journaling. It is a real pedagogical position, encoded as a schema.

**Three distinct live-session personas** are shipped as separate system instructions — this is the most
pedagogically interesting thing in the whole portfolio:

```
Lecturer: "You are an expert lecturer. Context: ${ctx}. Start with a 2-3 minute comprehensive and
           engaging discourse on the topic. Use vivid imagery and local context. After the discourse,
           invite the student to ask questions."

Socratic: "You are an expert Socratic teacher. Context: ${ctx}. Facilitate a discussion. Answer
           questions by asking leading questions that help the student discover the answer themselves."

Examiner: "You are a brilliant examiner. Context: ${ctx}. Conduct an interactive oral quiz. Ask one
           question at a time. Evaluate the student's response and provide feedback before moving to
           the next question. Be encouraging but rigorous."
```

Plus the base live persona: *"You are Drona, a wise Socratic tutor for ${name} (Grade ${grade},
${location}). Teach through questioning and dialogue."*

**Mode-switching between lecture / dialogue / assessment is already implemented.** What is missing is any
*policy* for when to switch — the learner picks. There is no mastery estimate driving the choice.

#### The repo/deployment split — a significant finding

`dlmastery/ekalavya-ai` on GitHub is **not** the deployed app. The repo is a **Next.js 15 / React 19
design prototype backed entirely by mock data**:

- `src/lib/mock/` — `fake-classroom.ts`, `fake-conversations.ts`, `fake-lessons.ts`, `fake-profiles.ts`,
  `fake-progress.ts`, `fake-quiz.ts`, `fake-whiteboard.ts`, `provider.ts` (16.5 KB).
- `package.json` has **no `@google/genai` dependency at all**. Zero LLM integration.
- Tests (`tests/unit/mock-provider.test.ts`, 23.8 KB) test the mocks.

But the repo contains something more valuable than the code: a complete **`DataProvider` interface**
(`src/lib/providers/data-provider.ts`) that enumerates 32 features (F01–F32) as a typed contract —
onboarding, `detectLearningStyle`, streaming chat, `getHint(level: HintLevel)`, mode switching, image
generation, TTS/STT, multi-agent classroom + debate, lesson/scene generation with PPTX/HTML export,
quiz generation + grading, whiteboard drawing steps / math construction / mindmap, learner model
get/update, progress + achievements + streaks, **village group mode**, and a mascot emotion engine.

**This interface is the best single artifact in the portfolio for the survey.** It is a specification of
what an AI-native tutor *should* expose, written before the implementation, with a mock implementation
proving the shape is coherent. The deployed app implements maybe 8 of the 32.

#### Research provenance

`docs/research/` contains a documented, agent-parallel competitive review — 12 research agents dispatched
2026-03-19 against OpenMAIC, ChatTutor, Tutor-GPT, SocraticAI, Gemini Live APIs, SocratiQ, AlgoMentor,
Algo Sensei, DeepTutor, Mr. Ranedeer (29.7k stars), Multi-Agent-Study-Assistant, and
`Awesome-AI-Era-Edu` (173 papers). `00-RESEARCH-DIARY.md` records the conclusion verbatim:

> "Key gap identified: NO existing repo has offline, mobile-first, voice-first, or rural optimization"

`02-SOKRATES-VISION-PRD.md` is the original vision — "Sokrates, the Child Socrates AI Tutor", *"No Child,
No Teen, No Adult Left Behind"*, Rural 3rd-World Education Edition. It targets **$30–50 Android devices**,
**Gemini Nano on-device / offline 95%+ of the time**, `<50 MB` initial download, solar-friendly, 100+
low-resource languages, AGPL-3.0, `<$0.01 per 30-min connected session`, "village USB sharing", 10M
learners in 3 years.

**The gap between the PRD and the deployment is the single most important datum in this whole section.**
The PRD demands offline-first Android with on-device Nano. What shipped is an online-only Cloud Run React
SPA that requires a WebSocket for voice. Every hard constraint (offline, low-end device, low data, cost
ceiling) was dropped. `docs/research/12-EDUCATION-UX-DESIGN-DIRECTION.md` is 78.5 KB — the design research
was thorough; the deployed artifact is the easy 20%.

### A.3 The Spanish and Telugu portals

**URLs:** `spanish-learning-portal-…`, `telugu-learning-portal-for-any-language-speakers-…` (both live).

These are the same app, twice. Both expose six surfaces, extracted from the bundles:
**Lesson Portal** (paginated, 10 parts/page), **Live Immersion**, **Speaking Studio / Pronunciation
Mirror**, **Writing Lab**, **Vocabulary Mastery Lab**, **Teacher (chat)**.

The lesson generator is the strongest piece of prompt-level pedagogy in the portfolio (verbatim, Spanish;
Telugu is identical modulo the language name):

```
You are the ultimate, world-class Spanish Teacher and Textbook Author.
Your mission is to provide a masterpiece lesson for: "${topic} / ${subTopic}".
Target Language for explanations: ${uiLanguage}.
Spanish Dialect: ${dialect}.            // "Castilian" | "Latin American"
Student's Learning Goal: ${goal}.        // e.g. "Hobby & Cultural Interest", "Business & Professional"
Current Page: ${page} (Targeting parts ${n} to ${n+9}).

PEDAGOGICAL STRATEGY:
- Use the "Comprehensible Input" method combined with Socratic questioning.
- Start with high-frequency vocabulary and essential structures.
- Provide clear, concise grammar "nuggets" that are easy to digest.
- Include cultural nuances that a native speaker would know, specifically for the ${dialect} dialect.
- Ensure a smooth transition from simple to complex concepts.
- Tailor examples and vocabulary to the student's goal: ${goal}.

CURRICULUM STRUCTURE (per part):
1. 'spanish': The core Spanish phrase/sentence (natural, modern Spanish).
2. 'phonetic': Precise phonetic guide (e.g., "oh-lah" for "hola").
3. 'meaning': Accurate translation in ${uiLanguage}.
4. 'explanation': A "Teacher's Insight" in ${uiLanguage} explaining the 'why' behind the structure.
5. 'grammarNugget': A specific, bite-sized grammar rule related to this part.
6. 'culturalTip': A nuance or fact about how this is used in ${dialect}.
7. 'example': A mini-dialogue or context where this is used.

Output MUST be a valid JSON object matching the schema.
```

Named pedagogy (Krashen's **Comprehensible Input**), dialect awareness, goal conditioning, and a
seven-field structured lesson unit. The Telugu variant is explicitly *teach-Telugu-through-any-language*
(`"You are capable of teaching Telugu through ANY language requested by the user."`), with a UI language
enum covering 15 Indian languages plus French/German/Chinese/Japanese/Russian/Portuguese — a genuinely
novel positioning (most Telugu resources assume an English-speaking learner).

**Live Immersion** uses the Gemini Live API (`gemini-2.5-flash-native-audio-preview-12-2025`,
`gemini-3.1-flash-live-preview`) with `inputAudioTranscription` + `outputAudioTranscription` both enabled
(so a live bilingual transcript renders: *"The teacher is listening. Start speaking to begin your
immersion session. Translations will appear here in real-time."*), and — importantly — **function
declarations as the assessment channel**:

```
open_lesson_portal(topic)          → "Transition to full lesson portal view."
provide_feedback(score, feedback, suggestion)
                                   → "Evaluate the student's Spanish pronunciation."
                                      score: "Accuracy score from 1 to 10."
mark_word_practiced(word)          → "Mark a vocabulary word as successfully practiced and mastered."
```

This is the **only place in the entire portfolio where the model emits structured evidence of learner
state**. `mark_word_practiced` is a one-bit mastery signal. It is exactly the right primitive — and it is
written to nothing. There is no Firestore, no localStorage persistence layer in these bundles. The
mastery signal is discarded at page reload.

There is also a mid-session language switch: on change, the client injects
`"The user has changed their preferred language to ${lang}. Please continue the lesson in ${lang} from
now on."` into the live stream.

**Writing Lab** grades free text against a schema of
`corrections[{original, corrected, explanation}]`, `overallFeedback`, `score` (1–10), `improvedVersion`.
Again: correct shape, discarded output.

### A.4 The devotional / wellness apps — Gita, Sanatana Dharma, Ayurveda, PsycheForge

These are the same codebase again, re-skinned. Evidence of literal forking:

- The `<style>` block in Spanish, Telugu, Gita, Sanatana Dharma and Ayurveda is **byte-identical**
  (md5 `680a31f73fa3204fa7e3c0b8b03ee0fd`) — same `--saffron/--gold/--vermillion/--temple-cream`
  variables, same `mandala.png` background, same `.diya-glow` and `.shimmer-text` animations, on a
  **Spanish-language learning portal**.
- **Two apps ship the wrong page title.** The Spanish portal and the Bhagavad Gita app both serve
  `<title>Sanatana Dharma AI Portal</title>`. This is what makes a browser-rendered review report
  "Sanatana Dharma AI Portal" when asked about the Spanish app.

Personas are swapped at the system-instruction layer only:

| App | System instruction (verbatim) |
|---|---|
| Sanatana Dharma | `You are an enlightened Vedic Guru. Provide the authentic sacred slokas for: "…"` / `You are the ultimate Guru AI. Your output must be localized to ${lang}.` |
| Bhagavad Gita | `You are the Divine Lord Sri Krishna, supreme guide of the Bhagavad Gita. Deliver the authentic verses, translations, and ultimate wisdom for: "…"` / `You are Lord Sri Krishna, supreme spiritual mentor.` |
| Ayurveda | `You are Lord Dhanvantari, the God of Ayurveda. Provide the authentic Ayurvedic wisdom and slokas for: "…"` / `You are Lord Dhanvantari, the Divine Physician. Your output must be localized to ${lang} and focused on traditional Ayurveda.` |

The Gita app's curriculum is topic-indexed by *life problem* rather than by chapter — e.g.
`"Bhagavad Gita lessons on mind control, emotional stability, and self-discipline"`,
`"…teachings on death, the eternal soul, and handling grief and loss"`,
`"…lessons on Bhakti Yoga, complete surrender, and infinite peace"`. Both Gita and Sanatana ship the
Taittiriya Upanishad line *"Treat your mother as God. Treat your father as God. Treat your teacher as
God. Treat your guest as God."*

All use `googleSearch` (32 refs) + `urlContext` (20 refs) grounding, `thinkingConfig` (16–18 refs),
`responseSchema` (14–18 refs), streaming (`generateContentStream`), TTS
(`gemini-3.1-flash-tts-preview`, `gemini-2.5-flash-preview-tts`), Live audio, and
`gemini-embedding-001` / `gemini-embedding-2`. **Search grounding on scripture is a real design decision**
and a real risk: grounding devotional/medical claims in web search results is a sourcing hazard the
survey should name explicitly (Ayurveda is dispensing health guidance in the voice of a deity, grounded
by `googleSearch`, with no disclaimer visible in the extracted strings).

**PsycheForge AI — The Dual Mirror Ecosystem** is the same shell aimed at clinical psychiatry:
"Dual-Mirror Architecture", "Clinical Nexus", "Activate Scribing Protocol", "AI-Native Neural Insight
Protocol v4.2", a clinical-scribe prompt (`You are a world-class Clinical Scribe. Analyze the attached
${audio|video}…`) with drag-drop session recordings, and a "Landscape/Assess" section of forward-looking
claims. Several shipped strings are **fabricated-sounding statistics presented as evidence** —
`"Behavioral phenotypes mapped against 1.2M genomic data points."`,
`"Diagnostic simulation benchmarks outperform junior residents in 8/10 categories."`,
`"CMS approves first 'AI-Steward' code for psychiatric billing."`,
`"Content aligned with 2025 WHO digital mental health guidelines."`
There is no citation mechanism in the bundle for any of these. **This is a credibility liability and the
survey should not cite PsycheForge as evidence of anything except the template's reach.**

### A.5 Akka — Rural Health Companion

**URL:** `https://more-triage-akka-rural-health-companion-…` (live, HTTP 200). Repo
`dlmastery/akka-rural-health-companion` (private, TypeScript, 62 KB). Title:
*"Akka - Rural health triage assistant"*. Single 115 KB inline-HTML shell with an importmap and a
`/public/websocket-interceptor.js` (i.e. Gemini Live traffic is intercepted client-side). No visible
text renders without JS. Relevant to the survey mainly as evidence that the same shell is being reused
for a *rural, low-connectivity, non-literate* audience — the same audience the Ekalavya PRD targets, with
the same offline gap.

### A.6 Exo 3.0 — The Organizational Singularity

**URL:** `https://storage.googleapis.com/exo-3-0-site/index.html` (live, static GCS, 26 KB, fully
server-rendered — the only app in the set that is readable without JS). Repo lineage:
`dlmastery/organizational-singularity` (private, 30 MB).

This is *not* a learning app in the tutor sense; it is a **structured book-as-website** — a distinct and
arguably more successful learning pattern than the chat apps. Structure: 4 Parts, 3 frameworks
("The Destination: ExO 3.0 = MTP + DRIVE + SHAPE"; "The Operating System: Intelligence Stack, 6 layers +
GOVERN/ASSURE, Boyd's OODA loop at machine speed"; "The Playbook: REWRITE, 6 sequenced steps"), a
"Landscape", a "Library", and **"Assess Your Firm" — a diagnostic instrument**.

Its core argument (verbatim): *"In 1937, Ronald Coase explained why firms exist… AI is about to make that
argument obsolete. When the marginal cost of coordination approaches zero… the rationale for the
traditional firm does not weaken. It collapses."* Attributed to "Salim Ismail with contributors".

Two pedagogical devices worth extracting: (a) an explicit **"If you remember nothing else: destination,
operating system, playbook"** compression, and (b) a **self-assessment diagnostic** as the call to
action. The diagnostic is the only assessment instrument anywhere in the deployed portfolio.

---

## B. `dlmastery/class` — the zero-to-hero corpus (PRIVATE)

**Repo:** private, `Jupyter Notebook`, **30.6 MB**, created 2026-05-31, last pushed 2026-06-21.
**1,128 tracked files.** This is the crown jewel and it is substantially *larger* than the brief
suggested (the brief said "26 colabs / ~3,100 cells"; that describes only the data-mining sub-series).

### B.1 Actual inventory

```
128  .ipynb notebooks total
 95  at repo root
 28  *_zero_to_hero.ipynb
 10  *_sota_2026.ipynb
 44  *_tutorial.ipynb
 29  under CMPE258_Deep_Learning_2026/
 88  .pptx decks (AI_PromptEng_HighSchool)
```

Top-level directories by file count: `AutogluonModels/` (234 — checked-in model pickles, junk),
`AI_PromptEng_HighSchool/` (140), `formulae/` (73), `CMPE258_Deep_Learning_2026/` (65), then ~20
`<topic>_build/` directories (13–33 files each) holding the generator driver scripts.

The repo is really **five programs stacked in one namespace**:

1. **Intro to Data Mining zero-to-hero** — 15 notebooks mapped to Tan/Steinbach/Karpatne/Kumar 2e.
2. **SOTA-2026 series** — 10 notebooks, "what is state of the art in May 2026 and how to use it".
3. **`formulae/`** — concept-mastery proof colabs (PCA, SVD) + interview gauntlets, dependency-ordered.
4. **CMPE258 Deep Learning (SJSU, Spring 2026)** — 14 weekly lectures, HW1–4, 8 quizzes, question banks,
   study guides, week-1 demo + SOTA colabs.
5. **AI Prompt Engineering for High School** — 88 PPTX decks in three parallel design systems
   (`decks/`, `decks_interactive/`, `decks_mckinsey/`) generated by ~30 Python builder scripts, plus 27
   interactive Python modules covering ethics, SPEC prompting, chain-of-thought, "Trust But Verify",
   hallucination hunting, and 20+ study/writing/research modules.

Plus `vizuara_research/` — a 186 KB competitive dossier on the vizuara.ai course ecosystem, and
`skills/` — the reusable method (§B.4).

### B.2 The zero-to-hero series: verified structure

From `ZERO_TO_HERO_COLABS.md` (verbatim status table, cells given as total (md/code)):

| # | Topic | Cells | dmbook ch. |
|---|---|---|---|
| 1 | Logistic Regression | 186 (110/76) | 4.6 |
| 2 | Support Vector Machines | 117 (69/48) | 4.9 |
| 3 | Naive Bayes & Bayesian | 132 (75/57) | 4.4–4.5 |
| 4 | Association Analysis | 182 (97/85) | 5–6 |
| 5 | Anomaly Detection | 131 (80/51) | 9 |
| 6 | Decision Trees & Model Evaluation | 136 (80/56) | 3 |
| 7 | k-Nearest Neighbors | 123 (82/41) | 4.3 |
| 8 | Ensemble Methods | 142 (79/63) | 4.10 |
| 9 | Data: Exploration & Preprocessing | 139 (72/67) | 2 |
| 10 | Clustering Algorithms | 128 (77/51) | 7–8 |
| 11 | Rule-Based Classifiers | 118 (70/48) | 4.2 |
| 12 | Avoiding False Discoveries | 128 (76/52) | 10 |
| + | Introduction to Data Mining | 101 | 1 |
| + | Similarity / Distance / Proximity | 115 | 2.4 |
| + | Advanced Clustering (SOM, CLIQUE, DENCLUE, BIRCH/CURE, Chameleon, SNN) | 111 | 8 |
| + | Exam prep — hardest solved problems | 123 | all |

SOTA-2026 series (10 notebooks, 82–114 cells each): Tabular Classification (110), Clustering (110),
Anomaly Detection (102), Pattern Mining (110), Vector Search / Embeddings (111), Bayesian &
Probabilistic ML (108), SVM & Kernel Methods (108), Data-Centric AI (114), Statistical Validity (82),
Deep Learning (71).

Direct verification (I downloaded and parsed three notebooks):

| Notebook | cells | md | code | md:code | h1+h2 | outputs shipped |
|---|---|---|---|---|---|---|
| `logistic_regression_zero_to_hero.ipynb` | 186 | 110 | 76 | 1.45 | 171 | 0 |
| `classification_tabular_sota_2026.ipynb` | 110 | 73 | 37 | 1.97 | 69 | 0 |
| `statistical_validity_sota_2026.ipynb` | 82 | 50 | 32 | 1.56 | 44 | 0 |

Metadata is exactly as the house style specifies (`kernelspec` + `language_info` only, no `colab` block,
`execution_count: null`, `outputs: []`). Cells ship un-run so Colab populates outputs on first Run-All.

### B.3 How difficulty progresses — and how it actually works

Difficulty is expressed as **⭐ ratings on Part headers and in the Table-of-Contents table**, not as
prerequisites or gating. Counts of `⭐` in the three sampled notebooks: 30, 48, 61.

The progression is **ladder-per-notebook, not ladder-across-notebooks**. Each notebook independently
climbs zero → hero. Verified from `logistic_regression_zero_to_hero.ipynb`:

```
PART 1 · FOUNDATIONS ⭐
  Task 1 Setup & The Classification Problem
  Task 2 From Linear Regression to Classification  ("The Tempting (but Wrong) Idea",
                                                    "Three Things That Just Went Wrong")
  Task 3 The Sigmoid (Logistic) Function
  Task 4 Odds, Log-Odds & the Logit
PART 2 · THE MODEL & ITS MATH ⭐⭐
  Task 5 Model & Decision Boundary
  Task 6 Maximum Likelihood & Log-Loss   ("Why Log-Loss, Not Just Count the Errors?", convexity)
  Task 7 Gradient Descent
  Task 8 From Scratch (NumPy)  → compared against sklearn
  Task 9 scikit-learn
PART 3 · INDUSTRY-STANDARD EVALUATION METRICS ⭐⭐
  Task 10 Confusion Matrix → Task 11 Accuracy/Precision/Recall/F1 ("The Accuracy Trap")
  → Task 12 ROC/AUC → PR-AUC → log-loss/Brier → calibration/ECE
… Parts 4–7 (Advanced modelling, Statistical rigor, MLOps, DL/SOTA bridge)
… Applied (ColumnTransformer end-to-end) · Explainability · Error analysis · Closing
```

The `_sota_2026` notebooks use the same skeleton at a higher floor. `classification_tabular_sota_2026`
runs Part 0 (setup + "everything has a fallback" rule) ⭐ → Part 1 Landscape ⭐⭐ (Grinsztajn 2022 and
its 2024–26 rebuttals, **TabArena** as a living leaderboard) → Part 2 GBDT ⭐⭐ → Part 3 **Tabular
foundation models** ⭐⭐⭐ (TabPFN-2.5/3, TabICL, in-context learning for tables) → Part 4 Deep tabular
nets ⭐⭐⭐ (FT-Transformer, TabNet, SAINT, RealMLP, **TabM built from scratch**) → Part 5 AutoML ⭐⭐
→ Part 6 SOTA workflow ⭐⭐⭐ → **Part 7 head-to-head bake-off on identical data** → Part 8
explainability. `statistical_validity_sota_2026` reaches ⭐⭐⭐⭐ on knockoffs and PPI, covering e-values,
e-BH under arbitrary dependence, anytime-valid confidence sequences, Model-X knockoffs, selective
inference, conformal risk control, and prediction-powered inference — and explicitly states its
prerequisite: *"We deliberately do not re-teach the basics of p-values, Bonferroni, or BH — those live in
the companion notebook `avoiding_false_discoveries_zero_to_hero`."*

**Notebook anatomy** (from `house_style.md`, verified against the artifacts):
Title cell → gradient welcome banner → 🎯 Learning Objectives → 📚 TOC table with ⭐ column → 🗺️ "How to
read" (the `🧠 Intuition → 📐 The Math (gently) → 💻 Code → 📊 Picture → ✅ Takeaway` loop) → ⏱️ estimated
time → `# Part N · TITLE ⭐` → `# Task N ·` → `## N.M` → `### Definition/Intuition/The Math` → each task
ends with `## N.x Task N Summary` (✅ Key Takeaways, 🔑 new variables, ➡️ Next Up) → closing cheat sheet
+ numbered Common Pitfalls + What's Next + "Course Complete" banner + References. Semantic HTML callouts
with a fixed palette (info `#e7f3fe/#2196F3`, success `#d4edda/#28a745`, warning, danger, special) and a
fixed emoji vocabulary. Density target: 120–160 cells, ~1.6 md : 1 code.

### B.4 Exercises and solutions — the central finding

**The zero-to-hero notebooks contain no exercises.** Programmatic scan of all markdown in the three
sampled notebooks:

```
                         logreg   tabular_sota   stats_sota
"Exercise"                  0          0             0
"Your Turn"                 0          0             0
"Try it"                    0          0             0
"Solution"                  0          0             0
"Quiz"                      0          0             0
"Pause"/"predict"           0          0             0
"🧠 Intuition"             12         13             5
"✅ "                      46         14            36
"⚠️"                       12          4             5
```

The design is **explanation + demonstration + verification-by-the-author**. The learner reads and runs;
the learner is rarely asked to produce anything. The skill's success criterion—
*"a student can narrate every cell in a 1-hour video"*—is a strong explanation and
understanding target. The next layer should add learner production, transfer
challenges, and scheduled recall so that this excellent explanatory base compounds
into independent mastery.

Practice exists only in two dedicated, separate notebooks:

- **`exam_prep_solved_problems_zero_to_hero.ipynb`** (123 cells, 85 md / 38 code) — **36 problems** in a
  strict four-beat format, counted programmatically: `📝 Problem` ×36 → `🧠 Approach` ×36 → `📐 Worked
  Solution` (LaTeX) ×36 → `✅ Answer` ×36, plus code verification. Mapped to book exercises (Ch2 Ex.19,
  Ch3 Ex.3/5/7/2, Ch4 Ex.7/12/14/20, …) and cross-checked against the official solutions manual. **But
  the solution is always immediately adjacent to the problem.** There is no hidden-answer, no attempt
  gate, no self-grading.
- **`formulae/pca_interview_gauntlet.ipynb`** (105 cells) — 29 `Trap` markers and 31 `Follow-up` markers,
  structured `Question → Intuition → Rigorous answer → Code check → Follow-ups & traps`. This is the
  closest thing in the corpus to a retrieval-practice instrument, and it is one notebook out of 128.

Neither `cellView: "form"` nor `jupyter.source_hidden` is actually set on any code cell in any notebook
I sampled — **including the `formulae/` ones, whose governing skill makes hiding code a
"non-negotiable" (rule 12).** The method document is ahead of the artifacts.

### B.5 The method is codified as agent skills — the most transferable asset

`class/skills/` (canonical) and `class/colab_kit/skill_snapshot/` (historical) contain two Claude Code
Agent Skills plus a builder kit. `skills/README.md` states the intent plainly:
*"They encode a complete, repeatable method for building rigorous, beautiful, interview-ready
educational Colabs."*

**`zero-to-hero-colab`** (8.0 KB SKILL.md + `house_style.md`, `colab_arc.md`). Six golden rules:
incremental+validated; explanation-first (~1.5–2 md per code cell); high-level libraries with runnable
offline fallbacks; Colab-friendly datasets; end at SOTA-2026 with honest "where this classic still wins";
match house style exactly. Mandates a 10-section arc including three sections added *"per user request"*:
real-world end-to-end, explainability, error analysis.

**`concept-mastery-colab`** (18.6 KB SKILL.md + 6 reference files) — the evolution. **Sixteen
non-negotiables**, several of which are directly quotable in a survey on AI-native pedagogy:

> 2. **Why-before-what + intuition-first.** Before teaching any concept, say *why the learner needs it
>    next* and *what it unlocks*… Motivation and intuition precede machinery, every single time.
> 3. **Prove it AND verify it.** Every derivation shown step-by-step in LaTeX **and** confirmed
>    numerically/symbolically… If you can't verify it in code, you haven't finished it.
> 4. **Study the masters first.** Phase 0 (mandatory): find & show the 2–3 best explainers
>    (3Blue1Brown / StatQuest / Serrano / Ng) and **review their transcripts** to extract their intuition
>    strategy — then build on it. *"Their videos brush off the math; we keep their gentle intuition AND
>    add the rigorous derivation they skip."*
> 9. **Elite-professor proofs.** Every proof is a *section*, not a paragraph — expanded 3–5× with a 🎯
>    Strategy box… **every step line ends with the rule/formula it used in right-side parentheses
>    `(reason)`** — non-negotiable.
> 10. **No formula verbatim.** A formula stated with no build-up is a defect.
> 15. **No jargon before it's grounded.** Keep a **term-grounding verifier** (`verify_grounding.py`) that
>    flags every term whose first *use* precedes its first plain-language *explanation*; treat a
>    non-empty report as a build failure.
> 16. **Reason → Act → Observe on every cell.** 🔭 REASON (read as a fresh 10th-grader; name the specific
>    gap) → 🛠️ ACT (smallest incremental edit) → 👁️ OBSERVE (`validate()` + re-run verifier + render in
>    Colab). Log each loop so the pass is auditable.

The litmus test is stated explicitly: *"a motivated 10th-grader can follow every step; the learner can
derive the whole thing at a whiteboard; and a candidate can breeze through a hard technical interview by
reasoning, not memorizing."*

**QC is mechanised.** `colab_kit/colab_qc.py` → `run_all(NB, glossary=…)` checks execution + nbformat
schema + **grounding** (no jargon before introduction) + **captions** (every illustration captioned) +
hidden-code + leaked-labels, and prints PASS/FAIL. A non-empty report is defined as "not done". On top,
a 4-layer human protocol: (1) independent math re-verification in a standalone script that does not trust
the notebook's own prints, (2) execution, (3) teacher read-through, (4) "award-winning-lecturer editorial
review" hunting specifically for *"assumed too much"*.

**Builder kit:** `colab_kit/nbkit.py` — `md()`, `code()`, `new_notebook()`, `append()`, `insert()`,
`find_cell()`, `count()`, `validate()`. Notebook path is a parameter, so N agents build N notebooks
without collision. Per-topic `<topic>_build/` driver directories are checked in (20 of them), making every
notebook **regenerable**.

**Parallel dispatch is a first-class part of the method** and is *asymmetric*: zero-to-hero colabs are
independent files → one agent each, unlimited concurrency ("The 5 above were built by 5 concurrent
agents"). Concept-mastery *enhancement* passes are constrained to ≤2 agents on non-overlapping regions,
and *"the orchestrator does the inserts sequentially — never two agents editing one `.ipynb`."* This is a
genuine, hard-won lesson about agentic content production that the survey should record.

### B.6 Coverage auditing and curriculum sequencing

`AUDIT_TOC_COVERAGE.md` is a programmatic keyword audit of every notebook's text against **every TOC
subsection** of the textbook, with a ✅/⚠️/❌ verdict per chapter. It found a real gap (Ch.8: *"SOM, grid,
subspace, DENCLUE, Chameleon, SNN, Jarvis-Patrick are MISSING"*), generated an action item, and the
gap-fill notebook `advanced_clustering_zero_to_hero.ipynb` (111 cells) was then built. **Audit → gap →
targeted build → re-audit is a working closed loop over curriculum coverage.** It is the one place in the
portfolio where an automated signal actually changed the curriculum.

`formulae/SEQUENCE.md` adds the piece the notebook series otherwise lacks — an explicit **dependency
graph** with a *minimum-repetition rule*:

> 01 PCA establishes → projection, covariance, eigen/spectral theorem, diagonalization `A=QΛQ⁻¹`,
> matrix powers `Aⁿ`, Lagrange multipliers. 02 SVD assumes PCA. 03 Eigen-deep assumes 01+02.
> 04 Gradient Descent & Backprop. 05 Lagrangian/Duality/KKT assumes 01+04. 06 Probability & Bayes…
>
> **The minimum-repetition rule:** (1) give a 2–4 sentence recap + a link ("see Part 6 of the PCA colab
> for the full spectral-theorem proof"); (2) show only what's new; (3) **never re-derive a proof an
> earlier colab already did in full.**

Status: *"01 PCA complete (tutorial 256 cells + interview gauntlet 105 cells). 02 SVD in progress."*
`formulae/CURRICULUM.md` (16 KB) is a critic-reviewed v2 plan of ~40 derivation colabs in book order
(F1–F7 foundations, then 2A–10A per chapter), each entry listing *Derives/Proves*, *Context/Prereqs*, and
*Tricky targets* cross-referenced to specific line numbers in a cleaned solutions manual
(`examprep_build/solmanual_clean.txt`). Its changelog documents an adversarial pass: *"v2 changelog (from
critic audit): added Regression (App. D), Overfitting/Model-Selection…; split Ch.8 into 4 colabs; fixed
the 3B↔Ch.10 ordering; de-duplicated 4D/4E and 2B/2C."*

**A critic agent auditing a curriculum plan and producing an ordered changelog is prior art for
automated curriculum QA**, and is directly relevant to §D.

### B.7 The adjacent syllabus repo

`dlmastery/aicourse_syllabus` (public, 2.9 MB, live at `dlmastery.github.io/aicourse_syllabus/`) is the
macro-level companion: **"Modern AI Mastery (June 2026)" — 6 subjects, 197 lectures, ~590 lecture-hours**,
consolidated from an earlier 17-module program, reconciled against 2025–26 Stanford/MIT/Princeton/
Cornell/Harvard/CMU/Berkeley courses and industry curricula. Every lecture carries: learning goals →
concept map → step-by-step **AI-builder lab** → **▶ practical project** (real GitHub repo) → **State of
the Art (June 2026)** note with hyperlinked references → graded rubric. Its stated pedagogy is
`prompt → workflow → skill → harness` plus a
`concept → code → critique → reflection → rebuild` loop, "evidence over vibes (every week leaves an
inspectable artifact)", and "baselines and failure modes before fancy methods". It ships **218 skills**
as `skills/<name>/SKILL.md` (23 book reader-skills + 195 per-lecture harness-skills).

This repo has **rubrics and reflection** — the two things the `class` notebooks lack. The survey should
note that the author has already written the assessment layer; it just lives in a different repo and was
never wired into the artifacts.

---

## C. Multimodal / streaming precedents already built

### C.1 What is already demonstrably solved, from the evidence in §A

Independent of the deeper repo dives, the deployed bundles prove the following are working production
capabilities in this portfolio today:

- **Bidirectional live voice with a persona.** Gemini Live API over WebSocket, in six shipped apps.
  `gemini-3.1-flash-live-preview`, `gemini-2.5-flash-native-audio-preview-09-2025` /
  `-12-2025`. Both `inputAudioTranscription` and `outputAudioTranscription` enabled → a live bilingual
  transcript is a solved UI.
- **Barge-in / interruption handling.** `interrupted` and `turnComplete` server events clear the queued
  audio buffers (`le.current = []`).
- **Client audio pipeline from scratch.** `getUserMedia` (echoCancellation, noiseSuppression, autoGainControl)
  → `ScriptProcessorNode(4096,1,1)` → manual decimation to 16 kHz → Int16 PCM → base64 → WS; playback
  scheduled at 24 kHz via `AudioBufferSourceNode` with a running `nextStartTime` cursor to avoid gaps.
  *(Note: `ScriptProcessorNode` is deprecated; `AudioWorklet` is the correct 2026 API. This is a real
  technical-debt item — it runs on the main thread and will glitch on low-end Android, i.e. exactly the
  Ekalavya target device.)*
- **Prebuilt voice selection** exposed to the learner: `Aoede (Female - Empathetic)`, `Kore (Female -
  Clear)`, `Charon (Male - Deep)`, `Puck (Male - Dynamic)`, `Fenrir (Male - Strong)`.
- **Tool-calling during a live voice session** (`provide_feedback`, `mark_word_practiced`,
  `open_lesson_portal`) — i.e. the model can drive the UI and emit structured assessment mid-conversation.
- **Search + URL grounding** (`googleSearch` ×32, `urlContext` ×20) and **thinking budgets**
  (`thinkingConfig`) in every app.
- **Structured generation** (`responseSchema`, `responseMimeType: application/json`) with min/max item
  constraints, plus JSON-repair fallbacks (`"Attempting JSON repair for truncated response…"`).
- **Streaming text** (`generateContentStream`) with progress percentages.
- **TTS** (`gemini-3.1-flash-tts-preview`, `gemini-2.5-flash-preview-tts`) as a separate path from Live.
- **Embeddings** (`gemini-embedding-001`, `gemini-embedding-2`) — present in every bundle, though no
  retrieval index is visible; likely used for semantic topic matching.
- **Multimodal input**: image upload ("Upload homework photos here"), and in PsycheForge drag-and-drop of
  audio/video recordings analysed by a clinical-scribe prompt.

**Conclusion for the survey:** the *real-time multimodal tutor* is not a research problem for this author.
It is shipped, six times over. The unsolved problem is everything behind it — state, assessment, memory,
and offline.

### C.2 `dlmastery/meditationguru` — live voice + live camera + tool-driven UI + 3D

Public, default branch **`master`**, Next.js 16 App Router + TypeScript, 389 KB, last push 2026-02-10.
All AI code is in `src/lib/` (no `services/`).

**Model IDs (they disagree across files — a real hazard for reuse):**

| Purpose | Exact model ID | File |
|---|---|---|
| Live bidi voice+video (legacy path) | `models/gemini-2.0-flash-live-001` | `src/lib/gemini.ts` |
| Live bidi voice+video (**the path the session page uses**) | `models/gemini-2.5-flash-live-001` (`const LIVE_MODEL`) | `src/lib/gemini-enhanced.ts` |
| Text (intent parse, plan gen) | `gemini-2.0-flash` | `src/lib/gemini.ts` |
| Image (yoga pose illustrations) | `gemini-2.5-flash-image` (3 call sites) | `src/lib/imagen.ts` |

The README advertises "Gemini 2.5 Flash Live", `CLAUDE.md` says "Gemini 2.0 Flash Live", and
`src/lib/gemini.ts` carries the comment
`model: 'gemini-2.0-flash',  // Using latest available, update to 3.0-flash-preview when available`.
Three sources of truth, three answers.

**Live API — raw WebSocket, no SDK.** Endpoint hardcoded in both files:
```
wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent?key=${apiKey}
```
The key is `NEXT_PUBLIC_GEMINI_API_KEY` — **shipped to the browser**. Same class of defect as the
AI-Studio apps in §A. Setup frame:
`{ setup: { model, generationConfig: { responseModalities: ['AUDIO','TEXT'], speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName } } } }, systemInstruction: { parts }, tools: [{ functionDeclarations }] } }`.

**Audio uplink** (`startAudioStream`): `getUserMedia({audio:{sampleRate:16000, channelCount:1,
echoCancellation:true, noiseSuppression:true}})` → `AudioContext({sampleRate:16000})` →
`createScriptProcessor(4096,1,1)` → `floatTo16BitPCM` → little-endian Int16 → base64 →
`{ realtimeInput: { mediaChunks: [{ mimeType: 'audio/pcm;rate=16000', data }] } }`.
**No `AudioWorklet` anywhere in the repo.**

**Audio downlink — a real bug worth not copying.** `src/app/session/page.tsx` (~L201–215) does
`new AudioContext({sampleRate:24000})` then `await audioContext.decodeAudioData(audioData)`. Gemini Live
returns **raw 24 kHz PCM, not a container** — `decodeAudioData` throws on it. There is also no playback
queue: each chunk creates a fresh `AudioContext` and `start()`s immediately, so chunks overlap and
stutter. **The correct fix already exists in this portfolio** — `lumiere.ai`'s `addWavHeader()` (§C.4)
wraps the PCM in a hand-written 44-byte RIFF/WAVE header. The right target is that plus a scheduled
queue (`nextStartTime += buffer.duration`) — which is exactly what the Spanish/Telugu bundles do (§C.1).
**Three implementations of the same problem in one portfolio: one correct, one partial, one broken.**

**Video uplink:** `getUserMedia({video:{width:640,height:480,facingMode:'user'}})` → offscreen `<canvas>`
→ `canvas.toDataURL('image/jpeg', 0.7)` → base64 → `realtimeInput.mediaChunks` at
`VIDEO_FRAME_INTERVAL_MS = 1000` (1 FPS, the Live API rate).

**Tool-calling over the live socket — the most reusable single idea in the portfolio.**
`FUNCTION_DECLARATIONS` in `src/lib/gemini-enhanced.ts` registers five tools that let the model drive the
React UI mid-sentence: `control_soundscape`, `generate_visualization`, `report_pose_analysis`,
`report_breathing_observation`, `report_emotion_observation`. Note the workaround: **every parameter is
typed `string`** even for numbers (`overallScore`: "Alignment score 0-100"; `corrections`: "JSON array of
corrections: [...]"), parsed client-side. Responses go back as
`{ toolResponse: { functionResponses: [{ name, response }] } }`. Incoming calls arrive at **both**
`message.toolCall.functionCalls` and `serverContent.modelTurn.parts[].functionCall`; the handler covers
both. For a tutor this maps 1:1 onto `show_diagram`, `run_quiz`, `highlight_step`,
`report_comprehension` — the model narrates by voice while mutating application state.

**System prompt** (`GURU_SYSTEM_PROMPT`, `src/lib/gemini.ts`) is a full persona spec — personality
("Warm, patient, and deeply caring… Wise but never condescending… Adapts your energy"), capabilities
("Teach and correct yoga poses by observing the user via video", "Remember the user's journey, goals, and
preferences"), and mode-specific delivery rules ("When guiding meditation: use calming, rhythmic speech…
allow moments of silence"). Two appended blocks matter for teaching:

> **Affective dialog:** "IMPORTANT: You have affective dialog capabilities. Pay close attention to the
> user's vocal tone, pace, and emotional cues. When you detect a shift in their emotional state, call the
> `report_emotion_observation` function. Adapt your tone and pacing to match or soothe their emotional
> state. If they sound anxious, slow down. If drowsy, add gentle energy."
>
> **Memory injection:** "CONTEXT FROM PREVIOUS SESSIONS:\n{guruMemoryContext}\nUse this context to
> personalize your guidance. Reference past sessions naturally."

**`meditationguru` is the only app in the portfolio with cross-session memory** (`src/lib/guru-memory.ts`
+ Firestore) and the only one with affect-conditioned pacing. Both are exactly what the learning apps
lack — and they were built for meditation, not for teaching.

**3D stack:** `three@^0.182` + `@react-three/fiber@^9.5` + `@react-three/drei@^10.7`.
`src/components/three/CosmicScene.tsx` is a fixed `inset-0 -z-10` `<Canvas>` (ACESFilmic tone mapping,
`dpr={[1,2]}`, fog 30–80) containing a `Starfield` (5000 pts, 8000 in onboarding, driven by a
`breathingIntensity` prop), three layered `Nebula` meshes whose colours switch on `sessionMood`
(`calm`/`energetic`/`neutral`), three `Particles` fields that can `flowToGuru`, and clickable `GoalOrbs`.
`CLAUDE.md` notes the two operational rules: dynamic import with `ssr:false`, and *"No traditional ML
models — Gemini handles all pose analysis via live video prompts."*

**Deployment: no Dockerfile, no Cloud Run.** `next.config.ts` is `output:'export'` + unoptimized images →
static export; `firebase.json` serves `out/` with SPA rewrite, plus Firestore rules/indexes (`us-east1`).
Also reusable: `src/lib/group-session.ts` (6-char invite codes from an unambiguous alphabet, max 8
participants, group-aware system prompts) and `src/lib/meditation-audio.ts` (asset-free WebAudio
oscillator bells/chimes/breath cues — a 432 Hz bell with a 2.01× detuned overtone).

### C.3 `dlmastery/face-swap-streamer` — progressive playback while still computing

Public, `main`, Python, 751 KB, last push 2026-06-06.

**Correction to the brief: the ffmpeg `tee` muxer was removed.** The repo description and README still say
"tee muxer"; the code does not use it. `webapp.py`'s `_spawn_ffmpeg` docstring explains why, verbatim:

> Why not fragmented MP4 in tee any more: with empty_moov+frag_keyframe many native players (especially
> mobile) can't open the file at all — symptoms were "format not supported" on phones and "audio only" on
> desktop because only the audio fragments were decodable.

And `docs/ARCHITECTURE.md` §4.3 states the generalised lesson:

> Lesson: fragmented MP4 is a streaming-protocol format, not a file format. Always remux to
> non-fragmented MP4 if the file will be opened by anything except an MSE-based player.

**The actual streaming invocation** (spawned with `cwd=job_dir`, `stdin=PIPE`, `bufsize=0`, stderr drained
to `ffmpeg.log`):

```
ffmpeg -y -hide_banner -loglevel info
  -f rawvideo -pixel_format bgr24 -video_size {w}x{h} -framerate {fps} -i pipe:0
  -i <abs path to original target.mp4>
  -map 0:v:0 -map 1:a:0?
  -c:v libx264 -preset ultrafast -tune zerolatency
  -pix_fmt yuv420p -profile:v high -level 4.1
  -g {2*fps} -keyint_min {2*fps} -sc_threshold 0
  -c:a aac -b:a 192k -ac 2 -ar 44100 -shortest
  -f hls -hls_time 2 -hls_list_size 0
  -hls_flags independent_segments+append_list
  -hls_segment_filename hls/seg_%05d.ts  hls/playlist.m3u8
```

**Audio sync is solved for free, and elegantly.** Video arrives on `pipe:0` as raw BGR at the source fps;
audio is a **second input read directly from the original file by ffmpeg itself**. ffmpeg timestamps both
against the same output clock, so AAC advances in wall-clock-correct step with the incoming frames no
matter how slowly the GPU produces them — no manual PTS math, no drift. `-shortest` terminates when the
finite video pipe closes. Audio lives inside the `.ts` segments, so the live stream has sound from frame 1.

**Segment strategy:** 2 s segments with the GOP pinned to exactly 2 s (`-g`/`-keyint_min = round(fps*2)`,
`-sc_threshold 0`) so every segment starts on a keyframe; `hls_list_size 0` keeps the full playlist so it
doubles as VOD.

**Finalisation** (`_remux_to_mp4`), after `stdin.close()` writes `#EXT-X-ENDLIST`:
```
ffmpeg -y -allowed_extensions ALL -i hls/playlist.m3u8 -c copy \
       -bsf:a aac_adtstoasc -movflags +faststart out.mp4
```
`-c copy` = no re-encode (~5 s for a 4-minute video); `aac_adtstoasc` repacks AAC from ADTS to MP4
framing; `+faststart` fronts the `moov` atom.

**Client-side progressive playback** (`web/components/HlsPlayer.tsx` + inline viewer in `webapp.py`):
`PREBUFFER_TARGET = 15` seconds buffered before `play()` — because the swap runs *slower than realtime*
(8–13 fps at 1080p vs 25–30 fps playback), so the buffer must absorb the deficit; `REBUFFER_TARGET = 8` s
to resume after a stall. hls.js config: `liveSyncDuration: preBufferSeconds, liveMaxLatencyDuration: 60,
maxBufferLength: 60, maxMaxBufferLength: 120, backBufferLength: 90`, plus **60 retries at 800 ms** on
manifest/level/frag loading (early polls hit a playlist with zero or one segment). Autoplay rescue via
`muted = true` + a "🔊 Click to unmute" pill, with the documented gotcha: *"Don't set `playStarted = true`
before `play()` resolves. A rejected promise leaves you wedged."* On completion the player swaps `src` to
the static MP4 and destroys the Hls instance. Server sets `Cache-Control: no-store` on all HLS responses
and path-whitelists `.m3u8`/`.ts`.

**Pipeline:** 4-stage bounded-queue thread pipeline, `Q_DEPTH = 128` ("each queue ~800 MB at 1080p"):
`reader (cv2.read) → detect (fa.get + embedding argmax) → main (sw.get swap) → writer (ffmpeg.stdin.write)`,
each forwarding an `END` sentinel. The honest note in `docs/ARCHITECTURE.md` §7: ORT serialises GPU calls
across threads, so *"The win from the pipeline isn't parallel GPU work; it's that CPU work (decode,
embedding match, pipe write, paste_back) overlaps with GPU work."*

**Models:** InsightFace `buffalo_l` at `det_size 480`; `inswapper_128_fp16.onnx` via **TensorRT FP16**
(engine cached, 60–90 s first build); `GFPGANv1.4.pth`; onnxruntime-gpu 1.23.2, TensorRT 10.x, CUDA 12,
ffmpeg 8.1. Matching: 512-d embeddings, cluster threshold cosine 0.30, per-frame `REFERENCE_THRESH = 0.22`,
batched `tgt_embs @ ref_embs.T` then argmax.

**Throughput (RTX 4090 Laptop, TRT FP16, det_size 480):** 480×360 → 30–45 fps; 640×480 → 18–25;
1280×720 → 12–18; 1920×1080 → 8–13. A commit-by-commit optimisation ledger is kept (7.5 → 10.1 async
writer → 10.8 async reader → 11.7 det_size 480 → 12+ batched embedding dot → 12+ 4-stage pipeline). A
multiprocess variant `webapp_mp.py` (`FACESWAP_WORKERS=6`) claims **33 fps at 1080p** at 87–95% SM util.
Time-to-first-frame ≈ 15 s prebuffer + ~30 s model warmup.

Job phases polled from `/job/<id>/status`:
`queued → loading_models → detecting_source → finding_reference → streaming → finalising → done`.

### C.4 `/home/eranti/dlmastery/lumiere.ai` — the full concept → video → narration pipeline

Vite 6 + React 19.2 + TS 5.8, `@google/genai@^1.31.0`, Firebase 12.8. `vite.config.ts` `define`s
`process.env.API_KEY` at build time — key in the bundle again.

Model IDs, all in `/home/eranti/dlmastery/lumiere.ai/services/geminiService.ts`:

| Purpose | Model ID |
|---|---|
| Director's treatment (concept) | `gemini-3-flash-preview` |
| Storyboard / script, refinement | `gemini-3-pro-preview` |
| Scene stills | `gemini-3-pro-image-preview` (`imageConfig = { aspectRatio:"16:9", imageSize:"1K" }`) |
| **Video** | **`veo-3.1-generate-preview`** |
| TTS | `gemini-2.5-flash-preview-tts` |

**Veo long-running-operation polling** (`generateSceneVideo`) — the canonical loop:
```ts
let operation = await ai.models.generateVideos({ model:'veo-3.1-generate-preview', prompt,
                    image:{imageBytes, mimeType}, config });
while (!operation.done) {
  await new Promise(r => setTimeout(r, 10000));        // fixed 10 s poll, no backoff, no timeout
  operation = await ai.operations.getVideosOperation({ operation });
}
const videoUri = operation.response?.generatedVideos?.[0]?.video?.uri;
const videoRes = await fetch(`${videoUri}&key=${process.env.API_KEY}`);   // URI needs the key appended
return URL.createObjectURL(await videoRes.blob());
```
Config `{ numberOfVideos:1, resolution:'720p', aspectRatio:'16:9' }` plus optional
`config.lastFrame = { imageBytes, mimeType }` — **first-frame + last-frame conditioning**, which is how
scene-to-scene continuity is achieved (each scene carries `description`, `narrative`,
`lastFrameDescription`).

**TTS → playable audio (the correct pattern):** `responseModalities:[Modality.AUDIO]` +
`prebuiltVoiceConfig.voiceName` (Kore/Puck/Charon/Fenrir/Zephyr) → base64 → `Uint8Array` →
`addWavHeader(bytes, 24000, 1)` (hand-written 44-byte RIFF/WAVE, PCM 16-bit mono 24 kHz) → `Blob` →
`URL.createObjectURL`.

**UI:** 4-view state machine in `App.tsx` (`hero | concept | planning | workspace`) with per-scene
`SceneStatus`. `components/Player.tsx` (22 KB) is a **canvas compositor**: `<canvas>` +
`requestAnimationFrame` drawing either the Veo clip or the still with a Ken Burns pan/zoom, aspect-fit
maths, captions, an `AudioContext` for voiceover, and **`MediaRecorder` to export the composed timeline
as a downloadable video**. The storyboard prompt uses a two-persona "Director drafts / Critic reviews"
structure with a `responseSchema` and a regex stripping `Voiceover:|Narrator:|Caption:` prefixes.

**This is a complete lesson-video pipeline that nobody pointed at a lesson.**

### C.5 Local generative-video infrastructure

**`/home/eranti/Wan2GP`** — upstream **WanGP by DeepBeepMeep** ("The best Open Source Generative Models
Accessible to the GPU Poor"), v12.3 (July 2026). Interface: **Gradio 5.29**, monolithic entrypoint
`wgp.py` (**766 KB**). `wan2gp.log` confirms it last ran at `http://localhost:7860` with an INT8
Quanto/triton backend and a "Motion Designer" plugin. Model zoo: video (Wan 2.1/2.2, LTX-2, Hunyuan
Video 1/1.5, LongCat, Kandinsky, MagiHuman), image (Qwen Image, Z-Image, Flux 1/2, HiDream, KREA-2),
audio/TTS (Qwen3 TTS, Ace Step 1/2/XL, Omnivoice, Index TTS2, Chatterbox), plus MMAudio soundtracks,
SeedVC voice replacement, RIFE/FlashVSR upsampling, whisper + pyannote diarization, LoRAs, and
int8/fp8/gguf/NVFP4/Nunchaku quantisation down to a **6 GB VRAM floor**. Launch: `scripts/install.sh` +
`scripts/run.sh`, or Docker (`Dockerfile` + `entrypoint.sh` with CUDA sanity checks). Has a headless/batch
mode and a **"WanGP API"** for embedding generation into other apps — that API is the hook if a learning
app needs local asset generation.

**`/home/eranti/wan-streamer`** — upstream **StreamDiffusionV2** (MLSys 2026 Best Research Paper,
arXiv 2511.07399, Apache-2.0). Wan2.1-T2V-1.3B or -14B base + distilled causal-DMD v2v checkpoints
(2-step / 1-step), optional TAEHV VAE decoder and TensorRT. Chunk-wise API you drive yourself:
`stream.prepare(prompt)` → `chunk_video` → `encode_chunk` → `denoise_chunk` → `decode_chunk`, with
sliding-window attention over a ring-buffer KV cache. Three launchers: `run_v2v.sh` (offline batch,
`torchrun` pipeline-parallel across GPUs), upstream `demo/` (FastAPI + WebSocket `/api/ws/{user_id}` +
SvelteKit frontend on 7860, 16 FPS input throttle, per-frame latency queue), and a **locally written**
`demo_stream/` ("Wan Streamer 0.2", port 7870, stdlib `ThreadingHTTPServer`, MJPEG over
`multipart/x-mixed-replace` into a plain `<img>`, with `POST /prompt`, `/start_image`, `/control`).

The transferable idea is its **hot-swap without reload**, verbatim from `demo_stream/server.py`:

> Hot-update model: the generation loop re-reads shared params (effective prompt, input source, denoise
> strength, seed) at every chunk boundary. Whenever any of them changes (signalled by a bumped source_id)
> it re-runs prepare(prompt) — which re-encodes the UMT5 text embedding / conditional_dict — and rebuilds
> the input chunks, WITHOUT reloading the ~5.6GB model. The model is loaded once.

And its own honesty note, which the survey should quote as a model of calibrated claiming:

> HONESTY: this is NOT a real-time interactive avatar. It is a low-FPS (~1.8 FPS on this GB10, arm64, no
> flash-attn/TensorRT) video-to-video style transfer stream. The keyboard keys drive diffusion PARAMETERS,
> not 3D camera or character movement (that would require a world model).

**Verdict for the survey: live generative video as a tutor avatar is not viable today on this hardware
(~1.8 FPS). Asynchronous generated lesson media streamed progressively over HLS is viable now.**

### C.6 The multimodal stack, assembled

Nothing new needs to be invented to build a real-time multimodal tutor from this portfolio:

| Capability | Source | Status |
|---|---|---|
| Bidi live voice, persona, barge-in | `gemini-enhanced.ts` / Spanish+Telugu bundles | working, needs key moved server-side |
| Live camera into the model (1 FPS JPEG) | `gemini-enhanced.ts` | working |
| Model drives UI mid-sentence via tools | `FUNCTION_DECLARATIONS` + dual dispatch | working |
| Affect-conditioned pacing | `report_emotion_observation` + prompt block | working (meditation only) |
| Cross-session memory injection | `guru-memory.ts` | working (meditation only) |
| PCM→playable audio at 24 kHz | `lumiere.ai addWavHeader` | correct impl exists |
| Scheduled gapless playback queue | Spanish/Telugu bundles | correct impl exists |
| Concept → storyboard → stills → video → VO → MP4 | `lumiere.ai geminiService.ts` + `Player.tsx` | working |
| Scene-to-scene visual continuity | Veo `lastFrame` conditioning | working |
| Watch-while-rendering (HLS, A/V synced) | `face-swap-streamer` | working, with negative results documented |
| Phase-based long-job progress UI | `face-swap-streamer` `/job/<id>/status` | working |
| Reactive 3D ambience | `CosmicScene.tsx` | working |
| Asset-free audio feedback cues | `meditation-audio.ts` | working |
| Local/offline generation fallback | Wan2GP (API + headless), wan-streamer | working, async only |

**The two things this stack cannot do are the two things a tutor needs most: it cannot say what the
learner knows, and it cannot run offline on a $50 phone.**

---

## D. The autoresearch family — candidate method for autonomous curriculum improvement

### D.1 Inventory

| Repo | Vis. | Lang | Size | Description (verbatim) |
|---|---|---|---|---|
| `autoresearch` | pub | Python | **227 MB** | "AutoResearch: Karpathy-style autonomous FX prediction optimization. Residual MLP champion test Sharpe +6.21" |
| `autoresearchspy` | pub | Python | **87.7 MB** | "Autonomous SPY (S&P 500 ETF) prediction — successor to dlmastery/autoresearch (FX). Three causally-anchored feature streams (daily yfinance + Asian/European pre-market block + Barchart.com hourly), **7-step Karpathy-style research loop**, and a comprehensive docs set." |
| `autoresearchindexstock` | pub | Python | 29.4 MB | "QQQ Nasdaq-100 index/stock autoresearch loop — **216+ experiments, 5 backbones complete**, mamba dmamba global champion +1.32 composite Sharpe" |
| `autoresearchtabular` | pub | Python | 435 KB | "Higgs UCI tabular benchmark (Baldi 2014). **25 experiments per backbone, 14 backbones. Citation Rigor + Reasoning Blob audit gates.**" |
| `autoresearchimage` | pub | Python | 24.8 MB | "Autonomous ML research loop for medical-imaging OOD AUC (PathMNIST/Camelyon17)" |
| `autoresearch_dsbench` | pub | HTML | 27.8 MB | "DSBench (ICLR 2025) solved with the autoresearch protocol: 74 Kaggle modeling + 38 Modeloff analysis tasks, **hill-climbed train/val only, 10-agent forensic audit, 44-skill industry-shareable pack. 82/112 beat DSBench, 112/112 forensic PASS.**" |
| `autoresearch_darebench` | pub | HTML | 812 KB | "DARE-bench (ICLR 2026, Snowflake-Labs) autoresearch port: **324 eval-task scaffolds + 11-agent forensic committee (incl. Agent K forbidden-path enforcer) + eval-only inversion.**" |

Adjacent members of the same family: `auto-research-voice-based-disease-detection` (*"Autonomous,
pre-registered research program… laptop-scale, rigor-gated, negative-results-first"*),
`nature_inspired_networks` (*"autoresearch-style ablation… 71 hypotheses + paradigm comparison"*),
`environment_stats_talk` (86 MB, *"autoresearch protocol, skills, runnable on a 4090"*).

Lineage is explicit: FX (`autoresearch`) → medical imaging (`autoresearchimage`) → tabular
(`autoresearchtabular`) → equity (`autoresearchspy`, `autoresearchindexstock`) → benchmark fan-outs
(`autoresearch_dsbench`, `autoresearch_darebench`). A domain-agnostic extraction exists at
`autoresearch/generalized_ml_autoresearch/` (44 files, "52/52 CLAUDE.md sections preserved") — **this is
the version that would be repointed at curriculum.**

### D.2 The loop, verbatim

**Framing** (`autoresearch/AUTORESEARCH_PROCESS.md`, mirrored in `autoresearchspy/`):

> ## Karpathy's Original Principle (github.com/karpathy/autoresearch)
> Karpathy's autoresearch: modify → train (5 min) → check if improved → keep/discard → repeat.
> "Everything is fair game: architecture, hyperparameters, optimizer, batch size."
> The agent runs autonomously until interrupted. One file modified. One metric to beat.

Three declared deviations from Karpathy:
> 1. **NEVER deviate far from the winner.** … The winner config is sacred — every experiment starts from it.
> 2. **Claude IS the expert researcher.** Karpathy's agent just tries things. Our agent must DIAGNOSE
>    per-fold, cite literature, form hypotheses…
> 3. **Epoch-bound, not time-bound.** 20 epochs with early stopping.

Core invariant:
> **Always start from the current best config. Modify ONE thing. Keep if composite improves. Revert if
> not. Never wander off.**

**The seven steps, named** (`## The Loop (Every Iteration)`):

1. **Read Results** — load `experiment_log.jsonl` (full history) + `best_config.json` (champion);
   examine per-window breakdown for BOTH val and test.
2. **Diagnose (This Is Where The Work Happens)** — five sub-analyses: *per-fold forensics*,
   *train–test gap analysis* (`gap < 0.5` healthy; `0.5–1.5` mild overfitting; `> 2.0` severe, needs
   structural change), *val–test consistency*, *composite decomposition*, *trajectory analysis*.
3. **Research (Go Deep When Stuck)** — literature keyed to the diagnosed failure mode.
4. **Hypothesize** — *"Write a SPECIFIC, FALSIFIABLE hypothesis"*; explicitly negated:
   `NOT: "Let me try warmup and see what happens."`
5. **Design ONE Experiment** — *"Change exactly ONE thing from the current best config… Predict what you
   expect to see."*
6. **Run & Analyse** — *"If composite improved → new best. If not → revert, hypothesis was wrong."*
7. **Decide Next Direction** — *"If REVERT after 3+ tries on the same problem: rethink the diagnosis…
   Occasionally try RADICAL changes to escape local optima."*

The ASCII form in `autoresearch/README.md` §"Seven-Step Scientific Process" names them differently and
more usefully:

```
 +---> 1. DIAGNOSE -----> Per-fold failure analysis
 |     2. CITE ---------> Literature search
 |     3. HYPOTHESIZE ---> Form a testable hypothesis
 |     4. PREDICT -------> State expected outcome BEFORE running
 |     5. RUN -----------> Execute ONE experiment
 |     6. ANALYZE -------> Compare per-fold deltas to champion
 |     7. CHECKPOINT ----> Save state for crash recovery
 +--------<+ (loop)
```

Canonical one-liner (`autoresearchtabular/AUTORESEARCH_PROCESS.md`):
`diagnose → cite → hypothesize → predict → run-ONE → analyze → checkpoint`, with the enforcement note:

> "The first four steps happen **before** training… Step 7 is the persistence step where the experiment
> row is appended to the leaderboard. **The runner refuses transitions in any other order.**"

An 8-row **Anti-Patterns** table accompanies it: *"Let me try X and see"* → *"I'm trying X because
[diagnosis] and [paper] suggests [mechanism]"*; *"Grid search (try 5 values of lr)"* → *"Diagnose →
hypothesize → test ONE value with justification"*; *"Changing 2+ things at once"* → *"ONE change."*;
*"Running without diagnosing"* → *"NEVER run an experiment without first writing the diagnosis"*. Plus a
section headed *"What Makes This Different From Hyperopt/Optuna"*: **"The researcher's advantage over
Optuna is understanding. Optuna can't read a paper."**

The whole method is packaged as a portable skill —
`autoresearch_dsbench/skills/autoresearch-pack/skills/seven-step-research-process/SKILL.md` — one of 48
in the pack.

### D.3 The hypothesis registry — the mechanism the survey should steal

Two parallel artifacts per experiment. **Neither is a database.** Append-only JSONL + JSON + Markdown.

**Reasoning registry** — `autoresearch_results/reasoning_annotations.json`, keyed by `experiment_num`,
with **machine-enforced word floors**:

| Field | Content | Floor |
|---|---|---|
| `diagnosis` | Why THIS experiment now: which champion weakness, which fold weakest, what prior experiments ruled out | ≥60 words |
| `citations` | Full author/year/venue/title/arXiv-id/relevance-note per paper | ≥40 words |
| `hypothesis` | "parameter X = value Y will change metric Z via mechanism M"; must contain "because" or "per [paper]" | ≥50 words |
| `prediction` | Numeric range on composite + a sub-prediction on at least one fold | ≥25 words |
| `verdict` | KEEP/DISCARD/NEAR-MISS + composite + delta vs champion + per-fold narrative | ≥30 words |
| `learning` | What this updates in the mental model; axis closed/open; next try | ≥40 words |

> **Two-phase write per experiment:** (1) **BEFORE launch** Claude inserts `diagnosis`, `citations`,
> `hypothesis`, `prediction`. **Experiment does not launch until this entry exists.** (2) **AFTER
> completion** Claude appends `verdict` + `learning`.

The generalised implementation is `core/reasoning.py`:

```python
WORD_FLOORS = {"diagnose":25, "cite":30, "hypothesize":30,
               "predict":25, "run":15, "analyze":50, "checkpoint":15}

def validate_reasoning_blob(blob, *, post_run):
    sections = ["diagnose","cite","hypothesize","predict","run"]
    if post_run: sections += ["analyze","checkpoint"]
    for s in sections:
        if s not in blob: raise ReasoningGateError(f"missing section '{s}'")
        if len(blob[s].split()) < WORD_FLOORS[s]: raise ReasoningGateError(...)
    validate_citation_rigor(blob["cite"])
```

**Experiment ledger** — `autoresearch_results/experiment_log.jsonl`, append-only, one object per line.
Actual row 1 from `autoresearchtabular` (~97 rows, 250 KB):

```json
{"experiment_num":1,"timestamp":"2026-04-26T06:46:35Z","backbone":"lightgbm",
 "description":"exp1 [lightgbm#1] default 1000 leaves 63 lr 0.05","seed":0,
 "params":{...}, "metrics":{"train":{...},"val":{...},"test":{...}},
 "composite":0.830114864061622,
 "composite_formula":"min(test_auc, val_auc) - 0.1 * abs(test_auc - val_auc)",
 "composite_fingerprint":"dc2d2526d9bf12e1",
 "train_time_s":96.66,"status":"KEEP/CHAMPION"}
```

Note `composite_fingerprint` — a SHA-256 of the objective formula string embedded in **every** row.
*"If anyone tries to silently swap the formula mid-campaign, the runner refuses to start
(**Goodhart-fingerprinting**)."* **This is the single most transferable safeguard in the whole portfolio
for anyone proposing to optimise a curriculum against a learning metric.**

### D.4 How experiments are proposed

**(a) LLM-authored, one at a time** (FX / SPY / QQQ / image / tabular). Claude writes the pre-run blob,
changes ONE knob, runs. *"ALWAYS hill-climb from the per-backbone champion (highest composite, NOT
highest A_sharpe…). One config change per experiment. ONE arXiv-cited rationale per experiment."*

**(b) Programmatic proposal library** (dsbench 112 tasks, darebench 324). `framework/hill_climb.py`:
`ITERATIONS_PER_BACKBONE = 25`, `EXTENDED_ITERATIONS = 200`. Per ADR-0005:

> **Every backbone runs 25 iterations. No early stop.** … 1. **Iter 1 is the published paper default**
> (Chen & Guestrin 2016 KDD for XGBoost; Ke et al. 2017 NeurIPS for LightGBM). 2. **Iters 8 and 9 are
> seed perturbations** (`seed=7`, `seed=99` paired with default `seed=42`) to compute a 3-seed median
> champion. Without this, claimed champions can be variance flukes.

Rationale for no early stop: *"Negative results inform downstream backbones. Knowing that
`colsample=0.5` failed on XGBoost shapes the LightGBM `feature_fraction` proposal."*

DARE-bench adds a **prompt-template axis** for grader-based tasks — `PROMPT_TECHNIQUES` of 8, each with
an arXiv citation: `zero_shot`, `cot`, `react`, `self_consistency`, `plan_and_solve`, `tree_of_thoughts`,
`least_to_most`, `reflexion`. **This is the closest existing analogue to sweeping *explanation
strategies* rather than model hyperparameters — and it is exactly the axis a curriculum loop would use.**

Conditional deepening (ADR-0006): a 200-iteration recovery cycle runs only on tasks still losing after
the base 125, across 15 extra backbone families, appending to the *same* ledger; stop when 200 complete
OR composite delta > 0.02 over baseline.

### D.5 Gating — five layers, all fail-fast

**Gate 1 — Data-split audit** (`core/evaluation/audit.py`, "7 auditors, `audit_or_die()`"):
split disjointness (*"Failures here are immediately fatal — there is no recovery path"*), split protocol,
class balance, size floors, no-leakage-via-metadata, reproducibility (`sha256(X.tobytes())`), feature
consistency. Emits a `data_split_fingerprint.txt` recorded in every experiment row —
*"if it ever changes, every prior leaderboard row is invalidated by definition."*

**Gate 2 — Citation Rigor.** A parser, not a norm:

```python
def validate_citation_rigor(text):
    if not re.search(r"[A-Z][a-z]+\s+\d{4}", text): raise ...("citation missing author + year")
    if not (re.search(r"§\s*\d", text) or re.search(r"Tab\.?\s*\d", text)
            or re.search(r"Fig\.?\s*\d", text)):    raise ...("missing section/table/figure reference")
    if "Higgs" not in text and not re.search(r"\b(low-level|high-level|jet|lepton|...)\b", text):
                                                    raise ...("citation missing reason naming ...")
```
Required format: `{hp_name} = {value} per {Author Year} §{section} ("{title}", {venue}) — {reason}`.
*"Bare URLs are rejected. Folklore ('LightGBM likes 256 leaves on big data') is rejected."*
The FX/SPY prose form requires 6 elements including `(arXiv:XXXX.XXXXX)`, with worked BAD examples.

**Gate 3 — Reasoning Blob Completeness** (§D.3). *"The runner refuses to start training without a
passing pre-run blob, and refuses to write the result row without a passing post-run blob."*

**Fail-fast semantics, verbatim:** *"Any auditor that fails raises `AuditFailure`, which is not caught.
The process exits with non-zero. The `all_runs.csv` is untouched. There is no 'warning, continuing
anyway' mode. … **There is no 'force-pass' mode. There is no `--skip-audit` flag. This is also by
design.**"*

**Gate 4 — Forensic committee.** `dsbench` runs **10 independent agents** (ADR-0004); `darebench` runs
**11 (A–K)**:

| Agent | Concern | Class |
|---|---|---|
| A | split-hash integrity (eval_test never read during hill climb) | FAIL |
| B | target/label leakage (MI per feature vs label) | FAIL |
| C | row overlap (train/val/test disjoint) | FAIL |
| D | distribution shift (KS per feature) | FAIL |
| E | anomaly (val > train, perfect 1.0, jumps > 0.3) | FAIL (whitelisted) |
| F | static-code grep for `X_test` / `y_test` | FAIL |
| G | temporal ordering | FAIL |
| H | seed stability | RECORD-ONLY |
| I | refit consistency (champion refits within ±0.005 of recorded test score) | FAIL |
| J | backbone diversity (≥3 distinct backbones tried) | WARN |
| K | **forbidden-path access** (static grep + runtime `open()` audit-log tail) | FAIL |
| Z | committee verdict aggregator | — |

Structural rule: *"**Independent agents.** No agent reads another's output during its check; they all
read raw artefacts… a bug in one agent can never silently corrupt another."* Cost: *"10 agents × 112
tasks = 1120 checks per audit. Total runtime ~10 minutes."*

**Gate 5 — Four-layer audit gate (ADR-0015):** (1) section coverage — 112/112, no `X_test` in runner
code; (2) forensic committee — 112/112 PASS; (3) explainability — **14 required sections** in every
winner's `audit_report.md`; (4) skill-pack coverage — every H2/H3 in the source CLAUDE.md files maps to
≥1 skill. Run via a 9-step commit ritual. Honest caveat quoted in-repo: *"The 9-step ritual takes ~15
minutes end-to-end… the ritual is **per-batch, not per-experiment**."*

### D.6 Champion selection and leakage control

**The objective is deliberately gap-penalised**, and is the sole criterion:

- Tabular/Higgs: `composite = min(test_auc, val_auc) − 0.1·|test_auc − val_auc|` (SHA-256 fingerprinted)
- FX/SPY: `composite = min(test_sharpe, val_sharpe) − 0.1·n_negative_folds`
- DSBench (test-embargoed): `composite = min(val, train) − 0.05·|val − train|`

> **Winner = global champion across ALL backbones AND ALL experiments** (by composite). Per-backbone
> bests are tracked separately but only the global best gets archived.

On promotion, `winners/<backbone>_exp<N>_<desc>/` archives `config.json`, `model_checkpoint.pt`, a
**frozen `code/` snapshot**, `inference/predict.py`, `reproduction/reproduce_log.txt`, a 14-section
`audit_report.md`, and a Colab notebook — plus a seed-fixed reproduction run and, at campaign end, a
**3-seed rerun** of the cross-backbone champion to record mean ± std.

**Leakage control — ADR-0002, "Hill-climb on train + val only; touch test once via `final_report.py`":**

> 1. **Code-gen invariant.** `generate_scaffolds.py` writes per-task runners that never reference
>    `X_test` or `y_test`.
> 2. **Runtime invariant.** `runner.py:run_one` predicts on `X_train` and `X_val` only.
> 3. **Forensic invariant.** Agent F greps for `X_test`/`y_test`; ANY reference is a FAIL. Agent A
>    re-hashes the test split pre/post run to confirm no read happened.

Named principle: **The Test-Set Embargo Rule** — *"if the test set is read once, it leaks once. There is
no 'just a peek' allowance. The only legal reader is `framework/final_report.py`, exactly once per
task."* Acknowledged cost, quoted honestly: *"The dashboard physically has no test-metric column for
non-champion rows."*

DARE-bench goes further with **eval-only inversion**: the 4,274-task HuggingFace benchmark-*train* half
is forbidden entirely; within each eval task, `verify/ground_truth*.csv` and `val_v*` are a second
forbidden surface; **Agent K tails `data/read_audit.log` and fails the run if any forbidden path was
opened.**

Domain-specific extras in FX/SPY: 7 regime windows (2006–2024) with a **90-day purge gap, 21-day embargo,
10-day label-horizon buffer**; a **shuffle test** (train on permuted labels, evaluate on real test —
FX result +0.006 Sharpe, i.e. no leakage) triggered whenever a tree model beats the best deep baseline by
> +1.0; a documented caught bug (*"FX's first XGBoost run gave composite −1.61 due to
`y = seg_tgt.values[seq_len:]` (lookahead by 1)… Fix gave +8.78 jump"*); and a hard `seq_len ≤ 60` rule
because larger windows silently skip val folds (*"NOT strict data leakage… but it IS metric-integrity
violation"*).

**Anti-local-optimum rule:** *"Three consecutive DISCARDs = STOP, rethink mechanism. Not 'try the next HP
axis'. … Multiple failures mean your hypothesis about what to change is wrong. The answer is NOT more
hyperparameter tweaks — it's a structural change."* `autoresearchspy/CLAUDE.md` reports **DISCARD ratios
of ~60% (FX) and ~70% (SPY) as a positive signal**: *"High DISCARD ratio is a sign of non-trivial
hypotheses."* It also contains a self-critical *"Don't-repeat-on-SPY list (mistakes I made already)"*
enumerating 7 protocol violations by the agent itself.

### D.7 Scale actually run

| Repo | Experiments | Backbones |
|---|---|---|
| `autoresearch` (FX) | 151 across 4 backbones (badge says 104; 265 at paper time — the counts are inconsistent across files) | MLP, LSTM, PatchTST, PatchTSMixer, LFM2-350M, XGBoost, LightGBM, CatBoost |
| `autoresearchspy` | 62 at transfer time; ~144+ trade logs; 350 more planned | MLP, LSTM, Mamba/dMamba, XGB, LGBM, CatBoost + 14 roadmapped |
| `autoresearchindexstock` | **216+** | 5–6 complete |
| `autoresearchtabular` | 25 × 14 = 350 planned; ledger at ~97 | LR, RF, LGBM, XGB, CatBoost, MLP, FT-Transformer, SAINT, NODE, TabNet, TabM, ResNet-tabular… |
| `autoresearchimage` | 21 (18 synthetic + 3 real WILDS-Camelyon17) | — |
| `autoresearch_dsbench` | 74×5×25 = **9,250** modeling + 38×25 = **950** analysis; docs claim **~14,000** total incl. the extended phase | 19 catalogued, 5 runner + 15 extension families |
| `autoresearch_darebench` | 324 scaffolds generated, **0 run** | ≥3 arXiv-cited per category |

Outcomes: FX champion LSTM Exp35 composite +6.4242 (test Sharpe +6.5242, 7/7 positive folds); QQQ
champion mamba dmamba exp52 composite +1.3216; tabular champion `ft_transformer` #95 composite 0.8723;
DSBench **82/112 BEAT, 112/112 FORENSIC PASS**; image real WILDS test_ood AUC 0.9220 ± 0.018 (3-seed) vs
Koh 2021's 0.853 ± 0.020.

### D.8 Persisted state — "the repository is the memory"

```
autoresearch_results/experiment_log.jsonl      — append-only experiment log
autoresearch_results/best_config.json          — current champion config + full results
autoresearch_results/reasoning_annotations.json— the hypothesis registry (two-phase write)
autoresearch_results/dashboard.html            — decoupled visual dashboard
research_journal.md / experiment_summary.md    — Claude-authored narrative, appended every run
memory/project_autoresearch_checkpoint.md      — the crash-recovery checkpoint
winners/<backbone>_exp<N>_<desc>/              — archived champion + frozen code
data_split_fingerprint.txt / .composite_fingerprint.json  — integrity anchors
```

The checkpoint is the load-bearing artifact:

> - **Checkpoint every 5 minutes AND after every experiment** (whichever comes first)
> - Contains: champion config, composite score, per-fold table, last experiment result, **exact next
>   command to run**, rationale, exhausted axes
> - **Self-contained:** A fresh Claude Code session reading ONLY `CLAUDE.md` + the checkpoint can resume
>   without reading any other file

The theoretical justification, from
`autoresearch_dsbench/docs/part_1_thesis/01_what_is_autoresearch_engineering.md`, is the single most
directly transferable paragraph in the family:

> AutoResearch projects sit on a fourth axis that the SWE-book doesn't address directly: **collaborator
> turns**. The LLM collaborator … has no persistent memory; every session starts cold. **The repository
> *is* the memory.**
> … A traditional ML project has a human researcher whose memory persists between sessions; if a tuning
> knob feels exhausted, the human remembers and doesn't re-try it. Our collaborator forgets. The
> Per-Backbone 25-Experiment Mandate is the rule that converts **"the human remembers" into "the log
> remembers and the next session reads the log"**.

Plus the context economics that force the design: *"Loading `CLAUDE.md` + the checkpoint + the last three
rows of `experiment_log.jsonl` is **~6 K tokens**; loading the global state would be ~600 K and
unworkable."*

**This is precisely the learner-model problem restated for agents. The portfolio solved "how does a
memoryless agent accumulate knowledge across sessions" and did not apply the same solution to "how does a
tutor accumulate knowledge about a learner across sessions."**

### D.9 Autonomy — the honest answer

**Mixed.** The repos *claim* full autonomy (`autoresearch/README.md`: *"Claude Code reads results,
diagnoses per-fold failures, cites published papers, forms hypotheses, runs experiments, and checkpoints
state. **No human in the loop during experimentation.**"*; Agent Rule 7: *"**The agent never stops.**"*).

The actual structure is **Claude as the outer loop, deterministic machine gates on the inner loop**. The
sequence diagram `docs/appendix_d_diagrams/per_experiment_lifecycle.mmd` is literally titled *"Per-experiment
lifecycle — **Claude as outer loop**"*: Claude pre-writes the reasoning blob → invokes proposal N →
runner fits on train/val → computes composite → appends JSONL → overwrites `best_config.json` if better
→ Claude post-writes verdict + learning → updates checkpoint with the next command. **The decision is
Claude's; the keep/discard is a deterministic comparison; the permission to run at all is enforced by
non-bypassable programmatic gates.**

Genuinely unattended batch execution exists in dsbench (two background jobs of 9,250 + 950 experiments,
resumable and idempotent). A fully-API-driven variant exists as a side branch —
`autoresearchspy/optimizer/agent_loop.py` (13.5 KB) with a `MODIFIABLE_FILES` whitelist,
`py_compile` syntax validation, a `.optimizer_backups/` rollback dir and `optimizer_state.json`, driven
by `run_overnight.py` — but it is small and older than the CLAUDE.md-driven protocol.

Human gating points that remain: user directives logged inline in `CLAUDE.md` redirect strategy between
batches; the CPU-pinning rule (*"NEVER lift this without explicit user approval"*); the 4-layer gate runs
per-batch and is *"a script, not a CI pipeline. **Self-discipline is required to actually run it.**"*;
and `final_report.py` (the single test-set touch) is a separate deliberate invocation.

### D.10 Why this matters for curriculum

Map the loop onto teaching and it becomes an **autonomous curriculum-improvement protocol**:

| Autoresearch element | Curriculum analogue |
|---|---|
| Fingerprinted composite objective | Learning gain, gap-penalised: `min(post_test, retention_30d) − λ·|post_test − retention_30d|`, SHA-256 pinned so nobody quietly swaps it when the number stops moving |
| Backbone sweep (25 iters, no early stop) | Explanation-strategy sweep: analogy-first vs formal-first vs worked-example vs Socratic vs interleaved — **the DARE-bench `PROMPT_TECHNIQUES` axis is already exactly this** |
| Iter 1 = published paper default | Lesson v1 = the textbook's own treatment; every variant must beat it |
| Iters 8, 9 = seed perturbations | Re-run the same lesson with different cohorts to separate a real gain from cohort variance |
| Hill-climb on train/val, embargo test | Tune on a pilot cohort; embargo a held-out cohort so the curriculum is not overfit to the learners who co-wrote it |
| Test-Set Embargo Rule + Agent A/F/K | A learner cohort that the authoring loop may never read, enforced by codegen + runtime + forensic grep |
| Citation Rigor gate (a regex, not a norm) | Every SOTA claim in a lesson must parse as `{claim} per {Author Year} §{section} ("{title}", {venue}) — {reason}`. Already a *stated* requirement of `zero-to-hero-colab`; here it is *enforced* |
| Reasoning Blob word floors | Every derivation step carries its `(reason)` annotation — already non-negotiable #9 of `concept-mastery-colab`, unenforced |
| 10/11-agent forensic committee, independent | `colab_qc.py`'s grounding + caption + leaked-label checks promoted to independent adversarial agents that read only raw artifacts |
| Three-consecutive-DISCARD rule | Three failed reworks of a lesson = the diagnosis is wrong; change the pedagogy, not the wording |
| High DISCARD ratio as a *positive* signal | A curriculum loop that keeps every change is testing trivial hypotheses |
| Crash-recovery checkpoint | The **learner model** — self-contained, resumable by a memoryless session, containing the exact next action |
| Winner archive + frozen code snapshot | The promoted version of a lesson, with its generator pinned so it is reproducible |
| 48-skill pack extraction | `skills/zero-to-hero-colab` and `concept-mastery-colab` themselves |

**The author has already built both halves and has not connected them.** `class` has the QC harness
(`colab_qc.py`, `verify_grounding.py`) and the coverage auditor (`AUDIT_TOC_COVERAGE.md`) but no
objective function, no experiment ledger, and no hypothesis registry. `autoresearch*` has the ledger, the
registry, the sweep, five layers of gates, champion archiving, and the "repository is the memory" thesis —
but is pointed at Sharpe ratios. **Joining them is the concrete, novel contribution the survey can
propose**, and the missing piece is the only genuinely hard one: a learning-gain signal. That requires
assessment, which §B.4 shows does not exist, which §A shows the Live API could already emit via
`provide_feedback` / `mark_word_practiced` function calls.

Two cautions the survey should carry forward, both stated in the repos themselves:

1. **Goodhart is the named enemy.** The composite-fingerprint mechanism exists precisely because an
   agent optimising a scalar will drift the scalar. A curriculum objective is far softer than AUC and
   correspondingly easier to game — a loop that hill-climbs "post-test score" will discover teaching to
   the test within a handful of iterations. The fingerprint plus the embargoed cohort are the minimum
   defences, and they are not sufficient.
2. **The autonomy claim does not survive contact with the code.** These repos advertise "no human in the
   loop" and are in fact Claude-as-outer-loop with human strategy redirection between batches and a
   commit ritual that *"requires self-discipline to actually run."* A survey section on autonomous
   curriculum improvement should describe the achievable version — machine-gated inner loop, human
   strategy setting — not the advertised one.

---

## E. Synthesis

### E.1 The recurring architecture

Six of the nine deployed apps are the same machine with different prompts:

```
Google AI Studio "Build"  →  single-page React 19 app
      ↓                        · esm.sh importmap (no bundler deps)
   Vite build                  · cdn.tailwindcss.com (runtime CDN, not a build step)
      ↓                        · @google/genai in the BROWSER
 Docker → Cloud Run            · window.aistudio.openSelectKey()  ← learner's own API key
 us-west1, project 262451841611
      ↓
 Gemini 3.x Flash / Flash-Lite  (structured JSON via responseSchema)
 + Gemini Live (native audio, bidi WS)   + Gemini TTS   + gemini-embedding-001
 + googleSearch & urlContext grounding   + thinkingConfig
```

Ekalavya alone breaks the pattern with a server tier (`/api/gemini/generate`, `/api/gemini/tts`,
`/api/live`), Firebase Auth, and Firestore persistence — and it is, not coincidentally, the only one with
a durable artifact.

**Consistent design vocabulary across all of them:** a hero landing with an aspirational one-liner; a
topic/deity/subject grid; a modal "Live Teacher/Guru" with a voice picker; paginated generated content;
staged loading copy that narrates the model's work ("Architecting Learning Path…", "Consulting the
dictionary…", "Receiving High-Density Intelligence…"); glassmorphism + gradient shimmer.

That loading-narration pattern is genuinely good UX for 10–40 s generation latency and is worth naming in
the survey as a technique: **make generation legible rather than hiding it behind a spinner.**

### E.2 What is already solved

1. **Real-time multimodal conversational tutoring.** Voice in, voice out, live transcript, barge-in,
   persona, mid-session language switching, tool calls that drive the UI. Six shipped instances.
2. **Curriculum synthesis on demand.** Any topic → a schema-constrained N-chapter path in one call,
   conditioned on grade, location, culture, interests, dialect, and stated goal.
3. **A codified, agent-executable authoring method.** `zero-to-hero-colab` + `concept-mastery-colab` +
   `nbkit.py` + `colab_qc.py`, with 128 notebooks as proof it scales, plus checked-in `<topic>_build/`
   drivers making the corpus regenerable, plus hard-won parallelism rules (independent files → N agents;
   same file → strictly sequential).
4. **Mechanical quality gates on generated teaching content.** Execution validation, schema validation,
   term-grounding (no jargon before its plain-language introduction), caption completeness, label leakage.
   This is the single most under-appreciated asset in the portfolio.
5. **Coverage auditing against an external syllabus** with a demonstrated audit → gap → build → re-audit
   cycle.
6. **Dependency-ordered curriculum with an enforced minimum-repetition rule** (`formulae/SEQUENCE.md`).
7. **A 32-feature typed contract for what an AI tutor should expose** (`ekalavya-ai` `DataProvider`).
8. **An autonomous experiment loop with a machine-enforced hypothesis registry, five layers of
   adversarial audit gates, a fingerprinted objective, and champion archiving** — proven at scale on
   external benchmarks (DSBench 82/112 BEAT, 112/112 forensic PASS; ~14,000 logged experiments).
9. **A solved "memoryless collaborator" problem** — the crash-recovery checkpoint plus append-only
   ledger, with an explicit thesis (*"the repository is the memory"*) and explicit context economics
   (~6 K tokens to resume vs ~600 K for global state).
10. **Streaming/progressive media delivery** — single-ffmpeg HLS with A/V sync solved by construction,
   2 s keyframe-pinned segments, a 15 s client prebuffer for slower-than-realtime producers, and a
   documented negative result (never ship fragmented MP4 as the download).
11. **A complete concept → storyboard → stills → video → narration → exportable MP4 pipeline**
   (`lumiere.ai`), including Veo last-frame conditioning for scene continuity and a canvas +
   `MediaRecorder` export path.
12. **Cross-session memory and affect-conditioned pacing** (`meditationguru`) — built for meditation,
   never applied to teaching.

### E.3 What is missing — the survey's agenda

**1. There is no learner model.** Nothing anywhere estimates what the learner knows. Ekalavya conditions
on `grade` and `location` — static demographics, set once at onboarding. `mark_word_practiced` and
`provide_feedback(score,…)` are emitted by the Live model and then dropped on the floor. Firestore stores
`users/{uid}/curriculums/{id}` — the *artifact*, not the *state*. **Recommendation for the survey: the
minimum viable learner model is (concept → mastery estimate → last-seen timestamp → evidence pointer),
and the Live-API function-call channel is already the right transport for writing it.**
The sharpest form of this gap: `meditationguru` has `guru-memory.ts` injecting *"CONTEXT FROM PREVIOUS
SESSIONS"* into every live session, and `autoresearch` has a formal thesis that *"the repository is the
memory"* for a memoryless agent. **The same author solved cross-session memory twice — for a meditation
app and for an ML agent — and shipped none of it in the tutors.**

**2. There is no assessment loop, and therefore no measurable learning.** 128 notebooks, 0 exercises.
The one instrument with real practice structure (`pca_interview_gauntlet`) is 1/128. The `examprep`
notebook puts every solution immediately below its problem. The `aicourse_syllabus` repo *has* graded
rubrics and reflection prompts for all 197 lectures — in a different repo, unconnected to any artifact.
**The stated success criterion — "a student can narrate every cell in a 1-hour video" — optimises for
fluency, not retention.** No spacing, no interleaving, no retrieval practice, no desirable difficulty,
no delayed testing anywhere in the corpus.

**3. Content is regenerated, never accumulated.** Every session re-prompts. Two learners on the same topic
get different, unversioned, unvalidated lessons — and none of the `class` repo's QC machinery
(`colab_qc.py`, grounding verifier, forensic review) runs on any of it. **The notebooks are rigorously
gated; the live apps are ungated.** This is the sharpest internal inconsistency in the portfolio: the
author knows how to QC generated teaching content and does not do it where content is generated at
runtime for real users.

**4. Reuse is by forking, and it has already broken production.**
   - Byte-identical `<style>` across 5 apps; `--saffron` / mandala / `.diya-glow` shipped on a Spanish
     course.
   - Spanish and Bhagavad Gita both serve `<title>Sanatana Dharma AI Portal</title>`.
   - **Six of seven bundles ship the literal string `apiKey: "MY_GEMINI_API_KEY"`** — Telugu at **6 call
     sites** (lesson generator, Live teacher, TTS, speech, Writing Lab), Ayurveda at 5, the rest at 2
     (Writing Lab and one other). **The Telugu portal's core lesson generation is therefore
     non-functional in production.** Spanish's main generator uses a proper key getter while its Writing
     Lab does not — the fix was applied to the parent and not propagated to the fork.
   - Ekalavya ships a hardcoded `AIzaSy…` Firebase web key (semi-public by design, but it should be
     domain-restricted; worth verifying).
   - `meditationguru` disagrees with itself about which model it uses across README, `CLAUDE.md`, and
     two source files; `face-swap-streamer`'s README and repo description still advertise an "ffmpeg tee
     muxer" that was **removed** from the code with a documented rationale.
   - The same PCM-audio-playback problem is solved three ways in one portfolio: correctly
     (`lumiere.ai addWavHeader`), correctly-with-scheduling (Spanish/Telugu bundles), and **incorrectly**
     (`meditationguru` calls `decodeAudioData` on raw PCM, which throws, with no playback queue).
   **A shared component/package boundary would have prevented all of these.**

**5. BYOK is an adoption wall.** `window.aistudio.openSelectKey()` in six apps, plus the shipped copy
*"To use high-fidelity Vision and Video features, a paid API key is required."* A platform for "the next
billion minds" cannot require the learner to obtain and paste a paid Gemini key. Ekalavya's server proxy
is the correct pattern and should be the template.

**6. The offline/on-device requirement was written and then abandoned.** The Sokrates PRD specifies
Gemini Nano on-device, offline 95%+ of the time, `<50 MB`, `<$0.01`/session, $30–50 Android, village USB
sharing. The deployment is an online-only React SPA whose voice path needs a persistent WebSocket and
whose audio capture uses a deprecated main-thread `ScriptProcessorNode` (in *every* app in the portfolio —
Ekalavya, the language portals, and `meditationguru`; `AudioWorklet` appears nowhere) that will glitch on
exactly those devices. The one genuinely local generative stack in the portfolio (`wan-streamer`) runs at
**~1.8 FPS** on this machine and says so in its own source. **The gap between the specified and the
shipped constraint set is a case study in its own right, and an honest one is more valuable to the survey
than a success story.**

**7. Grounding-quality and safety controls are absent where they matter most.** `googleSearch` grounding
is applied uniformly — to logistic regression *and* to Ayurvedic health guidance delivered in the voice of
Lord Dhanvantari, and to devotional scripture. No source-allowlist, no provenance display, no medical
disclaimer visible in the extracted strings. PsycheForge asserts uncited clinical statistics as fact.
**The `class` repo's "Citation Rigor" discipline exists; it is not applied to the consumer apps.**

**8. No evaluation of the apps themselves.** No A/B tests, no telemetry beyond a token counter, no
learning-outcome measurement, no user studies. The portfolio can say what was built; it cannot say
whether anyone learned anything. Note that a PostHog project exists in this environment — the
instrumentation channel is available and unused.

### E.4 What this portfolio demonstrates for the survey

- **Zero-to-hero is a real, mechanisable pattern.** It has a fixed section arc, a house style, a builder
  kit, a validator, a coverage auditor, a dependency-ordered sequence, and 128 artifacts. The survey can
  advocate it with a worked existence proof and a published skill definition rather than a hypothesis.
- **Agent-parallel content production works, with a specific asymmetry:** independent artifacts scale to
  N concurrent agents; enhancement of a single artifact must be strictly sequential with the orchestrator
  owning the writes. This is a transferable operational finding.
- **The bottleneck in AI-native learning is not generation.** Generation is solved to a startling degree.
  The bottleneck is **state**: knowing what the learner knows, keeping it, and acting on it. Every single
  gap in §E.3 (1, 2, 3, 8) reduces to the absence of a persisted learner model and an assessment signal.
- **Enforcement beats intention.** The single clearest lesson across §B and §D: `class` *states* its
  quality rules ("citation rigor", "no jargon before grounded", "hide code by default") and satisfies
  some of them; `autoresearch` *compiles its rules into regexes, word floors, hash fingerprints, and
  independent audit agents that exit non-zero*, with no `--skip-audit` flag. Where a rule is a norm it
  drifts (rule 12 is unimplemented in every `formulae/` notebook); where a rule is a gate it holds
  (112/112 forensic PASS). **A survey advocating AI-generated curricula must advocate gates, not
  guidelines.**
- **Method beats artifact.** The most reusable things here are not the notebooks or the apps — they are
  `skills/concept-mastery-colab/SKILL.md`, `colab_qc.py`, `AUDIT_TOC_COVERAGE.md`,
  `formulae/SEQUENCE.md`, `ekalavya-ai/src/lib/providers/data-provider.ts`,
  `autoresearchtabular/core/reasoning.py`, and `autoresearch_darebench/framework/forensic_audit.py`.
  Seven files.
- **The closing move is available and unbuilt:** point the autoresearch loop (§D) at the curriculum
  (§B), using an assessment signal the apps (§A) could already emit via Live-API function calls, with
  the multimodal delivery stack (§C) as the presentation layer and the crash-recovery checkpoint format
  (§D.8) as the learner model. Every component exists in this portfolio. None of them are wired
  together. That wiring — objective, ledger, hypothesis registry, embargoed cohort, forensic gates,
  champion promotion — is the survey's contribution.

---

## Source inventory

**Live deployments fetched (9, all HTTP 200, 2026-07-25):** Ekalavya AI · Spanish Learning Portal ·
Telugu Learning Portal · Bhagavad Gita AI · Sanatana Dharma AI · Personalized Ayurveda AI · PsycheForge AI ·
Akka Rural Health Companion · Exo 3.0. Production JS bundles downloaded and analysed for 7 of them
(Akka is inline; Exo is static HTML).

**GitHub repos read via authenticated `gh api`:** `dlmastery/class` (private; full 1,128-file tree +
12 files) · `dlmastery/ekalavya-ai` (full tree + 4 files) · `dlmastery/aicourse_syllabus` ·
`dlmastery/meditationguru` (tree + `src/lib/gemini.ts`, `gemini-enhanced.ts`, `imagen.ts`,
`CosmicScene.tsx`, `next.config.ts`, `firebase.json`, README, `CLAUDE.md`) ·
`dlmastery/face-swap-streamer` (tree + `webapp.py`, `docs/ARCHITECTURE.md`, `web/components/HlsPlayer.tsx`) ·
all seven `autoresearch*` repos (`AUTORESEARCH_PROCESS.md`, `CLAUDE.md`, `README.md`, `core/reasoning.py`,
`core/evaluation/audit.py`, `framework/forensic_audit.py`, `framework/hill_climb.py`,
`experiment_log.jsonl`, `memory/project_autoresearch_checkpoint.md`, ADRs 0002/0004/0005/0006/0015,
`docs/part_1_thesis/01_what_is_autoresearch_engineering.md`, `skills/autoresearch-pack/`) · plus metadata
for `image2video`, `youtube-to-ppt-converter`, `akka-rural-health-companion`,
`organizational-singularity`.

**Local directories inspected:** `/home/eranti/dlmastery/lumiere.ai` (`services/geminiService.ts`,
`App.tsx`, `components/Player.tsx`, `vite.config.ts`, `package.json`, `docs/`) · `/home/eranti/Wan2GP`
(README, `wgp.py` metadata, `Dockerfile`, `entrypoint.sh`, `wan2gp.log`) · `/home/eranti/wan-streamer`
(`run_v2v.sh`, `demo/main.py`, `demo_stream/server.py`, `demo_stream/server.log`, README).

**Key files quoted:** `class/ZERO_TO_HERO_COLABS.md` · `class/CLAUDE.md` ·
`class/AUDIT_TOC_COVERAGE.md` · `class/skills/README.md` · `class/skills/zero-to-hero-colab/SKILL.md` ·
`class/skills/zero-to-hero-colab/reference/colab_arc.md` ·
`class/skills/zero-to-hero-colab/reference/house_style.md` ·
`class/skills/concept-mastery-colab/SKILL.md` · `class/formulae/SEQUENCE.md` ·
`class/formulae/CURRICULUM.md` · `class/vizuara_research/README.md` · `class/deep_learning_app/README.md` ·
`ekalavya-ai/docs/research/00-RESEARCH-DIARY.md` · `ekalavya-ai/docs/research/02-SOKRATES-VISION-PRD.md` ·
`ekalavya-ai/src/lib/providers/data-provider.ts` · `ekalavya-ai/package.json` ·
`aicourse_syllabus/README.md`.

**Notebooks downloaded and programmatically analysed (5):**
`logistic_regression_zero_to_hero.ipynb` (186 cells) · `classification_tabular_sota_2026.ipynb` (110) ·
`statistical_validity_sota_2026.ipynb` (82) · `formulae/pca_interview_gauntlet.ipynb` (105) ·
`exam_prep_solved_problems_zero_to_hero.ipynb` (123).

**Reliability note.** §A and §B are entirely first-hand (bundles downloaded and parsed; notebooks
downloaded and parsed programmatically). §C and §D are first-hand reads of repository source and docs
performed by two parallel sub-investigations; all quoted step names, code blocks, ffmpeg invocations,
model IDs and thresholds are verbatim from those files. Counts marked "as claimed in-repo" (§D.7) are the
repos' own numbers and are internally inconsistent in `autoresearch` (FX) — treat 151/4 as the best
estimate and do not cite a single figure without checking which file it came from.

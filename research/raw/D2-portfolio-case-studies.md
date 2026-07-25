---
title: "Case Studies from an Existing Practitioner Portfolio (dlmastery)"
wave: D
date_researched: 2026-07-25
sources_count: 46
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
the learner is never asked to produce anything. The skill's own success criterion confirms this:
*"a student can narrate every cell in a 1-hour video."* That is a **fluency illusion** target, not a
mastery target. Re-reading and worked examples produce high confidence and poor retention; the corpus
optimises exactly for that.

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

### C.2 `dlmastery/meditationguru`

Repo: public, TypeScript, 389 KB, last pushed 2026-02-10. Description: *"AI-powered meditation & yoga app
with real-time Gemini AI Guru, 3D cosmic visuals, and voice interaction."* Detailed findings pending from
the parallel agent (see §C.5).

### C.3 `dlmastery/face-swap-streamer`

Repo: public, Python, 751 KB, last pushed 2026-06-06. Description: *"Live face-swap web app: upload image
+ video, watch the swap stream to your browser with synchronised audio while it processes. Flask + HLS +
ffmpeg tee muxer + InsightFace."* Detailed findings pending (§C.5).

The architecturally interesting claim is **"watch … while it processes"** — a progressive/live HLS stream
emitted by an ffmpeg `tee` muxer as frames are produced, rather than a batch render followed by playback.
That is exactly the primitive a *generated-video lesson* needs: the learner starts watching segment 1
while segment 8 is still being rendered. Related local work: `/home/eranti/Wan2GP`, `/home/eranti/wan-streamer`,
and `dlmastery/image2video` (*"Local web app for Sulphur-2 / LTX-2.3 text-to-video, image-to-video, and
video extension on Windows + RTX 4090"*, 3.4 MB).

### C.4 `lumiere.ai` (Gemini + Veo)

Repo `dlmastery/lumiere.ai` (public, TypeScript, 88 KB): *"AI-powered video creation platform with Google
Gemini & Veo."* Local checkout at `/home/eranti/dlmastery/lumiere.ai`. Detailed findings pending (§C.5).

Related: `dlmastery/youtube-to-ppt-converter` (*"AI-powered slide extraction from YouTube presentation
videos using Gemini and ffmpeg"*) — the inverse pipeline, video → slides, which is a plausible
lesson-ingestion path.

### C.5 Status

A dedicated sub-investigation of `meditationguru`, `face-swap-streamer`, `lumiere.ai`, `Wan2GP` and
`wan-streamer` was dispatched in parallel with this write-up and had not returned at the time of
writing. §C.2–C.4 record only what is verifiable from repo metadata and from the §C.1 bundle evidence.
**Do not cite §C.2–C.4 for implementation detail without re-running that dive.**

---

## D. The autoresearch family — candidate method for autonomous curriculum improvement

*(Investigated by a parallel agent; see §D.4 for status.)*

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

### D.2 What the loop is, from the descriptions

The recurring shape across all seven, as stated in the repo metadata:

1. A **fixed benchmark/target** with a single scalar objective (test Sharpe, composite Sharpe, OOD AUC,
   DSBench task score).
2. A **backbone sweep** — the same protocol re-run across N architectures (14 backbones × 25 experiments;
   5 backbones × 216 experiments) so the *method* is compared, not just one model.
3. **Hill-climbing on train/val only** — the test set is quarantined. `autoresearch_dsbench` states this
   explicitly and reports 82/112 tasks beating the published DSBench baselines.
4. **Audit gates as a first-class stage.** Named gates: **"Citation Rigor"**, **"Reasoning Blob"**
   (`autoresearchtabular`), a **10-agent forensic committee** (`dsbench`), an **11-agent forensic
   committee including "Agent K, forbidden-path enforcer"** (`darebench`). `dsbench` reports
   **112/112 forensic PASS** — i.e. the audit is run on every task and reported as a headline metric
   alongside performance.
5. **A named champion** promoted at the end ("Residual MLP champion test Sharpe +6.21", "mamba dmamba
   global champion +1.32 composite Sharpe").
6. **A skill pack extracted from the run** — `dsbench` yields a "44-skill industry-shareable pack",
   closing the loop back into reusable method.

### D.3 Why this matters for curriculum

Map the loop onto teaching and it becomes an **autonomous curriculum-improvement protocol**:

| Autoresearch element | Curriculum analogue |
|---|---|
| Objective (Sharpe / AUC) | Learning gain: post-test − pre-test, retention at 7/30 days |
| Backbone sweep | Explanation-strategy sweep: analogy-first vs formal-first vs worked-example vs Socratic |
| Hill-climb on train/val, quarantine test | Tune on a pilot cohort; hold out a validation cohort so you don't overfit the curriculum to the learners who wrote it |
| Citation Rigor gate | Every SOTA claim in a notebook must resolve to a real 2024–26 source (already a stated requirement of the `zero-to-hero-colab` skill) |
| Reasoning Blob gate | Every derivation step must carry its `(reason)` annotation (already non-negotiable #9) |
| Forensic committee / Agent K forbidden-path enforcer | The `colab_qc.py` grounding + caption + leaked-label checks, promoted to a multi-agent adversarial review |
| Named champion | The promoted version of a lesson |
| Skill pack extraction | `skills/zero-to-hero-colab` and `concept-mastery-colab` themselves |

**The author has already built both halves and has not connected them.** `class` has the QC harness
(`colab_qc.py`, `verify_grounding.py`) and the coverage auditor (`AUDIT_TOC_COVERAGE.md`) but no
objective function and no experiment ledger. `autoresearch*` has the ledger, the sweep, the gates, and
the champion-selection machinery but is pointed at Sharpe ratios. **Joining them is the concrete, novel
contribution the survey can propose**, and the missing piece is the only genuinely hard one: a learning-gain
signal, which requires assessment, which is exactly what §B.4 shows does not exist.

### D.4 Status

A dedicated sub-investigation of the loop's step names, ledger format, and gating implementation was
dispatched in parallel and had not returned at the time of writing. §D.2 records only what is verifiable
from repo descriptions. **The "7-step Karpathy-style research loop" step names are not yet verified
first-hand — re-run that dive before quoting them.**

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
8. **An autonomous experiment loop with adversarial audit gates and champion selection**, proven at scale
   on external benchmarks (DSBench 82/112, 112/112 forensic PASS).
9. **Streaming/progressive media delivery** (HLS + ffmpeg tee) and local generative video, as reusable
   primitives for generated lesson media.

### E.3 What is missing — the survey's agenda

**1. There is no learner model.** Nothing anywhere estimates what the learner knows. Ekalavya conditions
on `grade` and `location` — static demographics, set once at onboarding. `mark_word_practiced` and
`provide_feedback(score,…)` are emitted by the Live model and then dropped on the floor. Firestore stores
`users/{uid}/curriculums/{id}` — the *artifact*, not the *state*. **Recommendation for the survey: the
minimum viable learner model is (concept → mastery estimate → last-seen timestamp → evidence pointer),
and the Live-API function-call channel is already the right transport for writing it.**

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
   **A shared component/package boundary would have prevented all four.**

**5. BYOK is an adoption wall.** `window.aistudio.openSelectKey()` in six apps, plus the shipped copy
*"To use high-fidelity Vision and Video features, a paid API key is required."* A platform for "the next
billion minds" cannot require the learner to obtain and paste a paid Gemini key. Ekalavya's server proxy
is the correct pattern and should be the template.

**6. The offline/on-device requirement was written and then abandoned.** The Sokrates PRD specifies
Gemini Nano on-device, offline 95%+ of the time, `<50 MB`, `<$0.01`/session, $30–50 Android, village USB
sharing. The deployment is an online-only React SPA whose voice path needs a persistent WebSocket and
whose audio capture uses a deprecated main-thread `ScriptProcessorNode` that will glitch on exactly those
devices. **The gap between the specified and the shipped constraint set is a case study in its own right,
and an honest one is more valuable to the survey than a success story.**

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
- **Method beats artifact.** The most reusable things here are not the notebooks or the apps — they are
  `skills/concept-mastery-colab/SKILL.md`, `colab_qc.py`, `AUDIT_TOC_COVERAGE.md`,
  `formulae/SEQUENCE.md`, and `ekalavya-ai/src/lib/providers/data-provider.ts`. Five files.
- **The closing move is available and unbuilt:** point the autoresearch loop (§D) at the curriculum
  (§B) using an assessment signal the apps (§A) could already emit via Live-API function calls. Every
  component exists in this portfolio. None of them are wired together.

---

## Source inventory

**Live deployments fetched (9, all HTTP 200, 2026-07-25):** Ekalavya AI · Spanish Learning Portal ·
Telugu Learning Portal · Bhagavad Gita AI · Sanatana Dharma AI · Personalized Ayurveda AI · PsycheForge AI ·
Akka Rural Health Companion · Exo 3.0. Production JS bundles downloaded and analysed for 7 of them
(Akka is inline; Exo is static HTML).

**GitHub repos read via authenticated `gh api`:** `dlmastery/class` (private; full tree + 12 files) ·
`dlmastery/ekalavya-ai` (full tree + 4 files) · `dlmastery/aicourse_syllabus` · plus metadata for
`meditationguru`, `face-swap-streamer`, `lumiere.ai`, `image2video`, `youtube-to-ppt-converter`,
`akka-rural-health-companion`, `organizational-singularity`, and the seven `autoresearch*` repos.

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

---
title: "AI-Native Textbook and Course-Generation Platforms"
wave: A
section: A1
date_researched: 2026-07-27
sources_count: 61
status: raw
---

# A1 — AI-Native Textbook and Course-Generation Platforms

**Research constraint note:** WebSearch budget was exhausted for this session. Findings below come from
`WebFetch` on known URLs, raw `curl` against site HTML and JS bundles, the arXiv Atom API (rate-limited
mid-session; see §7.5) and the arXiv HTML search interface as fallback, and the authenticated GitHub API.
**OpenAlex was unavailable** — the account daily budget was exhausted (`{"error": "Rate limit exceeded",
"message": "Insufficient budget. This request costs $0.001 but you only have $0.0007 remaining"}`), the same
failure A2 recorded. **Semantic Scholar returned HTTP 429** on every attempt. Where a primary abstract could not
be retrieved, this is stated and the claim is downgraded.

**Evidence-strength key:**
- **[A]** Primary source retrieved and quoted this session; peer-reviewed empirical work.
- **[B]** Primary source retrieved and quoted this session, but preprint / self-evaluated / non-peer-reviewed.
- **[C]** Bibliographic record verified but abstract or numbers not retrievable this session.
- **[V]** **VENDOR** claim. Marketing copy, self-measured, not independently verified.
- **[O]** Observational fact about an artifact (site HTML, JS bundle, robots.txt, GitHub API) — verifiable,
  reproducible, but not evidence about learning.
- **[X]** Original measurement performed *this session* (the corpus audit in §6).

---

## 0. The one-sentence finding

Every system in this section generates **exposition** well and **practice** badly, and the strongest available
number says so precisely: when Sarsa et al. had Codex generate 240 programming exercises *with sample solutions
and test cases*, **only 30.9% had a sample solution that actually passed the exercise's own generated tests**
(arXiv:2206.11861, ICER 2022) — **[A]**. The prose was fine. The answer key was wrong two times out of three.
Section 6 shows the same asymmetry in the corpus these systems are trained on and imitate.

---

## 1. paradigm.study

### 1.1 What it is

- URL: <https://www.paradigm.study/> (canonical; `paradigm.study` 301s to `www`). HTTP 200, 205 KB Next.js app.
- Tagline, verbatim: **"A School of One."** — **[O]**
- Positioning, verbatim: *"Paradigm is a learning platform where anyone can build courses that adapt to what you
  know, what you're curious about, and how you learn."* — **[O]**
- Footer: **"© 2026 Paradigm, San Jose, CA"**. CEO named on the site as **Scott Fan**. — **[O]**
- Socials: [x.com/ParadigmStudy](https://x.com/ParadigmStudy),
  [linkedin.com/company/paradigmstudy](https://www.linkedin.com/company/paradigmstudy),
  [instagram.com/paradigm.study](https://instagram.com/paradigm.study), TikTok. Localised to `es` and `zh-Hans`. — **[O]**

### 1.2 What it generates — concretely

Input side, verbatim from the landing page: **"Bring what you've got — we break it down."** Three named intake
modes — **Upload files** (*"Slides, PDFs, a photo — we'll make sense of it"*), **Share a link**, **Drop your
text**. — **[O]**

Output side is a **course object with an explicit hierarchy**, and the sample cards state the shape exactly:

| Sample course | Author shown | Structure claimed |
|---|---|---|
| "Build your first app, hands-on" | Scott Fan · CEO of Paradigm | **5 units · 15 lessons** |
| "Produce your first track" | Theo Marsh · producer | **5 units · 14 lessons** |
| "Speed-run ICS 31" (UCI intro programming) | "Peter the Anteater · UCI" | **6 units · 18 lessons** |
| "Let's count to 10!" | Ms. Rosa · pre-K teacher | **10 lessons · ages 3–5** |

— **[O]**. Note the unit sizes: **~3 lessons per unit**, consistently. That is the module→lesson granularity
this survey cares about.

The "Build your first app" card describes real infrastructure, not just text: *"We spin up your own cloud
machine — terminal, Claude Code, the works — and walk you through it keystroke by keystroke."* — **[V]**

### 1.3 The UI — what it actually does

- **Node-graph course map.** The page ships accessibility strings for an editable graph: *"Press enter or space
  to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and
  escape to cancel."* and the same for **edges**. Instruction line: *"Drag the cards · scroll to pan · click to
  open."* This is a **drag-and-drop DAG editor over lessons** — i.e. the prerequisite graph is a first-class,
  user-editable object. — **[O]**
- **KaTeX is loaded** from `cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css` — math rendering is a
  first-class concern. — **[O]**
- **"Clover"**, a named agent, is the second pillar. Its role is explicitly **administrative, not instructional**:
  *"Deadlines. Check-ins. Reports. I keep the small stuff handled, so you're free to look further ahead."*
  Simulated Clover messages include *"Your calculus set is due Thursday"*, *"You've studied 5 days straight"*,
  *"Quiz tomorrow — want a 10-minute refresher tonight?"*, and — notably — *"I noticed you can bring a cheat
  sheet. Want me to build one around the topics you're weakest on?"* — **[O]**
- Clover also **generates courses from events**: *"I hope you had fun at the event! I organized the live notes
  and built you a vibe-coding course following their strategy."* → card labelled *"Vibe coding · Build-along
  path"*. — **[O]**

### 1.4 The hidden object model (the most informative artifact on the site)

`https://www.paradigm.study/robots.txt` disallows the authenticated surfaces, and in doing so **enumerates the
product's internal nouns** — **[O]**:

```
Disallow: /practice/     Disallow: /lesson/      Disallow: /notebook/
Disallow: /exam/         Disallow: /study/       Disallow: /learn/
Disallow: /courses/      Disallow: /my-course/   Disallow: /onboarding/
```

This matters for §5 and §6. Paradigm has **`/practice/` and `/exam/` as distinct routes from `/lesson/`** — the
product model does *not* collapse into exposition-only. It also has **`/notebook/`**, which suggests an
executable-notebook surface. Sitemap (`/sitemap.xml`) exposes only `/`, `/camp`, `/ai-archetype`, `/signup`;
everything pedagogical is behind auth, so **the generated artifacts themselves could not be inspected this
session** — this is a real gap in the evidence, see §7.1.

### 1.5 Pedagogical model — and the problem with it

The site's only theoretical claim is a Polanyi epigraph: **"We know more than we can tell." — Michael Polanyi**,
glossed as *"Paradigm captures the part of mastery no one can put into words, and brings it to you."* — **[O]**

This is rhetorically elegant and **substantively backwards**. Polanyi's tacit-knowledge thesis is that expert
knowledge *resists* propositional encoding; the standard pedagogical consequence is that it transfers through
apprenticeship, modelling and coached practice, not through better prose. A system whose primary act is
converting artifacts into lesson text is doing the opposite of what the epigraph implies. There is **no learning
theory, no efficacy claim, no research citation, and no study link anywhere on the site** — **[O]**, and this is
the single most important negative observation about the category (§7.2).

### 1.6 Pricing and social proof

- **"$500/mo"** headline, with a genuinely unusual mechanic: **"You decide the tuition — if you can make the
  case."** / *"Win Clover over — every good reason brings the tuition down."* — i.e. **the price is negotiated
  with the LLM agent.** — **[O]**
- **"Trusted by teams at: OpenClaw, NVIDIA, Hugging Face, Red Hat"** — **[V]**, unverified, and "teams at" is
  doing heavy lifting (typically means individual seats, not enterprise contracts).

### 1.7 The tell: their growth strategy recruits *human* authors

`/camp` — **"The YC Reject Camp"**, SF, July 24–27 2026 — is a free 4-day residency for **"4 marketers × 4
engineers"**. The ask, verbatim: *"A marketer and an engineer pair up, teach each other their craft, and publish
a course on Paradigm, then compete for which course gets the most traction."* Free housing, meals, travel
reimbursement, film crew. — **[O]**

**No mention of AI generation appears anywhere on `/camp`.** A platform whose landing page says content is
generated from your uploads is spending real money to acquire **human-authored courses with named human
authors** — the same pattern as the sample-course cards, each of which is attributed to a person (Scott Fan,
Theo Marsh, "Ms. Rosa"), not to a model. The generation engine is the *distribution* story; **authorship is
still human.** This is the single most useful observation in §1 and it recurs across every vendor in §3.

(`/ai-archetype` is a marketing quiz — *"what kind of tech bro are you?"* — with no pedagogical content. — **[O]**)

---

## 2. vizuara.ai

### 2.1 What it is

`https://vizuara.ai/` is a **1,407-byte React SPA shell**; `<title>Vizuara AI Labs</title>`. **WebFetch returned
HTTP 403** on the root, so the analysis below is from the JS bundle
(`/assets/index-CMDukm9D.js`, 1,473,533 bytes, HTTP 200) — **[O]**. The shell loads **Razorpay**
(`checkout.razorpay.com/v1/checkout.js`) → India-first payments — **[O]**.

Identity, from the YouTube channel description ([youtube.com/@vizuara](https://www.youtube.com/@vizuara), verbatim):

> *"We are team Vizuara, a fast-growing AI startup. www.vizuara.ai. **Vizuara is founded by alumni from IIT
> Madras, MIT, and Purdue University.** For questions, please email hello@vizuara.com"* — **[O]**

Channel metrics, from the YouTube page payload: **216K subscribers, 61,338,032 total views, joined Nov 23, 2021**
— **[O]**. Substack ([vizuara.substack.com](https://vizuara.substack.com/)): **"Over 5,000 subscribers"**;
its `/about` page contains only *"My personal Substack"* — no founder bios — **[O]**.

### 2.2 It is a course business, not a generation engine

Public route table extracted from the bundle — **[O]**:

```
/courses  /free-courses  /my-courses  /quizzes  /submissions  /mentorship
/instructor  /teacher  /dashboard  /cart  /invoices  /my-subscriptions  /zoom-meeting
```

Admin route table (partial, ~70 routes) reveals the operational reality — **[O]**:

```
/admin/create-course  /admin/edit-lesson/:lessonId  /admin/arrange-courses
/admin/create-cohort  /admin/research-bootcamps  /admin/mentorship
/admin/bulk-enrollments  /admin/certificate-requests  /admin/manage-assignment-authors
/admin/ai-features  /admin/analytics/vizz-ai  /admin/voice-agent  /admin/karma /admin/karmarules
```

Read that list carefully. `create-course`, `edit-lesson`, `arrange-courses`, **`manage-assignment-authors`** —
these are **human-authoring and human-curriculum-ordering tools**. Internal service names in the bundle
(`CourseService`, `CohortService`, `BundleService`, and a `CohortService - Cohort created with full curriculum`
log line) confirm a conventional LMS data model — **[O]**. Firestore collection constants include
`COURSE_END_TEST`, `COURSE_FREE_SUMMARIES`, `ASSIGNMENT_SUBMISSIONS`, `COLAB_NOTEBOOK`,
`COURSE_ZOOM_REGISTRANTS`, `CONFERENCE_DEADLINES` — **[O]**.

**Vizuara is a human-taught cohort-based course company with AI *features* bolted on**, not an AI-native
textbook generator. The AI surfaces are narrow and named: **"AI Course Assistant"**, **"Vizz AI"** (has its own
analytics dashboard), **"LLMWikiChatPage"**, and a **"voice-agent"** admin panel — **[O]**.

### 2.3 Named products

From bundle strings and video/playlist titles — **[O]**, with vendor-claimed scale flagged **[V]**:

- **"Build DeepSeek from Scratch"** / **"Build a DeepSeek Model (From Scratch)"**
- **"AI Agents Bootcamp"**, **"3-in-1 AI Bootcamp"**, **"10-Course AI & ML Bundle"**
- **"Computer Vision Research Bootcamp"** (*"Build strong foundations, work on impactful problems in CV"*)
- **"AI Highschool Researcher Bootcamp"**; **"AI Researcher Bootcamp"**
- **"Autonomous driving bootcamp"**; **"Context Engineering Workshop"**
- **"Advanced Generative AI for professionals"**; *"Deep dive into Scientific Machine Learning"*
- YouTube playlists: *"Building Neural Networks from Scratch"*, *"Transformers Explained"*, *"Machine Learning:
  Teach by Doing"*, *"Data Structures and Algorithms in Python"*, *"ML project based course: Learn Explainable
  AI (XAI) and publish research paper"*
- Site copy: **"20K+ Students"** — **[V]**; **"Claude Partner Network"** badge — **[V]**, unverified.

Two more observations. The bundle contains a bare string **`"Attention Is All You Need,"`** alongside
`"Build DeepSeek from Scratch,"` — these read as items in a **paper-reproduction curriculum**: the pedagogy is
*"rebuild the primary source."* And note **`/quizzes`** and `COURSE_END_TEST` exist as real routes — Vizuara
does ship assessment, but it is **human-authored** (hence `manage-assignment-authors`). — **[O]**

**Negative result:** despite the brief's framing ("their books"), **no evidence of a published Vizuara *book*
was found this session.** No ISBN, no publisher, no book landing route. The "from scratch" products are
**courses**, and the phrase collides with Sebastian Raschka's *Build a Large Language Model (From Scratch)*
(Manning), a separate human-authored work whose repo appears in §6. Anyone citing "Vizuara's books" should
verify first — **[O]**.

---

## 3. Adjacent players: generated vs. human-authored, and efficacy

The column that matters is the third one. **In every single case where the split is disclosed, the human keeps
the pedagogy and the machine gets the prose or the conversation.**

| Product | Generated by AI | Human-authored | Efficacy |
|---|---|---|---|
| **Khanmigo** ([khanmigo.ai/learners](https://www.khanmigo.ai/learners)) | The *tutoring turn* — Socratic dialogue, code review (JS/HTML/Python/SQL), writing coaching. Teacher-side: lesson plans, rubrics, exit tickets. | **The entire content library.** Khanmigo tutors *over* existing Khan exercises/videos; it does not author the course. | **No quantified data on page.** Only an unlinked Common Sense Media "4-star rating" + one testimonial. — **[V]** |
| **Coursera Coach** | — | — | **UNREACHABLE.** `coursera.org/coach` → 404; `coursera.org/about/coach` → 404; `blog.coursera.org/introducing-coursera-coach/` → 404; `coursera.org/gen-ai` → 404. **No claim made.** See §7.5. |
| **Duolingo Max** ([blog.duolingo.com/duolingo-max](https://blog.duolingo.com/duolingo-max/)) | Lily's real-time Video Call responses; follow-up turns in Roleplay; post-hoc feedback. | Verbatim: ***"Humans write the scenarios that learners see in Roleplay."*** Experts write opening messages, steer conversation direction, and review AI output for factual accuracy and tone. | **None.** Only *"impressed by the results."* — **[V]** |
| **Synthesis Tutor** ([synthesis.com/tutor](https://www.synthesis.com/tutor)) | Unspecified. K-5 math, ages 5–11. | Verbatim: ***"Synthesis Tutor leverages AI where appropriate while relying on our team of expert educators and neuroscientists to handle much of the pedagogy and interactive experiences."*** Also: *"it is not Chat-GPT"*, they don't *"simply outsource your child's education teaching to an LLM."* | **None.** Testimonials + *"35,000+ families"*. — **[V]** |
| **MagicSchool** ([magicschool.ai](https://www.magicschool.ai/)) | **80+ teacher tools, 50+ student tools**: Lesson Plan Generator, Multiple Choice Quiz, Rubric Generator, IEP Generator, Text Rewriter, Report Card Comments, AI Tutor. | Teacher is the author-of-record; the page **does not state** whether output is human-reviewed before students see it. | *"28% improvement in students meeting literacy grade-level expectations"*, *"7–10 hours saved per week"*, *"88% of teachers say it helps them reach every learner"* — **[V]**, **no study links, no methodology, no sample size.** |
| **Curipod** ([curipod.com](https://curipod.com/)) | Interactive lesson slides, polls, drawings, writing prompts + feedback. | **"100% teacher controlled"**, *"teacher led lessons."* | *"Students in Curipod classrooms improved by up to **23 percentage points** on state reading and writing assessments, with the furthest-behind students making the largest gains"*, sourced to *"official state test data from the California Department of Education."* *"Trusted in over 14,000 districts."* — **[V]** but **the strongest-sourced vendor claim in the table** (external test data); still self-selected case studies, "up to", no control group, no n. |
| **Diffit** ([web.diffit.me](https://web.diffit.me/)) | Adapted passages at target reading levels, summaries, key vocabulary (+translations), **multiple-choice, short-answer and open-response questions**, DOK-tuned. | 3-step workflow explicitly puts the teacher in the middle: input → **refine/tune/select** → export to Google/Microsoft/PDF, *"editable for easy mix and match."* | Survey of **2,517 teachers, Nov 2024**: *"96% saves me time"*, *"93% reaches students where they are"*, *"86% makes me a better teacher"* — **[V]**. **Note what is absent: not one accuracy metric, and not one claim about student learning.** |
| **Brisk Teaching** ([briskteaching.com](https://www.briskteaching.com/)) | 30+ tools: Presentation Maker, **Quiz Generator (with answer keys, into Google Forms)**, Lesson Plan, Newsletter, Podcast Generator, Batch Feedback. "Brisk Boost" is student-facing. | Teacher-facing by default; "Inspect Writing" analyses student writing *process* (revision history). | **None.** *"2 million teachers"*, *"20,000 school districts"* — adoption, not efficacy. — **[V]** |
| **SchoolAI** ([schoolai.com](https://schoolai.com/)) | "Dot" tutor turns; "PowerUps" (focused AI apps); personalisation within teacher-set bounds. | **"Every Space starts with a teacher"**; *"every safeguard, content boundary, and AI behavior is configurable by educators."* | **The best in the table.** **ESSA Level III**, two-year independent review by **Instructure**: *"28% boost in student critical thinking"*, *"2x students engaging in higher-order reasoning"*, from **13,882 student-AI conversations, 82 teachers, Jordan School District, Utah**. Plus a **Stanford SCALE** content analysis of **150,000+ teacher prompts** and 23,000+ Spaces. — **[V→B]**: sample sizes and a named external reviewer are disclosed, but ESSA Level III is the *correlational* tier (no causal design), so this is **not** an RCT. |
| **Ello** ([ello.com](https://www.ello.com/)) | The tutoring interaction — *"listens in real time and decides exactly what your child needs, right when they need it."* Kids also co-author stories. | *"exclusive library based on the **Science of Reading**"* — **thousands of professionally-authored books.** | *"88% of children read more after 4 weeks of Ello"* — **[V]**, internal, no RCT, no effect size, and note it measures **volume read**, not reading skill. |

**Three patterns worth putting in the survey:**

1. **The Stanford SCALE number in the SchoolAI row is the most revealing statistic in this whole table:**
   *"50%+ of prompts create lessons, assessments & feedback"* and *"~40% of messages focus on curriculum &
   standards."* Teachers are using these tools overwhelmingly as **content factories**, which is exactly the
   surface where §5's failure modes bite.
2. **Efficacy reporting is inverted.** The products that generate the *most* content (MagicSchool, Brisk,
   Diffit) report the *least* learning evidence — Diffit's three headline numbers are all teacher-*sentiment*.
   The products that generate the *least* (SchoolAI, Curipod, both of which keep the teacher as author) have the
   only externally-sourced outcome data. Generation volume is inversely correlated with evidence.
3. **Nobody claims their AI authors the curriculum.** Duolingo says humans write the scenarios. Synthesis says
   humans handle the pedagogy. Khan tutors over a human library. Ello licenses a human library. SchoolAI starts
   every Space with a teacher. Curipod is "100% teacher controlled." **The AI-native textbook does not exist in
   the commercial market yet** — what exists is AI-native *delivery* over human-authored *structure*.

---

## 4. Automatic course generation as research

### 4.1 Textbook / long-form course generation

- **arXiv:2503.17710** — *Slide2Text: Leveraging LLMs for Personalized Textbook Generation from PowerPoint
  Presentations* (2025-03-22). The closest thing to a literal "automatic textbook generation" paper: extracts
  slide content and expands it into a customised textbook. — **[B]**. Same input→exposition transform as
  Paradigm's "upload your slides."
- **arXiv:2510.26854v3** — *Inverse Knowledge Search over Verifiable Reasoning: Synthesizing a Scientific
  Encyclopedia from a Long Chains-of-Thought Knowledge Base* (2025-10-30). **The largest generated-corpus result
  found**: "SciencePedia", **~200,000 fine-grained entries** across maths, physics, chemistry, biology,
  engineering, computation, derived from **~3 million first-principles questions**. Framing quote:
  *"Most scientific materials compress reasoning, presenting conclusions while omitting the derivational chains
  that justify them."* Verification is by **cross-model answer consensus** — *"multiple independent solver models
  generate LCoTs, which are then rigorously filtered by prompt sanitization and cross-model answer consensus,
  retaining only those with verifiable endpoints."* Reports *"significantly lower factual error rates"* than a
  no-retrieval baseline **as judged by an external LLM**. — **[B]**. **Two caveats the survey should state:**
  the evaluation is LLM-as-judge (not human, not student), and the artifact is an *encyclopedia* — reference
  material, not a course. It has no ordering, no difficulty ramp, and no exercises.
- **arXiv:2607.13041** — *LessonBench-V1: A Benchmark Dataset for Evaluating AI Lesson Generation Agents*
  (2026-06-12), Silva, Lotfi, Ihianle, Shahtahmassebi, Bird. **647 human-written lessons** paired with
  LLM reverse-engineered plans, **240 STEM topics**, **3,620 learning objectives**, 97 open sources; evaluation
  grounded in **Bloom, Gagné's Events, Merrill's First Principles, and the 5E model**. Opening claim, verbatim:
  *"LLM based AI educational content generation systems are increasingly being developed, yet **no standardised
  benchmark exists** to systematically evaluate them."* — **[B]**. Headline failure numbers were **not
  retrievable from the abstract page** this session → **[C]** for any claim about where it says generation fails.
- **arXiv:2504.05370** — *EduPlanner: LLM-Based Multi-Agent Systems for Customized and Intelligent Instructional
  Design* (2025-04-07). Adversarial multi-agent (evaluator/optimiser) instructional design. — **[B]**
- **arXiv:2408.01102** — *LessonPlanner: Assisting Novice Teachers to Prepare Pedagogy-Driven Lesson Plans with
  Large Language Models* (2024-08-02). Explicitly **Gagné-scaffolded**; a *human-in-the-loop authoring aid*, not
  an autonomous generator. — **[B]**
- **arXiv:2503.09276** — *Fine-Tuning Large Language Models for Educational Support: Leveraging Gagne's Nine
  Events of Instruction for Lesson Planning* (2025-03-12). — **[B]**
- **arXiv:2510.19866** — *An Evaluation of the Pedagogical Soundness and Usability of AI-Generated Lesson Plans
  Across Different Models and Prompt Frameworks in High-School Physics* (2025-10-22). Five models (GPT-5,
  Claude Sonnet 4.5, Gemini 2.5 Flash, DeepSeek V3.2, Grok 4) × three prompt frameworks incl. TAG. — **[B]**
- **arXiv:2510.03369** — *TriQuest: An AI Copilot-Powered Platform for Interdisciplinary Curriculum Design*
  (2025-10-03). Motivating claim: *"Existing tools often lack the required pedagogical and domain-specific
  depth."* — **[B]**
- **arXiv:2405.05938** — *DOLOMITES: Domain-Specific Long-Form Methodical Tasks* (2024-05-09). Positions
  "teacher writing a lesson plan" as an instance of **long-form structured generation** — the right abstraction
  for full-course generation. — **[B]**
- **arXiv:2412.04185** — *Leveraging Large Language Models to Generate Course-specific Semantically Annotated
  Learning Objects* (2024-12) — RAG-situated question generation inside a specific course. — **[C]**
- **arXiv:2504.08856** — *Examining GPT's Capability to Generate and Map Course Concepts and Their Relationship*
  (2025-04) — concept extraction + relation mapping from course materials. — **[C]**
- **arXiv:2504.18603** — *Toward Personalizing Quantum Computing Education: An Evolutionary LLM-Powered
  Approach* (2025-04-24) — knowledge-graph-augmented teaching assistant. — **[B]**

### 4.2 Learning-path / curriculum sequencing

This is a mature pre-LLM literature that the generation wave has largely **ignored**, which is itself a finding.

- **arXiv:1905.12470** — *Exploiting Cognitive Structure for Adaptive Learning* (2019) — **[B]**
- **arXiv:2005.03818** — *Choose Your Own Question: Encouraging Self-Personalization in Learning Path
  Construction* (2020) — **[B]**
- **arXiv:2305.04475** — *Adaptive Learning Path Navigation Based on Knowledge Tracing and Reinforcement
  Learning* (ALPN; AKT + RL) (2023) — **[B]**
- **arXiv:2305.06398** — *Towards Scalable Adaptive Learning with Graph Neural Networks and RL* (2023) — **[B]**
- **arXiv:2306.04234** — *Set-to-Sequence Ranking-based Concept-aware Learning Path Recommendation* (2023) — **[B]**
- **arXiv:2406.10245** — *On conceptualisation and an overview of learning path recommender systems in
  e-learning* (2024) — survey — **[B]**
- **arXiv:2406.17518** — *Enhancing Explainability of Knowledge Learning Paths: Causal Knowledge Networks*
  (2024). Opens with the load-bearing premise: *"A reliable knowledge structure is a **prerequisite** for
  building effective adaptive learning systems."* — **[B]**
- **arXiv:2507.05295** — *Enhancing Learning Path Recommendation via Multi-task Learning* (2025) — **[B]**
- **arXiv:2506.22303** — *GraphRAG-Induced Dual Knowledge Structure Graphs for Personalized Learning Path
  Recommendation* (2025). Critique of the field, verbatim: *"most existing methods primarily rely on
  prerequisite relationships, which present..."* limitations. — **[B]**
- **arXiv:2604.14613** — *Uncertainty-aware Generative Learning Path Recommendation with Cognition-Adaptive
  Diffusion* (U-GLAD, 2026-04). Handles *"lucky guesses or accidental slips."* — **[B]**
- **arXiv:2605.16750** — *UniER: A Unified Benchmark for Item-level and Path-level Exercise Recommendation*
  (2026-05) — **[B]**
- **arXiv:2401.08517** — *Supporting Student Decisions on Learning Recommendations: An LLM-Based Chatbot with
  Knowledge Graph Contextualization* (2024) — **[B]**
- **arXiv:2511.21037** — *LOOM: Personalized Learning Informed by Daily LLM Conversations Toward Long-Term
  Mastery via a Dynamic Learner Memory Graph* (2025-11-26). Its framing is the sharpest critique of the
  category: *"many systems still assume **fixed curricula** or coarse progress signals… At the other extreme,
  lightweight incidental systems offer flexible, in-the-moment content but **rarely guide learners toward
  mastery**."* — **[B]**. **That sentence names the exact gap Paradigm sits in.**

**Structural observation — [O]:** §4.1 (generation) and §4.2 (sequencing) barely cite each other. The generation
papers produce *unordered exposition*; the sequencing papers assume *a pre-existing, human-curated item bank
with known prerequisites and calibrated difficulty*. **Nobody has closed the loop**, because closing it requires
generated items to arrive with valid difficulty parameters and valid answer keys — and §5 shows they do not.

### 4.3 Question/exercise generation

- **arXiv:2206.11861** — Sarsa, Denny, Hellas, Leinonen, *Automatic Generation of Programming Exercises and Code
  Explanations using Large Language Models*, **ICER 2022** — **[A]**. See §5.4; this is the load-bearing paper.
- **arXiv:2408.10947** — *Dr.Academy: A Benchmark for Evaluating Questioning Capability in Education for LLMs*,
  **ACL 2024** (Chen, Wu, Yan, Liu, Zhou, Xiao). Reframes evaluation *"from LLMs as learners to LLMs as
  educators"*; four metrics — relevance, coverage, representativeness, consistency — over Anderson & Krathwohl.
  Finding: *"GPT-4 demonstrates significant potential in teaching general, humanities, and science courses;
  Claude2 appears more apt as an interdisciplinary teacher."* — **[A]**
- **arXiv:2402.01512** — *Distractor Generation in Multiple-Choice Tasks: A Survey of Methods, Datasets, and
  Evaluation* (2024) — the field survey — **[B]**
- **arXiv:2307.16338** — *Distractor generation for MCQs with predictive prompting and LLMs* (Bitew, Deleu,
  Develder, Demeester, 2023). **Teacher review: "on average 53% of the generated distractors presented to the
  teachers were rated as high-quality"** → **~47% rejected by experts.** — **[A]**
- **arXiv:2406.19356** — *DiVERT: Distractor Generation with Variational Errors Represented as Text for Math
  MCQs* (2024) — *"automated distractor generation, even with the help of LLMs, remains **challenging** for
  subjects like math."* — **[B]**
- **arXiv:2405.05144** — *Improving Automated Distractor Generation for Math MCQs with Overgenerate-and-rank*
  (2024) — **[B]**. The name is the admission: you must overgenerate and filter.
- **arXiv:2308.03234** — *Automated Distractor and Feedback Generation for Math MCQs via In-context Learning*
  (2023) — **[B]**
- **arXiv:2311.04554** — *Assessing Distractors in Multiple-Choice Tests* (2023) — **[B]**
- **arXiv:2304.04881** — *DISTO: Evaluating Textual Distractors for Multi-Choice Questions* (2023). Key
  methodological finding: *"MT metrics often **misjudge** the suitability of generated distractors"* — the field
  was measuring the wrong thing. — **[B]**
- **arXiv:2511.01526** — *Difficulty-Controllable Cloze Question Distractor Generation* (2025) — notes *"the
  absence of difficulty-annotated datasets further hinders progress."* — **[B]**
- **arXiv:2601.14280** — *Hallucination-Free Automatic Question & Answer Generation for Intuitive Learning*
  (2026-01). **Names the taxonomy this section needs**, verbatim: *"We identified **four key hallucination types
  in MCQ generation: reasoning inconsistencies, insolvability, factual errors, and mathematical errors.**"* — **[B]**
- **arXiv:2601.06098** — *Automatic Question Generation for Intuitive Learning Utilizing Causal Graph Guided
  Chain of Thought Reasoning* (2026-01) — *"its effectiveness is hindered by hallucinations… which may generate
  factually incorrect, ambiguous…"* questions. — **[B]**
- **arXiv:2504.07994** — *Evaluating the Fitness of Ontologies for the Task of Question Generation* (2025) — **[B]**
- **arXiv:2507.22947** — *ELMES: An Automated Framework for Evaluating LLMs in Educational Scenarios*
  (2025) — *"evaluation metrics vary substantially across different educational scenarios."* — **[B]**
- **arXiv:2507.12484** — *AI-Powered Math Tutoring: Platform for Personalized and Adaptive Education* (2025) — **[B]**
- **arXiv:2507.17985** — *How K-12 Educators Use AI: LLM-Assisted Qualitative Analysis at Scale* (2025).
  **13,000+ unscripted educator-AI conversations** — the independent counterpart to SchoolAI's Stanford SCALE
  number. — **[B]**

---

## 5. What breaks at full-course scale

Take the brief's hierarchy — **modules → chapters → topics → exercises → quizzes** — and note that generation
quality **degrades monotonically as you descend it.** Modules are easy (they're an outline). Exposition is easy
(it's the training distribution). Exercises are hard. Answer keys are where it collapses.

### 5.1 Coherence across chapters

**No paper found this session measures cross-chapter coherence in a generated course.** This is a genuine hole.
The nearest framings are DOLOMITES (arXiv:2405.05938), which treats lesson planning as long-form *structured*
generation, and SciencePedia (arXiv:2510.26854), which sidesteps coherence entirely by generating **~200,000
independent encyclopedia entries** — a bag of atoms with no narrative thread, no callbacks, no "as we saw in
Chapter 3." LessonBench-V1 (arXiv:2607.13041) evaluates *lessons*, singular. **The unit of evaluation in this
entire literature is the lesson or the item; nobody evaluates the book.** — **[O]**, and see §7.4.

### 5.2 Prerequisite ordering

- **arXiv:2605.09635** — *K12-KGraph: A Curriculum-Aligned Knowledge Graph for Benchmarking and Training
  Educational LLMs* (2026-05). **"Gemini-3-Flash achieves only 57 percent exact match and Gemma-4-31B-IT reaches
  46 percent, with **Prereq and Neighbor being the hardest tasks**."** — **[B]**. Prerequisite reasoning is
  explicitly the *worst-performing* task family in a purpose-built curriculum benchmark.
- Contrast with §4.2: every learning-path system **assumes** a correct prerequisite graph as input. Paradigm's
  UI (§1.3) makes the DAG **hand-editable**, which is the honest engineering response — push the ordering
  decision back to the human, because the model can't be trusted with it.

### 5.3 Difficulty calibration

This is where the negative results are strongest, and they are worth quoting in full.

**The optimistic half of the literature** (predicting difficulty from item text, given real response data):
- **arXiv:2509.23486** — *Text-Based Approaches to Item Difficulty Modeling in Large-Scale Assessments: A
  Systematic Review* (2025-09). Best-case benchmarks: **RMSE as low as 0.165, Pearson up to 0.87, accuracy up to
  0.806.** — **[B]**
- **arXiv:2504.08804** — *Estimating Item Difficulty Using LLMs and Tree-Based ML* (2025-04): **r up to 0.87**,
  and critically **feature-based methods outperformed direct LLM prediction.** — **[B]**
- **arXiv:2602.00034** — *Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter
  Estimation* (2026-02): **Pearson ≈ 0.78** on unseen questions. — **[B]**
- **arXiv:2601.09953** — *Take Out Your Calculators: Estimating the Real Difficulty of Question Items with LLM
  Student Simulations* (2026-01): **r = 0.75 / 0.76 / 0.82** at grades 4 / 8 / 12. — **[B]**
- Also: arXiv:2503.08551 (28.3% MSE reduction), arXiv:2502.20663 (RMSE 0.59 vs 0.92 baseline, r=0.77),
  arXiv:2507.05129 (SMART), arXiv:2412.11831 (model uncertainty as difficulty signal), arXiv:2605.16290
  (R² 0.525→0.686), arXiv:2603.04670 (vision+language, MAE 0.224 vs text-only 0.338). — **[B]**

**The half that matters for generation:**
- **arXiv:2606.18709** — *LLMs Struggle to Measure What Distinguishes Students of Different Proficiency Levels:
  A Study of Item **Discrimination** in Reading Comprehension Assessment* (2026-06). *"Direct prediction yields
  weak alignment… best-performing model reaches only **Spearman correlation of 0.152**"*; response-based
  calibration gives *"limited signal, with… **Spearman correlation of 0.241**."* — **[B]**
- **arXiv:2602.00070** — *FoundationalASSIST* (2026-02). *"Every model **barely achieves trivial baseline** on
  knowledge tracing"*; ***"All models fall below random chance on item discrimination"***; only *"up to 68.6%"*
  on relative difficulty judgment. — **[B]**
- **arXiv:2512.18880** — *Can LLMs Estimate Student Struggles?* (2025-12). *"**systematic misalignment** where
  scaling up model size is **not reliably helpful**"*; *"**high performance often impedes accurate difficulty
  estimation**"*; a *"critical lack of introspection."* — **[B]**

**The synthesis the survey should make.** Difficulty (*how many students get it right*) is moderately
predictable — r≈0.75–0.87. **Discrimination (*whether the item separates strong from weak students*) is
essentially unpredictable — Spearman 0.152, below random chance in one benchmark.** Difficulty tells you where
to place an item in a ramp; discrimination tells you whether the item *measures anything at all.* A generated
course can therefore produce a plausible difficulty gradient made entirely of items with no diagnostic value —
a ramp that looks right and assesses nothing. And note arXiv:2512.18880's mechanism: **the model is too good at
the task to model a student failing it.** That is not a bug that scales away; the paper says scaling makes it
worse.

### 5.4 The notorious failure: generated exercises whose stated answers are wrong

**arXiv:2206.11861** (Sarsa, Denny, Hellas & Leinonen, ICER 2022) is the definitive measurement — **[A]**.
240 exercises generated by Codex (60 concept combinations × 2 temperatures × 2 exercises); 120 manually
evaluated. Verbatim numbers:

| Property | Result |
|---|---|
| Sensible | **75.0%** |
| Novel | **81.8%** |
| Had a matching sample solution | **76.7%** |
| Sample solution **executed without error** | **89.7%** |
| Included automated tests | **70.8%** |
| **Sample solution passed the exercise's own tests** | **30.9%** (51 of 165) |
| Statement coverage *when* tests passed (n=51) | 98.0% avg; 48/51 at 100% |
| **Code-explanation lines that were correct** | **117 / 174 = 67.2%** (though "90% explained all parts of the code") |

Read the 89.7% and the 30.9% together. **The code runs. It just doesn't solve the problem.** That gap —
*syntactically valid, semantically wrong* — is the exact signature of the failure the brief calls notorious, and
it is the reason generated exercises cannot be shipped unreviewed. The paper's own conclusion is
appropriately hedged: *"there remains a need for some oversight to ensure the quality of the generated content
before it is delivered to students."*

Note also the explanation number: **32.8% of generated explanation lines were wrong** even though the
explanations *looked* complete (90% covered all parts). **Coverage and correctness are uncorrelated.** Fluent,
complete, wrong — and in programming education, wrong at nearly the same rate as the answer keys.

Corroborating measurements: **~47% of LLM distractors rejected by teachers** (arXiv:2307.16338, **[A]**); the
four-way hallucination taxonomy — *reasoning inconsistencies, insolvability, factual errors, mathematical
errors* (arXiv:2601.14280, **[B]**). "Insolvability" is worth flagging separately: a generated exercise that
**has no correct answer at all** is a distinct and worse failure than one with a wrong key, and it is
invisible to any check that only validates the key's format.

### 5.5 Why the ladder degrades — the mechanism

Exposition has a **dense, self-supervised training signal**: the internet is exposition, and "plausible-sounding
paragraph about backprop" is exactly what next-token prediction optimises. An exercise has a **verification
requirement that the generator cannot discharge**: it must have exactly one correct answer, that answer must be
the stated one, the distractors must be wrong-but-tempting, the difficulty must land in the learner's zone, and
the item must discriminate. Five constraints, none of which is checkable from the text alone. Sarsa et al. only
caught the 30.9% because **programming exercises are executable** — there was a ground-truth oracle. **For
history, biology, or conceptual maths, no such oracle exists**, so the equivalent error rate in most subjects is
not merely unknown, it is *unmeasured by construction*. The overgenerate-and-rank paradigm (arXiv:2405.05144)
is the field's tacit admission: the only working strategy is to generate many and throw most away — and that
requires a discriminator, which returns you to §5.3, where discrimination prediction is at Spearman 0.152.

---

## 6. The corpus problem is exercises — an original replication

### 6.1 The claim under test

The survey's audit of a **128-notebook zero-to-hero corpus found ZERO exercises** — 0 hits for
Exercise / Your Turn / Quiz / Solution. **That claim's source document was not present in this repository**
(searched `survey/`, `PRD.md`, `CLAUDE.md`, `evidence/`; `evidence/` is empty and only three survey files exist).
It is **taken as given from the parent brief and treated as unverified here** — **[C]**. What follows is an
**independent replication on different corpora**, which is stronger evidence anyway.

### 6.2 Method

Via authenticated GitHub API: enumerate the default-branch tree, select `.ipynb` chapter/lecture notebooks,
fetch each from `raw.githubusercontent.com`, and count case-insensitive occurrences of
`exercise | your turn | questionnaire | quiz | try it yourself | solution | practice problem`. Reproducible;
run 2026-07-27. — **[X]**

### 6.3 Results

| Corpus | Notebooks scanned | Files with ≥1 marker | Total marker hits |
|---|---|---|---|
| **karpathy/nn-zero-to-hero** | 7 (all) | **1** | **4** |
| rasbt/LLMs-from-scratch (ch01–07 main) | 6 | 6 | 8 |
| fastai/fastbook (numbered chapters) | 20 | **19** | **74** |
| mrdbourke/pytorch-deep-learning (numbered) | 9 | **9** | **89** |

Whole-repo file-name scan — **[X]**:

- **`karpathy/nn-zero-to-hero`: 9 files total, 7 notebooks, and NOT ONE file whose name contains
  exercise / homework / problem-set / assignment / quiz / solution.**
- `rasbt/LLMs-from-scratch`: 353 files, **7 dedicated `exercise-solutions.ipynb`** (one per chapter + appendix A)
  plus `exercise_experiments.py`.
- `mrdbourke/pytorch-deep-learning`: 248 files, a dedicated **`extras/exercises/`** directory with 8+
  per-chapter exercise notebooks and templates.
- `fastai/fastbook`: 490 files — no exercise *files*, because its exercises are **in-chapter "Questionnaire"
  sections** (hence 74 in-content hits).

### 6.4 What the karpathy result actually is (the honest version)

The canonical **"zero to hero"** corpus — Karpathy's, the one the phrase comes from — is **7 notebooks with
4 exercise mentions, all 4 inside a single notebook**, `makemore_part4_backprop.ipynb`. **Six of seven notebooks
contain zero exercise scaffolding of any kind.**

And the four that exist are **pre-solved in place.** Verbatim from the notebook — **[X]**:

```python
# Exercise 1: backprop through the whole thing manually,
# backpropagating through exactly all of the variables
# as they are defined in the forward pass above, one by one
dlogprobs = torch.zeros_like(logprobs)
dlogprobs[range(n), Yb] = -1.0/n
dprobs = (1.0 / probs) * dlogprobs
...
```

The word "Exercise" appears, and **the answer is printed on the next line of the same cell.** There is no
withheld solution, no blank to fill, no check. It is a section heading over a worked example. So the strict
count of *actual exercises a learner must do* in `nn-zero-to-hero` is defensibly **zero**, and the survey's
"0 hits" finding replicates — with the nuance that a naive grep would report 4 and be wrong in the *opposite*
direction from what you'd expect.

### 6.5 The generalisation, and its limit

**The generalisation holds:** lecture-derived, exposition-first corpora — the kind LLM course generators are
trained on and the kind they imitate — carry essentially **no practice**. `nn-zero-to-hero` is a transcript of
videos: it is *demonstration*, and demonstration has no slot for the learner to fail in.

**The limit, stated plainly — this is the negative result for §6:** the pattern is **not** "notebook corpora
lack exercises." Three of four corpora scanned are *dense* with them — fastbook at 74 hits across 19/20 chapters,
mrdbourke at 89 across 9/9, LLMs-from-scratch with a per-chapter solutions notebook. **All three are books**
(fastbook → O'Reilly; LLMs-from-scratch → Manning; mrdbourke → a structured course). **The variable is not
format, it is authorial intent: works written as *books* have exercises; works written as *lecture transcripts*
do not.** A **~20× difference in exercise density** (4 hits/7 notebooks vs 89/9) between artifacts in the same
language, same domain, same file format.

### 6.6 Why this closes the loop

Generation systems inherit this. They optimise for exposition because **(a)** exposition dominates the training
corpus, **(b)** exposition has no verification requirement, and **(c)** exposition is what the demo shows well.
Every §3 vendor confirms the shape from the other direction: Duolingo's humans write the *scenarios*, Synthesis's
humans hold the *pedagogy*, Khan's library is human, Ello's books are human, SchoolAI's Spaces start with a
teacher. **The machine writes the telling; the human still writes the doing** — and §5.4 says why: the doing is
the only part with a right answer that can be wrong.

Paradigm is the interesting counter-instance and deserves to be tracked rather than dismissed: its `robots.txt`
exposes **`/practice/` and `/exam/` as first-class routes** (§1.4), so the product model at least *reserves a
slot* for practice. Whether what lands in that slot has correct answer keys is **unknown and unknowable from
outside the auth wall** — the most important open question in this section.

---

## 7. Negative and null results

1. **Paradigm's generated artifacts are unobservable.** Everything pedagogical (`/lesson/`, `/practice/`,
   `/exam/`, `/notebook/`) is auth-walled and `Disallow`ed; the sitemap exposes only marketing pages. **No
   generated Paradigm course was inspected this session.** All §1 quality claims are vendor-side. — **[O]**
2. **Paradigm publishes zero efficacy evidence.** No study, no citation, no outcome number, no research page —
   only a Polanyi epigraph that arguably argues *against* its own approach (§1.5). — **[O]**
3. **No Vizuara book was found.** Contra the brief's framing ("their books"), the bundle, site routes and
   YouTube metadata show **courses and bootcamps only**. No ISBN, publisher, or book route. — **[O]**
4. **No paper measuring cross-chapter coherence in generated courses was found.** The literature's unit of
   evaluation is the *lesson* (LessonBench, 647 lessons) or the *item* (Dr.Academy, distractor work); the
   largest generated corpus (SciencePedia, ~200k entries) is deliberately **non-sequential**. Full-course
   coherence is, as far as this session could determine, **unmeasured**. — **[O]**
5. **Coursera Coach could not be reached at all.** Four URLs, four 404s: `coursera.org/coach`,
   `coursera.org/about/coach`, `blog.coursera.org/introducing-coursera-coach/`, `coursera.org/gen-ai`.
   **No claim is made about it in this document.** — **[O]**
6. **An arXiv search for expert-reviewed error rates in AI-generated exam questions returned literally nothing:**
   *"Sorry, your query for all: AI generated exam questions expert review factual errors medical education
   produced no results."* — **[O]**. Informative rather than merely absent: **the expert-review literature on
   generated assessment items lives in medical-education and psychometrics journals, not on arXiv**, so any
   arXiv-only survey of this question will systematically understate the error rates.
7. **Infrastructure failures:** OpenAlex daily budget exhausted (0 queries succeeded); Semantic Scholar HTTP 429
   (0 queries succeeded); arXiv Atom API HTTP 429 after ~6 queries, forcing fallback to the HTML search
   interface, which returns fewer and less complete results (the `automatic textbook generation` HTML query
   surfaced only 4 papers, versus richer Atom results earlier). **§4's coverage is therefore a lower bound.**
8. **Vendor efficacy is near-worthless as a class.** Of ten adjacent products, **five publish no outcome number
   at all** (Khanmigo, Duolingo Max, Synthesis, Brisk, and Coursera Coach by unreachability); three publish
   internal self-measured numbers with no methodology (MagicSchool, Diffit, Ello); **one** has an externally
   reviewed correlational study (SchoolAI, ESSA Level III, Instructure); one cites external state test data in
   self-selected case studies (Curipod). **Zero RCTs. Zero effect sizes. Zero preregistrations.**

---

## 8. What this section contributes to the survey

1. **The ladder degrades monotonically.** Modules → chapters → topics → **exercises** → **quizzes**. Generation
   quality falls off a cliff at the exercise boundary, and the number to quote is **30.9%** (arXiv:2206.11861):
   the fraction of generated programming exercises whose own sample solution passed their own tests. Pair it
   with **89.7%** (executed without error) to make the point that **fluency and correctness are decoupled** — and
   with **67.2%** (correct explanation lines despite 90% coverage) to show the same decoupling in prose.
2. **Difficulty is learnable; discrimination is not.** r≈0.75–0.87 for difficulty vs **Spearman 0.152** for
   discrimination (arXiv:2606.18709), *below random chance* in FoundationalASSIST (arXiv:2602.00070). A
   generated course can have a perfect-looking difficulty ramp built entirely from items that measure nothing.
   And arXiv:2512.18880 says scaling **does not fix it** — competence at the task impedes modelling failure at it.
3. **Prerequisite ordering is the worst-performing task** in the only curriculum-aligned knowledge-graph
   benchmark found (K12-KGraph, arXiv:2605.09635: 57% / 46% exact match, *"Prereq and Neighbor being the hardest
   tasks"*). Paradigm's hand-editable DAG is the correct engineering concession.
4. **The exercise gap is inherited from the corpus, and it is about authorial intent, not format.** Original
   audit (§6): `nn-zero-to-hero` = 7 notebooks, 4 marker hits, all in one file, **all pre-solved**; fastbook = 74
   hits across 19/20; mrdbourke = 89 across 9/9. **~20× density difference, same language, same format.**
   Lecture transcripts have no slot for the learner to fail in; books do.
5. **No commercial system claims to author the curriculum.** Duolingo: *"Humans write the scenarios."*
   Synthesis: humans *"handle much of the pedagogy."* Khan tutors over a human library. Ello licenses one.
   SchoolAI: *"Every Space starts with a teacher."* Curipod: *"100% teacher controlled."* **The AI-native
   textbook does not yet exist as a shipped product** — what ships is AI-native *delivery* over human-authored
   *structure*. Paradigm's own YC Reject Camp, which pays to acquire human-authored courses, is the cleanest
   proof of this from inside the most AI-native company in the set.
6. **Evidence is inversely correlated with generation volume.** The heaviest generators (MagicSchool 130+ tools,
   Brisk 30+, Diffit) publish only teacher-*sentiment* numbers; the lightest (SchoolAI, Curipod, which keep the
   teacher as author) hold the only externally-sourced outcome data. Zero RCTs across ten products.

---

## Appendix: source ledger

**Primary web sources (17):** paradigm.study (`/`, `/camp`, `/ai-archetype`, `/robots.txt`, `/sitemap.xml`),
vizuara.ai (`/`, `/robots.txt`, `/assets/index-CMDukm9D.js`), vizuara.substack.com (`/`, `/about`),
youtube.com/@vizuara, khanmigo.ai/learners, blog.duolingo.com/duolingo-max, synthesis.com/tutor,
magicschool.ai, curipod.com, web.diffit.me, briskteaching.com, schoolai.com, ello.com.

**arXiv papers cited with IDs (41):** 2206.11861 · 2408.10947 · 2503.17710 · 2510.26854 · 2607.13041 ·
2504.05370 · 2408.01102 · 2503.09276 · 2510.19866 · 2510.03369 · 2405.05938 · 2412.04185 · 2504.08856 ·
2504.18603 · 1905.12470 · 2005.03818 · 2305.04475 · 2305.06398 · 2306.04234 · 2406.10245 · 2406.17518 ·
2507.05295 · 2506.22303 · 2604.14613 · 2605.16750 · 2401.08517 · 2511.21037 · 2402.01512 · 2307.16338 ·
2406.19356 · 2405.05144 · 2308.03234 · 2311.04554 · 2304.04881 · 2511.01526 · 2601.14280 · 2601.06098 ·
2504.07994 · 2507.22947 · 2507.12484 · 2507.17985 · 2605.09635 · 2606.18709 · 2602.00070 · 2512.18880 ·
2509.23486 · 2504.08804 · 2602.00034 · 2601.09953 · 2503.08551 · 2502.20663 · 2507.05129 · 2412.11831 ·
2605.16290 · 2603.04670 · 2411.01775 · 2606.13684 · 2312.01032 · 2412.19361.

**GitHub repositories audited (4, original measurement):** karpathy/nn-zero-to-hero · rasbt/LLMs-from-scratch ·
fastai/fastbook · mrdbourke/pytorch-deep-learning. Also enumerated: d2l-ai/d2l-en (1,027 files, **0 `.ipynb`** —
source is Markdown), ageron/handson-ml3 (28 notebooks).

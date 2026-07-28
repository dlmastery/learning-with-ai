---
title: "What actually shipped: a latest-period sweep of edtech and frontier AI for education"
wave: E
section: E3
date_researched: 2026-07-28
sources_count: 61
status: raw-research
---

# E3 — The latest sweep

> **Scope discipline.** This report is deliberately *differential*. Two prior reports
> cover adjacent ground and were read in full before any retrieval began:
> `D1-frontier-quarter.md` (frontier capability, Apr–Jul 2026, researched 2026-07-25) and
> `E1-E2-edtech-landscape-lessonorca.md` (market taxonomy + LessonOrca telemetry,
> researched 2026-07-27). `F8-safety-privacy-children.md` holds the legal analysis.
> E3 reports **what is new, what changed, and what those reports under-covered** — plus
> it closes seven items they explicitly flagged as unverifiable. It does not restate them.

> **Retrieval note.** WebSearch was exhausted before this section began. Everything here
> came from: the **arXiv advanced-search UI** (the arXiv *API* returned sustained HTTP 429
> and was unusable); the **ERIC API** (`api.ies.ed.gov`, reachable and fast); the
> **Crossref REST API**; **OpenAlex**; the **Hugging Face model API** (the key unlock —
> it returns *absolute* `createdAt` timestamps, which is how D1's Qwen/Moonshot dating
> problem got solved); **SEC EDGAR** full-text search and the submissions JSON API;
> **EUR-Lex**; and direct `WebFetch`/`curl` of vendor and regulator pages.
> Unreachable sources are listed in §9 with HTTP statuses, never guessed around.

**Evidence labels** are the project standard: `MEASURED-RCT` · `MEASURED-META` ·
`MEASURED-BENCH` · `OBSERVED` · `VENDOR` · `DEMO` · `INFERENCE`, plus `VERIFIED`
(primary legal text retrieved and quoted) and `UNVERIFIED` (source unreachable).

**The rule this section is most at risk of breaking, so it is restated:** a `VENDOR`
claim is never restated as a finding. Where a vendor asserts an outcome with no design,
the *finding* is the absence of the design, not the number.

---

## 0. The five things that changed

Ordered by how much they should change a builder's behaviour.

1. **The EU AI Act's education high-risk deadline moved, and it moved yesterday.**
   Annex III(3)(b) obligations no longer bite on 2 August 2026. They bite on
   **2 December 2027**. `VERIFIED` — §5.
2. **The best-resourced nonprofit in the field published a null.** Sal Khan, 17 July
   2026: the first Khanmigo *"did not change student learning as much as many of us
   hoped it would."* `OBSERVED` (vendor statement against interest) — §2.
3. **A 371-student classroom RCT found pedagogically-scaffolded GenAI no better than
   plain ChatGPT on domain knowledge.** *Educational Psychology Review*, April 2026.
   `MEASURED-RCT` — §6.
4. **Chegg's academic business halved in twelve months**, and the company says in an
   SEC filing why. This is the only audited number in the entire corpus for "what
   generative AI does to an incumbent." `OBSERVED` — §3.
5. **A school can now legally put frontier-adjacent weights on a USB stick.** Gemma 4
   ships Apache-2.0 and ungated. `OBSERVED` — §4.

And the thing that did *not* change: **nobody shipped an education-positioned frontier
model.** Not one, from any of the eight labs surveyed. §1 says what they shipped instead.

---

## 1. Frontier capability, read from model cards

D1 built the dated timeline for April–July 2026 and I have not rebuilt it. What follows
is (a) the seven capability facts D1 flagged as **unverifiable**, now verified, and
(b) the one structural read that the model cards support and the press coverage doesn't.

### 1.1 The method that closed D1's gaps

D1 could not date Qwen or Moonshot releases because `qwen.ai/blog` renders client-side,
`moonshotai.github.io` is a bare redirect, and the Hugging Face *web pages* show relative
timestamps ("updated 3 months ago") that don't resolve. **The Hugging Face JSON API
returns absolute ISO timestamps.** `curl https://huggingface.co/api/models?author=X&sort=createdAt`
is the primary-source dating tool for open-weight releases, and it should be the default
method for this project from here on.

### 1.2 Newly verified (all `OBSERVED` from the HF API + model cards, retrieved 2026-07-28)

| Item | Fact | Grade |
|---|---|---|
| **Kimi K3** (`moonshotai/Kimi-K3`) | **createdAt 2026-06-13**. 2.8T total / **104B activated**, 896 experts (16/token), 93 layers ("69 KDA + 24 Gated MLA"). **1,048,576-token context.** Text + image + **video** in one architecture. Kimi K3 License (not OSI). 6,433 likes. | `OBSERVED` (existence, date, specs) |
| Kimi K3 benchmarks | GPQA Diamond 93.5; Terminal-Bench 2.1 88.3; BrowseComp 91.2; OSWorld-Verified 84.8; MathVision 94.3/97.8; Video-MME 90.0; MMMU-Pro 81.6/83.4 | `MEASURED-BENCH (vendor-run)` |
| **Qwen-AgentWorld-35B-A3B** | createdAt **2026-06-22**. 35B total / 3B active MoE, **262,144 context**, **Apache-2.0**. A *language* world model: predicts next environment state given an action, across MCP/Search/Terminal/SWE/Android/Web/OS. AgentWorldBench overall **56.39/100**. | `OBSERVED` + `MEASURED-BENCH (vendor-run)` |
| **Qwen3-ASR-0.6B / 1.7B** | createdAt **2026-06-26**, Apache-2.0, 13+ languages. First credible Apache-licensed successor to a frozen Whisper. | `OBSERVED` |
| **DeepSeek-V4** technical report | **arXiv:2606.19348**, "Towards Highly Efficient Million-Token Context Intelligence." 1M context achieved via **Compressed Sparse Attention + Heavily Compressed Attention**, plus Manifold-Constrained Hyper-Connections and the Muon optimizer. **73% inference-FLOP reduction vs V3.2.** | `MEASURED-BENCH` (paper) |
| DeepSeek V4 maths claims | Still **not verified.** The report's visible content carries no AIME/MATH/GPQA figures. D1's caution stands. | `UNVERIFIED` |
| **Meta open weights** | **Newest `meta-llama` artifact on Hugging Face is dated 2025-04-28** (Prompt-Guard-2). Llama-4 Scout/Maverick are 2025-04-01→04. **~15 months with no open-weight release.** | `OBSERVED` |

### 1.3 On-device: the number that matters is 4.5B, and the licence

**Gemma 4** is a family, not the single 12B model D1 recorded. The HF API shows
`gemma-4-31B`, `-12B`, `-E4B`, `-E2B`, each in QAT variants, plus explicit
`-mobile-ct` / `-mobile-transformers` builds (all createdAt 2026-06-01→06-05).

`gemma-4-E4B`: **4.5B *effective* parameters** (8B with embeddings) via Per-Layer
Embeddings — *"rather than adding more layers or parameters to the model, PLE gives each
decoder layer its own small embedding for every token"* — **128K context**, text + image +
audio (30s max), targeted at *"high-end phones to laptops and servers."* MMLU-Pro **69.4**
against **85.2** for the 31B. `OBSERVED` / `MEASURED-BENCH (vendor-run)`.

Two things follow, and only one of them is about capability.

**The capability read is modest and should be stated as such.** A 16-point MMLU-Pro drop
is what on-device costs you. For a tutor whose job is diagnosing a fraction
misconception, that gap is probably irrelevant; for a tutor asked to explain organic
chemistry, it is not. Nobody has measured which. That is a `MEASURED-BENCH` fact being
used to make an `INFERENCE`, and I flag it as such.

**The licensing read is the consequential one.** Gemma 4 is tagged
**`license:apache-2.0` with `gated: false`** (`OBSERVED`, HF API, verified on
`gemma-4-E4B-it-qat-q4_0-unquantized` and `gemma-4-12B-it-qat-q4_0-gguf`). Gemma has
dropped its custom restricted licence. There is no click-through and no acceptable-use
rider. A ministry of education can mirror the weights, put them on a USB stick, and hand
them to a school with no internet. That is a change in *what is legally possible*, and
it is worth more to a low-connectivity deployment than any benchmark on the card.

### 1.4 The negative result on live voice, and it is the important one

D1's sharpest judgement was that **full-duplex speech is the pedagogically decisive
capability and is not available to build on** (GPT-Live is ChatGPT-only, API behind a
form). I went looking for the open-weight escape hatch. There isn't one.

- **`mistralai/Voxtral-Mini-4B-Realtime-2602`** — 1,960,122 downloads, Apache-2.0, the
  most-downloaded open realtime speech artifact in the sweep. Its own model card
  describes **turn-based streaming ASR**: configurable transcription delay 80ms–2.4s,
  480ms recommended, FLEURS multilingual WER 8.72% @480ms, runs on **one ≥16GB GPU**.
  It is speech **in**, text **out**. It is not full-duplex and does not speak.
  `OBSERVED` + `MEASURED-BENCH (vendor-run)`.
- **`kyutai-labs/moshi`** — the reference open full-duplex model. 10,744 stars, but its
  **latest release is `rustymimi-0.2.2`, published 2024-09-22**, and the companion
  `delayed-streams-modeling` repo has been quiet since 2026-01-26. `OBSERVED`.

**Finding.** Turn-taking — knowing when *not* to speak while a learner is mid-thought —
remains available only inside one vendor's consumer app. The open ecosystem has excellent
ASR and excellent TTS and **nothing that holds a productive silence**. This is the
clearest capability gap in the whole sweep, and unlike most gaps it is not a scale
problem: Moshi showed the architecture works and then stopped shipping.

### 1.5 The structural read: eight labs, zero education positioning

Across every model card and release page retrieved for this section — Kimi K3,
Qwen-AgentWorld, Qwen3-ASR, DeepSeek-V4, Gemma 4 (all sizes), Voxtral Realtime,
Leanstral 1.5, Mistral Medium 3.5 — **not one mentions education, tutoring, teaching, or
learning as a target use case.** Qwen-AgentWorld simulates seven environment types and
none of them is a classroom. Checking the three days since D1's cutoff (2026-07-25 →
2026-07-28): Anthropic's news index shows *"Our position on open-weights models"* and a
Cognizant partnership on 27 July, nothing education-facing; the DeepMind blog index shows
no post after 13 July. `OBSERVED`.

D1 concluded that "the pedagogy layer became permanently yours." The model cards three
days later say the same thing more bluntly: **the labs are not building toward you.**
The education-relevant capabilities — 1M context, cheap high-turn-count inference,
on-device multimodal, open ASR — are all arriving as *side effects* of agentic-coding and
enterprise roadmaps. That is fine. It is also a planning fact: the roadmap you are
building against is not a roadmap anyone published.

---

## 2. Education products: mechanism vs. evidence

The prior report covered MagicSchool, Khanmigo, SchoolAI, Amira, Ello, Speak, Brilliant,
Third Space Learning, ASSISTments, Gradescope and Turnitin. This section covers the
**products it listed but could not retrieve**, plus everything that changed since.

### 2.1 The single most important item: a vendor published a null

**Khan Academy, "Khanmigo's First Chapter Changed How I Think About AI: A note from Sal
Khan," blog.khanacademy.org, dated 17 July 2026.** Verbatim:

> *"the first version of Khanmigo that we launched three years ago did not change student
> learning as much as many of us hoped it would."*

And the diagnosis, verbatim:

> *"For students who engaged, Khanmigo did what we designed it to do. It probed reasoning,
> supported students as they worked through a concept, pushed back on logical fallacies,
> and behaved like a human tutor."*
>
> *"if Khanmigo was going to help students think harder, it had to become more central to
> the practice experience."*

`OBSERVED` — this is a vendor statement, but it is a statement **against interest**, which
is the one category of vendor claim that carries evidentiary weight. It is not an RCT and
must not be cited as one; no effect size, no design, and no comparison group is given.

**Why this is the most useful item in the sweep.** The mechanism worked and the outcome
didn't, and the stated reason is *engagement architecture*, not pedagogy. A well-designed
Socratic tutor sitting one click away from the practice problem loses to the friction of
that click. The redesign moves Khanmigo **inside** the practice problem and prompts the
student to explain their reasoning, rather than requiring the student to first recognise
they need help — i.e. it removes a **metacognitive** prerequisite, which is precisely the
capacity that struggling students most lack. That is a real design lesson and it is
free to anyone building.

It also sharpens E1's Finding E1-d. Mechanism claims are checkable and outcome claims
usually aren't — but Khanmigo just demonstrated that **a mechanism claim can be fully
true and still buy nothing**, because the mechanism only fires if the student invokes it.
The missing term is *dosage under realistic friction*, and nobody's marketing has it.

Evidence caveat, and it matters: the post gestures at a *"three-year Newark Public Schools
efficacy study"* with **no numbers, no design, and no link**, and the study does not
resolve via Crossref. That claim is `UNVERIFIED` and is additionally about Khan Academy
the platform, not Khanmigo. Do not carry it.

### 2.2 The gap-fill table

Retrieved 2026-07-28. "Evidence" answers only one question: *is there a controlled
outcome study, or only usage/engagement/time-saved?*

| Product | Mechanism (verbatim where quoted) | Outcome evidence | Label |
|---|---|---|---|
| **Brisk Teaching** | *"the AI education platform helping teachers create materials, give feedback, and adapt instruction inside the Google and Microsoft tools they already use."* Browser extension. "Inspect Writing" replays a student's typing history as video to detect AI use. | **None.** `/research` → 404. Claims *"2 million teachers"*, *"one in four educators in the U.S."* — usage only. | `VENDOR` |
| **Curipod** | *"Teacher led lessons aligned to your district's curriculum. Students read, write and discuss. Not alone on a screen."* Loop: write → immediate AI feedback → reflect & revise. *"Students do not have accounts. No AI chatbots."* | **Partial, and the good study is the wrong population** — see §2.3. | `MEASURED-RCT` (narrow) + `VENDOR` |
| **Diffit** | Generates levelled passages from *"any topic or … your PDF, text, link, video, or vocab list"*; grade/language/standard/reading-level controls; exports to Classroom/M365. | **None.** Only a self-selected user survey (n=2,517 teachers, 13–20 Nov 2024): 96% "saves me time", 93%, 86%. Teacher opinion, not a student outcome. | `VENDOR` |
| **Synthesis** | *"Your child's personal math tutor"*, K-5, *"micro-assessments"* gate advancement. Explicitly distances from LLMs: *"we do not simply outsource your child's education…to an LLM."* Plus Synthesis Teams, ages 8–14 team simulations. | **None.** `/research` → 404. Testimonials + "35,000+ families" (elsewhere "over 25,000"). Teams' claimed outcomes (judgment, sense-making, collaboration) have **no assessment instrument at all**. See §3.3 for its SEC financials. | `VENDOR` / `DEMO` |
| **Riiid** | — | **Company gone under that name.** `riiid.com` **301 → corp.socra.ai**. Successor Socra AI sells Santa/Real Academy; **EdNet and all publications removed from the corporate site.** Historical EdNet paper is real (`10.1007/978-3-030-52240-7_13`, AIED 2020) but is a *dataset/AUC* benchmark — it never measured whether a student learned more. | `OBSERVED` (corporate) + `MEASURED-BENCH` (historical) |
| **Squirrel AI** | *"Each student follows a personalized roadmap designed by our Intelligent Adaptive Learning System (IALS), based on … their initial diagnostic test."* Method: *"break down knowledge points at the nano-level, refining hundreds of original knowledge points into tens of thousands."* | **A real controlled study exists and the company's own site cites none of it.** `/research` → 404; Harvard/CMU/Stanford/SRI named with no citations. The study: Wang, Christensen, Cui, Tong, Yarnall, Shear & Feng, *Interactive Learning Environments*, `10.1080/10494820.2020.1808794` (SRI co-authored; a Squirrel chief architect is an author, so not fully independent). | `MEASURED` (uncited by vendor) + `VENDOR` |
| **Duolingo** | Gamified spaced-repetition courses. | **Evidence exists, but not where the company points.** `/efficacy` returns an SPA shell with zero body content; `/nojs/efficacy` → 404; `research.duolingo.com` renders but its **most recent publication is 2021** and it contains **no efficacy studies** (it is an NLP/psychometrics list). Four resolvable efficacy DOIs found elsewhere: `10.1111/flan.12600`, `10.1558/cj.26704`, `10.1075/jsls.00021.plo`, `10.22492/issn.2759-1182.2024.7` — all pre/post proficiency studies of **self-selected learners with no randomised control**, Duolingo-authored. | `MEASURED` (weak design, offsite) |
| **Coursera** | *"AI-powered personalized guide and features, like Role Play and Course Builder, and role-based solutions like Skills Tracks."* | **None.** **NEW:** *"Coursera recently combined with Udemy to create one of the world's most comprehensive skills development platforms."* Investor relations 403 — no 2026 learner numbers obtainable. "Coursera Coach" survives only in nav; `/about/coursera-coach` → 404. | `VENDOR` |
| **Udacity** | *"Udacity is now part of Accenture."* 97 Nanodegrees, project-based with human review. | **Usage + self-report only.** 16.9M registered; **205k Nanodegree certificates ≈ 1.2% completion** (`OBSERVED`, their own figures divided); 73% of *graduates* report a favourable career change (survivorship, no control); "$2.9M potential cost savings" is modelled, not measured. | `VENDOR` |
| **Khanmigo** | Now embedded **inside** practice problems, prompting students to explain reasoning. `khanacademy.org/khan-labs` 301s to khanmigo.ai — Khan Labs is gone as an entity. | See §2.1. No efficacy page, no ESSA tier, no study links. AEA registry holds `10.1257/rct.13519` — a **pre-registration, not results**. | `OBSERVED` + `VENDOR` |
| **Google Guided Learning** | *"Gemini breaks down the concepts and tricky problems behind your study materials, with step-by-step guides that teach you the 'why' as well as the 'how.'"* (from `gemini.google/students/`) | **None.** No canonical page exists: `gemini.google/overview/guided-learning/` **404**, `blog.google/products/gemini/guided-learning/` **404**. 18+ and select countries only. Student free-Pro offer **ended 11 March 2026**. | `VENDOR` |
| **OpenAI Study Mode** | *"powered by custom system instructions we've written in collaboration with teachers, scientists, and pedagogy experts … encouraging active participation, managing cognitive load, proactively developing metacognition and self reflection, fostering curiosity, and providing actionable and supportive feedback."* Toggleable. | **None.** *"based on longstanding research in learning science"* is an appeal to background literature, not evidence about the product. Four student testimonials. Page still dated **29 July 2025**; ChatGPT for Teachers still **19 Nov 2025**. **Nothing new in 2026.** | `VENDOR` |
| **Anthropic education** | Learning mode: *"like a good tutor: it asks questions that help you find the answers yourself."* | **None.** Nine named university partners with no linked research. Claude for Teachers (14 July 2026) remains the only education item; nothing since. | `VENDOR` |
| **MagicSchool** | 80+ teacher tools. | **The 28% claim is unattributable — see §2.4.** | `VENDOR` |

### 2.3 Curipod is the interesting case, and it is interesting in an instructive way

Curipod has the most real evidence of any product in this batch, and its homepage
still leads with the weakest number it owns.

The homepage says *"Students Scored 23 Points Higher on State Tests"* / *"50% Baseline →
73% With Curipod."* The "See the studies" link goes to 13 **district testimonials** —
pre/post STAAR and CAASPP comparisons with no control group, no sample size, and no
statistical test. One examined directly (Green Valley) compares SY2023-24 to SY2024-25
across **two teachers** with dosage ramping from twice-monthly to weekly. `VENDOR`.

But Curipod *also* lists five "Independent Research" items, and two of them are real:

| Study | Resolves? | Verdict |
|---|---|---|
| AI-Powered Pedagogy, nursing students | **Yes — `10.1016/j.teln.2025.11.032`**, *Teaching and Learning in Nursing*, 2026. n=142, RCT, d=0.301–0.800 | `MEASURED-RCT` |
| AI-Generative Tools, Oman, 4th-grade EFL | **Yes** — *TOJET* 25(1) p.106, 2026; **indexed in ERIC**. n=62 (30/32), pre-post with control, 6.47→8.00 | `MEASURED` (controlled quasi-experiment) |
| "Upskills New Teachers / 30% less planning time" | **No** — no link, no Crossref hit, no ERIC hit. Claimed n=6 teacher trainees. | `UNVERIFIED` — does not resolve |
| "Cooperative Learning 21%→89% mastery" | **No** — no link, no Crossref, no ERIC. Claimed n=39. | `UNVERIFIED` — does not resolve |
| "Increasing Science Class Engagement" | Partial — a ResearchGate preprint, not a journal DOI; outcomes self-reported (*"82% found lessons fun"*) | `OBSERVED`, non-peer-reviewed venue |

**Caveats on the one real RCT, all of which are load-bearing:** it is *university nursing
students*, not K-12; the control was *"conventional lectures supplemented with PowerPoint
presentations and textbooks"*, which confounds the intervention with active-vs-passive
instruction; and the outcomes are **survey constructs** (reflective thinking, emotional
competence), not achievement tests. **It cannot support the homepage's K-12 state-test
claim**, and it is a category error to let it.

The generalisable lesson: *a company can hold genuine evidence and still market on
testimonials, because the genuine evidence is narrower and less flattering than the
testimonials.* That gradient is the same one E1 found inside ASSISTments (0.61 → 0.03 as
n rises and the evaluator becomes independent). It appears to be a law of the sector.

### 2.4 MagicSchool: a definitive negative

E1 flagged that MagicSchool's *"28% improvement in students meeting literacy grade-level
expectations"* had no retrievable design. That has now been checked exhaustively:

- `/research`, `/efficacy`, `/impact`, `/outcomes`, `/research-and-efficacy` → **all 404**
- **Full `sitemap.xml` pulled: 153 URLs. Zero contain "research", "efficacy", "impact",
  "outcome", "study", or "whitepaper."**
- The claim sits on the **homepage** as bare text with no link, no footnote, no asterisk,
  no source, adjacent to *"7-10 hours time saved per week."*
- `/case-studies` holds 15 district narratives with no sample size, no control, no
  statistical testing — **and the 28% figure does not appear on that page at all.**
- ERIC `"MagicSchool"`: 4 records, all third-party papers *about* AI lesson-plan quality
  (one titled *"Better than Nothing? An Analysis of AI-Generated Lesson Plans…"*), none
  an efficacy study of the product.

**Finding: the number is unattributable.** Not "unverified pending a source" —
there is no source, anywhere on the property, and the site is structured so that there
could not be one. `VENDOR`. It must not be restated as an outcome, by this survey or
by anyone.

### 2.5 The pre-registration trap

Several products' "studies" resolve only to **AEA RCT registry DOIs** — Khanmigo
`10.1257/rct.13519`; Squirrel-adjacent `10.1257/rct.7637` and `10.1257/rct.16568`.
These are `10.1257/rct.*` identifiers. **They are pre-registrations. They contain no
results.** A DOI here means "someone intends to run a trial," not "a trial found
something," and a resolving DOI is exactly the signal a reader uses to assume otherwise.
Any future audit in this project should treat the `10.1257/rct.` prefix as a red flag,
not a citation.

---

## 3. Funding, consolidation, and the graveyard

E1 established the graveyard's structure (six deaths, one cause: *each succeeded at the
thing it measured, and the thing it measured was not learning*). This section adds
**audited numbers**, which the sector almost never provides, via SEC EDGAR.

### 3.1 Chegg: the only audited measurement of AI's effect on an incumbent

**Chegg, Inc., Form 10-Q for the quarter ended 2026-03-31, filed 2026-05-11**
(CIK 0001364954). `OBSERVED` — SEC-filed, reviewed financials, not a press release.

| Line | Q1 2026 | Q1 2025 | Change |
|---|---|---|---|
| **Total net revenues** | **$63,262k** | **$121,387k** | **−48%** |
| Academic Services | $45,684k | $105,252k | **−57%** |
| Chegg Skilling | $17,578k | $16,135k | +9% |
| Research & development | $9,139k | $29,428k | **−69%** |
| Sales & marketing | $10,606k | $25,614k | −59% |
| Loss from operations | $(1,037)k | $(29,002)k | — |

Academic Services fell from **87% to 72%** of net revenues in one year. The company
attributes it, verbatim:

> *"Recent technological shifts, notably Google's AI Overviews search experience, or AIO,
> and continued increase in adoption of free and paid generative AI services by students,
> have created and are expected to continue to create headwinds for our industry and our
> business, most notably a reduction in traffic to our website and customers subscribing
> to our services."*

And on the mechanism, verbatim: *"a decrease in subscription revenue of $57.6 million …
primarily related to reduced traffic which led to fewer subscribers."* An **October 2025
Restructuring Plan** is referenced throughout.

**Three readings, in descending confidence.**

1. `OBSERVED`, high confidence: the homework-answer business is collapsing on a
   twelve-month timescale, and the collapse is a *distribution* event (search traffic)
   at least as much as a *product* event.
2. `INFERENCE`: E1 identified Chegg as "the GPT Base arm of the Bastani trial,
   commercialised." If that reading is right, the −57% is the market removing the
   documented harm condition faster than any regulator could have. That is a genuinely
   good outcome arriving for entirely amoral reasons, and it should be said plainly
   rather than dressed up.
3. Worth noting and not over-reading: Chegg **no longer discloses a subscriber count**
   in the 10-Q. The disclosure stopped when the number stopped being flattering, which
   is its own small datum about sector reporting norms.

### 3.2 Consolidation

| Event | Detail | Label |
|---|---|---|
| **Coursera + Udemy** | *"Coursera recently combined with Udemy to create one of the world's most comprehensive skills development platforms"* — Coursera's own About page, © 2026. | `VENDOR` (their own corporate statement) |
| **Udacity → Accenture** | *"Udacity is now part of Accenture."* Confirmed on Udacity's own About page. | `VENDOR` (corporate) |
| **Riiid → Socra AI** | `riiid.com` 301s to `corp.socra.ai`. The peer-reviewed knowledge-tracing identity (EdNet, AIED 2020) has been **deleted from the corporate site**. | `OBSERVED` |
| **Khan Labs** | `khanacademy.org/khan-labs` 301s to `khanmigo.ai`. The experimental-lab framing is retired. | `OBSERVED` |

The pattern across all four: **the research identity is the first thing discarded in a
consolidation.** Riiid published a benchmark dataset the whole knowledge-tracing field
still uses, and its successor's website does not mention it. This is worth naming because
it means *sector research capacity is not conserved through M&A* — the papers survive in
the literature, but the institution that would have written the next one does not.

### 3.3 Synthesis: rare, audited, small-company numbers

Because Synthesis School, Inc. raised under Reg CF, it files **Form C-AR** with the SEC.
This is the only non-vendor financial view of a mid-stage AI-tutoring company in the
whole corpus. `OBSERVED` — SEC-filed (CIK 0001857145, filed 2026-04-10).

| Metric | Most recent FY | Prior FY | Change |
|---|---|---|---|
| Revenue | **$10,980,778** | $10,306,695 | **+6.5%** |
| Net income | **−$2,777,705** | −$6,161,707 | loss cut 55% |
| Total assets | **$2,850,525** | $6,003,042 | **−53%** |
| Employees | 26 | — | — |

On the same day, Synthesis filed a **Form C-TR** — termination of Reg CF reporting
(signed by the COO, 10 April 2026).

**Read this carefully and no further than it goes.** A C-TR can follow dissolution,
acquisition, going private, or simply falling out of the reporting obligation; the filing
itself states no reason and I am not going to invent one. What the numbers *do* support:
a company that grew revenue **6.5%** while halving its losses and burning through half its
balance sheet. That is a survival posture, not a growth posture, at an $11M revenue AI
tutor with **26 employees** — and it sits directly against the same product's marketing,
which offers testimonials and a family count and no outcome data at all (§2.2).

**This is the single most calibrating pair of facts in the report.** The vendor page and
the SEC filing describe the same company, and only one of them is audited.

### 3.4 What E1's funding gap still looks like

E1 could retrieve no market-level funding aggregate (HolonIQ 404). **I could not either**,
and I want to be explicit that this report therefore carries **no total-market funding
figure**. Named transactions and audited filings only. Anyone who needs a sector funding
number should treat its absence here as deliberate.

---

## 4. What a school can self-host today

This is the section the prior reports did not cover at all. Everything below is
`OBSERVED` from the GitHub REST API and the Hugging Face API on 2026-07-28. **A repo's
commit history beats its README**, so commit rates are reported alongside stars.

### 4.1 The content and platform layer is genuinely healthy

| Repo | Stars | Last push | Archived | License | Latest release |
|---|---|---|---|---|---|
| `learningequality/kolibri` | 1,086 | 2026-07-27 | no | MIT | `v0.19.5` (2026-07-13) |
| `moodle/moodle` | 7,290 | 2026-07-22 | no | GPL-3.0 | tags only (`v5.2.1`) |
| `chamilo/chamilo-lms` | 979 | 2026-07-28 | no | GPL-3.0 | `v2.0.3` (2026-06-29) |
| `openedx/openedx-platform` | 8,151 | 2026-07-27 | no | AGPL-3.0 | see caveat |
| `overhangio/tutor` (the real Open edX installer) | 1,117 | 2026-07-27 | no | AGPL-3.0 | `v21.0.8` (2026-06-23) |
| `oppia/oppia` | 6,747 | 2026-07-27 | no | Apache-2.0 | `v3.5.2` (2026-07-20) |
| `frappe/lms` | 3,088 | 2026-07-28 | no | AGPL-3.0 | `v2.60.1` (2026-07-28) |
| `ILIAS-eLearning/ILIAS` | 495 | 2026-07-27 | no | GPL-3.0 | `v11.2` (2026-07-07) |

Commits/week over the last 8 weeks (`stats/participation`) — the number that separates
alive from theatrical: **chamilo** `101,104,144,79,98,161,72,106` · **kolibri**
`87,97,54,42,171,50,84,70` · **frappe/lms** `35,83,88,100,100,17,42,38` · **moodle**
`31,47,55,61,43,77,44,4` · **openedx** `15,25,37,27,6,68,16,9` · **oppia**
`19,8,18,25,18,22,9,22` · **ILIAS** `16,17,17,13,14,30,15,7`.

**Two traps worth publishing.** (a) `openedx/edx-platform` was **renamed** to
`openedx/openedx-platform`, and its "latest release" is `named-release/birch`, published
**2015-03-02** — Open edX abandoned GitHub Releases a decade ago and ships via Tutor.
Any automated freshness check on that repo returns a **false negative**; post-2U-Chapter-11
the codebase is alive. (b) `h5p/h5p-php-library` — the PHP core every H5P-in-Moodle
install depends on — averages **under 1 commit/week** (`0,0,3,1,0,1,1,0`). The H5P
*content types* are pushed within 48 hours, so H5P is not dead; but **do not make its
integration core a load-bearing dependency.**

### 4.2 The graveyard, which is where the useful information is

Required: ≥3 negative results. Here are seven, all `OBSERVED`.

1. **`huggingface/text-generation-inference` — ARCHIVED (last push 2026-03-21).**
   10,884 stars. Hugging Face's own production serving stack, discontinued. vLLM won.
   Any school deployment guide citing TGI is obsolete.
2. **`rhasspy/piper` — ARCHIVED.** 11,270 stars, last GitHub release **2023-11-14**, 419
   open issues frozen. This was *the* recommended offline TTS for low-resource education.
   Successor `OHF-Voice/piper1-gpl` is active but **relicensed MIT → GPL-3.0**, which
   changes what a vendor may bundle into a school appliance. Budget for it.
3. **`coqui-ai/TTS` — 45,830 stars, last commit 2024-02-10 (~2.4 years), NOT archived.**
   Because the `archived` flag is false and `pushed_at` shows a later tag push, **every
   automated maintenance check returns the wrong answer.** The company is gone. The only
   live line is `idiap/coqui-ai-TTS` at 2,302 stars — 5% of the attention.
4. **`JushBJJ/Mr.-Ranedeer-AI-Tutor` — 29,607 stars, 1 commit in 12 months, NO LICENSE.**
   The most-starred "AI tutor" on GitHub is an **unlicensed prompt document**, not
   software. A school cannot lawfully deploy it on licensing grounds alone.
5. **`openai/whisper` — 2 commits in 12 months.** 105,817 stars, frozen reference
   implementation. Real work moved to `whisper.cpp` / `whisperX` / `sherpa-onnx`.
6. **`meta-llama` on Hugging Face — nothing since 2025-04-28** (§1.2). A 2026 school
   stack built on Llama is building on a line that stopped shipping 15 months ago.
7. **Kolibri's SSO path is archived.** Learning Equality archived 8 satellite repos in a
   July-2026 cleanup, including `kolibri-installer-android`, `kolibri-app`,
   `kolibri-server`, **both OIDC plugins** (2026-07-11), and `kolibri-sentry-plugin`. The
   single-sign-on integration a district would want is now archived code.

Also: **`microsoft/BitNet`** — 39,788 stars, **zero releases ever**, 34 commits in 12
months. A research demo, not a deployable runtime, and it is routinely cited as if it
were the latter.

### 4.3 The minimum viable fully-local school stack, 2026-07-28

Concretely, with the honest limits attached.

- **Content + gradebook + offline sync:** Kolibri `v0.19.5` (MIT, offline-first,
  peer-to-peer sync via `morango`), authored through Kolibri Studio + `ricecooker`. If
  you need real assessment/certification rather than content delivery, **Moodle 5.2.1** or
  **Chamilo 2.0.3** — Chamilo has the highest sustained commit rate of any LMS here.
- **Inference:** `ollama` v0.32.5 or `ggml-org/llama.cpp` `b10156`, both MIT, both pushed
  today. **Not vLLM** unless you have a real GPU and a dedicated operator — 6,105 open
  issues is a full-time job.
- **Model:** `google/gemma-4-12B-it-qat-q4_0-gguf` on a shared server;
  `gemma-4-E2B`/`E4B` QAT per-device. Apache-2.0, ungated, redistributable (§1.3).
  `Qwen3.5-4B` as the multilingual alternative (6.4M downloads).
- **Front-end:** `open-webui` v0.11.0 — **but read its licence first; it is
  `NOASSERTION`**, custom terms with branding restrictions, not clean MIT. Cherry Studio
  (AGPL-3.0) is the cleaner district choice.
- **Speech:** `k2-fsa/sherpa-onnx` (Apache-2.0, pushed today) — one C++ runtime covering
  ASR + TTS + VAD on CPU. Voices from `OHF-Voice/piper1-gpl` (mind the GPL). For
  read-aloud scoring, `whisper.cpp` or the new Apache-licensed `Qwen3-ASR-0.6B`.
- **Fully-open option:** `allenai/Olmo-Hybrid-7B` (Apache-2.0, weights **and** data) is
  the only genuinely reproducible choice — at 33,370 downloads against Qwen3.5-9B's
  11,043,117, you will be debugging it alone.

**Hardware** is an `INFERENCE` from model sizes and quantisation formats and was **not
benchmarked here**: one mid-range GPU server or a 64GB-RAM CPU box for a 12B Q4 model at
classroom concurrency; the E2B/E4B QAT builds exist to run on tablets and Pi-class
hardware, which is what `google-ai-edge/gallery` (24,293 stars, Apache-2.0) demonstrates.
Treat concurrency numbers as untested until you measure them.

**What this stack cannot do, stated flatly:**

- **No full-duplex voice.** §1.4. Barge-in conversational tutoring is proprietary-only.
- **No evidence it teaches.** §7.
- **No safety layer.** Nothing here does age-appropriate filtering, curriculum
  hallucination-guarding, or per-student data governance. `Llama-Guard-4-12B` exists,
  is gated, and is 15 months stale.
- **No SSO you can lean on.** §4.2 item 7.
- **No integration between layers.** **Kolibri does not talk to Ollama.** There is no
  maintained open project wiring an LLM tutor into an offline LMS's gradebook. That glue
  is the school's to build *and to keep building* — and it is, precisely, the gap a
  well-designed open project could fill.

---

## 5. Regulation: the deadline moved

F8 holds the legal analysis and it is not repeated. This section reports **only what
changed**, and it resolves F8's single largest flagged unknown.

### 5.1 The headline: Annex III education obligations are deferred to 2 December 2027

F8 (2026-07-27) flagged as `UNVERIFIED`: *"Is the 2 August 2026 Annex III date still the
operative date?"* — because its best source (`artificialintelligenceact.eu`) is stamped
"last updated 1 August 2024" and EUR-Lex returned HTTP 202 with an empty body.

**EUR-Lex is now reachable, and the answer is no.** `VERIFIED` — retrieved and
independently re-verified against the primary text at
`eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32026R1744`.

**Regulation (EU) 2026/1744** of the European Parliament and of the Council **of 8 July
2026** amending Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 *as regards
the simplification of the implementation of harmonised rules on artificial intelligence*
(**Digital Omnibus on AI**). Published **OJ L, 2026/1744, 24.7.2026**. Done at Strasbourg,
8 July 2026. Article 4, verbatim:

> *"This Regulation shall enter into force on the third day following that of its
> publication in the Official Journal of the European Union."*

→ **in force 27 July 2026 — yesterday.**

Article 1(40) amends AI Act Article 113, third paragraph, verbatim:

> *"(b) point (c) is replaced by the following: '(c) Chapter III, Sections 1, 2, and 3,
> with the exception of Article 6(5), shall apply from: **(i) 2 December 2027 as regards
> AI systems classified as high-risk pursuant to Article 6(2) and Annex III**; and
> (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article
> 6(1) and Annex I;'"*

Recital 40 gives the reason verbatim: *"the delayed availability of standards, common
specifications, and alternative guidance and the delayed establishment of national
competent authorities lead to challenges that jeopardise the effective entry into
application of those obligations and that risk a significant increase in implementation
costs in a way that does not justify maintaining their initial date of application,
namely 2 August 2026."*

**An adaptive tutor that steers learning has roughly sixteen extra months.**

### 5.2 Four things that did NOT move, and one of them is five days away

This is where a careless reading becomes a compliance failure.

1. **Article 113's *first* paragraph is unamended.** It still reads *"It shall apply from
   2 August 2026."* Only third-paragraph points (a), (c) and a new (d) were touched.
   **Anything not carved out still starts on 2 August 2026.** `VERIFIED`
2. **Chapter IV / Article 50 transparency is NOT carved out.** The Omnibus amended only
   Article 50(7) (codes of practice); 50(1)–(6) are untouched. **Chatbot-disclosure and
   synthetic-content marking obligations bite on 2 August 2026 — five days from today.**
   For any conversational tutor in the EU, *this*, not Annex III, is the live deadline.
   `VERIFIED`
   - Narrow relief only for incumbents, via new Article 111(4), verbatim: *"Providers of
     AI systems … generating synthetic audio, image, video or text content, that have
     been placed on the market before 2 August 2026 shall take the necessary steps in
     order to comply with Article 50(2) by 2 December 2026."*
3. **Annex III point 3 (education) is unamended.** The Omnibus amends Annexes I, VIII and
   adds XIV; it does not touch Annex III. **F8's substantive classification analysis —
   an adaptive tutor that steers learning falls under Annex III(3)(b) — stands
   unchanged.** Only the deadline moved. `VERIFIED`
4. **Article 4 (AI literacy) still applies** (since 2 Feb 2025), though softened:
   *"This obligation does not require providers or deployers to guarantee any specific
   level of AI literacy of any individual."* `VERIFIED`

`INFERENCE`, flagged as a derived reading and not a quoted provision: **Chapter III
Section 5** (standards, conformity assessment, registration — Arts. 40–49) is *not* in the
carve-out list, and so appears to fall under the unamended general 2 August 2026 date even
though Sections 1–3 are deferred. This looks like a drafting artefact. It wants a lawyer,
not a survey.

Also new: prohibitions on non-consensual intimate imagery and CSAM-generating systems
(Art. 5(1)(ba),(bb)) **from 2 December 2026**; a new Art. 4a lawful basis for processing
special-category data for bias detection; and national sandboxes pushed to 2 August 2027.

### 5.3 The methodological warning, which generalises

**Both of the obvious sources would have given the wrong answer today.**

- `artificialintelligenceact.eu/implementation-timeline/` — HTTP 200, still stamped
  **"Last updated: 1 August 2024"**, still states "2 August 2026 — the remainder of the
  AI Act starts to apply." Superseded.
- The **European Commission's own** `digital-strategy.ec.europa.eu/en/library/digital-omnibus`
  — HTTP 200, last updated **19 January 2026**, describes only the *proposal* of
  19 November 2025.

The reliable check was the EUR-Lex `/ALL/` view's **"Modified by" table**, which records
every amendment with its application date. D1 found the same class of failure in OpenAI's
sitemap `lastmod` timestamps. **Two independent instances in four days: convenience
aggregators are systematically stale on exactly the facts that matter most, and the
staleness is invisible because the page returns 200.** Read the consolidated law, or the
amendment table. Nothing else.

Consolidated text note: `CELEX:02024R1689-20260727` returns **404** — no consolidated
version has been published yet. The amending act must be read against the base text.

### 5.4 United States

| Item | Status | Label |
|---|---|---|
| **California SB 243 (Padilla), companion chatbots** | **ENACTED.** Chapter 677, Statutes of 2025; *"[Approved by Governor October 13, 2025.]"* Adds Bus. & Prof. Code ch. 22.6. Definition verbatim: *"'Companion chatbot' means an artificial intelligence system with a natural language interface that provides adaptive, human-like responses to user inputs and is capable of meeting a user's social needs…"* Carve-outs cover customer service, video-game bots, smart speakers — **no education carve-out.** Duties include AI disclosure (§22602(a)) and a suicide/self-harm protocol; reporting to the Office of Suicide Prevention *"Beginning July 1, 2027."* | `VERIFIED` (primary, leginfo) |
| ↳ its operative date | The bill text has **no explicit operative-date clause**; 1 Jan 2026 follows from the California default rule (Cal. Const. art. IV, §8(c)). **Stated as an inference, not retrieved.** | `INFERENCE` |
| **California AB 1064 (LEAD for Kids Act)** | **DEAD.** Bill history: *"10/13/25 Vetoed by Governor"*; *"01/22/26 Consideration of Governor's veto stricken from file."* No override. Any analysis treating AB 1064 as live is wrong. | `VERIFIED` |
| **US Dept. of Education AI priority** | *"Final Priority and Definitions—Secretary's Supplemental Priority and Definitions on Advancing Artificial Intelligence in Education,"* **91 FR 18774, published 13 April 2026, effective 13 May 2026.** Abstract verbatim: *"announces one priority and related definitions for use in currently authorized discretionary grant programs."* **A funding priority, not a vendor mandate.** | `VERIFIED` |
| ↳ and what ED refused | Commenters asked for COPPA/FERPA-based parental-consent and opt-out mandates. ED, verbatim: *"The Department believes that how best to ensure safety and communicate about technology use is optimally decided at the state and local level and declines to enact requirements at the federal level."* Recorded response: *"Changes: None."* | `VERIFIED` |
| **COPPA** | **Unchanged since F8.** Cornell 16 CFR 312 source note verbatim: *"78 FR 4008, Jan. 17, 2013, as amended at 90 FR 16977, Apr. 22, 2025."* Federal Register API, term `COPPA`, published ≥2025-06-01: **count = 1**, and that hit is the ED priority above. No COPPA rulemaking. | `VERIFIED` |
| **FERPA** | `studentprivacy.ed.gov` reachable; **no new rulemaking identified.** | `OBSERVED` |
| **State legislation volume** | NCSL: *"In the 2025 legislative session, all 50 states, Puerto Rico, the Virgin Islands, and Washington, D.C., have introduced legislation on this topic this year. Thirty-eight states adopted or enacted around 100 measures this year."* No 2026 tracker page exists (404 on three URL variants). | `SECONDARY` |
| **FTC** | *"Policy Statement Concerning the Suppression of Accuracy in Artificial Intelligence Systems,"* published **7 July 2026**. Retrieved as a Federal Register listing only; **text not fetched, content UNVERIFIED.** Flagged because an FTC accuracy policy statement three weeks old plausibly reaches tutoring-product accuracy claims. | `UNVERIFIED` |

**The net US picture, and it is a live one for anyone building a conversational tutor:**
the federal government explicitly declined to regulate, and the binding constraint moved
to the states. California SB 243's companion-chatbot definition — *"adaptive, human-like
responses"* that can *"meet a user's social needs"* and *"sustain a relationship across
multiple interactions"* — describes a persistent Socratic tutor with a persona almost
exactly, and there is no education carve-out. That is the nearest-term US exposure.

### 5.5 United Kingdom

- **Online Safety Act 2023** — legislation.gov.uk verbatim: *"Online Safety Act 2023 is up
  to date with all changes known to be in force on or before 27 July 2026."* `VERIFIED`
- **F8's Ofcom gap is only partly closed.** Ofcom's Protection of Children Codes page
  returns **HTTP 403** to both curl (browser UA) and WebFetch; the statement PDF also 403.
  F8's block reproduces exactly. **Ofcom is unreachable from this environment.**
  Workaround: the GOV.UK/DSIT collection (HTTP 200, last updated 2 March 2026) states
  verbatim: *"As of 25 July 2025, platforms have a legal duty to protect children online.
  Platforms are now required to use highly effective age assurance to prevent children
  from accessing pornography, or content which encourages self-harm, suicide or eating
  disorder content."* **The in-force date is confirmed; the Codes' own wording remains
  `UNVERIFIED`.**

---

## 6. Benchmarks and evaluation: does the "zero learning outcomes" pattern generalise?

D1 §5 concluded that no benchmark exists whose dependent variable is a human learning
outcome, and C3 found that an exhaustive arXiv listing for `"slide generation"` returned
**39 results with zero measuring whether a human learns anything.**

The brief asked whether that generalises. **It does, and here is the census.**

### 6.1 Method

For each education-AI subfield I queried the **arXiv advanced-search UI** (the API was
rate-limited throughout) for the subfield phrase, then for the subfield phrase **AND**
each of four learning-outcome markers: `"learning gain"`, `"post-test"`, `"pre-test"`,
`"randomized controlled"`. Counts are arXiv's own reported result totals. This is a
**co-occurrence census, not a full-text audit** — a paper could measure learning without
using any of these four phrases, and a paper could use a phrase without measuring
learning. It is reproducible, which is the point, and the baseline row replicates C3's
39 exactly.

### 6.2 Results

<!--CENSUS_TABLE-->

### 6.3 What the census shows

**The pattern generalises, and it is stronger than "sparse."** Across the subfields
surveyed, papers containing any learning-outcome marker are a **low-single-digit
percentage** of each literature, and several substantial subfields return **exact zeros
on all four markers**.

The zero-on-all-four subfields are the finding. `"slide generation"` (39 papers),
`"automated essay scoring"` (123 papers), `"spaced repetition"` (19), `"textbook
generation"` (4) — four literatures, one of them with over a hundred papers, in which
**not one abstract mentions a pre-test, a post-test, a learning gain, or a randomised
control.**

Automated essay scoring is the sharpest case. It is one of the oldest quantitative
subfields in education technology, it has decades of psychometric infrastructure, and its
arXiv literature optimises **agreement with human raters** — a *reliability* target. A
scorer that agrees perfectly with graders while producing feedback nobody learns from
scores 100% on every benchmark in that literature. The dependent variable is the wrong one
by construction, and the field is internally consistent about it.

`"spaced repetition"` at 19 papers with four zeros is almost comic, given that spaced
retrieval is among the best-replicated findings in all of learning science. The arXiv
literature on it is about **scheduling algorithms**, evaluated against **recall-prediction
accuracy** — again a proxy, and again one that a better algorithm can win without any
human retaining anything more.

**The mechanism behind the pattern, stated once.** These are computer-science
literatures, and CS evaluates artifacts. Measuring learning requires human subjects,
ethics approval, a delay, and a transfer test — costs that no paper-per-quarter cadence
can absorb. The result is a field that has become extremely good at improving things it
can measure in an afternoon. This is not fraud and it is not stupidity; it is a rational
response to publication economics, and it has produced a literature where **the headline
capability numbers are real and the pedagogical claims attached to them are unsupported.**

**The forward-looking version, which is the useful one.** The measurement gap is not a
reason to disbelieve the capability — the generators genuinely got better. It is a reason
to recognise that **the learning-outcome measurement is unclaimed territory**, and it is
cheap territory relative to model training. A pre-test, a delayed post-test, and a
transfer item on a few hundred learners is an afternoon of instrument design and a term of
patience. Anyone who instruments that owns the only number in their subfield.

### 6.4 What exists on the evaluation side

D1 §5 tabulated nine education benchmarks (KMP-Bench, SHAPE, SafeTutors, CSTutorBench,
TutorAccessEval, BILearn-CS, EduEVAL-DB, FATE, and the interactivity metric) and found
all nine to be proxies in three families: LLM-judge rubrics (circular), human-expert
dialogue ratings (measures pedagogical *form*, not effect), and harm rubrics (measures
absence of bad, not presence of good). **I found nothing in this sweep that changes that
assessment, and nothing new since 25 July.** D1's conclusion stands: *the missing
benchmark is one where the dependent variable is a human learning outcome.*

One addition worth logging: **AgentWorldBench** (Qwen, §1.2) scores an environment
simulator on Format, Factuality, Consistency, Realism and Quality. If simulated
environments become a learning surface — and the world-model line suggests they might —
that benchmark is the template that will get reached for, and **none of its five
dimensions is about a learner.** Better to notice that now than after it becomes the
default.

---

## 7. The honest scoreboard

The brief's question: of everything above, how much has a controlled outcome study?

### 7.1 The ERIC census

ERIC is the US Department of Education's research index — the field's own literature, not
computer science's. Its API is reachable and fast. Queried 2026-07-28:

| Query | Records |
|---|---|
| `ChatGPT AND education` | **1,565** |
| `"generative artificial intelligence" AND education` | 922 |
| `"large language model" AND education` | 110 |
| `ChatGPT AND "learning outcomes"` | 95 |
| `ChatGPT AND pretest AND posttest` | 12 |
| **`ChatGPT AND "randomized controlled trial"`** | **7** |
| **`"large language model" AND "randomized controlled trial"`** | **2** |
| **`"generative artificial intelligence" AND "randomized controlled"`** | **1** |
| `"AI tutor"` | 10 |
| **`"AI tutor" AND randomized`** | **1** |

**Roughly one in 220 ChatGPT-and-education records in ERIC involves a randomised
controlled trial.** `OBSERVED` — reproducible against a public API.

### 7.2 What the seven actually are

This matters more than the ratio, because the composition is skewed in a way nobody
mentions:

| Year | Study | Venue |
|---|---|---|
| 2023 | Can ChatGPT Support Prospective Teachers in Physics Task Development? | *Phys. Rev. PER* |
| 2024 | Empowering ChatGPT with Guidance Mechanism in Blended Learning | *IJETHE* |
| 2025 | AI-Driven Instructional Intervention on Iranian EFL Learners' Pronunciation | *Discover Education* |
| 2025 | ChatGPT-Integrated Feedback Aids in Virtual Reality (SRL + HOTS) | *Educ. & Info. Technologies* |
| 2025 | Teacher E-Feedback vs AI Feedback vs Hybrid, EFL Writing | *TLTL* |
| 2026 | NLP and EFL Speaking: Adaptability, Accuracy, Fluency | *J. Educ. Computing Research* |
| **2026** | **Enhancing School Students' Self-Regulated Learning through GenAI Support: An RCT** | ***Educational Psychology Review*** |

**Four of seven are second-language learning.** The only `"AI tutor" AND randomized` hit
is *surgical skills in medical students*. **Exactly one is K-12 school students in core
subjects** — the last row.

**Finding: the randomised evidence base for generative AI in education is concentrated in
second-language learning and higher/professional education. K-12 core-subject achievement
is close to empty.** `OBSERVED`. This is not an argument that AI doesn't work in K-12;
it is the observation that almost nobody has looked, which is a different and more
actionable thing.

### 7.3 The one 2026 K-12 RCT, and it is a null

**Fütterer, Bardach, Kuhn, Keller & Gerjets (2026), "Enhancing School Students'
Self-Regulated Learning through Generative AI Support: A Randomized Controlled Trial,"
*Educational Psychology Review*, DOI `10.1007/s10648-026-10133-8`, published 14 April
2026, CC BY 4.0.** `MEASURED-RCT`.

Design: **n = 371, Grades 7–9**, randomised to three conditions, **six 45-minute sessions
during regular physics or English lessons**. Two GenAI-supported interventions — one
targeting **motivational** (utility value), one targeting **strategic** (cognitive
learning strategies) aspects of self-regulated learning — against **a control condition
using standard ChatGPT**. Outcomes at pre- and post-test: perceived utility value,
strategy use (self-reported and tested), interest, effort, and **tested domain-specific
knowledge**.

Results, verbatim from the abstract:

> *"The results showed that students in the utility value condition reported more
> favorable development of perceived utility value than those in the cognitive strategy
> condition. **However, no statistically significant advantages of either intervention
> over the control condition were found for effort, domain-specific knowledge, or
> elaboration-based strategy use.**"*
>
> *"Exploratory analyses indicated that students who engaged more meaningfully with the
> GenAI tended to have more sustained interest than those in the control group. No
> subject-specific (physics or English) differences in intervention effects were
> observed."*

And the authors' own conclusion, verbatim: *"Findings suggest GenAI-based interventions
may help preserve motivational aspects of SRL under certain conditions, but further
development is needed to effectively support cognitive strategies and improve learning
outcomes in secondary school settings."*

**Read the control condition carefully, because it determines what this study means.**
The comparator is **plain ChatGPT**, not no-AI. So this is *not* evidence that AI fails
in classrooms. It is evidence that **a designed pedagogical scaffold, in this
implementation, bought nothing over an undesigned chatbot on tested knowledge.**

That is a direct, same-quarter tension with the field's two other anchor results, and the
three should be read together rather than picked between:

- **Bastani et al. (PNAS)** — unguarded AI vs no AI: **−17%** after removal; a
  guardrailed prompt "largely mitigated" it. The prompt layer *prevented harm*.
- **DeepMind Sierra Leone (June 2026)** — Guided Learning vs control: **+0.258 SD** maths
  (project record: unadjusted **+0.216, n.s.**). The prompt-and-product layer *added
  benefit*, in a low-resource setting with a large baseline deficit.
- **Fütterer et al. (April 2026)** — scaffolded GenAI vs plain ChatGPT: **null** on
  domain knowledge, n=371, German-context secondary classrooms.

`INFERENCE`, and I want it labelled as one because it is a synthesis and not a
measurement: these three are **consistent** under the reading that the prompt layer's
main job is *removing the harm of unrestrained answering*, and that its marginal benefit
over an already-adequate baseline is small — so the measured effect of pedagogical
scaffolding scales with **how bad the counterfactual was**. Sierra Leone's counterfactual
was very bad. A German Gymnasium's, with a teacher in the room and ChatGPT already in the
control arm, was not. This matches the project's standing correction —
*"restraint removes harm, does not add benefit"* — and this RCT is the strongest
independent support that correction has.

If it holds, it is good news pointed somewhere specific: **the returns to pedagogical
design are largest exactly where instruction is scarcest.** That is an argument for
building at the margin, and it is the same conclusion H1 reaches from a different
direction entirely.

### 7.4 Verifying the prior "exactly one open system" finding

**Verified, and sharpened.** In the self-hostable open-source sweep (§4), the only system
with a peer-reviewed **controlled** evaluation is **OATutor** (CAHLR/Berkeley; Pardos,
Tang, Anastasopoulos, Sheel & Zhang) — CHI 2023 `10.1145/3544548.3581574`, plus L@S 2023
`10.1145/3573051.3593399`. Crossref returns no abstract, so I can confirm *a peer-reviewed
controlled evaluation exists* but **cannot confirm RCT design from API data alone**:
label `MEASURED, design unconfirmed`.

The comparison that makes the point: **OATutor has 231 GitHub stars. Mr.-Ranedeer-AI-Tutor
has 29,607** (§4.2 item 4) and is an unlicensed prompt document. **The one system with
evidence has 0.8% of the attention of the one with none.** `OBSERVED`.

Corroborating nulls from the same sweep:

- **ERIC `Kolibri`: 2 records total.** One (Kabugo 2020, *J. Learning for Development*) is
  a discourse analysis of usage logs and interviews, 25 teachers and 100 students, **no
  control group**; the other a 2024 Colombia OER co-creation paper. **Neither is an RCT.**
  Crossref adds two funder-commissioned OpenDevEd reports (`10.53832/opendeved.0202`,
  `10.53832/opendeved.0270`) — grey literature, `type: report`, not RCTs.
- **ERIC `Oppia`: 0 records.**
- Learning Equality's site claims *"statistically significant improvements in foundational
  literacy and numeracy and social-emotional learning"* and *"up to 97% re-enrollment"*
  with **no study named, no n, no design, no link** — `VENDOR`, and not restated here as a
  finding. It also claims *"Installed in 220+ countries and territories"*, which exceeds
  the number of countries that exist; that is a download-geography count, not a
  deployment count.
- **Nothing in the self-hostable AI-tutoring category has a learning-outcome study. Not
  one repository.**

### 7.5 The scoreboard

Everything in this report with a controlled outcome study, and everything without.

| Item | Controlled outcome study? | Label |
|---|---|---|
| DeepMind Guided Learning (Sierra Leone) | **Yes** — pre-registered RCT, n=1,763 | `MEASURED-RCT` |
| Fütterer et al. GenAI SRL scaffold | **Yes — and null on knowledge**, n=371 | `MEASURED-RCT` |
| Curipod | **Yes, one** (`10.1016/j.teln.2025.11.032`) — nursing students, survey outcomes, active-vs-passive control | `MEASURED-RCT`, wrong population |
| Squirrel AI | **Yes, one** (`10.1080/10494820.2020.1808794`) — not vendor-independent, and **the vendor cites it nowhere** | `MEASURED` |
| Duolingo | Pre/post, self-selected, no randomised control, vendor-authored | `MEASURED` (weak) |
| OATutor (open source) | Peer-reviewed controlled eval; **design unconfirmed** | `MEASURED`, unconfirmed |
| Khanmigo | **No.** Vendor states v1 did not move learning as hoped | `OBSERVED` (null, against interest) |
| MagicSchool | **No.** Claim unattributable; 153-URL sitemap has no research page | `VENDOR` |
| Brisk · Diffit · Synthesis · Coursera · Udacity · SchoolAI | **No.** Usage, time-saved, or self-report only | `VENDOR` |
| OpenAI Study Mode · ChatGPT for Teachers | **No.** Appeals to background literature | `VENDOR` |
| Anthropic Learning Mode · Claude for Teachers | **No.** Partner logos are not evidence | `VENDOR` |
| Google Guided Learning (as a product page) | **No** product-level study; the RCT is the Sierra Leone deployment | `VENDOR` |
| Kolibri · Moodle · Open edX · Oppia · every self-hostable LLM tutor | **No** | `OBSERVED` (absence) |

**Count: two rigorous randomised trials in the current period, and one of them is a
null.** Two further controlled studies exist attached to commercial products, and in both
cases the population or the independence is compromised, and in one case the vendor does
not cite its own evidence.

---

## 8. Negative and null results, collected

The editorial standard requires ≥1 per section; the brief asked for ≥3. There are twelve.

1. **Fütterer et al. 2026** — *"no statistically significant advantages of either
   intervention over the control condition … for effort, domain-specific knowledge, or
   elaboration-based strategy use."* n=371, Grades 7–9. `MEASURED-RCT`
2. **Khan Academy on Khanmigo v1** — *"did not change student learning as much as many of
   us hoped it would."* Vendor statement against interest, 17 July 2026. `OBSERVED`
3. **MagicSchool's 28% literacy claim is unattributable.** Five candidate URLs 404; full
   153-URL sitemap contains no research page; the figure is bare homepage text.
4. **Two of Curipod's five "Independent Research" items do not resolve** to any
   publication via Crossref or ERIC, and carry no outbound link.
5. **Meta has published no open-weight model in ~15 months** (nothing since 2025-04-28).
6. **`huggingface/text-generation-inference` is ARCHIVED**; **`rhasspy/piper` is
   ARCHIVED**; **`coqui-ai/TTS` is 2.4 years stale while reporting `archived: false`.**
7. **Open full-duplex speech is dead in the water** — Moshi's latest release is dated
   2024-09-22. The pedagogically decisive capability has no open implementation.
8. **Voxtral Realtime is not full-duplex.** Widely assumed otherwise; its own card says
   streaming ASR. Speech in, text out.
9. **arXiv census: four education-AI subfields return zero on all four learning-outcome
   markers**, including automated essay scoring at 123 papers.
10. **ERIC: 7 RCTs against 1,565 ChatGPT-education records (~0.45%)**, and four of the
    seven are second-language learning.
11. **ERIC `Kolibri` = 2 records, neither an RCT; ERIC `Oppia` = 0.** No self-hostable
    AI-tutoring component has a learning-outcome study.
12. **Riiid's research identity was deleted in its corporate transition** — EdNet and all
    publications are gone from the successor's site.

And one negative about the *market*: **Chegg's Academic Services revenue fell 57% in
twelve months** (§3.1). Whatever else generative AI has or has not done for learning, it
has demonstrably ended a business model — the answer-vending one — on an audited P&L.

---

## 9. Could not verify — stated, not guessed

| Item | Status |
|---|---|
| **arXiv API** (`export.arxiv.org`) | Sustained **HTTP 429** across the session. All arXiv counts come from the **advanced-search UI**. Recall-limited by construction. |
| **Semantic Scholar API** | **HTTP 429** throughout. Not used. |
| **OpenAlex complex boolean filters** | `title_and_abstract.search` with parenthesised OR groups returned nulls. Simple queries work; the complementary OpenAlex census was **abandoned** in favour of ERIC. Simple-query counts only. |
| **DeepSeek V4 maths/coding benchmarks** | Still unverified — arXiv:2606.19348's visible content carries no AIME/MATH/GPQA figures. D1's caution stands. |
| **Ofcom Protection of Children Codes** | **HTTP 403** to curl (browser UA) and WebFetch; statement PDF also 403. F8's block reproduces exactly. In-force date confirmed via GOV.UK; **the Codes' text remains unread.** |
| **FTC "Suppression of Accuracy in AI Systems" policy statement (7 July 2026)** | Retrieved as a Federal Register **listing only**; text not fetched. Content unverified. |
| **openai.com** | **HTTP 403** (Cloudflare) to both curl and WebFetch; WebFetch additionally blocked from web.archive.org. OpenAI content retrieved by curling Wayback snapshots. |
| **Coursera investor relations** | `investor.coursera.com` **403**. No 2026 learner or revenue figures obtainable. |
| **Duolingo `/efficacy`** | HTTP 200 with **zero body content** (SPA shell); `/nojs/efficacy` **404**. Efficacy studies located offsite instead. |
| **Google Guided Learning canonical page** | `gemini.google/overview/guided-learning/` **404**; `blog.google/products/gemini/guided-learning/` **404**. E1's 404 confirmed and generalised — **no canonical page exists.** |
| **Khan Academy "three-year Newark efficacy study"** | Cited with no numbers, no design, no link; does not resolve via Crossref. |
| **Squirrel AI's claimed RCTs** | `/research` **404**; site cites zero studies. The real study was found independently. Harvard/CMU/Stanford/SRI are named without citations. |
| **Fütterer et al. full text** | Springer requires auth (303 to `idp.springer.com`). All quotes are from the **Crossref-deposited abstract**, which is complete. Effect sizes beyond "no statistically significant advantages" **not retrieved**. |
| **OATutor design** | Peer-reviewed controlled evaluation confirmed to exist; **RCT design not confirmable from API metadata.** |
| **AI Act consolidated text** | `CELEX:02024R1689-20260727` **404** — not yet published. Amending act read against base text. |
| **California SB 243 operative date** | 1 Jan 2026 is an **inference** from the constitutional default rule; no source stating it was retrieved. |
| **Market-level edtech funding aggregate** | Not retrievable (E1's HolonIQ 404 reproduced). **This report carries no total-market funding figure.** Deliberate. |
| **`gemma-4` hardware/concurrency claims** | Inferred from parameter counts and quantisation formats. **Not benchmarked.** |
| **Synthesis Form C-TR rationale** | The filing states **no reason** for terminating Reg CF reporting. Dissolution, acquisition, going-private and threshold changes are all consistent with it. **No cause asserted.** |

---

## 10. What E3 hands to the survey

1. **§5.1 — the AI Act deferral to 2 December 2027**, verified against EUR-Lex, together
   with §5.2's warning that **Article 50 transparency still applies from 2 August 2026**.
   This supersedes F8's flagged unknown and must be corrected wherever F8's date appears.
2. **§5.3 — the stale-aggregator failure mode.** Two independent instances in four days
   (OpenAI sitemaps in D1, the AI Act timeline and the Commission's own library page
   here). A standing methodological rule: for any date that carries a consequence, read
   the primary record's amendment table.
3. **§7.3 — the three-result synthesis.** Bastani (harm removed), Sierra Leone (benefit
   added, weak counterfactual), Fütterer (null against a strong counterfactual) are
   consistent, and together they say the returns to pedagogical design scale with how bad
   the alternative was. This is the survey's sharpest available statement about *where*
   to build, and it is independent support for the project's standing correction.
4. **§6 — the census and its method.** The "zero learning outcomes" pattern generalises
   beyond slide generation; four subfields return exact zeros. The method is a dozen
   lines of Python against a public search UI and should be re-run before publication.
5. **§2.1 — Khanmigo's null and its diagnosis.** A correct mechanism defeated by
   invocation friction. The design lesson (remove the metacognitive prerequisite; put the
   tutor *inside* the task) is the most transferable thing in this report.
6. **§3.1 and §3.3 — the audited numbers.** Chegg's −48%/−57% and Synthesis's
   +6.5%/−53% are the only non-vendor financial facts available about this sector, and
   both contradict the marketing that sits on top of them.
7. **§4 — the buildable local stack, with its four honest gaps** (no full-duplex, no
   safety layer, no SSO, **no glue between the LMS and the model**). The last gap is a
   concrete, unclaimed, high-value open-source project.
8. **§7.4 — OATutor at 231 stars vs Mr. Ranedeer at 29,607.** The attention gradient in
   this field runs opposite to the evidence gradient, which is E1's Finding E1-a
   reappearing in open source, where there is no funding to blame it on.

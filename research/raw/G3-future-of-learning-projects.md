---
title: "The Future of Learning as a Built Artifact — Mapping the Occupied, Contested, and Unclaimed Ground"
wave: G
date_researched: 2026-07-27
sources_count: 102
---

# G3 · The Future of Learning as a Built Artifact

> **Deliverable of this section:** a **design-space map**. Not a literature review — a registry of
> things that *exist and can be inspected*, each graded on the same six axes, followed by a
> three-way partition of the space into **occupied** (redoing it is waste), **contested**
> (credible people disagree about mechanism), and **empty** (nobody has built it). §7 tests the
> survey's own claim about what is unclaimed and **partially refutes it**.

---

## 0. Method, and the one rule that governs this section

Every other section of this survey asks *what is true*. This section asks a narrower and more
brutal question: **what exists as an artifact you can clone, run, read, or buy — and what does it
actually do when you do that?**

That distinction matters because the "future of learning with AI" genre has an unusually high
ratio of manifesto to mechanism. A README is not a book. A syllabus is not a course. A blog post
announcing an AI-native school is not an AI-native school. The discipline of this section is:

**Rule G3-1.** *No artifact is characterised from its own description. It is characterised from
its contents — files read, code executed, output diffed. Where I could only reach the description,
the row says so.*

Applying that rule produced the single most consequential finding in this section, which is worth
stating before any of the evidence: **the AI-learning field has built an enormous amount of
author-side infrastructure and almost no learner-side infrastructure.** The agentic skills, the
memory files, the spec-driven pipelines, the eval harnesses — they are pointed at the *production
of the book*, not at the *state of the reader*. §7 develops this; §1 shows it in miniature.

### Evidence labels used throughout

| Label | Meaning |
|---|---|
| **MEASURED-RCT** | Randomised trial with a control condition |
| **MEASURED-META** | Meta-analysis or systematic review |
| **MEASURED-BENCH** | A benchmark/test suite result, or a measurement I performed |
| **OBSERVED** | I read the primary artifact — file contents, repo tree, API response |
| **VENDOR** | The project's own marketing or self-description. **Never restated as a finding.** |
| **DEMO** | A demonstration exists; no controlled evidence |
| **INFERENCE** | My deduction from observed facts, labelled as mine |
| **UNREACHABLE** | Could not be verified through available channels; not guessed at |

Efficacy evidence for AI tutoring generally is **not** re-derived here — that is B2's job, and B2's
corpus (Bastani et al. PNAS 2025, Tutor CoPilot, Kestin et al., the Gemini/Sierra Leone RCT) is the
authority. G3 cites B2 where an artifact's claims need grading against it.

---

## 1. The primary target: `xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning`

**URL:** https://github.com/xiaol/Harnessing-LLM-Skills-to-Master-Machine-Learning
**Form:** mdBook manuscript + skill library + runnable example pack + video-production workspace.

This repository was named explicitly as the artifact to analyse. I cloned it, read the manuscript
source, executed every script in it, and diffed the results against its committed outputs. What
follows is from the contents, not the README.

### 1.1 Provenance — the fact that reframes everything else

**[OBSERVED]** `git log` on the repository shows **two commits, total**:

```
c235b27 | 2026-04-25 18:59:13 +0800 | Xiaol | Refine release description
886c41f | 2026-04-25 18:21:23 +0800 | Xiaol | Initial publish of ML course book and skills
```

Thirty-eight minutes apart. Repository created `2026-04-25T10:08:27Z`, last push
`2026-04-25T10:59:23Z` (API). **The entire artifact — 20 chapters, ~57,000 words of manuscript,
23 skill definitions, 16 runnable example projects, 20 chapters of video-production assets — was
published in a single session and has not been touched since.** As of 2026-07-27 that is three
months of no activity.

**[OBSERVED]** Social signal is nil: **0 stars, 0 forks, 0 watchers, 0 open issues, 0 network
members, no license file.**

**[OBSERVED]** `book.toml` names the author:

```toml
authors = ["OpenAI Codex with Xiaol"]
```

The artifact is explicit that a model is the first author. This is unusual and, to its credit,
honest. But it means the correct reference class is not "a book about AI-native learning"; it is
**"the first single-shot, model-authored, complete technical curriculum I have been able to
inspect end to end."** That is genuinely interesting, and it is a different thing from what the
README claims to be.

### 1.2 The pedagogical model, stated in its own words

The book's thesis is **harness engineering**. `OUTLINE.md` **[OBSERVED]**:

> "This book teaches machine learning as an AI-native engineering discipline in which learners do
> not merely use AI tools, but learn to build and operate harnesses, skills, and evaluation loops
> that make learning and production work reliable."

And the vocabulary ladder, which is the book's actual conceptual contribution
(`OUTLINE.md`, restated in `preface.md`) **[OBSERVED]**:

> - `prompting`: ask once
> - `workflow`: repeat the steps manually
> - `skill`: package the workflow so it can be reused
> - `harness engineering`: design the whole system so the skill works reliably under constraints

The claimed learning mechanism is a six-step reader loop, from
`src/how-to-use-reader-skills.md` **[OBSERVED]**, quoted in full because it is the load-bearing
specification:

> 1. Read the chapter until you can state the main judgment in your own words.
> 2. Work through the chapter's `Case Study to Work Through` section so you have one concrete object in mind.
> 3. Choose the matching reader skill from [Appendix B. Reader Skill Catalog](appendix-b.md).
> 4. Run that skill on the chapter case, the runnable example, or one of your own problems.
> 5. **Compare the skill output with your own reasoning instead of accepting it blindly.**
> 6. Use the chapter's `Skill Sink-In` section to decide what artifact you should save next.

And the persistence instruction:

> After each run, save a small artifact with: the original task or case · the skill you used · the
> output you accepted · **the output you rejected or revised** · the next experiment or follow-up
> question. This turns AI help into accumulated engineering judgment instead of disposable chat
> history.

### 1.3 Is this LLM-skills-as-learning-mechanism, or LLM-as-writing-tool? — Both, and the split is the finding

The honest answer is **both, in different layers, and the layers are not equally developed.**

**As a writing tool: heavily, and it left fingerprints.** `BOOK_SUMMARY.md` is described in its own
first line **[OBSERVED]** as:

> "Use this file as compressed context when drafting future chapters or revising the manuscript."

Every chapter also ships a `refs.md` containing author-facing sections titled `Concepts That Must
Stay Stable`, `Possible Figures to Add Later`, and `Reminders for Future Revision` — e.g.
`src/chapter-04/refs.md` **[OBSERVED]**:

> "- keep the runnable delivery example central
> - add one very small code example for logistic regression later
> - include one table comparing the three first-model families"

**As a learning mechanism: genuinely, and this is the real novelty.** The 23 skills in `skills/`
are not prose about skills — they are actual Codex/Claude-format `SKILL.md` files with YAML
frontmatter, invocable as `$ml-baseline-builder`, shipped *inside the book repo* so the reader can
read the workflow. Each has a `Workflow`, an `Output Format`, and — the strongest design element in
the artifact — a `Quality Bar`. From `skills/ml-baseline-builder/SKILL.md` **[OBSERVED]**:

> ## Quality Bar
> - Do not recommend complexity before a naive and interpretable baseline exist.
> - Keep the comparison on the same split and metric.
> - Name at least one slice where the baselines may fail differently.
> - Treat simple models as instruments for understanding, not as embarrassment.

That is a *constraint on the generator*, authored by the curriculum, travelling with the book. It
is a small but real answer to "how do you stop the tutor from being agreeable slop," and it is more
mechanism than most trade books on this topic contain.

**[INFERENCE]** So the correct characterisation is: **this book's contribution is to treat the
prompt-scaffold as a curricular object with version-controlled quality criteria, rather than as
disposable chat.** That is a defensible, novel, small idea. It is not the idea the README claims,
which is much larger.

### 1.4 Executability audit — I ran it **[MEASURED-BENCH]**

This is where the artifact does best, and where the result is genuinely surprising.

**Test performed:** cloned at `c235b27`, ran `scripts/run-example-cases.sh`, then ran each of the 16
example scripts individually and byte-diffed stdout against the `artifacts/run-output.txt` file
committed alongside it.

| Measurement | Result |
|---|---|
| Example projects | **16** |
| Total Python LOC in examples | **1,940** |
| External dependencies | **numpy in 2 of 16; the other 14 are Python-stdlib-only** (`csv`, `math`, `statistics`, `pathlib`, `collections`, `json`, `re`) |
| Exit code of full run | **0** |
| Wall-clock, all 16 | **0.555 s** on Python 3.12.3 |
| **Committed outputs reproduced byte-identically** | **16 / 16 (100%)** |
| Test files (`test_*.py`, `conftest.py`, `pytest.ini`) | **0** |
| CI configuration (`.github/`) | **0** |
| Dataset sizes | 3–84 data rows (median ≈ 6) |

Put that 100% next to F3 §3.1's finding that **published Jupyter notebooks reproduce their own
stated results 4.03% of the time**. This artifact beat that by two orders of magnitude — and it did
so with no clever infrastructure whatsoever. **[INFERENCE]** The mechanism is pure subtraction:
*no external dependencies, no randomness, no network, no GPU, no data download, tiny deterministic
inputs, plain-text committed outputs.* The lesson generalises and §8 promotes it to a rule.

There are two large caveats, and they are the difference between *reproducible* and *verifiable*:

1. **[OBSERVED]** There are no assertions. `run-example-cases.sh` runs scripts and prints; nothing
   *fails*. Reproducibility here is a property I established by diffing from outside. The artifact
   does not check itself, and a reader who breaks something gets no signal.
2. **[OBSERVED]** The datasets are 3–84 rows. `delivery_time_data.csv` has 20 data rows split
   14 train / 6 test. The book fits a 5-feature linear regression on 14 rows and then interprets
   the coefficient signs in prose (§4.4). It does flag this — "the sample may be too small for
   stable coefficient interpretation" — but it flags it *after* spending a page reading meaning
   into the weights.

**Executable in the browser: no. [MEASURED-BENCH]** I grepped the built HTML in `book/`. mdBook's
`playground` feature only executes **Rust**, and only by POSTing to the remote Rust Playground API;
there is no run button, no Pyodide, no WASM. The published book is static HTML.

**[OBSERVED] A genuinely good property nobody advertises:** `scripts/generate_chapter4_figures.py`
opens `examples/delivery-time-prediction/data/delivery_time_data.csv` and plots from it with
matplotlib (8 of 13 figure scripts use matplotlib). **The figures are generated from the same data
the scripts run on.** The dataset diagram, the MAE comparison, and the fitted-coefficient panel are
therefore not illustrations of the argument — they are renderings of it. That closes a loop most
textbooks leave open, and it is the second thing worth stealing.

### 1.5 The prose–code gap **[MEASURED-BENCH]**

Counting fenced code blocks by language across all 72 manuscript markdown files:

| Fence language | Count |
|---|---|
| ` ```text ` (prompt scaffolds) | **64** |
| ` ```bash ` | 18 |
| ` ```python ` | **3** |

**A ~57,000-word machine-learning course contains three Python code blocks and sixty-four prompt
templates.** The single code block in Chapter 4 is one line:

```python
pred = sum(w * xi for w, xi in zip(weights, x)) + bias
```

followed by the sentence "That line is not separate from the math. It is the math." — which is a
good sentence attached to almost no code. All real code lives in `examples/`, referenced by
filesystem path. **[INFERENCE]** This is the structural signature of a book *about* the harness
rather than a book *made of* one: the prose teaches judgment vocabulary and delegates all
verifiable content to a directory the reader is told to visit.

### 1.6 What it does not do, measured

| Claimed / implied | Evidence in artifact |
|---|---|
| "Adaptive learning systems with memory" (OUTLINE, "Bold Guesses") | **[OBSERVED]** `adaptive` appears in 2 files, `personaliz*` in 1, `spaced repetition` in **0**. Zero adaptive machinery exists. |
| Four-level "Reader Ladder" (Beginner→Builder→Engineer→Specialist) | **[OBSERVED]** Declared in `OUTLINE.md` and `BOOK_SUMMARY.md`. **The manuscript never branches on it.** Chapters 13, 14, 15 mention "beginner" zero times. Every reader gets identical text. The ladder is an author's plan, not a reader's path. |
| Assessment | **[OBSERVED]** `quiz`: 0 files. `answer key`: 0. `self-test`: 0. `rubric`: 1. "Extension Exercises" are 5 ungraded prose prompts per chapter with **no solutions, no tests, no keys**. Nothing can mark anything. |
| Personalisation | **[OBSERVED]** None. |
| Persistent learner state | **[OBSERVED]** The reader is told to "save a small artifact" — by hand, to their own filesystem, in a format the book does not specify and nothing reads back. |
| Evidence for its pedagogical claims | **[OBSERVED]** `bibliography.md` is 20 entries: Bishop, Murphy, ESL, ISL, Goodfellow, Prince, D2L, Huyen, Burkov, Sutton & Barto, Sculley et al., plus Adam/ResNet/Transformer/BERT. **No URLs, no DOIs, no page numbers, no dates on several, and not one citation to learning science, education research, or any evaluation of AI tutoring.** Chapter `refs.md` files cite things like "Source Spine: introductory statistical learning material" — a gesture at a source, not a source. |

The five "Bold Bets" in the preface (adaptive memory-rich education; skills as educational
infrastructure; portfolios showing harnesses; the learner/engineer line blurring; harness
engineering as the differentiator) are **[VENDOR]** in the strict sense: assertions by the artifact
about its own domain, with zero supporting evidence, and they may not be restated as findings.

### 1.7 The tell — and it is the thesis of this whole section

Line these two facts up:

- **[OBSERVED]** The artifact ships `BOOK_SUMMARY.md`, explicitly a *compressed memory file so that
  future authoring sessions stay coherent*, plus 20 per-chapter `Reminders for Future Revision`
  blocks.
- **[OBSERVED]** The artifact ships **no persistence mechanism of any kind for the learner.**

**The authoring agent gets memory. The reader does not.** The one component that would matter most
to a learner — durable state across sessions — was built, correctly and deliberately, *and pointed
at the machine writing the book instead of the human reading it.*

**[INFERENCE]** This is not an oversight peculiar to one repo. §3.2 and §4 show the same inversion
across the entire genre, including the highest-starred artifacts in it. It is the field's
characteristic blind spot, and it is the single strongest support for the survey's claim about
unclaimed ground (§7.1).

### 1.8 Grade

| Axis | Verdict |
|---|---|
| Pedagogical mechanism claimed | Reader builds and reuses versioned skill-scaffolds; compares AI output to own reasoning; saves judgment artifacts |
| Executable | **Yes, out-of-band** — 16 scripts, 100% reproducible, 0.55 s, near-zero deps. **Not in-browser, not asserted, not tested.** |
| Verifiable | **No.** Nothing can fail. The learner is the only grader, and the loop's step 5 asks the learner to out-reason the model that wrote the book. |
| Personalises | **No** |
| Assesses | **No** |
| Evidence offered | **None** |
| Demonstrably solves | (a) Reproducible-by-subtraction executable examples; (b) data-generated figures; (c) skill-as-curricular-object with an explicit Quality Bar; (d) honest AI-authorship disclosure |
| Asserts without support | Adaptivity, memory, the four-level ladder, "harness engineering will become a differentiator," and every claim in "Five Bold Bets" |

**Bottom line.** As a demonstration that a frontier model can produce a coherent, internally
consistent, fully-reproducible 57k-word technical curriculum with a working example pack in one
sitting, it is a striking **[DEMO]** and worth citing as exactly that. As a design for how a human
learns, it is a **static book with a prompt appendix**, and the gap between the two is the space
this survey is written into.

---

## 2. The Karpathy axis — the most-cited competing architecture, and what is actually in it

Eureka Labs' "teacher + AI TA" is the architecture most often invoked when people say "AI-native
school." It deserves a precise reading, because the citation traffic vastly exceeds the artifact.

### 2.1 Eureka Labs' actual specification **[VENDOR — quoted, not endorsed]**

From https://eurekalabs.ai/ (page dated 2024-07-16; `/blog` returns **404 — UNREACHABLE, it does
not exist**):

> "We are Eureka Labs and we are building a new kind of school that is AI native."

The mechanism, verbatim — this is the whole of it:

> "the teacher still designs the course materials, but they are supported, leveraged and scaled
> with an AI Teaching Assistant who is optimized to help guide the students through them."

And the aspiration, by analogy:

> [like] "Feynman, who is there to guide you every step of the way."

**[OBSERVED]** That is the complete public specification. There is no statement of what the AI TA
grades, what it has access to, what it refuses to do, how it models the student, whether it
persists anything, or how it is evaluated. "Optimized to help guide" is the entire mechanism claim.

**[INFERENCE]** The architecture's real content is a *division of labour* claim — human authors the
curriculum, AI scales the guidance — and its real force is negative: it is an argument that
**LLM-tutor-alone is insufficient**, that a designed course must exist for the TA to assist with.
That negative claim is correct and is directly corroborated by B2's corpus (Bastani et al.'s −17%
unassisted-exam effect for unguarded GPT-4 is exactly what "AI without a designed course" produces).
The positive claim — that a TA "optimized to guide" is the missing piece — remains **entirely
unspecified and unevaluated**, two years after publication.

### 2.2 LLM101n — vaporware, by its own admission **[OBSERVED]**

- `karpathy/LLM101n`: **37,504 stars, 2,064 forks, archived: true**, created 2024-05-27, last push
  **2024-08-01**. Contributors: 1.
- **Total commit history: three commits.** Total repo contents: **two files** — `README.md` and
  `llm101n.jpg`. No chapters, no code, no notebooks, no exercises.
- The README's own banner, verbatim:

> **!!! NOTE: this course does not yet exist. It is current being developed by [Eureka Labs](https://eurekalabs.ai). Until it is ready I am archiving this repo !!!**

The 17-chapter syllabus is real and well-designed (Bigram → Micrograd → N-gram → Attention →
Transformer → Tokenization → Optimization → Device/Precision/Distributed → Datasets → kv-cache →
Quantization → SFT → RL → Deployment → Multimodal). **Not one chapter has a page of content.**
As of 2026-07-27 the repo has been frozen for **just under two years**.

**37,504 stars for an empty repository** is the most efficient possible demonstration of this
section's core problem: in this field, *the promise is the artifact*, and it accumulates social
proof at a rate uncoupled from delivery.

### 2.3 The Eureka Labs graveyard-within-the-graveyard **[OBSERVED]**

- `gh api orgs/EurekaLabsAI` returns **`public_repos: 0`**, org created 2024-07-08, `updated_at`
  2024-07-09.
- But surviving third-party mirrors prove they *did* ship two chapter modules in July 2024 before
  the public repos disappeared: `EurekaLabsAI/ngram` (working Python + C char-level n-gram LM,
  32,032-name SSA dataset, train/val/test split, reproducible logs) and `EurekaLabsAI/tensor`
  (C + Python 1-D tensor with a pytest suite).
- The `ngram` README's own TODO list, verbatim: **`"- Make better / - Make exercises / - Call for
  help: nice visualization / webapp..."`**

**The exercises were explicitly planned and never made** — in a repo shipped by the organisation
whose entire thesis is pedagogy. **[INFERENCE]** The code was the easy part and got done in two
weeks. The pedagogy was the hard part and never got done. That ordering recurs everywhere in this
section.

### 2.4 nanochat — a superb artifact that is not a course **[OBSERVED]**

- `karpathy/nanochat`: **56,693 stars, 7,847 forks, 441 commits, 51 contributors**, created
  2025-10-13, last push 2026-07-04. Actively developed.
- **[VENDOR]** README: *"you can train your own GPT-2 capability LLM (which cost ~$43,000 to train
  in 2019) for only $48 (~2 hours of 8XH100 GPU node)... On a spot instance, the total cost can be
  closer to ~$15."*
- **[OBSERVED]** The README carries a live **"Time-to-GPT-2 Leaderboard"** — six dated entries from
  2026-01-29 to 2026-03-14, wall-clock falling 3.04 h → 1.65 h, each row carrying a commit hash and
  a named contributor.
- **[OBSERVED]** Pedagogical structure: **none.** No exercises, no checkpoints, no assessment, no
  lessons. `tests/` contains unit tests *of the code* (`test_engine.py`, `test_tokenizer.py`), not
  tests of the learner.
- **[VENDOR]** Scope disclaimer: *"nanochat is not an exhaustively configurable LLM 'framework'...
  It is a single, cohesive, minimal, readable, hackable, maximally-forkable 'strong baseline'
  codebase."*
- **[OBSERVED]** Its AI policy is itself a pedagogical artifact worth noting: *"When submitting a
  PR, please declare any parts that had substantial LLM contribution and that you have not written
  or that you do not fully understand."* — an **understanding**-based, not authorship-based,
  disclosure rule.

**[INFERENCE]** The leaderboard is the interesting part. It is an **assessment mechanism that
nobody calls one**: a public, reproducible, adversarially-checkable benchmark with a fixed target
("GPT-2 capability") and a single scalar (wall-clock). It grades the *artifact*, not the person —
but it is the closest thing in the Karpathy corpus to a working evaluation loop, and it emerged
from the community rather than from the pedagogy.

### 2.5 The rest of the corpus **[OBSERVED]**

| Repo | Stars | Last push | Archived | Learner exercises? |
|---|---:|---|---|---|
| `nn-zero-to-hero` | 23,706 | 2024-08-18 | No | **Yes** — the only one. "Every lecture also has a set of exercises included in the video description"; Lecture 5: "I recommend you work through the exercise yourself... The exercise is here as a Google Colab" |
| `nanoGPT` | 61,572 | 2025-11-12 | No | No — **self-deprecated** (below) |
| `llm.c` | 30,648 | 2025-06-26 | No | No (one `doc/layernorm` walkthrough; `make test_gpt2` is a code test) |
| `micrograd` | 16,867 | 2024-08-08 | No | No (pytest correctness tests only) |
| `build-nanogpt` | 5,391 | 2024-08-13 | No | No — git history + video is the structure. **Its `## FAQ` header has been empty for ~2 years.** |
| `minGPT` | 24,736 | 2024-08-15 | No | No |

**[OBSERVED]** `nanoGPT`'s README banner, "Update Nov 2025": *"nanoGPT has a new and improved cousin
called nanochat... nanoGPT (this repo) is now very old and deprecated but I will leave it up for
posterity."*

**[OBSERVED]** `nn-zero-to-hero`'s README has read *"(This may grow into something more
respectable.)"* and ended with *"Ongoing..."* since 2022 — four years unresolved.

### 2.6 What the Karpathy axis demonstrably solves, and what it does not

**Solves [OBSERVED/DEMO]:** *from-scratch reconstruction as a curriculum spine.* The lineage
micrograd → nanoGPT → build-nanogpt → llm.c → nanochat is the field's best-executed instance of
"What I cannot create, I do not understand" (the Feynman line LLM101n opens with). It is genuinely
hard to do, it has been done six times, and the community adoption (61k + 56k + 37k + 30k + 24k
stars) is real. **Rebuilding this is waste.**

**Does not solve:** anything about the learner. No assessment of a person, no model of a person, no
adaptation to a person, no memory of a person. **[INFERENCE]** The pedagogy in this corpus is
carried almost entirely by *video* (`nn-zero-to-hero`) and by *reading the git history*
(`build-nanogpt`) — both of which are one-way media that the repos merely host.

**A note on the "verifiability" thread.** Karpathy's Nov 2025 essay *Verifiability* argues
**[OBSERVED, quoted]**: *"Software 1.0 easily automates what you can specify. Software 2.0 easily
automates what you can verify"* — and that "the more a task/job is verifiable, the more amenable it
is to automation." I checked: **the essay contains no passage about education, learning, or
tutoring.** The obvious corollary — that *verifiable* learning artifacts will survive and
*specifiable-only* ones will not — is mine, not his, and is labelled **[INFERENCE]**. His current
blog (bearblog.dev, started March 2025) contains **no post about Eureka Labs, LLM101n, or AI-native
schools** at all.

---

## 3. The course-repo axis — where assessment actually got built

### 3.1 Stanford CS336 — the strongest assessment mechanism found in this entire section **[OBSERVED]**

`stanford-cs336/assignment1-basics` (2,466★, last push 2026-04-07) README, verbatim:

> ### Run unit tests
> ```sh
> uv run pytest
> ```
> Initially, all tests should fail with `NotImplementedError`s. To connect your implementation to
> the tests, complete the functions in `./tests/adapters.py`.

**[OBSERVED]** The tests exist and are real: `tests/test_model.py`, `test_optimizer.py`,
`test_nn_utils.py`, `test_data.py`, `conftest.py`, plus an `adapters.py` indirection layer — and,
critically, **numeric reference snapshots** (`tests/_snapshots/test_rope.npz`,
`test_transformer_lm.npz`, `test_adamw.npz`). The student implements RoPE, RMSNorm, SwiGLU, and
multi-head attention from scratch; each component is checked *numerically against a reference
implementation*, not against a description of one.

Org state: `lectures` 3,536★ (2026-05-28), `assignment1-basics` 2,466★, `assignment2-systems` 283★,
`assignment3-scaling` 85★, `assignment4-data` 70★, `assignment5-alignment` 188★, plus a separate
`assignment1-basics-leaderboard` (44★). Actively taught across multiple years.

**[INFERENCE]** This is the design worth copying and the one the AI-book genre has ignored. The
`adapters.py` pattern is the key move: it decouples *the student's architecture* from *the grader's
interface*, so the test suite can be strict about behaviour while staying agnostic about design.
That is how you get a checker that can say **no** without dictating the answer — precisely the
property F3 §8 demands and precisely the property every artifact in §1 and §2 lacks.

### 3.2 Sebastian Raschka — `rasbt/LLMs-from-scratch` **[OBSERVED]**

**99,909★, 15,356 forks**, created 2023-07-23, **pushed 2026-07-27 (same day as this research)**,
only **2 open issues**. The most actively maintained artifact in this section.

- Structure: Ch01–Ch07 + Appendices A–E; each chapter ships `chXX.ipynb` **plus a dedicated
  `exercise-solutions.ipynb`.**
- **[VENDOR]** README: *"Each chapter of the book includes several exercises. The solutions are
  summarized in Appendix C... you can download a free 170-page PDF titled 'Test Yourself On Build a
  Large Language Model (From Scratch)'... It contains approximately 30 quiz questions and solutions
  per chapter."*
- **[OBSERVED]** CI badges for Linux/Windows/macOS — GitHub Actions test suites run on every push.

**[INFERENCE]** This is the highest-quality *conventional* artifact in the space: executable,
cross-platform-tested, exercises with published solutions, ~210 quiz items. It has no
personalisation, no adaptation, and no learner state — and it is nonetheless the one I would hand
to a learner today. That fact should discipline our ambitions: **a well-maintained static book with
tested code and answer keys beats every adaptive claim currently shipping.**

### 3.3 The rest **[OBSERVED]**

| Artifact | Stars | Last push | Executable | Assess | Personalise |
|---|---:|---|---|---|---|
| `mlabonne/llm-course` | 81,262 | 2026-02-05 | Colabs, runnable | **No** | No |
| `d2l-ai/d2l-en` | 29,241 | **2024-08-18 (stale ~2y)** | Yes — multi-framework notebooks (MXNet/PyTorch/TF/JAX) | **No** | **No** |
| `fastai/fastbook` | 25,155 | **2024-08-16 (stale ~2y)** | Colab notebooks | No | No |
| `fastai/course22` | 3,670 | **2024-10-08 (stale)** | Notebooks + spreadsheets | No | No |
| `fastai/course-v3` | 4,912 | **2024-05-21 (dead)** | Notebooks | No | No |
| Stanford CS25 | — | current | **No** | **No — explicitly** | No |

- **[VENDOR]** d2l-en describes itself as *"Interactive deep learning book with multi-framework
  code, math, and discussions. Adopted at 500 universities from 70 countries."* The 500-university
  figure is **[VENDOR]** and I could **not verify it** through any independent channel; it must not
  be restated as a finding. What *is* **[OBSERVED]** is that the book is drafted entirely in Jupyter
  notebooks with parallel per-framework code blocks, has **no adaptive or personalised element
  whatsoever**, and **has not been pushed to in ~2 years.**
- **[VENDOR]** Stanford CS25: *"The only homework for students is weekly attendance to the
  talks/lectures."* A speaker series with zero assessment — materially different from CS336, and
  frequently conflated with it.
- **[UNREACHABLE]** fast.ai's famous "top-down, code-first" pedagogy statement is **not in either
  repo's README**; `fastbook`'s own license forbids redistribution of the prose ("The remainder
  (including all markdown cells... and other prose) is not licensed for any redistribution"), so I
  could not quote it from a primary GitHub source. Flagged, not guessed.

---

## 4. The genre nobody names: what "AI-native textbook" actually means in 2026

Before the infrastructure and research sections, one empirical observation about the *modal*
artifact, because it reframes what "already occupied" means.

**[OBSERVED]** GitHub search for `AI native textbook` (2026-07-27) returns 123 repos. The top
results are not diverse:

| Repo | ★ | Pushed | Description (verbatim) |
|---|---:|---|---|
| `EnggQasim/physical-ai-robotics-textbook` | 5 | 2025-12-02 | "AI-native textbook for Physical AI & Humanoid Robotics course - **Docusaurus + RAG Chatbot** + Podcast + Diagrams" |
| `AbdulSamad94/Cognita` | 3 | 2026-04-12 | "Interactive AI-native textbook platform with **Agentic RAG, personalized learning**, and humanoid robotics curriculum" |
| `zeeshan080/ai-native-robotics` | 2 | 2025-12-03 | "AI-Native Robotics Textbook" |
| `Bil4l-Mehmood/physical-ai-textbook` | 2 | 2025-12-10 | same course |
| `HamzaSheikh768/Physical-AI-Humanoid-Robotics-TextBook` | 2 | 2025-12-15 | "Used **Spec Driven and AI Native Development**" |
| `HezziCode/...`, `EmanIqbal620/ai-native-book`, +many | 1 | 2025-12 → 2026-06 | same course |

**[OBSERVED]** The query `physical ai humanoid robotics textbook` returns **501 repositories** —
one course cohort, replicating one architecture, hundreds of times.

I inspected two of them. Both are dominated not by content but by **agentic authoring scaffolding**:

- `EnggQasim/physical-ai-robotics-textbook`: 41 files — 34 `.md`, 7 `.sh`. The tree is
  `.claude/commands/sp.{specify,plan,tasks,implement,analyze,clarify,checklist,constitution,adr,phr}.md`
  + `.specify/{memory/constitution.md, scripts/bash/*, templates/*}`. **[OBSERVED]**
- `AbdulSamad94/Cognita`: 185 files including `.claude/skills/{chapter-analyzer,docusaurus,backend,
  chatbot,database,deployment,devops,nextjs,auth,architecture}/SKILL.md` and
  `.claude/agents/{fullstack-architect,qa-specialist,robotics-tutor}.md`. **[OBSERVED]**

**[INFERENCE] The modal "AI-native textbook" of 2026 is: Docusaurus (or Next.js) + a RAG chatbot
over the book's own text, produced by a spec-driven agent pipeline.** Of ~10 `.claude/skills/`
directories in Cognita, **nine are about building the website** and one (`robotics-tutor`) is about
teaching. This is §1.7's inversion again, at population scale: *the genre has industrialised
author-side agentic tooling and shipped, as its learner-side contribution, a chatbot that can
search the book.*

That matters for our positioning. "AI-native textbook" is **not** unclaimed ground — it is
*saturated* ground, occupied by hundreds of near-identical RAG-over-Docusaurus builds. What is
unclaimed is everything those builds skip.


---

## 5. The form factor nobody has written up yet: the agent-skill as the learning artifact

This is original primary research for this section, and it is the finding that most changes the
survey's positioning. **Between roughly May and July 2026 a new artifact class appeared: the
learning system shipped as a CLI-agent plugin/skill, with state on disk.** It is tiny, it is
unevaluated, and it is the *only* place in this entire survey where the four "unclaimed" primitives
are being built. Our claim to unclaimed ground has to be re-stated against it.

### 5.1 How I found it, and why the negative results matter

GitHub repository search, 2026-07-27 **[OBSERVED]**. Query counts are AND-over-terms and therefore
conservative, but the pattern is stark:

| Query | Total repos | Top result |
|---|---:|---|
| `teachable agent LLM learning by teaching` | **0** | — |
| `learner model knowledge tracing memory LLM tutor` | **0** | — |
| `protege effect AI` | **1** | `GOOHAESEUNG/moni` (0★, Korean: "학생이 AI를 가르치며 배운다" — *the student learns by teaching the AI*) |
| `learning by teaching LLM` | 18 | top result 1★ |
| `knowledge tracing LLM` | 31 | `umass-ml4ed/dialogue-kt` (40★, research code) |
| `socratic tutor refuse answer` | **5** | 6★, all created **May–July 2026** |
| `spaced repetition LLM tutor` | 23 | `TovTechOrg/Tov-learn` (34★, created **2026-05-20**) |

**[INFERENCE]** Read the dates. Every artifact in the refusal / persistence / SRS categories is
**less than three months old**. This is not an empty field; it is a field whose first structures
went up this quarter. Anything the survey says about "nobody has built X" needs a timestamp on it.

### 5.2 `Flagrare/llm-tutor` — the most serious refusal engine I could find **[OBSERVED]**

5★, created 2026-06-02, last push 2026-06-03. A Claude Code plugin. 45 files. Read the tree, not
the README:

```
plugins/llm-tutor/hooks/hooks.json
plugins/llm-tutor/hooks/refill-cycles.sh
plugins/llm-tutor/scripts/state.sh          (5,559 B)
plugins/llm-tutor/output-styles/{cipher,echo,vex}.md
docs/research/05-anti-dependency-design.md  (22,513 B)
docs/research/02-llm-tutor-landscape-2026.md (27,595 B)
docs/research/04-gamification-evidence.md   (16,165 B)
docs/decisions/2026-06-02-tutor-start-and-gamification.md (19,496 B)
```

**Persistent state is real and correctly engineered.** `state.sh` **[OBSERVED, quoted from source]**:

```bash
STATE_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.claude/llm-tutor}"
STATE_FILE="$STATE_DIR/state.json"
SCHEMA_VERSION=1
...
  schema_version: $v,
  user: { xp: 0, cycles: 5, cycles_cap: 5, cycles_last_reset: $now },
  topics: {}
```

with per-topic status (`state.sh set '.topics["python-decorators"].status' '"in_progress"'`) and —
note the engineering maturity — **atomic writes**: *"Atomic write: write to .tmp in the same
directory, then rename. Avoids torn reads if multiple hooks/skills write concurrently."*

**The refusal engine has an economy.** `cycles` is a **budget of help**, capped at 5, refilled
daily by a `UserPromptSubmit` hook that fires before *every* prompt (`refill-cycles.sh`, idempotent
and silent). Spending help costs `state.sh add .user.cycles -1`. **[INFERENCE]** This is the first
implementation I have seen where *not answering* is enforced by a resource constraint rather than by
a persona instruction — i.e. where refusal is a **system property** rather than a prompt that the
model can be talked out of. That is the architecturally correct move and it is worth naming.

**Its design doc is better than most of the published literature.** `05-anti-dependency-design.md`
proposes ten mechanisms **[OBSERVED, via fetch of the document]**, of which the non-obvious ones are:

- *Do-It-First Sequencing* — the help affordance is **locked until an independent attempt exists**.
- *Retrieval Practice Before Hint* — "Before offering any hint, ask the learner to recall what they already know."
- *Calibrated Struggle Windows* — 5–10 minute enforced delay before intervention, **with the window disclosed to the learner**.
- *Deliberate Latency* — 10–30 s imposed delay before hints render, framed as "think time."
- *Progressive Scaffolding Fading* — scaffolds are removed per problem-type once solved.
- *Explicit Graduation Moments* — "When a skill has been demonstrated independently across N instances, the tool explicitly tells the learner they no longer need the tool."

And — rarer than the mechanisms — **five honest admissions**, quoted **[OBSERVED]**:

1. *"A tool that succeeds at its mission loses its users. Subscription models are directly misaligned."*
2. *"Withholding answers presupposes the learner has baseline capacity to struggle productively"* — a first-generation student who must pass an exam to keep a scholarship *"does not have the luxury of deliberate practice philosophy."*
3. Anti-dependency design *"depends on accurate real-time assessment of where the learner is"*; miscalibration yields either helplessness or false autonomy.
4. The autonomy paradox: designing for independence requires modelling readiness, which creates dependency on the tool's judgment of readiness.
5. *"A tool that prominently withholds answers signals virtue but may not improve outcomes if the friction is theatrical rather than calibrated."*

Admission (5) is the sharpest sentence about refusal engines anywhere in this section, and it is in
a 5-star repo. Admission (2) is directly load-bearing for **H1** — refusal is not neutral across
learners, and a refusal engine designed without SELPA/at-risk learners in mind is an equity hazard.

**Two cautions on this artifact [OBSERVED / INFERENCE]:**
- Its evidence base is second-hand and contains at least one **apparent misattribution**: it credits
  the "−17% on the final exam" result to *"Mollick et al. (Penn/Wharton)"*. Per B2 §3.3 that result
  is **Bastani et al., PNAS 2025** (Penn/Wharton, but different authors). The number is right; the
  attribution is not.
- It relays a "Khanmigo validation" claim that a refuse-to-answer variant achieved *"nearly double
  the short-term gains"* versus vanilla ChatGPT. **I could not verify this number through any
  primary source. It must be treated as UNVERIFIED and may not be restated.**
- It also leans on the MIT EEG preprint, which B2 §4.5 already grades as weak. The doc does flag it
  as preprint with "active methodological discussion" — more caution than most secondary writing.

### 5.3 `TovTechOrg/Tov-learn` — persistent learner state, actually shipped **[OBSERVED]**

34★, created 2026-05-20, last push 2026-07-19. 127 files. A Claude Code skill with modules
`learn/{setup,teaching,quiz,progress,status,resume,project,project-analysis,slides,export,import,
deploy,security,cli-first}.md`.

The persistence design, from `.claude/commands/learn/progress.md` **[OBSERVED, quoted]** — it writes
a per-lesson Markdown file to `~/skill-tutor-tutorials/tutorials/lesson-{n}.md` with YAML
frontmatter:

```yaml
topic: [lesson title]
lesson: {lesson_number}
source_project: [learner's project from profile]
understanding_score: null
last_quizzed: null
```

and body sections including *"Topics Covered — in the learner's words, **not copied from the
script**"*, *"Common Mistakes to Watch For — what the learner got wrong or hesitated on"*, and
*"Q&A — every question the learner asked + the short answer."* Update semantics are append-only:
*"**Do not replace** existing content."*

Session continuity is handled outside the model entirely, by
`.claude/scripts/auto-save-progress.ps1` **[OBSERVED]**: *"Auto-save progress when Claude session
ends. Reads lesson/slide from TTS temp files and writes to skill-tutor-tutorials/progress/."* It
preserves quiz scores across writes and stamps lesson + slide + timestamp.

**[INFERENCE]** Three properties worth stealing: (a) the learner model is **human-readable
Markdown**, i.e. an open learner model by default; (b) it is **append-only**, so the record of
errors is not overwritten by later success — which is exactly what a spaced-repetition or
error-analysis layer needs; (c) `understanding_score` and `last_quizzed` are *declared fields that
are `null`* — the schema anticipates assessment the artifact has not yet built. That is an honest
placeholder, and it marks the exact boundary of what has been done. **[OBSERVED]** The persistence
mechanism is PowerShell and hooks into Windows `%TEMP%` — it is platform-bound and fragile.

### 5.4 `quzhi-ai/deep-learning` — a non-Western artifact with the sharpest pedagogy in the set **[OBSERVED]**

6★, created and last pushed 2026-06-06. Six files. Bilingual (Chinese primary, English README).
A single `SKILL.md` of 4,527 bytes. It is the highest ratio of pedagogy-per-byte in this section.

Mechanisms, quoted from the source (translations mine, originals retained):

- **Restate-before-correct, named as the核心杀伤力 ("core kill-power"):** *"先复述，再补漏 …
  优先让对方先用自己的话复述理解，再根据复述内容补充遗漏、纠正误区、填补知识空白。不要假设对方懂了
  ——让他证明给你看。这一步…把'好像懂了'逼成'真懂'或'真不懂'，没有中间地带。"* — "Restate first,
  then fill gaps… Do not assume they understand — make them prove it. This step forces 'I think I
  get it' into either 'I really get it' or 'I really don't'. **There is no middle ground.**"
- **An explanation ladder that matches F10's exactly, independently arrived at:** ELI5 / 初中生
  (middle-schooler, "analogy and intuition") / 大学生 (undergraduate, "principles and derivation") /
  职场新人 (new professional, "real work scenarios and an on-ramp"). Plus a calibration rule: *"不确定
  对方水平时，先问一句，或从中间层切入再根据反应调档"* — when unsure of level, ask, or enter at the
  middle rung and shift by response.
- **A persistent, visible learning checklist** with a fixed three-part skeleton (the problem itself /
  the solution / the wider context and consequences), explicitly *"活的"* — living, items added and
  removed as the topic unfolds, but the skeleton preserved.
- **Assessment hygiene most published prompts get wrong:** *"出题时不要提前透露答案"* (never leak the
  answer when posing the question) and *"选择题要打乱正确答案的位置顺序，不要总放某个固定选项"*
  (**shuffle the position of the correct option — do not always place it in a fixed slot**). That
  second rule is a direct patch for a known LLM item-writing failure and I have not seen it stated
  in any Western artifact in this section. Cross-reference **C2** on distractor quality.
- **Explicit anti-sycophancy:** *"导师口吻——有判断、有骨头，不做'你说得对'式的咨询腔"* — "a mentor's
  register: with judgment, with backbone; not the consultant's 'you're quite right' voice."
  And *"不空泛鼓励"* — no vague encouragement.
- **A termination condition, which almost nothing else in this section has:** *"清单全部打勾、且关键项
  对方能用自己的话复述并举出反例/边界情况，才算学完"* — done means every checklist item ticked **and**
  the learner can restate the key ones in their own words **and produce counterexamples / edge
  cases**.
- **A refusal engine at the routing layer**, in the YAML frontmatter: an explicit `不要用于`
  ("do not use for") clause naming three categories the skill must decline — pure factual lookup,
  execution tasks that need fast output, and decision/design/diagnosis work. **[INFERENCE]** This is
  refusal implemented as *scope*, not as *persona* — the skill declines to be the wrong tool. It is
  a different and more robust refusal primitive than "don't give the answer."

### 5.5 What §5 does to the survey's positioning

**[INFERENCE]** The agent-skill form factor has, in ten weeks and with a combined ~45 GitHub stars,
independently produced: durable on-disk learner state with atomic writes and an open, append-only,
human-readable learner model; a help budget that makes refusal a system property; a struggle-window
timer; a graduation condition; an ELI-ladder identical to F10's; and an explicit
do-not-answer routing scope. **None of it is evaluated. All of it is real code.**

The right conclusion is not "we were wrong about the empty space." It is: **the empty space is
being probed from the CLI-agent direction, by hobbyists, at the level of mechanism but not of
evidence.** The gap our survey can actually own is the one none of them touch — *measurement*.
See §10.


---

## 6. The most-adopted AI-learning artifact ever built, and it is dead

### 6.1 `JushBJJ/Mr.-Ranedeer-AI-Tutor` **[OBSERVED]**

**29,606 stars. 3,293 forks.** Created 2023-03-31. Last push 2025-09-30. No license. Repo size
342 KB, of which the artifact proper is **one 14,095-byte text file**.

The first line of the README, verbatim:

> `# DISCONTINUED`

**[OBSERVED]** That line was added in the commit of **2025-09-30**, the repo's final activity. The
most-starred AI-tutoring artifact in existence — with roughly **half the stars of nanoGPT and
almost as many as LLM101n** — is a prompt, and it has been formally abandoned by its author for ten
months.

This matters more than a curiosity, because Mr. Ranedeer contained more *pedagogical mechanism* than
most funded products. From `Mr_Ranedeer.txt` **[OBSERVED, quoted]**:

- **Learner configuration as a first-class object**: `Depth · Learning-Style · Communication-Style ·
  Tone-Style · Reasoning-Framework · Emojis · Language`, declared at the top of the prompt and
  recalled into a Python dict at every step.
- **Prerequisite decomposition before instruction**: the `[Curriculum]` function writes a
  *prerequisite* ladder numbered 0.1 → 0.9 that "will lead up to the photoelectric effect… but not
  include the topic itself (1.0)", *then* the main curriculum 1.1 → 1.10. Cross-reference **F10**:
  this is explanation laddering with an explicit prerequisite boundary, in a 2023 prompt.
- **A near/far transfer ladder in the assessment**: `[Test]` generates *"simple familiar problem,
  difficulty 3/10 · complex familiar problem, difficulty 6/10 · **complex unfamiliar problem,
  difficulty 9/10**"* — the familiar/unfamiliar axis is exactly the transfer distinction B2 says
  almost no study measures.
- **Verification by execution**: per `CHANGES.md` v2.7, *"Ability to solve mathematical problems in
  python first in the /test command before showing them to the student."* The tutor runs the
  problem in Code Interpreter before posing it. That is F3's grounding ladder, tier "execution",
  implemented in a prompt in 2023.
- **One-question-at-a-time**, added in v2.7 as *"Improve question accuracy by only giving one
  question at a time #40"*, with an explicit `<stop your response> <wait for student response>`.
- **A hidden learner model.** Every lesson step opens a code environment and writes
  *"a short assessment on how you think the student is learning and what changes to their
  configuration will be changed"*, then — the striking part —
  `<convert the output to base64> <output base64>` followed by
  `<do *not* show what you written in the code environment>`.

**[INFERENCE]** That base64 trick is the whole story of this genre in one line. It is an attempt to
build the two things this survey cares most about — **a learner model** and **hidden tutor
reasoning** — using the only substrate available to a prompt: the transcript itself, obfuscated so
the student cannot read it. It is ingenious and it is structurally doomed. The learner model lives
in the context window, so it dies with the session. The one persistence attempt —
`<save prerequisite and main curriculum into a .txt file>` — writes into the Code Interpreter
sandbox, which is also session-scoped. **The artifact wanted persistent learner state, tried twice
to get it, and could not, because the platform gave it nowhere to put it.**

### 6.2 The rot mechanism, admitted by the artifact itself **[OBSERVED]**

The README carries this warning, in the author's own words:

> *"Warning: The quality of outputs may vary depending on how OpenAI updates GPT-4, it may be either
> worse or better than a few weeks ago."*

And the dependency list: *"Recommended: ChatGPT Plus Subscription with GPT-4 **Code Interpreter**.
Not Recommended: GPT-3.5 · GPT-4 **without code interpreter** (As per v2.7) · GPT-4 with plugins."*
`CHANGES.md` records features being *removed* as the platform shifted — v2.6 deleted the `search`,
`self-eval`, and `visualize` commands and abandoned the JSON/YAML format for a bespoke one to cut
tokens; v2.7 removed the `teach` function and the "token check & magic number."

**[INFERENCE] This is the canonical case study of how an AI-learning artifact rots.** Every one of
its mechanisms was implemented as a *behaviour requested of a specific vendor model with a specific
tool surface*. When the model changed, the base64 trick, the sandbox file, the code-interpreter
verification, and the response-halting all became probabilistic. There was no substrate underneath
to hold the design. 29,606 stars did not save it. §11 turns this into a design rule.


---

## 7. Executable-book infrastructure — what actually runs in a browser today

F3 established *why* verification matters. This section establishes *what substrate exists to do it
in a book*, because that determines what our reference implementation can assume. The headline:
**the gap between "interactive" and "executes in the reader's browser" is enormous, and most of the
famous names are on the wrong side of it.**

### 7.1 The partition **[OBSERVED, from docs read directly]**

**Genuinely client-side, no server, today:**

| Project | ★ | State | Runtime |
|---|---:|---|---|
| Pyodide | 14,756 | Active; rel. 314.0.3 (2026-07-24) | CPython→WASM |
| JupyterLite | 4,856 | Active; v0.8.1 (2026-07-08) | Pyodide |
| marimo (WASM export / molab) | 22,072 | Active, weekly releases | Pyodide |
| Quarto Live | 259 | Active | webR **+** Pyodide |
| WebR | 1,085 | Active; v0.6.0 (2026-05-19) | R→WASM |
| Starboard | 1,350 | **Stale — no push since 2024-03-08** | Browser-native |

**Claims "live"/"interactive" but calls a remote server:**

- **Jupyter Book v1 and v2** — **[OBSERVED, v2 docs verbatim]**: *"By default, Jupyter Book will not
  execute any notebooks when your site builds. To execute your content at build time, use the
  `--execute` flag."* In-page execution is a separate feature that *"will use mybinder.org to build
  and provide the environment for computation... **This is a beta feature.**"* v1's live path
  (Thebe+Binder) is documented as *"an experimental feature, and may change in the future or work
  unexpectedly."*
- **mdBook** — **[OBSERVED, docs verbatim]**: *"Rust language code blocks will automatically get a
  play button (▶)... This works by sending the code to the Rust Playground [play.rust-lang.org]."*
  **Rust only, over the network, to a third party.** This is why §1.4's finding holds: an
  mdBook-based book *cannot* execute Python in the browser, however "interactive" it looks.
- **MyST / Curvenote in-page execution** — same Binder default, JupyterLite as beta alternative.
- **Thebe** — a kernel-*connector* UI, not an executor. (Also: `executablebooks/thebe` now
  301-redirects to `jupyter-book/thebe`; 442★, latest tagged release `0.9.2` from **2024-09-06**
  despite repo activity — stale releases against live development.)
- **Colab / Deepnote** — VM-backed by design. **[OBSERVED, Colab FAQ verbatim]**: *"Code is
  executed in a virtual machine private to your account."*
- **Runme / Stencila** — a *third* category: execution on the reader's own local machine via
  subprocess kernels. No sandbox at all.

### 7.2 The load-bearing constraint: what WASM cannot do **[OBSERVED, quoted from docs]**

Pyodide `docs/usage/wasm-constraints.md` — stdlib modules **removed**: `curses, dbm, ensurepip,
fcntl, grp, idlelib, lib2to3, msvcrt, pwd, resource, syslog, termios, tkinter, turtle.py,
turtledemo, venv, winreg, winsound`. Present-but-broken: `multiprocessing, threading, sockets`.
`ssl` is *"replaced with a stub implementation that does not use OpenSSL... actual SSL/TLS
connections, certificate validation, etc., are not available."* FAQ: *"fork and pthreads do not work
in Pyodide... Attempts to use threading, multiprocessing, or subprocess will raise a RuntimeError."*

Size **[OBSERVED, verbatim]**: *"The full distribution including all vendored packages... is quite
large (200+ megabytes)."* A `pyodide-core` tarball exists for the minimal boot set. **Startup
latency is not documented anywhere I could reach — UNREACHABLE, and I will not estimate it.**

JupyterLite's own troubleshooting page **[OBSERVED, verbatim]** names the same wall: packages that
*"require native C extensions that are not compiled for WebAssembly · depend on system libraries not
available in the browser · use threading or multiprocessing features not supported in WebAssembly ·
access the file system in ways not compatible with the browser sandbox."*

marimo WASM **[OBSERVED]**: *"PDB is not currently supported"*; *"WASM notebooks have a memory limit
of 2GB"*; concurrency raises `UnsupportedWasmConcurrencyError`.

**[INFERENCE]** Design consequence for our reference implementation: **anything the learner runs
in-browser must be single-threaded, network-free, pure-Python-or-ported, and small.** That is
precisely the profile of §1.4's stdlib-only examples — which is why that artifact's crude approach
turns out to be the *only* approach that ports to a browser without a server.

### 7.3 Reactivity ≠ verification — a distinction the field keeps blurring **[OBSERVED]**

marimo's README: *"marimo guarantees your notebook code, outputs, and program state are
**consistent**."* That is a guarantee about staleness, not about truth. A marimo notebook cannot
show you an output that no longer matches its code; it can happily show you an output that is
wrong. Correctness is bring-your-own (`pytest` over cells whose function names begin with `test_`).

**[INFERENCE]** Worth stating explicitly in the survey because "always up to date" reads as
"verified" to almost every reader, and it is not. Cross-reference F3's ladder: reactivity is a
*consistency* property, one tier below *execution-with-assertion*.

### 7.4 Only one book toolchain has real grading **[OBSERVED, verified at code level]**

**Quarto Live** is the single exception in the browser-native set. A `#| check: true` block receives
`.result`, `.evaluate_result`, `.user_code`, and `.solution_code` — genuine execution-state
introspection, including the ability to match actual R error text (e.g. `"non-numeric argument to
binary operator"`) and respond to *that specific failure*. It can also delegate to the mature
`{gradethis}` / `learnr` engine for structural comparison. **This is real automated grading running
entirely client-side, and it is the state of the art for a book.** It has 259 stars.

**[INFERENCE]** The distribution here is the story: the *most capable* browser-native assessment
substrate in existence has ~1% of the attention of the *least* capable one (mdBook, 22,014★).
Capability and adoption are almost uncorrelated in this space.

### 7.5 Autograding infrastructure state **[OBSERVED]**

| Project | ★ | Latest release | Open issues | Verdict |
|---|---:|---|---:|---|
| `ucbds-infra/otter-grader` | 157 | **v7.0.0, 2026-07-27** (same day as research) | 19 | **Healthiest** |
| `jupyter/nbgrader` | 1,369 | v0.9.5, **2025-01-17 (~18 mo stale)** | **269** | Alive, release-stalled |
| `github-education-resources/autograding` | 59 | none | — | **ARCHIVED** |

**[OBSERVED, verbatim]** GitHub Classroom's own open-source autograder README: *"Repo Archived.
NOTE: This Action is no longer used for Autograding tests created via the GitHub Classroom GUI...
**This project does not currently have a roadmap.**"* The replacement is closed-source and
in-product.

### 7.6 The pre-LLM systems that already solved what the AI-book crowd has not

This is the most uncomfortable finding in §7.

**PrairieLearn** (491★, pushed 2026-07-27, continuously deployed). **[OBSERVED, verbatim]**:
*"PrairieLearn allows you to securely run custom grading scripts in environments that you specify...
a Docker image to execute your tests in."* Server-side, container-isolated grading — the opposite
trust model from client-side WASM, and the correct one when the grade matters.

**[MEASURED-BENCH]** PrairieLearn has real efficacy research, which almost nothing in this section
does. Chen, West & Zilles, *Journal of Engineering Education* 2019, DOI `10.1002/jee.20292`:
analysis of **31,673 exam records across four semesters and six courses**, finding that *"controlling
for student ability (via synchronous exams) removes 70% of the decline observed in average
asynchronous exam scores over the exam period"* and concluding *"there is no evidence for widespread
collaborative cheating."* Foundational paper: West, Herman & Zilles, ASEE 2015, DOI
`10.18260/p.24575` (81 citations).

**Runestone** (`RunestoneInteractive/rs`, 70★, active). Runtime is **Skulpt** (a JS reimplementation
of CPython), not WASM. Its real differentiator is not execution — it is **durable, cross-session,
instructor-visible state**. **[OBSERVED, verbatim]**: *"Many actions that students take are
logged... Loading a book page, Answering a multiple choice question... Running code in an ActiveCode
window."* Ships a Chapter Progress Report, per-student progress views, aggregate histograms, an
autograde button, and a "Learning Engineering and Analytics Portal."

**[INFERENCE] This is the punchline of §7.** Runestone — an interactive CS textbook platform that
predates LLMs by a decade — has persistent per-learner state, a gradebook, and analytics. **None of
Pyodide, JupyterLite, marimo, Quarto Live, or any AI-native textbook in §4 persists or aggregates
learner performance at all.** The new stack has better execution and *worse memory*. It threw away
the learner model to get rid of the server.

**[OBSERVED]** Runestone's efficacy literature is, by contrast, thin — system/adoption papers only
(Miller & Ranum L@S 2014, 20 citations; Ericson & Miller SIGCSE 2020, 28 citations), no outcome
study comparable to the PrairieLearn JEE paper.

### 7.7 The substrate under the substrate is disclaimed by its own operators

Every "live" book that defaults to Binder inherits this. **[OBSERVED, mybinder.org docs, verbatim]**:

> *"As mybinder.org is a research pilot project... we want our users to understand the intent of
> this service is research and we offer no guarantees of its performance in mission critical uses."*
> ... *"it has no dedicated funding and runs entirely on donations of cloud resources... Please do
> not use mybinder.org as backend for your for-profit service or product."*

Hard caps: 1–2 GB RAM, 10-minute inactivity shutdown, ~6 CPU-hours per session, **max 100
simultaneous users per repository**.

**[INFERENCE]** Jupyter Book's default "live execution" path rests on an unfunded research pilot
that explicitly disclaims reliability and caps a book at 100 concurrent readers. Any survey claim
that "executable books are a solved substrate" is false in the direction that matters.


---

## 8. Book-length works, graded on one axis: does it prescribe a mechanism or narrate anecdotes?

The trade-book layer of this genre is where the survey will most often be compared, so it needs a
grade rather than a summary. One axis: **can a reader implement the claim, or only agree with it?**

**Method note and honesty flag.** SSRN abstract pages return **HTTP 403 to automated fetch —
UNREACHABLE**. I could verify **bibliographic facts** via Crossref but **not full text** for the
Mollick working papers. Where I characterise their contents below, it is labelled **[INFERENCE]**
and is based on the titles' explicit self-description, not on retrieved text. Numbers I could not
verify are marked as such.

| Work | Form | Verified facts | Prescribes a mechanism? |
|---|---|---|---|
| Mollick & Mollick, *"Assigning AI: Seven Approaches for Students, **with Prompts**"* | Working paper | **[OBSERVED, Crossref]** DOI `10.2139/ssrn.4475995`, deposited 2023-06-22, **195 citations** | **Yes, weakly.** The title's own "with Prompts" is the mechanism claim: seven named instructional roles, each shipped with a literal prompt. **[INFERENCE]** A prompt is a mechanism a reader can execute; it is also the most fragile substrate available (§6.2). |
| Mollick & Mollick, *"Using AI to Implement Effective Teaching Strategies in Classrooms: Five Strategies, **Including Prompts**"* | Working paper | **[OBSERVED, Crossref]** DOI `10.2139/ssrn.4391243`, deposited 2023-03-24, **198 citations** | Same form. |
| Mollick & Mollick, *"Instructors as Innovators: a Future-focused Approach to New AI Learning Opportunities, With Prompts"* | Working paper | **[OBSERVED, Crossref]** DOI `10.2139/ssrn.4802463`, 2024-04-23, **54 citations** | Same form. |
| Mollick, *Co-Intelligence: Living and Working with AI* (2024) | Trade book | **[UNREACHABLE]** — no DOI record retrievable via Crossref/OpenAlex within budget; **I could not verify sales, print run, or citation figures and will not state any** | **[INFERENCE] Mostly no.** Its contribution is a *stance* (invite AI to the table; keep a human in the loop; give the AI a persona; assume today's model is the worst you will use) plus extensive anecdote. Stances are adoptable, not implementable. |
| Bates, *Teaching in a Digital Age* (open textbook, 3rd ed.) | Open text | **[OBSERVED, Crossref]** review at DOI `10.19173/irrodl.v24i2.7063` (IRRODL, 2023) | **[INFERENCE]** Prescribes instructional-design *process* (pre-LLM lineage), not AI mechanism. Its durability is the interesting property — a continuously-revised open text with named editions. |

**[INFERENCE] The grade.** The trade layer's real contribution is *vocabulary and permission* — it
made AI-in-education discussable for administrators, and the citation counts (195, 198) show the
prompt papers being used as canonical references. Its real limitation is that **the most
implementable thing it ships is a prompt**, and §6 documents in detail what happens to a
prompt-shaped artifact over 30 months.

**A rule this suggests for our survey.** Anything we prescribe should be gradeable on the same axis
we are grading others: *can the reader run it, and can something tell them they ran it wrong?* If
the answer to the second question is no, we have written a stance.


---

## 9. The graveyard — thirteen documented deaths, stalls, and undelivered promises

The brief asked for three. The space supplied thirteen, and the *pattern* across them is more
useful than any single one. All **[OBSERVED]**, all dated, quoted where the wording carries weight.

### 9.1 Dead by explicit declaration

| # | Artifact | ★ | Date of death | The artifact's own words |
|---|---|---:|---|---|
| 1 | `JushBJJ/Mr.-Ranedeer-AI-Tutor` | **29,606** | 2025-09-30 | README line 1: **`# DISCONTINUED`** |
| 2 | `karpathy/LLM101n` | **37,504** | archived 2024-08-01 | *"this course does not yet exist... Until it is ready I am archiving this repo"* |
| 3 | `github-education-resources/autograding` | 59 | archived 2024-05-02 | *"Repo Archived... This project does not currently have a roadmap."* |
| 4 | `RunestoneInteractive/RunestoneServer` | 575 | archived 2024-06-30 | *"This repo is now Archived. Future development has moved to our monorepo called rs."* |
| 5 | `RunestoneInteractive/RunestoneComponents` | 103 | archived 2023-06-07 | same |
| 6 | `karpathy/nanoGPT` | 61,572 | self-deprecated Nov 2025 | *"nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity."* |
| 7 | Observable **Cloud** | — | current docs | tagged **`[DEPRECATED]`** on Observable's own documentation index (Notebooks, notably, is **not**) |
| 8 | `executablebooks/*` early lineage | — | 2019–2024 | `thebe-core` archived 2022-08-22; `myst`, `cli`, `rst2myst`, `mistletoe-ebp` archived 2019–20; `myst-book-theme`/`myst-article-theme` archived 2023-04-26; `jupyter-book-myst` archived, last push 2024-10-01. **No "funding ended" statement was found in reachable sources — the archival pattern is the evidence, not a notice. `executablebooks.org` was UNREACHABLE (429).** |

### 9.2 Dead by silence

| # | Artifact | ★ | Last push | Note |
|---|---|---:|---|---|
| 9 | `gzuidhof/starboard-notebook` | 1,350 | **2024-03-08** | A genuine browser-native, no-server execution pioneer. All satellites (`starboard-cli/-jupyter/-python/-observable`) frozen since **2021**. Not archived — just stopped. |
| 10 | `d2l-ai/d2l-en` | 29,241 | **2024-08-18** | ~2 years. Still the most-adopted interactive DL textbook. |
| 11 | `fastai/fastbook` · `course22` · `course-v3` | 25,155 / 3,670 / 4,912 | 2024-08-16 / 2024-10-08 / **2024-05-21** | Three generations of the same course, none archived, all frozen. |
| 12 | `jupyter/nbgrader` | 1,369 | active commits, but **last release v0.9.5 = 2025-01-17 (~18 months)**, **269 open issues** | Release-stalled, not dead. The distinction matters when you depend on it. |
| 13 | `xiaol/Harnessing-LLM-Skills...` (§1) | **0** | 2026-04-25 | Born complete, never touched again. A different failure mode: not abandonment but *single-shot artifacts that have no second commit by design*. |

### 9.3 The undelivered promises — a category of its own

- **`EurekaLabsAI/ngram`'s own TODO list**: *"- Make better / - **Make exercises** / - Call for
  help..."* Never done. From the organisation whose thesis is pedagogy.
- **`karpathy/build-nanogpt`**: has carried an **empty `## FAQ` header** for ~2 years.
- **`karpathy/nn-zero-to-hero`**: *"(This may grow into something more respectable.)"* … *"Ongoing..."*
  — unresolved since 2022.
- **`TovTechOrg/Tov-learn`** (§5.3): ships `understanding_score: null` and `last_quizzed: null` in
  its learner-model schema. Honest, and precisely the boundary of what is built.
- **`mybinder.org`**, the substrate under every "live" Jupyter Book: *"no dedicated funding and runs
  entirely on donations of cloud resources... we offer no guarantees of its performance in mission
  critical uses."* Capped at **100 simultaneous users per repository**.

### 9.4 What kills these things — four mechanisms, ranked by body count

**[INFERENCE]** Reading the thirteen together:

1. **Vendor-behaviour dependency (the biggest killer).** Mr. Ranedeer died because its mechanisms
   were *requests to a specific model with a specific tool surface* — base64 CoT-hiding, sandbox
   file persistence, code-interpreter verification, response-halting. Every one degraded silently as
   the platform moved. The author documented it himself: *"quality of outputs may vary depending on
   how OpenAI updates GPT-4."* **29,606 stars bought no immunity.**
2. **The pedagogy is the part that doesn't get built.** Eureka Labs shipped working n-gram and
   tensor code in two weeks and never made the exercises. LLM101n has a beautiful syllabus and zero
   chapters. **In every case, the code shipped and the pedagogy didn't** — because the code has a
   definition of done and the pedagogy does not.
3. **Attention is uncorrelated with capability.** mdBook (22,014★) cannot run Python. Quarto Live
   (259★) does client-side execution *with real grading*. LLM101n (37,504★) is two files. The star
   count of an AI-learning artifact predicts almost nothing about what it does.
4. **Unfunded shared substrate.** Binder, `executablebooks`, GitHub Classroom's autograder — the
   layer everything else assumed was permanent turned out to be a grant, a volunteer, or a
   deprioritised internal project.


---

## 10. The registry — every artifact, one row, six axes

Columns: **Exec** = code runs · **Verif** = something can say *no* · **Pers** = adapts to this
learner · **Assess** = measures this learner · **Evid** = evidence offered for its learning claims.
`—` = absent. `(b)` = in-browser. `(s)` = server/remote required.

### 10.1 Books, courses, and curricula

| Artifact | Form | ★ | Mechanism claimed | Exec | Verif | Pers | Assess | Evid |
|---|---|---:|---|---|---|---|---|---|
| **xiaol/Harnessing-LLM-Skills** | mdBook + skills + examples | 0 | Harness engineering; reusable skill-scaffolds with a Quality Bar; learner compares AI output to own reasoning | ✅ local, **16/16 reproducible [MEASURED-BENCH]** | — (no asserts, no tests) | — | — | **none** |
| `stanford-cs336/assignment1-basics` | Course + autograder | 2,466 | Implement transformer components from scratch; numeric snapshot tests via `adapters.py` | ✅ (s) | ✅ **strongest found** | — | ✅ per-component | course-internal |
| `rasbt/LLMs-from-scratch` | Book repo | 99,909 | Build an LLM chapter by chapter; exercises + published solutions + ~30 quiz items/ch | ✅ CI on 3 OSes | ✅ code tests | — | ✅ answer keys | — |
| `mlabonne/llm-course` | Roadmap + Colabs | 81,262 | Curated path in 3 tracks | ✅ Colab (s) | — | — | — | — |
| `d2l-ai/d2l-en` | Interactive textbook | 29,241 | Multi-framework executable notebooks | ✅ (s) | — | — | — | **[VENDOR]** "500 universities" — **unverified** |
| `fastai/fastbook` | Book repo | 25,155 | Top-down code-first | ✅ Colab (s) | — | — | — | **[UNREACHABLE]** pedagogy statement not in repo |
| `karpathy/nn-zero-to-hero` | Video + notebooks | 23,706 | Build from scratch; exercises in video descriptions | ✅ Colab (s) | — | — | partial | — |
| `karpathy/nanochat` | Codebase | 56,693 | Full LLM pipeline, forkable strong baseline | ✅ (s, GPU) | ✅ code tests + **public leaderboard** | — | — (of the artifact, not the person) | **[VENDOR]** $48/2h GPT-2-capability |
| `karpathy/LLM101n` | **Syllabus only** | 37,504 | 17-chapter build-a-Storyteller course | — | — | — | — | — |
| Stanford CS25 | Speaker series | — | Exposure to research | — | — | — | **[VENDOR]** *"The only homework... is weekly attendance"* | — |
| "Physical AI textbook" cluster (~501 repos) | Docusaurus + RAG | 1–5 each | Ask-the-book chatbot | — | — | **[VENDOR]** "personalized learning" | — | — |
| Mollick & Mollick prompt papers | Working papers | — | Named instructional roles, each with a literal prompt | — | — | — | — | 195 / 198 citations **[OBSERVED]** |

### 10.2 Products and prompt-artifacts

| Artifact | Form | ★ | Mechanism | Exec | Verif | Pers | Assess | Evid |
|---|---|---:|---|---|---|---|---|---|
| `Mr.-Ranedeer-AI-Tutor` | 14 KB prompt | **29,606** | Learner config object; prerequisite ladder 0.1→0.9; 3/6/9-difficulty familiar/unfamiliar test; python-verified problems; base64-hidden learner model | ✅ via Code Interpreter (s) | ✅ *executes the problem before posing it* | ✅ config-driven | ✅ `/test` | — · **DISCONTINUED** |
| Eureka Labs | Company/thesis | — | **[VENDOR]** *"teacher still designs the course materials... supported, leveraged and scaled with an AI Teaching Assistant who is optimized to help guide the students"* | — | — | — | — | none; no product |

### 10.3 The agent-skill class (all created May–July 2026)

| Artifact | ★ | Created | Mechanism | Exec | Verif | Pers | Assess | Evid |
|---|---:|---|---|---|---|---|---|---|
| `Flagrare/llm-tutor` | 5 | 2026-06-02 | **`state.json` (atomic writes) + `cycles` help-budget refilled daily by a `UserPromptSubmit` hook**; 10 anti-dependency patterns incl. do-it-first gating, struggle windows, scaffold fading, graduation | agent-hosted | — | ✅ per-topic status | XP only | cites B2-grade literature; **one misattribution + one unverifiable claim (§5.2)** |
| `TovTechOrg/Tov-learn` | 34 | 2026-05-20 | Per-lesson Markdown learner model, **append-only, human-readable**, auto-saved on session end; project-grounded examples | agent-hosted | — | ✅ | schema declared, **`understanding_score: null`** | — |
| `quzhi-ai/deep-learning` | 6 | 2026-06-06 | **Restate-before-correct** ("no middle ground"); ELI5→中学→大学→职场 ladder; living checklist; shuffled-position MCQ; anti-sycophancy; **termination = restate + produce counterexamples**; `不要用于` refusal scope | — | learner-restatement as the check | ✅ level calibration | ✅ open/MCQ/case | — |

### 10.4 Executable-book and assessment infrastructure

| Artifact | ★ | In-browser exec | Verifiable | Persists learner state | Note |
|---|---:|---|---|---|---|
| **Quarto Live** | 259 | ✅ webR + Pyodide | ✅ **real grading**: `.result`/`.user_code`/`.solution_code`, error-text matching, `{gradethis}` | — | **Best browser-native assessment substrate in existence** |
| JupyterLite | 4,856 | ✅ Pyodide | BYO | — | Documented WASM limits (§7.2) |
| marimo (WASM) | 22,072 | ✅ Pyodide | **consistency ≠ correctness**; BYO pytest | — | 2 GB cap, no PDB, no threads |
| Pyodide | 14,756 | ✅ (engine) | n/a | n/a | 200+ MB full dist; no threads/sockets/ssl |
| WebR | 1,085 | ✅ | n/a | n/a | — |
| Jupyter Book v1/v2 | 4,259 | **❌ default** — build-time static; live = **Binder, beta/experimental** | — | — | Inherits mybinder's disclaimers |
| mdBook | 22,014 | **❌ Rust only, via remote play.rust-lang.org** | — | — | The substrate under §1 |
| Thebe | 442 | connector only | — | — | Release stale since 2024-09-06 |
| Colab / Deepnote | — | ❌ VM-backed | — | — | *"a virtual machine private to your account"* |
| **PrairieLearn** | 491 | ❌ by design (Docker, server) | ✅ **container-isolated custom graders** | ✅ | **[MEASURED-BENCH]** 31,673 exam records, JEE 2019 |
| **Runestone** | 70 | ✅ Skulpt | ✅ autograde | ✅ **full event log + gradebook + analytics portal** | Efficacy lit thin (20/28 citations) |
| otter-grader | 157 | n/a | ✅ | ✅ | v7.0.0 same-day — healthiest autograder |
| nbgrader | 1,369 | n/a | ✅ | ✅ | 18-mo release gap, 269 open issues |
| Starboard | 1,350 | ✅ (was) | — | — | **Stale since 2024-03-08** |


### 10.5 Research systems and vendor stacks

| Artifact | Form | Mechanism | Evidence offered | Grade |
|---|---|---|---|---|
| **OATutor** (`CAHLR/OATutor`, 231★, active) | Open ITS, React+Firebase, Bayesian Knowledge Tracing, OpenStax content, §508-compliant, in classrooms since Fall 2024 | Adaptive hints + BKT learner model | **[MEASURED-RCT]** Pardos & Bhandari, *PLOS ONE* 2024, `10.1371/journal.pone.0304013`: 3×4 design, **N=274**. Only the ChatGPT-hint condition produced significant gains vs. no-help control; **no significant difference between ChatGPT- and human-tutor-authored hints** on gains or time-on-task. **Also measured: ChatGPT help failed quality checks on 32% of problems**, reduced to ~0% (algebra) / 13% (statistics) via self-consistency mitigation. CHI'23 `10.1145/3544548.3581574` | **The best-evidenced open artifact in this entire section** |
| **Bridge** (Wang et al., Stanford; arXiv:2310.10648, code on GitHub) | Method | Cognitive task analysis distilling expert tutors' error→strategy→intent decision into a remediation decision model | **[MEASURED-BENCH]** 700 real tutoring conversations; GPT-4 conditioned on expert decisions **+76% preferred**; **random decisions −97%** | The decision layer, not the generator, carries the quality |
| **LearnLM** (arXiv:2412.16429) | Model + report | "Pedagogical instruction following" — pedagogy as system instruction rather than hard-coded theory | **[MEASURED-BENCH, preference only]** experts prefer LearnLM **+31% vs GPT-4o, +11% vs Claude 3.5 Sonnet, +13% vs Gemini 1.5 Pro**. **These are expert preferences on dialogue quality, not student learning outcomes.** No student RCT in the retrievable abstract; full PDF exceeded fetch limits — rater counts/rubrics **UNREACHABLE** | See D3. Preference ≠ learning |
| **Khanmigo** | Product | — | **[OBSERVED]** Crossref returns only SWOT analysis (`10.22521/edupij.2025.16.272`), a CALL-app evaluation, a semiotic/discourse analysis, and **conference posters** on an Oklahoma pilot (`10.3102/ip.25.2196913`). **No RCT or controlled learning-outcome study found in any permitted database.** | **VENDOR only** |
| **Anthropic Learning Mode / OpenAI Study Mode** | Products | — | **UNREACHABLE** — anthropic.com/news/claude-for-education 404, openai.com study-mode page 403. No academic paper found. **Not characterised.** | — |
| **EduGuard** (arXiv:2607.15738) | RAG tutor | Overreliance control + claim-level verification | **[MEASURED, small pilot N=10]** post-test 68.4%→81.2%; overreliance 38.0%→17.0% vs GPT-4o-mini-Tutor. Benchmark (600 queries): correctness 90.1%, hallucination 4.9%, **direct-answer leakage 9.8%** | Small N; leakage is now a *measured quantity* |
| **HypoCompass** (arXiv:2310.05292) | Teachable agent | Student plays TA, LLM plays tutee, for debugging | **[MEASURED]** 4× more efficient bug generation than humans; **+12 pp** pre→post debugging | — |
| **TutorGym** (arXiv:2505.01563) | Benchmark | ITS backbone over OATutor + CTAT + Apprentice Tutors, 223 tutor domains | **[MEASURED-BENCH]** LLMs-as-tutors: 52–70% next-step accuracy and **"none did better than chance at labeling incorrect actions"**; LLMs-as-students via ICL produce "remarkably human-like learning curves" | The single most useful number in this table (below) |
| **Squirrel AI** (China) | Product + papers | Adaptive learning at fine knowledge-point granularity | **[MEASURED, quasi-experimental]** Cui et al. arXiv:1901.10268; Cui/Tong + **SRI International** co-authors, *Interactive Learning Environments* 2020, `10.1080/10494820.2020.1808794`, **235 citations** — third-party co-authorship raises credibility above pure vendor research. MUTLA multimodal dataset arXiv:1910.06078 | Best-evidenced non-Western product |
| **SocraticLM** (NeurIPS 2024, `10.52202/079017-2721`) | Model | Socratic tutoring | USTC + **iFlytek** co-authorship confirmed; abstract **UNREACHABLE** | Real, uncharacterised |
| **CTAT** (`CMUCTAT/CTAT`, 122★) · **Apprentice Learner** (`apprenticelearner/AL_Core`, 15★) | Authoring toolkits | Cognitive-tutor authoring; simulated-student model tracing | Long-running academic lineage | Shared research substrate |
| **Sunbird-Ed** (India, DIKSHA) | National platform, open source | 30+ repos, `SunbirdEd-portal` 40★ | **[OBSERVED]** Genuine national-scale open infrastructure, but **content/LMS, not a generative tutor**. No official government-shipped generative-AI tutor found; GitHub "NCERT AI" returns only 5–8★ hobbyist repos | Scale without AI pedagogy |
| **X5GON** (EU H2020, arXiv:2112.01242) | Platform | Cross-lingual OER personalisation | Vision/report paper, no RCT | **DEMO** |


---

## 11. The occupied space — redoing these is waste

**[INFERENCE, from the registry]** Six things are done well enough that rebuilding them is a
misallocation. For each, the correct move is *depend on it or cite it*, not rebuild it.

**11.1 From-scratch reconstruction as a curriculum spine.** micrograd → nanoGPT → build-nanogpt →
llm.c → nanochat, plus `rasbt/LLMs-from-scratch` (99,909★, pushed the day of this research, exercise
solutions + ~30 quiz items/chapter + 3-OS CI). Combined ~250,000 stars. **Settled.**

**11.2 Autograded from-scratch implementation.** Stanford CS336's `adapters.py` + numeric snapshot
pattern (§3.1) is the reference design for "the student implements it, and something checks the
tensors." Copy the pattern; do not reinvent the grader.

**11.3 Browser-native code execution.** Pyodide/JupyterLite/WebR/marimo-WASM work, with documented
and *stable* limits (§7.2). The engineering is done. What is not done is anything above it.

**11.4 Server-side, container-isolated assessment.** PrairieLearn. Ten years of it, plus real
efficacy research on 31,673 exam records. If a grade must be trustworthy, this is the trust model.

**11.5 Durable learner state with instructor analytics — *in the pre-LLM stack*.** Runestone logs
every page load, MCQ answer, and ActiveCode run, and ships a progress report, per-student views, and
an analytics portal. **This is the most under-recognised fact in this section.** The capability our
survey calls unclaimed *exists*; it exists in a 70-star decade-old CS-textbook platform, and the
entire LLM-era stack dropped it.

**11.6 "AI-native textbook" as a phrase and as a product shape.** §4: ~501 repos replicating
Docusaurus + RAG-over-the-book. **Saturated.** Any survey that positions on this phrase is
positioning on occupied ground.

---

## 12. The contested space — where credible people disagree about mechanism

**12.1 Does unguarded AI access harm learning? — genuinely unresolved, and B2 should know it.**

B2 anchors on Bastani et al. (PNAS 2025, `10.1073/pnas.2422633122`, N≈1,000): during access, GPT
Base **+48%** and GPT Tutor **+127%** on practice; with access removed, GPT Base **−17%** versus
never-had-access. **[MEASURED-RCT]**

**[OBSERVED] New for G3 — this result is under active dispute:**
- A **PNAS Correction** exists: `10.1073/pnas.2518204122`. **Its content is UNREACHABLE (PNAS
  returned 403). I do not know what was corrected and will not guess.**
- A formal design critique: Tan & Rajaratnam, *"Critique of Generative AI Can Harm Learning Study
  Design,"* `10.2139/ssrn.4898213` (abstract unreachable).
- A direct counter-study: *"Generative AI Can Improve Performance and Engagement without Harming
  Learning,"* `10.2139/ssrn.5929576` (abstract unreachable).

**[INFERENCE] Action item for the survey:** the −17% number is load-bearing in at least five of our
sections. It must be cited *with* the correction notice and the critique, or we inherit a contested
finding as settled. **This is a cross-section flag for B2, F1, F2, H1, and E1.**

**12.2 Does a conversational tutor beat reading? — the best-designed studies say no.**

**[MEASURED-RCT]** Ruffle&Riley (CMU/ETH), an LLM learning-by-teaching conversational tutor, nulled
**twice**: arXiv:2310.01420 (N=100) — no significant post-test difference vs. QA chatbot or plain
reading; arXiv:2404.17460 (N=200, biology) — *"we did not find significant differences in short-term
learning gains over the reading activity"*, and users needed **more time**. High subjective ratings
of understanding and helpfulness in both.

Corroborating: **[MEASURED-RCT]** arXiv:2412.15747, N=214 sixth-graders, AI-chatbot-generated
materials vs. textbook materials — *"AI-generated materials had an indefinite [non-significant]
impact on learning outcomes"* while significantly improving interest, self-efficacy, and cognitive
load.

**[INFERENCE]** Twice-replicated null plus an affect/outcome dissociation. The contested claim is not
"does AI help" — it is **"is conversation the right interface at all, or does it buy affect and
sell time?"** Our survey must not assume the conversational form.

**12.3 Is generated content as good as expert content? — surprisingly, sometimes yes.**

**[MEASURED-RCT]** OATutor, N=274: ChatGPT-authored hints produced learning gains **statistically
indistinguishable from human-tutor-authored hints**, and were the *only* condition significantly
better than no-help. **[MEASURED]** But 32% of generated hints failed quality checks, dropping to
~0% (algebra) / 13% (statistics) under self-consistency mitigation.

**[INFERENCE]** The contested mechanism is *where the quality comes from*. Bridge says the
**decision** does the work (expert-conditioned +76% preferred; **random decisions −97%**) — i.e. the
generator is fine and the routing is everything. OATutor says the **content** is fine if you filter
it. Both cannot be the primary lever. Our F10/C2 design should treat this as an open empirical
question and instrument for it.

**12.4 Can an LLM tell that a student is wrong? — the field's most important negative number.**

**[MEASURED-BENCH]** TutorGym (arXiv:2505.01563), across 223 tutor domains: LLMs used as tutors
score 52–70% on next-step accuracy, and — quoted — **"none did better than chance at labeling
incorrect actions."** Meanwhile the same paper finds LLMs used *as students* via in-context learning
*"produce remarkably human-like learning curves."*

**[INFERENCE] This single result reorganises the design space.** The model is a *better simulated
learner than it is an error detector.* Every architecture that assumes the tutor can diagnose the
student — including "teacher + AI TA" (§2.1) — is building on the weaker of the two capabilities.
Architectures that put the model in the *learner* seat, or that route diagnosis to a non-linguistic
checker (F3's ladder, CS336's snapshot tests), are building on the stronger one.

**12.5 Refusal: virtue signal or mechanism?** `llm-tutor`'s own design doc states the dispute better
than the literature does — *"A tool that prominently withholds answers signals virtue but may not
improve outcomes if the friction is theatrical rather than calibrated"* — against its own admission
that calibration *"depends on accurate real-time assessment of where the learner is,"* which §12.4
says the model cannot do. **[INFERENCE] Refusal without diagnosis is theatre. That is the contested
core, and it is currently unresolved in both directions.**

---

## 13. The empty space — testing the survey's claim

The survey's stated claim: the unclaimed ground is **(a)** persistent learner state across sessions,
**(b)** a teachable agent that can be wrong on purpose and hold the error, **(c)** deixis — pointing
at the thing in a shared visual field, and **(d)** the refusal engine — deciding *not* to answer.

Verdict: **one refuted, two confirmed, one confirmed-with-a-major-amendment.** Plus two additions.

### 13.1 (a) Persistent learner state — **CONFIRMED, but the claim must be re-worded**

**Literature [OBSERVED, systematic absence]:** arXiv direct-phrase searches for `"open learner
model"` and `"long-term learner model"` return **zero**. `"knowledge tracing" AND "large language
model"` returns 45, essentially all about *predicting* knowledge state for benchmarks (SINKT, CIKT,
LLM-KT, MERIT), **not about persisting and reusing state across multi-session deployments with a
measured benefit.** No RCT found comparing a stateful tutor to a stateless one.

**Artifacts [OBSERVED]:** GitHub `learner model knowledge tracing memory LLM tutor` → **0 repos.**
But §5 found `Flagrare/llm-tutor` (`state.json`, atomic writes, per-topic status) and
`TovTechOrg/Tov-learn` (append-only human-readable per-lesson learner model, auto-saved on session
end) — both **created in the last ten weeks**, combined 39 stars, **zero evaluation**.

**And the amendment that matters:** §7.6 — **Runestone has had this since before LLMs.** Full event
logging, gradebook, per-student progress, analytics portal.

**[INFERENCE] Corrected claim:** persistent learner state is *not unbuilt*. It was **built a decade
ago in the ITS stack, discarded by the LLM stack when it went serverless, is being rebuilt right now
by hobbyists in the agent-skill form factor, and has never once been measured against a stateless
baseline.** The unclaimed ground is not the feature. **It is the evidence that the feature does
anything.** That is a stronger and more defensible position than "nobody has built it," and it is
one we can actually occupy.

### 13.2 (b) Teachable agent, wrong on purpose, holding the error — **CONFIRMED, and now we know why**

**[OBSERVED]** Nothing in the literature or on GitHub deliberately inserts a specific false belief
and defends it until the learner corrects it. The nearest approaches come at it sideways:
- **arXiv:2603.26142** — *machine unlearning* to surgically remove knowledge from weights, producing
  a genuinely novice agent, then measuring re-teaching. **[MEASURED-BENCH]** on a Python MCQ set.
  This is **suppression of knowledge**, not **insertion of an error**.
- **MathDial** (arXiv:2305.14536) — 3k dialogues where an LLM is *"prompted to represent common
  student errors"* from real transcripts. Scripted wrongness, dataset-scale, not live.
- GitHub: `teachable agent LLM learning by teaching` → **0 repos**; `protege effect AI` → **1 repo,
  0 stars, Korean** (`GOOHAESEUNG/moni`).

**[OBSERVED] The failure mechanism is now documented, which is the valuable part.** Two independent
findings:
- arXiv:2603.26142: LLMs *prompted* to act like novices **drift back to expert-level correct
  answers.** Prompting cannot hold an error.
- arXiv:2412.15226 (learning-by-teaching with ChatGPT, programming): knowledge gains and code quality
  improved but error-correction skill did **not**, because *"ChatGPT tends to generate correct code,
  reducing opportunities [for the learner] to practice debugging."* And arXiv:2309.14534: the
  agent's *"expansive knowledge... discourages learners from teaching."*

**[MEASURED-RCT] And the warning:** where LLM learning-by-teaching *has* been tested at reasonable
power — Ruffle&Riley, N=100 then N=200 — it **nulled both times** (§12.2).

**[INFERENCE] Verdict: the strongest of the four claims, with a caveat.** The ground is empty
*and* we now know it is empty for a reason: **error-holding is a weight-level or
architecture-level property, not a prompt-level one**, and the one team that took it seriously
reached for machine unlearning. Anyone who ships this via a system prompt will watch it decay
mid-session. And if we build it, §12.2 says we must power the study properly, because the adjacent
paradigm has already nulled twice.

### 13.3 (c) Deixis — **CONFIRMED, the emptiest of the four**

**[OBSERVED]** Literature: `"referring expression" AND "tutor"` → 0. `"pointing" AND "multimodal
tutor"` → 0. `"gaze" AND "tutoring"` → 7, none about an AI pointing at shared content. One partial
hit: **CoMAP** (arXiv:2604.06200), *"a Shared Visual Workspace for Designing Project-Based
Learning"* — a shared graph canvas with dual-modality AI support, but **the AI does not perform
deictic reference at a referent**. DEMO-level, no efficacy numbers.

**[OBSERVED]** Artifacts, my own search: `AI tutor whiteboard pointing` → **0 repos**. `screen share
tutor LLM` → **0**. `multimodal tutor pointing gesture` → **0**. `shared canvas AI tutor` → **2**,
both ≤10 stars.

**[INFERENCE] Verdict: fully confirmed, and it is the cleanest greenfield in the survey.** Nobody —
research or product, Western or otherwise — has built a tutor that says *"no, **that** term, the one
in the denominator"* while both parties look at the same object. Cross-reference **A4** (live
multimodal) and **A2** (interactive animation): the *capability* substrate now exists; the
*pedagogical* use of it does not.

### 13.4 (d) The refusal engine — **REFUTED. This ground was claimed during 2026.**

This is the finding that most requires the survey to change what it says.

**[MEASURED-BENCH] It is a named research target with benchmarks:**
- **Bridge** (arXiv:2310.10648, Stanford, code public): 700 real tutoring conversations; expert
  decision-conditioned responses **+76% preferred**; **random decisions −97%**.
- **Adversarial answer-leakage robustness** (arXiv:2604.18660): explicitly tests tutors against
  persuasive student jailbreaks, finds naive adversaries insufficient, **fine-tunes a dedicated
  adversarial-student agent as the benchmark core**, and proposes defences.
- **CSTutorBench** (arXiv:2607.05571): 11 models, 4B–120B, finds models *"struggle with... avoiding
  answer leakage"* even when surface tone and vocabulary are right; targeted prompt revision improved
  10/11.
- **EduGuard** (arXiv:2607.15738): overreliance control + claim-level verification; **direct-answer
  leakage measured at 9.8%**; pilot post-test 68.4%→81.2%, overreliance 38.0%→17.0% (N=10).
- **SocraticLM** (NeurIPS 2024, USTC + iFlytek).

**[OBSERVED] And it is a shipping artifact class**, all from the last ten weeks: five GitHub
repos matching `socratic tutor refuse answer` (top 6★), plus `Flagrare/llm-tutor`'s **`cycles` help
budget with a daily-refill hook** — refusal as a resource constraint rather than a persona
instruction (§5.2) — plus `quzhi-ai/deep-learning`'s **`不要用于` routing-scope refusal** (§5.4).

**[INFERENCE] Verdict: refuted as empty ground, and we should be glad.** "Answer leakage" is now a
*measured quantity with a benchmark*, which is exactly the maturation this survey should want.
**Our defensible position is not "we invented refusal." It is a narrower and better one:** refusal is
currently implemented as (i) a persona, (ii) a fine-tune, or (iii) a budget — and **none of these
is conditioned on a learner model**, because §12.4 says the model cannot reliably tell whether the
student is wrong. **The unclaimed part is calibrated refusal: deciding not to answer *because of
what this specific learner has previously demonstrated*, with the decision auditable.** That claim
survives contact with the evidence. The broad one does not.

### 13.5 Two additions to the empty space

**(e) Measurement of any of it.** **[INFERENCE, from the whole registry]** Of every artifact in §10,
**exactly one open system has a real learning-outcome RCT**: OATutor (N=274, PLOS ONE). LearnLM has
preference margins, not outcomes. Khanmigo has SWOT analyses and posters. The entire agent-skill
class has nothing. Every mechanism in §5 — help budgets, struggle windows, graduation conditions,
restate-before-correct — is **unmeasured**. A survey that ships one properly-powered comparison of
a *stateful* against a *stateless* tutor would be the only such thing in existence.

**(f) A portable learner-model format.** **[OBSERVED]** Runestone's state is in its own database;
PrairieLearn's in its own; `Tov-learn`'s in `~/skill-tutor-tutorials/*.md`; `llm-tutor`'s in
`~/.claude/llm-tutor/state.json`. **There is no interchange format, no schema, no way for a learner
to carry their model between systems, and no way to audit it.** `Tov-learn`'s human-readable
append-only Markdown is the closest thing to a good answer and it is a 34-star hobby project.
**[INFERENCE]** This is the plumbing problem whose absence guarantees every system re-learns the
learner from zero. It is unglamorous, fully unclaimed, and probably more consequential than three of
the four original claims.


---

## 14. Structural lessons for a 100-page survey

### 14.1 How the best of these organise

**[OBSERVED]** Four organisational patterns are worth stealing, and one is worth stealing *for the
survey itself*.

**Pattern 1 — the symmetric unit (CS336).** Every assignment is the same five objects: spec ·
`adapters.py` interface · test suite · numeric snapshot · leaderboard. Because the unit is
identical, a reader who learns to navigate one navigates all five, and a maintainer can replace one
without touching the others. **[INFERENCE]** The load-bearing property is that *the checker is part
of the unit*, not a separate appendix.

**Pattern 2 — the symmetric chapter (Raschka; and, to its credit, §1's artifact).**
`rasbt/LLMs-from-scratch`: chapter notebook · `exercise-solutions.ipynb` · quiz items · CI.
`xiaol/Harnessing-LLM-Skills`: motivating case · concepts · build · Harness Lab · failure modes ·
reflection artifact · exercises + system-design extension. Both hold the shape for 7 and 20 chapters
respectively. **[INFERENCE]** A survey with 27 sections needs this more than either of them did.

**Pattern 3 — functions with declared pre/post conditions (Mr. Ranedeer).** `[Curriculum]`,
`[Lesson]`, `[Test]`, `[Question]`, each with explicit entry state, steps, and a stop condition
(`<stop your response> <wait for student response>`). **[INFERENCE]** It is a state machine written
in English. That it was fragile in execution does not make it wrong as *specification style* — it
is far more precise than any prose description of a tutoring loop in the literature.

**Pattern 4 — dated decision records, separated from research notes (`Flagrare/llm-tutor`).** This
is the one I would adopt for our own survey. **[OBSERVED]** The repo separates:

```
docs/research/01-how-boots-actually-works.md
docs/research/02-llm-tutor-landscape-2026.md
docs/research/03-pedagogy-and-curriculum-theory.md
docs/research/04-gamification-evidence.md
docs/research/05-anti-dependency-design.md
docs/decisions/2026-06-02-tutor-start-and-gamification.md
docs/decisions/2026-06-03-statusline-integration-architecture.md
```

**Numbered research (what we found) vs. dated decisions (what we chose, and when).** **[INFERENCE]**
A 5-star hobby repo has better epistemic hygiene than most published work in this area, because when
a finding expires you can trace exactly which decisions rested on it. Given §12.1 — that our
load-bearing Bastani number is now under formal dispute — we need precisely this.

### 14.2 What makes an AI-learning artifact age well vs. rot in six months

Derived from the thirteen graveyard entries (§9) and the survivors. **[INFERENCE]** throughout,
grounded in the observations cited.

**Rot Rule 1 — Never make a vendor behaviour load-bearing.** Mr. Ranedeer implemented its learner
model as base64 in a Code Interpreter transcript, its persistence as a sandbox file, its
verification as a Python call, and its pacing as a request to stop generating. All four were
requests to *one model with one tool surface*. All four decayed. 29,606 stars conferred no immunity.
The survivors (CS336's numpy snapshots, Raschka's pytest, §1's stdlib scripts) depend on things that
cannot change their mind. **Corollary: a prompt is not a mechanism; it is a request for a mechanism.**

**Rot Rule 2 — Reproducibility is bought by subtraction, not by infrastructure.** §1's artifact hit
**16/16 byte-identical reproduction** against F3's 4.03% baseline for published notebooks, using no
infrastructure at all: no external deps, no randomness, no network, no GPU, no data download, tiny
deterministic inputs, committed plain-text outputs. **This is also, exactly, the profile that ports
to Pyodide (§7.2).** The same subtraction buys durability *and* browser-native execution. Take it.

**Rot Rule 3 — Ship the checker with the claim, or the claim decays into prose.** CS336 ships
snapshots. Raschka ships solutions and CI. Quarto Live ships `.solution_code` introspection. §1's
artifact ships scripts *without assertions* — and so nothing in it can ever fail, which means nothing
in it can ever be known to have broken. **A survey chapter with no failing condition is a chapter
that rots silently.**

**Rot Rule 4 — Watch the prose-to-executable ratio.** §1.5: 64 prompt scaffolds, 3 Python blocks, in
57,000 words of an ML course. **[INFERENCE]** The ratio is diagnostic. When an artifact's verifiable
content lives in a directory the prose merely *points at*, the prose is free to drift from it, and
will.

**Rot Rule 5 — Date every capability claim, and name the model.** Everything in this section
that broke, broke because a capability claim had no timestamp. LLM101n's syllabus is undated and
therefore reads as current two years after freezing. Mr. Ranedeer's *"Recommended: GPT-4 with Code
Interpreter"* is now archaeology. **[INFERENCE]** Our survey should carry, per claim, the model
generation and date it was true of — otherwise every capability statement silently converts into a
false present-tense claim.

**Rot Rule 6 — Build learner-side memory, not just author-side memory.** §1.7's inversion —
`BOOK_SUMMARY.md` for the writing agent, nothing for the reader — recurs across §4's ~501-repo
cluster (nine author-side skills, one teaching skill). **[INFERENCE]** It is the field's
characteristic mistake and it is easy to make, because author-side memory pays off during
construction and learner-side memory only pays off after shipping.

**Rot Rule 7 — Name the termination condition.** Almost nothing in this section says what *done*
means. The exceptions are instructive: `quzhi-ai/deep-learning` — done is *"every checklist item
ticked and the learner can restate the key ones in their own words and produce counterexamples /
edge cases"*; `llm-tutor`'s Explicit Graduation — *"the tool explicitly tells the learner they no
longer need the tool."* **[INFERENCE]** An artifact with no termination condition cannot be assessed,
cannot be finished, and cannot tell whether it worked.

**Rot Rule 8 — Do not infer capability from adoption.** mdBook 22,014★ cannot execute Python.
Quarto Live 259★ does client-side execution *with real grading*. LLM101n 37,504★ is two files.
Mr. Ranedeer 29,606★ is a discontinued prompt. **[MEASURED-BENCH, from §10]** In this registry, star
count and capability are close to uncorrelated. Cite artifacts by what they do, never by their
popularity.

**Rot Rule 9 — Audit the substrate you are standing on.** Binder disclaims reliability and caps a
book at 100 simultaneous readers. GitHub Classroom's autograder is archived with *"no roadmap."*
nbgrader has an 18-month release gap and 269 open issues. **[INFERENCE]** For each dependency the
survey's reference implementation takes, record: who funds it, when it last released, and what the
fallback is.

### 14.3 The positioning that survives this section

**[INFERENCE]** Three sentences, each defensible against everything above:

1. **Not "AI-native textbook"** — that phrase names ~501 Docusaurus-plus-RAG repos and is saturated
   (§4, §11.6).
2. **Not "we invented refusal"** — answer leakage is a benchmarked quantity as of 2026 (§13.4).
3. **The claim that survives:** *the field has built mechanism without measurement, and author-side
   memory without learner-side memory.* The unclaimed ground is **calibrated, learner-conditioned,
   auditable behaviour** — refusal, difficulty, and error-holding decided from a persistent record
   of what *this* learner has demonstrated — **plus the study that shows it matters.** Exactly one
   open system in this registry has a learning-outcome RCT (§13.5).

---

## 15. Handoff

**To B2, F1, F2, H1, E1 — action required.** Bastani et al. (PNAS 2025) now carries a **Correction**
(`10.1073/pnas.2518204122`, **content UNREACHABLE — 403**), a formal design critique
(`10.2139/ssrn.4898213`), and a counter-study (`10.2139/ssrn.5929576`). The −17% figure must not be
cited as settled without these. §12.1.

**To F3.** §1.4 supplies a MEASURED counterpoint to the 4.03% notebook-reproducibility figure:
16/16 byte-identical, achieved purely by dependency subtraction. Rot Rule 2. Also: §7.3's
consistency-vs-correctness distinction (marimo) belongs on F3's ladder, one tier below execution.

**To F5 (learner model).** §13.1 and §13.5(f): the capability exists in Runestone/PrairieLearn, was
dropped by the LLM stack, is being rebuilt in the agent-skill class, has **never** been measured
against a stateless baseline, and **has no interchange format**.

**To F2 (beyond the tutor).** §12.4's TutorGym result — *"none did better than chance at labeling
incorrect actions"*, against human-like learning curves for LLMs-as-students — is the strongest
architectural argument in the survey for putting the model in the learner's seat.

**To F10 (ELI ladder).** §5.4: `quzhi-ai/deep-learning` independently derived a four-rung ladder
(ELI5 / middle-school / undergraduate / new-professional) with a calibration rule. Independent
convergence is evidence; cite it.

**To C2 (assessment).** §5.4's MCQ position-shuffling rule; §10.5's EduGuard leakage metric (9.8%);
§7.4's Quarto Live `.solution_code` grading as the only browser-native grading substrate.

**To H1 (SELPA).** §5.2's admission: *"Withholding answers presupposes the learner has baseline
capacity to struggle productively"* — a first-generation student who must pass to keep a scholarship
*"does not have the luxury of deliberate practice philosophy."* **A refusal engine designed without
the margin in mind is an equity hazard.** Design refusal at the margin first.

**To G2 (agent village).** §2.1's Eureka Labs spec is the competing architecture and it is
**unspecified**. Our "certified agent" requirement (§41 of the ledger) is a strictly stronger claim,
and §12.4 supplies the eval that any tutoring agent must pass: error *detection*, not error
*generation*.

### Methodological limitations, stated plainly

- **OpenAlex was quota-exhausted** for this session (*"Insufficient budget... resets at midnight
  UTC"*) — **UNREACHABLE**. arXiv and Semantic Scholar were heavily rate-limited (HTTP 429);
  coverage from them is partial. **Crossref, the GitHub API, and direct raw-file fetches were the
  reliable channels**, and most primary-artifact claims here rest on those.
- SSRN (403), PNAS (403), openai.com study-mode (403), anthropic.com/news/claude-for-education
  (404), executablebooks.org (429), next.jupyterbook.org (connection refused), and
  r-wasm WebR limitations docs (403) were all **UNREACHABLE**. Nothing behind them is guessed at.
- GitHub repository-search totals are AND-over-terms and therefore **conservative lower bounds**; a
  zero result means "no repo matches all these terms," not "no such repo exists." I have said so
  wherever a zero is load-bearing.
- Numbers I could not verify and have explicitly *not* restated: d2l's "500 universities"; the
  "Khanmigo refuse-to-answer nearly double the gains" claim relayed by `llm-tutor`; Bastani's
  study country; Pyodide startup latency; the content of the PNAS correction.

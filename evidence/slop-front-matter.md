# Adversarial prose review — front matter

**Scope:** `README.md`, `docs/index.html`, `docs/thesis.html`, `docs/deck.html`.
**Method:** markup and `<script>`/`<style>` stripped; counts run over the prose only.
Word counts used throughout: README 1,180 · index 2,982 · thesis 6,361 · deck 1,346.
**Date:** 2026-07-29. Not a fact-check and not a copy-edit.

---

## VERDICT

This is written by someone who knows the subject — the numbers are load-bearing, the nulls are
volunteered, and nothing here is padded with the standard vocabulary (`delve`, `tapestry`,
`crucial`, `myriad`: zero hits in all four files). What it is not is written by someone who has
read it aloud. The author has one rhetorical move — *state a negation, then supply the correction
as a second clause* — and runs it about ten times across these four files and sixty-plus times in
`paper.html`. Around it sits a small cluster of supporting tics: paragraphs that open on the
fragment "Which …" (six in the thesis), the possessive "the honest version / answer / prior /
counter-case" (five), "the whole problem / strategy / effect / landscape / frame" (eight), and
"nobody has built / measured / studied / done it" (twenty-six, sixteen in the thesis alone). None
of these is wrong in isolation. At this density they stop reading as judgement and start reading
as cadence, and cadence is the thing a machine produces for free. The second failure is
emphasis: 2.4–2.9 bold spans per 100 words, which is a bold span roughly every forty words, at
which point bold means "sentence" rather than "this one matters." The deck survives this review
almost intact; the thesis is where the tics concentrate; `index.html` has one verbatim
duplicated card. Fix the negation beat, halve the bolding, and this reads as a person.

---

## FREQUENCY TABLE

### Sentence-opening words (all four files; total sentences: README 55, index 168, thesis 379, deck 78)

| Opener | README | index | thesis | deck | total | what it reveals |
|---|---:|---:|---:|---:|---:|---|
| `The` | 9 | 28 | 87 | 22 | **146** | 23% of thesis sentences open `The`. Definite-article default. |
| `A` | 4 | 3 | 28 | 3 | 38 | — |
| `It` | 4 | 4 | 21 | 2 | **31** | Almost all copular: `It is …`. Nearly all are the second half of the negation beat. |
| `What` | 1 | 10 | 12 | 4 | 27 | Headers announcing rather than informing. |
| `That` | 4 | 2 | 14 | 0 | 20 | `That is the …` ×7 in the thesis; anaphoric summary sentence. |
| `And` | 2 | 1 | **15** | 0 | 18 | Sentence-initial `And` as rhythm, not connective. |
| `Which` | 0 | 1 | **8** | 0 | 9 | **Six open a paragraph as a sentence fragment.** The signature tic. |
| `So` | 1 | 1 | 5 | 0 | 7 | — |

### Constructions

| Construction | README | index | thesis | deck | total |
|---|---:|---:|---:|---:|---:|
| **`X is not Y. It is Z.`** (the beat) | 2 | 2 | 6 | 2 | **12** |
| `Which …` opening a paragraph/fragment | 0 | 1 | **6** | 0 | 7 |
| `the honest {version, answer, prior, counter-case, field-wide number}` | 0 | 2 | 3 | 0 | **5** |
| `is exactly the / which is exactly why` | 0 | 0 | **4** | 0 | 4 |
| `the whole {problem, strategy, effect, landscape, frame, corpus, time}` | 1 | 2 | **6** | 0 | 9 |
| `nobody has {built, measured, studied, done it}` | 2 | 5 | **16** | 3 | **26** |
| `worth {stating, doing, having, running, taking}` | 0 | 1 | **7** | 1 | 9 |
| `It is worth stating precisely` | 0 | 0 | 1 | 0 | 1 |
| Enumerative header (`Two/Three/Four X that …`) | 1 | 0 | **6** | 3 | 10 |
| Paragraph ending on a ≤9-word closer | — | — | **28 / 118 paras (24%)** | — | — |

### Density

| | README | index | thesis | deck |
|---|---:|---:|---:|---:|
| Em-dashes per 100 words | 1.02 | 1.51 | **1.79** | 1.63 |
| — of which `— and` (dash as joint) | 3 | 8 | **22** | 4 |
| Bold spans per 100 words | 2.37 | 2.58 | **2.45** | **2.90** |
| Bold + italic per 100 words | 3.05 | **3.55** | 3.21 | 3.42 |

Reference points: literate non-fiction runs roughly 0.2–0.5 em-dashes per 100 words. The thesis
runs 3.5–9× that. At 2.45 bold spans per 100 words a reader hits emphasis every ~40 words.

### Duplication

- **README ∩ index:** 6 runs of ≥12 identical words, longest **39 words**.
- **thesis ∩ deck:** 6 runs, longest 20 words. (Defensible — deck is the compressed thesis.)
- **index internal:** 23 repeated 8-grams, all from **one 27-word block appearing twice on the
  same page** (lines 128–133 and 232).
- **thesis internal:** the 74.4% / 44.3% passage is stated at near-full length twice (§5 lines
  198–213, §6 lines 249–253).

---

## KILL LIST

Ranked by what makes an expert reader stop.

---

### 1 · `docs/thesis.html:228` — the single worst line

> "The closest existing template is what happened in coding. **It is worth stating precisely,
> because the analogy holds in three places and fails in one — and the one where it fails is the
> whole strategy.**"

Three tells in nineteen words: "It is worth stating precisely" (announcing that you are about to
be precise is the opposite of being precise), a table-of-contents preamble that tells the reader
the shape of the next 600 words instead of starting them, and "is the whole strategy" — the
eighth "the whole X" in the file.

**Rewrite:** "The closest template is what happened in coding. It transfers in three places and
breaks in one, and the break decides the strategy."

---

### 2 · The negation beat — 12 instances across the four files, 60+ in `paper.html`

The most damaging finding, because once a reader notices it they cannot stop noticing it.

| File · line | Quote |
|---|---|
| `README.md:32` | "A twenty-fold spread, and the axis **is not** task difficulty. **It is** how good the check is." |
| `README.md:71` | "What limits polymathy **is not** learning rate. **It is** the fixed cost of orientation" |
| `docs/thesis.html:123` | "the book **is not** bad. **It is** a fixed artifact" |
| `docs/thesis.html:401` | "The recursive loop **is not** a separate play. **It is** what the verifier unlocks." |
| `docs/thesis.html:644` | "This **is not** a scale argument. **It is** structural" |
| `docs/thesis.html:662` | "the binding constraint in this market **is not** appetite — **it is** the gate" |
| `docs/index.html:194` | "the K-12 → postgraduate span **is not** a difficulty gradient. **It is** a reversal" |
| `docs/index.html:290` | "**is not** a smaller version of that result. **It is** a different question" |
| `docs/deck.html:124` | "the effect **is not** smaller. **It is** gone." |
| `docs/deck.html:145` | "the axis **is not** difficulty. **It is** how good the check is." |

The construction earns its keep exactly once — when the reader genuinely holds the wrong belief
being negated. `deck.html:124` is that case and should stay. The other nine are the author
warming up before saying the thing.

**Rewrites:**
- `README.md:32` → "A twenty-fold spread, and it tracks the quality of the check, not the
  difficulty of the task."
- `thesis.html:401` → "The recursive loop is what the verifier unlocks, not a second play
  alongside it."
- `thesis.html:644` → "The argument is structural rather than about scale, and it follows from
  what the asset is."
- `index.html:194` → "So the K-12 → postgraduate span is a reversal, not a difficulty gradient"
  — keep one clause.

---

### 3 · `docs/thesis.html` — six paragraphs opening on the fragment "Which …"

> `:98` "**Which is the whole problem stated in one line.**"
> `:215` "**Which yields the structural argument:**"
> `:278` (h3) "**Which yields the actual strategy**"
> `:316` "**Which retires a whole category of pitch.**"
> `:389` "**Which forces a three-tier fitness function**, and the middle tier is the thing this whole page is about:"
> `:652` "**Which has a sharp consequence:** no single publisher can build this"

A dangling relative pronoun starting a paragraph is a deliberate effect. Six of them in one
document is a template. Two of the six ("Which yields the structural argument:", "Which yields
the actual strategy") are also empty transitions — they carry no content, only the promise of
content.

**Rewrites:** delete `:215` and `:278` outright; the following block is the argument and does not
need to be introduced. `:98` → "That is the whole problem in one line." `:316` → "It retires a
whole category of pitch." `:389` → "A three-tier fitness function follows, and the middle tier is
this page's subject:" `:652` → "The consequence is sharp: no single publisher can build this"

---

### 4 · `docs/index.html:128–133` vs `:232` — 27 words duplicated verbatim on the same page

> `:130` "In the randomised trial that settles it, both arms revised instruction more often — and
> **only the arm told *what to change*** moved achievement. **Dashboards, streaks, mastery bars
> and adaptive difficulty are all the arm that measured more and moved nothing.**"

> `:232` "Both arms revised programs more often; **only the arm told *what to change*** moved
> achievement. **Dashboards, streaks, mastery bars and adaptive difficulty are all the arm that
> measured more and moved nothing.**"

Two hundred lines apart under two different headings ("Three findings" and "Findings that change
what you build"), with the second contributing nothing the first did not. This is the most
machine-like artefact on the site: a card generated to fill a grid slot.

**Rewrite:** cut the `:232` card entirely and let the grid run to eleven, or replace its body with
the consequence rather than the finding: "The rule is the product. If a dashboard cannot name the
next instructional move, it is the arm that measured more and changed nothing — and no amount of
resolution fixes it."

---

### 5 · `docs/thesis.html` §5 and §6 — the same trial narrated twice

`:198–213` establishes 74.4% / 3,617 / 44.3% and the reading. `:249–253` re-establishes it:

> "In the one trial that measured a human-supervised AI tutor at scale, tutors **accepted 74.4% of
> 3,617 drafts unedited** — and **44.3% of their edits were slowing the model's questioning
> down.**"

The internal 8-gram scan finds the phrase "trial that measured a human-supervised AI tutor" twice.
Two sections apart in a 6,300-word page, a reader remembers.

**Rewrite:** §6 should reference, not restate — "The same trial supplies it: 74.4% accept, and
44.3% of edits slowing the questioning down (§5). That is *accept · reject · edit* on a
pedagogical decision."

---

### 6 · `docs/thesis.html:690` — a general law manufactured from one project's two halves

> "That finding came from the supply side, asking what is missing for a school. The ecosystem
> strategy arrives at the same object from the demand side. **When a gap is visible independently
> from both directions, it is usually real.**"

Epistemic slop of the most consequential kind. The two "directions" are two workstreams of the
same survey, run by the same authors under the same priors — the definition of *not* independent.
And "it is usually real" is a hedged non-claim: no evidence could contradict it. A document whose
entire pitch is *we publish our corrections* cannot afford this sentence.

**Rewrite:** "The supply-side sweep and the ecosystem argument name the same gap. They share
authors and priors, so this is corroboration rather than independent confirmation — but it is the
only item that appears in both."

---

### 7 · The "honest X" possessive — 5 instances

| File · line | Quote |
|---|---|
| `docs/thesis.html:123` | "**The honest version of the problem**, then: the book is not bad." |
| `docs/thesis.html:268` | "**The honest answer** is that you cannot know from the acceptance." |
| `docs/thesis.html:759` | "And **the honest prior** on the adjacent claim:" |
| `docs/index.html:364` | "**The honest counter-case** to this whole survey:" |
| `docs/index.html:405` | "a chart bar labelled *'the honest field-wide number'*" |

One of these is a virtue. Five is a mannerism, and it implies the unmarked sentences were the
dishonest version. `index.html:405` is a quotation of the project's own past error and must stay.

**Rewrites:** `thesis:123` → "So, exactly: the book is not bad." `thesis:268` → "You cannot know
from the acceptance." `thesis:759` → "The prior on the adjacent claim is bad:" `index:364` → "The
counter-case to this whole survey:"

---

### 8 · `README.md:20` and `docs/thesis.html:141` — the one banned word that got through, twice

> `README.md:20` "That is not an isolated weakness. **It explains the whole reliability
> landscape.**"
> `docs/thesis.html:141` (h2) "3. **The rule predicts the whole landscape**"

Metaphorical `landscape` is the single most recognisable machine-prose noun in English, and it is
doing no work in either place — both mean "the spread of results", which is a phrase the document
already uses well ("A twenty-fold spread").

**Rewrites:** `README:20` → "That is not an isolated weakness. It explains the spread." (delete
the preceding negation too — see #2.) `thesis:141` → "3. The rule predicts where agents work and
where they collapse" — which is literally the first line of the section beneath it.

---

### 9 · `docs/thesis.html` — three broken cross-references and a numbering collision

- `:349` `<h2>9. Which moats survive a frontier release</h2>` and `:368` `<h2>9. The recursive
  loop</h2>`. **Two sections numbered 9, no section 8.** The page advertises 21 sections and has
  20 headings.
- `:535` "because **§10** shows that the engagement machinery everyone ships is the weakest cell"
  — §10 is *Auto-research*. Gamification is §12.
- `:623` "That is the three-tier fitness function from **§7**, fully instantiated" — §7 is *The
  economics, corrected*. The three-tier table is in the second §9.
- `:636` "what **§21** calls **correlated pedagogical error**" — §21 is *The one-line version* and
  does not mention it. The term is defined in §16 itself.

Prose-critic relevance: a reader who follows one cross-reference and lands somewhere unrelated
stops believing the internal structure was authored. Fix the numbering first; the references
follow.

---

### 10 · Substitution-test failures — sentences that survive a topic change

| File · line | Quote | Why it fails |
|---|---|---|
| `docs/thesis.html:723` | "**If it were easy it would not be a moat.**" | True of every business. Pure decoration. |
| `docs/thesis.html:242` | "**This is the test of a real moat: when the frontier improves, does your advantage widen or evaporate?**" | Restates §9's table before the table. |
| `docs/thesis.html:331` | "It does not mean the thesis is wrong. **It means the leverage has to be demonstrated, not assumed**" | Applies to any unproven claim. |
| `docs/thesis.html:518` | "**That is the sharpest structural fit in this document.**" | Self-assessment, unfalsifiable, and the document should not rank itself. |
| `docs/thesis.html:702` | "**and the cheapest strategic move on this page.**" | Same move, forty lines later. |
| `docs/index.html:394` | "**The claim that should make you suspicious of any survey is that it got everything right.**" | Generic epistemic virtue-signal; the *next* sentence ("This one did not, and the record is the point") is the actual claim and is good. |

**Rewrites:** cut `:723`, `:242`, `:518`, `:702` and the first sentence of `index:394` with no
replacement — every one is followed immediately by the specific version of itself. `:331` → "The
leverage ratio has to be reported, monthly, by anyone claiming it."

---

### 11 · `docs/thesis.html:657` — false precision

> "it is why the value is **superlinear in the breadth of the ecosystem** rather than in the size
> of any one partner."

"Superlinear" is a claim about a functional form. Nothing on this page or in the survey measures
one. It reads as a number where there is no number — on a page whose stated discipline is
"Numbers that could not be verified are not here" (`:62`).

**Rewrite:** "…which is why breadth of the ecosystem matters more than the size of any one
partner. How much more is unmeasured."

---

### 12 · `docs/thesis.html:301` — unattributed manufactured balance

> "**And the data-moat thesis is contested even in coding. A serious reading is that** distribution
> and product craft did the work and the model followed."

"A serious reading is that" attributes a position to nobody. Everywhere else this document names
its source or stamps `OBSERVED` / `INFERENCE`; here it launders an objection into existence so it
can be conceded. The concession itself is good and worth keeping — it needs an owner or a label.

**Rewrite:** "And the data-moat thesis is contested even in coding: the competing account is that
distribution and product craft did the work and the model followed. `INFERENCE` — we have not
found this settled either way."

---

### 13 · Bold density — 2.4–2.9 spans per 100 words, all four files

`docs/thesis.html:123–126` is representative: 45 words containing two `<strong>` runs, one `<em>`,
and three em-dashes.

> "**The honest version of the problem, then:** the book is not bad. It is a fixed artifact,
> written at one altitude, for a reader who does not exist, with no memory, no schedule, no
> diagnosis and no feedback — and it has been carrying the entire load in every setting where the
> teacher is absent, overloaded, or teaching thirty other children."

**Rule to apply, mechanically:** at most one bold span per paragraph, and only on a *number* or on
a claim the reader is meant to quote back. On the current text that is roughly a 60% cut: thesis
156 → ~60, index 77 → ~35, deck 39 → ~20. Nothing else about the prose need change for the
remaining emphasis to start working again.

---

### 14 · Tidy-able: enumerative headers that announce rather than inform

`docs/thesis.html` h3s: "Three parts transfer directly" `:247` · "Two ways the analogy could
mislead you" `:294` · "Two market facts that change where you look" `:336` · "Four more things
line up in the same direction" `:520` · "Two things the metaphor should also warn you about" `:625`
· "Why this composes with everything above" `:613`. Six of twenty-two. Each tells the reader how
many items are coming and nothing about what they are.

**Rewrites:** `:247` → "The inner loop, the narrow task, the deprioritised model". `:294` →
"Lower volume, and a contested premise". `:336` → "The relief money never arrived, and the TAM has
no source". `:520` → "Cold start, counterfactual, motivation, syllabus". `:625` → "Publishers
fought Amazon, and one mentor's errors are correlated". `:613` → delete; the numbered list under
it composes fine unannounced.

---

### 15 · Minor, thesis only: "nobody has X" as the recurring argumentative move — 16 instances

`:58, :112, :185 (×2), :249, :289, :304, :318, :366, :371, :459, :559, :607, :668, :678, :732`.
Every one is true and most are load-bearing; the problem is that the *same* rhetorical shape
carries the whole document — value is repeatedly established by absence rather than by
mechanism. Two of them are back-to-back at `:366` ("it is the one nobody is building") and `:371`
("the reason nobody has it is not ambition"), and `:732` ends a section on the bare fragment
"**Nobody has done it.**"

**Rewrite (`:366`):** the sentence "One row survives cleanly, and it is the one nobody is
building" duplicates the table directly above it, which already says so. Cut it.

---

## WHAT IS CLEAN

- `docs/thesis.html:139` — "Sampling without a selector is noise. Execution without a test is
  output. Persistence without a schema is a transcript. Absence without a verifier is unsupervised
  drift." Four clauses, four different contents, no filler item. This is what the rest of the
  document's parallelism is imitating.
- `docs/thesis.html:261` — "In coding, the accept signal is validated within seconds. In tutoring,
  you find out in six weeks." The whole strategic problem in twenty words, no bold needed.
- `docs/thesis.html:244` — "`OBSERVED` — the pattern is inferred from public product behaviour, not
  from disclosed internals. Treat the mechanism as the claim; the company is the illustration."
  Genuinely rare epistemic hygiene, and stated without congratulating itself.
- `docs/index.html:172–176` — the Bloom's-2σ figcaption. Names its own superseded number, says
  which review moved it, and gives the multiplier. Self-implicating and specific.
- `README.md:113` — "This survey got things wrong. The record of that is the reason to trust the
  rest of it." Two sentences, no hedging, does the work of a paragraph.
- `docs/deck.html` slides 12 and 14 — the three disqualifying questions and the two-column
  will/won't. Concrete, falsifiable, dated, and *self-applied*. The deck is the strongest artifact
  of the four and needs almost nothing.
- Zero hits across all four files for `delve`, `tapestry`, `realm`, `testament`, `crucial`,
  `pivotal`, `myriad`, `nuanced`, metaphorical `navigate`, `underscore`. The obvious register was
  successfully avoided; everything above is the subtler layer.

# Adversarial prose audit — the fourteen demo pages and a six-report sample

Scope: prose only. Header ledes, the three-panel orientation blocks, section headings,
in-page explanation, closing "what this proves / what it does not". CSS and JS ignored
except where a string is user-facing copy.

All counts below were produced by running them, not by eyeballing.

---

## VERDICT

### Demos — **pass on vocabulary, fail on template**

The vocabulary is genuinely, unusually clean. Across 1,958 lines of extracted demo prose:
`delve` 0 · `tapestry` 0 · `testament` 0 · `crucial` 0 · `pivotal` 0 · `myriad` 0 ·
`underscore` 0 · `realm` 0 · metaphorical `navigate` 0. `which is precisely` appears once,
`not merely` three times. Nobody needs to defend this word list.

The failure is structural, and it is exactly where the brief predicted. **Fourteen pages,
three panels each, one sitting, one template — and the template is visible.** The "How to
use it" panel is the same sentence machine fourteen times: 14/14 open with a bare
imperative, 12/14 pivot on a sentence-initial "Then", 11/14 contain "watch", and 11/14 run
the complete *imperative → Then → perception-verb* rhythm. Two of them
(`refusal-engine.html:63`, `connector.html:65`) are structurally interchangeable — you
could swap the nouns and not notice.

Worse, and separately: the honesty block — the single most important thing these pages do —
contains a **verbatim boilerplate sentence pair repeated on five pages across five
unrelated topics**. That is the substitution test failing in the one place the project
cannot afford it.

Three factual/editorial defects also land here: `index.html` miscounts its own gallery,
`textbook-teardown.html` ships with no "what this proves" block at all, and the number
`0.48` is used for two different effects on a single page.

### Reports — **clean, with one house verbal tic**

Held to the lower bar the brief asks for, and they clear it comfortably. The six sampled
reports do not read as one voice, do not follow one section skeleton, and every load-bearing
claim in the six carries an evidence label, a date, and a query that can be re-run. Heading
text across all forty is almost entirely non-repeating — the opposite of template
exhaustion.

One tic is corpus-wide and unmissable once counted: **`the honest ___` appears 133 times
across 39 of 40 files**, in 78 distinct noun forms. `which is precisely` (23 hits, 17 files)
and `not merely` (39 hits, 22 files) are the second and third. All three are cosmetic. **No
finding in the six sampled reports would mislead a reader.**

---

## FREQUENCY TABLE

### The fourteen orientation blocks (42 panels)

`index.html` has no orientation block; the other fourteen files each have exactly three panels.

#### "How to use it" — the template exhaustion exhibit

| Feature | Count |
|---|---|
| Opens with a bare imperative verb | **14 / 14** |
| Contains sentence-initial `Then` as the pivot | **12 / 14** |
| Contains `watch` | **11 / 14** |
| Contains `watch` OR `see` OR `read` | 13 / 14 |
| Full *imperative → Then → perception-verb* rhythm | **11 / 14** |
| Exactly 3 sentences | 9 / 14 (2 sentences: 3; 4 sentences: 2) |
| `and watch` as a clause-joiner | 8 occurrences |
| `and see` as a clause-joiner | 4 occurrences |

Opening verbs actually used (12 distinct across 14 — see WHAT IS CLEAN):
`Run`×2, `Generate`×2, `Accept`, `Answer`, `Change`, `Corrupt`, `Make`, `Read`, `Set`,
`Start`, `Step`, `Take`.

#### "What this is"

| Feature | Count |
|---|---|
| Opens with a verbless noun-phrase fragment (no page opens with a sentence) | **14 / 14** |
| Opens with the article `A` | **10 / 14** (`Two` 2, `The` 1, `One` 1) |
| Sentence count | 2 sents: 7 · 3 sents: 4 · 1 sent: 3 |

#### "Why it matters"

| Feature | Count |
|---|---|
| Contains a numeral/statistic anywhere | 9 / 14 |
| **Opens with a statistic in the first sentence** | **4 / 14** |
| Sentence count | 3 sents: 7 · 2 sents: 5 · 4 sents: 2 |

The brief asked specifically how many "Why it matters" panels open on a statistic. The answer
is 4 (`connector`, `eli-ladder`, `refusal-engine`, `teachable-agent`) — lower than the shape
of the panels suggests, because most bury the number in sentence two. That is the healthier
pattern; noting it as a non-finding.

#### Cross-panel

| Feature | Count |
|---|---|
| Em-dashes, all 42 panels | 32 total (what 10 · why 10 · how 12) |
| Panels containing ≥1 em-dash | 29 / 42 |
| `rather than` | 5 |
| Sentence-initial `And` / `But` / `So` | 3 total — **not a finding** |

### Section headings (87 `<h2>` across 15 files)

| Feature | Count |
|---|---|
| Match the numbered pattern `N · …` | 71 / 87 |
| **Of those, `N · The …`** | **45 / 71 (63%)** |
| `N · Why …` | 4 · `N · What …` 6 |

### Closing "what this proves / what it does not" (104 bullets, 13 files)

| Feature | Count |
|---|---|
| Bullets opening `That ` | 73 / 104 |
| **Files carrying the verbatim boilerplate pair** | **5** |
| Files with a `<strong>` bullet lead | 13 / 13, but on 1–3 arbitrary bullets each |
| **Files with no proves-block at all** | **1 (`textbook-teardown.html`)** |

The `That ` opener is grammatically governed by the panel heading ("What it does not prove:
*That* X") and is correct parallel construction. Not a finding.

### Demo vocabulary scan (1,958 prose lines)

Zero hits: `delve`, `tapestry`, `testament`, `crucial`, `pivotal`, `myriad`, `underscore`,
`realm`, metaphorical `navigate`, `seamless`, `leverage`, `unlock`, `empower`, `profound`,
`nuanced`, `multifaceted`, `cornerstone`, `paramount`, `at its core`, `it is worth noting`,
`discover`, `see how`, `remarkable`, `striking`, `stunning`, `powerful`.

Hits: `which is precisely` 1 · `not merely` 3 · `arguably` 1 · `robust` 2 (both statistical)
· `harness` 6 (all "test harness", technical).

### Reports — all 40, grep-only (no reading)

| Term | Files | Hits |
|---|---|---|
| **`the honest ___`** | **39 / 40** | **133** |
| `not merely` | 22 | 39 |
| `which is precisely` | 17 | 23 |
| `leverage` | 16 | 41 |
| `crucial` | 13 | 15 |
| `unlock` | 8 | 14 |
| `landscape` | 9 | 13 |
| `worth noting` | 7 | 8 |
| `the honest version` | 6 | 7 |
| `moreover` | 4 | 7 |
| `nuanced` | 4 | 6 |
| `navigate` | 4 | 5 |
| `furthermore` | 3 | 3 |
| `cornerstone` | 3 | 3 |
| `delve` / `tapestry` / `testament` / `pivotal` / `myriad` / `underscore` | **0** | **0** |

Report opening shapes (40 files): 22 open with a `>` blockquote, 6 with `## 0. …`, the rest
with a bolded label. Label families: `Thesis…` ×5, `Retrieval note` ×3, `Scope …` ×4,
`Why this section exists` ×3, `The claim under test / defends` ×4, `Purpose of this section`
×2, `Deliverable of this section` ×2, `Research constraint note` ×2.

Scaffold sections, of 40: `Negative and null results` 19 · `Sources`/`Bibliography` 24 ·
`Executive summary` 4 · `Handoff notes` 6 · `What I could not verify` 2.

---

## TEMPLATE EXHAUSTION

**1 · The "How to use it" panel is one sentence machine run fourteen times.**
11/14 execute *imperative → `Then` → perception-verb*. The generator that produced them is
still in the repo at `/home/eranti/learning-with-ai/evidence/gen-demo-orientation.py`, which
holds all thirteen original panels as a single Python dict and writes them in one loop. The
brief is not merely visible; it is committed.

**2 · The honesty block has become boilerplate.** Five pages close on the same two
sentences about five different topics. Detail in KILL LIST #2.

**3 · `N · The …` on 45 of 71 numbered headings.** The default heading move is "number,
middot, definite article, noun".

**4 · Every "What this is" panel is a verbless noun-phrase fragment, 10 of 14 starting
with "A".** Consistency is defensible for a gallery. Fourteen for fourteen with no variation
is a template.

**5 · The orientation blocks were bolted on top of ledes that already said the same thing.**
Four pages repeat their own lede a dozen lines later — `pivot-loop`, `teachable-agent`,
`patha`, `distractors`. Detail in KILL LIST #6.

**6 · Reports: template exhaustion is largely absent.** Heading text across forty files is
near-unique; the shared scaffolding is a bolded-label opener and a numbered `##` spine, which
is house style rather than exhaustion. The one real artefact is the retrieval-note boilerplate
(KILL LIST #12).

---

## KILL LIST

Ranked. File · line · quote · why · rewrite.

---

### 1 · `docs/demos/index.html:32` — the gallery miscounts itself

> `A survey that only describes techniques is a reading list. All thirteen demos`
> `here run in your browser — no server, no key, no sign-in — and each states`
> `plainly what it proves and what it merely illustrates.`

There are **fourteen**. `grep -o 'href="[a-z-]*\.html"' index.html | sort -u` returns 14
cards. `textbook-teardown.html` was added 2026-07-29 and the lede was never updated. This is
the first sentence a reader meets, on the page whose entire pitch is numerical honesty.

**Rewrite:** `All fourteen demos here run in your browser` — and, given the second half of
that sentence is currently false too (see #3), `and each states plainly what it proves and
what it merely illustrates` should not be restored until #3 is fixed.

---

### 2 · Five pages, one verbatim closing paragraph — the substitution test, failed

> `cbm-probe.html:285` · `That any of this teaches anyone anything. A demo shows a mechanism is buildable and coherent. It is not evidence that it teaches.`
> `distractors.html:254` · *identical*
> `felt-vs-real.html:248` · *identical*
> `pivot-loop.html:335` · *identical*
> `patha.html:344` · `That this teaches anyone anything. Even the parts that work are error-detection machinery, not instruction. A demo shows a mechanism is buildable and coherent. It is not evidence that it teaches.`

The last bullet of the "what it does not prove" list is the load-bearing sentence of the
whole gallery — the moment the page declines to oversell. It is the same sentence on
curriculum-based measurement, distractor generation, felt-learning, pivot rules, and Vedic
recitation. Nothing in it is about any of them. This is decoration in the one slot that
cannot be decoration, and a reader who opens two demos will spot it.

**Rewrite — make each one carry its own topic:**

- `cbm-probe.html:285` → `That the prescribed change is the right change. The 1991 trial validated one expert system, on paper-and-pencil reading probes, in one district, thirty-five years ago. The menu in §4 is assembled by analogy and has never been administered to a child.`
- `distractors.html:254` → `That a diagnostic option changes what anyone does with it. Generator B makes a wrong answer readable. Whether a teacher or a system reads it, and acts differently, is untested here and mostly untested anywhere.`
- `felt-vs-real.html:248` → `That failing the Null-Learner Test disqualifies a metric in practice. It disqualifies it logically. Every product on the market ships the failing metrics anyway, which suggests the argument is not the binding constraint.`
- `pivot-loop.html:335` → `That a slower loop teaches better than a fast one. This page shows the fast loop is mostly fitting noise. It does not show that waiting nine weeks helps a learner who is stuck in week two.`

---

### 3 · `docs/demos/textbook-teardown.html` — the newest demo has no honesty block

Thirteen of fourteen demos end on `<h2>What this proves / what it does not</h2>`.
`textbook-teardown.html` ends on `6 · What the learner leaves with` (line 200) and stops.
Its own header chips at lines 59–61 read `Checkers computed · Dialogue scripted · Shows a
documented null`, so the page knows it has scripted content — it just never says so in the
place a reader looks for it. Meanwhile `index.html:33–34` promises "each states plainly what
it proves and what it merely illustrates."

**Rewrite:** add the block. It has real material to work with:

```
<h2>What this proves / what it does not</h2>
  What it proves
  • That the fidelity invariants apply to a real textbook page and return specific,
    locatable flags rather than a general complaint.
  • That the quantifier checker and the numeric falsifier run, on your machine, against
    claims you type.
  What it does not prove
  • That the eight strategies are the right eight, or that the diagnosis selects
    correctly. The selection rule is hand-authored.
  • That the mentor's replies would survive a real model. They are scripted; the chips
    say so and this is the second place saying so.
  • That any of this repairs the limits misconception it opens with.
```

---

### 4 · `0.48` names two different effects on one page

> `textbook-teardown.html:139` · `<em>d</em> ≈ 0.48 while knowledge moves zero`  *(preference/felt-learning gap)*
> `textbook-teardown.html:242` · `ev:"g = 0.48 with expectancy · −0.02 without"`  *(learning-by-teaching, Kobayashi 2024)*

Two unrelated findings, same number, one page, no disambiguation. The collision is
corpus-wide: `research/raw/C3-slides-and-presentations.md:715` carries a **third**
`g = 0.48` (worked examples on maths, Barbieri et al. 2023). `index.html:59` and
`index.html:120` place the first two eight lines apart in the same gallery grid. A careful
reader will assume a typo; a careless one will assume they are the same result.

**Rewrite:** at minimum, disambiguate at the collision point —
`textbook-teardown.html:242` → `ev:"teaching-expectancy g = 0.48 · −0.02 without (unrelated to the d ≈ 0.48 above)"`.
Better: spell the construct out everywhere — `preference d ≈ 0.48`, `teaching-expectancy g = 0.48`.

---

### 5 · The interchangeable pair — template made visible in two panels

> `refusal-engine.html:63` · `Set <em>attempted</em> to no and watch every branch refuse to answer. Then switch the learner to explicit-instruction mode and see the logic <em>invert</em> —`
> `connector.html:65` · `Change a time zone or an availability window and watch the ranking reorder. Then toggle the EEF coefficient and see human contact move up the list.`

Identical skeleton: *[imperative] [control] and watch [thing] [verb]. Then [imperative]
[control] and see [thing] [verb].* Swap the nouns and neither reader would notice. Eleven of
fourteen panels run some version of this; these two are the clearest proof.

**Rewrite — break the rhythm on one of them.** `connector.html:65` →
`The ranking is a computation, so change its inputs: move a time zone, narrow an
availability window. Then find the EEF toggle. Flipping it moves human contact up the list,
because the 3:5 ratio is a literal coefficient and not a sentiment.`

---

### 6 · Four pages repeat their own lede a dozen lines later

> `pivot-loop.html:68` (lede) · `A tutor that changes method after three wrong answers is not adapting. It is <strong>fitting noise</strong>.`
> `pivot-loop.html:81` (Why it matters) · `A tutor that changes method after three wrong answers is not adapting — it is fitting noise, and this page computes exactly how often.`

Six shared 6-grams. Same for `teachable-agent.html:45–46` vs `:56` ("the gap between what
you meant and what you said is the entire pedagogical payload" — 5 shared 6-grams),
`patha.html:59–62` vs `:72` (7 shared), `distractors.html:65–66` vs `:77` (2 shared). The
orientation block was generated separately and inserted after `</header>`, so it never saw
the lede it now sits two inches beneath.

**Rewrite:** the orientation panel should advance, not restate. `pivot-loop.html:81` →
`<b>Why it matters</b><p>Worse than the noise itself: <b>measurement alone is inert</b>. In
the randomised trial both arms revised instruction more often, and only the arm told
<em>what to change</em> moved achievement. A faster loop and a better dashboard are the same
non-intervention.</p>` — the lede already made the noise point.

---

### 7 · Three pages each claim to be the most important one

> `cbm-probe.html:77` · `The load-bearing trial in this whole survey.`
> `pivot-loop.html:242` · `The load-bearing finding, and the reason a dashboard is not a product.`
> `felt-vs-real.html:70` · `This is the central finding of the whole survey.`
> `index.html:119` · `The central finding of the whole survey, made tangible`

`cbm-probe` and `pivot-loop` are pointing at the **same** Fuchs, Hamlett & Stecker 1991
trial and both call it the load-bearing one, in different words, on different pages.
`felt-vs-real` and `index` award the title to something else entirely. A reader who visits
three demos is told three times that they have arrived at the centre.

**Rewrite:** pick one. Give `felt-vs-real` "the central finding" (the index already agrees),
and demote the other two to their actual scope. `cbm-probe.html:77` → `The trial that
separates measurement from instruction, and the one this project leans on hardest.`
`pivot-loop.html:242` → `The finding that turns a dashboard from a product into a
prerequisite.`

---

### 8 · Paragraph-final punch fragments, and one that congratulates the author

> `deixis.html:71` · `That difference is the whole argument.`
> `eli-ladder.html:206` · `This is the whole argument for enforcing the rule at authoring time`
> `patha.html:73` · `This is what publishing a falsification looks like.`

The first two are the same rhetorical move — a short final sentence claiming totality — used
twice with the identical phrase "the whole argument". The third is worse: it is an
orientation panel, telling the reader how to feel about the authors' integrity, in the slot
reserved for telling them which button to press. The falsification is genuinely admirable
and `patha.html` §5 makes the case properly; the panel does not need to take a bow.

**Rewrite:** `deixis.html:71` → `— the sentences are identical, and the load on your working
memory is not.` (drop the final fragment; the clause already lands it).
`patha.html:73` → `Then read §4, which reports our own benchmark: <b>87.5%/87.5%</b> and
<b>100%/100%</b>, exactly at chance, losing to plain self-consistency by 18.8 and 43.8
points.` (stop there — the numbers are the argument).

---

### 9 · `cbm-probe.html:78` — the page admires its own output

> `Run the loop in <em>dashboard only</em> mode and watch it produce a beautiful graph and no instruction.`

"Beautiful" is the page marketing its own chart, in a demo whose entire thesis is that
beautiful charts are the arm that did nothing. The irony is presumably intended; it still
reads as the copy admiring itself, and the chart is a plain goal-line plot.

**Rewrite:** `…and watch it produce a clean trend line and no instruction. That is the arm
of the trial that moved nothing.`

---

### 10 · `docs/demos/*.html` — 45 of 71 numbered headings are `N · The …`

Representative run from one file: `1 · The corpus` · `2 · The controls` ·
`3 · What the three rungs cost and catch` · `4 · Which rung catches which mutation` ·
`5 · The null result…` · `6 · The corpus figures…` (`grounding-ladder.html:74–175`).

Cosmetic, but it is the same default reaching for the same construction 45 times.

**Rewrite:** vary where the section actually has a verb in it. `grounding-ladder.html:74`
`1 · The corpus` → `1 · Twenty formulas, five ways to break each`.

---

### 11 · `<strong>` bullet leads applied arbitrarily

`adversary` 2/9 · `cbm-probe` 3/9 · `patha` 2/8 · `distractors` 2/7 · every other file
exactly 1/N. There is no rule; the emphasis lands wherever the writer's attention was.
Purely cosmetic, listed for completeness.

**Rewrite:** bold the lead clause of every "does not prove" bullet, or none.

---

## KILL LIST — reports (lower bar; all cosmetic unless marked)

### 12 · `the honest ___` — 133 hits, 39 of 40 files, 78 distinct nouns

> `A1-ai-native-textbooks.md:535` · `### 6.4 What the karpathy result actually is (the honest version)`
> `A2-interactive-animation.md:27` · `## 0. Executive framing: the honest version of the animation story`
> `G2-agent-village.md:20` · `## 0. The thesis, and the honest version of it`
> `M1-market-and-model.md:1504` · `The honest version has three real changes and three false ones.`
> `J1-personalisation-engine.md:252` · `The honest version of the`

Also: `the honest answer` ×12, `the honest headline` ×6, `the honest caveat` ×5, `the honest
reading` ×8, `the honest position` ×5, and singletons down to `the honest workhorse`, `the
honest terminus`, `the honest LOPI`, `the honest scoreboard`.

This is the project's signature move and it is doing real work most of the time — but at 133
repetitions the word has stopped modifying anything. When every version is the honest
version, "honest" is a throat-clear.

**Rewrite:** in headings, name the content instead of the virtue. `A2:27` →
`## 0. Executive framing: what the animation literature actually supports`.
`G2:20` → `## 0. The thesis, and where it overstates`.

---

### 13 · `which is precisely` — 23 hits, 17 files; three in one report

> `F9-open-problems.md:543` · `property, not a prompt-level one** — which is precisely why the one team that took it`
> `F9-open-problems.md:1433` · `or litigation, not through experiment — which is precisely why it belongs in an open-problems`
> `F9-open-problems.md:1574` · `the field toward fidelity and dosage, which is precisely what H1 argues for special`

Em-dash + `which is precisely` is a single rhetorical unit deployed three times in one
document. Each instance is a claim of inevitability that the sentence has not earned; the
construction asserts that the connection is obvious rather than showing it.

**Rewrite:** `F9:1433` → `…or litigation, not through experiment. That is the test for
inclusion here: a question settled by a court is not an open problem, it is a closed one with
the wrong judge.`

Not all instances are bad — `A5-world-models.md:197` (`a computer algebra system cannot be
wrong about algebra, which is precisely the property a generative model lacks`) earns it, and
should stay.

---

### 14 · `not merely` — 39 hits, 22 files; four in one report

> `N4-explanation-atlas.md:31` · `And this is not merely an inference from the general finding: it has been`
> `N4-explanation-atlas.md:855` · `failed* — is not merely unvalidated; the one study that tested it against an outcome found`
> `N4-explanation-atlas.md:1210` · `**The felt/real gap here is not merely that platforms measure the`
> `N4-explanation-atlas.md:1590` · `verified 2026-07-29. The door is not merely locked contractually; it has been closed.`

`N4` also carries the highest sentence-initial `And`/`But`/`So` rate of the six sampled
(14 per 20,493 words; `D2-portfolio-case-studies.md` has **0** in 14,190 words). Line 31
stacks both tics in one clause: *And this is not merely an inference…*

**Rewrite:** `N4:31` → `This is not an inference from the general finding — it has been
measured directly on this exact corpus (§1.4).`

---

### 15 · Retrieval-note boilerplate, near-verbatim across five reports

> `A1-ai-native-textbooks.md:12` · `**Research constraint note:** WebSearch budget was exhausted for this session. Findings below come from`
> `A2-interactive-animation.md:12` · `**Research constraint note:** WebSearch budget was exhausted for this session. All findings below come from`
> `F5-learner-model.md:12` · `> **Retrieval note.** WebSearch budget was exhausted before this section began.`
> `F11-scientific-remembering.md:12` · `> **Retrieval note.** WebSearch budget was exhausted before this section began.`
> `E1-E2-edtech-landscape-lessonorca.md:12` · `> **Retrieval note.** The WebSearch budget for this project was exhausted before this`

Two label variants, one sentence, five files. Purely cosmetic — and arguably correct, since
the same real constraint applied. Flagged only because the brief asked where the shared brief
becomes visible, and this is the clearest instance in the corpus.

**Rewrite:** none needed; standardise the label to `Retrieval note.` and leave it.

---

### 16 · Scaffold sections applied to under half the corpus — *not slop, but worth knowing*

`Negative and null results` appears in 19/40 · `Executive summary` 4/40 ·
`What I could not verify` 2/40 · `Handoff notes` 6/40. The reports that carry a null-results
register are visibly stronger for it. The 21 that do not are not thereby dishonest — several
integrate nulls inline — but a reader cannot tell which from the outside.

**Not a rewrite:** a structural note for whoever consolidates these.

---

## WHAT IS CLEAN

Short and specific, as instructed.

- **The demo vocabulary is genuinely clean.** Zero hits for the entire standard tell-list
  across 1,958 lines. The three `robust`/`arguably` survivors are statistical and correct.
  This is rarer than it sounds and should not be touched.

- **The "How to use it" panels vary the verb even though they do not vary the rhythm.**
  Twelve distinct opening imperatives across fourteen panels (`Corrupt`, `Step`, `Accept`,
  `Make`, `Answer`…). Somebody was paying attention to the word and missed the sentence.

- **The "does not prove" bullets are mostly excellent and specific.**
  `adversary.html:233` — `That generation is "unbounded". It is not, and the page says the
  number out loud for that reason` — is a page arguing against its own headline, with the
  receipt. `grounding-ladder.html:241` — `That L3 here is SymPy. It is a canonical-form
  comparator of about eighty lines.` — pre-empts the exact objection an expert would raise.

- **`patha.html` publishes its own falsification in the header.** `patha.html:59–62` leads
  with `benchmarked it, and <strong>falsified it</strong>. Both halves are here.` The panel
  at line 73 oversells it (#8), but the lede does not.

- **Report headings are the anti-template.** Forty reports, and the h2 text barely repeats:
  the top recurring heading is `N. Sources` at five instances. Forty agents under one brief
  produced forty different spines. That is the outcome the brief was worried about, and it
  did not happen.

- **`N3-two-hour-school.md:20–45` leads with the refutation and the arithmetic.** Before any
  framing, it states the vendor's own denominator, the NWEA cell it contradicts (`9.61 RIT`
  against the claimed `4 points`), and the conclusion that an average grade-8 student scores
  as learning *infinitely* fast because the denominator is zero. No hedging preamble.

- **`H1-selpa-accessibility.md:30–46`** puts ten findings in a table with an evidence label on
  every row, including `F4`, which dismantles the framework the section is named after
  (`UDL is a design philosophy with weak empirical support`). A report that undercuts its own
  title in the first table is not following a template.

---

## SAMPLE SELECTION — the six reports, and why

Selected by file mtime, per the brief.

| # | Report | Basis |
|---|---|---|
| 1 | `A5-world-models.md` | **Earliest.** `2026-07-25T22:52` — joint-oldest file in the directory. |
| 2 | `D2-portfolio-case-studies.md` | **Earliest.** `2026-07-25T22:52` — the other half of that tie. |
| 3 | `F9-open-problems.md` | **Middle, random.** Drawn with `shuf --random-source` from the 20-file middle band (ranks 11–30 by recency). |
| 4 | `H1-selpa-accessibility.md` | **Middle, random.** Second draw from the same band. |
| 5 | `N4-explanation-atlas.md` | **Most recent.** `2026-07-29T18:24`. |
| 6 | `N3-two-hour-school.md` | **Most recent.** `2026-07-29T18:33` — newest file in the corpus. |

The two earliest are three days and roughly thirty reports removed from the two most recent,
which is where voice drift would show if the brief were tightening over time. It is not:
`D2` (earliest) has zero sentence-initial `And`/`But`/`So` in 14,190 words; `N4` (most
recent) has fourteen in 20,493. The drift is toward *more* voice, not toward convergence.

Corpus-wide counts (vocabulary, headings, scaffolds, opening shapes) were taken by `grep`
across all forty without reading them, as permitted.

---

## METHOD

- Orientation panels extracted programmatically from `<section class="orient">` in all 15
  files in `docs/demos/`; `index.html` has none, leaving 14 × 3 = 42 panels.
- Demo prose extracted with `<script>`/`<style>` blocks stripped and original line numbers
  preserved: 1,958 lines.
- All frequency figures produced by `grep -o … | sort | uniq -c | sort -rn` or equivalent
  Python counting. No count in this document was estimated.
- Lede/orientation duplication measured by shared 6-gram overlap between the `<header>` and
  the orientation block of each page.
- Reports: corpus-wide greps across all 40; six files read.

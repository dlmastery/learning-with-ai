# Slop audit — survey sections 00–18

Adversarial prose review. 19 files, 48,807 words. All counts run, not eyeballed.

---

## VERDICT

**Yes — this was written by someone who knows the subject.** The evidence is
load-bearing rather than decorative: numbers arrive with their confidence intervals,
sample sizes, and the reason they might be wrong. Nulls are given space. Corrections
are dated and attributed. The vocabulary is clean — zero instances of *delve*,
*tapestry*, *landscape*, *realm*, *testament*, *myriad*, metaphorical *navigate*, or
*underscore* across 48,807 words. That is a real achievement and it means the obvious
tells are not the story.

**The failure is not vocabulary. It is that a rhetorical machine got left running.**
Nineteen sections share one sentence engine — antithesis (`X, not Y` ×147;
`That is not A. It is B.` ×26), enumerative preamble (`Two things follow.` ×69), and a
bolded aphorism to close. Individually each is good writing. At this density they stop
being choices. By §09 an attentive reader can predict the shape of the next paragraph
from its first four words, and by §13 the survey is quoting itself: **two sections end
with the same sentence.**

The second failure is a confidence tell. The text tells you it is being honest
(*honest/honesty/honestly* ×36) and ranks its own contents for you (*the most important
X in this section/survey/corpus* ×22) instead of letting the material do it. An expert
who trusted the reader would delete every one.

Verdict in one line: **the research is first-rate and the prose is running on
autopilot at roughly 1 tic per 220 words.**

---

## FREQUENCY TABLE

Corpus: 48,807 words across 19 files.

### Construction tics

| Tic | Count | Per 1,000 w | Note |
|---|---:|---:|---|
| Em-dash | **578** | 11.8 | ~30 per file; 49 in §13 alone |
| `X, not Y` comma antithesis | **147** | 3.01 | the governing sentence shape |
| `rather than` | **71** | 1.45 | vs. `instead of` ×11 — a 6.5:1 register lock |
| Enumerative preamble (`Two X follow.`) | **69** | 1.41 | 38 begin with *Two* |
| `…, and it is [appositive]` | **60** | 1.23 | 47 with the comma; 7 in §10 alone |
| One-sentence punch paragraph | **53** | 1.09 | incl. `Now the trap.` / `Not the count.` |
| `exactly` | **44** | 0.90 | |
| Author-written blockquote aphorism (`> **…**`) | **37** | 0.76 | pull-quote as punchline |
| `honest / honesty / honestly` | **36** | 0.74 | see below |
| `That is not A. It is B.` (full-stop antithesis) | **26** | 0.53 | |
| Self-ranking superlative (*the most X in this survey*) | **22** | 0.45 | conservative regex; true count higher |
| `precisely` | **21** | 0.43 | 13 as a bare intensifier |
| Imperative `Read the…` | **8** | 0.16 | *Read the ratio / the third row / the objective function* |
| `worth stating / worth being exact about` | **4** | 0.08 | |

### Bold saturation

**1,013 bold spans — one every 48 words.** Emphasis at this rate is wallpaper.

| File | Bold / 1,000 w | | File | Bold / 1,000 w |
|---|---:|---|---|---:|
| 01-central-finding | **33.2** | | 09-the-scoreboard | 18.3 |
| 07-who-is-not-in-the-room | **30.2** | | 04-the-empty-chair | 18.0 |
| 02-teach-to-learn | 30.1 | | 16-the-substrate | 17.8 |
| 13-grounding | 26.8 (114 spans) | | 18-textbook | 17.7 |
| 14-motivation | 26.1 (108 spans) | | 17-showing | 17.5 |
| 00-north-star | 25.5 | | 11-the-archivist | 16.4 |
| 05-explanation | 24.6 | | 12-assessment | 15.6 |
| 08-scheduler | 24.5 | | **15-what-we-owe-children** | **8.7** |

The 3.8× spread between §01 and §15 is the clearest voice seam in the corpus.

### Template headers — the staleness signal

| Header | Files |
|---|---:|
| `## N. What this section commits us to` | **14 of 19** |
| `## N. The nulls, given their own space` | **6** (§09, §10, §11, §12, §13, §14) — *verbatim, word for word* |
| `## N. The strongest counter-argument` | **5** (+1 variant in §07) |
| `The inversion` in a header | **8** |

Six sections carry an identical seven-word header. Fourteen close with an identical
checklist. The template was a good idea in §04 and is furniture by §14.

### Closing-move census

**11 of 19 files end on the `not X / it is Y` antithesis.** Five open their final
paragraph with the same connective formula:

- §06:220 "The through-line, which is the same one the grounding sections reached from the other direction:"
- §08:249 "The pattern here is the one this survey keeps finding from different directions."
- §13:438 "The through-line is the same one this survey keeps arriving at from other directions."
- §17:351 "The through-line is the same one the rest of this survey keeps arriving at from other directions."
- §14:461 "The through-line: …"

---

## KILL LIST

Ranked by severity. Severity 1 = an expert stops reading.

### ▸ 1. Two sections end with the same sentence

**`survey/06-what-the-object-must-refuse.md:220-222`**
> The through-line, which is the same one the grounding sections reached from the
> other direction: what teaches is not the richness of what the learner is given. It
> is the **precision of what they are not allowed to do wrong without noticing.**

**`survey/13-grounding.md:438-441`**
> The through-line is the same one this survey keeps arriving at from other directions. What
> teaches is not the richness of what the learner is given. It is **the precision of what
> they are not allowed to get wrong without noticing** — and, increasingly, …

**Why it fails.** Identical but for one verb (*do* → *get*). A reader who reaches §13
having read §06 discovers the survey has a closing-sentence generator. Every claim of
independent convergence in the document ("three literatures converge," "nine groups
converged") is retroactively cheapened by the discovery that the convergence was
copy-paste. Compounded by §08 and §17 opening their last paragraphs with the same
"through-line…from other directions" frame — four sections, one ending.

**Rewrite.** Let §06 keep the aphorism, without the preamble that advertises it:

> A well-built simulation refuses more illegal states than wood does. What teaches is
> not the richness of what the learner is given — it is the precision of what they
> cannot get wrong without noticing.

Delete the sentence entirely from §13 and end on the line already there, which is
better and is specific to grounding:

> The correction can now come from a program the learner runs themselves, rather than
> from a machine claiming to know.

Delete the through-line frame from §08:249 and §17:351 and open those paragraphs on
their own subject matter.

---

### ▸ 2. A paragraph nobody read after editing it

**`survey/15-what-we-owe-children.md:79-88`**
> …**it was reached on 2026-07-28 and the delay is real; see the correction at the head
> of this section. The paragraph below is retained as written, and superseded.** The
> stale reasoning ran:
> research (HTTP 202, empty body), and a simplification package proposing deferral
> has been publicly discussed. ~~Do not plan on a delay.~~ **Superseded — …** Check
> Article 113 against EUR-Lex before making a compliance decision.**

**Why it fails.** This is not a style problem, it is unread output. "The stale reasoning
ran: research (HTTP 202, empty body), and…" is a decapitated sentence — the subject was
deleted when the correction was pasted in, leaving a parenthetical error code as the
sentence's grammatical head. Line 88 ends with an unmatched `**`. A section whose entire
argument is *we correct in public within a day* proves, in its own body text, that the
correction was applied without anyone rereading the paragraph. This is the single
strongest machine-authorship signal in the 19 files.

**Rewrite.** The correction at lines 11–32 already carries every fact. Delete lines
79–88 and close the paragraph at line 78:

> Two secondary readings are open rather than settled. Annex III 3(b) lacks the
> institutional limiter that 3(c) and 3(d) carry, which on plain text pulls
> direct-to-consumer tutors into scope; no authoritative construction was found. On the
> application date, see the correction at the head of this section — it moved after this
> paragraph was drafted.

---

### ▸ 3. A file that repeats itself inside 1,400 words

**`survey/01-central-finding.md:65-66`** and **`:88-89`** — verbatim, 22 lines apart:
> Felt learning is what every optimisation loop can measure. Real learning is what
> none of them measure.

**Why it fails.** Once it is the thesis. Twice in the same short file, the second time
as a bare section-opener, it reads as two drafts merged without a read-through. §01 is
1,385 words; there is nowhere for the reader to have forgotten.

**Rewrite.** Keep it at line 65 where it earns its place, and open §"Why this is a
systems problem" on the consequence instead:

> Every instrument a product team already owns points at the wrong quantity.

---

### ▸ 4. A finding restated as new, five times

`+0.195 SD per SD of baseline` and its gloss "the strong pulled further ahead" appear in
**§01:25, §01:150, §03:200, §04:183, §07:70, §09:80, §09:286.** Twice within §01 alone.

Worse, a whole sentence is templated across two files:

- **`04-the-empty-chair.md:196-197`** "Anyone selling **guardrails** as a learning gain is ahead of the evidence, including us."
- **`09-the-scoreboard.md:159-160`** "Anyone selling **restraint** as a learning gain is ahead of the evidence, including us."

And the self-congratulating omission formula, twice:

- **`06:72`** "because omitting an inconvenient number is worse than discounting a bad one."
- **`12:307`** "because omitting inconvenient nulls is worse than reporting them."

**Why it fails.** Category D. Each instance is written as though the finding is arriving
for the first time — "Sierra Leone's effect loaded at…" with full apparatus, five times.
A survey is allowed to cross-reference; it is not allowed to re-perform surprise.

**Rewrite.** §09 is the section of record for the Sierra Leone reanalysis. Everywhere
else, cite and move: "gap-widening loaded on baseline attainment (§09)". Delete the
duplicated *ahead of the evidence* sentence from §04 — the section already says "Benefit
not demonstrated" two lines earlier and does not need the flourish. Cut the *omitting
inconvenient nulls* formula from §12 and keep §06's, once.

---

### ▸ 5. The honesty performance — 36 instances

Worst offenders:

**`16-the-substrate.md:118`** `## 3. The face: 25 FPS on one GPU, and an honest null`
**`16-the-substrate.md:147`** "That is the honest position: **a face reliably makes learners feel better…**"
**`10-the-village.md`** — six in 3,538 words: *the honest scope*, *honestly labelled*, *the honest workhorse*, *the honest state*, *the honest caveat*, *the honest position*.

**Why it fails.** An honest sentence does not need the adjective. Thirty-six of them read
as a style-brief instruction ("be candid about limitations") that leaked into surface
vocabulary. It also creates a two-tier text: if §16's null is *the honest* one, what were
the other nulls? The word is doing self-certification, not work.

**Rewrite.**
- §16:118 → `## 3. The face: 25 FPS on one GPU, and no measured learning effect`
- §16:147 → "So: a face reliably makes learners feel better and does not reliably make them learn more."
- §10:89 "C1 is the honest workhorse because…" → "C1 does the work, because it is the only tier where the system generates its own ground truth."

Target: fewer than eight instances corpus-wide, reserved for places where honesty is
genuinely the contested question (§15's correction, §09's Sierra Leone reanalysis).

---

### ▸ 6. The self-ranking superlative — 22+ instances

- **`00:12`** "the most important design decision in this document"
- **`08:112`** "This is the most important table in the section"
- **`11:199`** "The single most important architectural idea in this literature"
- **`13:243`** "The single most important number in this area"
- **`16:223`** "Here is the design that follows, and it is the most useful thing in this section."
- **`17:90`** "The single cleanest measurement in this literature"
- **`14:11`** "Here is the cheapest useful test in this survey."

**Why it fails.** Substitution test: every one survives unchanged if the finding
underneath it were different. They are load-bearing for the *author's* confidence, not
the reader's understanding — and when eleven things are the most important, none is.

**Rewrite.** §08:110-112 →
> This table should govern what anyone builds:

§16:223 →
> The design that follows splits the substrate in two.

§13:243 → delete the sentence; the blockquote `97% × 69% = 36%` under it is
self-evidently the number.

---

### ▸ 7. `…, and it is [appositive]` — 47 instances, 7 in one section

**`10-the-village.md:114`** "Here is the finding that most constrains the design, and it is a negative one."
**`10-the-village.md:172`** "**T0 is the tier that carries the load**, and it is the least glamorous."
**`10-the-village.md:184`** "**T3 is where the architecture earns its keep pedagogically**, and it is the one result…"

**Why it fails.** Three identical clause-shapes inside one 3,500-word section. The tail
always does the same job — upgrade the claim just made — which means it never surprises
and eventually stops being read.

**Rewrite.** §10:114 → "The finding that most constrains the design is a negative one."
§10:172 → "T0 carries the load, and it is the least glamorous tier." → "T0 carries the
load. It is also the least glamorous tier in the ladder." Vary or cut; two per section is
the ceiling.

---

### ▸ 8. The announcement header and the announcement sentence

- **`02:35`** "This is the finding that kills the obvious implementation."
- **`05:150`** "This is the finding that inverts the request."
- **`14:298`** "This is the result that should govern every training decision in an AI learning system."
- **`18:175`** "This is the null result that most changes what a course generator may claim, and it deserves its own space."
- **`06:50`** `## 2. The result that reverses the premise`
- **`05:122`** `## 6. The result that kills the obvious design`

**Why it fails.** Category C: headers that announce rather than inform. Six headers and
sentences promise a reversal without naming it; the reader must read on to learn what was
reversed. A header that said *what* happened would carry the same drama and more
information.

**Rewrite.**
- §06:50 → `## 2. Gesture beat action on objects`
- §05:122 → `## 6. Without prior expectancy, teaching is worth g = −0.02`
- §05:150 → delete. Wang, Cheng & Mayer's result inverts the request without being told to.
- §18:175 → "Difficulty is predictable from item text. Discrimination is not." (already the
  next two paragraphs — promote it and cut the announcement.)

---

### ▸ 9. The enumerative preamble — 69 instances

**`16-the-substrate.md:46`** "Two of these decide whether you have a tutor."
**`16-the-substrate.md:102`** "Two absences follow."
**`16-the-substrate.md:159`** "Two things the evidence does support."
**`12-assessment.md:360`** "Two answers."
**`12-assessment.md:333`** "Two observations about that table matter more than its contents."

**Why it fails.** 38 sentences begin with *Two*. This is the shape of an outline that was
never dissolved into prose — the counting is a scaffold for the writer, not information
for the reader, who can see there are two items because two items follow.

**Rewrite.** §16:102 → "There is no code execution inside a live session on Gemini Live
at all, and neither API has any output channel beyond audio, transcript and tool calls."
§12:360 → delete; start directly on "The burden moved rather than grew."
Corpus target: halve it. Keep the count only where it is genuinely surprising
(*"Nine barriers stand between a child and a tutor. Abundant attention removes three."* —
that one earns it).

---

### ▸ 10. Substitution-test failures — decoration that survives any topic

- **`09:53`** "That is not a disappointing result. It is a *stable* one, and stability is what makes a foundation."
- **`17:242`** "Evidence and engineering rarely agree this cleanly."
- **`13:26`** "…and that framing produces bad products. It makes verification a filter bolted onto the end of a generator. The better framing is capability."
- **`12:66`** "This reframing is generative rather than gloomy…"
- **`07:82`** "That is a materially more optimistic finding than the one it replaces, and it raises the standard rather than lowering it"

**Why it fails.** Swap the topic for supply-chain logistics and every sentence still
parses. These are the connective tissue an LLM produces when it has finished the argument
and has not been told to stop.

**Rewrite.**
- §09:53 → "0.258, 0.31, 0.37, 0.32–0.42, 0.288. Four countries, three languages, two technology generations. A number that reproduces like that is one you can design against."
- §17:242 → delete outright. The preceding sentence ("Spend the automated gate's budget on contiguity and reserve humans for coherence") is the conclusion.
- §12:66 → delete "This reframing is generative rather than gloomy, because"; start at "the design problem is not…".

---

### ▸ 11. Bold saturation, worst case

**`01-central-finding.md:10-28`** — four competing bold emphases in nineteen lines:
`**The wins available today are large, real, and measured.**` … `**+127%**` …
`**Corrected in place:**` … `**+0.216 SD, SE 0.137 — not significant.**`

**Why it fails.** §01 runs 33.2 bold spans per 1,000 words — one every 30 words. When the
framing sentence, the finding, the correction label and the number are all bold, the
reader's eye has no route through and the emphasis conveys nothing. §13 (114 spans) and
§14 (108) are the same problem at scale.

**Rewrite.** One rule, applied corpus-wide: **bold only numbers that contradict the
sentence a reader expected.** Unbold every framing sentence, every list-item lead, and
every commitment-list header. That drops the corpus from ~1,013 spans to roughly 350 and
makes the remaining ones mean something.

---

### ▸ 12. `precisely` as a free intensifier — 13 of 21 uses

**`10:343`** "running all ten at once is precisely the failure MAST catalogues"
**`14:192`** "the class deployed most heavily is precisely the class identified as corrosive"
**`16:98`** "1 FPS discards precisely the information that makes procedural feedback possible"
**`04:218`** "a compliance failure for precisely the population it claims to serve"

**Why it fails.** In each, deleting the word changes nothing except the swagger. It is the
tell of a writer reaching for emphasis the sentence structure should have supplied.

**Rewrite.** Delete in all four. Where the coincidence really is the point (§05:47,
§02:30), keep it — that is two uses, not thirteen.

---

## VOICE DRIFT

Four seams are visible.

**§01-central-finding is written by a different hand from everything after it.** It is the
only file in the set with **unnumbered headers** ("Why the field mostly builds the other
one", "The uncomfortable corollary") and the only one with **zero blockquotes**. Every
other file uses `## N. Title` and the pull-quote aphorism. It also has the corpus's
highest bold density (33.2/1,000) and the corpus's only internal verbatim self-repetition
(item 3 above). Reads like the earliest draft, never brought into the house style.

**§00-north-star-jarvis is a spec sheet wearing an essay's clothes.** The only file using
status emoji (⛔ ⚠️ ✅ ×7), telegraphic register ("Escape hatch: `contextWindowCompression`
+ `sessionResumption`"), and an addendum bolted on ("Addendum — Wan Streamer changes three
of the seven blockers") that supersedes its own §3 and §5 in place rather than being
integrated. It also carries the only capability table in the corpus that renders as a
project tracker.

**§03-the-vision breaks register upward and nothing else in the survey reaches for it.**
`03:233` "**Nobody's thumb, ever again — and this time, the record travels with them.**"
The mythic frame (Ekalavya, Drona, Star Trek, Kobayashi Maru) and the keynote cadence are
unique in the set. It is the only closing line that would work read aloud to a room. Not
a defect on its own — but it means §03 and §12 (Cronbach's alpha as a cold open, LaTeX in
line 13) cannot plausibly be the same writer at the same sitting.

**§15-what-we-owe-children is the outlier the numbers already flagged.** 8.7 bold spans
per 1,000 words against a corpus mean of ~21 — a 3.8× gap, and 2.6× below the next-lowest
file. The register is legal-brief continuous prose with long paragraphs and few punch
fragments. It is also the only file carrying an unrepaired textual wound (item 2). The
combination reads as a section drafted separately, under a different instruction, and
merged late.

**Where the seam does *not* show:** §09–§14 and §16–§18 are strikingly uniform — same
header grammar, same nulls section, same counter-argument section, same commitments list,
same closing aphorism. That is the opposite failure. Six files that consistent were
produced from one template, and the template is now the most visible thing about them.

---

## WHAT IS CLEAN

Short, and meant.

- **The vocabulary.** Zero hits for the entire standard slop lexicon across 48,807 words.
  Deliberate, and rare.
- **§12's cold open** (`12:11-22`). Cronbach's alpha, then *"Look at k."*, then the kill:
  alpha is not biased under generated assessment, it is undefined. No announcement, no
  superlative, no bold framing sentence. The best 200 words in the corpus.
- **§13's pāṭha self-falsification** (`13:196-234`). The survey benchmarks its own earlier
  proposal, finds it exactly at chance, prints the table, and keeps the negative result.
  The sentence *"A protocol whose false-alarm rate rises exactly as fast as its recall
  does not get better with scale; it gets louder"* is earned by the four preceding
  paragraphs rather than asserted ahead of them.
- **§18's corpus audit** (`18:208-244`). An original measurement, a naive count, the
  correction of the naive count in the *opposite* direction from expectation, and then the
  refusal to over-generalise from it. Structurally honest without once using the word.
- **§11's opening** (`11:11-46`). Mr. Ranedeer's base64 trick as the whole genre in one
  line. Concrete, specific, unrepeatable, and it does the section's argument before the
  section states it.
- **The correction discipline generally.** Dated, in-place, attributed, with the wrong
  version left visible (§01's B2 correction, §05:105 "including by us", §16:109 "A
  correction the project owes its readers"). Whatever else is mechanical here, this is
  not.

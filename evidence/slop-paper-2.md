# Slop audit — survey, second half (§19–§37)

Adversarial prose review. Scope: `19-the-canon` … `37-the-business-of-it` (19 files,
40,306 words). Baselines for comparison: `04-the-empty-chair`, `08-nobody-needs-a-better-scheduler`
(hand-written, earliest), plus `05`, `06` where useful.

---

## VERDICT

**This is good prose with four measurable tics and one hard seam.** The obvious slop
vocabulary is essentially absent — `delve` 0, `tapestry` 0, `realm` 0, `testament` 0,
`crucial` 0, `pivotal` 0, `myriad` 0, `underscore` 0, metaphorical `navigate` 0
across 40k words. That is a genuinely rare result and it should be said first.

What is wrong is one register up. Four constructions have been ground into template:

1. **The self-referential superlative** — 27 instances of "the single most X in this
   document/section/survey." Three of them independently claim to be *the cheapest
   experiment in this document*. They cannot all be. This is the worst finding
   because it is simultaneously a prose failure and a factual contradiction.
2. **The announcement paragraph** — a one-line paragraph whose entire job is to say
   that something good is coming ("Here is the reframe that makes this section worth
   writing."). 78 short paragraphs of this shape; roughly a third are pure metadata.
3. **The numeral lead-in** — 45 paragraphs open "Two X…/Three Y…" with a rotating
   verb (set / belong / compound / complete / keep / carry / follow / reinforce /
   define / deserve). Same frame, disguised.
4. **"is not X. It is Y."** — 37 instances. This one is *native* (04 runs it at
   2.37/1k, 05 at 2.73/1k, higher than most of §19–§37), so it is not drift. It is
   saturation. 13 of 19 sections also close on it.

**The seam is real and it is in the closers, not the voice.** §29–§37 close with a
label + colon + bolded aphorism **9 times out of 9**. §19–§28 do it 2 times out of 10.
That is the fingerprint of the fast block, and it is the one thing a reader would
notice.

**One outright duplication:** §33 §5 reproduces §21 §1 — 43 overlapping 9-grams,
same citation, same bolded clause, same closing sentence with two words shuffled.

---

## FREQUENCY TABLE

### What is absent (report this — it is the headline)

| Term | Count in 40,306 words |
|---|---|
| delve, tapestry, realm, testament, crucial, pivotal, myriad, underscore, multifaceted, holistic, paradigm, intricate, profound, furthermore, moreover, "In other words", "it is worth noting" | **0 each** |
| landscape | 5 (4 literal — "energy landscape"; **1 metaphorical**, §32:16) |
| leverage | 5 (all the finance noun, correct usage) |

### What is over-used

| Construction | Count | Rate | Baseline (04/08) | Read |
|---|---|---|---|---|
| **"the [superlative] … in this document/section/survey"** | **27** | 1.4/section | 04: 1, 08: 0 | **Worst tic.** Inflation; 3 mutual contradictions |
| "is not X. It is Y." | 37 | 0.92/1k | 04: 2.37/1k, 05: 2.73/1k | Native, but saturated |
| Short "announcement" paragraphs (≤14 w, ending in `:` or evaluative tail) | 78 | 4.1/section | 04: 3, 08: 4 | Structural filler |
| Paragraphs opening on a bare numeral ("Two…/Three…") | 45 | 2.4/section | — | Same frame, rotated verb |
| "exactly/precisely the …" | 26 | 1.4/section | — | Intensifier tic |
| "The honest [reading/summary/version/prior/…]" | 16 | 0.84/section | — | Named in the brief; confirmed |
| "Read the / Note the [ordinal]…" reader-imperative | 8 | — | 04: 1 | 3 share the exact frame |
| "worth stating/naming/checking" | 5 | — | — | The announcing tic |
| "the [secondary] is more useful/instructive than the [primary]" | 5 | — | — | **Pure substitution-test failure** |
| Self-authored aphorism blockquotes | 38 | 2.0/section | 04: 3, 08: 2 | At baseline. Fine. |
| Bold spans | 979 | 24.3/1k | 04: 17.9, 08: 24.4 | At baseline. §24 (32.0), §34 (31.1), §22 (30.6) are hot |
| Em-dashes | 508 | 12.6/1k | 04: 12.7, 08: 11.7 | **Exactly at baseline. Not a finding.** |
| Sections closing "What this section commits us to" | 19/19 | — | 08: yes, 04: no | House template. Not stale — the *contents* differ every time |

### The seam, quantified

| | Closes with label + colon + bolded aphorism |
|---|---|
| §19–§28 | **2 / 10** (21, 23) |
| §29–§37 | **9 / 9** |

Sentence-opening connectives ("And/But/So/Which") per 1,000 words: 04 = 1.4,
08 = 2.0. Target range 0.0–4.1. Only **§35 (4.1)**, **§23 (3.8)** and **§30 (3.6)**
exceed baseline meaningfully. This is *not* a general problem.

---

## KILL LIST

### 1 — `25:325` + `30:227` + `33:113` · Three cheapest experiments

> `25-the-ladder-of-explanation.md:325` — "It is also **the cheapest experiment in this section**, and the one that would turn the ladder from an output into an instrument."
> `30-the-compression.md:227` — "**Ship the session decomposition study.** … It is **the cheapest high-value experiment in this document**."
> `33-greenfield.md:113` — "Build this first. It is **the cheapest experiment in this document** and it gates the rest."

**Why it fails:** the superlative is doing rhetorical work, not carrying information,
and the proof is that the document asserts it three times about three different
studies. A reader who notices stops trusting every other superlative in the survey —
and there are 27 of them. This is the single most damaging line-level failure in the
second half.

**Rewrite:** pick one and cost the other two.
- 33:113 → "Build this first. Two labelled corpora and one rank correlation — no new
  data, no learners — and it gates five of the eight designs."
- 30:227 → "Ship the session decomposition study. One instrumented cohort, a
  fortnight, and it closes the gap §1 could not."
- 25:325 → "It needs no new instrument: the learner already writes the ELI10."

### 2 — `21:53–58` ↔ `33:188–192` · The paragraph written twice

> `21-what-we-cannot-see-from-here.md:55` — "**71% of one model's misconception-detection failures concentrate in two question types** — reported incidentally by researchers studying something else entirely. Model pedagogical blind spots are not diffuse. They are structurally concentrated, which is exactly the condition under which monoculture bites hardest."
> `33-greenfield.md:188` — "**71% of one model's misconception-detection failures concentrate in two question types** — found incidentally by researchers studying something else. Model blind spots are not diffuse. They are structurally concentrated, which is the condition under which monoculture bites hardest."

**Why it fails:** 43 shared 9-grams. The only differences are *reported→found*,
*entirely* deleted, *exactly* deleted, *pedagogical* deleted. This is regeneration,
not writing, and it is the clearest machine artefact in the second half. §33 was
written in a later session and re-derived a paragraph that already existed.

**Rewrite:** §33 should not restate it. Replace 33:181–192 with:

> "The population-scale versions concentrate exactly the risk §21 named. §21 carries
> the mechanism — Kleinberg and Raghavan's monoculture theorem, and the 71%
> concentration of one model's detection failures. What §33 adds is that the atlas is
> where that risk is *manufactured*: one corpus, one graph, one mentor. The mitigation
> is the same instrument either way."

### 3 — `22:99` · The paragraph that announces its own worth

> `22-the-one-interaction-that-survived.md:99` — "Here is the reframe that makes this section worth writing."

**Why it fails:** it contains no information about learning, personalisation, or
anything else. It would survive verbatim in any of the other thirty-six sections —
the substitution test's purest failure in the corpus. It is also self-congratulatory
in a document whose whole authority comes from not doing that.

**Rewrite:** delete it. The next paragraph — "The blocker on real personalisation was
**never compute, and never the algorithm**" — is the reframe, and it lands harder
without a drumroll.

### 4 — `29:95–113` · A correction inserted, the surrounding prose not repaired

> `29:95` — "**Corrected 2026-07-29, and the correction is more useful than the original claim.**" … `29:102` — "So in the one experiment that isolates it, the load-bearing variable is **naming the wrong idea**, not the order in which the machinery arrives."
> `29:107` — "**The reader has no slot to put it in.** They remember it as a list of tricks…"
> `29:112` — "**The rule: lead with the constraint that forces the design.**"

**Why it fails:** this is the worst *structural* defect in the second half. 107 is the
orphaned original paragraph — its "it" now has no antecedent, because the claim it
elaborated was retracted five lines above. Then 112 reasserts the retracted rule as
"**The rule**." A careful reader hits a contradiction inside a subsection whose whole
subject is intellectual honesty about corrections. The seam is visible.

**Rewrite:** move 107 above the correction and mark it as the superseded reasoning,
then downgrade 112:

> "The original argument was mechanistic: machinery before obstacle leaves the reader
> with no slot to put it in, so they remember a list of tricks and cannot tell
> essential from incidental. **Muller's design does not test that.** His Refutation
> condition is the Exposition script verbatim plus the misconception named — same
> order, d = 0.79. So ordering may help; naming is what has been shown to work.
> **The rule we can defend: name the wrong idea. The rule we would like to defend
> but cannot yet: lead with the constraint that forces the design.**"

### 5 — `35:49–68` · "Three separate times", then four items

> `35-the-explanation-atlas.md:49` — "That hypothesis is dead, and it died three separate times."
> Followed by: `**Measured.**` … `**Structurally foreclosed.**` … `**And it was already built.**` … `**Worse, the sign may be backwards.**`

**Why it fails:** four items. The tricolon was chosen for rhythm and then overrun by
the evidence, and nobody counted. In a survey that audits other people's arithmetic
line by line, miscounting your own list is expensive.

**Rewrite:** "That hypothesis is dead, and it died four separate ways." (Or promote
"Worse, the sign may be backwards" into the *Measured* item, where it belongs — it is
also a measurement.)

### 6 — `32:37` · A parallelism that forced an empty term

> `32-pedagogy-has-no-pytest.md:37` — "Sampling without a selector is noise. **Execution without a test is output.** Persistence without a schema is a transcript. Absence without a verifier is unsupervised drift."

**Why it fails:** three of the four are real. "Execution without a test is output" is
a tautology — execution produces output whether or not a test exists. The slot was
filled to complete the anaphora. This is the exact mechanism by which good writers
produce slop: the pattern outruns the content.

**Rewrite:** "Execution without a test is a side effect." (Now it says something: the
run changed the world and nobody knows whether it should have.)

### 7 — `32:16` · The one metaphorical `landscape` in 40,000 words

> `32:15` — "The answer turns out to be a single sentence, and once you have it the entire **reliability landscape** of agentic AI resolves into one line."

**Why it fails:** the only lapse into the register the rest of the survey scrupulously
avoids. It is also doubled — "a single sentence" and "resolves into one line" are the
same claim twice.

**Rewrite:** "The answer is a single sentence, and it orders every reliability result
in agentic AI."

### 8 — The reader-imperative, three times with the same frame

> `19:66` — "**Read the middle clause**, because it is almost never quoted."
> `23:89` — "**Read the control condition**, because it is the whole finding:"
> `34:32` — "**Read the third row carefully**, because it kills the usual explanation."
> (plus `30:59`, `31:168`, `36:60`, `27:30`, `32:188` — 8 total)

**Why it fails:** once, this is a good move. Three times with the identical
`Read the <ordinal/noun>, because it <verb> the <noun>` frame, and eight times in
total, it becomes a verbal habit the reader starts hearing instead of obeying. It also
does the reader's work for them, which the rest of the survey pointedly refuses to do.

**Rewrite:** keep one — 23:89, where it is load-bearing. For the others, let the
sentence itself do it:
- 19:66 → "The middle clause is almost never quoted. **Mastery designs…**"
- 34:32 → "The third row kills the usual explanation. Pure decoration is
  **inert, not harmful** —"
- 36:60 → "The metric returns a multiple greater than one for a nationally average
  student. That is a property of the denominator, not of the instruction."

### 9 — The "more useful than" self-satisfaction, ×5

> `29:95` — "and **the correction is more useful than the original claim**"
> `33:165` — "**the pattern in the rejections is more useful than any single one**"
> `35:43` — "**and the way it died is instructive**"
> `35:134` — "But the ordering has changed, **and the reasoning is the useful part**"
> `35:23` — "**and finding them was worth more than the prediction**"

**Why it fails:** every one of these clauses survives a change of topic unchanged.
They are the author telling the reader that what follows is interesting instead of
making it interesting. Three of the five are in §35, a 1,218-word section.

**Rewrite:** cut all five and let the following sentence stand. E.g. 35:134 →
"**Build the error atlas first.**" (The reasoning is in the next two sentences; it
does not need to be announced as reasoning.)

### 10 — `37:44` · A section header that opens on "And"

> `37-the-business-of-it.md:44` — "## 2. **And** the leverage has not been measured"

**Why it fails:** the connective-as-rhythm tic has escaped the prose and got into the
table of contents. A header is a retrieval handle; "And" gives a reader scanning the
contents page nothing. §37 also opens four paragraphs on "And" (L79, L98, L118, plus
this) in 1,319 words — the highest density of the tic in the corpus.

**Rewrite:** "## 2. The leverage has not been measured — including by us"

### 11 — `36:34` · And + precisely + bold, in one clause

> `36-the-two-hour-school.md:34` — "**And it is precisely why the two-hour figure cannot explain the attainment claim.**"

**Why it fails:** three emphasis devices stacked on one clause — the connective
opener, the intensifier, and full-sentence bold. Each cancels the others. `precisely`
adds nothing to `why`; §36 uses `exactly/precisely` three times in 1,135 words.

**Rewrite:** "Which is why the two-hour figure cannot explain the attainment claim."
(Or, better, unbolded — the next sentence, "If two hours buys parity, it buys parity,"
is the punch, and it should not be competing with bold above it.)

### 12 — `30:37` and `30:152` · "So" doing structural work

> `30:37` — "**So** the encoding fraction is small and the headroom is enormous"
> `30:152` — "**So the honest shape of the claim** is not 'everything compresses' or 'nothing does'."

**Why it fails:** minor, but §30 runs 3.6 connective-openers per 1,000 words against
the 04 baseline of 1.4, and both instances above are summary-restatements — the
paragraph before already said it. 152 also stacks the `honest` tic on top.

**Rewrite:** 37 → "The encoding fraction is small and the headroom is enormous, which
is what makes the original claim plausible rather than silly." 152 → "The shape of the
claim is therefore neither 'everything compresses' nor 'nothing does'. It is:"

---

## VOICE DRIFT — is §33–§36 distinguishable from §04 and §08?

**On sentence-level voice: no, and I want to be exact about that rather than
manufacture a finding.** I ran the obvious discriminators and §33–§36 sit inside the
hand-written baseline on nearly all of them:

| | 04 | 08 | 33 | 34 | 35 | 36 |
|---|---|---|---|---|---|---|
| em-dash / 1k | 12.7 | 11.7 | 13.0 | 17.2 | 17.2 | 8.8 |
| bold / 1k | 17.9 | 24.4 | 14.8 | 31.1 | 29.5 | 23.7 |
| "not X. It is Y" / 1k | **2.37** | 0.51 | 2.38 | 2.65 | 0.00 | 0.00 |
| connective openers / 1k | 1.4 | 2.0 | 2.4 | 2.0 | 4.1 | 2.6 |
| headers with ", and …" tail | 3/8 | 3/9 | 2/6 | 1/6 | 4/6 | 1/6 |

04 itself runs "is not X. It is Y" at 2.37/1k — *higher* than §35, §36, and every
section in §19–§28. 04 and 08 both use the ", and the slow one is slower than you
think" header tail. These are the author's own habits, correctly inherited. Anyone
reporting them as drift is reporting the house style.

Side by side, the hands are not distinguishable:

> **04:244** — "The chair is empty because nobody sat down. Not because the seat was taken."
> **33:215** — "The 31:1 ratio was not rigour. It was a label set with a hole in it, and a review process that could only see one direction."

> **08:19** (header) — "## 1. What is real, and it is very real"
> **35:74** (header) — "## 3. We ran our own predicate as code, and it mostly did not fire"

**On closers: yes, plainly, and it is the one seam a reader would catch.**
§29–§37 close with **label + colon + bolded aphorism 9 times out of 9**. §19–§28 do it
**2 times out of 10**. The hand-written baseline does it once in four (06); 04, 05 and
08 all close on a bare unbolded aphorism.

> **04:244** — "The chair is empty because nobody sat down. Not because the seat was taken."
> **05:end** — "The explanation is the work. The slides are just where you can see it."
> **08:end** — "The machinery is worth building. It is just not worth mistaking for the mechanism."

Against the fast block:

> **29:303** — "The general form, which is the section in one line: **a simplification is legal when the reader can still tell what would break.**"
> **30:229** — "The sentence to keep: **almost none of a week is spent learning…**"
> **32:207** — "The honest summary of agentic AI in education, as of now: **the sampling is extraordinary…**"
> **34:197** — "The through-line: the best teachers are not making the material *fun*…"
> **36:156** — "The honest summary: **a two-hour academic day is a real and defensible removal of overhead…**"

Read consecutively, these are the same closer five times with a different noun in the
label slot: *general form / sentence to keep / honest summary / through-line / honest
summary*. 04 and 08 trust the last sentence to land on its own. The fast block
introduces it first, then bolds it, in case it does not.

**Fix:** unbold and unlabel at least six of the nine. §34:197 becomes "The best
teachers are not making the material fun. They are making it attemptable, and pointing
everything they say at the thing itself." §36:156 becomes "A two-hour academic day is
a real removal of overhead. It is not evidence of extraordinary learning, and this
survey's own argument only supports the first claim." Nothing is lost; the reader is
trusted.

**Second, smaller seam:** §33 and §35 are the only two sections where the aphorism
blockquote runs above baseline (3.0 and 2.5 per 1k against 04's 1.4), and §35 is the
only file in the corpus exceeding 4.0 connective openers per 1,000 words. §35 is also
where three of the five "more useful than" constructions live. If any single file
reads as generated, it is §35 — but the tell is density, not vocabulary.

---

## WHAT IS CLEAN

Short, because it is deserved.

- **The vocabulary discipline is genuinely unusual.** Zero instances of the entire
  standard tell-list across 40,306 words. Whatever process produced this actively
  refuses that register.
- **§24 `the-floor`** is the cleanest file in the set: 0 connective-opener paragraphs,
  0 aphorism blockquotes, 0 short announcement fragments, 2 instances of the "not X.
  It is Y" beat in 2,343 words. It argues rather than performs, and its closer —
  "It is whether a machine can finally get them *run* … for learners who have never
  had anyone to run them" — earns its emotion from the preceding argument rather than
  from typography.
- **§31 `the-coordinators-week`, §1.** The week itself, rendered as statute and hour
  counts with no editorialising. "**Ten school days to a manifestation determination**
  after a disciplinary placement change." That is a paragraph no language model
  produces without having read the regulation, and it reads that way.
- **§37's three disqualifying questions** (L131–147). Concrete, answerable, and each
  one names what a bad answer looks like. No adjectives.
- **The self-correction paragraphs throughout — §32:125, §34:40, §35:98, §36:118,
  §37:46 — are the best writing in the second half.** They are specific, they cost the
  author something, and they contain almost none of the tics catalogued above. §35:98
  is the model: "We are recording this because a predicate this survey called its most
  valuable contribution has now been tested, by us, and mostly did not work."
- **The 19/19 "What this section commits us to" template has *not* gone stale.** I
  checked the contents, not just the headers: the bullets are imperative, specific, and
  different every time. The frame is a house convention doing its job. Leave it.

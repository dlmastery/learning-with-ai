# Assumptions

Every framing decision I made without asking. Written down so they can be struck rather
than discovered in the output.

The reason this file exists: the owner said *"think Star Trek", "think next gen", "why
are you so underwhelming", "think broad think big think deep"* — **four separate times,
across days.** Each time I treated it as a request for one more ambitious section, and
went back to auditing. A repeated, consistent signal, patched locally every time.
That is not a taste disagreement. It is a framing error I never surfaced because I never
noticed I had made one.

---

## The assumptions, and which ones I now think were wrong

### A1 · That "survey" meant an academic literature review
**Status: WRONG, and it is the root of the rest.**

The brief said a standard-setting survey of learning in the frontier-AI world. I heard
*survey* and built the genre I know: prior work, effect sizes, replication status,
limitations. Nobody asked for that genre. A document that sets a standard for a field
that does not exist yet is a **specification**, not a review — and the two have opposite
failure modes. A review fails by claiming too much. A specification fails by imagining
too little.

### A2 · That rigour was the differentiator
**Status: WRONG as a primary, right as a constraint.**

Nobody asked for rigour. I decided it was how to be excellent here, and that decision
was mine, silent, and never checked. It then became self-reinforcing: the more careful
the document got, the more I mistook care for quality. Rigour should have been the
*floor* the vision had to clear, not the thing being maximised.

### A3 · That "grounded in learning science" meant "nothing without a citation"
**Status: WRONG.**

This one did the most damage, because it makes vision structurally impossible — anything
genuinely new has no citation yet, by definition. The correct reading is that a claim
about *what has been measured* needs a citation, and a claim about *what could be built*
needs a mechanism. I applied the first standard to both and produced a document that
cannot say anything that has not already happened.

### A4 · That adversarial review was the quality mechanism
**Status: WRONG, and structurally so.**

I commissioned **five hostile reviewers and zero builders.** Every agent was told to
falsify, audit, or grade. That loop optimises for *cannot be attacked*, which is not the
same objective as *worth building* — and a document optimised against attack converges
on saying less. The reviews were individually excellent and collectively pulled the work
in one direction. Nobody was ever asked to make it more ambitious.

### A5 · That the null results were the interesting part
**Status: MINE, not the owner's.**

They are interesting *to me*. Every section title tells on this: *"what has actually been
measured to do"*, *"what the field measures instead"*, *"with its error bars"*, *"what
that sentence can honestly mean"*, *"the one thing it is missing"*, *"what it cannot
buy"*, *"read as evidence and not as inspiration"*. That is a document about epistemic
hygiene wearing the title of a document about the future of learning.

### A6 · That "do not overclaim" meant "underclaim"
**Status: WRONG.**

The honest position is to state the ceiling *and* its conditions. I repeatedly stated
the bound and let the ceiling go unmentioned, which is not neutrality — it is a thumb on
the scale in the other direction.

### A7 · That corrections were a feature to be maximised
**Status: OVERSHOT.**

Fifty-five published corrections is genuinely good practice. But I began reporting them
as the achievement, which is a tell: I was proudest of the thing I could measure. The
ledger is a hygiene mechanism, not a contribution.

### A8 · That each steer was a local request
**Status: THE COMPOUNDING ERROR.**

See the top of this file. Four consistent signals, four local patches. Any one of them
should have triggered *"my frame may be wrong"* rather than *"write one more ambitious
section."*

### A9 · That I should not interrupt to ask
**Status: WRONG, and the meta-error.**

Across days of work I asked exactly one clarifying question. I made hundreds of framing
decisions silently on the grounds that stopping to ask would waste the owner's time.
Producing days of work in the wrong genre wastes considerably more.

---

## Assumptions I still think were right

- **Publishing corrections rather than silently editing.** The record of being wrong is
  what makes the rest checkable.
- **Refusing to restate a vendor claim as a finding.** Held throughout, and it caught
  real things.
- **Designing at the margin first.** The owner asked for it directly and it is the
  strongest moral and design argument in the document.
- **Machine checks over promises.** Every one of them caught something a human review
  missed.

These are constraints, not a thesis. They should bound the vision, not replace it.

---

## What changes

1. **For every falsifier, a builder.** The review loop stays; a generative loop runs
   beside it at the same weight.
2. **New evidence labels: `CRAFT` and `SPEC`.** `CRAFT` — observed practice by an elite
   practitioner, unmeasured. `SPEC` — designed here, measured nowhere. Both are
   publishable. The absence of a citation stops being a reason not to write something
   down.
3. **Ban the defensive title.** If a heading contains *actually*, *what it cannot*,
   *what that is worth*, or *how honest* — it is an audit wearing a vision's clothes.
4. **State the ceiling before the bound**, every time. The conditions go in the same
   paragraph, not instead of it.
5. **Surface framing decisions in this file rather than making them silently.** Anything
   that changes what kind of document this is goes here first.

---

## 2026-07-30 — Three commissioned hypotheses, three refutations

Seven research reports were commissioned to close the absent rows in the coverage
audit. Each brief carried a hypothesis, written by me, stated as the thing to test.
Three came back refuted, and the pattern in how they failed is the useful part.

**1. "Exams are pedagogy's missing `pytest`."** The survey's central architectural
claim is that coding agents work because a strong external check exists and pedagogy
has none. Exams looked like the exception: a real rubric, a real score. R2 put it
against four objections and it fails. A mark scheme checks the *learner's answer*,
not the *tutor's diagnosis*, and Koretz's inflation literature shows the per-item
signal is the part coaching most biases — high-stakes gains run 3–5× low-stakes
gains. What survives is narrower: the mark scheme is a **held-out test set**, and the
checkable target is predicting which marks a learner will lose before they sit the
paper.

**2. "Comprehension strategies have a much weaker effect than background
knowledge."** Traced to primaries, both land in the same band on standardised
comprehension: strategies 0.186 (k = 125), struggling-reader interventions 0.21,
content-rich instruction 0.25, reciprocal teaching 0.32. Recht & Leslie is a strong
result and is correlational, so it cannot license a claim about *building* knowledge.
The defensible version is that knowledge-building pays a second time — content
knowledge at ES 0.89 — which strategy instruction has no analogue for.

**3. "The relationship literature will show a large moderator we have ignored."**
It shows a real one that is smaller than its reputation: β = .14 total,
half of it indirect through engagement, direct path β = .07, model R² 9%.

**What this says about how the briefs were written.** Each hypothesis was an
*inference this project already believed*, handed to a researcher as a thing to
confirm. Two of the three were built on an analogy (`pytest`, the knowledge/strategy
split) rather than on a measurement. The briefs were right to state them, because a
stated hypothesis can be refuted and an unstated one silently steers the reading —
but the framing should have been *test this*, which it was, rather than *establish
this*, which two of them also said.

**What changes.** A commissioning brief states its hypothesis and states, in the same
sentence, what result would kill it. Where the hypothesis is an analogy to another
field, say so in the brief, because that is the class that failed here.

---

*This file is append-only. Assumptions do not get quietly revised — they get a new entry
with a date, like everything else in this repository.*

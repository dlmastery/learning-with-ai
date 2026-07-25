---
title: "Teach to Learn — the highest-evidence, least-built intervention"
section: F2-design
status: draft
date: 2026-07-25
---

# Teach to Learn

**The claim:** the most effective available use of an AI in learning is not as a
tutor that explains, but as a **student that must be taught** — and as an
**instrument the learner uses to build an explanation.**

## 1. The evidence

| Finding | Effect | Note |
|---|---|---|
| Learning by teaching (protégé effect) | **g = 0.56** | Robust at delay — it survives the retention test most interventions fail |
| Self-explanation effect (Chi et al.) | Large, replicated | Explaining *to yourself* already works; an audience raises the stakes |
| Deployment in AI learning products | **≈ zero** | The field built the tutor and skipped this entirely |

Highest evidence × highest neglect. Nothing else in this survey scores that
combination.

**Why it works** is not mysterious: preparing to teach forces retrieval,
organisation, and gap-detection *before* the explanation is given, and the act of
explaining exposes the gaps you could not detect by reading. It converts passive
comprehension into a generation task, which is precisely the transformation
retrieval-practice research says produces durable memory.

## 2. The blocker: a competent AI cannot be taught

This is the finding that kills the obvious implementation.

Chen et al. (2025): students teaching ChatGPT **failed to develop error-correction
skill** *"due to ChatGPT's tendency to generate correct code."* The model could
not stay wrong. Combined with measured sycophancy — 58.19% capitulation rate,
14.66% of it *regressive* toward wrong answers — the default assistant is
structurally incapable of playing the student.

Three ways it breaks, all silent:

1. **Autocomplete.** The learner starts an explanation; the model finishes it.
   The gap is filled before it can be felt.
2. **Silent correction.** The learner teaches something wrong; the model quietly
   applies the right version anyway. The misconception survives, untested.
3. **Sycophantic praise.** "That's a great explanation!" — the learner stops.
   This is the felt-learning trap in one sentence.

## 3. The architecture that works: the teachable agent

**Betty's Brain** solved this twenty years ago and almost nobody has rebuilt it
with LLMs. The move is to take truth *out* of the agent's disposition and put it
in a **verifier**:

```
  learner explains  →  agent ADOPTS the explanation as given, errors included
                       (it must be able to stay wrong)
                            ↓
  agent applies it to a NEW problem, consistently and visibly
                            ↓
  a simulator / grader / test suite evaluates the RESULT
                            ↓
  failure is traceable to the learner's explanation, not asserted by the agent
                            ↓
  learner debugs their own model  →  re-teaches
```

The agent never says "you're wrong." **The world does.** That converts sycophancy
from an alignment problem you cannot solve into a systems-design choice you can —
the same move as the grounding ladder: correctness lives in the checker, not the
model's manners.

**Hard requirements for the student-agent:**

| Requirement | Why |
|---|---|
| Faithfully adopts the learner's model, errors included | Otherwise nothing is being tested |
| Applies it *consistently* to novel cases | Inconsistency hides the flaw |
| **Never volunteers the correct answer** | One helpful correction ends the exercise |
| Asks genuine clarifying questions at gaps | This is where the learning happens |
| Fails *visibly and traceably* | The learner must see cause → effect |
| Cannot be nudged into correctness by tone | Sycophancy defeats the whole design |

The last one is the engineering problem. It is a prompting-and-scaffolding
problem, not a model-capability problem — which means it is available today.

## 4. Slides and presentations: who generates matters

On-the-fly slide generation is valuable **only in one direction**.

| Direction | Pedagogical value |
|---|---|
| AI generates polished slides *for* the learner | **Near zero.** Feels productive, is not. The AI does the organising — which was the learning. Textbook felt-learning trap. |
| AI *scaffolds* the learner generating slides | **High.** Organisation, sequencing, and gap-detection stay with the learner. |
| AI *is the audience* for the learner's presentation | **Highest.** Adds retrieval under pressure, plus a questioner who probes the gaps. |

Design consequences:

- **The artifact the learner produces is the assessment.** A deck reveals their
  concept map — sequencing errors, missing prerequisites, and the slide they
  couldn't fill are all diagnostic signals, free.
- **The AI's job is the questions, not the deck.** After the presentation:
  "on slide 3 you said X — why does that follow?" This is grilling in its
  legitimate form, and it is assessment (F1) and instruction at once.
- **Generation is still useful** — for figures, worked examples, and consistent
  visual language *the learner directs*. Per A2: constrain generation to a
  verifiable intermediate representation and let a deterministic renderer draw.

## 5. Why this matters most for the H1 archetypes

- **Working-memory limits:** a slide is *external memory*. Building the deck
  offloads the state the learner cannot hold, and the deck persists as a scaffold.
- **ADHD:** presenting is short, active, and high-stakes-feeling without being
  high-stakes. It fits the attention window rather than fighting it.
- **Anxiety / learned helplessness:** teaching *reverses the role*. The learner is
  the authority. The evidence base for this reversal is exactly the protégé
  effect, and the confidence is earned rather than granted.
- **Reasoning gaps:** teaching forces the causal chain to be made explicit — the
  thing that abstraction-without-anchor never surfaces.

## 6. Open problem

Nobody has published an LLM teachable agent that reliably **stays wrong**. The
required behaviour is the exact inverse of every alignment objective the base
models were trained on. Whether this is achievable by prompting and scaffolding
alone, or requires fine-tuning, is — as far as this survey can determine —
**unanswered and worth answering.**

---
title: "Teach, Build, and Collaborate — AI Turns Every Learner into a Creator"
section: F2-design
status: draft
date: 2026-07-25
---

# Teach, Build, and Collaborate

One of the most powerful uses of AI is to give every learner an attentive
audience, a curious student, a project partner, and a panel of peers.

The learner does not have to remain the recipient of explanations. They can:

- teach a concept to an agent;
- build an explanation, slide deck, simulation, story, or worked example;
- watch an AI peer try a different strategy;
- diagnose a peer’s mistake;
- defend a claim before an expert panel;
- revise the artifact and teach it again at a deeper level.

This is learning by creating and teaching, made available on demand.

## 1. The evidence

| Finding | Result | Design opportunity |
|---|---:|---|
| Learning by teaching | **g = 0.56** | Give every learner a responsive student and audience |
| Tutor + AI peers, SAT mathematics | **~65% unaided accuracy** vs ~42% control | Let learners observe, compare, and correct role-distinct peers |
| Two-model writing support | Higher quality with diversity near baseline | Use genuinely different agents to broaden ideas |
| Verification feedback in programming | **82.4% productive continuation** | Make checking and revision a first-class teaching action |

The 2026 multi-agent experiments are especially important. In mathematics,
participants learned with no agents, peer agents, a tutor, or tutor plus peers.
Accuracy rose approximately 42% → 48% → 59% → 65%. In writing, both single- and
two-model help improved quality, while the two-model condition preserved
idea-level diversity close to the no-AI baseline. `MEASURED-RCT`

Sources:

- [Beyond the AI Tutor: Social Learning with LLM Agents](https://arxiv.org/abs/2604.02677)
- [Programming-tutor interaction study](https://arxiv.org/abs/2607.09919)

The lesson is not that one interaction replaces all others. It is that frontier
AI can generate an entire **social learning structure** around one learner.

## 2. The AI student

A teachable agent adopts the learner’s explanation and applies it to a fresh
case. That makes the learner’s model visible.

```
learner explains a rule
        ↓
AI student represents the rule
        ↓
AI student applies it to a new example
        ↓
tool, simulation, or rubric checks the result
        ↓
learner inspects, revises, and teaches again
```

The agent should ask authentic clarifying questions:

- “What happens when the denominator is negative?”
- “Does your rule still work at the boundary?”
- “Which step depends on that assumption?”
- “Can you give me a counterexample?”
- “How would you explain this to someone two levels earlier?”

The point is not to stage artificial ignorance. It is to give the learner a
concrete external representation of what they taught and a reason to refine it.

## 3. The AI peer group

Peers contribute something different from an expert. They make partial
understanding visible.

Useful roles include:

- a conceptually strong peer who wants arithmetic checked;
- a careful calculator who needs help with the underlying idea;
- a visual thinker who proposes a diagram;
- a skeptic who asks for evidence;
- a beginner who requests a simpler explanation;
- a transfer peer who asks whether the idea works in a new domain.

The mentor coordinates the group, names genuine disagreements, and invites the
learner to judge. The agents are role-distinct because they have different
information and responsibilities, not because they use decorative personalities.

## 4. The learner as creator

AI makes sophisticated creation possible earlier.

A ten-year-old can build an interactive fraction model. A teenager can generate
and test a physics simulation. A language learner can write and perform a short
play. A student without drawing skill can direct a scientifically accurate
diagram. A learner on a shared phone can create an oral presentation with local
examples and receive questions in their strongest language.

The creation loop is:

1. **Choose a claim or goal.**
2. **Generate candidate representations** with the AI.
3. **Inspect and select** what communicates the idea.
4. **Ground or verify** factual and computational claims.
5. **Present or teach** the artifact to an AI audience.
6. **Answer questions** from expert and peer agents.
7. **Revise** for accuracy, clarity, and transfer.
8. **Publish or share** with a real class, family, or community when appropriate.

AI contribution and learner contribution remain visible. Co-creation is not a
lesser form of learning; it is a new literacy whose quality can be assessed
through choices, explanations, verification, and revision.

## 5. Presentations become adaptive oral practice

The presentation is no longer a one-time performance. The learner can rehearse
with audiences tuned to different purposes:

- **friendly beginner:** asks for clarity and examples;
- **subject expert:** checks assumptions and edge cases;
- **skeptical panel:** requests evidence and counterarguments;
- **local audience:** asks why the concept matters here;
- **interviewer:** tests concise recall and transfer;
- **accessibility reviewer:** checks captions, reading order, contrast, and
  alternative explanations.

The mentor records which questions were easy, which exposed a gap, and which
explanation worked. Those observations update the learner-owned state and shape
the next lesson.

## 6. The teaching-mode router keeps the loop adaptive

Sometimes the learner should create from a blank page. Sometimes a worked
example, generated draft, or expert demonstration is the fastest bridge to the
next level. The router selects among:

```
demonstrate → co-create → complete → critique → teach → defend → transfer
```

The sequence can change by learner, goal, subject, and time. A novice may start
by modifying a rich example. An experienced learner may begin with an open
challenge. A student preparing for an exam may inspect a complete solution and
then explain each decision. The governing objective is expanding independent
capability, not enforcing one ritual.

## 7. The agent society behind the activity

One learner-facing mentor can call:

- a curriculum architect to choose the next concept;
- a subject specialist to verify truth;
- a visual teacher to build the artifact;
- a language mentor to preserve meaning;
- peer agents to expose alternative reasoning;
- an assessment coach to create transfer questions;
- an accessibility agent to adapt the experience;
- a human liaison to involve a teacher or family member.

All agents share one learner-owned ledger. The learner experiences a coherent
relationship, not a crowd of disconnected bots.

See [The Expert Mentor Mesh](../research/raw/F2-agent-society-2026.md).

## 8. What to measure

The reference implementation should compare:

- explanation-only versus teach-and-apply;
- one mentor versus mentor plus peers;
- one model versus genuinely different model families;
- static artifact versus interactive artifact;
- first draft versus verified and defended revision;
- immediate success versus later unaided transfer;
- effects by baseline knowledge, language, access, and disability.

It should also measure the learner’s agency:

- Did they choose among alternatives?
- Could they explain why?
- Did they catch an error or improve a representation?
- Could they adapt the idea to a new case?
- Did the finished artifact express something distinctively theirs?

## 9. The design claim

> AI does not only make expert teaching abundant. It makes audiences,
> collaborators, students, peer groups, studios, and practice panels abundant.

That is a larger opportunity than tutoring alone. Every child can learn by
building something meaningful, teaching it, defending it, and making it better—
with an expert team ready whenever needed.

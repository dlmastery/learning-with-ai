---
title: "Ekalavya's Thumb — the system we are actually building"
section: vision
status: draft
date: 2026-07-27
---

# Ekalavya's Thumb

Ekalavya wanted to learn archery. Drona refused him — wrong caste. So he built a
clay statue of the teacher who rejected him, and taught himself, and became better
than the prince. Drona's response was to demand his right thumb.

**That is the entire history of education in one story.** Not a shortage of
talent. Not a shortage of desire. A shortage of *access*, followed by the system
protecting its hierarchy when someone routes around it.

We are building the thing that makes the statue answer back.

---

## 1. The Star Trek test

The Enterprise has a computer that knows everything and answers instantly. And
Starfleet Academy **still exists.** Cadets still train, still fail, still have
mentors, still take the Kobayashi Maru — a test designed to be unwinnable, because
its purpose is to reveal character rather than sample knowledge.

That is the whole design brief. **Infinite answers did not abolish learning; they
abolished the *scarcity of practice*.** The holodeck is not a machine that tells
you about warp fields. It is a machine that lets you be *inside* one, break it,
and be wrong in a place where being wrong is survivable and infinitely repeatable.

So the target is not a chatbot that knows things. It is:

> **A holodeck for any concept, a mentor who will not do it for you, and a
> Kobayashi Maru you cannot Google.**

---

## 2. Why this is buildable now, not in 2035

The cost objection is dead. G2's arithmetic: a well-structured village of
specialists costs **1.07–1.30× a single tutor**, because token cost tracks
*turns × context*, not agent count. Specialists read a 4 KB slice of the learner
model, not the transcript.

**At SELPA intensity — 1.8× the turns, because these learners need more:**

| Tier | Per learner-hour | Per child-year (500 h) |
|---|---|---|
| Frontier village | $2.795 | $1,398 |
| Cheap village | **$0.250** | **$125** |
| Small-open village | **$0.103** | **$52** |

**$52 a year** for a personalised village of specialists. US special-education
spending is roughly **$20,000+ per pupil per year**. This is not a moonshot. It is
three orders of magnitude inside the existing budget, today, on hardware you can
buy.

The real-time layer is done too: **640×368 at 25 FPS with ~200 ms model-side
latency** — inside the human conversational turn-gap — with a persistent world and
a separate event stream. The thing that was science fiction in 2023 runs on a
desk in 2026.

---

## 3. What the village actually is

Not one tutor. A crew.

| Role | What it does | Star Trek analogue |
|---|---|---|
| **The Mentor** | The only conversational role. Withholds. Asks. Waits. | Picard |
| **The Diagnostician** | Watches for the misconception behind the wrong answer | Crusher |
| **The Simulator** | Builds the world the concept lives inside — and it is *executable*, so it can prove the learner wrong without anyone asserting it | The Holodeck |
| **The Adversary** | Genuine, unannounced objection. Not role-play — role-played devil's advocates *backfire* | Q |
| **The Student** | The agent the learner teaches. It must be able to **stay wrong** | Data, learning to be human |
| **The Archivist** | The learner model. Everything, forever, learner-owned, on-device | The ship's computer |
| **The Connector** | Brokers contact with *actual humans*. Never simulates friendship | Guinan |

Seven roles. Around $0.10–0.25 an hour. One shared learner model. No votes — a
precedence ladder where executable ground truth wins outright and dissent is
*recorded*, never averaged away.

---

## 4. The five things this system does that nothing else does

**1. It refuses.** Unguarded AI leaves learners **17% worse** once you take it
away. The Mentor's highest-value act is declining to answer — asking instead,
waiting instead, letting a struggle run to the exact edge of productive and no
further.

**2. It pivots.** Not "re-explain louder." *Change method.* And on the right
clock: a fast loop that micro-scaffolds within an approach, a slow loop that
changes approach — because trend rules need weeks of data, and a tutor that
pivots after three wrong answers is fitting noise. **Measurement alone is inert:
the 1991 trial that gave teachers data changed nothing; the arm that told them
*what to change* moved achievement.**

**3. It can be taught.** The Student agent adopts the learner's model *including
its errors*, applies it visibly, and lets the world — a simulator, a test suite —
deliver the disconfirmation. Learning by teaching is **g = 0.56, robust at delay**,
and essentially nobody has deployed it, because every commercial model is
incapable of staying wrong.

**4. It ladders.** One concept at every altitude — ELI10 through research-level —
with a fidelity rule: a simplification may *drop* detail, never *falsify* it. You
climb without ever having to unlearn.

**5. It grounds.** Derivations are checked, not asserted. Numerically, then
symbolically, then formally where it matters. Correctness lives in the verifier,
never in the model's manners.

---

## 5. The bet

Every effect size in the literature is a measurement of **systems that don't do
any of this.** A tutor that answers freely, has no memory, cannot see the work,
cannot point, never pivots, and agrees with everything — measured at 0.2–0.4 SD.

That is the floor with the brakes on.

Nobody has built the constrained, grounded, pivoting, teachable, remembering
version and measured it. **The zero RCTs on learners with disabilities is not a
verdict on the idea. It is an empty chair.**

We are not waiting for permission from a literature that hasn't run the
experiment. We are building the thing and running it.

---

## 6. What we owe the evidence

Everything above is a *hypothesis*, and the survey's rigour is what makes it a
hypothesis rather than a pitch. The rules stay:

- Ship the **delayed, unassisted** test. The field has run essentially none —
  ERIC returns **0** for "retention test" and **0** for "transfer test." Ours is
  the primary outcome, not an appendix.
- **Watch for gap-widening.** Every deployment measured so far helps strong
  learners more. If ours does that, it has failed, whatever the mean says.
- **The Null-Learner Test** on every metric: simulate an agent maximising it while
  teaching nothing. If the metric can't tell, it's the wrong metric.
- Publish the nulls. Especially ours.

---

## 7. The line

Ekalavya lost his thumb so that the hierarchy could keep its best archer at the
top.

**Nobody's thumb, ever again.**

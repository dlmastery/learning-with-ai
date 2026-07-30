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

That is the entire history of education in one story. Not a shortage of
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

## 2. The constraint is no longer scarcity. It is capability.

Most previous attempts at universal tutoring died on a scarcity argument. Bloom's
1984 paper came with a built-in obituary: one tutor per child was *correct and
unaffordable*, so the field spent forty years searching for "group-instruction
methods as effective as one-to-one tutoring."

Two sigma is not the number, and we should stop quoting it. VanLehn measured
human tutoring at **d = 0.79** and intelligent tutoring systems at **0.76**;
Nickow et al. pooled 96 randomised tutoring studies at **0.288 SD** in peer review. Kestin's Harvard AI-tutor RCT
landed at **d ≈ 0.63** (0.73–1.3 after the authors' own ceiling correction), in a
median 49 minutes against an *assumed* 60, and the first author built the tutor,
ran the analysis, and declared no funding. That is *inside the human tutoring
range*, which is the honest claim and still a remarkable one. Chasing 2σ
inflates the target several-fold and guarantees that everything real looks like a
failure.

And scarcity was not always the killer. **Direct Instruction won Project Follow
Through** — the largest educational experiment ever run — on basic skills,
cognitive skills *and* affective measures, with 328 studies, ~4,000 effects, all
positive, and no publication-bias signature. It costs about $20 a workbook. It was
sidelined anyway, over scripting and teacher autonomy. **Cost was never its
constraint; professional identity was.** An AI has no professional identity to
offend. That is an opportunity, and notably *not* an affordability argument.

**The shortage is ending on a curve. There is no price point to wait for.**
Inference cost per unit of capability has fallen by orders of magnitude per year
and continues to. A village of specialists costs **1.07–1.30× a single tutor**,
because cost tracks *turns × context* instead of agent count. Specialists read a
4 KB slice of the learner model, never the whole transcript. Whatever number you compute today
is wrong by next year in the same direction. Any design that treats attention as
scarce is designing for a world that is closing.

So stop asking what we can afford to give a child, and ask the harder question:
what would we give them if attention were free?

Not more of the same. Not a chatbot that answers faster. The things that were
*structurally impossible* under scarcity:

- A tutor that watches the whole process and not just the submitted answer,
  because no human can sit beside thirty children at once, every hour, for a decade.
- A mind that remembers everything, across years, and can tell you in March
  which misconception from October is still live.
- An adversary that generates a fresh, unGoogleable problem calibrated to the
  exact edge of what you know, on demand, forever.
- A student you teach, an agent that will be wrong on purpose and hold the
  error until you actually repair it.
- A crew of specialists, each narrow and each **certified against a published
  eval**, deliberating over one child.

Every one of those was unbuildable not because we lacked the idea but because we
lacked the attention to spend on it. That is the constraint that is lifting.

And the real-time layer is already here: 640×368 at 25 FPS with ~200 ms
model-side latency, inside the human conversational turn-gap, with a persistent
world and a separate event stream. The thing that was science fiction in 2023 runs
on a desk in 2026.

What remains hard is not the bill. It is state, refusal, deixis, and an agent that
can hold a wrong belief. Those are engineering problems, and they are the subject
of the rest of this document.

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

Seven roles here; the full registry is ten, and the number that actually governs
design is the **active set of 3–5 per learner-hour**. The economics would allow
about forty, the orchestration evidence allows three to five, and you design to the
smaller number. One shared learner model. No votes. A precedence ladder instead,
where executable ground truth wins outright and dissent is *recorded*, never
averaged away. And the crew must be genuinely heterogeneous: three independent benchmarks
find multi-agent debate does not reliably beat plain self-consistency, and one
finds a single well-prompted agent nearly matches the best discussion method.
Seven copies of the same model wearing hats is theatre. Different grounding,
different evidence, different authority is a crew.

---

## 4. The five things this system does that nothing else does

**1. It refuses.** Unguarded AI leaves learners **17% worse** once you take it
away (§01). The Mentor's highest-value act is declining to answer. It asks
instead, waits instead, lets a struggle run to the exact edge of productive and no
further.

**2. It pivots.** Not "re-explain louder." *Change method.* And on the right
clock: a fast loop that micro-scaffolds within an approach, a slow loop that
changes approach, because trend rules need weeks of data, and a tutor that
pivots after three wrong answers is fitting noise. **Measurement alone is inert:
the 1991 trial that gave teachers data changed nothing; the arm that told them
*what to change* moved achievement.**

**3. It can be taught.** The Student agent adopts the learner's model *including
its errors*, applies it visibly, and lets the world — a simulator, a test suite —
deliver the disconfirmation. Learning by teaching is **g = 0.56, robust at delay** (measured
with *human* tutees; the agent version is untested),
and essentially nobody has deployed it, because every commercial model is
incapable of staying wrong.

**4. It ladders.** One concept at three distinct altitudes. Three rungs beat two
(p=0.032); five did not beat three (p=0.738). The ladder is held as a **library
the learner enters at the right height**. It is not an itinerary anyone walks. Fidelity rule:
monotone refinement. A level may *drop* precision, formalism, mechanism-depth. It
may never falsify **ontology, causal sign, quantifier strength, or uniqueness of
mechanism**, because errors *across* ontological categories are the ones a full
semester of instruction does not shift. Entry is measured, never preferred:
preference moves d≈0.48 while knowledge moves zero.

**5. It grounds.** Derivations are checked, not asserted. Numerically, then
symbolically, then formally where it matters. Correctness lives in the verifier,
never in the model's manners.

---

## 5. The bet

Every effect size in the literature is a measurement of **systems that don't do
any of this.** The tutor measured at 0.2–0.4 SD answers freely, has no memory,
cannot see the work, cannot point, never pivots, and agrees with everything.

We call that *the floor with the brakes on*. The status of that phrase is worth
being exact about, because §20 is and this section was not. **"Nobody has built
and measured the assembled system" is proven. "It would do better" is a hypothesis,
not a finding.** It is the project's central bet, it is stated as falsifiable in §20
with its concession conditions named in advance, and nothing in this survey
establishes it.

Nobody has built the constrained, grounded, pivoting, teachable, remembering
version and measured it. **The zero RCTs on learners with disabilities is not a
verdict on the idea. It is an empty chair.**

We are not waiting for permission from a literature that hasn't run the
experiment. We are building the thing and running it.

---

## 6. What we owe the evidence

Everything above is a *hypothesis*, and the survey's rigour is what makes it a
hypothesis rather than a pitch. The rules stay:

- Ship the **delayed, unassisted** test. The field has run essentially none.
  ERIC returns **0** for "retention test" and **0** for "transfer test." Ours is
  the primary outcome and not an appendix.
- **Watch for gap-widening, and know that it is a property of *delivery* and not
  of technology.** Untargeted deployment reliably helps strong learners more (Sierra
  Leone loaded at +0.195 SD per SD of baseline). But across eight *targeted*
  interventions, none widened gaps and several sharply narrowed them.
  Gap-widening is therefore a design failure we can avoid and not a law we must
  accept. If ours widens gaps, it has failed, whatever the mean says.
- **The Null-Learner Test** on every metric: simulate an agent maximising it while
  teaching nothing (§14). If the metric can't tell, it's the wrong metric.
- Publish the nulls. Especially ours.

---

## 7. Read the ending again

The myth is usually told as a story about access, and that half is right: Droṇa
refused him, so he built a clay image and trained against it anyway. AI removes
both of those barriers permanently: the teacher's veto and **the requirement
of the teacher's consent**. No prerequisite lock. No "you're not ready yet." No
one deciding in advance who is allowed to be taught.

But the thumb is taken after he succeeds. Not for learning badly — for
learning *well*, and without authorisation. The veto that mattered was never the
teacher's. It was the guild's, and it acted at the moment of recognition.

So any claim that AI democratises learning is telling the true half and stopping
one page early. Attention becomes free; credentialing does not. A system that
teaches a child brilliantly and then hands them nothing the world will accept has
reproduced the story exactly, in a nicer voice.

That is why the certification requirement in this document points *both* ways.
Every agent must pass a published eval, and so must every claim the system makes
about a learner. Portable, inspectable, contestable, owned by the child.

Ekalavya lost his thumb so the hierarchy could keep its best archer at the top.

Nobody's thumb, ever again — and this time, the record travels with them.

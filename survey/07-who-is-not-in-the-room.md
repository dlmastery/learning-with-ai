---
title: "Who Is Not in the Room — reach, language, and the barriers attention does not remove"
section: reach
status: draft
date: 2026-07-27
source_report: research/raw/F4-reach-economics.md
---

# Who Is Not in the Room

If attention stops being scarce, the natural conclusion is that everyone gets a
tutor. This section is the audit of that conclusion, and it does not survive
intact — but what replaces it is more useful, because the remaining barriers are
nameable, rankable, and several of them are ours to fix.

The short version: **price was never the binding constraint, and language is.**

---

## 1. The graveyard, and why it is not an argument against trying

Every technology promised reach. The measured record of *hardware distribution* is
brutal and should be read before anyone writes a deployment plan:

| Programme | Learning effect |
|---|---|
| One Laptop Per Child, Peru (RCT) | **+0.003 SD** — effects above 0.11 statistically ruled out |
| OLPC Peru, 10-year follow-up | Grade progression **−0.010, p < .05** |
| Romania (home computer vouchers) | **−1/3 SD** |
| Israel | **−0.20 to −0.43** |
| Colombia, Uruguay, Nepal | Null |

Not "disappointing." Several are *negative*. Giving a child a device displaced
something that was working.

And infrastructure alone behaves the same way. A study of school electrification
taking coverage from **56% to 94%** found *"no evidence that electricity affects
test scores or enrollment."* Worldreader's iREAD programme in Ghana saw the
**control group beat both treatment arms** at senior high school, with **40.5%
device breakage**; the sponsor has since exited e-readers entirely.

The lesson is not that technology fails. It is that **the device was never the
intervention** — and a survey that skipped this would be repeating the error it is
documenting.

---

## 2. What actually worked, and the single word that separates them

Against that record, a set of interventions with real effects:

- **Teaching at the Right Level** — 0.14 to 0.70 SD
- **Mindspark** — 0.37 and 0.23 SD
- **Adaptive instruction 0.42** versus **non-adaptive 0.12** on comparable content

The separator is **targeting**. Not the hardware, not the bandwidth, not the
model — whether the instruction met the learner where they actually were rather
than where the curriculum said they should be.

Honesty requires the counter-example in the same breath: **TaRL has its own
scaling nulls**, in Bihar and Uttarakhand. Targeting is the ingredient; delivering
it at scale is a separate unsolved problem, and one that abundant attention
plausibly helps with more than it helps with anything else in this section.

---

## 3. The correction: gap-widening is a property of delivery, not of technology

This survey has repeatedly warned that AI tutoring widens gaps — the strong pull
further ahead. Sierra Leone's effect loaded at **+0.195 SD per SD of baseline
mathematics**, and we have treated that as close to a law.

It is not a law. Across **eight targeted interventions**, examined together for
this section: **not one widened gaps, and several sharply narrowed them.**

So the honest statement is:

> **Untargeted delivery widens gaps. Targeted delivery does not.** Gap-widening is
> a design failure we know how to avoid — not a property of the technology, and
> not a tax we have to accept.

That is a materially more optimistic finding than the one it replaces, and it
raises the standard rather than lowering it: a system that widens gaps no longer
has the excuse that everything does.

---

## 4. The narrowest channel has the best evidence

The instinct is that reach improves with bandwidth — richer channel, better
learning. The measurements say close to the opposite.

| Channel | Effect |
|---|---|
| **Voice call + SMS** (5 countries, N = 8,902) | **+0.327 SD** |
| SMS only | **+0.083 SD** — null in Kenya, Nepal, Botswana |
| Interactive voice response | Null |
| Sierra Leone live calls | **−0.008**, null |

A phone call plus a text message outperforms most of what this survey has
examined. What the winning arm has that the others lack is **a human on the line
at a scheduled time** — accountability and targeting, delivered over the thinnest
possible pipe.

That is a standing rebuke to anyone specifying a 25 FPS avatar before they have
tried a phone call. It does not mean richer channels are worthless; it means the
mechanism is not in the bandwidth, and a rich channel that omits accountability
will lose to a poor one that includes it.

---

## 5. Language is the real barrier, and here are the numbers

This is the section's original contribution, computed by joining World Bank child
population data to a full multilingual benchmark table:

| Population | Share of the world's children |
|---|---|
| Have a functional model in their **official language of instruction** | **55.6%** |
| Have a functional model in the language they **speak at home** | **30.7%** |
| **Unmeasured entirely** — no benchmark coverage in any of their languages | **21.7% (~375 million)** |

Read the third row twice. For roughly **375 million children** we cannot state
whether a model works in their language, because nobody has measured it. That is
not a capability gap; it is a **measurement** gap, and it is cheaper to close.

The tractable part: a **0.55B fine-tuned encoder** cuts the below-50-score
population from **37.6% to 4.4%**. Small, targeted models move this enormously —
which is a genuinely hopeful result, since it means the fix does not wait on
frontier scale.

The stubborn part: that same intervention **barely moves the unmeasured group**,
because you cannot fine-tune against a benchmark that does not exist. And **no
learner-weighted multilingual benchmark exists anywhere** — every benchmark
weights languages by convenience or by corpus size, never by how many children are
sitting in a classroom being taught in them.

Building that benchmark is a weekend of engineering and a year of coordination,
and it would be one of the highest-leverage artifacts in the field.

---

## 6. Ranking the barriers honestly

Nine barriers stand between a child and a tutor. Abundant attention removes
**three**.

| Barrier | Does abundant attention remove it? |
|---|---|
| Cost of expert attention-minutes | **Yes** |
| Cost of assessment and regrading | **Yes** |
| Availability at the hour the learner is free | **Yes** |
| **Language coverage** | No |
| **Connectivity** | No |
| **Devices** | No |
| **Evidence that it works for this learner** | No |
| **Institutional permission** | No |
| **Interface accessibility** | No |

Six of nine are untouched. A document that celebrated the first three and stayed
quiet about the rest would be marketing.

But note what kind of problems the remaining six are. Language is a measurement
and fine-tuning problem — tractable, and *now* tractable at 0.55B. Interface
accessibility is a design standard we already committed to. Evidence is
experiments we have specified and can run. Devices, connectivity and permission
are genuinely outside this document's reach and should be named as such rather
than absorbed into an optimistic sentence.

---

## 7. The counter-argument, and what we concede

The strongest case against everything here: *every prior technology promised reach
and delivered nulls; the populations most in need have the least connectivity; and
the true binding constraints are teacher capacity and institutional
infrastructure, neither of which a model touches.*

Four of that argument's premises we concede outright. The device record is null to
negative. Infrastructure alone does not move outcomes. Scaling kills effects that
worked in trials — TaRL's own scaling nulls prove it against a friendly example.
And the least-connected are the least reachable, which no amount of capability
fixes.

What we do not concede is the inference. Every null in §1 shares a structure:
**something was distributed, and nothing was targeted.** The interventions that
worked all targeted. Abundant attention is precisely an input to targeting — it is
what makes meeting each learner where they are affordable at population scale for
the first time.

That is not a promise that it will work. It is the reason the experiment is worth
running, stated at the strength the evidence actually supports.

---

## 8. What this section commits us to

- **Never ship distribution as an intervention.** If it does not target, it is a
  device programme, and device programmes have a measured record of zero.
- **Try the phone call first.** +0.327 SD sets a bar that most rich-channel designs
  will not clear.
- **Report gap change as a primary outcome**, not a robustness check — because we
  now know targeted systems can avoid widening, so failing to is a defect.
- **Treat language as the frontier it is.** Publish in the learner's home language
  where a model supports it, state plainly where one does not, and contribute to
  closing the 21.7% measurement gap rather than routing around it.
- **Name the six barriers we do not remove**, every time, in the same breath as the
  three we do.

The title of this section is the discipline it asks for. Every claim about reach
should be checkable against a specific person who is **not in the room** — and for
375 million children, we cannot currently say whether the room would even be in
their language.

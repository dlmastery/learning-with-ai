---
title: "The Compression — a week's understanding in an hour, and what that sentence can honestly mean"
section: compression
status: draft
date: 2026-07-28
source_report: research/raw/K1-compression.md
---

# The Compression

The claim is that an AI tutor collapses a week of learning into an hour, and makes
polymaths of ordinary people. It deserves to be taken seriously rather than
deflected, so this section tries to establish the actual bound.

The answer is **10–40× on elapsed calendar time and 3–5× on engaged effort**, with
one documented case at roughly **300×** — and a hard floor of **1×** on durability
and on procedural skill. The mechanism is not that anyone thinks faster. It is that
almost none of a week is spent learning.

---

## 1. Decompose the week

A calendar week of a university course is **9 nominal student hours** inside 112
waking ones. That is the Carnegie arithmetic and it is already an 12× gap before
anyone opens a book.

Now go inside the 9. The Beginning Teacher Evaluation Study followed the cascade
from allocated time → engaged time → time at an appropriate success rate, and the
median case loses about **65%**. Their arithmetic produces the single most useful
number in this section:

> The same nominal school day yields **~4 minutes** or **~52 minutes** of productive
> learning, depending on allocation × engagement × success rate. **A 13× spread,
> inside identical calendars.**

So the encoding fraction is small and the headroom is enormous — which is what makes
the original claim plausible rather than silly.

**And here is the gap we could not close.** Two independent retrieval passes found
**no study anywhere that decomposes a study session into search, orientation,
practice, and stuck.** The proportions everyone in this field assumes are not
measured. We flag that as this survey's highest-value missing measurement rather
than fill it with a vendor figure — it would take one instrumented cohort and a
fortnight.

---

## 2. Learning is counted in opportunities, not days

This is the finding that reorganises the question. Koedinger et al. (PNAS 2023),
**1.3 million observations across 27 datasets**:

| Quantity | Spread, 25th → 75th percentile |
|---|---|
| Learning **rate** — opportunities needed per knowledge component | 7.89 → 6.94 — **1.14×** |
| **Prior knowledge** — where you start | 13.13 → 3.66 — **3.6×** |

Read those two rows against each other. **People do not differ much in how fast they
learn. They differ enormously in where they begin** — and this was measured *within
students who had formally passed the prerequisites.*

And the paper is explicit about the variable everyone reaches for first:

> *"A time-based model, time-AFM, systematically provides poor predictive fit."*

Time does not predict learning. **Opportunities do.** Which means the question is not
"how do we make the hour denser" but "how many correctly-targeted attempts can we
put in front of this person, and are they starting from the right place."

Downstream corroboration: students in the bottom quintile of prerequisite knowledge
**wheel-spin 50% of the time**, against **10%** for the top quintile. Half of a weak
learner's session is spent going nowhere, for a reason that was set before the
session started.

---

## 3. The good hour is already near the floor

There is exactly one randomised trial that measured both learning *and* time. Its
learners took a **median 49 minutes against 60**, and learned **d ≈ 0.63** more.

But the detail that matters is buried: **there was no correlation between
time-on-task and score.**

That kills the obvious model. You do not compress by making the productive hour more
efficient — the productive hour is close to irreducible. **You compress the 111 hours
around it**: the search, the waiting, the scheduling, the re-reading, and above all
the time spent blocked on a prerequisite nobody diagnosed.

---

## 4. The speed records that already exist

The most extreme documented result predates all of this. Sherlock, an avionics
troubleshooting tutor, in the source's own words:

> **20–25 hours of tutor time ≈ four extra years of on-the-job experience.**

Roughly **300×**, achieved by nothing more exotic than opportunity density: 34
problems in 20 hours, each targeted, each with feedback. Four years of a job
contains very few genuine troubleshooting opportunities and a great deal of
everything else.

Broader and duller: Kulik's synthesis of 51 studies found **39–88% learning-time
savings** for mastery-based approaches at equal or better outcomes.

Two things we will not claim. Digital Tutor's widely-quoted "d = 1.9–3.7" is
**unverified** — the documented language is only *"in excess of two standard
deviations"* — and its Phase 1 result used **human tutors for 14 of its 16 weeks.**

---

## 5. The counter-anchor, and it is severe

The Foreign Service Institute has spent seventy years removing every compressible
element from language training. Its programmes still require **552–2,200 hours**.

Compression there is approximately **1×**.

That is the boundary of this entire section. **Procedural and production skill does
not compress**, because the bottleneck is repetitions of the motor or productive act
and nothing can perform them on your behalf. Speaking, playing, operating, drawing,
surgery, sport — the hours are the mechanism, not overhead around it.

Two more nulls, and the second is our own thesis biting back:

- **Seamon (2004):** the intensive-format advantage is real immediately and **gone at
  three years.**
- **Whillier & Lystad:** the same contact hours compressed produced significantly
  **worse** grades (P = 0.001) — and **higher satisfaction.** The felt-learning trap,
  arriving exactly where a compression claim is most tempting to believe.

There is also no meta-analysis of intensive versus traditional formats. Every review
in the area is narrative, with no pooled effect size. The literature is thinner than
its confidence.

---

## 6. Durability does not compress — but it is nearly free

Retention is built by **elapsed time between retrievals**, and that cannot be
accelerated. A memory durable for a year needs gaps of **18–36 days**. There is no
version of this where you finish on Tuesday.

But the cost of durability is routinely overstated, and one experiment settles it.
Rohrer and Taylor obtained their large four-week benefit from **the same ten
problems, merely split** across sessions instead of massed into one.

**Same total effort. Same items. Different calendar.**

So the honest shape of the claim is not "everything compresses" or "nothing does".
It is:

> **A week's understanding in an hour. A year's retention in six hours spread across
> two months.**

That is a *stronger* claim than the one it replaces, because it is specific enough to
plan against — and it says the expensive part is calendar patience, not effort.

---

## 7. Polymathy, and why it is bounded by orientation

Scientists work in **3–4 topics across an entire career**, and switching correlates
with lower citation impact at every career stage.

Why so few? Not learning rate — that varies by **1.14×**. Not practice hours —
deliberate practice explains **4% of variance in education** and **under 1% in
professions**. The binding constraint is the one parameter that varies by **3.6×**:
**where you start**, which is to say the fixed cost of orientation in a new field.

Orientation is knowing what the field's real question is, which of its words mean
something different here, what a good question sounds like, which results are load-
bearing and which are decoration, and who to read. It takes months, it is almost
entirely search and social access, and **it is the part of expertise that has nothing
to do with intelligence.**

It is also the part an agent can collapse most completely — it is retrieval,
structuring, and diagnosis, none of which require the learner's own working memory.

> **What limits polymathy is not how many fields you can learn. It is how many times
> you can afford to be a beginner.** That price is what falls.

This is the strongest version of the claim in this section, and it is
`INFERENCE` — it follows from the measured parameters rather than from a trial of
anyone becoming a polymath. Nobody has run that study. It is eminently runnable.

---

## 8. The number, with its conditions

**10–40× on elapsed calendar. 3–5× on engaged effort.**

Rising above 40× — documented once at ~300× — when the baseline is *informal
experience* rather than a structured course, because informal experience has the
worst opportunity density of any learning arrangement.

Falling to **1×** for procedural and production domains, and **1×** for durability.

Three conditions, and all three are load-bearing:

1. **Accurate diagnosis of the starting point.** The 3.6× lever is prior knowledge,
   and it only pays if measured — see §22, where the measurement costs 15–40 seconds.
2. **The learner actually attempts.** Unguarded assistance leaves learners **17%
   worse** on later unassisted work. Compression achieved by watching someone else
   solve it is not compression; it is substitution.
3. **A short retention horizon, or a spaced schedule.** Compress acquisition, then be
   patient. Those are different resources and conflating them is where the claim
   becomes false.

---

## 9. What this section commits us to

- **Never quote a compression factor without saying which resource.** Calendar,
  engaged effort, and durability compress at wildly different rates, and a single
  number that does not name one is marketing.
- **Optimise opportunities, not minutes.** Time-based models of learning have
  systematically poor fit. Count attempts at the right difficulty.
- **Spend the compression budget on orientation and prerequisite repair**, which are
  worth 3.6×, not on speeding up the productive hour, which is already near its
  floor.
- **Claim 1× on procedural skill**, out loud, every time. The FSI hours are real and
  no model shortens them.
- **Ship the session decomposition study.** Nobody has measured where a study hour
  actually goes. It is the cheapest high-value experiment in this document.

The sentence to keep: **almost none of a week is spent learning, and that — not
processing speed, not talent, not effort — is what an agent takes back.**

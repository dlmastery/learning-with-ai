---
title: "Fifteen Hundred Papers, Seven Trials — what the field measures instead of learning"
section: field-state
status: draft
date: 2026-07-28
source_report: research/raw/E3-latest-sweep.md
---

# Fifteen Hundred Papers, Seven Trials

Earlier in this survey a small census turned up something odd: an exhaustive search
for papers on automatic slide generation returned 39 results, of which **zero
measured whether a human learned anything.** We flagged it as a local curiosity.

It is not local. We ran the census across the field.

---

## 1. The number

**2,907 arXiv papers across 20 education-AI subfields. At most 1.79% carry any
learning-outcome marker. Eight of the twenty subfields sit at exactly zero.**

The distribution is informative rather than uniform. Split the subfields by what
they build:

| Cluster | Papers carrying a learning-outcome marker |
|---|---|
| **Generation** — items, slides, figures, explanations, courseware | **≤ 1.08%** |
| **Interaction** — tutoring dialogue, feedback, scaffolding | **≤ 3.48%** |

And the finding that should sting: **the pre-LLM intelligent-tutoring-systems
literature measures learning *more* than the LLM literature does.** The field got
better at building and worse at checking, in the same decade.

The peer-reviewed education literature gives the same shape from the other
direction. ERIC holds **1,565 records** on ChatGPT in education. **Seven are
randomised controlled trials.** Four of those seven are second-language learning.

So: fifteen hundred papers, seven trials, and three of them outside language
teaching.

That is not a scandal and we are not going to write it as one. It is a **phase**
— an enormous generative capability arrived, and the field is still enumerating
what can be built. Enumeration is legitimate work. But it should be labelled as
enumeration, and a survey that reported "1,565 papers on AI tutoring" without the
denominator would be actively misleading.

---

## 2. A null published against interest

The most valuable single item in this sweep is a company publishing a result that
costs it something. Sal Khan, on the first Khanmigo:

> *"did not change student learning as much as many of us hoped it would."*

Khan Academy has more instrumented learner-hours than almost any organisation
alive, and it said the thing out loud. That deserves to be recorded as a
contribution, not a stumble.

The diagnosis is what makes it useful. The failure was **not pedagogical**. The
tutor's mechanism worked when it fired — and it only fired when a student
**recognised that they needed help and went to get it.** The metacognitive
prerequisite was the bottleneck. Knowing that you are confused, and acting on it,
is precisely the skill that struggling learners have least of.

The redesign puts the tutor **inside the practice problem**, where the student
already is, removing the need to self-diagnose before help can begin.

This is the most transferable design lesson in the sweep, and it generalises well
beyond one product:

> **Invocation is part of the intervention.** A tutor that must be summoned is a
> tutor that reaches the students who need it least. Measure the mechanism *and*
> the path to it.

---

## 3. Three results that fit together

A second null, from a controlled trial. Fütterer et al. (*Educational Psychology
Review*, April 2026, n = 371, Grades 7–9) found

> *"no statistically significant advantages of either intervention over the
> control condition… for effort, domain-specific knowledge, or elaboration-based
> strategy use."*

Read the control condition, because it is the whole finding: **the control was
plain ChatGPT.** Two carefully designed pedagogical interventions failed to beat
an unmodified general-purpose chatbot.

Now line it up with two results already in this survey:

| Study | Comparison | Result |
|---|---|---|
| Bastani | Guardrailed vs unguarded AI | Guardrails **removed harm** (−17% → −0.004 n.s.) |
| Fütterer | Pedagogical design vs **plain ChatGPT** | **No advantage** |
| Sierra Leone | Designed tutor vs **little instruction** | Benefit |

One reading fits all three, and it is not that pedagogical design is worthless:

> **The measured return on pedagogical design scales with how bad the counterfactual
> was.** Against an unguarded answer machine, design removes harm. Against a
> competent general-purpose chatbot in a well-resourced Western classroom, design
> has not yet demonstrated an advantage. Against scarce instruction, it produces
> benefit.

That is an uncomfortable finding for the premium-product end of the market and an
encouraging one for the reach argument: **returns are largest where instruction is
scarcest.** It also sets the bar for anyone claiming a pedagogical advance — the
control must be plain ChatGPT, not nothing.

---

## 4. Two audited numbers, and one that evaporated

Vendor copy is not evidence, but SEC filings are audited and carry liability.

**Chegg, Q1 2026 10-Q:** total revenue **−48% year over year**; Academic Services
**−57%.** The filing itself attributes this to AI Overviews and student adoption of
generative AI. That is a company stating under oath that the business of selling
homework answers is being dismantled.

**Synthesis School, SEC Form C-AR:** revenue **+6.5%**, losses roughly halved,
total assets **−53%**, 26 employees — filed alongside a **termination of
reporting**. Modest growth, shrinking balance sheet, and going dark.

And one number that dissolved on contact. MagicSchool's widely repeated **"28%
literacy improvement"** is **unattributable**: five candidate URLs return 404, and
the full 153-URL sitemap contains **no research page at all.** Not weak evidence —
*no locatable source*. It should not be cited by anyone, and the fact that it
circulates is a small case study in how a `VENDOR` claim becomes a "finding"
through repetition.

---

## 5. What is genuinely newly possible

The sweep's good news is concrete and it is about **sovereignty** rather than
capability.

**Gemma 4 is Apache-2.0 and ungated.** Weights can go to a school on a USB stick.
No API key, no account, no per-seat licence, no data leaving the building, no
vendor able to deprecate the model a district built its year around. For the
populations in §07 — the ones behind connectivity, language, and permission
barriers — that is a larger change than another point of benchmark accuracy.

And a genuinely maintained local stack now exists end to end: **Kolibri** for
offline content and progress, **llama.cpp / Ollama** for inference, **sherpa-onnx**
for speech. All actively maintained, all self-hostable.

---

## 6. The four gaps, stated as an invitation

Between that stack and a deployable school system there are four holes. We name
them precisely because each is a tractable open-source project rather than a
research problem.

1. **No open full-duplex voice.** Moshi's last release is 2024-09-22; Voxtral
   Realtime is turn-based ASR, not full duplex. Barge-in and overlap — the things
   that make speech feel like conversation — have no maintained open
   implementation.
2. **No safety layer.** Nothing in the open stack does age-appropriate filtering,
   crisis detection, or safeguarding escalation. Given that omission rather than
   harmful output is the dominant crisis failure mode, this is the gap with the
   sharpest consequences.
3. **No SSO.** Kolibri's OIDC plugins were **archived on 2026-07-11**. Without
   identity integration, nothing enters a school district.
4. **No glue between an LMS and a model.** Rosters, gradebooks, assignments,
   standards alignment — the unglamorous integration layer. **This is the highest-
   value unclaimed open project in the field**, and it needs no new research at
   all.

That last one deserves emphasis. Everything else in this survey is a question about
evidence. This is a question about somebody writing an adapter.

---

## 7. The regulatory correction, because it is days away

This sweep also caught a live error in our own §15, and the correction is
time-sensitive enough to repeat here.

The EU AI Act's **Annex III** education obligations were widely expected to apply
from 2 August 2026. **They were deferred to 2 December 2027** by Regulation (EU)
2026/1744 — the Digital Omnibus on AI, in force **27 July 2026**, verified against
the EUR-Lex primary text.

But Article 113's first paragraph is unamended and Chapter IV is not carved out.
**Article 50 — transparency, chatbot disclosure, synthetic-content marking — still
applies from 2 August 2026.** For a conversational tutor, that is the live deadline.

Two sources a careful person would check both return the wrong answer today:
`artificialintelligenceact.eu` is stamped *"last updated 1 August 2024"*, and the
Commission's own Digital Omnibus page still describes only the proposal. A claim
verified against a secondary source last week is wrong this week.

---

## 8. What this section commits us to

- **Publish the denominator.** "1,565 papers" without "7 RCTs" is a misleading
  sentence, and we will not write it.
- **Treat invocation as part of the intervention.** A tutor that must be summoned
  reaches the learners who need it least. Instrument the path to help, not just the
  help.
- **The control is plain ChatGPT.** Any claim of pedagogical advantage is measured
  against a competent general-purpose chatbot, never against nothing.
- **Expect the return to scale inversely with the counterfactual.** Design a system
  for where instruction is scarce and be honest that the same system may show no
  advantage in a well-resourced classroom.
- **Never cite an unlocatable number.** If five URLs 404 and the sitemap has no
  research page, the number does not exist, however often it is repeated.
- **Re-verify regulatory dates against primary text**, every time, because the
  aggregators are eighteen months stale and the deadline moved four days ago.

The field is not failing. It is early, and it is measuring the wrong thing while it
gets its bearings. The correction is cheap and entirely within reach: **run the
delayed unassisted test, against a real control, and publish the denominator.**

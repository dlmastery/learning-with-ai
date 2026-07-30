---
title: "Inference Is 0.43% of Delivery — and human judgement is the scarce input"
section: market
status: draft
date: 2026-07-29
source_report: research/raw/M1-market-and-model.md
---

# Inference Is 0.43% of Delivery

A survey that specifies a system and never asks who pays for it has described a
prototype. This section is the audit of the commercial half. It is included because
three of its findings **contradict things stated earlier in this document**, which is
the strongest argument for having done it.

Every figure here was traced to a primary source. Where a number could not be traced,
it is reported as untraceable instead of cited, and that happened more often than any
other section in this survey.

---

## 1. The number that retires a whole category of argument

> **Inference is 0.43% of the delivered cost of a human-supervised tutoring session.**

Two independent measurements converge on it. A published cost model puts tokens at
£0.0037 of a £0.861 session. A deployed programme's measured API bill was
$1,419.66 for 429 tutors over two months, or $19.86 per tutor per year, against a
tutor working 200 hours at the US mean tutor wage of $23.10/hour. Same figure, from
two directions.

This survey has argued from the first section that cost is not the interesting
constraint. That framing was right for the wrong reason. We treated inference cost as
*falling toward irrelevance*. It is already irrelevant — not because it fell, but
because **it was never the denominator.** If inference went to zero tomorrow, a
human-in-the-loop gross margin would improve by less than half a point.

The consequence is sharp and it disqualifies a common pitch: *"our costs fall as
models get cheaper"* is true, and worth 0.43%. The entire margin question is the
**leverage ratio**: learner-hours supervised per paid tutor-hour.

---

## 2. The leverage has not been measured, including by us

This is a correction to our own §10, where the Eedi trial's draft-acceptance figure
was cited in a way that implied a demonstrated efficiency gain.

**The acceptance rate verifies exactly**: 2,691 of 3,617 drafts accepted unedited, or
74.4%, with zero harmful messages and five factual errors. That number is solid, and
the moat argument in this survey rests on it.

The efficiency reading is not solid. The authors state that their design

> *"precludes a rigorous measurement of throughput or efficiency."*

The published throughput gain (concurrency 2.3 → 3.5, netting −13.6% cost per
session) comes from a six-tutor role-play simulation in an appendix, and the
labour rate underpinning the saving is cited to **a tutoring marketplace's blog
post**.

So: 74.4% is a measured *signal stream*, which is all the argument needs. It is not a
measured productivity gain, and this document should not have implied otherwise.

---

## 3. The only audited comparable went the wrong way

A listed tutoring company rebuilt, in its own filing's words, *"on entirely new,
AI-native codebases."* In that fiscal year:

| | |
|---|---|
| Gross margin | **67.5% → 58.0%** (62.3% excluding a write-off) |
| Expert costs | **up $5.2M** |
| Revenue | **down $11.2M** |

The following quarter recovered to 66.2%, on price rises and expert incentives and
not on AI. The 10-K states plainly:

> *"There can be no assurance that our investments in AI will be beneficial to our
> business."*

That is the single audited data point on an AI-native rebuild of exactly this business
model, and it is negative. It does not falsify the thesis. It does mean **leverage
must be demonstrated rather than assumed**, and that a company claiming it should be
asked to produce the ratio monthly.

---

## 4. Two market facts that relocate the opportunity

The funding wave never arrived where everyone models it. Summed from the education
department's own state-level obligation data, the reported *tutoring* line of the
pandemic relief appropriation is **$994.7 million, or 0.52% of $189.5 billion**. The
category most often cited as the demand driver received half a percent of it.

And the numbers in circulation mostly have no source. Six of six analyst houses
fail traceability on the tutoring market size: two dead links, one report not shown
to exist, one figure internally inconsistent by three orders of magnitude. For scale
on how far the reported totals drift: **Korea alone (₩27.5 trillion, and falling) is
roughly 20% of the claimed global market.**

The most striking absence: **the United States has not measured per-pupil
special-education spending since 1999–2000.** No federal survey currently produces it.
A document that argued in §22 for designing at the margin first should say plainly
that the sector it points at is the least financially measured in education.

---

## 5. China is a policy risk and not a market

Retrieved in full from the Ministry of Education: the July 2021 *double reduction*
order states that no new approvals will be issued for core-subject tutoring
institutions and that existing ones re-register as non-profits. One listed
operator's revenue fell 62% in twelve months, per its filing.

And the compounding finding: **no official Chinese statistic on tutoring market size
exists, before or after 2021.** Every "$100bn+ market" figure descends from vendor
reports rather than a national statistics office, which means **the destroyed value
is itself unmeasurable.** That should be sobering about the downside of this category
and not only its upside.

---

## 6. The three questions, and the answers that disqualify

The section's deliverable. These are aimed at any AI-tutoring company, including one
built from this document.

**1 · "Show me learner-hours delivered ÷ paid tutor-hours, monthly, for 24 months."**
*Disqualifying:* the company cannot produce it, or it is flat while headcount grows.
That means the AI is decorative and the buyer is underwriting a staffing business at a
software multiple.

**2 · "What is your delayed, unannounced, novel-item transfer result, with n, and who
held the item bank?"**
*Disqualifying:* the only outcome evidence is in-product mastery or engagement. One
deployment moved its exit ticket +4pp and was null on the state test. That
dissociation between the proxy and the outcome is the most reproducible finding
in this literature.

**3 · "Have you ever run an arm against plain ChatGPT?"**
*Disqualifying:* never tried, or tried and buried it. A controlled trial (n = 371)
found scaffolded generative AI no better than plain ChatGPT on domain knowledge.
If the pedagogy has never beaten the free substitute customers already have, the moat
is a prompt.

---

## 7. What a buyer should be able to check

- **Never argue from falling inference cost.** It is 0.43% of delivery. The claim is
  worth less than a rounding error and signals that the speaker has not done the
  arithmetic.
- **Report the leverage ratio monthly, from month one**, because it is the only number
  that distinguishes a software business from a staffing business here.
- **Cite the audited counter-comparable** whenever claiming AI improves tutoring
  margins. Omitting the one negative data point because it is inconvenient is the
  failure this survey exists to name.
- **Treat 74.4% as a signal stream, never as productivity.** The authors said so
  themselves.
- **Do not quote a market size without its primary source.** Six of six fail. If the
  figure cannot be traced to a statistics office or a filing, say it is untraceable.
- **State that special-education spend has been unmeasured since 1999–2000** wherever
  this document argues for building at the margin. The moral case is strong; the
  financial case is undocumented, and conflating them would be dishonest.

Our own framing changed here. The cost of intelligence was never the constraint on
this business, and it is not becoming one. What is scarce is the human judgement that
currently has to verify it — a conclusion §14 reached from the technical side, arrived
at independently from a profit-and-loss account.

---
title: "Motivation — wanting to continue"
section: motivation
status: draft
date: 2026-07-28
source_report: research/raw/F6-motivation-persistence.md
---

# Motivation

Here is the cheapest useful test in this survey. Take any metric you are thinking of
putting in an objective function. Now simulate an agent that maximises it **while
learning nothing** — the cheapest possible action sequence that satisfies the
measurement. If it scores well, the metric is invalid as a learning objective.

Call it the **Null-Learner Test**. Run it:

| Metric | Null learner | Verdict |
|---|---|---|
| Daily active users | Opens the app, taps the easiest lesson | **Maxes it. Invalid** |
| Streak length | Same, once a day | **Maxes it. Invalid** |
| XP | Farms the cheapest points-per-minute activity | **Maxes it. Invalid** |
| Time on app | Leaves it open | **Maxes it. Invalid** (and time-on-task estimation is independently fragile enough to invalidate learning-analytics findings built on it) |
| Session count, notification-response rate, thumbs-up rate | Trivially | **Invalid** |
| **Delayed, unannounced, novel-item transfer assessment** | Cannot be maxed without learning | **Valid** |

Every metric the industry ships fails. That is the whole argument in one table, and
this section carries the test throughout, because motivation is the topic where
otherwise-careful people start reasoning in engagement units without noticing.

---

## 1. What AI genuinely changes, and it is large

Self-determination theory posits three needs whose satisfaction produces autonomous
motivation: **autonomy, competence, relatedness.** Two of them were previously
rationed by teacher time, and are now not.

**Autonomy — AI is structurally the best autonomy-support technology ever built.**
Choice enhances intrinsic motivation, effort, task performance and perceived
competence across 41 studies. A generative system can offer choice over topic,
sequence, pace, difficulty, representation, example domain, and *what the learner is
learning it for*. No prior educational technology could offer real choice over the
**content of the explanation** — only over the order of fixed assets. This is also the
need conventional schooling most systematically violates.

> *Guardrail, in the same breath:* autonomy in SDT is not "many options"; it is
> volition and self-endorsement of one's own action. A system that generates 40 paths,
> selects which 3 to display, and orders them by predicted engagement is supplying
> **choice architecture masquerading as volition.**

Competence — AI can supply it, conditional on being willing to say no. Competence
support is optimal challenge plus immediate informative feedback plus visible progress
against a real standard. Every one of those is continuous and cheap for an LLM tutor
and impossible for a human at any realistic ratio. The strongest direct evidence is
Kestin et al.'s randomised physics trial, where students using a pedagogically designed
AI tutor learned more in less time and reported feeling more engaged and more motivated.

> *Guardrail:* that was a single lesson. It measures acute motivation, not persistence
> over months. And competence support requires **honest negative feedback**. A model
> tuned on user satisfaction that tells a learner their wrong derivation is "a great
> start!" has not supplied competence support — it has supplied its counterfeit.
> **Sycophancy is the AI-specific mechanism by which competence support silently
> inverts.**

Relatedness — no, for the load-bearing part. Section 6 below.

Two of three, at zero marginal cost, both previously rationed. That is a real and large
change, and it is what this section leads with. The sharpest available failure mode is
that a system will *appear* to supply the third and thereby displace the humans who
could.

---

## 2. Availability was never the binding constraint

Free, world-class, unlimited instructional content has existed at global scale for
fourteen years.

| Study | Sample | Completion |
|---|---|---|
| Jordan 2014 | 91 courses | avg. 43,000 enrolled, **6.5% complete** |
| Jordan 2015 | 221 MOOCs, 129 with completion data | **median 12.6%**, range 0.7%–52.1% |
| Henderikx et al. 2017 | 2 MOOCs, completion-based | **6.5% and 5.6%** |

And the load-bearing finding, from six years of HarvardX/MITx edX data: *"the vast
majority of MOOC learners never return after their first year"*; growth concentrated
almost entirely in the world's most affluent countries; and *"the bane of MOOCs —
low completion rates — has not improved over 6 years."*

Read the third against what the field shipped between 2012 and 2018: better video,
better platforms, mobile apps, adaptive sequencing, mastery gating, cohorts, gamified
progress, social forums, certificates, paid verification. Completion did not move.
And the second destroys the access narrative: the marginal MOOC user was not an
underserved learner in a low-income country. It was an already-credentialed
professional in a rich one.

The honest rebuttal, stated because it is measured rather than rhetorical.
Completion is arguably the wrong denominator, because most enrollees never intended to
complete. Henderikx et al. ran the same two MOOCs under both definitions:
completion-based success **6.5% and 5.6%**; intention-adjusted success — did the
learner achieve *their own* stated goal — **59% and 70%**. A tenfold swing from a
definitional choice. Kizilcec's four-trajectory taxonomy (completing, auditing,
disengaging, sampling) made this tractable by treating the clusters as different
products being consumed rather than degrees of failure. *And the replication note that
belongs with it:* an attempt to reproduce that structure on a different,
social-constructivist platform failed to fully replicate, with only samplers and
completers stable across platforms. Engagement patterns are shaped by pedagogy, not
intrinsic to learners.

Where the rebuttal fails. It rescues MOOCs from the charge of failure but not from
irrelevance to the persistence problem. Reframing sampling as success does not produce
one additional person who learned a hard thing they could not previously do. And
platform-level non-return across a *year* is not a definitional artefact.

> **Content supply was solved, and solving it moved almost nothing.** Any proposal whose
> theory of change is "better, more personalised content" is pushing harder on the one
> lever already pushed to exhaustion.

---

## 3. The nulls, given their own space

Behavioural interventions to raise persistence do not survive scaling. This is the most
under-cited literature in edtech.

| Study | Scale | Result |
|---|---|---|
| Bird, Castleman, Denning et al. 2021 | Two RCTs, **>800,000 students** | *"We find no impacts on aid receipt or college enrollment overall or for any subgroups. We find no evidence that different approaches to message framing, delivery, or timing, or access to one-on-one advising affected campaign efficacy."* |
| Kizilcec, Reich, Yeomans et al. 2020, *PNAS* | ~250,000 students, **247 courses**, 2.5 years, preregistered | Hypothesised medium-to-large effects **not supported**. Self-regulation interventions raised engagement in the first few weeks but **not final completion**. *"Scaling behavioral science interventions across various online learning contexts can reduce their average effectiveness by an order-of-magnitude."* State-of-the-art ML could not forecast where an achievement gap would occur |
| Oreopoulos & Petronijevic 2023 | Five years, ~20,000 students, three campuses | *"Some improvement on study time but no effect on academic outcomes."* Treated students correctly updated their beliefs about required effort and wanted better grades more — and it still did not translate |
| Kizilcec, Pérez-Sanagustín & Maldonado 2016 | MOOC RCT | Recommending self-regulated learning strategies **did not improve performance** |

Against that, one robust positive, from a single study that also contains two of its own
nulls:

| Tool | Effect |
|---|---|
| **Commitment device** — learner pre-commits to a time budget | **+24% time on course, +0.29 SD grades, +40% more likely to complete** |
| Alert tool | statistically indistinguishable from control |
| Distraction-blocking tool | statistically indistinguishable from control |

**Being told things does nothing. Being reminded does nothing. Being blocked does
nothing. Binding your own future self does a lot.**

The structural reason is the organising idea of this section. A commitment device is the
only intervention in that list that transfers volition to the learner instead of
spending it. Every other one is the system acting *on* the learner. Hold that distinction
— it predicts, retroactively, almost every result below.

---

## 4. Gamification, reported honestly

Two independent meta-analyses converge on a real, medium effect, and this survey says so.

| Meta-analysis | Effect |
|---|---|
| Sailer & Homner 2020 | **Cognitive g = .49** [.30, .69]; **motivational g = .36** [.18, .54]; **behavioural g = .25** [.04, .46] |
| Bai, Hew & Huang 2020 (30 interventions, N = 3,202) | **Hedges' g = 0.504** [0.284, 0.723] (§24)|

So the headline is *not* "gamification doesn't work." Four caveats the marketing omits.

The cell vendors sell is the weakest one. The cognitive effect "was stable in a
subsplit analysis of studies employing high methodological rigor," whereas "effects on
motivational and behavioral outcomes were less stable." The claim actually made —
*it makes people keep coming back* — rests on g = .25 with a lower CI bound of .04.

The moderators point away from points, badges and leaderboards. The significant
moderators were game fiction and social interaction, with "combining competition
with collaboration" particularly effective. Nothing supports the PBL triad as the active
ingredient.

Novelty decay is measured, not folklore. Perceived benefits decline with how long
users have been using the service. And the best longitudinal test deliberately built
*need-supporting*, SDT-designed elements and measured motivation four times over 15
weeks: autonomous motivation was curvilinear — an initial downward trend that only
later recovered. Even theory-driven gamification produced a medium-run motivational
dip.

And the undermining effect is the mechanism. Across 128 experiments, tangible,
expected, performance-contingent rewards significantly undermine intrinsic motivation for
interesting tasks, measured by free-choice persistence; verbal and informational feedback
does not. *Contested at the time and reported as contested*, with the contest resolved
mostly in SDT's favour for the interesting-task case. A useful refinement from a
forty-year meta-analysis: incentives predict the quantity of performance; intrinsic
motivation predicts the quality.

> Gamification's genuine cognitive effect most likely arrives via the mundane mechanisms
> it smuggles in — increased practice frequency, immediate feedback, clearer goals. Its
> *motivational* claim is the weakest cell in the evidence, decays with exposure, and the
> reward class deployed most heavily is precisely the class identified as corrosive.
> **Points, badges and leaderboards buy short-run behaviour by spending long-run
> interest.**

---

## 5. The best case study, read carefully

Duolingo is the correct case study because it is the only consumer learning product to
have solved retention at scale — and the cleanest demonstration that solving retention is
not the same as solving learning.

Its own engineers published the mechanism: millions of daily reminders optimised with a
custom bandit algorithm explicitly designed to handle novelty effects. The reported
result: **"a 0.5% increase in total daily active users and a 2% increase in new user
retention over a strong baseline."**

Read the objective function. The target is DAU and new-user retention. Not
vocabulary retained, not level attained, not time-to-proficiency. It is a competent,
well-executed piece of engineering whose loss function contains **no learning term at
all** — published honestly, and it is the industry-standard objective.

The streak claims are vendor claims, labelled as such and never restated as findings.
"Learners who reach a streak of just 7 days are 3.6 times more likely to complete their
course" is selection, not causation. New streak animations raised seven-day return by
+1.7%. Two simultaneous streak freezes raised relative DAU by +0.38%. And the thing that
is absent: **the published mechanism reports no data comparing learning outcomes between
streak-holders and non-holders.** Every number is in engagement units.

The mechanism is well-understood and not learning-specific. A streak counter is a pure
endowed-progress device, and endowed progress is measured to drive retention in
reward programmes; past a certain length the streak is maintained to avoid losing it, not
to gain anything. Habit automaticity in the real world took a **median 66 days, range
18–254** — a genuine reason to want daily return in the first two months and no reason at
all to want it in year three.

And streaks get metagamed, documented. Adolescents maintaining structurally identical
Snapchat streaks develop strategies to uphold the counter while hollowing out the
underlying activity: content becomes minimal, meaningless, purely instrumental to the
number. **A streak counter measures counter-preservation, and any user under time
pressure will find the cheapest lesson that preserves it** — the precise inverse of
desirable difficulty. Run the Null-Learner Test on it: it maxes it.

On outcomes, the independent evidence is thin: a semester-long study with nine
participants; company-affiliated studies of learners who *completed* beginner courses
reaching roughly **CEFR A2**; and a flagship favourable efficacy study that is
**vendor-commissioned and could not be retrieved through any bibliographic API used in
this project** — reported as unverifiable rather than omitted. A systematic review of 35
Duolingo studies concluded the field's *"focus on app design marks an emphasis on the
creation of tools rather than the process and outcomes of language learning."*

> Duolingo is a genuine, under-appreciated achievement: it made hundreds of millions of
> people return to a learning activity daily, which nobody else has done. It did not prove
> that engagement mechanics teach. **It proved that engagement mechanics engage.**

---

## 6. Relatedness, and why the AI must broker rather than substitute

The human baseline is strong: 99 studies, ~88,000 students, affective teacher–student
relationships significantly associated with engagement and achievement — with effects on
engagement larger than on achievement, meaning the human relationship is primarily a
*persistence* technology.

The AI-companion evidence is real and should not be dismissed. Five studies find AI
companions do reduce loneliness, "on par only with interacting with another person,"
mediated by whether the chatbot makes users feel heard. A survey of 1,006 student
Replika users found them lonelier than typical student populations yet perceiving high
social support, with **3% reporting the agent halted their suicidal ideation** — *work
contested in the same journal* on the grounds that important context was omitted, and
reported here as contested. And an OpenAI × MIT Media Lab study — 3M+ conversations,
4,000+ surveyed, plus an IRB-approved RCT with ~1,000 participants over 28 days — found
that *"very high usage correlates with increased self-reported indicators of dependence."*

The argument that resolves this for learning specifically:

> Relatedness in SDT is not the *feeling* of being cared about. It is the state of
> **mattering to an agent whose regard was contingent and could have been withheld.** An
> LLM's positive regard is unconditional by construction and costless by construction. It
> can produce the affective signature of relatedness — "feel heard" is exactly that
> signature — without the property that makes relatedness motivating for effortful,
> unpleasant, long-horizon work: **that someone would notice and mind if you stopped.**

Loneliness relief is a state. Academic persistence is a commitment. **A companion that
never notices your absence cannot underwrite a commitment.**

So the design consequence is that the AI's role in this dimension is **matchmaker and
scheduler, not friend**: pair cohorts, surface a real person who will notice a missed
week, make the learner's progress legible to someone who cares.

One more negative result belongs here, and it indicts the single most-deployed social
mechanic. Exposure to exemplary peer performance undermined motivation and success,
causing people to perceive high performance as unattainable and to **de-identify with the
domain** — demonstrated in a MOOC context. *Contested, with a clear moderator:* a separate
trial found social-comparison framing can raise completion when the comparison target is
attainable. Reading both together gives the design rule: **social comparison helps against
a near peer and harms against a distant exemplar** — and a global leaderboard is, for
almost every user, a distant-exemplar display.

**Never show a learner the top of a distribution. Show them someone half a step ahead, or
nobody.**

---

## 7. The hinge: flow feels good, learning feels bad

This is the result that should govern every training decision in an AI learning system.

Randomised, identical content, same instructors, introductory college physics: students in
active classrooms learned more but felt they learned less — and the paper shows the
negative correlation is caused in part by the increased cognitive effort active learning
requires. The general statement is the desirable-difficulties framework: conditions that
impair performance during acquisition frequently *enhance* long-term retention and
transfer.

> **Learner-reported satisfaction, perceived learning, enjoyment and session pleasantness
> are, under experimental control, negatively correlated with actual learning.**

Any system that optimises for what learners report liking — or for behavioural proxies of
liking, such as session length, return rate, or rating — will be systematically pushed
away from the methods that work. This is not a risk. It is a demonstrated experimental
result, and it applies with full force to any model tuned on learner preference.

Hence the quarantine: **preference data may be used for tone and safety. Never for
pedagogy.**

A footnote on flow, the most-cited motivational idea in edtech and the least useful as
stated: its meta-analytic association with performance is correlational, and flow may be a
consequence of competence rather than a cause of learning. Exactly two of its conditions
are engineerable — challenge calibrated to current skill, and immediate feedback — and both
are already justified by competence support. Implement those and stop talking about flow.

---

## 8. What actually moves phase 3

Hidi and Renninger's four-phase interest model is the most design-relevant framework here
because it is developmental: triggered situational interest, maintained situational
interest, emerging individual interest, well-developed individual interest.

The critical structural fact: gamification, notifications and streaks operate **entirely in
phases 1–2** and are constitutionally incapable of producing phases 3–4, because phases 3–4
are *defined* by voluntary re-engagement in the absence of external triggers.

> **A system whose retention comes from notifications has, by construction, not moved a
> single learner past phase 2. An AI that maximises engagement is trying to make phase-2
> interest do phase-3 work — and the attempt consumes the intrinsic motivation phase 3
> requires.**

Two interventions have real causal evidence for the 2→3 transition, and both are
AI-native.

Utility-value writing. High-school science students asked to write about the relevance
of the material to their own lives showed increased interest and grades, **concentrated in
students with low initial success expectations; a college biology replication closed
achievement gaps** for first-generation and underrepresented-minority students. *Caveat
required by §3:* the 247-course scale-up found value-relevance effects only in courses that
*had* a global achievement gap — real and conditional, not universal. It is also a
generative task, which is exactly what an LLM can elicit, read and respond to at scale
and a multiple-choice platform cannot.

Manufactured curiosity. Curiosity arises from awareness of a *gap* and is maximised at
intermediate knowledge levels — you must know enough to know what you don't know. Curiosity
states enhance hippocampus-dependent encoding, including of incidental material. And
the actionable result: requiring learners to **generate a prediction before seeing an
answer** raised both curiosity ratings and learning, relative to generating an example.

Predict-before-reveal costs one extra turn, requires no rewards, and is **intrinsically
incompatible with an engagement objective, because it adds friction.** That incompatibility
is a feature. It is how you tell the two kinds of system apart.

---

## 9. The objective function

> **RTC/h = D(t+30d) · T / H**
>
> **Retained Transferable Capability per Learner-Hour.**

**D(t+30d)** is the score on a delayed (≥30 days), unannounced, novel-item
assessment — items never seen, generated post hoc, not drawn from practised sets. Delay and
novelty are what make it un-gameable; announcement would reintroduce cramming. T is the
transfer coefficient: the proportion earned on items requiring application in an unpractised
context rather than recognition. H is total learner hours invested, *including time
outside the system*.

The denominator is the entire design. Putting learner time in the denominator inverts
the commercial incentive: the system now profits by making learning *faster*, and every
minute of retained attention it does not convert into durable capability costs it score.
An engagement-optimising system and an RTC/h-optimising system diverge on the first design
decision they make.

Guardrail metrics, all non-decreasing, any decrease blocking release:

| Metric | Definition |
|---|---|
| **Unprompted Return Rate** | Fraction of sessions initiated with **no notification, email or reminder in the preceding 24h**. The closest measurable proxy for phase 3 |
| **Autonomous Motivation Index** | Periodic short SDT-validated autonomous-versus-controlled measure |
| **Goal Attainment & Graduation Rate** | Fraction of learners who reach their **own declared** goal — and then leave. A learning system should have a **positive churn target** |
| **Off-Platform Application Rate** | Evidence the capability was used somewhere that is not the product. The only measure definitionally external to the engagement loop |
| **Human-Connection Rate** | Fraction of learners connected to at least one real person who would notice their absence |

And the list that is reported but never optimised, monitored as harm indicators with
alarm thresholds: DAU/MAU, session length, streak length, notification-response rate, XP,
leaderboard engagement, satisfaction ratings. **A sustained rise in any of these without a
corresponding rise in RTC/h is a defect report, not a success.**

Four governance rules. Run the Null-Learner Test on any metric before it enters any
objective; failure excludes it. Unprompted Return Rate is the tie-breaker when RTC/h and
an engagement measure conflict, because a system that only works while pushing has not
taught anyone to want anything. Preference data is quarantined to tone and safety.
Graduation is a success event, not churn — a learner leaving because they got what they
came for is the product working, and any metric that penalises this is disqualified.

*Honest limitations, stated rather than hidden.* RTC/h is expensive in learner goodwill:
delayed unannounced assessment is a burden no consumer product can bear at full population
scale. It is realistically measurable on a sampled, compensated panel with cheap online
proxies calibrated against it — which is how ad-supported media measures reach, so the
tooling pattern exists. And RTC/h says nothing about *who never enrolled*; it optimises the
experience of people already inside the funnel.

---

## 10. The strongest counter-argument

*A learner who quits learns nothing. Engagement is not the enemy of learning; it is the
precondition for it. You have forbidden every tool anyone has for keeping people around, on
the strength of a distinction between "phase 2" and "phase 3" that no product manager can
operationalise.*

The first sentence is true and the conclusion does not follow.

The tools do not work at scale. 800,000 students, null. 250,000 students across 247
courses, order-of-magnitude effect decay. 20,000 students over five years, null on
outcomes. Alert tools and distraction blockers, null. That is not a philosophical objection
to reminders; it is the measured record of reminders.

**And phase 3 is operationalisable.** Unprompted Return Rate — sessions started with no
notification in the previous 24 hours — is computable today from data every system already
has. It is the free-choice-persistence paradigm, operationalised at scale. A system that
raises DAU while flattening URR has learned to push rather than to teach.

What survives the objection is a genuine constraint on ambition: **a bounded habit scaffold
is defensible.** Habit automaticity takes a median 66 days. An eight-to-ten-week scaffold
with a declared end date is a reasonable thing to build. An unbounded, escalating,
loss-framed counter with a purchasable freeze economy is not the same object, and calling
both "streaks" is how the first becomes the second.

---

## 11. What this section commits us to

- **Run the Null-Learner Test on every metric before it enters any objective.** DAU,
  streak, XP, time-on-app and satisfaction all fail it.
- **RTC/h is the objective, with learner time in the denominator.** Delayed, unannounced,
  novel-item, transfer-weighted, measured on a compensated sampled panel.
- **Preference data is quarantined to tone and safety.** Under experimental control,
  liking is negatively correlated with learning.
- **Transfer volition to the learner; never exercise it over them.** Commitment devices
  (+40% completion, +0.29 SD), utility-value writing, predict-before-reveal. Not reminders,
  not rewards, not rankings.
- **Broker human relatedness; never simulate it.** No friend role, no "I missed you," no
  anthropomorphic bid for continued interaction. Human-Connection Rate is a release gate.
- **Never show the top of a distribution.** Near peer or nobody.
- **Habit scaffolds are bounded and declare their end date.** ~66 days is the evidence;
  year three is not.
- **Graduation is a success event.** Positive churn target, and any metric that penalises a
  learner leaving satisfied is disqualified.

The through-line: every intervention that works hands the learner power over their own
future self — commit yourself, find your own reason, predict before you are told, be
accountable to a person you chose. Every intervention that fails or backfires exercises
power over the learner — remind them, reward them, rank them, retain them.

**The question a learning system must answer is not whether the learner came back. It is
whether they came back with nobody asking.**

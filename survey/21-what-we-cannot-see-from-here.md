---
title: "What We Cannot See From Here — the unknown unknowns, and the questions that expose them"
section: epistemics
status: draft
date: 2026-07-28
source_report: synthesis across the corpus
---

# What We Cannot See From Here

Every section before this one reports what has been measured. This one is about the
shape of the space where nothing has been measured — not the gaps we have
catalogued and specified experiments for, but the ones we suspect are there because
of how the field is built.

A known unknown gets a study design. An unknown unknown gets a question you did not
think to ask. What follows is our best attempt at the second category, offered in
the knowledge that any list of things you have not thought of is, by construction,
incomplete.

---

## 1. Correlated pedagogical error

Thirty teachers make thirty different mistakes.

That throwaway observation about human variability is a **structural
safety property** of every education system that has ever existed. A teacher who
misexplains limits, or who has an idiosyncratic blind spot about the passive voice,
damages thirty children a year. The next teacher has a different blind spot. Across
a school, a district, a generation, the errors are uncorrelated and the system
averages them out. Nobody designed that redundancy. It is a free consequence of
teaching being done by many separate minds.

A model's errors are not like that. They are **systematic, reproducible, and
identical for every learner simultaneously.** If a widely deployed model holds a
subtly wrong account of natural selection, or a plausible-but-broken intuition for
conditional probability, then every child using it receives the same defect on the
same afternoon, and the defect is invisible because it is universal.
There is no dissenting teacher down the corridor.

Nobody has studied this in education, and there is no monitoring for it and no
benchmark that would detect it. But an earlier draft of this section claimed it has
*no name in the literature*, and that was wrong. The correction strengthens the
argument instead of weakening it.

It has a formal result, in another field. Kleinberg and Raghavan's *algorithmic
monoculture* (PNAS 2021) proves that convergence on a single algorithm can **reduce
collective decision quality even when that algorithm is more accurate for each agent
in isolation**, and with no exogenous shock required. The harm is a consequence of
correlation itself, not of the model being bad.

That is our risk, stated as a theorem, five years before anyone applied it here. And
there is now a measured hint of the mechanism: **71% of one model's
misconception-detection failures concentrate in two question types**, reported
incidentally by researchers studying something else entirely. Model pedagogical blind
spots are not diffuse. They are structurally concentrated, which is exactly the
condition under which monoculture bites hardest.

We keep the name *correlated pedagogical error* for the education-specific case, and
withdraw the claim of novelty.

It is invisible for one specific reason. Every evaluation we have
compares a model against a *reference answer*. Correlated error is the case where
the model and the reference are wrong together, or where the error lives in the
*explanation* rather than the answer. A model can be 100% accurate on the benchmark
and systematically misteach the mechanism behind it.

What would detect it: an ensemble of genuinely independent models and human
experts, explaining the same concept, with disagreement treated as the signal when
it falls in the *explanation* and not the answer. That is a monitoring system nobody is building
because nobody has named the failure.

---

## 2. Every effect in this document is measured in weeks

The longest outcome interval in this corpus is months. Most are a single session.
The Sierra Leone trial, the largest deployment we examine, ran **eight weeks**. An
earlier version of this sentence said "a school year", which was wrong and made the
field's time horizon look better than it is (§09). Almost nothing comes close even to eight
weeks.

Now consider a technique that measures **+0.5 SD at six weeks** and, over three
years, gradually teaches a learner that difficulty is a signal to ask rather than a
signal to persist. Every study in this survey would score it a success. **The
instrument cannot see the failure**, because the failure operates on a timescale an
order of magnitude longer than the measurement.

This is not hypothetical hand-wringing. It is the exact shape of the one long-horizon
result we do have: unguarded AI produced **+48% during access and −17% once
withdrawn.** The sign flipped when the window widened (§01). We got that only because
someone thought to measure after taking the tool away — and almost nobody does.

We are optimising on a horizon far shorter than the thing we claim to affect, and
we have one data point showing that the horizon is where the sign lives.

---

## 3. The curriculum nobody wrote

Every interaction teaches something other than its subject.

When a tutor answers immediately, it teaches that answers arrive immediately. When
it is confident about a contested question, it teaches that contested questions have
confident answers. When it never says *I don't know*, it teaches that not knowing is
not a state a competent agent occupies. When it accepts a sloppy question and
produces a clean answer, it teaches that precision in asking is optional.

This is epistemic curriculum, it runs on every single turn, and it is measured
nowhere. No benchmark scores it. No rubric in the corpus contains a line for it.

We think it is plausibly larger than the subject-matter effect, for a simple reason:
subject matter is encountered in units of a topic, and epistemics is encountered in
units of a *turn*. A child might meet photosynthesis five times and meet "how a
confident answer sounds" ten thousand times.

We do not know its magnitude or its sign. The uncomfortable part is that nobody is
looking, and that a field measuring post-test scores would not notice either way.

---

## 4. The learner model may be a category error

Every architecture in this survey, including ours, assumes there is a stable person
to be modelled — an entity with properties that persist long enough to be estimated,
stored, and acted on.

For a doctoral student, defensible. For a nine-year-old, much less obvious. In
childhood the subject changes faster than the model converges, and a model that has
finally learned who a child was in October is describing someone who no longer
exists by March.

Worse than merely stale: potentially constraining. A system that has confidently
concluded a child struggles with multi-step reasoning will route around multi-step
reasoning, and the routing is invisible to the child, the parent, and the model. The
prediction becomes a wall. We know this failure mode intimately from human education.
It is called tracking, its harms are well documented, and we are proposing to
automate the inference that produces it.

Nobody has asked whether personalisation is developmentally *anti*-adaptive. It is
not a question the field's instruments are shaped to ask, because measuring it
requires following the same child for years while withholding the personalisation
from a matched group.

The design response, which we adopt without waiting for the answer: the learner
model is inspectable and correctable by the learner and the parent, it decays by
default, and any inference that would *restrict* what is offered requires stronger
evidence than one that expands it.

---

## 5. Everything was measured where nobody else had it

Education is heavily positional. Credentials, ranking, admission, hiring — a great
deal of what education *buys* is relative, and relative goods do not scale the way
absolute ones do.

Every effect size in this document was measured in a world where the treatment group
had something the control group did not. What the same technique does when
everyone has it is not a smaller version of that result. It is a different
question, and it has never been asked.

Two mechanisms make it different and not merely attenuated. If a tutor lifts
everyone by 0.4 SD, the *absolute* learning is real and the *positional* benefit is
zero — which matters if the learner's actual goal was admission. And if assessment
adapts to a higher mean, the bar moves, and the measured gain evaporates while the
knowledge remains.

We are not equipped to resolve this and neither is anyone else. It is named here
because a survey that quotes effect sizes without stating this condition is quietly
extrapolating from a scarcity regime into an abundance one.

---

## 6. Competence and performance have come apart

Every assessment instrument in existence rests on one assumption: **the artifact
reflects the person who submitted it.**

That assumption broke, comprehensively, and the field's response has been detection
— which runs **61.22% false-positive on non-native writers** against 5.19% on
native ones, and which fails hardest on students taught sentence frames *as a
documented accommodation*, because those frames lower perplexity by design. The tool
catches the honest and misses the dishonest.

Treating this as a cheating problem may be the deepest frame error in contemporary
education. It is a measurement crisis: our instruments stopped measuring what
they were built to measure. Detection tries to restore the old instrument. The
alternative starts by admitting the instrument is gone instead of defending it:
build assessment that is valid *given* assistance, measure the process and not the
artifact, and test what a person can do unassisted when that is the thing you
actually care about.

We do not know what the replacement looks like. We are fairly confident it is not a
classifier.

---

## 7. Nobody has checked whether staying wrong is safe

The teachable agent is this survey's most promising untested mechanism. It requires
an agent that adopts a learner's flawed model and holds it — applies it visibly,
does not silently repair it, and lets the world deliver the disconfirmation.

Every argument for it is good. The human analogue is strong (g = 0.48 with prior
expectancy). The mechanism is clear. Nobody has shipped it because commercial models
cannot stay wrong.

And nobody has checked the obvious risk: **does the learner repair the error, or
absorb it?** A confident agent demonstrating a wrong procedure across several
worked examples is, from a different angle, a very effective way to teach that wrong
procedure. The literature on erroneous-example instruction is small and mixed, and
none of it uses an agent that argues back.

This is the clearest case in the document of a risk that is obvious in hindsight and
entirely unstudied — and it sits underneath the mechanism we are most enthusiastic
about. We flag it against ourselves.

---

## 8. Ten questions that expose most of this

If the sections above are what we cannot see, these are the instruments for looking.
They are aimed at any vendor, any paper, any demo, and at this document. Most
claims in this field fail on the first three.

1. **Show me the delayed, unassisted, novel-item test.** Not the practice score, not
   the same items. Weeks later, device closed, problems never seen. ERIC returns
   **0 records** for `"retention test" AND "ChatGPT"` and 0 for `"transfer test"`.
   Without it, nothing was measured about learning.

2. **What happened to the gap, not the mean?** Report the interaction with prior
   attainment. Untargeted delivery reliably loads on the already-strong — Sierra
   Leone at **+0.195 SD per SD** of baseline.

3. **Does your metric survive the Null-Learner Test?** Simulate an agent maximising
   it while teaching nothing (§14). Engagement, time-on-task, streaks, satisfaction and
   session count all fail.

4. **Which arm isolates the AI from the humans around it?** In one trial, **44.3% of
   tutor edits were slowing the AI's questioning down.** No published trial isolates
   prompt-alone pedagogy from the human structure surrounding it.

5. **Is that a backtest or an intervention?** On a 350-million-review benchmark, a
   zero-parameter moving average beats every FSRS version. Predicting what a
   learner already did is not causing them to remember.

6. **What is your inter-rater reliability on the construct you claim to measure?**
   Published once for the field's leading pedagogy rubric and never again:
   Krippendorff's α of **0.066** for *inspires interest*, **0.023** for *monitors
   motivation*.

7. **Active control, or nothing?** Against nothing, almost everything works.
   Orton-Gillingham looks excellent until compared with other explicit instruction:
   **g = 0.22, p = .40.**

8. **What did you pre-register, and what did you report?** The largest trial in this
   corpus abandoned pre-registered subdomain analyses, had differential attrition
   favouring treatment, and swapped models mid-trial.

9. **Who consented out?** Every result is conditioned on a connected, consenting,
   mostly curious population. In one census, the learners this field most claims to
   serve appear zero times.

10. **What would falsify your thesis, and has it already happened?**

---

## 9. Turning question ten on ourselves

The counter-case to this entire survey, at full strength: **0.2–0.4 SD may be a
population parameter and not a technology limit.** The concession is only evaluable
if we say what the band is, so: **it is three field trials** (§09). Sierra Leone,
whose unadjusted estimate is not significant; Nigeria, which lost 43% of its sample;
Rori, which has eleven clusters and was authored by the people who sell it. A
rounding of those three, with no pooling and no confidence interval. A number that
thin is a weak ceiling and an equally weak floor, and the project's falsifier is
staked on it either way.

The reading that would hurt is that all three trials measured the same learners in
the same schools doing the same thing, and that what they found was the learners and
not the technology.

The evidence for that reading is not weak. The best-powered studies on record are
nulls — lesson study at **ES 0.02** across 181 schools and 12,747 pupils with very
high security and no dose–response; expanding intervals at **g = 0.032** with
**I² = 0%** across 54 experiments; Orton-Gillingham non-significant. And our own
corpus repeatedly shows elaboration losing to simplicity: five explanation rungs
did not beat three (**p = .738**), multiple representations harmed, mixed agent
panels lost to one good agent, eight random substitutions bought nothing over one.

There is a reading of this document in which every sophisticated mechanism we
propose is another elaboration about to lose to simplicity.

What would force us to concede: a well-powered trial of the assembled system,
constrained and grounded and pivoting and remembering and teachable, with a delayed unassisted
novel-item outcome, landing inside the 0.2–0.4 band. Not below it. *Inside* it.
That would mean the mechanisms are decorative and the band is the ceiling — and it
would be the first time that band had been measured on this class of system with
more than three field trials behind it, which is the only reason the trial settles
anything.

If that happens, the rewrite we would owe the reader is already drafted: *AI's
contribution is scalable, high-fidelity, high-dosage delivery of what already
worked.* Which is a smaller claim, still true, still worth building, and is
what the special-education evidence argues for on its own terms.

---

## 10. What we do while these remain unmeasured

- **Name correlated pedagogical error and build the monitor**, because a failure with
  no name gets no budget.
- **Measure past the point where the sign is known to flip.** One session is not an
  outcome.
- **Assume the epistemic curriculum is running** whether or not we measure it, and
  write the tutor's default behaviours as though a child is learning epistemics from
  every turn, because they are.
- **Let the learner model decay, and make restriction harder to justify than
  expansion.**
- **State the scarcity condition** whenever quoting an effect size measured in a
  world where the control group had nothing.
- **Never let a measurement of something else stand in for the measurement we have
  not taken.** Where no frontier trial exists, name the trial and its cost (§09). A
  survey that fills the gap with a number from a different machine has not been
  cautious; it has published a ceiling nobody measured.
- **Ask question ten first**, of everyone, including us.

The list above is incomplete. That is not modesty; it is the definition of the
category. What we can commit to is the posture: **publish the nulls, name the
failures we have not measured, and put the falsifier in writing before the result
arrives.**

---
title: "Groups and the Lifespan — cooperative learning's effect is an incentive rule, and software computes it for free"
section: lifespan
status: draft
date: 2026-07-30
source_report: research/raw/R7-groups-and-the-lifespan.md
---

# Groups and the Lifespan

Slavin's review of 99 cooperative-learning studies splits into two piles, and only
one of them contains the effect the field quotes.

Slavin (2014), *Anales de Psicología*, restating Slavin (1995): 99 studies in
elementary and secondary schools, each running at least four weeks, each comparing
achievement gains against a control class taught the same content conventionally. Of
the 64 whose group reward was computed from the sum of members' individual learning,
**50 (78%) found significantly positive effects on achievement and none found
negative effects, median effect size +0.32.** Studies whose group goal rested on a
single group product, or which gave no group reward at all, found few positive
effects: **median +0.07.** `MEASURED-META`, and a vote-count review with median
effect sizes, so no confidence interval exists or can.

Slavin states the mechanism in the same paper: if the reward comes from a single
group product, *"there is little incentive for group members to explain concepts to
one another, and one or two group members may do all the work."* The free-rider
problem and the achievement effect are one variable seen from two sides.

That reframes the finding. +0.32 against +0.07 is not a fact about groups. It is a
fact about incentive design, measured on groups, which makes it far more portable,
because incentive design is something software does and seating is not.

---

## 1. The condition is met in 17% of lessons

Adl-Amini, Völlinger & Eckart (2024), *European Journal of Psychology of Education*,
ran survey, structured interviews and rated observation across 49 German classrooms:

> *"Results show that the implementation quality of CL lessons was rather low. Only
> 7% of the observed teachers implemented the basic elements. Even group goals and
> individual accountability, the two most important elements of CL, were implemented
> in only 17% of the lessons observed."*

`OBSERVED`, ERIC EJ1439225. One country, one sample, no representativeness claim,
and the only classroom-scale fidelity measurement the source report could locate.

The modal classroom therefore delivers the +0.07 arm, because computing a reward from
every member's separately measured learning costs teacher time and a single poster
does not. Whenever this survey compares a one-to-one tutor against "what a classroom
does," the number on the other side is the small one.

For the eleven-year-old this survey is written around, the point is concrete. In a
group graded on one artifact, her contribution is either carried by somebody else or
invisible, and both are recorded identically. The condition that makes the
cooperative-learning effect appear is the condition that makes her work visible.

---

## 2. The field's most-quoted table never went through peer review

The base literature descends from two American programmes that both sell training in
the method they meta-analyse, and the checks on them are thinner than the field's
confidence.

**Johnson, Johnson & Stanne (2000)**, *Cooperative Learning Methods: A
Meta-Analysis*, is the usual source for per-method effect sizes. An ERIC title search
returns zero records. It circulates as a University of Minnesota Cooperative Learning
Center document; the authors run the Cooperative Learning Institute and publish
through Interaction Book Company. `OBSERVED — absence`. That is not an accusation. It
is a statement that the per-method table the field quotes was never peer reviewed and
could not be retrieved.

**Kyndt, Raes, Lismont, Timmers, Cascallar & Dochy (2013)**, *Educational Research
Review*, is the one deliberately independent replication attempt, with the strictest
inclusion rule in the field: 65 articles, 1995 onwards, primary through tertiary,
conducted in real classrooms. It reports positive effects on achievement and
attitudes, with study domain, age level and culture as significant moderators. Its
pooled magnitudes could not be retrieved: closed access, `is_oa: false` with zero
open-access locations, ScienceDirect 403, the repository copy intranet-only.
`MEASURED-META`, magnitude untraceable.

**Colliver, Feltovich & Verhulst (2003)**, *Teaching and Learning in Medicine*,
re-examined the primary studies under Springer, Stanne & Donovan's (1999)
meta-analysis and concluded that *"the meta-analysis' call for more widespread
implementation of small group learning is not supported"* (ERIC EJ664775). That paper
is closed too, so its internal argument could not be read.

This survey reports an unverifiable claim as a finding instead of dropping it (§24).
Applied here that yields one instruction: **treat a per-method cooperative-learning
effect size with no retrievable source as absent.** The condition-level result in §1
is open access and quoted verbatim. Build on that one.

---

## 3. Rationing artifact and mechanism, separated

This survey has been ducking a question: is the group a delivery constraint AI
removes, or a mechanism AI destroys? The question contains a false disjunction, and
the measured literature separates the halves cleanly enough to price both.

**Most of a classroom is a rationing artifact, and the numbers say so.** Traditional
lecture exists because talking to thirty people at once is the only way to talk to
thirty people at once; Freeman et al. (2014), *PNAS*, across 225 studies, put
examination and concept-inventory performance **+0.47 SD** under active learning
(`n = 158` studies) with an **odds ratio of 1.95** for failing under traditional
lecturing (`n = 67` studies), `MEASURED-META`. Ability-heterogeneous grouping,
imposed because a classroom cannot sort continuously, loses **0.12** against
homogeneous grouping across Lou et al.'s (1996) 20 direct comparisons. The single
group product is the +0.07 condition. AI removes all of this, and this survey has
been right about it.

Three things are mechanisms, and they behave differently under substitution.

**(a) Individual accountability, which AI supplies better than a classroom does.**
The entire measured achievement effect of cooperative learning is the margin by
which a reward computed from every member's individual learning suppresses the free
rider. A classroom reaches that condition one lesson in six because computing it
costs teacher time. A system that already measures every learner continuously
computes it for nothing. This is the one place where a group mechanism is
*strengthened* by removing the group.

**(b) Explaining and being explained to, partly recoverable.** This survey already
records `g = 0.56` for human learning-by-teaching and `g = 0.43` for peer tutoring's
tutor gain (§02). Marion & Thorley (2016), *Psychological Bulletin*, 75 effect sizes
from 64 studies, supply the mechanism for one part: collaborative inhibition is
robust, so a group recalls less than the pooled non-redundant recall of the same
number of individuals alone, while a separate 27-effect analysis found that
*"collaborative remembering tends to benefit later individual retrieval"* with
re-exposure to the study material partly responsible. Hearing the material again in
someone else's order does not require the other person to be a person.

**(c) Being disagreed with by someone genuinely uncertain, which AI cannot supply.**
Smith, Wood, Adams, Wieman, Knight, Guild & Su (2009), *Science*, in undergraduate
genetics, followed peer discussion with a second isomorphic question answered
individually to separate understanding from social transmission. Their result:
*"peer discussion enhances understanding, even when none of the students in a
discussion group originally knows the correct answer."* Whatever produces that gain
requires two agents who have committed to positions, neither of whom knows, and
whose commitment is real. A model that knows the answer and performs uncertainty is
not in that state. §19 reaches the same conclusion from the traditions side, where
chavruta's symmetry does not survive substitution.

**What is (c) worth?** The upper bound is Slavin's +0.32, of which (a) is by
construction the largest part, since removing it takes the effect to +0.07. The
better estimate of the residual is Lou, Abrami & d'Apollonia (2001) — 486 findings
from 122 studies, 11,317 learners, small group against individual with the
technology held constant — at **+0.15 on individual achievement, significantly
heterogeneous**. Call the irreducible peer mechanism 0.1 to 0.2 SD. It is real, it
is the only part of the group that cannot be faked, and it is smaller than this
survey's anxiety about it.

### The cost that has never been priced

The loss is not zero, and it sits somewhere specific. Two CSCL meta-analyses measure
scripted collaboration against unstructured or unguided collaboration, and both
split the same way:

| Meta-analysis | Base | Domain knowledge | Collaboration skills |
|---|---|---|---|
| Vogel, Wecker, Kollar & Fischer (2017) | CSCL scripts vs unstructured CSCL | **d = 0.20** | **d = 0.95** |
| Radkowitsch, Vogel & Fischer (2020) | 53 studies, 5,616 learners, vs unguided | **g = 0.24** | **g = 0.72** |

Radkowitsch et al. also report motivation at `g = 0.13, n.s.`, which is the
over-scripting worry failing to replicate in the form that was measured. Both
`MEASURED-META`.

Read the two columns against each other. If the goal is that a child understands
photosynthesis, this literature offers a fifth of a standard deviation. If the goal
is that a child can work with another person, it offers close to a full one, and
nothing else in this survey produces that outcome at all. So the real price of
perfect personalisation is not subject matter; it is that the learner never practises
working with a person. This survey has treated personalisation as an unmixed good and
has never costed that. For the learner it was written around, the cost lands hardest:
"works with others" is written into her plan as a goal, and a tutor that removes
every other person from the room removes the only instrument anyone has shown to
move it.

---

## 4. The group project that taught less than a shortened solo version

Bacon (2005), *Journal of Management Education* 29(2), verbatim:

> *"The characteristics of effective collaborative learning tasks, including group
> goals and individual accountability, are often not found in student group projects
> assigned in business classes. The current research found that content learning was
> actually inhibited by the use of a group project. The results indicate that the
> students who completed a project in groups learned less of the project-related
> content than did students who completed a shortened version of the project
> individually."*

`MEASURED-RCT` in the paper's own design terms, undergraduate business students. The
*shortened* individual version is the fair comparison, because the group version
distributes the work. Magnitude is not in the abstract and the article is closed.

This is a good null because it is not a failure to detect an effect. It found an
effect with the wrong sign, in the condition Slavin predicted would produce it, in
the setting where group projects are most heavily used. Alongside it, Murphy et al.
(2009), *Journal of Educational Psychology*, meta-analysed classroom discussion
approaches: they reliably increased student talk, reduced teacher talk and improved
text comprehension, while *"few approaches to discussion were effective at increasing
students' literal or inferential comprehension and critical thinking and
reasoning."* `MEASURED-META`. Discussion changes who is talking; whether it changes
what anyone understands depends on the approach, and for most approaches it did not.

---

## 5. The contingency exception does not survive

The argument this survey wanted for very young children is that a responsive AI is
contingent where a DVD is not, so the video deficit should not apply to it. Chased
properly, the exception does not hold.

The founding positive is Roseberry, Hirsh-Pasek & Golinkoff (2014), *Child
Development*: toddlers 24–30 months, **`N = 36`** across live interaction, socially
contingent video chat and yoked non-contingent video, so twelve children per cell.
*"Results suggest that children only learned novel verbs in socially contingent
interactions."* `MEASURED-RCT`.

Everything larger points the other way.

- **Troseth, Strouse, Verdine & Saylor (2018)**, *Frontiers in Psychology*, `n = 132`
  toddlers at 24 and 30 months in four conditions crossing responsiveness with
  medium: children learned in the responsive live condition at both ages and in the
  unresponsive live condition at 30 months, and *"neither group learned in the
  responsive or unresponsive video conditions."* `MEASURED-RCT`. This is Troseth's own
  lab, which produced the 2006 contingent-video result the exception rests on.
- **Strouse, Troseth, O'Doherty & Saylor (2018)**, `n = 88` 30-month-olds: on-screen
  contingency and parent modelling both raised engagement, *"however, only parent
  modeling increased children's subsequent word learning."* `MEASURED-RCT`.
- **Tsuji, Fiévét & Cristia (2021)**, 16-month-olds across in-person, video chat and
  a virtual agent: above-chance word learning in the in-person group only, and the
  verbatim conclusion that *"contingency is not sufficient either."* `MEASURED-RCT`.
- **Strouse & Samson (2021)**, *Child Development*, 122 independent effect sizes from
  59 reports across ages 0–6: an average deficit of about half a standard deviation,
  decreasing with age, and *"no difference between studies using live versus
  prerecorded video,"* with the authors flagging quality and publication-bias problems
  that may have overestimated it. `MEASURED-META`.

What survives moderation is the adult in the room. Mallawaarachchi et al. (2024),
*JAMA Pediatrics*, pooled 100 studies and 176,742 participants: among all screen-use
contexts examined, **co-use was the only one positively associated with cognitive
outcomes, `r = 0.14, 95% CI [0.03, 0.25]`**, against programme viewing at `r = −0.16`
and background television at `r = −0.10`. `MEASURED-META`, observational.

### The product decision

**Under three, ship nothing child-facing.** WHO (2019) recommends no screen time for
infants under 1 and for 1-year-olds, and no more than one hour for ages 2 and 3–4.
DeLoache et al. (2010) randomised a month of at-home baby-media DVD viewing in
12–18-month-olds: *"children who viewed the DVD did not learn any more words,"* with
the highest learning in a no-video condition where parents taught the same words
during everyday activities. And the intervention family that works moves the adult:
Dowdall et al. (2020), 19 RCTs, `N = 2,594`, caregiver book-sharing competence
**`d = 1.01`** against child expressive language `d = 0.41`, while Noble et al. (2019)
put shared reading at **`ḡ = 0.021, p = .783`** against active controls, confirmed by
their own `n = 150` RCT. There is no gap in that picture for a child-facing tutor to
fill.

**Three to five, ship one shape.** Xu, Aubele, Vigil, Bustamante, Kim & Warschauer
(2022), *Child Development*: **117 children aged 3–6**, randomly assigned in a 2×2
crossing dialogic against non-dialogic reading with a conversational agent against a
human partner. Dialogic reading raised story comprehension — event memorisation
`β = 0.53, p < .001`, inference making `β = 0.38, p < .05`, sequence understanding
`β = 0.34, p < .05` — and *"the interaction model suggested that dialogic reading
with an agent induced a comparable level of positive effect on children's story
comprehension as an adult reader (β = 0.22, p = .35)."* `MEASURED-RCT`. Carry the
caution the authors state themselves: a non-significant interaction at `n = 117` is
an underpowered equivalence claim and not demonstrated equivalence, and the sample
had *"homogeneous high language proficiency."*

Written as the product decision it is: for ages three to five the system's user is
the caregiver and the child is the beneficiary; the surface is a dialogic reading
partner that talks, that the child answers aloud, on content an adult chose, with the
adult present and reading along; the primary reported outcome is caregiver
book-sharing competence, and child language is accepted as the small downstream
consequence it is. §15 sets the floor on what is owed to children, and this is the
first place in the survey where meeting it means shipping nothing.

---

## 6. Andragogy is a null, and the training industry does not measure what it sells

Knowles's andragogy organises the adult-education field, and it was put to
experimental test. Rachal (1994), ERIC ED380566, reviewed 18 experimental comparisons
of andragogical against pedagogical method, 15 of them dissertations. Of the **16 that
examined achievement, 10 found no significant difference and 2 found the traditional
group performed better.** Two variables did favour andragogy: application of the
learned material, and attendance. `MEASURED-META`, a vote-count review with no
pooling. The most recent randomised test agrees: Bradley (2010) randomised 52
non-profit staff to andragogical or pedagogical online grant-writing modules and
analysed 33, finding no significant differences in reaction, achievement growth,
grant-writing performance or completion. `MEASURED-RCT`, null on every outcome. And
`OBSERVED — absence`: **no meta-analysis of andragogy exists**, ERIC returning zero
records for `"andragog*" AND "meta-analysis"`, with the one item calling itself a
meta-analysis being a narrative review carrying no `k` and no pooled estimate.

What survives is not a learning mechanism. It is two behavioural facts, that adults
who chose to be there apply the material and attend, plus one design constraint, that
participation is voluntary and attrition is therefore the binding risk, which §14
already builds for.

The industry that sells to these learners gives itself away in its sample sizes.
Arthur, Bennett, Edens & Bell (2003), *Journal of Applied Psychology*, report
training-effectiveness sample-weighted mean `d`s of **0.60 (`k = 15, N = 936`) for
reaction, 0.63 (`k = 234, N = 15,014`) for learning, 0.62 (`k = 122, N = 15,627`) for
behaviour, and 0.62 (`k = 26, N = 1,748`) for results.** `MEASURED-META`. Every effect
sits between 0.60 and 0.63, which looks suspicious until you read the `k`s, and the
`k`s are the finding. Learning is measured 234 times. Results are measured 26 times,
on 1,748 people in total, and that is the whole industry's evidence for whether
training changes anything an employer would pay for. Blume, Ford, Baldwin & Huang
(2010), 89 studies, supplies the reason to distrust even the 122: transfer outcomes
obtained by the same source in the same measurement context *"consistently inflated
transfer relationships."*

For practice figures, use the survey that has a DOI. Twitchell (1997), LSU
dissertation, published as Twitchell, Holton & Trott (2000), `n = 146` returned
surveys at a 42% response rate, found technical training managers reporting each of
Kirkpatrick's four levels in this percentage of their courses: **Level 1 — 72.74%,
Level 2 — 47.05%, Level 3 — 33.73%, Level 4 — 20.82%.** `OBSERVED`. The far more
widely circulated claim that only about 10% of training transfers to the job is
folklore with a citation attached. It is universally attributed to Georgenson (1982)
in a trade magazine, and that paper is absent from Crossref, absent from OpenAlex and
absent from ERIC, which indexes a *different* Georgenson article from the same journal
and era, so the gap is not a coverage artefact. No sample, no method, not cited here.

Adults have the most money, the least time, and the only unambiguous transfer
criterion in this survey: a job, recorded by somebody else in state
unemployment-insurance wage records. Every other population requires the evaluator to
build the outcome measure first. This one does not, which makes it the one segment
where an outcome could genuinely be measured, and it is the segment that measures
results 26 times.

---

## 7. Paying adults £5 a class reduced attendance

Brooks, Burton, Cole, Miles, Torgerson & Torgerson (2008), *Oxford Review of
Education*, cluster-randomised 29 adult literacy classes using minimisation and paid
intervention-group learners **£5 (US$10) for each class attended**. In the 28
remaining classes there was *"a statistically significant reduction of about 1.5
sessions (95% confidence interval (CI) 0.28, 2.79; p = 0.019) attended by the
intervention group compared with control, after adjusting for cluster size and
baseline scores."* The reading-score difference was **−2.38**, with controls scoring
higher, not statistically significant (95% CI −7.40 to 2.57, p = 0.33).
`MEASURED-RCT`, the only UK RCT of financial incentives in adult literacy, and the
intervention ran backwards on its own primary outcome.

The companion result is about software. Ainsworth et al. (2012) ran two RCTs of an
online medication-dosage simulation for student nurses' general numeracy and found a
small negative intention-to-treat effect, statistically significant in one trial,
*"however, compliance with the intervention was very low in both trials, with only 24
and 12% of students allocated to the intervention groups spending more than 15
minutes using the programme."* `MEASURED-RCT`. Between 76% and 88% of a motivated,
professionally obligated population did not spend a quarter of an hour with free
software aimed at a skill they were being assessed on. For adults, dosage is the
trial, and an adult-tutoring specification whose efficacy argument does not open with
an engagement number is not making an argument.

---

## 8. One trial, two arms, one journal

The WIA Gold Standard Evaluation randomly assigned over 34,000 customers across 28
randomly selected local workforce investment areas to three research groups. At
thirty months, intensive staff-assisted services raised earnings by *"$3,300 to
$7,100 (7 to 20 percent) per customer depending on the data source."* The training
arm produced nothing: *"the evidence suggests that training funded by the Adult and
Dislocated Worker programs does not have positive impacts in the 30 months after
study enrollment."* `MEASURED-RCT`.

The counselling result appears as McConnell, Schochet, Rotz, Fortson, Burkander &
Mastri (2021) in the *Journal of Policy Analysis and Management*. The training null
appears only in the grey-literature report to the Department of Labor.

Same trial, same randomisation, same investigators, two arms, one journal
publication. That is the file-drawer problem visible inside a single federal
evaluation, and it bears on how this survey reads every literature it cites, because
the shelf we read from is the published one.

---

## 9. What the arithmetic of the missing trial requires

The question this section could not answer from the literature is whether the
irreducible peer mechanism — commitment plus genuine mutual uncertainty — carries
measured achievement over an AI tutor supplying everything else. The trial has three
arms, randomised at learner level within classrooms, one term, one subject with a
validated concept inventory such as introductory mechanics: **A**, AI tutor alone
with individual-accountability scoring and no peers; **B**, AI tutor plus an AI peer
that commits to a possibly-wrong position and defends it, which is §26's
specification put to test; **C**, AI tutor plus brokered human pairing on
disagreement items. Primary outcome is a delayed concept-inventory score at eight
weeks, scored blind; secondary is a collaboration-skill measure.

The contrast that matters is C − B. §3 puts the residual at 0.1–0.2 SD, so the trial
must be powered for the low end. Detecting `d = 0.15` at 80% power, α = 0.05
two-sided, needs `n ≈ 699` per arm, about 2,100 learners across three arms. With
individual randomisation inside classrooms, an ICC of 0.05 and an average cluster
size of 25 give a design effect of `1 + (25 − 1)(0.05) = 2.2` against contamination,
raising the requirement to roughly **4,600**. At a more optimistic `d = 0.25` it is
`n ≈ 252` per arm before the design effect and about 1,700 after.

That arithmetic explains the state of the field. A 60-learner pilot has 80% power
only for `d ≈ 0.51`, which is larger than the entire cooperative-learning effect. So
**any study reporting a null on peers with fewer than 500 learners per arm has not
tested the hypothesis**, and this survey will read every such result that way.

The cheap experiment is a different one. The collaboration-skill secondary outcome is
where the CSCL meta-analyses predict `g ≈ 0.7`, and at that magnitude `n ≈ 33` per
arm suffices before the design effect. The first experiment worth running is not the
achievement question at all: it is whether an AI-mediated group teaches a learner to
work with a person.

### Obligations

- **Compute every multi-learner score from members' separately measured individual
  performance**, never from a shared artifact. The falsifier is already in the
  literature, since a system rewarding a single group product has a predicted effect
  of +0.07.
- **Keep the system outside the dyad when the goal is disagreement.** Match two
  learners whose current model states disagree on the same item, require each to
  commit before seeing the other, then let them talk. The matching criterion is
  disagreement, not complementary expertise, because Smith et al. show the gain
  survives when neither knows.
- **Publish a collaboration-skill measure alongside every achievement claim**, or
  concede that the survey has stopped measuring the one outcome the group was best at
  producing.
- **Nothing child-facing under three.** From three to five, a caregiver-facing
  dialogic reading partner whose primary reported outcome is caregiver book-sharing
  competence.
- **For adults, publish minutes-on-task before any efficacy claim**, and where
  administrative wage records exist, plan to read the outcome at seven and ten years.
- **Treat a per-method effect size with no retrievable source as absent**, including
  the ones this survey would like to use.

The classroom's best-evidenced mechanism turned out to be an incentive rule that
classrooms can afford one lesson in six. A system that already measures every learner
continuously can afford it every time, which makes it the cheapest large win
available here and the one thing on this list that needs no new research at all. The
expensive item is the trial above, and the reason to state its arithmetic in public
is that we would otherwise be free to call the peer question settled on evidence that
never had the power to settle it.

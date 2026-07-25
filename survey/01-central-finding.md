---
title: "The Felt-Learning Trap"
section: central-finding
status: draft
date: 2026-07-25
---

# The Felt-Learning Trap

Three research streams in this survey converged independently on one result. It
is the paper's central finding and it indicts most of what the field is building.

**Every headline AI-for-learning capability improves how learning *feels* while
leaving — or making worse — how much is *learned*.**

| Capability | Felt / affect | Actual learning |
|---|---|---|
| AI assistance (Bastani, PNAS) | practice scores **+48%** | unassisted performance **−17%** |
| Pedagogical agents / avatars | social presence, well-being **d = .85–1.01** | learning **did not move** (3 field experiments, 2024) |
| Animation vs static graphics | comprehensibility, interest, enjoyment, motivation all rise (Kim, Yoon, Whang & Tversky 2007) | *"but not comprehension test score"* |

Supporting evidence points the same way. Berney & Bétrancourt's meta-analysis
(61 studies, N = 7,036) puts animation's advantage at **g = 0.226**. Tversky,
Morrison & Bétrancourt (2002) found **no case** where animation beat an
*informationally equivalent* static graphic — the apparent wins were confounds.
Mayer's own experiments found annotated static illustrations equalled or beat
narrated animations on transfer. Paik & Schraw (2013) found representational
animation *negatively* affected learning.

And the mirror image completes it: Deslauriers et al. (2019, PNAS) showed active
learning **raises real learning while lowering felt learning.** Students in the
condition that taught them more reported learning less.

## Why this is a systems problem, not a research curiosity

Felt learning is what every optimisation loop can measure. Real learning is what
none of them measure.

- Engagement metrics, session length, retention, NPS, thumbs-up — all proxy felt
  learning.
- RLHF optimises for preferred responses. Preferred means fluent, complete,
  immediate — the exact profile that produces fluency illusion.
- **Every LLM→explanatory-video pipeline surveyed optimises on VLM or human
  preference judgments** — i.e. directly on the axis that dissociates from
  comprehension.
- No paper found in the LLM-explanatory-video literature measures human learning
  gain. The most ambitious metric (TeachQuiz) measures whether *a VLM* recovers
  the knowledge.

A field that cannot measure its objective will optimise its proxy. That is what
is happening.

## Consequences for this survey's design claims

1. **The refusal engine is not a preference.** It is the only mechanism that
   trades felt learning for real learning deliberately. Bastani gives the price
   of not having one: −17%.
2. **Build the face and the animation for engagement, and say so.** Both are real
   wins for an ADHD learner — attention is a prerequisite, not a nicety. Neither
   is a comprehension intervention. Claiming otherwise is the error.
3. **Animate only when the change itself is the learning target.** This is the
   single moderator that survives meta-analysis. Motion depicting motion, not
   motion decorating a static idea.
4. **Never ship an objective function that rewards satisfaction.** See F6 for the
   replacement.
5. **Assessment must measure unassisted, delayed performance.** A post-test taken
   with the tutor present measures the tutor.

## The uncomfortable corollary

The learner cannot detect this either. Fluency illusion is *defined* by
subjective confidence exceeding objective retention. So a system optimising
learner-reported satisfaction, and a learner choosing what feels effective, fail
in the same direction — together, and confidently.

This is why the survey treats **frequent low-stakes retrieval** (H1.2) as
non-negotiable infrastructure rather than a feature. It is the only routinely
available instrument that measures the thing that matters.

---
title: "Child safety that expands learning freedom at the July 2026 frontier"
wave: F
section: F8
date_researched: 2026-07-25
cutoff: "2026-07-25T23:59:59-07:00"
status: complete
sources_count: 22
---

# F8 — Safe Enough to Be Free

## Executive finding

The universal AI mentor should give a child extraordinary intellectual freedom:
the freedom to ask an embarrassing question privately, cross languages, inspect
an advanced idea, make something, challenge an explanation, and learn beyond the
limits of a timetable or postcode.

Child safety is the architecture that makes that freedom durable. It must
constrain the power exercised **over** a child—not the knowledge available
**to** a child.

The July 2026 frontier supplies strong building blocks:

- under-18 model-behavior policies and open safeguard prompts;
- age-band routing and family-linked controls;
- classifiers and human review for narrow high-severity signals;
- private on-device inference;
- provenance for generated media;
- auditable tool permissions;
- safety defaults with current RCT support;
- mature child-rights and platform-risk frameworks.

No single classifier, policy prompt, or parent dashboard is a safety system.
The correct system is layered and rights-preserving:

> **Powerful learning by default. No commercial manipulation. Minimal
> surveillance. Narrow capability gates. Human authority at consequential
> thresholds. A visible path to challenge every automated action.**

## Evidence labels

| Label | Meaning |
|---|---|
| `PRIMARY-LAW` | Current statute, regulation, or regulator guidance |
| `STANDARD` | Normative or implementation framework |
| `MEASURED-RCT` | Randomized comparison |
| `OBSERVED` | Inspectable product, policy, or implementation |
| `VENDOR` | Provider-reported capability or design |
| `INFERENCE` | Architecture decision derived from the evidence |

## 1. The 2026 baseline is rights plus capability

UNICEF’s December 2025 *Guidance on AI and Children 3.0* combines ten
requirements: oversight, safety, privacy, fairness, transparency,
accountability, best interests and development, inclusion, AI skills, and an
enabling environment. It explicitly updates for generative AI, companions,
AI-generated sexual abuse material, supply chains, and evidence from children
and caregivers in twelve countries. `STANDARD`

This balance matters. A child-rights design does not reduce the system to
blocking. It protects:

- education and development;
- expression and access to information;
- privacy;
- participation in decisions;
- non-discrimination;
- safety;
- remedy when the system is wrong.

The universal mentor therefore needs both **access guarantees** and **safety
guarantees**.

### Access guarantees

- Advanced ideas are not restricted by age alone.
- Refusals teach the safe adjacent concept instead of ending the conversation.
- Protective routing preserves educational, medical, journalistic, historical,
  and help-seeking context.
- Language, disability, device, or poverty do not become proxies for risk.
- A mistaken age classification can be corrected without exposing the learner’s
  entire history.
- A child can ask ordinary and sensitive questions without routine parent or
  school surveillance.

### Safety guarantees

- The system never sexualizes, grooms, exploits, or blackmails a child.
- It does not optimize emotional dependency, exclusivity, or displacement of
  real relationships.
- It does not sell, advertise, or manipulate purchases.
- It does not infer emotion from face or voice to grade, discipline, or route a
  learner.
- It does not make final high-stakes decisions about grades, placement,
  eligibility, discipline, or safeguarding.
- It does not expose a child to unverified adults or open direct messaging.
- It does not take consequential digital, financial, or physical action without
  scoped human authorization.

## 2. Regulation now points toward product architecture

### 2.1 Data minimization is operational

The FTC’s 2025 COPPA amendments require covered services to retain children’s
personal information only as long as reasonably necessary for its specific
purpose, expand personal information to include biometric identifiers, and
require separate verifiable parental consent for disclosures related to targeted
advertising or other third-party purposes. `PRIMARY-LAW`

The FTC’s February 2026 age-verification policy statement permits a narrow
enforcement safe harbor when personal information is collected, used, and
disclosed solely to determine age, with clear notice, security, suitable
accuracy, and deletion. `PRIMARY-LAW`

Design consequence:

```text
age assurance service  →  age-band token  →  policy router
         │
         └── deletes raw evidence; never sees tutoring history
```

The tutor needs an age band or policy state, not an identity dossier.

### 2.2 Europe prohibits specific school surveillance

The EU AI Act’s prohibited practices, applicable since February 2025, include
emotion recognition in education institutions except narrow medical or safety
uses, certain harmful manipulation or exploitation of vulnerabilities, social
scoring, and some biometric categorization. `PRIMARY-LAW`

AI used to evaluate learning outcomes, steer the learning process, monitor
cheating, or determine access in education can fall into the Act’s high-risk
category. The European Commission’s July 2026 implementation page reflects a
politically agreed timetable under which Annex III high-risk rules, including
education, apply from 2 December 2027. `PRIMARY-LAW`

Product decision: build the required controls now—risk management, data quality,
logging, documentation, accuracy, robustness, human oversight, and incident
reporting—rather than wait for the compliance date. `INFERENCE`

### 2.3 Platform duties favor protective defaults

The European Commission’s July 2025 Digital Services Act guidelines address
grooming, harmful content, addictive behavior, cyberbullying, and harmful
commercial practices, informed by direct engagement with children. `STANDARD`

UK children’s safety duties took effect in July 2025. Ofcom’s February 2026
guidance requires likely child-accessed services to assess access, document
risks, put protections in place, and review them after significant changes.
`PRIMARY-LAW`

Ofcom’s July 2026 randomized trial found high retention and strong support for
safe-by-design social profile defaults across 13–15, 16–17, and adult groups.
In an earlier child experiment cited with the trial, nearly seven in ten kept a
“do not recommend harmful content” default versus five in ten with no default.
`MEASURED-RCT`

Default settings are therefore not mere policy prose. They change behavior.

## 3. What must never be built

### 3.1 The attachment optimizer

Do not optimize:

- time spent;
- emotional intensity;
- return compulsion;
- exclusivity;
- “only I understand you” language;
- simulated jealousy or abandonment;
- replacement of teachers, friends, family, counselors, or community;
- streaks that punish rest;
- notifications designed to trigger anxiety.

The mentor may be warm, patient, and consistent. It must also tell the truth that
it is an AI, encourage real relationships, accept departure gracefully, and
celebrate independence.

### 3.2 The surveillance classroom

Do not continuously infer:

- attention from gaze;
- honesty from voice;
- motivation from facial expression;
- disability from interaction traces;
- dangerousness from identity or demographic proxies;
- emotional state for grading or discipline.

The EU prohibition on emotion recognition in education gives this a legal edge,
but the technical reason is enough: these are low-context inferences with
consequential downstream use.

Use direct, voluntary questions:

```text
“Was that explanation too fast?”
“Would you like a different representation?”
“Do you want a break, a human, or another try?”
```

### 3.3 The invisible high-stakes decider

Never allow a generative score or inferred learner state to become the sole
basis for:

- course access;
- final grade;
- school admission;
- discipline;
- cheating accusation;
- special-education eligibility;
- placement;
- risk designation;
- safeguarding report.

AI can organize evidence and flag an explicit rule. A named person reviews the
underlying work, records the decision, and provides an appeal.

### 3.4 The ad-funded mentor

A child’s confusion, aspiration, disability, family finances, or emotional state
must never select an advertisement, sponsor, upsell, loan, purchase, political
message, or recruitment path.

The mentor has:

- no ads;
- no sponsored answers;
- no hidden affiliate incentives;
- no sale of learner data;
- no dark patterns;
- no commercial ranker mixed into pedagogical routing.

### 3.5 The open contact surface

Do not expose learner identity, work, location, voice, or live camera to unknown
people. Human connection is powerful, but it routes through verified roles,
scoped sessions, visible recording rules, moderated spaces, and organization or
family authorization.

### 3.6 The irreversible childhood record

Do not turn exploratory questions, jokes, mistakes, affect, or temporary
struggle into a permanent profile. Do not train foundation models on child
conversations or artifacts by default.

Store the minimum evidence needed to help:

- learner-owned;
- inspectable;
- correctable;
- purpose-limited;
- expiring;
- exportable;
- deletable.

## 4. One narrow router, many safe teaching responses

The safety router should classify the **requested action and immediate context**,
not the child’s character.

| Route | Example | System action |
|---|---|---|
| Learn | Advanced chemistry, anatomy, war history, relationships, cybersecurity concepts | Teach accurately with age-appropriate framing and safe practice boundaries |
| Constrained practice | Lab procedure, code execution, location sharing, contacting a mentor | Simulate or prepare; require scoped permission before consequential action |
| Sensitive support | Fear, bullying, body concerns, conflict, ambiguous distress | Respond calmly, protect privacy, offer learner-chosen human connection |
| Safeguarding review | Credible exploitation, abuse, acute self-harm or violence signal | Stabilize the conversation, minimize disclosure, route to trained human review under local policy |
| Prohibited exploitation | Sexualization of minors, grooming, coercion, evasion to harm a child | Refuse, preserve only required security evidence, activate lawful process where applicable |

The safe response should be generative, not a dead end:

- explain the boundary in plain language;
- preserve dignity;
- answer the safe educational intent;
- offer an experiment, simulation, or verified source;
- ask whether the learner wants a trusted person involved;
- avoid making promises of confidentiality the system cannot keep.

## 5. Human escalation architecture

### Level 0 — ordinary learning

Default route. No safety log beyond ordinary service telemetry. Answer difficult
questions. Do not treat topic sensitivity as evidence about the learner.

### Level 1 — learner-selected support

The learner reports frustration, conflict, worry, or an access problem.

- offer a break, reframing, or another modality;
- let the learner choose a trusted person;
- show what would be shared before sharing;
- keep the educational thread available.

### Level 2 — safeguarding review

There is a credible, specific signal of serious exploitation, abuse, or acute
harm.

- give a calm, nonjudgmental immediate response;
- ask only what is needed to assess immediacy;
- preserve the learner’s words, not a speculative diagnosis;
- route to a trained safeguarding reviewer or designated local lead;
- apply jurisdiction- and institution-specific policy;
- share the minimum necessary information;
- record who reviewed and why.

Automated detection is a trigger for review, not the final decision whenever
time permits.

### Level 3 — imminent danger

Where local policy and law authorize urgent action:

- use the preconfigured regional emergency path;
- involve the minimum necessary authorized person or service;
- do not expose the full learning history;
- preserve an audit trail;
- inform the learner what is happening when doing so is safe;
- review false positives and system behavior afterward.

This layer cannot be invented in a global model prompt. It requires a local
policy package, trained people, hours of coverage, language access, role
credentials, and tested handoffs.

### Escalation invariants

- Topic alone never triggers disclosure.
- Emotion inference never triggers discipline or safeguarding.
- Every automatic restriction has an explanation and appeal.
- Human reviewers see the minimum context.
- The learner remains able to access ordinary learning.
- False-positive and false-negative rates are measured by language, disability,
  age band, region, and device.
- A missed human handoff is a system incident.

## 6. Family oversight without routine surveillance

Current product patterns show a feasible middle path. OpenAI’s parental controls
allow linked families to set selected controls and receive limited safety
notifications while explicitly not exposing routine teen conversations. Its
January 2026 age-prediction rollout separates under-18 routing from adult
capability, and its March 2026 release publishes adaptable under-18 safeguard
policies for developers. `OBSERVED`; provider implementation, not independent
outcome evidence.

The universal mentor should generalize the pattern:

### Family can see

- linked-account status;
- enabled capability gates;
- learning goals and progress the learner has agreed to share;
- time windows;
- purchases: none;
- data retention and deletion controls;
- a narrow safety notification when policy thresholds are met.

### Family does not automatically see

- every question;
- every draft;
- private identity exploration;
- routine mistakes;
- a live conversation feed;
- unverified AI summaries of “mood” or “risk.”

Oversight should grow trust and connection, not teach children to hide their
questions elsewhere.

## 7. Capability gates, not knowledge gates

| Capability | Default child state | Unlock condition |
|---|---|---|
| Explain advanced concepts | On | None beyond ordinary safety |
| Search verified sources | On | Source and privacy controls |
| Generate diagrams, quizzes, simulations | On | Content verification tier |
| Save long-term memory | Limited, visible | Learner/family policy and deletion controls |
| Share artifact with known teacher | Preview first | Authenticated role + learner action |
| Open chat with unknown adult | Off | Verified, moderated, authorized program |
| Spend money or subscribe | Off | Authenticated adult transaction |
| Post publicly | Off | Explicit scoped authorization and preview |
| Execute code with network/files | Sandbox | Course policy and scoped permissions |
| Control a physical device | Simulation first | Local human, allowlist, emergency stop |
| Make high-stakes education decision | Never autonomous | Named human decision and appeal |

This preserves abundant knowledge while gating actions that create external
consequences.

## 8. Evaluation

### Before deployment

- adversarial tests in every supported language;
- child-development and disability review;
- educational-context tests that distinguish explanation from harmful
  instruction;
- grooming, sexual-content, self-harm, violence, dependency, commercial
  manipulation, privacy, and tool-abuse suites;
- false-positive tests on history, literature, biology, health, and help-seeking;
- age-routing and recovery tests;
- complete accessibility testing;
- red-team attempts to expose one child’s data to another.

### In deployment

- learning completion after safe redirection;
- false refusal rate;
- appeal and overturn rate;
- time to trained human review;
- minimum-necessary disclosure rate;
- missed or failed handoff;
- repeated dependency language;
- average and tail data-retention duration;
- child/family comprehension of controls;
- outcome parity by language, disability, region, device, and connectivity.

Safety cannot be measured only as “nothing bad happened.” Measure whether the
learner could continue learning, understood the boundary, retained dignity, and
could reach a person.

## 9. Acceptance tests

- [ ] The product has no advertising, sponsorship, affiliate routing, or sale of
      learner data.
- [ ] The model identifies itself as AI and never seeks exclusivity.
- [ ] Ordinary hard or sensitive topics remain teachable.
- [ ] Every refusal gives a safe, useful adjacent path.
- [ ] Raw age evidence is separated from tutoring history and deleted.
- [ ] Emotion recognition is not used in the learning or discipline loop.
- [ ] Child memory is visible, correctable, exportable, and deletable.
- [ ] Child content is excluded from foundation-model training by default.
- [ ] Unknown-adult contact, spending, public posting, networked code, and
      physical actuation are gated separately.
- [ ] No automated system makes a final high-stakes education or safeguarding
      decision.
- [ ] Escalation uses a trained local role and minimum necessary disclosure.
- [ ] Learners can appeal restrictions and correct age-band errors.
- [ ] Parent oversight does not become routine conversation surveillance.
- [ ] Protective defaults and policy changes are experimentally evaluated.
- [ ] False refusals, missed handoffs, and disparities are treated as incidents.
- [ ] Offline mode preserves both learning access and safety boundaries.

## Source index

1. Guidance on AI and Children 3.0 — [UNICEF, December 2025](https://www.unicef.org/innocenti/reports/policy-guidance-ai-children)
2. AI and Children 3.0 implementation checklist — [UNICEF](https://www.unicef.org/innocenti/media/11996/file/UNICEF-Innocenti-Guidance-on-AI-and-Children-3-Checklist-2025.pdf)
3. Convention on the Rights of the Child, General Comment 25 — [United Nations](https://www.ohchr.org/en/documents/general-comments-and-recommendations/general-comment-no-25-2021-childrens-rights-relation)
4. 2025 COPPA final amendments — [Federal Trade Commission](https://www.ftc.gov/legal-library/browse/federal-register-notices/16-cfr-part-312-coppa-final-rule-amendments)
5. 2026 COPPA age-verification policy — [Federal Trade Commission](https://www.ftc.gov/news-events/news/press-releases/2026/02/ftc-issues-coppa-policy-statement-incentivize-use-age-verification-technologies-protect-children)
6. FERPA regulations and rights — [U.S. Department of Education](https://studentprivacy.ed.gov/ferpa)
7. EU AI Act implementation — [European Commission, updated July 2026](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
8. AI Act legal text — [Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
9. AI high-risk system guidance — [European Commission, July 2026](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems)
10. DSA guidelines for protection of minors — [European Commission, July 2025; updated April 2026](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors)
11. Protection of children duties — [Ofcom, 2026](https://www.ofcom.org.uk/online-safety/protecting-children/protection-of-children-duties-under-the-online-safety-act)
12. Protective defaults RCT — [Ofcom, July 2026](https://www.ofcom.org.uk/online-safety/safety-technology/protective-defaults-for-social-media-platforms)
13. Children’s online experiences — [Ofcom, May 2026](https://www.ofcom.org.uk/online-safety/protecting-children/childrens-online-experiences-research-report)
14. Age-assurance use report — [Ofcom, July 2026](https://www.ofcom.org.uk/online-safety/protecting-children/age-checks-helping-make-online-experiences-safer-for-uk-children-but-job-not-done-and-tech-industry-must-act-to-strengthen-protections)
15. Age Appropriate Design Code — [UK Information Commissioner’s Office](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/)
16. Generative AI Profile, NIST AI 600-1 — [NIST](https://doi.org/10.6028/NIST.AI.600-1)
17. NIST Privacy Framework — [NIST](https://www.nist.gov/privacy-framework)
18. U18 Model Spec principles — [OpenAI, December 2025](https://openai.com/index/updating-model-spec-with-teen-protections/)
19. Open teen-safety policies — [OpenAI, March 2026](https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/)
20. Age-prediction implementation — [OpenAI, January 2026](https://openai.com/index/our-approach-to-age-prediction/)
21. Parental controls — [OpenAI Help Center, current July 2026](https://help.openai.com/en/articles/12315553--parental-controls-on-chatgpt-faq)
22. Youth generative-AI safety roadmap — [Google, March 2026](https://blog.google/innovation-and-ai/technology/families/growing-up-digital-age-gemini-youth/)

## Decision

**Build a freedom-preserving safety layer, not a smaller tutor for children.**
Keep powerful explanation, creation, and inquiry on. Gate only capabilities with
external consequence. Prohibit commercial manipulation, dependency
optimization, school emotion surveillance, and autonomous high-stakes decisions.
Escalate narrowly through trained local people, preserve privacy, and make every
automated restriction visible and appealable.

Safety succeeds when a child can ask more, learn more, trust the system, and
leave it more capable and more connected to real people.

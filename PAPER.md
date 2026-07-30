# Beyond the AI Tutor

## Evidence and a reference architecture for persistent, multimodal learning systems

**Article type:** Design-oriented evidence synthesis and reference architecture

**Manuscript status:** Working paper, 30 July 2026

**Authorship:** To be supplied by the project owner before submission

**Companion materials:** [Living Evidence Atlas](ATLAS.md) · [Corrections ledger](CORRECTIONS.md) · [Research reports](research/raw/) · [Runnable mechanism demonstrations](docs/demos/)

> Authorship, affiliations and a corresponding-author address are deliberately omitted. Submission requires named, accountable human authors.

## Abstract

Generative models can explain, converse, generate media and call tools, but those capabilities do not by themselves constitute a learning system. The central design problem is control: selecting a next action from evidence about a learner, changing representation when the evidence warrants it, withdrawing assistance before apparent fluency becomes dependence, and testing whether capability transfers after the system is absent. This article synthesizes recent evidence on generative-AI tutoring with established findings from learning science and proposes a reference architecture for a persistent, multimodal personal learning system. The evidence supports a constrained position. Purpose-built and human-supervised systems can improve proximal performance, while unguarded assistance can improve practice and degrade subsequent unassisted performance. Preference, ease and engagement are therefore unsafe primary objectives. Evidence about durable transfer, learners with disabilities and integrated multimodal systems remains sparse. The proposed architecture separates five functions: learner-state estimation, competing diagnostic hypotheses, representation selection and generation, pedagogical orchestration, and independent outcome verification. It adds three requirements that are commonly peripheral in tutoring systems: access preferences as first-class state; portable, inspectable learner records; and an interchange through which authors and educators can contribute attributable instructional techniques. The evaluation protocol makes delayed, unassisted performance on novel tasks the primary outcome, compares against a strong general-model baseline, and reports distributional effects alongside means. The resulting thesis is narrower than “AI tutors work” and more actionable: frontier models are components of a possible learning system, but the system must be designed and tested as an evidence-seeking control loop whose objective is independent capability.

**Keywords:** artificial intelligence in education; intelligent tutoring systems; generative AI; learner modelling; multimodal interaction; accessibility; transfer; human–AI collaboration

## 1. Introduction

The public interface to generative artificial intelligence is usually a conversation. That interface encourages a category error in education. A fluent system that answers questions, produces explanations and remembers a thread may feel like a tutor, yet none of those behaviours establishes that a learner has acquired a capability. The conversation can improve while the learner’s independent performance remains unchanged or deteriorates.

This distinction matters because generative systems make assistance unusually cheap, immediate and persuasive. In a randomized field experiment with secondary-school mathematics students, access to an unconstrained GPT-based interface increased performance during practice but produced worse performance when the tool was removed; a pedagogically constrained interface eliminated the measured harm without establishing a positive unassisted effect ([Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122)). The result does not prove that generative assistance is generally harmful. It demonstrates that assisted performance and learning can have opposite signs, and that an evaluation which ends while assistance is present can reward the wrong system.

At the same time, dismissing model-based instruction would ignore positive results. A purpose-built physics tutor outperformed an active-learning classroom condition in a short, developer-led randomized study ([Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6)). Tutor CoPilot improved tutors’ proximal instructional outcomes, with larger gains among lower-rated tutors, while a more distal state assessment did not significantly move ([Wang et al., 2024](https://arxiv.org/abs/2410.03017)). These studies show that model assistance can be useful under particular designs. They do not establish durable, domain-general learning or a complete replacement for human instructional systems.

A more useful question is:

> What system would reliably turn model capabilities into durable, independent learner capability, for a heterogeneous population, while preserving learner control?

This article offers a design answer. Its thesis is that a personal learning system should be treated as an evidence-seeking control loop instead of a chat product. The loop begins with a goal and uncertain learner state, selects a probe or instructional action, observes what the learner does, updates competing explanations, changes representation or support, fades that support, and measures transfer after withdrawal. Speech, image, video, simulation and generated applications are renderers within that loop. Specialist agents are bounded decision-makers within it. Neither is the product by itself.

The contribution is fourfold:

1. It separates empirical findings, technical capability and product hypotheses, keeping one from standing in for another.
2. It specifies a reference architecture that connects learner evidence to instructional action across sessions and media.
3. It treats accessibility, learner-state ownership and the provenance of human instructional techniques as architectural requirements.
4. It defines an evaluation program whose primary outcome is delayed, unassisted, novel-task performance; engagement and assisted completion remain secondary measures.

The intended result is a falsifiable specification. The specified system remains unvalidated.

## 2. Scope and method

### 2.1 Review type

This design-oriented evidence synthesis makes no claim to be a systematic review or meta-analysis. It draws on a project corpus of 54 research reports assembled through iterative searches of scholarly databases, reference lists, benchmark publications, official technical documentation and product materials. The corpus covers learning outcomes, learner modelling, assessment, feedback, accessibility, multimodal interfaces, agent systems, media generation, memory, governance and educational markets. Its search history was not prospectively registered, its inclusion criteria changed as the design problem developed, and study-level risk of bias was not independently scored by two reviewers. It would therefore be misleading to apply the evidentiary authority of a systematic review.

The complete interpretive corpus is retained as a [Living Evidence Atlas](ATLAS.md), and the underlying reports remain available in [research/raw/](research/raw/). The present manuscript selects findings only when they constrain an architectural or evaluative decision. This separation prevents a literature notebook from being represented as a finished article while preserving traceability for readers who want the larger record.

### 2.2 Evidence classes

Claims are separated into four classes:

- **Measured:** an outcome observed in a study, with the population, comparison and timing retained.
- **Technical capability:** a documented function of a model, API or tool. Capability alone provides zero evidence of a learning effect.
- **Observed absence:** a gap found by a declared search. Absence is scoped to the searched sources and date.
- **Design hypothesis:** a proposed mechanism or architecture that requires prospective testing.

Vendor-reported capabilities define engineering feasibility and provide no support for learning claims. Benchmarks are used only for the task they measure. A result from a human tutoring study or a pre-generative intelligent tutoring system is not presented as a measured effect of a frontier model.

### 2.3 Selection for this manuscript

Evidence was retained in the main text when it met at least one of three criteria: it directly separated assisted performance from later independent performance; it altered a system requirement; or it specified a credible evaluation method. Domain-specific mechanisms, product catalogues and extended market material were moved to the atlas. Claims without a traceable source, marketing market-size estimates and repository activity counts were excluded.

The review cutoff for the present version is 30 July 2026. Because model products and technical interfaces change rapidly, named systems in the companion dashboard illustrate capability classes; the architecture does not depend on those products.

### 2.4 Limits of the method

The corpus is broad but heterogeneous. Some frontier-system results are preprints, developer-evaluated deployments or short interventions. Publication bias is likely. Measures, comparisons and timescales differ enough that pooling them would create false precision. The literature involving learners with disabilities is especially thin, and the project’s search for randomized generative-AI tutoring trials did not establish representative coverage of special-education populations. The proposed architecture should consequently be read as a disciplined hypothesis derived from imperfect evidence.

## 3. What the evidence constrains

### 3.1 Independent capability is the target construct

The most important boundary condition is measurement after withdrawal. Bastani and colleagues distinguish performance with AI access from performance on a subsequent unassisted examination ([Bastani et al., 2025](https://doi.org/10.1073/pnas.2422633122)). The unconstrained system produced large gains during practice and a penalty after removal. The constrained system prevented the measured penalty. This pattern is compatible with cognitive offloading: the interface can complete or simplify the very operation the learner needs to acquire.

This boundary is not unique to generative AI. Learners can misjudge the effectiveness of instruction, favouring experiences that feel fluent over those that produce more learning. In a randomized comparison, students in an active-learning classroom learned more while reporting that they had learned less than students receiving fluent lectures ([Deslauriers et al., 2019](https://doi.org/10.1073/pnas.1821936116)). Ease, confidence and satisfaction may be useful process measures, but they cannot serve as the primary objective of an adaptive system.

The architectural consequence is direct: the system must maintain separate variables for assisted task performance and demonstrated independent capability. Assistance level must be recorded with each observation. A learner who succeeds after a generated hint has produced different evidence from a learner who succeeds without access to the system.

### 3.2 Positive effects are design-specific

Short, purpose-built interventions show that generative systems can improve learning under controlled conditions. Kestin and colleagues reported higher learning gains from a carefully designed physics tutor than from an active-learning class during two lessons ([Kestin et al., 2025](https://doi.org/10.1038/s41598-025-97652-6)). The system incorporated structured pedagogy and restricted the chat interaction. Its duration, developer involvement and outcome timing limit generalization, but the study rebuts the claim that model-based instruction can only improve convenience.

Tutor CoPilot used a different allocation of labour: the model provided live support to human tutors. The randomized trial reported improved exit-ticket mastery and larger gains for students of lower-rated tutors ([Wang et al., 2024](https://arxiv.org/abs/2410.03017)). The null on a distal state assessment matters as much as the proximal gain. It suggests that improving a local instructional interaction does not automatically produce broad or durable effects.

These studies support decomposition. A model can draft, classify, retrieve, simulate, generate or coach within a larger instructional process. The resulting decision and learner outcome are the units of evaluation.

### 3.3 Prior state dominates a fixed starting point

Across 1.3 million observations from diverse learning systems, Koedinger and colleagues found much greater variation in learners’ initial knowledge than in their estimated learning rates ([Koedinger et al., 2023](https://doi.org/10.1073/pnas.2221311120)). A later reanalysis reports that the estimated learning-rate variation is sensitive to the length of the observed practice sequence, so the apparent regularity should not be treated as a universal learner property ([Lee et al., 2026](https://arxiv.org/abs/2605.01690)). The original result still argues against systems that infer ability from elapsed time and advance every learner through the same prerequisite sequence; it does not imply that all people learn identically.

The corresponding design requirement is a low-cost diagnostic entry. The system should avoid a broad test when a small discriminating task can resolve the uncertainty that matters for the next decision. It should maintain multiple candidate explanations for an error and avoid converting one action into a stable learner trait.

### 3.4 Measurement without an action policy is incomplete

Progress monitoring is valuable only when its result changes instruction. In curriculum-based measurement research, providing measurements alongside an explicit rule for revising instruction produced different effects from measurement alone ([Fuchs, Fuchs, Hamlett, & Stecker, 1991](https://doi.org/10.3102/00028312028003617)). The precise historical intervention should not be generalized uncritically to a contemporary AI system. The durable design lesson is that a learner model has to support a specified, auditable choice among actions.

For a generative system, the danger is greater because it can create an impressive response to every new datum. Adaptation must mean more than variation. A change is adaptive only if the observation supports it, the alternative actions are explicit, and the outcome can update the policy.

### 3.5 The population in the evidence is too narrow

The generative-AI tutoring literature provides little direct evidence for learners with disabilities, for learners using alternative communication modes, or for the institutional coordination surrounding an individualized education program. This does not justify assuming no benefit. It prevents average effects from being presented as universal.

An access-first architecture follows from uncertainty as well as equity. If the system confounds reading fluency with conceptual understanding, it will build the wrong learner model. If it allows speech, drawing, pointing or manipulation as alternate evidence channels, it can distinguish a subject-matter difficulty from an interface barrier. Accessibility improves identification of the construct being learned and belongs inside the evidence loop.

## 4. Reference architecture

### 4.1 The control loop

Let \(s_t\) denote the system’s uncertain representation of the learner at time \(t\), \(g\) the learner’s goal, \(a_t\) an instructional or diagnostic action, and \(o_{t+1}\) the learner’s subsequent observable action. A minimal loop is:

\[
a_t = \pi(s_t, g, c_t), \qquad
s_{t+1} = U(s_t, a_t, o_{t+1}, \ell_t)
\]

where \(c_t\) represents contextual constraints and \(\ell_t\) records the level of assistance available when the observation was produced. The policy \(\pi\) selects among actions such as probing, explaining, generating a representation, offering a hint, changing modality, fading support or scheduling retrieval. The update function \(U\) does not treat the model’s interpretation as ground truth; it revises uncertainty using the learner’s action and the conditions under which it occurred.

This formalism is intentionally modest. It does not require a psychologically complete model of the learner. It requires enough state to choose and evaluate the next action without converting uncertain inference into identity.

### 4.2 Portable learner state

The learner record has four layers:

1. **Declared state:** goals, interests, language, access preferences, consent and constraints supplied by the learner or an authorized support person.
2. **Observed events:** tasks, responses, artifacts, timing, representation, tools available and assistance level.
3. **Inferred state:** probabilistic mastery estimates, candidate misconceptions and predicted support needs, each carrying provenance and uncertainty.
4. **Outcome evidence:** later performance on unaided and transfer tasks, including evidence that contradicts earlier inferences.

Declared and observed state must not be silently overwritten by inference. Sensitive attributes should not be inferred simply because a model can produce a plausible label. The learner should be able to inspect, correct, export and delete the record. Portability reduces platform lock-in and allows a teacher, tutor, course or tool to contribute to one learning history with permission.

### 4.3 Competing diagnostic hypotheses

Open-ended judgement of a learner’s belief is unreliable when based on a single incorrect response. The system should instead enumerate a bounded set of candidate explanations derived from domain knowledge, prior learner evidence and observed error patterns. It then selects a task likely to discriminate among them.

For example, an incorrect fraction comparison might arise from treating the larger denominator as the larger fraction, comparing numerator–denominator differences, misreading a symbol, or making an arithmetic slip. A second carefully selected comparison can distinguish these explanations more effectively than a long generated diagnosis. The next instructional action is conditional on the resulting evidence.

Candidate enumeration does not solve diagnosis. The library can omit the learner’s actual reasoning, encode cultural assumptions or collapse several processes into one label. The system therefore needs an “unclassified” state, an escalation path, and regular analysis of errors that do not fit. The value lies in making the hypothesis space inspectable and testable.

### 4.4 Representation selection and generation

Frontier systems can produce text, speech, diagrams, code, notebooks, animations, video and interactive applications. A learning architecture should expose these as renderers selected by the policy, avoiding a carousel of content formats.

Each generated representation passes through four checks:

- **Semantic:** does it preserve the target concept and avoid introducing a false relationship?
- **Instructional:** does it reveal the relevant structure without performing the target operation for the learner?
- **Accessible:** can the learner perceive and control it through the required modes, including captions, text alternatives, keyboard operation and adjustable motion?
- **Operational:** does it load within the interaction budget, preserve privacy and fail safely?

Generation is justified when it changes what the learner can inspect or manipulate. A decorative animation that repeats the prose adds media cost without instructional value. A number-line manipulation that makes a mistaken ordering rule executable may expose a belief that prose did not.

The system should begin with the smallest adequate representation. It may escalate from a prompt to a worked contrast, a diagram, a manipulable object, a simulation or an immersive environment. The escalation order is empirical and learner-specific; richer media are not inherently better.

### 4.5 Pedagogical orchestration

The architecture separates specialist functions without forcing the learner to coordinate an agent organization:

- a **diagnostic function** maintains candidate explanations and chooses probes;
- a **domain function** protects correctness, prerequisite structure and authentic practice;
- a **representation function** selects and checks media;
- an **access function** manages communication modes, cognitive load and executive supports;
- an **evaluation function** constructs and scores independent evidence.

One accountable orchestrator chooses the exposed action. Specialists return bounded proposals containing a predicted learner response, the evidence supporting the proposal, relevant uncertainty and an abstention condition. Disagreement is resolved by a learner task or human review when possible; rhetorical model judgement is avoided.

Specialist agents require certification within scope. Certification should test domain competence, tool permissions, calibration, abstention, accessibility behaviour and resistance to prompt injection or contaminated learner content. Runtime monitoring should detect distribution shift and revoke a specialist that fails its declared bounds.

### 4.6 Memory and scheduling

Persistence serves two distinct functions. Instructional continuity restores the learner’s open goal and unresolved question at the next session. Learning scheduling selects when an idea should return for retrieval. Neither requires storing an unrestricted transcript forever.

Memory should preferentially retain compact evidence: the task, observed action, assistance level, accepted interpretation, uncertainty, subsequent outcome and source provenance. Raw audio, video or screen streams should be ephemeral unless the learner explicitly chooses otherwise. A scheduling layer can implement established retrieval and spacing principles while allowing the policy to update from actual recall.

### 4.7 Fading and graduation

Every support has a withdrawal rule. The system records the strongest support used and then creates an opportunity to perform with less support. Graduation from a concept requires a novel task, completed without target-relevant assistance, after a delay appropriate to the domain.

Teaching a deliberately stubborn simulated peer can be a useful elicitation task because it makes explanation observable. This alone provides no proof of mastery. The simulated peer must raise domain-relevant objections, and success must still predict performance on an independent task.

## 5. Access, governance and the human ecosystem

### 5.1 Access preferences as state

Universal Design for Learning motivates multiple means of engagement, representation, and action and expression ([CAST, 2024](https://udlguidelines.cast.org/)). In the proposed architecture, these options are not generic toggles applied after content generation. They are persistent learner preferences and contextual needs available to the selection policy.

A learner may listen to a problem while responding through drawing; another may need stable visual structure and reduced motion; another may prefer text but require optional decoding support. The architecture distinguishes a change in interface from a change in the construct assessed. If oral reading is the target, speech synthesis would invalidate the observation. If proportional reasoning is the target, requiring unsupported decoding may contaminate it.

### 5.2 Human authority and coordination

The system does not diagnose disability, prescribe clinical treatment or replace the legal and professional roles surrounding special education. It can produce compact, attributable evidence for an authorized teacher, tutor, parent or coordinator: what task was attempted, what support was present, what happened, what interpretation is proposed and how confident the system is.

Humans should be able to constrain goals, representations, data sharing and escalation. A system recommendation that affects placement, accommodation or high-stakes assessment requires human review and an appeal path. The purpose of persistence is continuity, not surveillance.

### 5.3 Authors, educators and creators

Generated content can detach instructional techniques from the people who developed them. The architecture instead proposes a technique interchange. A contribution contains:

- the concept and learner state for which the technique is intended;
- the instructional move and its rationale;
- contraindications or known failure modes;
- source and authorship provenance;
- compatible representations;
- evidence, if any, about outcomes;
- terms for attribution, revision and compensation.

The system can then select a technique for a reason, preserve its origin, measure its outcome and return evidence to its contributor. Publishers and course providers can distribute concept packages without surrendering learner-state ownership. This arrangement treats human expertise as an upstream asset instead of raw material for anonymous generation.

### 5.4 Privacy and security

Educational interaction can expose sensitive information through voice, video, handwriting, location, performance and family context. Data minimization should be the default: process live streams ephemerally where possible, retain derived events only when needed, and separate identity from research records. Tool-using agents receive least-privilege access. External content is treated as untrusted input. Learners can see when sensing is active and what is retained.

Legal compliance depends on deployment context and jurisdiction and is not resolved by architecture alone. The system nonetheless supports compliance by making consent, provenance, retention, access and deletion explicit instead of burying them in conversational logs.

## 6. Evaluation program

### 6.1 Primary question

The first integrated trial should ask:

> Does the persistent, multimodal control loop improve delayed, unassisted performance on novel tasks compared with access to a strong general-purpose model, without widening outcome gaps?

A weak worksheet, no-treatment or obsolete tutoring control would not answer whether the architecture adds value over the tool learners can already use.

### 6.2 Trial design

The initial domain should be bounded, externally scored and valuable to the learner. One plausible product wedge is mathematics preparation for a dated standardized assessment, but that is a commercialization choice distinct from a scientific requirement.

At minimum, the trial includes:

- random assignment within relevant strata;
- equal access to source content and practice time;
- a strong general-model comparison condition;
- pre-registration of outcomes, exclusions and subgroup analyses;
- an item bank held or audited independently of the product team;
- immediate assisted process measures;
- a delayed assessment with system access removed;
- novel items that test transfer beyond memorized surface forms;
- analysis by baseline attainment and declared access needs;
- explicit reporting of attrition and intervention fidelity.

The primary effect is the between-group difference on delayed, unassisted novel tasks. Secondary outcomes include retention, transfer distance, time to criterion, calibration, learner agency, human support time, adverse events and gap change. Satisfaction and engagement are reported as experience measures.

### 6.3 Component experiments

Before or alongside the integrated trial, smaller experiments should test load-bearing decisions:

1. **Diagnostic selection:** compare a discriminating-probe policy with open-ended model diagnosis and with a non-adaptive task sequence.
2. **Representation policy:** compare evidence-selected media with learner-selected and fixed representations, including accessibility outcomes.
3. **Fading:** compare explicit withdrawal schedules with unrestricted assistance and hint-only constraints.
4. **Persistence:** compare cross-session evidence state with transcript summaries and session-local instruction.
5. **Specialist orchestration:** compare bounded specialist proposals with a single general model under matched tool access.
6. **Technique interchange:** test whether attributable creator-supplied techniques outperform generated defaults and whether outcome feedback improves subsequent selection.

Component success does not establish system success. Interactions among components can erase isolated gains, increase cognitive load or create new failure modes.

### 6.4 Safety and stopping rules

The trial should pre-specify stopping or review thresholds for factual error, harmful content, privacy breach, widening subgroup gaps and evidence of dependence. The system must make assistance visible to evaluators. Any claim of benefit should report both the average and distribution, including learners for whom the system did not work.

### 6.5 What would falsify the thesis

The architecture would lose its justification if a strong general model with simple persistence performs equivalently on delayed transfer; if representation adaptation adds complexity without outcome benefit; if the diagnostic layer cannot outperform cheaper task sequencing; if access-first design does not improve construct validity or reach; or if the human technique interchange fails to attract contributors or improve outcomes. These are product and research risks, not details to defer until after deployment.

## 7. Discussion

The reference architecture changes the object being built. The familiar AI tutor is a conversational actor. The proposed system is a policy over evidence, people, models, tools, representations and time. Conversation may be its most common surface, but the learner can also interact through a camera, shared canvas, notebook, simulation or generated application. The surface changes because the policy predicts that a different action will help resolve a particular uncertainty.

This framing avoids two excesses. The first is model solutionism: the belief that a more capable base model will automatically produce better learning. Stronger models improve available actions, but they do not choose the learning objective, distinguish assistance from acquisition, determine when to withdraw, or establish consent. The second is pedagogical decoration: attaching named teaching techniques to a chatbot without measuring whether they change later capability. A technique belongs in the system only when its triggering conditions and expected evidence can be stated.

The architecture also reframes agentic learning. Multiple agents do not create a faculty merely by adopting role names. A faculty requires bounded competence, shared but governed state, accountable orchestration and a way to resolve disagreement through external evidence. The test of an agent is not the persuasiveness of its explanation but whether its action improves a declared outcome within scope.

The design has important limitations. Learner models can harden transient behaviour into labels. Generated representations can be semantically wrong while appearing polished. Persistent systems can become surveillance systems. Adaptation can narrow experience around what is easiest to measure. An outcome-oriented product can overfit to a standardized assessment. Human expertise can be extracted without credit. Each risk corresponds to an architectural countermeasure described above, but none is eliminated by specification.

There is also a boundary to personalization. Education is social, cultural and civic, not merely an optimization of individual knowledge state. Peers, teachers and communities supply norms, care, identity, contestation and shared purpose that a personal system should not simulate away. The architecture is best understood as infrastructure for personal instruction and coordination, not a complete theory of education.

## 8. Conclusion

The frontier capability is real: models can attend to multimodal interaction, generate representations, use tools and persist through agent runtimes. The learning effect of assembling those components is not yet established. Evidence supports carefully designed model assistance and warns against equating fluent help with acquired capability.

A credible personal learning system should therefore close a specific loop. It observes an action under known assistance conditions, maintains uncertainty, selects a discriminating or instructional next move, changes medium when warranted, fades support, returns after a delay and asks the learner to act independently on something new. It preserves access preferences and learner control of state. It treats authors and educators as attributable contributors. It submits its central claim to a strong baseline and an external outcome.

The ambition is broad access to excellent personal instruction. The scientific claim is narrower: an evidence-seeking, persistent and multimodal control loop may produce more durable independent capability than an excellent general model used as a conversational assistant. That claim is important enough to build—and precise enough to fail.

## Declarations

**Funding:** No funding statement has been supplied.

**Competing interests:** No competing-interest statement has been supplied.

**Ethics:** This manuscript reports no new study involving human participants. Any future trial described here requires appropriate ethics review, consent or assent, data-governance review and jurisdiction-specific compliance.

**Data and materials:** The evidence corpus, demos, build scripts and append-only corrections ledger are available in this repository. The corpus is a research record, not a redistributable archive of source publications.

**Use of generative AI:** The repository concerns and uses generative AI. Accountable human authors must review every claim, source and disclosure before submission.

**Author contributions:** To be supplied when authorship is named.

## References

Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences, 122*(26), e2422633122. <https://doi.org/10.1073/pnas.2422633122>

CAST. (2024). *Universal Design for Learning Guidelines version 3.0*. <https://udlguidelines.cast.org/>

Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). Measuring actual learning versus feeling of learning in response to being actively engaged in the classroom. *Proceedings of the National Academy of Sciences, 116*(39), 19251–19257. <https://doi.org/10.1073/pnas.1821936116>

Fuchs, L. S., Fuchs, D., Hamlett, C. L., & Stecker, P. M. (1991). Effects of curriculum-based measurement and consultation on teacher planning and student achievement in mathematics operations. *American Educational Research Journal, 28*(3), 617–641. <https://doi.org/10.3102/00028312028003617>

Kestin, G., Miller, K., Klales, A., Milbourne, T., & Ponti, G. (2025). AI tutoring outperforms in-class active learning: An RCT introducing a novel research-based design in an authentic educational setting. *Scientific Reports, 15*, 17458. <https://doi.org/10.1038/s41598-025-97652-6>

Koedinger, K. R., Carvalho, P. F., Liu, R., & McLaughlin, E. A. (2023). An astonishing regularity in student learning rate. *Proceedings of the National Academy of Sciences, 120*(13). <https://doi.org/10.1073/pnas.2221311120>

Lee, H., Lichand, G., Barnard, C., Klotz, L., Thille, C., Kim, Y., & Domingue, B. W. (2026). The “astonishing regularity” revisited: Sensitivity of learning-rate estimates to practice-sequence length. *arXiv*. <https://arxiv.org/abs/2605.01690>

VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist, 46*(4), 197–221. <https://doi.org/10.1080/00461520.2011.611369>

Wang, R. E., Ribeiro, A. T., Robinson, C. D., Loeb, S., & Demszky, D. (2024). Tutor CoPilot: A human–AI approach for scaling real-time expertise. *arXiv*. <https://arxiv.org/abs/2410.03017>

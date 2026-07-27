const learners = {
  amina: {
    name: "Amina",
    initials: "AM",
    goal: "connect fractions to algebra",
    next: "Concrete worked example",
    reason: "Because symbolic transfer is uncertain while visual partitioning is stable.",
    skills: [
      ["Visual partitioning", 88],
      ["Equivalent fractions", 71],
      ["Symbolic transfer", 43],
      ["Explain reasoning", 64],
    ],
  },
  leo: {
    name: "Leo",
    initials: "LE",
    goal: "debug a transistor circuit",
    next: "Camera-guided circuit trace",
    reason: "Because the calculation is sound but the observed voltage path is inconsistent.",
    skills: [
      ["Ohm’s law", 91],
      ["Circuit diagrams", 77],
      ["Transistor biasing", 46],
      ["Measurement practice", 68],
    ],
  },
  mei: {
    name: "Mei",
    initials: "ME",
    goal: "defend a scientific claim",
    next: "Evidence-to-claim teach-back",
    reason: "Because source selection is strong while causal explanation needs another pass.",
    skills: [
      ["Source evaluation", 84],
      ["Claim structure", 76],
      ["Causal reasoning", 49],
      ["Scientific revision", 72],
    ],
  },
};

const explanations = {
  intuitive: {
    title: "Intuitive · see the relationship",
    body: "Three of four equal market baskets are filled. The fraction ¾ names both the partition and how many parts we have.",
  },
  concrete: {
    title: "Concrete · manipulate an example",
    body: "Split 12 counters into four equal groups. Select three groups. You selected 9 of 12 counters, so ¾ = 9⁄12.",
  },
  formal: {
    title: "Formal · preserve the invariant",
    body: "For b ≠ 0, a⁄b and ka⁄kb represent the same rational number for every nonzero k because multiplication by k⁄k equals one.",
  },
  transfer: {
    title: "Transfer · use it somewhere new",
    body: "A recipe needs ¾ of 20 ml. Without drawing the original model, explain why dividing by four and multiplying by three is valid.",
  },
};

const capabilities = [
  {
    id: "conductor",
    group: "Control plane",
    title: "Mentor conductor",
    summary: "Select the next teaching action from current evidence, uncertainty, and constraints—and make the reason visible.",
    evidence: "Build frontier",
    metrics: [["Action", "worked example"], ["Decision", "42 ms"], ["Confidence", "0.84"], ["Fallback", "guided hint"]],
    logs: [
      "Read permitted LearnerState: symbolic transfer remains uncertain.",
      "Compared explain, retrieve, hint, and worked-example policies.",
      "Selected worked example; expected signal: independent explanation.",
      "Scheduled a transfer probe after the learner acts.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">Explicit control loop</span>
          <h3>Why this action, now?</h3>
          <p>The conductor chooses pedagogy before it chooses words or media.</p>
          <div class="decision-path">
            <div class="decision-node"><b>Goal</b><small>connect fractions → algebra</small></div>
            <div class="decision-node"><b>Evidence</b><small>visual stable · symbols uncertain</small></div>
            <div class="decision-node"><b>Action</b><small>worked example → teach-back</small></div>
            <div class="decision-node"><b>Signal</b><small>solve without the model</small></div>
          </div>
          <div class="contract-code">TeachingAction {
  mode: "worked_example",
  reason: "bridge stable visual knowledge to symbols",
  learner_action: "explain each transformation",
  success_signal: "independent transfer",
  fallback: "concrete manipulable"
}</div>
        </article>
        <article class="demo-panel span-5 soft-teal">
          <span class="demo-label">Candidate policies</span>
          <h3>Router comparison</h3>
          <div class="choice-list">
            <button class="choice active" type="button" data-choice><span class="choice-icon">01</span><span><b>Worked example</b><small>bridge to symbols</small></span><span>84%</span></button>
            <button class="choice" type="button" data-choice><span class="choice-icon">02</span><span><b>Retrieval prompt</b><small>test prior memory</small></span><span>68%</span></button>
            <button class="choice" type="button" data-choice><span class="choice-icon">03</span><span><b>Direct explanation</b><small>fast but passive</small></span><span>51%</span></button>
            <button class="choice" type="button" data-choice><span class="choice-icon">04</span><span><b>Human pairing</b><small>available at hub</small></span><span>45%</span></button>
          </div>
        </article>
      </div>`,
  },
  {
    id: "live",
    group: "Perception",
    title: "Live multimodal mentor",
    summary: "Listen, see, interrupt, point, annotate, and change modality without restarting the learning relationship.",
    evidence: "Broadly shipped",
    metrics: [["Turn latency", "310 ms"], ["Speech", "0.93"], ["Vision", "page + hand"], ["Mode", "full duplex"]],
    logs: [
      "Opened a temporary audio/vision observation window.",
      "Detected the learner pointing to the denominator; speech confidence 0.93.",
      "Paused immediately on interruption and preserved the unfinished explanation.",
      "Converted the next turn to a manipulable visual in the learner’s language.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel dark span-5">
          <span class="demo-label">Full-duplex channel</span>
          <h3>Listening in ${ctx.language}</h3>
          <p>Temporary sensory context expires after the turn unless the learner saves it.</p>
          <div class="waveform" aria-label="Animated voice waveform">
            ${"<i></i>".repeat(17)}
          </div>
          <div class="sensor-row">
            <span class="sensor on">● voice</span><span class="sensor on">● page</span><span class="sensor on">● gesture</span><span class="sensor">○ screen</span>
          </div>
        </article>
        <article class="demo-panel span-7">
          <span class="demo-label">Interruptible conversation</span>
          <h3>See the work, not only the prompt</h3>
          <div class="live-transcript">
            <div class="bubble">I know three parts are shaded, but why does the bottom number stay four?</div>
            <div class="bubble mentor">The four names how many equal parts make the whole. Point to one whole for me.</div>
            <div class="bubble">Wait—can I move the pieces instead?</div>
            <div class="bubble mentor">Yes. I paused the explanation and opened the manipulable.</div>
          </div>
          <div class="tool-row">
            <button class="tool-chip on" type="button" data-toggle aria-pressed="true">interrupt</button>
            <button class="tool-chip" type="button" data-toggle aria-pressed="false">caption</button>
            <button class="tool-chip" type="button" data-toggle aria-pressed="false">AAC choices</button>
            <button class="tool-chip on" type="button" data-toggle aria-pressed="true">ephemeral media</button>
          </div>
        </article>
      </div>`,
  },
  {
    id: "mesh",
    group: "Expertise",
    title: "Expert mentor mesh",
    summary: "Route each subproblem to role-certified specialists by evidence, language, privacy, latency, cost, and device tier.",
    evidence: "Emerging",
    metrics: [["Specialists", "4 active"], ["Agreement", "0.91"], ["Local roles", "2"], ["Cloud calls", "1"]],
    logs: [
      "Decomposed the turn into pedagogy, mathematics, language, and verification roles.",
      "Kept language and accessibility processing on the community hub.",
      "Called one regional proof checker with a minimum-necessary payload.",
      "Compared specialist outputs and returned one coherent mentor turn.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">Role certification</span>
          <h3>A faculty behind one mentor voice</h3>
          <div class="expert-list">
            ${[
              ["P", "Pedagogy router", "adaptive sequencing", 96],
              ["∑", "Math specialist", "rational-number invariants", 93],
              ["文", `${ctx.language} specialist`, "meaning + terminology", 89],
              ["✓", "Verification agent", "independent check", 91],
              ["A", "Access specialist", "modality composition", 86],
            ].map(([icon, name, role, score]) => `
              <div class="expert"><span class="expert-icon">${icon}</span><span><b>${name}</b><small>${role}</small></span><span class="score-bar"><i style="width:${score}%"></i></span></div>
            `).join("")}
          </div>
        </article>
        <article class="demo-panel span-5 soft-blue">
          <span class="demo-label">Selection constraints</span>
          <h3>Best role fit, not biggest model</h3>
          <div class="contract-code">MentorTool {
  role: "fraction_invariant_check",
  tier: "${ctx.network}",
  data_scope: ["ConceptSpec", "candidate"],
  max_latency_ms: 900,
  consequence: "learning_only",
  certification: 0.93
}</div>
          <div class="tag-row"><span class="tag on">privacy fit</span><span class="tag on">latency fit</span><span class="tag on">role evidence</span><span class="tag">premium model</span></div>
        </article>
      </div>`,
  },
  {
    id: "compiler",
    group: "Knowledge",
    title: "Verified knowledge compiler",
    summary: "Compile trusted sources into one ConceptSpec, then generate every explanation, diagram, simulation, and assessment from shared truth.",
    evidence: "Build frontier",
    metrics: [["Sources", "6 grounded"], ["Invariants", "4 / 4"], ["Representations", "5"], ["Checks", "passed"]],
    logs: [
      "Resolved six source claims into one explicit ConceptSpec.",
      "Locked four invariants shared by text, visual, simulation, and assessment.",
      "Generated learner-specific representations from the same specification.",
      "Passed truth, render, accessibility, and provenance checks.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-12">
          <span class="demo-label">Executable knowledge pipeline</span>
          <h3>Generate from a contract, not a blank prompt</h3>
          <div class="pipeline">
            <div class="pipeline-step"><b>Sources</b><small>authority + scope</small></div>
            <div class="pipeline-step"><b>Claims</b><small>resolve conflict</small></div>
            <div class="pipeline-step"><b>ConceptSpec</b><small>invariants + tests</small></div>
            <div class="pipeline-step"><b>Represent</b><small>text · visual · sim</small></div>
            <div class="pipeline-step"><b>Verify</b><small>truth · render · access</small></div>
            <div class="pipeline-step"><b>Evidence</b><small>learner action</small></div>
          </div>
        </article>
        <article class="demo-panel span-6 dark">
          <span class="demo-label">ConceptSpec · rational equivalence</span>
          <div class="contract-code">invariants:
  - denominator ≠ 0
  - equal scaling preserves value
  - partitions are equal-sized
misconceptions:
  - "larger denominator means larger value"
tests:
  - symbolic equivalence
  - visual area conservation
  - novel-context transfer</div>
        </article>
        <article class="demo-panel span-6 soft-teal">
          <span class="demo-label">Compiled representation</span>
          <div class="concept-visual">
            <div class="fraction-model"><i class="filled"></i><i class="filled"></i><i class="filled"></i><i></i></div>
            <span class="concept-equation">¾ = 9⁄12</span>
          </div>
        </article>
      </div>`,
  },
  {
    id: "state",
    group: "Memory",
    title: "Learner-owned state",
    summary: "Keep uncertain mastery, goals, evidence, access preferences, consent, and corrections portable across models and institutions.",
    evidence: "Build frontier",
    metrics: [["Claims", "12"], ["Corrections", "2"], ["Owner", "learner"], ["Portability", "JSON-LD"]],
    logs: [
      "Read only the evidence pointers permitted for this teaching turn.",
      "Updated one mastery hypothesis; preserved the competing explanation.",
      "Applied a learner correction to preferred terminology.",
      "Prepared a portable state delta independent of the current model vendor.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">Uncertainty, not a permanent label</span>
          <h3>${ctx.learner.name} can inspect and correct every claim</h3>
          <div class="expert-list">
            ${ctx.learner.skills.map(([name, score]) => `
              <div class="expert"><span class="expert-icon">${score >= 70 ? "✓" : "?"}</span><span><b>${name}</b><small>${score >= 70 ? "supported by multiple tasks" : "needs a fresh probe"}</small></span><span class="score-bar"><i style="width:${score}%"></i></span></div>
            `).join("")}
          </div>
        </article>
        <article class="demo-panel span-5 dark">
          <span class="demo-label">Portable LearnerState</span>
          <div class="contract-code">{
  "owner": "${ctx.learner.name}",
  "goal": "${ctx.learner.goal}",
  "language": "${ctx.language}",
  "mastery": {"symbolic_transfer": {
    "estimate": 0.43,
    "uncertainty": 0.18,
    "evidence": ["ev-018", "ev-021"]
  }},
  "permissions": ["learning", "local_sync"],
  "expires": {"sensory_context": "now"}
}</div>
        </article>
      </div>`,
  },
  {
    id: "textbook",
    group: "Learning objects",
    title: "AI-native textbook",
    summary: "Compile the next micro-chapter around the learner’s goal, sources, state, preferred modality, and demonstrated evidence.",
    evidence: "Emerging",
    metrics: [["Edition", "learner 014"], ["Reading time", "7 min"], ["Objects", "4"], ["Next edition", "after probe"]],
    logs: [
      "Mapped the learner goal to the verified concept dependency graph.",
      "Selected one explanation, one worked example, and one manipulable.",
      "Removed material already supported by current evidence.",
      "Bound the next edition to the learner’s teach-back response.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel span-8">
          <span class="demo-label">Compiled micro-chapter · edition 014</span>
          <h3>From equal parts to equivalent expressions</h3>
          <p>Built for ${ctx.learner.name} in ${ctx.language}; resumes from stable visual partitioning.</p>
          <div class="pipeline">
            <div class="pipeline-step"><b>See</b><small>¾ partition</small></div>
            <div class="pipeline-step"><b>Build</b><small>scale pieces</small></div>
            <div class="pipeline-step"><b>Formalize</b><small>× k⁄k</small></div>
            <div class="pipeline-step"><b>Explain</b><small>teach it back</small></div>
            <div class="pipeline-step"><b>Transfer</b><small>new context</small></div>
          </div>
          <div class="concept-visual">
            <div class="fraction-model"><i class="filled"></i><i class="filled"></i><i class="filled"></i><i></i></div>
            <span class="concept-equation">Next: why ¾ = 6⁄8</span>
          </div>
        </article>
        <article class="demo-panel span-4 soft-amber">
          <span class="demo-label">Edition recipe</span>
          <h3>Only what helps now</h3>
          <div class="check-list">
            <div class="check-row"><span>✓</span><span><b>Skip definition review</b><small>already stable</small></span><span></span></div>
            <div class="check-row"><span>✓</span><span><b>Keep manipulable</b><small>strong access path</small></span><span></span></div>
            <div class="check-row"><span>✓</span><span><b>Add symbolic bridge</b><small>current uncertainty</small></span><span></span></div>
            <div class="check-row"><span>○</span><span><b>Defer word problems</b><small>after teach-back</small></span><span></span></div>
          </div>
        </article>
      </div>`,
  },
  {
    id: "notebook",
    group: "Interactive objects",
    title: "Reactive learning document",
    summary: "Turn explanations into semantic dependency graphs where changing one quantity updates the visual, equation, narration, and probe.",
    evidence: "Emerging",
    metrics: [["Variables", "3 linked"], ["Dependencies", "8"], ["Recompute", "instant"], ["Probe", "adaptive"]],
    logs: [
      "Changed launch velocity from 12 to 16 m/s.",
      "Recomputed trajectory, peak, flight time, and narration from shared variables.",
      "Detected a prediction mismatch before revealing the new result.",
      "Generated a contrast case around the learner’s misconception.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-8 soft-blue">
          <span class="demo-label">Executable notebook · projectile motion</span>
          <h3>Predict, change, observe, explain</h3>
          <div class="notebook-canvas">
            <div class="trajectory" id="trajectory"></div>
            <div class="trajectory-dot"></div>
            <span class="axis-label y">height</span><span class="axis-label x">distance</span>
          </div>
          <div class="range-wrap">
            <label for="velocityRange"><span>Launch velocity</span><b><output id="velocityOutput">12</output> m/s</b></label>
            <input id="velocityRange" type="range" min="6" max="20" value="12" data-range="velocity">
          </div>
        </article>
        <article class="demo-panel span-4">
          <span class="demo-label">Linked outputs</span>
          <div class="choice-list">
            <div class="choice active"><span class="choice-icon">h</span><span><b>Peak height</b><small id="heightOutput">3.7 m</small></span><span>live</span></div>
            <div class="choice"><span class="choice-icon">t</span><span><b>Flight time</b><small id="timeOutput">1.7 s</small></span><span>live</span></div>
            <div class="choice"><span class="choice-icon">?</span><span><b>Adaptive probe</b><small>What stays unchanged?</small></span><span>next</span></div>
          </div>
        </article>
      </div>`,
  },
  {
    id: "visuals",
    group: "Verified generation",
    title: "Verified visual generator",
    summary: "Generate learner-specific diagrams only through truth, render, accessibility, and provenance checks—with targeted repair.",
    evidence: "Emerging",
    metrics: [["Truth checks", "8 / 8"], ["Render checks", "6 / 6"], ["Access checks", "4 / 4"], ["Repairs", "1 targeted"]],
    logs: [
      "Generated a fraction representation from the locked ConceptSpec.",
      "Caught a low-contrast label in the accessibility check.",
      "Repaired only the label treatment; preserved geometry and meaning.",
      "Attached source, model, prompt, checks, and repair provenance.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-7 soft-teal">
          <span class="demo-label">Generated object</span>
          <div class="concept-visual">
            <div class="fraction-model"><i class="filled"></i><i class="filled"></i><i class="filled"></i><i></i></div>
            <span class="concept-equation">3 equal parts of 4</span>
          </div>
          <div class="tag-row"><span class="tag on">same-size parts</span><span class="tag on">count matches</span><span class="tag on">alt text</span><span class="tag on">source attached</span></div>
        </article>
        <article class="demo-panel span-5">
          <span class="demo-label">Verification pipeline</span>
          <h3>Correctness before vividness</h3>
          <div class="check-list">
            <button class="check-row" type="button" data-check><span>✓</span><span><b>Truth</b><small>all invariants preserved</small></span><span>pass</span></button>
            <button class="check-row" type="button" data-check><span>✓</span><span><b>Render</b><small>no overlap or clipping</small></span><span>pass</span></button>
            <button class="check-row" type="button" data-check><span>↺</span><span><b>Accessibility</b><small>contrast repaired</small></span><span>fixed</span></button>
            <button class="check-row" type="button" data-check><span>✓</span><span><b>Provenance</b><small>generation record attached</small></span><span>pass</span></button>
          </div>
        </article>
      </div>`,
  },
  {
    id: "assessment",
    group: "Evidence",
    title: "Assessment evidence engine",
    summary: "Measure the claim you actually need—from activity through delayed independent transfer—and feed evidence into the next teaching action.",
    evidence: "Measured + frontier",
    metrics: [["Current level", "performance"], ["Support", "one hint"], ["Evaluator", "hybrid"], ["Transfer", "day 7"]],
    logs: [
      "Defined the claim: independently recognize and generate equivalent fractions.",
      "Recorded the response, support used, evaluator, and uncertainty.",
      "Separated immediate performance from durable learning evidence.",
      "Scheduled a novel-context transfer task for day seven.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-6">
          <span class="demo-label">Assurance ladder</span>
          <h3>Do not confuse activity with learning</h3>
          <div class="assurance-ladder">
            ${[
              ["L0", "Activity", "opened · clicked", ""],
              ["L1", "Response", "answered", ""],
              ["L2", "Explanation", "reasoned", ""],
              ["L3", "Performance", "solved with one hint", "active"],
              ["L4", "Transfer", "new context · day 7", ""],
              ["L5", "Portfolio", "learner-owned evidence", ""],
            ].map(([n, label, detail, active]) => `<div class="assurance-rung ${active}"><span>${n}</span><b>${label}</b><small>${detail}</small></div>`).join("")}
          </div>
        </article>
        <article class="demo-panel span-6 soft-amber">
          <span class="demo-label">LearningEvidence</span>
          <div class="contract-code">claim: "generate equivalent fractions"
task: "show two forms of ¾"
response: "¾ = 6⁄8 because both scale by 2"
support: ["one metacognitive hint"]
evaluator: ["rule_check", "mentor_review"]
uncertainty: 0.08
next: "novel-context transfer · day 7"
disclosure: "learner + teacher"</div>
          <div class="tool-row"><button class="tool-chip on" type="button" data-toggle aria-pressed="true">process</button><button class="tool-chip on" type="button" data-toggle aria-pressed="true">capability</button><button class="tool-chip" type="button" data-toggle aria-pressed="false">credential</button></div>
        </article>
      </div>`,
  },
  {
    id: "depth",
    group: "Adaptation",
    title: "One concept, four depths",
    summary: "Change sophistication without changing truth: intuitive, concrete, formal, and transfer representations share one invariant thread.",
    evidence: "Build frontier",
    metrics: [["Concept", "equivalence"], ["Depth", "concrete"], ["Invariant drift", "0"], ["Language", "adaptive"]],
    logs: [
      "Read the same ConceptSpec at four sophistication levels.",
      "Selected concrete depth from current evidence and learner preference.",
      "Verified that each representation preserved equal scaling and equal partitions.",
      "Prepared a transfer task rather than repeating the explanation.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-12">
          <span class="demo-label">Invariant-preserving explanation ladder</span>
          <h3>The learner can climb without changing concepts</h3>
          <div class="depth-tabs">
            ${Object.keys(explanations).map((key) => `<button class="depth-tab ${key === "concrete" ? "active" : ""}" type="button" data-depth="${key}">${key}</button>`).join("")}
          </div>
          <div class="explanation-card" id="explanationCard">
            <b>${explanations.concrete.title}</b><p>${explanations.concrete.body}</p>
          </div>
          <div class="tag-row"><span class="tag on">equal partitions</span><span class="tag on">same value</span><span class="tag on">scaling by k⁄k</span><span class="tag on">learner must act</span></div>
        </article>
      </div>`,
  },
  {
    id: "memory",
    group: "Longitudinal",
    title: "Memory that compounds",
    summary: "Encode through action, retrieve with spacing, repair misconceptions, vary contexts, and connect evidence across years.",
    evidence: "Measured + emerging",
    metrics: [["Next retrieval", "2 days"], ["Strength", "0.71"], ["Contexts", "3"], ["Correction", "preserved"]],
    logs: [
      "Encoded the concept through explanation and construction, not exposure alone.",
      "Scheduled retrieval from the learner’s evidence and uncertainty.",
      "Varied the next context from visual partitions to recipe quantities.",
      "Connected the corrected idea to ratio and algebra dependencies.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">Adaptive retrieval schedule</span>
          <h3>Remember by reconstructing</h3>
          <div class="memory-events">
            <div class="memory-event done"><span class="day">NOW</span><span><b>Teach it back</b><small>explain why scaling preserves value</small></span><span>✓</span></div>
            <div class="memory-event done"><span class="day">+1D</span><span><b>Retrieve</b><small>no diagram · one prompt</small></span><span>✓</span></div>
            <div class="memory-event future"><span class="day">+3D</span><span><b>Vary</b><small>recipe and measurement context</small></span><span>queued</span></div>
            <div class="memory-event future"><span class="day">+7D</span><span><b>Transfer</b><small>unfamiliar ratio problem</small></span><span>queued</span></div>
            <div class="memory-event future"><span class="day">+21D</span><span><b>Connect</b><small>bridge to algebraic proportion</small></span><span>future</span></div>
          </div>
        </article>
        <article class="demo-panel span-5 soft-teal">
          <span class="demo-label">Memory strength</span>
          <h3>Evidence, not transcript hoarding</h3>
          <div class="range-wrap">
            <label for="memoryRange"><span>Retrieval success</span><b><output id="memoryOutput">71</output>%</b></label>
            <input id="memoryRange" type="range" min="20" max="100" value="71" data-range="memory">
          </div>
          <div class="contract-code">store:
  claim + evidence pointer
  uncertainty + correction
  successful teaching action
expire:
  raw audio · raw video
  temporary emotion inference</div>
        </article>
      </div>`,
  },
  {
    id: "persistence",
    group: "Motivation",
    title: "Compassionate persistence",
    summary: "Turn difficulty into purpose, visible progress, belonging, and a shame-free path back to meaningful action.",
    evidence: "Learning science",
    metrics: [["Momentum", "recovering"], ["Challenge", "productive"], ["Return cost", "low"], ["Belonging", "protected"]],
    logs: [
      "Detected repeated hesitation without assigning a permanent motivation label.",
      "Preserved the meaningful goal and reduced only the next action size.",
      "Made progress visible without turning learning into points accumulation.",
      "Offered a shame-free return and one human connection option.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-12 soft-amber">
          <span class="demo-label">Persistence control loop</span>
          <h3>Keep the purpose; change the path</h3>
          <div class="persistence-loop">
            <button class="persistence-step active" type="button" data-choice><b>Purpose</b><small>repair a real circuit</small></button>
            <button class="persistence-step" type="button" data-choice><b>Action</b><small>one measurable step</small></button>
            <button class="persistence-step" type="button" data-choice><b>Challenge</b><small>hard, still reachable</small></button>
            <button class="persistence-step" type="button" data-choice><b>Progress</b><small>show what changed</small></button>
            <button class="persistence-step" type="button" data-choice><b>Return</b><small>resume without shame</small></button>
          </div>
        </article>
        <article class="demo-panel span-7">
          <span class="demo-label">Mentor response</span>
          <div class="live-transcript">
            <div class="bubble">I’ve tried this three times. I’m just bad at circuits.</div>
            <div class="bubble mentor">The measurements you took are good. One connection is still ambiguous. Let’s test only that branch.</div>
          </div>
        </article>
        <article class="demo-panel span-5">
          <span class="demo-label">Path options</span>
          <div class="tool-row"><button class="tool-chip on" type="button" data-toggle aria-pressed="true">smaller step</button><button class="tool-chip" type="button" data-toggle aria-pressed="false">different modality</button><button class="tool-chip" type="button" data-toggle aria-pressed="false">peer join</button></div>
        </article>
      </div>`,
  },
  {
    id: "teachbuild",
    group: "Agency",
    title: "Teach, build, collaborate",
    summary: "Make learners author explanations, artifacts, defenses, revisions, and transfers so creation becomes evidence of understanding.",
    evidence: "Measured + design",
    metrics: [["Artifact", "fraction lesson"], ["Peer questions", "2"], ["Revisions", "1"], ["Evidence", "authored"]],
    logs: [
      "Asked the learner to build a representation rather than select an answer.",
      "Generated two peer questions targeting the artifact’s weakest claim.",
      "Recorded the learner’s defense and revision as process evidence.",
      "Transferred the authored explanation to a new example.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-12">
          <span class="demo-label">Learner-authored evidence loop</span>
          <h3>Create → teach → defend → revise → transfer</h3>
          <div class="pipeline">
            <div class="pipeline-step"><b>Create</b><small>build a fraction model</small></div>
            <div class="pipeline-step"><b>Teach</b><small>explain each choice</small></div>
            <div class="pipeline-step"><b>Defend</b><small>answer peer questions</small></div>
            <div class="pipeline-step"><b>Revise</b><small>repair one ambiguity</small></div>
            <div class="pipeline-step"><b>Transfer</b><small>teach a new example</small></div>
          </div>
        </article>
        <article class="demo-panel span-6 soft-teal">
          <span class="demo-label">Learner artifact</span>
          <div class="concept-visual">
            <div class="fraction-model"><i class="filled"></i><i class="filled"></i><i class="filled"></i><i></i></div>
            <span class="concept-equation">“Same whole, same value”</span>
          </div>
        </article>
        <article class="demo-panel span-6">
          <span class="demo-label">Peer review</span>
          <div class="choice-list">
            <button class="choice" type="button" data-choice><span class="choice-icon">Q1</span><span><b>What if the pieces are unequal?</b><small>tests the partition invariant</small></span><span>answer</span></button>
            <button class="choice" type="button" data-choice><span class="choice-icon">Q2</span><span><b>Why can both numbers scale?</b><small>tests the formal bridge</small></span><span>answer</span></button>
          </div>
        </article>
      </div>`,
  },
  {
    id: "worlds",
    group: "Simulation",
    title: "Worlds you can question",
    summary: "Generate explorable worlds only when executable laws, grounded sources, and real observation remain connected.",
    evidence: "Emerging",
    metrics: [["World state", "inspectable"], ["Laws", "3 executable"], ["Sources", "attached"], ["Reality check", "required"]],
    logs: [
      "Loaded an executable watershed model from checked laws and local parameters.",
      "Changed rainfall while preserving conservation constraints.",
      "Separated simulated prediction from observed local evidence.",
      "Generated a field observation task to test the model’s assumptions.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-8">
          <span class="demo-label">Verified watershed world</span>
          <div class="world-canvas">
            <div class="world-sun"></div><div class="world-mountain"></div><div class="world-river"></div>
            <div class="world-reading">rainfall: <output id="rainOutput">42</output> mm<br>runoff: <output id="runoffOutput">18</output>%<br>status: simulated</div>
          </div>
          <div class="range-wrap">
            <label for="rainRange"><span>Rainfall</span><b><output id="rainLabel">42</output> mm</b></label>
            <input id="rainRange" type="range" min="10" max="100" value="42" data-range="rain">
          </div>
        </article>
        <article class="demo-panel span-4 soft-blue">
          <span class="demo-label">Four-layer truth stack</span>
          <div class="assurance-ladder">
            <div class="assurance-rung active"><span>04</span><b>Real observation</b><small>measure the stream</small></div>
            <div class="assurance-rung"><span>03</span><b>Grounded sources</b><small>local climate + soil</small></div>
            <div class="assurance-rung"><span>02</span><b>Executable law</b><small>water balance</small></div>
            <div class="assurance-rung"><span>01</span><b>Generated world</b><small>explorable view</small></div>
          </div>
        </article>
      </div>`,
  },
  {
    id: "embodied",
    group: "Action",
    title: "Screen-to-world mentor",
    summary: "Move from explanation to seeing, sensing, coaching real action, connecting people, and carefully authorized actuation.",
    evidence: "Emerging",
    metrics: [["Scene objects", "4"], ["Action step", "measure V₂"], ["Safety", "learning-only"], ["Human nearby", "yes"]],
    logs: [
      "Identified the learner’s physical circuit without storing the camera stream.",
      "Mapped the visible components to the checked circuit specification.",
      "Suggested one safe measurement and waited for learner confirmation.",
      "Escalated ambiguity to the local teacher before any consequential action.",
    ],
    render: () => `
      <div class="prototype-grid">
        <article class="demo-panel span-8">
          <span class="demo-label">Camera-guided field view</span>
          <div class="camera-view">
            <div class="camera-frame"></div>
            <span class="camera-label a">R1 · 1 kΩ</span><span class="camera-label b">measure V₂ here</span>
          </div>
        </article>
        <article class="demo-panel span-4 soft-amber">
          <span class="demo-label">Action continuum</span>
          <div class="assurance-ladder">
            <div class="assurance-rung"><span>01</span><b>Explain</b><small>available</small></div>
            <div class="assurance-rung"><span>02</span><b>See + sense</b><small>active</small></div>
            <div class="assurance-rung active"><span>03</span><b>Coach action</b><small>current</small></div>
            <div class="assurance-rung"><span>04</span><b>Connect human</b><small>ready</small></div>
            <div class="assurance-rung"><span>05</span><b>Actuate</b><small>permission-gated</small></div>
          </div>
        </article>
      </div>`,
  },
  {
    id: "access",
    group: "Inclusion",
    title: "Accessibility-first pivot",
    summary: "Preserve the learning goal while composing language, sensory, cognitive, motor, and communication access around the learner.",
    evidence: "Design standard",
    metrics: [["Goal", "preserved"], ["Modalities", "4 available"], ["Learner control", "on"], ["Pivot", "instant"]],
    logs: [
      "Preserved the concept goal while changing the access path.",
      "Composed captions, visual choices, shorter turns, and keyboard control.",
      "Asked the learner which modality felt clearest rather than inferring permanently.",
      "Saved the preference as correctable and context-specific.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel span-7 soft-teal">
          <span class="demo-label">Access compositor</span>
          <h3>Same ambitious goal. More ways in.</h3>
          <p>Active profile for ${ctx.learner.name}; every setting is learner-visible and reversible.</p>
          <div class="toggle-row">
            <button class="toggle-chip" type="button" data-toggle aria-pressed="false">captions</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="false">AAC choices</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="true">shorter turns</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="true">high contrast</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="false">audio description</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="true">keyboard first</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="false">reduced motion</button>
            <button class="toggle-chip" type="button" data-toggle aria-pressed="false">symbol support</button>
          </div>
        </article>
        <article class="demo-panel span-5">
          <span class="demo-label">Pivot loop</span>
          <div class="decision-path" style="flex-direction:column">
            <div class="decision-node"><b>Preserve goal</b><small>equivalent fractions</small></div>
            <div class="decision-node"><b>Observe access</b><small>learner feedback, not labels</small></div>
            <div class="decision-node"><b>Compose + teach</b><small>text · voice · visual · AAC</small></div>
            <div class="decision-node"><b>Probe + pivot</b><small>did understanding improve?</small></div>
          </div>
        </article>
      </div>`,
  },
  {
    id: "offline",
    group: "Delivery",
    title: "Offline-first continuity",
    summary: "Keep identity, cached curriculum, common teaching actions, practice, evidence, and encrypted sync useful on the learner’s device.",
    evidence: "Shipped + frontier",
    metrics: [["Active tier", "device"], ["Cached concepts", "128"], ["Sync queue", "3 events"], ["Learning", "continuous"]],
    logs: [
      "Detected the active network tier and removed unavailable rich-media actions.",
      "Continued with cached ConceptSpecs, local practice, and append-only evidence.",
      "Queued three encrypted purpose-bound deltas for the community hub.",
      "Preserved the teaching relationship while labeling reduced specialization.",
    ],
    render: (ctx) => {
      const offline = ctx.network === "offline";
      const hub = ctx.network === "hub";
      return `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">Three-tier delivery</span>
          <h3>Capability degrades. Learning continues.</h3>
          <div class="offline-stack">
            <div class="tier"><span class="tier-number">1</span><span><b>Learner device</b><small>state · curriculum · practice · evidence</small></span><span class="tier-status">active</span></div>
            <div class="tier ${offline ? "off" : ""}"><span class="tier-number">2</span><span><b>Community hub</b><small>local models · speech · teacher view · groups</small></span><span class="tier-status">${offline ? "queued" : "active"}</span></div>
            <div class="tier ${offline || hub ? "off" : ""}"><span class="tier-number">3</span><span><b>Regional / cloud</b><small>frontier reasoning · rare expertise · rich media</small></span><span class="tier-status">${offline || hub ? "offline" : "active"}</span></div>
          </div>
        </article>
        <article class="demo-panel span-5 dark">
          <span class="demo-label">Local continuity</span>
          <div class="contract-code">available now:
  ✓ text + compact speech
  ✓ 128 cached ConceptSpecs
  ✓ common teaching actions
  ✓ practice + evidence append
  ${offline ? "○" : "✓"} specialist routing
sync queue:
  3 encrypted deltas
  purpose: learning continuity
  next: ${offline ? "when hub returns" : "now"}</div>
          <div class="tag-row"><span class="tag on">shared-phone safe</span><span class="tag on">local custody</span><span class="tag on">sync later</span></div>
        </article>
      </div>`;
    },
  },
  {
    id: "human",
    group: "Human network",
    title: "Human handoff",
    summary: "Bring teachers, family, peers, tutors, and experts into the same learning relationship with minimum context and explicit authority.",
    evidence: "Measured + emerging",
    metrics: [["Role", "local teacher"], ["Context shared", "minimum"], ["Authority", "learning support"], ["Continuity", "preserved"]],
    logs: [
      "Detected an ambiguity that benefits from local observation, not more model scale.",
      "Explained to the learner why a teacher is joining and what will be shared.",
      "Created a minimum-necessary HumanHandoff with bounded authority.",
      "Prepared a continuity note so learning resumes after the human turn.",
    ],
    render: (ctx) => `
      <div class="prototype-grid">
        <article class="demo-panel span-7">
          <span class="demo-label">HumanHandoff contract</span>
          <h3>People are first-class nodes</h3>
          <div class="handoff-card">
            <div class="handoff-head"><span class="human-avatar">MS</span><span><b>Ms. Sato · local teacher</b><small>available at community hub · 3 min</small></span></div>
            <div class="handoff-fields">
              <div class="handoff-field"><span>Reason</span><b>observe the physical setup</b></div>
              <div class="handoff-field"><span>Urgency</span><b>normal · learning continues</b></div>
              <div class="handoff-field"><span>Shared</span><b>goal + one evidence item</b></div>
              <div class="handoff-field"><span>Not shared</span><b>history · raw camera</b></div>
              <div class="handoff-field"><span>Authority</span><b>advise + annotate</b></div>
              <div class="handoff-field"><span>Resume</span><b>return to mentor loop</b></div>
            </div>
          </div>
        </article>
        <article class="demo-panel span-5 soft-blue">
          <span class="demo-label">Learner-visible invitation</span>
          <div class="live-transcript">
            <div class="bubble mentor">A local teacher can check the physical connection I cannot see clearly. I’ll share your current goal and this one image—not your full history. Invite her?</div>
          </div>
          <div class="tool-row"><button class="tool-chip on" type="button" data-toggle aria-pressed="true">invite</button><button class="tool-chip" type="button" data-toggle aria-pressed="false">change sharing</button><button class="tool-chip" type="button" data-toggle aria-pressed="false">continue alone</button></div>
        </article>
      </div>`,
  },
];

const state = {
  active: location.hash.slice(1) || "conductor",
  learner: "amina",
  language: "English",
  network: "cloud",
  ran: new Set(),
  trace: [],
};

const els = {
  nav: document.querySelector("#capabilityNav"),
  labCount: document.querySelector("#labCount"),
  title: document.querySelector("#labTitle"),
  group: document.querySelector("#labGroup"),
  summary: document.querySelector("#labSummary"),
  evidence: document.querySelector("#evidencePill"),
  metrics: document.querySelector("#stageMetrics"),
  prototype: document.querySelector("#prototype"),
  eventLog: document.querySelector("#eventLog"),
  learnerName: document.querySelector("#learnerName"),
  learnerAvatar: document.querySelector("#learnerAvatar"),
  learnerGoal: document.querySelector("#learnerGoal"),
  skillList: document.querySelector("#skillList"),
  nextAction: document.querySelector("#nextAction"),
  nextReason: document.querySelector("#nextReason"),
  nextTier: document.querySelector("#nextTier"),
  toast: document.querySelector("#toast"),
};

function context() {
  return {
    learner: learners[state.learner],
    language: state.language,
    network: state.network,
  };
}

function activeCapability() {
  return capabilities.find((capability) => capability.id === state.active) || capabilities[0];
}

function renderNav(query = "") {
  const term = query.toLowerCase().trim();
  const filtered = capabilities.filter((capability) =>
    `${capability.title} ${capability.group} ${capability.summary}`.toLowerCase().includes(term),
  );
  const grouped = filtered.reduce((map, capability) => {
    if (!map.has(capability.group)) map.set(capability.group, []);
    map.get(capability.group).push(capability);
    return map;
  }, new Map());
  let index = 0;
  els.nav.innerHTML = [...grouped.entries()].map(([group, items]) => `
    <span class="nav-group-label">${group}</span>
    ${items.map((capability) => {
      index += 1;
      const fullIndex = capabilities.indexOf(capability) + 1;
      return `<button class="capability-link" type="button" data-capability="${capability.id}" ${capability.id === state.active ? 'aria-current="page"' : ""}>
        <span class="capability-index">${String(fullIndex).padStart(2, "0")}</span>
        <span class="capability-name">${capability.title}</span>
        <span class="capability-state ${state.ran.has(capability.id) ? "ran" : ""}" aria-label="${state.ran.has(capability.id) ? "Scenario run" : "Not run"}"></span>
      </button>`;
    }).join("")}
  `).join("");
  if (!index) {
    els.nav.innerHTML = '<p class="nav-group-label">No matching capability</p>';
  }
}

function renderLearner() {
  const learner = learners[state.learner];
  els.learnerName.textContent = learner.name;
  els.learnerAvatar.textContent = learner.initials;
  els.learnerGoal.textContent = `Goal: ${learner.goal}`;
  els.nextAction.textContent = learner.next;
  els.nextReason.textContent = learner.reason;
  els.nextTier.textContent = `Tier: ${state.network === "cloud" ? "device + cloud" : state.network}`;
  els.skillList.innerHTML = learner.skills.map(([name, score]) => `
    <div class="skill-row"><b>${name}</b><span>${score}%</span><span class="skill-bar"><i style="width:${score}%"></i></span></div>
  `).join("");
}

function renderTrace() {
  els.eventLog.innerHTML = state.trace.length
    ? state.trace.slice(-8).map((item) => `<li>${item}</li>`).join("")
    : "<li>Run a scenario to inspect the mentor’s decisions.</li>";
  els.eventLog.scrollTop = els.eventLog.scrollHeight;
}

function renderLab({ updateHash = true } = {}) {
  const capability = activeCapability();
  const capIndex = capabilities.indexOf(capability) + 1;
  els.labCount.textContent = `${String(capIndex).padStart(2, "0")} / ${capabilities.length}`;
  els.title.textContent = capability.title;
  els.group.textContent = capability.group;
  els.summary.textContent = capability.summary;
  els.evidence.textContent = capability.evidence;
  els.metrics.innerHTML = capability.metrics.map(([label, value]) => `<div class="metric"><span>${label}</span><b>${value}</b></div>`).join("");
  els.prototype.innerHTML = capability.render(context());
  renderLearner();
  renderNav(document.querySelector("#labSearch").value);
  if (updateHash) {
    history.replaceState(null, "", `#${capability.id}`);
  }
}

function selectCapability(id, options = {}) {
  if (!capabilities.some((capability) => capability.id === id)) return;
  state.active = id;
  state.trace = [];
  renderTrace();
  renderLab(options);
}

function addTrace(message) {
  state.trace.push(`${new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" })} · ${message}`);
  renderTrace();
}

function showToast(message) {
  els.toast.textContent = message;
  els.toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => els.toast.classList.remove("show"), 2600);
}

function runScenario() {
  const capability = activeCapability();
  state.trace = [];
  document.body.classList.add("running");
  capability.logs.forEach((message, index) => {
    setTimeout(() => {
      addTrace(message);
      if (index === capability.logs.length - 1) {
        state.ran.add(capability.id);
        document.body.classList.remove("running");
        renderNav(document.querySelector("#labSearch").value);
        showToast(`${capability.title} scenario complete`);
      }
    }, index * 260);
  });
}

function runCompleteLoop() {
  const loop = [
    ["live", "Perceived voice, page, and learner gesture."],
    ["conductor", "Selected an explicit teaching action."],
    ["mesh", "Routed verification to role-certified specialists."],
    ["compiler", "Compiled a checked learning object."],
    ["state", "Read minimum learner-owned state."],
    ["human", "Kept a trusted human available with bounded context."],
    ["assessment", "Captured evidence and scheduled delayed transfer."],
  ];
  state.trace = [];
  document.body.classList.add("running");
  document.querySelector("#labs").scrollIntoView({ behavior: "smooth", block: "start" });
  loop.forEach(([id, message], index) => {
    setTimeout(() => {
      state.ran.add(id);
      addTrace(message);
      if (index === loop.length - 1) {
        document.body.classList.remove("running");
        renderNav(document.querySelector("#labSearch").value);
        showToast("Complete mentor loop finished · all seven planes connected");
      }
    }, index * 220);
  });
}

function updateReactiveRange(input) {
  const value = Number(input.value);
  if (input.dataset.range === "velocity") {
    document.querySelector("#velocityOutput").textContent = value;
    document.querySelector("#heightOutput").textContent = `${(value * value / 39).toFixed(1)} m`;
    document.querySelector("#timeOutput").textContent = `${(value / 7).toFixed(1)} s`;
    const trajectory = document.querySelector("#trajectory");
    trajectory.style.width = `${45 + value * 2}%`;
    trajectory.style.height = `${55 + value * 3}px`;
  }
  if (input.dataset.range === "memory") {
    document.querySelector("#memoryOutput").textContent = value;
  }
  if (input.dataset.range === "rain") {
    document.querySelector("#rainOutput").textContent = value;
    document.querySelector("#rainLabel").textContent = value;
    document.querySelector("#runoffOutput").textContent = Math.round(8 + value * 0.24);
  }
}

function exportLearnerState() {
  const learner = learners[state.learner];
  const payload = {
    schema: "LearnerState/0.1-demo",
    owner: learner.name,
    goal: learner.goal,
    language: state.language,
    network_tier: state.network,
    skills: Object.fromEntries(learner.skills.map(([name, score]) => [name, { estimate: score / 100, uncertainty: 0.12 }])),
    permissions: ["learning", "portable_export"],
    note: "Synthetic interaction prototype. No real learner data.",
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = `${learner.name.toLowerCase()}-learner-state-demo.json`;
  anchor.click();
  URL.revokeObjectURL(url);
  showToast("Portable learner state exported");
}

document.addEventListener("click", (event) => {
  const capabilityButton = event.target.closest("[data-capability]");
  if (capabilityButton) {
    selectCapability(capabilityButton.dataset.capability);
    document.querySelector("#lab").focus({ preventScroll: true });
    if (event.target.closest("#architectureTrack")) {
      document.querySelector("#labs").scrollIntoView({ behavior: "smooth", block: "start" });
    }
    return;
  }

  const toggle = event.target.closest("[data-toggle]");
  if (toggle) {
    const pressed = toggle.getAttribute("aria-pressed") === "true";
    toggle.setAttribute("aria-pressed", String(!pressed));
    toggle.classList.toggle("on", !pressed);
    addTrace(`${toggle.textContent.trim()} ${pressed ? "disabled" : "enabled"} by learner control.`);
    return;
  }

  const depth = event.target.closest("[data-depth]");
  if (depth) {
    document.querySelectorAll("[data-depth]").forEach((button) => button.classList.remove("active"));
    depth.classList.add("active");
    const explanation = explanations[depth.dataset.depth];
    document.querySelector("#explanationCard").innerHTML = `<b>${explanation.title}</b><p>${explanation.body}</p>`;
    addTrace(`Changed explanation depth to ${depth.dataset.depth}; invariants preserved.`);
    return;
  }

  const choice = event.target.closest("[data-choice]");
  if (choice) {
    const container = choice.parentElement;
    container.querySelectorAll("[data-choice]").forEach((button) => button.classList.remove("active"));
    choice.classList.add("active");
    addTrace(`Selected ${choice.textContent.trim().replace(/\s+/g, " ")}.`);
  }
});

document.addEventListener("input", (event) => {
  if (event.target.matches("[data-range]")) {
    updateReactiveRange(event.target);
  }
});

document.querySelector("#runLab").addEventListener("click", runScenario);
document.querySelector("#runLoop").addEventListener("click", runCompleteLoop);
document.querySelector("#resetLab").addEventListener("click", () => {
  state.trace = [];
  renderTrace();
  renderLab({ updateHash: false });
  showToast("Prototype reset");
});
document.querySelector("#clearTrace").addEventListener("click", () => {
  state.trace = [];
  renderTrace();
});
document.querySelector("#exploreButton").addEventListener("click", () => {
  document.querySelector("#labs").scrollIntoView({ behavior: "smooth", block: "start" });
  document.querySelector("#lab").focus({ preventScroll: true });
});
document.querySelector("#exportState").addEventListener("click", exportLearnerState);
document.querySelector("#accessButton").addEventListener("click", (event) => {
  const pressed = event.currentTarget.getAttribute("aria-pressed") === "true";
  event.currentTarget.setAttribute("aria-pressed", String(!pressed));
  document.body.classList.toggle("access-mode", !pressed);
  showToast(pressed ? "Standard display restored" : "Access profile enabled");
});
document.querySelector("#labSearch").addEventListener("input", (event) => renderNav(event.target.value));
document.querySelector("#learnerSelect").addEventListener("change", (event) => {
  state.learner = event.target.value;
  renderLab({ updateHash: false });
  addTrace(`Loaded ${learners[state.learner].name}’s permitted learner state.`);
});
document.querySelector("#languageSelect").addEventListener("change", (event) => {
  state.language = event.target.value;
  renderLab({ updateHash: false });
  addTrace(`Teaching language changed to ${state.language} without resetting state.`);
});
document.querySelector("#networkSelect").addEventListener("change", (event) => {
  state.network = event.target.value;
  renderLab({ updateHash: false });
  addTrace(`Delivery tier changed to ${state.network}; capability set recomputed.`);
});

window.addEventListener("hashchange", () => {
  const id = location.hash.slice(1);
  if (id && id !== state.active) selectCapability(id, { updateHash: false });
});

if (!capabilities.some((capability) => capability.id === state.active)) {
  state.active = "conductor";
}

renderLab();
renderTrace();

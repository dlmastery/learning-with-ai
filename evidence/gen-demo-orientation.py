#!/usr/bin/env python3
"""Insert a what/why/how orientation block after <header> on every demo page.
Written per-demo. Re-runnable: replaces an existing block rather than stacking."""
import pathlib, re

O = {
"teachable-agent": (
 "A protégé you teach. You write a rule in your own words; a parser applies that rule <em>literally</em> to eight fresh fraction problems and shows its working. It has no knowledge of fractions and no way to quietly fix a bad rule.",
 "Learning by teaching is <b>g = 0.48</b> when the expectancy to teach is set <em>before</em> study, and <b>g = −0.02</b> without it. Every commercial model silently repairs a learner's wrong rule, which destroys the mechanism. The gap between what you meant and what you actually said is the entire pedagogical payload.",
 "Accept the expectancy first — that ordering is the effect. Then type a rule, even a wrong one (try <kbd>add tops, add bottoms</kbd>), and press run. Watch <em>which</em> item it happens to pass. Edit the rule and re-run until the suite is green."),
"refusal-engine": (
 "The decision function of a tutor that would rather ask than answer, with every input exposed as a control. Move a slider and the verdict — answer · ask · wait · pivot · escalate — recomputes, along with the rule that fired.",
 "Unguarded AI leaves learners <b>17% worse</b> on later unassisted work. Guardrails measurably remove that harm (unassisted coefficient −0.004, n.s.). They have not been shown to add benefit. Restraint is the one thing no vendor ships and the one thing the evidence demands.",
 "Set <em>attempted</em> to no and watch every branch refuse to answer. Then switch the learner to explicit-instruction mode and see the logic <em>invert</em>. For that learner, withholding is the harm."),
"grounding-ladder": (
 "A real verification stack running in your browser. Twenty textbook formulas, five ways of breaking each, and three checkers — dimensional, numeric, symbolic — timed with <code>performance.now()</code>. Nothing here is hardcoded.",
 "If a tutor can be <em>checked</em>, it can contradict a confident learner without anyone asserting authority. The measured surprise: numeric checking is the cheap default at near-perfect recall, and symbolic escalation costs far more for almost nothing — the opposite of how everyone builds it.",
 "Run the suite and read the per-rung table. Then raise <em>k</em>, the number of random substitutions, and watch recall stay flat while latency climbs — that is a null we measured. Look for the row where our own symbolic checker <b>gets it wrong</b>; it is disclosed, not hidden."),
"adversary": (
 "A problem generator whose search space is enumerated rather than claimed. It reports exactly how many distinct items it can address, and measures distinctness rather than asserting it.",
 "An adversary that can generate a fresh, unGoogleable problem at the edge of what you know — forever — is one of the things that was structurally impossible when attention was scarce. But difficulty has to be <em>semantic</em>: difficulty that is merely perceptual measures <b>d = −0.05</b>.",
 "Generate a few items and note the index — each is one of a stated finite number. Move the difficulty dial and watch the <em>derivation depth</em> change rather than the surface wording. Read §3 for why an <em>announced</em> devil's advocate backfires."),
"learner-model": (
 "A persistent learner model living in your browser's own storage, shown as raw JSON. Teach it something, watch its per-concept estimates move, then correct it or destroy it.",
 "Persistent state is the single largest unmeasured engineering commitment in this field — <b>no study compares a stateful tutor against a stateless one</b>. The most-adopted AI tutor ever built (29,606 stars) opens its README with <code>DISCONTINUED</code> after failing twice to persist a learner model.",
 "Answer a few items and watch the estimates update. Then <em>correct</em> an entry the model got wrong — a learner and a parent must be able to. Finally press delete and re-read the record: under IDEA §300.624 that deletion has to be real, not a flag."),
"deixis": (
 "A shared visual field the tutor can point at. It circles, arrows and highlights while its words say &ldquo;this&rdquo; — and a toggle strips the pointing so you feel what is lost.",
 "Pointing at a shared referent is how humans teach anything spatial, and no vendor exposes it as a live-session primitive. The substrate now exists (<b>49% IoU</b> fine-tuned against &lt;1% zero-shot); the tutoring loop built on it does not.",
 "Step through the tutor's turns with the pointing on. Then switch to <em>words only</em> and read the same explanation — the sentences are identical and the burden on your working memory is not. That difference is the whole argument."),
"connector": (
 "A role that brokers contact with real people and refuses to be your friend. It computes overlapping availability across time zones, ranks candidates, and declines a companionship framing outright.",
 "Technology-mediated collaborative learning delivers <b>+3 months against +5</b> in person — the mediation costs something real. And adults anthropomorphise AI companions <em>more</em> than teens do. A system that simulates friendship is substituting for the thing with the better evidence.",
 "Change a time zone or an availability window and watch the ranking reorder. Then toggle the EEF coefficient and see human contact move up the list. Read the refusal in §3 — it is scripted, and labelled as such."),
"felt-vs-real": (
 "A study you can run. Set how <em>fluent</em> and how <em>effortful</em> a condition feels, and the page computes both satisfaction and delayed retention — with Welch's <em>t</em> and a real <em>p</em>-value, not a cartoon.",
 "This is the central finding of the whole survey. Preference moves at <b>d ≈ 0.48</b> while knowledge moves <b>zero</b>, and it survives explicit debiasing. Students in the condition that taught them <em>more</em> reported learning <em>less</em>. Every optimisation loop can measure the first axis; almost none measure the second.",
 "Make a condition feel maximally fluent and watch satisfaction rise as retention does not. Then run the <b>Null-Learner Test</b>: pick a metric and see whether an agent that teaches nothing can max it out. Engagement, streaks and time-on-task all fail."),
"eli-ladder": (
 "One genuinely hard concept written at three distinct altitudes, presented as a <em>library you enter</em> rather than a staircase you climb — with the fidelity rule enforced in code.",
 "Three rungs beat two (<b>p = 0.032</b>); five did <em>not</em> beat three (<b>p = 0.738</b>). So ELI10/15/20/25 is one level too many, and entry must be <em>measured</em> — preference moves d ≈ 0.48 while knowledge moves zero. A simplification may drop precision. It may never falsify ontology.",
 "Take the short probe and let it choose your door rather than picking one. Then open the <em>violation</em> toggle: a plausible-sounding simplification that breaks ontology, and the reason a full semester of instruction does not shift that particular error."),
"pivot-loop": (
 "Two decision loops, simulated honestly. An exact run-length calculation for &ldquo;three wrong in a row&rdquo;, a 4,000-learner Monte Carlo for trend rules, and a closed-form answer for how many weeks a real decision needs.",
 "A tutor that changes method after three wrong answers is not adapting — it is fitting noise, and this page computes exactly how often. Worse: <b>measurement alone is inert</b>. In the randomised trial, both arms revised instruction more often and only the arm told <em>what to change</em> moved achievement.",
 "Start with the three-in-a-row rule and read the expected false pivots per term. Then move to the weekly probe loop and drag the number of data points — watch detection and false-alarm trade against each other until the published 7–10 week bound falls out."),
"distractors": (
 "Two multiple-choice generators on the same stem, side by side. One asks for plausible wrong answers. The other models a named <em>misconception</em> first and derives the option from it.",
 "LLMs produce distractors that are mathematically valid and pedagogically empty — they are &ldquo;less adept at anticipating common errors among real students&rdquo;, and that survived fine-tuning. Modelling the error as a first-class object lets a <b>7B model beat GPT-4o</b>.",
 "Generate from both and compare. Generator A's options are a function of the <em>key</em> — so a student choosing one tells you nothing. Generator B's map to specific errors, which makes a wrong answer diagnostic. Watch the collision counter reject options that two misconceptions would both produce."),
"patha": (
 "A three-thousand-year-old error-detection scheme, implemented, and then the benchmark that killed the idea this project built on it.",
 "The Vedic <em>pāṭha</em> recitations permute word order deliberately, which disables semantic autocorrect, the exact failure mode of LLM paraphrase drift. We proposed adapting it as a fidelity check on model output. It was worth trying and it does not work.",
 "Corrupt a token and watch <em>krama</em> catch a transposition that plain recitation misses. That part is real and computed. Then read §4, which reports our own benchmark: 87.5%/87.5% and 100%/100%, exactly at chance, losing to plain self-consistency by 18.8 and 43.8 points. This is what publishing a falsification looks like."),
"cbm-probe": (
 "A curriculum-based measurement loop: generate brief equivalent-form probes, graph them against a goal line, apply a stated decision rule — and, critically, emit a <em>prescribed instructional change</em> when it fires.",
 "The load-bearing trial in this whole survey. Both arms measured more and revised more; <b>only the arm with an expert system telling teachers what to change moved achievement</b>. Dashboards, streaks and mastery bars are all the arm that did nothing.",
 "Run the loop in <em>dashboard only</em> mode and watch it produce a beautiful graph and no instruction. Switch on the prescription and see the same data yield a named action. Then audit the probes: readability-matched forms varied <b>67.9–93.9 WCPM</b> — roughly a semester of apparent growth from form alone."),
}

D = pathlib.Path("docs/demos")
BLOCK = re.compile(r'\n<section class="orient">.*?</section>\n', re.S)
n = 0
for slug, (what, why, how) in O.items():
    f = D / f"{slug}.html"
    if not f.exists():
        print(f"  !! missing {slug}"); continue
    t = BLOCK.sub("\n", f.read_text())
    block = (f'\n<section class="orient">\n'
             f'  <div class="o"><b>What this is</b><p>{what}</p></div>\n'
             f'  <div class="o"><b>Why it matters</b><p>{why}</p></div>\n'
             f'  <div class="o"><b>How to use it</b><p>{how}</p></div>\n'
             f'</section>\n')
    if "</header>" not in t:
        print(f"  !! no </header> in {slug}"); continue
    t = t.replace("</header>", "</header>\n" + block, 1)
    f.write_text(t); n += 1
print(f"orientation blocks written: {n}/13")

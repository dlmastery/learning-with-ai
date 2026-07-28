# Evidence

Everything here exists so a reader can check us rather than trust us.

## The adversarial reviews

A hostile reviewer — brief: *fail this work* — read the repository three times.
The first two verdicts were **not publishable**.

| | Verdict | What it found |
|---|---|---|
| [First pass](review-2026-07-28.md) | not yet | A superseded effect size published five times, in the document that states the rule against doing exactly that |
| [Second pass](review-2-2026-07-28.md) | not yet | Corrections were being applied by *silently rewriting the ledger rows* — inside a table headed "published rather than silently edited" |
| [Third pass](review-3-2026-07-28.md) | not yet | The propagation checker built to prevent all this **did not work**; the reviewer planted the original errors back in and it reported zero violations |

Eight of the corrections in [`CORRECTIONS.md`](../CORRECTIONS.md) came from these,
not from us.

## The checks, and how to run them

```bash
# no superseded value survives anywhere on a published surface
python3 evidence/check-corrections.py --self-test --strict

# every demo page renders, runs, and does not overflow at 390px
cd /tmp/pw && npm i playwright@1.62.0 --no-save && npx playwright install chromium-headless-shell
node test-demos.mjs
node test-pages.mjs
```

`--self-test` plants each known violation into a scratch copy and **fails if the rule
does not fire**. It exists because the first version of this checker was theatre.

## Original measurements

| File | What it measures |
|---|---|
| [`F3-grounding-ladder-harness.py`](F3-grounding-ladder-harness.py) | Dimensional / numeric / symbolic checking against seeded derivation errors |
| [`F7-A3/`](F7-A3/) | Reactive-notebook hazard classes; the `teachcheck` conformance checker |
| [`bastani-2025-correction-check.md`](bastani-2025-correction-check.md) | Verifying a claim made *to* us — and rejecting it |
| [`build-paper.py`](build-paper.py) | Assembles `survey/` into `PAPER.md` and the web edition |

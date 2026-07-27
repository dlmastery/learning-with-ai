#!/usr/bin/env python3
"""
G1 · Two original follow-on measurements on F3's grounding-ladder corpus
(20 formulas, 37 semantically-equivalent rewrites, 113 mutants).

(1) THE ABSTENTION FIX.  F3 §4.2 finding 3 reported a single numeric miss: the
    Lorentz-factor "wrong variable" mutant substitutes v->c, both sides evaluate
    to a non-finite value, and the checker compared two degenerate values and
    reported AGREEMENT.  F3 prescribed a one-line fix (non-finite => ABSTAIN,
    never PASS) but did not run it.  We run it and measure the effect on recall
    AND on the false-alarm rate over the 37 equivalent rewrites.

(2) THE SAMPLING BUDGET.  F3 used 8 random substitutions per check without
    justifying 8.  We sweep trials in {1,2,4,8,16} and sample domains in
    {narrow-positive (F3's), wide-positive, signed} and report recall,
    false alarms and cost.  This decides how cheap the default rung really is.

Requires the F3 corpus: run from the same directory as F3-grounding-ladder-harness.py.
"""
import importlib.util, random, time, sys, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "F3-grounding-ladder-harness.py")

# Load F3's CORPUS + mutation operators without running its report.
src = open(SRC).read()
head = src.split("# ---------------------------------------------------------------- tiers")[0]
g = {"__name__": "f3corpus"}
exec(compile(head, SRC, "exec"), g)
CORPUS, MUTS = g["CORPUS"], g["MUTS"]

DOMAINS = {
    "narrow_pos (F3)": lambda: random.uniform(0.31, 0.87),
    "wide_pos":        lambda: random.uniform(0.05, 20.0),
    "signed":          lambda: random.choice([-1, 1]) * random.uniform(0.05, 20.0),
}

def L2(cand, ref, trials, draw, guard_nonfinite):
    """Return True (agree), False (disagree) or None (abstain)."""
    fs = sorted(cand.free_symbols | ref.free_symbols, key=sp.default_sort_key)
    seen_valid = False
    for _ in range(trials):
        sub = {s: sp.Float(draw()) for s in fs}
        try:
            a = complex(sp.N(cand.subs(sub)))
            b = complex(sp.N(ref.subs(sub)))
            d = complex(sp.N((cand - ref).subs(sub)))
        except Exception:
            continue                      # this draw is undefined -> skip it
        if guard_nonfinite:
            vals = [a, b, d]
            bad = any((v.real != v.real) or (v.imag != v.imag) or
                      abs(v) == float("inf") for v in vals)
            if bad:
                continue                  # ABSTAIN on this draw; never PASS on it
        seen_valid = True
        sc = abs(a) + abs(b) + 1e-30
        if abs(d) > 1e-9 * sc:
            return False
    return True if seen_valid else None

def build():
    """(kind, name, mutation, cand, ref) rows: 20 identical, 37 equivalent, 113 mutants."""
    rows = []
    for name, ref, eqs, dims, unit in CORPUS:
        for i, e in enumerate(eqs):
            rows.append(("equivalent", name, "rewrite%d" % i, e, ref))
        for mn, fn in MUTS:
            random.seed(abs(hash((name, mn))) % (2**31))
            try:
                bad = fn(ref)
            except Exception:
                continue
            if sp.simplify(bad - ref) == 0:
                continue
            rows.append(("mutant", name, mn, bad, ref))
    return rows

def evaluate(rows, trials, domain, guard, seed=7):
    random.seed(seed)
    draw = DOMAINS[domain]
    caught = missed = abst_m = 0
    fa = ok = abst_e = 0
    t = []
    for kind, name, mut, cand, ref in rows:
        t0 = time.perf_counter()
        r = L2(cand, ref, trials, draw, guard)
        t.append(time.perf_counter() - t0)
        if kind == "mutant":
            caught += (r is False); missed += (r is True); abst_m += (r is None)
        else:
            fa += (r is False); ok += (r is True); abst_e += (r is None)
    t.sort()
    return dict(caught=caught, missed=missed, abstain_m=abst_m,
                false_alarm=fa, ok=ok, abstain_e=abst_e,
                median_ms=1000*t[len(t)//2], p95_ms=1000*t[int(.95*len(t))])

if __name__ == "__main__":
    rows = build()
    nm = sum(1 for r in rows if r[0] == "mutant")
    ne = len(rows) - nm
    print(f"corpus: {nm} mutants, {ne} semantically-equivalent rewrites\n")

    print("=== (1) THE ABSTENTION FIX (trials=8, F3's narrow_pos domain) ===")
    print(f"{'guard':22s} {'caught':>8s} {'missed':>7s} {'abstain':>8s} | "
          f"{'false alarm':>12s} {'abstain':>8s}")
    for guard, label in [(False, "F3 as published"), (True, "non-finite=>ABSTAIN")]:
        r = evaluate(rows, 8, "narrow_pos (F3)", guard)
        print(f"{label:22s} {r['caught']:>4d}/{nm:<3d} {r['missed']:>7d} {r['abstain_m']:>8d} | "
              f"{r['false_alarm']:>7d}/{ne:<4d} {r['abstain_e']:>8d}")

    print("\n=== (2) SAMPLING BUDGET (guard on) ===")
    print(f"{'domain':18s} {'k':>3s} {'recall':>12s} {'miss':>5s} {'abst':>5s} "
          f"{'false alarm':>12s} {'med ms':>8s} {'p95 ms':>8s}")
    for domain in DOMAINS:
        for k in (1, 2, 4, 8, 16):
            r = evaluate(rows, k, domain, True)
            rec = 100 * r["caught"] / nm
            print(f"{domain:18s} {k:>3d} {r['caught']:>4d}/{nm:<3d}={rec:5.1f}% "
                  f"{r['missed']:>5d} {r['abstain_m']:>5d} "
                  f"{r['false_alarm']:>7d}/{ne:<4d} {r['median_ms']:>8.3f} {r['p95_ms']:>8.3f}")

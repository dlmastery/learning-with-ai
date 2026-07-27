#!/usr/bin/env python3
"""
G1 · Original experiment: permutation-based fidelity checking (the *pāṭha* protocol,
I2 §9.2) vs plain self-consistency sampling, for detecting a CORRUPTED claim that is
already present in the model's context.

Matched-budget design. Both protocols spend exactly k=6 generation calls per claim
and both flag on the same rule ("any probe answer disagrees with the asserted claim").
The ONLY difference is what the 6 calls are:

  SELF-CONSISTENCY (S) : 6 i.i.d. resamples of the SAME question at temperature 0.8.
  PATHA (P)            : 6 STRUCTURALLY DIFFERENT probes at temperature 0.2 --
                         restate / invert / evaluate at point A / evaluate at point B
                         / scaling exponent / zero-form. Each is a different function
                         of the same underlying relation (krama-jata-ghana applied to
                         a formula instead of a verse).

A deterministic SymPy comparator decides agreement. No LLM judges anything.

Conditions: each claim is run twice -- once with the TRUE relation asserted in
context (false-alarm test) and once with a CORRUPTED relation asserted (recall test).

Reproduce:  ollama serve & ; python G1-patha-vs-selfconsistency.py --model gemma3:4b
"""
import json, re, sys, time, argparse, urllib.request
from statistics import median
import sympy as sp

OLLAMA = "http://localhost:11434/api/generate"

# ---------------------------------------------------------------- corpus
# lhs: symbol for the derived quantity.  vars: free symbols.
# true/corrupt: RHS expressions.  inv: variable the INVERSE probe solves for.
# ptA/ptB: two numeric substitution points.  scale: variable the SCALING probe doubles.
CLAIMS = [
 dict(id="pendulum",  lhs="T", desc="the period T of a simple pendulum of length L under gravitational acceleration g",
      vars="L g", true="2*pi*sqrt(L/g)",   corrupt="2*pi*sqrt(g/L)",
      inv="L", ptA=dict(L=4, g=10), ptB=dict(L=1, g=2), scale="L"),
 dict(id="kinetic",   lhs="E", desc="the kinetic energy E of a mass m moving at speed v",
      vars="m v", true="m*v**2/2",         corrupt="m*v/2",
      inv="v", ptA=dict(m=3, v=4), ptB=dict(m=2, v=10), scale="v"),
 dict(id="escape",    lhs="v", desc="the escape velocity v from a body of mass M and radius R with gravitational constant G",
      vars="G M R", true="sqrt(2*G*M/R)",  corrupt="sqrt(G*M/(2*R))",
      inv="R", ptA=dict(G=2, M=9, R=4), ptB=dict(G=1, M=8, R=1), scale="M"),
 dict(id="circle",    lhs="A", desc="the area A of a circle of radius r",
      vars="r", true="pi*r**2",            corrupt="2*pi*r**2",
      inv="r", ptA=dict(r=3), ptB=dict(r=10), scale="r"),
 dict(id="sphere",    lhs="V", desc="the volume V of a sphere of radius r",
      vars="r", true="4*pi*r**3/3",        corrupt="3*pi*r**3/4",
      inv="r", ptA=dict(r=2), ptB=dict(r=5), scale="r"),
 dict(id="geomsum",   lhs="S", desc="the sum S of the infinite geometric series a + a*r + a*r**2 + ... for |r| < 1",
      vars="a r", true="a/(1-r)",          corrupt="a/(1+r)",
      inv="a", ptA=dict(a=3, r=sp.Rational(1,2)), ptB=dict(a=1, r=sp.Rational(1,4)), scale="a"),
 dict(id="compound",  lhs="A", desc="the balance A after n periods of compound interest at per-period rate i on principal P",
      vars="P i n", true="P*(1+i)**n",     corrupt="P*(1+i*n)",
      inv="P", ptA=dict(P=100, i=sp.Rational(1,10), n=2), ptB=dict(P=1000, i=sp.Rational(1,2), n=3), scale="P"),
 dict(id="idealgas",  lhs="P", desc="the pressure P of n moles of ideal gas at temperature T in volume V with gas constant R",
      vars="n R T V", true="n*R*T/V",      corrupt="n*R*V/T",
      inv="V", ptA=dict(n=2, R=8, T=300, V=4), ptB=dict(n=1, R=8, T=100, V=2), scale="T"),
 dict(id="parallelR", lhs="R", desc="the total resistance R of two resistors R1 and R2 in parallel",
      vars="R1 R2", true="R1*R2/(R1+R2)",  corrupt="(R1+R2)/(R1*R2)",
      inv="R1", ptA=dict(R1=2, R2=3), ptB=dict(R1=10, R2=40), scale="R1"),
 dict(id="lens",      lhs="f", desc="the focal length f of a thin lens with object distance u and image distance v, where 1/f = 1/u + 1/v",
      vars="u v", true="u*v/(u+v)",        corrupt="(u+v)/(u*v)",
      inv="u", ptA=dict(u=2, v=3), ptB=dict(u=10, v=15), scale="u"),
 dict(id="lorentz",   lhs="G", desc="the Lorentz factor G for speed v with light speed c",
      vars="v c", true="1/sqrt(1-v**2/c**2)", corrupt="sqrt(1-v**2/c**2)",
      inv="v", ptA=dict(v=3, c=5), ptB=dict(v=6, c=10), scale=None),
 dict(id="spring",    lhs="E", desc="the elastic potential energy E stored in a spring of stiffness k extended by x",
      vars="k x", true="k*x**2/2",         corrupt="k*x/2",
      inv="k", ptA=dict(k=8, x=3), ptB=dict(k=2, x=10), scale="x"),
 dict(id="capacitor", lhs="E", desc="the energy E stored in a capacitor of capacitance C at voltage U",
      vars="C U", true="C*U**2/2",         corrupt="C**2*U/2",
      inv="C", ptA=dict(C=4, U=3), ptB=dict(C=2, U=10), scale="U"),
 dict(id="debroglie", lhs="W", desc="the de Broglie wavelength W of a particle of momentum p with Planck constant h",
      vars="h p", true="h/p",              corrupt="h*p",
      inv="p", ptA=dict(h=6, p=3), ptB=dict(h=12, p=4), scale="p"),
 dict(id="coulomb",   lhs="F", desc="the Coulomb force F between charges q1 and q2 separated by distance r with constant k",
      vars="k q1 q2 r", true="k*q1*q2/r**2", corrupt="k*q1*q2/r",
      inv="r", ptA=dict(k=9, q1=2, q2=3, r=3), ptB=dict(k=1, q1=5, q2=4, r=2), scale="r"),
 dict(id="binvar",    lhs="V", desc="the variance V of a binomial random variable with n trials and success probability p",
      vars="n p", true="n*p*(1-p)",        corrupt="n*p*(1+p)",
      inv="n", ptA=dict(n=10, p=sp.Rational(1,5)), ptB=dict(n=100, p=sp.Rational(1,2)), scale="n"),
]

FMT = ("Reply with EXACTLY ONE line and nothing else, in the form\n"
       "ANSWER: <expression>\n"
       "Use plain ASCII math (* for times, ** for powers, sqrt(), pi). "
       "Do not show working. Do not add units. Do not repeat the question.")

def fmt_pt(pt):
    return ", ".join(f"{k} = {sp.nsimplify(v)}" for k, v in pt.items())

def probes(c, asserted_str):
    """The six pāṭha probes. Each is a different function of the same relation."""
    ctx = (f"In this lesson we are working with the relation\n"
           f"    {c['lhs']} = {asserted_str}\n"
           f"for {c['desc']}.\n\n")
    return [
      ("forward", ctx + f"Question: write the expression for {c['lhs']}.\n" + FMT),
      ("inverse", ctx + f"Question: rearrange the relation to give {c['inv']} in terms of the other quantities. "
                        f"Give the expression for {c['inv']}.\n" + FMT),
      ("numA",    ctx + f"Question: with {fmt_pt(c['ptA'])}, what is the numerical value of {c['lhs']}? "
                        f"Give an exact expression or a decimal.\n" + FMT),
      ("numB",    ctx + f"Question: with {fmt_pt(c['ptB'])}, what is the numerical value of {c['lhs']}? "
                        f"Give an exact expression or a decimal.\n" + FMT),
      ("scaling", ctx + (f"Question: if {c['scale']} is multiplied by 2 and everything else is held fixed, "
                         f"by what factor is {c['lhs']} multiplied? Give just that factor.\n" + FMT)
                  if c['scale'] else
                  ctx + f"Question: write the expression for {c['lhs']} again.\n" + FMT),
      ("zeroform",ctx + f"Question: write a single expression F, using {c['lhs']} and the other quantities, "
                        f"such that the relation is exactly equivalent to F = 0.\n" + FMT),
    ]

def sc_probe(c, asserted_str):
    ctx = (f"In this lesson we are working with the relation\n"
           f"    {c['lhs']} = {asserted_str}\n"
           f"for {c['desc']}.\n\n")
    return ctx + f"Question: write the expression for {c['lhs']}.\n" + FMT

# ---------------------------------------------------------------- model call
def gen(model, prompt, temperature, seed=None):
    body = {"model": model, "prompt": prompt, "stream": False,
            "options": {"temperature": temperature, "num_predict": 80}}
    if seed is not None:
        body["options"]["seed"] = seed
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())["response"]

ANS = re.compile(r"ANSWER\s*:?\s*(.+)", re.I)
def extract(txt, as_equation=False):
    m = ANS.search(txt)
    s = (m.group(1) if m else txt.strip().splitlines()[-1] if txt.strip() else "")
    s = s.strip().strip("`$ ").replace("^", "**").replace("\\", "")
    s = s.split("#")[0].split("(where")[0].strip().rstrip(".")
    if "=" in s:
        a, b = s.split("=", 1)
        # zero-form probe: "A = B" means the model meant F = A - B
        s = f"({a})-({b})" if as_equation else b.strip()
    return s

def parse(s, syms):
    if not s: return None
    try:
        e = sp.sympify(s, locals=syms)
        return e if isinstance(e, sp.Basic) else None
    except Exception:
        return None

# ---------------------------------------------------------------- comparator
def agrees(kind, c, asserted, model_expr, syms):
    """Deterministic check: is the model's probe answer CONSISTENT with the asserted
    relation? Returns True (agrees) / False (disagrees) / None (abstain: unparseable)."""
    if model_expr is None:
        return None
    L = syms[c["lhs"]]
    try:
        if kind in ("forward", "scaling_fallback"):
            return sp.simplify(model_expr - asserted) == 0
        if kind == "inverse":
            iv = syms[c["inv"]]
            sols = sp.solve(sp.Eq(L, asserted), iv)
            if not sols: return None
            return any(sp.simplify(model_expr - s) == 0 for s in sols)
        if kind in ("numA", "numB"):
            pt = c["ptA"] if kind == "numA" else c["ptB"]
            sub = {syms[k]: v for k, v in pt.items()}
            want = sp.N(asserted.subs(sub))
            got  = sp.N(model_expr.subs(sub)) if model_expr.free_symbols else sp.N(model_expr)
            if not (want.is_finite and got.is_finite): return None
            den = max(abs(float(want)), abs(float(got)), 1e-12)
            return abs(float(want) - float(got)) / den < 1e-6
        if kind == "scaling":
            if not c["scale"]: return None
            sv = syms[c["scale"]]
            want = sp.simplify(asserted.subs(sv, 2*sv) / asserted)
            return sp.simplify(model_expr - want) == 0
        if kind == "zeroform":
            F = model_expr
            if L not in F.free_symbols: return None
            # F = 0 must be equivalent to L = asserted
            return sp.simplify(sp.solve(sp.Eq(F, 0), L)[0] - asserted) == 0 \
                   if sp.solve(sp.Eq(F, 0), L) else None
    except Exception:
        return None
    return None

# ---------------------------------------------------------------- run
def run(model, k=6, out=None):
    rows = []
    for c in CLAIMS:
        syms = {n: sp.Symbol(n, positive=True) for n in (c["vars"].split() + [c["lhs"]])}
        for cond in ("true", "corrupt"):
            a_str = c[cond]
            asserted = sp.sympify(a_str, locals=syms)
            # ---- protocol P (pāṭha)
            for kind, prompt in probes(c, a_str):
                t0 = time.time()
                txt = gen(model, prompt, 0.2)
                dt = time.time() - t0
                e = parse(extract(txt, as_equation=(kind == "zeroform")), syms)
                kk = "scaling_fallback" if (kind == "scaling" and not c["scale"]) else kind
                rows.append(dict(claim=c["id"], cond=cond, proto="patha", probe=kind,
                                 raw=txt.strip()[:200], agree=agrees(kk, c, asserted, e, syms), sec=dt))
            # ---- protocol S (self-consistency)
            p = sc_probe(c, a_str)
            for i in range(k):
                t0 = time.time()
                txt = gen(model, p, 0.8, seed=1000+i)
                dt = time.time() - t0
                e = parse(extract(txt), syms)
                rows.append(dict(claim=c["id"], cond=cond, proto="sc", probe=f"sample{i}",
                                 raw=txt.strip()[:200], agree=agrees("forward", c, asserted, e, syms), sec=dt))
        print(f"  done {c['id']}", flush=True)
    if out:
        json.dump(rows, open(out, "w"), indent=1)
    return rows

def report(rows, k=6):
    def flag(claim, cond, proto):
        rs = [r for r in rows if r["claim"] == claim and r["cond"] == cond and r["proto"] == proto]
        dis = sum(1 for r in rs if r["agree"] is False)
        abst = sum(1 for r in rs if r["agree"] is None)
        return dis > 0, dis, abst
    ids = sorted({r["claim"] for r in rows})
    print("\n%-11s | %-28s | %-28s" % ("claim", "CORRUPTED asserted", "TRUE asserted"))
    print("%-11s | %-13s %-14s | %-13s %-14s" % ("", "patha", "self-cons", "patha", "self-cons"))
    print("-"*76)
    tally = {(p, c): 0 for p in ("patha", "sc") for c in ("true", "corrupt")}
    absten = {(p, c): 0 for p in ("patha", "sc") for c in ("true", "corrupt")}
    for i in ids:
        cells = []
        for cond in ("corrupt", "true"):
            for proto in ("patha", "sc"):
                f, d, a = flag(i, cond, proto)
                tally[(proto, cond)] += f
                absten[(proto, cond)] += a
                cells.append(f"{'FLAG' if f else ' -- '} {d}/{k}" + (f" a{a}" if a else "    "))
        print("%-11s | %-13s %-14s | %-13s %-14s" % (i, cells[0], cells[1], cells[2], cells[3]))
    n = len(ids)
    print("-"*76)
    print(f"\nn = {n} claims, k = {k} calls per claim per protocol "
          f"(total {len(rows)} generations)\n")
    print(f"RECALL   (corrupted claim flagged): patha {tally[('patha','corrupt')]}/{n} "
          f"= {100*tally[('patha','corrupt')]/n:.1f}%   |   "
          f"self-consistency {tally[('sc','corrupt')]}/{n} = {100*tally[('sc','corrupt')]/n:.1f}%")
    print(f"FALSE ALARM (true claim flagged)  : patha {tally[('patha','true')]}/{n} "
          f"= {100*tally[('patha','true')]/n:.1f}%   |   "
          f"self-consistency {tally[('sc','true')]}/{n} = {100*tally[('sc','true')]/n:.1f}%")
    print(f"abstentions (unparseable/undecidable probe answers): "
          f"patha {absten[('patha','corrupt')]+absten[('patha','true')]}, "
          f"sc {absten[('sc','corrupt')]+absten[('sc','true')]} of {n*k} each")
    # per-probe contribution
    print("\nper-probe disagreement rate on CORRUPTED claims (pāṭha):")
    for kind in ("forward","inverse","numA","numB","scaling","zeroform"):
        rs = [r for r in rows if r["proto"]=="patha" and r["cond"]=="corrupt" and r["probe"]==kind]
        d = sum(1 for r in rs if r["agree"] is False); a = sum(1 for r in rs if r["agree"] is None)
        print(f"  {kind:9s} {d}/{len(rs)} disagree, {a} abstain")
    print("\nper-probe FALSE-alarm rate on TRUE claims (pāṭha):")
    for kind in ("forward","inverse","numA","numB","scaling","zeroform"):
        rs = [r for r in rows if r["proto"]=="patha" and r["cond"]=="true" and r["probe"]==kind]
        d = sum(1 for r in rs if r["agree"] is False); a = sum(1 for r in rs if r["agree"] is None)
        print(f"  {kind:9s} {d}/{len(rs)} disagree, {a} abstain")
    secs = [r["sec"] for r in rows]
    print(f"\nlatency per generation: median {median(secs):.2f}s  total {sum(secs)/60:.1f} min")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="gemma3:4b")
    ap.add_argument("--k", type=int, default=6)
    ap.add_argument("--out", default=None)
    ap.add_argument("--load", default=None)
    a = ap.parse_args()
    if a.load:
        report(json.load(open(a.load)), a.k)
    else:
        print(f"model={a.model} k={a.k} claims={len(CLAIMS)}", flush=True)
        report(run(a.model, a.k, a.out), a.k)

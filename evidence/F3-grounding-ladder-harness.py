"""
Grounding-ladder coverage/cost experiment.

Backs the MEASURED-BENCH figures in research/raw/F3-executable-verifiable.md §4.2.
Run:  pip install sympy pint  &&  python F3-grounding-ladder-harness.py
Measured with SymPy 1.14.0 / pint 0.25.3 / Python 3.12 on 2026-07-27.

NOTE ON LABELS: the internal identifiers below (L2/L3/L5) predate the tier names
used in the section. The mapping is:
    L5 in this file  ->  tier L2a (dimensional)  in F3
    L2 in this file  ->  tier L2b (numeric)      in F3
    L3 in this file  ->  tier L3  (symbolic)     in F3

Setup: for each textbook formula we have a REFERENCE expression (ground truth).
A generator (an LLM, a student) emits a CANDIDATE. Three cheap checkers decide
whether candidate == reference:

  numeric     : random substitution, 8 trials, rtol 1e-9
  symbolic    : sympy simplify(candidate - reference) == 0
  dimensional : pint dimensionality(candidate) == dimensionality(reference)

Candidates come in three flavours:
  (a) IDENTICAL          -> all tiers must say "agree"
  (b) EQUIVALENT REWRITE -> semantically equal, syntactically different.
                            Any "disagree" is a FALSE ALARM.
  (c) MUTANT             -> genuinely wrong. Any "agree" is a MISS.

Mutations model real derivation errors: sign flip, factor of 2, factor of 1/2,
exponent off by one, dropped additive term, wrong variable.
"""
import time, random, json, statistics, collections
import sympy as sp
import pint

UREG = pint.UnitRegistry()
S = sp.symbols

x, y, t, v, c, m, k, g, h, r, L, T, w, a, b, n, u = sp.symbols(
    'x y t v c m k g h r L T w a b n u', positive=True)

# ---------------------------------------------------------------- corpus
# (name, reference_expr, [equivalent rewrites], dims|None, result_unit|None)
CORPUS = [
    ("binomial_square", (x + a)**2,
     [sp.expand((x + a)**2), x*x + a*x + x*a + a*a], None, None),
    ("geometric_series_sum", 1/(1 - x),
     [(1 - x)**-1, sp.Rational(1,1)/(1 - x)], None, None),
    ("product_rule_xsinx", sp.sin(x) + x*sp.cos(x),
     [sp.diff(x*sp.sin(x), x), x*sp.cos(x) + sp.sin(x)], None, None),
    ("gaussian_integral", sp.sqrt(sp.pi/a),
     [sp.pi**sp.Rational(1,2)*a**sp.Rational(-1,2),
      sp.integrate(sp.exp(-a*x**2), (x, -sp.oo, sp.oo))], None, None),
    ("cos_double_angle", 1 - 2*sp.sin(x)**2,
     [sp.cos(2*x), 2*sp.cos(x)**2 - 1, sp.cos(x)**2 - sp.sin(x)**2], None, None),
    ("taylor_sin_o4", x - x**3/6,
     [x*(1 - x**2/6), (6*x - x**3)/6], None, None),
    ("cubic_expansion", a**3 + 3*a**2*b + 3*a*b**2 + b**3,
     [(a + b)**3, sp.expand((a + b)**3)], None, None),
    ("log_product", sp.log(x) + sp.log(y),
     [sp.log(x*y), sp.log(x) + sp.log(y)], None, None),
    ("pythagorean_identity", sp.Integer(1),
     [sp.sin(x)**2 + sp.cos(x)**2, sp.cosh(x)**2 - sp.sinh(x)**2], None, None),
    ("partial_fractions", 1/(x*(x + 1)),
     [1/x - 1/(x + 1), sp.apart(1/(x*(x+1)), x)], None, None),

    # ---- dimensioned physics formulas ----
    ("kinetic_energy", m*v**2/2,
     [sp.Rational(1,2)*m*v*v, m*v**2*sp.Rational(1,2)],
     {'m': 'kilogram', 'v': 'meter/second'}, 'joule'),
    ("pendulum_period", 2*sp.pi*sp.sqrt(L/g),
     [2*sp.pi*sp.sqrt(L)/sp.sqrt(g), sp.sqrt(4*sp.pi**2*L/g)],
     {'L': 'meter', 'g': 'meter/second**2'}, 'second'),
    ("spring_energy", k*x**2/2,
     [sp.Rational(1,2)*k*x**2], {'k': 'newton/meter', 'x': 'meter'}, 'joule'),
    ("escape_velocity", sp.sqrt(2*g*r),
     [sp.sqrt(2)*sp.sqrt(g)*sp.sqrt(r), (2*g*r)**sp.Rational(1,2)],
     {'g': 'meter/second**2', 'r': 'meter'}, 'meter/second'),
    ("photon_energy", h*c/L,
     [h*c*L**-1, c*h/L], {'h': 'joule*second', 'c': 'meter/second', 'L': 'meter'}, 'joule'),
    ("lorentz_factor", 1/sp.sqrt(1 - v**2/c**2),
     [(1 - v**2/c**2)**sp.Rational(-1,2), c/sp.sqrt(c**2 - v**2)],
     {'v': 'meter/second', 'c': 'meter/second'}, 'dimensionless'),
    ("free_fall_distance", g*t**2/2,
     [sp.Rational(1,2)*g*t*t], {'g': 'meter/second**2', 't': 'second'}, 'meter'),
    ("momentum", m*v, [v*m], {'m': 'kilogram', 'v': 'meter/second'},
     'kilogram*meter/second'),
    ("centripetal_accel", v**2/r,
     [v*v/r, v**2*r**-1], {'v': 'meter/second', 'r': 'meter'}, 'meter/second**2'),
    ("grav_potential_energy", m*g*h,
     [g*h*m], {'m': 'kilogram', 'g': 'meter/second**2', 'h': 'meter'}, 'joule'),
]

# ---------------------------------------------------------------- mutations
def mut_sign(e):
    ts = sp.Add.make_args(sp.expand(e))
    if len(ts) > 1:
        i = random.randrange(len(ts))
        return sp.Add(*[(-q if j == i else q) for j, q in enumerate(ts)])
    return -e

def mut_x2(e):   return e*2
def mut_half(e): return e/2

def mut_exp(e):
    ps = sorted([p for p in e.atoms(sp.Pow)
                 if p.exp.is_Number and p.exp.is_integer and p.exp > 0],
                key=sp.default_sort_key)
    if ps:
        p = random.choice(ps)
        return e.subs(p, sp.Pow(p.base, p.exp + 1), simultaneous=True)
    fs = sorted(e.free_symbols, key=sp.default_sort_key)
    return e*random.choice(fs) if fs else e + 1

def mut_drop(e):
    ts = sp.Add.make_args(sp.expand(e))
    if len(ts) > 1:
        i = random.randrange(len(ts))
        return sp.Add(*[q for j, q in enumerate(ts) if j != i])
    return e - 1

def mut_swap(e):
    fs = sorted(e.free_symbols, key=sp.default_sort_key)
    if len(fs) < 2: return e
    p, q = random.sample(fs, 2)
    return e.subs(p, q, simultaneous=True)

MUTS = [("sign_flip", mut_sign), ("factor_2", mut_x2), ("factor_half", mut_half),
        ("exponent_off_by_one", mut_exp), ("dropped_term", mut_drop),
        ("wrong_variable", mut_swap)]

# ---------------------------------------------------------------- tiers
def L2(cand, ref, trials=8):
    fs = sorted(cand.free_symbols | ref.free_symbols, key=sp.default_sort_key)
    for _ in range(trials):
        sub = {s: sp.Float(random.uniform(0.31, 0.87)) for s in fs}
        try:
            d = complex(sp.N((cand - ref).subs(sub)))
            sc = abs(complex(sp.N(cand.subs(sub)))) + abs(complex(sp.N(ref.subs(sub)))) + 1e-30
        except Exception:
            return None
        if abs(d) > 1e-9*sc:
            return False
    return True

def L3(cand, ref):
    try:
        d = sp.simplify(cand - ref)
        if d == 0: return True
        return sp.simplify(sp.trigsimp(sp.powsimp(sp.expand(d), force=True))) == 0
    except Exception:
        return None

def dimof(e, dims):
    if dims is None: return None
    try:
        ns = {s.name: 1.0*UREG(dims[s.name]) for s in e.free_symbols}
    except KeyError:
        return None
    ns.update({'sqrt': lambda q: q**0.5, 'pi': 3.141592653589793,
               'sin': lambda q: 0.5, 'cos': lambda q: 0.5,
               'exp': lambda q: 0.5, 'log': lambda q: 0.5})
    try:
        code = sp.printing.pycode(e).replace('math.', '')
        q = eval(code, {'__builtins__': {}}, ns)
        return q.dimensionality if hasattr(q, 'dimensionality') else UREG('').dimensionality
    except pint.DimensionalityError:
        return 'INCONSISTENT'
    except Exception:
        return None

def L5(cand, dims, unit):
    if dims is None: return None
    d = dimof(cand, dims)
    if d is None: return None
    if d == 'INCONSISTENT': return False     # pint raised: the expression adds unlike units
    return d == (1.0*UREG(unit)).dimensionality

# ---------------------------------------------------------------- run
rows = []
def run(name, kind, mut, cand, ref, dims, unit):
    t0 = time.perf_counter(); r2 = L2(cand, ref); d2 = time.perf_counter()-t0
    t0 = time.perf_counter(); r3 = L3(cand, ref); d3 = time.perf_counter()-t0
    t0 = time.perf_counter(); r5 = L5(cand, dims, unit); d5 = time.perf_counter()-t0
    rows.append(dict(formula=name, kind=kind, mutation=mut,
                     L2=r2, L3=r3, L5=r5, d2=d2, d3=d3, d5=d5,
                     cand=str(cand)))

for name, ref, eqs, dims, unit in CORPUS:
    run(name, 'identical', '-', ref, ref, dims, unit)
    for i, e in enumerate(eqs):
        run(name, 'equivalent', 'rewrite%d' % i, e, ref, dims, unit)
    for mn, fn in MUTS:
        random.seed(abs(hash((name, mn))) % (2**31))
        try: bad = fn(ref)
        except Exception: continue
        if sp.simplify(bad - ref) == 0:      # no-op mutation
            continue
        run(name, 'mutant', mn, bad, ref, dims, unit)

# ---------------------------------------------------------------- report
ident = [r for r in rows if r['kind'] == 'identical']
equiv = [r for r in rows if r['kind'] == 'equivalent']
mut   = [r for r in rows if r['kind'] == 'mutant']
dimd  = [r for r in rows if r['L5'] is not None]

print("corpus: %d formulas | %d identical | %d equivalent rewrites | %d mutants"
      % (len(CORPUS), len(ident), len(equiv), len(mut)))
print("(%d of %d formulas carry physical dimensions)"
      % (sum(1 for cc in CORPUS if cc[3]), len(CORPUS)))
print()

print("=== RECALL: fraction of WRONG candidates the tier flags ===")
for tier in ('L2','L3','L5'):
    ap = [r for r in mut if r[tier] is not None]
    ca = sum(1 for r in ap if r[tier] is False)
    print("  %s  %3d/%3d = %5.1f%%   (abstained on %d of %d mutants)"
          % (tier, ca, len(ap), 100*ca/len(ap) if ap else 0,
             len(mut)-len(ap), len(mut)))
print()

print("=== FALSE ALARMS on semantically EQUIVALENT rewrites ===")
for tier in ('L2','L3','L5'):
    ap = [r for r in equiv if r[tier] is not None]
    fa = sum(1 for r in ap if r[tier] is False)
    print("  %s  %3d/%3d = %5.1f%% falsely flagged" %
          (tier, fa, len(ap), 100*fa/len(ap) if ap else 0))
    for r in ap:
        if r[tier] is False:
            print("        MISFIRE %-24s %s  cand=%s" % (r['formula'], r['mutation'], r['cand']))
print()

print("=== RECALL BY ERROR TYPE ===")
by = collections.defaultdict(lambda: collections.defaultdict(lambda: [0,0]))
for r in mut:
    for tier in ('L2','L3','L5'):
        if r[tier] is None: continue
        by[r['mutation']][tier][1] += 1
        if r[tier] is False: by[r['mutation']][tier][0] += 1
print("  %-22s %-12s %-12s %-12s" % ("error type","L2 numeric","L3 symbolic","L5 dimensional"))
for mn,_ in MUTS:
    cells=[]
    for tier in ('L2','L3','L5'):
        cnt,tot = by[mn][tier]
        cells.append("%d/%d"%(cnt,tot) if tot else "n/a")
    print("  %-22s %-12s %-12s %-12s" % (mn,*cells))
print()

print("=== L5 restricted to the 10 dimensioned physics formulas ===")
dm = [r for r in mut if r['L5'] is not None]
by5 = collections.defaultdict(lambda: [0,0])
for r in dm:
    by5[r['mutation']][1]+=1
    if r['L5'] is False: by5[r['mutation']][0]+=1
for mn,_ in MUTS:
    c,tt = by5[mn]
    if tt: print("  %-22s caught %d/%d" % (mn,c,tt))
print()

print("=== COST: wall clock per check (seconds) ===")
for tier,key in (('L2','d2'),('L3','d3'),('L5','d5')):
    vs = sorted(r[key] for r in rows)
    print("  %s  median %.5f  mean %.5f  p95 %.5f  max %.5f   (n=%d)"
          % (tier, statistics.median(vs), statistics.mean(vs),
             vs[int(.95*len(vs))], vs[-1], len(vs)))
print()

# ---- L3's hard boundary: zero-equivalence (Wester section L / Richardson) ----
print("=== L3 BOUNDARY: known-hard zero-equivalence cases ===")
hard = [
 ("sqrt(x)*sqrt(y) - sqrt(x*y)  (true only for x,y>=0)",
  sp.sqrt(S('p'))*sp.sqrt(S('q')) - sp.sqrt(S('p')*S('q'))),
 ("log(exp(z)) - z  (true only in a branch)", sp.log(sp.exp(S('z'))) - S('z')),
 ("2**(1/3)*(1+... ) nested radical", sp.sqrt(2 + sp.sqrt(3)) - (sp.sqrt(6)+sp.sqrt(2))/2),
 ("Wester L: (x+1)^(1/3) vs radical rewrite",
  ((x+1)**sp.Rational(1,3))**3 - (x+1)),
 ("exp/log tangle", sp.exp(sp.log(x)+sp.log(y)) - x*y),
]
for lab, e in hard:
    t0=time.perf_counter()
    try:
        res = sp.simplify(e)
        ok = (res == 0)
    except Exception as ex:
        res, ok = 'ERROR:%s'%ex, None
    dt=time.perf_counter()-t0
    print("  %-52s simplify->%-18s zero=%s  (%.3fs)" % (lab, str(res)[:18], ok, dt))

json.dump(rows, open('ladder2_results.json','w'), indent=1, default=str)
print("\nwrote ladder2_results.json")

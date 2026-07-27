"""Shannon entropy: the uniform distribution maximises it."""
import math
def H(p): return -sum(q*math.log2(q) for q in p if q > 0)
cases = [[1.0], [0.5,0.5], [0.25]*4, [0.9,0.1], [0.7,0.2,0.1]]
for p in cases: print(f"H({p}) = {H(p):.4f} bits")
assert abs(H([0.25]*4) - 2.0) < 1e-12, "uniform over 4 outcomes must be exactly 2 bits"
assert H([0.9,0.1]) < H([0.5,0.5]), "uniform must maximise entropy"
assert H([1.0]) == 0.0

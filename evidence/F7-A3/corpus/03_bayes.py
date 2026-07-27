"""Base rates: the screening-test paradox, computed rather than asserted in prose."""
prev, sens, spec = 0.001, 0.99, 0.99
p_pos = sens*prev + (1-spec)*(1-prev)
ppv = sens*prev/p_pos
print(f"prevalence      {prev:.4f}")
print(f"P(positive)     {p_pos:.6f}")
print(f"P(disease|+)    {ppv:.6f}")
assert ppv < 0.10, "a 99%/99% test on a 1-in-1000 disease must have PPV under 10%"
assert abs(ppv - (sens*prev)/(sens*prev+(1-spec)*(1-prev))) < 1e-15

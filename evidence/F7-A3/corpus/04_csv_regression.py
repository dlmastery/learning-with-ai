"""Read the same tiny dataset the figures are drawn from."""
import csv, pathlib
rows = list(csv.DictReader(open(pathlib.Path(__file__).parent/"data"/"tiny.csv")))
xs = [float(r["x"]) for r in rows]; ys = [float(r["y"]) for r in rows]
n = len(xs); mx = sum(xs)/n; my = sum(ys)/n
w = sum((x-mx)*(y-my) for x,y in zip(xs,ys)) / sum((x-mx)**2 for x in xs)
print(f"n={n} slope={w:.4f} intercept={my-w*mx:.4f}")
assert n == 5 and 2.0 < w < 2.5

"""Least squares by gradient descent, checked against the closed form."""
xs = [1.0, 2.0, 3.0, 4.0, 5.0]
ys = [2.1, 3.9, 6.2, 7.8, 10.1]
n = len(xs)
mx, my = sum(xs)/n, sum(ys)/n
sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
sxx = sum((x-mx)**2 for x in xs)
w_closed, b_closed = sxy/sxx, my - (sxy/sxx)*mx
w, b, lr = 0.0, 0.0, 0.01
for _ in range(20000):
    dw = -2/n * sum(x*(y-(w*x+b)) for x, y in zip(xs, ys))
    db = -2/n * sum((y-(w*x+b)) for x, y in zip(xs, ys))
    w, b = w - lr*dw, b - lr*db
print(f"closed form : w={w_closed:.6f} b={b_closed:.6f}")
print(f"grad descent: w={w:.6f} b={b:.6f}")
assert abs(w - w_closed) < 1e-4, "gradient descent did not reach the closed form"
assert abs(b - b_closed) < 1e-4

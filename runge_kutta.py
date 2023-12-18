# Runge Kutta
# penyelesaian persamaan matematika menggunakan metode Runge Kutta
# dy/dx = e^2x-3y^(3/2)

import math


def f(x, y):
  return math.exp(2 * x) - 3 * math.pow(y, 3 / 2)


def k(h, x0, y0):
  return h * f(x0, y0)


def main():
  x = float(input("initial value of x (x0) : "))
  y = float(input("initial value of x (y0) : "))
  h = float(input("step size (h) : "))
  xn = float(input("target value of x (xt) : "))

  step = 1
  while (x + h) <= xn:
    print(f"\nf({x}, {y}) : { f(x, y)}")

    k1_ = k(h, x, y)
    print("k1 = h * f(x0, y0) =", k1_)
    k2_ = k(h, x + (h / 2), y + (k1_ / 2))
    print("k2 = h * f(x0 + h/2, y0 + k1/2) = ", k2_)
    k3_ = k(h, x + (h / 2), y + (k2_ / 2))
    print(f"k3 = h * f(x0 + h/2, y0 + k2/2) = {k3_}")
    k4_ = k(h, x + h, y + k3_)
    print(f"k4 = h * f(x0 + h, y0 + k3) = {k4_}")
    y = y + (1 / 6) * (k1_ + (2 * k2_) + (2 * k3_) + k4_)
    print(f"y{step} = y0 + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4) = {y}")
    x = x + h
    step = step + 1


if __name__ == "__main__":
  main()


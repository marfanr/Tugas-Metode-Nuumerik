import math

def f(x, y):
  return math.exp(2 * x) - 3 * math.pow(y, 3 / 2)

def main():
  print("solution for e^2x - 3*y^(3/2) sing euler method")
  h = float(input("step size (h) : "))
  xt = float(input("target of x (xt) : "))
  x0 = float(input("intial value of x (x0) : "))
  y0 = float(input("intial value of y (y0) : "))
  print("\nf(x0, y0) = ", f(x0, y0))

  step = 1
  while x0 < xt:
    y1 = y0 + (h * f(x0, y0))
    print(f"step{step}: y{step} = y{step-1} + h * f(x{step-1},y{step-1}) = {y1}")
    
    y0 = y1    
    x0 = x0 + h
    step = step + 1

  print(f"y({xt}) = {y0}")

if __name__ == "__main__":
  main()

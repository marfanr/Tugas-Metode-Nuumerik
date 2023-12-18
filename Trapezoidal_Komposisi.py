# Trapezoidal Composition Method
import math


# Define function to integrate
def f(x):
  return 1/(math.pow(x,3)+math.pow(x,2))


# Implementing trapezoidal method
def trapezoidal(x0, xn, n):
  # calculating step size
  h = (xn - x0) / n

  # Finding sum
  integration = f(x0) + f(xn)
  sigma = 0
  for i in range(1, (n)):
    sigma = sigma + f(i)
  integration = integration + (2 * sigma)

  # Finding final integration value
  integration = (h / 2) * integration

  return integration


# Input section
print("f(x) = (x^3+x^2)^-1")
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal Compotition method is: %0.6f" %
      result)

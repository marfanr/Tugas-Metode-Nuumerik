# Simpson's 1/3 Rule

# Define function to integrate
import math
import sympy as sym
def f(x):
    return 1/(math.pow((x-1),1.5)*(math.pow((x-2), 0.5)))

# Implementing Simpson's 1/3 
def simpson13(x0,xn):
    # calculating step size
    h = (xn - x0) / 2

    # Finding sum 
    integration = f(x0) + f(xn)

    c = (xn+x0)/2
    integration = integration + 4*f(c)  

    # Finding final integration value
    integration = integration * h/3

    return integration

# Input section
print("f(x) = sec (x)")
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))

# Call trapezoidal() method and get result
result = simpson13(lower_limit, upper_limit)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )
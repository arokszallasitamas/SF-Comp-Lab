# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:16:58 2026

@author: arokszat
"""

# The function I chose is f(x) = x^2 + x - 30

# x is the value where the f(x) will be calculated
def value_of_fx(x):
    return x ** 2 + x - 30

# plots the function in the range of [-8, 8]
import numpy as np
import matplotlib.pylab as plt 


x = np.arange(-8.0, 8.0, 0.2)
a = 1
b = 1
c = -30

plt.plot(x, a * x * x + b * x + c)
plt.plot(x, 0.0 * x)


x1 = 0
x3 = -8

# checks if the values are initialized correctly
if value_of_fx(x1) >= 0:
    print("x1 not initialised corectly")
if value_of_fx(x3) <= 0:
    print("x3 not initialised corectly")

x2 = 0.5 * (x1 + x3)

if value_of_fx(x2) > 0:
    x3 = x2
else:
    x1 = x2

print(f"x1: {x1}")
print(f"x3: {x3}")

plt.plot(x2, a * x2 * x2 + b * x2 + c, 'ro')
nsteps = 1

tol = 0.0001
while (tol < abs(value_of_fx(x2))):
    x2 = 0.5 * (x1 + x3)
    if value_of_fx(x2) > 0:
        x3 = x2
    else:
        x1 = x2
    nsteps += 1

print(f"x2 after while loop: {x2}")
print(f"f(x2) after while loop: {value_of_fx(x2)}")

plt.plot(x2, a * x2 * x2 + b * x2 + c, 'yo')
plt.show()

print(nsteps)

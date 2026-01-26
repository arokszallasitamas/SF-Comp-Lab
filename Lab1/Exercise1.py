# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 16:16:58 2026

@author: arokszat
"""

# The function I chose is f(x) = x^2 + x - 30

# x is the value where the f(x) will be calculated
def value_of_fx(x, args):
    return args[0] * x ** 2 + args[1] * x + args[2]

# plots the function in the range of [-8, 8]
import numpy as np
import matplotlib.pylab as plt 


x = np.arange(-8.0, 8.0, 0.2)
args = [1, 1, -30]

plt.plot(x, value_of_fx(x, args))
plt.plot(x, 0.0 * x)
#plt.show()

#initialize the starting points of the search
x1 = 0.2
x3 = 8.1

# checks if the values are initialized correctly
if value_of_fx(x1, args) >= 0:
    print("x1 not initialised corectly")
if value_of_fx(x3, args) <= 0:
    print("x3 not initialised corectly")

x2 = 0.5 * (x1 + x3)

if value_of_fx(x2, args) > 0:
    x3 = x2
else:
    x1 = x2

print(f"x1: {x1}")
print(f"x3: {x3}")

plt.plot(x2, value_of_fx(x2, args), 'ro')
#plt.show()
nsteps = 1

tol = 0.0001
while (tol < abs(value_of_fx(x2, args))):
    x2 = 0.5 * (x1 + x3)
    if value_of_fx(x2, args) > 0:
        x3 = x2
    else:
        x1 = x2
    nsteps += 1

print(f"x2 after while loop: {x2}")
print(f"f(x2) after while loop: {value_of_fx(x2, args)}")

plt.plot(x2, value_of_fx(x2, args), 'yo')
plt.show()

print(nsteps)

tol = 0.1
listtol = []
listtollog = []
listnsteps = []
for i in range(50):
    listtol.append(tol)
    listtollog.append(np.log10(tol))
    x1 = 0.2
    x3 = 8.1
    x2 = 0.5 * (x1 + x3)
    nsteps = 0
    while (tol < abs(value_of_fx(x2, args))):
        x2 = 0.5 * (x1 + x3)
        if value_of_fx(x2, args) > 0:
            x3 = x2
        else:
            x1 = x2
        nsteps += 1
    listnsteps.append(nsteps)
    tol /= 10

plt.plot(listtol, listnsteps)
plt.show()
plt.plot(listtollog, listnsteps)
plt.show()

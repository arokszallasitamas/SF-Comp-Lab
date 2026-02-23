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

plt.title("Parabola and x axis")
plt.plot(x, value_of_fx(x, args), label='x^2 + x - 30')
plt.plot(x, 0.0 * x, label='x-axis')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#initialize the starting points of the search
x1 = 0.3
x3 = -6.1

# checks if the values are initialized correctly
if value_of_fx(x1, args) >= 0:
    print("x1 not initialised corectly")
if value_of_fx(x3, args) <= 0:
    print("x3 not initialised corectly")

x2 = 0.5 * (x1 + x3)

plt.title("First midpoint")
plt.plot(x, value_of_fx(x, args), label='x^2 + x - 30')
plt.plot(x, 0.0 * x, label='x-axis')
plt.plot(x2, value_of_fx(x2, args), 'ro', label='initial point')
plt.plot(x1, value_of_fx(x1, args), 'yo', label='initial point')
plt.plot(x3, value_of_fx(x3, args), 'yo', label='initial point')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

if value_of_fx(x2, args) > 0:
    x3 = x2
else:
    x1 = x2
print(f"x1: {x1}")
print(f"x3: {x3}")

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

plt.title("Found value")
plt.plot(x, value_of_fx(x, args))
plt.plot(x, value_of_fx(x, args), label='x^2 + x - 30')
plt.plot(x, 0.0 * x, label='x-axis')
plt.plot(x2, value_of_fx(x2, args), 'yo', label='found point')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(nsteps)

tol = 0.1
listtol = []
listtollog = []
listnsteps = []
for i in range(13):
    listtol.append(tol)
    listtollog.append(np.log10(tol))
    x1 = 0.293653459892839
    x3 = 6.129084093284092
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

plt.title("Number of steps w.r.t. tolerance")
plt.plot(listtol, listnsteps, label='nsteps w.r.t tol')
plt.xlabel('Tolerance')
plt.ylabel('Number of steps')
plt.legend()
plt.show()
plt.title("Number of steps w.r.t. tolarence (log scale)")
plt.plot(listtollog, listnsteps, label='nsteps w.r.t tol')
plt.xlabel('Log(tolerance)')
plt.ylabel('Number of steps')
m, b = np.polyfit(listtollog, listnsteps, 1)
x = np.arange(-13, 0, 1)
plt.plot(x, m*x + b, color='red', label='Linear fit')
plt.legend()
plt.show()

print(f"m is {m}")
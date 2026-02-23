# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 15:02:40 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pylab as plt

def value_of_fx(x, args):
    return args[0] * x ** 2 + args[1] * x + args[2]

def der_value_of_fx(x, args):
    return args[0] * x * 2 + args[1]

x = np.arange(-12.0, 12.0, 0.2)
#args stores the arguments of a quadratic function a, b, c

args = [1, 1, -30] 
plt.title("The function and its derivative")
plt.plot(x, value_of_fx(x, args), label='f(x)')
plt.plot(x, der_value_of_fx(x, args), label='f\'(x)')
plt.plot(x, 0.0 * x)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

x1 = 1
x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
plt.title("Guess after one cycle")
plt.plot(x, value_of_fx(x, args), label='f(x)')
plt.plot(x, der_value_of_fx(x, args), label='f\'(x)')
plt.plot(x, 0.0 * x)
plt.plot(x1, value_of_fx(x1, args), 'ro', label='Guess after one cycle')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

nsteps = 1
tol = 0.0000000000001
while tol < abs(value_of_fx(x1, args)):
      x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
      nsteps += 1

print(f"The value of x1 is: {x1}")
print(f"Te value of f(x1) is {value_of_fx(x1, args)}")
print(nsteps)

plt.title("Found value")
plt.plot(x, value_of_fx(x, args), label='f(x)')
plt.plot(x, der_value_of_fx(x, args), label='f\'(x)')
plt.plot(x, 0.0 * x)
plt.plot(x1, value_of_fx(x1, args), 'ro', label='Root of f(x)')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

tol = 0.1
listtol = []
listtollog = []
listnsteps = []
for i in range(50):
    listtol.append(tol)
    listtollog.append(np.log10(tol))
    x1 = 0
    nsteps = 0
    while tol < abs(value_of_fx(x1, args)):
          x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
          nsteps += 1
    listnsteps.append(nsteps)
    tol /= 10

plt.title("Newton-Raphson method number of cycles vs tolerance")
plt.plot(listtol, listnsteps, label='Newton-Raphson method')
plt.xlabel("Tolerance")
plt.ylabel("Number of cycles")
plt.legend()
plt.show()
plt.title("Newton-Raphson method number of cycles vs log(tolerance)")
plt.plot(listtollog, listnsteps, label='Newton-Raphson method')
m, b = np.polyfit(listtollog, listnsteps, 1)
x = np.arange(-13, 0, 1)
plt.plot(x, m*x + b, color='red', label='Linear fit')
plt.xlabel("Log tolerance")
plt.ylabel("Number of cycles")
plt.legend()
plt.show()

print(m)
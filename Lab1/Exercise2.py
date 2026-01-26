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

x = np.arange(-8.0, 8.0, 0.2)
#args stores the arguments of a quadratic function a, b, c

args = [1, 1, -30] 
plt.plot(x, value_of_fx(x, args))
plt.plot(x, der_value_of_fx(x, args))
plt.plot(x, 0.0 * x)

x1 = 1
x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
plt.plot(x1, value_of_fx(x1, args), 'ro')
plt.show()

nsteps = 1
tol = 0.0001
while tol < abs(value_of_fx(x1, args)):
      x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
      nsteps += 1

print(f"The value of x1 is: {x1}")
print(f"Te value of f(x1) is {value_of_fx(x1, args)}")
print(nsteps)

tol = 0.1
listtol = []
listtollog = []
listnsteps = []
for i in range(10):
    listtol.append(tol)
    listtollog.append(np.log10(tol))
    x1 = 1
    nsteps = 0
    while tol < abs(value_of_fx(x1, args)):
          x1 = x1 - (value_of_fx(x1, args) / der_value_of_fx(x1, args))
          nsteps += 1
    listnsteps.append(nsteps)
    tol /= 10

plt.plot(listtol, listnsteps)
plt.show()
plt.plot(listtollog, listnsteps)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 15:40:43 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pylab as plt

def value_of_vx(x):
    return 1090 * np.exp(-x/0.033) - 1.44/x

def value_of_der_vx(x):
    return -1090 * np.exp(-x/0.033)/0.033 + 1.44/x**2

def value_of_doubleder_vx(x):
    return 1090 * np.exp(-x/0.033)/0.033**2 - 1.44/x**3

x = np.arange(0.2, 1, 0.01)
plt.plot(x, value_of_vx(x))
plt.plot(x, value_of_der_vx(x))
plt.show()

nsteps = 0
x1 = 0.2
tol = 0.1
listtol = []
listtollog = []
listnsteps = []
for i in range(10):
    listtol.append(tol)
    listtollog.append(np.log10(tol))
    x1 = 0.2
    nsteps = 0
    while tol < abs(value_of_der_vx(x1)):
          x1 = x1 - (value_of_der_vx(x1) / value_of_doubleder_vx(x1))
          nsteps += 1
    listnsteps.append(nsteps)
    tol /= 10

print(x1)
plt.plot(listtol, listnsteps)
plt.show()
plt.plot(listtollog, listnsteps)
plt.show()
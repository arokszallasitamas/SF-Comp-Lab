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

x = np.arange(0.1, 1, 0.01)
plt.title("Ionic potential")
plt.plot(x, value_of_vx(x))
plt.plot(x, 0.0 * x)
plt.xlabel("x (nm)")
plt.ylabel("V (eV)")
plt.show()

plt.title("Force between the ions")
plt.plot(x, -value_of_der_vx(x))
plt.plot(x, 0.0 * x)
plt.xlabel("x (nm)")
plt.ylabel("F (eV/nm)")
plt.show()

nsteps = 0
x1 = 0.2
tol = 0.1
while tol < abs(value_of_der_vx(x1)):
    x1 = x1 - (value_of_der_vx(x1) / value_of_doubleder_vx(x1))

print(f"The radius is {x1}")
x = np.arange(0.1, 1, 0.01)
plt.title("Minimum of potential")
plt.plot(x, value_of_vx(x))
plt.plot(x1, value_of_vx(x1), 'ro')
plt.plot(x, 0.0 * x)
plt.xlabel("x (nm)")
plt.ylabel("V (eV)")
plt.show()
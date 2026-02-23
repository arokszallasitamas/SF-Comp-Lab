# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 14:57:09 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pyplot as plt

#Task 1-2: Functions copied from Exercise1, f was modified to calculated sin(theta)
def f(theta, omega, t, k, A, phi):
    return -np.sin(theta)-k*omega+A*np.cos(phi*t)

def trap(theta, omega, dt, t, k, A, phi):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t, k, A, phi)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt, k, A, phi)
    theta = theta + (k1a + k2a) / 2
    omega = omega + (k1b + k2b ) / 2
    t = t + dt
    return theta, omega, t

k, phi, A = 0.0, 0.66667, 0.0
theta, omega, t, dt = 0.2, 0.0, 0.0, 0.01

#Task 3: Run the program for this non-linear pendulum as well
thetainit = [0.2, 1.0, 3.14, 0.0]
omegainit = [0.0, 0.0, 0.0, 1.0]
for i in range(4):
    listtheta = []
    listomega = []
    listtime = []
    theta = thetainit[i]
    omega = omegainit[i]
    t=0
    nsteps = 0
    for i in range(5000):
        listtime.append(t)
        listtheta.append(theta)
        listomega.append(omega)
        theta, omega, t = trap(theta, omega, dt, t, k, A, phi)

    plt.plot(listtime, listtheta, label='Theta')
    plt.plot(listtime, listomega, label='Omega')
    plt.legend()
    plt.axis(xmin=0, xmax=50, ymin=-np.pi, ymax=np.pi)
    plt.show()

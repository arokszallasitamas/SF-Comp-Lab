# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 15:04:00 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pyplot as plt

#Task 1-2: The Runge-Kutta algorithm is introduced as well
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

def rk(theta, omega, dt, t, k, A, phi):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t, k, A, phi)
    k2a = dt * (omega + k1b/2)
    k2b = dt * f(theta + k1a/2, omega + k1b/2, t + dt/2, k, A, phi)
    k3a = dt * (omega + k2b/2)
    k3b = dt * f(theta + k2a/2, omega + k2b/2, t + dt/2, k, A, phi)
    k4a = dt * (omega + k3b)
    k4b = dt * f(theta + k3a, omega + k3b, t + dt, k, A, phi)
    theta = theta + (k1a + 2*k2a + 2*k3a + k4a) / 6
    omega = omega + (k1b + 2*k2b + 2*k3b + k4b) / 6
    t = t + dt
    return theta, omega, t

#Task 3: Compare Runge-Kutta with the Trapezoid rule with the given initial conditions
#Trapezoid rule
k, phi, A = 0.0, 0.66667, 0.0
theta, omega, t, dt = 3.1415, 0.0, 0.0, 0.01

listtheta = []
listtime = []
for i in range(5000):
    listtime.append(t)
    listtheta.append(theta)
    theta, omega, t = trap(theta, omega, dt, t, k, A, phi)

plt.plot(listtime, listtheta, label='Theta')
plt.legend()
plt.axis(xmin=0, xmax=50, ymin=-np.pi, ymax=np.pi)
plt.show()

#Runge-Kutta
k, phi, A = 0.0, 0.66667, 0.0
theta, omega, t, dt, nsteps = 3.1415, 0.0, 0.0, 0.01, 0

listtheta = []
listomega = []
listtime = []
for i in range(5000):
    listtime.append(t)
    listtheta.append(theta)
    theta, omega, t = rk(theta, omega, dt, t, k, A, phi)

plt.plot(listtime, listtheta, label='Theta')
plt.legend()
plt.axis(xmin=0, xmax=50, ymin=-np.pi, ymax=np.pi)
plt.show()

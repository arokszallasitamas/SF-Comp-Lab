# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 15:30:17 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pyplot as plt

#Task 1-2: Exercise3 copied but k is changed to introduce damping 
def f(theta, omega, t, k, A, phi):
    return -np.sin(theta)-k*omega+A*np.cos(phi*t)

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

k, phi, A = 0.5, 0.66667, 0.0
theta, omega, t, dt = 3.0, 0.0, 0.0, 0.01


#Task3: Theta and omega plotted separately for the damped pendulum

listtheta = []
listomega = []
listtime = []
for i in range(2500):
    listtime.append(t)
    listtheta.append(theta)
    listomega.append(omega)
    theta, omega, t = rk(theta, omega, dt, t, k, A, phi)

plt.plot(listtime, listtheta, label='Theta')
plt.legend()
plt.axis(xmin=0, xmax=25, ymin=-np.pi, ymax=np.pi)
plt.show()
plt.plot(listtime, listomega, label='Omega')
plt.legend()
plt.axis(xmin=0, xmax=25, ymin=-np.pi, ymax=np.pi)
plt.show()

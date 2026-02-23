# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 15:35:57 2026

@author: arokszat
"""

import numpy as np
import matplotlib.pyplot as plt

#Task 1-2: Exercise4 copied but initial conditions were changed, a sinusoidal driving force is introduced
def f(theta, omega, t, k, A, phi):
    return -np.sin(theta)-k*omega+A*np.cos(phi*t)

def rk(theta, omega, dt, t, k, A, phi, iteration_number):
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
    iteration_number = iteration_number + 1
    return theta, omega, t, iteration_number


#Task3: Theta and omega plotted separately for the damped pendulum
Ainit = [0.90, 1.07, 1.35, 1.47, 1.5]
shift = [0, 0, 0, 1, 1]
for i in range(5):
    
    k, phi, A = 0.5, 0.66667, Ainit[i]
    theta, omega, t, dt = 3.0, 0.0, 0.0, 0.01

    #Task 3-4: Introduce variables to eliminate transient motion
    iteration_number = 0
    transient = 5000
    
    listtheta = []
    listomega = []
    listtime = []
    
    a = 0
    print(iteration_number)
    for j in range(7000):
        if (np.abs(theta-shift[i]) > np.pi):
            if theta > np.pi:
                a += 1
            else:
                a -= 1
            theta -= 2 * np.pi * np.abs(theta-shift[i]) / (theta-shift[i])

        if iteration_number > transient:
            listtime.append(t)
            listtheta.append(theta + 2 * a * np.pi)
            listomega.append(omega)
        
        theta, omega, t, iteration_number = rk(theta, omega, dt, t, k, A, phi, iteration_number)

    plt.plot(listtime, listtheta, label='Theta')
    plt.legend()
    plt.axis(xmin=listtime[0], xmax=listtime[len(listtime)-1], ymin=min(listtheta)-1, ymax=max(listtheta)+1)
    plt.show()
    plt.plot(listtime, listomega, label='Omega')
    plt.legend()
    plt.axis(xmin=listtime[0], xmax=listtime[len(listtime)-1], ymin=-np.pi, ymax=np.pi)
    plt.show()
import numpy as np
import matplotlib.pyplot as plt

#f calculates the function f(theta, omega, t) with sin(theta)=theta and g/l=1
def f(theta, omega, t, k, A, phi):
    return -theta-k*omega+A*np.cos(phi*t)

#modifies theta an omega to be theta(n+1) and omega(n+1)
def trap(theta, omega, dt, t, k, A, phi):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t, k, A, phi)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt, k, A, phi)
    theta = theta + (k1a + k2a) / 2
    omega = omega + (k1b + k2b ) / 2
    t = t + dt

k, phi, A = 0.0, 0.66667, 0.0
theta, omega, t, dt, nsteps = 0.2, 0.0, 0.0, 0.01, 0

for i in range(1000):
    plt.plot(theta, nsteps)
    plt.plot(omega, nsteps)
    trap(theta, omega, dt, t, k, A, phi)
    nsteps += 1
plt.show()
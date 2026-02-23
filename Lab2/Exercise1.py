import numpy as np
import matplotlib.pyplot as plt

#Task 1: f calculates the function f(theta, omega, t) with sin(theta)=theta and g/l=1
def f(theta, omega, t, k, A, phi):
    return -theta-k*omega+A*np.cos(phi*t)

#Task 5: modifies theta an omega to be theta(n+1) and omega(n+1)
def trap(theta, omega, dt, t, k, A, phi):
    k1a = dt * omega
    k1b = dt * f(theta, omega, t, k, A, phi)
    k2a = dt * (omega + k1b)
    k2b = dt * f(theta + k1a, omega + k1b, t + dt, k, A, phi)
    theta = theta + (k1a + k2a) / 2
    omega = omega + (k1b + k2b ) / 2
    t = t + dt
    return theta, omega, t

#Task 2-3: initialise all the variables
k, phi, A = 0.0, 0.66667, 0.0
theta, omega, t, dt, nsteps = 0.2, 0.0, 0.0, 0.01, 0

#Task 4: test if f works properly
theta1 = 0
omega1 = 0
t1 = 0
for i in range(10):
    #print(f"f({theta1}, {omega1}, {t1}) = {f(theta1, omega1, t1, k, A, phi)}")
    omega1 += 0.1
    theta1 += 0.2
    t1 += 0.05

#Task 6-8: Trapezoid rule in for loop, plot omega and theta in each step
listtheta = []
listomega = []
listnsteps = []
for i in range(1000):
    theta, omega, t = trap(theta, omega, dt, t, k, A, phi)
    listnsteps.append(nsteps)
    listtheta.append(theta)
    listomega.append(omega)
    nsteps += 1

plt.plot(listnsteps, listtheta, label='Theta')
plt.plot(listnsteps, listomega, label='Omega')
plt.legend()
plt.axis(xmin=0, xmax=500, ymin=-np.pi, ymax=np.pi)
plt.show()

#Task 9: Plot theta and omage with different initial conditions

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
    for i in range(1000):
        listtime.append(t)
        listtheta.append(theta)
        listomega.append(omega)
        theta, omega, t = trap(theta, omega, dt, t, k, A, phi)
        nsteps += 1

    plt.plot(listtime, listtheta, label='Theta')
    plt.plot(listtime, listomega, label='Omega')
    plt.legend()
    plt.axis(xmin=0, xmax=10, ymin=-np.pi, ymax=np.pi)
    plt.show()

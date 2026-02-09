# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:26:24 2026

@author: arokszat
"""
import numpy as np
import matplotlib.pylab as plt

def V_phi(q1, q2, phi, R):
    const = q1*q2/(4*np.pi*8.854*10**-12)
    return const/(np.abs(2*R*np.sin(phi/2)))

def F_phi(q1, q2, phi, R):
    const = q1*q2/(4*np.pi*8.854*10**-12)
    return const/((np.abs(2*R*np.sin(phi/2)))**2)

def dF_phi(q1, q2, phi, R):
    const = q1*q2/(4*np.pi*8.854*10**-12)
    return -2*const/((np.abs(2*R*np.sin(phi/2)))**3)

def d2F_phi(q1, q2, phi, R):
    const = q1*q2/(4*np.pi*8.854*10**-12)
    return -6*const/((np.abs(2*R*np.sin(phi/2)))**4)

phi = np.arange(-0.3, -np.pi, -0.01)
plt.plot(phi, V_phi(1, 1, phi, 1), 'r')
plt.plot(phi, F_phi(1, 1, phi, 1), 'b')
phi = np.arange(0.3, np.pi, 0.01)
plt.plot(phi, V_phi(1, 1, phi, 1), 'r')
plt.plot(phi, F_phi(1, 1, phi, 1), 'b')
phi = np.arange(-np.pi, np.pi, 0.01)
plt.plot(phi, 0.0 * phi, 'g')
plt.show()

print(f"The total energy for two charges for a ring is {V_phi(1, 1, np.pi, 1)} J")
print(f"The force acting on each charge is {-F_phi(1, 1, np.pi, 1)} N")

def F_charge1(q1, q2, q3, phi1, phi2, R):
    delta = phi2 - phi1
    F1 = F_phi(q1, q2, phi1, R)*np.cos(phi1/2)
    F2 = F_phi(q2, q3, delta, R)*np.cos(delta/2)
    return F1-F2

def F_charge2(q1, q2, q3, phi1, phi2, R):
    delta = phi2 - phi1
    theta = 2*np.pi-phi2
    F1 = F_phi(q3, q3, delta, R)*np.cos(delta/2)
    F2 = F_phi(q1, q3, theta, R)*np.cos(theta/2)
    return F1-F2

def dcos(phi, R):
    return -phi/(2*R**2*np.sqrt(4-phi**2/R**2))

def d2cos(phi, R):
    return -2/((4*R**2-phi**2)*np.sqrt(4-(phi**2/R**2)))

def dF_charge1(q1, q2, phi1, phi2, R):
    #delta = phi2 - phi1
    dF1 = dF_phi(q1, q2, phi1, R)*np.cos(phi1/2)
    dF2 = F_phi(q1, q2, phi1, R)*dcos(phi1, R)
    #dF2_1 = dF_phi(q1, q2, delta, R)*np.cos(delta/2)
    #dF2_2 = F_phi(q1, q2, delta, R)*dcos(delta)
    return dF1+dF2

def dF_charge2(q1, q3, phi1, phi2, R):
    #delta = phi2 - phi1
    theta = 2*np.pi-phi2
    #dF1_1 = dF_phi(q1, q2, delta, R)*np.cos(delta/2)
    #dF1_2 = F_phi(q1, q2, delta, R)*dcos(delta)
    dF1 = dF_phi(q1, q3, theta, R)*np.cos(theta/2)
    dF2 = F_phi(q1, q3, theta, R)*dcos(theta, R)
    return -dF1-dF2

def d2F_charge1(q1, q2, phi1, phi2, R):
    dF1_1 = d2F_phi(q1, q2, phi1, R)*np.cos(phi1/2)
    dF1_2 = dF_phi(q1, q2, phi1, R)*dcos(phi1, R)
    dF2_2 = F_phi(q1, q2, phi1, R)*d2cos(phi1, R)
    return dF1_1+2*dF1_2+dF2_2

def d2F_charge2(q1, q3, phi1, phi2, R):
    theta = 2*np.pi-phi2
    dF1_1 = d2F_phi(q1, q3, theta, R)*np.cos(theta/2)
    dF1_2 = dF_phi(q1, q3, theta, R)*dcos(theta, R)
    dF2_2 = F_phi(q1, q3, theta, R)*d2cos(theta, R)
    return -dF1_1-2*dF1_2-dF2_2



tol = 100000
q1 = 1
q2 = 1
q3 = 1
phi1 = 2.4
phi2 = 4
R = 100
print(F_charge1(q1, q2, q3, phi1, phi2, R))
while tol < abs(F_charge1(q1, q2, q3, phi1, phi2, R)):
    phi1 = phi1-2*np.arcsin(dF_charge1(q1, q2, phi1, phi2, R)/d2F_charge1(q1, q2, phi1, phi2, R)/2*R)
    while tol < abs(F_charge2(q1, q2, q3, phi1, phi2, R)):
        phi2 = phi2-2*np.arcsin(dF_charge2(q1, q3, phi1, phi2, R)/d2F_charge2(q1, q3, phi1, phi2, R)/2*R)
        
print(phi1)
print(phi2)

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:26:24 2026

@author: arokszat
"""
import numpy as np
import matplotlib.pylab as plt

def value_of_vq(q1, q2, phi, R):
    return (q1*q2/(4*np.pi*8.854*10**-12))/(np.abs(2*R*np.sin(phi/2)))

def value_of_fq(q1, q2, phi, R):
    return (q1*q2/(4*np.pi*8.854*10**-12))/(np.abs(2*R*np.sin(phi/2)**2))

phi = np.arange(-0.3, -np.pi, -0.01)
plt.plot(phi, value_of_vq(1, 1, phi, 1), 'r')
plt.plot(phi, value_of_fq(1, 1, phi, 1), 'b')
phi = np.arange(0.3, np.pi, 0.01)
plt.plot(phi, value_of_vq(1, 1, phi, 1), 'r')
plt.plot(phi, value_of_fq(1, 1, phi, 1), 'b')
phi = np.arange(-np.pi, np.pi, 0.01)
plt.plot(phi, 0.0 * phi, 'g')
plt.show()

#total energy for two charges, if there are two charges the separation is pi
total_e = value_of_vq(1, 1, np.pi, 1)
force = -value_of_fq(1, 1, np.pi, 1)
print(f"The total potential energy for a two charge system with R = 1 m, q1 = 1 C, q2 = 1 C is {total_e} J")
print(f"The forceacting on each charge with R = 1 m, q1 = 1 C, q2 = 1 C is {force} N")

#total energy for three charge system
def total_e_three_charge(q1, q2, q3, phi1, phi2, R):
    v12 = value_of_vq(q1, q2, phi1, R)
    v13 = value_of_vq(q1, q3, phi2, R)
    v23 = value_of_vq(q2, q3, phi2 - phi1, R)
    return v12 + v13 + v23

def dv_over_phi1(q1, q2, q3, phi1, phi2, R):
    return 1/(8*np.pi*8.854*10**-12*R)*(-q1*q2*(np.sin(phi1)/(4*np.abs(np.sin(phi1/2))**3)-q2*q3*(np.sin(phi1-phi2))/(4*np.abs(np.sin((phi2-phi1)/2))**3)))

def second_der_phi1(q1, q2, q3, phi1, phi2, R):
    return 1/(8*np.pi*8.854*10**-12*R)*(q1*q2*((np.sin(phi1/2)**2*(np.cos(phi1)+3))/(8*np.abs(np.sin(phi1/2))**5))+q2*q3*(3*np.sin(phi1-phi2)**2-4*np.sin((phi2-phi1)/2)**2*np.cos(phi1-phi2))/(16*np.abs(np.sin((phi2-phi1)/2))**5))

def dv_over_phi2(q1, q2, q3, phi1, phi2, R):
    return 1/(8*np.pi*8.854*10**-12*R)*(-q1*q3*(np.sin(phi2)/(4*np.abs(np.sin(phi2/2))**3)+q2*q3*(np.sin(phi1-phi2))/(4*np.abs(np.sin((phi2-phi1)/2))**3)))

def second_der_phi2(q1, q2, q3, phi1, phi2, R):
    return 1/(8*np.pi*8.854*10**-12*R)*(q1*q2*((np.sin(phi2/2)**2*(np.cos(phi2)+3))/(8*np.abs(np.sin(phi2/2))**5))+q2*q3*(3*np.sin(phi1-phi2)**2-4*np.sin((phi2-phi1)/2)**2*np.cos(phi1-phi2))/(16*np.abs(np.sin((phi2-phi1)/2))**5))

q1 = 1
q2 = 1
q3 = 1
tol = 0.0001
phi1 = 2*np.pi/3
phi2 = 4*np.pi/3
while tol < np.abs(dv_over_phi1(q1, q2, q3, phi1, phi2, 1)):
    phi1 = phi1 - (dv_over_phi1(q1, q2, q3, phi1, phi2, 1) / second_der_phi1(q1, q2, q3, phi1, phi2, 1))
    while tol < np.abs(dv_over_phi2(q1, q2, q3, phi1, phi2, 1)):
        phi2 = phi2 - (dv_over_phi2(q1, q2, q3, phi1, phi2, 1) / second_der_phi2(q1, q2, q3, phi1, phi2, 1))
    
print(phi1)
print(phi2)
    
    
    
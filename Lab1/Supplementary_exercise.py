# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 16:26:24 2026

@author: arokszat
"""
import numpy as np
import matplotlib.pylab as plt

def value_of_vq(q1, q2, phi, R):
    return (q1*q2/(4*np.pi*8.854*10**-12))/(np.abs(2*R*np.sin(phi/2)))

phi = np.arange(0, np.pi, 0.01)
plt.plot(phi, value_of_vq(1, 1, phi, 1))
plt.show()

#for two equal charges, phi1 = phi2


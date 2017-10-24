# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 21:19:12 2017

@author: jdk2py
"""
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

#Uniforme a=-2,b=3
def fUni(x,a=0,b=1):
    return stats.uniform.pdf(x, loc=a, scale=b-a)

x = np.arange(-4,4,0.01)
y = fUni(x,-2,3)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)
plt.show()

#Cauchy a=1
def fCau(x):
    return stats.cauchy.pdf(x)
x = np.arange(-4,4,0.01)
y = fCau(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)
plt.show()

#Gamma con alfa = 2 y beta =1
def fGam(x, a):
    return stats.gamma.pdf(x, a)
x = np.arange(0,20,0.01)
y = fGam(x, 5)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)
plt.show()

#Chi-cuadrada con 4 grados de libertad
def fChi2(x, nu):
    return stats.chi2.pdf(x, df=nu)
x = np.arange(0,20,0.01)
y = fChi2(x,4)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)
plt.show()

#Chi-cuadrada con 4 grados de libertad
def ft(x, nu):
    return stats.t.pdf(x, df=nu)
def Ft(x, nu):
    return stats.t.cdf(x, df=nu)
x = np.arange(-4,4,0.01)
y = ft(x,30)
yc = Ft(x,30)
fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.plot(x, yc, 'b', linewidth=2)
plt.ylim(ymin=0)
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 14:15:42 2017

@author: jdk2py
"""

from scipy import stats
import numpy as np

A0 = 20.
A = 21.2
s = 3.
n = 64.
b = 0.05

N = stats.norm(0,1)

def F(x):
    return N.cdf(x)
    
Z = (A-A0)/(s/np.sqrt(n))
print(Z)
print(F(Z))

pvalue = 1- F(Z)
print(pvalue)

print("A un nivel de significación de "+str(b))
if b<pvalue:
    print("se acepta la hipótesis nula.")
else:
    print("la hipótesis nula se rechaza.")
    

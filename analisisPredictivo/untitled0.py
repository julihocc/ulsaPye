#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:19:07 2017

@author: jdk2py
"""
from scipy.stats import chi2

def F(x):
    return chi2.cdf(x, df=1)

valorp = 1 - F(11.236)
print(valorp)

beta = 0.05

if valorp > beta:
    print("No se puede rechazar la hipótesis nula")
else:
    print("Se rechaza la hipótesis nula")
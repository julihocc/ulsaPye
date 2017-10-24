# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:22:03 2017

@author: jdk2py
"""


from scipy import stats

#7.16
mu = 1500
sigma = 350
nd = stats.norm(mu, sigma)

def F(x):
    return nd.cdf(x)
    
#a
print F(750)
#b
print 1-F(2000)

def inverseF(x):
    return nd.ppf(x)

#c
print inverseF(.90)
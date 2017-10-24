# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 21:22:03 2017

@author: jdk2py
"""


from scipy import stats
import math
import scipy.special

print math.factorial(5)
print scipy.special.binom(8,3)

#7.2 N=50, p=15%
def f(x):
    return stats.binom(50,.15).pmf(x)
def F(x):
    return stats.binom(50,.15).cdf(x)
#(a) P(X<=10)
print sum([f(x) for x in range(0,10+1)])
print F(10)
#(b) P(X>=5)
print 1-sum([f(x) for x in range(0,4+1)])
print 1-F(4)
#(c) P(3<=X<=6)
print sum([f(x) for x in range(3,6+1)])
print F(6)-F(2)
#(d) P(X=5)
print f(5)

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

#7.28
#a
N = 2000
p = 0.001
print stats.binom(N,p).pmf(3)
print stats.poisson(N*p).pmf(3)
#(b)
print 1-stats.binom(N,p).cdf(2)
print 1-stats.poisson(N*p).cdf(2)
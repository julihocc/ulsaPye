#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:39:01 2017

@author: jdk2py
"""

import pandas as pd
advert = pd.read_csv("./dataBases/Advertising.csv")

import matplotlib.pyplot as plt

plt.plot(advert['TV'],advert['Sales'],'ro')
plt.title('TV vs Sales')
plt.show()

plt.plot(advert['Radio'],advert['Sales'],'ro')
plt.title('Radio vs Sales')
plt.show()

plt.plot(advert['Newspaper'],advert['Sales'],'ro')
plt.title('Newspaper vs Sales')
plt.show()
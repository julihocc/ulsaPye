#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:01:07 2017

@author: jdk2py
"""

import pandas as pd
import statsmodels.formula.api as smf

advert = pd.read_csv("./dataBases/Advertising.csv")
model2=smf.ols(formula='Sales~TV+Newspaper',
               data=advert).fit()

print(model2.params)
print(model2.pvalues)
print(model2.rsquared)

sales_pred=model2.predict(advert[['TV','Newspaper']])
print(sales_pred.head())

#RSE
import numpy as np
advert['sales_pred']= 5.77 + 0.046901*advert['TV'] + \
                      0.044219*advert['Newspaper']
advert['SSD'] = (advert['Sales']- \
                  advert['sales_pred'])**2
SSD=advert.sum()['SSD']
n = len(advert["Sales"])
print("n",n)
p = 2
RSE=np.sqrt(SSD/(n-p-1))
print("RSE", RSE)
salesmean=np.mean(advert['Sales'])
print("salesmean", salesmean)
error=RSE/salesmean
print("error", error)
print(4*"\n")
print(model2.summary())
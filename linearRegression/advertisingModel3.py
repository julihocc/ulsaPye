#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:01:07 2017

@author: jdk2py
"""

import pandas as pd
import statsmodels.formula.api as smf

advert = pd.read_csv("./dataBases/Advertising.csv")
model3=smf.ols(formula='Sales~TV+Radio',data=advert).fit()
print(model3.params)
print(model3.pvalues)

a = model3.params[0]
btv = model3.params[1]
bradio = model3.params[2]

advert["sales_pred"] = a + btv * advert["TV"] + \
                        bradio * advert["Radio"]
                        
sales_pred=model3.predict(advert[['TV','Radio']])
print(sales_pred.head())

print(model3.summary())
                        
#RSE
import numpy as np

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
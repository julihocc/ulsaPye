#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:01:07 2017

@author: jdk2py
"""

import pandas as pd

advert = pd.read_csv("./dataBases/Advertising.csv")

import numpy as np

def rCoef(df, var1, var2):
    df["dX*dY"] = (df[var1]-np.mean(df[var1]))*(df[var2]-np.mean(df[var2]))
    df["dX**2"] = (df[var1]-np.mean(df[var1]))**2
    df["dY**2"] = (df[var2]-np.mean(df[var2]))**2
    sxy = df.sum()["dX*dY"]
    sxx = df.sum()["dX**2"]
    syy = df.sum()["dY**2"]
    r = sxy/np.sqrt(sxx*syy)
    return r

tvVsSales = rCoef(advert, "TV", "Sales")
radioVsSales = rCoef(advert, "Radio", "Sales")
newVsSales = rCoef(advert, "Newspaper", "Sales")
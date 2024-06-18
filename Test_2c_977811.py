# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:54:31 2020

@author: Morgan Bridge
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

data=np.array([[-2.00000000e+01, -2.22002789e-03],[-1.86666667e+01, -3.68792308e-03],[-1.73333333e+01,  1.07560863e-02],[-1.60000000e+01, -3.81997588e-03],[-1.46666667e+01,  5.63614872e-03],[-1.33333333e+01,  2.16508662e-03],[-1.20000000e+01, -1.97677774e-05],[-1.06666667e+01,  1.38566696e-03],[-9.33333333e+00,  8.04287512e-03],[-8.00000000e+00,  4.95042701e-03],[-6.66666667e+00,  1.29892553e-02],[-5.33333333e+00,  7.33505491e-03],[-4.00000000e+00,  2.59083765e-02],[-2.66666667e+00,  2.65086094e-02],[-1.33333333e+00,  3.97218416e-02],[ 0.00000000e+00,  6.09597045e-02],[ 1.33333333e+00,  9.14128829e-02],[ 2.66666667e+00,  1.01092944e-01],[ 4.00000000e+00,  7.67090506e-02],[ 5.33333333e+00,  5.77314665e-02],[ 6.66666667e+00,  4.13955834e-02],[ 8.00000000e+00,  2.49527673e-02],[ 9.33333333e+00,  1.49444689e-02],[ 1.06666667e+01,  1.38750557e-02],[ 1.20000000e+01,  1.08447634e-02],[ 1.33333333e+01,  1.01580483e-02],[ 1.46666667e+01,  7.85952160e-03],[ 1.60000000e+01,  5.53099781e-03],[ 1.73333333e+01,  1.02625306e-03],[ 1.86666667e+01,  2.14979928e-03],[ 2.00000000e+01,  9.05826797e-03]])
datax=data[:, [0][0]]
xdata=datax.tolist()
datay=data[:, [1][0]]
ydata=datay.tolist()
yerrs=[]
for n in range(len(data)):
    yerrs.append(5e-3)


def L(x,A,gamma,x0): return A*(gamma/(gamma**2+(x-x0)**2))

from scipy.optimize import curve_fit
guess = [0,3,2]
opt,cov = curve_fit(L, xdata, ydata, p0=guess)

xaxis = np.linspace(min(xdata),max(xdata),1001)
ybest = L(xaxis, *opt)

plt.figure()
plt.plot(xaxis, ybest, 'k-', label='Best fit')
plt.errorbar(xdata, ydata, yerrs, fmt='b*', label='Data')    
plt.legend()
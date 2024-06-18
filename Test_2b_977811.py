# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 14:02:35 2020

@author: mogzy
"""

from scipy.optimize import newton

import numpy as np

from scipy.interpolate import interp1d

#1

def f(x):return x**x-2

sol = newton(f, 1.5)

#2

numb=np.linspace(0, 1, num=10)
arr= np.zeros((10,2))
arr[:,0]=np.array(numb)
arr[:,1]=arr[:,0]**2

#3

x = [0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00]
y = [0.38, 0.98, 0.68, -0.25, -0.95, -0.78, 0.11, 0.90, 0.86, 0.03, -0.82]

ifunc=interp1d(x,y)

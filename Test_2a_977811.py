# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:02:01 2020

@author: Morgan Bridge
"""

import numpy as np
from scipy.integrate import quad

#1
x = np.linspace(0,10,2001)
def f(x):return np.sin(x**2)*np.exp(-np.sqrt(x))
compute=f(x)

#2
def g(x): return np.exp(-x**4)
integrate, err = quad(g, -np.inf, np.inf)

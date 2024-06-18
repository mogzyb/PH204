# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:58:04 2020

@author: Morgan Bridge
"""

import numpy as np
from scipy.linalg import det, expm

#1
u=np.array([1,2,1])
v=np.array([2,2,1])

vec=np.cross(u,v)

#2
A=np.array([[9,2],[3,4]])

D=det(A)

#3
B=np.array([[0,1],[1,0]])*1e-2
X0=np.array([1,0])

M=expm(B)

X=M@X0
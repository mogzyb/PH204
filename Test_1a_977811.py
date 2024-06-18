# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:00:33 2020

@author: mogzy
"""
import numpy                    
import numpy as np

#1
def mean(x):
    total=sum(x)
    length=len(x)
    y=total/length
    return y

#2
def decay(x):
    y=np.exp(-x)*np.cos(x**2)
    return y

#3
cubes=[]

def cube_function(x):
    y=x**3
    return y
for n in range(-10,11):
    cubes.append(cube_function(n))
    
#4
def builder(x):
    return [n**2 for n in range(0,x)]
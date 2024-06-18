# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:01:26 2020

@author: Morgan Bridge
"""

#1
def sequence(x): return[(2**n-1)**2-2 for n in range(0,x)]

#2
a = {5,7,2}; b = {1,6,3}; c = {9,4,8}; h = {5,7,1,3,6,9}
students=(a|b|c)-h
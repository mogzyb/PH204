# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:09:25 2020

@author: Morgan Bridge
"""

def factors(stuff):
    factordic={}
    for x in stuff:
        primes=[n for n in range(2,x) if all([n % m != 0 for m in range(2,n)])]
        mod=[]
        for n in primes:
            if x%n==0:
                mod.append(n)
        modset=set(mod)
        factordic[x]=modset
    return factordic
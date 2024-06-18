# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:09:24 2020

@author: Morgan Bridge
# """


# def gifts(N):
    
#     def nfact(N):
#         fact=1
#         for n in range(1,N+1):
#             fact=fact*n
#         return fact
    
#     def kfact(N):
#         fact=[1]
#         for n in range(1,N+1):
#                 x=fact[n-1]
#                 fact.append(x*n)
#         return fact 
    
#     kfactlist=[]
#     nkfactlist=[]
#     kfactlist=kfact(N)
#     for n in kfactlist:
#           nkfactlist.append(n)
#     nkfactlist.reverse()
  
#     numer=nfact(N)

#     denom=[a * b for a, b in zip(kfactlist, nkfactlist)]
#     result=[]
#     for n in denom:
#         result.append(numer/n)
       
#     return result
"""
In a lapse of jugement I thought the gift series was the same as a binomial coefficients
series so I ended up writing an algorithm to give me the binomial coefficient for power n. 
I've spent too much time on it and am too proud of the fact I got it to work to delete 
it so I'll just leave it here for your own enjoyment! :) 
"""

def gifts(N):
    day=[]
    gift=[]
    for n in range(1,N+1):
        day.append(n)
    for n in day:
          gift.append(n)
    gift.reverse()
    y=[a*b for a,b in zip(day, gift)]
    return y
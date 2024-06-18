# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:09:25 2020

@author: mogzy
"""
# from random import shuffle
# from itertools import permutations

def random_locations(N,L=400,D=2):
    def loc(L,D=2):
        from random import random
        return tuple([L*(random() - 0.5) for d in range(D)])
    return [loc(L,D) for n in range(N)]

locations=random_locations(12,L=400,D=2)
visitdic={}
home=(0,0)
cordlist=[]
# def rover(locations):
#     def path_length(locs):
#         def pair_distance(a,b): return sum([(ai-bi)**2 for ai,bi in zip(a,b)])**0.5
#         return sum([pair_distance(a,b) for a,b in zip([(0,0)]+ locs,locs)])

#     return order_to_visit 
for x in range(12):
    distance={}
    locs=[]
    for x in locations:
        locs=[x]
        def path_length(locs):
            def pair_distance(a,b): return sum([(ai-bi)**2 for ai,bi in zip(a,b)])**0.5
            return sum([pair_distance(a,b) for a,b in zip([home]+ locs,locs)])
    
        distance[x]=path_length(locs)
        
    sorted_distance=sorted(distance.items(), key=lambda x: x[1], reverse=False)
   
    # short_dis=sorted_distance[0]
    # cordlist.append(short_dis)
    # visitdic[short_dis[0]]=short_dis[1]
    # locations.remove(short_dis[0])

# order_to_visit=list(visitdic)

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d
# f = interp1d(order_to_visit) # basic form.  doesn't allow points outside.  defaults to linear interpolation

# f_lin = interp1d(order_to_visit,kind='linear', bounds_error=False, fill_value=0)
# f_cub = interp1d(order_to_visit,kind='cubic',  bounds_error=False, fill_value=0)

# x_int = np.linspace(-3,3,1001)
# y_lin = f_lin(x_int)
# y_cub = f_cub(x_int)

# plt.figure()
# plt.plot(x_int,y_lin,label='linear')
# plt.plot(x_int,y_cub,label='cubic')
# plt.plot(order_to_visit,'.',label='data')

# plt.legend()
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:08:07 2020

@author: mogzy
"""

import numpy as np
data = np.loadtxt("cake.csv", delimiter=',', skiprows=1)

T = data[:,0]
D = data[:,1]
C = data[:,2]

X = np.array([T,D,D**2,D**3]).T

Y = C # allows cut-and-paste reuse of example

import sklearn
from sklearn import linear_model
X_train,X_test,Y_train,Y_test = sklearn.model_selection.train_test_split(X,Y, test_size=0.2)
reg = linear_model.LinearRegression() # make an instance of the linear regression model
reg.fit(X_train,Y_train)             # train the model


test_predicted = reg.predict(X_test)
train_predicted = reg.predict(X_train)

# Y_max = max(Y)
# Y_min = min(Y)

# import matplotlib.pyplot as plt
# plt.figure()
# plt.plot(Y_train, train_predicted, '*b', label='Train')
# plt.plot(Y_test,  test_predicted,  '*r', label='Test')
# plt.plot([Y_min,Y_max],[Y_min,Y_max],'k')

# plt.xlabel('Actual')
# plt.ylabel('Model')

# plt.legend()

# plt.figure()
# plt.plot(Y_train, train_predicted-Y_train, '*b', label='Train')
# plt.plot(Y_test,  test_predicted -Y_test,  '*r', label='Test')
# plt.plot(Y, C-Y, '*g', label='Naive')
# plt.xlabel('Actual cost')
# plt.ylabel('Difference between model and actual')
# plt.legend()

cake=reg.predict([[1,18,18**2,18**3]])
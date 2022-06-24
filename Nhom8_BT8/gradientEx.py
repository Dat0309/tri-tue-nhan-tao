# Gradient
import numpy as np
from numpy import *
from numpy.random import *
import pandas as pd
from sklearn.model_selection import train_test_split

def gradientDescent(F, dF, d):
    # F is the function
    # dF is the gradient
    # d is the dimension
    w = zeros(d)
    eta = 0.001
    for t in range(100):
        value = F(w)
        gradient = dF(w)
        print('t = {}, value = {}, w = {}'.format(t, value, w))
        w = w - eta * gradient
    return w


def stochasticGradientDescent(sF, sdF, d, n):
    # sF is the function
    # sdF is the gradient
    # d is the dimension
    # n is the number of datapoints
    w = zeros(d)
    eta = 0.01
    for t in range(10):
      # shuffer Trains
        for i in range(n):
            value = sF(w, i)
            gradient = sdF(w, i)
            w = w - eta * gradient
        print('t = {}, value = {}, w = {}'.format(t, value, w))
    return w


def F(w):
    return sum((x.dot(w) - y)**2 for x, y in trains) / len(trains)


def dF(w):
    return sum(2*(x.dot(w) - y)*x for x, y in trains) / len(trains)


def sF(w, i):
    x, y = trains[i]
    return (x.dot(w) - y)**2


def sdF(w, i):
    x, y = trains[i]
    return 2*(x.dot(w) - y)*x


def predict(w, x):
    return x.dot(w)


def createData():
    # Generating synthetic data
    data_frame = pd.read_csv(
    "Test1_MeanData_ML.csv")

    train_set, test_set = train_test_split(data_frame, test_size=0.1)
    x_train = train_set.values[:,1:-1]
    y_train = train_set.values[:,-1]

    true_w = y_train
    d = len(true_w)
    trains = []
    trains.append((x_train, y_train))
    return trains

data_frame = pd.read_csv(
    "Test1_MeanData_ML.csv")

train_set, test_set = train_test_split(data_frame, test_size=0.1)
x_test = test_set.values[:,1:-1]
y_test = test_set.values[:, -1]

trains = createData()
d = 5
w = gradientDescent(F, dF, d)
for i in range(20):
    x, y = trains[i]
    print(y, '\t', predict(w, asarray(x)))

w = stochasticGradientDescent(sF, sdF, d, len(trains))
x = x_test
y = y_test
for i in range(20):
    x, y = trains[i]
    print(y, '\t', predict(w, asarray(x)))

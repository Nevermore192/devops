import numpy as np
from numpy import*

def sigmoid(X):
    return 1 / (1 + np.exp(-x))

def deriv_sigmoid(x):
    fx = sigmoid(x)
    return fx * (1 -fx)

def mse_loss(y_true, y_pred) :
    return ((y_true - y_pred) ** 2).mean()

class OurNerwork
def _init_(self):

    self.w1 = np.random.normal()
    self.w2 = np.random.normal()
    self.w3 = np.random.normal()
    self.w4 = np.random.normal()
    self.w5 = np.random.normal()
    self.w6 = np.random.normal()

    self.b1 = np.random.normal()
    self.b2 = np.random.normal()
    self.b3 = np.random.normal()

#ssa
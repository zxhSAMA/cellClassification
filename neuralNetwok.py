__author__ = 'zhangxianghui'
import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_prime(x):
    return sigmoid(x)*(1-sigmoid(x))

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1.0-np.tanh(x)*np.tanh(x)

def softplus(x):
    return np.log(1+np.exp(x))

def softplus_prime(x):
    return sigmoid(x)

def relu(x):
    return np.maximum(x,0.0)

def relu_prime(x):
    driv=lambda x:1 if x>0 else 0
    return driv(x)
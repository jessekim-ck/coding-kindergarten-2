import numpy as np


def step_function(x):
    return (x > 0).astype(np.int)


def sigmoid_function(x):
    return 1/(1 + np.exp(-x))


def relu_function(x):
    return np.maximum(x, 0)


def softmax_function(x):
    x = x - np.max(x)  # overflow 방지
    return np.exp(x)/np.sum(np.exp(x))

import numpy as np


def mean_squared_loss(y, t):
    """
    Input
        y: (N, C) 차원의 행렬. 추론값.
        t: (N, C) 차원의 행렬. 정답값.
    Output
        loss: scalar 값
    """
    return np.sum((y - t)**2) / y.shape[0] / 2


def cross_entropy_loss(y, t):
    """
    Input
        y: (N, C) 차원의 행렬. 추론값.
        t: (N, C) 차원의 행렬. 정답값.
    Output
        loss: scalar 값
    """
    return -np.sum(t*np.log(y + 1e-8)) / y.shape[0]
from re import L
import numpy as np


def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


def perceptron(x, w, b):
    """
    Input
        x: np.ndarray(N,)
        w: np.ndarray(N,)
        b: numeric
    Ouput
        y: 1 | 0
    """
    a = np.sum(x*w) + b
    return step_function(a)


def and_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -1.5
    return perceptron(x, w, b)


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([1, 1])
    b = -0.5
    return perceptron(x, w, b)


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-1, -1])
    b = 1.5
    return perceptron(x, w, b)


def xor_gate(x1, x2):
    return and_gate(
        nand_gate(x1, x2),
        or_gate(x1, x2)
    )


if __name__ == "__main__":
    print(xor_gate(1, 0))
    print(xor_gate(0, 1))
    print(xor_gate(0, 0))
    print(xor_gate(1, 1))

from activation_function import (
    step_function
)


def perceptron(x, w, b):
    """
    Input
        x: np.ndarray(N, )
        w: np.ndarray(N, )
        b: numeric
    Output
        y: numeric
    """
    return step_function(w*x + b)


def and_gate(x):
    w = None
    b = None
    return perceptron(x, w, b)


def or_gate(x):
    w = None
    b = None
    return perceptron(x, w, b)


def nand_gate(x):
    w = None
    b = None
    return perceptron(x, w, b)


def xor_gate(x):
    raise NotImplementedError

import numpy as np
from activation import relu_function, softmax_function


class Perceptron:
    """신경망에서 하나의 노드(동그라미)"""
    def __init__(self, input_num):
        self.w = np.random.random(input_num)  # np.ndarray(input_num, )
        self.b = np.random.random()  # np.float
    
    def forward(self, x):
        return np.sum(self.w*x) + self.b


class MyNeuralNet1:
    def __init__(self):
        self.layer_1 = [
            Perceptron(784),
            Perceptron(784),
            Perceptron(784),
            Perceptron(784),
            Perceptron(784)
        ]
        self.layer_2 = [
            Perceptron(5),
            Perceptron(5),
            Perceptron(5),
            Perceptron(5),
            Perceptron(5)
        ]
        self.layer_3 = [Perceptron(5) for _ in range(5)]
        self.output_layer = [Perceptron(5) for _ in range(10)]
    
    def forward(self, x):
        assert x.shape == (784,)

        # layer 1
        x1 = list()
        for layer in self.layer_1:
            x1.append(
                relu_function(
                    layer.forward(x)
                )
            )
        x1 = np.array(x1)  # np.ndarray(5,)

        x2 = list()
        for layer in self.layer_2:
            x2.append(relu_function(layer.forward(x1)))
        x2 = np.array(x2)

        x3 = list()
        for layer in self.layer_3:
            x3.append(relu_function(layer.forward(x2)))
        x3 = np.array(x3)

        out = list()
        for layer in self.output_layer:
            out.append(layer.forward(x3))
        out = np.array(out)  # np.ndarray(10,)
        out = softmax_function(out)

        return out


class Layer:
    """하나의 레이어를 표현하는 클래스"""
    def __init__(self, input_num, output_num):
        self.w = np.random.random((input_num, output_num))  # input_num x output_num 짜리 행렬
        self.b = np.random.random((1, output_num))  # output_num 짜리 벡터
    
    def forward(self, x):
        return np.matmul(
            x.reshape(1, -1),  # (784, ) => (1, 784)
            self.w
        ) + self.b


class MyNeuralNet2:
    def __init__(self):
        self.layer_1 = Layer(784, 5)
        self.layer_2 = Layer(5, 5)
        self.layer_3 = Layer(5, 5)
        self.output_layer = Layer(5, 10)
    
    def forward(self, x):
        x = self.layer_1.forward(x)
        x = relu_function(x)

        x = self.layer_2.forward(x)
        x = relu_function(x)

        x = self.layer_3.forward(x)
        x = relu_function(x)

        x = self.output_layer.forward(x)
        x = softmax_function(x)
        return x


if __name__ == "__main__":

    x = np.random.random((28, 28))
    x = x.reshape(-1)

    neural_net_1 = MyNeuralNet1()
    print(neural_net_1.forward(x))
    
    neural_net_2 = MyNeuralNet2()
    print(neural_net_2.forward(x))

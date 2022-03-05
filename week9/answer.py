import torch
import torchvision
import numpy as np


class Linear:
    def __init__(self, input_dim, output_dim):
        self.W = np.random.randn(input_dim, output_dim) * np.sqrt(2/input_dim)
        self.b = np.zeros(output_dim)
        self.X = None
        self.learning_rate = 0.0001
    
    def forward(self, X):
        """
        Input
            X: (N, input_dim) 차원의 행렬
        Output
            out: (N, output_dim) 차원의 행렬
        """
        self.X = X
        
        # TODO: 구현하세요!
        out = np.matmul(self.X, self.W) + self.b
        ################

        return out
    
    def backward(self, d_out):
        """
        Input
            d_out: (N, output_dim) 차원의 행렬
        Output
            dX: (N, input_dim) 차원의 행렬
        """
        # TODO: 구현하세요!
        dX = np.matmul(d_out, self.W.T)  # X의 y에 대한 미분값
        self.dW = np.matmul(self.X.T, d_out)  # W의 y에 대한 미분값
        self.db = np.sum(d_out, axis=0)  # b의 y에 대한 미분값
        ################

        return dX

    def step(self):
        # TODO: 구현하세요!
        self.W = self.W - self.learning_rate * self.dW
        self.b = self.b - self.learning_rate * self.db
        ################
        pass


class ReLU:
    def __init__(self):
        self.out = None

    def forward(self, X):
        """
        Input
            X: (N, M) 차원의 행렬
        Output
            out: (N, M) 차원의 행렬
        """

        # TODO: 구현하세요!
        out = np.maximum(X, 0)
        ################

        self.out = out
        return out

    def backward(self, d_out):
        """
        Input:
            d_out: (N, M) 차원의 행렬
        Output:
            dX: (N, M) 차원의 행렬
        """

        # TODO: 구현하세요!
        mask = (self.out > 0).astype(np.float64)
        dX = d_out * mask
        ################
        return dX

    def step(self):
        pass


def softmax(X):
    """
    Input
        X: (N, C=10) 차원 행렬
    Output
        Y: (N, C=10) 차원 행렬
    """
    X = np.exp(X - np.max(X))  # overflow 방지
    return X / np.sum(X, axis=0)


def cross_entropy(y, t):
    """
    Input
        y: (N, C) 차원의 행렬
        t: (N, C) 차원의 행렬
    Output
        loss: scalar 값
    """
    return -np.sum(t * np.log(y + 1e-8)) / y.shape[0]


class SoftmaxWithCrossEntropy:
    def __init__(self):
        self.y = None
        self.t = None
    
    def forward(self, X, t):
        """
        Input
            X: (N, C=10) 차원의 행렬
            t: (N, C=10) 차원의 행렬
        Output
            loss: scalar 값
        """

        # TODO: 구현하세요!
        self.t = t
        self.y = softmax(X)  # Softmax 계산
        loss = cross_entropy(self.y, self.t)  # CrossEntropy 계산
        ################
        
        return loss, self.y
    
    def backward(self):
        """
        Output
            dX: (N, C=10) 차원의 행렬
        """

        # TODO: 구현하세요!
        dX = (self.y - self.t) / self.y.shape[0]  # X의 y에 대한 미분값 계산
        ################
        return dX


class NeuralNet:
    def __init__(self):
        self.layers = [
            Linear(784, 128),
            ReLU(),
            Linear(128, 10)
        ]
        self.loss_layer = SoftmaxWithCrossEntropy()

    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def loss(self, X, t):
        return self.loss_layer.forward(X, t)

    def backward(self):
        d_out = self.loss_layer.backward()
        for layer in reversed(self.layers):
            d_out = layer.backward(d_out)
    
    def step(self):
        for layer in reversed(self.layers):
            layer.step()


if __name__ == "__main__":
    mnist_data = torchvision.datasets.MNIST(
        "./data",
        train=True,
        download=True,
        transform=torchvision.transforms.Compose([
            torchvision.transforms.ToTensor()
        ])
    )
    data_loader = torch.utils.data.DataLoader(
        mnist_data,
        batch_size=64,
        shuffle=True
    )

    net = NeuralNet()
    for epoch in range(10):
        for i, data in enumerate(data_loader):
            inputs, labels = data
            inputs = inputs.numpy().reshape(inputs.shape[0], -1)
            labels = np.array([[float(i == label) for i in range(10)] for label in labels])

            outputs = net.forward(inputs)
            loss, Y = net.loss(outputs, labels)
            net.backward()
            net.step()

            if i % 200 == 0:
                right = list()
                for y, label in zip(Y, labels):
                    r = np.argmax(y) == np.argmax(label)
                    right.append(r)
                acc = np.mean(right)
                print(f"Epoch {epoch + 1} | Iteration {i} | Loss {loss:.4f} | ACC {acc:.4f}")

    pass
import torch
import torchvision
import numpy as np


class Linear:
    def __init__(self, input_dim, output_dim):
        self.X = None
        self.dW = None
        self.db = None

        # 파라미터 초기화 - He initialization
        self.W = np.random.randn(input_dim, output_dim) * np.sqrt(2/input_dim)
        self.b = np.zeros(output_dim)

        # 하이퍼파라미터
        self.learning_rate = 0.0001
    
    def forward(self, X):
        """
        신경망의 순전파.

        Input
            X: (N, input_dim) 차원의 행렬
        Output
            out: (N, output_dim) 차원의 행렬
        """
        self.X = X  # 역전파 미분 계산 시에 필요합니다.
        
        # TODO: 구현하세요!
        out = None
        ################

        return out
    
    def backward(self, d_out):
        """
        신경망의 역전파. 미분값을 계산한다.

        Input
            d_out: (N, output_dim) 차원의 행렬
        Output
            dX: (N, input_dim) 차원의 행렬
        """
        # TODO: 구현하세요!
        dX = None  # X의 y에 대한 미분값
        self.dW = None  # W의 y에 대한 미분값
        self.db = None  # b의 y에 대한 미분값
        ################

        return dX

    def step(self):
        """
        신경망의 학습. 미분값으로 파라미터 값을 조정한다.
        """

        # TODO: 구현하세요!
        self.W = None
        self.b = None
        ################
        pass


class ReLU:
    def __init__(self):
        self.out = None

    def forward(self, X):
        """
        순전파. ReLU 계산.

        Input
            X: (N, M) 차원의 행렬
        Output
            out: (N, M) 차원의 행렬
        """

        # TODO: 구현하세요!
        out = None
        ################

        self.out = out  # 역전파 미분 계산 시에 필요합니다.
        return out

    def backward(self, d_out):
        """
        역전파. 미분값 계산.

        Input:
            d_out: (N, M) 차원의 행렬
        Output:
            dX: (N, M) 차원의 행렬
        """

        # TODO: 구현하세요!
        dX = None
        ################

        return dX

    def step(self):
        pass


def softmax(X):
    """
    Softmax 계산

    Input
        X: (N, C=10) 차원 행렬
    Output
        Y: (N, C=10) 차원 행렬
    """
    X = np.exp(X - np.max(X))  # overflow 방지
    return X / np.sum(X, axis=0)


def cross_entropy(y, t):
    """
    Cross Entropy loss 계산

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
        순전파. Softmax - CrossEntropy 계산.

        Input
            X: (N, C=10) 차원의 행렬
            t: (N, C=10) 차원의 행렬
        Output
            loss: scalar 값
        """

        # TODO: 구현하세요!
        self.t = t  # 역전파 미분 계산 시에 필요합니다.
        self.y = None  # Softmax 계산
        loss = None  # CrossEntropy 계산
        ################
        
        return loss, self.y
    
    def backward(self):
        """
        역전파. 미분값 계산.

        Output
            dX: (N, C=10) 차원의 행렬
        """

        # TODO: 구현하세요!
        dX = None  # X의 y에 대한 미분값 계산
        ################
        return dX


class NeuralNet:
    def __init__(self):
        """
        신경망의 각 계층을 초기화한다.
        """
        # hidden layer
        self.layers = [
            Linear(784, 128),
            ReLU(),
            Linear(128, 10)
        ]
        # output layer
        self.loss_layer = SoftmaxWithCrossEntropy()

    def forward(self, X):
        """순전파"""
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def loss(self, X, t):
        """손실 함수 계산"""
        return self.loss_layer.forward(X, t)

    def backward(self):
        """역전파를 통한 미분값 계산"""
        d_out = self.loss_layer.backward()
        for layer in reversed(self.layers):
            d_out = layer.backward(d_out)
    
    def step(self):
        """학습 - 파라미터 조정"""
        for layer in reversed(self.layers):
            layer.step()


if __name__ == "__main__":
    # MNIST 데이터셋 로드
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

    net = NeuralNet()  # 신경망 초기화

    # 학습
    for epoch in range(10):
        for i, data in enumerate(data_loader):
            # 데이터 불러오고 가공하기
            inputs, labels = data
            inputs = inputs.numpy().reshape(inputs.shape[0], -1)  # flatten
            labels = np.array([[float(i == label) for i in range(10)] for label in labels])  # one-hot-encoding

            outputs = net.forward(inputs)  # 순전파
            loss, Y = net.loss(outputs, labels)  # 손실 함수 계산
            net.backward()  # 역전파
            net.step()  # 학습

            # 학습 경과 로깅하기
            if i % 200 == 0:
                right = list()
                for y, label in zip(Y, labels):
                    r = np.argmax(y) == np.argmax(label)
                    right.append(r)
                acc = np.mean(right)
                print(f"Epoch {epoch + 1} | Iteration {i} | Loss {loss:.4f} | ACC {acc:.4f}")

    pass
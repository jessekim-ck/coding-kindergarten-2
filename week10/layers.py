import numpy as np


class Convolution:
    def __init__(self):
        self.input_channels = 3
        self.output_channels = 5
        self.kernel_size = 3
        self.kernel = np.random.randn((
            self.output_channels,
            self.input_channels,
            self.kernel_size, self.kernel_size
        ))
        self.padding = 1
        self.stride = 1

    def forward(self, X):
        """
        Input
            X: np.ndarray of shape (3, 64, 64)
        Output
            Y: np.ndarray of shape (5, output_h, output_w)
        """

        output_h = (
            (self.X.shape[1] - (self.kernel_size - 1) + 2 * self.padding) // 
            self.stride
        )  # output의 height 미리 계산하기
        output_w = (
            (self.X.shape[2] - (self.kernel_size - 1) + 2 * self.padding) // 
            self.stride
        )  # output의 width 미리 계산하기
        output = np.zeros((
            self.output_channels, output_h, output_w
        ))
        X = np.pad(X, self.padding)

        for c in range(self.output_channels):
            for i in range(output_h):
                for j in range(output_w):
                    kernel = self.kernel[c]  # 3 x 3 x 3

                    # 이미지의 세로 인덱스
                    h_start = self.stride * i
                    h_end = self.stride * (i + 1)

                    # 이미지의 가로 인덱스
                    w_start = self.stride * j
                    w_end = self.stride * (j + 1)

                    # 연산하고자 하는 이미지의 부분
                    window = X[:][h_start:h_end][w_start:w_end]  # 3 x 3 x 3

                    # 합성곱!
                    value = np.sum(kernel * window)

                    output[c][i][j] = value

        return output


class Pool:
    def __init__(self):
        self.kernel_size = 2
    
    def forward(self, X):
        """
        Input
            X: np.ndarray of shape (3, 64, 64)
        Ouput
            Y: np.ndarray of shape (?, ?, ?)
        """

        output_c = X.shape[0]  # output channel
        output_h = X.shape[1] // self.kernel_size  # output height
        output_w = X.shape[2] // self.kernel_size  # output width
        output = np.zeros((
            output_c, output_h, output_w
        ))

        for c in range(output_c):
            for i in range(output_h):
                for j in range(output_w):
                    h_start = i*self.kernel_size
                    h_end = (i + 1)*self.kernel_size

                    w_start = j*self.kernel_size
                    w_end = (j + 1)*self.kernel_size

                    window = X[c][h_start:h_end][w_start:w_end]

                    output[c][i][j] = np.max(window)  # pooling 연산하기

        return output

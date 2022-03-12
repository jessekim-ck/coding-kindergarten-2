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

        output_h = None  # output의 height 미리 계산하기
        output_w = None  # output의 width 미리 계산하기
        output = np.zeros((
            self.output_channels, output_h, output_w
        ))

        for c in range(self.output_channels):
            for i in range(output_h):
                for j in range(output_w):
                    output[c][i][j] = None  # convolution 연산하기

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

        output_c = None  # output channel
        output_h = None  # output height
        output_w = None  # output width
        output = np.zeros((
            output_c, output_h, output_w
        ))

        for c in range(output_c):
            for i in range(output_h):
                for j in range(output_w):
                    output[c][i][j] = None  # pooling 연산하기

        return output

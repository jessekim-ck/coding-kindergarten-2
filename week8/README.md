# 8주차: 퍼셉트론과 신경망

## 1. 퍼셉트론
퍼셉트론이란 1957년에 Frank Rosenblatt 형님이 제안한, 실제 뇌를 구성하는 뉴런의 매커니즘을 벤치마킹한 알고리즘. 회귀분석 모형을 구현하는 하나의 방법으로 바라볼 수도 있다!

![perceptron](https://compmath.korea.ac.kr/appmath2021/_images/neuron-node1.png)

### 1.1. 퍼셉트론이란?
다수의 정보(신호)를 입력받아 하나의 정보(신호)를 출력하는 알고리즘. 물론 컴퓨터에게 정보란 숫자이다!

$x_1$ 과 $x_2$ 라는 두 개의 정보를 입력받았을 때, 퍼셉트론은 다음과 같은 정보를 출력한다.

$$
y = f(w_1 x_1 + w_2 x_2 + \theta), \\
\text{where }
f(x) = \begin{cases}
1 \ (x > 0) \\
0 \ (else)
\end{cases}
$$

### 1.2. 논리 회로
#### AND gate
퍼셉트론으로 AND gate를 표현해보자.

| $x_1$ | $x_2$ | $y$ |
| -- | -- | -- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 1 | 1 |

#### OR gate
퍼셉트론으로 OR gate를 표현해보자.

| $x_1$ | $x_2$ | $y$ |
| -- | -- | -- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

#### NAND gate
퍼셉트론으로 NAND gate를 표현해보자.

| $x_1$ | $x_2$ | $y$ |
| -- | -- | -- |
| 0 | 0 | 1 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

#### XOR gate?
퍼셉트론으로 XOR gate를 표현해보자.

| $x_1$ | $x_2$ | $y$ |
| -- | -- | -- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

### 1.3. 다층 퍼셉트론
퍼셉트론을 여러 층 쌓아 더 복잡한 논리 회로를 구현할 수 있다!

#### XOR gate!
**다층 퍼셉트론**으로 XOR gate를 표현해보자.

| $x_1$ | $x_2$ | $y$ |
| -- | -- | -- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |


## 2. 신경망
퍼셉트론에서 신경망으로 나아가는 데는 두 가지 포인트가 있다. 첫 번째는 퍼셉트론을 매우 두껍고 깊게 쌓는 것이고, 두 번째는 퍼셉트론의 parameter(매개변수)를 데이터로부터 학습하게 하는 것!

![neural network](https://ichi.pro/assets/images/max/724/1*dGcBoXQyD6jAVRgAGAqRew.png)

### 2.1. 퍼셉트론에서 신경망까지
#### N층 퍼셉트론
첫 번째는 퍼셉트론을 매우 두껍고 깊게 쌓는 것이다. 2층 퍼셉트론으로 1층 퍼셉트론이 표현할 수 없었던 XOR gate을 표현해냈듯, N층 퍼셉트론으로 매우 복잡한 함수(e.g. 시각 인지 함수)를 표현해낼 수 있게 된다.

#### 활성화 함수 (activation function)
더 쉽게 복잡한 함수를 표현해내기 위해, 그리고 파라미터의 학습을 더 빠르고 쉽게 만들기 위해 신경망에서는 다양한 activation function을 활용한다.

### 2.2. 활성화 함수
활성화 함수의 가장 중요한 요소는 비선형성이다. 선형 함수는 아무리 합성해도 선형 함수이기 때문에, 단층 퍼셉트론보다 복잡한 함수를 표현해내지 못하는 반면, 비선형 함수는 합성할수록 더욱 복잡한 함수를 표현해낼 수 있기 때문!

#### Step function
퍼셉트론에서 쓰였던 그 함수.

그렇다! 사실 퍼셉트론은 step function을 activation function으로 이용하는 신경망이었던 것이다!

$$
f(x) = \begin{cases}
1 \ (x > 0) \\
0 \ (else)
\end{cases}
$$

![step function](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3G1fQG0S0YkPuf1w1TK1gIHqeQPN0n37rN04QKxDMsHFKZBDaqySu2JKMb9Xb4u359sQ&usqp=CAU)

#### Sigmoid function
고전 딥러닝에서 애용되던 activation function. Step function 과의 핵심적인 차이점은 연속성 혹은 매끄러움. 이 매끄러움이 신경망의 학습을 원활하게 한다.

$$
f(x) = \frac{1}{1 + \exp{(-x)}}
$$

![sigmoid function](https://miro.medium.com/max/1280/1*sOtpVYq2Msjxz51XMn1QSA.png)

#### ReLU function
Rectified Linear Unit. 현대 딥러닝에서 애용되고 있는 activation function. Sigmoid function 보다 계산이 쉽고, 학습이 빠르다. 역시나 연속 함수!

$$
f(x) = \begin{cases}
x \ (x > 0) \\
0 \ (else)
\end{cases}
$$

![ReLU function](https://miro.medium.com/max/754/1*3JUMOqugWKB2SDra6x6v0A.png)

#### Other functions
Leaky ReLU 등 그 외의 아주 다양한 activation function들이 연구되고 활용된다.

### 2.3. 출력층 설계하기
신경망을 통해 얻어내고자 하는 결과는 매우 다양하다. 어떤 숫자인지 맞추는 것일 수도 있고, 부동산 가격을 추론하는 것일 수도 있고, 이미지를 만드는 것일 수도 있다!

위와 같이 얻어내고자 하는 결과에 따라 출력층을 설계하기 위해서는, 출력층의 너비와 activation function을 정해야 한다.

#### Identity function
항등 함수. 범위가 특정되어있지 않은 값을 추론할 때 주로 사용함.

$$
f(x) = x
$$

#### Sigmoid function
아까 봤던 그 함수. 어떤 특성에 대한 확률을 나타낼 때 주로 사용함.

$$
f(x) = \frac{1}{1 + \exp{(-x)}}
$$

#### Softmax function
총합이 1이라는 특성을 이용하여, 여러 가능한 가짓수의 확률을 나타낼 때 주로 사용함.

$$
f(x_k) = \frac{\exp(x_k)}{\sum_i^n{\exp(x_i)}}
$$

### 2.4. 구현해보기
MNIST 이미지를 받아 0~9 class들의 확률을 출력하는 3층 신경망 구현해보기!

---
*E.O.D.*
# 12주차: Pytorch tutorial

## 1. [Pytorch](https://pytorch.org/)
An open source machine learning framework that accelerates the path from research prototyping to production deployment.

Pytorch tutorials: [link](https://pytorch.org/tutorials/beginner/basics/intro.html)

파이토치와 같은 머신 러닝 프레임워크를 쓰는 이유는 크게 두 가지가 있을 것 같습니다! (주관적)
- 모델, 데이터 로더, 옵티마이저 등을 아주 편하게 갖다쓰기 위해
    - Back propagation, convolution layer, linear layer, cross entropy loss, ... 이런 거 다 구현되어있음!
    - Adam Optimizer 같은 것들도 당연히 다 구현되어 있고, 데이터를 갖다 쓰기 위한 파이프라인도 구현되어있음!
    - 덕분에 아주 편리함
- GPU 가속 연산을 위해
    - 딥러닝 학습/추론에 있어서, GPU 연산은 CPU 연산에 비해 훨ㄹㄹ씬 빠르다!
    - 하지만 대부분의 프로그래밍 언어는 CPU 기반
    - 여기서 파이토치는 데이터를 GPU 메모리로 보내고, GPU 기반의 연산을 실행하고, 이를 다시 CPU로 모아주는 역할을 함

[Fashion Mnist 데이터셋](https://drive.google.com/file/d/1HXxF6B2QQN0w3WqFZumaIX_Mduzm-kII/view?usp=sharing)으로 실습하면서 따라해보자!

### 1.0. Install
Anaconda를 통해 설치 가능. (pytorch와 torchvision을 설치하는데, pytorch 버전에 맞게 설치하라는 뜻.)

```
conda install pytorch torchvision -c pytorch
```

### 1.1. Tensor
Tensor는 수학적으로는 3차원 이상의 행렬을 의미한다. numpy의 array를 생각하면 쉽다. numpy에 있는 기능들은 torch에도 있고, 구글링해보면 바로 나온다!

### 1.2. Datasets and DataLoaders
컴퓨터에 저장된 데이터들을 순서대로 불러오고(mini-batch), 후처리하여(data augmentation) 모델에 입력해주는 파이프라인이 필요하다. Dataset과 DataLoader가 이 역할을 한다!

### 1.3. Transforms
Data augmentation 혹은 원활한 학습을 위한 후처리를 해주는 패키지이다!

### 1.4. Build Model
우리가 한 땀 한 땀 구현했던 모델을, 아주 쉽게 구현하고/수정하고/실험할 수 있게 해 준다!

### 1.5. Automatic Differentiation
Backpropagation! 그런 거 크게 신경 쓸 필요 없다! 파이토치가 모든 연산 그래프를 기억해두었다가, backpropagation을 통한 미분을 알아서 계산해준다. `loss.backward()` 메서드 하나면 끝!

### 1.6. Optimization Loop
데이터 로딩 - 모델 추론 - 미분 계산 - 학습 루프의 구현. 위의 재료들을 활용하면 끝!

### 1.7. Save, Load and Use Model
학습한 모델(웨이트)을 저장하고, 다시 불러와서 사용한다.

---
*E.O.D.*
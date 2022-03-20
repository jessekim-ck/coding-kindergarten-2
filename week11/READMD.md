# 11주차: Recap & 실전 트렌드

## 1. Recapitulation
- 파이썬
    - 기본 연산자와 자료형
    - 조건문과 루프
    - 함수와 클래스
    - 파일 I/O, 라이브러리
    - 예외 처리
    - pandas, numpy, matplotlib
- 기계학습과 딥러닝 (W7)
- 퍼셉트론과 신경망 (W8)
- 신경망의 학습 (W9)
- Convolutional Neural Network (W10)

## 2. 딥러닝 모델 트렌드
### 2.1. ResNet (2015)
- 논문: https://arxiv.org/abs/1512.03385
- 코드: https://pytorch.org/vision/0.8/_modules/torchvision/models/resnet.html
- 아이디어
    - 모델을 깊게 하면 할수록 성능이 떨어지는 문제가 있는데, 이론상 말이 안 됨.
    - 그냥 모델이 학습하기 어려워서해서 그런 것 같은데, 학습을 쉽게 해줄 수 있지 않을까?
    - 찾고자 하는 함수가 H(x)면, F(x) = H(x) - x (Residual)를 학습하도록 하고, x 는 그냥 뒤에서 더해주자! F(x) + x 처럼.
    - 그러면 잘 안 되면 F(x)를 0으로 보내버리면 되니까, 적어도 깊은 모델이 얕은 모델보다 못하는 일은 없지 않을까?
    - 오... 해보니까 겁나 잘 되네? 개쩐다!
    - 이후 딥러닝 씬의 표준이 됨.

![Skip Connection](https://kharshit.github.io/img/resnet_block.png)

### 2.2. EfficientNet (2019)
- 논문: https://arxiv.org/abs/1905.11946
- 코드: https://github.com/lukemelas/EfficientNet-PyTorch
- 아이디어
    - 모델을 깊게 만들 때 깊이만 깊게 만들거나, 너비만 넓게 만들거나 하는데, 둘 다 늘려야 시너지가 날 것 같아.
    - 음 근데 왠지 너비와 깊이의 최적의 비율이 있을 것만 같아.
    - 이 비율을 딥러닝을 통해 찾도록 해보자!
        - Neural Archtecture Search: 모델의 구조를 파라미터로 두고 딥러닝 모델이 이 모델의 구조의 최적값을 찾도록 함.
    - 오... 이렇게 찾아보니까, 기존보다 훨씬 빠르면서도 성능은 더 좋은 효율적인(Efficient) 모델이 나왔어!
    - 이후 딥러닝 씬의 표준이 됨.

![Efficiency of EfficientNet](https://miro.medium.com/max/710/1*IjlNQ7pX1ArDpyJf4FU-3A.png)

### 2.3. Transformer (ViT, 2020)
- 논문: https://arxiv.org/pdf/2010.11929.pdf
- 코드: https://github.com/lucidrains/vit-pytorch
- 아이디어
    - 나도 잘 모름ㅎㅎ 공부해야되는데 맨날 미루는 중...
    - 시간 될 때 공부하고 알려드림
    - 아직 학계의 표준이 되지는 못함! 모델이 너무 복잡하고 느려서, 상용화가 어려움.
    - 하지만 느리면서도 성능이 워낙 좋아서 미래의 표준이 될 것 같다고 학계의 주목을 받는 중.

![Transformer](https://d33wubrfki0l68.cloudfront.net/a76be57763d942798f8081b77edf8f078720cd45/bd31a/img/transformer_architecture_positional_encoding/model_arc.jpg)

## 3. 탬플릿
- Model: EfficientNet / 엄청 느려도 되면 Transformer
- Optimizer: Adam / AdamW
- Loss: BCE(Binary Cross Entropy) / CE(Cross Entropy) / MSE (Mean Squared Error)
- Augmentation: 쓸 수 있는 거 전부 다!

---
*E.O.D.*
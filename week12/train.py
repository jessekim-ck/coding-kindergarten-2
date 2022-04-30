import torch
import numpy as np

from data import get_test_data_loader, get_train_data_loader
from model import FashionClassifier


model = FashionClassifier()  # 모델 객체 초기화
train_data_loader = get_train_data_loader(
    "fashion_mnist/train.csv"
)  # 학습용 데이터 로더 초기화
loss_function = torch.nn.CrossEntropyLoss()  # loss function chrlghk
optimizer = torch.optim.Adam(
    model.parameters(), lr=0.001
)  # 학습 optimizer 초기화

model.train()  # 학습할 때는 필수!! Dropout 등을 활성화한다.
for epoch in range(1):
    # 데이터셋을 한 바퀴 돈다
    # batch_size 만큼의 데이터를 묶어서 줌
    for i, (imgs, labels) in enumerate(train_data_loader):

        y = model(imgs)  # 이미지를 딥러닝 모델을 통해 추론
        y = torch.nn.Softmax(dim=1)(y)  # softmax를 통해 확률값으로 변환

        loss = loss_function(y, labels)  # loss function 계산

        optimizer.zero_grad()  # optimizer에 쌓여있던 gradient 값을 0으로 초기화
        loss.backward()  # optimizer에 새로운 gradient 값을 쌓는다
        optimizer.step()  # 쌓인 gradient 값을 통해 파라미터를 업데이트

        if i % 100 == 0:
            print(f"Epoch: {epoch + 1} | Batch: {i + 1} | Loss: {loss}")
        
        if i == 200:
            break


test_data_loader = get_test_data_loader(
    "fashion_mnist/test.csv"
)  # 테스트용 데이터 로더 초기화
model.eval()  # 모델 추론할 때는 필수!! Dropout 등을 비활성화한다.
with torch.no_grad():  # 역시 모델 추론할 때는 필수!! 추론 시에는 필요 없는 계산 그래프를 저장하지 않도록 한다.
    correctness = list()
    for imgs, labels in test_data_loader:
        y = model(imgs)
        y = torch.argmax(y, dim=1)
        correctness.extend(labels == y)  # [True, False, False, True, ...]
    acc = np.mean(correctness)  # 정확도 - 맞은 개수 / (맞은 개수 + 틀린 개수)
    print(f"Accuracy: {acc}")


# 학습한 모델 파라미터 저장하기
torch.save(
    {
        "model_name": "FashionClassifier",
        "epoch": 35,
        "state_dict": model.state_dict()
    },
    "model_weight.pt"
)
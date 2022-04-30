import torch
import numpy as np

from model import FashionClassifier
from data import get_test_data_loader


model = FashionClassifier()  # 모델 먼저 초기화하고,
model.load_state_dict(
    torch.load("model_weight.pt")["state_dict"]
)  # 모델에 저장했던 파라미터 불러와서 로드하기
print("Loaded model!")

print("Calculating accuracy...")
test_data_loader = get_test_data_loader(
    "fashion_mnist/test.csv"
)
model.eval()
with torch.no_grad():
    correctness = list()
    for imgs, labels in test_data_loader:
        y = model(imgs)
        y = torch.argmax(y, dim=1)
        correctness.extend(labels == y)  # [True, False, False, True, ...]
    acc = np.mean(correctness)  # 맞은 개수 / (맞은 개수 + 틀린 개수)
    print(f"Accuracy: {acc}")

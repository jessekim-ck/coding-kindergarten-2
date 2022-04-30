import torch
from torchvision import transforms

import pandas as pd
from PIL import Image


class FashionDataset(torch.utils.data.Dataset):

    def __init__(self, csv_file_path, transform):
        data = pd.read_csv(csv_file_path)
        self.transform = transform

        self.labels = data["label"].values
        self.img_paths = data["path"].values

        self.length = len(self.labels)  # 50000

    def __getitem__(self, idx):
        label = self.labels[idx]
        
        img_path = "fashion_mnist/" + self.img_paths[idx]  # idx 번째 이미지 경로
        img = Image.open(img_path)  # 이미지 열기
        img = self.transform(img)  # 후처리

        return img, label

    def __len__(self):
        return self.length


def get_train_data_loader(csv_file_path):
    dataset = FashionDataset(
        csv_file_path,
        transforms.Compose([
            transforms.RandomHorizontalFlip(),  # 50%의 확률로 좌우 반전
            transforms.ToTensor()  # numpy array를 torch tensor로 전환 + 픽셀값을 255로 나눔
        ])
    )
    return torch.utils.data.DataLoader(
        dataset,
        batch_size=32,  # 한 번에 32개의 데이터를 묶어서 주기로
        shuffle=True  # 데이터셋의 순서를 섞어서 던져주기로
    )


def get_test_data_loader(csv_file_path):
    dataset = FashionDataset(
        csv_file_path,
        transforms.Compose([
            transforms.ToTensor()
        ])
    )
    return torch.utils.data.DataLoader(
        dataset,
        batch_size=64,
        shuffle=False
    )

if __name__ == "__main__":
    data_loader = get_train_data_loader("fashion_mnist/train.csv")
    iterator = iter(data_loader)
    img, label = next(iterator)

    print(img)
    print(label)

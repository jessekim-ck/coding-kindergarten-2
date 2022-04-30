from data import get_train_data_loader
from model import FashionClassifier, EfficientNet


def infer():
    data_loader = get_train_data_loader("fashion_mnist/train.csv")
    x, y = next(iter(data_loader))

    model = FashionClassifier()
    # model = EfficientNet.from_name(
    #     "efficientnet-b0",
    #     num_classes=10
    # )
    y_ = model(x)  # equiv. to `model.forward(x)`

    print(y_)


if __name__ == "__main__":
    infer()
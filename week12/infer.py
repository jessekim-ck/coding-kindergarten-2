from data import get_train_data_loader
from model import FashionClassifier


def infer():
    data_loader = get_train_data_loader("fashion_mnist/train.csv")
    x, y = next(iter(data_loader))

    model = FashionClassifier()
    y_ = model(x)  # equiv. to `model.forward(x)`

    print(y_)


if __name__ == "__main__":
    infer()
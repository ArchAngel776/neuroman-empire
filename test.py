from os import path

import torch

from torch.nn import Module, CrossEntropyLoss, Conv2d, Linear, Sequential, ReLU, BatchNorm1d, BatchNorm2d
from torch.nn.functional import max_pool2d, dropout, dropout2d
from torch.optim import SGD
from torch.utils.data import DataLoader

from torchvision import datasets
from torchvision.transforms.v2 import Compose, ToImageTensor, ConvertImageDtype, RandomHorizontalFlip, RandomAffine

from app import ROOT, MODEL, ML_BATCH_SIZE, ML_OPT_LEARNING_RATE, ML_OPT_MOMENTUM, ML_EPOCHS


# Model definition

class ImagesDetectorNetwork(Module):
    def __init__(self):
        super().__init__()
        self.relu = ReLU()

        self.conv_layer_1 = Sequential(
            Conv2d(3, 32, kernel_size=3, padding=1),
            BatchNorm2d(32),
            self.relu,
            Conv2d(32, 32, kernel_size=3, padding=1),
            BatchNorm2d(32),
            self.relu
        )

        self.conv_layer_2 = Sequential(
            Conv2d(32, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            self.relu,
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            self.relu
        )

        self.conv_layer_3 = Sequential(
            Conv2d(64, 128, kernel_size=3, padding=1),
            BatchNorm2d(128),
            self.relu,
            Conv2d(128, 128, kernel_size=3, padding=1),
            BatchNorm2d(128),
            self.relu
        )

        self.lin1 = Sequential(
            Linear(128 * 4 * 4, 128),
            BatchNorm1d(128),
            self.relu
        )

        self.lin2 = Linear(128, 10)

    def forward(self, x):
        x = dropout2d(max_pool2d(self.conv_layer_1(x), 2, 2), p=.2)
        x = dropout2d(max_pool2d(self.conv_layer_2(x), 2, 2), p=.3)
        x = dropout2d(max_pool2d(self.conv_layer_3(x), 2, 2), p=.4)

        x = torch.flatten(x, 1)

        x = dropout(self.lin1(x), p=.5)

        return self.lin2(x)

    @property
    def classes(self):
        return "plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"


# Create datasets

training_transform = Compose([
    RandomHorizontalFlip(),
    RandomAffine(degrees=0, translate=(.1, .1)),
    ToImageTensor(),
    ConvertImageDtype()
])

test_transform = Compose([
    ToImageTensor(),
    ConvertImageDtype()
])


training_data = datasets.CIFAR10(
    root=ROOT,
    download=True,
    train=True,
    transform=training_transform
)

test_data = datasets.CIFAR10(
    root=ROOT,
    download=True,
    train=False,
    transform=test_transform
)


# Load data

training_loader = DataLoader(training_data, batch_size=ML_BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_data, batch_size=ML_BATCH_SIZE, shuffle=False)


# Init model_old

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = ImagesDetectorNetwork()
model.to(device)

if path.exists(MODEL) and path.isfile(MODEL):
    model.load_state_dict(torch.load(MODEL))
    model.eval()


# Optimization

loss_function = CrossEntropyLoss()
optimizer = SGD(model.parameters(), lr=ML_OPT_LEARNING_RATE, momentum=ML_OPT_MOMENTUM)


# Deep learning

for epoch in range(ML_EPOCHS):
    # Epoch init

    running_loss = 0.

    correct_prediction = {
        class_name: 0 for class_name in model.classes
    }

    total_prediction = {
        class_name: 0 for class_name in model.classes
    }

    # Training

    for i, data in enumerate(training_loader, 0):
        inputs, labels = data[0].to(device), data[1].to(device)

        optimizer.zero_grad()

        outputs = model(inputs)

        loss = loss_function(outputs, labels)
        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        if i % 150 == 149:
            print(f"[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 150:.3f}")
            running_loss = 0.

    # Tests

    with torch.no_grad():
        for data in test_loader:
            inputs, labels = data[0].to(device), data[1].to(device)

            outputs = model(inputs)
            _, predictions = torch.max(outputs.data, 1)

            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_prediction[model.classes[label]] += 1

                total_prediction[model.classes[label]] += 1

    # Epoch result

    for class_name, correct_count in correct_prediction.items():
        accuracy = 100 * float(correct_count) / total_prediction[class_name]
        print(f"Accuracy for class: {class_name:5s} is {accuracy:.1f} %")

    torch.save(model.state_dict(), MODEL)


print("Deep learning done!")

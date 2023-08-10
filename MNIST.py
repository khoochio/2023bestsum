from torchvision import datasets
from torchvision.transforms import ToTensor 
train = datasets.MNIST(
    root = 'C:/Users/user/Desktop/data',
    train = True,                         
    transform = ToTensor(), 
    download = True,            
)

import torch

train_data = torch.utils.data.DataLoader(dataset=train, 
                                           batch_size=16, 
                                           shuffle=True)

import matplotlib.pyplot as plt
t1 = next(iter(train_data))
print(t1[1][0])
plt.imshow(t1[0][0][0])

t1[0].shape

t1[0][0].shape # sample, width, heigh
import torch.nn as nn

class classicationmodel(nn.Module):
    def __init__(self):
        super( classicationmodel,self).__init__()
        self.linear1 = nn.Linear(28*28, 100) 
        self.linear2 = nn.Linear(100, 50) 
        self.final = nn.Linear(50, 10)
        self.relu = nn.ReLU()

    def forward(self, image):
        x = image.view(-1, 28*28)
        x = self.relu(self.linear1(x))
        x = self.relu(self.linear2(x))
        x = self.final(x)
        return x

cmodel = classicationmodel()

cmodel(t1[0])

import torch.optim as optim
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(cmodel.parameters(), lr=0.01)

criterion(cmodel(t1[0]),t1[1])

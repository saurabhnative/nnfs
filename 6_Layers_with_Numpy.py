# Implement multilayer neural network using numpy
import numpy as np

#Input Values
X = [[1,2,5,7],
     [0.5,0.6,0.7,0.8],
     [1.2,2.1,2.2,1],
     [1.3,4.5,6.7,8.9]    
    ]

#Class for creating layer
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

#Sample layer example
layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
# print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)


'''
Output:
[[ 0.23578061  0.04330904]
 [ 0.04591294  0.00409279]
 [ 0.15820558 -0.00793119]
 [ 0.37765267  0.05743735]]
'''


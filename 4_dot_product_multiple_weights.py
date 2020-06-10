#Example of dot product of multiple wieghts using numpy
import numpy as np

#Sample input
inputs = [1,2,3,2.5]

#Sample weights
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]

#bias values
bias = [1,2,3]

#Summation of inputs and weights
summation = np.dot(weights, inputs) 

#Final output of perceptron
output = summation + bias

#Print output
print(output)


"""
Program output:
[3.8   0.21  4.885]
"""



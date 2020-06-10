#Example of dot product using numpy
import numpy as np

#Sample input to perceptron
inputs = [1.2, 2.2, 3.3, 2.5]

#Weights passed to perceptron
weights = [0.4,0.6,-0.7, 1.1]

#bias for a particular perceptron
bias = 2

#Take dot product between weights and input 
#and add bias to the summation value
output = np.dot(inputs, weights) + bias
print(output)

#Output:-
4.24
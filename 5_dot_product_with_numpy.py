import numpy as np

inputs = [[1.0,2.0,3.0,4.0],
          [2.3,3.4,5.6,7.8],
          [1.2,3.4,5.6,9.7]
         ]

wieghts = [[0.2,-0.6,4.7,3.7],
           [-2.8,9.7,2.8,4.8],
           [0.7,3.5,6.7,9.1] 
          ]

biases = [2.0,3.0,5.6]

outputs = np.dot(inputs, np.array(wieghts).T) + biases

print(outputs)
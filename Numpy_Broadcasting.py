# Numpy Broadcasting

import numpy as np

# when two array are not of equal size they are performed by making size equal and then following operations

a=np.array([[1,2,3],[4,5,6]])
b=np.array([2,3,4])
print(np.sum([a,b]))
print()
print(np.subtract(a,b))
print()
print(np.multiply(a,b))
print()
print(np.divide(a,b))

'''
[[ 3  5  7]
 [ 6  8 10]]

[[-1 -1 -1]
 [ 2  2  2]]

[[ 2  6 12]
 [ 8 15 24]]

[[0.5        0.66666667 0.75      ]
 [2.         1.66666667 1.5       ]]
'''
# Basic of Numpy

import numpy as np

#Numpy Basic Meathods
# functions below which estimated o/p is written

a=np.zeros([3,4])
print(a)
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

print(np.arange(10,25,5))
'''
[10 15 20]
'''

print(np.arange(6))
'''
[0 1 2 3 4 5]
'''

print(np.full([5,6],7))
'''
[[7 7 7 7 7 7]
 [7 7 7 7 7 7]
 [7 7 7 7 7 7]
 [7 7 7 7 7 7]
 [7 7 7 7 7 7]]
'''

print(np.linspace(5,6,7))
#example
'''
[5.         5.16666667 5.33333333 5.5        5.66666667 5.83333333
 6.        ]
'''

print(np.random.random([3,4]))
#example
'''
[[0.99617166 0.37578954 0.89045527 0.69061383]
 [0.12104095 0.84556253 0.71863965 0.92271056]
 [0.73418333 0.0070335  0.01753762 0.689775  ]]
'''

a=np.array([[1,2,3],[4,5,6]])
print(a.dtype)
print(a.shape)
print(a.ndim)
'''
int32
(2, 3)
2
'''
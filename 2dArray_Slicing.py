# 2d array slicing

import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[0])
print()
print(a[:1])
print()
print(a[:1,:1])
print()
print(a[:1,1:])
print()
print(a[:,1:])
print()
print(a[:2,2:])

'''
[1 2 3]

[[1 2 3]]

[[1]]

[[2 3]]

[[2 3]
 [5 6]
 [8 9]]

[[3]
 [6]]
'''
# concatenation of array

import numpy as np

#1d array concatenation is done normally

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.concatenate([a,b]))

'''
[1 2 3 4 5 6]
'''

#2d array have both vertical and horizintal concatenation

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[3,4,5],[5,6,7]])
print(np.concatenate([a,b],axis=0))
print()
print(np.concatenate([a,b],axis=1))

'''
[[1 2 3]
 [4 5 6]
 [3 4 5]
 [5 6 7]]

[[1 2 3 3 4 5]
 [4 5 6 5 6 7]]
'''
# numpy split function

import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print(np.split(a,2,0))
print()
print(np.split(a,2,axis=0))
print()
print(np.split(a,3,axis=1))      #division is in equal parts
print()
print(np.split(a,[1,2],axis=0))   #divided into a[:1] a[1:2] a[2:]
print()
print(np.split(a,[1,2],axis=1))   # divided into a[:,:1] a[:,1:2] a[:,2:]

'''
[array([[1, 2, 3]]), array([[4, 5, 6]])]

[array([[1, 2, 3]]), array([[4, 5, 6]])]

[array([[1],
       [4]]), array([[2],
       [5]]), array([[3],
       [6]])]

[array([[1, 2, 3]]), array([[4, 5, 6]]), array([], shape=(0, 3), dtype=int32)]

[array([[1],
       [4]]), array([[2],
       [5]]), array([[3],
       [6]])]
'''
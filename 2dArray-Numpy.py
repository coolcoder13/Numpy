# 2d in Numpy

import numpy as np

# 2-D array meathods

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(np.sum([a,b]))
print(np.sum([a,b],axis=0))
print(np.sum([a,b],axis=1))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.sin([a,b]))
print(np.log([a,b]))
print(np.equal(a,b))
print(np.array_equal(a,b))

'''
[5 7 9]
21
[5 7 9]
[ 6 15]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]
[[ 0.84147098  0.90929743  0.14112001]
 [-0.7568025  -0.95892427 -0.2794155 ]]
[[0.         0.69314718 1.09861229]
 [1.38629436 1.60943791 1.79175947]]
[False False False]
False
'''
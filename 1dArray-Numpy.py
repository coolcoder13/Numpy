# 1d in Numpy

import numpy as np

#1-D array meathods (aggregate functions are for 1d)

a=np.array([1,2,3,4])
print(np.sum(a))
print(np.sin(a))
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.corrcoef(a))
'''
10
[ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
4
1
2.5
2.5
1.118033988749895
1.0
'''
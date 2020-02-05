# -*- coding:utf-8 -*-
import numpy as np 

# Shape 数组的形状取决于其每个轴上的元素个数
a = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
print a
# [[1 2 3 4]
#  [2 3 4 5]
#  [3 4 5 6]]
print a.shape
# (3, 4)

# reshape 改变数组形状
a.ravel()
a.shape=(2, 6)
a.transpose()
print a
# [[1 2 3 4 2 3]
#  [4 5 3 4 5 6]]
print a.reshape(4, 3)
# [[1 2 3]
#  [4 2 3]
#  [4 5 3]
#  [4 5 6]]
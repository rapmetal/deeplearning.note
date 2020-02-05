# -*- coding:utf-8 -*-
import numpy as np 

'''
    array函数
    构造一个ndarray
'''
array = np.array([(1,2,3), (7.0, 3.1, 4.78)])  

print (array)
# 输出格式
# [[ 1.    2.    3.  ]
# [ 7.    3.1   4.78]]

print (array.dtype)
# dtype: 表示数组中元素类型的对象，可使用标准的python类型创建或指定dtype
# 🈶️int64 和 float64，向下兼容到float64

print (array.shape)
# shape: 数组的维度。为一个表示数组在每个维度上大小的整数元组。
# 例如二维数组中，表示数组的“行数”和“列数”。
# ndarray.shape返回一个元组，这个元组的长度就是维度的数目，即ndim属性
# (2, 3)

print (array.ndim)
# ndim: 数组的维数（即数组轴的个数），等于秩。最常见的为二维数组（矩阵）
# 2

print (array.size)
# size: 数组元素的总个数，等于shape属性中元组元素的乘积
# 2 * 3 = 6

print (array.itemsize)
# itemsize: 数组中每个元素的字节大小。
# 例如，一个元素类型为float64的数组itemsiz属性值为8
# (float64占用64个bits，每个字节长度为8，所以64/8，占用8个字节），
# 又如，一个元素类型为complex32的数组item属性为4（32/8）
# 8

'''
    zeros函数
    创建一个全部为0的array
'''
zero_array = np.zeros((3, 5))

print (zero_array)
#[[ 0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.]]
print (zero_array.dtype)
# float64

'''
    ones函数
    创建一个全部为1的array
'''

ones_array = np.ones((2, 2, 3))
print (ones_array)
# [[[ 1.  1.  1.]
# [ 1.  1.  1.]]
#
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]]
print (ones_array.dtype)
# float64

'''
    empty函数
    创建一个内容随机并且依赖与内存状态的数组
'''
empty_array = np.empty((2, 5))
print (empty_array)
# [[  3.10503618e+231  -3.11108148e+231   6.93131184e-310   9.88131292e-324
#    6.93131184e-310]
# [  6.93131184e-310   6.93131184e-310   2.18582438e-314   6.93128705e-310
#    0.00000000e+000]]
print (empty_array.dtype)
# float64

'''
    arange函数
    返回一个数列形式的数组
    
'''
print (np.arange(4))
# [0 1 2 3]
arange = np.arange(0, 40, 4)
print (arange)
# 从0到40，差值为4的等差数列：
# [ 0  4  8 12 16 20 24 28 32 36]
print (arange.dtype)
# int64

'''
    linespace函数
'''
linspace = np.linspace(0, 5, 5)
print (linspace)
# [ 0.    1.25  2.5   3.75  5.  ]
print (linspace.dtype)
# float64

'''
    np.vstack(tup)使用
    沿着竖直方向将矩阵堆叠起来。
    Note: the arrays must have the same shape along all but the first axis. 
    除开第一维外，被堆叠的矩阵各维度要一致。
'''
print np.vstack((np.array([1, 2, 3]), np.array([4, 5, 6])))
# [[1 2 3]
# [4 5 6]]

'''
    np.hstack(tup)
    沿着水平方向将数组堆叠起来。
    Note:
    tup : sequence of ndarrays
    All arrays must have the same shape along all but the second axis.
'''
print np.hstack((np.array([1, 2, 3]), np.array([4, 5, 6])))
# [1 2 3 4 5 6]
print np.hstack((np.array([[1, 2], [3, 4], [5, 6]]), 
                np.array([[7, 8], [9, 0], [0, 1]])))
# [[1 2 7 8]
#  [3 4 9 0]
#  [5 6 0 1]]
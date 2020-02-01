# -*- coding:utf-8 -*-
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

# Example Data
Xi=np.array([2.29, 7.51, 3.29, 6.41, 4.8, 2.96, 3.98, 2.5, 9.1, 4.2])
Yi=np.array([4.35, 9.83, 4.45, 8.31, 4.1, 4.23, 5.05, 1.98, 10.5, 6.3])


def func(p, x):
    k, b = p
    return k * x + b

def error(p, x, y):
    return func(p, x) - y

p0 = [1, 20]
Para=leastsq(error,p0,args=(Xi,Yi))
k, b = Para[0]
print("k=", k, "b=", b)
print("cost：" + str(Para[1]))
print("求解的拟合直线为:")
print("y=" + str(round(k,2)) + "x+" + str(round(b,2)))

plt.figure(figsize=(8,6))
plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2) 

x=np.linspace(0,12,100)
y=k*x+b
plt.plot(x,y,color="red",label="拟合直线",linewidth=2) 
plt.legend(loc='lower right')
plt.show()
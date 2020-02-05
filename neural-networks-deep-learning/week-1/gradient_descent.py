# -*- coding:utf-8 -*-
import numpy as np

# 定义一个数据集的规模
dataset_size = 20

# 构造一个 dataset_size规模的X0，X1
X0 = np.ones((dataset_size, 1))
X1 = np.arange(1, dataset_size + 1).reshape(dataset_size, 1)
X = np.hstack((X0, X1))

# 构造一个 dataset_size规模的y
y = np.array([
    3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
    11, 13, 13, 16, 17, 18, 17, 19, 21
]).reshape(dataset_size, 1)

# The Learning Rate alpha.
alpha = 0.01

def loss_function(theta, X, y):
    '''Loss function J definition.'''
    diff = np.dot(X, theta) - y
    return (1./2 * dataset_size) * np.dot(np.transpose(diff), diff)
    
def gradient_function(theta, X, y):
    '''Gradient of the function J definition.'''
    diff = np.dot(X, theta) - y
    return (1. / dataset_size) * np.dot(np.transpose(X), diff)

def gradient_descent(X, y, alpha):
    '''Perform gradient descent.'''
    theta = np.array([1, 1]).reshape(2, 1)
    gradient = gradient_function(theta, X, y)
    while not np.all(np.absolute(gradient) <= 1e-5):
        theta = theta - alpha * gradient
        gradient = gradient_function(theta, X, y)
    return theta

optimal = gradient_descent(X, y, alpha)
print('optimal:', optimal)
print('error function:', loss_function(optimal, X, y)[0,0])
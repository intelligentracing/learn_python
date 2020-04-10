## This is course material for Introduction to Python Scientific Programming
## Class 18 Example code: gradient_descent.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()

sample_count = 100
x_sample = 10*np.random.random(sample_count)-5
y_sample = 2*x_sample - 1 + np.random.normal(0, 1.0, sample_count)

# plots the parameter space
ax2 = fig.add_subplot(1,1,1, projection = '3d')

def penalty(para_a, para_b):
    global x_sample, y_sample, sample_count

    squares = (y_sample - para_a*x_sample - para_b)**2
    return 1/2/sample_count*np.sum(squares)

a_arr, b_arr = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1) )

func_value = np.zeros(a_arr.shape)
for x in range(a_arr.shape[0]):
    for y in range(a_arr.shape[1]):
            func_value[x, y] = penalty(a_arr[x, y], b_arr[x, y])

ax2.plot_surface(a_arr, b_arr, func_value, color = 'red', alpha = 0.8)
ax2.set_xlabel('a parameter')
ax2.set_ylabel('b parameter')
ax2.set_zlabel('f(a, b)')

# Plot the gradient descent

def grad(aa):
    global sample_count, y_sample, x_sample

    grad_aa = np.zeros(2)
    update_vector = 1/sample_count * (y_sample - aa[0] * x_sample - aa[1])
    grad_aa[0] = - x_sample.dot(update_vector)
    grad_aa[1] = - np.ones(sample_count).dot(update_vector)
    return grad_aa


aa = np.array([-4, 4])
ax2.scatter(aa[0], aa[1], penalty(aa[0],aa[1]), marker = 'o')
delta = np.inf
epsilon = 0.001
learn_rate = 0.1
# Update vector aa
while delta > epsilon:
    aa_next = aa - learn_rate * grad(aa)
    delta = np.linalg.norm(aa - aa_next)
    aa = aa_next
    ax2.scatter(aa[0], aa[1], penalty(aa[0],aa[1]), marker = 'o')

plt.show()
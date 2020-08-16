## This is course material for Introduction to Python Scientific Programming
## Class 19 Example code: least_squares_penalty.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)

# subplot 1 plots the noisy samples
# Define the model
x = np.arange(-5, 5, 0.1)
y = 2*x - 1
plt.plot(x, y, 'gray', linewidth = 3)

# Generate noisy sample
sample_count = 100
x_sample = 10*np.random.random(sample_count)-5
y_sample = 2*x_sample - 1 + np.random.normal(0, 1.0, sample_count)
# Try some colormaps: hsv, gray, pink, cool, hot
ax1.scatter(x_sample, y_sample, c = x_sample, cmap = 'hsv')

# subplot 2 plots the parameter space
ax2 = fig.add_subplot(1,2,2, projection = '3d')

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

# Find the minimum value
optimal_x, optimal_y = np.where(func_value == np.amin(func_value))
ax2.scatter(a_arr[min_x, min_y], b_arr[min_x, min_y], func_value[min_x, min_y],marker = '*')

plt.show()
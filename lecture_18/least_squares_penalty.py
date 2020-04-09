## This is course material for Introduction to Python Scientific Programming
## Class 18 Example code: least_squares_penalty.py
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
y = 2*x -1
plt.plot(x, y, 'gray', linewidth = 3)

# Generate noisy sample
sample_count = 20
x_sample = 10*np.random.random(sample_count)-5
y_sample = 2*x_sample-1 + np.random.normal(0, 1.0, sample_count)
ax1.scatter(x_sample, y_sample, c = x_sample, cmap = 'hsv')

# subplot 2 plots the parameter space
ax2 = fig.add_subplot(1,2,2, projection = '3d')

def penalty(para_a, para_b):
    global x_sample, y_sample

    squares = (y_sample - para_a*x_sample - para_b)**2
    return 1/len(x_sample)*np.sum(squares)

a_arr, b_arr = np.meshgrid(np.arange(-5, 5, 0.1), np.arange(-5, 5, 0.1) )

func_value = np.zeros(a_arr.shape)
for x in range(len(a_arr)):
    for y in range(len(a_arr[x])):
            func_value[x, y] = penalty(a_arr[x, y], b_arr[x, y])

ax2.plot_surface(a_arr, b_arr, func_value, color = 'red', alpha = 0.8)

ax2.scatter(2, -1, penalty(2,-1),marker = '*')

plt.show()
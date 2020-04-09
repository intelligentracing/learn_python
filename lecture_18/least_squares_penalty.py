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

plt.show()
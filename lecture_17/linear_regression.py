## This is course material for Introduction to Python Scientific Programming
## Class 17 Example code: linear_regression.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

# Define the model
x = np.arange(-5, 5, 0.1)
y = 2*x -1
l1,=plt.plot(x, y, 'gray', linewidth = 3)
l1.set_label('Model')

# Generate noisy sample
ax = plt.axes()
sample_count = 20
x_sample = 10*np.random.random(sample_count)-5
y_sample = 2*x_sample-1 + np.random.normal(0, 1.0, sample_count)
ax.scatter(x_sample, y_sample, c = x_sample, cmap = 'hsv')

A = np.zeros((sample_count, 2))
for i in range(sample_count):
    A[i,0] = x_sample[i]
    A[i,1] = 1.0

aa = np.linalg.lstsq(A, y_sample, rcond = None)[0]
print(aa)

y_estimate = aa[0]*x + aa[1]
l2, = plt.plot(x, y_estimate, 'r', linewidth = 3)
l2.set_label('Prediction')
ax.legend()

plt.show()
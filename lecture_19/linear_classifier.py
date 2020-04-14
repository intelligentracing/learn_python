## This is course material for Introduction to Python Scientific Programming
## Class 19 Example code: linear_classifier.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

# describe an underlying linear separation model y = 3x - 2
def linear_model(x):
    return 3*x - 2

# generate two classes that are separable by the linear model
class_sample_count = 25  # Generate 10 samples in Class 0 and 10 in Class 1
x_sample_class_0 = 10 * np.random.random(class_sample_count) - 5
x_sample_class_1 = 10 * np.random.random(class_sample_count) - 5
y_sample_class_0 = linear_model(x_sample_class_0)+ 25*np.random.random(class_sample_count)
y_sample_class_1 = linear_model(x_sample_class_1) - 25*np.random.random(class_sample_count)
y_sample = np.append(y_sample_class_0, y_sample_class_1)
x_sample = np.append(x_sample_class_0, x_sample_class_1)

# Display the two classes
plt.plot(x_sample_class_0, y_sample_class_0, '*r')
plt.plot(x_sample_class_1, y_sample_class_1, 'Db')

# Display the underlying model
x = np.arange(-6, 6, 0.1)
y = linear_model(x)
plt.plot(x, y, 'gray', linewidth = 3)

plt.show()
## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_sigmoid.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)

# Move left y-axis and bottim x-axis to centre
ax1.spines['left'].set_position('center')
ax1.spines['bottom'].set_position('center')
# Eliminate upper and right axes
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

plt.plot(x,sig, linewidth = 3)

ax2 = fig.add_subplot(1,2,2)
# Move left y-axis to centre
ax2.spines['left'].set_position('center')
ax2.spines['bottom'].set_position(('data',0))
# Eliminate upper and right axes
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')

plt.plot(x,sig,  linewidth = 3)

plt.show()
## This is course material for Introduction to Python Scientific Programming
## Class 15 Example code: plot_euler_number.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
from matplotlib import pyplot

x = np.arange(0,10,0.1)
y = (1+1/x)**x
e = np.e*np.ones(len(x))

pyplot.plot(x, y)
pyplot.plot(x, e, color = 'r', dashes = [4,2])
pyplot.show()
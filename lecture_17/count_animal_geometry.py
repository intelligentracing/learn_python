## This is course material for Introduction to Python Scientific Programming
## Class 17 Example code: linear_system_geometry.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,50,1)
y1 = 35 - x
y2 = 55 - 2*x

line1, = plt.plot(x, y1, 'r', linewidth = 3)
line1.set_label('Total pigs and chicken = 35')
line2, = plt.plot(x, y2, 'b', linewidth = 3)
line2.set_label('Total leg count = 110')
intersection, = plt.plot(20, 15, 'kD', markersize = 8)
intersection.set_label('[20, 15]')
plt.legend()

plt.show()

## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_histogram.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.' # From War and Peace

hist = np.zeros(0)
for c in text:
    if c.isalpha():
        index = ord(c.lower()) - ord('a')
        np.append(hist, index)

plt.hist(hist, bin = [0:26])
plt.title("ASCII histogram")
plt.show()

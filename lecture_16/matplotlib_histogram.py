## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_histogram.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.' # From War and Peace

hist_labels = list('abcdefghijklmnopqrstuvwxyz') # label the 26 histogram bins with their text

hist = np.zeros(0)
for c in text:
    if c.isalpha():
        index = ord(c.lower()) - ord('a')
        hist = np.append(hist, index)

plt.hist(hist, 26, facecolor = 'green', alpha = 0.5)
plt.title("ASCII histogram")
#plt.xticks(list(range(0,26)), hist_labels)   # This option will print tick lables at the beginning of a bin
plt.xticks(np.array(np.arange(0,26))+0.5, hist_labels)
plt.xlim(0,26)
plt.show()

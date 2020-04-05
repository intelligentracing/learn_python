## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_histogram.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt

text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.' # From War and Peace

hist_labels = list('abcdefghijklmnopqrstuvwxyz') # label the 26 histogram bins with their text

hist = np.zeros(0, dtype = int)
for c in text:
    if c.isalpha():
        index = int(ord(c.lower()) - ord('a'))
        hist = np.append(hist, index)
print(hist)

max_value = np.max(hist)
n, bins, patches = plt.hist(hist, max_value+1, facecolor = 'green', alpha = 0.5)
plt.title("ASCII histogram")
label_axis = (bins[1:26] + bins[0:25])/2 
plt.xticks(label_axis, hist_labels)
plt.xlim(0,max_value+1)
plt.show()

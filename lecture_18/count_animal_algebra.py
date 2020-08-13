## This is course material for Introduction to Python Scientific Programming
## Class 18 Example code: count_animal_algebra.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np

A = np.array([[1,1],[4,2]])
b = np.array([35, 110])
Ainv = np.linalg.inv(A)
print('A inverse =\n', Ainv)

xx = Ainv.dot(b)
print('Animal count vector = ', xx)

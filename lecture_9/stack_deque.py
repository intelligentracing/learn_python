## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: stack_deque.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque

S = deque()
S.append(5)
S.append(1)
S.append(4)
print(S.pop())
print(S.pop())
print(S.pop())

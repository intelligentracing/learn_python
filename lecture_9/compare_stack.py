## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: compare_stack.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque
from random import sample
from time import time

# Generate a sufficiently long list for comparison
sample_count = 1000000
random_input = sample(range(0, sample_count),sample_count)

# Test speed of enqueue and dequeue operations in list type
test_list=[]
begin_time = time()
for i in random_input:
    test_list.append(i)

for i in range(sample_count):
    test_list.pop(-1)

elapsed_time = time() - begin_time
print('List FILO time: {}'.format(elapsed_time))

# Test speed of push and pop operations in dequeue type
test_stack=deque()
begin_time = time()
for i in random_input:
    test_stack.append(i)

for i in range(sample_count):
    test_stack.pop()

elapsed_time = time() - begin_time
print('Stack FILO time: {}'.format(elapsed_time))
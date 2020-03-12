## This is course material for Introduction to Python Scientific Programming
## Class 8 Example code: compare_queue.py
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
    test_list.pop(0)

elapsed_time = time() - begin_time
print('List FIFO time: {}'.format(elapsed_time))

# Test speed of enqueue and dequeue operations in dequeue type
test_queue=deque()
begin_time = time()
for i in random_input:
    test_queue.append(i)

for i in range(sample_count):
    test_queue.popleft()

elapsed_time = time() - begin_time
print('Queue FIFO time: {}'.format(elapsed_time))
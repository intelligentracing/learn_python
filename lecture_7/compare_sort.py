## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: compare_sort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random
import time

# Generate a sufficiently long list for sorting
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method 1: Insert Sort ********
print('*** Insert Sort ***')
begin_time = time.time()

for index in range(sample_count):
    
    # Compare and sort elements one by one
    current = random_input[index]

    while index>0 and random_input[index-1]>current:
        random_input[index] = random_input[index-1]
        random_input[index-1] = current
        index -=1

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(random_input[0:20])




# ******** Method 2: 
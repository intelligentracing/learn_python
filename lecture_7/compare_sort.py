## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: compare_sort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random
import time

def insert_sort(input_list):
    ''' A custom function to sort number sequences using insert sort
    Parameters:
    Input:  input_list  - Expecting a list of numerical numbers

    Output: status      - Boolean: True or False
            input_list  - sorted list if status is True
    '''
    if type(input_list)!=list:
        return False

    for index in range(1, len(input_list)):
    
        # Compare and sort elements one by one
        current = input_list[index]

        # Verify the type of each element
        if type(current)!=int and type(current)!=float:
            current = float(current)

        # Insert to previous sorted sub-list
        while  (index>0 and input_list[index-1]>current):
            # Insert iteratively until insert condition is False
            input_list[index] = input_list[index-1]
            input_list[index-1] = current
            index -=1
    
    return True

# Generate a sufficiently long list for sorting
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method 1: Insert Sort ********
print('*** Insert Sort ***')
result = random_input.copy()
begin_time = time.time()
insert_sort(result)

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])

# ******** Method 2: Built-in Timsort ******
print('*** Python Sort ***')
result = random_input.copy()
begin_time = time.time()
result.sort()

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])
## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: compare_sort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random
import time

ASCENDIND_ORDER = 0
DESCENDIND_ORDER = 1

def insert_sort(input_list, order = 0):
    ''' A custom function to sort number sequences using insert sort
    Parameters:
    Input:  input_list  - Expecting a list of numerical numbers
            order       - Ascending or descending order, default = 0

    Output: status      - Boolean: True or False
            input_list  - sorted list if status is True
    '''
    
    for index in range(len(input_list)):
    
        # Compare and sort elements one by one
        current = input_list[index]

        # Verify the type of each element
        if type(current)!=int and type(current)!=float:
            return False

        # Insert to previous sorted sub-list
        while index>0 and input_list[index-1]>current:
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




# ******** Method 2: 
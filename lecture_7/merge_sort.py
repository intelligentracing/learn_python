## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: merge_sort.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random
import time

def merge_sort(input_list):
    ''' Merge sort function using recursion
    Parameters:
    Input:  input_list  - a list of numerical numbers

    Output: input_list  - sorted list
    '''
    
    # Deploy Divide-and-Conquer
    if len(input_list)>1:
        mid = len(input_list)//2
        left_half = input_list[:mid]
        right_half = input_list[mid:]

        # Recursively sort left and right sub-lists
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging left_half and right_half 
        left_pointer=0
        right_pointer=0
        merged_pointer=0
        while left_pointer < len(left_half) and right_pointer < len(right_half):
            if left_half[left_pointer] <= right_half[right_pointer]:
                input_list[merged_pointer]=left_half[left_pointer]
                left_pointer=left_pointer+1
            else:
                input_list[merged_pointer]=right_half[right_pointer]
                right_pointer=right_pointer+1
            merged_pointer=merged_pointer+1

        while left_pointer < len(left_half):
            input_list[merged_pointer]=left_half[left_pointer]
            left_pointer=left_pointer+1
            merged_pointer=merged_pointer+1

        while right_pointer < len(right_half):
            input_list[merged_pointer]=right_half[right_pointer]
            right_pointer=right_pointer+1
            merged_pointer=merged_pointer+1

# Generate a sufficiently long list for sorting
sample_count = 10000
random_input = random.sample(range(0, sample_count),sample_count)

# ******** Method: Merge Sort ********
print('*** Merge Sort ***')
result = random_input.copy()
begin_time = time.time()
merge_sort(result)

# tic-toc 
elapsed_time = time.time() - begin_time
print(elapsed_time)
print(result[0:20])
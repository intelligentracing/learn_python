## This is course material for Introduction to Python Scientific Programming
## Class 8 Example code: sort_queue.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque

def sort_deque(input_deque, reverse = False):
    ''' a sorting algorithm for deque treated as an FIFO queue
    Solution uses recursing merging 1 and (n-1) queues

    parameters:
    Input:  input_deque - a deque type 
            reverse     - bool type, ascending by default False, descending by True
    
    Output: input_queue - return sorted values
    '''

    if type(input_deque)!=deque or type(reverse)!=bool:
        raise TypeError('Input arguments are not allowed.')

    if len(input_deque)==1:
        return input_deque
    
    first = input_deque.popleft()               # pop the first element
    sorted_deque = sort_deque(input_deque)      # recursively sort the (n-1) elements

    # Merge first and sorted_deque into one return deque
    new_deque = deque()
    while len(sorted_deque)>0:
        k_element = sorted_deque.popleft()
        if first <  k_element:
            new_deque.append(first)
            new_deque.append(k_element)
            break
        else:
            new_deque.append(k_element)
    else:
        new_deque.append(first)     # if while never breaks, first should be the last

    while len(sorted_deque)>0:      # After break, if any elements left in sorted_deque
        k_element = sorted_deque.popleft()
        new_deque.append(k_element)
        
    return new_deque

input_deque = deque([7,2,3,6,4,1,5])
print(sort_deque(input_deque))
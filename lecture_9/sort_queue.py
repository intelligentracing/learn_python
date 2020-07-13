## This is course material for Introduction to Python Scientific Programming
## Class 9 Example code: sort_queue.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from collections import deque

def sort_deque(input_deque):
    ''' a sorting algorithm for deque treated as an FIFO queue
    Solution uses recursing merging 1 and (n-1) queues in default ascending order
    Parameters:
    Input:  input_deque - a deque type 
    Output: input_queue - return sorted values
    '''

    if type(input_deque)!=deque:
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
            first = None
            break
        else:
            new_deque.append(k_element)
    
    if not first is None:
        new_deque.append(first)     # first is not None, manually add it to the end
    elif len(sorted_deque)>0:    # sorted_deque is not empty, manually add it to the end
        new_deque.extend(sorted_deque) 
        
    return new_deque

input_deque = deque([7,2,3,6,4,1,5])
print(sort_deque(input_deque))
## This is course material for Introduction to Python Scientific Programming
## Class 10 Example code: DP_fibonacci.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from time import time

def fibonacci(n):
    ''' A recursive function to calculate the Fibonacci number
    Parameters:
    - Input: n an integer >= 0
    - Output: Integer Fibonacci number
    '''

    if type(n)!= int:
        raise TypeError('Incorrect Fibonacci argument type.')
    elif n<0:
        raise ValueError('Fibonacci argument must be greater than zero.')

    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def DP_fibonacci(n):
    ''' More efficiently solving fibonacci using a global variable to remember sub-problems
    Parameters:
    - Input: n an integer >=0
    - Output: Integer Fibonacci number
    '''

    if not 'fib_memory' in globals():
        # global variable fib_memory has not been initiated
        global fib_memory 
        fib_memory = [None]*(n + 1)
        fib_memory[0] = 0
        fib_memory[1] = 1

    if fib_memory[n]==None:
        # fib_memory does not have memory of the nth result
        fib_memory[n] = DP_fibonacci(n-1) + DP_fibonacci(n-2)
    
    return fib_memory[n]

limit = 40

# This is using the basic recursion without storing the sub-problem solutions
begin_time = time()
result = fibonacci(limit)
elapsed_time = time() - begin_time
print('Calculating fibonacci({0}) took {1}s'.format(limit, elapsed_time))

# This is using dynamic programming with a global memory
begin_time = time()
result = DP_fibonacci(limit)
elapsed_time = time() - begin_time
print('Calculating DP_fibonacci({0}) took {1:.10f}s'.format(limit, elapsed_time))
print(result)

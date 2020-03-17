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

fib_memory = [None]*(limit + 1)
fib_memory[0] = 0
fib_memory[1] = 1

def DP_fibonacci(n):
    ''' More efficiently solving fibonacci using a global variable to remember sub-problems
    Parameters:
    - Input: n an integer >=0
    - Output: Integer Fibonacci number
    '''
    global fib_memory

    if fib_memory[n]==None:
        # fib_memory does not have memory of the nth result
        fib_memory[n] = DP_fibonacci(n-1) + DP_fibonacci(n-2)
    
    return fib_memory[n]

limit = 40

begin_time = time()
result = fibonacci(limit)
elapsed_time = time() - begin_time
print('Calculating {0} took {1}s'.format(result, elapsed_time))

begin_time = time()
result = DP_fibonacci(limit)
elapsed_time = time() - begin_time
print('Calculating {0} took {1}s'.format(result, elapsed_time))

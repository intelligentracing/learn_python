## This is course material for Introduction to Python Scientific Programming
## Class 6 Example code: find_prime.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use
import math
import sys

string_input = input("Please provide an integer limit for finding prime numbers: ")
try:  # Try to catch posible error when int_limit is not an integer
    int_limit = int(string_input)
except: # When runtime error occurs, except will be executed
    print("Not a valid integer input. Exit!")
else: # else means no runtime error
    if int_limit<2:   # Testing prime only meaningful for numbers >=2
        print("No prime number within the range")
        sys.exit()
    for n in range(2, int_limit+1):
        if n==2:  # Number 2 is defined as a the first prime number 
            print(n, 'is a prime number')
            continue

        # if n is > 2, test if n can be divided by two nontrivial integers
        for x in range(2, math.ceil(math.sqrt(n)+1)):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
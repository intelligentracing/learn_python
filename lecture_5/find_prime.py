## This is course material for Introduction to Python Scientific Programming
## Class 5 Example code: find_prime.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use


int_limit = input("Please provide an integer limit for finding prime numbers: ")
try:
    int_limit = int(int_limit)
except:
    print("Not a valid integer input. Exit!")
else:
    if int_limit<2:
        print("No prime number within the range")
        exit
    for n in range(2, int_limit):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')
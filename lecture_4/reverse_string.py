## This is course material for Introduction to Python Scientific Programming
## Class 4 Example code: reverse_string.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use


input_string = "Python"

# Method 1, using loop
reversed_string = ""
index = len(input_string) # index point to last character + 1
while index>0:
    index = index -1
    reversed_string = reversed_string + input_string[index]

print(reversed_string)

# Method 2, using slicing
reversed_string = input_string[len(input_string)-1::-1]
print(reversed_string)

sliced_string = input_string[::-1]
print(sliced_string)
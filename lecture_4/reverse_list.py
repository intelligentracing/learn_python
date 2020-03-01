## This is course material for Introduction to Python Scientific Programming
## Class 2 Example code: reverse_list.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

List = list("Python")

# Method 1, using loop
reversed_list = []
index = len(List) # index point to last character + 1
while index>0:
    index = index -1
    reversed_list.append(List[index])

print(reversed_list)

# Method 2: extended slicing
reversed_list = List[::-1]
print(reversed_list)

# Method 3: use object method
reversed_list = List.copy()
reversed_list.reverse()  # reverse in-place
print(reversed_list)
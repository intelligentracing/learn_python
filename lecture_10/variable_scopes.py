## This is course material for Introduction to Python Scientific Programming
## Class 10 Example code: variable_scopes.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Use of local variables

local_variable = 1
global_variable = 1

mutable_list = [1]

def local_variable_function():

    print('local variable {0} in a function.'.format(local_variable))

    global global_variable
    global_variable = 10

    mutable_list.append(2)
    mutable_local_list = [3]

local_variable_function()

print('global variable {0} outside a function.'.format(global_variable))
print(mutable_list)
print(mutable_local_list)
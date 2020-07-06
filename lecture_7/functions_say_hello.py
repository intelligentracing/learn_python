## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: functions_say_hello.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def print_hello_world():
    ''' The function prints Hello World! string
    '''
    print('Hello World!') 

def print_string(argin):
    ''' The function converts argin to string and print
    '''
    try:
        string = str(argin)
    except:
        print('Illegal input! exit')
    else: 
        print(string) 

def hello_world():
    ''' The function returns Hellow World! string
    '''
    return('Hello World!')
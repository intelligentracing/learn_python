## This is course material for Introduction to Python Scientific Programming
## Class 7 Example code: func_test.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def func_test(L = ['a', 'b'], S = 'ab'):
    ''' Append and return one mutable list and one immutable string. '''
    L.append('c')
    S = S + 'c'
    return L, S

def func_test1(L , S ):
    ''' Append and return one mutable list and one immutable string. '''
    L.append('c')
    S = S + 'c'
    return S

def func_test2(L):
    ''' Append and return one mutable list and one immutable string. '''
    global S

    L= L.append('c')
    S = S + 'c'

L = ['a', 'b']; S = 'ab'
S = func_test1(L, S)
print('{0}, {1}'.format(L,S))

L = ['a', 'b']; S = 'ab'
func_test2(L)
print('{0}, {1}'.format(L,S))
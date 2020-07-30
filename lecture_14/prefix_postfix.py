## This is course material for Introduction to Python Scientific Programming
## Class 14 Example code: prefix_postfix.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

class PrefixPostfix:
    def __init__(self):
        self._internal = 0
        self.__double_underscore = 'name mangling'
        self.__prefix_postfix_double__ = 'no change'

    def print_out(self):
        print('_internal: ', self._internal)
        print('_double_underscore: ', self.__double_underscore)
        print('__prefix_postfix_double__: ', self.__prefix_postfix_double__)

test = PrefixPostfix()
test.print_out()
print(dir(test))
print(test._PrefixPostfix__double_underscore)
## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: person_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

class Person:
    ''' An example class to show Python Class definitions'''
    
    retirement_age = 65

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(selfish):
        print('First Name: {0}, Last Name: {1}'.format(selfish.first_name, selfish.last_name))

x1 = Person('John', 'Smith')
x2 = Person('Jane', 'Doe')
x1.print_name()
x2.print_name()
print(x1.retirement_age)

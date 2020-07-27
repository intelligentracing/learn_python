## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: person.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

class Person:
    ''' An example class to show Python Class definitions'''
    
    retirement_age = 65   # Class attribute

    def __init__(self, first_name, last_name):
        if type(first_name)!=str or type(last_name)!=str:
            raise TypeError('Person class initailzed with the unsupported types.')

        self.first_name = first_name
        self.last_name = last_name
        self.age = None

    def set_age(self, age):
        if age<0:
            raise ValueError('age attribute in Person must be nonnegative.')

        self.age = age

    def print_name(selfish):
        print('First Name: {0}, Last Name: {1}'.format(selfish.first_name, selfish.last_name))

    @classmethod
    def set_retirement_age(careful, retirement_age):
        if retirement_age<0:
            raise ValueError('age attribute in Person must be nonnegative.')

        careful.retirement_age = retirement_age

    @classmethod    
    def years_until_retirement(cls, age):
        until_retirement_year = cls.retirement_age - age
        if until_retirement_year<=0:
            print('This person has retired')
        else:
            print('This person has {0} years until retirement'.format(until_retirement_year))

    @staticmethod
    def copyright():
        print('This class is for noncommercial use only!')
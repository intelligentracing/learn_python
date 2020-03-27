## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: student_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from person_class import Person

class Student(Person):

    next_ID = 0

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.student_ID = Student.next_ID
        Student.next_ID += 1

    def __del__(self):
        print(self.student_ID, 'deleted')

    def __add__(self, other):
        return [self, other]

    def print_ID(self):
        print('{0} {1}\'s student ID is: {2}'.format(self.first_name, self.last_name, self.student_ID))

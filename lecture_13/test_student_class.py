## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: test_student_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from student_class import Student

s1 = Student('John', 'Smith')
s2 = Student('Jane', 'Doe')

enroll = s1 + s2
enroll[0].print_name()
enroll[0].print_ID()


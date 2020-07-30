## This is course material for Introduction to Python Scientific Programming
## Class 14 Example code: test_student_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from student import Student

s1 = Student('John', 'Smith', 2024)
s2 = Student('Jane', 'Doe', 2024)

s1.set_age(18)
s1.years_until_retirement()

print(s2.year_of_graduation())
print(s2.student_ID)
print(Student.ID_record)
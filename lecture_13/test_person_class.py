## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: test_person_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from person import Person

x1 = Person('John', 'Smith')
x1.print_name()

x2 = Person('Jane', 'Doe')
x2.print_name()
print(x2.first_name, 'Retirement Age: ', x1.retirement_age)

Person.years_until_retirement(42)

print(x1.first_name, 'Retirement Age:', x1.retirement_age)
x1.retirement_age = 80
print(x1.first_name, 'Retirement Age:', x1.retirement_age)
x1.set_retirement_age(80)
print('Class Retirement Age:',Person.retirement_age)

Person.copyright()
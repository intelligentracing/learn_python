## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: test_person_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from person_class import Person

x1 = Person('John', 'Smith')
x2 = Person('Jane', 'Doe')
x1.print_name()
x2.print_name()
print(x1.retirement_age)
Person.years_until_retirement(42)
Person.years_until_retirement(80)
Person.copyright()

print(id(x1))
x1.retirement_age = 70
print(id(x1))

x2 = x1; print(id(x2))

import copy
x3 = copy.copy(x1); print(id(x3))
print(x3.retirement_age)
## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: test_person_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from person import Person

x1 = Person('John', 'Smith')
x2 = Person('Jane', 'Doe')
x1.print_name()
x2.print_name()

print(x1.retirement_age)
Person.years_until_retirement(42)
x1.set_age(80)
x1.years_until_retirement(x1.age)
Person.copyright()
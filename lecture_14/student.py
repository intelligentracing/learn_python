## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: student.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from person import Person

class Student(Person):

    ID_record = dict()

    def __init__(self, first_name, last_name, class_year):
        super().__init__(first_name, last_name)
        self.set_ID(class_year)
    
    def set_ID(self, class_year):
        if type(class_year)!=int:
            raise TypeError('class_year shall be an integer')
        if class_year < 1900 or class_year>2999:
            raise ValueError('Class year value is not supported')

        if class_year in Student.ID_record:
            Student.ID_record[class_year] += 1
        else:
            Student.ID_record[class_year] = 1
        
        self.student_ID = str(class_year) + \
            format(Student.ID_record[class_year],'04d')


    def year_of_graduation(self):
        return (int(self.student_ID[0:4]))
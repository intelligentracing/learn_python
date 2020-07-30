## This is course material for Introduction to Python Scientific Programming
## Class 14 Example code: shape_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

class Shape:
    ''' An example class that defines an empty abstract shape '''
    initiated = False

    def get_area(self):
        ''' virtual method to calculate area of a shape'''
        pass

    @classmethod
    def is_init(cls):
        ''' return True if a shape has been assigned to the class'''
        return cls.initiated

class Square(Shape):
    ''' A subclass of Shape, specifically for calculating square area'''

    def __init__(self, width):
        self.width = width
        self.get_area()
        self.__class__.initiated = True      
    
    def get_area(self):
        ''' Area of a square is its width times width'''
        self.area = self.width*self.width
        return self.area
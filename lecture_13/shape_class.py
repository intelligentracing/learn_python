## This is course material for Introduction to Python Scientific Programming
## Class 13 Example code: shape_class.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

class Shape:
    initiated = False

    def get_area(self):
        pass

    @classmethod
    def is_init(cls):
        return cls.initiated

class Square(Shape):

    def __init__(self, width):
        self.width = width
        self.get_area()
        self.__class__.initiated = True      
    
    def get_area(self):
        self.area = self.width*self.width
        return self.area
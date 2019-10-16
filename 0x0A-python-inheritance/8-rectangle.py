#!/usr/bin/python3
"""
Module for a class Rectangle
that inherits from BaseGeometry
"""


class BaseGeometry:
    """
    base geometry still empty
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """
    rectangle clasee herencia from BaseGeometry
    """
    def __init__(self, width, height):
        """
        init constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

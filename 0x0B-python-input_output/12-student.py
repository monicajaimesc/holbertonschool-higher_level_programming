#!/usr/bin/python3
"""
Module that contain a class Student
"""


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return studen dictionary """
        temporal_dict = {}
        if attrs is None:
            return self.__dict__
        temporal_dict = dict()
        # only attribute names
        # contained in this list must be retrieved
        for key in attrs:
            if key in self.__dict__.keys():
                temporal_dict[key] = self.__dict__[key]
        return temporal_dict

#!/usr/bin/python3
"""
Module that contain the first class Base
"""


class Base:
    """
    This class will be the “base” of all other
    classes in this project.
    """
    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor with its
        assign the public instance attribute id
        Args:
            id - value greater than 0
        """
        if id is not None:
            # public instance attribute
            self.id = id
        else:
            Base.__nb_objects += 1
            # assign the new value to the public instance attribute id
            self.id = Base.__nb_objects

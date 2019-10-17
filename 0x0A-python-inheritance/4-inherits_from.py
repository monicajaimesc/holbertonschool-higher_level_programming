#!/usr/bin/python3
"""
Module to check if object is an instance of a
class that inherited (directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

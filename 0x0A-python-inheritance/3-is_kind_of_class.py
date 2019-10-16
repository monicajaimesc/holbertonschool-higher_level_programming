#!/usr/bin/python3
"""
Module that cointain function that check if an object
is an instance of or object is an instance of a class
that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    object is the most base class and a_class is an instance
    return condition true or false
    """
    # isinstance(object, type)
    return (isinstance(obj, a_class))

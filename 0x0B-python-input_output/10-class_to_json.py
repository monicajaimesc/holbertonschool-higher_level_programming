#!/usr/bin/python3
"""
Module that contain a function that returns
the dictionary description for JSON of an object
"""


def class_to_json(obj):
    """
    returns the dictionary descritpion
    """
    return obj.__dict__

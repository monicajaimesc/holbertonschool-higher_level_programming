#!/usr/bin/python3
"""
Module that contains a function that returns an
object represented by Json string
"""
import json


def from_json_string(my_str):
    """ Decoding JSON: """
    return json.loads(my_str)
    # ['streaming API']

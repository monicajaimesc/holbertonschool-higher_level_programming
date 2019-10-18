#!/usr/bin/python3
"""
Module that contains a funtion that
returns number of lines of a text file:
"""


def number_of_lines(filename=""):
    """
    return number of lines
    in the text file
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        counter_lines = 0
        for line in f:
            counter_lines += 1
    return counter_lines

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
    with open("my_file_0.txt", mode='r' , encoding="utf-8") as f:
        counter = 0
        for line in f:
            counter += 1 
    f.closed
    return counter

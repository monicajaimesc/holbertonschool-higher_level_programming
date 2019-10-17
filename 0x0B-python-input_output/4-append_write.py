#!/usr/bin/python3
"""
Module that contains a function that appends
a string at the end of a tex file
"""


def append_write(filename="", text=""):
    """
    return file and a string append it
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        appended_text = f.write(text)
    f.closed
    return (appended_text)

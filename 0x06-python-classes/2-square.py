#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares
"""


class Square:
    """
    Square class: was created it
    """
    def __init__(self, size=0):
        """
        init for the square class. Basic error checking for int size.
        """
        # size must be an integer
        if not isinstance(size, int):
            # otherwhise raise a TypeError
            raise TypeError("size must be an integer")
        # if size is less than 0
        if size < 0:
            # raise a ValueError
            raise ValueError("size must be >= 0")
        self.__size = size

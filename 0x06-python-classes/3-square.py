#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares
"""


class Square:
    """
    Square class: enabling you to print out of area(size) of the square
    amazing and new
    """
    def __init__(self, size=0):
        """
        init for the square class. Requieres a valid integer size.
        """
        if not isinstance(size, int):
            # otherwhise raise a TypeError
            raise TypeError("size must be an integer")
        # if size is less than 0
        if size < 0:
            # raise a ValueError
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square (size ** 2)
        """
        return (self.__size ** 2)

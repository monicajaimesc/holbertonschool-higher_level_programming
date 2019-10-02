#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares
"""


class Square:
    """
    Square class now has a setters and getters for the size
    amazing and new
    """
    def __init__(self, size=0):
        """
        Square class init! takes in a size
        """
        # methos that inherit from the class
        self.size = size

    @property
    def size(self):
        """
        Size getter, returns the private size.
        """
        # return current area
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Size setter, sets the size
        """
        # it has to be an integer
        if type(value) != int:
            # otherwhise raise a TypeError
            raise TypeError("size must be an integer")
        # if size is less than 0
        if value < 0:
            # raise a ValueError
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        # Returns the area of the square
        return (self.__size ** 2)

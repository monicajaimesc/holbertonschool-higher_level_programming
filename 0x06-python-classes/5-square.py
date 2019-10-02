#!/usr/bin/python3
"""
Square Module - for all your needs, as long as they include printing squares!
"""


class Square:
    """
    Square class, now with a function to print the square
    """
    # Instantiation with optional size:
    def __init__(self, size=0):
        """
        Init for square! Takes in a size, defaults to 0.
        """
        self.__check_size__(size)
        self.__size = size

    @property
    # property def size(self): to retrieve it
    def size(self):
        """
        Size getter, returns the private size.
        """
        return (self.__size)

    @size.setter
    # property setter def size(self, value): to set it:
    def size(self, value):
        """
        Size setter, sets the private size.
        """
        self.__check_size__(value)
        self.__size = value

    # Public instance method:
    def area(self):
        """
        Returns the area of the square.
        """
        return (self.__size ** 2)

    # Public instance method, could do it with join as well:
    def my_print(self):
        """
        Prints the square! Should only print a newline if size is 0.
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if j == (self.size - 1):
                        print("#")
                        break
                    print("#", end="")

    def __check_size__(self, size):
        """
        Size error checking!
        """
        # size must be an integer, otherwise raise a TypeError exception
        if type(size) != int:
            raise TypeError("size must be an integer")
        # if size is less than 0, raise a ValueError
        if size < 0:
            raise ValueError("size must be >= 0")

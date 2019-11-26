#!/usr/bin/python3
"""
Square Module - for all your needs.
"""


class Square:
    """
    Square class for square objects. Square square square.
    Square is one of those words that looks stranger the more you type it.
    """
    # Instantiation with optional size and optional position:
    def __init__(self, size=0, position=(0, 0)):
        """
        Square init. Square. Skware
        Now takes a position for your sqware
        """
        self.size = size
        self.position = position

    @property
    # Private instance attribute: size:
    def size(self):
        """
        Getter for the size of the square
        """
        return (self.__size)
    # create the private variable
    @size.setter
    def size(self, value):
        """
        Setter for setting sqwar size.
        """
        # calling the setter
        self.__check_size__(value)
        self.__size = value

    # Private instance attribute: position:
    @property
    def position(self):
        """
        Getter for the size of ya square
        """
        return (self.__position)

    # property setter def position(self, value)
    @position.setter
    def position(self, value):
        """
        Setter for square position
        where your square is
        """
        # to set it:
        # size must be an integer
        self.__check_pos__(value)
        # size is less than 0
        self.__position = value

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
        Now includes the position to print them at.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for h in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    if k == (self.size - 1):
                        print("#")
                        break
                    print("#", end="")

    # create a new attribute in python
    def __check_pos__(self, position):
        """
        Error checking for a square position
        position must be a tuple of 2 positive integers
        """
        if (type(position) != tuple or len(position) != 2 or
            type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            # otherwise, raise a TypeError
            raise TypeError("position must be a tuple of 2 positive integers")

    def __check_size__(self, size):
        """
        Error checking for square sizes!
        Must be a valid integer, >= 0
        """
        # size must be an integer, otherwise raise a TypeError exception
        if type(size) != int:
            raise TypeError("size must be an integer")
        # if size is less than 0, raise a ValueError
        if size < 0:
            raise ValueError("size must be >= 0")

#!/usr/bin/python3
"""
Square Module - for all your square needs.
"""


class Square:
    """
    Square class for square objects. Square square square.
    Square is one of those words that looks stranger the more you type it.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Square init. Square. Skware
        Now takes a position for your sqwar
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size of ya skware
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter for setting sqwar size.
        """
        self.__check_size__(value)
        self.__size = value

    @property
    def position(self):
        """
        Getter for the position of your skare.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter for square position.
        WHERE UR SQKWAR AT
        """
        self.__check_pos__(value)
        self.__position = value

    def area(self):
        """
        Returns the area of the skware.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints your squarez!
        Now includes the position to print them at.
        """
        if (self.__size == 0):
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join((" " * self.__position[0]) + "#" * self.__size
                            for i in range(self.__size)))

    def __check_pos__(self, position):
        """
        Error checking for skware positions!
        Must be a tuple with two positive integers!
        """
        if (type(position) != tuple or len(position) != 2 or
            type(position[0]) != int or type(position[1]) != int or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __check_size__(self, size):
        """
        Error checking for square sizes!
        Must be a valid integer, >= 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

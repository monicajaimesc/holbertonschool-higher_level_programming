#!/usr/bin/python3
""" Rectangle Module - For rectangular purposes only. """


class Rectangle:
    """ Rectangle class For rectangles ONLY. """
    # Public class attribute
    number_of_instances = 0
    # Public class attribute
    print_symbol = '#'

    # Instantiation
    def __init__(self, width=0, height=0):
        """ init """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ string conversion """
        string = ((str(self.print_symbol) * self.__width) + '\n')*self.__height
        return string[:-1]
    # repr() should return a string representation
    # of the rectangle to be able to recreate a
    # new instance by using eval()

    def __repr__(self):
        """ string conversion """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    # Private instance attribute:
    def width(self):
        """ width getter """
        return self.__width

    # property sette
    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.__height * self.__width

    # Public instance method
    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest
        rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        # always we will call a function with ()
        if rect_1.area() >= rect_2.area():
            # Returns rect_1 if both have the same area value
            return (rect_1)
        return (rect_2)

    @classmethod
    # CLS" is a reference to "fraction
    def square(cls, size=0):
        return Rectangle(size, size)

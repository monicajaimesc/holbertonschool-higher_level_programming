#!/usr/bin/python3
"""
Module that contain a Class Rectangle
inherits from Base, private instance attributes
width and height
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle subclass, inherited from Base Class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Class constructor
        """
        # Private instance attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # Call the super class with id
        # this super call use the logic of the __init__ of the Base class
        super().__init__(id)

    # instance attributes with its own public getter and setter:
    @property
    def width(self):
        """width Getter"""

        return self.__width
    # Why not directly public attribute with getter/setter?
    # to protect attributes of our class.
    # With a setter, you are able to validate
    # what a developer is trying to assign to a variable.
    # So after, in your class you can “trust” these attributes.
    @width.setter
    def width(self, value):
        """ width setter, sets width """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """X setter """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('value must be >= 0')
        self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """X setter """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Y Getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

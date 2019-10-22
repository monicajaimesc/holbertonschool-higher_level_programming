#!/usr/bin/python3
"""Module that contains a class square"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor:
            __init__ method: initialize the passing variables
            Args:
                size: size of square
                x: x position of square
                y: y position of square
                id: id of square
        """
        # Call the super class, it'll use the logic
        # of the __init__ of the Rectangle
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """__str__ method: return a string
        Return:
            return [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y, self.width))
        # Now you have a Square class who has the same attributes
        # and same methods.

    @property
    def size(self):
        """Getter: get size of square
        return: size of square
        """

        return self.width

    @size.setter
    def size(self, value):
        """Setter: set argument value to size
        Args:
            Value: size of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update public method: assigns a key/value argument to each attribute
        Args:
            Kwargs: double point to a dictionary: key/value
        """
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super(Rectangle, self).__init__(arg)
                if idx == 1:
                    self.size = arg
                if idx == 2:
                    self.x = arg
                if idx == 3:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super(Rectangle, self).__init__(value)
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """to_dictionary public method: Rectangle instance to dictionary
        representation
        Return:
            returns the dictiory representation of a Rectangle
        """
        # attrs_list = ["id", "width", "height", "x", "y"]
        # return {key: getattr(self, key) for key in attrs_list}
        return {'id': self.id, 'y': self.y, 'x': self.x, 'size': self.size}

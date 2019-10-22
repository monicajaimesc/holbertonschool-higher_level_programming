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
        """Getter: get width of the
        rectangle"""

        return self.__width
    # Why not directly public attribute with getter/setter?
    # to protect attributes of our class.
    # With a setter, you are able to validate
    # what a developer is trying to assign to a variable.
    # So after, in your class you can “trust” these attributes.

    @width.setter
    def width(self, value):
        """ setter: set the argument value to witdth
        Attributes:
            __width: width of rectangle
        Args:
            value: width of rectangle
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Height Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: set the argumet value to height
        Attributes:
               __height: the height of rectangle
        Args:
               value: the height of rectangle
        Raises:
               TypeError: height must be an integer
               ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ X getter """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter: set argument value to x
        Attributes:
               __x: the x position of rectangle
        Args:
               value: the x position of rectangle
        Raises:
               TypeError: x must be an integer
               ValueError: x must be >= 0
         """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter: get y position of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter: set argument value to y
        Attributes:
               __y: the y position of rectangle
        Args:
               value: the y position of rectangle
        Raises:
               TypeError: y must be an integer
               ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Public method: calulate the area of
        rectangle
        Return:
            return the area
        """
        return self.width * self.height

    def display(self):
        """ display public method: prints in stdout
        the Rectangle instance with the character #
        (take in account x and y position)
        """
        print(self.y * '\n', end='')
        # width = anchura
        row = self.x * ' ' + self.width * '#'
        # string = (('#' * self.__width) + '\n') * self.__height
        # return string[:-1]
        print('\n'.join([row for h in range(self.height)]))

    def __str__(self):
        """overriding the__str__ method: return a string
        Return:
            return [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """update public method: update the dictionary
        (key/value) argument to each attribute
        Args:
            Kwargss: CAN BE! a double pointer to a dictionary: key/value
        """
        if args and len(args) > 0:
            #  kwargs is behavior in terms you’re already familiar wit
            # **kwargs must be skipped if *args exists and is not empty
            # args: non-keyworded variable length argument list to the funtion
            for idx, arg in enumerate(args):
                # enumerate: Return an enumerate object.
                if idx == 0:
                    # self.id = arg
                    super().__init__(arg)
                if idx == 1:
                    self.width = arg
                if idx == 2:
                    self.height = arg
                if idx == 3:
                    self.x = arg
                if idx == 4:
                    self.y = arg
        # if args not exist
        # pass keyworded variable lenght of arguments to a function
        # this is a dictionary, use items
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super().__init__(value)
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
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
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

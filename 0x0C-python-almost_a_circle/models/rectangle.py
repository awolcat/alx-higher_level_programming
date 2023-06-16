#!/usr/bin/python3
"""This module defines a class Rectangle
    that inherits from Base
"""


from models.base import Base

class Rectangle(Base):
    """This class defines a rectangle object that
        inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a rectangle object
            including its id through the Base class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """No args.
            Return width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set width.
            Args: width must be a number
        """
        self.__width = width

    @property
    def height(self):
        """Return height.
            No arguments
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set height property.
            Args: height must be a number
        """
        self.__height = height

    @property
    def x(self):
        """Getter for x.
            Takes no args
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x.
            x must be a number
        """
        self.__x = x

    @property
    def y(self):
        """Getter for y.
            Takes no args
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y.
            y must be a number
        """
        self.__y = y

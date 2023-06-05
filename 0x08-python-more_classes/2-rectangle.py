#!/usr/bin/python3
"""
    This module contains the definition Class: Rectangle

    The class is defined below
"""


class Rectangle:
    """
        This classs defines a rectangle

        The class also defines many functionalities
        that can be applied to any Rectangle object
    """

    def __init__(self, width=0, height=0):
        """
            __init__ prompts initialization of
            width and height attributes for Rectangle object
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """A getter: returns width of an object"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter: sets value of an object's width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: will return object height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: set value for object height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            This public instance method returns the area
            of a Rectangle object
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            This public instance method returns the perimeter
            of a Rectangle object
        """
        p = (self.__width + self.__height) * 2
        return p

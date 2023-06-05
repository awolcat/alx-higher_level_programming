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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A getter: returns width of an object"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter: sets value of an object's width"""
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

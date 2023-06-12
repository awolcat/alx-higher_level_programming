#!/usr/bin/python3
"""
    This module defines a new class: Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
        This Rectangle class is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
            Initialize width and height attributes
            for the object
        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """
            This method calculates and returns the area of
            a rectangle objects
        """
        return self.__width * self.__height

    def __str__(self):
        """
            This magic method defines the print format
            for Rectangle objects
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

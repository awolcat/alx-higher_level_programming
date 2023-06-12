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
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__height = BaseGeometry.integer_validator(self, "height", height)

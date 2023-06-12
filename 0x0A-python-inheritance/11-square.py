#!/usr/bin/python3
"""
    This module defines a Square class that inherits
    from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This class inherits from Rectangle
    """
    def __init__(self, size):
        """
            This function initializes a Square object
        """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """
            This function computes and returns
            the area of a Square object
        """
        return self.__size ** 2

    def __repr__(self):
        """
            This function returns a custom
            string representation of a square object
        """
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

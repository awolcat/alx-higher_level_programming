#!/usr/bin/python3
"""
    This module defines a new class: BaseGeometry
"""


class BaseGeometry():
    """
        This is a base class that defines different objects
    """

    def area(self):
        """
            This function raises an exception that reports
            the fact that the area method is not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            This function validates if value is of type int
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

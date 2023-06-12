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

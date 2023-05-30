#!/usr/bin/python3
"""Module for my first Python Class"""


class Square:
    """My first Python Class"""

    def __init__(self, size=0):
        """Initialize size"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

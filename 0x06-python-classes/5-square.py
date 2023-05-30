#!/usr/bin/python3
"""Module for my first Python Class"""


class Square:
    """My first Python Class"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """Return the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Set size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

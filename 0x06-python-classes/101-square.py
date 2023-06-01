#!/usr/bin/python3
"""Module for my first Python Class"""


class Square:
    """My first Python Class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Return the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Get size property"""
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

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position property"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False or \
                isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for z in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Print the square in #'s"""
        my_str = ""
        for i in range(self.__position[1]):
            my_str += '\n'
        for rows in range(self.__size):
            for i in range(self.__position[0]):
                my_str += " "
            for i in range(self.__size):
                my_str += "#"
            my_str += '\n'

        return my_str[:-1]

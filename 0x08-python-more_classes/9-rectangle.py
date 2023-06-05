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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            __init__ prompts initialization of
            width and height attributes for Rectangle object
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return self.width * self.height

    def perimeter(self):
        """
            This public instance method returns the perimeter
            of a Rectangle object
        """
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = (self.width + self.height) * 2
        return p

    def __str__(self):
        """
            Magic method:
            Returns Rectangle object with '#'
        """
        my_str = ""
        if self.width == 0 or self.height == 0:
            return my_str
        else:
            for tall in range(self.height):
                for wide in range(self.width):
                    my_str += str(self.print_symbol)
                if tall < self.height - 1:
                    my_str += "\n"
            return my_str

    def __repr__(self):
        """
            Magic method:
            Returns string representation of the object
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Deletes a Rectangle object"""
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):

        """
            Determines the bigger rectangle by area between two

            Args:
                both rect1 and rect2 are Rectangle objects

            Returns:
                    The bigger rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Defines a square (l == w) Rectangle object"""
        size = int(size)
        return cls(size, size)

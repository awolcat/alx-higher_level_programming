#!/usr/bin/python3
"""This module describes the class Square
    which inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines a square object
        and has the same characteristics as
        a Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing a square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading str method that returns
            a string representation of a square object
        """
        string = ''
        string += f'[{self.__class__.__name__}] ({self.id})'
        string += f' {self.x}/{self.y} - {self.height}'
        return string

    @property
    def size(self):
        """Size property of a square, which
            is eqaul to its height and width
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the size prperty of a square object
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the attributes of an instance
            Args:
                *args: a variable number of unnamed args
                **kwargs: a variable number of named args
        """
        if args is not None and len(args) > 0:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        else:
            for key in kwargs:
                if key == 'size':
                    self.size = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
                if key == 'id':
                    self.id = kwargs[key]

    def to_dictionary(self):
        """Create and return a dictionary representation
            of  a square object
        """
        dictionary = {
                        'id': self.id,
                        'x': self.x,
                        'size': self.size,
                        'y': self.y
                        }
        return dictionary

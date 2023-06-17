#!/usr/bin/python3
"""This module defines a class Rectangle
    that inherits from Base
"""


from models.base import Base

class Rectangle(Base):
    """This class defines a rectangle object that
        inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method initializes a rectangle object
            including its id through the Base class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """No args.
            Return width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set width.
            Args: width must be a number
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width


    @property
    def height(self):
        """Return height.
            No arguments
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set height property.
            Args: height must be a number
        """
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for x.
            Takes no args
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x.
            x must be a number
        """
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for y.
            Takes no args
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y.
            y must be a number
        """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """Calculates and returns
            The area of an instance
        """
        return self.height * self.width

    def display(self):
        """This method will print the object
            using '#'
        """
        string = ''
        string = '\n' * self.y
        for height in range(self.height):
            string += (' ' * self.x) + ('#' * self.width)
            if height < self.height - 1:
                string += '\n'
        print(string)
        return string

    def __str__(self):
        """This method will return
            a custom string representation
            to the print function/user
        """
        string = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"
        string += f" - {self.width}/{self.height}"
        return string

    def update(self, *args, **kwargs):
        """Update the attributes of an instance
            Args:
                *args: a variable number of unnamed args
        """
        if args is not None and len(args) > 0:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length >= 5:
                self.y = args[4]
        else:
            for key in kwargs:
                if key == 'width':
                    self.width = kwargs[key]
                if key == 'height':
                    self.height = kwargs[key]
                if key == 'x':
                    self.x = kwargs[key]
                if key == 'y':
                    self.y = kwargs[key]
                if key == 'id':
                    self.id = kwargs[key]

    def to_dictionary(self):
        """Create and return a dictionary representation
            of a rectangle
        """
        dic = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
        return dic

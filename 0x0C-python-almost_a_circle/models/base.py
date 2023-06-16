#!/usr/bin/python3
"""This module defines the Base class. This project superclass
    will manage the unique id variable accross the project
"""


class Base:
    """This Base class is the main superclass
        and will manage id for all objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This special method will initialize
            the id variable
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

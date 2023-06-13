#!/usr/bin/python3
"""
    This module defines a class Student
"""


class Student:
    """
        This class defines a student object
    """
    def __init__(self, first_name, last_name, age):
        """This method will initialize the three attributes
            provided as arguments to the class constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method will return a dicrionary
            containing all the attributes of a student object
        """
        return self.__dict__

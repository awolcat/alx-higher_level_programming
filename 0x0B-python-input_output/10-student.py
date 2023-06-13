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

    def to_json(self, attrs=None):
        """This method will return a dicrionary
            containing the attributes of a student object
            named in attrs

            Args:
                attrs: a list of strings (keys)
            Return:
                A dictionary with the named keys and their
                respective values
        """
        obj_dict = self.__dict__
        if isinstance(attrs, list):
            check_str = [isinstance(x, str) for x in attrs]
            if all(check_str):
                new_dict = dict()
                for k in obj_dict:
                    if k in attrs:
                        new_dict[k] = obj_dict[k]
                return new_dict
        return obj_dict

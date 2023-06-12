#!/usr/bin/python3
"""
    This module defines one function only
"""


def inherits_from(obj, a_class):
    """
        This function checks if obj inherits
        from a_class or not and returns True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

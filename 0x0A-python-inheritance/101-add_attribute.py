#!/usr/bin/python3
"""
    This module defines a single function
    that enables the addition of attributes
"""


def add_attribute(obj, attr="", value=""):
    """
        This function will add an attribute
        to the object obj if possible
    """
    if len(dir(obj)) > 26:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)

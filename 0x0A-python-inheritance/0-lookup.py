#!/usr/bin/python3

"""
    This module contains one function lookup(obj)
"""


def lookup(obj):
    """
        This function returns the methods and attributes
        of an object in the form of a list

        Args:
            obj: any object
    """
    return list(dir(obj))

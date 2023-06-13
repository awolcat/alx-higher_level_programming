#!/usr/bin/python3
"""
    This module defines a single function: class_to_json
"""


def class_to_json(obj):
    """
        This function takes an object,
        and returns its attributes as a dictionary
    """
    attributes = obj.__dict__
    return attributes

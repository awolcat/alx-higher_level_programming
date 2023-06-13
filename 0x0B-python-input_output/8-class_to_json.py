#!/usr/bin/python3
"""
    This module defines a single function: class_to_json
"""
import json


def class_to_json(obj):
    """
        This function takes an object,
        serializes its attributes, and returns
        a serialized json object
    """
    attributes = obj.__dict__
    return attributes

#!/usr/bin/python3
"""
    This module defines one function: to_json_string
"""


def to_json_string(my_obj):
    """
        This function will accept any object type
        and attempt to serialize it to a JSON
        representation (string)
    """
    serial = json.dumps(my_obj)
    return serial

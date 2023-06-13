#!/usr/bin/python3
"""
    This module defines one single function: from_json_string
"""
import json


def from_json_string(my_str):
    """
        This function will deserialize a JSON object

        Args:
            my_str: the JSON object to deserialize
        Return:
            deserialized version of my_str
    """
    deserialized = json.loads(my_str)
    return deserialized

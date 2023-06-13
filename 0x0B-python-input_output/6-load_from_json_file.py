#!/usr/bin/python3
"""
    This module defines a single function: load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
        This function will load serialized daata from
        a JSON file and deserialize it

        Args:
            filename: name of the json file
        Return:
            A deserialized object
    """
    with open(filename, encoding="utf-8") as a_file:
        obj = json.load(a_file)
        return obj

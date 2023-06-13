#!/usr/bin/python3
"""
    This module defines a single function: save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
        This function will serialize an object my_obj
        and save the output to a JSON file, filename

        Args:
            my_obj: the object to be serialized
            filename: the JSON file to store the serialized data
        Return:
            nothing
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)

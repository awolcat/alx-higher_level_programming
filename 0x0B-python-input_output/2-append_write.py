#!/usr/bin/python3
"""
    This module defines a single function: append_write
"""


def append_write(filename="", text=""):
    """
        This function appends text to a file filename
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        count = a_file.write(text)
    return count

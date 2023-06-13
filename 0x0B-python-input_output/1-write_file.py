#!/usr/bin/python3
"""
    This module defines a single function: write_file
"""


def write_file(filename="", text=""):
    """
        This function will write text to a file
        and return the number of characters written

        Args:
            filename: name/path to the file as a string
            text: the string to be written to the file
        Return:
            Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        wrote = a_file.write(text)
    return wrote

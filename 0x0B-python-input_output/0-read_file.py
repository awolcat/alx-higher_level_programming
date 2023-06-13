#!/usr/bin/python3
"""
    This module only defines one function: read_file
"""


def read_file(filename=""):
    """
        This function will read an entire file
        and print its contents to stdout

        Args:
            filename(optional): name of the file

        Return:
            nothing
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")

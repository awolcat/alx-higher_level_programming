#!/usr/bin/python3
"""
    This module contains only one function

    The function is described below
"""


def print_square(size):
    """
        This function will print a square
        of the given size

        Size must be an integer >= 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    idx = 0
    while idx < size:
        for i in range(size):
            print("#", end="")
        print()
        idx += 1

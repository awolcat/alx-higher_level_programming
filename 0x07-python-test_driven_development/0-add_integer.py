#!/usr/bin/python3
"""
    The 0-add_integer module contains only one function

    The add_integer function is described below
"""


def add_integer(a, b=98):
    """
        The add_integer function adds two values and returns an integer

        The two arguments must be integers or floats
        or a mixture of both types

        Floats are floored before addition.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

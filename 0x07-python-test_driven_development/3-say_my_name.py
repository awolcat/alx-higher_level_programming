#!/usr/bin/python3
"""
    This module has only one function

    The function is described below
"""


def say_my_name(first_name, last_name=""):
    """
        This function will say your name!

        It must be given a name to say
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""This module defines a single function"""


def find_peak(list_of_integers):
    """Method to find the largest number in a sequence
        args:   a list of integers
        return: an integer
    """
    if len(list_of_integers):
        list_of_integers.sort()
        return list_of_integers[-1]

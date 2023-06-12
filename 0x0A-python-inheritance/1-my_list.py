#!/usr/bin/python3
"""
    This module defines a class MyList that inherits from list
"""


class MyList(list):
    """
        This class inherits from list
        and defines a new method not available in the parent class
    """
    def __init__(self):
        """
            Initialize instance variables in the sub
            and parent class
        """
        pass

    def print_sorted(self):
        """
            This function takes no arguments except self,
            which should be a list of integers,
            and prints it as a sorted list
        """
        new_list = list.copy(self)
        new_list.sort()
        print(new_list)

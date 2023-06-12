#!/usr/bin/python3
"""
    This module defines a class MyInt that
    inherits from int but behaves eerily differently
"""


class MyInt(int):
    """
        This class has inverted logic when its objects
        are used with == and !=
    """
    def __eq__(self, other):
        """
            Comparing equivalent operators/values
            will  evaluate to false
        """
        return (self - other) > 0

    def __ne__(self, other):
        """
            Comparing non-equal values/operators
            will evaluate to True
        """
        return not (self == other)

#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    This module defines unit tests for
    a predefined function max_integer(list=[]) that takes
    a list of integers and returns the largest
    integer
"""
class TestMaxInt(unittest.TestCase):
    """
        This class contains methods that test
        the behavior of the max_integer function
    """
#    def test_input(self):
 #       """Test if the input is a non-empty list"""
  #      self.assertIs(max_integer(), list)

    def test_return(self):
        """Test the return of the function"""
        self.assertIs(max_integer([]), None)
        self.assertIs(max_integer([1, 2, 3, 4]), 4)

#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_arguments(self):
        self.assertRaises(Exception, Rectangle.__init__, self)
        self.assertRaises(Exception, Rectangle.__init__, self, 9)

    def test_init(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        self.assertIsNotNone(obj.id)

        obj = Rectangle(3, 4, 6, 6, 20)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 6)
        self.assertEqual(obj.id, 20)

#!/usr/bin/python3

import unittest
from models import square
Square = square.Square


class TestRectangle(unittest.TestCase):

    def test_doc(self):
        doc_mod = len(square.__doc__)
        doc_class = len(Square.__doc__)
        self.assertTrue(doc_mod > 0)
        self.assertTrue(doc_class > 0)

    def test_init(self):
        # Test for docstring
        doc = len(Square.__init__.__doc__)
        self.assertTrue(doc > 0)
        # Test for initialization
        obj = Square(5)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        self.assertIsNotNone(obj.id)

        obj = Square(4, 6, 6, 20)
        self.assertEqual(obj.size, 4)
        self.assertEqual(obj.x, 6)
        self.assertEqual(obj.y, 6)
        self.assertEqual(obj.id, 20)

    def test_init_types(self):
        # Square without required minimum args
        self.assertRaises(TypeError, Square)
        # Size values and types
        self.assertRaises(TypeError, Square, "2", 3, 3, 3)
        self.assertRaises(ValueError, Square, 0, 3, 3, 3)
        # x and y values and types
        self.assertRaises(ValueError, Square, 2, 3, -1, 9)
        self.assertRaises(ValueError, Square, 4, -3, 2, 1)
        self.assertRaises(TypeError, Square, 3, 3, "3", 2)
        self.assertRaises(TypeError, Square, 3, "3", 3, 2)

    def test_area(self):
        # Test method docstring
        doc = len(Square.area.__doc__)
        self.assertTrue(doc > 0)
        # Test return
        obj = Square(4)
        self.assertEqual(obj.area(), 16)

    def test_display(self):
        # Test method docstring
        doc = len(Square.display.__doc__)
        self.assertTrue(doc > 0)
        # Test output with x, y = 0, 0
        obj = Square(2)
        self.assertEqual(obj.display(), "##\n##")
        # Test output with x and y > 0
        obj = Square(2, 2, 2)
        self.assertEqual(obj.display(), "\n\n  ##\n  ##")

    def test___str__(self):
        doc = len(Square.__str__.__doc__)
        s1 = Square(4, 2, 1, 12)
        self.assertTrue(doc > 0)
        self.assertTrue(str(s1) == "[Square] (12) 2/1 - 4")

    def test_size(self):
        doc = len(Square.size.__doc__)
        self.assertTrue(doc > 0)
        s1 = Square(5)
        self.assertTrue(str(s1) == "[Square] (5) 0/0 - 5")
        s1.size = 10
        self.assertTrue(str(s1) == "[Square] (5) 0/0 - 10")
        self.assertNotIn('height', Square.__dict__)

    def test_update_0(self):
        doc = len(Square.update.__doc__)
        self.assertTrue(doc > 0)
        s1 = Square(5)
        self.assertTrue(str(s1) == "[Square] (6) 0/0 - 5")
        s1.update(10)
        self.assertTrue(str(s1) == "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertTrue(str(s1) == "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertTrue(str(s1) == "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertTrue(str(s1) == "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertTrue(str(s1) == "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertTrue(str(s1) == "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertTrue(str(s1) == "[Square] (89) 12/1 - 7")

#!/usr/bin/python3

import unittest
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):

    def test_doc(self):
        doc_mod = len(rectangle.__doc__)
        doc_class = len(Rectangle.__doc__)
        self.assertTrue(doc_mod > 0)
        self.assertTrue(doc_class > 0)

    def test_init(self):
        # Test for docstring
        doc = len(Rectangle.__init__.__doc__)
        self.assertTrue(doc > 0)
        # Test for initialization
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

    def test_init_types(self):
        # Rectangle without required minimum args
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 9)
        # Height and width values and types
        self.assertRaises(TypeError, Rectangle, "2", 3, 3, 3, 3)
        self.assertRaises(TypeError, Rectangle, 2, "3", 3, 3, 3)
        self.assertRaises(ValueError, Rectangle, 0, 3, 3, 3, 3)
        self.assertRaises(ValueError, Rectangle, 3, 0, 3, 3, 3)
        self.assertRaises(ValueError, Rectangle, -1, 3, 3, 3, 3)
        self.assertRaises(ValueError, Rectangle, 3, -1, 3, 3, 3)
        # x and y values and types
        self.assertRaises(ValueError, Rectangle, 2, 3, -1, 9)
        self.assertRaises(ValueError, Rectangle, 4, 3, 2, -1)
        self.assertRaises(TypeError, Rectangle, 3, 3, "3", 2)
        self.assertRaises(TypeError, Rectangle, 3, 3, 3, "2")

    def test_area(self):
        # Test method docstring
        doc = len(Rectangle.area.__doc__)
        self.assertTrue(doc > 0)
        # Test return
        obj = Rectangle(4, 6)
        self.assertEqual(obj.area(), 24)

    def test_display(self):
        # Test method docstring
        doc = len(Rectangle.display.__doc__)
        self.assertTrue(doc > 0)
        # Test output with x, y = 0, 0
        obj = Rectangle(2, 2)
        self.assertEqual(obj.display(), "##\n##")
        # Test output with x and y > 0
        obj = Rectangle(2, 2, 2, 2)
        self.assertEqual(obj.display(), "\n\n  ##\n  ##")

    def test___str__(self):
        doc = len(Rectangle.__str__.__doc__)
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertTrue(doc > 0)
        self.assertTrue(str(r1) == "[Rectangle] (12) 2/1 - 4/6")

    def test_update_0(self):
        doc = len(Rectangle.update.__doc__)
        self.assertTrue(doc > 0)
        r1 = Rectangle(10, 10, 10, 10)
        self.assertTrue(str(r1) == "[Rectangle] (5) 10/10 - 10/10")
        r1.update(89)
        self.assertTrue(str(r1) == "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertTrue(str(r1) == "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertTrue(str(r1) == "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertTrue(str(r1) == "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertTrue(str(r1) == "[Rectangle] (89) 4/5 - 2/3")

    def test_update_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertTrue(str(r1) == "[Rectangle] (6) 10/10 - 10/10")
        r1.update(height=1)
        self.assertTrue(str(r1) == "[Rectangle] (6) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertTrue(str(r1) == "[Rectangle] (6) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertTrue(str(r1) == "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertTrue(str(r1) == "[Rectangle] (89) 1/3 - 4/2")

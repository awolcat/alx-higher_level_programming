import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_init(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(10).id, 10)

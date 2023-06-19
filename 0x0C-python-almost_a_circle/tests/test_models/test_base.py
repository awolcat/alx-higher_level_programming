import unittest
from models import base
Base = base.Base

class TestBase(unittest.TestCase):

    def test_doc(self):
        doc_mod = len(base.__doc__)
        doc_class = len(Base.__doc__)
        doc_init_m = len(Base.__init__.__doc__)

        self.assertTrue(doc_mod > 0)
        self.assertTrue(doc_class > 0)
        self.assertTrue(doc_init_m > 0)

    def test_base_init(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(10).id, 10)

    def test_to_json_string(self):
        doc = len(Base.to_json_string.__doc__)
        self.assertTrue(doc > 0)
        json_dictionary = Base.to_json_string([])
        self.assertTrue(json_dictionary == "[]")
        json_dictionary = Base.to_json_string([{'height': 2, 'width': 2}])
        self.assertTrue(type(json_dictionary) is str)
        json_dictionary = Base.to_json_string([{'size': 2}])
        self.assertTrue(type(json_dictionary) is str)

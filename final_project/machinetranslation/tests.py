import unittest
from translator import english_to_french
from translator import french_to_english

class test_f2e(unittest.TestCase):
    def not_null(self):
        self.assertNotEqual(french_to_english("Bonjour"), "")
    def test_tran(self):
        self.assertEqual(english_to_french("Bonjour"), "Hello")

class test_e2f(unittest.TestCase):
    def not_null(self):
        self.assertNotEqual(english_to_french("Hello"), "")
    def test_tran(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

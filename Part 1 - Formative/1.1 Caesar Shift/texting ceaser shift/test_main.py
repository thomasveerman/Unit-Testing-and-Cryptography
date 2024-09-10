from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class Testcaesar_encode(TestCase):
    def test_caesar_encode_one_words_lowercase(self):
        self.assertEqual(caesar_encode("orange"), "TWFSLJ")

    def test_caesar_encode_one_words_with_uppercase(self):
        self.assertEqual(caesar_encode("APPLE"), "FUUGJ")

    def test_caesar_encode_empty_insert(self):
        self.assertEqual(caesar_encode("apple", ""), "FUUGJ")

    def test_caesar_encode_empty_text(self):
        self.assertEqual(caesar_encode("", "orange"), "TWFSLJ")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode("  ", "orange"), " TWFSLJ ")
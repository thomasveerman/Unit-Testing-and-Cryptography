from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_encode

class TestcCesarEncode(TestCase):
    def test_caesar_encode_one_words_lowercase(self):
        self.assertEqual(caesar_encode("orange", 5), "TWFSLJ")

    def test_caesar_encode_one_words_with_uppercase(self):
        self.assertEqual(caesar_encode("APPLE", 5), "FUUQJ")

    def test_caesar_encode_empty_text(self):
        self.assertEqual(caesar_encode("", 5), "")

    def test_caesar_encode_whitespace(self):
        self.assertEqual(caesar_encode("apple orange", 5), "FUUQJ TWFSLJ")
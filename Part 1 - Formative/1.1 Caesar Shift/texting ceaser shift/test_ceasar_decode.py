from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode

class TestCesarDecode(TestCase):
    def test_caesar_decode_basic(self):
        encoded_text = "TWFSLJ"
        self.assertEqual(caesar_decode(encoded_text, 5), "ORANGE")


    def test_caesar_decode_empty_text(self):
        self.assertEqual(caesar_decode("", 5), "")


    def test_caesar_decode_whitespace(self):
        self.assertEqual(caesar_decode("FUUQJ TWFSLJ", 5), "APPLE ORANGE")
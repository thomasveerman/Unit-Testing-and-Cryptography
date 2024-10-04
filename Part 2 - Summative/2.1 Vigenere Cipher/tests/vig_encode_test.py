from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode

class Testvigencode(TestCase):

    def test_vig_encode_one_word_lowercase(self):
        key = "TEST"
        self.assertEqual(vig_encode("apple", key), "TTHEX")

    def test_vig_encode_two_word_lowercase(self):
        key = "TEST"
        self.assertEqual(vig_encode("hello", key), "AIDEH")

    def test_vig_encode_one_word_uppercase(self):
        key = "TEST"
        self.assertEqual(vig_encode("ORANGE", key), "HVSGZI")

    def test_vig_encode_empty_string(self):
        key = "TEST"
        self.assertEqual(vig_encode("", key), "")

    def test_vig_encode_long_word_no_space(self):
        key = "TEST"
        self.assertEqual(vig_encode("THECATWASLAZYANDTIRED", key), "MLWVTXOTLPSSREFWMMJXW")
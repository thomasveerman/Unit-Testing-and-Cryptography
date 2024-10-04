from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode

class Testvigdecode(TestCase):
    def test_vig_decode_one_word_lowercase(self):
        key = "TEST"
        self.assertEqual(vig_decode("TTHEX", key), "APPLE")

    def test_vig_decode_two_word_lowercase(self):
        key = "TEST"
        self.assertEqual(vig_decode("AIDEH", key), "HELLO")

    def test_vig_decode_one_word_uppercase(self):
        key = "TEST"
        self.assertEqual(vig_decode("HVSGZI", key), "ORANGE")

    def test_vig_decode_empty_string(self):
        key = "TEST"
        self.assertEqual(vig_decode("", key), "")

    def test_vig_decode_long_word_no_space(self):
        key = "TEST"
        self.assertEqual(vig_decode("MLWVTXOTLPSSREFWMMJXW", key), "THECATWASLAZYANDTIRED")
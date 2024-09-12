from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode


class TestSubstitutionCipher(TestCase):
    def test_sub_decode_basic(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_decode("MXTTHAHOTU", cipher_alphabet), "HELLOWORLD")

    def test_sub_decode_empty_text(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_decode("", cipher_alphabet), "")
    def test_sub_decode_two_words(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_decode("MXTTH AHOTU", cipher_alphabet), "HELLO WORLD")

    def test_sub_decode_two_words_lower_case(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_decode("mxtth ahotu", cipher_alphabet), "HELLO WORLD")

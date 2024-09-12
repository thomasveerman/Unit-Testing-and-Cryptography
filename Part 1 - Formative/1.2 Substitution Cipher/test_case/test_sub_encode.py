from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode


class TestSubstitutionCipher(TestCase):

    def test_sub_encode_one_word(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_encode("HELLOWORLD", cipher_alphabet), "MXTTHAHOTU")
    def test_sub_encode_basic(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_encode("HELLO WORLD", cipher_alphabet), "MXTTH AHOTU")
    def test_sub_encode_empty_text(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_encode("", cipher_alphabet), "")
    def test_sub_encode_one_word_lower_case(self):
        cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
        self.assertEqual(sub_encode("helloworld", cipher_alphabet), "MXTTHAHOTU")





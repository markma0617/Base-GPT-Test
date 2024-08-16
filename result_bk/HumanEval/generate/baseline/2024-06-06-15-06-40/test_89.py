from code_89 import encrypt

import unittest
from my_module import encrypt

class TestEncrypt(unittest.TestCase):

    def test_encrypt_basic(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_encrypt_longer_input(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_encrypt_letters_at_ends(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_encrypt_mixed_letters(self):
        self.assertEqual(encrypt('et'), 'ix')

if __name__ == '__main__':
    unittest.main()

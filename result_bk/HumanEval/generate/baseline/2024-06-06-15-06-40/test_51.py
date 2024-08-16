from code_51 import remove_vowels

import unittest
from your_module import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_string_with_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')
        self.assertEqual(remove_vowels('aaaaa'), '')
        self.assertEqual(remove_vowels('aaBAA'), 'B')
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

if __name__ == '__main__':
    unittest.main()

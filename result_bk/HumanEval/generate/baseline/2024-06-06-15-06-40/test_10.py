from code_10 import make_palindrome
from code_10 import is_palindrome

import unittest
from solution import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    
    def test_make_palindrome_empty_string(self):
        self.assertEqual(make_palindrome(''), '')
    
    def test_make_palindrome_single_character(self):
        self.assertEqual(make_palindrome('a'), 'a')
    
    def test_make_palindrome_palindromic_string(self):
        self.assertEqual(make_palindrome('aba'), 'aba')
    
    def test_make_palindrome_non_palindromic_string(self):
        self.assertEqual(make_palindrome('abc'), 'abcba')
    
    def test_make_palindrome_longer_string(self):
        self.assertEqual(make_palindrome('hello'), 'helloleh')
    
    def test_make_palindrome_even_length_string(self):
        self.assertEqual(make_palindrome('helloo'), 'hellooleh')

if __name__ == '__main__':
    unittest.main()

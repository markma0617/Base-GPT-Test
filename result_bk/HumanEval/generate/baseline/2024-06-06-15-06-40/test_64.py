from code_64 import vowels_count

import unittest

def test():
    class TestVowelsCount(unittest.TestCase):
        
        def test_vowels_count(self):
            self.assertEqual(vowels_count("abcde"), 2)
            self.assertEqual(vowels_count("ACEDY"), 3)
            self.assertEqual(vowels_count("python"), 2)
            self.assertEqual(vowels_count("rhythm"), 0)
            self.assertEqual(vowels_count("hello"), 2)
            self.assertEqual(vowels_count("bye"), 1)
            self.assertEqual(vowels_count("Happy"), 2)
    
    return TestVowelsCount

from code_64 import vowels_count

import unittest

def test():
    class TestVowelsCount(unittest.TestCase):
        def test_vowels_count(self):
            self.assertEqual(vowels_count("abcde"), 2)
            self.assertEqual(vowels_count("ACEDY"), 3)
            self.assertEqual(vowels_count("python"), 1)
            self.assertEqual(vowels_count("hello"), 2)
            self.assertEqual(vowels_count("world"), 1)
            
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVowelsCount)
    unittest.TextTestRunner().run(suite)

test()

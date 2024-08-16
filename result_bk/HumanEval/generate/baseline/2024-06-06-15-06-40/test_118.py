from code_118 import get_closest_vowel

import unittest

def test():
    class TestGetClosestVowel(unittest.TestCase):
        
        def test_example_1(self):
            self.assertEqual(get_closest_vowel("yogurt"), "u")
        
        def test_example_2(self):
            self.assertEqual(get_closest_vowel("FULL"), "U")
            
        def test_example_3(self):
            self.assertEqual(get_closest_vowel("quick"), "")
            
        def test_example_4(self):
            self.assertEqual(get_closest_vowel("ab"), "")
            
        def test_edge_case_short_word(self):
            self.assertEqual(get_closest_vowel("a"), "")
            
        def test_edge_case_no_vowel(self):
            self.assertEqual(get_closest_vowel("xyz"), "")
    
    return TestGetClosestVowel

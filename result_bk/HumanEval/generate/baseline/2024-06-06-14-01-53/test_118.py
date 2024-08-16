from code_118 import get_closest_vowel

import unittest

def test_get_closest_vowel():
    test_cases = {
        "Test case 1": ("yogurt", "u"),
        "Test case 2": ("FULL", "U"),
        "Test case 3": ("quick", ""),
        "Test case 4": ("ab", "")
    }
    
    for name, (input_word, expected_output) in test_cases.items():
        with self.subTest(name):
            self.assertEqual(get_closest_vowel(input_word), expected_output)

if __name__ == '__main__':
    unittest.main()

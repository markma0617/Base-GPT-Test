from code_51 import remove_vowels

import unittest

def test_remove_vowels():
    test_cases = [
        ('', ''),
        ('abcdef\nghijklm', 'bcdf\nghjklm'),
        ('abcdef', 'bcdf'),
        ('aaaaa', ''),
        ('aaBAA', 'B'),
        ('zbcd', 'zbcd'),
    ]
    
    for text, expected_output in test_cases:
        result = remove_vowels(text)
        assert result == expected_output, f"Expected: {expected_output}, but got: {result}"

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

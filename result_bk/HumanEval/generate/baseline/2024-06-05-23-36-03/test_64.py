from code_64 import vowels_count

import unittest

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("python") == 1
    assert vowels_count("aeiou") == 5
    assert vowels_count("why") == 1

if __name__ == '__main__':
    unittest.main()

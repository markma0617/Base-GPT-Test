from code_66 import digitSum

import unittest
from solution import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_all_lower_case(self):
        self.assertEqual(digitSum("abAB"), 131)

    def test_mixed_case(self):
        self.assertEqual(digitSum("abcCd"), 67)

    def test_some_upper_case(self):
        self.assertEqual(digitSum("helloE"), 69)

    def test_multiple_upper_case(self):
        self.assertEqual(digitSum("woArBld"), 131)

    def test_all_upper_case(self):
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()

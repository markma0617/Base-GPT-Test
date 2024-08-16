from code_66 import digitSum

import unittest
from solution import digitSum

class TestDigitSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(digitSum(""), 0)

    def test_uppercase_only(self):
        self.assertEqual(digitSum("abAB"), 131)
        self.assertEqual(digitSum("abcCd"), 67)
        self.assertEqual(digitSum("helloE"), 69)
        self.assertEqual(digitSum("woArBld"), 131)
        self.assertEqual(digitSum("aAaaaXa"), 153)

if __name__ == '__main__':
    unittest.main()

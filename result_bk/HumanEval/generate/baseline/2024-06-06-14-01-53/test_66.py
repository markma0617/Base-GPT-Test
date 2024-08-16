from code_66 import digitSum

import unittest

def test():
    class TestDigitSum(unittest.TestCase):
        
        def test_empty_string(self):
            self.assertEqual(digitSum(""), 0)

        def test_mixed_string1(self):
            self.assertEqual(digitSum("abAB"), 131)

        def test_mixed_string2(self):
            self.assertEqual(digitSum("abcCd"), 67)

        def test_mixed_string3(self):
            self.assertEqual(digitSum("helloE"), 69)

        def test_mixed_string4(self):
            self.assertEqual(digitSum("woArBld"), 131)

        def test_mixed_string5(self):
            self.assertEqual(digitSum("aAaaaXa"), 153)

    return TestDigitSum

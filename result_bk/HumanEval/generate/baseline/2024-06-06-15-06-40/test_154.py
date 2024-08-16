from code_154 import cycpattern_check

import unittest
from your_module import cycpattern_check

class TestCycPatternCheck(unittest.TestCase):

    def test_cycpattern_check(self):
        self.assertFalse(cycpattern_check("abcd","abd"))
        self.assertTrue(cycpattern_check("hello","ell"))
        self.assertFalse(cycpattern_check("whassup","psus"))
        self.assertTrue(cycpattern_check("abab","baa"))
        self.assertFalse(cycpattern_check("efef","eeff"))
        self.assertTrue(cycpattern_check("himenss","simen"))

if __name__ == '__main__':
    unittest.main()

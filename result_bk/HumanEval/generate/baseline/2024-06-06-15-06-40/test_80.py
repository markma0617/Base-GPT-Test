from code_80 import is_happy

import unittest
from your_module import is_happy

class TestIsHappy(unittest.TestCase):
    def test_too_short_string(self):
        self.assertFalse(is_happy('a'))
        self.assertFalse(is_happy('aa'))
    
    def test_happy_string(self):
        self.assertTrue(is_happy('abcd'))
        self.assertTrue(is_happy('adb'))
    
    def test_unhappy_string(self):
        self.assertFalse(is_happy('aabb'))
        self.assertFalse(is_happy('xyy'))

if __name__ == '__main__':
    unittest.main()

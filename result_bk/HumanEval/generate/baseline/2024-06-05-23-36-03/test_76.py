from code_76 import is_simple_power

import unittest

def test_is_simple_power():
    class TestIsSimplePower(unittest.TestCase):
        def test_simple_power(self):
            self.assertTrue(is_simple_power(1, 4))
            self.assertTrue(is_simple_power(2, 2))
            self.assertTrue(is_simple_power(8, 2))
            self.assertFalse(is_simple_power(3, 2))
            self.assertFalse(is_simple_power(3, 1))
            self.assertFalse(is_simple_power(5, 3))

    return TestIsSimplePower('test_simple_power')

if __name__ == '__main__':
    unittest.main()

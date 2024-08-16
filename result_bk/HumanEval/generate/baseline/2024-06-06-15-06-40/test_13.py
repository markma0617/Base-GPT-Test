from code_13 import greatest_common_divisor
import unittest

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()
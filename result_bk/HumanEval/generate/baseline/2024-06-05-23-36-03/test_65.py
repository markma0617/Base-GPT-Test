from code_65 import circular_shift

import unittest
from your_module import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_circular_shift_positive_shift(self):
        self.assertEqual(circular_shift(12345, 2), "45123")

    def test_circular_shift_negative_shift(self):
        self.assertEqual(circular_shift(54321, -2), "21543")

    def test_circular_shift_shift_equal_to_length(self):
        self.assertEqual(circular_shift(12345, 5), "12345")

    def test_circular_shift_shift_greater_than_length(self):
        self.assertEqual(circular_shift(123, 4), "321")

if __name__ == '__main__':
    unittest.main()

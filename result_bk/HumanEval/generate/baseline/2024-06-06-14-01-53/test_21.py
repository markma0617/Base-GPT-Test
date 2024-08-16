from code_21 import rescale_to_unit

import unittest
from your_module import rescale_to_unit


class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_negative_numbers(self):
        numbers = [-5, -3, -1, 0, 2, 4]
        expected_result = [0.0, 0.2, 0.4, 0.5, 0.7, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_duplicate_numbers(self):
        numbers = [10, 10, 10, 10]
        expected_result = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

    def test_rescale_to_unit_two_numbers(self):
        numbers = [3, 7]
        expected_result = [0.0, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)


if __name__ == '__main__':
    unittest.main()

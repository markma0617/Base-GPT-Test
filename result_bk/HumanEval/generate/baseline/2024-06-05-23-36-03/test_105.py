from code_105 import by_length

import unittest
from your_module import by_length

class TestByLength(unittest.TestCase):

    def test_by_length_empty_array(self):
        arr = []
        self.assertEqual(by_length(arr), [])

    def test_by_length_normal_case(self):
        arr = [2, 1, 1, 4, 5, 8, 2, 3]
        expected_result = ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
        self.assertEqual(by_length(arr), expected_result)

    def test_by_length_strange_number(self):
        arr = [1, -1, 55]
        expected_result = ['One']
        self.assertEqual(by_length(arr), expected_result)

if __name__ == '__main__':
    unittest.main()

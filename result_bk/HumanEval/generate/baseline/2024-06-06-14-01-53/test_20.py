from code_20 import find_closest_elements

import unittest
from my_module import find_closest_elements

class TestFindClosestElements(unittest.TestCase):

    def test_find_closest_elements_basic(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
        self.assertEqual(find_closest_elements(numbers), (2.0, 2.2))

    def test_find_closest_elements_same(self):
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
        self.assertEqual(find_closest_elements(numbers), (2.0, 2.0))

    def test_find_closest_elements_negative(self):
        numbers = [-1.0, -2.0, -3.0, -4.0, -5.0, -2.2]
        self.assertEqual(find_closest_elements(numbers), (-2.0, -2.2))

    def test_find_closest_elements_large_numbers(self):
        numbers = [1000000.0, 2000000.0, 3000000.0, 4000000.0, 5000000.0, 2000000.1]
        self.assertEqual(find_closest_elements(numbers), (2000000.0, 2000000.1))

if __name__ == '__main__':
    unittest.main()

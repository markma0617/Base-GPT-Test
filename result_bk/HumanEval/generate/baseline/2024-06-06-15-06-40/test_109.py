from code_109 import move_one_ball

import unittest
from your_module import move_one_ball

class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(move_one_ball([]))

    def test_sorted_array(self):
        self.assertTrue(move_one_ball([1, 2, 3, 4, 5]))

    def test_possible_case(self):
        self.assertTrue(move_one_ball([3, 4, 5, 1, 2]))

    def test_impossible_case(self):
        self.assertFalse(move_one_ball([3, 5, 4, 1, 2]))

    def test_single_element(self):
        self.assertTrue(move_one_ball([7]))

    def test_two_elements_sorted(self):
        self.assertTrue(move_one_ball([2, 4]))

    def test_two_elements_not_sorted(self):
        self.assertFalse(move_one_ball([4, 2]))

if __name__ == '__main__':
    unittest.main()

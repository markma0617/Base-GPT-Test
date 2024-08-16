from code_102 import choose_num

import unittest
from your_module import choose_num

class TestChooseNum(unittest.TestCase):
    
    def test_choose_num_with_valid_range(self):
        self.assertEqual(choose_num(12, 15), 14)
    
    def test_choose_num_y_is_even(self):
        self.assertEqual(choose_num(10, 12), 12)
    
    def test_choose_num_x_greater_than_y(self):
        self.assertEqual(choose_num(13, 12), -1)
    
    def test_choose_num_x_equal_to_y(self):
        self.assertEqual(choose_num(8, 8), -1)

if __name__ == '__main__':
    unittest.main()

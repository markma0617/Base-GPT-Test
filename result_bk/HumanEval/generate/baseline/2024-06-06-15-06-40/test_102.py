from code_102 import choose_num

import unittest
from your_module import choose_num

class TestChooseNum(unittest.TestCase):
    
    def test_choose_num_with_valid_input(self):
        self.assertEqual(choose_num(12, 15), 14)
    
    def test_choose_num_with_y_even(self):
        self.assertEqual(choose_num(9, 10), 10)
    
    def test_choose_num_with_invalid_input(self):
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(5, 5), -1)

if __name__ == '__main__':
    unittest.main()

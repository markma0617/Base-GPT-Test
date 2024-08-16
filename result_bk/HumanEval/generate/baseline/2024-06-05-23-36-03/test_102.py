from code_102 import choose_num

import unittest
from your_module import choose_num

class TestChooseNum(unittest.TestCase):

    def test_choose_num_valid(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(7, 16), 16)
        self.assertEqual(choose_num(4, 4), -1)

    def test_choose_num_invalid(self):
        self.assertEqual(choose_num(13, 12), -1)
        self.assertEqual(choose_num(8, 9), -1)
        self.assertEqual(choose_num(10, 3), -1)

if __name__ == '__main__':
    unittest.main()

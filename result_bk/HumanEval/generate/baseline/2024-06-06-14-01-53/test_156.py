from code_156 import int_to_mini_roman

import unittest
from your_file_name import int_to_mini_roman

class TestIntToMiniRoman(unittest.TestCase):

    def test_int_to_mini_roman(self):
        self.assertEqual(int_to_mini_roman(19), 'xix')
        self.assertEqual(int_to_mini_roman(152), 'clii')
        self.assertEqual(int_to_mini_roman(426), 'cdxxvi')
        self.assertEqual(int_to_mini_roman(1000), 'm')

if __name__ == '__main__':
    unittest.main()

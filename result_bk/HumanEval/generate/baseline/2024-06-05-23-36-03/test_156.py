from code_156 import int_to_mini_roman

import unittest

def test():
    class TestIntToMiniRoman(unittest.TestCase):
        def test_1(self):
            self.assertEqual(int_to_mini_roman(19), 'xix')

        def test_2(self):
            self.assertEqual(int_to_mini_roman(152), 'clii')

        def test_3(self):
            self.assertEqual(int_to_mini_roman(426), 'cdxxvi')

    return TestIntToMiniRoman

if __name__ == '__main__':
    unittest.main()

from code_153 import Strongest_Extension

import unittest
from solution import Strongest_Extension

class TestStrongestExtension(unittest.TestCase):

    def test_example(self):
        self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

    def test_multiple_extensions(self):
        self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')

    def test_same_strength(self):
        self.assertEqual(Strongest_Extension('test_class', ['ABC', 'Xyz', 'DEF']), 'test_class.ABC')

if __name__ == '__main__':
    unittest.main()

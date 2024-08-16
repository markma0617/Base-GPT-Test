from code_153 import Strongest_Extension

import unittest

def test():
    class TestStrongestExtension(unittest.TestCase):

        def test_example_case(self):
            self.assertEqual(Strongest_Extension('my_class', ['AA', 'Be', 'CC']), 'my_class.AA')

        def test_custom_case(self):
            self.assertEqual(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']), 'Slices.SErviNGSliCes')

    return TestStrongestExtension

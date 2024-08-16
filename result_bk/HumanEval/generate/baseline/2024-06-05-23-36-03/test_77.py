from code_77 import iscube

import unittest

def test():
    
    class TestIsCube(unittest.TestCase):

        def test_positive_cube(self):
            self.assertTrue(iscube(1))
            self.assertTrue(iscube(64))

        def test_negative_cube(self):
            self.assertTrue(iscube(-1))

        def test_non_cube(self):
            self.assertFalse(iscube(2))
            self.assertFalse(iscube(180))

        def test_zero_cube(self):
            self.assertTrue(iscube(0))

    return TestIsCube

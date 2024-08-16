from code_69 import search

import unittest

def test():
    class TestSearch(unittest.TestCase):

        def test_example1(self):
            self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

        def test_example2(self):
            self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

        def test_example3(self):
            self.assertEqual(search([5, 5, 4, 4, 4]), -1)

    return TestSearch


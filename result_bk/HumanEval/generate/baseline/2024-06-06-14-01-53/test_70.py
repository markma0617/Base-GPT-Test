from code_70 import strange_sort_list

import unittest

def test_strange_sort_list(self):
    self.assertEqual(strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])
    self.assertEqual(strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])
    self.assertEqual(strange_sort_list([]), [])
    self.assertEqual(strange_sort_list([4, 3, 2, 1]), [1, 4, 2, 3])
    self.assertEqual(strange_sort_list([5, 2, 7, 3]), [2, 7, 3, 5])
    self.assertEqual(strange_sort_list([1]), [1])
    self.assertEqual(strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 9, 2, 8, 3, 7, 4, 6, 5])
    self.assertEqual(strange_sort_list([100, 2, 30, 1, 91]), [1, 100, 2, 91, 30])

TestGenerated = type('TestGenerated', (unittest.TestCase,), {'test_strange_sort_list': test_strange_sort_list})

def test():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerated)
    unittest.TextTestRunner().run(suite)

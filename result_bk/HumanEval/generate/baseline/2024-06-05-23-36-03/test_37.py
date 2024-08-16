from code_37 import sort_even

import unittest

def test():
    class TestSortEven(unittest.TestCase):
    
        def test_sort_even_example1(self):
            self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
    
        def test_sort_even_example2(self):
            self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortEven)
    unittest.TextTestRunner().run(suite)

return test

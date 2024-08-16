from code_73 import smallest_change

import unittest

def test():
    class TestSmallestChange(unittest.TestCase):

        def test_example_1(self):
            self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)

        def test_example_2(self):
            self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

        def test_example_3(self):
            self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestSmallestChange)
    unittest.TextTestRunner(verbosity=2).run(suite)

test()

from code_53 import add

import unittest

def test():
    class TestAddFunction(unittest.TestCase):
        def test_add_with_positive_numbers(self):
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(5, 7), 12)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestAddFunction)
    unittest.TextTestRunner().run(suite)

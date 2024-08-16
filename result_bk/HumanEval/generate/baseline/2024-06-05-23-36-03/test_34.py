from code_34 import unique

import unittest

def test():
    class TestUniqueFunction(unittest.TestCase):
        def test_unique(self):
            self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

    suite = unittest.TestLoader().loadTestsFromTestCase(TestUniqueFunction)
    unittest.TextTestRunner().run(suite)

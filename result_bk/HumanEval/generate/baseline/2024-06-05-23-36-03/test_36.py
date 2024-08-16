from code_36 import fizz_buzz

import unittest

def test():
    class TestFizzBuzz(unittest.TestCase):
        def test_fizz_buzz(self):
            self.assertEqual(fizz_buzz(50), 0)
            self.assertEqual(fizz_buzz(78), 2)
            self.assertEqual(fizz_buzz(79), 3)

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFizzBuzz)
    unittest.TextTestRunner().run(suite)

test()

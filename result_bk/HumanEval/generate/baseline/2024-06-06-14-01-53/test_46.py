from code_46 import fib4

import unittest
from your_module import fib4

class TestFib4(unittest.TestCase):

    def test_fib4(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(4), 2)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)

if __name__ == '__main__':
    unittest.main()

from code_83 import starts_one_ends

import unittest

def starts_one_ends(n):
    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))

class TestStartsOneEnds(unittest.TestCase):

    def test_start_one_end(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 18)
        self.assertEqual(starts_one_ends(3), 180)
        self.assertEqual(starts_one_ends(4), 1800)

if __name__ == '__main__':
    unittest.main()

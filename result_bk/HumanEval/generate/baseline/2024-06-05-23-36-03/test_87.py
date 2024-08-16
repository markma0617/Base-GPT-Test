from code_87 import get_row

import unittest

def test():
    class TestGetRow(unittest.TestCase):
        def test_1(self):
            self.assertEqual(get_row([
                [1,2,3,4,5,6],
                [1,2,3,4,1,6],
                [1,2,3,4,5,1]
            ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

        def test_2(self):
            self.assertEqual(get_row([], 1), [])

        def test_3(self):
            self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])

    return TestGetRow

from code_87 import get_row

import unittest

def get_row(lst, x):
    coords = [(i, j) for i in range(len(lst)) for j in range(len(lst[i])) if lst[i][j] == x]
    return sorted(sorted(coords, key=lambda x: x[1], reverse=True), key=lambda x: x[0])

class TestGetRow(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_row([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(get_row([[], [1], [1, 2, 3]], 3), [(2, 2)])

    def test_regular_case(self):
        self.assertEqual(get_row([
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ], 1), [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)])

if __name__ == '__main__':
    unittest.main()

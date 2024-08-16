from code_69 import search

import unittest

def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;
    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    return ans

class TestSearchFunction(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)

    def test_case2(self):
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)

    def test_case3(self):
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()

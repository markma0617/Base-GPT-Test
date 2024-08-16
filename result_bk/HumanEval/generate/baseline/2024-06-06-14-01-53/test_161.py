from code_161 import solve

import unittest

def solve(s):
    flg = 0
    idx = 0
    new_str = list(s)
    for i in s:
        if i.isalpha():
            new_str[idx] = i.swapcase()
            flg = 1
        idx += 1
    s = ""
    for i in new_str:
        s += i
    if flg == 0:
        return s[len(s)::-1]
    return s

class TestSolve(unittest.TestCase):

    def test_all_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_no_letters(self):
        self.assertEqual(solve("1234"), "4321")

    def test_mixed_string(self):
        self.assertEqual(solve("#a@C"), "#A@c")

if __name__ == '__main__':
    unittest.main()

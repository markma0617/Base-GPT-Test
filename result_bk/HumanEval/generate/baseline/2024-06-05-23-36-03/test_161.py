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

class TestSolveFunction(unittest.TestCase):

    def test_all_letters_uppercase(self):
        self.assertEqual(solve("HELLO"), "hello")

    def test_all_letters_lowercase(self):
        self.assertEqual(solve("hello"), "HELLO")

    def test_mixed_letters(self):
        self.assertEqual(solve("HeLLo"), "hEllO")

    def test_no_letters(self):
        self.assertEqual(solve("1234"), "4321")

    def test_only_special_characters(self):
        self.assertEqual(solve("#@$%"), "%$@#")

if __name__ == '__main__':
    unittest.main()

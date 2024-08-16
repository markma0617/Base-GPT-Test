from code_112 import reverse_delete

import unittest

def reverse_delete(s, c):
    s = ''.join([char for char in s if char not in c])
    return (s, s[::-1] == s)

class TestReverseDelete(unittest.TestCase):

    def test_1(self):
        self.assertEqual(reverse_delete("abcde", "ae"), ('bcd', False))

    def test_2(self):
        self.assertEqual(reverse_delete("abcdef", "b"), ('acdef', False))

    def test_3(self):
        self.assertEqual(reverse_delete("abcdedcba", "ab"), ('cdedc', True))

if __name__ == '__main__':
    unittest.main()

from code_132 import is_nested

import unittest

def is_nested(string):
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '[':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

class TestIsNested(unittest.TestCase):
    
    def test_case1(self):
        self.assertEqual(is_nested('[[]]'), True)
    
    def test_case2(self):
        self.assertEqual(is_nested('[]]]]]]][[[[[]'), False)
    
    def test_case3(self):
        self.assertEqual(is_nested('[][]'), False)
    
    def test_case4(self):
        self.assertEqual(is_nested('[]'), False)
    
    def test_case5(self):
        self.assertEqual(is_nested('[[][]]'), True)
    
    def test_case6(self):
        self.assertEqual(is_nested('[[]][['), True)

if __name__ == '__main__':
    unittest.main()

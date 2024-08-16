from code_132 import is_nested

import unittest

def test():
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

    return TestIsNested

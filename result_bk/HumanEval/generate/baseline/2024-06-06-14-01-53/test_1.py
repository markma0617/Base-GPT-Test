from code_1 import separate_paren_groups

import unittest
from separate_paren_groups import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):

    def test_separate_paren_groups(self):
        self.assertEqual(separate_paren_groups('( ) (( )) (( )( ))'), ['()', '(())', '(()())'])
        self.assertEqual(separate_paren_groups('()()()()'), ['()', '()', '()', '()'])
        self.assertEqual(separate_paren_groups('(())'), ['(())'])
        self.assertEqual(separate_paren_groups('()'), ['()'])
        self.assertEqual(separate_paren_groups('((()))'), ['((()))'])
        self.assertEqual(separate_paren_groups('()()'), ['()', '()'])
        self.assertEqual(separate_paren_groups('((()(())))'), ['((()(())))'])
        self.assertEqual(separate_paren_groups('()()()(()())()'), ['()', '()', '()', '()', '()'])
        self.assertEqual(separate_paren_groups('((()))(()(()))'), ['((()))', '(()(()))'])
        self.assertEqual(separate_paren_groups('(( ) (( )) (( )( )))'), ['( )', '(())', '(()())'])

if __name__ == '__main__':
    unittest.main()

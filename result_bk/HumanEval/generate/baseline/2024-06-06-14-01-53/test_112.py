from code_112 import reverse_delete

import unittest

def test():
    class TestReverseDelete(unittest.TestCase):
        
        def test_example1(self):
            result = reverse_delete("abcde", "ae")
            self.assertEqual(result, ('bcd', False))
        
        def test_example2(self):
            result = reverse_delete("abcdef", "b")
            self.assertEqual(result, ('acdef', False))
        
        def test_example3(self):
            result = reverse_delete("abcdedcba", "ab")
            self.assertEqual(result, ('cdedc', True))
    
    return TestReverseDelete

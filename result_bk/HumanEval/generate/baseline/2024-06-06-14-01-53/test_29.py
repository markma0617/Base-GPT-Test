from code_29 import filter_by_prefix

import unittest
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

class TestFilterByPrefix(unittest.TestCase):
    
    def test_empty_list(self):
        result = filter_by_prefix([], 'a')
        self.assertEqual(result, [])
    
    def test_prefix_a(self):
        input_list = ['abc', 'bcd', 'cde', 'array']
        result = filter_by_prefix(input_list, 'a')
        self.assertEqual(result, ['abc', 'array'])
    
    def test_prefix_b(self):
        input_list = ['abc', 'bcd', 'cde', 'array']
        result = filter_by_prefix(input_list, 'b')
        self.assertEqual(result, ['bcd'])
        
if __name__ == '__main__':
    unittest.main()

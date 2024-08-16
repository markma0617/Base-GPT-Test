from code_149 import sorted_list_sum

import unittest

def test():
    class TestSortedListSum(unittest.TestCase):
        
        def test_case1(self):
            self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        
        def test_case2(self):
            self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])
        
        def test_case3(self):
            self.assertEqual(sorted_list_sum(["hello", "world", "python"]), ["world", "python"])
    
    return TestSortedListSum

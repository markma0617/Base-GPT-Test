from code_149 import sorted_list_sum

import unittest
from your_file import sorted_list_sum

class TestSortedListSum(unittest.TestCase):

    def test_sorted_list_sum(self):
        self.assertEqual(sorted_list_sum(["aa", "a", "aaa"]), ["aa"])
        self.assertEqual(sorted_list_sum(["ab", "a", "aaa", "cd"]), ["ab", "cd"])
        self.assertEqual(sorted_list_sum(["hello", "world", "python"]), ["python"])
        self.assertEqual(sorted_list_sum(["aa", "bb", "cc", "dd"]), ["aa", "bb", "cc", "dd"])
        self.assertEqual(sorted_list_sum(["banana", "apple", "kiwi"]), ["apple", "kiwi"])

if __name__ == '__main__':
    unittest.main()

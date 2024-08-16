from code_74 import total_match

import unittest

def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2

class TestTotalMatch(unittest.TestCase):
    def test_empty_lists(self):
        self.assertEqual(total_match([], []), [])
    
    def test_case_sensitive_matching(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'Hi']), ['hI', 'Hi'])
    
    def test_total_char_count(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']), ['hi', 'admin'])
    
    def test_equal_char_count(self):
        self.assertEqual(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']), ['hI', 'hi', 'hi'])
    
    def test_single_char_lists(self):
        self.assertEqual(total_match(['4'], ['1', '2', '3', '4', '5']), ['4'])

if __name__ == '__main__':
    unittest.main()

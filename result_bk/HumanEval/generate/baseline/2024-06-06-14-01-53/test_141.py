from code_141 import file_name_check

import unittest

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'

class TestFileNameCheck(unittest.TestCase):

    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name_digit_count_exceeds(self):
        self.assertEqual(file_name_check("1234example.txt"), 'No')

    def test_invalid_file_name_empty_before_dot(self):
        self.assertEqual(file_name_check(".txt"), 'No')

    def test_invalid_file_name_no_dot(self):
        self.assertEqual(file_name_check("no_dot_txt"), 'No')

    def test_invalid_file_name_no_alphabetic_start(self):
        self.assertEqual(file_name_check("123example.exe"), 'No')

    def test_invalid_file_name_invalid_extension(self):
        self.assertEqual(file_name_check("example.pdf"), 'No')

if __name__ == '__main__':
    unittest.main()

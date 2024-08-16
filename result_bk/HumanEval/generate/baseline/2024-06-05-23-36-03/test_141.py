from code_141 import file_name_check

import unittest
from file_name_check import file_name_check

class TestFileNameCheck(unittest.TestCase):

    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name_start_with_digit(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_invalid_file_name_too_many_digits(self):
        self.assertEqual(file_name_check("file1234.txt"), 'No')

    def test_invalid_file_name_no_dot(self):
        self.assertEqual(file_name_check("filename"), 'No')

    def test_invalid_file_name_empty_prefix(self):
        self.assertEqual(file_name_check(".dll"), 'No')

    def test_invalid_file_name_invalid_suffix(self):
        self.assertEqual(file_name_check("example.py"), 'No')

if __name__ == '__main__':
    unittest.main()

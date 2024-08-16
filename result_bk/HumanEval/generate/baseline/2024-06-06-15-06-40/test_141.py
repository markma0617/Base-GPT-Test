from code_141 import file_name_check

import unittest
from file_name_validator import file_name_check

class TestFileNameCheck(unittest.TestCase):

    def test_valid_file_name(self):
        self.assertEqual(file_name_check("example.txt"), 'Yes')

    def test_invalid_file_name_starts_with_digit(self):
        self.assertEqual(file_name_check("1example.dll"), 'No')

    def test_invalid_file_name_too_many_digits(self):
        self.assertEqual(file_name_check("example1234.txt"), 'No')

    def test_invalid_file_name_missing_extension(self):
        self.assertEqual(file_name_check("example"), 'No')

from code_95 import check_dict_case

import unittest
from your_module import check_dict_case

class TestCheckDictCase(unittest.TestCase):

    def test_all_lower_case(self):
        self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

    def test_all_mixed_case(self):
        self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))

    def test_mixed_keys(self):
        self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))

    def test_mixed_upper_lower(self):
        self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

    def test_all_upper_case(self):
        self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

if __name__ == '__main__':
    unittest.main()

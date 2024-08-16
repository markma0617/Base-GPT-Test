from code_95 import check_dict_case

import unittest

def test():
    class TestCheckDictCase(unittest.TestCase):

        def test_empty_dict(self):
            self.assertFalse(check_dict_case({}))

        def test_all_lower_case(self):
            self.assertTrue(check_dict_case({"a": "apple", "b": "banana"}))

        def test_mixed_case(self):
            self.assertFalse(check_dict_case({"a": "apple", "A": "banana", "B": "banana"}))
            self.assertFalse(check_dict_case({"a": "apple", 8: "banana", "a": "apple"}))
            self.assertFalse(check_dict_case({"Name": "John", "Age": "36", "City": "Houston"}))

        def test_all_upper_case(self):
            self.assertTrue(check_dict_case({"STATE": "NC", "ZIP": "12345"}))

    return TestCheckDictCase

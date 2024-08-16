from code_134 import check_if_last_char_is_a_letter

import unittest

def test():
    class TestCheckIfLastCharIsALetter(unittest.TestCase):
        
        def test_1(self):
            self.assertEqual(check_if_last_char_is_a_letter("apple pie"), False)
        
        def test_2(self):
            self.assertEqual(check_if_last_char_is_a_letter("apple pi e"), True)
        
        def test_3(self):
            self.assertEqual(check_if_last_char_is_a_letter("apple pi e "), False)
        
        def test_4(self):
            self.assertEqual(check_if_last_char_is_a_letter(""), False)
    
    return TestCheckIfLastCharIsALetter

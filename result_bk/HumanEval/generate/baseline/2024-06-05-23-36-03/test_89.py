from code_89 import encrypt

import unittest

def test():
    class TestEncryptFunction(unittest.TestCase):
        
        def test_case_1(self):
            self.assertEqual(encrypt('hi'), 'lm')
        
        def test_case_2(self):
            self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        
        def test_case_3(self):
            self.assertEqual(encrypt('gf'), 'kj')
        
        def test_case_4(self):
            self.assertEqual(encrypt('et'), 'ix')

    return TestEncryptFunction

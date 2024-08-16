from code_27 import flip_case

import unittest

def test():
    class TestFlipCase(unittest.TestCase):
        def test_flip_case(self):
            self.assertEqual(flip_case('Hello'), 'hELLO')
            self.assertEqual(flip_case('WORLD'), 'world')
            self.assertEqual(flip_case('tEst'), 'TeST')
            self.assertEqual(flip_case('123'), '123')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlipCase)
    unittest.TextTestRunner().run(suite)

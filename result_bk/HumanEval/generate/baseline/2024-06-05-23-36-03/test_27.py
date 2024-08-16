from code_27 import flip_case

import unittest

def test():
    class TestFlipCase(unittest.TestCase):
        
        def test_flip_case(self):
            self.assertEqual(flip_case('Hello'), 'hELLO')
            self.assertEqual(flip_case('hELLO'), 'Hello')
            self.assertEqual(flip_case(''), '')
            
    unittest.main(argv=[''], exit=False)

test()

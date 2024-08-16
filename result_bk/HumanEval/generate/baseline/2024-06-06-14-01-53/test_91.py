from code_91 import is_bored

import unittest

def test():
    class TestIsBored(unittest.TestCase):
        def test_no_boredom(self):
            self.assertEqual(is_bored("Hello world"), 0)
            self.assertEqual(is_bored("The sky is blue. The sun is shining."), 0)
        
        def test_one_boredom(self):
            self.assertEqual(is_bored("I love this weather. The sun is shining."), 1)
            self.assertEqual(is_bored("The weather is great! I am happy."), 1)
    
    return TestIsBored

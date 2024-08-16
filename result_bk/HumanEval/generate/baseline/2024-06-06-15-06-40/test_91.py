from code_91 import is_bored

import unittest
from your_module import is_bored

class TestIsBored(unittest.TestCase):
    
    def test_no_boredom(self):
        self.assertEqual(is_bored("Hello world"), 0)
        self.assertEqual(is_bored("The sky is blue. The sun is shining. I love this weather"), 0)

    def test_single_boredom(self):
        self.assertEqual(is_bored("I am bored. How about you?"), 1)
        self.assertEqual(is_bored("I love Python. Do you?"), 1)

    def test_multiple_boredom(self):
        self.assertEqual(is_bored("I am bored. How about you? I think I am not."), 2)
        self.assertEqual(is_bored("I love Python. Do you? I really love it."), 2)

if __name__ == '__main__':
    unittest.main()

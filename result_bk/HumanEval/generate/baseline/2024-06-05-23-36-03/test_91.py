from code_91 import is_bored

import unittest
from solution import is_bored

class TestIsBored(unittest.TestCase):

    def test_no_boredom(self):
        result = is_bored("Hello world")
        self.assertEqual(result, 0)

    def test_one_boredom(self):
        result = is_bored("The sky is blue. The sun is shining. I love this weather")
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

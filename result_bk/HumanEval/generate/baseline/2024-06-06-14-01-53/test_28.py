from code_28 import concatenate

import unittest
from your_module import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_multiple_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

if __name__ == '__main__':
    unittest.main()

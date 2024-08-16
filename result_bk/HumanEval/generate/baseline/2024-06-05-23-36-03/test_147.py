from code_147 import get_max_triples

import unittest
from your_module import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_example(self):
        self.assertEqual(get_max_triples(5), 1)

    def test_zero_input(self):
        self.assertEqual(get_max_triples(0), 0)

    def test_large_input(self):
        self.assertEqual(get_max_triples(10), 4)

    def test_negative_input(self):
        self.assertEqual(get_max_triples(-5), 0)

if __name__ == '__main__':
    unittest.main()

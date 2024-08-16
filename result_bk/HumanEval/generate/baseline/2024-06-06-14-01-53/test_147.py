from code_147 import get_max_triples

import unittest
from solution import get_max_triples

class TestGetMaxTriples(unittest.TestCase):

    def test_get_max_triples_example1(self):
        self.assertEqual(get_max_triples(5), 1)

    def test_get_max_triples_example2(self):
        self.assertEqual(get_max_triples(3), 0)

    def test_get_max_triples_example3(self):
        self.assertEqual(get_max_triples(7), 3)

if __name__ == '__main__':
    unittest.main()

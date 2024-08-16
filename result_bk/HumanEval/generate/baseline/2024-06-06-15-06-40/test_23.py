from code_23 import strlen

import unittest

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_nonempty_string(self):
        self.assertEqual(strlen('abc'), 3)

if __name__ == '__main__':
    unittest.main()

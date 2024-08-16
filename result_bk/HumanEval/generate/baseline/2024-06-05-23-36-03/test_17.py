from code_17 import parse_music

import unittest
from test import parse_music

class TestParseMusic(unittest.TestCase):

    def test_parse_music(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

if __name__ == '__main__':
    unittest.main()

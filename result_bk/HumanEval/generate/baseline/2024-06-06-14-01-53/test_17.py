from code_17 import parse_music

import unittest
from your_module import parse_music

class TestParseMusic(unittest.TestCase):

    def test_parse_music_example(self):
        self.assertEqual(parse_music('o o| .| o| o| .| .| .| .| o o'), [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    def test_parse_music_empty_string(self):
        self.assertEqual(parse_music(''), [])

    def test_parse_music_invalid_notes(self):
        self.assertEqual(parse_music('o o| .| x x|'), [4, 2, 1]) 

if __name__ == '__main__':
    unittest.main()

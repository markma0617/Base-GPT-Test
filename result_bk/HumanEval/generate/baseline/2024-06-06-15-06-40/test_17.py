from code_17 import parse_music

import unittest
from your_module import parse_music


class TestParseMusic(unittest.TestCase):

    def test_parse_music(self):
        test_cases = [
            ('o o| .| o| o| .| .| .| .| o o', [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]),
            # Add more test cases here
        ]

        for music_string, expected_output in test_cases:
            with self.subTest(music_string=music_string, expected_output=expected_output):
                self.assertEqual(parse_music(music_string), expected_output)


if __name__ == '__main__':
    unittest.main()

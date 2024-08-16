from code_18 import how_many_times

import unittest
from your_file_name import how_many_times

class TestHowManyTimes(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(how_many_times('', 'a'), 0)
        
    def test_single_character(self):
        self.assertEqual(how_many_times('aaa', 'a'), 3)
        
    def test_multiple_characters(self):
        self.assertEqual(how_many_times('aaaa', 'aa'), 3)

if __name__ == '__main__':
    unittest.main()

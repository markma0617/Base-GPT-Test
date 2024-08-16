from code_113 import odd_count

import unittest
from your_script import odd_count

class TestOddCount(unittest.TestCase):

    def test_odd_count(self):
        self.assertEqual(odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])

    def test_odd_count_multiple(self):
        self.assertEqual(odd_count(['3',"11111111"]), ["the number of odd elements 1n the str1ng 1 of the 1nput.",
                                                       "the number of odd elements 8n the str8ng 8 of the 8nput."])

if __name__ == '__main__':
    unittest.main()

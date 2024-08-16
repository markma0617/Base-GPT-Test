from code_98 import count_upper

import unittest

def test_count_upper(self):
    self.assertEqual(count_upper('aBCdEf'), 1)
    self.assertEqual(count_upper('abcdefg'), 0)
    self.assertEqual(count_upper('dBBE'), 0)

if __name__ == '__main__':
    unittest.main()

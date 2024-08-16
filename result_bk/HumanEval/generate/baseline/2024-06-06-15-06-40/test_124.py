from code_124 import valid_date

import unittest
from your_module import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(valid_date('03-11-2000'))
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('04-0-2040'))
        self.assertTrue(valid_date('06-04-2020'))
        self.assertFalse(valid_date('06/04/2020'))

if __name__ == '__main__':
    unittest.main()

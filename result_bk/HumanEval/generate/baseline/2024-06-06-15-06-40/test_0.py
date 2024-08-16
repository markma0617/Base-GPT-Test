from code_0 import has_close_elements

import unittest
from your_module import has_close_elements

class TestHasCloseElements(unittest.TestCase):

    def test_no_close_elements(self):
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        self.assertFalse(has_close_elements(numbers, threshold))

    def test_has_close_elements(self):
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        threshold = 0.3
        self.assertTrue(has_close_elements(numbers, threshold))

if __name__ == '__main__':
    unittest.main()

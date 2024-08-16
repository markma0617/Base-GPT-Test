from code_21 import rescale_to_unit

import unittest
from my_module import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

if __name__ == '__main__':
    unittest.main()

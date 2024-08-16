from code_135 import can_arrange

import unittest

def test_can_arrange(self):
    self.assertEqual(can_arrange([1, 2, 4, 3, 5]), 3)
    self.assertEqual(can_arrange([1, 2, 3]), -1)
    self.assertEqual(can_arrange([4, 3, 2, 1]), 3)
    self.assertEqual(can_arrange([5, 4, 3, 2, 1]), 4)

class TestCanArrangeFunction(unittest.TestCase):
    test_can_arrange = test_can_arrange

if __name__ == '__main__':
    unittest.main()

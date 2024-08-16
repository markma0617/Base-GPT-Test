from code_72 import will_it_fly

import unittest

def test():
    class TestWillItFly(unittest.TestCase):

        def test_balanced_and_sum_less_than_max_weight(self):
            self.assertTrue(will_it_fly([3, 2, 3], 9))
            self.assertTrue(will_it_fly([3], 5))

        def test_balanced_but_sum_greater_than_max_weight(self):
            self.assertFalse(will_it_fly([3, 2, 3], 1))

        def test_unbalanced(self):
            self.assertFalse(will_it_fly([1, 2], 5))

    return TestWillItFly

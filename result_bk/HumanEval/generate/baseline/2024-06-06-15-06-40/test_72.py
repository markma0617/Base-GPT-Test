from code_72 import will_it_fly

import unittest

def test():
    class TestWillItFly(unittest.TestCase):
        def test_balanced_and_within_weight_limit(self):
            self.assertEqual(will_it_fly([3, 2, 3], 9), True)
            self.assertEqual(will_it_fly([3], 5), True)

        def test_unbalanced(self):
            self.assertEqual(will_it_fly([1, 2], 5), False)

        def test_balanced_but_exceeds_weight_limit(self):
            self.assertEqual(will_it_fly([3, 2, 3], 1), False)

    return TestWillItFly

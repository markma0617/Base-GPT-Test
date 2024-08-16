from code_67 import fruit_distribution

import unittest

def test():
    class TestFruitDistribution(unittest.TestCase):

        def test_case1(self):
            self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

        def test_case2(self):
            self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

        def test_case3(self):
            self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

        def test_case4(self):
            self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

    return TestFruitDistribution

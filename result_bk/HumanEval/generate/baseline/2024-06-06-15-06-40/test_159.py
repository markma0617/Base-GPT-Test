from code_159 import eat

import unittest

def test():
    class TestEat(unittest.TestCase):
        def test_enough_carrots(self):
            self.assertEqual(eat(5, 6, 10), [11, 4])
            self.assertEqual(eat(4, 8, 9), [12, 1])

        def test_not_enough_carrots(self):
            self.assertEqual(eat(1, 10, 10), [11, 0])
            self.assertEqual(eat(2, 11, 5), [7, 0])

        def test_edge_cases(self):
            self.assertEqual(eat(0, 0, 0), [0, 0])
            self.assertEqual(eat(1000, 1000, 1000), [2000, 0])

    suite = unittest.TestLoader().loadTestsFromTestCase(TestEat)
    unittest.TextTestRunner().run(suite)

from code_106 import f

import unittest

def test():
    class TestF(unittest.TestCase):
        def test_f(self):
            self.assertEqual(f(1), [1])
            self.assertEqual(f(2), [1, 2])
            self.assertEqual(f(3), [1, 2, 6])
            self.assertEqual(f(4), [1, 2, 6, 24])
            self.assertEqual(f(5), [1, 2, 6, 24, 15])
            self.assertEqual(f(6), [1, 2, 6, 24, 15, 720])
    
    return TestF

if __name__ == '__main__':
    unittest.main()

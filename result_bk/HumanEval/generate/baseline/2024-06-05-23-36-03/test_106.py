from code_106 import f

import unittest

def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret

class TestFunction(unittest.TestCase):
    
    def test_example(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])
    
    def test_n_equals_1(self):
        self.assertEqual(f(1), [1])
        
    def test_n_equals_2(self):
        self.assertEqual(f(2), [1, 3])
        
    def test_n_equals_3(self):
        self.assertEqual(f(3), [1, 3, 6])
        
    def test_n_equals_4(self):
        self.assertEqual(f(4), [1, 3, 6, 24])
        
    def test_n_equals_6(self):
        self.assertEqual(f(6), [1, 3, 6, 24, 10, 21])

if __name__ == '__main__':
    unittest.main()

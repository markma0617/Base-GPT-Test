from code_122 import add_elements

import unittest

def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)

class TestAddElements(unittest.TestCase):
    
    def test_example(self):
        arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
        k = 4
        self.assertEqual(add_elements(arr, k), 24)
    
    def test_all_elements_fit(self):
        arr = [10, 20, 30, 40, 50, 60]
        k = 6
        self.assertEqual(add_elements(arr, k), 210)
    
    def test_no_element_fits(self):
        arr = [111, 202, 303, 404]
        k = 4
        self.assertEqual(add_elements(arr, k), 0)
    
    def test_some_elements_fit(self):
        arr = [100, 101, 200, 201, 1000, 1001]
        k = 5
        self.assertEqual(add_elements(arr, k), 702)

if __name__ == '__main__':
    unittest.main()

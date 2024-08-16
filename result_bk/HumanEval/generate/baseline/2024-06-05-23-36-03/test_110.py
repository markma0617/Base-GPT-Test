from code_110 import exchange

import unittest

def exchange(lst1, lst2):
    odd = 0
    even = 0
    for i in lst1:
        if i % 2 == 1:
            odd += 1
    for i in lst2:
        if i % 2 == 0:
            even += 1
    if even >= odd:
        return "YES"
    return "NO"

class TestExchangeFunction(unittest.TestCase):

    def test_exchange_all_even(self):
        self.assertEqual(exchange([2, 4, 6, 8], [1, 3, 5, 7]), "YES")

    def test_exchange_single_odd(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_exchange_no_exchange_needed(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_exchange_more_even_elements_available(self):
        self.assertEqual(exchange([1, 2, 3, 4], [2, 4, 6, 8]), "YES")

    def test_exchange_odd_more_than_even(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

if __name__ == '__main__':
    unittest.main()

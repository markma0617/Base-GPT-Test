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

    def test_exchange_all_even_numbers(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 2, 3, 4]), "YES")

    def test_exchange_not_possible(self):
        self.assertEqual(exchange([1, 2, 3, 4], [1, 5, 3, 4]), "NO")

    def test_exchange_empty_lists(self):
        self.assertEqual(exchange([], []), "YES")

    def test_exchange_one_odd_number(self):
        self.assertEqual(exchange([1], [2]), "YES")

if __name__ == '__main__':
    unittest.main()

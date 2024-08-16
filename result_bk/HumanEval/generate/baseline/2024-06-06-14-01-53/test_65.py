from code_65 import circular_shift

import unittest

def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]

class TestCircularShift(unittest.TestCase):
    
    def test_circular_shift_1(self):
        self.assertEqual(circular_shift(12, 1), "21")
        
    def test_circular_shift_2(self):
        self.assertEqual(circular_shift(12, 2), "12")

if __name__ == '__main__':
    unittest.main()

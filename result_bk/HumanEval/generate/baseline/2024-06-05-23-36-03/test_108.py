from code_108 import count_nums

import unittest

def test_count_nums():
    test_cases = [
        ([], 0),
        ([-1, 11, -11], 1),
        ([1, 1, 2], 3)
    ]

    for arr, expected in test_cases:
        result = count_nums(arr)
        assert result == expected, f"Expected: {expected}, but got: {result}"

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)

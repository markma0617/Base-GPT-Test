from code_47 import median

import unittest

def test_median():
    test_cases = [
        ([3, 1, 2, 4, 5], 3),
        ([-10, 4, 6, 1000, 10, 20], 15.0)
    ]
    
    for input_list, expected_output in test_cases:
        result = median(input_list)
        assert result == expected_output, f"Expected: {expected_output}, but got: {result}"

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

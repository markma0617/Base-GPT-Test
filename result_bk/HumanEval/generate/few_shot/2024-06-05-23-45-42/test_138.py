from code_138 import is_equal_to_sum_even
def test():
    assert is_equal_to_sum_even(4) == False
    assert is_equal_to_sum_even(6) == False
    assert is_equal_to_sum_even(8) == True
    assert is_equal_to_sum_even(10) == True
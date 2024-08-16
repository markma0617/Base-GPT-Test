from code_13 import greatest_common_divisor

def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(10, 25) == 5
    assert greatest_common_divisor(12, 16) == 4
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(-3, 5) == 1
    assert greatest_common_divisor(7, -14) == 7
    assert greatest_common_divisor(-2, -8) == 2
    assert greatest_common_divisor(99, 100) == 1

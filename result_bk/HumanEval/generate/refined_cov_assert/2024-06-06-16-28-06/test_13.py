from code_13 import greatest_common_divisor
def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(14, 28) == 14
    assert greatest_common_divisor(72, 48) == 24
    assert greatest_common_divisor(17, 31) == 1
    assert greatest_common_divisor(100, 75) == 25
    assert greatest_common_divisor(0, 5) == 5
    assert greatest_common_divisor(0, 0) == 0
    assert greatest_common_divisor(50, 0) == 50
    assert greatest_common_divisor(13, 13) == 13
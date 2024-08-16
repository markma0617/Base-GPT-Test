from code_13 import greatest_common_divisor

def test():
    assert greatest_common_divisor(3, 5) == 1
    assert greatest_common_divisor(25, 15) == 5
    assert greatest_common_divisor(100, 75) == 25
    assert greatest_common_divisor(11, 22) == 11
    assert greatest_common_divisor(0, 5) == 5

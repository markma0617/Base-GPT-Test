from code_60 import sum_to_n

def test():
    assert sum_to_n(30) == 465
    assert sum_to_n(100) == 5050
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(1) == 1
    assert sum_to_n(20) == 210
    assert sum_to_n(7) == 28
    assert sum_to_n(99) == 4950
    assert sum_to_n(0) == 0
    assert sum_to_n(-5) == 0

from code_155 import even_odd_count

def test():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(7654321) == (3, 4)
    assert even_odd_count(-987654321) == (4, 5)
    assert even_odd_count(11111111) == (0, 8)
    assert even_odd_count(22222222) == (8, 0)
    assert even_odd_count(10101010) == (4, 4)
    assert even_odd_count(9999) == (0, 4)
    assert even_odd_count(0000) == (4, 0)

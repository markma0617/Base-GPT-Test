from code_155 import even_odd_count

def test():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(24680) == (5, 0)
    assert even_odd_count(13579) == (0, 5)
    assert even_odd_count(111222) == (3, 3)
    assert even_odd_count(-111222) == (3, 3)
    assert even_odd_count(123456789) == (4, 5)
    assert even_odd_count(987654321) == (5, 4)
    assert even_odd_count(-987654321) == (5, 4)

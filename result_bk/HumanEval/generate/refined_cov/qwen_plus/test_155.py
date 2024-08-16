from code_155 import even_odd_count

def test():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(7891) == (1, 3)
    assert even_odd_count(-9876) == (3, 1)

from code_155 import even_odd_count

def test():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(24680) == (5, 0)

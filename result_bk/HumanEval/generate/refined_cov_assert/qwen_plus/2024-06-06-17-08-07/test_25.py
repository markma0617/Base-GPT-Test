from code_25 import factorize

def test():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
    assert factorize(12) == [2, 2, 3]
    assert factorize(36) == [2, 2, 3, 3]
    assert factorize(91) == [7, 13]
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(15) == [3, 5]
    assert factorize(315) == [3, 3, 5, 7]
    assert factorize(1) == []

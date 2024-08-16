from code_25 import factorize

def test():
    assert factorize(8) == [2, 2, 2]
    assert factorize(25) == [5, 5]
    assert factorize(70) == [2, 5, 7]
    assert factorize(1) == []
    assert factorize(2) == [2]
    assert factorize(3) == [3]
    assert factorize(4) == [2, 2]
    assert factorize(12) == [2, 2, 3]
    assert factorize(100) == [2, 2, 5, 5]
    assert factorize(131) == [131]
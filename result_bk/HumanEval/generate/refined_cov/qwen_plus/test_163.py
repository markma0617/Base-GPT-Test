from code_163 import generate_integers

def test():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(5, 11) == [6, 8]
    assert generate_integers(1, 9) == [2, 4, 6, 8]

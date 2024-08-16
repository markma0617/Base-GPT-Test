from code_163 import generate_integers

def test():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 10) == [2, 4, 6, 8]
    assert generate_integers(15, 20) == [16, 18, 20]
    assert generate_integers(20, 15) == [20, 18, 16]
    assert generate_integers(4, 4) == [4]
    assert generate_integers(6, 6) == [6]
    assert generate_integers(9, 12) == []
    assert generate_integers(1, 9) == [2, 4, 6, 8]

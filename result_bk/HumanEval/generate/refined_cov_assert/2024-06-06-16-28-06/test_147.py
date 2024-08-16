from code_147 import get_max_triples

def test():
    assert get_max_triples(5) == 1
    assert get_max_triples(1) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(6) == 2
    assert get_max_triples(8) == 4
    assert get_max_triples(10) == 6
    assert get_max_triples(15) == 11
    assert get_max_triples(20) == 19
    assert get_max_triples(25) == 27
    assert get_max_triples(30) == 36

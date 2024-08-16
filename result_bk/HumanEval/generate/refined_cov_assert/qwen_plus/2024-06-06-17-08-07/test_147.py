from code_147 import get_max_triples

def test():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 2
    assert get_max_triples(7) == 2
    assert get_max_triples(8) == 3
    assert get_max_triples(9) == 5
    assert get_max_triples(10) == 6

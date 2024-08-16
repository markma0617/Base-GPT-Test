from code_147 import get_max_triples

def test():
    assert get_max_triples(5) == 1
    assert get_max_triples(10) == 10
    assert get_max_triples(1) == 0
    assert get_max_triples(8) == 12

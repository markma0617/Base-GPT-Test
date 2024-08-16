from code_147 import get_max_triples

def test():
    assert get_max_triples(5) == 1
    assert get_max_triples(3) == 0
    assert get_max_triples(6) == 2

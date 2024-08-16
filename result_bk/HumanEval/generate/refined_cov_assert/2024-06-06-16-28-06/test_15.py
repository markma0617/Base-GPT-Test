from code_15 import string_sequence

def test():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '0 1'
    assert string_sequence(2) == '0 1 2'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert string_sequence(20) == '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'
    assert string_sequence(50) == ' '.join(str(x) for x in range(51))
    assert string_sequence(100) == ' '.join(str(x) for x in range(101))
    assert string_sequence(500) == ' '.join(str(x) for x in range(501))
    assert string_sequence(1000) == ' '.join(str(x) for x in range(1001))

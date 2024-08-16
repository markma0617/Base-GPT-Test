from code_15 import string_sequence

def test():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'
    assert string_sequence(-1) == ''
    assert string_sequence(1) == '0'
    assert string_sequence(100) == '0 1 2 3 4 5 6 7 8 9 10 ... 97 98 99 100'
    assert string_sequence(0.5) == '0'
    assert string_sequence(10.5) == '0 1 2 3 4 5 6 7 8 9 10'
    assert string_sequence(1000) == '0 1 2 3 4 5 6 7 8 9 10 ... 997 998 999 1000'
    assert string_sequence(0.0) == '0'

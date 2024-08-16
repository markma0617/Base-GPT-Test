from code_111 import histogram

def test():   
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    assert histogram('a b b a') == {'a': 2, 'b': 2}
    assert histogram('a b c a b') == {'a': 2, 'b': 2}
    assert histogram('b b b b a') == {'b': 4}
    assert histogram('') == {}
    assert histogram('a b b a c c') == {'a': 2, 'b': 2, 'c': 2}
    assert histogram('a b a b a b a b') == {'a': 4, 'b': 4}
    assert histogram('a b c d e f g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}
    assert histogram('a a a b b c c c d d') == {'a': 3, 'b': 2, 'c': 3}
    assert histogram('apple banana cherry') == {'apple': 1, 'banana': 1, 'cherry': 1}

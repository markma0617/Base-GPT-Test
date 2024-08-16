from code_111 import histogram

def test():
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    assert histogram('a b b a') == {'a': 2, 'b': 2}
    assert histogram('a b c a b') == {'a': 2, 'b': 2}
    assert histogram('b b b b a') == {'b': 4}
    assert histogram('') == {}
    assert histogram('x y z') == {'x': 1, 'y': 1, 'z': 1}
    assert histogram('x x y y') == {'x': 2, 'y': 2}
    assert histogram('x y z x y') == {'x': 2, 'y': 2}
    assert histogram('y y y y x') == {'y': 4}
    assert histogram('x y z w') == {'x': 1, 'y': 1, 'z': 1, 'w': 1}

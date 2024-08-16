from code_89 import encrypt

def test():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('python') == 'rzbtynm'
    assert encrypt('special case') == 'xqggdwzcwv'

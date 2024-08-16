from code_112 import reverse_delete

def test():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("racecar", "ace") == ('rc', True)
    assert reverse_delete("hello", "lo") == ('he', False)
    assert reverse_delete("madam", "m") == ('ada', True)
    assert reverse_delete("abcdefg", "fgh") == ('abcde', False)
    assert reverse_delete("xyyx", "x") == ('yy', True)
    assert reverse_delete("aabbcc", "abc") == ('', True)
    assert reverse_delete("aAa", "a") == ('A', False)

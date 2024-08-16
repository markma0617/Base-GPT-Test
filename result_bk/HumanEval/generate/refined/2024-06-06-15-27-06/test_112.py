from code_112 import reverse_delete
def test():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
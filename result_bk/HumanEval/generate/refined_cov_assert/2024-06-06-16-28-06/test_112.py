from code_112 import reverse_delete

def test():
    assert reverse_delete("abcde", "ae") == ('bcd', False)
    assert reverse_delete("abcdef", "b") == ('acdef', False)
    assert reverse_delete("abcdedcba", "ab") == ('cdedc', True)
    assert reverse_delete("abracadabra", "rb") == ('acaadaaca', True)
    assert reverse_delete("hello", "el") == ('ho', True)
    assert reverse_delete("racecar", "rce") == ('aa', True)
    assert reverse_delete("python", "no") == ('pyth', False)
    assert reverse_delete("madam", "mad") == ('', True)
    assert reverse_delete("level", "evl") == ('', True)
    assert reverse_delete("programming", "pgr") == ('oamin', False)

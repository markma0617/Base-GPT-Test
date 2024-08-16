from code_18 import how_many_times

def test():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcabcabc', 'abc') == 3
    assert how_many_times('abababab', 'ab') == 4
    assert how_many_times('mississippi', 'issi') == 2
    assert how_many_times('aaaa', 'aaa') == 2
    assert how_many_times('aaaa', 'aaaa') == 1
    assert how_many_times('abcdabcdabcd', 'abcd') == 3
    assert how_many_times('abcdabcdabcd', 'ab') == 4

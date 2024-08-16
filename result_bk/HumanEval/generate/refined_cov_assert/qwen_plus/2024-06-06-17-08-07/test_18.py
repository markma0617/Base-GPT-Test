from code_18 import how_many_times

def test():
    assert how_many_times('', 'a') == 0
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('hello', 'll') == 1
    assert how_many_times('hello', 'world') == 0
    assert how_many_times('overlapping', 'lap') == 2
    assert how_many_times('testtest', 'test') == 2
    assert how_many_times('thisisatest', 'test') == 1
    assert how_many_times('thisisatest', 'notpresent') == 0
    assert how_many_times('abcabcabc', 'abc') == 3

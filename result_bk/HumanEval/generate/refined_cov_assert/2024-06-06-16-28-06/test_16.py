from code_16 import count_distinct_characters

def test():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abc') == 3
    assert count_distinct_characters('aabbcc') == 3
    assert count_distinct_characters('12345') == 5
    assert count_distinct_characters('aaAA11') == 3
    assert count_distinct_characters('') == 0
    assert count_distinct_characters('aAaAaAaA') == 2
    assert count_distinct_characters('aBbCcDdEe') == 5
    assert count_distinct_characters('!@#$%^&*') == 8

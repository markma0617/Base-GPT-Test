from code_16 import count_distinct_characters

def test():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('aAaA') == 1
    assert count_distinct_characters('AbCdefGh') == 7
    assert count_distinct_characters('') == 0
    assert count_distinct_characters('123456') == 6
    assert count_distinct_characters('helloWorld') == 7
    assert count_distinct_characters('thisisatest') == 7
    assert count_distinct_characters('aBcDeFgHiJkLmNoPqRsTuVwXyZ') == 26
    assert count_distinct_characters('aabbccddeeff') == 6

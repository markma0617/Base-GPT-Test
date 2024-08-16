from code_16 import count_distinct_characters
def test():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('HelloWorld') == 8
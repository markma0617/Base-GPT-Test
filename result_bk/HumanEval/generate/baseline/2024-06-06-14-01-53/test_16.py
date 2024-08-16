from code_16 import count_distinct_characters
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
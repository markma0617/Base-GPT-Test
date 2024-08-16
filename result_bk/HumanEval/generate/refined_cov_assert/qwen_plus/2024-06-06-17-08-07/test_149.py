from code_149 import sorted_list_sum

def test():
    assert sorted_list_sum([]) == []
    assert sorted_list_sum(["a"]) == []
    assert sorted_list_sum(["aa", "a"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa"]) == ["ab"]
    assert sorted_list_sum(["ab", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["cd", "ab"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "abcd", "ab", "abcde"]) == ["ab", "abc", "abcd"]
    assert sorted_list_sum(["xyz", "xy", "x", "y", "z"]) == ["xy", "xyz"]
    assert sorted_list_sum(["apple", "banana", "pear", "kiwi"]) == ["kiwi", "pear", "apple"]
    assert sorted_list_sum(["hello", "world", "short", "longest"]) == ["hello", "short", "world", "longest"]

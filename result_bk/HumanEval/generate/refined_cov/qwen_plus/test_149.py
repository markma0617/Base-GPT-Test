from code_149 import sorted_list_sum

def test():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["even", "length", "words", "are", "kept"]) == ["are", "even", "kept", "length", "words"]
    assert sorted_list_sum(["same", "length", "words", "come", "first"]) == ["come", "first", "length", "same", "words"]
    assert sorted_list_sum(["abc", "abcdef", "abcde"]) == ["abc", "abcde"]
